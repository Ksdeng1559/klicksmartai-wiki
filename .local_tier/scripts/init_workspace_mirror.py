#!/usr/bin/env python3
"""
init_workspace_mirror.py — Create one `.local_tier/clients/<slug>.duckdb`
per wiki client, with the workspace/deliverable/approval/sync schema
pre-staged. Empty by design; rows are populated by sync_supabase_to_duckdb.py
once Supabase (Tier 3) has data.

Schema mirrors the planned `client_workspaces` pattern documented at
~/.hermes/skills/productivity/supabase/references/client-workspaces-pattern.md
and the Frappe DocType plan at ~/wiki/processes/frappe-workspace-preliminary-plan.md.

Idempotent. Re-runnable. Safe to run for clients already initialised.

Usage:
    python3 init_workspace_mirror.py                       # all slugs in clients_index.duckdb
    python3 init_workspace_mirror.py --add gpc-development veritas-developments
    python3 init_workspace_mirror.py --list                # show what exists
"""

from __future__ import annotations
import argparse
import os
import sys
from pathlib import Path

import duckdb

REPO_ROOT = Path(os.path.expanduser("~/wiki")).resolve()
INDEX_DB = REPO_ROOT / ".local_tier" / "clients_index.duckdb"
CLIENTS_DIR = REPO_ROOT / ".local_tier" / "clients"


# Schema block — mirrors `client_workspaces` pattern + Frappe DocType fields.
# Keep in sync with the published references; sync scripts rely on these names.
SCHEMA = """
-- ── Workspace identity (1 row per client) ───────────────────────────────────
CREATE TABLE IF NOT EXISTS workspace (
    slug                       VARCHAR PRIMARY KEY,
    name                       VARCHAR NOT NULL,
    wiki_root                  VARCHAR NOT NULL,
    client_workspace_id        UUID,                       -- mirrors Supabase client_workspaces.id (nullable until Tier 3 wired)
    tier_3_supabase_project_id VARCHAR,
    canonical_workspace_path   VARCHAR,
    sync_state                 VARCHAR NOT NULL DEFAULT 'idle',   -- idle | syncing | error
    last_synced_at             TIMESTAMP,
    created_at                 TIMESTAMP NOT NULL DEFAULT now(),
    updated_at                 TIMESTAMP NOT NULL DEFAULT now()
);

-- ── Leads (mirrored from Supabase public.leads when wired) ──────────────────
CREATE TABLE IF NOT EXISTS leads (
    entity_id           VARCHAR PRIMARY KEY,
    domain              VARCHAR,
    business_name       VARCHAR,
    vertical            VARCHAR,
    quality_gate        VARCHAR NOT NULL DEFAULT 'PENDING',    -- PASS | FAIL | PENDING
    promoted_to_supabase BOOLEAN NOT NULL DEFAULT FALSE,
    client_workspace_id UUID,
    raw                 JSON,
    observed_at         TIMESTAMP,
    synced_at           TIMESTAMP NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS ix_leads_domain ON leads(domain);
CREATE INDEX IF NOT EXISTS ix_leads_quality ON leads(quality_gate);

-- ── Signals (append-only event log; never UPSERT in sync) ───────────────────
CREATE TABLE IF NOT EXISTS signals (
    signal_id       VARCHAR PRIMARY KEY,
    entity_id       VARCHAR NOT NULL,
    signal_type     VARCHAR NOT NULL,
    signal_category VARCHAR,
    observed_at     TIMESTAMP NOT NULL,
    source          VARCHAR,
    evidence        JSON,
    strength        DOUBLE,
    confidence      DOUBLE,
    synced_at       TIMESTAMP NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS ix_signals_entity ON signals(entity_id);
CREATE INDEX IF NOT EXISTS ix_signals_type ON signals(signal_type);

-- ── Opportunities (qualified opps derived from signals) ─────────────────────
CREATE TABLE IF NOT EXISTS opportunities (
    opportunity_id     VARCHAR PRIMARY KEY,
    entity_id          VARCHAR NOT NULL,
    stage              VARCHAR,
    status             VARCHAR,
    score              DOUBLE,
    confidence         DOUBLE,
    estimated_value    DOUBLE,
    next_action_at     TIMESTAMP,
    synced_at          TIMESTAMP NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS ix_opportunities_entity ON opportunities(entity_id);
CREATE INDEX IF NOT EXISTS ix_opportunities_stage ON opportunities(stage);

-- ── Deliverables (Frappe DocType: Deliverable, mirror of wiki files) ────────
CREATE TABLE IF NOT EXISTS deliverables (
    idempotency_key   VARCHAR PRIMARY KEY,                  -- slug:lane:relpath
    slug              VARCHAR NOT NULL,
    lane              VARCHAR NOT NULL,                     -- drafts | review | approved | delivered
    subcategory       VARCHAR,                              -- seo | outreach | deck | ...
    title             VARCHAR,
    source_file_path  VARCHAR NOT NULL,
    tier_3_supabase_id VARCHAR,
    kanban_task_id    VARCHAR,
    status            VARCHAR,                              -- auto-derived from lane
    frappe_synced_at  TIMESTAMP,
    created_at        TIMESTAMP NOT NULL DEFAULT now(),
    updated_at        TIMESTAMP NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS ix_deliverables_slug ON deliverables(slug);
CREATE INDEX IF NOT EXISTS ix_deliverables_lane ON deliverables(lane);

-- ── Approval Requests (Frappe DocType: Approval Request, replaces wiki VALIDATION_QUEUE.md) ──
CREATE TABLE IF NOT EXISTS approvals (
    idempotency_key   VARCHAR PRIMARY KEY,
    deliverable_key   VARCHAR,                              -- fk → deliverables.idempotency_key
    requested_by      VARCHAR,
    reviewer          VARCHAR,
    verdict           VARCHAR NOT NULL DEFAULT 'pending',   -- pending | approved | revise | killed
    rationale         TEXT,
    proposed_changes  TEXT,
    closed_at         TIMESTAMP,
    created_at        TIMESTAMP NOT NULL DEFAULT now(),
    updated_at        TIMESTAMP NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS ix_approvals_verdict ON approvals(verdict);

-- ── Audit (Tier 4 → Tier 3 boundary guard; every change logged) ─────────────
CREATE SEQUENCE IF NOT EXISTS audit_log_seq START 1;
CREATE TABLE IF NOT EXISTS audit_log (
    id            BIGINT PRIMARY KEY DEFAULT nextval('audit_log_seq'),
    slug          VARCHAR,
    source        VARCHAR NOT NULL,                         -- 'wiki' | 'supabase' | 'frappe' | 'agent'
    action        VARCHAR NOT NULL,
    payload       JSON,
    ts            TIMESTAMP NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS ix_audit_slug ON audit_log(slug);
"""


def list_initialised() -> list[str]:
    if not CLIENTS_DIR.exists():
        return []
    return sorted(p.stem for p in CLIENTS_DIR.glob("*.duckdb"))


def list_from_index() -> list[str]:
    if not INDEX_DB.exists():
        return []
    con = duckdb.connect(str(INDEX_DB), read_only=True)
    try:
        rows = con.execute("SELECT slug FROM workspaces ORDER BY slug").fetchall()
        return [r[0] for r in rows]
    finally:
        con.close()


def init_one(slug: str) -> dict:
    db_path = CLIENTS_DIR / f"{slug}.duckdb"
    existed = db_path.exists()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    con = duckdb.connect(str(db_path))
    try:
        con.execute(SCHEMA)
        # mark workspace sync_state
        con.execute("""
            INSERT INTO workspace (slug, name, wiki_root, sync_state)
            VALUES (?, ?, ?, 'idle')
            ON CONFLICT (slug) DO UPDATE SET updated_at = now()
        """, [slug, slug, str(REPO_ROOT / "clients" / slug)])
        # audit
        con.execute("""
            INSERT INTO audit_log (slug, source, action, payload)
            VALUES (?, 'agent', 'init_workspace_mirror', ?)
        """, [slug, f'{{"existed": {str(existed).lower()}}}'])
    finally:
        con.close()
    # chmod 600
    try:
        os.chmod(db_path, 0o600)
    except OSError:
        pass
    return {"slug": slug, "path": str(db_path), "existed": existed}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--add", nargs="+", default=None,
                   help="Restrict to these slugs (default: all slugs from clients_index.duckdb)")
    p.add_argument("--list", action="store_true", help="List initialised slugs and exit")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    if args.list:
        initd = list_initialised()
        indexed = list_from_index()
        print(f"initialised ({len(initd)}): {initd}")
        print(f"in clients_index ({len(indexed)}): {indexed}")
        missing_from_index = sorted(set(initd) - set(indexed))
        missing_from_init = sorted(set(indexed) - set(initd))
        if missing_from_index:
            print(f"in .duckdb but NOT in clients_index: {missing_from_index}")
        if missing_from_init:
            print(f"in clients_index but NOT initialised: {missing_from_init}")
        return 0

    if args.add:
        slugs = args.add
    else:
        slugs = list_from_index()
        if not slugs:
            print("clients_index.duckdb is empty. Run init_clients_index.py first.", file=sys.stderr)
            return 1

    CLIENTS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"clients dir: {CLIENTS_DIR}")
    print(f"slugs: {len(slugs)}")

    results = []
    for slug in slugs:
        info = init_one(slug)
        results.append(info)
        marker = "↻" if info["existed"] else "+"
        print(f"  {marker} {slug:32s} → {info['path']}")

    print(f"\nDone. {len(results)} per-client mirrors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

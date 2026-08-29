#!/usr/bin/env python3
"""
sync_workspace_to_supabase_and_duckdb.py — TWO-PHASE build.

PHASE A: insert (or UPSERT) a `public.workspaces` row in Supabase for each
         wiki client, populated from the wiki CLAUDE.md / IDENTITY.md.

PHASE B: mirror the 5 workspace-scoped CRM tables from Supabase into
         `.local_tier/clients/<slug>.duckdb`.

This is the "duplicate the client workspace into the supabase table" flow.
Both phases are idempotent: re-running updates the row on slug collision and
UPSERTs the mirror rows on natural keys.

Tables in scope (workspace-scoped, confirmed via information_schema 2026-08-29):
    public.workspaces    → workspace_meta
    public.contacts      → contact
    public.organizations → organization
    public.tasks         → task
    public.touchpoints   → touchpoint

Out of scope (no clean workspace attribution in this project):
    leads, opportunities, companies, partners, notes
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Any

WIKI_ROOT = Path.home() / "wiki"
LOCAL_TIER = WIKI_ROOT / ".local_tier"
CLIENTS_DIR = LOCAL_TIER / "clients"
AUDIT_SEQ = "audit_log_seq"

# Supabase project — read from env, never echo in chat.
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_SECRET_KEY") or os.environ.get("SUPABASE_PUBLISHABLE_KEY")
SUPABASE_PROJECT_ID = "amgknqnhiscryvcfeoyj"

# workspace_meta columns — exact copy of public.workspaces (verified 2026-08-29)
WORKSPACE_META_DDL = """
CREATE TABLE IF NOT EXISTS workspace_meta (
    id                 UUID,
    name               VARCHAR NOT NULL,
    slug               VARCHAR NOT NULL PRIMARY KEY,
    plan               VARCHAR NOT NULL,
    vertical           VARCHAR NOT NULL,
    settings           JSON,
    onboarding_status  TEXT NOT NULL,
    vertical_pack      TEXT,
    created_at         TIMESTAMP WITH TIME ZONE,
    updated_at         TIMESTAMP WITH TIME ZONE
);
"""

CONTACT_DDL = """
CREATE TABLE IF NOT EXISTS contact (
    id                    UUID PRIMARY KEY,
    workspace_id          UUID NOT NULL,
    full_name             TEXT NOT NULL,
    normalized_name       TEXT,
    email                 TEXT,
    phone                 TEXT,
    role_title            TEXT,
    contact_type          TEXT,
    status                TEXT,
    metadata              JSON,
    source_intake_id      UUID,
    created_at            TIMESTAMP WITH TIME ZONE,
    updated_at            TIMESTAMP WITH TIME ZONE,
    gtm_tier              INTEGER,
    icp_fit               TEXT,
    relationship_status   TEXT,
    new_offer_fit         TEXT,
    scored_at             TIMESTAMP WITH TIME ZONE,
    first_name            TEXT,
    last_name             TEXT,
    organization_name     TEXT,
    relationship_health   TEXT,
    tier                  TEXT,
    last_contacted_at     TIMESTAMP WITH TIME ZONE,
    city                  TEXT,
    employment_type       TEXT,
    lead_score            INTEGER,
    source                TEXT,
    partner_id            UUID,
    pipa_consent          BOOLEAN NOT NULL,
    pipa_consent_at       TIMESTAMP WITH TIME ZONE,
    company_id            UUID
);
"""

ORGANIZATION_DDL = """
CREATE TABLE IF NOT EXISTS organization (
    id                    UUID PRIMARY KEY,
    workspace_id          UUID NOT NULL,
    name                  TEXT NOT NULL,
    normalized_name       TEXT,
    organization_type     TEXT,
    website               TEXT,
    industry              TEXT,
    location              TEXT,
    metadata              JSON,
    source_intake_id      UUID,
    created_at            TIMESTAMP WITH TIME ZONE,
    updated_at            TIMESTAMP WITH TIME ZONE
);
"""

TASK_DDL = """
CREATE TABLE IF NOT EXISTS task (
    id                    UUID PRIMARY KEY,
    workspace_id          UUID NOT NULL,
    title                 TEXT NOT NULL,
    description           TEXT,
    status                TEXT,
    priority              TEXT,
    due_at                TIMESTAMP WITH TIME ZONE,
    assigned_to           TEXT,
    related_entity_type   TEXT,
    related_entity_id     UUID,
    source_episode_id     UUID,
    source_intake_id      UUID,
    metadata              JSON,
    created_at            TIMESTAMP WITH TIME ZONE,
    updated_at            TIMESTAMP WITH TIME ZONE
);
"""

TOUCHPOINT_DDL = """
CREATE TABLE IF NOT EXISTS touchpoint (
    id                    UUID PRIMARY KEY,
    workspace_id          UUID NOT NULL,
    touchpoint_type       TEXT NOT NULL,
    contact_id            UUID,
    organization_id       UUID,
    episode_id            UUID,
    direction             TEXT,
    summary               TEXT,
    occurred_at           TIMESTAMP WITH TIME ZONE,
    metadata              JSON,
    updated_at            TIMESTAMP WITH TIME ZONE,
    created_at            TIMESTAMP WITH TIME ZONE
);
"""

SYNC_STATE_DDL = """
CREATE SEQUENCE IF NOT EXISTS sync_state_seq START 1;
CREATE TABLE IF NOT EXISTS sync_state (
    id              INTEGER PRIMARY KEY DEFAULT nextval('sync_state_seq'),
    slug            VARCHAR NOT NULL UNIQUE,
    last_sync_at    TIMESTAMP WITH TIME ZONE NOT NULL,
    rows_mirrored   JSON NOT NULL,
    source          VARCHAR NOT NULL DEFAULT 'supabase',
    notes           TEXT
);
"""

AUDIT_DDL = f"""
CREATE SEQUENCE IF NOT EXISTS {AUDIT_SEQ} START 1;
CREATE TABLE IF NOT EXISTS audit_log (
    id            BIGINT PRIMARY KEY DEFAULT nextval('{AUDIT_SEQ}'),
    slug          VARCHAR,
    source        VARCHAR NOT NULL,
    script        VARCHAR NOT NULL,
    action        VARCHAR NOT NULL,
    details       TEXT,
    created_at    TIMESTAMP WITH TIME ZONE DEFAULT now()
);
"""

SYNC_TABLES = [
    ("contact", "contacts", CONTACT_DDL),
    ("organization", "organizations", ORGANIZATION_DDL),
    ("task", "tasks", TASK_DDL),
    ("touchpoint", "touchpoints", TOUCHPOINT_DDL),
]

# Default values used when populating public.workspaces from a wiki client.
# Mirrors the shape of the existing demo-capital / dev-workspace rows.
DEFAULT_PLAN = "lite"
DEFAULT_VERTICAL = "rios_general"
# Allowed by CHECK constraint: pending | in_progress | complete | legacy_skip.
# New wiki clients use 'pending' — real workspaces that haven't run onboarding.
DEFAULT_ONBOARDING_STATUS = "pending"


def load_supabase_client() -> Any:
    """Return a supabase.Client or raise. Reads creds from ~/.hermes/.env."""
    try:
        from supabase import create_client  # type: ignore
    except ImportError as exc:
        raise RuntimeError("supabase-py not installed; pip install supabase") from exc
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise RuntimeError(
            "SUPABASE_URL / SUPABASE_SECRET_KEY not in env. "
            "Set in ~/.hermes/.env (chmod 600)."
        )
    return create_client(SUPABASE_URL, SUPABASE_KEY)


def read_wiki_client(slug: str) -> dict:
    """Extract a minimal workspace row from the wiki client's IDENTITY.md / CLAUDE.md.

    Strategy: pull the first H1 ('#' header) and the table cell at '| Client |'.
    That's enough to populate `name` and `slug` — the CRM columns `plan`,
    `vertical`, `settings`, `onboarding_status` get safe defaults.
    """
    base = WIKI_ROOT / "clients" / slug
    if not base.exists():
        raise FileNotFoundError(f"Wiki client folder missing: {base}")
    name = None
    for fname in ("IDENTITY.md", "CLAUDE.md", "README.md"):
        path = base / fname
        if not path.exists():
            continue
        in_frontmatter = False
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            stripped = line.strip()
            # YAML frontmatter: lines between --- ... --- at top of file.
            if stripped == "---":
                in_frontmatter = not in_frontmatter
                continue
            if in_frontmatter:
                # Only capture root-level `title:` keys (no leading whitespace).
                # Nested YAML items under `- id:` etc. have indented keys.
                if not line[:len(line) - len(line.lstrip())].startswith(" ") and stripped.startswith("title:"):
                    name = stripped[len("title:"):].strip().strip("'\"")
                    # Strip trailing descriptors like "— Workspace Identity"
                    # by dropping common suffixes, not splitting on the first sep.
                    for suffix in (" — Workspace Identity", " — Workspace", " - Workspace Identity"):
                        if name.endswith(suffix):
                            name = name[: -len(suffix)].strip()
                            break
                continue
            # Markdown H1.
            if stripped.startswith("# ") and len(stripped) > 2:
                name = stripped[2:].strip()
                # If the first token is a filename (e.g. "IDENTITY.md"),
                # drop it — the real title comes after it.
                parts = name.split(maxsplit=1)
                if parts and (parts[0].endswith(".md") or parts[0] in ("CLAUDE.md", "README.md", "IDENTITY.md")):
                    if len(parts) > 1:
                        name = parts[1].strip()
                        # Strip leading "— " or "—" if the title started with the
                        # separator on its own (e.g. "IDENTITY.md — GPC Dev...").
                        if name.startswith("— "):
                            name = name[2:].strip()
                        elif name.startswith("—"):
                            name = name[1:].strip()
                    else:
                        name = parts[0]
                # Drop trailing descriptors like "— Workspace Identity".
                for suffix in (" — Workspace Identity", " — Workspace", " - Workspace Identity"):
                    if name.endswith(suffix):
                        name = name[: -len(suffix)].strip()
                        break
                break
        if name:
            break
    if not name:
        name = slug.replace("-", " ").title()
    return {
        "slug": slug,
        "name": name,
        "plan": DEFAULT_PLAN,
        "vertical": DEFAULT_VERTICAL,
        "settings": {},
        "onboarding_status": DEFAULT_ONBOARDING_STATUS,
        "vertical_pack": None,
    }


def upsert_workspace(sb: Any, ws: dict) -> dict:
    """UPSERT a public.workspaces row on slug. Returns the resolved row."""
    # Try insert first; on slug conflict, update the existing row.
    payload = dict(ws)
    payload["settings"] = {}  # jsonb
    res = sb.table("workspaces").upsert(payload, on_conflict="slug").execute()
    if not res.data:
        raise RuntimeError(f"upsert returned no rows for slug={ws['slug']}")
    row = res.data[0]
    print(f"  ✓ workspaces.upsert(slug={ws['slug']}) → id={row['id']}")
    return row


def ensure_schema(con) -> None:
    """Idempotent DDL for all mirror tables."""
    con.execute(WORKSPACE_META_DDL)
    con.execute(CONTACT_DDL)
    con.execute(ORGANIZATION_DDL)
    con.execute(TASK_DDL)
    con.execute(TOUCHPOINT_DDL)
    con.execute(SYNC_STATE_DDL)
    con.execute(AUDIT_DDL)


def mirror_one_table(sb: Any, con, workspace_id: str, duck_table: str, supa_table: str, slug: str) -> int:
    """Fetch all rows in supa_table scoped to workspace_id, UPSERT into duck_table."""
    res = (
        sb.table(supa_table)
        .select("*")
        .eq("workspace_id", workspace_id)
        .execute()
    )
    rows = res.data or []
    if not rows:
        return 0
    # UPSERT by primary key 'id'. DuckDB uses ON CONFLICT semantics via
    # DELETE + INSERT for full row replacement (safer than partial UPDATE
    # given the CRM column count is non-trivial).
    placeholders = ",".join(["?"] * len(rows[0]))
    col_list = list(rows[0].keys())
    col_list_sql = ",".join(f'"{c}"' for c in col_list)
    con.execute(f"DELETE FROM {duck_table} WHERE workspace_id = ?", [workspace_id])
    for row in rows:
        vals = [row.get(c) for c in col_list]
        con.execute(
            f"INSERT INTO {duck_table} ({col_list_sql}) VALUES ({placeholders})",
            vals,
        )
    con.execute(
        f"INSERT INTO audit_log (slug, source, script, action, details) VALUES (?, ?, ?, ?, ?)",
        [slug, "supabase", "sync_workspace_to_supabase_and_duckdb.py", "mirror", f"{supa_table}:{len(rows)} rows"],
    )
    return len(rows)


def mirror_workspace_meta(con, sb_row: dict, slug: str) -> None:
    """Mirror the workspace_meta row from Supabase public.workspaces."""
    con.execute("DELETE FROM workspace_meta WHERE slug = ?", [slug])
    cols = list(sb_row.keys())
    placeholders = ",".join(["?"] * len(cols))
    col_list_sql = ",".join(f'"{c}"' for c in cols)
    con.execute(
        f"INSERT INTO workspace_meta ({col_list_sql}) VALUES ({placeholders})",
        [sb_row.get(c) for c in cols],
    )
    con.execute(
        "INSERT INTO audit_log (slug, source, script, action, details) VALUES (?, ?, ?, ?, ?)",
        [slug, "supabase", "sync_workspace_to_supabase_and_duckdb.py", "mirror", "workspaces:1 row"],
    )


def process_slug(sb: Any, slug: str, dry_run: bool = False) -> dict:
    print(f"\n=== {slug} ===")
    ws = read_wiki_client(slug)
    print(f"  wiki identity: name='{ws['name']}', slug='{ws['slug']}'")
    if dry_run:
        print("  (dry run — skipping supabase upsert + mirror)")
        return {"slug": slug, "skipped": True, "reason": "dry-run"}

    # PHASE A — upsert into Supabase
    sb_row = upsert_workspace(sb, ws)
    workspace_id = sb_row["id"]

    # PHASE B — open per-client DuckDB and mirror
    db_path = CLIENTS_DIR / f"{slug}.duckdb"
    db_path.parent.mkdir(parents=True, exist_ok=True)
    # If a stale/empty file sits at the path, drop it so DuckDB can create
    # a fresh DB. Valid DuckDB files are >= 1024 bytes; any smaller is junk.
    if db_path.exists() and db_path.stat().st_size < 1024:
        db_path.unlink()
    import duckdb
    con = duckdb.connect(str(db_path))
    # Lock down perms now that DuckDB has the file open.
    try:
        db_path.chmod(0o600)
    except OSError:
        pass
    try:
        ensure_schema(con)
        mirror_workspace_meta(con, sb_row, slug)

        rows_mirrored = {"workspace_meta": 1}
        for duck_table, supa_table, _ddl in SYNC_TABLES:
            n = mirror_one_table(sb, con, workspace_id, duck_table, supa_table, slug)
            rows_mirrored[supa_table] = n

        # record sync_state
        import json
        import datetime as dt
        con.execute(
            "INSERT INTO sync_state (slug, last_sync_at, rows_mirrored, source, notes) VALUES (?, ?, ?, ?, ?) "
            "ON CONFLICT (slug) DO UPDATE SET last_sync_at = EXCLUDED.last_sync_at, rows_mirrored = EXCLUDED.rows_mirrored",
            [slug, dt.datetime.now(dt.timezone.utc).isoformat(), json.dumps(rows_mirrored), "supabase", "two-phase build"],
        )
        con.execute(
            "INSERT INTO audit_log (slug, source, script, action, details) VALUES (?, ?, ?, ?, ?)",
            [slug, "sync_workspace_to_supabase_and_duckdb.py", "sync_workspace_to_supabase_and_duckdb.py", "complete", json.dumps(rows_mirrored)],
        )
        print(f"  ✓ mirror complete: {rows_mirrored}")
        return {"slug": slug, "ok": True, "rows": rows_mirrored, "db": str(db_path), "workspace_id": workspace_id}
    finally:
        con.close()


def main() -> int:
    parser = argparse.ArgumentParser(description="Two-phase build: supabase insert + duckdb mirror")
    parser.add_argument("slugs", nargs="+", help="wiki client slugs to mirror")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print(f"Supabase project: {SUPABASE_PROJECT_ID}")
    print(f"Wiki root: {WIKI_ROOT}")
    print(f"Local tier: {LOCAL_TIER}")
    print(f"Slugs: {', '.join(args.slugs)}")

    sb = None if args.dry_run else load_supabase_client()
    results = [process_slug(sb, s, dry_run=args.dry_run) for s in args.slugs]

    ok = sum(1 for r in results if r.get("ok"))
    print(f"\n=== summary ===")
    print(f"processed: {len(results)} / succeeded: {ok}")
    for r in results:
        if r.get("ok"):
            print(f"  {r['slug']:30s}  workspace_id={r['workspace_id']}")
        elif r.get("skipped"):
            print(f"  {r['slug']:30s}  skipped ({r.get('reason')})")
        else:
            print(f"  {r['slug']:30s}  FAIL")
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

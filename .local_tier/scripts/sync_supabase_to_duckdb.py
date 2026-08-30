#!/usr/bin/env python3
"""
sync_supabase_to_duckdb.py — Tier 3 (Supabase) → Tier 2 (DuckDB mirror) sync.

Mirrors Supabase rows scoped per `client_workspace_id` into the matching
`.local_tier/clients/<slug>.duckdb`. Boundary rules per
`processes/lead-sniperai-cli-os.md`:

- Tier 2 → Tier 3 is PASS-graded sync only. Failed entities stay local.
- Tier 3 is read-only for downstream consumers.
- Tier 4 (Frappe) reads from this mirror, never writes back.

Idempotent: re-running on the same source rows is a no-op (PKs are
content-hashed dedup keys).

Tables mirrored (matches the schema in `init_workspace_mirror.py`):

  public.leads            →  leads          (PK = entity_id)
  public.lead_signals     →  signals        (PK = signal_id)
  public.lead_opportunities → opportunities (PK = opportunity_id)

The `client_workspaces` table is the filter: rows with
`client_workspace_id IS NULL` are skipped (not yet attributed).

Usage:
    python3 sync_supabase_to_duckdb.py                     # all workspaces
    python3 sync_supabase_to_duckdb.py --slug spectra-holdings
    python3 sync_supabase_to_duckdb.py --dry-run           # show counts, no writes
    python3 sync_supabase_to_duckdb.py --verbose           # per-row logging
"""

from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any

import duckdb

REPO_ROOT = Path(os.path.expanduser("~/wiki")).resolve()
INDEX_DB = REPO_ROOT / ".local_tier" / "clients_index.duckdb"
CLIENTS_DIR = REPO_ROOT / ".local_tier" / "clients"
SUPABASE_PROJECT_ID = "amgknqnhiscryvcfeoyj"  # Klicksmartai-RIOS

try:
    import supabase as _supabase_pkg  # type: ignore
    create_client = _supabase_pkg.create_client
    HAS_SUPABASE = True
except ImportError:
    create_client = None  # type: ignore
    HAS_SUPABASE = False


def get_supabase_client():
    """Read creds from ~/.hermes/.env (600-chmod). Returns supabase.Client or None."""
    if not HAS_SUPABASE:
        return None
    env_path = Path(os.path.expanduser("~/.hermes/.env"))
    if not env_path.exists():
        return None
    env = {}
    for line in env_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    url = env.get("SUPABASE_URL")
    key = env.get("SUPABASE_SECRET_KEY") or env.get("SUPABASE_SERVICE_ROLE_KEY")
    if not url or not key or create_client is None:
        return None
    return create_client(url, key)


def load_workspaces() -> list[dict]:
    """Load workspaces + their (possibly-null) client_workspace_id from clients_index.duckdb.

    The index doesn't actually carry the supabase uuid yet — that's a future field
    on the workspace row. For now, we resolve client_workspace_id from Supabase's
    client_workspaces table by slug (the slug column is the natural key on both sides).
    """
    if not INDEX_DB.exists():
        return []
    con = duckdb.connect(str(INDEX_DB), read_only=True)
    try:
        rows = con.execute("""
            SELECT slug, name, has_identity, has_claude,
                   n_drafts, n_projects, n_deliverables
            FROM workspaces ORDER BY slug
        """).fetchall()
    finally:
        con.close()
    return [
        {
            "slug": r[0], "name": r[1],
            "has_identity": bool(r[2]), "has_claude": bool(r[3]),
            "n_drafts": r[4], "n_projects": r[5], "n_deliverables": r[6],
            "client_workspace_id": None,  # populated below from Supabase
        }
        for r in rows
    ]


def resolve_workspace_uuids(sb, workspaces: list[dict]) -> tuple[dict[str, str], str]:
    """Returns ({slug: uuid}, table_used).

    Tries `client_workspaces` first (the planned pattern in the supabase skill
    references), falls back to `workspaces` (the actual table in this Supabase
    project per Klicksmartai-RIOS schema). Both tables are expected to have an
    `id` (uuid) and a `slug` (text) column.

    If neither table exists, returns an empty map and the error table name so
    callers can report cleanly.
    """
    out: dict[str, str] = {}
    table_used = ""
    for candidate in ("client_workspaces", "workspaces"):
        try:
            resp = sb.table(candidate).select("id,slug").execute()
        except Exception as e:
            err = str(e)
            if "PGRST205" in err or "Could not find the table" in err:
                continue  # try next candidate
            print(f"  WARN: could not read {candidate}: {e}", file=sys.stderr)
            continue
        rows = resp.data or []
        if not rows:
            # table exists but is empty — fall through to next candidate too
            continue
        for row in rows:
            slug = row.get("slug")
            wid = row.get("id")
            if slug and wid:
                out[slug] = wid
        if out:
            table_used = candidate
            return out, table_used
    # neither table had rows; report the first one we tried
    return out, "client_workspaces" if not out else table_used


def fetch_rows(sb, table: str, workspace_id: str, limit: int = 5000) -> list[dict]:
    """Fetch rows from a Supabase table filtered by client_workspace_id."""
    try:
        resp = (sb.table(table)
                  .select("*")
                  .eq("client_workspace_id", workspace_id)
                  .limit(limit)
                  .execute())
    except Exception as e:
        print(f"  WARN: read {table} failed: {e}", file=sys.stderr)
        return []
    return resp.data or []


def upsert_leads(db_con, rows: list[dict], verbose: bool = False) -> int:
    """Upsert into Tier 2 leads table. Returns count written."""
    n = 0
    for r in rows:
        if not r.get("entity_id"):
            continue
        db_con.execute("""
            INSERT INTO leads (entity_id, domain, business_name, vertical,
                               quality_gate, promoted_to_supabase,
                               client_workspace_id, raw, observed_at, synced_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, now())
            ON CONFLICT (entity_id) DO UPDATE SET
                domain              = EXCLUDED.domain,
                business_name       = EXCLUDED.business_name,
                vertical            = EXCLUDED.vertical,
                quality_gate        = EXCLUDED.quality_gate,
                promoted_to_supabase= EXCLUDED.promoted_to_supabase,
                client_workspace_id = EXCLUDED.client_workspace_id,
                raw                 = EXCLUDED.raw,
                observed_at         = EXCLUDED.observed_at,
                synced_at           = now()
        """, [
            r["entity_id"], r.get("domain"), r.get("business_name"), r.get("vertical"),
            r.get("quality_gate", "PENDING"), bool(r.get("promoted_to_supabase", False)),
            r.get("client_workspace_id"), json.dumps(r) if r else None,
            r.get("observed_at"),
        ])
        n += 1
        if verbose:
            print(f"      lead {r['entity_id'][:12]}…  {r.get('business_name')}")
    return n


def upsert_signals(db_con, rows: list[dict], verbose: bool = False) -> int:
    """Append (insert-only) signals — signals are an append-only log."""
    n = 0
    for r in rows:
        # signal_id is required; skip if missing
        sid = r.get("signal_id") or r.get("id")
        if not sid:
            continue
        # use ON CONFLICT DO NOTHING to keep the append-only invariant safe on re-runs
        db_con.execute("""
            INSERT INTO signals (signal_id, entity_id, signal_type, signal_category,
                                 observed_at, source, evidence, strength, confidence, synced_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, now())
            ON CONFLICT (signal_id) DO NOTHING
        """, [
            sid, r.get("entity_id"), r.get("signal_type"), r.get("signal_category"),
            r.get("observed_at"), r.get("source"),
            json.dumps(r.get("evidence")) if r.get("evidence") is not None else None,
            r.get("strength"), r.get("confidence"),
        ])
        n += 1
        if verbose:
            print(f"      signal {sid[:12]}…  {r.get('signal_type')}/{r.get('signal_category')}")
    return n


def upsert_opportunities(db_con, rows: list[dict], verbose: bool = False) -> int:
    n = 0
    for r in rows:
        oid = r.get("opportunity_id") or r.get("id")
        if not oid:
            continue
        db_con.execute("""
            INSERT INTO opportunities (opportunity_id, entity_id, stage, status,
                                       score, confidence, estimated_value,
                                       next_action_at, synced_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, now())
            ON CONFLICT (opportunity_id) DO UPDATE SET
                stage           = EXCLUDED.stage,
                status          = EXCLUDED.status,
                score           = EXCLUDED.score,
                confidence      = EXCLUDED.confidence,
                estimated_value = EXCLUDED.estimated_value,
                next_action_at  = EXCLUDED.next_action_at,
                synced_at       = now()
        """, [
            oid, r.get("entity_id"), r.get("stage"), r.get("status"),
            r.get("score"), r.get("confidence"), r.get("estimated_value"),
            r.get("next_action_at"),
        ])
        n += 1
        if verbose:
            print(f"      opportunity {oid[:12]}…  {r.get('stage')}")
    return n


def sync_workspace(slug: str, sb, dry_run: bool, verbose: bool) -> dict:
    """Sync one workspace. Returns a result dict for the report."""
    db_path = CLIENTS_DIR / f"{slug}.duckdb"
    if not db_path.exists():
        return {"slug": slug, "skipped": True, "reason": "no per-client mirror yet"}

    # resolve this workspace's uuid from Supabase
    uuid_map, _table_used = resolve_workspace_uuids(sb, load_workspaces())
    workspace_id = uuid_map.get(slug)
    if not workspace_id:
        return {"slug": slug, "skipped": True, "reason": "no workspace row in Supabase for this slug"}

    # fetch rows
    leads = fetch_rows(sb, "leads", workspace_id)
    signals = fetch_rows(sb, "lead_signals", workspace_id)
    opps = fetch_rows(sb, "lead_opportunities", workspace_id)

    if dry_run:
        return {"slug": slug, "dry_run": True, "leads": len(leads),
                "signals": len(signals), "opportunities": len(opps)}

    # open mirror and write
    con = duckdb.connect(str(db_path))
    try:
        # update workspace row with the supabase uuid if missing
        con.execute("""
            UPDATE workspace SET client_workspace_id = ?, sync_state = 'syncing', updated_at = now()
            WHERE slug = ? AND client_workspace_id IS NULL
        """, [workspace_id, slug])

        n_leads = upsert_leads(con, leads, verbose=verbose)
        n_signals = upsert_signals(con, signals, verbose=verbose)
        n_opps = upsert_opportunities(con, opps, verbose=verbose)

        con.execute("""
            UPDATE workspace SET sync_state = 'idle', last_synced_at = now(), updated_at = now()
            WHERE slug = ?
        """, [slug])

        # audit row
        con.execute("""
            INSERT INTO audit_log (slug, source, action, payload)
            VALUES (?, 'supabase', 'sync', ?)
        """, [slug, json.dumps({
            "leads": n_leads, "signals": n_signals, "opportunities": n_opps,
            "workspace_id": workspace_id,
        })])
    finally:
        con.close()

    return {"slug": slug, "skipped": False,
            "leads": n_leads, "signals": n_signals, "opportunities": n_opps,
            "workspace_id": workspace_id}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--slug", default=None, help="Sync one workspace only")
    p.add_argument("--dry-run", action="store_true", help="Show counts, no writes")
    p.add_argument("--verbose", action="store_true", help="Per-row logging")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    sb = get_supabase_client()
    if sb is None:
        print("ERROR: supabase-py not installed or SUPABASE_URL/SUPABASE_SECRET_KEY missing.", file=sys.stderr)
        print("       pip install supabase", file=sys.stderr)
        print("       check ~/.hermes/.env has SUPABASE_URL + SUPABASE_SECRET_KEY", file=sys.stderr)
        return 2

    if args.slug:
        workspaces = [{"slug": args.slug, "name": args.slug}]
    else:
        workspaces = load_workspaces()
        if not workspaces:
            print("No workspaces in clients_index.duckdb. Run init_clients_index.py first.", file=sys.stderr)
            return 1

    # resolve all workspace uuids in one call
    uuid_map, table_used = resolve_workspace_uuids(sb, workspaces)
    print(f"Supabase project: {SUPABASE_PROJECT_ID}")
    print(f"Workspaces in index: {len(workspaces)}")
    if uuid_map:
        print(f"Workspaces in Supabase {table_used}: {len(uuid_map)}")
    else:
        print(f"NOTE: no rows in client_workspaces OR workspaces tables in Supabase.")
        print("      This is expected — Tier 3 schema has the tables but they're empty.")
        print("      All workspaces will sync zero rows until workspace rows are inserted.")
    if args.dry_run:
        print("(dry run — no writes)\n")

    print()
    print(f"{'workspace':32s}  {'leads':>6s}  {'signals':>8s}  {'opps':>5s}  status")
    print("-" * 70)

    total = {"leads": 0, "signals": 0, "opportunities": 0}
    for ws in workspaces:
        slug = ws["slug"]
        if slug not in uuid_map:
            print(f"{slug:32s}  {0:>6d}  {0:>8d}  {0:>5d}  SKIP (no client_workspaces row)")
            continue

        info = sync_workspace(slug, sb, dry_run=args.dry_run, verbose=args.verbose)
        if info.get("skipped"):
            print(f"{slug:32s}  {0:>6d}  {0:>8d}  {0:>5d}  SKIP ({info.get('reason')})")
            continue
        if info.get("dry_run"):
            print(f"{slug:32s}  {info['leads']:>6d}  {info['signals']:>8d}  {info['opportunities']:>5d}  DRY-RUN")
            continue
        print(f"{slug:32s}  {info['leads']:>6d}  {info['signals']:>8d}  {info['opportunities']:>5d}  OK")
        total["leads"] += info["leads"]
        total["signals"] += info["signals"]
        total["opportunities"] += info["opportunities"]

    print()
    print(f"Total: {total['leads']} leads, {total['signals']} signals, {total['opportunities']} opportunities")
    return 0


if __name__ == "__main__":
    sys.exit(main())

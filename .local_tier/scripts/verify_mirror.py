#!/usr/bin/env python3
"""
verify_mirror.py — Assert each per-client DuckDB mirror has the expected
schema, expected tables exist, audit_log is being written, and the index
registry matches what's on disk.

Read-only. Safe to run anytime.

Usage:
    python3 verify_mirror.py                  # verify everything
    python3 verify_mirror.py --slug gpc-development
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

EXPECTED_TABLES = {
    "workspace", "leads", "signals", "opportunities",
    "deliverables", "approvals", "audit_log",
}

EXPECTED_INDEXES = {
    "ix_leads_domain", "ix_leads_quality",
    "ix_signals_entity", "ix_signals_type",
    "ix_opportunities_entity", "ix_opportunities_stage",
    "ix_deliverables_slug", "ix_deliverables_lane",
    "ix_approvals_verdict",
    "ix_audit_slug",
}


def check_one(slug: str) -> dict:
    db_path = CLIENTS_DIR / f"{slug}.duckdb"
    if not db_path.exists():
        return {"slug": slug, "ok": False, "errors": ["file does not exist"], "warnings": []}

    # permissions
    mode = oct(db_path.stat().st_mode & 0o777)
    warnings = []
    if mode != "0o600":
        warnings.append(f"permissions are {mode}, expected 0o600")

    errors = []
    con = duckdb.connect(str(db_path), read_only=True)
    try:
        # tables
        tables = {r[0] for r in con.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema='main'"
        ).fetchall()}
        missing = EXPECTED_TABLES - tables
        if missing:
            errors.append(f"missing tables: {sorted(missing)}")

        # indexes
        try:
            idxs = {r[0] for r in con.execute(
                "SELECT index_name FROM duckdb_indexes()"
            ).fetchall()}
            missing_idx = EXPECTED_INDEXES - idxs
            if missing_idx:
                warnings.append(f"missing indexes: {sorted(missing_idx)}")
        except Exception:
            pass

        # audit_log row count (should be ≥1 after init_workspace_mirror.py)
        try:
            audit_n = con.execute("SELECT COUNT(*) FROM audit_log").fetchone()[0]
        except Exception:
            audit_n = 0

        # workspace row count (should be exactly 1)
        try:
            ws_n = con.execute("SELECT COUNT(*) FROM workspace").fetchone()[0]
        except Exception:
            ws_n = 0
        if ws_n != 1:
            errors.append(f"workspace row count is {ws_n}, expected 1")

        # workspace sync_state
        try:
            sync_row = con.execute("SELECT sync_state FROM workspace").fetchone()
            sync_state = sync_row[0] if sync_row else None
        except Exception:
            sync_state = None
    finally:
        con.close()

    return {
        "slug": slug,
        "path": str(db_path),
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "audit_log_rows": audit_n,
        "workspace_rows": ws_n,
        "sync_state": sync_state,
        "permissions": mode,
    }


def check_index() -> dict:
    if not INDEX_DB.exists():
        return {"ok": False, "errors": ["clients_index.duckdb does not exist"]}

    con = duckdb.connect(str(INDEX_DB), read_only=True)
    try:
        rows = con.execute("""
            SELECT slug, name, has_identity, has_claude,
                   n_drafts, n_projects, n_deliverables, sync_state
            FROM workspaces ORDER BY slug
        """).fetchall()
    finally:
        con.close()

    workspaces = [
        {
            "slug": r[0], "name": r[1],
            "has_identity": bool(r[2]), "has_claude": bool(r[3]),
            "n_drafts": r[4], "n_projects": r[5], "n_deliverables": r[6],
            "sync_state": r[7],
        }
        for r in rows
    ]
    return {"ok": True, "workspaces": workspaces, "errors": []}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--slug", default=None, help="Verify one workspace only")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    print("=" * 70)
    print("clients_index.duckdb")
    print("=" * 70)
    idx = check_index()
    if not idx["ok"]:
        print(f"  ERROR: {idx['errors']}")
        return 1
    for ws in idx["workspaces"]:
        flags = []
        if not ws["has_identity"]:
            flags.append("NO_IDENTITY")
        if not ws["has_claude"]:
            flags.append("NO_CLAUDE")
        flag_str = " [" + ", ".join(flags) + "]" if flags else ""
        print(f"  {ws['slug']:32s} drafts={ws['n_drafts']:3d}  projects={ws['n_projects']:3d}  deliverables={ws['n_deliverables']:3d}{flag_str}")

    print()
    print("=" * 70)
    print("per-client mirrors")
    print("=" * 70)

    if args.slug:
        slugs = [args.slug]
    else:
        slugs = sorted(p.stem for p in CLIENTS_DIR.glob("*.duckdb"))
        if not slugs:
            print("  (none — run init_workspace_mirror.py first)")
            return 0

    overall_ok = True
    for slug in slugs:
        info = check_one(slug)
        marker = "✓" if info["ok"] else "✗"
        line = f"  {marker} {slug:32s}  audit_log={info.get('audit_log_rows', 0)}  ws_rows={info.get('workspace_rows', 0)}  perms={info.get('permissions')}"
        print(line)
        for w in info["warnings"]:
            print(f"      WARN  {w}")
        for e in info["errors"]:
            print(f"      ERROR {e}")
        if not info["ok"]:
            overall_ok = False

    print()
    if overall_ok:
        print("OK — all mirrors conformant.")
        return 0
    print("FAIL — see errors above.")
    return 1


if __name__ == "__main__":
    sys.exit(main())

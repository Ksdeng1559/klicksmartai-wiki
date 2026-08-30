#!/usr/bin/env python3
"""
init_clients_index.py — Populate `.local_tier/clients_index.duckdb` from
`~/wiki/clients/<slug>/CLAUDE.md` + `IDENTITY.md`.

Idempotent. Re-runnable. UPSERT on slug.

Usage:
    python3 init_clients_index.py              # all clients with CLAUDE.md
    python3 init_clients_index.py --add gpc-development veritas-developments
"""

from __future__ import annotations
import argparse
import datetime as dt
import os
import re
import sys
from pathlib import Path

import duckdb

REPO_ROOT = Path(os.path.expanduser("~/wiki")).resolve()
CLIENTS_DIR = REPO_ROOT / "clients"
INDEX_DB = REPO_ROOT / ".local_tier" / "clients_index.duckdb"


SCHEMA = """
CREATE TABLE IF NOT EXISTS workspaces (
    slug              VARCHAR PRIMARY KEY,
    name              VARCHAR NOT NULL,
    client_root       VARCHAR NOT NULL,
    has_identity      BOOLEAN NOT NULL DEFAULT FALSE,
    has_claude        BOOLEAN NOT NULL DEFAULT FALSE,
    identity_excerpt  TEXT,
    claude_excerpt    TEXT,
    n_drafts          INTEGER NOT NULL DEFAULT 0,
    n_projects        INTEGER NOT NULL DEFAULT 0,
    n_deliverables    INTEGER NOT NULL DEFAULT 0,
    last_synced_at    TIMESTAMP NOT NULL DEFAULT now(),
    sync_state        VARCHAR NOT NULL DEFAULT 'idle'
);

CREATE TABLE IF NOT EXISTS workspace_files (
    slug          VARCHAR NOT NULL,
    relpath       VARCHAR NOT NULL,
    abspath       VARCHAR NOT NULL,
    file_kind     VARCHAR NOT NULL,    -- 'identity' | 'claude' | 'draft' | 'project' | 'deliverable' | 'config' | 'other'
    bytes         BIGINT,
    mtime         TIMESTAMP,
    PRIMARY KEY (slug, relpath)
);

CREATE SEQUENCE IF NOT EXISTS sync_log_seq START 1;
CREATE TABLE IF NOT EXISTS sync_log (
    id            BIGINT PRIMARY KEY DEFAULT nextval('sync_log_seq'),
    slug          VARCHAR,
    script        VARCHAR NOT NULL,
    action        VARCHAR NOT NULL,
    details       TEXT,
    ts            TIMESTAMP NOT NULL DEFAULT now()
);
"""


def excerpt(text: str, max_chars: int = 600) -> str:
    text = text.strip()
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rsplit(" ", 1)[0] + "..."


def first_heading(text: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+?)$", text, re.MULTILINE)
    return m.group(1).strip() if m else fallback


def count_md(subdir: Path) -> int:
    if not subdir.exists():
        return 0
    return sum(1 for _ in subdir.rglob("*.md"))


def discover_files(slug_dir: Path) -> list[dict]:
    out = []
    for p in slug_dir.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(slug_dir).as_posix()
        if rel.startswith("."):
            continue
        if rel.endswith((".duckdb", ".duckdb.wal", ".db-wal", ".db-shm", ".png", ".jpg", ".jpeg", ".gif", ".pdf")):
            continue
        kind = "other"
        low = rel.lower()
        if low == "identity.md":
            kind = "identity"
        elif low == "claude.md":
            kind = "claude"
        elif low.startswith("_config/"):
            kind = "config"
        elif low.startswith("drafts/"):
            kind = "draft"
        elif low.startswith("projects/"):
            kind = "project"
        elif low.startswith("deliverables/"):
            kind = "deliverable"
        try:
            stat = p.stat()
        except OSError:
            continue
        out.append({
            "relpath": rel,
            "abspath": str(p),
            "file_kind": kind,
            "bytes": stat.st_size,
            "mtime": dt.datetime.fromtimestamp(stat.st_mtime, tz=dt.timezone.utc),
        })
    return out


def upsert_workspace(con, slug: str, slug_dir: Path) -> dict:
    identity_path = slug_dir / "IDENTITY.md"
    claude_path = slug_dir / "CLAUDE.md"

    identity_text = identity_path.read_text(encoding="utf-8", errors="replace") if identity_path.exists() else ""
    claude_text = claude_path.read_text(encoding="utf-8", errors="replace") if claude_path.exists() else ""

    # derive name: from CLAUDE.md heading, fallback to title-case of slug
    name = first_heading(claude_text, slug.replace("-", " ").title())

    files = discover_files(slug_dir)
    n_drafts = sum(1 for f in files if f["file_kind"] == "draft")
    n_projects = sum(1 for f in files if f["file_kind"] == "project")
    n_deliverables = sum(1 for f in files if f["file_kind"] == "deliverable")

    row = {
        "slug": slug,
        "name": name,
        "client_root": str(slug_dir),
        "has_identity": identity_path.exists(),
        "has_claude": claude_path.exists(),
        "identity_excerpt": excerpt(identity_text) if identity_text else None,
        "claude_excerpt": excerpt(claude_text) if claude_text else None,
        "n_drafts": n_drafts,
        "n_projects": n_projects,
        "n_deliverables": n_deliverables,
    }

    con.execute("""
        INSERT INTO workspaces (slug, name, client_root, has_identity, has_claude,
                                identity_excerpt, claude_excerpt,
                                n_drafts, n_projects, n_deliverables, last_synced_at, sync_state)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, now(), 'idle')
        ON CONFLICT (slug) DO UPDATE SET
            name              = EXCLUDED.name,
            client_root       = EXCLUDED.client_root,
            has_identity      = EXCLUDED.has_identity,
            has_claude        = EXCLUDED.has_claude,
            identity_excerpt  = EXCLUDED.identity_excerpt,
            claude_excerpt    = EXCLUDED.claude_excerpt,
            n_drafts          = EXCLUDED.n_drafts,
            n_projects        = EXCLUDED.n_projects,
            n_deliverables    = EXCLUDED.n_deliverables,
            last_synced_at    = now(),
            sync_state        = 'idle'
    """, [row["slug"], row["name"], row["client_root"], row["has_identity"], row["has_claude"],
          row["identity_excerpt"], row["claude_excerpt"],
          row["n_drafts"], row["n_projects"], row["n_deliverables"]])

    # files: replace for this slug (cheap; small N)
    con.execute("DELETE FROM workspace_files WHERE slug = ?", [slug])
    for f in files:
        con.execute("""
            INSERT INTO workspace_files (slug, relpath, abspath, file_kind, bytes, mtime)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT (slug, relpath) DO UPDATE SET
                abspath   = EXCLUDED.abspath,
                file_kind = EXCLUDED.file_kind,
                bytes     = EXCLUDED.bytes,
                mtime     = EXCLUDED.mtime
        """, [slug, f["relpath"], f["abspath"], f["file_kind"], f["bytes"], f["mtime"]])

    con.execute(
        "INSERT INTO sync_log (slug, script, action, details) VALUES (?, ?, ?, ?)",
        [slug, "init_clients_index", "upsert", f"files={len(files)} drafts={n_drafts} projects={n_projects} deliverables={n_deliverables}"]
    )

    return {"slug": slug, "files": len(files), "drafts": n_drafts, "projects": n_projects, "deliverables": n_deliverables}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--add", nargs="+", default=None,
                   help="Restrict to these slugs (default: all clients with CLAUDE.md)")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    if not CLIENTS_DIR.exists():
        print(f"ERROR: clients dir not found: {CLIENTS_DIR}", file=sys.stderr)
        return 2

    INDEX_DB.parent.mkdir(parents=True, exist_ok=True)
    con = duckdb.connect(str(INDEX_DB))
    try:
        con.execute(SCHEMA)
    except Exception as e:
        print(f"ERROR applying schema: {e}", file=sys.stderr)
        return 3

    # pick clients
    if args.add:
        slugs = args.add
    else:
        slugs = sorted(
            d.name for d in CLIENTS_DIR.iterdir()
            if d.is_dir() and not d.name.startswith("_") and (d / "CLAUDE.md").exists()
        )

    if not slugs:
        print("No clients with CLAUDE.md found.", file=sys.stderr)
        return 1

    print(f"clients_index.db: {INDEX_DB}")
    print(f"clients: {len(slugs)}")

    results = []
    for slug in slugs:
        slug_dir = CLIENTS_DIR / slug
        if not slug_dir.is_dir():
            print(f"  SKIP {slug}: not a directory")
            continue
        info = upsert_workspace(con, slug, slug_dir)
        results.append(info)
        print(f"  ✓ {slug:32s} files={info['files']:3d}  drafts={info['drafts']:2d}  projects={info['projects']:2d}  deliverables={info['deliverables']:2d}")

    con.close()
    print(f"\nDone. {len(results)} workspaces in {INDEX_DB}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

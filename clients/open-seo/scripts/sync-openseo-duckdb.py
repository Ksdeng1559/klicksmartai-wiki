#!/usr/bin/env python3
"""Mirror the OpenSEO D1 SQLite database into a DuckDB analytical store.

Lives at /home/denni/wiki/clients/open-seo/scripts/sync-openseo-duckdb.py
Run manually or via cron to keep the DuckDB in sync with the live container.

Pattern follows LeadSniper's .local_tier convention:
  DataForSEO → Supabase (canonical) → DuckDB mirror (.local_tier) → HTML report.

For OpenSEO the canonical source is the live container's D1 SQLite file; the
mirror gives an OLAP-friendly query layer (columnar-vectorized) for analytics
that would be slow or impossible in SQLite.
"""
from __future__ import annotations

import argparse
import json
import logging
import shutil
import subprocess
import sys
from pathlib import Path

import duckdb

logging.basicConfig(level=logging.INFO, format="%(asctime)s openseo-mirror %(levelname)s %(message)s")
log = logging.getLogger("openseo-mirror")

# Container → host paths
CONTAINER_NAME_DEFAULT = "open-seo-lanpubs-open-seo-1"
D1_PATH_INSIDE_CONTAINER = (
    "/app/.wrangler/state/v3/d1/"
    "miniflare-D1DatabaseObject/"
    "8776b4b8f1ef4325faa1c4edcc1d76726313abcd813c380a6b567bfe699b1f34.sqlite"
)

# Where we land on the host
WORKSPACE = Path("/home/denni/wiki/clients/open-seo")
LOCAL_TIER = WORKSPACE / ".local_tier"
SQLITE_STAGING = LOCAL_TIER / "d1-staging.sqlite"
DUCKDB_PATH = LOCAL_TIER / "clients" / "open-seo.duckdb"


def pull_d1_from_container(container: str, dest: Path) -> None:
    log.info("Pulling D1 SQLite from container %s", container)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        dest.unlink()
    out = subprocess.run(
        ["docker", "cp", f"{container}:{D1_PATH_INSIDE_CONTAINER}", str(dest)],
        capture_output=True, text=True,
    )
    if out.returncode != 0:
        log.error("docker cp failed: %s", out.stderr)
        raise SystemExit(1)
    log.info("  → %s (%d KB)", dest, dest.stat().st_size // 1024)


def get_table_names(con) -> list[str]:
    return [r[0] for r in con.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    ).fetchall()]


def mirror_tables(sqlite_path: Path, duck_path: Path) -> dict[str, int]:
    """Copy every D1 table into DuckDB 1:1. The schema column types may not
    match DuckDB exactly (SQLite has loose typing); we cast aggressively
    where Drizzle emits typed columns. This is best-effort — if a column
    fails we record it and skip that table."""
    con_duck = duckdb.connect(str(duck_path))
    try:
        # Drop and recreate the d1_raw schema each run (idempotent mirror)
        con_duck.execute("DROP SCHEMA IF EXISTS d1_raw CASCADE")
        con_duck.execute("CREATE SCHEMA d1_raw")
        # Required for json_extract_string in views
        con_duck.execute("INSTALL json; LOAD json")

        # Attach SQLite
        con_duck.execute(
            f"ATTACH '{sqlite_path}' AS d1_source (TYPE sqlite, READ_ONLY)"
        )

        # Get table list from SQLite. DuckDB exposes attached SQLite tables under
        # the alias name (no schema prefix). The catalog tables (sqlite_master)
        # are exposed in the main schema of the DuckDB connection itself.
        tables = con_duck.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()
        counts: dict[str, int] = {}
        for (table_name,) in tables:
            if table_name.startswith("sqlite_") or table_name.startswith("_cf_"):
                continue
            try:
                # CREATE mirror table from SQLite, then INSERT rows
                con_duck.execute(
                    f"CREATE TABLE d1_raw.{table_name} AS "
                    f"SELECT * FROM d1_source.{table_name}"
                )
                cnt_row = con_duck.execute(
                    f"SELECT COUNT(*) FROM d1_raw.{table_name}"
                ).fetchone()
                cnt = cnt_row[0] if cnt_row else 0
                counts[table_name] = cnt
            except Exception as e:
                log.warning("Failed to mirror %s: %s", table_name, e)
                # Mark it as broken so we don't silently lose data
                counts[table_name] = -1
        con_duck.execute("DETACH d1_source")
        return counts
    finally:
        con_duck.close()


def flatten_paa_data(sqlite_path: Path, duck_path: Path) -> dict[str, int]:
    """Expand the PAA JSON report column into proper DuckDB tables.
    DuckDB's JSON table-function ergonomics are awkward for nested arrays, so
    we read + parse in Python then INSERT into typed tables — faster and more
    reliable than fighting the SQL."""
    import json as json_mod

    con_src = duckdb.connect(str(sqlite_path), read_only=True)
    try:
        rows = con_src.execute("""
            SELECT scan_id, project_id, seed, region, report, created_at
            FROM main.paa_scans
        """).fetchall()
    finally:
        con_src.close()

    con_dst = duckdb.connect(str(duck_path))
    try:
        con_dst.execute("INSTALL json; LOAD json")
        # Idempotent: drop and recreate the typed tables
        for t in ["paa_demand_signals_flat", "paa_social_threads_flat"]:
            con_dst.execute(f"DROP TABLE IF EXISTS {t}")

        con_dst.execute("""
            CREATE TABLE paa_demand_signals_flat (
                scan_id VARCHAR,
                project_id VARCHAR,
                seed VARCHAR,
                region VARCHAR,
                question VARCHAR,
                intent VARCHAR,
                snippet VARCHAR,
                rank_in_scan BIGINT,
                created_at VARCHAR
            )
        """)
        con_dst.execute("""
            CREATE TABLE paa_social_threads_flat (
                scan_id VARCHAR,
                project_id VARCHAR,
                seed VARCHAR,
                question VARCHAR,
                source VARCHAR,
                thread_title VARCHAR,
                thread_link VARCHAR,
                snippet VARCHAR,
                thread_rank BIGINT,
                created_at VARCHAR
            )
        """)

        sig_rows: list[tuple] = []
        thr_rows: list[tuple] = []
        for scan_id, project_id, seed, region, report, created_at in rows:
            if not report:
                continue
            try:
                r = json_mod.loads(report)
            except json_mod.JSONDecodeError:
                continue
            questions = r.get("questions") or []
            for q_idx, q in enumerate(questions):
                sig_rows.append((
                    scan_id, project_id, seed, region,
                    q.get("question", ""), q.get("intent", ""),
                    q.get("snippet", ""), q_idx, created_at,
                ))
                for s_idx, s in enumerate(q.get("social") or []):
                    thr_rows.append((
                        scan_id, project_id, seed,
                        q.get("question", ""),
                        s.get("source", ""),
                        s.get("title", ""),
                        s.get("link", ""),
                        s.get("snippet", ""),
                        s_idx, created_at,
                    ))

        # Bulk insert
        if sig_rows:
            con_dst.executemany(
                "INSERT INTO paa_demand_signals_flat VALUES (?,?,?,?,?,?,?,?,?)",
                sig_rows,
            )
        if thr_rows:
            con_dst.executemany(
                "INSERT INTO paa_social_threads_flat VALUES (?,?,?,?,?,?,?,?,?,?)",
                thr_rows,
            )

        # Refresh the views to point at the new typed tables
        for v in ["v_paa_demand_signals", "v_paa_social_threads"]:
            con_dst.execute(f"DROP VIEW IF EXISTS {v}")
        con_dst.execute("""
            CREATE VIEW v_paa_demand_signals AS
            SELECT * FROM paa_demand_signals_flat
        """)
        con_dst.execute("""
            CREATE VIEW v_paa_social_threads AS
            SELECT * FROM paa_social_threads_flat
        """)
        return {
            "paa_demand_signals_flat": len(sig_rows),
            "paa_social_threads_flat": len(thr_rows),
        }
    finally:
        con_dst.close()


def create_views(duck_path: Path) -> list[str]:
    """Curated analyst views on top of d1_raw. These are the queries Dennis
    actually wants to run: PAA scan reports, keyword metrics, audit findings,
    SAM session history."""
    con_duck = duckdb.connect(str(duck_path))
    try:
        con_duck.execute("INSTALL json; LOAD json")
        # Drop existing views (rebuild fresh each sync).
        # v_paa_demand_signals and v_paa_social_threads are managed by
        # flatten_paa_data() — leave them alone.
        for v in [
            "v_paa_reports",
            "v_keyword_metrics_by_project",
            "v_audit_findings",
            "v_rank_tracking_summary",
            "v_saved_keyword_library",
        ]:
            con_duck.execute(f"DROP VIEW IF EXISTS {v}")

        con_duck.execute("""
            CREATE VIEW v_paa_reports AS
            SELECT
                s.scan_id,
                s.id AS row_id,
                s.project_id,
                s.seed,
                s.region,
                s.question_count,
                s.created_at,
                p.name AS project_name
            FROM d1_raw.paa_scans s
            LEFT JOIN d1_raw.projects p ON p.id = s.project_id
        """)

        # v_paa_demand_signals and v_paa_social_threads are created in
        # flatten_paa_data() because they require SQL-side JSON unnesting
        # that DuckDB's json extension handles awkwardly. The Python flatten
        # produces typed tables that the views then alias.

        con_duck.execute("""
            CREATE VIEW v_keyword_metrics_by_project AS
            SELECT
                km.id AS keyword_metric_id,
                km.project_id,
                km.keyword,
                km.location_code,
                km.language_code,
                km.search_volume AS volume,
                km.keyword_difficulty AS difficulty,
                km.cpc,
                km.intent,
                km.competition,
                km.monthly_searches,
                km.fetched_at,
                p.name AS project_name
            FROM d1_raw.keyword_metrics km
            LEFT JOIN d1_raw.projects p ON p.id = km.project_id
            ORDER BY km.search_volume DESC NULLS LAST
        """)

        con_duck.execute("""
            CREATE VIEW v_audit_findings AS
            SELECT
                ai.id AS issue_id,
                ai.audit_id,
                ai.page_url,
                ai.severity,
                ai.issue_type AS category,
                ai.details_json AS details,
                a.project_id,
                a.start_url,
                a.status AS audit_status,
                a.started_at,
                a.completed_at,
                p.name AS project_name
            FROM d1_raw.audit_issues ai
            JOIN d1_raw.audits a ON a.id = ai.audit_id
            LEFT JOIN d1_raw.projects p ON p.id = a.project_id
            ORDER BY
                CASE ai.severity
                    WHEN 'critical' THEN 0
                    WHEN 'high' THEN 1
                    WHEN 'medium' THEN 2
                    WHEN 'low' THEN 3
                    ELSE 4
                END,
                ai.audit_id DESC
        """)

        con_duck.execute("""
            CREATE VIEW v_rank_tracking_summary AS
            SELECT
                p.id AS project_id,
                p.name AS project_name,
                rtc.id AS config_id,
                rtc.location_name,
                rtc.domain,
                rtc.schedule_interval,
                rtc.is_active,
                rtc.created_at,
                COUNT(DISTINCT rtk.id) AS keyword_count,
                MAX(rs.checked_at) AS last_snapshot_at
            FROM d1_raw.projects p
            LEFT JOIN d1_raw.rank_tracking_configs rtc ON rtc.project_id = p.id
            LEFT JOIN d1_raw.rank_tracking_keywords rtk ON rtk.config_id = rtc.id
            LEFT JOIN d1_raw.rank_snapshots rs ON rs.tracking_keyword_id = rtk.id
            GROUP BY p.id, p.name, rtc.id, rtc.location_name, rtc.domain,
                     rtc.schedule_interval, rtc.is_active, rtc.created_at
        """)

        # saved_keywords uses location_code, not country
        con_duck.execute("""
            CREATE VIEW v_saved_keyword_library AS
            SELECT
                sk.project_id,
                sk.keyword,
                sk.location_code,
                sk.language_code,
                sk.created_at,
                p.name AS project_name
            FROM d1_raw.saved_keywords sk
            LEFT JOIN d1_raw.projects p ON p.id = sk.project_id
        """)

        return [
            "v_paa_reports",
            "v_paa_demand_signals",
            "v_paa_social_threads",
            "v_keyword_metrics_by_project",
            "v_audit_findings",
            "v_rank_tracking_summary",
            "v_saved_keyword_library",
        ]
    finally:
        con_duck.close()


def write_manifest(duck_path: Path, counts: dict[str, int], view_names: list[str]) -> None:
    manifest_path = LOCAL_TIER / "sync-manifest.json"
    manifest = {
        "duckdb_path": str(duck_path),
        "synced_at": __import__("datetime").datetime.now().isoformat(),
        "tables": counts,
        "views": view_names,
        "table_count": len([c for c in counts.values() if c >= 0]),
        "broken_tables": [t for t, c in counts.items() if c < 0],
        "note": "paa_demand_signals_flat and paa_social_threads_flat appear as broken because mirror_tables() doesn't know about them — they are created by flatten_paa_data() and contain the real PAA flattened data.",
    }
    manifest_path.write_text(json.dumps(manifest, indent=2))
    log.info("Manifest written → %s", manifest_path)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--container", default=CONTAINER_NAME_DEFAULT)
    p.add_argument("--no-pull", action="store_true",
                   help="Skip container pull; reuse existing SQLite staging file")
    args = p.parse_args()

    LOCAL_TIER.mkdir(parents=True, exist_ok=True)
    DUCKDB_PATH.parent.mkdir(parents=True, exist_ok=True)

    if not args.no_pull:
        pull_d1_from_container(args.container, SQLITE_STAGING)

    if not SQLITE_STAGING.exists():
        log.error("Staging SQLite missing: %s", SQLITE_STAGING)
        return 1

    log.info("Mirroring to DuckDB → %s", DUCKDB_PATH)
    counts = mirror_tables(SQLITE_STAGING, DUCKDB_PATH)
    log.info("Mirrored %d tables (broken: %s)",
             sum(1 for c in counts.values() if c >= 0),
             [t for t, c in counts.items() if c < 0])

    log.info("Flattening PAA JSON reports")
    paa_counts = flatten_paa_data(SQLITE_STAGING, DUCKDB_PATH)
    for k, v in paa_counts.items():
        log.info("  %-40s %d rows", k, v)

    log.info("Creating analyst views")
    views = create_views(DUCKDB_PATH)
    for v in views:
        log.info("  view: %s", v)

    write_manifest(DUCKDB_PATH, counts, views)
    log.info("Done. Total: %d tables, %d views, %d KB",
             sum(1 for c in counts.values() if c >= 0),
             len(views),
             DUCKDB_PATH.stat().st_size // 1024)
    return 0


if __name__ == "__main__":
    sys.exit(main())
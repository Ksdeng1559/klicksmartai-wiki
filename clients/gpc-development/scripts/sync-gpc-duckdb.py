#!/usr/bin/env python3
"""Sync OpenSEO D1 SQLite → DuckDB analytical mirror (GPC Development).

Scoped to project_id 34afee19-d725-4073-b43f-1b76c6275c11.
Pulls D1 from the running OpenSEO container, mirrors only GPC tables,
creates per-project views for analyst queries.

Manual run:
    python3 scripts/sync-gpc-duckdb.py
"""
import duckdb
import subprocess
from pathlib import Path
from datetime import datetime

PROJECT_ID = "34afee19-d725-4073-b43f-1b76c6275c11"
D1_CONTAINER_PATH = "/app/.wrangler/state/v3/d1/miniflare-D1DatabaseObject/8776b4b8f1ef4325faa1c4edcc1d76726313abcd813c380a6b567bfe699b1f34.sqlite"
DUCKDB_PATH = Path(__file__).parent.parent / ".local_tier" / "clients" / "gpc-development.duckdb"


def log(level, msg):
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} gpc-mirror {level:5} {msg}")


def pull_d1():
    """Pull D1 SQLite from OpenSEO container to /tmp via docker cp."""
    tmp_path = Path("/tmp/open-seo-d1-gpc.sqlite")
    if tmp_path.exists():
        tmp_path.unlink()
    result = subprocess.run(
        ["docker", "cp",
         f"open-seo-lanpubs-open-seo-1:{D1_CONTAINER_PATH}",
         str(tmp_path)],
        capture_output=True, text=True
    )
    if result.returncode != 0 or not tmp_path.exists() or tmp_path.stat().st_size == 0:
        raise FileNotFoundError(f"Cannot copy D1 from container: {result.stderr}")
    return tmp_path


def main():
    log("INFO", f"Pulling D1 for project {PROJECT_ID}")
    d1_path = pull_d1()

    DUCKDB_PATH.parent.mkdir(parents=True, exist_ok=True)
    if DUCKDB_PATH.exists():
        DUCKDB_PATH.unlink()

    con = duckdb.connect(str(DUCKDB_PATH))
    log("INFO", "Attaching D1 source (READ_ONLY)")
    con.execute(f"ATTACH '{d1_path}' AS d1_source (READ_ONLY)")

    # Create the GPC schema
    con.execute("CREATE SCHEMA IF NOT EXISTS gpc")

    # Tables with project_id column (mirror only this project's rows)
    gpc_tables = [
        ("saved_keywords", "project_id"),
        ("keyword_metrics", "project_id"),
        ("paa_scans", "project_id"),
        ("rank_tracking_configs", "project_id"),
    ]

    for table, pid_col in gpc_tables:
        try:
            cnt = con.execute(
                f"SELECT COUNT(*) FROM d1_source.{table} WHERE {pid_col} = ?",
                [PROJECT_ID]
            ).fetchone()[0]
            if cnt > 0:
                con.execute(
                    f"CREATE OR REPLACE TABLE gpc.{table} AS "
                    f"SELECT * FROM d1_source.{table} WHERE {pid_col} = ?",
                    [PROJECT_ID]
                )
                log("INFO", f"  {table:35} {cnt:5} rows")
        except Exception as e:
            log("WARN", f"  {table:35} skipped ({type(e).__name__}: {str(e)[:50]})")

    # Project-scoped tables with FK pattern:
    # audits (project_id) → audit_pages (audit_id) → audit_issues (audit_id)
    # rank_tracking_configs (project_id) → rank_tracking_keywords (config_id) → rank_snapshots (run_id)
    try:
        # audits
        cnt = con.execute(
            "SELECT COUNT(*) FROM d1_source.audits WHERE project_id = ?", [PROJECT_ID]
        ).fetchone()[0]
        if cnt > 0:
            con.execute(
                "CREATE OR REPLACE TABLE gpc.audits AS "
                "SELECT * FROM d1_source.audits WHERE project_id = ?",
                [PROJECT_ID]
            )
            log("INFO", f"  {'audits':35} {cnt:5} rows")

            # Get the audit IDs
            audit_ids = [r[0] for r in con.execute(
                "SELECT id FROM gpc.audits"
            ).fetchall()]
            if audit_ids:
                placeholders = ",".join(["?"] * len(audit_ids))
                for table in ["audit_pages", "audit_issues", "audit_lighthouse_results"]:
                    try:
                        cnt = con.execute(
                            f"SELECT COUNT(*) FROM d1_source.{table} WHERE audit_id IN ({placeholders})",
                            audit_ids
                        ).fetchone()
                        if cnt and cnt[0] > 0:
                            con.execute(
                                f"CREATE OR REPLACE TABLE gpc.{table} AS "
                                f"SELECT * FROM d1_source.{table} WHERE audit_id IN ({placeholders})",
                                audit_ids
                            )
                            log("INFO", f"  {table:35} {cnt[0]:5} rows")
                    except Exception as e:
                        log("WARN", f"  {table:35} skipped ({type(e).__name__}: {str(e)[:50]})")
    except Exception as e:
        log("WARN", f"  audits chain skipped ({type(e).__name__}: {str(e)[:50]})")

    # Rank tracking chain: rank_tracking_configs (project_id) → rank_tracking_keywords (config_id)
    try:
        configs = [r[0] for r in con.execute(
            "SELECT id FROM gpc.rank_tracking_configs"
        ).fetchall()]
        log("DEBUG", f"rank chain: {len(configs)} config(s)")
        if configs:
            # Single-element tuples need `IN (?,)` syntax, not `IN (?)`
            placeholders = ",".join(["?"] * len(configs))
            for table in ["rank_tracking_keywords"]:
                try:
                    cnt = con.execute(
                        f"SELECT COUNT(*) FROM d1_source.{table} WHERE config_id IN ({placeholders})",
                        configs
                    ).fetchone()
                    log("DEBUG", f"  {table} count query: {cnt}")
                    if cnt and cnt[0] > 0:
                        con.execute(
                            f"CREATE OR REPLACE TABLE gpc.{table} AS "
                            f"SELECT * FROM d1_source.{table} WHERE config_id IN ({placeholders})",
                            configs
                        )
                        log("INFO", f"  {table:35} {cnt[0]:5} rows")
                except Exception as e:
                    log("WARN", f"  {table:35} skipped ({type(e).__name__}: {str(e)[:200]})")
                    import traceback
                    log("DEBUG", traceback.format_exc())

            # rank_snapshots joined via tracking_keyword_id
            try:
                keyword_ids = [r[0] for r in con.execute(
                    "SELECT id FROM gpc.rank_tracking_keywords"
                ).fetchall()]
            except Exception:
                keyword_ids = []
            if keyword_ids:
                placeholders = ",".join(["?"] * len(keyword_ids))
                try:
                    cnt = con.execute(
                        f"SELECT COUNT(*) FROM d1_source.rank_snapshots WHERE tracking_keyword_id IN ({placeholders})",
                        keyword_ids
                    ).fetchone()
                    if cnt and cnt[0] > 0:
                        con.execute(
                            f"CREATE OR REPLACE TABLE gpc.rank_snapshots AS "
                            f"SELECT * FROM d1_source.rank_snapshots WHERE tracking_keyword_id IN ({placeholders})",
                            keyword_ids
                        )
                        log("INFO", f"  {'rank_snapshots':35} {cnt[0]:5} rows")
                except Exception as e:
                    log("WARN", f"  rank_snapshots skipped ({type(e).__name__}: {str(e)[:50]})")
    except Exception as e:
        log("WARN", f"  rank chain skipped ({type(e).__name__}: {str(e)[:50]})")

    # Project-scoped tables that aren't tied to audits/keywords/rank-tracker
    # (context sections, competitors, key pages, research log)
    for table in ["project_context_sections", "project_competitors",
                   "project_key_pages", "project_research_log"]:
        try:
            cnt = con.execute(
                f"SELECT COUNT(*) FROM d1_source.{table} WHERE project_id = ?",
                [PROJECT_ID]
            ).fetchone()
            if cnt and cnt[0] > 0:
                con.execute(
                    f"CREATE OR REPLACE TABLE gpc.{table} AS "
                    f"SELECT * FROM d1_source.{table} WHERE project_id = ?",
                    [PROJECT_ID]
                )
                log("INFO", f"  {table:35} {cnt[0]:5} rows")
        except Exception as e:
            log("WARN", f"  {table:35} skipped ({type(e).__name__}: {str(e)[:50]})")

    # Create empty fallback tables so views always work even when source has 0 rows
    con.execute("""
        CREATE TABLE IF NOT EXISTS gpc.rank_tracking_keywords (
            id VARCHAR PRIMARY KEY,
            config_id VARCHAR,
            keyword VARCHAR,
            created_at TIMESTAMP,
            search_volume INTEGER,
            keyword_difficulty INTEGER,
            cpc DOUBLE,
            metrics_fetched_at TIMESTAMP
        )
    """)
    con.execute("""
        CREATE TABLE IF NOT EXISTS gpc.rank_snapshots (
            id VARCHAR PRIMARY KEY,
            run_id VARCHAR,
            tracking_keyword_id VARCHAR,
            keyword VARCHAR,
            device VARCHAR,
            position INTEGER,
            url VARCHAR,
            serp_features VARCHAR,
            checked_at TIMESTAMP
        )
    """)

    # Now create the analyst views
    log("INFO", "Creating views")
    try:
        con.execute("""
            CREATE OR REPLACE VIEW gpc.v_keyword_metrics_by_project AS
            SELECT keyword, location_code AS market, language_code AS lang,
                   search_volume, keyword_difficulty AS kd, cpc, intent, monthly_searches
            FROM gpc.keyword_metrics
        """)
        log("INFO", "  v_keyword_metrics_by_project")
    except Exception as e:
        log("WARN", f"  v_keyword_metrics_by_project skipped ({str(e)[:80]})")

    try:
        con.execute("""
            CREATE OR REPLACE VIEW gpc.v_saved_keyword_library AS
            SELECT keyword, location_code, language_code, created_at
            FROM gpc.saved_keywords
        """)
        log("INFO", "  v_saved_keyword_library")
    except Exception as e:
        log("WARN", f"  v_saved_keyword_library skipped ({str(e)[:80]})")

    try:
        con.execute("""
            CREATE OR REPLACE VIEW gpc.v_audit_findings AS
            SELECT i.id, i.audit_id, i.page_url, i.issue_type, i.severity, i.details_json,
                   a.start_url, a.started_at, a.completed_at
            FROM gpc.audit_issues i
            LEFT JOIN gpc.audits a ON a.id = i.audit_id
        """)
        log("INFO", "  v_audit_findings")
    except Exception as e:
        log("WARN", f"  v_audit_findings skipped ({str(e)[:80]})")

    try:
        con.execute("""
            CREATE OR REPLACE VIEW gpc.v_paa_demand_signals AS
            SELECT scan_id, seed, region, question_count,
                   json_extract_string(report, '$.paaSourceRegion') AS paa_source_region,
                   json_extract_string(report, '$.questions') AS questions_json,
                   created_at
            FROM gpc.paa_scans
        """)
        log("INFO", "  v_paa_demand_signals")
    except Exception as e:
        log("WARN", f"  v_paa_demand_signals skipped ({str(e)[:80]})")

    try:
        con.execute("""
            CREATE OR REPLACE VIEW gpc.v_rank_tracking_summary AS
            SELECT c.domain, c.schedule_interval, c.devices, c.is_active,
                   c.last_checked_at, c.next_check_at,
                   COUNT(k.id) AS keyword_count
            FROM gpc.rank_tracking_configs c
            LEFT JOIN gpc.rank_tracking_keywords k ON k.config_id = c.id
            GROUP BY c.id, c.domain, c.schedule_interval, c.devices, c.is_active,
                     c.last_checked_at, c.next_check_at
        """)
        log("INFO", "  v_rank_tracking_summary")
    except Exception as e:
        log("WARN", f"  v_rank_tracking_summary skipped ({str(e)[:80]})")

    try:
        con.execute("""
            CREATE OR REPLACE VIEW gpc.v_audit_pages AS
            SELECT url, status_code, title, meta_description, h1_count, h2_count,
                   word_count, images_missing_alt, internal_link_count, external_link_count,
                   response_time_ms, is_indexable
            FROM gpc.audit_pages
        """)
        log("INFO", "  v_audit_pages")
    except Exception as e:
        log("WARN", f"  v_audit_pages skipped ({str(e)[:80]})")

    # Stats
    n_tables = con.execute(
        "SELECT COUNT(*) FROM duckdb_tables WHERE schema_name = 'gpc'"
    ).fetchone()[0]
    n_views = con.execute(
        "SELECT COUNT(*) FROM duckdb_views WHERE schema_name = 'gpc'"
    ).fetchone()[0]

    # Write manifest
    manifest_path = DUCKDB_PATH.parent / "sync-manifest.json"
    manifest = {
        "client": "gpc-development",
        "project_id": PROJECT_ID,
        "duckdb_path": str(DUCKDB_PATH),
        "tables": n_tables,
        "views": n_views,
        "synced_at": datetime.now().isoformat(),
    }
    import json
    manifest_path.write_text(json.dumps(manifest, indent=2))

    con.close()

    # Cleanup tmp
    if d1_path.exists():
        d1_path.unlink()

    log("INFO", f"Done. {n_tables} tables + {n_views} views in {DUCKDB_PATH}")


if __name__ == "__main__":
    main()

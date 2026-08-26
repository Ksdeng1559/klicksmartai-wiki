# OpenSEO — Task Routing

This is the task routing table. When asked to do something OpenSEO-related,
find the row that matches and follow the destination.

| Task | Destination | Notes |
|------|-------------|-------|
| Pull D1 → DuckDB mirror | `scripts/sync-openseo-duckdb.py` | Pulls from container, mirrors to `.local_tier/clients/open-seo.duckdb`, builds 7 analyst views |
| View PAA demand signals | DuckDB: `SELECT * FROM v_paa_demand_signals` | Already-flattens JSON, queryable in standard SQL |
| View PAA social threads | DuckDB: `SELECT * FROM v_paa_social_threads` | Source column: reddit/quora/v2ex/bilibili |
| View top keywords | DuckDB: `SELECT * FROM v_keyword_metrics_by_project` | Order by search_volume DESC |
| View audit issues | DuckDB: `SELECT * FROM v_audit_findings` | Severity-sorted |
| Add new OpenSEO module | `/home/denni/repos/open-seo` + branch pattern | Cherry-pick from upstream, add to staging at `/tmp/open-seo-lanpubs/`, rebuild image, restart container |
| Deploy / rebuild container | `/tmp/open-seo-lanpubs/` (staging dir = Docker build context) | rsync from `/home/denni/repos/open-seo` excluding `.git`, `node_modules`, `dist`, `.output`, `.env*` |
| Push code to GitHub | `git push fork main` (not `git push origin`) | PAT is pull-only on `every-app/open-seo`; push to `Ksdeng1559/open-seo` fork |
| Add MCP server (Hermes) | `hermes mcp add <name>` | Use inline `set` pattern in cmd.exe for WSL |
| Run PAA scan via MCP | `run_paa_mining` tool | Requires `SERPER_API_KEY` set in container env |

## Standing Conventions

- **Workspace root**: `/home/denni/wiki/clients/open-seo/`
- **Source root**: `/home/denni/repos/open-seo/` (branch `main`, ahead of origin by 9 commits as of 2026-08-25)
- **Staging dir (Docker build context)**: `/tmp/open-seo-lanpubs/`
- **Compose file**: `/tmp/open-seo-lanpubs/compose.yaml`
- **Container name**: `open-seo-lanpubs-open-seo-1`
- **Image**: `open-seo:local` (3.77GB)
- **Port mapping**: host 3005 → container 3001

## Module Dormancy Rules

| Key missing | What still works | What doesn't |
|---|---|---|
| `DATAFORSEO_API_KEY` | All non-DataForSEO features | SERP data, keyword metrics, rank tracking, Search Console reads |
| `ONPAGE_API_KEY` | All other features | Content Optimization page + MCP tools (`run_content_scan`, `get_content_scan`) |
| `SERPER_API_KEY` | All non-Serper features | PAA module page, `run_paa_mining`, `get_paa_scan`, Google SERP queries |
| `OPENROUTER_API_KEY` | Everything else | SAM in-app chat agent (`sam_chat` DO), onboarding chat (`onboarding_chat` DO) |

When a key is missing, MCP tools answer "module not configured" and the corresponding sidebar item / route is hidden.
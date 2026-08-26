# OpenSEO

Self-hosted SEO platform with PAA + Social Mining module for demand discovery.

- **Repository**: `/home/denni/repos/open-seo`
- **GitHub**: `Ksdeng1559/open-seo` (fork, push target)
- **Container**: `open-seo-lanpubs-open-seo-1` on `:3005`
- **MCP**: 50 tools exposed
- **License**: MIT

## What's Inside

- **Stock OpenSEO** — keywords, ranks, site audits, Search Console reads
- **On-Page.ai Content Optimization** (BYO key, dormant if empty)
- **PAA + Social Mining** (BYO Serper key + Agent-Reach social proxy) — surfaces language patterns from Reddit/Quora/V2EX/Bilibili
- **SAM agent** (BYO OpenRouter key) — in-app SEO chat

## Data

| Layer | Storage |
|---|---|
| Live data | D1 SQLite (41 tables) in Docker volume `open-seo-lanpubs_open_seo_data` |
| **Analytical mirror** | DuckDB at `.local_tier/clients/open-seo.duckdb` (8.5MB, 39 raw + 7 views) |

Sync the mirror: `python3 scripts/sync-openseo-duckdb.py`

## Quick Queries

```python
import duckdb
con = duckdb.connect("clients/open-seo/.local_tier/clients/open-seo.duckdb", read_only=True)

# Top keywords by volume
con.execute("SELECT keyword, volume, difficulty FROM v_keyword_metrics_by_project LIMIT 10").fetchall()

# PAA demand signals by intent
con.execute("SELECT intent, COUNT(*) FROM v_paa_demand_signals GROUP BY intent").fetchall()

# Social thread sources used
con.execute("SELECT source, COUNT(*) FROM v_paa_social_threads GROUP BY source").fetchall()
```

See [IDENTITY.md](IDENTITY.md) for full project map.
See [CONTEXT.md](CONTEXT.md) for task routing.
See [`_config/conventions.md`](_config/conventions.md) for commit/branch conventions.
# OpenSEO — Conventions

## Commit Messages

OpenSEO uses Conventional Commits. For this fork's custom work:

- `feat: <description>` — new user-facing feature
- `fix: <description>` — bug fix
- `chore: <description>` — maintenance, refactor, dep updates
- `docs: <description>` — documentation only

Examples from this fork's history:
- `feat: integrate On-Page.ai Content Optimization module (lanpubs fork) onto v0.1.6`
- `feat: PAA + Social Mining module for demand discovery`

## Branches

| Branch | Purpose |
|---|---|
| `main` | Production — deployed to `:3005` |
| `feat/paa-social-intelligence` | PAA module work (merged to main, branch retained) |
| `lanpubs` (remote) | Upstream fork: `lanpublications/open-seo` `feat/onpage-content-optimization` |

## Module Dormancy Rules

When a BYO API key is missing, the corresponding module is **dormant** (not just disabled):
- No sidebar item
- No route
- No MCP tool surface

This is by design: the self-host stays clean until the operator enables a module. No need to delete settings UI on a fresh deploy.

## Naming

- MCP tool names: `snake_case` (`run_paa_mining`, `get_content_scan`)
- DB tables: `snake_case` (`paa_scans`, `keyword_metrics`)
- Files: `kebab-case.ts` / `kebab-case.tsx`
- React components: `PascalCase.tsx`

## Ports

- OpenSEO UI: `127.0.0.1:3005` (host) → container `3001`
- OpenSEO MCP: same endpoint, `/mcp` path
- Social proxy: `127.0.0.1:9876` (host) → container reaches via `host.docker.internal:9876`

## Memory Persistence

Live D1 data persists across container recreates via the named Docker volume `open-seo-lanpubs_open_seo_data`. The DuckDB mirror lives at `clients/open-seo/.local_tier/clients/open-seo.duckdb` and is the recommended path for analytical queries.

## Run Order for New Module

1. Develop on a feature branch off `main`
2. Test locally (`pnpm types:check`, `pnpm lint`, `pnpm test`, `pnpm ci:check`)
3. Commit + push to fork remote (`git push fork <branch>`)
4. Merge to main
5. rsync source → `/tmp/open-seo-lanpubs/` (staging dir)
6. Rebuild image: `docker build -f Dockerfile.selfhost -t open-seo:local .` in `/tmp/open-seo-lanpubs/`
7. Restart container: `docker compose up -d` in `/tmp/open-seo-lanpubs/`
8. Wait ~3 min for in-container tsc + vite preview
9. Run `scripts/sync-openseo-duckdb.py` to refresh the analytical mirror
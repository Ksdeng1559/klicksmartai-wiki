# OpenSEO — Workspace Identity

> Self-hosted SEO platform with PAA + Social Mining module for demand discovery. Living at `/home/denni/repos/open-seo`, deployed as Docker container `open-seo-lanpubs-open-seo-1` on port `:3005`.

This is a **client workspace** inside the KlickSmartAI wiki. It follows the
ICM 3-layer template at `shared/templates/client-workspace-icm/` and obeys
the wiki source-of-truth rule (drafts → HITL → projects).

---

## Project Overview

| | |
|---|---|
| **Name** | OpenSEO (forked from `every-app/open-seo`, integrated `lanpublications/open-seo` On-Page.ai module) |
| **Repository** | `/home/denni/repos/open-seo` |
| **GitHub fork** | `Ksdeng1559/open-seo` (push target — `every-app/open-seo` PAT is pull-only) |
| **Container** | `open-seo-lanpubs-open-seo-1` |
| **URL** | `http://127.0.0.1:3005/` |
| **Active MCP tools** | 50 |
| **Stack** | Cloudflare Workers + D1 + Postgres (drizzle), React Start, pnpm workspace |
| **License** | MIT (fork of MIT) |
| **Maintenance mode** | Active — adding custom PAA + Social Mining module |

## Data Storage

| Layer | Storage | Path |
|---|---|---|
| Application data (D1 SQLite) | 41 tables, 1.4MB | Docker volume `open-seo-lanpubs_open_seo_data` → `/app/.wrangler/state/v3/d1/miniflare-D1DatabaseObject/8776b4b8f1ef4325faa1c4edcc1d76726313abcd813c380a6b567bfe699b1f34.sqlite` |
| KV namespace | SQLite per namespace | Same volume, `kv/` |
| R2 blobs | Files | Same volume, `r2/open-seo/blobs/` |
| Durable Objects (SAM, Onboarding, Workflows) | SQLite per DO | Same volume, `workflows/`, `kv/` |
| **DuckDB analytical mirror** | 39 raw tables + 7 analyst views | `/home/denni/wiki/clients/open-seo/.local_tier/clients/open-seo.duckdb` (8.5MB) |

The DuckDB mirror is the recommended path for analytical queries — it's 10-100× faster than SQLite for analytical workloads and integrates with MotherDuck MCP for AI-agent querying.

## Environment Variables

| Variable | Status | Purpose |
|---|---|---|
| `DATAFORSEO_API_KEY` | ✅ wired (52 chars) | SERP data, keyword metrics, rank tracking |
| `ONPAGE_API_KEY` | ⏸️ empty (dormant) | On-Page.ai content optimization module |
| `SERPER_API_KEY` | ✅ wired (40 chars) | Google SERP + PAA + Reddit baseline for social mining |
| `OPENROUTER_API_KEY` | ✅ wired (73 chars) | SAM agent + onboarding chat |
| `SOCIAL_PROXY_URL` | default `http://host.docker.internal:9876` | Agent-Reach social proxy for rdt-cli + V2EX + Bilibili |

## Modules

| Module | Branch / Commit | Status |
|---|---|---|
| Stock OpenSEO | upstream main | ✅ |
| On-Page.ai Content Optimization | `lanpublications/open-seo` fork (6 commits cherry-picked, 1 merge commit) | ✅ integrated |
| **PAA + Social Mining** | `feat/paa-social-intelligence` (commit `09ebdf0`) | ✅ integrated |
| Multi-source social expansion (rdt + V2EX + Bilibili) | post-merge commits on `main` | ✅ live, awaiting `rdt login` |

## Folder Map

```
clients/open-seo/
├── IDENTITY.md            # you are here — Layer 0
├── CONTEXT.md             # Layer 1 — task routing table
├── README.md              # human-facing overview
├── _config/               # Layer 3 — voice, conventions, glossary
│   └── conventions.md
├── projects/              # Layer 4 — validated deliverables
├── drafts/                # Layer 4 — AI work in progress
├── deliverables/          # Layer 4 — client-ready exports
├── drafts-preview/        # Layer 4 — HTML previews
├── skills/                # client-specific skills
├── scripts/               # maintenance scripts (sync-openseo-duckdb.py)
└── .local_tier/           # data + exports (gitignored)
    ├── d1-staging.sqlite  # most recent pull from container
    ├── clients/open-seo.duckdb  # analytical mirror
    └── sync-manifest.json # last sync metadata
```

## Companion Tools (running)

| Tool | Port | Purpose |
|---|---|---|
| OpenSEO container `:3005` | 3005 | Main app + MCP |
| Social proxy `:9876` | 9876 | rdt-cli + V2EX + Bilibili gateway |
| OpenSEO MCP | mcp://openseo | 50 tools exposed via `hermes mcp test openseo` |
| Serper MCP | mcp://serper | `google_search` + `scrape` (npx-based, requires `rdt login` for full Reddit) |
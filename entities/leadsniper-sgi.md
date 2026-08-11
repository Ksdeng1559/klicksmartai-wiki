---
title: LeadSniperAI / SGI Plumbing
created: 2026-08-11
updated: 2026-08-11
type: entity
tags: [entity, leadsniper, sgi, dataforseo, mcp, docker]
sources: []
confidence: medium
---

# LeadSniperAI / SGI Plumbing

LeadSniperAI + Search & Growth Intelligence (SGI) module. Live in Dennis's
Docker setup as `leadsniper-30-*` containers.

## Containers
- `leadsniper-30-backend` (uvicorn) — exposes port 8000 (host) → 8080 (container)
- `leadsniper-30-leadsniper` — exposes port 8090 → 8080 (status: unhealthy
  per most recent check)
- `open-seo-open-seo-1` — DataForSEO-backed provider on 127.0.0.1:3002

## Repo
- `/mnt/c/Users/denni/AI-Applications/LeadSniper-3.0/` (real env, real
  Supabase keys in `.env`).
- WSL project at `~/LeadSniper-3.0/` symlink-equivalent (verify).

## SGI module specifics
- Backend path: `backend/app/sgi/`, 17 routes under `/api/v1/sgi`.
- SQLite at `~/.local/share/leadsniper-sgi/sgi.db`.
- The `sgi_data` volume **survives `docker compose down/up`** (named volume).
- SGI v2 wired: `local` / `VOC` / `zero-volume` variants. Social-derived data,
  requires near-coordinates for `local` / `VOC`.
- **SGI CLI is not built yet** — defer automation until CLI exists.

## Provider plumbing (DataForSEO via OpenSEO)
- OpenSEO is self-hosted at `http://localhost:3002` (loopback only).
- DataForSEO credentials live in OpenSEO container's env, not in the
  LeadSniper `.env`.
- **Post-recreate recovery step:** `docker network connect leadsniper-30_leadsniper-network open-seo-open-seo-1`
  — the OpenSEO container is on a different network by default.

## Supabase access (gotcha)
- Project `yolqrstktoqlszywymw` **DNS fails from WSL** (no internet
  resolution to `*.supabase.co`). Use the pooler URL instead.
- Pooler needs `SUPABASE_DB_PASSWORD` (different from the API key).
- Real keys ONLY in `/mnt/c/Users/denni/AI-Applications/LeadSniper-3.0/.env`,
  NOT in the WSL copy.

## MCP servers for LeadSniper
- `mcp__leadsniper__*` (57 tools) — exposed in this session: search,
  enrichment, decision-maker search, reviews, social enrich, learnings,
  workflow, batch, export.

## See also
- [[Api-Keys-And-Providers]]
- [[Search-Provider-Rotation]]
- [[Service-Port-Registry]]
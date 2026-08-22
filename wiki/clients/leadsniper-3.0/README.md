# LeadSniper-3.0

**Last verified:** 2026-08-22
**Repo:** `~/LeadSniper-3.0` (git-tracked, internal tool)
**Stack:** FastAPI backend (`:8000`) + Next.js SGI frontend (`:8090`) + Python SGI data pipeline
**Owner:** Dennis / KlickSmartAI internal

---

## TL;DR

LeadSniper-3.0 is an internal B2B lead generation tool. It uses Gemini + Google Maps grounding to find businesses by niche/location, enriches them with DataForSEO/Tavily data, and stores batches in Supabase.

The MCP wrapper at `/home/denni/printing-press/library/leadsniper/build/stage/bin/leadsniper-pp-mcp` is registered with Hermes but **all 27 MCP tools return `MCP tenant gate is not configured`** — the printing-press generated CLI has no provider identity adapter, and there's no local Go toolchain to rebuild it.

**Workaround: hit the FastAPI backend directly at `http://127.0.0.1:8000` — 55 routes, no auth, fully working.**

Three live bugs were patched 2026-08-22:
1. Gemini `response_mime_type` + `tools` combo (8 occurrences in 3 files) — removed.
2. `LeadResponse.ownerName: str` default missing — set to `""`.
3. `LeadResponse.phone/website` parse-time guard only rejected `"N/A"`/`"Unknown"`, not `None` — added `isinstance(x, str)` check.

All patches live in BOTH the running container AND the host copy. See [runbook.md](runbook.md) for full operational details.

---

## Documents in this folder

- **README.md** — this file (overview)
- **runbook.md** — operational runbook: services, endpoints, hot-patching procedure, known issues
- **endpoint-catalog.md** — full route inventory (55 routes) with payloads

---

## Quick start

```bash
# Verify backend is healthy
curl -sS http://127.0.0.1:8000/api/v1/health

# Run a search
curl -sS -m 120 -X POST -H "Content-Type: application/json" \
  -d '{"niche":"coffee roaster","city":"Bellingham","state":"WA","focus":"any","max_results":5}' \
  http://127.0.0.1:8000/api/v1/search | head -c 2000

# Get keyword data for a domain
curl -sS -X POST -H "Content-Type: application/json" \
  -d '{"domain":"klicksmartai.com","country":"US","locationCode":2840,"language":"en","requestedBy":"dennis"}' \
  http://127.0.0.1:8000/api/v1/sgi/keywords | head -c 1500
```

## Container services

| Container | Port | Purpose |
|---|---|---|
| `leadsniper-backend` | `8000` | FastAPI app (Gemini + DataForSEO + Tavily) |
| `leadsniper-production` | `8090` | Next.js SGI SPA ("AI Strategic Growth Auditor") |

## Auth

None. The FastAPI backend has no auth middleware. Do NOT expose publicly.

## Links

- Repo: `~/LeadSniper-3.0`
- .env: `~/LeadSniper-3.0/.env`
- docker-compose: `~/LeadSniper-3.0/docker-compose.yml`
- MCP wrapper (broken): `/home/denni/printing-press/library/leadsniper/build/stage/bin/leadsniper-pp-mcp`
- Source for wrapper: `/home/denni/printing-press/library/leadsniper/`
- OpenAPI live: `http://127.0.0.1:8000/openapi.json`

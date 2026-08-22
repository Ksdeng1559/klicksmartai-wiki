# LeadSniper-3.0 Operational Runbook

**Last verified:** 2026-08-22

---

## Architecture

```
┌─────────────────────────────────────────┐
│  Hermes Agent (this session)            │
│  - MCP server: leadsniper (BLOCKED)     │
│  - Direct REST: works                   │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  Docker container: leadsniper-backend   │
│  - Port 8000 → container 8080           │
│  - uvicorn app.main:app (no --reload)   │
│  - Mounted: /data (sgi persistent)      │
└──────┬────────────────────┬─────────────┘
       │                    │
       ▼                    ▼
┌──────────────┐    ┌──────────────────┐
│ Gemini API   │    │ OpenSEO provider │
│ (Vertex,     │    │ :3002            │
│  google_     │    │ → DataForSEO API │
│  search      │    └──────────────────┘
│  grounding)  │
└──────────────┘
```

**External deps:**
- Gemini API: `GEMINI_API_KEY` in `~/LeadSniper-3.0/.env`, mounted into the container.
- OpenSEO provider (DataForSEO proxy): separate container on the `leadsniper-30_leadsniper-network`.
- Supabase: configured via `SUPABASE_URL` + `SUPABASE_KEY` in `.env`; some routes use it for client/batch persistence.

---

## Service map

| Container | Port | Purpose | Status |
|---|---|---|---|
| `leadsniper-backend` | `8000` | FastAPI app (Gemini + DataForSEO + Tavily) | healthy |
| `leadsniper-production` | `8090` | Next.js SGI SPA ("AI Strategic Growth Auditor") | serving HTML |

Both run from the same image (`backend` service in `docker-compose.yml`); the production container is mapped to port 8090 for browser access.

---

## Auth

**None.** The FastAPI backend has no auth middleware. The OpenAPI spec declares no security schemes. All 55 routes are open.

**Implication:** LeadSniper-3.0 backend should NEVER be exposed to the public internet without fronting auth.

---

## Known issues

### 1. MCP wrapper is dead (printing-press generated CLI)
- Binary at `/home/denni/printing-press/library/leadsniper/build/stage/bin/leadsniper-pp-mcp` registered with Hermes, but every tool call returns `MCP tenant gate is not configured`.
- Root cause: generated Go code in `platform_client.go` has `registeredPlatformSource == nil`. The init function that would call `registerPlatformSource(...)` was never generated.
- Local Go toolchain not installed (`go` not in PATH; `go.mod` requires Go 1.26.5, a future version only available via the printing-press build system).
- To fix upstream: re-run the printing-press build with a provider identity adapter registered.
- Until then: hit the FastAPI backend directly.

### 2. Search is slow
- Gemini + Google Maps grounding takes ~60-90s for a single search call.
- Set curl `--max-time 120` minimum.

### 3. Some routes 422 on simple payloads
- `/sgi/*` routes expect `SGIContext` schema (organizationId, clientId, auditId, domain, country, locationCode) — not raw search params.
- `/enrich*` routes expect a full `LeadResponse` shape, not just a name.

### 4. SGI audit routes are slow
- `/api/v1/sgi/audit` (full audit) and `/api/v1/sgi/audit/deep` may exceed 30s.
- `/api/v1/sgi/audit/quick` is the lightweight alternative.

---

## Container management

```bash
cd ~/LeadSniper-3.0
docker compose ps                    # check status
docker compose restart backend       # restart FastAPI after hot-patch
docker compose logs --tail 100 backend
docker exec -it leadsniper-backend sh       # shell into container
docker exec leadsniper-backend cat /code/app/api/endpoints.py > /tmp/x   # pull file
docker cp /tmp/x leadsniper-backend:/code/app/api/endpoints.py           # push file
```

---

## Hot-patching procedure (2026-08-22 lessons)

1. **Don't trust the host copy** — patches on `~/LeadSniper-3.0/backend/...` only affect a future container build. The running container has its own overlay filesystem.
2. **Patch the container file directly** with `docker exec` + `sed`/`python3`.
3. **Mirror patches to host** so the next container build has them.
4. **Restart with `docker compose restart backend`** — `uvicorn` doesn't have `--reload`, so a restart is needed to load code changes.
5. **Verify health** with `curl http://127.0.0.1:8000/api/v1/health` before re-testing.

---

## Patches applied 2026-08-22

### Patch 1: Gemini `response_mime_type` removal

**Files:** `app/api/endpoints.py`, `app/services/vertex_audit.py`, `app/services/review_intelligence.py`

**Problem:** Gemini rejects `response_mime_type: application/json` when used with grounding tools:
```
400 INVALID_ARGUMENT: 'Tool use with a response mime type: application/json is unsupported'
```

**Fix:** Remove the `response_mime_type` line from the Gemini config when `tools` is present. The prompt itself instructs Gemini to return JSON, which works.

### Patch 2: `ownerName` default

**File:** `app/api/endpoints.py`

**Problem:** `LeadResponse.ownerName: str` had no default. Gemini returns `None` for unknown owners → Pydantic validation error → 500.

**Fix:** `ownerName: str = ""`

### Patch 3: `phone`/`website` None handling

**File:** `app/api/endpoints.py` (line ~280)

**Before:**
```python
phone=raw.get("phone") if raw.get("phone") not in ["N/A", "Unknown"] else "",
website=raw.get("website") if raw.get("website") not in ["N/A", "Unknown"] else "",
```

**After:**
```python
phone=raw.get("phone") if isinstance(raw.get("phone"), str) and raw.get("phone") not in ["N/A", "Unknown"] else "",
website=raw.get("website") if isinstance(raw.get("website"), str) and raw.get("website") not in ["N/A", "Unknown"] else "",
```

---

## Future work

- [ ] Rebuild printing-press CLI with provider identity adapter (needs Go 1.26.5 toolchain + printing-press CI integration).
- [ ] Mount host `./backend/app/` into the container so patches don't need to be applied twice.
- [ ] Add a tenant-gate bypass for unauthenticated sources (the binary should not call `verifyFreshMCPInvocation` when `auth_type: "none"` in `.printing-press.json`).
- [ ] Add Gemini fallback (the search handler should fall back to a different model if Gemini returns unstructured text instead of JSON).
- [ ] Add auth to the backend if it'll ever leave localhost.

---

## Quick reference

| What | Where |
|---|---|
| Repo | `/home/denni/LeadSniper-3.0` |
| Backend entry | `backend/app/main.py` |
| Backend API | `backend/app/api/endpoints.py` |
| Services | `app/services/*.py` |
| .env | `~/LeadSniper-3.0/.env` |
| docker-compose | `~/LeadSniper-3.0/docker-compose.yml` |
| OpenAPI spec (host) | `~/LeadSniper-3.0/backend/...` |
| OpenAPI spec (live) | `http://127.0.0.1:8000/openapi.json` |
| MCP wrapper (broken) | `/home/denni/printing-press/library/leadsniper/build/stage/bin/leadsniper-pp-mcp` |
| Source for wrapper | `/home/denni/printing-press/library/leadsniper/` |
| AGENTS.md (wrapper) | `/home/denni/printing-press/library/leadsniper/AGENTS.md` |

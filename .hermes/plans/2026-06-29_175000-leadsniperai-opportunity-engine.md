# LeadSniperAI Inspection & AI Website Opportunity Engine — Implementation Plan

> **For Hermes:** Use `subagent-driven-development` to implement task-by-task. Each task is one subagent, two-stage review (spec compliance → code quality).
>
> **Note on workspace:** This plan is saved under the active wiki workspace, but the project lives at `G:\AI - Coding Projects\LeadSniperAI\`. Move the file (or copy `docs/leadsniperai-opportunity-engine.md` into the repo) when execution starts.

**Goal:** Build an autonomous Business Opportunity Discovery Engine that finds local businesses with strong reputations but weak websites, audits them, scores the opportunity, generates an AI Search–enabled Next.js rebuild, and prepares outreach — wired to the existing LeadSniperAI Vite/React dashboard as the operator UI.

**Architecture:** Two-repo product. The existing `G:\AI - Coding Projects\LeadSniperAI\` Vite/React 19 + TS dashboard stays as the operator UI; a new sibling service `leadsniper-engine` (Python 3.11 + FastAPI + ARQ + PostgreSQL/SQLite + Qdrant) handles crawl/audit/scoring/proposal/site-generation. Engine stores knowledge in RIOS via the OKF bundle, generates websites as commits in per-client Git repos, and exposes a REST API the dashboard already knows how to call.

**Tech Stack:**
- **Engine:** Python 3.11, FastAPI, ARQ (Redis queue), SQLAlchemy + Alembic, httpx, Scrapling, ScrapeGraphAI, Claude Code (Anthropic SDK), Jinja2 (proposal PDF)
- **Discovery:** Serper (Google Maps SERP), DataForSEO (enrichment + Local Finder), Exa (semantic filters)
- **AI:** Anthropic Claude Sonnet 4.5 (analysis + generation), Ollama `nomic-embed-text` (embeddings — already provisioned in Memory OS)
- **Knowledge:** RIOS OKF bundle + Qdrant (existing infrastructure in `G:\AI-Applications\memory-os\`)
- **CMS/Output:** Per-client Next.js 15 + Tailwind site generated as static export, committed to Git, deployed via Vercel/Netlify
- **Outreach:** Resend (email) + Unipile (LinkedIn + CRM hub); SmartLead/GHL deferred
- **Existing UI to reuse:** Vite dashboard at `G:\AI - Coding Projects\LeadSniperAI\` (React 19 + Supabase + Firebase already in `package.json`)
- **Tests:** pytest + pytest-asyncio (engine), Vitest + Testing Library (UI changes)

---

## Phase 0 — Foundation (must complete before any other phase)

### Task 0.1: Create engine repo and shared contract

**Objective:** Establish the new engine service as a sibling repo with a frozen API contract the dashboard can build against immediately.

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\README.md`
- Create: `G:\AI - Coding Projects\leadsniper-engine\pyproject.toml`
- Create: `G:\AI - Coding Projects\leadsniper-engine\.env.example`
- Create: `G:\AI - Coding Projects\leadsniper-engine\docker-compose.yml` (Postgres + Redis + ARQ worker)
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\__init__.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\main.py` (FastAPI skeleton, `/health` only)
- Create: `G:\AI - Coding Projects\leadsniper-engine\contracts\openapi.yaml` — frozen v1 contract

**Step 1: Init repo**

```bash
cd "G:/AI - Coding Projects"
mkdir leadsniper-engine && cd leadsniper-engine
git init
uv init --python 3.11
mkdir -p app contracts tests
```

**Step 2: Write the OpenAPI v1 contract first (frozen)**

`contracts/openapi.yaml` must define (no implementation yet — schema-only):
- `POST /discovery/jobs` — body: `{vertical, geography, filters}` → `{job_id}`
- `GET /discovery/jobs/{job_id}` — status + count of businesses found
- `POST /inspection/run` — body: `{business_id}` → `{inspection_id}`
- `GET /inspection/{inspection_id}` — full audit JSON (site.json schema)
- `POST /opportunity/score` — body: `{inspection_id}` → `{score, revenue_estimate}`
- `POST /proposal/generate` — body: `{business_id}` → `{proposal_id, pdf_url}`
- `POST /site/generate` — body: `{business_id}` → `{site_id, repo_url, preview_url}`
- `GET /crm/contacts/{business_id}` — Unipile contact record
- `POST /outreach/email` — body: `{business_id, template_id}` → `{send_id}`
- Webhook: `POST /webhooks/unipile` — inbound replies/status

**Step 3: Write failing test for `/health`**

```python
# tests/test_health.py
from fastapi.testclient import TestClient
from app.main import app

def test_health():
    c = TestClient(app)
    r = c.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}
```

**Step 4: Implement minimal `app/main.py`**

```python
from fastapi import FastAPI
app = FastAPI(title="LeadSniperAI Engine", version="1.0.0")
@app.get("/health")
def health():
    return {"status": "ok"}
```

**Step 5: Verify + commit**

```bash
uv run pytest tests/test_health.py -v
git add . && git commit -m "feat(engine): scaffold + frozen v1 OpenAPI contract"
```

---

### Task 0.2: Wire engine to dashboard via API client

**Objective:** Make the existing Vite dashboard able to call the engine. This validates the contract before either side builds real logic.

**Files:**
- Modify: `G:\AI - Coding Projects\LeadSniperAI\.env` (add `VITE_ENGINE_URL`)
- Create: `G:\AI - Coding Projects\LeadSniperAI\services\engine.ts` (typed API client generated from `openapi.yaml`)
- Modify: `G:\AI - Coding Projects\LeadSniperAI\App.tsx:1-50` (add a "Engine Status" badge that hits `/health`)

**Step 1: Generate TS client** using `openapi-typescript`:
```bash
cd "G:/AI - Coding Projects/LeadSniperAI"
npm i -D openapi-typescript
npx openapi-typescript "G:/AI - Coding Projects/leadsniper-engine/contracts/openapi.yaml" -o types/engine.d.ts
```

**Step 2: Write failing Vitest**

```tsx
// services/engine.test.ts
import { describe, it, expect } from 'vitest';
import { engine } from './engine';

describe('engine client', () => {
  it('hits /health', async () => {
    const r = await engine.health();
    expect(r.status).toBe('ok');
  });
});
```

**Step 3: Implement `services/engine.ts`** using `fetch` + the generated types. Stub with localhost fallback.

**Step 4: Add badge in App.tsx** — small pill showing engine up/down based on `/health`.

**Step 5: Verify + commit**

```bash
npm run test:run -- services/engine.test.ts
npm run typecheck
git add . && git commit -m "feat(dashboard): engine API client + status badge"
```

---

## Phase 1 — Discovery (Serper + DataForSEO + Exa)

### Task 1.1: Serper Google Maps discovery adapter

**Objective:** Find local businesses matching a vertical + geography using Serper's Google Maps SERP.

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\discovery\__init__.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\discovery\serper.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\discovery\models.py` (Pydantic: `Business`, `DiscoveryJob`)
- Create: `G:\AI - Coding Projects\leadsniper-engine\tests\test_discovery_serper.py`

**Step 1: Write failing test (use recorded Serper response fixture)**

```python
# tests/fixtures/serper_maps.json — paste a real response here
async def test_serper_extracts_businesses(httpx_mock):
    httpx_mock.add_response(json=json.load(open("tests/fixtures/serper_maps.json")))
    results = await serper_maps_search("roofing contractors", "Kelowna, BC")
    assert len(results) >= 5
    assert all("name" in b and "website" in b for b in results)
```

**Step 2: Implement adapter**

```python
# app/discovery/serper.py
import os, httpx
from .models import Business

SERPER_URL = "https://google.serper.dev/maps"

async def serper_maps_search(query: str, location: str, limit: int = 20) -> list[Business]:
    async with httpx.AsyncClient() as c:
        r = await c.post(SERPER_URL,
            headers={"X-API-KEY": os.environ["SERPER_API_KEY"]},
            json={"q": query, "location": location, "num": limit})
        r.raise_for_status()
        return [_to_business(p) for p in r.json().get("places", [])]

def _to_business(p: dict) -> Business:
    return Business(
        name=p["title"], address=p.get("address"),
        phone=p.get("phone"), website=p.get("website"),
        rating=p.get("rating"), review_count=p.get("reviews"),
        place_id=p.get("placeId"), source="serper_maps",
    )
```

**Step 3: Verify + commit**

```bash
uv run pytest tests/test_discovery_serper.py -v
git commit -am "feat(discovery): serper maps adapter"
```

---

### Task 1.2: DataForSEO enrichment adapter (NAP + backlink snapshot)

**Objective:** Enrich discovered businesses with structured NAP, business listings count, and trust signals (review velocity, citation count).

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\discovery\dataforseo.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\tests\test_discovery_d4s.py`

**Step 1: Failing test** — use DataForSEO Business Listings fixture; assert enrichment fields populated.

**Step 2: Implement adapter** — wraps `business_listings_search` + `backlinks_summary`. Store raw responses for audit trail.

**Step 3: Verify + commit.**

---

### Task 1.3: "Weak website" heuristic gate

**Objective:** Filter discovered businesses to only those with weak/old/missing websites — the core PRD insight.

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\discovery\qualifier.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\tests\test_qualifier.py`

**Step 1: Failing test**

```python
def test_weak_site_gate():
    assert qualifies(Business(name="A", website=None, review_count=120, rating=4.7)) is True
    assert qualifies(Business(name="B", website="https://agency-site.com", review_count=120, rating=4.7)) is False
    assert qualifies(Business(name="C", website="https://old-wp.com", review_count=120, rating=4.7, domain_age_years=12)) is True
```

**Step 2: Implement rules** (PRD-aligned):
- `review_count >= 50` AND `rating >= 4.0` (proven business)
- AND (`website is None` OR `domain_age_years >= 8` OR `tech_stack in {"wordpress-old", "wix", "weebly", "static"}`)
- AND `website_status_code == 200` (don't chase dead sites)

**Step 3: Verify + commit.**

---

### Task 1.4: Discovery job orchestrator (ARQ worker)

**Objective:** Wire discovery into the job queue so a cron or dashboard click can run 1,000+ businesses without blocking.

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\workers\__init__.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\workers\discovery.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\workers\settings.py` (ARQ settings)
- Modify: `G:\AI - Coding Projects\leadsniper-engine\docker-compose.yml` (add ARQ worker service)
- Create: `G:\AI - Coding Projects\leadsniper-engine\tests\test_discovery_worker.py`

**Step 1: Failing test** — async test that enqueues a job and asserts a Business row lands in DB within 30s (use real Redis from compose, pytest-asyncio).

**Step 2: Implement worker** — paginates Serper (e.g., 100 results per call, 10 calls = 1,000 businesses), runs qualifier, persists to Postgres, enqueues per-business inspection jobs.

**Step 3: Verify** with `docker compose up redis postgres worker` and `uv run pytest tests/test_discovery_worker.py`.

**Step 4: Commit.**

---

## Phase 2 — Website Inspection (Scrapling + ScrapeGraphAI)

### Task 2.1: Scrapling crawler producing structured outputs

**Objective:** Crawl a website end-to-end and emit the six JSON files the PRD specifies.

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\inspection\__init__.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\inspection\crawler.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\inspection\outputs.py` (Pydantic models for the 6 outputs)
- Create: `G:\AI - Coding Projects\leadsniper-engine\tests\test_crawler.py`

**Step 1: Failing test** — crawl a fixture site (use a saved HTML mirror in `tests/fixtures/sites/`) and assert all 6 output files are produced with the expected schema.

**Step 2: Implement crawler** — `Scrapling` `StealthyFetcher` for JS render, BFS link following up to 200 pages, capture: HTML, CSS, JS, images, PDFs, sitemap.xml, robots.txt, favicon, canonical, OG, Twitter cards, performance timings.

**Step 3: Verify** — `pytest tests/test_crawler.py -v` against 3 fixture sites (simple HTML, JS-heavy SPA, broken WP).

**Step 4: Commit.**

---

### Task 2.2: Technical, SEO, Performance analyzers

**Objective:** Score the site across the 8 categories the PRD lists (Technical, SEO, Performance, Trust, Conversion, AI Search, Content, Brand, Accessibility).

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\inspection\analyzers\__init__.py`
- Create one analyzer per category: `technical.py`, `seo.py`, `performance.py`, `trust.py`, `conversion.py`, `ai_search.py`, `content.py`, `brand.py`, `accessibility.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\inspection\score.py` (weighted aggregator)
- Create: `G:\AI - Coding Projects\leadsniper-engine\tests\test_analyzers.py`

**Step 1: For each analyzer: failing test → implementation → commit.** Keep each analyzer's contract narrow — input is one of the 6 output files, output is `{score: int (0-100), findings: list[str], evidence: dict}`.

**Step 2: Critical detail for `ai_search.py`** — explicitly check for JSON-LD types per PRD §4: Organization, LocalBusiness, FAQ, Review, Article, Breadcrumb, Person. Missing required types = heavy penalty (per the AI Search readiness framing).

**Step 3: Weighted score formula** — derive weights from PRD §5 example (Website Quality 48/100); document weights in `score.py:WEIGHTS`.

**Step 4: Verify + commit.**

---

### Task 2.3: ScrapeGraphAI extraction (conditional)

**Objective:** Run ScrapeGraphAI only on pages where structural extraction (services, staff, FAQs, pricing) is ambiguous.

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\inspection\extraction\scrapegraphai.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\inspection\extraction\gate.py` (decides when to invoke)
- Create: `G:\AI - Coding Projects\leadsniper-engine\tests\test_scrapegraphai.py`

**Step 1: Failing test** — gate logic returns `True` for a fixture with no `<dl>`/`<table>` structure for services, `False` otherwise.

**Step 2: Implement gate** — heuristic check: parse DOM for known service-list selectors (Bootstrap `.list-group`, WordPress `ul.services`, etc.); if absent and ScrapeGraphAI is configured, invoke.

**Step 3: Wrap ScrapeGraphAI call** — prompt: "Extract: services, staff, team members, pricing, FAQs, contact info, industries, products. Return JSON schema {services: [...], staff: [...], faqs: [...], contact: {...}}".

**Step 4: Verify + commit.**

---

### Task 2.4: Claude reasoning layer

**Objective:** Pass all 6 analyzer outputs to Claude for a structured "weakness narrative" — the thing humans actually read.

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\inspection\reasoning\claude.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\inspection\reasoning\prompts.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\tests\test_claude_reasoning.py` (use Anthropic mock client)

**Step 1: Failing test** — feed mocked analyzer outputs; assert narrative has expected sections (weaknesses, top-3 issues, recommended rebuild components).

**Step 2: Implement prompt + call** — single Claude Sonnet 4.5 call; structured output JSON `{weaknesses: [...], top_issues: [...], rebuild_components: [...]}`.

**Step 3: Verify + commit.**

---

## Phase 3 — Opportunity Scoring + Revenue Estimate

### Task 3.1: Score persistence + revenue engine

**Objective:** Persist scores to Postgres; compute revenue per PRD §6 template ($4,500 website, $800 AI Search, $300/mo CMS, $500/mo SEO, $14,000 LTV).

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\opportunity\__init__.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\opportunity\score.py` (already partially done in Phase 2)
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\opportunity\revenue.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\alembic\versions\001_opportunities.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\tests\test_revenue.py`

**Step 1: Failing test** — given a score of 48, revenue estimate yields website >= $4,000, LTV >= $10,000, monthly >= $500.

**Step 2: Implement tiered formula:**
- Website: `$1500 + (100 - score) * $60` (worse site = bigger project)
- AI Search: `score < 60 → $800 one-time + $300/mo`
- CMS: `score < 50 → $500/mo`
- SEO: `score < 70 → $500/mo`
- LTV: `12 * monthly + website`

**Step 3: Migrate DB + commit.**

---

## Phase 4 — Knowledge Storage in RIOS

### Task 4.1: RIOS ingest adapter

**Objective:** Every inspection becomes an OKF-typed knowledge artifact in `G:\AI - Coding Projects\RIOS-CRM\RIOS\okf\` so future agents can recall.

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\knowledge\__init__.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\knowledge\rios.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\tests\test_rios_ingest.py`

**Step 1: Failing test** — given a Business + Inspection, write an OKF Entity markdown file with frontmatter `{type: Entity, vertical, geography, score, ...}` and a sister Reference file with the audit.

**Step 2: Implement writer** — follows OKF v0.1 spec (per the existing `references/okf-spec-summary.md` in RIOS). Use `pathlib` to write under `G:\AI - Coding Projects\RIOS-CRM\RIOS\okf\entities\businesses\<slug>.md`. Trigger Memory OS worker via ARQ queue (reuse the existing `process_wiki_file` job pattern).

**Step 3: Verify** — file lands in RIOS, Qdrant gets a new point.

**Step 4: Commit.**

---

## Phase 5 — Proposal Generation

### Task 5.1: PDF proposal from templates

**Objective:** Generate a branded proposal PDF per inspection (executive summary, audits, competitor comparison, pricing, roadmap).

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\proposal\__init__.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\proposal\templates\default.html` (Jinja2)
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\proposal\generator.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\tests\test_proposal.py`

**Step 1: Failing test** — generate proposal from a fixture inspection; assert PDF is non-empty, contains business name, all 7 sections.

**Step 2: Implement** — Jinja2 template + WeasyPrint (HTML→PDF). Save to S3-compatible storage (or local `proposals/<business_id>/proposal.pdf` for v1).

**Step 3: Commit.**

---

## Phase 6 — Website Generation

### Task 6.1: Per-client Next.js 15 template repo

**Objective:** Maintain a canonical Next.js 15 + Tailwind + SEO + AI Search template that gets forked per client.

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\templates\nextjs-site\package.json`
- Create: `G:\AI - Coding Projects\leadsniper-engine\templates\nextjs-site\tailwind.config.ts`
- Create: `G:\AI - Coding Projects\leadsniper-engine\templates\nextjs-site\app\layout.tsx`
- Create: `G:\AI - Coding Projects\leadsniper-engine\templates\nextjs-site\app\page.tsx` (will be overwritten by generator)
- Create: `G:\AI - Coding Projects\leadsniper-engine\templates\nextjs-site\components\jsonld.tsx` (helper for AI Search schemas)
- Push to: dedicated GitHub template repo (or `git clone` per client into `G:\AI-Applications\leadsniper-clients\<slug>\`)

**Step 1: Hand-build template** — must include from PRD §8: Tailwind, SEO meta helpers, JSON-LD schema helpers (Organization/LocalBusiness/FAQ/Review/Breadcrumb/Article/Person), responsive, blog (MDX), landing pages, FAQ pages, location pages.

**Step 2: AI Search optimized by default** — every page renders appropriate schema; sitemap.xml auto-generated; canonical URLs; speakable schema for voice.

**Step 3: Commit template.**

---

### Task 6.2: Site generator (Claude fills template with client content)

**Objective:** Given an Inspection + ScrapeGraphAI extracted services/staff/FAQs, generate a complete client site.

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\generator\__init__.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\generator\prompts.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\generator\generate.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\tests\test_generator.py`

**Step 1: Failing test** — given fixture inspection, generate site files, assert pages exist for: home, services, about, contact, blog index, FAQ, each location.

**Step 2: Implement** — clone template repo, write `data/client.json` (services, staff, contact, NAP), invoke Claude to generate copy + page structure, write files, commit to per-client Git repo.

**Step 3: Deploy** — Vercel/Netlify deploy hook (v1: manual; v2: triggered API).

**Step 4: Commit.**

---

## Phase 7 — CMS Generation

### Task 7.1: Markdown-based content for the generated site

**Objective:** Generate the content corpus from PRD §9 (Blog, Pages, Services, Staff, Projects, Testimonials, FAQs, Images alt-text, Downloads, News, Resources).

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\cms\__init__.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\cms\content.py`

**Step 1: Failing test** — content corpus renders to MDX files in the cloned site repo.

**Step 2: Implement** — reuses `generator.generate.py`; every content type is an MDX file with frontmatter.

**Step 3: Commit.**

---

## Phase 8 — CRM Integration (Unipile only, per user decision)

### Task 8.1: Unipile contact creation on qualified lead

**Objective:** When a Business qualifies (score + revenue threshold), create a Unipile contact with all known fields.

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\crm\__init__.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\crm\unipile.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\tests\test_unipile.py`

**Step 1: Failing test** — mock Unipile API; assert contact is created with all PRD §11 fields (owner, website, email, phone, opportunity_score, proposal_status, website_status, pipeline).

**Step 2: Implement** — POST to Unipile contacts endpoint; persist `unipile_contact_id` on the Business row.

**Step 3: Webhook handler** — `POST /webhooks/unipile` for inbound reply/status updates; updates Business state.

**Step 4: Commit.**

---

## Phase 9 — Outreach (Resend only)

### Task 9.1: Resend email sender

**Objective:** Send first-touch cold emails with the proposal PDF attached.

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\outreach\__init__.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\outreach\resend.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\outreach\templates\first_touch.md`
- Create: `G:\AI - Coding Projects\leadsniper-engine\tests\test_outreach.py`

**Step 1: Failing test** — given Business + proposal_id, send email; assert Resend returns send_id.

**Step 2: Implement** — Resend Python SDK; attach proposal PDF; template pulled from disk (Markdown → HTML via `markdown` lib).

**Step 3: Wire webhook** — listen for Resend delivery/open/reply events; update Unipile contact state.

**Step 4: Commit.**

---

## Phase 10 — Operator UI Integration

### Task 10.1: Discovery jobs page in dashboard

**Objective:** Operator clicks "Run discovery" in the existing Vite dashboard; sees results stream in.

**Files:**
- Create: `G:\AI - Coding Projects\LeadSniperAI\pages\DiscoveryJobs.tsx`
- Modify: `G:\AI - Coding Projects\LeadSniperAI\App.tsx` (add route)
- Create: `G:\AI - Coding Projects\LeadSniperAI\__tests__\DiscoveryJobs.test.tsx`

**Step 1: Failing test** — render component, mock engine client, assert form submits and table displays jobs.

**Step 2: Implement** — uses generated `engine` client from Task 0.2.

**Step 3: Verify + commit.**

---

### Task 10.2: Inspection viewer + opportunity score card

**Objective:** Operator clicks a business, sees the full audit JSON, the score gauge, the revenue estimate, and a "Generate Proposal" button.

**Files:**
- Create: `G:\AI - Coding Projects\LeadSniperAI\pages\BusinessDetail.tsx`
- Create: `G:\AI - Coding Projects\LeadSniperAI\components\ScoreGauge.tsx`
- Create: `G:\AI - Coding Projects\LeadSniperAI\components\AuditReport.tsx`
- Create: `G:\AI - Coding Projects\LeadSniperAI\__tests__\BusinessDetail.test.tsx`

**Step 1: Failing test** — mock `/inspection/{id}`; render; assert all audit sections + score gauge visible.

**Step 2: Implement** — reuses existing Tailwind/shadcn-style components already in the Vite app.

**Step 3: Commit.**

---

## Phase 11 — Observability + Quota Management

### Task 11.1: Per-API quota tracking

**Objective:** PRD §14 says Hermes tracks API quotas and rate limits. Build a single source of truth.

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\quota\__init__.py`
- Create: `G:\AI - Coding Projects\leadsniper-engine\app\quota\tracker.py` (Redis-backed counters)
- Modify: each adapter (`serper.py`, `dataforseo.py`, `scrapegraphai.py`, `claude.py`) — add `@quota("vendor:endpoint")` decorator
- Create: `G:\AI - Coding Projects\leadsniper-engine\tests\test_quota.py`

**Step 1: Failing test** — exceeding daily Serper quota raises `QuotaExceeded` and the ARQ job retries with backoff.

**Step 2: Implement decorator + tracker.**

**Step 3: Commit.**

---

## Phase 12 — Success Metrics + End-to-End Test

### Task 12.1: End-to-end smoke test

**Objective:** Single command runs the whole pipeline against 3 fixture businesses; asserts all 12 PRD KPIs are achievable.

**Files:**
- Create: `G:\AI - Coding Projects\leadsniper-engine\tests\test_e2e.py`

**Step 1: Implement** — pytest with fixtures for: discovery → inspection → score → proposal → site generation → outreach (mocked). Asserts:
- Discovery yields ≥3 businesses in <30s
- Each inspection completes in <180s
- Each score is 0–100
- Each proposal PDF is non-empty
- Each generated site builds (`npm run build`)
- Each outreach email enqueues successfully

**Step 2: Verify + commit.**

---

## Files Likely to Change (summary)

**New repo:** `G:\AI - Coding Projects\leadsniper-engine\`
- `pyproject.toml`, `docker-compose.yml`, `.env.example`, `README.md`
- `contracts/openapi.yaml` (frozen v1)
- `app/main.py`, `app/discovery/`, `app/inspection/`, `app/inspection/analyzers/`, `app/inspection/extraction/`, `app/inspection/reasoning/`, `app/opportunity/`, `app/knowledge/`, `app/proposal/`, `app/generator/`, `app/cms/`, `app/crm/`, `app/outreach/`, `app/quota/`, `app/workers/`
- `templates/nextjs-site/` (canonical Next.js template)
- `alembic/` (DB migrations)
- `tests/` (pytest + pytest-asyncio)

**Modified:** `G:\AI - Coding Projects\LeadSniperAI\`
- `.env` (add `VITE_ENGINE_URL`)
- `types/engine.d.ts` (generated, committed)
- `services/engine.ts`, `App.tsx`, new pages `pages/DiscoveryJobs.tsx`, `pages/BusinessDetail.tsx`, new components `ScoreGauge.tsx`, `AuditReport.tsx`
- New tests in `__tests__/`

**New OKF artifacts in RIOS:** `G:\AI - Coding Projects\RIOS-CRM\RIOS\okf\entities\businesses\*.md`, `G:\AI - Coding Projects\RIOS-CRM\RIOS\okf\references\inspections\*.md`

**Per-client repos:** `G:\AI-Applications\leadsniper-clients\<slug>\` (one Next.js project per business)

---

## Tests / Validation

Per task above; cumulatively:

```bash
# Engine
cd "G:/AI - Coding Projects/leadsniper-engine"
uv run pytest -v                 # unit + integration
uv run pytest tests/test_e2e.py  # full pipeline smoke
uv run ruff check .              # lint
uv run mypy app                  # typecheck

# Dashboard
cd "G:/AI - Coding Projects/LeadSniperAI"
npm run test:run
npm run typecheck
npm run lint
```

**Acceptance gates** before any phase is "done":
1. All tests pass
2. Engine `/health` returns 200 from dashboard
3. RIOS file appears in `okf/entities/businesses/` for any new inspection
4. Generated site builds (`npm run build`) with no errors
5. Proposal PDF opens in Chrome

---

## Risks, Tradeoffs, and Open Questions

### Risks
- **Serper Maps quota burn** — 1,000 businesses/day × 5 enrichment calls = 5K/day. Stay under 50K/mo cap. Mitigation: cache by `place_id`.
- **ScrapeGraphAI cost** — invoked per ambiguous page. Mitigation: aggressive `gate.py` heuristic + daily cap.
- **Existing dashboard coupling** — Vite app is Supabase + Firebase. We're not replacing auth; we're adding an API client. Mitigation: keep Supabase for user auth, engine for ops data.
- **Per-client Git repos scale** — generating 1,000 sites/month creates repo sprawl. Mitigation: GitHub App + monorepo with per-client workspaces (Phase 2 optimization).
- **AI Search metric is moving target** — "AI Search readiness" today ≠ in 6 months. Mitigation: analyzer weights are config, not code; can be tuned without redeploy.

### Tradeoffs accepted
- **No Lighthouse in v1** (Phase 2 per PRD) — Core Web Vitals approximated via Scrapling perf timings.
- **No competitor benchmarking in v1** — flagged for Phase 2.
- **No vision-based UI analysis in v1** — flagged for Phase 2.
- **No continuous monitoring / change detection in v1** — flagged for Phase 2.
- **Single CRM (Unipile)** — SmartLead/GHL deferred per user decision.

### Open questions for the user
1. **Target verticals for v1** — narrow to 1–2 verticals (e.g., "roofing" + "dental") or broad horizontal? Narrow ships faster, broader is more revenue.
2. **Geography** — single city (Kelowna) for v1, or multi-region from day one?
3. **Pricing tier** — is the PRD's $4,500/$300/$500 numbers the price card, or just scoring inputs? Real pricing needs a separate decision.
4. **Acceptance target per phase** — when do we consider Phase N "done"? Recommendation: each phase has its own KPI from PRD §Success Metrics table; phase is done when KPI is hit on real data, not fixtures.

---

## Time estimate

Per phase (assuming one developer + one parallel reviewer, no major surprises):
- Phase 0: 1 day (scaffold + contract)
- Phase 1: 2 days (discovery)
- Phase 2: 3 days (inspection — biggest phase)
- Phase 3: 0.5 day
- Phase 4: 1 day (RIOS integration)
- Phase 5: 1 day (proposal PDF)
- Phase 6: 2 days (site generation)
- Phase 7: 0.5 day
- Phase 8: 1 day (Unipile)
- Phase 9: 0.5 day (Resend)
- Phase 10: 2 days (UI integration)
- Phase 11: 1 day (quota)
- Phase 12: 0.5 day (E2E)

**Total: ~16 working days to v1.** Aggressive but realistic with `subagent-driven-development` parallelizing phases 4/8/9 and parallelizing analyzers in Phase 2.
---
title: "Project Meridian" — AI Local Growth Monitor roadmap
created: 2026-08-27
updated: 2026-08-27
status: future-feature / deferred-build catalogue
priority: high (commercial) — gated on user direction to start
blocker: none (user has signed up for On-Page.ai; ready to ship when green-lit)
goal: AI Local Growth Monitor as a productized KlickSmartAI service on top of OpenSEO
---

## What this is

Project Meridian is the **deferred-build catalogue** for the AI Local Growth Monitor — a 4-tier KlickSmartAI service offering that packages OpenSEO's existing 14-skill stack behind a single orchestrator (Meridian) for commercial delivery to SMB clients with Google Business Profiles.

User direction 2026-08-27: **catalogue this under Project Meridian, address later.** All scope items below are preserved in priority order for the next time we green-light the build.

## Status of dependencies (current)

| Dependency | Status | Notes |
|------------|--------|-------|
| OpenSEO platform | ✅ Running | `127.0.0.1:3005`, 50 MCP tools, container `open-seo-lanpubs-open-seo-1` |
| OpenSEO 14-skill catalog | ✅ Authored | `clients/open-seo/_config/seo-skill-catalog.md` |
| `local-seo` skill (Layer 5) | ✅ Bound (in catalog) | **❌ Underlying feature code missing in `src/server/features/`** |
| `content-optimization` skill (Layer 3) | ✅ Bound (in catalog) | **⏸️ Dormant — needs `ONPAGE_API_KEY`** |
| On-Page.ai account | ✅ **User signed up 2026-08-27** | $1 + $10 credits, key not yet wired into container |
| `DATAFORSEO_API_KEY` | ✅ Wired | 52 chars |
| `SERPER_API_KEY` | ✅ Wired | 40 chars |
| `OPENROUTER_API_KEY` | ✅ Wired | 73 chars |
| Meridian orchestrator skill | ❌ Not built | `~/.hermes/skills/meridian/` does not exist |
| Service-offering page | ❌ Not built | `clients/open-seo/_config/service-offering.md` does not exist |
| Sprint doc §11 update | ❌ Not yet | `processes/seo-client-onboarding-sprint.md` |
| GPC Development pilot | ❌ Not started | Existing client, perfect pilot candidate |

## Scope catalogue (priority order, address when unblocked)

### Step 1 — Wire `ONPAGE_API_KEY` + verify skill activation (~30 min)

**Why first:** smallest, fastest, highest information value. Lights up the entire `content-optimization` skill, validates the full On-Page.ai ↔ OpenSEO integration end-to-end. Single env var change in `/tmp/open-seo-lanpubs/.env`, container restart, verify the dormant sidebar item appears in the OpenSEO UI, run one test scan against a known URL.

**Files touched:**
- `/tmp/open-seo-lanpubs/.env` — populate `ONPAGE_API_KEY=<key>`
- `/home/denni/wiki/clients/open-seo/IDENTITY.md` — flip `ONPAGE_API_KEY` from `⏸️ empty (dormant)` to `✅ wired`
- `/home/denni/wiki/clients/open-seo/_config/seo-skills.md` — flip `content-optimization` binding from `⏸️ dormant` to `✅ bound`
- Verification: run `run_content_scan` via MCP on a Veritas or GPC URL, confirm 11-section report returns

**Risk:** none — fully reversible, single env var

### Step 2 — Build `local-seo` feature module in OpenSEO repo (~2-3 days)

**Why second:** biggest net-new code, but it's the prerequisite for any Tier 1+ retainer client. The `local-seo` skill is in the catalog but the underlying feature module (`src/server/features/local-seo/`) doesn't exist — there's no Google Business Profile + Maps + reviews + local-grid query surface in the codebase today. This is the foundational code that every "Local Growth" deliverable runs on.

**Architectural pattern** (per `repos/open-seo/AGENTS.md`): `src/server/features/<name>/{services,repositories}/` + mirror UI in `src/client/features/<name>/`. Follow the `content-optimization` module structure (lanpublications fork) since it's the closest analog.

**What it needs:**
- `repositories/` — D1 schema for GBP profiles, reviews, local-grid snapshots, citation records
- `services/` — DataForSEO Local Finder API calls (no separate Localo vendor needed — DataForSEO already has `get_business_profile`, `get_business_reviews`, `get_business_questions`, `get_business_updates`, `search_local_businesses`, `list_business_categories` per the catalog, these are MCP tools but the backend services need to exist)
- `services/onpage/` — extend with local-entity coverage + Recipe #16 GBP Alignment Verification
- `client/features/local-seo/` — GBP dashboard UI + local-rank grid + review velocity charts
- Migration scripts — D1 schema additions, DuckDB mirror view updates
- MCP tool surface — verify all 6 `local-seo` skill tools work end-to-end
- Unit tests — pattern from `src/server/lib/onpage/client.test.ts`

**Files touched (OpenSEO repo):**
- `src/server/features/local-seo/{services,repositories}/*` (new)
- `src/client/features/local-seo/*` (new)
- `src/server/lib/dataforseo/*` (extend with local endpoints)
- `db/migrations/*` (GBP + reviews + local-grid tables)
- `src/server/lib/onpage/client.ts` (extend with local recipes)

**Files touched (wiki):**
- `clients/open-seo/IDENTITY.md` (document new feature)
- `clients/open-seo/CONTEXT.md` (add local-seo row to routing table)
- `clients/open-seo/_config/seo-skill-catalog.md` (mark local-seo as built, not just bound)
- `.local_tier/clients/open-seo.duckdb` (add local_seo_* tables + v_local_visibility view)

**Risk:** medium — touches core data layer, needs migration + DuckDB view rebuild + UI polish

### Step 3 — Build Meridian orchestrator skill (~1 day)

**Why third:** the only piece that doesn't touch the open-seo repo — it lives in `~/.hermes/skills/meridian/` as a Hermes agent skill. Orchestrates the 14 existing skills (not replaces them) — so all HITL gates, audit trails, and DuckDB patterns are inherited for free.

**Pattern source:** `drafts/future-projects/meridian-local-seo-agent.md` (already written, 195 lines, commit `054cb40`)

**What it needs:**
- `~/.hermes/skills/meridian/SKILL.md` — 4-division orchestration logic (Intelligence → Strategy → Execution → Quality), HITL gate via `drafts/` + `VALIDATION_QUEUE.md`
- 7 slash commands: `/meridian portfolio`, `client`, `monitor`, `opportunities`, `report`, `prospect`, `revenue-hunt`
- HITL wiring — every Meridian run lands a row in `clients/<slug>/drafts/seo/STRATEGIC_INTELLIGENCE_BRIEF_<date>.md` + `VALIDATION_QUEUE.md` + Telegram ping
- Cron integration — `/meridian monitor` runs every 30 min, exception-only alerts
- Composite Visibility Score computation — organic 40% + Maps 35% + reviews 15% + citations 10%

**Risk:** low — pure Hermes skill, no repo changes

### Step 4 — Service-offering page + sprint doc §11 (~1 hour)

**Why fourth:** marketing/docs, no code. Can be done any time after Steps 1-3 are complete (or in parallel with Step 2).

**Files touched (wiki):**
- `clients/open-seo/_config/service-offering.md` (new) — public-facing product page with 4-tier pricing matrix
- `processes/seo-client-onboarding-sprint.md` §11 — add "AI Local Growth Monitor" section
- `clients/open-seo/_config/seo-skill-catalog.md` — add Layer 6 (Orchestration) entry for Meridian
- `drafts/future-projects/on-page-ai-seo-automation.md` — update status from "evaluating" to "activated"
- `drafts/future-projects/meridian-local-seo-agent.md` — update status from "blocked on Localo" to "awaiting green-light"

**Risk:** none — pure docs

### Step 5 — GPC Development pilot (~2 weeks)

**Why last:** depends on all four prior steps. Once Step 1-3 ship, GPC is the perfect pilot:
- Existing client (Tak Ho + Zulliy Alnahas)
- Multi-location (per-location strategy logic test)
- DuckDB mirror already running (`.local_tier/clients/gpc-development.duckdb`)
- 21 pages already audited (3 prior OpenSEO audits)
- Workspace + `_config/gtm-skills.md` already established

**Pilot sequence:**
- Week 1 Day 1: free Tier 1 audit (Composite Visibility Score baseline) — hand-delivered
- Week 1 Day 2-3: client review + Tier 2 Foundation proposal
- Week 1 Day 4-5: execute Tier 2 top 5 actions
- Week 2: kick off Tier 3 Retainer, first weekly cron + monthly SIB
- Capture case study + open to next 5 clients

**Risk:** low — established client relationship, no surprises

## Source drafts (already written, awaiting execution)

| Draft | Commit | Status |
|-------|--------|--------|
| `meridian-local-seo-agent.md` | `054cb40` | Architecture spec ready, skill not built |
| `on-page-ai-seo-automation.md` | `9ee1bc2` | API + 23 recipes catalogued, user signed up |
| `klicksmartai-ai-local-growth-monitor-service.md` | `ad5493a` | 4-tier service offering spec (v2: OpenSEO positioning) |

## Related commitments (preserved)

- AI SEO Modules A+B committed `30c6c4d` — Module A $3-5K/$5-8K/$10-15K+ setup, Module B $1.5-3K/mo retainer (companion add-ons to Meridian tiers)

## Next green-light

When ready to start, user replies "proceed" or "start Step 1" or "start Step N" — each step is independently shippable and the user picks the entry point.

## Open questions (for next session)

1. Step 1 first (validate the pipeline, ~30 min) or Step 3 first (build Meridian against current skills, ~1 day)?
2. Localo MCP still needed? Or can DataForSEO's local endpoints cover everything (per the catalog, they already do)?
3. Brand name — "AI Local Growth Monitor" or rename?
4. Pilot client — GPC Development confirmed, or different first customer?

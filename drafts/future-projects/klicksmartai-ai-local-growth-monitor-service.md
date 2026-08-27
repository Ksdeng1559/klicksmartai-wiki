---
title: "AI Local Growth Monitor" — OpenSEO service offering
created: 2026-08-27
updated: 2026-08-27
status: draft / service-offering (v2 — repositioned as OpenSEO suite product)
priority: high (commercial)
blocker: `ONPAGE_API_KEY` (already wired env, just empty — $1 to activate) + Localo MCP consideration
target client: SMBs with Google Business Profiles (contractors, dentists, attorneys, real estate, multi-location retail, home services)
deliverable: a sellable recurring service that runs on Meridian orchestrating the OpenSEO skill stack
---

## TL;DR — the corrected mental model

After reading the existing `clients/open-seo/` workspace, the **AI Local Growth Monitor is not a new product** — it's a **productized packaging** of the OpenSEO skill stack that already exists in our codebase:

- **OpenSEO platform** at `127.0.0.1:3005` — already deployed, already serving MCP
- **14 SEO skills** in 5 layers — already authored, already HITL-gated
- **On-Page.ai Content Optimization** — already integrated (lanpublications fork), just needs `ONPAGE_API_KEY` populated (currently dormant)
- **`local-seo` skill (Layer 5)** — already exposes GBP + reviews + Local SERP via `get_business_profile`, `get_business_reviews`, etc.
- **`content-optimization` skill (Layer 3)** — already exposes On-Page.ai via `run_content_scan`, `get_content_scan`
- **`seo-enrichment-planner` (Layer 1 gate)** — already enforces HITL + cost estimate before every spend
- **DuckDB mirror** at `clients/open-seo/.local_tier/clients/open-seo.duckdb` — already running, 8.5MB, refreshed every 30 min

What's missing is the **productization**: the 4-tier packaging, the marketing surface, the onboarding playbook, and the **Meridian orchestrator** that ties the 14 skills together into a continuous monitor rather than a set of one-shot commands.

This draft now reflects that — the service offering is a **KlickSmartAI product line built ON TOP OF OpenSEO**, not a competing product.

## Why now — the On-Page.ai activation

The single blocker is `ONPAGE_API_KEY` (52 chars, empty). With it populated:

- `content-optimization` skill comes out of dormancy
- `run_content_scan` and `get_content_scan` MCP tools activate
- Content Optimization page in the UI unlocks
- 11-section PDF audits (eHarmony format) become available
- Recipe #9 (Full Client Website Audit) becomes the centerpiece deliverable

**Cost to activate:** $1 sign-up + $10 in credits per the On-Page.ai `/install` page. **Time to ship:** 5 minutes to wire the key, 30 minutes to verify the skill comes online, 1 day to re-test on Veritas + GPC.

The `content-optimization` skill goes from `⏸️ dormant` to `✅ bound` in `_config/seo-skills.md` — one-line change.

## The OpenSEO skill stack (what we're packaging)

```
┌─────────────────────────────────────────────────────────────────────┐
│                  MERIDIAN — AI Local Growth Orchestrator            │
│           (new skill: orchestrator, sits ABOVE the 14-skill stack)  │
└─────────────────────────────────────────────────────────────────────┘
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        │                              │                              │
   Layer 5 — Outreach            Layer 4 — Score              Layer 3 — Enrich
   ───────────────────            ───────────────              ───────────────
   • local-seo          ✅         • site-audit        ✅        • content-       ⏸️→✅
     (GBP + Maps +                  • rank-tracking    ✅          optimization  ($1)
      reviews + Local              • serp-intelligence ✅         • keyword-library ✅
      SERP) — already                                                    │
      bound                                                             │
        │                              │                              │
        └──────────────┬───────────────┘                              │
                       ↓                                              │
                  Layer 2 — Discover (keyword universe)              │
                  ────────────────────────────────────                │
                  • keyword-research         ✅ bound                 │
                  • paa-demand-mining        ✅ bound (flagship)      │
                  • serp-intelligence        ✅ bound                 │
                  • domain-research          ✅ bound                 │
                       ↓                                              │
                  Layer 1 — Plan (HITL gate)                          │
                  ─────────────────────────                           │
                  • seo-enrichment-planner   ✅ bound (GATE)         │
                                                                       │
                       ↑                                              │
              Cross-cutting (work in any layer)  ←─────────────────────┘
              ──────────────────────────────────
              • openseo-project-intake (project setup)
              • openseo-data-export (DuckDB mirror)
```

Every existing skill stays. The new piece is the **Meridian orchestrator** that runs the 5-layer stack as a continuous monitor (cron-driven), not a one-shot audit.

## What changes in the OpenSEO codebase (minimal)

| Change | Type | File | Effort |
|--------|------|------|--------|
| Populate `ONPAGE_API_KEY` in container env | ops | `compose.yaml` env block | 5 min |
| Update `content-optimization` binding status | docs | `_config/seo-skills.md` | 1 min |
| Add `Meridian` skill to `~/.hermes/skills/local-growth/` (or `~/.hermes/skills/meridian/`) | new skill | `~/.hermes/skills/meridian/SKILL.md` | 1 day |
| Add Meridian orchestrator doc to OpenSEO wiki | docs | `clients/open-seo/_config/meridian-orchestrator.md` | 1 hour |
| Add Meridian to `_config/seo-skill-catalog.md` as Layer 6 (Orchestration) | docs | `_config/seo-skill-catalog.md` | 30 min |
| Build `_config/service-offering.md` (the public-facing product page) | docs | `clients/open-seo/_config/service-offering.md` | 2 hours |
| Add 4-tier pricing to sprint doc §11 | docs | `processes/seo-client-onboarding-sprint.md` | 30 min |

**Total engineering to ship v1: ~3-5 days** (assuming On-Page.ai key activated Day 1).

## The 4 product tiers (repackaging the existing stack)

### Tier 1 — Local Growth Audit (one-time)

**What the client gets:** one-shot 4-division run on their domain + GBP.

| Phase | OpenSEO skill used | Deliverable |
|-------|---------------------|-------------|
| Plan | `seo-enrichment-planner` | Cost + scope agreement (HITL) |
| Discover | `domain-research` + `local-seo` | Domain overview, GBP profile, local SERP |
| Enrich | `content-optimization` (deep scan) | 11-section eHarmony-format PDF (Recipe #9 equivalent) |
| Score | `site-audit` | Technical SEO issue list, severity-sorted |
| Outreach | `local-seo` | GBP review velocity + Maps pack rank report |

**Pricing:**
- $1.5K (single-location SMB, < 50 pages)
- $2.5K (multi-location or 50-200 pages)
- $3K+ (enterprise, 200+ pages, multi-region)

**What it costs us:** ~3-5 On-Page.ai deep scans + ~$1 OpenSEO calls + ~30 min Meridian orchestration. **Gross margin ~95%.**

### Tier 2 — Local Growth Foundation (one-time)

**Everything in Tier 1, plus:**
- Execute top 5 actions from the audit (via `content-optimization` Recipe #7 standard optimization on the 3 highest-priority pages, plus `local-seo` GBP field updates drafted)
- 1 round of content rewrites for the 3 highest-priority pages
- Schema JSON-LD additions (LocalBusiness, Service, FAQPage)
- AI SEO Module A (llms.txt + Organization schema + E-E-A-T author bios + bot-access audit — per the existing `seo-client-onboarding-sprint.md` §10)
- Re-scan + before/after delta report

**Pricing:**
- $3K (single-location SMB)
- $4.5K (multi-location / 50-200 pages)
- $6K (regional / 200-500 pages)
- $8K+ (enterprise / 500+ pages)

**What it costs us:** ~$10-15 in API calls + ~2-4 hours Meridian + ~1-2 hours Dennis review. **Gross margin ~75-85%.**

### Tier 3 — AI Local Growth Retainer ($1.5K-3K/mo, monthly recurring)

**What the client gets:**
- **Weekly Meridian cron** — pulls `local-seo`, `domain-research`, `rank-tracking` from OpenSEO MCP
- **Monthly On-Page.ai deep scan** — full site content audit, before/after delta vs prior month
- **Monthly SIB (Strategic Intelligence Brief)** — 1-page executive brief with the 3 numbers that matter: rank delta, review velocity, citation count
- **Exception alerts via Telegram/email** when something drops (rank -5+, negative review, GBP field missing)
- **1 content refresh / month** (Recipe #6 Light Page Refresh or Recipe #13 Image Alt-Text)
- **Quarterly strategic review call**

**What it costs us:** ~$5-10/mo in API + ~30 minutes Meridian + ~30 minutes Dennis. **Gross margin ~85-90% on the retainer.**

### Tier 4 — Local Growth Dominance ($3K-6K/mo, monthly recurring)

**Everything in Tier 3, plus:**
- Bi-weekly On-Page.ai deep scans (vs monthly)
- 2 content refreshes / month (Recipe #7 standard optimization)
- A/B test tracking for GBP posts + landing pages
- Local competitor monitoring (top 3, weekly delta via `get_local_serp_results`)
- Lead attribution from GBP calls + direction requests + website clicks
- Quarterly on-site strategy session with Dennis + client

## Pricing matrix (target client sizes)

| Client type | Tier 1 Audit | Tier 2 Foundation | Tier 3 Retainer | Tier 4 Dominance |
|-------------|--------------|--------------------|------------------|-------------------|
| Single-location SMB (1 city, < 50 pages) | $1.5K | $3K | $1.5K/mo | $3K/mo |
| Multi-location SMB (2-5 cities, 50-200 pages) | $2.5K | $4.5K | $2K/mo | $4K/mo |
| Regional operator (5-15 cities, 200-500 pages) | $3K | $6K | $2.5K/mo | $5K/mo |
| Enterprise / national (15+ cities, 500+ pages) | $4K+ | $8K+ | $3K/mo | $6K+/mo |
| Add-on: AI SEO Module A (one-time) | $3-5K | $5-8K | $5-8K | $5-8K |
| Add-on: AI SEO Module B (monthly) | — | — | $1.5K/mo | $1.5K/mo |

## Meridian — the new orchestrator (the only net-new code)

Meridian is a new skill that sits **above the 14-skill OpenSEO stack**. It does NOT replace any existing skill — it composes them.

### Subcommands (the slash-command surface)

| Command | Maps to | What it does |
|---------|---------|--------------|
| `/meridian portfolio` | All 14 skills, parallel | Cross-client health dashboard (Composite Visibility Score per client) |
| `/meridian client <slug>` | Layer 1 → Layer 5 walk | Full 5-layer run on one client, lands in `VALIDATION_QUEUE.md` |
| `/meridian monitor` | `local-seo` + `rank-tracking` only | Cron-driven exception-only check (default: every 30 min) |
| `/meridian opportunities` | `domain-research` + `local-seo` | Find SMBs with weak local + organic for outbound (LeadSniperAI hook) |
| `/meridian report <slug>` | Layer 5 (analytics-reporting + local-seo) | Monthly client growth report, 1-page SIB |
| `/meridian prospect <url>` | All 14 skills | New-prospect SIB + audit + cold email package |
| `/meridian revenue-hunt` | Cross-portfolio | Cross-client signal mining for expansion opportunities |

### How Meridian calls the existing skills

Meridian does NOT bypass the existing skill stack. It uses the same HITL gate:

1. Meridian calls `seo-enrichment-planner` first → cost estimate + scope agreement
2. Dennis (the human-in-the-loop) approves with "yes" / "no" / "adjust"
3. Meridian walks Layer 2 → Layer 5 using the existing skills
4. Each skill's output is added to the running SIB draft
5. SIB lands in `clients/<slug>/drafts/seo/STRATEGIC_INTELLIGENCE_BRIEF_<date>.md`
6. VALIDATION_QUEUE row appended
7. Telegram ping to Dennis

This means **Meridian inherits all of OpenSEO's audit trail, MCP wiring, and HITL gates for free**. The 4-division architecture I sketched in v1 of this draft is now implemented as a Meridian sub-skill that orchestrates the 14 existing skills rather than a parallel agent system.

## What this unlocks commercially (OpenSEO becomes the platform)

OpenSEO is currently a **technical/infra client** (the engagement is *building* OpenSEO itself). With the AI Local Growth Monitor packaged on top:

1. **OpenSEO stays the platform** — every KlickSmartAI SEO engagement runs through it
2. **The DuckDB mirror is the canonical store** — every retainer client gets their own `.local_tier/clients/<slug>.duckdb`
3. **The 14-skill stack stays the building blocks** — no skill retirement, no rewrite
4. **Meridian becomes the entry point** — clients see one name, not 14 skills
5. **The OpenSEO repo gets a public-facing surface** — `clients/open-seo/_config/service-offering.md` becomes the product page
6. **The On-Page.ai integration gets activated** — single env var change, all the dormant skill lights up
7. **GPC Development + Veritas become case studies** — both have working OpenSEO integrations already

## First customer candidate (unchanged)

**GPC Development** (existing client in our wiki):
- ✅ OpenSEO baseline already in place (audit `d07f8a86` complete, project `34afee19-d725-4073-b43f-1b76c6275c11`)
- ✅ DuckDB mirror pattern proven (`.local_tier/clients/gpc-development.duckdb`)
- ✅ Multi-location model — perfect test for Meridian's per-location logic
- ❌ `ONPAGE_API_KEY` not populated — would need to be activated before pilot

**Pilot sequence (revised, 2 weeks):**
- Day 1: Activate `ONPAGE_API_KEY` ($1), verify `content-optimization` skill comes online, run 3 test scans on GPC
- Day 2: Author Meridian skill (the orchestrator), bind to OpenSEO wiki
- Day 3: First full `/meridian client gpc-development` run — 5-layer walk
- Day 4: Build the SIB template + monthly report template
- Day 5: Hand off Tier 1 audit (free) to GPC owner as proof-of-concept
- Week 2: Iterate on SIB format, propose Tier 2 Foundation + Tier 3 Retainer

## Sprint doc integration (updated)

Add to `processes/seo-client-onboarding-sprint.md` §11:

```markdown
## §11. AI Local Growth Monitor (OpenSEO service packaging)

After completing §1-§10, offer the client the AI Local Growth Monitor retainer.
The product is built on top of OpenSEO's existing 14-skill stack — Meridian
is the orchestrator, not a separate agent system.

Default offering sequence:
1. Free Composite Visibility Score baseline (no commitment) — runs via Meridian
2. Tier 1 Audit if score < 60/100 — uses `content-optimization` deep scan
3. Tier 2 Foundation if they accept the audit — executes top 5 actions
4. Tier 3 Retainer after Foundation lands — weekly cron + monthly SIB
5. Tier 4 Dominance for clients with budget + multi-location ambition

**Prerequisite for all tiers:** OpenSEO deployed + On-Page.ai key active.
The Meridian skill + Composite Visibility Score dashboard must be in place
before any client engagement ships Tier 1.
```

## Composite Visibility Score (unchanged)

The single number a CFO can track:
- **OpenSEO organic health (via `domain-research`): 40%**
- **Local SEO Maps rank (via `local-seo`): 35%**
- **Review velocity (via `local-seo.get_business_reviews`): 15%**
- **Citation consistency (via `local-seo.search_local_businesses`): 10%**

Computed weekly by Meridian, written to DuckDB, surfaced in the SIB.

## HITL guarantees (per existing OpenSEO wiki rules)

Per `clients/open-seo/_config/seo-skill-catalog.md`:
- Every skill below Layer 1 presents a cost estimate + HITL approval before spend
- "yes" / "no" / "adjust" response is the gate — never auto-spend
- Per-client bindings override catalog defaults (Veritas: skip `paa-demand-mining`; GPC: skip `content-optimization` until key active)
- Module dormancy: if `ONPAGE_API_KEY` missing, `content-optimization` reports "module dormant"

Per `clients/open-seo/CLAUDE.md` (auto-generated adapter for Claude Code):
- AI-generated client content always lands in `drafts/` first
- No promotion from `drafts/` to `projects/` without Dennis's explicit approval
- No autonomous client sends

## Open questions (for Dennis)

1. **Brand name** — keep "AI Local Growth Monitor" or rename? "Meridian" is the orchestrator, the suite is OpenSEO
2. **First customer** — GPC Development as planned (requires On-Page.ai activation), or pick a different client?
3. **`ONPAGE_API_KEY`** — buy the $1 sign-up + $10 credits now? Or wait until a paying client?
4. **Pricing tiers** — does the table above feel right?
5. **Sales motion** — outbound (LeadSniperAI + cold email) or inbound (referrals from existing SEO clients like Veritas)?
6. **Meridian skill location** — `~/.hermes/skills/local-growth/` (existing draft) or `~/.hermes/skills/meridian/`? Or inside the OpenSEO repo at `clients/open-seo/skills/`?

## Source files referenced

- `clients/open-seo/IDENTITY.md` — OpenSEO platform identity (DataForSEO + Serper + On-Page.ai + Rank Tracker)
- `clients/open-seo/CONTEXT.md` — task routing table (DuckDB sync, PAA, MCP, deploy)
- `clients/open-seo/_config/seo-skill-catalog.md` — 14 skills, 5 layers, HITL gate
- `clients/open-seo/_config/seo-skills.md` — per-client binding rules
- `clients/open-seo/_config/conventions.md` — module dormancy + commit conventions
- `clients/open-seo/CLAUDE.md` — Hermes + Claude Code entry point
- `drafts/future-projects/meridian-local-seo-agent.md` — earlier Meridian draft (now folded into this offering)
- `drafts/future-projects/on-page-ai-seo-automation.md` — earlier On-Page.ai evaluation (resolved: activation only)
- `processes/seo-client-onboarding-sprint.md` §10-§11 — AI SEO Modules A+B + new AI Local Growth Monitor section
- https://api.on-page.ai/llms-full.txt — canonical API reference
- https://api.on-page.ai/compare/dataforseo — coexistence justification (DataForSEO + On-Page.ai = complementary, not competitive)

## Next steps

1. Dennis reviews this v2 draft + answers the 6 open questions
2. Activate `ONPAGE_API_KEY` ($1) → `content-optimization` skill comes online
3. Author Meridian skill (1 day) → orchestrator wires the 14 existing skills
4. Build public-facing service-offering page at `clients/open-seo/_config/service-offering.md`
5. Pilot on GPC Development (2 weeks)
6. Capture case study + open Tier 1 + Tier 2 to next 5 clients

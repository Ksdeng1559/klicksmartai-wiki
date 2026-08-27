---
title: "AI Local Growth Monitor" — KlickSmartAI service offering
created: 2026-08-27
updated: 2026-08-27
status: draft / service-offering
priority: high (commercial)
blocker: Localo MCP paid plan + On-Page.ai MCP install (low cost, ~$1 sign-up)
target client: SMBs with Google Business Profiles (contractors, dentists, attorneys, real estate, multi-location retail, home services)
deliverable: a sellable recurring service that runs on Meridian (the agent)
---

## TL;DR

**AI Local Growth Monitor** is the KlickSmartAI product line that combines three agent-grade data sources (Localo MCP for GBP / Maps / reviews, OpenSEO/DataForSEO for SERP / keywords / backlinks, On-Page.ai for on-page audits) behind a single 4-division agent (Meridian) that monitors, diagnoses, drafts, and reports on a client's local-search presence continuously — and never publishes anything without the client approving it through our existing HITL validation queue.

**Pricing model: $1.5K-6K setup + $1.5K-3K/mo retainer.** Margins are healthy because the underlying API costs are tiny (~$5-15/yr per active client) and the work is mostly agent-orchestrated, not human-time.

## Why now

We have all three data sources already authorized or evaluable:
- **Localo MCP** — needs payment, but the integration path is well-understood (same MCP-remote pattern as OpenSEO)
- **OpenSEO/DataForSEO MCP** — already wired in `~/.hermes/config.yaml` and proven on Veritas + GPC Development
- **On-Page.ai MCP** — $1 sign-up + $10 in credits to evaluate, async scan model, 23 recipe library, MCP-native

And the architectural pattern is confirmed by On-Page.ai themselves: **"Different layers of the SEO stack — most teams use both"** (their `/compare/dataforseo` page). They explicitly recommend running both tools in a coexistence workflow: DataForSEO for cohort + keyword research, On-Page.ai for the audit, then re-scan after edits. That's exactly what Meridian does.

## The three data sources

| Layer | Vendor | What it covers | What it costs us |
|-------|--------|----------------|------------------|
| **Local SEO + GBP** | Localo MCP | GBP fields, Maps 3-pack rank, reviews (count, velocity, sentiment), local-grid queries, citations | Per-client subscription (~$20-50/mo depending on plan) |
| **Broad SEO + SERP** | OpenSEO / DataForSEO MCP | Whole-domain audit, SERP rank tracking, keyword volumes, backlinks, on-page basic, PAA mining | Pay-per-call (~$0.01-0.50 per call depending on endpoint) |
| **On-page deep + entity** | On-Page.ai MCP | Page-1 cohort benchmark, entity coverage (100+ entities), internal-link candidates, schema gap, SERP-speed benchmark, 11-section PDF audit | Per-scan credits (1.5/2/3 per scan, ~$0.15-$0.30 per scan effective) |

**Combined per-client monthly API cost: ~$5-15.** That's the cost basis for the entire retainer tier.

## The Meridian agent (4 divisions)

```
       ┌─────────────────────────────────────────────────────────────┐
       │                  MERIDIAN — AI Local Growth Monitor         │
       └─────────────────────────────────────────────────────────────┘
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        │                              │                              │
   Division 1                   Division 2                     Division 3
   INTELLIGENCE                 STRATEGY                       EXECUTION
   ─────────────                 ─────────                      ─────────
   • Localo MCP pull             • Maps pack rank              • Refresh queue
   • OpenSEO MCP pull              gap analysis                   priorities
   • On-Page.ai scan             • GBP profile health          • Content briefs
   • DuckDB historical           • Review velocity +            • Citation list
     pattern lookup                sentiment                   • Schema additions
   • LeadSniper signal           • Citation NAP audit          • On-page fixes
   • Deepline enrichment         • Competitor cohort           • GBP field updates
                                   (15-page deep scan)            (drafts only)
                                 • "Near me" keyword           • AI citation audit
                                   cluster                       (Module A)
                                 • Maps-pack battle plan
        │                              │                              │
        └──────────────┬───────────────┘                              │
                       ↓                                              │
                  Division 4 — QUALITY                                │
                  ────────────────────                                │
                  • Before/after score                                │
                  • SIB (Strategic Intel Brief)                       │
                  • VALIDATION_QUEUE row                              │
                  • Approval gate (Dennis + client sign-off)          │
                       ↓                                              │
                  Published on approval  ←─────────────────────────────┘
```

Each division hands off a JSON payload to the next. HITL gates sit between Division 3 and Division 4 (no client-facing artifact leaves the system without a VALIDATION_QUEUE row + Dennis approval + client sign-off).

## Product tiers

### Tier 1 — Local Growth Audit (one-time, $1.5K-3K)

**What the client gets:**
- Full 4-division run on their domain + GBP
- 11-section PDF audit (eHarmony format via On-Page.ai Recipe #9)
- Composite Visibility Score (organic 40% + Maps 35% + reviews 15% + citations 10%)
- Priority ladder: top 5 actions ranked by impact × ease × cost
- SIB (1-page executive brief)
- 60-minute strategy call with KlickSmartAI

**What we charge:**
- $1.5K (single-location SMB, < 50 pages)
- $2.5K (multi-location or 50-200 pages)
- $3K+ (enterprise, 200+ pages, multi-region)

**What it costs us:** ~3-5 deep scans + 2 standard scans = ~15-20 credits On-Page.ai (~$2-3) + ~$1 OpenSEO calls + ~30 minutes Meridian run time. **Gross margin ~95%.**

### Tier 2 — Local Growth Foundation (one-time, $3K-6K)

**Everything in Tier 1, plus:**
- Execute the top 5 actions from the audit (Recipe #2 site-wide internal links, Recipe #7 standard optimization, Recipe #16 GBP alignment, citation NAP cleanup, schema additions)
- 1 round of content rewrites for the 3 highest-priority pages
- Schema JSON-LD additions (LocalBusiness, Service, FAQPage)
- AI SEO Module A (llms.txt + Organization schema + E-E-A-T author bios + bot-access audit)
- Re-scan + before/after delta report

**What it costs us:** ~$10-15 in API calls + ~2-4 hours Meridian + ~1-2 hours Dennis review + ~2-3 hours dev (only if client can't self-publish). **Gross margin ~75-85%.**

### Tier 3 — AI Local Growth Retainer ($1.5K-3K/mo, monthly recurring)

**What the client gets:**
- Weekly Meridian cron pull (Localo + OpenSEO + On-Page.ai deep scan monthly)
- Monthly SIB (1-page executive brief) with the 3 numbers that matter: rank delta, review velocity, citation count
- Exception alerts via Telegram/email when something drops (rank -5+, negative review, GBP field missing)
- 1 content refresh / month (Recipe #6 Light Page Refresh or Recipe #13 Image Alt-Text)
- Quarterly strategic review call

**What it costs us:** ~$5-10/mo in API + ~30 minutes Meridian + ~30 minutes Dennis + ~15 minutes client-success. **Gross margin ~85-90% on the retainer.**

### Tier 4 — Local Growth Dominance ($3K-6K/mo, monthly recurring)

**Everything in Tier 3, plus:**
- Bi-weekly deep scans (vs monthly)
- 2 content refreshes / month (Recipe #7 standard optimization)
- A/B test tracking for GBP posts + landing pages
- Local competitor monitoring (top 3, weekly delta)
- Lead attribution from GBP calls + direction requests + website clicks
- Quarterly on-site strategy session with Dennis + client

**What it costs us:** ~$15-25/mo in API + ~60 minutes Meridian + ~45 minutes Dennis. **Gross margin ~85% on the retainer.**

## Pricing table (target client sizes)

| Client type | Tier 1 Audit | Tier 2 Foundation | Tier 3 Retainer | Tier 4 Dominance |
|-------------|--------------|--------------------|------------------|-------------------|
| Single-location SMB (1 city, < 50 pages) | $1.5K | $3K | $1.5K/mo | $3K/mo |
| Multi-location SMB (2-5 cities, 50-200 pages) | $2.5K | $4.5K | $2K/mo | $4K/mo |
| Regional operator (5-15 cities, 200-500 pages) | $3K | $6K | $2.5K/mo | $5K/mo |
| Enterprise / national (15+ cities, 500+ pages) | $4K+ | $8K+ | $3K/mo | $6K+/mo |
| Add-on: AI SEO Module A (one-time) | $3-5K | $5-8K | $5-8K | $5-8K |
| Add-on: AI SEO Module B (monthly) | — | — | $1.5K/mo | $1.5K/mo |

## What makes this different

1. **The agent is the product.** Meridian never sleeps, monitors continuously, and catches the rank drops + negative reviews + GBP field changes the moment they happen — not at the next monthly check-in.
2. **Every artifact is grounded in evidence.** No "best practices" — every recommendation cites the specific scan that surfaced it.
3. **HITL gate is non-negotiable.** Meridian never publishes to GBP, never replies to a review, never sends outreach. Everything goes through the client's approval queue.
4. **Composite Visibility Score is one number a CFO can track.** Organic 40% + Maps 35% + reviews 15% + citations 10% — single metric, weekly cadence.
5. **All three data sources in one report.** The client doesn't need to know we run three vendors — they see one Meridian dashboard.

## First customer candidate

**GPC Development** (existing client in our wiki):
- ✅ Vancouver GC + multifamily, multi-page (21 pages audited)
- ✅ OpenSEO baseline already in place
- ✅ DuckDB mirror pattern proven
- ✅ Owner relationship established (Tak Ho / Zulliy Alnahas)
- ✅ Existing workspace with `_config/gtm-skills.md`
- ✅ Multi-location model (perfect test for Meridian's per-location logic)
- ❌ Localo MCP not yet paid — need to acquire before pilot

**Pilot sequence (3 weeks):**
- Week 1: Buy Localo MCP, install On-Page.ai MCP, build Meridian skill v1, run first `/meridian client gpc-development`
- Week 2: Build the SIB + monthly report template, validate against client expectations, run a Tier 1 audit for free as proof-of-concept
- Week 3: Hand off Tier 2 Foundation scope to GPC owners, propose Tier 3 retainer

## Implementation dependencies

| Dependency | Status | Cost to unblock |
|------------|--------|------------------|
| Localo MCP | ❌ Blocked on payment | Per-client subscription (~$20-50/mo) |
| OpenSEO MCP | ✅ Done | (already paid via DataForSEO) |
| On-Page.ai MCP | ⏳ Not installed | $1 sign-up + $10 in credits |
| Meridian skill | ❌ Not built | ~3-5 days |
| `_config/gtm-skills.md` binding | ❌ Not yet | ~1 hour per client |
| Sprint doc §11 update | ❌ Not yet | ~30 minutes |
| `seo-client-onboarding-sprint.md` integration | ❌ Not yet | ~2 hours |
| Sales collateral (1-page PDF, case study, deck) | ❌ Not yet | ~1 day |

**Total time to ship v1: ~1-2 weeks** (assuming Localo + On-Page.ai acquired within first 2 days).

## Sprint doc integration

Add to `processes/seo-client-onboarding-sprint.md` §11:

```markdown
## §11. AI Local Growth Monitor (optional retainer)

After completing §1-§10, offer the client the AI Local Growth Monitor retainer.
Lead with the audit-free Tier 3 path for clients who already did an audit; lead
with Tier 1 + Tier 2 for new prospects who want a phased approach.

Default offering sequence:
1. Free Composite Visibility Score baseline (no commitment)
2. Tier 1 Audit if score < 60/100
3. Tier 2 Foundation if they accept the audit
4. Tier 3 Retainer after Foundation lands
5. Tier 4 Dominance for clients with budget + multi-location ambition
```

## VALIDATION_QUEUE workflow (per client)

Every Meridian execution lands a row in `clients/<slug>/drafts/VALIDATION_QUEUE.md` with:
- Trigger (cron run / manual / event)
- Composite Visibility Score (current vs prior)
- Tier actions taken
- Drafts ready for review (linked)
- Decision options (approve / reject / escalate to client)

Client never sees raw API calls. They see one executive brief per month + exception alerts.

## Open questions (for Dennis)

1. **Brand name** — "AI Local Growth Monitor" vs "Meridian" vs "Local Pulse" vs something else?
2. **First customer** — pilot with GPC Development as planned, or pick a different client first to validate the model?
3. **Localo pricing** — what's the per-client subscription cost once we sign up? Need this for the margin math.
4. **Pricing tiers** — does the table above feel right? Should Tier 1 be free as a lead magnet?
5. **Sales motion** — outbound (LeadSniperAI + cold email) or inbound (wait for referrals from existing SEO clients)?

## Source files referenced

- `drafts/future-projects/meridian-local-seo-agent.md` — the agent architecture (4 divisions, 7 slash commands)
- `drafts/future-projects/on-page-ai-seo-automation.md` — the on-page deep-scan tier
- `processes/seo-client-onboarding-sprint.md` — where this slots into the existing client flow
- `processes/_config/gtm-skills.md` — per-client skill binding
- https://api.on-page.ai/llms-full.txt — canonical API reference
- https://api.on-page.ai/compare/dataforseo — coexistence workflow justification

## Next steps

1. Dennis reviews this draft + answers the 5 open questions
2. Acquire Localo MCP paid plan + On-Page.ai MCP sign-up
3. Build Meridian v1 (skill + 4-division orchestration)
4. Pilot on GPC Development
5. Capture case study + build sales collateral
6. Open Tier 1 + Tier 2 to next 5 clients

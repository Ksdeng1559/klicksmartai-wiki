---
title: Meridian — Local SEO Hermes Agent
created: 2026-08-27
updated: 2026-08-27
status: ready-to-build (was: deferred)
priority: high (commercial — gated on user green-light, not on missing tools)
blocker: none (Localo blocker cleared — DataForSEO local endpoints cover the same surface)
target-start: next green-light
target-effort: 3-5 days v1 build, then iterate
owner: Dennis
type: build-pending
tags: [local-seo, hermes-agent, ai-seo, geo, llmo, openseo, dataforseo, meridian, future-project]
related: [processes/seo-client-onboarding-sprint, clients/gpc-development, /home/denni/wiki/drafts/future-projects]
sources: [skills/agent-architecture-design, skills/ai-seo, skills/seo-client-onboarding-sprint]
---

# Meridian — Local SEO Hermes Agent

> **Status:** Ready to build. Was deferred on Localo MCP, but DataForSEO local endpoints already provide the GBP / Maps / Reviews / Local-grid surface (verified 2026-08-27). Build is gated on user green-light — not on missing tools.
> **Target:** Build v1 in 3-5 days after green-light. Pre-flight: confirm pricing tier on the bundle line item.
> **Pilot client:** GPC Development (Vancouver GC + multifamily).

## Why the blocker cleared

Earlier draft said Localo MCP (paid) was the required local-data source. The OpenSEO fork (50 MCP tools, live 2026-08-27) exposes DataForSEO's local endpoints — which cover the same GBP / Maps / Reviews / local-pack surface:

| Capability | Localo MCP | DataForSEO via OpenSEO fork |
|---|---|---|
| Google Business Profile data | ✅ | ✅ via `mcp__openseo__get_business_profile` |
| Business reviews | ✅ | ✅ via `mcp__openseo__get_business_reviews` |
| Local Pack rank grid | ✅ | ✅ via `mcp__openseo__get_local_rank_grid` |
| Local SERP results | ✅ | ✅ via `mcp__openseo__get_local_serp_results` |
| GBP questions | ❌/✅ | ✅ via `mcp__openseo__get_google_business_questions` |
| GBP updates | ✅ | ✅ via `mcp__openseo__get_business_updates` |
| Business search (NAP lookup) | ✅ | ✅ via `mcp__openseo__search_local_businesses` |
| Business categories | ✅ | ✅ via `mcp__openseo__list_business_categories` |

**Conclusion:** the Meridian wrapper can be built entirely on top of the existing OpenSEO fork stack. Localo can still be added later if its pricing makes sense, but it is no longer a blocker.

## Goal

Build **Meridian**, a Hermes agent that does continuous local SEO + Maps + GBP + review monitoring for clients, with a prospect-discovery mode that finds businesses losing local share while showing budget signals. The output is a sellable KlickSmartAI product line: **AI Local Growth Monitor**.

## Architecture (4-division pipeline per `agent-architecture-design`)

```
       ┌──────────────────────────────────────────────────┐
       │              MERIDIAN — Local SEO Agent         │
       └──────────────────────────────────────────────────┘
                          ↓
        ┌─────────────────┼─────────────────┐
        ↓                 ↓                 ↓
   Division 1        Division 2        Division 3
   INTELLIGENCE      STRATEGY          EXECUTION
   ─────────────     ─────────         ─────────
   • DataForSEO via • Maps pack gap   • Refresh queue
     OpenSEO MCP      analysis        • Content briefs
     (8 local        • GBP health    • Citation list
     tools)         • Review velocity • Schema additions
   • DuckDB           • Citation NAP   • GBP field drafts
   • LeadSniperAI       audit         • Review replies
   • Deepline        • "Near me"       • AI citation
                       keywords          (Module A)
                     • Competitor        deliverables
                       local-visibility
        ↓                 ↓                 ↓
        └─────────────────┼─────────────────┘
                          ↓
                  Division 4 — QUALITY
                  ────────────────────
                  • Before/after score
                  • SIB (Strategic Intel Brief)
                  • VALIDATION_QUEUE.md row
                  • Approval gate
                          ↓
                  Hermes publishes on Dennis approval
```

## Skill surface (slash commands)

| Command | Purpose |
|---------|---------|
| `/meridian portfolio` | All clients, combined DataForSEO (via OpenSEO fork) + OpenSEO health dashboard |
| `/meridian client <slug>` | Deep-dive on one client (full 4-division run) |
| `/meridian monitor` | Cron-style check, exception-only output (Telegram ping if something moves) |
| `/meridian opportunities` | Prospect mode — businesses with weak local + organic |
| `/meridian report <slug>` | Monthly client growth report (DataForSEO + OpenSEO combined) |
| `/meridian prospect <name>` | SIB + audit + cold email package for one business |
| `/meridian revenue-hunt` | Cross-portfolio signal mining for high-value prospects |

## Implementation steps (in build order)

| Step | What | Skill/system | Time |
|------|------|--------------|------|
| 1 | Confirm `DATAFORSEO_API_KEY` is wired into fork stack (verified 2026-08-27) | OpenSEO fork `.env` | done |
| 2 | Create `~/.hermes/skills/meridian/SKILL.md` (orchestrator skill that wraps 50 OpenSEO MCP tools) | Hermes skill | 1 day |
| 3 | Author 4 sub-agent specs in `meridian/agents/` (intelligence / strategy / execution / quality) | agent-architecture-design | 2 hours |
| 4 | Build `meridian-execution` hand-off JSON schema (canonical data contract between divisions) | data contracts | 1 hour |
| 5 | Wire DuckDB mirror view `v_local_organic_health` (DataForSEO via MCP + OpenSEO merged) | d1-to-duckdb-mirror pattern | 2 hours |
| 6 | Add `meridian-monitor` cron job (no_agent, every 30 min, exception-only) | hermes-cron-management | 1 hour |
| 7 | Build `/meridian portfolio` HTML dashboard (Chief-of-Staff briefing widget) | chief-of-staff-briefing | 2 hours |
| 8 | Pilot on GPC Development (Vancouver GC + multifamily) | existing workspace | 1 day |
| 9 | Add `meridian` to `_config/gtm-skills.md` binding for each client workspace | per-client config | 1 hour |
| 10 | Add "AI Local Growth Monitor" line item to `seo-client-onboarding-sprint.md` §11 | sprint process doc | 30 min |

**Total v1 build: ~3-5 days** — same estimate as before; the Localo-purchase wait was the difference between "blocked" and "ready to build."

## Data sources (final state)

| Layer | Tool | Status |
|-------|------|--------|
| Local Maps rank, GBP, reviews, citations | **DataForSEO via OpenSEO fork** (`get_business_profile` / `get_business_reviews` / `search_local_businesses` / `get_local_rank_grid` / `get_local_serp_results` / `get_google_business_questions` / `get_business_updates` / `list_business_categories`) | ✅ wired (8 local MCP tools live 2026-08-27) |
| Domain authority, backlinks, organic keywords, PAA, structured data | OpenSEO MCP | ✅ wired |
| Signal layer (hiring, ads, news, tech) | LeadSniperAI | ✅ wired |
| Decision-maker enrichment | Deepline | ✅ wired |
| Public intelligence | Agent Reach | ✅ wired |
| Cold email | Mystrika | ✅ wired |
| Calling | Telnyx | ✅ wired |
| Storage | Supabase + DuckDB | ✅ wired |
| HITL gate | drafts/ + VALIDATION_QUEUE.md + Telegram approval | ✅ wired |

## Pilot: GPC Development (Vancouver)

GPC is the ideal first customer:
- ✅ OpenSEO baseline already in place (clean access, audit done, scorecard built)
- ✅ Vancouver market — high-value local SEO vertical
- ✅ Existing workspace with `_config/gtm-skills.md` ready to extend
- ✅ DuckDB mirror pattern proven
- ✅ Multi-location model — tests Meridian's per-location strategy logic

Pilot sequence after green-light:
1. Day 1: Create Meridian skill (`~/.hermes/skills/meridian/`), wire to OpenSEO fork (50 MCP tools), point at GPC
2. Day 2: First full `/meridian client gpc-development` run — 4-division output
3. Day 3: Build the SIB + monthly report template from the run
4. Day 4: Add `meridian-monitor` cron (every 30 min, exception-only)
5. Day 5: Hand off to GPC owner with bundled offer

## Commercial product line (priced)

| Product | Module | Pricing |
|---------|--------|---------|
| Local Growth Audit (one-time) | Full 4-division run, SIB delivered | $3-5K |
| Local Growth Retainer (monthly) | Meridian portfolio + monitor + monthly report | $1.5-3K/mo |
| AI SEO Foundation (existing) | Module A from sprint doc | $3-15K |
| AI Visibility Retainer (existing) | Module B from sprint doc | $1.5-3K/mo |
| **Combined: Local Growth + AI SEO Foundation** | Meridian + Module A as bundle | $5-18K |
| **Combined: Full-stack Local Growth + AI + Organic** | Meridian + Module A + Module B + Phase 1-4 core SEO | $8-25K + monthly |

The combined package is the agency-killer offering — one agent, full-stack monitoring, executive reporting, AI citation, organic SEO, local Maps growth.

## HITL guarantees

| Action | Autonomous? | Reason |
|--------|------------|--------|
| DataForSEO local data pull | ✅ yes | Read-only |
| OpenSEO data pull | ✅ yes | Read-only |
| LeadSniperAI signal check | ✅ yes | Read-only |
| Strategy generation | ✅ yes | Internal |
| Draft any client artifact | ✅ yes | Lands in `drafts/` |
| Post to GBP | ❌ NEVER | Google ToS policy safety (drafts only) |
| Reply to review | ❌ NEVER | Drafted only, Dennis approves |
| Send cold email | ❌ NEVER | Mystrika + Dennis approval |
| Update client website | ❌ NEVER | Dev hand-off via draft |
| Add row to VALIDATION_QUEUE | ✅ yes | Internal notification |
| Telegram ping to Dennis | ✅ yes | Chief-of-Staff surface |

## Self-maintenance (Hermes v0.12 curator)

Meridian is a living skill. The v0.12 curator:
- Grades Meridian's output quality over time
- Prunes stale sub-commands
- Auto-consolidates overlapping skills (e.g., a future `local-seo-prospector` would merge in)
- Downgrades trust score if gate checks start failing

So the skill **improves itself** between sessions without manual curation.

## Pre-build checklist (before starting)

1. Confirm `DATAFORSEO_API_KEY` is in `~/.hermes/secrets/` and `OPEN_SEO_IMAGE=open-seo:local` is set in `/tmp/open-seo-lanpubs/.env` — both verified 2026-08-27
2. Confirm pilot client `gpc-development` workspace is intact (run `~/.hermes/scripts/regenerate-project-settings.py gpc-development` if uncertain)
3. Decide on bundle pricing before Step 8 (see Q4)
4. Run `python ~/.hermes/skills/seo/audit-to-recommendations/scripts/build_recommendations.py` against the current GPC audit (paid run, ~$3, ~30 min) to populate the recommendations machine-learning corpus
5. Proceed with Step 1-10 above

## Related artifacts

- `/home/denni/wiki/processes/seo-client-onboarding-sprint.md` §10 (AI SEO add-on modules)
- `/home/denni/wiki/clients/gpc-development/CLAUDE.md` (pilot workspace)
- `/home/denni/wiki/clients/gpc-development/drafts-preview/seo/audit-1page-2026-08-26-gpc-development.html` (current baseline)
- `~/.hermes/skills/agent-architecture-design/SKILL.md` (Division-based design pattern)
- `~/.hermes/skills/ai-seo/SKILL.md` (Module A + B specs)
- Memory: OpenSEO wired + paid credits verified (2026-08-26)

## Open questions

1. ~~**Localo pricing tier** — which plan gives the MCP endpoint access? (need to confirm before buying)~~ — RESOLVED 2026-08-27: Localo not needed; DataForSEO via OpenSEO fork covers the surface.
2. **DataForSEO rate limits** — does the OpenSEO fork throttle per client per minute, or per workspace? (verify before building Step 6 cron)
3. **Review response policy** — even drafted replies need a Google ToS review. Add a "ToS pre-check" to Division 4?
4. **Pricing the bundle** — what's the right number for a Vancouver SMB full-stack engagement? Test on GPC's first quote.

---

*This is a build-pending draft. The original Localo blocker is cleared (2026-08-27); build is gated on user green-light. Re-validate the architecture against `agent-architecture-design` when starting — Hermes v0.12+ curator may have evolved the skill conventions since this was drafted.*

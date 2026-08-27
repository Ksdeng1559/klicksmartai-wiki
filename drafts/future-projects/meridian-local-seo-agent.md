---
title: Meridian — Local SEO Hermes Agent (deferred until Localo MCP purchased)
created: 2026-08-27
updated: 2026-08-27
status: future-project
priority: medium
blocker: requires Localo MCP paid plan
target-start: TBD (after Localo MCP purchased + endpoint available)
target-effort: 3-5 days v1 build, then iterate
owner: Dennis
type: future-build
tags: [local-seo, hermes-agent, ai-seo, geo, llmo, openseo, localo, meridian, future-project]
related: [processes/seo-client-onboarding-sprint, clients/gpc-development, /home/denni/wiki/drafts/future-projects]
sources: [skills/agent-architecture-design, skills/ai-seo, skills/seo-client-onboarding-sprint]
---

# Meridian — Local SEO Hermes Agent

> **Status:** Deferred. Blocked on Localo MCP paid plan purchase.
> **Target:** Build v1 in 3-5 days after Localo MCP is available.
> **Pilot client:** GPC Development (Vancouver GC + multifamily).

## Why defer

- Localo MCP is the primary data source for GBP / Maps / Reviews / Local-grid intelligence.
- Localo exposes its MCP only on paid plans — endpoint not accessible without subscription.
- All other components (OpenSEO, LeadSniperAI, Deepline, Mystrika, Telnyx, Hermes skill system, DuckDB mirror) are already wired.
- No value building the wrapper skill without the underlying MCP — Meridian is a thin orchestrator on top of Localo + OpenSEO.

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
   • Localo MCP      • Maps pack gap   • Refresh queue
   • OpenSEO MCP       analysis        • Content briefs
   • DuckDB          • GBP health      • Citation list
   • LeadSniperAI    • Review velocity • Schema additions
   • Deepline        • Citation NAP    • GBP field drafts
                       audit           • Review replies
                     • "Near me"       • AI citation
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
| `/meridian portfolio` | All clients, combined Localo + OpenSEO health dashboard |
| `/meridian client <slug>` | Deep-dive on one client (full 4-division run) |
| `/meridian monitor` | Cron-style check, exception-only output (Telegram ping if something moves) |
| `/meridian opportunities` | Prospect mode — businesses with weak local + organic |
| `/meridian report <slug>` | Monthly client growth report (Localo + OpenSEO combined) |
| `/meridian prospect <name>` | SIB + audit + cold email package for one business |
| `/meridian revenue-hunt` | Cross-portfolio signal mining for high-value prospects |

## Implementation steps (in build order)

| Step | What | Skill/system | Time |
|------|------|--------------|------|
| 1 | Install Localo MCP in `~/.hermes/config.yaml` (need endpoint URL from paid plan) | Hermes MCP infrastructure | 30 min |
| 2 | Create `~/.hermes/skills/local-growth/SKILL.md` (skill wrapper) | Hermes skill | 1 hour |
| 3 | Author 4 sub-agent specs in `local-growth/agents/` | agent-architecture-design | 2 hours |
| 4 | Build `meridian-execution` hand-off JSON schema | data contracts | 1 hour |
| 5 | Wire DuckDB mirror view `v_local_organic_health` (Localo + OpenSEO merged) | d1-to-duckdb-mirror pattern | 2 hours |
| 6 | Add `meridian-monitor` cron job (no_agent, every 30 min, exception-only) | hermes-cron-management | 1 hour |
| 7 | Build `/meridian portfolio` HTML dashboard (Chief-of-Staff briefing widget) | chief-of-staff-briefing | 2 hours |
| 8 | Pilot on GPC Development (Vancouver GC + multifamily) | existing workspace | 1 day |
| 9 | Add `meridian` to `_config/gtm-skills.md` binding for each client workspace | per-client config | 1 hour |
| 10 | Add "AI Local Growth Monitor" line item to `seo-client-onboarding-sprint.md` §11 | sprint process doc | 30 min |

**Total v1 build: ~3-5 days**

## Data sources (final state)

| Layer | Tool | Status |
|-------|------|--------|
| Local Maps rank, GBP, reviews | **Localo MCP** | ❌ blocked on purchase |
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

Pilot sequence after Localo is wired:
1. Day 1: Install Localo MCP, create Meridian skill, point at GPC
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
| Localo data pull | ✅ yes | Read-only |
| OpenSEO data pull | ✅ yes | Read-only |
| LeadSniperAI signal check | ✅ yes | Read-only |
| Strategy generation | ✅ yes | Internal |
| Draft any client artifact | ✅ yes | Lands in `drafts/` |
| Post to GBP | ❌ NEVER | Localo doesn't allow anyway (policy safety) |
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

## What to do when Localo MCP is purchased

1. Get the Localo MCP endpoint URL (their docs page on the Localo site)
2. Wire it into `~/.hermes/config.yaml` (same MCP-remote pattern as OpenSEO)
3. Verify with `mcp__localo__whoami` equivalent
4. Run Step 1-10 above in order
5. Pilot on GPC Development
6. Iterate based on first 3-5 client runs

## Related artifacts

- `/home/denni/wiki/processes/seo-client-onboarding-sprint.md` §10 (AI SEO add-on modules)
- `/home/denni/wiki/clients/gpc-development/CLAUDE.md` (pilot workspace)
- `/home/denni/wiki/clients/gpc-development/drafts-preview/seo/audit-1page-2026-08-26-gpc-development.html` (current baseline)
- `~/.hermes/skills/agent-architecture-design/SKILL.md` (Division-based design pattern)
- `~/.hermes/skills/ai-seo/SKILL.md` (Module A + B specs)
- Memory: OpenSEO wired + paid credits verified (2026-08-26)

## Open questions

1. **Localo pricing tier** — which plan gives the MCP endpoint access? (need to confirm before buying)
2. **Multi-location rate limits** — does Localo MCP throttle per client per minute, or per workspace?
3. **Review response policy** — even drafted replies need a Google ToS review. Add a "ToS pre-check" to Division 4?
4. **Pricing the bundle** — what's the right number for a Vancouver SMB full-stack engagement? Test on GPC's first quote.

---

*This is a deferred-build draft. Do not start until Localo MCP endpoint is available. Re-validate the architecture against `agent-architecture-design` when starting — Hermes v0.12+ curator may have evolved the skill conventions since this was drafted.*

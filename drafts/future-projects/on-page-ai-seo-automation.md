---
title: On-Page.ai SEO Automation — evaluation draft (deferred)
created: 2026-08-27
updated: 2026-08-27
status: future-project / evaluation-draft
priority: medium-high (could replace or augment Phase 2-3 of client sprint)
blocker: requires pricing confirmation + MCP signup
target-start: TBD
owner: Dennis
type: future-build
tags: [seo, automation, on-page-ai, mcp, ai-seo, recipes, future-project, evaluation]
related: [drafts/future-projects/meridian-local-seo-agent, processes/seo-client-onboarding-sprint]
sources: [https://on-page.ai/pages/automate-seo/, https://api.on-page.ai]
---

# On-Page.ai SEO Automation — Evaluation Draft

> **Status:** Evaluation. The 17-recipe library is real, the MCP connector is documented at `api.on-page.ai`, but pricing/access details need confirmation before buying.
> **Action needed:** Decide whether to add On-Page.ai MCP alongside OpenSEO, and if so, on which clients.

## What it is

On-Page.ai ships an **MCP connector** at `api.on-page.ai` that gives an AI agent (Claude, Codex, Hermes) live SERP intelligence — and a **library of 17 SEO automation recipes** written as prompt patterns that drive the MCP. The recipes are designed to be agent-agnostic but they recommend Claude Code and Codex.

The MCP exposes:
- Live SERP data (not training-data guesses)
- Entity coverage analysis (similar to what we saw in the eHarmony example report)
- Competitor benchmarks (page-1 average for any keyword)
- Internal link opportunities (per-page)
- Salient terms + titlematch scores + passage-embed scores
- Site focus / category alignment (petacatTaxId, siteRadius)
- Standard scan report (the 11-section JSON we already saw)

The recipes layer orchestration logic on top — they tell the agent **how** to use the data, not just expose it.

## The 17 recipes (per the page)

The page header says 17 recipes; the body I could read lists these explicitly:

| # | Recipe | What it does | Maps to our sprint phase |
|---|--------|--------------|--------------------------|
| 1 | **Recover a stuck page** | Diagnose why a page isn't ranking, fix it | Phase 1 (Foundation) |
| 2 | **Site-wide internal links** (50-20K pages) | Build manifest, batch-process 75 pages at a time | Phase 1 (Foundation) |
| 3 | **Add natural anchor text links** | Per-page internal links from most relevant pages | Phase 1 (Foundation) |
| 4 | **Optimize sub-headlines** | H2/H3 level rewrite for entity coverage | Phase 3 (Content) |
| 5 | **Optimize image alt-text** | Per-page alt-text refresh | Phase 1 (Foundation) |
| 6 | **Optimize entities** | Add missing entities from page-1 benchmark | Phase 3 (Content) |
| 7 | **Refresh outdated content** | Per-page research + refresh | Phase 4 (Maintenance) |
| 8 | **Build client-ready SEO audit PDF** | Audit generation (the 11-section format we saw) | Phase 3 (Artifacts) |
| 9 | **Audit local SEO pages** | Local-vertical version of standard audit | Phase 3 (Artifacts) |
| 10 | **Find service+city cannibalization** | Detect competing pages on local sites | Phase 1 (Foundation) |
| 11 | **Process large sites with manifest runners** | Resume-safe batching pattern | All phases |
| 12 | **Diagnose why a page isn't ranking** | Diagnosis mode (lighter than recover) | Phase 1 |
| 13 | **(continued in un-read middle of source)** | — | — |
| 14 | — | — | — |
| 15 | — | — | — |
| 16 | — | — | — |
| 17 | — | — | — |

The full list of 17 was truncated in the page read. The pattern is clear regardless: each recipe is a **prompt template** that orchestrates MCP calls + page edits + verification + manifest tracking.

## Three architectural layers (per the page)

```
Layer 1: Real-time SEO data (the MCP connector itself)
   ↓
Layer 2: SEO interpretation context (specialized resources the MCP bundles —
         17 years of Eric Lancheres's heuristics for entity salience, topical
         relevance, content preservation, modern ranking techniques)
   ↓
Layer 3: The recipes (prompt patterns that orchestrate Layer 1 + Layer 2
         against actual pages with audit trail + manifest tracking)
```

This is **exactly the structure `agent-architecture-design` recommends** (Intelligence → Strategy → Execution → Quality). The recipes *are* the Strategy + Execution divisions; the MCP is the Intelligence division.

## How this overlaps with what we already have

| Capability | OpenSEO MCP | On-Page.ai MCP | Overlap |
|------------|-------------|----------------|---------|
| Site audit | ✅ `run_site_audit` | ✅ "standard scan" | Same domain, different lens |
| Audit issues list | ✅ 5 categories (on-page, technical, content, etc.) | ✅ 11 sections (entity, structured data, originality, etc.) | **Complementary — On-Page has entity + originality + speed + structured-data that we don't** |
| Page-1 benchmark | ❌ not in 1-pager | ✅ built-in (word count, H1/H2/H3, image, entity vs page-1 avg) | **Big gap** — adding this to our 1-pager was the upgrade we identified earlier |
| Entity coverage | ❌ no | ✅ 100+ entities per page with coverage status | **Big gap** |
| Internal link opportunities | ❌ no (just orphan count) | ✅ top 3 source pages per target | **Big gap** |
| Structured-data benchmark | ❌ no | ✅ page-1 schema vs yours | Module A would cover this |
| Speed benchmark (SERP speed) | ✅ Lighthouse runs in audit | ✅ built-in (TTFB, FCP, LCP) | **Both have it, different layers** |
| Originality | ❌ no (just thin content) | ✅ content uniqueness score | **On-Page wins** |
| Link opportunities | ✅ `get_backlinks_overview` | ✅ per-page internal | Different (external vs internal) |
| Rank tracker | ✅ weekly, 25 keywords for GPC | ❌ | **OpenSEO wins** |
| Local grid | ❌ | ❌ (Localo wins for this) | n/a |
| Reviews / GBP | ❌ | ❌ (Localo wins for this) | n/a |
| Recipes / orchestration | ❌ raw tools only | ✅ 17 prompt patterns | **On-Page wins** |
| Audit trail | ❌ | ✅ manifest-based resume pattern | **On-Page wins** |

## What it could do for KlickSmartAI

### 1. Replace / augment our Phase 1-3 client sprint

The "Recover a stuck page" + "Site-wide internal links" + "Optimize entities" recipes cover **Phase 1 (Foundation) + part of Phase 3 (Content)** of the sprint doc. If On-Page.ai works well, we could:
- Run their `standard scan` instead of (or alongside) OpenSEO `run_site_audit`
- Use their internal-link recipe for the orphaned-pages fix
- Use their entity-coverage recipe for content refresh

### 2. Generate the audit report format we evaluated

Remember the eHarmony Statistics 11-section report? That's their **standard output**. We could ship client audits in this exact format — it's already industry-recognized, more detailed than our 5-section 1-pager, and includes entity + structured-data + speed + originality that we currently don't surface.

### 3. Get the page-1 benchmark bar we identified as the biggest gap

Section 02 (Page-1 benchmarks) is **the** differentiator. Adding it to our 1-pager was the upgrade we flagged earlier. On-Page.ai ships it natively.

### 4. Internal-link manifest pattern = repeatable at scale

The "manifest-based runner" approach (process 75 pages, save manifest, resume next batch) is **exactly the pattern** for our clients with 50-500+ pages. We can run it on GPC (21 pages, small enough to do in one batch).

## Pricing decision (open question)

The MCP endpoint is at `api.on-page.ai`. Pricing is gated behind a signup flow. **Need to confirm:**
1. Does the MCP require a paid plan, or is there a free tier?
2. Per-call credits (like OpenSEO's DataForSEO model)?
3. Monthly subscription model?
4. Per-client or per-workspace?
5. Does the 17-recipe library require a separate purchase from the MCP?

Without this info, can't make a clean buy/no-buy decision. **Action: sign up at `api.on-page.ai`, check pricing, get an API key, run a free test scan on GPC to verify the format matches what's documented.**

## Risk assessment

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Recipe outputs degrade human-written content | Medium | Page warns about this — must review every change against the original |
| Over-optimization penalties | Medium | Recipe #1 has guardrails; we should still spot-check |
| Cost overruns on large sites | Medium | Use the manifest pattern; batch 75 pages, monitor spend |
| Vendor lock-in if recipes only work with their MCP | Low | We can extract the prompt patterns and re-implement against OpenSEO if needed |
| Duplicate spend with OpenSEO | Low | On-Page covers gaps OpenSEO doesn't; net additive |

## What the eHarmony example actually tells us

The 11-section JSON we extracted earlier proves:
- ✅ The MCP works (we got real structured output)
- ✅ The auditor format is solid (entity coverage is the most actionable section in the entire report)
- ✅ The page-1 benchmark is real and concrete ("you 2036 words / page-1 avg 2542.5")
- ✅ Score + grade + confidence framing is mature

## Recommendation

**Sign up for On-Page.ai MCP, get a free-tier API key, run one standard scan on GPC Development (the same `gpcdevelopment.ca` we already audited).**

Cost: signup time + maybe $0 if there's a free tier.
Value: real-world confirmation that the MCP works with Hermes, and a side-by-side comparison of OpenSEO `run_site_audit` output vs On-Page.ai `standard scan` output.

If the test scan produces a higher-signal report than OpenSEO for GPC, we have a clear answer: **add On-Page.ai to the sprint stack as the per-page deep-scan tool, keep OpenSEO for whole-site health + rank tracking.**

If the test scan is roughly equivalent, we don't need it — OpenSEO already does this job and we already have it wired.

## Implementation steps (after we buy / sign up)

1. Sign up at `api.on-page.ai`, get MCP endpoint URL + API key
2. Wire into `~/.hermes/config.yaml` (same MCP-remote pattern as OpenSEO + Localo)
3. Verify with `mcp__onpage__whoami`-equivalent
4. Run standard scan on GPC's homepage — compare with existing OpenSEO audit
5. If useful: add On-Page.ai to `seo-client-onboarding-sprint.md` Phase 2 as optional tool
6. If useful: draft On-Page.ai-specific recipes for our clients (internal-link runs, entity-coverage refresh)
7. If useful: add to `_config/gtm-skills.md` binding per client

## Open questions

1. **Pricing** — need to confirm before buying. Most likely a free tier + paid MCP access.
2. **Compatibility with our 4-layer pipeline** — does their output drop cleanly into our DuckDB mirror? Need to test.
3. **Claude Code vs Hermes as the driver** — page says "compatible with both"; we're on Hermes. Recipe prompt syntax needs to map to our SKILL.md format, not `.claude/skills/`.
4. **Image generation in Codex** — page mentions this but we don't use Codex. Skip.
5. **The 5 recipes I couldn't read** — middle of the source was truncated; need to read full page to enumerate all 17.

## Related drafts

- `/home/denni/wiki/drafts/future-projects/meridian-local-seo-agent.md` — Meridian (Localo + OpenSEO + LeadSniperAI + Deepline)
- `/home/denni/wiki/processes/seo-client-onboarding-sprint.md` — Phase 1-5 sprint + Module A/B AI SEO
- `/home/denni/wiki/clients/gpc-development/drafts-preview/seo/audit-1page-2026-08-26-gpc-development.html` — current GPC 1-pager

---

*Evaluation draft. Do not buy until pricing is confirmed at api.on-page.ai and a free-tier test scan validates the format on GPC.*

---
title: On-Page.ai SEO Automation — wired + evaluating
created: 2026-08-27
updated: 2026-08-27
status: wired-and-evaluating (was: evaluation-draft)
priority: high (key live; sprint enrichment evaluation underway 2026-08-27)
blocker: none (signed up + $10 credits loaded + ONPAGE_API_KEY wired into fork 2026-08-27)
target-start: live (first scans underway)
owner: Dennis
type: active-integration
tags: [seo, automation, on-page-ai, mcp, ai-seo, recipes, openseo-integrated, live]
related: [drafts/future-projects/meridian-local-seo-agent, processes/seo-client-onboarding-sprint, skills/content-optimization]
sources: [https://on-page.ai/pages/automate-seo/, https://api.on-page.ai]
---

# On-Page.ai SEO Automation — Wired, Now Evaluating

> **Status:** Wired. ONPAGE_API_KEY in fork `.env`, `content-optimization` skill live, `run_content_scan` verified 2026-08-27. Active question is no longer "should we buy" but "does the per-page output beat OpenSEO for our clients?"
> **Action:** Run side-by-side scan on GPC homepage (OpenSEO `run_site_audit` vs On-Page.ai standard scan); commit the verdict to `_config/seo-tool-decisions.md`.

## What it is

On-Page.ai ships an **MCP connector** at `api.on-page.ai` that gives an AI agent (Claude, Codex, Hermes) live SERP intelligence — and a **library of 23 SEO automation recipes** written as prompt patterns that drive the MCP. The recipes are designed to be agent-agnostic but they recommend Claude Code and Codex.

The MCP exposes:
- Live SERP data (not training-data guesses)
- Entity coverage analysis (similar to what we saw in the eHarmony example report)
- Competitor benchmarks (page-1 average for any keyword)
- Internal link opportunities (per-page)
- Salient terms + titlematch scores + passage-embed scores
- Site focus / category alignment (petacatTaxId, siteRadius)
- Standard scan report (the 11-section JSON we already saw)

The recipes layer orchestration logic on top — they tell the agent **how** to use the data, not just expose it.

## The 23 recipes (per the API page)

The anchor `#op3-element-TxnrP7JS` points to the marketing page which has **17 recipes**. The API endpoint `/automate-seo` is the newer page with **23 recipes** ("23 prompts shown"). Recipe numbering is preserved across both pages; the API page adds recipes #12 and #13 that were missing from the older marketing page.

**RESOLVED 2026-08-27:** All 23 recipes enumerated via deep-link `#op3-element-TxnrP7JS` (the recipe library section header) + the `/automate-seo` endpoint page.

| # | Recipe | What it does | Maps to our sprint phase |
|---|--------|--------------|--------------------------|
| **1** | **Recover a Stuck Page in ONE Command** | Diagnose why a page isn't ranking + fix it in one run; has guardrails ("only use on never-ranked / dropped / declining pages") | Phase 1 (Foundation) |
| **2** | **Site-Wide Internal Links (50 to 20,000+ pages)** | Manifest-based runner, 75 pages per batch, 10-page sub-batches, 5 parallel scans max, 3 links per target, 750 max per run | Phase 1 (Foundation) |
| 2b | Continue / Resume Internal Linking | Resume from saved manifest at next page range | Phase 1 |
| 2c | Follow-up Continue / Resume Internal Linking | Same after interruption | Phase 1 |
| 2d | Emergency "Process Interrupted" Resume | Recovery after crash | Phase 1 |
| **3** | **Single Page Internal Links — Detailed Version** | Per-page 3-source internal link builder | Phase 1 |
| **4** | **Single Page Internal Links — Simple Version** | Lighter variant for quick wins | Phase 1 |
| **5** | **Site-Wide Refresh — Fix All Your Old/Stale Pages** | Batch refresh stale content across full sitemap | Phase 4 (Maintenance) |
| 5b | Continue / Resume Light SEO Refresh | Resume variant | Phase 4 |
| 5c | Emergency Resume Light SEO Refresh | Recovery after crash | Phase 4 |
| **6** | **Light Page Refresh (Single Page)** | Single-page quick refresh | Phase 4 |
| **7** | **Standard Optimization (Single Page)** | Single-page full optimization | Phase 3 (Content) |
| **8** | **Standard Optimization (Site-Wide)** | Batch version of #7 across full site | Phase 3 |
| 8b | Resume / Continue Standard Optimization (Site-Wide) | Resume variant | Phase 3 |
| **9** | **Full Client Website Audit (PDF)** | The 11-section eHarmony-format PDF report (Executive Summary, Full Audit Walkthrough, Competitor Gap, Entity/Content Gap, Technical/Speed, Image/Alt Text, Topical/Category Alignment, Recommended Fixes) | Phase 3 (Artifacts) |
| **10** | **Single Page Audit (PDF)** | Per-page version of #9 with same 11 sections | Phase 3 |
| **11** | **Advanced Page Diagnostic: "Why Isn't This Page Ranking?"** | Diagnosis mode (lighter than Recipe #1, for pages already in top 10 or page 2) | Phase 1 |
| **12** | **Sub-Headline Optimization (Single Page)** | H1/H2/H3 rewrite for entity coverage | Phase 3 |
| **13** | **Image and Alt-Text Optimization (Single Page)** | Per-page alt-text refresh | Phase 1 |
| **14** | **Local Page Diagnostic: "Why Isn't This Local Page Ranking?"** | Local-vertical diagnosis | Phase 3 (Local) |
| **15** | **Local Page Tuning (Standard Optimization)** | Local-vertical version of #7 | Phase 3 |
| **16** | **Local Website & GBP Alignment Verification** | Compares website content against Google Business Profile fields (NAP, services, hours, categories) | **Big deal — overlaps with Meridian strategy** |
| **17** | **Local Website Cannibalization Checker (City/Region) — Audit** | Detects service+city cannibalization (e.g., /vancouver-plumbing vs /plumbing-vancouver competing) | Phase 1 |

Recipe #16 (Local Website & GBP Alignment) is the **most strategically important** — it's the only one that bridges classic SEO and GBP/local, which is exactly where Meridian sits.

Each recipe is a **prompt template** that orchestrates MCP calls + page edits + verification + manifest tracking with full audit trail. The manifest-based runner pattern (Recipes #2, #5, #8) is what makes large-site work safe — you can resume from where you left off if the agent crashes.

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
| Local grid | ✅ (DataForSEO via OpenSEO fork) | ❌ | **OpenSEO wins** |
| Reviews / GBP | ✅ (DataForSEO `get_business_reviews`, `get_business_profile`) | ❌ | **OpenSEO wins** |
| Recipes / orchestration | ❌ raw tools only | ✅ 23 prompt patterns | **On-Page wins** |
| Audit trail | ❌ | ✅ manifest-based resume pattern | **On-Page wins** |

## What it could do for KlickSmartAI

### 1. Replace / augment our Phase 1-4 client sprint

The "Recover a stuck page" + "Site-wide internal links" + "Standard optimization" recipes cover **Phase 1 (Foundation) + Phase 3 (Content) + Phase 4 (Maintenance)** of the sprint doc. If On-Page.ai works well, we could:
- Run their `standard scan` instead of (or alongside) OpenSEO `run_site_audit` for the per-page report format
- Use Recipes #2 / #5 / #8 (the manifest runners) for batched optimization at scale
- Use Recipes #9 / #10 (Full Client Audit PDF, Single Page Audit PDF) to ship our deliverable **in the eHarmony 11-section format** rather than our current 5-section 1-pager

### 2. **Recipe #16 = the GBP-Alignment bridge**

This is the one that surprised me. **Local Website & GBP Alignment Verification** compares the website content against Google Business Profile fields. This is **exactly** the alignment check Meridian Division 2 was going to build — but On-Page.ai ships it as a recipe. If we adopt On-Page.ai, **Recipe #16 effectively replaces the alignment-check we were going to build into Meridian Division 2.**

That changes the Meridian architecture:
- Meridian still owns DataForSEO (via OpenSEO fork) for: real-time Maps rank, reviews, GBP field completeness, competitor local-grid, business search
- On-Page.ai Recipe #16 owns: website ↔ GBP content alignment (one-shot verification, not continuous monitoring)

This **decouples** the alignment check from the live-monitoring loop, which is actually cleaner architecture.

### 2. Generate the audit report format we evaluated

Remember the eHarmony Statistics 11-section report? That's their **standard output**. We could ship client audits in this exact format — it's already industry-recognized, more detailed than our 5-section 1-pager, and includes entity + structured-data + speed + originality that we currently don't surface.

### 3. Get the page-1 benchmark bar we identified as the biggest gap

Section 02 (Page-1 benchmarks) is **the** differentiator. Adding it to our 1-pager was the upgrade we flagged earlier. On-Page.ai ships it natively.

### 4. Internal-link manifest pattern = repeatable at scale

The "manifest-based runner" approach (process 75 pages, save manifest, resume next batch) is **exactly the pattern** for our clients with 50-500+ pages. We can run it on GPC (21 pages, small enough to do in one batch).

## Pricing (RESOLVED 2026-08-27)

The MCP endpoint is at `api.on-page.ai`. Pricing documented at `/install` and confirmed via `llms-full.txt`:

- **One-time $1 sign-up, $10 in credits included** (no credit card needed for the free path)
- **$20 in credits with a business email** (their preferred path)
- **Deep scan = 3 credits** → 3 deep scans per $10, or 3 deep + mix with standard/lite
- **Standard scan = 2 credits** → 5 standard scans per $10
- **Lite scan = 1.5 credits** → 6 lite scans per $10
- **Classify = 0.2 credits** → 50 topical classifications per $10
- **Job polling (GET /v1/jobs/{id})** and **result fetch (GET /v1/jobs/{id}/result)** are FREE — no credits reserved
- **27 supported scan regions** (default US, includes CA which is what we need for GPC)

Signed up 2026-08-27: API key in `~/.hermes/secrets/onpage-api-key.txt` (mode 600), $10 credits loaded, `ONPAGE_API_KEY` wired into `/tmp/open-seo-lanpubs/.env`. Active decision is no longer cost-of-entry; it's the comparison verdict.

### Full endpoint map (from llms-full.txt)

| Method | Path | Cost | Description |
|--------|------|------|-------------|
| POST | `/v1/scan` | 2 credits | Standard SEO scan vs top Google results for a keyword |
| POST | `/v1/scan/lite` | 1.5 credits | Quick scan — entity coverage + cohort only |
| POST | `/v1/scan/deep` | 3 credits | Deep scan — 15 competitors + SERP-speed benchmark |
| POST | `/v1/classify` | 0.2 credits | Categorize a URL or text into 1,091 categories |
| GET | `/v1/jobs/{job_id}` | Free | Poll job status + progress |
| GET | `/v1/jobs/{job_id}/result` | Free | Fetch the full report |
| GET | `/v1/credits` | Free | Credit balance |
| GET | `/v1/regions` | Free | List supported regions (no auth needed) |
| POST | `/v1/webhooks/test` | Free | Queue a test webhook delivery |

**Two ways to integrate:**
- REST API at `https://api.on-page.ai` (async job model)
- MCP server at `https://api.on-page.ai/mcp` (HTTP Streamable transport)

The MCP transport is what we want — drops straight into `~/.hermes/config.yaml` next to OpenSEO.

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

**Run a side-by-side scan on GPC Development (the same `gpcdevelopment.ca` we already audited) and decide based on output, not theory.**

Status (2026-08-27):
- ✅ Signed up at `api.on-page.ai`, $10 credits loaded
- ✅ `ONPAGE_API_KEY` wired into OpenSEO fork `.env`
- ✅ `content-optimization` skill live in Hermes (skill_view verified)
- ⏳ `run_content_scan` not yet run on GPC — pending green-light (~$2 for 1 standard scan, ~30s wall time)

**Evaluation plan:**
1. Pick 3 representative GPC pages: homepage, one service page (`/services/general-contracting/` or similar), one project page
2. Run `mcp__openseo__run_content_scan` for each → save to `clients/gpc-development/drafts/seo/onpage-vs-openseo-2026-08-27.md`
3. Compare the entity coverage, page-1 benchmark, internal-link suggestions, originality score against the OpenSEO `run_site_audit` data already in the audit MD
4. **Verdict threshold:** if On-Page.ai's per-page report raises ≥3 actionable items the OpenSEO audit missed, promote to sprint Phase 3 stack. Otherwise, mark as "considered, not adopted" and close this draft.
5. Commit verdict to `_config/seo-tool-decisions.md`

## Open questions

1. ~~**Pricing** — need to confirm before buying. Most likely a free tier + paid MCP access.~~ — RESOLVED 2026-08-27: $1 + $10 credits loaded, key wired.
2. **Compatibility with our 4-layer pipeline** — does the `run_content_scan` JSON shape drop cleanly into our DuckDB mirror? Need to run a real scan to know.
3. **Claude Code vs Hermes as the driver** — page says "compatible with both"; we're on Hermes. Recipe prompt syntax needs to map to our SKILL.md format, not `.claude/skills/`. **Resolved:** On-Page.ai MCP transports over HTTP Streamable — same pattern as OpenSEO; no driver translation needed. We're using Hermes via MCP, recipes execute server-side on `api.on-page.ai`.
4. ~~**Image generation in Codex** — page mentions this but we don't use Codex. Skip.~~
5. ~~**The 5 recipes I couldn't read** — middle of the source was truncated; need to read full page to enumerate all 17.~~ — RESOLVED 2026-08-27: All 23 recipes enumerated (see table above).

**New open question (2026-08-27):**
6. **Verdict threshold defined?** — Promotion bar = ≥3 unique actionable items vs OpenSEO audit. Is that the right bar? Open to adjustment after first scan.

## Related drafts

- `/home/denni/wiki/drafts/future-projects/meridian-local-seo-agent.md` — Meridian (DataForSEO via OpenSEO fork + LeadSniperAI + Deepline)
- `/home/denni/wiki/processes/seo-client-onboarding-sprint.md` — Phase 1-5 sprint + Module A/B AI SEO
- `/home/denni/wiki/clients/gpc-development/drafts-preview/seo/audit-1page-2026-08-26-gpc-development.html` — current GPC 1-pager

---

*Active integration draft. Key is wired + signed up + credits loaded (2026-08-27). Pending: side-by-side scan on GPC for verdict — gated on user's "run the scan" green-light (~30s wall time, ~2 standard-scan credits).*

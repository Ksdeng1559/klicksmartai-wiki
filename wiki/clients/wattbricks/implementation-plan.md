---
title: WattBricks — Topical Authority Implementation Plan
created: 2026-04-20
updated: 2026-04-20
type: implementation
tags: [wattbricks, seo, content, execution, hermes-agent, tasks]
related: [clients/wattbricks/topical-authority-plan, clients/wattbricks/authority-map, entities/wattbricks]
---

# WattBricks — Topical Authority Implementation Plan

## Overview

This is the **executable task list** for building WattBricks' topical authority. The full strategy lives in `clients/wattbricks/topical-authority-plan.md`. This doc is the operational layer — what Hermes executes, in what order, and how.

**Tasks are in the Google Sheet (Backlog tab):** `1gZdR1MdNlCjjHiLE29dML4EeK-y6F56zuf9LcwtzTuQ` — Backlog rows 3–40.

**Source doc (Google Doc):** https://docs.google.com/document/d/1fuQpavgrAYVrf8a6c93gOP4IbBFZ0rn84R_R3HXTOXU/edit

---

## Execution Priorities

### P0 — Do First (Block Everything Else)

| Task | Sheet Row | Status | Notes |
|------|-----------|--------|-------|
| Add blog/content hub to Shopify | Backlog #1 | Pending | **Site has zero content infrastructure.** No blog = no SEO. Nothing else matters until this is done. |
| Implement Product schema on product pages | Backlog #2 | Pending | Required before any content goes live |
| Submit wattbricks.com to Google Search Console | Backlog #37 | Pending | Not indexed in Canada. Verify ownership + sitemap first |
| Fix title tags + meta descriptions | Backlog #35 | Pending | Currently generic — no Canada targeting |
| WattBricks vs EcoFlow comparison (B1) | Backlog #5 | Pending | **Highest-value piece in the entire plan. Zero SERP competition.** |
| Home Backup Canada pillar (H1) | Backlog #6 | Pending | Cluster anchor — 8,100/mo keyword. Everything links here. |

### P0 Rationale

The site has no blog, no schema, and no Canada indexing. Adding content to a site with no infrastructure is wasted effort — Google won't find it, won't rank it, and won't display it well. **The Shopify blog + schema + GSC setup MUST happen in Week 1 before any content is written.**

---

## Content Writing Instructions (for Hermes)

### Content Brief Template

For every piece of content, Hermes should produce:

```
1. Title tag: [Exact target keyword] | WattBricks Canada
2. Meta description: [≤160 chars — includes CTA, Canada mention, key differentiator]
3. H1: [Exact target keyword or close variant]
4. URL slug: /[keyword-phrase]/[secondary-keyword]/
5. Word count target: 1,500–2,500 words
6. Internal links required: 2+ to existing articles
7. External links: 2–3 (NotebookLM sources, government/regulatory sources)
8. Schema type: FAQPage | HowTo | Article (as applicable)
9. Target keyword + 3 supporting keywords (bold in first 100 words)
```

### Content Rules

- **Canada-first framing** — every piece must reference Canadian grid context, Canadian retailers, or Canadian energy policy. Never generic US copy.
- **No broadcast marketing** — sound like a knowledgeable person, not a brand. "We" only appears after the problem/use case is fully established.
- **Link to NotebookLM sources** — cite specific stats from the Energy Crisis notebook (`c97aa28a`) for credibility.
- **Internal links** — every article links to at least 2 existing articles using keyword-rich anchor text. New articles → existing pillar.
- **Schema before publish** — FAQPage schema on all blog posts, HowTo schema on tutorials. Apply before marking task done.

---

## Phase Execution Order

### Phase 0: Site Infrastructure (Before Any Content)
**Target: Complete by April 25, 2026**

1. Add Shopify blog to wattbricks.com
2. Install Product schema on all product pages
3. Submit wattbricks.com to GSC, verify ownership, submit sitemap
4. Fix title tags (add "Canada", model number, key feature)
5. Fix meta descriptions (add CTA + Canada copy + Trustpilot mention)
6. Establish brand separation statement for wattbricksenergy.com confusion

### Phase 1: P0 Content Sprint (Week 1–2)
**Target: B1 + H1 live by April 30, 2026**

1. B1 — WattBricks vs EcoFlow (publish first — blue ocean)
2. H1 — Portable Power Station Home Backup Canada (cluster anchor)
3. H2 — How Long Will My Fridge Run? (supports H1)
4. H6 — CPAP Battery Backup (supports H1)
5. C1 — Best Camping Power Stations Canada (supports camping pillar)
6. B2 — WattBricks vs Jackery (blue ocean)

**Ongoing:** Submit B1 and H1 to Google Index via GSC the day they publish.

### Phase 2: Depth (Week 3–7)
**Target: All P1 content live by May 21, 2026**

Week 3: J1 (Job Site pillar), H3 (Ontario's Grid — newsjacking)
Week 4: C2 (Solar Generator Camping), H4 (Whole Home vs Portable)
Week 5: B3 (Is WattBricks a Good Brand?), C3 (RV Off-Grid)
Week 6: H5 (DIY UPS — HowTo schema), J2 (Silent Job Sites)
Week 7: C4 (Snowbird Guide), J3 (HVAC Contractors)

### Phase 3: Scale (Week 8–12)
**Target: All content live by June 9, 2026**

Week 8: H7 (Ontario Energy Rebate), C5 (Ice Fishing)
Week 9–10: 5x comparison short-forms + 5x long-tail posts
Week 11–12: FAQ hub, Glossary, Installation guide

---

## NotebookLM Prompts (Copy-Paste for Content Writers)

### Energy Crisis / Urgency Angle (H1, H3)
```
Query NotebookLM notebook c97aa28a:
"What does the notebook say about Canada's electricity crisis, grid reliability issues,
and demand growth projections? Include specific statistics from 'Canada's Energy Future 2026'
and RSM Canada about infrastructure constraints and electricity demand increases."
```

### Fridge Runtime / Practical Use (H2)
```
Query NotebookLM notebook c97aa28a:
"What specific runtime calculations or appliance wattage data does the notebook provide?
Look for anything about how long a portable power station can run a refrigerator, freezer,
CPAP, or other common household devices during a power outage."
```

### Solar / Off-Grid Angle (C2, C3)
```
Query NotebookLM notebook c97aa28a:
"What does the notebook say about solar energy, off-grid power, or renewable energy
trends in Canada? Any data about solar adoption, energy independence, or grid defection?"
```

### Contractor / Job Site Angle (J1, J2, J3)
```
Query NotebookLM notebook c97aa28a:
"What does the WattBricks problem definition doc say about contractor pain points,
job site power challenges, or professional/trades use cases for portable power?"
```

---

## Schema Markup Reference

### FAQPage Schema (apply to all blog posts)
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Question from article]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Answer text]"
      }
    }
  ]
}
```

### HowTo Schema (apply to tutorials: H5, C2, J2)
```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "[Article title]",
  "step": [
    {"@type": "HowToStep", "name": "[Step 1]", "text": "[Step 1 text]"},
    {"@type": "HowToStep", "name": "[Step 2]", "text": "[Step 2 text]"}
  ]
}
```

### Product Schema (already on product pages — verify completeness)
Required fields: `name`, `image`, `description`, `sku`, `brand`, `offers.price`, `offers.priceCurrency`, `aggregateRating`

---

## Success Metrics

| Metric | Baseline | 90-Day Target |
|--------|----------|--------------|
| Non-branded keywords ranking | 0 | 15+ |
| "wattbricks vs ecoflow" rank | Not indexed | **#1** |
| "portable power station Canada" rank | Not indexed | Top 20 |
| Content pages published | 0 | 20+ |
| FAQ schema pages | 0 | 12+ |
| HowTo schema pages | 0 | 3+ |
| Internal links per article | N/A | 3+ |
| Organic ETV | $0.10/mo | $150+/mo |

---

## Key Files

| File | Location |
|------|----------|
| Topical Authority Plan (strategy) | `clients/wattbricks/topical-authority-plan.md` |
| Authority Map | `clients/wattbricks/authority-map.md` |
| Entity (brand intel) | `entities/wattbricks.md` |
| Domain Analysis (source) | `G:/AI - Coding Projects/WattBricks/wattbricks_domain_analysis.html` |
| Growth Playbook (GTM) | `G:/AI - Coding Projects/WattBricks/Domain Analysis/wattbricks_growth_playbook.html` |
| Energy Crisis NotebookLM | https://notebooklm.google.com/notebook/c97aa28a-fd32-4e3e-a745-4c5498fa27de |
| Google Doc (formatted) | https://docs.google.com/document/d/1fuQpavgrAYVrf8a6c93gOP4IbBFZ0rn84R_R3HXTOXU/edit |
| Task Sheet (Backlog) | `1gZdR1MdNlCjjHiLE29dML4EeK-y6F56zuf9LcwtzTuQ` — Backlog rows 3–40 |

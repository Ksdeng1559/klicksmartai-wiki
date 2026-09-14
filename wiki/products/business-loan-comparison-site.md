---
title: Business Loan Comparison Site
tags: [products, seo, content-strategy, keyword-strategy]
type: products / note
---

# Business Loan Comparison Site — Strategy

**Status:** Phase 1 complete (Foundation & Research), Phase 2 pending "yes" approval. Strategy rev. 2 (2026-09-13). Notion parent: Business Loan Comparison Site — Strategy & Research (`3db9e94cf0a48149984af95c7fa068fe`), under LeadSniperAI Marketplace OS.

## Two differentiators
1. **Broker with an opinion** — Swoop is pure aggregator, BDC is crown corp. No Canadian competitor owns "broker-led comparison with a human who tells you which lender fits."
2. **AI chatbot over knowledge base** — not a feature, a content-distribution mechanism. Every page feeds the chatbot KB; every unanswered question becomes a future article.

## Headline numbers (Aug 2026)
- 1,361 unique commercial + comparison terms with Canada volume
- 52,700 total monthly searches (top 30 = 34,600 in Aug, −29.6% vs avg)
- Top term `business loan` 3,600/mo @ $46.33 CPC
- Highest-CPC comparison term `best business loan companies` 10 vol @ $112.52
- **Top gap SERP:** `BDC vs private lender` — empty CA page 1, 2,990 vol aggregate

## Consolidated keyword set (124 terms, 10 play groups — source of truth)
`consolidated_keyword_set.json` in `~/.hermes` run dir. 102 commercial-intent + 22 tariff.

| Group | Terms | Vol/mo | Avg CPC |
|---|---:|---:|---:|
| Generic / Head Terms | 67 | 25,400 | $95.94 |
| Line of Credit | 8 | 2,680 | $102.49 |
| Unsecured | 8 | 2,080 | $60.45 |
| Term Length | 11 | 810 | $155.27 |
| Working Capital / Cash Flow | 3 | 660 | $159.88 |
| MCA, Inventory, Refinance, Growth | 5 | 190 | ~$97 |
| Tariff Trigger (separate) | 22 | 10 | $0.06 |

## Build order
**7-pillar cluster first** (steady daily demand): `/business-loans-canada` (14k+ vol), `/unsecured-business-loans` (Rail B core), `/working-capital-loans`, `/business-line-of-credit`, `/short-term-business-loans`, `/bdc-vs-private-lender` (25k agg), `/equipment-financing`. Province derivatives (ON=60% of head volume): ontario / alberta / british-columbia.

**Tariff = separate cluster, NOT a pillar** (decision): zero commercial-intent volume, news-anchored. Only viable term `BDC tariff loan vs private lender` (score 35). Build `/tariff-financing-canada` single trigger page, publish on tariff-news events (BDC $1B steel/aluminum program = the obvious Rail B "private lender alternative" play). Don't pollute the 7-pillar plan.

## Phase A (Month 1)
Homepage + `/best-small-business-loans-canada` + `/best-business-loans-canada` + `/bdc-vs-private-lender` + 3 brand reviews (swoop/lendified/merchant-growth) + 3 province pages.

## Phase 2 (needs "yes")
Page architecture: wireframes (10 page types), FAQ bank (33 PAA Q&A, 150–300 w each), JSON-LD schema spec (FAQPage/Product/Review/Org/Breadcrumb/LocalBusiness), comparison table designer, internal-link map (20+/page), CTA hierarchy, chatbot KB ingestion plan. **Two flagged inputs before start:** (1) real lender data for comparison tables vs placeholder scaffold; (2) chatbot stack choice (OpenAI Assistants vs custom RAG).

See [[Klick2Client-Agentic-Os]], [[BDC-tariff-loan-vs-private-lender]]. Skill: `organic-paid-traffic-strategy`.

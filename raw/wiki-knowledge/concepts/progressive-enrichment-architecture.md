---
title: Progressive Enrichment Architecture (Explorium Reference)
created: 2026-08-06
updated: 2026-08-06
type: concept
category: gtm
tags: [concept, enrichment, architecture, leadgen, exploratory, lead-sniper, entity-resolution, gtm]
related: [entities/leadsniper-sgi-prd, entities/swan-gtm-gtm-skills, gtm-engineer-resources, deepline]
sources: [user-provided reference, Explorium Quick Starts + Data Catalog]
---

# Progressive Enrichment Architecture

**Strategic thesis:** Explorium is useful less as a single enrichment vendor and more as a **reference architecture and taxonomy for enrichment workflows**. Its Quick Starts document one end-to-end workflow (prospecting + lead enrichment), but its Data Catalog contains a much broader library of company, people, and event signals.

## Core enrichment workflow (Explorium's recommended sequence)

**Market sizing → company discovery/matching → company enrichment → decision-maker discovery → contact enrichment → iteration**

1. Use a **statistics endpoint** to estimate audience size
2. Identify or match the correct company entity
3. Retrieve company attributes and identifiers
4. Find employees by department, seniority, or role
5. **Enrich only selected people** with verified email + phone data
6. Refine filters based on quality and cost

> **Operating pattern for LeadSniperAI:** avoids enriching every record prematurely. This is the cost-control core.

## Enrichment use-case catalog

### 1. Market and ICP sizing
Answer: how many businesses fit the ICP? Which regions concentrate? Distribution by industry/size/revenue/category? **Is the market large enough before spending credits?**
→ **LeadSniperAI app:** ICP Market Mapper — estimates TAC (total addressable accounts) before campaign launch. Runs aggregated statistics BEFORE retrieving full records.

### 2. Business discovery
Discover by: industry/category, geography, employee count, revenue range, company type, domain, technology/operational characteristics.
Applications: M&A target discovery, commercial-finance borrower discovery, mortgage referral-partner discovery, AI-agency prospecting, construction/dev discovery, capital-raise investor/partner ID.

### 3. Entity resolution and matching
Persistent identifiers (`business_id`, `prospect_id`): **match the entity first, then enrich by identifier** — reduces duplicates, false matches, unnecessary calls.
→ **LeadSniperAI app:** Convex canonical entity layer: raw company → normalized domain → matched external IDs → canonical company ID → enrichment history → signals → scores → opportunities. **Explorium IDs = provider-specific aliases, NOT the primary key.**

### 4. Account enrichment
Enrich matched companies for: qualification, segmentation, scoring, personalization, territory, market analysis.
Use cases: estimate ability to borrow, identify expansion-stage companies, determine likely service needs, detect acquisition candidates, build account-specific opportunity theses, assign to mortgage/M&A/capital/growth campaigns.

### 5. Buying-committee discovery
Retrieve employees by: department, title, job level, company, email availability. Works for finance, ownership, operations, development, real estate, tech, executive — not just marketing/sales.

### 6. Contact enrichment (progressive)
Separate **discovery from contact-data enrichment**. General profile first; email/phone only for qualified prospects.

| Stage | Purpose |
|-------|---------|
| 1. Company qualification | Is the account worth pursuing? |
| 2. Role qualification | Does the buying committee matter? |
| 3. Person qualification | Is this person a decision-maker? |
| 4. Contact enrichment | Verify email/phone for qualified only |
| 5. Verification | Confirm deliverability |
| 6. Outreach activation | Engage with sufficient evidence |

> More economical than purchasing complete contact data for every company.

### 7. Trigger-event enrichment
Data Catalog as a **business-event catalog**: company awards, office closures/openings, work anniversaries, funding rounds, product launches, investments, IPO announcements, partnerships → convert to GTM/opportunity triggers.

## High-value use cases for LeadSniperAI

### Pre-M&A signal engine
Combine: office closures, executive tenure changes, declining hiring, owner longevity, weak digital presence, high review volume but poor responsiveness, expansion-then-contraction, industry consolidation, new investment/partnership.
**Output:** Acquisition Readiness Score · Owner Transition Probability · Financial Stress Probability · Strategic Buyer Fit · Estimated Outreach Timing.
*Explorium supplies evidence; LeadSniperAI owns the scoring.*

### Commercial-finance intelligence
Signals: new office, new product, expansion, partnership, funding, hiring growth, construction activity, new geographic market.
**Output:** likely capital requirement · financing purpose · estimated timing · appropriate product · decision-makers · personalized thesis.

### Growth-agency prospecting
Account enrichment + company size, category, product launch, funding, market entry, partnership, weak website/SEO.
**Output:** growth-gap score · recommended campaign · estimated impact · outreach personalization.

### Capital-raise OS
Enrich: investors, strategic partners, companies raising, recent funding participants, partnership networks, geo/sector exposure. Supports investor matching, comp-transaction research, relationship mapping.

## Recommended architecture

```
Explorium / Deepline / other providers
              ↓
Provider adapter layer
              ↓
Entity resolution
              ↓
Convex canonical company + person records
              ↓
Raw enrichment attributes
              ↓
Event and signal normalization
              ↓
LeadSniperAI proprietary scoring
              ↓
Opportunity thesis
              ↓
Next-best action
              ↓
Smartlead / HeyReach / Telnyx / Unipile
```

## Strategic conclusion — Explorium's three roles

1. **Potential enrichment provider**
2. **Reference workflow for progressive enrichment**
3. **Signal-taxonomy catalog for LeadSniperAI**

> Its most valuable architectural lesson is not merely "find emails." It is: **size the market, resolve the company, qualify the account, identify the buying committee, enrich selectively, and activate outreach only when sufficient evidence exists.**

## Wiring into KlickSmartAI

- **`gtm-enrichment-planner`** — the 6-stage progressive model (company → role → person → contact → verify → activate) IS the credit-cost control: enrich selectively, never pre-enrich the whole list
- **`deepline` skill** — the provider adapter + waterfall layer maps directly to Stage 4-5 (contact enrichment + verification)
- **`leadsniper-sgi-prd`** — entity resolution + canonical ID layer aligns with the SGI domain-audit model
- **`swan-gtm-gtm-skills`** — the GTM decision layer (signal qualification → scoring → outreach) consumes the progressive-enriched output

## Related

- [[entities/leadsniper-sgi-prd]] · [[entities/swan-gtm-gtm-skills]] · [[gtm-engineer-resources]] · deepline skill

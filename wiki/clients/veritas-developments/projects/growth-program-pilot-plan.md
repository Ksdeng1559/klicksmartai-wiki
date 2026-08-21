---
title: Veritas Developments — Growth Program Pilot Plan (Content Growth Strategies)
created: 2026-08-14
updated: 2026-08-14
type: workflow
client: Veritas Developments (David Poole)
projects: Prime Lee's Summit, Stonehaven Estates
tags: [veritas, growth, content, demand-generation, attribution, pilot, jackson-county, mcf, kcclt]
sources: [notion: Growth Program — 3bc9e94cf0a4818aa34fe056740261b6, wiki: processes/content-growth-strategies.md]
related: [content-growth-strategies, jackson-county-mo-county-intelligence-report, jackson-county-mo-investor-leads, jackson-county-mo-kcclt-partnership-memo]
---

# Veritas Developments — Growth Program Pilot Plan

> **Status: PILOT PLAN (draft for review)** — grounds the generic Content Growth Strategies workflow in a real client. Not yet executed. Requires Dennis's approval before any external content is published.

## Why Veritas is the right pilot

The generic workflow (`processes/content-growth-strategies.md`) is a framework. This doc makes it concrete. Veritas is the natural first pilot because:

1. **Signed engagement** (2026-08-11) — deal loan structure + investor flywheel (webinars) + CRM build. The Growth Program directly feeds the investor flywheel.
2. **Deep intelligence already exists** — 7-deliverable Jackson County package (county intelligence, housing, CRE, market data annex, investor leads, KCCLT memo, east-side pro-forma). The "Signals → Intelligence" half is already done.
3. **A clear commercial path** — the MCF (Mission Capital Fund) needs investors, partners, and county buy-in. Content converts that intelligence into authority and demand.
4. **Two distinct audiences** — investors (capital) and the community/partners (deal flow). The Growth Program serves both.

## The commercial objective (top 3 outcomes)

1. **Raise MCF capital** — attract family offices, CDFIs, faith foundations, CRA banks to the Veritas MCF structure.
2. **Assemble the partner stack** — position Veritas as the consolidator of KCCLT + Central Bank + AG/KC + PEDC + Habitat (the "integration premium" the county report identifies).
3. **Win county/municipal support** — land-bank disposition, Housing Trust Fund co-investment, permitting fast-track.

## Evidence-backed content pillars (3–5)

Grounded in the Jackson County intelligence, not generic growth doctrine:

| Pillar | Evidence base | Audience | Commercial purpose |
|--------|--------------|----------|-------------------|
| **P1: The 18,000-Home Opportunity** | County report §3, §12 — 18,000 off-market vacant units, 60% of all vacant stock, $94K–$150K acquisition basis | Investors, family offices | Raise MCF capital — "the cheapest acquisition basis in any major U.S. metro" |
| **P2: Vacancy Conversion as Manufacturing** | County report §9 — rehab "assembly line," CLT version of manufactured housing | Investors, developers | Position Veritas as the consolidator; the integration premium |
| **P3: The Faith-Aligned Capital Stack** | County report §12, investor leads — AG/KC, PEDC, United Believers, NCF Heartland | Faith foundations, CDFIs | Assemble the faith-framed capital layer |
| **P4: The KCCLT Partnership Model** | KCCLT memo — dual-ownership, subsidy recycling, Pay-as-We-Sell | Investors, county officials | Prove the permanent-affordability engine |
| **P5: The East-Side Market Data** | Market data annex — 4.9–5.6% vacancy tightening, 16-yr rent growth record | Investors, county officials | De-risk the thesis with hard numbers |

## First campaign thesis (the pilot)

**Campaign: "The Harvest is Plentiful"** — named after the county report's opening verse (Matthew 9:37), which frames the whole thesis.

- **Core authority asset:** A market briefing — *"Kansas City's 18,000 Empty Homes: The Most Efficient Unit of Social Equity in America"* — turning the county intelligence report into a public-facing, investor-grade narrative.
- **Derivative assets:** LinkedIn posts (David Poole as author), a webinar (feeds the investor flywheel), an investor one-pager, a county-official briefing, an FAQ, a video thesis.
- **CTA classes:** Request a market analysis · Book a strategy call · Download the briefing · Join a webinar.
- **Approval gate:** All claims sourced from the verified Jackson County package. Brand voice = David Poole / Veritas. No external delivery without Dennis's approval.

## Attribution strategy — what's measurable now vs. later

### The honest scope

The generic workflow's KPI framework lists "campaign-attributed revenue" and "closed-won revenue" — but **that attribution plumbing does not fully exist yet.** The stack has GA4 + GTM (per the KlickSmartAI.com site spec) and Supabase/CRM, but no unified attribution layer. So the pilot must be honest about what's measurable.

### Recommended model: U-shaped (position-based) attribution

Based on the 2026 attribution scan, **U-shaped (40% first-touch / 40% last-touch / 20% middle)** is the right fit for Veritas:

- **Why:** The Veritas journey has two distinct inflection points — *discovery* (the investor first learns about the MCF / 18,000-home thesis) and *conversion* (the investor books a call / commits capital). U-shaped credits both, which is exactly the awareness→conversion structure the Growth Program creates.
- **Why not last-touch (67% of B2B teams use it, but it's proven ineffective):** It would credit only the final touchpoint (e.g., the webinar) and ignore the market briefing that created the awareness. For a capital-raising program, discovery is as valuable as conversion.
- **Why not first-touch:** It would overvalue top-of-funnel and ignore the nurture that closes.
- **Why not W-shaped:** W-shaped is for enterprise deals with 10+ touchpoints and distinct stage gates (demo/proposal). Veritas's capital raise is shorter and has two clear inflection points, not three. U-shaped is simpler and sufficient.

### Implementation — phased, not all-at-once

**Phase 1 (now, no new tooling):** Standardize UTM parameters on every content asset. Every CTA link carries `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`. This is the foundation — no attribution works without it.

**Phase 2 (pilot, GA4 + CRM):** Configure GA4 conversion events (CTA click, webinar registration, briefing download, strategy-call booking). Pipe form submissions into the CRM (Supabase) with the UTM source captured. This gives first-touch and last-touch visibility immediately.

**Phase 3 (post-pilot, if it earns it):** Build the U-shaped calculation in SQL/BigQuery or a lightweight attribution tool. Only after Phase 1–2 prove the data is clean. The 2026 scan is clear: *no attribution model can overcome poor data quality.*

### KPI scorecard for the pilot (measurable now)

| Layer | KPI | Tool |
|-------|-----|------|
| Production | Core assets produced, derivatives, cycle time | Hermes / task sheet |
| Distribution | Publishing consistency, channel coverage | Content calendar |
| Engagement | Views, watch time, comments, shares | GA4 / platform analytics |
| Intent | CTA clicks, downloads, webinar registrations, strategy-call bookings | GA4 + CRM |
| Pipeline | Qualified investor conversations, meetings | CRM (Supabase) |
| Revenue | Capital commitments (tracked manually until attribution matures) | CRM + manual |

**Explicitly deferred (not measurable yet):** campaign-attributed revenue, closed-won capital attribution. These require the Phase 3 attribution layer. The pilot should NOT pretend to measure them.

## 30/60/90 for Veritas

### First 30 days — Foundation
- Approve the "Harvest is Plentiful" campaign thesis.
- Define the 5 content pillars (above) as the standing editorial structure.
- Install the Growth Content Engine skills in Hermes (`/content-research`, `/content-strategy`, `/content-factory`, `/content-distribute`, `/content-optimize`).
- Implement `/growth-campaign veritas`.
- Set up UTM standardization + GA4 conversion events (Phase 1–2 attribution).
- Produce the core authority asset (market briefing) + first derivatives.
- **Success:** one complete signal→content campaign, factually accurate, commercially purposeful.

### Days 31–60 — Distribution + Pipeline
- Publish the briefing + derivatives across LinkedIn, webinar, email.
- Run the first investor webinar (feeds the flywheel).
- Capture engagement + intent into the CRM with UTM source.
- Connect qualified investor conversations to the MCF pipeline.
- **Success:** measurable conversations/inquiries/qualified investor activity — not just content volume.

### Days 61–90 — Optimization + Scale
- Compare pillars/channels against pipeline outcomes.
- Identify winning content patterns.
- Build reusable campaign templates for the next Veritas campaign (and future clients).
- Evaluate whether the U-shaped attribution layer (Phase 3) is worth building.
- **Success:** the program is replicable for another client with limited setup.

## Governance (from the generic workflow, applied)

1. **Evidence before content** — every claim sourced from the verified Jackson County package.
2. **Commercial purpose before volume** — each asset maps to a pillar and a CTA.
3. **One core idea, many derivatives** — the briefing is the core; everything derives from it.
4. **Human approval for sensitive material** — investor claims, financial figures, county-specific facts, faith framing all require Dennis's review.
5. **Measure downstream outcomes** — engagement is useful; investor conversations and capital commitments determine success.
6. **Store learning** — winning patterns feed back into the next campaign.
7. **Client isolation** — Veritas brand voice, data, and campaign history stay separate from Spectra and other clients.

## Open questions for Dennis

1. **Is David Poole the author/voice** for the content, or should it be Veritas-branded without a named author?
2. **Which CTA is primary** for the first campaign — webinar registration (feeds the flywheel) or strategy-call booking?
3. **Does the investor flywheel (webinars) already have a landing page / registration flow** we should route into, or does that need building?
4. **Approve the "Harvest is Plentiful" thesis** and the 5 pillars before I scaffold the skills and produce the core asset?

---

*Drafted for internal use. No external content published without Dennis's approval.*

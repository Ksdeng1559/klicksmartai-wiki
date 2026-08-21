# EXECUTIVE BRIEF: THE MISSING MIDDLE INFILL OPPORTUNITY

**To:** Principal Underwriters & Investment Committee, Eng and Company
**Topic:** Structural Real Estate Restructuring & Capital Allocation for Missing Middle Development
**Date:** July 7, 2026
**Status:** Ingest of an IC-distribution brief; canonical copy in this wiki.
**Linked client page:** [eng-and-company/README.md](./README.md)
**Linked feasibility work:** [drafts/garrett-street-feasibility.md](../../drafts/garrett-street-feasibility.md)

---

## 0. Reusable Option-Agreement Metaprompt (copy-paste block)

> **Why it's here:** the brief is addressed to a specific deal, but the **metaprompt** that stress-tests an option is reusable across every Eng and Company assembly. It is also lifted to a dedicated skill: `real-estate-option-agreement-metaprompt` (under `software-development/`) so it loads automatically on related prompts. Use the block below to feed a property into any LLM workspace for a same-shape analysis.

````markdown
# SYSTEM INSTRUCTIONS: REAL ESTATE OPTION AGREEMENT & RISK UNDERWRITING ENGINE

You are an expert commercial real estate attorney and institutional land acquisition strategist
specializing in Canadian Transit-Oriented Development (TOD) and "Missing Middle" land
assemblies. Analyze the legal and financial viability of executing a Wholly Assignable Option
Agreement based on the property and market data provided by the user.

---

## 1. EXPECTED INPUTS
The user will provide:
- Target Property Address & Current Estimated Fair Market Value (FMV).
- Assembly Scope (e.g., Single lot multiplex vs. 3-lot mid-rise apartment block).
- Current Zoning vs. Target OCP Density (e.g., RS1 to 3.00 FSR Mid-Rise).

---

## 2. REQUIRED OUTPUT STRUCTURE

### 2.1 Legal Viability & "Wholly Assignable" Clause Stress-Test
- Structure the assignment clause so the corporate entity can assign the contract to an
  institutional buyer, REIT, or joint-venture partner for a lift/premium without triggering
  seller blockages or double property transfer tax (PTT).
- Identify risk-mitigation language to protect the buyer's deposit if zoning amendments are
  rejected by the city.

### 2.2 Optimal Timeline & Milestone Framework
- Propose an explicit timeline (in months) for the option term based on current municipal
  permitting drag (e.g., 3–5 months for multiplex permits vs. 12–18 months for full TOA
  mid-rise rezoning).
- Break down critical milestones (Title searches, Environmental Phase 1, Quantity Surveyor
  cost proformas, City Pre-Application meetings).

### 2.3 Financial Terms & Consideration Architecture
- **Option Consideration (Deposit):** Tiered, non-refundable (but applicable to purchase
  price) deposit structure that keeps the seller incentivized while minimizing upfront hard
  cash exposure.
- **Strike Price Strategy:** Peg the final purchase price (Fixed premium over current FMV
  vs. Escalating price scale over time).

### 2.4 Seller Psychology & Negotiation Leverage
- Primary friction points a single-family homeowner will have regarding tying up their
  property on an option.
- 3 clear scripts/value-propositions to convince the seller that an option agreement with a
  corporate entity is superior to a standard straight sale.

---

### START ANALYSIS
Ingest the property data below and evaluate the Option Agreement strategy.
````

---

## 1. How Eng and Company Should Structure the Option

The agreement should sit on **three pillars** that together retain maximum control with minimal hard-cash exposure during the downturn.

### A. The Assignment Clause — the "lift mechanism"
Wording must explicitly state the buyer is **"Eng and Company and/or its nominee or permitted assignee."**

- **Goal:** secure the land, run the rezoning, then "flip" or assign the contract to a
  massive institutional REIT or pension fund before the final closing date.
- **Benefit:** the assignee steps into your shoes, pays you an assignment fee (your profit),
  and is cut out of the final land title transfer — meaning **you avoid a double layer of
  Property Transfer Tax (PTT)**.

### B. Condition Precedents — the "escape hatches"
Option exercisable at the sole discretion of Eng and Company, contingent on:
- **Favourable Quantity Surveyor (QS) report** — hard construction costs do not impair
  target yields.
- **City planning support** — written confirmation that the proposed 3.00 FSR density or
  multiplex configuration is supported without prohibitive offsite infrastructure fees.
- **Satisfactory Phase 1 Environmental Site Assessment (ESA).**

### C. Tiered Consideration — the "financial deposit stack"
Money drops in stages tied to timeline milestones, not on day one:

| Stage | Trigger | Amount | Purpose |
|-------|---------|--------|---------|
| Day 1 — Execution | Contract signed | **$10,000** | Ties up land for 90 days |
| Month 3 — Due Diligence | Phase 1 ESA + City Pre-Application cleared | **$15,000** | Unlocks 6-month extension if needed |
| Month 12 — Extension | City timeline drags | **$25,000** | Buys another 6 months of runway |

All amounts are **non-refundable but applicable to the purchase price**, so the seller stays
incentivized to keep the deal alive.

---

## 2. How Long to Hold the Option

The option duration must match the **regulatory track of the chosen tenure and format**:

### Track 1 — Ground-Oriented Infill Multiplex (4–6 Units)
**Recommended duration:** 6–9 months (with a 3-month unilateral extension clause).

- **Logic:** Bill 44 multiplex rules make these builds **as-of-right**; public hearings are
  bypassed entirely. New Westminster and Burnaby average a lean 3–5 months to clear these
  permits.
- A 9-month window gives time to: secure architectural drawings → run a pre-application →
  clear the city permit track → arrange CMHC MLI Select construction debt → close.

### Track 2 — High-Density Transit-Oriented Land Assembly (8-Storey Mid-Rise)
**Recommended duration:** 18–24 months (12-month base + two 6-month extensions).

- **Logic:** Moving into a high-density TOA Tier 3 assembly shifts the project out of
  "as-of-right" rules and into a formal municipal rezoning application. In BC, a mid-rise
  rezoning and offsite infrastructure upgrade negotiation absorb **12–18 months minimum**.
- A two-year runway prevents being forced to close on millions in land debt before the city
  has formally approved the 3.00 FSR density uplift.

---

## 3. Contextual Macro Environment — the "1990s" paradigm shift

Macroeconomic housing data demonstrates the Lower Mainland real estate market has officially
exited a 20-year cycle characterized by falling interest rates and aggressive, pre-sale-driven
asset speculation. According to institutional real estate data:

- **The end of free capital:** interest rates are rangebound, and home-price escalation has
  flattened. Real estate has fundamentally inverted from a vehicle of **rapid wealth
  generation** back to a traditional model of **wealth preservation**.
- **Flight to quality & functional demand:** investor demand for speculative, hyper-dense
  single-occupant configurations (studios and small 1-bedroom pre-sales) has collapsed,
  producing illiquidity. Conversely, there is a severe, non-cyclical structural shortage of
  family-oriented **2- and 3-bedroom ground-oriented "Missing Middle" housing**.
- **Pre-sale funding crisis:** the traditional pre-sale model is in a delivery-cost crisis.
  Owner-occupier families cannot purchase 3–4 years before completion, so projects require a
  restructured capital stack.

---

## 4. Strategic Asset Realignment — Infill vs. Assembled Formats

Eng and Company must optimize capital deployment by evaluating two distinct execution tracks
for property holdings like **419 Garrett Street, New Westminster**:

```
+--------------------------------+--------------------------------+
|  SMALL-SCALE INFILL            |  HIGH-DENSITY LAND ASSEMBLY    |
|  (Lot: ~5,000 sqft)            |  (Lot: ~15,000 sqft)           |
|                                |                                |
|  • Framework: As-of-Right      |  • Framework: Provincial TOA   |
|    SSMUH / Bill 44             |    Tier 3 (Sapperton)          |
|  • Density: 0.70–0.85 FSR      |  • Density: Up to 3.00 FSR     |
|    baseline                    |    minimum floor               |
|  • Target Form: 4–6 unit       |  • Target Form: 8-storey       |
|    multiplex / townhomes       |    mid-rise apartment block    |
|  • Red Tape: 3–5 months        |  • Red Tape: 12–18 months      |
|    (no public hearings)        |    (formal municipal rezoning) |
+--------------------------------+--------------------------------+
```

### Option A — Small-Scale Infill Development (standard infill blueprint)
- **Zoning dynamics:** capitalizes on Bill 44 and municipal updates (e.g., OCP Amendment
  Bylaw No. 8573) to construct 4–6 ground-oriented units outright.
- **Risk profile:** bypasses public hearings, slashing approval timelines to **3–5 months**.
- **Project cost baseline:** TPC **$4,760,000** ($793,332/unit), hard construction
  underwritten at **$375/sqft**.

### Option B — High-Density Land Assembly (institutional scale play)
- **Zoning dynamics:** consolidating 419 Garrett Street with 2–3 adjacent lots to exceed a
  **120–150 ft frontage threshold** triggers Transit-Oriented Area (TOA) Tier 3 guidelines
  due to proximity to Sapperton SkyTrain. Land classification shifts to **Residential –
  Limited Mid-Rise (RLM)**.
- **Density multiplier:** elevates vertical height to **8 storeys** and FSR to a
  **3.00 FSR minimum floor**. On a 15,000 sqft parcel, buildable area scales from 4,250
  sqft to **45,000 sqft**, yielding **35–60+ apartment units**.

---

## 5. Financial Architecture & Capital-Stack Solutions

Funding Missing Middle or mid-rise density in 2026 demands a shift away from individual
mom-and-pop investor financing toward **institutional partnership frameworks**.

### The Build-to-Hold Rental Stack — CMHC MLI Select
Given the continuous employment demand generated by the adjacent **Royal Columbian Hospital
complex**, a purpose-built rental strategy is the premier **wealth-preservation** vehicle.

- **Leverage:** CMHC MLI Select unlocks up to **95% Loan-to-Cost (LTC)** financing with a
  historical **40–50 year amortization window**.
- **Institutional pivot:** major family offices and developers are bypassing traditional
  buyers by matching equity with pension funds and institutional equity partners to carry
  rental assets long-term.

### The Strata Liquidation Stack — Conventional Construction Debt
- **Leverage:** tier-1 commercial debt restricts leverage to **65–70% LTC** and mandates a
  rigid **50–65% pre-sale requirement**.
- **Infill workaround:** to avoid pre-sale friction and preserve the ability to market 2–3
  bedroom townhomes to families at completion, developers must source **alternative
  private equity funds or private debt** (underwritten at **9–12% interest**) to bridge the
  construction cycle.

---

## 6. Underwriting Directive — Municipal & Fee Reform Advocacy

To make project proformas functional under rangebound interest rates, Eng and Company must
factor the municipal "cost delivery crisis" into acquisitions:

1. **Factor fee compression into land value.** Municipalities spent 20 years layering on
   inclusionary zoning, strict building codes, and massive development charges because
   rising home values cushioned the blow. With interest rates capped, cities must reduce
   development charges substantially to keep projects viable. **Discount land acquisition
   bids to account for these fixed municipal fees.**
2. **Deploy advanced construction methodologies.** Underwrite all Missing Middle designs
   using **prefabricated, factory-built panelized envelopes**. CMHC's explicit extension of
   MLI Select financing to modular formats compresses on-site construction schedules by
   **up to 4 months**, reducing carrying interest cost and countering global supply-chain
   drag.

---

## 7. Underwriting Verdict for Eng and Company

For an institutional developer, **single-lot multiplex development** is a safe, steady-margin
execution play. However, **land assembly represents the maximum-upside route**. By using
**wholly assignable option agreements** to tie up adjacent lots along Garrett Street, Eng
and Company can:

- secure a high-density footprint near a primary healthcare employment node,
- unlock a 3.00 FSR mid-rise profile,
- position itself to control a highly resilient asset class,
- **and exit via assignment** to a REIT or pension fund before final land closing,
  capturing the lift premium without holding title or paying double PTT.

---

## Appendix — Cross-References in This Wiki

- `clients/eng-and-company/README.md` — client profile, linked properties, source links
- `drafts/garrett-street-feasibility.md` — full feasibility study, 33k chars
- `drafts/garrett-health-district-dom.md` — DOM brief for the RCH health district
- `drafts/sapperton-district-feasibility.md` — broader Sapperton district feasibility
- `software-development/real-estate-option-agreement-metaprompt/SKILL.md` — the
  reusable prompt lifted to a skill

> The skills/ folder location for the lifted skill is `skills/software-development/real-estate-option-agreement-metaprompt/SKILL.md` (in-repo path; see the software-development authoring skill for placement).

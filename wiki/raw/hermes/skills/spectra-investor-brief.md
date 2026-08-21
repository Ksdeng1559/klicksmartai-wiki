---
name: spectra-investor-brief
description: Write an investor-ready brief for Spectra Holdings MCF pipeline. Feeds on census data from spectra-census-research.
trigger: /spectra-investor-brief
---

# /spectra-investor-brief

Write an investor-ready brief for Spectra Holdings Master Credit Facility pipeline.

## Prerequisites

Run `/spectra-census-research <county>, <state> --deliverable investor-brief` first to populate the census data file at `census/<county>-<state-abbrev>.md`.

## Usage

```
/spectra-investor-brief <county>, <state>
```

## Input

| Input | Description |
|-------|-------------|
| `county` | County name (must match census file) |
| `state` | Two-letter state code |

## Workflow

### 1. Read Census Data

Read `census/<county>-<state-abbrev>.md` to extract:
- Population, demographics, housing stock
- Affordability gap calculations
- Homelessness metrics
- CDFI landscape
- MCF intervention thesis

### 2. Structure the Brief

Follow this structure exactly:

**Header block:**
```
title: "<County Name, ST> — Investor Brief"
client: Spectra Holdings Group
scope: <City / County / Metro Area>
audience: Investors | Foundation Partners | CDFIs
tags: [<county>, <state>, investor-brief, mcf, spectra-holdings]
```

**Document sections:**

1. **Cover / Executive Summary** (1 page max)
   - Investment thesis in 3 bullet points
   - Key metrics at a glance (units gap, affordability gap, population)
   - Target return profile (if available)
   - Risk snapshot (top 3)

2. **Market Overview**
   - Population and growth trajectory
   - Housing supply deficit (units gap)
   - Why this market is structurally underserved

3. **The Affordability Crisis**
   - Quantified gap: what workforce earns vs. what housing costs
   - Who is impacted (rental vs. ownership, income tiers)
   - Trend direction (getting better or worse — be honest)

4. **Impact Metrics**
   - Homelessness baseline and trend
   - K-12 homeless students
   - Cost-burdened households
   - Eviction rate (if applicable)
   - Map each metric to ESG / PRI reporting categories

5. **CDFI / Financing Landscape**
   - Active CDFIs in county
   - Financing gap this project fills
   - Match with MCF structure

6. **Spectra Holdings MCF Opportunity**
   - Why Spectra / KlickSmartAI is the right capital partner
   - Project pipeline (if known — link to project file)
   - Community impact thesis

7. **Risk Factors** (be honest)
   - Market risks
   - Execution risks
   - Regulatory risks
   - Mitigation levers

8. **Appendix**
   - Data sources with full citations
   - Methodology notes

### 3. Writing Standards

- **Tone:** Professional, data-driven, fiduciary-grade
- **Lead with scale** — the investor needs to understand the magnitude of the problem before they can size the opportunity
- **Quantify everything** — "significant" is not a number. Say "115,125 units" not "tens of thousands"
- **Be honest about risk** — credibility is built by acknowledging risk, not hiding it
- **No faith framing in investor briefs** — save that for advertorials
- **Map impact to standard categories** — ESG Real Estate, PRI, IRIS+, or local equivalents
- **Max length:** 8–10 pages (excluding appendix)

### 4. Output

Save to: `clients/spectra-holdings/deliverables/<county>-<state>-investor-brief.md`

After saving:
```
cd ~/wiki && git add -A && git commit -m "deliverable: <county> investor brief" && git push origin master
```

---

## Pitfalls

- **Don't pad the impact section** — if the data is weak, say "data pending" rather than estimating
- **Don't mix advertorial and investor tones** — investor briefs are professional, not faith-framed
- **Don't skip the risk section** — investors will respect the honesty and it protects you legally
- **Don't cite stale data** — note the vintage of each data point

---

## Verification Steps

1. Census data file read and all 8 sections extracted
2. Brief has all 8 sections in correct order
3. Affordability gap is quantified (not just described)
4. Risk factors section is present and honest
5. All data claims have a source citation
6. Output saved to correct path
7. Git committed and pushed

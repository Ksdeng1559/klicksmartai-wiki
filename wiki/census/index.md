# Census Data — County Research Schema

> Standard schema for all county-level census briefs used in Spectra Holdings MCF pipeline.

---

## Required Sections

Every county brief must include:

### 1. Population
- Total population (most recent estimate)
- Growth rate (5-year, 10-year)
- Persons per household
- Foreign-born %
- Age distribution

### 2. Demographics
- Racial/ethnic breakdown
- Poverty rate
- Educational attainment
- Language other than English spoken at home

### 3. Housing Stock
- Total housing units
- Owner-occupied rate
- Rental vacancy rate (note: healthy = 5–7%)
- Owner vacancy rate (healthy = ~2%)
- Building permits issued (recent year)

### 4. Housing Costs & Affordability
- Median home value
- Median gross rent
- Rent by bedroom count (1-br, 2-br, 3-br)
- **Affordability gap** — calculate: what income supports the median mortgage/rent vs. actual median income
- % of renters cost-burdened (≥30% income on housing)
- % severely cost-burdened (≥50%)

### 5. Income & Economy
- Median household income
- Unemployment rate
- Poverty rate
- Income distribution by tier

### 6. Homelessness & Social Impact
- Point-in-Time Count (most recent)
- Sheltered vs. unsheltered breakdown
- Year-over-year trend
- Self-reported causes of homelessness
- K-12 homeless students (if available)
- System performance metrics (if available)

### 7. CDFI / Financing Landscape
- Active CDFIs in county
- Recent bond issuances or CMF awards
- LIHTC activity
- Opportunity Zone status
- State/county housing finance programs

### 8. The Affordability Gap (narrative)
- Quantified gap between what workforce earns and what they can afford
- Housing deficit in units
- Who's being priced out and why

### 9. MCF Intervention Thesis
- Why this county is a compelling MCF pilot market
- Demand drivers (structural vs. cyclical)
- Local partner / developer fit
- Faith-aligned impact metrics

---

## File Naming Convention

```
census/<county-name>-<state-abbrev>.md
census/whatcom-county-wa.md
census/bexar-county-tx.md
census/okaloosa-county-fl.md
```

---

## Frontmatter Schema

```yaml
---
title: "<County Name, ST> — Census & Housing Brief"
client: Spectra Holdings Group
scope: <City / County / Metro Area>
audience: Investor | Foundation Partner | MCF Due Diligence
tags: [<county>, <state>, census, demographics, housing, cdfi, affordable-housing]
sources:
  - id: 1
    name: "<Source Name>"
    url: "<URL>"
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
status: active | archived
---
```

---

## Approved Sources

| Source | URL | Use For |
|--------|-----|---------|
| U.S. Census QuickFacts | census.gov/quickfacts | Population, demographics, housing |
| Data USA | datausa.io | Income, education, diversity |
| ACS 5-Year Estimates | census.gov/programs-surveys/acs | Detailed demographics |
| Point-in-Time Count | CoC local reports | Homelessness |
| State/County Housing Reports | Local gov sites | Vacancy, permit, affordability |
| NLIHC Gap Report | nlihc.org | Housing deficit |
| Texas Housers / local advocates | State-specific | Eviction, displacement |

---

## Status

- [x] Whatcom County, WA — `census/whatcom-county-wa.md`
- [x] Bexar County, TX — `census/bexar-county-tx.md`
- [ ] _Next county_ — add above

---

**Maintained by:** Hermes (KlickSmartAI)
**Last updated:** 2026-05-09

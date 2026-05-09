---
name: spectra-census-research
description: Research and compile county-level census + housing data for Spectra Holdings MCF pipeline. Outputs advertorial, investor brief, and internal brief formats.
trigger: /spectra-census-research
---

# /spectra-census-research

Research and compile county-level census and housing data for Spectra Holdings MCF pipeline.

## Usage

```
/spectra-census-research <county>, <state> --deliverable <type> [--focus <areas>]
```

**Examples:**
```
/spectra-census-research Harris County, TX --deliverable investor-brief
/spectra-census-research Maricopa County, AZ --deliverable advertorial --focus homelessness
/spectra-census-research King County, WA --deliverable internal-brief
```

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `county` | Yes | Full county name | 
| `state` | Yes | Two-letter state code |
| `deliverable_type` | Yes | `investor-brief` \| `advertorial` \| `internal-brief` |
| `focus_areas` | No | Comma-separated: `homelessness,eviction,affordability,income` |

## Workflow

### Phase 1 — Source Discovery

Use sources in priority order:

```
1. U.S. Census QuickFacts → https://www.census.gov/quickfacts/fact/table/<county><state>
2. Data USA → https://datausa.io/profile/geo/<county>-county-<state>
3. ACS 5-Year Estimates → detailed demographics
4. State housing finance agency reports
5. Point-in-Time Count (CoC local reports)
6. Local housing coalition / advocacy orgs
7. NLIHC Gap Report → national context
```

Extract for each source: URL, access date, data vintage.

### Phase 2 — Data Extraction

Extract these 8 sections (see `census/index.md` in wiki for full schema):

**1. Population**
- Total population (most recent estimate)
- 5-year and 10-year growth rate
- Foreign-born %
- Median age
- Persons per household

**2. Demographics**
- Racial/ethnic breakdown (%)
- Poverty rate
- Educational attainment
- Language other than English

**3. Housing Stock**
- Total housing units
- Owner-occupied rate
- Rental vacancy rate (flag if below 5%)
- Building permits (recent year)

**4. Housing Costs & Affordability**
- Median home value
- Median gross rent
- Rent by bedroom count
- **Affordability gap** — calculate:
  - Income needed for median rent vs. actual median individual wage
  - Income needed for median home vs. actual median household income
- % renters cost-burdened (≥30%)
- % severely cost-burdened (≥50%)

**5. Income & Economy**
- Median household income
- Unemployment rate
- Poverty rate
- Income distribution by tier

**6. Homelessness & Social Impact**
- Point-in-Time Count (most recent)
- Sheltered vs. unsheltered breakdown
- YoY trend
- K-12 homeless students
- System performance metrics

**7. CDFI / Financing Landscape**
- Active CDFIs in county
- Recent bond/CMF awards
- LIHTC activity
- Opportunity Zone status

**8. The Affordability Gap (narrative)**
- Quantified gap narrative
- Who's being priced out and why

### Phase 3 — Deliverable Framing

**Advertorial**
- Lead with human impact story, not data
- Weave census data as supporting evidence
- Faith framing: Matthew 9:37, "the least of these" (Matt 25:35–46)
- Call to action: community investment, prayer, CDFI partnership
- Tone: hopeful, relational, kingdom-minded

**Investor Brief**
- Lead with market opportunity and scale of need
- Quantified investment thesis: units gap, affordability gap, demand drivers
- Risk factors honestly stated
- Impact metrics that map to ESG / PRI reporting
- Tone: professional, data-driven, fiduciary

**Internal Brief**
- Lead with project status and action items
- Data in structured tables, less narrative
- Delta flag: what changed since last brief
- Decision points and recommendations
- Tone: concise, operational, action-oriented

### Phase 4 — Write to Wiki

File naming: `census/<county-name>-<state-abbrev>.md`

Follow frontmatter schema in `census/index.md`.

After writing:
```
cd ~/wiki && graphify update .
git add -A && git commit -m "census: <county> county, <state>" && git push origin master
```

Update `census/index.md` status tracker.

### Phase 5 — Generate Output Doc

| Deliverable | Output Path |
|-------------|-------------|
| Advertorial | `clients/spectra-holdings/deliverables/<county>-advertorial.md` |
| Investor Brief | `clients/spectra-holdings/deliverables/<county>-investor-brief.md` |
| Internal Brief | `clients/spectra-holdings/deliverables/<county>-internal-brief.md` |

---

## Pitfalls

- **Don't cite QuickFacts alone** — cross-reference with ACS and local sources
- **Don't skip the affordability gap calculation** — core investor thesis
- **Eviction data is county-level** — check county vs. city/county distinction
- **PIT counts are undercounts** — note this explicitly
- **Rental vacancy below 5% = supply shortage** — don't frame as healthy market
- **Use county-specific income figures** — not regional/ metro medians for county-level analysis

---

## Verification Steps

1. All 8 sections populated from Phase 2
2. Affordability gap calculated (not just stated)
3. At least 5 sources cited
4. Frontmatter complete (title, client, scope, audience, tags, sources)
5. File saved to `census/<county>-<state>.md`
6. `census/index.md` status tracker updated
7. Graph updated (`graphify update .`)
8. Git pushed to origin/master
9. Deliverable document saved to correct output path

---

## Related Skills

- `spectra-advertorial` — write advertorial from census data
- `spectra-investor-brief` — write investor brief from census data  
- `spectra-internal-brief` — write internal brief from census data

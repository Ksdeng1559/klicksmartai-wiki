---
name: spectra-census-research
description: "SOP for Step 1 of the Spectra Holdings county pipeline: Census & Housing research for MCF county due diligence. Outputs census/<county>-<ST>.md. Depends on no other skills."
owner: Dennis
category: project
triggers:
  - /spectra-census-research
  - run census on
  - pull county census data
  - Spectra county research
---

# spectra-census-research

Execute Step 1 of the Spectra Holdings MCF county pipeline: produce a quantitative census and housing brief for a target county.

**Output:** `census/<county>-<ST>.md` — feeds into Step 2 (social intelligence) and all downstream deliverables.

---

## Pre-Check: Enumerate Known County Facts First

Before running any search, open the wiki census index and check whether this county already has a research file:

```
read_file: wiki/census/index.md
```

If the county already exists, read the existing file and treat it as the baseline — patch only the sections that are stale or missing. Do not rewrite from scratch.

---

## Source Priority Order

| Priority | Source | What It Covers | Cost | Library / Tool |
|----------|--------|---------------|------|----------------|
| 1st | Wikipedia API via `wikipedia-api` lib | Historical census (2000/2010/2020), population, age, housing units | Free | `pip install wikipedia-api` |
| 2nd | Exa deep search | ACS income, housing costs, rent, poverty — synthesized with citations | Free tier | `mcp_exa_deep_search_exa` |
| 3rd | DataUSA | Cross-cut income, housing, employment by county | Free | Web search |
| 4th | Census ACS 5-Year via curl | Income, rent, affordability — direct API call | Requires free Census API key | `curl` |
| 5th | State portal / county open data | Supplemental housing / permit data | Free | Web search |

**Wikipedia API setup:**
```python
import wikipediaapi
wiki = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)
page = wiki.page(f"{county_name} County, Washington")
print(page.text)  # full wiki section dump
```

**Wikipedia API failure mode:** Wikipedia County pages typically only have decennial census data (2000/2010/2020). For current-year ACS estimates (MHI 2024, rent burden, affordability), always fall through to Exa synthesis as the 2nd priority.

**Do not use Firecrawl** — exhausts credits on government domains with no gain over Wikipedia API.

---

## Step-by-Step SOP

### Step A — County FIPS + Wikipedia Baseline

1. **Find the Wikipedia page** for the county:
```
web_search: {County Name} {State} county wikipedia demographics
```

2. **Extract via Wikipedia API:**
```
https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext&titles={County_Name},_{State}&format=json
```

3. **Extract via Wikipedia API for the county seat city** (richer housing data):
```
https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext&titles={City_Name},_{State}&format=json
```

4. **Parse the response** — pull:
   - Population: 2020, 2010, 2000 (directionally check growth)
   - Median age
   - Housing units total
   - Homeownership rate
   - Median home value
   - Median household income (MHI)

### Step B — ACS Income + Housing (Exa)

Run a single deep Exa search covering the county's current ACS profile:

```
search_queries:
  - "{County Name} county {State} median household income 2023 2024"
  - "{County Name} county {State} median home value 2024"
  - "{County Name} county {State} housing affordability gap 2024"
  - "{County Name} county {State} poverty rate rent burden 2024 ACS"
```

Synthesize results into structured data. Flag every figure with its source URL.

### Step C — Affordability Gap Calculation

If you have MHI and median rent or median home value, compute the ratio:

**Rent-to-income ratio:**
```
rent burden % = (median rent × 12) / MHI × 100
```

If ratio > 30%: housing cost-burdened. If > 50%: severely cost-burdened.

**Homeownership affordability (assuming 30-year, 7% conventional):**
```
Max affordable purchase price ≈ MHI × 3.0 (conventional rule of thumb)
Gap = median home value − (MHI × 3.0)
```

### Step D — Corridor / Sub-Area Data (if applicable)

For the Semiahmoo–Birch Bay–Blaine corridor or similar sub-areas:
1. Search each city/CDP separately via Wikipedia API
2. Search corridor-level data via Exa with "growth corridor" framing
3. Aggregate at the corridor level — do not average; report the range

### Step E — Homeless + Eviction Baseline

Run Exa searches:
```
search_queries:
  - "{County Name} county {State} point-in-time count homeless 2024"
  - "{County Name} county {State} eviction rate filing 2023"
```

Pull from:
- HUD Continuum of Care Point-in-Time Count (annual, late Jan)
- Eviction Lab at Princeton (evictionrate.org) — free CSV download

---

## Output Format

Write to: `census/<county>-<ST>.md`

```markdown
---
county: Whatcom County
state: WA
fips: "53073"
research-date: 2025-05-12
sources: [Wikipedia API, DataUSA 2024, ACS 5-Year 2023, Exa synthesis]
corridor: Semiahmoo-Birch Bay-Blaine
---

# Census Brief — Whatcom County, WA

## 1. Population & Growth

| Year | Population | Change | Source |
|------|-----------|--------|--------|
| 2020 | 234,954 | +7.2% from 2010 | Wikipedia/2020 Census |
| 2010 | 219,189 | +9.1% from 2000 | Wikipedia/2010 Census |
| 2000 | 200,798 | — | Wikipedia/2000 Census |

**County seat:** Bellingham (92,314, 2020)

## 2. Demographics

| Metric | Value | Source |
|--------|-------|--------|
| Median age | 37.8 | 2020 Census |
| Under 18 | 20.3% | 2020 Census |
| Over 65 | 17.1% | 2020 Census |
| Non-white | 18.6% | 2020 Census |

## 3. Income & Economy

| Metric | Value | Source |
|--------|-------|--------|
| MHI (2023 ACS 5-yr) | $81,784 | DataUSA / Exa synthesis |
| Per capita income | $38,250 | 2023 ACS 5-yr |
| Poverty rate | 12.9% | 2023 ACS 5-yr |
| Median home value | $585,800 | 2024 Exa synthesis |
| Median gross rent | $1,465/mo | 2023 ACS 5-yr |
| Rent burden (>30% income) | 21.7% | ACS-derived |

## 4. Housing Stock

| Metric | Value | Source |
|--------|-------|--------|
| Total housing units | 101,340 | 2020 Census |
| Homeownership rate | 63.7% | 2023 ACS 5-yr |
| Vacancy rate | 8.3% | 2020 Census |
| Seasonal/recreation vacancy | ~25-26% in Birch Bay | Exa synthesis |

## 5. Affordability Gap

- **Max affordable purchase price** (MHI x 3.0 rule): $245,352
- **Median home value:** $585,800
- **Gap:** $340,448 -- homeownership gap is 2.4x the conventional threshold
- **Rent-burdened households:** 21.7% of renters pay >30% income on rent
- **Severe housing problems** (overcrowded, lacking kitchen/plumbing, cost-burdened): 19.2%

## 6. Homelessness + Eviction

| Metric | Value | Source |
|--------|-------|--------|
| PIT Count (2024) | ~600-700 range | CoC report / Exa |
| Eviction rate | ~2.1/1000 renter households | Eviction Lab |

## 7. Corridor-Level Data — Semiahmoo-Birch Bay-Blaine

| Place | Pop (2020) | Change since 2019 | MHI | Median Home |
|-------|-----------|------------------|-----|-------------|
| Blaine | 6,606 | +12.3% | ~$72,000 | ~$415,000 |
| Birch Bay CDP | ~8,700 | +15%+ | $86,854 | $439,100 |
| Semiahmoo Spit | -- | -- | -- | ~$500K+ (vacation) |

**Key dynamic:** Short-term rental capture removes ~18% of Semiahmoo housing from long-term market. Birch Bay vacancy ~25-26% is seasonal second-home stock.

## 8. Data Gaps

- [ ] ACS 2023 5-year income/housing data requires Census Bureau API key (api.census.gov -- free) for direct pull
- [ ] 2024 point-in-time homeless count requires local CoC report or HUD exchange
- [ ] Sub-CDP (Birch Bay) has no separate Census block -- figures are approximations from CDPs and surveys

## Source References

[#1] Wikipedia -- Whatcom County, Washington (2020 Census data)
[#2] DataUSA 2024 -- Whatcom County, WA (ACS cross-cuts)
[#3] Exa synthesis -- ACS income, housing, rent burden 2023-2024
[#4] World Population Review / Neilsberg -- Birch Bay CDP data
```

---

## Required Data Points

Every `census/<county>-<ST>.md` must contain:

- Population: 2020, 2010, 2000 (with % change)
- Median household income (with year and source)
- Median home value (with year and source)
- Median gross rent (with year)
- Homeownership rate
- Rent burden % (computed or sourced)
- Affordability gap (home price vs. MHI x 3.0)
- Vacancy rate (and seasonal/second-home note if applicable)
- Poverty rate
- Homeless estimate (PIT count, year)
- Any available sub-area / corridor data

If any field is unavailable, write `[DATA GAP -- source needed]` in that cell and add a note in Section 8 (Data Gaps).

---

## Post-Write Protocol

After writing the census file:

1. **Write to wiki:** `wiki/census/<county>-<ST>.md` -- canonical source
2. **Copy to clients:** `clients/spectra-holdings/research/census/<county>-<ST>.md` -- working copy
3. **Git commit + push:**
```bash
cd ~/wiki && git add -A && git commit -m "census: {County Name}, {ST}" && git push origin master
```
4. **Update the RYG test status** -- mark the census output test as YELLOW once file exists with partial data, GREEN once all Required Data Points are filled.

---

## Failure Modes

| Symptom | Fix |
|---------|-----|
| Wikipedia page has no demographics section | Try the county page instead of the city page; fall back to Census QuickFacts |
| Exa returns no income data for a small county | Use DataUSA directly; fallback to ACS via curl if key is available |
| ACS income missing (Census API key not available) | Flag as data gap, use 2020 Census income as placeholder, note vintage |
| No sub-area data for a corridor | Aggregate from individual city Wikipedia pages; note as approximation |
| Gap calculation produces negative number | Median home value may be below MHI x 3.0 in rural counties -- report as "homeownership within reach" not a gap |

---

## Integration with spectra-pipeline

This skill is Step 1. After completion:

1. Mark test `test_county_census_file_exists` as YELLOW/GREEN
2. Proceed to `spectra-social-intelligence` (Step 2) -- social intelligence file depends on this census file existing
3. Do not run any deliverable skill (investor brief, advertorial, etc.) until both Step 1 and Step 2 are complete

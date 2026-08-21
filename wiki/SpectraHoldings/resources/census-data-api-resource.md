# Census Data API Resource for Spectra Holdings

## Purpose

The U.S. Census API should become Spectra Holdings' structured demographic and housing data layer for county intelligence, investor presentations, municipal briefings, landowner outreach, and Master Credit Facility underwriting.

This resource supports the Spectra intelligence workflow:

**INPUT → MODEL → VALIDATION → DECISION → OUTPUT**

The Census API is not just a research tool. It is the quantitative truth layer that helps Spectra determine where housing demand exists, where affordability pressure is highest, where workforce housing is most defensible, and where public-private partnership narratives can be supported with data.

---

## Strategic Use Case

Spectra Holdings positions itself as a vertically integrated community development platform capable of delivering housing, jobs, infrastructure, and local economic impact at scale. Census data strengthens this position by providing repeatable county-level evidence for:

- Housing demand
- Population pressure
- Income affordability gaps
- Rent burden
- Homeownership constraints
- Workforce demographics
- Poverty and low-to-moderate-income indicators
- Vacancy and housing supply weakness
- Municipal redevelopment need
- Investor-grade market feasibility

This directly supports:

- Market Intelligence Engine
- Deal Intelligence Engine
- Capital Stack Engine
- Master Credit Facility Engine
- County Intelligence Reports
- Investor and family office presentations
- NCF / faith-based impact capital narratives
- Municipal and landowner presentations

---

## Primary Census API Endpoint

Use ACS 5-Year data first because it is the most useful for county-level and smaller-area analysis.

Base endpoint:

```txt
https://api.census.gov/data/2024/acs/acs5
```

Example county query for Washington State:

```txt
https://api.census.gov/data/2024/acs/acs5?get=NAME,B01003_001E,B19013_001E,B25077_001E,B25064_001E&for=county:*&in=state:53&key=YOUR_API_KEY
```

Important: Census API keys are required for production usage. Store the key as an environment variable, not in source code.

Recommended environment variable:

```txt
CENSUS_API_KEY=
```

---

## Core Variables for Spectra County Intelligence

### Population and Demand

| Field | Census Variable | Purpose |
|---|---:|---|
| Total Population | B01003_001E | Baseline market size |
| Total Households | B11001_001E | Demand base for housing units |
| Population 18+ | B01001_026E+ | Adult population / workforce proxy |

### Income and Affordability

| Field | Census Variable | Purpose |
|---|---:|---|
| Median Household Income | B19013_001E | Affordability benchmark |
| Per Capita Income | B19301_001E | Economic capacity |
| Poverty Count | B17001_002E | LMI / impact need |
| Poverty Universe | B17001_001E | Poverty rate denominator |

### Housing Market

| Field | Census Variable | Purpose |
|---|---:|---|
| Median Home Value | B25077_001E | Ownership affordability |
| Median Gross Rent | B25064_001E | Rental affordability |
| Occupied Housing Units | B25003_001E | Housing stock base |
| Owner-Occupied Units | B25003_002E | Ownership penetration |
| Renter-Occupied Units | B25003_003E | Rental market depth |
| Vacant Units | B25002_003E | Supply and absorption signal |

### Workforce and Commuting

| Field | Census Variable | Purpose |
|---|---:|---|
| Workers 16+ | B08301_001E | Workforce base |
| Mean Travel Time to Work | B08303_001E | Commuting burden / workforce housing need |
| Worked from Home | B08301_021E | Remote-work share |

### Education and Readiness

| Field | Census Variable | Purpose |
|---|---:|---|
| High School Graduate or Higher | B15003 selected variables | Workforce readiness |
| Bachelor's Degree or Higher | B15003 selected variables | Economic capacity / employer attraction |

---

## Derived Metrics to Generate

Each county pull should calculate standardized derived metrics.

### Housing Affordability Metrics

- Median rent as percentage of median household income
- Median home value to median household income ratio
- Owner occupancy rate
- Renter occupancy rate
- Vacancy rate
- Poverty rate
- Estimated workforce housing stress score

### Spectra Market Feasibility Indicators

- Population scale score
- Affordability pressure score
- Housing supply weakness score
- Workforce housing need score
- LMI impact score
- PPP alignment score
- Investor narrative strength score

---

## Standard Workflow

### 1. INPUT

Required county inputs:

- State name
- State FIPS code
- County name
- County FIPS code
- Target asset type
- Proposed unit count
- Intended stakeholder audience

### 2. MODEL

Pull Census data through ACS 5-Year API.

Normalize variable names into a standard schema:

```json
{
  "county_name": "",
  "state_fips": "",
  "county_fips": "",
  "population_total": 0,
  "median_household_income": 0,
  "median_home_value": 0,
  "median_gross_rent": 0,
  "occupied_units": 0,
  "owner_occupied_units": 0,
  "renter_occupied_units": 0,
  "vacant_units": 0,
  "poverty_count": 0,
  "poverty_universe": 0,
  "source_year": "2024 ACS 5-Year"
}
```

### 3. VALIDATION

Validation rules:

- Confirm state and county FIPS match the county name
- Flag null, negative, suppressed, or margin-of-error-sensitive values
- Store source endpoint used
- Store pull date
- Compare against prior pull if available
- Document any missing fields

### 4. DECISION

Every county report must answer:

- Is there sufficient population and household demand?
- Is affordability pressure strong enough to support workforce housing?
- Does the county support an investor-grade housing thesis?
- Is there a public-private partnership angle?
- Does the data support Spectra's vertical integration value proposition?
- Does this county deserve deeper underwriting?

### 5. OUTPUT

Outputs should include:

- County Intelligence Report
- Investor Market Slide
- Municipal Briefing Slide
- Landowner Opportunity Narrative
- NCF / impact capital alignment memo
- JSON data object for model ingestion
- CSV export for portfolio comparison

---

## Integration with Spectra Systems

### Market Intelligence Engine

Census data feeds the market feasibility score and demand forecast.

### Deal Intelligence Engine

Census data supports absorption assumptions, price/rent validation, and downside risk.

### Capital Stack Engine

Census data supports grant, CDFI, NMTC, municipal bond, and impact capital narratives.

### Master Credit Facility Engine

Census data helps prioritize counties where recycled capital can be deployed repeatedly with defensible demand.

### WhyNow Engine

Census data becomes the factual backbone behind county-specific advertorials and public-private partnership narratives.

---

## Recommended Technical Implementation

Create a reusable module:

```txt
/spectra-intelligence/data_sources/census_api_client.py
```

Functions:

```python
get_county_profile(state_fips: str, county_fips: str) -> dict
get_state_counties(state_fips: str) -> list
calculate_affordability_metrics(profile: dict) -> dict
score_market_feasibility(profile: dict) -> dict
export_county_profile(profile: dict, format: str = "json")
```

Recommended storage:

- Development: JSON + CSV
- Lightweight analytics: DuckDB / MotherDuck
- Enterprise scale: Snowflake
- App layer: Supabase

---

## Governance Rules

- Every variable must retain its Census code.
- Every data pull must retain endpoint, year, and pull date.
- Every derived metric must be calculated consistently across counties.
- No investor presentation should use Census figures without source year and geography.
- All county comparisons must use the same ACS year.
- API keys must not be committed to GitHub.

---

## Decision Standard

A county should advance to deeper Spectra underwriting when it shows:

- Clear housing affordability pressure
- Meaningful household or population base
- Evidence of workforce or LMI need
- Public-private partnership potential
- Alignment with Spectra vertical integration advantages
- Ability to support repeatable capital deployment through the MCF

---

## Next Build Tasks

1. Create Census API key and store it securely.
2. Build `census_api_client.py`.
3. Create standard Spectra variable map.
4. Build county profile JSON output.
5. Add derived affordability and feasibility metrics.
6. Create a county comparison table.
7. Connect outputs to Spectra County Intelligence Reports.
8. Prepare Codex task to implement and test the module.

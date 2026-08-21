# Spectra Holdings Search Capability TDD Requirements

## Purpose

This document defines the test-driven development requirements for Spectra Holdings' external research stack.

The goal is to test search-engine capability before relying on any tool for investor-facing, municipal-facing, or Master Credit Facility research outputs.

Core rule:

**Every search engine must be tested against a known research task, scored against expected output, and routed only to the work it is best suited to perform.**

---

## System Objective

Build a repeatable county intelligence research system that can answer:

- Which data source should be used?
- Which search engine is best for this task?
- Did the tool return current, cited, usable information?
- Did it fill the actual data gap?
- Is the output strong enough for investor or municipal use?
- Should the result trigger a Spectra decision?

---

## Search Stack Routing Doctrine

Search tools are not interchangeable.

Each tool must have a defined job.

| Tool | Primary Role | Should Be Used For | Should Not Be Used For |
|---|---|---|---|
| Census API | Structured quantitative data | ACS variables, population, income, housing units, affordability metrics | Narrative synthesis or news discovery |
| Exa.ai | Lead research engine for geographic and census-adjacent research | Current demographic summaries, housing stats, municipal reports, hard-to-find data pages | Bulk SERP scraping only |
| Brave Search | Broad discovery | News, web discovery, local policy mentions, broad source finding | Final source-of-truth data without validation |
| Serper.dev | Google-style validation | Confirming official sources, News, Maps/Places, government pages | Deep synthesis or semantic matching |
| Tavily | Cited extraction and research summaries | Source-backed summaries, research briefs, policy extraction | Raw monitoring or bulk crawling |
| Firecrawl | Website crawling and extraction | County websites, planning pages, agendas, PDF archives | Open-ended web search |
| Parallel.ai | Persistent monitoring and raw web signal discovery | Ongoing alerts, signal streams, RFPs, council agenda monitoring, bulk result discovery | Structured ACS/census demographic retrieval |
| Perplexity / AI answer engines | Early orientation | Fast overview, question framing | Final investor-facing source of truth |

---

## Key Lesson from Whatcom County Test

### Finding

Parallel.ai did not necessarily fail. It was routed to the wrong job.

The task was:

> Pull current ACS / demographic / housing / income data for Whatcom County and corridor-level communities such as Blaine and Birch Bay.

This is a structured, geography-specific, data-gap-filling task.

Exa.ai performed better because:

- It found current demographic and housing pages.
- It handled semantic research better than flat keyword search.
- It returned content snippets and citations.
- It filled specific data gaps, including updated Birch Bay income and Whatcom County income figures.
- It was more useful for geographic and census-adjacent research.

Parallel.ai is better suited for monitoring and signal detection, not primary ACS-style demographic retrieval.

### Routing Conclusion

For county census / demographic data:

**Census API first → Exa.ai second → Serper/Brave validation → Tavily extraction → Firecrawl if source site requires crawling.**

For ongoing county change detection:

**Parallel.ai becomes the monitoring layer after the baseline county profile is established.**

---

## TDD Philosophy

Each search capability must be tested using:

1. A known research question
2. Expected fields
3. Expected sources
4. Known benchmark data
5. Pass/fail criteria
6. Routing decision
7. Recommended usage classification

No tool should be labeled good or bad generally. Each tool should be rated by task class.

---

# Test Suite 1: County Demographic Retrieval

## Test ID

`SEARCH-TDD-001`

## Objective

Determine which tool can best retrieve current county-level demographic, income, and housing data.

## Benchmark County

Whatcom County, Washington

## Required Fields

- County population
- Median household income
- Median home value
- Median rent
- Poverty rate
- Homeownership rate
- Rent or housing cost burden
- Source year
- Source URL
- Confidence rating

## Primary Expected Source Types

- U.S. Census ACS
- Data USA
- FRED
- World Population Review
- Neilsberg
- IncomeByCounty
- Census Reporter
- Official county or state sources if available

## Tool Routing Expectation

| Tool | Expected Result |
|---|---|
| Census API | Pass for structured county data |
| Exa.ai | Pass for semantic discovery and current source identification |
| Serper.dev | Pass for validation |
| Brave Search | Partial pass for broad discovery |
| Tavily | Pass for cited synthesis after source discovery |
| Firecrawl | Pass only if crawling official pages/PDFs |
| Parallel.ai | Partial/fail for initial demographic retrieval, pass for monitoring |

## Pass Criteria

A tool passes if it returns:

- At least 6 of 8 required fields
- Source URLs
- Source year
- Current or clearly dated information
- No obvious 2000-era or stale data presented as current
- Data usable in a county intelligence report

## Fail Criteria

A tool fails if it:

- Returns generic snippets without usable data
- Cannot identify source year
- Confuses county and city geographies
- Uses stale historical values without warning
- Provides no direct source URLs
- Cannot fill the stated data gap

---

# Test Suite 2: Corridor-Level Community Data

## Test ID

`SEARCH-TDD-002`

## Objective

Test ability to retrieve sub-county community-level data.

## Benchmark Communities

- Blaine, Washington
- Birch Bay, Washington
- Semiahmoo / coastal corridor if available

## Required Fields

- Population
- Median household income
- Median home value
- Median rent if available
- Growth trend
- Source year
- Source URL
- Data quality note

## Whatcom Benchmark Observations

Known findings from recent Exa research:

- Blaine population: approximately 6,606
- Birch Bay population: approximately 10,837 to 12,367 depending on source
- Combined corridor: approximately 17,500 to 19,000 people
- Birch Bay MHI: approximately $77,120 to $86,854 depending on source
- Birch Bay median home value: approximately $439,100
- Blaine city income profile remains a known data gap; county-wide proxy may be needed

## Expected Tool Performance

| Tool | Expected Result |
|---|---|
| Exa.ai | Best for filling sub-county data gaps |
| Serper.dev | Good for validation and source confirmation |
| Brave Search | Useful for broad discovery |
| Census API | Useful if geography codes are available |
| Tavily | Good for synthesis after source discovery |
| Parallel.ai | Not ideal for first-pass retrieval |
| Firecrawl | Useful if community profile pages need extraction |

---

# Test Suite 3: Municipal Agenda / Planning Signal Detection

## Test ID

`SEARCH-TDD-003`

## Objective

Determine which tool detects current county/city planning signals.

## Required Signals

- County council agenda mentioning housing
- Planning commission agenda
- Housing RFP / RFQ
- Infrastructure funding notice
- Municipal bond discussion
- Zoning or comprehensive plan update
- Public-private partnership opportunity

## Expected Tool Routing

| Tool | Expected Result |
|---|---|
| Parallel.ai | Pass for persistent monitoring |
| Firecrawl | Pass for crawling agenda portals |
| Serper.dev | Pass for search validation |
| Brave Search | Pass for broad discovery |
| Exa.ai | Partial pass for semantic discovery |
| Tavily | Pass for cited extraction after page identification |
| Census API | Not applicable |

## Pass Criteria

A tool passes if it returns:

- Current or dated agenda/source
- URL
- Signal category
- Why-now explanation
- Recommended Spectra action

---

# Test Suite 4: Incentives and Capital Stack Research

## Test ID

`SEARCH-TDD-004`

## Objective

Test ability to discover and validate local, state, federal, and alternative capital programs.

## Required Program Types

- CDBG
- HOME
- HUD programs
- USDA rural housing or infrastructure programs
- EDA grants
- FEMA disaster resilience funding
- Municipal bonds
- Tax increment financing if applicable
- Opportunity Zones
- CDFI activity
- NMTC
- Housing trust funds
- Faith-based / donor-advised impact capital alignment

## Expected Tool Routing

| Tool | Expected Result |
|---|---|
| Exa.ai | Strong for semantic policy discovery |
| Serper.dev | Strong for official validation |
| Brave Search | Good for broad discovery |
| Tavily | Strong for cited program summaries |
| Firecrawl | Strong for official program pages and PDFs |
| Parallel.ai | Good for monitoring new funding announcements |
| Census API | Supports eligibility narrative, not program discovery |

---

# Test Suite 5: Investor Narrative Evidence

## Test ID

`SEARCH-TDD-005`

## Objective

Test whether search tools can generate evidence that supports investor-facing narratives.

## Required Evidence Categories

- Housing demand
- Affordability pressure
- Supply constraints
- Workforce housing need
- Economic development priorities
- Disaster resilience need
- Public-private partnership opportunity
- Capital stack support
- Spectra differentiation

## Pass Criteria

A tool passes if it provides:

- Source-backed facts
- Clear source hierarchy
- Current dates
- Strategic interpretation
- Stakeholder-specific relevance
- No unsupported claims

---

## Standard TDD Output Format

Every tool test should produce this structure:

```json
{
  "test_id": "SEARCH-TDD-001",
  "tool": "Exa.ai",
  "county": "Whatcom County, WA",
  "task_class": "county_demographic_retrieval",
  "date_tested": "YYYY-MM-DD",
  "required_fields_returned": 8,
  "required_fields_total": 8,
  "source_urls_returned": true,
  "source_years_returned": true,
  "data_gap_filled": true,
  "stale_data_flagged": true,
  "routing_recommendation": "lead_engine_for_geographic_research",
  "result": "pass",
  "notes": "Exa found current ACS-adjacent and source-backed demographic/housing data."
}
```

---

## Scoring System

Score each tool per test class using 100 points.

| Category | Points |
|---|---:|
| Data completeness | 25 |
| Source quality | 20 |
| Recency | 15 |
| Geographic precision | 15 |
| Citation / URL quality | 10 |
| Data gap resolution | 10 |
| Investor-readiness | 5 |

## Score Bands

| Score | Classification |
|---:|---|
| 85–100 | Primary tool for this task |
| 70–84 | Strong supporting tool |
| 50–69 | Validation or backup tool |
| 30–49 | Not recommended except narrow use |
| 0–29 | Fail for this task |

---

## Tool Capability Matrix Template

| Task Class | Census API | Exa | Brave | Serper | Tavily | Firecrawl | Parallel |
|---|---:|---:|---:|---:|---:|---:|---:|
| County demographics | Primary | Primary | Support | Validate | Support | Conditional | Not primary |
| Sub-county data | Conditional | Primary | Support | Validate | Support | Conditional | Not primary |
| Municipal agendas | N/A | Support | Support | Validate | Support | Primary | Primary |
| Incentive discovery | Support | Primary | Support | Validate | Primary | Primary | Monitor |
| News monitoring | N/A | Support | Support | Support | Support | Conditional | Primary |
| Investor narrative evidence | Support | Primary | Support | Validate | Primary | Conditional | Support |
| Website/PDF extraction | N/A | Support | N/A | N/A | Support | Primary | N/A |

---

## Required Benchmark Tasks

To validate the research stack, run each tool against these benchmark tasks:

### Benchmark 1: Whatcom County Baseline

```txt
Find the latest population, median household income, median home value, median rent, poverty rate, homeownership rate, and rent/housing burden for Whatcom County, Washington. Include source year and URLs.
```

### Benchmark 2: Blaine / Birch Bay Corridor

```txt
Find current population, median household income, median home value, and growth indicators for Blaine, WA and Birch Bay, WA. Identify any data gaps and whether county-level proxies are required.
```

### Benchmark 3: Whatcom Housing Policy

```txt
Find official Whatcom County or City of Blaine planning documents, housing plans, council agendas, or economic development sources that mention housing supply, workforce housing, affordable housing, redevelopment, or infrastructure.
```

### Benchmark 4: Capital Stack Programs

```txt
Find available federal, state, county, municipal, CDFI, Opportunity Zone, grant, bond, or housing incentive programs that could support workforce housing or community redevelopment in Whatcom County, Washington.
```

### Benchmark 5: Monitoring Signal

```txt
Monitor Whatcom County and Blaine/Birch Bay for new housing-related RFPs, council agenda items, planning commission updates, zoning changes, municipal bond notices, grant announcements, and economic development signals.
```

---

## Expected Routing After Testing

Initial expected routing based on current evidence:

1. **Census API** = structured baseline demographics
2. **Exa.ai** = lead engine for geographic/census-adjacent data discovery
3. **Serper.dev** = Google validation and official source confirmation
4. **Brave Search** = broad discovery
5. **Tavily** = cited synthesis and brief generation
6. **Firecrawl** = county website and PDF extraction
7. **Parallel.ai** = monitoring and signal detection, not first-pass census retrieval

---

## Definition of Done

The search capability testing project is complete when:

- Each tool has been tested against all benchmark tasks
- Each tool has a score by task class
- Routing rules are confirmed or corrected
- Failure cases are documented
- At least one county intelligence report can be generated using the full workflow
- All outputs include source URLs and dates
- The system can explain why one tool was used instead of another
- The workflow supports go / no-go decisions for Spectra

---

## Final Decision Principle

A tool does not fail because it performs poorly on the wrong job.

A tool fails only when it performs poorly on the job it is supposed to do.

The Spectra system must therefore test tools by task class, not by general reputation.

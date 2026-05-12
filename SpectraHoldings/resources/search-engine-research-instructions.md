# Spectra Holdings Search Engine Research Instructions

## Purpose

This document defines how Spectra Holdings should use external search engines, extraction tools, and structured APIs to produce repeatable county intelligence, investor-ready narratives, municipal briefing materials, landowner outreach, and Master Credit Facility support research.

The goal is not random internet research. The goal is to operate a standardized intelligence system that converts public information into defensible decisions.

Core workflow:

**INPUT → SEARCH → EXTRACT → VALIDATE → SCORE → DECISION → OUTPUT**

Every search should support one or more of the following decisions:

- Should Spectra pursue this county?
- Is there housing demand?
- Is there a public-private partnership angle?
- Is there landowner or developer opportunity?
- Is there investor-grade market evidence?
- Is there capital stack support through grants, bonds, CDFIs, DAFs, or municipal programs?
- Does this market support Master Credit Facility deployment?

---

## Search Stack Overview

| Tool | Primary Use | Best For |
|---|---|---|
| Census API | Structured demographic data | Population, income, housing, affordability |
| Brave Search | Broad discovery | News, county pages, development activity, general web intelligence |
| Serper.dev | Google-style search validation | Search, News, Places, Maps-style discovery |
| Tavily | AI-ready research extraction | Summaries, citations, focused research briefs |
| Exa.ai | Semantic discovery | Finding conceptually similar pages, policy documents, obscure reports |
| Parallel.ai | Persistent monitoring | Ongoing county/project/news signal tracking |
| Firecrawl | Website crawling and extraction | County websites, planning pages, PDFs, meeting agendas |
| Perplexity / AI answer engines | Fast synthesis only | Early orientation, not final source of record |

---

## Golden Rule

Use tools in layers:

1. **Census API** for structured quantitative facts.
2. **Search engines** for discovery.
3. **Firecrawl / Tavily / Exa** for extraction and source capture.
4. **Parallel** for ongoing monitoring.
5. **Human or AI validation** before investor-facing use.

Do not rely on a single tool as the final source of truth.

---

# 1. Census API Instructions

## Role

Census API is the quantitative truth layer.

Use it to support:

- Population size
- Household formation
- Median income
- Rent burden
- Home values
- Poverty / low-to-moderate-income indicators
- Occupancy and vacancy
- Workforce housing need

## Prompt / Task Template

```txt
Pull the latest ACS 5-Year Census data for [COUNTY], [STATE].

Return:
- Total population
- Total households
- Median household income
- Median home value
- Median gross rent
- Owner-occupied units
- Renter-occupied units
- Vacant housing units
- Poverty count and poverty rate
- Workforce / commuting indicators if available

Normalize output into JSON using Spectra's county intelligence schema.
Include variable codes, source year, endpoint used, and pull date.
Then calculate affordability pressure, vacancy rate, ownership rate, renter share, and workforce housing stress.
```

## Output Required

- JSON county profile
- CSV row for comparison table
- Short investor narrative
- Municipal briefing bullets

---

# 2. Brave Search Instructions

## Role

Brave Search is the broad discovery engine.

Use Brave to find:

- County housing plans
- Local news
- Economic development activity
- Planning commission updates
- Municipal agendas
- Development incentives
- Public-private partnership opportunities
- Disaster recovery needs
- Local infrastructure gaps

## Search Prompt Template

```txt
Research [COUNTY], [STATE] for Spectra Holdings' county intelligence report.

Find public information related to:
- Housing shortage or affordability issues
- Workforce housing needs
- County or city redevelopment plans
- Planning commission or council discussions
- Economic development priorities
- Available land, vacant land, or underutilized land
- Infrastructure needs
- Disaster resilience or recovery needs
- Incentives, grants, municipal bonds, CDBG, HOME, NMTC, CDFI, or Opportunity Zone references

Prioritize official county/city sources, planning documents, recent news, and economic development agencies.
Return title, URL, date, source type, summary, and why it matters to Spectra.
```

## Query Examples

```txt
[COUNTY] [STATE] housing needs assessment workforce housing
[COUNTY] [STATE] comprehensive plan housing affordability
[COUNTY] [STATE] economic development strategic plan
[COUNTY] [STATE] planning commission housing development agenda
[COUNTY] [STATE] affordable housing grants CDBG HOME
[COUNTY] [STATE] opportunity zone map redevelopment
[COUNTY] [STATE] disaster recovery housing resilience
```

## Best Output

A source table with:

- Source title
- URL
- Source type
- Date
- Key finding
- Spectra relevance
- Confidence level

---

# 3. Serper.dev Instructions

## Role

Serper.dev is the Google-style validation and search expansion layer.

Use Serper when you need:

- Search result validation
- Google News-style recency checks
- Local business / map-style discovery
- County government pages
- Economic development organizations
- Developer, builder, and landowner discovery

## Search Prompt Template

```txt
Use Serper.dev to validate and expand research for [COUNTY], [STATE].

Search for official and recent sources related to:
- Housing affordability
- Workforce housing
- County redevelopment
- Development incentives
- Public-private partnerships
- Economic development agencies
- Planning commission agendas
- Opportunity Zones
- CDBG / HOME / municipal bond programs
- Land development activity

Return only source-backed results with title, URL, date if available, snippet, and category.
Flag official government sources separately from media sources.
```

## Query Examples

```txt
site:.gov [COUNTY] [STATE] housing plan
site:.gov [COUNTY] [STATE] planning commission agenda housing
site:.gov [COUNTY] [STATE] CDBG HOME housing
site:.org [COUNTY] [STATE] economic development housing
[COUNTY] [STATE] workforce housing news
[COUNTY] [STATE] affordable housing development news
```

## Decision Use

Use Serper to confirm whether a finding from Brave or AI search is real, recent, and source-backed.

---

# 4. Tavily Instructions

## Role

Tavily is the AI research extraction layer.

Use Tavily to generate structured research summaries with citations.

Best for:

- County-level research briefs
- Summarizing long government pages
- Extracting policy priorities
- Turning source links into briefing notes
- Producing cited research summaries for investor materials

## Tavily Prompt Template

```txt
Prepare a cited research brief on [COUNTY], [STATE] for Spectra Holdings.

Research focus:
1. Housing affordability and supply pressure
2. Workforce housing need
3. Economic development priorities
4. Municipal planning and redevelopment goals
5. Infrastructure or resilience challenges
6. Incentives, grants, bonds, CDFIs, Opportunity Zones, or public funding programs
7. Landowner or developer partnership opportunities

For each finding, include:
- Source URL
- Source name
- Date if available
- Key quote or fact
- Strategic interpretation for Spectra
- Stakeholder relevance: investor, county official, landowner, or NCF/impact capital

End with a go / no-go research recommendation and the top three follow-up questions.
```

## Output Format

```txt
Executive Summary
Key Findings
Source Table
Spectra Strategic Interpretation
Stakeholder Narratives
Risk Flags
Follow-Up Research Questions
```

---

# 5. Exa.ai Instructions

## Role

Exa.ai is the semantic discovery engine.

Use Exa when keyword search misses useful sources.

Best for finding:

- Similar county housing plans
- Economic development strategy PDFs
- Regional planning documents
- Affordable housing reports
- Policy research papers
- CDFI / grant / foundation-related documents
- Comparable public-private partnership case studies

## Exa Prompt Template

```txt
Find high-quality public documents and web pages semantically related to this research objective:

Spectra Holdings is evaluating [COUNTY], [STATE] for scalable workforce housing, community redevelopment, public-private partnership potential, and Master Credit Facility deployment.

Find sources similar to:
- county housing needs assessments
- comprehensive plans
- workforce housing studies
- economic development strategic plans
- redevelopment authority documents
- affordable housing trust fund programs
- CDBG / HOME / NMTC / CDFI housing programs
- disaster resilience housing plans

Prioritize official government, regional planning, academic, nonprofit, and economic development sources.
Return title, URL, source type, publication date, and relevance explanation.
```

## Use Exa For

- Better discovery of PDFs and obscure planning documents
- Finding comparable models from other counties
- Building national pattern recognition for Spectra

---

# 6. Parallel.ai Instructions

## Role

Parallel.ai should be used as the persistent monitoring layer.

Use it to track county-level signals over time.

Best for:

- New council agendas
- Planning commission updates
- Housing grant announcements
- Infrastructure funding notices
- Disaster recovery funding
- Land development announcements
- Public-private partnership RFPs
- Municipal bond notices
- Opportunity Zone updates
- County economic development announcements

## Monitor Setup Prompt

```txt
Create a persistent monitoring stream for [COUNTY], [STATE] to support Spectra Holdings county intelligence and Master Credit Facility deployment.

Monitor for new information related to:
- Housing development
- Workforce housing
- Affordable housing
- Planning commission agendas
- County council / city council agendas
- Public-private partnership opportunities
- RFPs / RFQs for housing or infrastructure
- CDBG / HOME / HUD funding
- Municipal bonds
- Opportunity Zones
- CDFI or nonprofit housing activity
- Disaster relief / resilience funding
- Major employer expansions or layoffs
- Land development approvals

For each signal, return:
- Date discovered
- Source URL
- Signal type
- Summary
- Why now?
- Stakeholder affected
- Recommended Spectra action
- Priority: Hot / Warm / Watch
```

## Signal Priority Rules

### Hot

Immediate Spectra action within 24–72 hours.

Examples:

- County issues housing RFP
- New bond measure approved
- Major land redevelopment discussion
- Disaster funding announced
- Council agenda includes housing incentives

### Warm

Action within 1–2 weeks.

Examples:

- New housing study released
- Economic plan identifies workforce housing
- Planning committee discusses zoning change

### Watch

Monitor but no immediate outreach.

Examples:

- General news article
- Early-stage discussion
- Weak source without official confirmation

---

# 7. Firecrawl Instructions

## Role

Firecrawl is the website and document extraction layer.

Use Firecrawl when a county website, planning page, or agenda archive needs structured crawling.

Best for:

- County planning department websites
- City council agenda portals
- Economic development websites
- PDF archives
- Housing authority websites
- Redevelopment agency sites
- Grant program pages

## Firecrawl Task Template

```txt
Crawl the official website for [COUNTY], [STATE] and extract pages related to:

- Housing
- Planning and zoning
- Economic development
- Grants and incentives
- Public-private partnerships
- CDBG / HOME / HUD programs
- Municipal bonds
- Opportunity Zones
- Land development
- Disaster resilience
- Infrastructure

Return:
- Page title
- URL
- Extracted text
- Date if available
- Source category
- Key Spectra-relevant facts
- Recommended follow-up
```

## Firecrawl Extraction Rules

- Keep original URLs.
- Preserve page titles.
- Capture document dates.
- Flag PDFs separately.
- Flag outdated pages.
- Do not treat crawled content as validated until reviewed.

---

# 8. Recommended County Research Sequence

For a new county, run the workflow in this order:

## Step 1 — Structured Data

Use Census API.

Output:

- Demographic profile
- Housing affordability metrics
- Initial demand score

## Step 2 — Broad Discovery

Use Brave Search.

Output:

- Initial source list
- County themes
- News and policy signals

## Step 3 — Source Validation

Use Serper.dev.

Output:

- Official source validation
- Recency check
- Government and media source separation

## Step 4 — Deep Extraction

Use Tavily, Exa, and Firecrawl.

Output:

- Research summaries
- Source-backed county intelligence
- Planning document extracts

## Step 5 — Persistent Monitoring

Use Parallel.ai.

Output:

- Ongoing signal stream
- Why-now alerts
- Action triggers

## Step 6 — Decision Output

Generate:

- County Intelligence Report
- Investor Brief
- Municipal Brief
- Landowner Outreach Narrative
- NCF / Impact Capital Alignment Memo
- Go / No-Go recommendation

---

# 9. Standard Prompt for Hermes Agent

Use this master prompt when assigning a county research task to Hermes or another research agent.

```txt
You are operating as the Spectra Holdings County Intelligence Agent.

Your task is to research [COUNTY], [STATE] to support capital flow into Spectra Holdings' Master Credit Facility and community redevelopment model.

Primary stakeholders:
1. Investors and family offices
2. County and municipal officials
3. Landowners and land developers
4. National Christian Foundation / donor-advised and impact capital partners

Research objective:
Determine whether [COUNTY] has sufficient housing demand, affordability pressure, workforce housing need, public-private partnership opportunity, landowner/developer opportunity, and capital-stack alignment to justify deeper Spectra underwriting.

Use this research sequence:
1. Census API for structured demographic and housing data
2. Brave Search for broad discovery
3. Serper.dev for Google-style validation and official sources
4. Tavily for cited research extraction
5. Exa.ai for semantic discovery of planning reports and comparable programs
6. Firecrawl for county website, planning page, and agenda extraction
7. Parallel.ai for ongoing monitoring signals

Required research areas:
- Population and household trends
- Income and affordability gap
- Rent burden and homeownership constraints
- Housing shortage and supply issues
- Workforce housing demand
- Local employers and economic development priorities
- County/city planning priorities
- Available incentives, grants, CDBG, HOME, HUD, NMTC, CDFI, municipal bond, and Opportunity Zone programs
- Disaster resilience or recovery funding
- Public-private partnership opportunities
- Vacant land, underutilized land, and redevelopment opportunities
- NCF / faith-based impact capital alignment

Required output:
1. Executive summary
2. Source-backed findings table
3. Census data summary
4. County opportunity thesis
5. Investor narrative
6. Municipal official narrative
7. Landowner/developer narrative
8. NCF / impact capital narrative
9. Risk flags
10. Go / No-Go recommendation
11. Top 10 follow-up questions
12. Recommended next actions for Spectra

Every factual claim must include a source URL or data source reference.
Every recommendation must connect to a decision or action.
Do not produce generic research. Produce decision-ready intelligence.
```

---

# 10. Source Quality Rules

Rank sources in this order:

1. Official county / city government sources
2. Census, HUD, USDA, EDA, FEMA, Treasury, EPA, BEA, BLS
3. Regional planning authorities
4. Economic development agencies
5. Housing authorities and nonprofit housing organizations
6. Academic / policy research institutions
7. Local newspapers and business journals
8. Industry blogs and general web sources

Investor-facing outputs should rely primarily on source tiers 1–5.

---

# 11. Validation Checklist

Before using research in an investor or municipal briefing, confirm:

- Source is current or clearly dated
- Geography matches target county
- Data year is stated
- Official sources are prioritized
- Claims are not based only on AI summaries
- URLs are retained
- Conflicting facts are flagged
- Census year is consistent across counties
- Incentive programs are checked for eligibility and timing

---

# 12. Decision Output Standard

Every county research package must end with one of these recommendations:

## Proceed

County has strong housing need, public/private alignment, investor narrative, and capital deployment potential.

## Proceed with Conditions

County is promising but requires validation of land, incentives, zoning, infrastructure, or political support.

## Monitor

County has emerging signals but is not ready for active pursuit.

## No-Go

County lacks sufficient demand, support, economics, or strategic alignment.

---

## Final Operating Principle

Search tools do not make the decision. They feed the Spectra Financial Intelligence System.

The final output must always support:

- Capital formation
- Project execution
- County prioritization
- Investor confidence
- Municipal alignment
- Master Credit Facility deployment

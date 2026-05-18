# Product Solution Document — GrantFundingAI

## Project Name
GrantFundingAI

## Parent System
KlickSmartAI Venture Studio → Funding Intelligence Layer

## Purpose
GrantFundingAI converts a company website into a structured funding-readiness assessment for SBIR, STTR, federal grants, county programs, tribal/community opportunities, and capital-stack routing.

The product is designed to answer one core question:

> Is this company or project fundable, and what evidence is missing before it can pursue funding?

---

## 1. Solution Overview

GrantFundingAI will operate as a SaaS workflow that accepts a company website URL, extracts evidence, evaluates SBIR readiness, matches potential agencies, detects missing evidence, and generates a funding-readiness report.

```text
Company Website URL
  → Website Crawl
  → Evidence Extraction
  → Eligibility Screen
  → Problem + Technology Classification
  → Agency Match
  → County / Community Fit
  → Missing Evidence Detector
  → Funding Readiness Report
```

---

## 2. Core Product Modules

### Module 1 — Website Audit Engine
Crawls and extracts relevant content from a company website.

Pages to prioritize:

- Homepage
- About page
- Product/service pages
- Technology pages
- Team page
- Case studies
- Blog/articles
- PDF documents
- Contact/location page
- Partner pages

Primary output:

- Raw page content
- Page summaries
- Evidence snippets
- Source URLs

---

### Module 2 — Evidence Extraction Engine
Uses AI to convert website content into structured funding signals.

Extracted signals:

- Company identity
- Business location
- Problem statements
- Technology claims
- Product/service descriptions
- Innovation signals
- R&D signals
- Prototype/pilot evidence
- Commercialization evidence
- Customer segments
- Team credibility
- Partner signals
- Government/public-sector signals
- County/community signals

Evidence logic:

```text
YES = evidence found
NO = evidence contradicted or absent after review
UNKNOWN = website does not provide enough information
```

UNKNOWN should generate follow-up questions.

---

### Module 3 — SBIR Eligibility Engine
Screens for high-level SBIR readiness using evidence-based logic.

Core fields:

| Field | Values |
|---|---|
| U.S.-based entity | YES / NO / UNKNOWN |
| For-profit company | YES / NO / UNKNOWN |
| Small business indicator | YES / NO / UNKNOWN |
| R&D / technical component | YES / NO / UNKNOWN |
| Commercialization potential | YES / NO / UNKNOWN |

Important rule:

> GrantFundingAI does not make legal eligibility determinations. It provides a readiness and evidence-confidence assessment.

---

### Module 4 — Problem Classification Engine
Classifies the company/project into funding-relevant domains.

Initial domains:

- Energy
- Environment
- Waste recovery
- Critical materials
- Rural infrastructure
- Housing/community development
- Manufacturing
- AI/software
- Health
- Defense/dual-use
- Agriculture/food/water

---

### Module 5 — Agency Match Engine
Maps extracted signals to likely funding agencies and program paths.

| Signal | Likely Path |
|---|---|
| Energy, grid, storage, resilience | DOE |
| Recycling, remediation, pollution reduction | EPA |
| Rural systems, agriculture, food, water | USDA |
| Broad deep technology | NSF |
| Housing/community development | HUD / CDBG / CDFI |
| Manufacturing/jobs | EDA |
| Defense/dual-use | DOD |
| Health/biotech | NIH |

Output fields:

- Agency name
- Match reason
- Confidence score
- Evidence snippets
- Recommended next action

---

### Module 6 — County / Community Fit Engine
Evaluates whether the project aligns with local, county, tribal, rural, or disadvantaged-community needs.

Signals:

- Rural relevance
- Tribal/community relevance
- Environmental improvement
- Workforce/job creation
- Housing/infrastructure benefit
- Energy resilience
- Local economic development

Potential outputs:

- County Fit: High / Medium / Low
- Tribal Fit: High / Medium / Low
- Rural Fit: High / Medium / Low
- Environmental Fit: High / Medium / Low

---

### Module 7 — Missing Evidence Detector
Identifies what is missing from the website or intake data before a funding case can be built.

Examples:

- U.S. incorporation not confirmed
- Employee count not visible
- For-profit status unclear
- Prototype status unclear
- Pilot customers not found
- IP ownership not confirmed
- Commercialization plan weak
- Public-sector use case not described
- No measurable problem statement

This module supports a major upsell:

> Improve your funding readiness before applying.

---

### Module 8 — Interview Engine
Generates targeted follow-up questions based only on missing evidence.

Example:

```text
We could not confirm the following:

1. Is the company incorporated in the United States?
2. Does the company have fewer than 500 employees?
3. Is there a working prototype?
4. Are there pilot customers?
5. Who owns the intellectual property?
6. Has the company applied for SBIR/STTR before?
```

---

### Module 9 — Report Generator
Creates a structured funding-readiness report.

Minimum report sections:

1. Company summary
2. Website evidence summary
3. Problem statement
4. Technology classification
5. SBIR readiness screen
6. Agency matches
7. County/community fit
8. Missing evidence
9. Recommended next action
10. Proposal starter outline

---

## 3. System Architecture

```text
Frontend
  Lovable / Next.js

Backend
  Supabase / Postgres

Website Crawler
  Scrapling / Firecrawl

AI Extraction Layer
  Claude / GPT / Gemini

Scoring Engine
  Python

Analytics Layer
  MotherDuck / DuckDB

Report Generator
  HTML → PDF

Workflow Layer
  Python-first
  n8n optional

CRM / Follow-up
  GoHighLevel optional
```

---

## 4. Data Flow

```text
User submits website URL
  → Create audit_run
  → Crawl pages
  → Store website_pages
  → Extract structured signals
  → Store extracted_signals
  → Run eligibility_checks
  → Run scoring_model
  → Generate agency_matches
  → Generate missing_evidence
  → Generate interview_questions
  → Generate report
```

---

## 5. Core Data Objects

```text
users
companies
websites
website_pages
audit_runs
extracted_signals
eligibility_checks
problem_classifications
agency_matches
county_matches
community_matches
interview_questions
interview_answers
scores
reports
subscriptions
```

---

## 6. MVP Scope

The MVP should stay narrow.

### MVP Features

- Company website URL intake
- Website crawl
- AI extraction
- SBIR readiness checklist
- Agency matching
- Missing evidence detector
- Scoring engine
- HTML report
- Admin review dashboard

### Excluded From MVP

- Full live Grants.gov integration
- Full SAM.gov integration
- Automated application filing
- Legal eligibility certification
- Multi-user enterprise workspaces
- Full CRM automation

---

## 7. MVP User Flow

```text
User enters website URL
  → System crawls site
  → System extracts evidence
  → System scores readiness
  → System displays missing evidence
  → User answers follow-up questions
  → System updates score
  → User downloads report
```

---

## 8. First Vertical Focus

GrantFundingAI should initially focus on:

- Clean energy
- Waste recovery
- Critical materials
- Community infrastructure
- Rural development
- Tribal/community resilience

Reason:

This focus aligns with Tiyo Energy, MineTeck, Spectra Holdings, DOE, EPA, USDA, county development, and tribal opportunity mapping.

---

## 9. Monetization Paths

| Tier | Offer |
|---|---|
| Free | Basic readiness snapshot |
| Starter | Full audit report |
| Pro | Audit + interview + funding roadmap |
| Studio | Done-with-you funding strategy |
| Enterprise | Monitoring for consultants, accelerators, and economic development groups |

---

## 10. Definition of Done

The solution is validated when a user can submit a website and receive a structured report containing:

- Company summary
- Problem statement
- Technology classification
- SBIR eligibility status
- SBIR readiness score
- Agency matches
- Missing evidence
- County/community fit
- Recommended next action

---

## 11. Strategic Positioning

GrantFundingAI should not be positioned as a generic grant search tool.

It should be positioned as:

> An opportunity qualification and funding intelligence system for innovation companies, counties, tribal partners, grant consultants, and venture studios.

For KlickSmartAI, GrantFundingAI becomes a Venture Studio intake engine:

```text
Company website
  → Opportunity score
  → Funding path
  → Proposal
  → Pilot
  → Venture
```

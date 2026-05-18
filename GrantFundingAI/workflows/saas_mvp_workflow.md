# GrantFundingAI SaaS MVP Workflow

## Core Flow

```text
Website URL
  → Crawl website
  → Extract evidence
  → Run SBIR eligibility screen
  → Classify problem + technology
  → Match agencies
  → Detect missing evidence
  → Generate report
```

## Step 1 — Intake
User submits:

- Company name
- Website URL
- Industry
- Location
- Target county/state/tribal community, if known
- Optional technology description

## Step 2 — Website Crawl
Crawler retrieves:

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

## Step 3 — AI Extraction
The system extracts:

- Company summary
- Problem statements
- Technology claims
- Products/services
- Customer segments
- Commercialization evidence
- Team signals
- Partner signals
- Government/public-sector signals
- County/community signals
- Missing evidence

## Step 4 — Eligibility Gate
Use PASS / FAIL / UNKNOWN logic.

- U.S.-based entity
- For-profit company
- Small business indicators
- R&D / technology component
- Commercialization potential

UNKNOWN should trigger follow-up interview questions, not automatic rejection.

## Step 5 — Problem Classification
Classify into domains:

- Energy
- Environment
- Rural systems
- Housing/community development
- Manufacturing
- AI/software
- Health
- Defense/dual-use

## Step 6 — Agency Matching

| Signal | Likely Agency / Path |
|---|---|
| Energy, grid, storage, resilience | DOE |
| Recycling, remediation, pollution | EPA |
| Rural systems, agriculture, food, water | USDA |
| Broad deep technology | NSF |
| Housing/community development | HUD / CDBG / CDFI |
| Manufacturing/jobs | EDA |
| Defense/dual-use | DOD |
| Health/biotech | NIH |

## Step 7 — Missing Evidence Detector
Examples:

- U.S. incorporation not confirmed
- Employee count not visible
- Prototype status unclear
- Pilot customers not found
- Commercialization path weak
- No public-sector use case described
- Ownership/IP not confirmed

## Step 8 — Report Output
Minimum report:

- Company summary
- Problem statement
- Technology classification
- Eligibility status
- SBIR readiness score
- Agency matches
- Missing evidence
- County/community fit
- Recommended next action

## MVP Definition of Done
The MVP is done when a user can submit a website URL and receive a structured funding readiness report in HTML or PDF format.

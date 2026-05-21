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

### Agency + Phase Guidance Table

| Signal | Likely Agency / Path | Phase I Window | Phase III Path |
|--------|----------------------|----------------|----------------|
| Energy, grid, storage, resilience | DOE | Opens Sept 2026 | OCIO procurement |
| Recycling, remediation, pollution | EPA | Opens Aug 2026 | Tribal land set-aside |
| Rural systems, agriculture, food, water | USDA | Rolling | Rural development grants |
| Broad deep technology | NSF | Opens Jan 2026 | Fast-track review |
| Housing/community development | HUD / CDBG / CDFI | Rolling | CDFI gap financing |
| Manufacturing/jobs | EDA | Rolling | Economic adjustment assistance |
| Defense/dual-use | DOD | Invitational | SBIR C-sUAS contract |
| Health/biotech | NIH | Standard 3-cycle | NIAID tribal set-aside |

### APEX Counselor Step (between Eligibility Gate and Problem Classification)

```
Eligibility Gate
  → APEX Counselor Step    ← NEW
  → Problem Classification
```

**APEX Counselor Step Details**

After the Eligibility Gate, first-time or low-score applicants are referred to an APEX counselor for:

- **Registration support** — SAM/UEI/CAGE setup walkthrough
- **Proposal writing mentorship** — technical narrative structure and merit framing
- **Program manager relationships** — SBIR Road Tour introductions
- **Certification navigation** — 8(a)/WOSB/HUBZone/SDVOSB eligibility review

*GrantFundingAI generates a PTAC referral package (PDF export) at the Eligibility Gate output. The package includes all extracted evidence and eligibility signals so the counselor can proceed without re-doing discovery.*

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

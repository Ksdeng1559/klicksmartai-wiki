# Product Requirements Document — GrantFundingAI

## Project Name
GrantFundingAI

## Parent System
KlickSmartAI Venture Studio → Funding Intelligence Layer

## Version
PRD v1.0

## Status
Draft MVP Requirements

---

## 1. Product Summary

GrantFundingAI is a SaaS application that audits a company website and generates an evidence-based funding readiness report for SBIR/STTR, federal grants, county programs, tribal/community opportunities, and capital-stack pathways.

The product helps answer:

> Is this company fundable, what programs might fit, and what evidence is missing?

---

## 2. Core Value Proposition

GrantFundingAI transforms a website into a structured funding-readiness assessment.

```text
Website URL
  → Website crawl
  → Evidence extraction
  → SBIR readiness screen
  → Problem + technology classification
  → Agency matching
  → County/community fit
  → Missing evidence detector
  → Funding readiness report
```

---

## 3. Target Users

### Internal Users

- KlickSmartAI Venture Studio
- Spectra Holdings
- Tiyo Energy
- MineTeck
- Venture Studio operators

### External Users

- Innovation startups
- Grant consultants
- Economic development organizations
- Accelerators/incubators
- County partners
- Tribal/community partners
- Clean energy and infrastructure companies

---

## 4. MVP Scope

### Included in MVP

- User submits company name and website URL
- Website crawl for priority pages
- AI extraction of structured evidence
- SBIR readiness scoring
- PASS / FAIL / UNKNOWN eligibility logic
- Agency match recommendations
- County/community fit signals
- Missing evidence detector
- Follow-up interview questions
- HTML report output
- Admin view of audit runs

### Excluded From MVP

- Automated SBIR application filing
- Live Grants.gov integration
- Live SAM.gov integration
- Legal eligibility certification
- Full multi-tenant enterprise workspace
- Full CRM integration
- Automated proposal submission

---

## 5. User Stories

### Website Audit

As a user, I want to enter a company website URL so that I can receive a funding-readiness assessment.

Acceptance criteria:

- User can enter company name and website URL
- System creates an audit run
- System stores website content and extracted evidence
- System returns audit status

---

### SBIR Readiness Score

As a user, I want to see an SBIR readiness score so that I know whether the company is a strong funding candidate.

Acceptance criteria:

- System displays total score from 0 to 100
- System displays category-level scores
- System assigns one of four decisions:
  - High Priority
  - Strong Candidate
  - Needs Development
  - Not SBIR Ready

---

### Missing Evidence Detector

As a user, I want to see what evidence is missing so that I can improve the website or prepare follow-up documents.

Acceptance criteria:

- System lists missing eligibility evidence
- System lists missing commercialization evidence
- System lists missing innovation evidence
- System creates follow-up interview questions

---

### Agency Match

As a user, I want to see likely funding agencies so that I know which programs to research first.

Acceptance criteria:

- System identifies likely agencies
- Each agency match includes a reason
- Each agency match includes a confidence score
- Agency matches are based on extracted evidence

---

### Funding Readiness Report

As a user, I want to download or view a report so that I can share the findings with partners, founders, or internal stakeholders.

Acceptance criteria:

- Report includes company summary
- Report includes problem statement
- Report includes technology classification
- Report includes SBIR readiness score
- Report includes agency matches
- Report includes missing evidence
- Report includes recommended next action

---

## 6. Functional Requirements

### F-01: Company Intake

Fields:

- Company name
- Website URL
- Industry
- Location
- Target county/state/tribal community
- Optional technology description

Priority: Must Have

---

### F-02: Website Crawl

System should crawl:

- Homepage
- About page
- Product/service pages
- Technology pages
- Team page
- Case studies
- Blog/articles
- PDFs, if available
- Contact/location page
- Partner pages

Priority: Must Have

---

### F-03: Structured Evidence Extraction

System should extract:

- Company identity
- Problem statements
- Technology claims
- Commercialization signals
- Innovation signals
- Prototype/pilot evidence
- Patent/IP signals
- Team signals
- Partner signals
- Government signals
- Community signals
- Missing evidence

Priority: Must Have

---

### F-04: Eligibility Logic

System must evaluate:

- U.S.-based entity
- For-profit status
- Small business indicator
- R&D / technical component
- Commercialization potential

Use:

```text
YES / NO / UNKNOWN
```

Priority: Must Have

---

### F-05: SBIR Scoring Engine

Weighted categories:

| Category | Weight |
|---|---:|
| Eligibility | 20 |
| Problem significance | 15 |
| Innovation | 15 |
| Commercialization | 15 |
| Government fit | 15 |
| Community fit | 10 |
| Partnerships | 10 |

Priority: Must Have

---

### F-06: Agency Match Engine

Initial agency routing:

| Signal | Agency / Path |
|---|---|
| Energy, grid, storage, resilience | DOE |
| Recycling, remediation, pollution | EPA |
| Rural systems, agriculture, food, water | USDA |
| Broad deep technology | NSF |
| Housing/community development | HUD / CDBG / CDFI |
| Manufacturing/jobs | EDA |
| Defense/dual-use | DOD |
| Health/biotech | NIH |

Priority: Must Have

---

### F-07: Missing Evidence Detector

System should identify missing or weak evidence, such as:

- U.S. incorporation not confirmed
- Employee count not visible
- For-profit status unclear
- Prototype status unclear
- Pilot customers missing
- IP ownership unclear
- Commercialization path weak
- Public-sector use case not described

Priority: Must Have

---

### F-08: Interview Question Generator

System should generate targeted follow-up questions only for missing evidence.

Priority: Should Have

---

### F-09: Report Generator

Report must include:

- Company summary
- Website evidence summary
- Problem statement
- Technology classification
- Eligibility status
- SBIR readiness score
- Agency matches
- County/community fit
- Missing evidence
- Recommended next action

Priority: Must Have

---

### F-10: Admin Dashboard

Admin should be able to view:

- Audit runs
- Company records
- Scores
- Missing evidence
- Generated reports

Priority: Should Have

---

## 7. Non-Functional Requirements

### Accuracy

The system must distinguish between evidence, inference, and unknown status.

### Explainability

Every score and agency match should include a reason.

### Auditability

Each extracted signal should preserve source URL and page reference.

### Human Review

The system should not claim final legal eligibility. It should recommend human review before application.

### Extensibility

The agency match engine should allow new agencies, state programs, county programs, and tribal funding paths to be added later.

---

## 8. Data Model

Core objects:

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

## 9. Suggested Screens

### Screen 1 — Dashboard

Shows recent audits, scores, and next actions.

### Screen 2 — New Audit

Company intake form.

### Screen 3 — Audit Processing

Shows crawl/extraction/scoring progress.

### Screen 4 — Audit Results

Displays score, agency matches, missing evidence, and recommendations.

### Screen 5 — Interview

Shows missing-evidence questions.

### Screen 6 — Report

Displays exportable report.

### Screen 7 — Admin

Shows all companies, audits, and reports.

---

## 10. MVP Definition of Done

The MVP is complete when:

```text
A user submits a website URL
  → System crawls priority pages
  → System extracts structured evidence
  → System scores SBIR readiness
  → System identifies likely agencies
  → System detects missing evidence
  → System generates a structured report
```

Minimum report output:

- Company summary
- Problem statement
- Technology classification
- Eligibility status
- SBIR readiness score
- Agency matches
- Missing evidence
- County/community fit
- Recommended next action

---

## 11. Initial Vertical Focus

GrantFundingAI should initially focus on:

- Clean energy
- Waste recovery
- Critical materials
- Community infrastructure
- Rural development
- Tribal/community resilience

This vertical aligns with Spectra Holdings, Tiyo Energy, MineTeck, DOE, EPA, USDA, county opportunity mapping, and tribal/community development pathways.

---

## 12. Success Metrics

| Metric | Target |
|---|---:|
| Website audit completed | Under 10 minutes |
| Structured report generated | 100% of completed audits |
| Missing evidence generated | 100% of incomplete audits |
| Agency match explainability | 100% of matches |
| Human review flag shown | 100% of reports |
| First pilot audits | 10–20 companies |

---

## 13. Risks

| Risk | Mitigation |
|---|---|
| Website lacks enough information | Use UNKNOWN + interview engine |
| False grant eligibility claims | Use readiness language, not certification language |
| Agency criteria changes | Keep agency rules modular |
| Overly broad product scope | Start with clean energy / waste / critical materials |
| User assumes report is legal advice | Add human review disclaimer |

---

## 14. Strategic Positioning

GrantFundingAI is not a generic grant finder.

It is:

> An opportunity qualification and funding intelligence system for innovation companies, counties, tribal partners, grant consultants, and venture studios.

For KlickSmartAI, it becomes a Venture Studio intake engine:

```text
Company website
  → Audit run
  → Readiness score
  → Agency matches
  → Missing evidence
  → Report output
```

---

## 15. SBIF Phase Requirements

The Small Business Innovation Research (SBIR) and Small Business Technology Transfer (STTR) programs fund R&D in three sequential phases. GrantFundingAI assesses readiness and generates guidance for each phase.

---

### Phase I — Technical Merit

**Purpose:** Establish technical feasibility and scientific merit.

**Duration:** 1 year (6–12 months)

**Funding Amount:** Up to $275,000 (DOE, NSF, NIH, USDA) — varies by agency

**Eligibility Requirements:**

- U.S.-based for-profit small business (500 employees or fewer)
- Principal investigator must be employed by the company (≥51% time)
- R&D must be performed in the U.S.
- Business must have the technical and managerial capability to complete the project

**Submission Requirements:**

- Company registration in SAM.gov and SBA SBIR/STTR company registry
- Project description (no more than 12 pages, excluding appendices)
- Technical objectives and key milestones
- Innovation statement — what is new/unproven compared to existing knowledge
- Commercialization plan — how the results will lead to a marketable product
- Budget and budget justification
- List of key personnel and their qualifications
- Letters of intent or preliminary data (if required by agency)

**GrantFundingAI Assessment Triggers:**

- Missing: evidence of U.S. incorporation or small business status
- Missing: team credentials or R&D employment signals
- Missing: technical approach description or innovation claims
- Missing: commercialization path signals

---

### Phase II — Development & Demonstration

**Purpose:** Continue R&D and demonstrate commercial potential based on Phase I results.

**Duration:** 2 years (24 months)

**Funding Amount:** Up to $1,100,000 (varies by agency and topic)

**Eligibility Requirements:**

- Must have successfully completed Phase I
- Phase I contract must be in good standing (no extensions, no termination)
- Company must demonstrate technical progress against Phase I milestones
- Must show clear commercial market potential

**Submission Requirements:**

- Phase I results summary and technical progress report
- Phase II project description with detailed technical work plan
- Detailed commercialization plan with market analysis
- Updated budget reflecting full Phase II scope
- Evidence of Phase I technical success (data, prototypes, preliminary results)
- List of Phase II anticipated deliverables and milestones
- Letters of support or intent from potential customers or partners
- IP ownership documentation (if applicable)

**GrantFundingAI Assessment Triggers:**

- Missing: Phase I completion confirmation
- Missing: prototype or technical demonstration evidence
- Missing: customer discovery or market validation signals
- Missing: pilot customers, LOIs, or commercial interest evidence
- Missing: IP/patent status or technology advantage documentation

---

### Phase III — Commercialization

**Purpose:** Bring the technology to market. No SBIR/STTR funds are available for this phase.

**Funding:** Must come from private capital, non-SBIR federal grants, or commercial revenue

**Eligibility Requirements:**

- Must have completed Phase II (or in rare cases, Phase I with agency agreement)
- Technology must be positioned for commercial deployment
- Company must be investment-ready or revenue-generating

**Submission Requirements:**

- Private investment documentation or commercial contracts
- Non-SBIR federal funding (e.g., TSP, PRIME, MCEP, DOE loan programs)
- Evidence of market traction: revenue, LOIs, pilot contracts, or strategic partnerships

**GrantFundingAI Assessment Triggers:**

- Missing: investor or capital stack signals
- Missing: commercial contracts or pilot revenue evidence
- Missing: follow-on grant opportunities (DOE MCEP, EPA STAR, USDARural)

---

### Agency-Specific Variations

| Agency | Phase I | Phase II | Phase III Requirement |
|---|---|---|---|
| DOE | $275K / 1 yr | $1.1M / 2 yr | Must show energy market pathway |
| NSF | $275K / 1 yr | $1.1M / 2 yr | Must show research/commercial potential |
| NIH | $275K / 1 yr | $1.1M / 2 yr | Must show health/clinical application |
| USDA | $275K / 1 yr | $1.1M / 2 yr | Must show agricultural or rural impact |
| DOD | Varies | Varies | Must show defense or dual-use pathway |

---

### GrantFundingAI Phase Guidance Output

For each audit, the system will indicate:

- Which phase(s) the company appears most likely to qualify for
- What evidence is present supporting Phase I/II/III readiness
- What evidence gaps exist before attempting submission
- Recommended next steps for building toward the next phase

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

## 11. APEX Integration and Federal Registration Pathway

GrantFundingAI integrates with the APEX (Association of Procurement Technical Assistance Centers) network to guide users through federal contractor registration and socioeconomic certification, converting readiness assessments into actionable registration steps.

---

### 11.1 SAM/UEI/CAGE/DSBS Registration Walkthrough

Most federal grant and contract opportunities require prior registration in government systems. The walkthrough guides users step-by-step through each registration.

#### Step 1 — Obtain a Unique Entity Identifier (UEI)

**What it is:** The UEI is the official identifier for doing business with the U.S. government. It replaced the DUNS number in 2022.

**Where to register:** sam.gov

**GrantFundingAI action:**

- Detect whether the company website mentions an existing UEI
- If missing, generate a guided prompt: "Apply for a UEI at sam.gov before proceeding"
- Flag if the company's legal business name and address are inferable from the website for pre-filling

**Evidence signals checked:**

- Legal business name on website vs. official registration
- Physical address matches a U.S. location
- "Registered" or "Incorporated" language present

---

#### Step 2 — Register in SAM.gov (System for Award Management)

**What it is:** SAM.gov is the primary database for contractors and grantees. Active registration is required to receive federal awards.

**Key registration components:**

- Entity information (name, address, business size, fiscal year close)
- NAICS codes (primary and secondary)
- PSCs / Product Service Codes
- Size standards (small business determination)
- Representations and certifications (FAR/DFARS)
- Federal flags (debarment, suspension checks)

**GrantFundingAI action:**

- Run a pre-registration checklist based on extracted evidence
- Evaluate whether the company website demonstrates small business size compliance
- Flag if the company's described work falls under a NAICS code the user has not selected
- Generate a "SAM Pre-Registration Readiness" score

**Output fields:**

| Field | Value |
|---|---|
| UEI present | YES / NO / UNKNOWN |
| SAM active | YES / NO / UNKNOWN |
| NAICS codes identified | [list] |
| Size standard met | YES / NO / UNKNOWN |
| Debarment/suspension check | CLEAR / FLAG / PENDING |

---

#### Step 3 — Obtain a CAGE Code

**What it is:** The Commercial and Government Entity (CAGE) code is a 5-character identifier used for standardized supplier identification in federal procurement.

**GrantFundingAI action:**

- Inform user that CAGE codes are assigned automatically upon SAM registration
- If previously registered, prompt user to confirm CAGE code is current
- Add CAGE to the company profile for future proposal generation

---

#### Step 4 — Register in DSBS (Dynamic Small Business Search)

**What it is:** DSBS is SBA's online database used by federal agencies to identify small business contractors for set-aside opportunities.

**Who should register:** All small businesses seeking federal contracts, especially those pursuing socioeconomic certifications.

**GrantFundingAI action:**

- Evaluate whether the company meets basic small business size standards
- Cross-reference extracted NAICS codes against SBA size standards
- If eligible, trigger a DSBS registration prompt with pre-populated firmographic data
- Track DSBS registration as a milestone in the funding readiness timeline

---

### 11.2 APEX Counselor Integration Workflow

APEX (Association of Procurement Technical Assistance Centers) provides free counseling through local PTACs (Procurement Technical Assistance Centers) to help small businesses navigate federal registration and contracting.

#### Workflow Steps

**Step 1 — Identify PTAC Eligibility**

GrantFundingAI evaluates whether the company is likely to benefit from PTAC counseling based on:

- Geographic location (PTACs serve specific regions)
- Industry/NAICS codes
- Registration status gaps
- Socioeconomic certification goals

**Step 2 — Generate a PTAC Referral Package**

The system produces a structured referral package containing:

- Company summary from the audit report
- Identified registration gaps (UEI, SAM, CAGE, DSBS)
- NAICS codes with size standards
- Agency matches with contract opportunity potential
- SBIR/STTR phase fit

**Step 3 — Counselor Portal Integration**

GrantFundingAI provides a shared report link or PDF export that a PTAC counselor can review to:

- Skip the intake interview — company data is pre-populated
- Focus on specific registration gaps
- Prioritize certification pathway analysis
- Identify prime contractor teardown opportunities

**Step 4 — Follow-up Scoring**

After PTAC engagement, the user returns to GrantFundingAI to:

- Update registration status fields
- Receive an updated funding readiness score reflecting formal registrations
- Trigger new agency matches based on certifications obtained

---

### 11.3 Socioeconomic Certification Pathways

GrantFundingAI identifies which certification pathways the company may qualify for and provides a step-by-step routing guide.

#### 8(a) Business Development Program

**What it is:** SBA program for socially and economically disadvantaged small businesses. Provides access to federal contracts, joint ventures, and streamlined SBA loans. Term: 9 years maximum.

**Eligibility signals:**

- Owner is socially disadvantaged (race, ethnicity, gender, disability, long-term residence in underutilized area)
- Owner has net worth under $850K (excluding primary residence)
- Company has been in business for at least 2 years
- Company is a small business by SBA size standards

**GrantFundingAI action:**

- Flag owner demographic signals from website/LinkedIn if publicly available
- Check business age and size standard compliance
- Generate certification pre-screen result
- If pre-screen is positive, produce a step-by-step 8(a) application roadmap

---

#### Women-Owned Small Business (WOSB)

**What it is:** Federal contracting program for women-owned small businesses. Contracts are set aside for WOSBs in industries where women are substantially underrepresented.

**Eligibility signals:**

- At least 51% female-owned and controlled
- Company qualifies as small under SBA size standards
- Primary NAICS code is in a WOSB-eligible industry
- Woman owner has operational control (governing board, day-to-day management)

**GrantFundingAI action:**

- Evaluate ownership structure from website/LinkedIn evidence
- Check if the company's NAICS code is WOSB-eligible
- Flag operational control language gaps
- Generate WOSB pre-certification checklist and SBA official registry guidance

---

#### HUBZone (Historically Underutilized Business Zone)

**What it is:** Program for small businesses located in economically disadvantaged areas. HUBZone businesses receive preferential access to federal contracts.

**Eligibility signals:**

- Principal office is in a HUBZone-designated area (or at least 35% of employees work from HUBZone)
- Company has been operating for at least 2 years
- At least 35% of employees reside in a HUBZone (for non-principal-office companies)
- Owner is a U.S. citizen or permanent resident

**GrantFundingAI action:**

- Check if the company address resolves to a HUBZone census tract
- Evaluate team page for employee location signals
- Generate a HUBZone eligibility pre-screen
- If eligible, provide SBA MapBox tool guidance and HUBZone application steps

---

#### Service-Disabled Veteran-Owned Small Business (SDVOSB)

**What it is:** Federal contracting program for businesses owned and controlled by service-disabled veterans. Contracts are often set aside under the SDVOSB sole source authority.

**Eligibility signals:**

- Service-connected disability (verified through VA or DD-214)
- At least 51% veteran-owned and controlled
- Veteran has operational control
- Company qualifies as small under SBA size standards
- Company is a U.S. citizen or permanent resident

**GrantFundingAI action:**

- Flag veteran ownership signals from website/team page if publicly present
- If service-disabled status is inferable, flag as "potential SDVOSB — verify disability rating"
- Generate SDVOSB pre-screen result
- Provide SBA verification portal link and relevant FAR/DFARS provisions

---

#### Certification Pathway Summary

| Certification | Key Requirement | Primary Benefit | GrantFundingAI Output |
|---|---|---|---|
| 8(a) | Socially/economically disadvantaged owner | Set-asides, sole source, loans | Pre-screen + application roadmap |
| WOSB | 51% women-owned, eligible NAICS | Set-asides in underrepresented industries | Pre-screen + NAICS eligibility check |
| HUBZone | Located in HUBZone census tract or 35% employee residency | Set-asides, price preference | Geocode check + pre-screen |
| SDVOSB | Service-disabled veteran ownership | Sole source set-asides | Pre-screen + verification guide |

---

### 11.4 Registration Status Tracking

GrantFundingAI maintains a registration milestone timeline for each company:

| Milestone | Status | Date Completed |
|---|---|---|
| UEI Obtained | PENDING / COMPLETE | — |
| SAM Active | PENDING / COMPLETE | — |
| CAGE Code | PENDING / COMPLETE | — |
| DSBS Listed | PENDING / COMPLETE | — |
| 8(a) Enrolled | PENDING / ELIGIBLE / ENROLLED / GRADUATED | — |
| WOSB Certified | PENDING / ELIGIBLE / CERTIFIED | — |
| HUBZone Certified | PENDING / ELIGIBLE / CERTIFIED | — |
| SDVOSB Verified | PENDING / ELIGIBLE / VERIFIED | — |

Each completed milestone triggers a funding readiness score recalculation and new agency match refresh.

---

## 12. Strategic Positioning

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

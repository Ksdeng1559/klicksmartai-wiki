# Problem Definition Document — GrantFundingAI

## Project Name
GrantFundingAI

## Parent System
KlickSmartAI Venture Studio → Funding Intelligence Layer

## Problem Statement
Innovative companies, county initiatives, tribal partners, and emerging ventures struggle to determine whether they qualify for SBIR, federal grants, county programs, tribal funding, or capital-stack opportunities. The current process is fragmented across agency websites, solicitations, eligibility rules, county data, and manual proposal research.

## Core Problem
Most applicants do not know whether they are fundable before spending time and money on applications.

They lack a fast way to answer:

- Is the company SBIR-ready?
- Is there enough R&D/technical innovation?
- Does the website communicate commercialization potential?
- Which agencies are most relevant?
- What evidence is missing?
- Are there county, tribal, rural, or disadvantaged-community funding angles?
- What capital stack should be considered beyond SBIR?

## Current State

```text
Company website
  → manual research
  → agency searching
  → eligibility guessing
  → weak proposal narrative
  → missed funding opportunities
```

## Desired Future State

```text
Company website URL
  → AI website extraction
  → SBIR eligibility screen
  → problem + technology classification
  → agency matching
  → community/county fit
  → missing evidence detector
  → funding readiness report
```

## Primary Users

- KlickSmartAI Venture Studio
- Innovation companies
- Grant consultants
- Economic development organizations
- County partners
- Tribal partners
- Clean energy and infrastructure ventures

## Initial Use Cases

- Tiyo Energy: waste-to-energy / infrastructure / clean energy
- MineTeck: e-waste / critical mineral recovery / environmental impact
- Spectra Holdings: county development / community infrastructure / capital stack alignment

## SBIF Applicant Personas

### Persona 1: First-Time SBIF Applicant
**Profile:** Early-stage founder or researcher with a novel tech solution and limited GovCon experience.

| Dimension | Detail |
|-----------|--------|
| Barriers | No SAM/UEI/CAGE registration, unfamiliar with technical merit scoring, no existing relationship with a program manager |
| GrantFundingAI Role | Intake engine surfaces SBIF eligibility gaps; agency matching recommends NSF or DOE as Phase I onramps |
| APEX Integration | APEX counselor provides proposal writing mentorship; connects to local SBDC for registration support |

### Persona 2: Growth-Stage GovCon
**Profile:** Established small business with 1–2 prior SBIR awards seeking Phase II or Phase III expansion.

| Dimension | Detail |
|-----------|--------|
| Barriers | Transitioning from R&D to commercialization pathway; Phase III dual-procurement strategy unfamiliar |
| GrantFundingAI Role | Crawl + AI Extraction maps existing award history; Missing Evidence module flags Phase III pitch deck gaps |
| APEX Integration | APEX Government Marketing Toolkit supports Phase III market penetration; SBIR Road Tour unlocks program manager relationships |

### Persona 3: County / Tribal Economic Development
**Profile:** County economic development office or tribal council seeking SBIF-aligned programs to fund infrastructure or community tech.

| Dimension | Detail |
|-----------|--------|
| Barriers | Regulatory complexity, CDFI alignment, narrative framing for merit review |
| GrantFundingAI Role | Classification engine maps community need → agency program; report module generates evidence Brief |
| APEX Integration | APEX counselor provides CDFI navigator introduction; 8(a)/WOSB certification guidance; Native American APEX centers (Muscogee Creek, Cherokee, Oglala Sioux, etc.) |

## Success Metrics

| Metric | Target |
|---|---:|
| Website audit time | Under 10 minutes |
| Missing evidence generated | Yes |
| Agency match generated | Yes |
| SBIR readiness score generated | Yes |
| Report export generated | Yes |
| Manual review required | Yes, for final qualification |

## Definition of Done
The system can accept a company website URL and generate a structured funding readiness report containing company summary, problem statement, technology classification, eligibility status, SBIR readiness score, agency matches, missing evidence, county/community fit, and recommended next action.

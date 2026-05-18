# GrantFundingAI

GrantFundingAI is a KlickSmartAI Venture Studio initiative for auditing company websites and qualifying them for SBIR, STTR, federal grants, county programs, tribal opportunities, and capital-stack pathways.

## Core Promise

Paste a company website URL and receive an evidence-based funding readiness report.

```text
Website URL
  → Website extraction
  → SBIR eligibility screen
  → Problem + technology classification
  → Agency matching
  → County/community fit
  → Missing evidence detector
  → Funding readiness report
```

## Strategic Positioning

GrantFundingAI is not just a grant search tool. It is an opportunity qualification and funding intelligence system for innovation companies, counties, tribal partners, grant consultants, economic development organizations, and venture studios.

For KlickSmartAI, GrantFundingAI becomes a Venture Studio intake engine:

```text
Company website
  → Opportunity score
  → Funding path
  → Proposal
  → Pilot
  → Venture
```

## Initial Focus

The initial version focuses on:

- SBIR/STTR readiness
- Clean energy
- Waste recovery
- Critical materials
- Community infrastructure
- Rural development
- Tribal/community resilience
- County opportunity matching

This focus supports early use cases around Spectra Holdings, Tiyo Energy, MineTeck, DOE, EPA, USDA, county development, and tribal/community funding pathways.

## Current Wiki Structure

```text
GrantFundingAI/
│
├── README.md
│
├── docs/
│   ├── PDD.md
│   ├── PSD.md
│   └── PRD.md
│
├── prompts/
│   └── website_extraction_prompt.md
│
├── schemas/
│   └── audit_result.schema.json
│
├── scoring/
│   └── sbir_readiness_rubric.md
│
└── workflows/
    └── saas_mvp_workflow.md
```

## Current Files

| File | Purpose |
|---|---|
| `docs/PDD.md` | Defines the problem, users, current state, desired state, and success metrics |
| `docs/PSD.md` | Defines the solution architecture, modules, data flow, and MVP scope |
| `docs/PRD.md` | Defines product requirements, user stories, features, screens, and acceptance criteria |
| `workflows/saas_mvp_workflow.md` | Defines the end-to-end SaaS MVP workflow |
| `scoring/sbir_readiness_rubric.md` | Defines the SBIR readiness scoring model |
| `prompts/website_extraction_prompt.md` | Defines the AI extraction prompt for website analysis |
| `schemas/audit_result.schema.json` | Defines the structured output schema for an audit result |

## Planned Files

```text
prompts/
├── sbir_scoring_prompt.md
├── missing_evidence_prompt.md
└── report_generation_prompt.md

schemas/
├── company_profile.schema.json
└── scoring_model.schema.json

scoring/
├── agency_match_rules.md
└── county_fit_score.md

reports/
├── sample_grant_readiness_report.md
└── executive_summary_template.md

workflows/
├── website_audit_workflow.md
└── founder_interview_workflow.md

examples/
├── tiyo_energy_audit.md
├── mineteck_audit.md
└── spectra_county_use_case.md
```

## MVP Definition

The MVP is complete when a user can submit a company website and receive a structured report containing:

- Company summary
- Problem statement
- Technology classification
- SBIR eligibility status
- SBIR readiness score
- Agency matches
- Missing evidence
- County/community fit
- Recommended next action

## MVP Workflow

```text
User submits website URL
  → System crawls priority pages
  → System extracts structured evidence
  → System scores SBIR readiness
  → System identifies likely agencies
  → System detects missing evidence
  → System generates a structured report
```

## Scoring Model

| Category | Weight |
|---|---:|
| Eligibility | 20 |
| Problem significance | 15 |
| Innovation | 15 |
| Commercialization | 15 |
| Government fit | 15 |
| Community fit | 10 |
| Partnerships | 10 |

## Decision Thresholds

| Score | Decision |
|---:|---|
| 85–100 | High Priority |
| 70–84 | Strong Candidate |
| 40–69 | Needs Development |
| 0–39 | Not SBIR Ready |

## Key Principle

GrantFundingAI should distinguish between:

```text
Evidence found
Inference made
Unknown / missing evidence
```

UNKNOWN should trigger founder interview questions, not automatic rejection.

## Next Build Priorities

1. Add agency match rules
2. Add missing evidence prompt
3. Add report generation prompt
4. Add company profile schema
5. Add sample audits for Tiyo, MineTeck, and Spectra
6. Create Lovable / Claude Code build prompt
7. Convert PRD requirements into implementation tasks

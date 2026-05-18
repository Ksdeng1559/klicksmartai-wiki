# GrantFundingAI

GrantFundingAI is a KlickSmartAI Venture Studio initiative for auditing company websites and qualifying them for SBIR, federal grants, county programs, tribal opportunities, and capital-stack pathways.

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

GrantFundingAI is not just a grant search tool. It is an opportunity qualification and funding intelligence system for innovation companies, counties, tribal partners, and venture studios.

## Initial Focus

The initial version will focus on:

- SBIR/STTR readiness
- Clean energy
- Waste recovery
- Critical materials
- Community infrastructure
- Rural development
- Tribal/community resilience
- County opportunity matching

## Planned Wiki Structure

```text
GrantFundingAI/
│
├── README.md
│
├── docs/
│   ├── PDD.md
│   ├── PSD.md
│   ├── PRD.md
│   └── SaaS_Workflow.md
│
├── prompts/
│   ├── website_extraction_prompt.md
│   ├── sbir_scoring_prompt.md
│   ├── missing_evidence_prompt.md
│   └── report_generation_prompt.md
│
├── schemas/
│   ├── company_profile.schema.json
│   ├── audit_result.schema.json
│   └── scoring_model.schema.json
│
├── scoring/
│   ├── sbir_readiness_rubric.md
│   ├── agency_match_rules.md
│   └── county_fit_score.md
│
├── reports/
│   ├── sample_grant_readiness_report.md
│   └── executive_summary_template.md
│
├── workflows/
│   ├── website_audit_workflow.md
│   ├── founder_interview_workflow.md
│   └── saas_mvp_workflow.md
│
└── examples/
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

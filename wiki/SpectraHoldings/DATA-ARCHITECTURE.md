# SpectraHoldings Data Architecture

## Purpose

The SpectraHoldings wiki is the semantic and governance layer for report outputs. DuckDB or MotherDuck is the structured storage and analytics layer.

The goal is to preserve every report output so users of the reports can query, reuse, validate, compare, and update the intelligence over time.

## System Role Separation

```text
Raw Sources
    -> SpectraHoldings Wiki
    -> DuckDB / MotherDuck
    -> Agent Workflows
    -> Report Outputs
    -> User-Facing Reports / Dashboards
```

## What Goes in the Wiki

The wiki stores human-readable and agent-readable intelligence:

- executive summaries
- county intelligence briefs
- investor narratives
- landowner briefs
- assumptions memos
- validation memos
- source notes
- contradiction logs
- decision briefs
- reusable prompt patterns
- agent instructions
- concept definitions
- relationship maps

## What Goes in DuckDB / MotherDuck

DuckDB or MotherDuck stores structured report data:

- counties
- projects
- stakeholders
- data sources
- report runs
- output sections
- citations
- assumptions
- metrics
- scores
- scenarios
- capital stack items
- sensitivity tables
- validation results
- user access metadata

## Recommended Storage Choice

### DuckDB

Use DuckDB for:

- local development
- fast analysis
- prototype report generation
- offline workflows
- single-user testing

### MotherDuck

Use MotherDuck for:

- shared team access
- multi-user report consumption
- cloud-hosted analytical storage
- dashboards
- report history
- agent access across environments

## Recommended Decision

Start with DuckDB locally, then promote the same schema to MotherDuck when reports need to be shared with multiple users.

## Core Tables

### reports

Stores each generated report.

Fields:

- report_id
- report_type
- title
- county_id
- project_id
- stakeholder_type
- generated_at
- generated_by_agent
- status
- confidence_score
- decision_recommendation

### report_sections

Stores structured sections of each report.

Fields:

- section_id
- report_id
- section_name
- section_order
- section_markdown
- section_summary
- confidence_score

### citations

Stores source citations used in report outputs.

Fields:

- citation_id
- report_id
- section_id
- source_id
- claim_text
- source_url
- source_title
- source_date
- retrieved_at
- confidence_score

### assumptions

Stores assumptions used in models and reports.

Fields:

- assumption_id
- report_id
- assumption_name
- assumption_value
- assumption_unit
- assumption_source
- assumption_type
- confidence_score
- validation_status

### metrics

Stores reusable county, project, and financial metrics.

Fields:

- metric_id
- entity_type
- entity_id
- metric_name
- metric_value
- metric_unit
- period
- source_id
- confidence_score

### scores

Stores agent-generated scores.

Fields:

- score_id
- report_id
- score_type
- score_value
- score_max
- score_reason
- agent_name
- created_at

### capital_stack_items

Stores deal-level capital stack components.

Fields:

- capital_stack_item_id
- report_id
- project_id
- source_type
- provider_name
- amount
- cost_of_capital
- term
- constraints
- status

### validation_results

Stores validation checks.

Fields:

- validation_id
- report_id
- validation_type
- result
- issue_severity
- issue_description
- recommended_action
- reviewed_by
- reviewed_at

## Agent Rule

Every agent that produces a report must save two outputs:

1. Wiki artifact: human-readable markdown summary
2. Database record: structured facts, sections, metrics, assumptions, citations, scores, and validation status

## Report Output Principle

A report is not complete until it can be:

- read by a human
- queried by an agent
- validated against sources
- compared against prior reports
- reused in future decision briefs

## Recommended Promotion Path

```text
Phase 1: Local DuckDB
Phase 2: Shared MotherDuck
Phase 3: Dashboard layer
Phase 4: Snowflake or warehouse integration, if institutional scale requires it
```

## Initial Use Cases

1. County Intelligence Report storage
2. Investor Decision Brief storage
3. MCF Deployment Model storage
4. Capital Stack Package storage
5. Landowner Partnership Brief storage
6. Market Feasibility Package storage
7. Validation Memo storage

## Key Governance Rule

The wiki explains meaning. The database stores evidence.

Both are required for investor-ready outputs.

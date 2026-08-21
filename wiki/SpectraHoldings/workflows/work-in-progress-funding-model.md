---
title: Work in Progress Funding Model
created: 2026-05-10
updated: 2026-05-10
type: workflow
status: active
confidence: 0.82

tags:
  - spectra
  - capital-stack
  - mcf
  - investor
  - project-financing
  - work-in-progress
  - funding-model
  - decision-brief

sources:
  - SpectraHoldings/agents/capital-formation-agent.md
  - SpectraHoldings/concepts/cdfi-and-municipal-bond-capital.md
  - SpectraHoldings/DATA-ARCHITECTURE.md

relationships:
  - related_to: capital-formation-agent
  - related_to: master-credit-facility
  - related_to: capital-stack-engine
  - supports: deal-intelligence-engine
  - supports: investor-narrative-engine

contradictions: []

decision_impact:
  - investor-capital
  - mcf-deployment
  - project-financing
  - funding-gap-analysis
  - capital-readiness
---

# Work in Progress Funding Model

## Purpose

The Work in Progress Funding Model evaluates whether a development project is best funded by:

1. a single investor or investor group funding the whole project,
2. a specific segment or draw of the Master Credit Facility funding the project,
3. a blended structure combining investor funds, MCF capacity, CDFI capital, municipal bonds, grants, and other sources.

This model exists because Spectra may not always need a full blended capital stack. In some cases, one investor may fund the entire project. In other cases, the MCF may fund only a specific portion of the work in progress.

## Core Decision Question

What is the most efficient, executable, and risk-adjusted funding path for the current stage of the project?

## Funding Modes

## Mode 1: Whole Project Investor Funding

A single investor or investor group funds the full development budget.

### Best Fit When

- investor capital is committed or highly probable
- project size fits investor mandate
- timeline is urgent
- public finance would slow execution
- MCF capacity should be preserved for other projects
- investor seeks direct project exposure

### Required Analysis

- total development cost
- investor contribution amount
- investor return structure
- repayment source
- collateral position
- exit timing
- expected IRR / ROI
- downside case
- control rights
- dilution impact

## Mode 2: MCF Segment Funding

A defined portion of the Master Credit Facility funds a project stage, construction draw, or cycle.

### Best Fit When

- project has repeatable construction logic
- MCF capital can be recycled quickly
- draw timing is predictable
- repayment source is near-term
- investor capital is better used at facility level
- project supports proof-of-concept for MCF velocity

### Required Analysis

- MCF segment amount
- draw timing
- eligible use of funds
- expected cycle time
- repayment source
- capital recycling date
- return obligation
- liquidity impact on the facility
- facility concentration risk

## Mode 3: Blended Funding Structure

Multiple capital sources fund different layers of the project.

### Possible Sources

- investor equity
- sponsor equity
- senior debt
- construction debt
- MCF segment
- CDFI debt
- municipal bonds
- grants
- tax credits
- donor-advised impact capital
- landowner contribution
- public infrastructure support

### Best Fit When

- project is larger than one investor mandate
- public benefit is strong
- infrastructure support is required
- affordability requirements exist
- multiple repayment sources are available
- capital cost can be reduced through public or mission-aligned sources

## Stage-Based Funding Logic

The model should classify funding by stage:

### Stage 1: Predevelopment

Possible sources:

- sponsor equity
- investor seed capital
- grants
- CDFI predevelopment loan
- municipal planning support

### Stage 2: Land / Site Control

Possible sources:

- investor equity
- landowner contribution
- acquisition debt
- CDFI acquisition financing
- municipal land contribution

### Stage 3: Entitlements / Approvals

Possible sources:

- sponsor equity
- investor capital
- grants
- municipal support

### Stage 4: Infrastructure

Possible sources:

- municipal bonds
- public infrastructure support
- tax increment financing
- CDFI debt
- grants

### Stage 5: Vertical Construction

Possible sources:

- MCF segment
- construction loan
- investor funds
- CDFI debt
- senior debt

### Stage 6: Stabilization / Sale / Refinance

Possible sources:

- takeout debt
- sale proceeds
- permanent financing
- rental income
- refinance proceeds

## Required Inputs

- project name
- county / municipality
- project stage
- total development cost
- amount already funded
- amount currently required
- remaining funding gap
- use of funds
- timing of required capital
- expected repayment source
- expected repayment timing
- investor availability
- MCF availability
- public finance availability
- project risk profile

## Required Outputs

## 1. Funding Mode Recommendation

The model must recommend:

- Whole Project Investor Funding
- MCF Segment Funding
- Blended Funding Structure
- Not Fundable Yet
- Request More Data

## 2. Work in Progress Capital Schedule

The model must show:

- stage
- funding need
- funding source
- amount
- timing
- repayment source
- repayment date
- confidence level

## 3. MCF Capacity Impact

If MCF funding is used, the model must show:

- MCF segment amount
- percentage of facility used
- expected cycle duration
- expected recycle date
- return obligation
- concentration risk
- available remaining facility capacity

## 4. Investor Capital Impact

If investor funding is used, the model must show:

- investor amount
- return structure
- repayment source
- expected IRR / ROI
- control rights
- security position
- downside exposure

## 5. Funding Gap

The model must show:

- total capital required
- capital committed
- capital probable
- capital speculative
- remaining unfunded amount

## 6. Decision Brief

The final output must answer:

1. What funding mode should be used?
2. Why is this mode optimal?
3. What is the minimum capital required now?
4. What capital is needed later?
5. What source should be pursued first?
6. What risks could break the funding plan?
7. What data is missing?

## Scoring Model

## Funding Path Score

Score from 0 to 100.

Suggested weighting:

- 20% capital availability
- 15% execution speed
- 15% cost of capital
- 15% repayment certainty
- 10% strategic fit with MCF
- 10% investor attractiveness
- 10% risk containment
- 5% documentation readiness

## Tiering

- 80-100: Ready to fund
- 65-79: Fundable with conditions
- 50-64: Restructure required
- below 50: Not fundable yet

## DuckDB / MotherDuck Persistence

The Work in Progress Funding Model should store outputs in:

- reports
- report_sections
- funding_modes
- capital_stack_items
- funding_stage_schedule
- mcf_draws
- investor_commitments
- assumptions
- metrics
- scores
- citations
- validation_results

## Recommended Tables

### funding_modes

Fields:

- funding_mode_id
- report_id
- project_id
- selected_mode
- mode_rationale
- funding_path_score
- decision_status
- created_at

### funding_stage_schedule

Fields:

- schedule_id
- report_id
- project_id
- project_stage
- funding_need
- funding_source
- source_type
- amount
- timing_required
- repayment_source
- expected_repayment_date
- confidence_score

### mcf_draws

Fields:

- mcf_draw_id
- report_id
- project_id
- facility_id
- draw_amount
- use_of_funds
- draw_date
- expected_cycle_days
- expected_recycle_date
- return_obligation
- facility_capacity_used_percent
- concentration_risk
- status

### investor_commitments

Fields:

- investor_commitment_id
- report_id
- project_id
- investor_name
- investor_type
- commitment_amount
- commitment_status
- return_structure
- security_position
- expected_irr
- expected_roi
- repayment_source
- expected_exit_date
- confidence_score

## Agent Rule

The Capital Formation Agent must not assume that every project requires the full capital stack.

It must first classify the project into one of three funding modes:

1. whole project investor funding
2. MCF segment funding
3. blended funding structure

Only after classification should it build the detailed capital stack.

## Governance Rule

Do not present investor funds, MCF availability, CDFI support, municipal bonds, or grants as committed unless evidence exists.

Classify every capital source as:

- committed
- soft committed
- likely
- possible
- speculative
- rejected

## Output Template

```markdown
# Work in Progress Funding Brief

## Executive Recommendation

Selected Funding Mode:
Decision Status:
Funding Path Score:

## Project Stage

## Immediate Capital Required

## Full Project Capital Requirement

## Recommended Funding Schedule

| Stage | Need | Source | Amount | Timing | Repayment Source | Confidence |
|---|---:|---|---:|---|---|---:|

## MCF Capacity Impact

## Investor Capital Impact

## Public Finance / CDFI / Bond Layer

## Funding Gap

## Risks

## What Improves the Funding Path

## What Breaks the Funding Path

## Missing Data

## Validation Status
```

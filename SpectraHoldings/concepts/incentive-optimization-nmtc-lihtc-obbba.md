---
title: Incentive Optimization - NMTC, LIHTC, and OBBBA
created: 2026-05-10
updated: 2026-05-10
type: concept
status: active
confidence: 0.70

tags:
  - spectra
  - capital-stack
  - incentive
  - tax-credit
  - nmtc
  - lihtc
  - obbba
  - cdfi
  - municipal-bond
  - mcf
  - housing
  - public-private-partnership

sources:
  - SpectraHoldings/agents/capital-formation-agent.md
  - SpectraHoldings/concepts/cdfi-and-municipal-bond-capital.md
  - SpectraHoldings/workflows/work-in-progress-funding-model.md
  - SpectraHoldings/DATA-ARCHITECTURE.md

relationships:
  - related_to: capital-formation-agent
  - related_to: cdfi-and-municipal-bond-capital
  - related_to: work-in-progress-funding-model
  - supports: master-credit-facility
  - supports: public-finance-intelligence-engine
  - supports: county-intelligence-engine

contradictions: []

decision_impact:
  - investor-capital
  - tax-credit-strategy
  - housing-delivery
  - public-finance
  - mcf-deployment
  - project-feasibility
---

# Incentive Optimization - NMTC, LIHTC, and OBBBA

## Purpose

This concept defines how Spectra evaluates, places, and optimizes incentives, tax credits, and public-purpose capital inside a project or Master Credit Facility capital stack.

The goal is to determine where each incentive belongs, what it can fund, what it cannot fund, how it improves the deal, and what compliance risk it introduces.

## Core Question

How should NMTC, LIHTC, OBBBA-related benefits, CDFI capital, municipal bonds, grants, and other incentives be sequenced to maximize project feasibility, affordability, investor confidence, and MCF efficiency?

## Important Governance Note

This wiki does not treat tax credits or legislative benefits as committed capital until eligibility, allocation, counsel review, and execution pathway are confirmed.

Every incentive must be classified as:

- confirmed
- likely eligible
- possible
- speculative
- rejected

## Incentive Categories

### New Markets Tax Credits - NMTC

Potential role:

- supports qualifying projects in eligible low-income communities
- may improve economics for community facilities, mixed-use, commercial, manufacturing, or economic development components
- often requires CDE involvement and structured compliance

Potential Spectra placement:

- anchor hub facilities
- manufacturing components
- community-serving commercial space
- mixed-use redevelopment
- nonprofit / community development structures
- infrastructure-adjacent economic development projects

Key questions:

1. Is the project located in an NMTC-eligible census tract?
2. Is there a qualified active low-income community business structure available?
3. Is a CDE partner available?
4. What portion of the project qualifies?
5. Does the use align with community development outcomes?
6. What compliance period and reporting obligations apply?
7. Does NMTC conflict with or complement other funding sources?

### Low-Income Housing Tax Credits - LIHTC

Potential role:

- supports affordable rental housing development
- may reduce equity requirement through tax credit investor participation
- can improve feasibility for income-restricted multifamily projects

Potential Spectra placement:

- affordable rental housing
- mixed-income rental components
- nonprofit housing projects
- Propel Community Development projects
- projects with long-term affordability restrictions

Key questions:

1. Is the project rental housing or mixed-use with eligible rental housing components?
2. Does the project meet income restriction requirements?
3. Is the project eligible for 4 percent or 9 percent LIHTC?
4. Is tax-exempt bond financing required or useful?
5. What is the state Qualified Allocation Plan requirement?
6. What affordability period applies?
7. What compliance, rent, income, and reporting obligations apply?
8. What is the likely equity pricing and timing?

### OBBBA-Related Incentives / Benefits

Potential role:

- may support disaster recovery, housing, infrastructure, charitable giving, community revitalization, or public-purpose funding depending on final statutory and regulatory interpretation
- may interact with donor-advised funds, nonprofit structures, public finance, and emergency housing initiatives

Potential Spectra placement:

- disaster recovery housing
- homeless housing
- low-income housing
- county redevelopment initiatives
- nonprofit-driven community development
- public-private partnership projects
- faith-based capital pathways

Key questions:

1. What specific OBBBA provision applies?
2. Who is the eligible recipient or implementing entity?
3. What uses of funds are eligible?
4. Does the benefit flow through a nonprofit, municipality, CDFI, donor-advised fund, or project entity?
5. Does it support equity, debt, grants, guarantees, or charitable deployment?
6. What compliance, timing, and documentation requirements apply?
7. Does it improve MCF liquidity, reduce project-level gap, or support repayment capacity?

## Placement Logic

Each incentive must be placed into the capital stack according to its legal use, timing, restrictions, and repayment effect.

### Possible Placement Layers

1. Predevelopment support
2. Land acquisition support
3. Infrastructure funding
4. Vertical construction funding
5. Permanent financing support
6. Operating subsidy
7. Tax credit equity
8. Credit enhancement / guarantee
9. Grant layer
10. Investor return enhancement
11. MCF liquidity support
12. Takeout / refinance support

## Optimization Sequence

The Incentive Optimization Agent should evaluate incentives in this order:

```text
1. Project eligibility and geography
2. Eligible use of funds
3. Timing of benefit
4. Compliance burden
5. Stack compatibility
6. Effect on funding gap
7. Effect on cost of capital
8. Effect on investor returns
9. Effect on affordability
10. Effect on MCF recycle timing
11. Risk of delay or non-award
12. Go / no-go impact
```

## Capital Stack Interaction

Incentives must be evaluated alongside:

- CDFI debt
- municipal bonds
- senior debt
- MCF segment funding
- investor equity
- donor-advised capital
- grants
- land contribution
- public infrastructure support

## Required Output

For every project, the agent must create an Incentive Impact Memo answering:

1. Which incentives may apply?
2. What project components qualify?
3. Where should each incentive sit in the capital stack?
4. What is the estimated dollar impact?
5. What is the timing impact?
6. What is the compliance burden?
7. What improves IRR, DSCR, affordability, or payback?
8. What creates delay or execution risk?
9. What requires legal, tax, bond counsel, or CDE confirmation?
10. What is the recommended next action?

## Incentive Fit Score

Score from 0 to 100.

Suggested weighting:

- 20% eligibility strength
- 15% dollar impact
- 15% timing compatibility
- 15% capital stack compatibility
- 10% compliance burden
- 10% execution certainty
- 10% effect on affordability / community benefit
- 5% effect on MCF recycle timing

Tiering:

- 80-100: High-priority incentive
- 65-79: Pursue with conditions
- 50-64: Monitor or secondary use
- below 50: Do not rely on this incentive

## DuckDB / MotherDuck Persistence

Incentive outputs should be stored in structured tables.

### incentive_programs

Fields:

- incentive_program_id
- program_name
- program_type
- jurisdiction
- administering_entity
- eligible_geographies
- eligible_uses
- eligible_entities
- benefit_type
- max_benefit
- timing
- compliance_requirements
- source_url
- last_verified_at
- confidence_score

### project_incentive_analysis

Fields:

- analysis_id
- report_id
- project_id
- incentive_program_id
- eligibility_status
- qualifying_component
- estimated_benefit_amount
- benefit_timing
- required_partners
- required_approvals
- compliance_burden
- stack_placement
- risk_level
- recommended_action
- confidence_score

### incentive_stack_placement

Fields:

- placement_id
- report_id
- project_id
- incentive_program_id
- capital_stack_layer
- amount
- timing
- restricted_use
- dependency
- impact_on_gap
- impact_on_cost_of_capital
- impact_on_mcf_recycle
- status

## Validation Requirements

Before using incentives in investor-facing outputs, validate:

- eligibility geography
- eligible entity type
- eligible use of funds
- benefit amount logic
- timing and award probability
- compliance burden
- interaction with other capital sources
- whether counsel, CDE, allocator, issuer, or administering agency confirmation is required

## Governance Rule

Tax credits, OBBBA benefits, grants, municipal bonds, and CDFI capital must not be described as available, committed, or guaranteed unless formally verified.

Investor-ready materials must use careful language:

- confirmed
- eligible subject to approval
- potentially applicable
- under review
- not currently available

## Decision Standard

An incentive improves the deal only if it either:

- reduces the funding gap
- lowers cost of capital
- improves DSCR
- improves investor risk-adjusted return
- improves affordability
- accelerates public-sector support
- improves MCF recycle timing
- strengthens community impact evidence

If it adds delay, compliance risk, or uncertainty greater than its economic benefit, the agent should recommend not relying on it in the base case.

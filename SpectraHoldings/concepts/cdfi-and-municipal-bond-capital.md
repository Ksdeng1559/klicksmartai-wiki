---
title: CDFI and Municipal Bond Capital
created: 2026-05-10
updated: 2026-05-10
type: concept
status: active
confidence: 0.80

tags:
  - spectra
  - capital-stack
  - cdfi
  - municipal-bond
  - housing
  - county
  - public-private-partnership
  - mcf

sources:
  - SpectraHoldings/agents/capital-formation-agent.md
  - SpectraHoldings/DATA-ARCHITECTURE.md
  - SpectraHoldings/AGENTS.md

relationships:
  - related_to: capital-formation-agent
  - related_to: capital-stack-engine
  - supports: master-credit-facility
  - supports: county-intelligence-engine
  - supports: public-private-partnership

contradictions: []

decision_impact:
  - investor-capital
  - county-partnerships
  - public-finance
  - housing-delivery
  - mcf-deployment
---

# CDFI and Municipal Bond Capital

## Purpose

CDFI capital and municipal bond capital are priority funding sources in the Spectra capital formation system.

They should be treated as structured public / mission-aligned capital sources that can support housing, infrastructure, community redevelopment, disaster resilience, workforce housing, and low-to-moderate income development.

## Strategic Role

CDFI and municipal bond capital can help Spectra:

- lower blended cost of capital
- reduce reliance on private equity
- finance infrastructure and community improvements
- support affordability objectives
- improve public-private partnership viability
- align with county redevelopment goals
- increase fundability of the Master Credit Facility

## CDFI Capital

### What It Is

CDFI capital comes from mission-driven financial institutions focused on underserved communities, affordable housing, small business development, community facilities, and economic revitalization.

### Potential Spectra Use Cases

- construction lending
- predevelopment funding
- acquisition financing
- infrastructure support
- affordable housing debt
- bridge financing
- community facility financing
- workforce housing support
- nonprofit / Propel Community Development initiatives

### CDFI Evaluation Criteria

The Capital Formation Agent must evaluate:

- geographic coverage
- eligible borrower type
- eligible project type
- maximum loan amount
- loan-to-cost / loan-to-value limits
- interest rate range
- amortization period
- term
- collateral requirements
- guarantee requirements
- underwriting requirements
- reporting requirements
- mission alignment
- community benefit requirements

### CDFI Fit Score

Recommended scoring:

- 25% geography fit
- 20% mission alignment
- 15% eligible use of funds
- 15% loan sizing capacity
- 10% pricing / cost of capital
- 10% speed and execution certainty
- 5% reporting burden

## Municipal Bond Capital

### What It Is

Municipal bond capital is public finance issued or supported by a state, county, municipality, authority, or eligible conduit issuer to finance public-purpose projects.

### Potential Spectra Use Cases

- workforce housing
- affordable housing
- disaster recovery housing
- public infrastructure
- roads and utilities
- water / sewer extensions
- community facilities
- manufacturing or economic development facilities
- public-private partnership infrastructure
- tax-exempt housing finance structures

### Bond Structure Types to Evaluate

The agent should consider:

- general obligation bonds
- revenue bonds
- private activity bonds
- tax-exempt housing bonds
- conduit bonds
- industrial development bonds
- infrastructure district bonds
- community development district bonds
- tax increment financing bonds

### Municipal Bond Evaluation Criteria

The Capital Formation Agent must evaluate:

- issuer eligibility
- public purpose justification
- project eligibility
- tax-exempt status potential
- repayment source
- debt service coverage
- voter approval requirements
- legal authority
- bond counsel requirements
- rating requirements
- reserve requirements
- timing to issuance
- political support
- compliance obligations

### Municipal Bond Fit Score

Recommended scoring:

- 20% public purpose alignment
- 15% issuer / conduit availability
- 15% repayment source strength
- 15% legal feasibility
- 10% political support
- 10% cost of capital advantage
- 10% execution timeline
- 5% compliance burden

## How These Sources Fit the Capital Stack

CDFI and municipal bond capital should be evaluated before high-cost private capital when the project has strong community benefit.

Recommended sequencing:

```text
1. Grants / incentives
2. Municipal support / public infrastructure support
3. Municipal bond or conduit bond capacity
4. CDFI debt
5. Senior construction debt
6. Impact / donor-advised capital
7. Private equity
8. Mezzanine / gap capital
```

## Relationship to the Master Credit Facility

CDFI and municipal bond capital may support the MCF by:

- reducing project-level capital gaps
- financing infrastructure outside the MCF
- providing lower-cost leverage
- supporting affordable or workforce housing components
- creating public-sector validation
- improving investor confidence
- accelerating repeatable county deployment

## Required Agent Output

When a project or county is evaluated, the Capital Formation Agent must include a CDFI and Municipal Bond section answering:

1. Are CDFIs available for this geography and project type?
2. Which CDFI mandates fit the project?
3. Could municipal bond capital apply?
4. What public purpose supports the bond case?
5. What repayment source exists?
6. What legal or political approvals are required?
7. How does this capital reduce the private funding gap?
8. What is the execution risk?

## Database Persistence

Each CDFI or municipal bond source must be stored in `capital_stack_items` with:

- source_type
- provider_name or issuer_name
- amount
- cost_of_capital
- term
- repayment_priority
- eligible_use
- constraints
- status
- confidence_score

Additional recommended table:

### public_finance_sources

Fields:

- source_id
- source_type
- jurisdiction
- issuer_name
- program_name
- eligible_uses
- max_amount
- rate_type
- repayment_source
- approval_required
- expected_timeline
- compliance_requirements
- source_url
- last_verified_at
- confidence_score

## Governance Rule

Do not present CDFI or municipal bond capital as committed unless there is written confirmation, term sheet, issuer support, lender indication, or formal program eligibility evidence.

Classify each source as:

- confirmed
- likely eligible
- possible
- speculative
- rejected

## Decision Standard

CDFI and municipal bond capital improve a deal only if they reduce capital cost, improve execution certainty, increase affordability, or strengthen public-sector alignment without creating unacceptable timing or compliance risk.

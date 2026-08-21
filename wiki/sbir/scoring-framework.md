# SBIR/STTR Scoring Framework

This scoring model ranks SBIR/STTR opportunities by strategic fit, eligibility, timing, and commercialization potential.

## Scoring Dimensions

| Dimension | Weight |
|----------|--------|
| Technology fit | 20 |
| Agency mission alignment | 15 |
| Solicitation specificity | 15 |
| Eligibility confidence | 15 |
| Commercialization potential | 15 |
| Strategic relationship access | 10 |
| Proposal readiness | 10 |

Total: 100

## Decision Bands

```text
85–100 = Priority pursuit
70–84  = Strong candidate
55–69  = Monitor / research further
Below 55 = Deprioritize
```

## Technology Fit

Measures how closely the company capability maps to the solicitation topic.

Examples:

- Tiyo → waste-to-energy / distributed energy / energy recovery
- MineTeck → e-waste / critical minerals / materials recovery
- Spectra → rapid housing / resilient building systems / community infrastructure

## Agency Mission Alignment

Measures whether the project directly supports the agency mission.

Examples:

- DOE → energy resilience
- EPA → environmental recovery
- DoD → supply chain resilience
- NSF → commercialization of technical innovation
- USDA → rural development

## Solicitation Specificity

Measures how explicitly the solicitation calls for the relevant technology, problem, or use case.

## Eligibility Confidence

Measures company eligibility, U.S. ownership/control considerations, research team readiness, and small business qualification.

## Commercialization Potential

Measures likelihood of moving from Phase I → Phase II → Phase III / customers.

## Relationship Access

Measures whether RIOS can identify:

- agency contacts
- APEX support
- county/tribal partners
- commercialization partners
- warm introduction paths

## Proposal Readiness

Measures whether the team has:

- technical description
- commercialization plan
- budget assumptions
- customer discovery
- pilot partner
- letters of support

## Output Record

Each scored opportunity should produce:

```json
{
  "opportunity_id": "",
  "agency": "",
  "program": "",
  "topic": "",
  "company_fit": "",
  "score": 0,
  "decision_band": "",
  "why_now": "",
  "recommended_action": "",
  "required_research": []
}
```

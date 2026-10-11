# Capital Stack Design Worksheet

Use this for every new project. The output becomes `projects/<developer-slug>/02-capital-stack.md`.

## Project
- Project name:
- Sponsor:
- Total project cost (TPC):
- Target hold period:
- Target IRR (LP):
- Target cash-on-cash (sponsor):
- Target equity multiple:

## Sizing by layer

| Layer | Target $ | Target % | Lender type | Notes |
|---|---:|---:|---|---|
| 1. Senior debt | | | | |
| 2. Mezzanine | | | | |
| 3. Preferred equity | | | | |
| 4. JV equity (LP) | | | | |
| 5. Sponsor equity (GP) | | | | |
| **Total** | | **100%** | | |

## Loan sizing assumptions
- LTC:
- LTV (stabilized):
- DSCR (stabilized):
- Debt yield:
- Rate assumption:
- Term + amortization:
- Interest-only period:

## Equity sizing assumptions
- LP pref:
- GP promote:
- Promote tiers:
- Waterfall:

## Layer-specific lender candidates

### Layer 1 — Senior debt candidates
- Source: `library/lenders/` filtered by `capital_type=debt`, `asset_class`, `geography`, `project_stage`
- Top 3-5 with fit scores

### Layer 2 — Mezzanine candidates
- Source: `library/lenders/` filtered by `capital_type=mezz`
- Top 3-5

### Layer 3 — Preferred equity candidates
- Source: `library/lenders/` filtered by `capital_type=pref`
- Top 3-5

### Layer 4 — JV equity candidates
- Source: `library/lenders/` filtered by `capital_type=lp|co-gp`
- Top 5-10

### Layer 5 — Sponsor equity
- Internal: Veritas GP commitment

## Tax credit / public overlays (if applicable)
- LIHTC (9% or 4%):
- NMTC:
- HTC (historic):
- State / local programs:
- AHP / FHLB:
- Affordable housing trust funds:

## Compliance routing
- Lane 1 (CRE debt):
- Lane 2 (residential MLO):
- Lane 3 (mezz structured):
- Lane 4 (securities):

## Open questions
- What the sponsor needs to confirm before outreach

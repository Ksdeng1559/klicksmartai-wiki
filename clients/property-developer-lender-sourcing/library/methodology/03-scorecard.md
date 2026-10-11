# Step 03 — Fit Scorecard

Score each candidate against the intake. Output: `projects/<developer-slug>/04-fit-scorecard.md`.

## Scoring weights

| Dimension | Weight | What it measures |
|---|---:|---|
| Geography | 15% | Lender's footprint vs. project market |
| Asset class | 15% | Lender's product fit for the asset type |
| Project stage | 15% | Lender's fit for the project's current stage |
| Leverage / structure | 15% | LTC / LTV / DSCR fit + recourse fit |
| Loan / investment size | 10% | Min + max range vs. project size |
| Sponsor experience | 10% | Sponsor's track record vs. lender's threshold |
| Recourse | 10% | Recourse tolerance alignment |
| Execution certainty | 5% | Lender's reputation for closing on time |
| Broker / channel | 5% | Whether the lender accepts broker or referral channel |
| **Total** | **100%** | |

## Per-dimension scoring (0-5)

| Score | Meaning |
|---:|---|
| 5 | Perfect fit — lender explicitly serves this exact market/asset/stage/structure |
| 4 | Strong fit — within stated criteria, may require light negotiation |
| 3 | Moderate fit — within criteria but some friction (geography, structure, stage) |
| 2 | Weak fit — outside stated criteria but historically has done similar deals |
| 1 | Marginal fit — outside criteria, requires exception |
| 0 | Not a fit — explicitly does not serve this segment |

## Worked example

Project: $30M Lee's Summit multifamily. Sponsor: Veritas (1 completed, 2 in pipeline).

| Lender | Geog (15%) | Asset (15%) | Stage (15%) | Lev (15%) | Size (10%) | Sponsor (10%) | Recourse (10%) | Exec (5%) | Channel (5%) | Weighted |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| UMB Bank | 5 | 5 | 5 | 4 | 3 | 3 | 4 | 4 | 5 | **4.30** |
| ACORE Capital | 4 | 5 | 5 | 5 | 5 | 3 | 3 | 4 | 5 | **4.30** |
| Parkview Financial | 3 | 5 | 5 | 5 | 5 | 3 | 3 | 4 | 5 | **4.10** |
| PGIM Real Estate | 5 | 5 | 4 | 5 | 5 | 2 | 4 | 5 | 3 | **4.15** |
| Griffin Capital | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 3 | **3.70** |

## Tier-aware cutoffs

| Tier | Suggested minimum score |
|---|---:|
| Tier 1 (local) | 3.0+ |
| Tier 2 (regional / FFO) | 3.5+ |
| Tier 3 (institutional) | 3.5+ |
| Tier 4 (international) | 4.0+ |

## Output

Sort by weighted score. Top 5-10 = shortlist. Bottom-half = longlist. Below tier cutoff = archive.

## Reference

`~/wiki/clients/veritas-developments/drafts/leadsniper-search-alignment-2026-08-23.md` has a worked tier 1-3 cutoff for the Lee's Summit deal.

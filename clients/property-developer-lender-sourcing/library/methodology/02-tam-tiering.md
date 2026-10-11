# Step 02 — TAM Tiering

Build the addressable lender universe in 4 tiers. Output: `projects/<developer-slug>/03-tam-lender-list.md`.

## Tier definitions

| Tier | Description | Typical count | Typical role |
|---|---|---:|---|
| **Tier 1 — Local / market-rooted** | Lenders headquartered in or with a strong commitment to the project's market. KC community banks, KC CDFIs, KC foundations, market-rooted GPs. | 5-15 | Senior debt, LIHTC, mission equity, co-sponsor |
| **Tier 2 — Regional / FFO** | Regional banks, regional FFOs, regional wealth managers, regional GPs with multi-state reach. | 15-30 | Senior debt, FFO LP equity, co-sponsor |
| **Tier 3 — Institutional / national** | National banks, national FFOs, institutional GPs, public REITs, life companies, CMBS, Fannie/Freddie. | 20-50 | Senior debt, perm takeout, institutional LP / co-GP |
| **Tier 4 — International / cross-border** | Canadian, European, Asian capital for cross-border deals. | 5-20 | Cross-border senior, MIC, private credit |

## How to build each tier

### Tier 1 — Local

1. Start with market's top-10 community banks + CDFIs (per `library/capital-stack/_stack-layer-coverage.md`)
2. Add market's top foundations (CRA, mission, faith-aligned)
3. Add market's local GPs (real estate operators, multifamily specialists)
4. Add market-rooted law firms + CPAs as referral channels (separate file: `06-referral-channels.md`)

### Tier 2 — Regional / FFO

1. Pull from `library/lenders/` filtered by `geography=regional` + `capital_type=lp|co-gp`
2. Add regional wealth managers, RIAs, broker-dealers
3. Add regional banks (with KC office or MO/KS footprint)

### Tier 3 — Institutional / national

1. Pull from `library/lenders/` filtered by `geography=national` + `asset_class` matches
2. Add institutional GPs from the Notion doc reference (Harrison Street, AEW, TruAmerica, GID, JLL, CBRE IM, Brookfield, Blackstone, Starwood, Rockpoint, etc.)
3. Add life companies, CMBS, Fannie/Freddie for permanent takeout
4. Add BTR / SFR specialists (Lennar, Pretium, Invitation Homes, AMH, Progress)

### Tier 4 — International / cross-border

1. Pull from `library/lenders/` filtered by `country=CA|other` (only if cross-border)
2. Add Canadian banks, MICs, commercial finance
3. Add cross-border private credit

## Tier-overlap rule

If a lender could appear in multiple tiers, place it in the **lowest tier where it has the strongest relationship or specialization**. Example: a KC-headquartered national bank goes in Tier 1 if it has KC deal flow, Tier 3 if it is purely national.

## Output

CSV with columns:

```
tier, lender_slug, name, capital_type, asset_classes, geography, fit_score_initial
```

Then sorted by tier + fit score.

## Reference

`~/wiki/clients/veritas-developments/projects/co-sponsor-gp-target-list.md` shows the worked TAM for a Lee's Summit multifamily project (5 KC foundations + 21 FFO + 27 institutional GPs = 53 orgs).

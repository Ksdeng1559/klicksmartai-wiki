# OpenSEO Project File — KonstructionComOS

**Compiled:** 2026-10-16 by Hermes  
**Project ID:** TBD — to be created in OpenSEO  
**Domain target:** konstructioncomos.com (or per PRD)  
**Primary geo:** British Columbia, Canada  
**Primary market intent:** BC Commercial Mortgage origination via BC-licensed broker network  

---

## 1. Summary

- **Total unique keywords (after dedup):** 267
- **BC-only (geo-filtered):** 9
- **Broad-Canada (will need re-filtering):** 258

⚠️ **Honest caveat:** None of the three source keyword sets were originally pulled with `location_code: 20114` (BC). The 78-keyword DataForSEO pull was country-level and bled into Ontario. The 124-term BFC commercial-intent set is country-level. The 78 OpenSEO-enriched keywords are also country-level. **A BC-only re-run ($1-5 in DataForSEO spend) is the right next step before locking pillar pages.**

## 2. Source Sets

### konstruction_comos_78_kw_2026_10_15
- **File:** `/home/denni/wiki/clients/konstruction-comos/research/keyword-research-2026-10-17.json`
- **Keywords pulled:** 78
- **Known issues:** Broad-match Canada results bled into Ontario (Toronto/Ottawa/Hamilton). BC-only re-run with location_code=20114 recommended when budget allows.

### mortgagesbydenniseng_124_kw_commercial_intent_2026_09_13
- **File:** `/home/denni/wiki/clients/mortgagesbydenniseng/research/tariff-loan-batch/consolidated_keyword_set.json`
- **Keywords pulled:** 124
- **Context:** Business Funding Canada sub-vertical, primary canonical keyword set for the comparison-site build (102 commercial-intent + 22 tariff-trigger)

### open_seo_78_enriched_2026_09_14
- **File:** `/home/denni/wiki/clients/mortgagesbydenniseng/research/openseo-enrichment/raw_keyword_metrics.json`
- **Keywords pulled:** 78
- **Context:** OpenSEO Project f10eab85-b2d6-45ad-9f5c-5a4be7c7822c — Business Funding Canada, with KD + intent + competition annotations

## 3. Dedup & Scoring Method

- **Dedup:** exact-string lowercase match, max-volume / max-cpc wins on collision
- **Intent classification:** primary_intent per keyword uses OpenSEO main_intent (preferred) or heuristic cluster→intent mapping
- **Opportunity score:** `(search_volume × cpc / 10) × ((100 - KD) / 100) — favors high-CPC commercial intent with winnable KD`

## 4. Cluster Summary (sorted by total monthly volume)

| Cluster | # Keywords | Total Vol/mo | Avg CPC | Avg Opp Score |
|---|---:|---:|---:|---:|
| locations | 23 | 505,200 | $4.55 | 5144.7 |
| BFC: Commercial Intent | 66 | 29,310 | $23.85 | 667.4 |
| Generic / Head Terms | 67 | 25,700 | $96.02 | 1108.7 |
| tools | 16 | 19,640 | $2.74 | 148.5 |
| research | 30 | 15,380 | $2.28 | 49.6 |
| financing | 9 | 9,010 | $6.9 | 356.2 |
| Line of Credit | 8 | 2,690 | $102.49 | 1275.2 |
| Unsecured | 7 | 1,820 | $64.42 | 975.1 |
| Term Length | 11 | 810 | $155.27 | 595.9 |
| Working Capital / Cash Flow | 3 | 660 | $159.88 | 1674.4 |
| MCA / Factoring | 1 | 110 | $58.61 | 322.3 |
| Inventory / Supplier | 1 | 40 | $81.04 | 162.0 |
| Refinance / Consolidation | 2 | 30 | $141.19 | 106.7 |
| Tariff Trigger (separate cluster — spike/news-anchored) | 22 | 10 | $1.4 | 0.0 |
| Growth / Expansion | 1 | 10 | $105.37 | 52.6 |

## 5. Top 30 Keywords by Opportunity Score

| Keyword | Vol/mo | CPC | KD | Primary Intent | Sources | Opp Score |
|---|---:|---:|---:|---|---|---:|
| mortgage quote | 33,100 | $24.38 | — | transactional | DataForSEO | 40348.9 |
| mortgage loan | 27,100 | $10.92 | — | transactional | DataForSEO | 14796.6 |
| mortgage broker | 22,200 | $13.04 | — | transactional | DataForSEO | 14474.4 |
| mortgage | 27,100 | $8.86 | — | transactional | DataForSEO | 12005.3 |
| business loan | 3,600 | $46.33 | 34 | commercial | BFC, OpenSEO | 11008.0 |
| business loans | 3,600 | $46.33 | 34 | commercial | OpenSEO | 11008.0 |
| business lending | 3,600 | $46.33 | — | commercial | BFC | 8339.4 |
| lending for business | 3,600 | $46.33 | — | commercial | BFC | 8339.4 |
| loan business loan | 3,600 | $46.33 | — | commercial | BFC | 8339.4 |
| business loans canada | 1,600 | $47.7 | 28 | commercial | BFC, OpenSEO | 5495.0 |
| mortgage rates | 49,500 | $2.19 | — | transactional | DataForSEO | 5420.2 |
| small business loan | 2,400 | $28.92 | 27 | commercial | OpenSEO | 5066.7 |
| small business loans | 2,400 | $28.92 | 27 | commercial | OpenSEO | 5066.7 |
| small business loans canada | 1,900 | $34.42 | 25 | commercial | OpenSEO | 4904.8 |
| business line of credit | 1,000 | $53.12 | 15 | commercial | BFC, OpenSEO | 4515.2 |
| small business loan canada | 1,900 | $26.74 | 23 | commercial | OpenSEO | 3912.0 |
| mortgage rates canada | 49,500 | $1.41 | — | transactional | DataForSEO | 3489.7 |
| mortgage rates ontario | 33,100 | $2.1 | — | transactional | DataForSEO | 3475.5 |
| working capital loan | 320 | $115.68 | 21 | commercial | BFC, OpenSEO | 2924.3 |
| business lending canada | 1,300 | $42.91 | — | commercial | BFC | 2789.1 |
| loan business canada | 1,300 | $42.91 | — | commercial | BFC | 2789.1 |
| line of credit business loan | 1,000 | $53.12 | — | commercial | BFC | 2656.0 |
| bankrate mortgage calculator | 40,500 | $1.22 | — | transactional | DataForSEO | 2470.5 |
| mortgage calculator bankrate | 40,500 | $1.22 | — | transactional | DataForSEO | 2470.5 |
| cibc mortgage rates | 27,100 | $1.72 | — | transactional | DataForSEO | 2330.6 |
| rfa mortgage | 5,400 | $8.16 | — | transactional | DataForSEO | 2203.2 |
| unsecured business loan | 260 | $88.25 | 8 | commercial | BFC, OpenSEO | 2110.9 |
| canada small business financing program | 2,900 | $9.41 | 23 | commercial | OpenSEO | 2101.2 |
| working capital lenders | 320 | $115.68 | — | commercial | BFC | 1850.8 |
| operating capital loan | 320 | $115.68 | — | commercial | BFC | 1850.8 |

## 6. BC-Filtered Keywords (markers only — 9 hits)

These are the only keywords with explicit BC city/region markers. **This is the highest-signal sub-list — every dollar of lead-gen spend should prioritize these once BC-only re-run lands.**

| Keyword | Vol/mo | CPC | KD | Sources | Opp Score |
|---|---:|---:|---:|---|---:|
| cibc mortgage rates | 27,100 | $1.72 | — | DataForSEO | 2330.6 |
| payday loans bc | 4,400 | $7.44 | — | DataForSEO | 1636.8 |
| bc loans | 1,300 | $9.01 | — | DataForSEO | 585.6 |
| loan calculator bc | 480 | $2.43 | — | DataForSEO | 58.3 |
| vancouver commercial property for sale | 480 | $1.01 | — | DataForSEO | 24.2 |
| personal loans bc | 170 | $9.65 | — | DataForSEO | 82.0 |
| north vancouver commercial real estate | 70 | $1.02 | — | DataForSEO | 3.5 |
| burnaby commercial real estate | 40 | $1.14 | — | DataForSEO | 2.2 |
| tariff loan BC | 0 | $0 | — | BFC | 0 |

## 7. Recommended Next Steps (OpenSEO Workstream)

1. **Create the OpenSEO project:** `konstruction-comos` does not yet appear in the 3-project list (veritas, gpcdevelopment, default). Once brand/domain finalized, run `create_project` via the OpenSEO MCP. Project file = `openseo-project-file-2026-10-17.json` (this file).
2. **BC-only re-run:** Approve $1-5 DataForSEO spend to pull 100-150 BC-only commercial mortgage keywords using `location_code: 20114`, then merge into this project file.
3. **Pillar page targets** (mapped from highest-opp-score broad-CA terms until BC re-run lands):
   - `/commercial-mortgage-bc` (head term — placeholder until BC re-run returns true commercial-mortgage volume)
   - `/business-loans-canada` (per BFC strategy doc, 14k+ vol, $46 CPC)
   - `/unsecured-business-loans` (4.2k vol, $60 CPC)
   - `/working-capital-loans` (660 vol, $159 CPC — highest CPC band)
   - `/bdc-vs-private-lender` (comparison play)
4. **Geographic overlays:** Once BC re-run lands, generate `/commercial-mortgage-vancouver`, `/commercial-mortgage-surrey`, etc. from the BC set.
5. **Defer tariff cluster:** Tariff terms (22 from BFC) are event-spike triggered, not a pillar. Re-evaluate after first BC-only commercial mortgage set lands.

## 8. Open Questions / Blockers

- BC-only DataForSEO re-run: cost ~$0.01-0.05/keyword × 78 keywords ≈ $0.78-3.90. Recommended for production.
- OpenSEO project creation: konstruction-comos project does not yet exist in the 3-project list (veritas, gpc, default). Create with `create_project` once canonical brand/domain finalized.
- PRD §15 open decisions (legal entity, compensation model, brand) block lead-distribution work but not keyword research.

## 9. File Inventory

| Path | Purpose |
|---|---|
| `openseo-project-file-2026-10-17.json` | Machine-readable project file (267 keywords + scoring) |
| `openseo-project-file-2026-10-17.md` | This summary |
| `keyword-research-2026-10-17.json` | Source 1: 78-keyword DataForSEO pull (broad-CA, needs BC re-run) |
| `keyword-research-2026-10-17.md` | Source 1: human-readable |
| `../../../mortgagesbydenniseng/research/tariff-loan-batch/consolidated_keyword_set.json` | Source 2: 124-term BFC commercial-intent (broad-CA) |
| `../../../mortgagesbydenniseng/research/tariff-loan-batch/KEYWORD_STRATEGY.md` | Source 2: human-readable strategy |
| `../../../mortgagesbydenniseng/research/openseo-enrichment/raw_keyword_metrics.json` | Source 3: 78 OpenSEO-enriched commercial keywords (KD + intent) |

## 10. To Push to OpenSEO

Once the project is created in OpenSEO, the `openseo-project-file-2026-10-17.json` payload is ready to upload via the OpenSEO MCP `bulk_add_keywords` tool. The top-30 in §5 are the first candidates for ranking/pillar planning; the BC-filtered 9 in §6 are the highest-priority once re-confirmed with `location_code: 20114`.

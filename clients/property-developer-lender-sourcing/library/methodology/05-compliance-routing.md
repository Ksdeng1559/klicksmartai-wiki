# Step 05 — Compliance Routing

Classify every capital source into one of 4 lanes BEFORE drafting the outreach. Output: included in `projects/<developer-slug>/02-capital-stack.md` + `06-referral-channels.md`.

## The 4 lanes

| Lane | Lane name | Who executes | What it covers |
|---|---|---|---|
| 1 | Commercial mortgage / construction debt | Sponsor's commercial debt team or licensed commercial mortgage broker | Senior + mezz debt on commercial / multifamily / mixed-use |
| 2 | Residential mortgage | Licensed MLO (state license required) | 1-4 unit residential, condo, SFR |
| 3 | Mezzanine debt | Structured-credit team or licensed broker | Subordinated debt (often Lane 1 + Lane 3 same person) |
| 4 | Securities — preferred equity, LP, JV, fund interests | Registered professionals only (RIA, broker-dealer, securities counsel) | Equity raises, fund formation, LP solicitation |

## Lane assignment rules

| Capital source type | Lane | Why |
|---|---|---|
| Senior construction loan (commercial) | 1 | Commercial mortgage activity |
| Senior construction loan (1-4 unit residential) | 2 | Residential MLO activity |
| Permanent loan (multifamily, commercial) | 1 | Commercial mortgage activity |
| Permanent loan (residential 1-4 unit) | 2 | Residential MLO activity |
| Mezzanine debt (any asset) | 3 | Subordinated debt is structured credit |
| Preferred equity | 4 | Security under SEC |
| Common equity (LP) | 4 | Security under SEC |
| Co-GP / JV equity | 4 | Security under SEC |
| Fund-of-fund / SMA | 4 | Investment company activity |
| LIHTC syndication (investor LP) | 4 | Security under SEC + state HFA |
| NMTC allocation (investor LP) | 4 | Security under SEC + CDFI Fund |
| Crowdfund LP (Reg D 506(c)) | 4 | Security under SEC + state |

## Per-lane execution checklist

### Lane 1 (CRE debt)
- [ ] Sponsor's commercial mortgage broker license verified
- [ ] State-by-state license check if multi-state
- [ ] NMLS disclosure if required
- [ ] Loan estimate / good faith estimate per RESPA if applicable
- [ ] Reg D exemption not required (not a security)

### Lane 2 (residential MLO)
- [ ] Sponsor's state MLO license verified
- [ ] NMLS unique identifier disclosed
- [ ] State-specific disclosure language attached
- [ ] Reg D exemption not required
- [ ] TRID compliance (Loan Estimate, Closing Disclosure)

### Lane 3 (mezz)
- [ ] Counsel review of mezz docs
- [ ] Intercreditor agreement between senior + mezz
- [ ] Reg D exemption if structured as PIK-with-equity-kicker

### Lane 4 (securities)
- [ ] Reg D exemption claimed (506(b) or 506(c))
- [ ] Form D filed with SEC within 15 days of first sale
- [ ] State blue-sky filings if required
- [ ] Investor verification (accredited / qualified purchaser)
- [ ] Securities counsel review of all offering docs (PPM, operating agreement, subscription agreement)
- [ ] FINRA review if any broker-dealer activity
- [ ] Subscription agreement + KYC/AML completed

## Lane 4 — Reg D 506(b) vs 506(c) decision

| Rule | 506(b) | 506(c) |
|---|---|---|
| General solicitation | ✗ Prohibited | ✓ Allowed |
| Investor relationship requirement | Pre-existing substantive relationship | None (but must verify accredited) |
| Investor cap | Unlimited accredited + up to 35 sophisticated | Unlimited accredited only |
| Accredited verification | Self-attest OK | Required (CPA letter, tax returns, W-2, etc.) |
| Form D filing | Required within 15 days of first sale | Required within 15 days of first sale |
| Annual report | None | None |
| Best for | Warm network (FFO, family, friends, broker) | Cold outreach (institutional, online, mass marketing) |

**Default for KlickSmartAI-drafted outreach:** 506(b) — assume warm network. Switch to 506(c) only if sponsor has verified-accredited investor funnel + counsel approval.

## Disclaimers

Every client-facing artifact should carry:

> **Compliance.** This document is for informational and planning purposes only. Nothing herein is an offer to sell or solicitation to buy any security. KlickSmartAI does not provide legal, tax, securities, or mortgage-origination advice. Sponsor is responsible for engagement of licensed professionals (MLO, RIA, broker-dealer, securities counsel) before any solicitation, commitment, or closing.

## Reference

- Full compliance rules: `../../_config/compliance.md`
- Worked example: `~/wiki/clients/veritas-developments/_config/` (if present) or use the Veritas Notion doc as reference

# Step 07 — Deliverables

What to produce for the client at each stage. Output: `deliverables/<developer-slug>/`.

## Stage → Deliverable map

| Stage | Deliverable | Format | Audience |
|---|---|---|---|
| Post-intake (Stage 20) | Intake confirmation memo | `.md` | Sponsor |
| Post-stack-design (Stage 30) | Capital stack map | `.md` + diagram | Sponsor + counsel |
| Post-TAM (Stage 40) | TAM CSV + shortlist | `.csv` + `.md` | Sponsor + broker |
| Post-scorecard (Stage 40) | Fit-scorecard | `.md` + table | Sponsor + counsel |
| Post-outreach-draft (Stage 50) | Outreach sequence | `.md` + per-touch templates | Sponsor |
| Pre-outreach (Stage 60) | Compliance-routed outreach package | `.md` + per-touch templates | Sponsor + counsel |
| Pre-TS (Stage 70) | Term-sheet comparison model | `.xlsx` or `.md` table | Sponsor + counsel |
| Post-closing (Stage 90) | Closing memo + post-close capture | `.md` | Sponsor + KlickSmartAI knowledge base |

## Per-deliverable schema

### Intake confirmation memo (Stage 20)
- Sponsor, asset, market, deal size, stage, overlays, timeline
- Compliance posture + lane assignment
- Open questions for sponsor
- Next steps

### Capital stack map (Stage 30)
- 5-layer model with $/% per layer
- Per-layer lender candidates (3-5 each)
- Per-layer assumptions (LTC, LTV, DSCR, pref, promote)
- Tax credit / public overlays (if applicable)
- Compliance routing per layer

### TAM CSV (Stage 40)
- Columns: tier, lender_slug, name, capital_type, asset_classes, geography, fit_score_initial, contact, source, last_verified

### Fit-scorecard (Stage 40)
- Per-lender scoring against 9 dimensions
- Weighted score
- Tier-aware cutoff
- Shortlist (top 5-10) + longlist (bottom half of survivors)

### Outreach sequence (Stage 50)
- 7-touch plan
- Per-touch template (email, LinkedIn, call script)
- Per-touch compliance disclaimer
- Per-touch owner (sponsor / KlickSmartAI / counsel)

### Compliance-routed outreach package (Stage 60)
- Lane classification per capital source
- Reg D exemption strategy (506(b) or 506(c))
- Per-touch disclaimer
- Form D filing plan (if Lane 4)
- State-by-state license check (if Lane 2)

### Term-sheet comparison model (Stage 70)
- Per-TS columns: lender, asset coverage, leverage, rate, term, amort, recourse, fees, pref, promote, covenants, conditions, expiration
- Side-by-side comparison
- Recommended TS
- Negotiation priorities

### Closing memo (Stage 90)
- Final terms
- Closing checklist
- Post-close obligations
- Lessons learned (for KlickSmartAI knowledge base)

## Standard disclaimers

Every deliverable carries (per `_config/compliance.md`):

> **Compliance.** This document is for informational and planning purposes only. Nothing herein is an offer to sell or solicitation to buy any security. KlickSmartAI does not provide legal, tax, securities, or mortgage-origination advice. Sponsor is responsible for engagement of licensed professionals (MLO, RIA, broker-dealer, securities counsel) before any solicitation, commitment, or closing.

## Self-host constraint

Per Dennis's standing rule:
- No plain-text credentials in delivered artifacts
- Use `[REDACTED]` for passwords, API keys, account numbers, PII
- Self-host all credential storage (no shared docs, no email attachments with credentials)

## Reference

- `~/wiki/clients/veritas-developments/deliverables/` — worked examples of TAM CSV, county intelligence, KCCLT partnership memo, east-side pilot pro-forma
- `~/wiki/clients/veritas-developments/projects/prime-lees-summit-co-sponsor-brief.md` — worked example of a co-sponsor / GP brief

# Business Funding Canada

> **Pay-per-lead generation for Canadian SMB business funding.** BFC captures qualified SMB-owner funding requests and **resells leads** to other funders / brokers who close and fund the deal. The site exists to *originate* funding inquiries, not to underwrite them.

> **Model:** BFC = front-of-funnel. Other funders / brokers / lenders (the "buyers") pay per qualified lead delivered. BFC does NOT lend its own capital. BFC does NOT close the borrower.

> **Note:** Workspace in scaffold state. CLAUDE.md (entry-point adapter) is pending Dennis's approval — protected agent-instruction file. IDENTITY.md holds the binding rules in the meantime.

---

## What this workspace is for

A new site / brand that **generates and qualifies leads** for the alt-SMB funding market in Canada. The 9 verticals below define the **lead products** BFC sells:

## Vertical map (subject)

| Vertical | Audience | Lead product |
|----------|---------|-----------------|
| Growth | Growing SMBs | Lead — Growth capital ready |
| Buyouts & Acquisitions | Acquirers | Lead — M&A / buyout ready |
| Restructuring | Distressed / turn-around | Lead — Restructuring / turnaround |
| Slow Receivables | B2B with long AR | Lead — A/R financing needed |
| Unexpected Events | Reactive needs | Lead — Bridge / emergency capital |
| Equipment | Capex-heavy SMBs | Lead — Equipment financing |
| Inventory | Retail / wholesale | Lead — Inventory financing |
| Small Business Loans | Sub-$250K needs | Lead — Term loan / LOC |
| ABL | Mid-market | Lead — ABL ready |

## Status: 🟡 SCAFFOLD + NOTION DOC INCOMING (2026-10-02)

- Workspace created today
- Identity reframed for **pay-per-lead model**
- Accord Financial full sitemap scraped (35 pages, 648 KB) as competitor research
- Structured competitor summary drafted (`drafts/competitors/accord-financial-summary-2026-10-02.md`)
- CLAUDE.md pending approval
- Voice direction pending from Dennis
- **Next:** Notion doc from Dennis describing the business model

## Folder layout

```
business-funding-canada/
├── CLAUDE.md             # pending approval
├── IDENTITY.md           # workspace map + rules (REFRAMED for pay-per-lead)
├── CONTEXT.md            # task routing
├── README.md             # this file
├── _config/              # voice, conventions, glossary, compliance, gtm-skills, deliverables
│   └── lead-buyers/      # to be created — per-buyer contracts, pricing, SLA
├── projects/             # validated deliverables (source of truth)
├── drafts/               # AI work in progress (pre-HITL)
│   └── competitors/      # competitor briefs (Accord summary here)
├── deliverables/         # client-ready exports
├── drafts-preview/       # HTML previews
├── skills/               # client-specific skills
└── research/
    └── competitors/
        └── accord-financial/
            └── 2026-10-02/   # 35 .md files (Accord full sitemap scrape)
```

## Compliance (PPL — pay-per-lead model)

- **PIPEDA** — SMB owner PII (financials, identity) is protected at capture and at every disclosure to a lead buyer. **Express consent required** for transfer.
- **CASL** — Express consent for marketing email/SMS to lead sources.
- **No provincial mortgage-broker regulator** applies (BCFSA / RECA / FSRA / OACIQ are all mortgage-only).
- **No rate quote, no "guaranteed approval", no lending language** in BFC copy — BFC is lead generation; the buyer funds.

See `_config/compliance.md`.

## Open — awaiting Dennis

1. **Notion doc** describing the business model (incoming this turn).
2. CLAUDE.md approval.
3. Wedge verticals for first 90 days (which of the 9 lead products ship first).
4. Voice direction (default = "transparent lead-generation for SMB funding", but confirm).
5. First deliverable — landing page, content article, or lead-form spec?
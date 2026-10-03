---
type: Client Workspace
okf_version: "0.2"
title: "Business Funding Canada — Identity"
client: business-funding-canada
status: active
generated: 2026-10-02
verified: 2026-10-02
manifest:
  client: business-funding-canada
  version: "0.1"
  generator: icm-client-workspace-setup
---

# Business Funding Canada — Workspace Identity

> **Pay-per-lead generation** for Canadian SMB business funding. BFC captures qualified SMB-owner funding requests and **resells leads** to other funders / brokers who close and fund the deal. The site exists to *originate* funding inquiries, not to underwrite them.

> **Model:** BFC is the front-of-funnel. Other funders / brokers / lenders (the "buyers") pay per qualified lead delivered. BFC does NOT lend its own capital. BFC does NOT close the borrower.

This is a **client workspace** inside the KlickSmartAI wiki. It follows the
ICM 3-layer pattern (Identity → Context → Config) and obeys the wiki
source-of-truth rule: **AI-generated content ALWAYS lands in `drafts/`** first;
nothing moves to `projects/` or `deliverables/` until Dennis approves (HITL gate).

---

## Vertical map (SMB financing surface area)

> These are the **subject verticals** — the SMB funding situations BFC captures leads for. Each vertical defines a **lead product** that BFC sells to funders.

| Vertical | Audience | Lead product |
|----------|---------|-----------------|
| `growth` | Growing SMBs | Lead — Growth capital ready |
| `buyouts` | Acquirers | Lead — M&A / buyout ready |
| `restructuring` | Distressed/turnaround | Lead — Restructuring / turnaround |
| `slow-receivables` | B2B with long AR | Lead — A/R financing needed |
| `unexpected-events` | Reactive needs | Lead — Bridge / emergency capital |
| `equipment` | Capex-heavy SMBs | Lead — Equipment financing |
| `inventory` | Retail / wholesale | Lead — Inventory financing |
| `small-business-loans` | Sub-$250K needs | Lead — Term loan / LOC |
| `abl` | Mid-market | Lead — ABL ready |

**Lead-buyer relationships live in a **separate channel** (`_config/lead-buyers/` once populated). Each lead buyer may buy one or more verticals; lead pricing, exclusivity, and SLA per vertical are negotiated per buyer.

---

## Folder Map

```
business-funding-canada/
├── CLAUDE.md            # Hermes + Claude Code entry-point (auto-loaded)
├── IDENTITY.md          # you are here — Layer 0 (workspace map + rules)
├── CONTEXT.md           # Layer 1 — task routing table
├── README.md            # human-facing overview
├── _config/             # Layer 2 — voice, conventions, glossary, compliance, gtm-skills
│   ├── voice.md
│   ├── conventions.md
│   ├── deliverables.md
│   ├── glossary.md
│   ├── compliance.md    # financial services — PIPEDA + provincial
│   └── gtm-skills.md
├── projects/            # Layer 4 — validated deliverables (source of truth)
├── drafts/              # Layer 4 — AI work in progress (pre-HITL)
├── deliverables/        # Layer 4 — client-ready exports
├── drafts-preview/      # Layer 4 — HTML previews of drafts/
├── skills/              # client-specific skills (optional)
└── research/            # research runs
    └── competitors/
        └── accord-financial/
                └── 2026-10-02/   # Accord Financial full sitemap scrape (648 KB, 35 .md files)
```

---

## Stage Map (Quick-mode — virtual stages defined in CONTEXT.md)

Default pipeline:

```
01_intake → 02_research → 03_draft → 04_review → 05_publish
   |            |            |          |            |
drafts/      drafts/      drafts/    drafts/      projects/  +  deliverables/
                                                          (HITL gate at 04→05)
```

---

## Compliance mode

**Mode:** `privacy` + `financial-services` + `lead-generation` (Canada)

**Adjusted for pay-per-lead operation:**
- BFC is NOT a lender, broker, or mortgage broker. **No provincial mortgage-broker regulator applies** (BCFSA / RECA / FSRA / OACIQ are all mortgage-broker regulators and are out-of-scope here).
- BFC **must register / comply with provincial lead-generation rules** where applicable — varies by province.
- **PIPEDA** governs PII capture from SMB owners. Critical: every lead transferred to a buyer is a PIPEDA-controlled disclosure — express consent required.
- **CASL** governs marketing email/SMS to lead sources.
- **No rate quote, no "guaranteed approval", no lending language** in BFC copy. BFC is lead generation; the buyer funds.

`_config/compliance.md` is the binding read for any client-facing copy. **Lead-buyer contracts** (consent to transfer, IP, exclusivity, SLA) live in `_config/lead-buyers/` (when present).

---

## Raw Source Locations

| Source | Path | Contents |
|--------|------|----------|
| Accord Financial competitor scrape | `research/competitors/accord-financial/2026-10-02/` | Full sitemap scrape: 35 .md files, 648 KB. Reference benchmark for product surface area + IA. |
| (more reserves) | `research/<run>/` | future research runs |

---

## Rules

1. **Source-of-truth gate.** AI-generated content ALWAYS lands in `drafts/` first.
2. **HITL gate.** Promotion requires Dennis's explicit approval.
3. **Routing first.** Read `CONTEXT.md` at session start.
4. **Voice follows `_config/voice.md`.**
5. **Citations required.** Every external claim carries the URL inline.
6. **No autonomous sends.**
7. **Compliance reads mandatory.** Any rate quote, payment estimate, or qualification language requires a compliance check.
8. **No real borrower / SMB financials in `drafts/`.** Use synthetic placeholders.
9. **Escalate uncertainty.**

---

## Escalation

| Situation | Action |
|-----------|--------|
| Borrower / SMB financials in source data | STOP. Synthetic placeholders only. |
| Rate quote without date + lender source | STOP. Compliance check first. |
| Marketing email going to SMB leads | Express-consent verification per CASL. |
| Lender / competitor relationship fact | Add `[VALIDATE: <source>]` and gate to projects/. |
| New vertical beyond the 9 here | Propose in `drafts/` before adding to IDENTITY.md. |

---

## Migration / generation notes (2026-10-02)

- Initial scaffold. CLAUDE.md pending — blocked on user approval (protected file).
- Accord Financial scrape ingested as `research/competitors/accord-financial/2026-10-02/`. Will be referenced as the SMB-financing IA benchmark when building this site's first vertical.
- Vertical set will start with `landing-page` + `content` for the first end-to-end run; verticals in the **Vertical map** table above are the **subject verticals**, not the **deliverable verticals** yet.
---
title: "Investor White Paper — Paper 1 — Claim Register (empty, awaiting population)"
type: claim-register
client: veritas-developments
paper: 1-of-6
paper_title: "Manufacturing Development Certainty"
governing_plan: "drafts/white-paper-program/wp1-research-plan-2026-10-10.md"
canonical_source: "drafts/notion-mirror/investor-white-paper-2026-09-08.md"
prepared_by: agent:hermes
prepared_on: 2026-10-10
status: empty — awaiting Dennis evidence-quality review of research plan before population
next_step: "populate rows after research plan approved"
okf_version: "0.2"
---

# Paper 1 — Claim Register (empty)

> **Why this file is empty:** Per the Notion HITL workflow, the claim register is built AFTER the research plan is approved by Dennis (evidence-quality owner). This file is the schema + template only. No claims have been collected.
>
> **What goes here:** Every quantitative, legal, tax, market, and project claim intended for the Paper 1 draft. One row per claim. Every claim must be sourced, classed, and confidence-rated before it can move from `unverified` to `supported`.

## How to read this register

Each row corresponds to one claim that will appear in the Paper 1 draft. A claim is `supported` only when (a) the source is recorded, (b) the source is on the approved source hierarchy (per the research plan), (c) the claim class is set, (d) the confidence rating is justified, and (e) the reviewer assignment is made.

Claims that cannot reach `supported` status are either (i) revised, (ii) removed, or (iii) flagged as `open` in the draft as `**[OPEN ITEM: <what is needed>]**`.

## Schema (locked, from research plan §"Source-record schema")

| Field | Description |
|---|---|
| Claim ID | `WP1-C###` (auto) |
| Proposed claim | Quoted text intended for the draft |
| Claim class | One of: `FACT-V` (verified fact) / `FACT-S` (sponsor-provided) / `ASSUMP` (underwriting assumption) / `PROJ` (projection) / `DRAFT` / `CLAIM-A` (approved external claim) / `CONF` (confidential — never published) / `SUPERSEDED` |
| Source (URL) | Public link or internal doc path |
| Publisher | Source organization / Veritas project |
| Publication date | YYYY-MM-DD |
| Data period | What the source measures (e.g., "2024 ACS 5-year estimates") |
| Retrieval date | YYYY-MM-DD |
| Geography | Exact metro / county / submarket |
| Methodology | How the figure is calculated (units, base, weighting) |
| Confidence | `H` / `M` / `L` + reason |
| Section # | Which of the 14 sections the claim lands in |
| Reviewer | `D` (David) / `Dn` (Daniel) / `Sp` (specialist) / `n/a` |
| Status | `unverified` / `supported` / `disputed` / `revised` / `removed` |

## Claim register (empty)

| Claim ID | Proposed claim | Class | Source (URL) | Publisher | Pub date | Data period | Retrieval | Geography | Methodology | Confidence | Section | Reviewer | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | _awaiting population_ | | | | | | | | | | | | |

## Confidence rubric (locked)

- **H** = primary government / municipal / Veritas internal contract / data ≤ 12 months old
- **M** = brokerage / appraisal / industry research with disclosed methodology; or data 12-36 months old
- **L** = aggregator, business media context, or data > 36 months old → must be upgraded or removed

## Claim class quick reference (locked)

| Class | Tag | Treatment in draft |
|---|---|---|
| Verified Fact | `FACT-V` | Cite inline; full source in bibliography |
| Sponsor-Provided Fact | `FACT-S` | Cite inline; flagged as sponsor-sourced |
| Underwriting Assumption | `ASSUMP` | Disclose; show base / upside / downside / severe downside |
| Projection | `PROJ` | Disclose horizon + sensitivity; no certainty language |
| Draft | `DRAFT` | Internal only; never public |
| Approved External Claim | `CLAIM-A` | Cite source + Veritas approval on file |
| Confidential | `CONF` | Do not include in paper; deal-room only |
| Superseded | `SUPERSEDED` | Do not include; reference superseded-by doc |

## Reviewer assignment (locked)

| Reviewer | What they review |
|---|---|
| David Poole | Strategy, operating capabilities, intended positioning, development process + construction practicality, project descriptions / quantities / status / sponsor representations, land control / entitlement / horizontal-delivery logic, whether any statement exceeds what Veritas can prove or execute |
| Daniel Bailey | Real estate / brokerage / transaction language, landowner / builder / buyer assumptions, comparable-property and market-context relevance, sourcing / acquisition / disposition pathways, pricing / demand / liquidity / buyer-class claims, whether the CTA supports qualified conversations |
| Dennis Eng | Evidence quality — source quality, claim class discipline, OPEN ITEM hygiene, no fabricated data |
| Specialist | Triggered per claim (attorney / CPA / engineer / appraiser / licensed financing professional) |

## Population workflow

After Dennis approves the research plan, the register is populated in this order:

1. **§1 Executive summary** — 1 thesis claim + 3-5 evidence points (Veritas + KC market)
2. **§4 Green Acres four-step model** — 1 claim from Veritas Business Plan 2026
3. **§7 Seven-stage parcel lifecycle** — 7 stage definitions from Veritas source
4. **§8 Six investment gates** — 6 gate definitions from Veritas source
5. **§11 Capital-at-risk ladder** — staged cap model from Veritas source
6. **§12 Walk-away discipline** — 5+ stress tests + thresholds
7. **§2 Failure modes** — 3+ named sources (academic / institutional)
8. **§3 Raw acreage ≠ investment** — appraiser / institutional definition
9. **§5 Control before ownership** — legal definitions (attorney pre-clearance)
10. **§6 Residual method** — institutional reference + project-specific inputs
11. **§9 Demand-led design** — Veritas LOIs + brokerage market evidence
12. **§10 Entitled / shovel-ready / finished-pad exits** — Veritas exit criteria + buyer-class research
13. **§13 Worked example** — labeled hypothetical OR David + Daniel-approved project
14. **§14 CTA** — David + Daniel-approved + attorney pre-cleared

Each populated claim moves through: `unverified` → research → `supported` (or `disputed` / `removed`).

## Open questions blocking population (per research plan §"Open questions for Dennis")

1. Business Plan 2026 on file location
2. Veritas internal claim scope
3. CTA legal review sequencing
4. Project redacted example availability
5. Investor Mind Map access

These are tracked in `drafts/VALIDATION_QUEUE.md` item 7.

---

*This register is the gate. The draft is the gate after that. Nothing becomes paper without David + Daniel joint approval.*

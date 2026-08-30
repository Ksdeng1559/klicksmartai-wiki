---
type: Playbook
title: CDFI 7-touch outreach — callable SOP
description: Sequential 7-touch cold-outreach cadence for faith-aligned CDFIs, verified against Reg D 506(b). Callable by any LLM that reads this file.
tags: [sop, cdfi, cold-outreach, faith-aligned-capital, callable]
status: stable
parameters:
  - { name: leads_csv, type: string, required: true, description: "path to CSV with columns: name, email, organization, tier, relationship_status" }
  - { name: tier_filter, type: string, required: false, description: "tier values to include (default: 1,2)" }
  - { name: cadence_start, type: date, required: true, description: "ISO date for touch 1 (e.g. 2026-09-01)" }
  - { name: compliance_check, type: boolean, required: true, description: "must be true; every lead must be a pre-existing substantive relationship or accredited investor with verifiable prior connection" }
executor:
  resource: /sop/run-cdfi-cadence.py
  receipt: [lead_ids_processed, touch_log, draft_paths, validation_queue_row]
attester:
  resource: /sop/attesters/verify-cdfi-cadence.py
generated: { by: human:dennis, at: 2026-08-29T14:00:00Z }
verified:
  - { by: human:david_poole, at: 2026-08-29T14:00:00Z }
  - { by: human:daniel_bailey, at: 2026-08-29T14:00:00Z }
stale_after: 2027-02-28T00:00:00Z
sources:
  - id: reg-d-overlay
    resource: /_config/compliance.md
    title: Reg D 506(b) compliance overlay
  - id: cdfi-tam-2026-08-22
    resource: /intelligence/cdfi-tam-2026-08-22/notebook.md
    title: CDFI TAM list (2026-08-22)
  - id: gtm-binding
    resource: /_config/gtm-skills.md
    title: GTM skills registry (cold-outreach + enrichment bindings)
okf_version: "0.2"
---

# CDFI 7-touch outreach — callable SOP

You are the cadence runner. The user supplies `leads_csv`, `cadence_start`, and `compliance_check=true`. Optional `tier_filter` (default tiers 1, 2).

## Pre-conditions (all must hold)

- `compliance_check` is `true`. Every lead is a **pre-existing substantive relationship** or an **accredited investor with a verifiable prior connection** under Reg D 506(b).[^reg-d-overlay]
- Every lead row has `name`, `email`, `organization`, `tier`, `relationship_status`.
- A `VALIDATION_QUEUE.md` row is created before touch 1 fires (source-of-truth gate).
- No autonomous send. Drafts only; Dennis + David approve before any send.

## Steps

1. **Load** `leads_csv`. Filter by `tier_filter` (default tiers 1, 2).
2. **Classify** each lead by `relationship_status`:
   - `existing` → warm sequence (touch 1 = direct ask)
   - `warm-intro` → intro sequence (touch 1 = reference mention)
   - `cold` → standard 7-touch (touch 1 = handshake)
3. **Build the 7-touch cadence** per lead, starting `cadence_start`:
   - Touch 1 (Day 0): handshake — name the shared faith-aligned-capital thesis, one line on Veritas's Jackson County MO work.
   - Touch 2 (Day 3): signal acknowledgment — reference the CDFI's recent fund deployment or hiring signal.[^cdfi-tam]
   - Touch 3 (Day 7): value — the Co-Sponsor Capital TAM list or county intelligence brief.
   - Touch 4 (Day 12): proof — a deal-by-deal IRR / MOIC example from a comparable sponsor.
   - Touch 5 (Day 18): objection — address the most likely concern (check size, geography, faith alignment).
   - Touch 6 (Day 25): soft close — invite to a webinar or a 15-min intro call.
   - Touch 7 (Day 35): final — one-line re-ask, then stop. No further touches without a new signal.
4. **Draft** each touch to `drafts/email/<lead-slug>/touch-N.md` (source-of-truth gate: drafts, never projects).
5. **Preflight** every touch through `cold-email-preflight` (Reg D 506(b) + deliverability) before it is queued.
6. **Write the receipt** (see below) and add the `VALIDATION_QUEUE.md` row.

## Receipt format

The executor returns a JSON receipt shaped by `executor.receipt`:

```json
{
  "lead_ids_processed": ["cdfi-001", "cdfi-002"],
  "touch_log": [
    { "lead_id": "cdfi-001", "touch": 1, "draft_path": "drafts/email/cdfi-001/touch-1.md", "preflight": "pass" }
  ],
  "draft_paths": ["drafts/email/cdfi-001/touch-1.md"],
  "validation_queue_row": "drafts/VALIDATION_QUEUE.md#cdfi-7-touch-2026-08-29"
}
```

## Attestation

The attester (`/sop/attesters/verify-cdfi-cadence.py`) deterministically checks the receipt:
- every `draft_path` exists and is under `drafts/` (never `projects/`),
- every touch has `preflight: pass`,
- `compliance_check` was `true` at invocation,
- the `VALIDATION_QUEUE.md` row exists.

A failing attestation means the run did not follow the sanctioned SOP — do not present it as a Veritas deliverable.

## Why this is callable

Any LLM — ChatGPT, Claude, Gemini, Hermes, Mistral — can read this file, understand the `parameters[]`, follow `executor.resource`, run the cadence, and check `attester.resource`. No KlickSmartAI skill install required. The folder is the knowledge graph; this SOP is a node with a call signature.

[^reg-d-overlay]: /_config/compliance.md §3
[^cdfi-tam]: /intelligence/cdfi-tam-2026-08-22/notebook.md

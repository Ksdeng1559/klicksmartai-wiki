---
type: Reference
title: "Folder contract — lead-magnet"
description: OKF v0.2 frontmatter; type/status visible to any LLM that reads the bundle.
status: stable
generated: { by: human:dennis, at: 2026-08-29T18:00:00Z }
verified: []
okf_version: "0.2"
---
# drafts/lead-magnet/ — Veritas AI Work in Progress for lead-magnet

**Purpose:** AI-generated lead-magnet drafts for Veritas Development Group LLC. Pre-HITL, NOT source-of-truth.

**Gate:** Promotion to `projects/lead-magnet/` or `deliverables/lead-magnet/` requires Dennis + David (or Daniel for relationship facts) approval via the parent `drafts/VALIDATION_QUEUE.md`.

## Vertical config

- **Type:** lead-magnet
- **Default Hermes skill:** see `../../_config/deliverables.md`
- **Source format:** `.md` is canonical. Generated `.html`/`.mp4`/`.png` lives here until HITL.

## Procedure

1. Create `<artifact>-<YYYY-MM-DD>.md` here — the markdown source / spec.
2. Run the configured Hermes skill to produce the asset.
3. Add a row to `../VALIDATION_QUEUE.md` (parent `drafts/`) — artifact, type=lead-magnet, approvers, status.
4. Build any preview into `../../drafts-preview/lead-magnet/` (optional).
5. On HITL approval: `.md` → `../../projects/lead-magnet/`, asset → `../../deliverables/lead-magnet/`.

# drafts/email/ — Veritas AI Work in Progress for email

**Purpose:** AI-generated email drafts for Veritas Development Group LLC. Pre-HITL, NOT source-of-truth.

**Gate:** Promotion to `projects/email/` or `deliverables/email/` requires Dennis + David (or Daniel for relationship facts) approval via the parent `drafts/VALIDATION_QUEUE.md`.

## Vertical config

- **Type:** email
- **Default Hermes skill:** see `../../_config/deliverables.md`
- **Source format:** `.md` is canonical. Generated `.html`/`.mp4`/`.png` lives here until HITL.

## Procedure

1. Create `<artifact>-<YYYY-MM-DD>.md` here — the markdown source / spec.
2. Run the configured Hermes skill to produce the asset.
3. Add a row to `../VALIDATION_QUEUE.md` (parent `drafts/`) — artifact, type=email, approvers, status.
4. Build any preview into `../../drafts-preview/email/` (optional).
5. On HITL approval: `.md` → `../../projects/email/`, asset → `../../deliverables/email/`.

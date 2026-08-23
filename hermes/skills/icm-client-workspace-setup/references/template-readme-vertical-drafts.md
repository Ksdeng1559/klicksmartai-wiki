# drafts/<vertical>/ — AI Work in Progress for <vertical>

**Purpose:** Working drafts of <vertical> deliverables for <client_name>. Anything here is AI-generated, pre-HITL, and NOT source-of-truth.

**Gate:** Same source-of-truth rule applies — promotions require explicit Dennis + relevant vertical-validation.

## Files in this folder

_<initially empty>_ Add artifacts here as the user briefs them.

## Built with

- **Default Hermes skill:** `<vertical-skill>` (configured in `_config/deliverables.md`)
- **Source format:** `.md` is canonical. Generated `.html`, `.mp4`, `.png`, etc. live alongside.
- **Voice rules:** start from `_config/voice.md`, override in `<vertical>/voice.md` if the user gives direction.

## Procedure

1. Create `<vertical>/<artifact-name>-<YYYY-MM-DD>.md` — the markdown source / spec.
2. Run the configured Hermes skill to produce the asset.
3. Update `VALIDATION_QUEUE.md` (under `drafts/<vertical>/`) with the artifact + approvers.
4. Build any preview needed (HTML rendered into `drafts-preview/<vertical>/`).
5. Wait for HITL. On approval, promote: `.md` → `projects/<vertical>/`, asset → `deliverables/<vertical>/`.

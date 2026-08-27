# projects/

Validated deliverables — source of truth artifacts.

**Per the ICM source-of-truth gate:** nothing lands here until promoted from `drafts/` after Dennis's explicit approval. See `drafts/VALIDATION_QUEUE.md` for the HITL ledger.

## Promotion contract

To promote a file from `drafts/` → `projects/`:
1. The file has a row in `drafts/VALIDATION_QUEUE.md` with `status = approved`.
2. The approver matches the artifact type (e.g. module code requires technical review; data artifacts require dataset validation).
3. The promoted file is renamed (no version suffix — the approved version is canonical).

## Currently empty

This client has no validated deliverables yet. Module work has been committed to the GitHub fork; analytical artifacts are in `.local_tier/` (data, not source of truth for the engagement).
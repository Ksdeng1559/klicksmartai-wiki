# Validation Queue

Every file in this `drafts/` folder starts as `pending Dennis review`. Promote to `projects/` or `deliverables/` only after explicit approval.

| File | Status | Approver | Promoted date | Notes |
|---|---|---|---|---|
| (none yet) | — | — | — | Workspace scaffolded 2026-10-10; no drafts in flight |

## How to use

1. Add a new row when a draft is created
2. Mark `pending Dennis review` once surfaced
3. Wait for Dennis's explicit `approve` / `promote` / `kill`
4. On approval, move file to `projects/<slug>/` or `deliverables/`, set `status: approved` in frontmatter
5. Update this queue row with date + approver
6. Never auto-promote. Never auto-archive.

## Statuses

- `pending` — drafted, awaiting review
- `in-review` — Dennis actively reviewing
- `approved` — promoted to `projects/` or `deliverables/`
- `revise` — Dennis asked for changes; loop back
- `killed` — discarded (move to `drafts/_killed/`, do not delete)

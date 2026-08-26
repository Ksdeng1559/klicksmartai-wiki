# drafts/

AI work in progress — pre-HITL. **All AI-generated client content MUST land here first**, per the source-of-truth gate.

## Gate ledger

`VALIDATION_QUEUE.md` lives here. Every artifact in `drafts/` has a row with:
- File path
- Artifact type (module-code, data-export, skill, doc)
- Author (which agent or human)
- Status (`pending` | `approved` | `rejected` | `needs-revision`)
- Approver required
- Date created

On approval → promote `.md` (source) to `projects/`, plus rendered artifact (if any) to `deliverables/`.

## Currently empty

No drafts yet. The PAA module work + DuckDB mirror are operational artifacts (code + data), not draft deliverables. When the next module is started, document it here first.
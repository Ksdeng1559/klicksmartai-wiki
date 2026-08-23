# skills/ — Client-Specific Skills (optional)

**Purpose:** Hermes skills scoped to Veritas-specific mechanical steps or repeated procedures. General ICM skills live at `~/.hermes/skills/` (cross-project); client-specific ones live here so they stay with the workspace.

**What could live here:**
- `veritas-intake` — run the Stage 01 intake for a new Veritas deliverable
- `veritas-promote` — promote an approved draft from `drafts/` → `projects/` + `deliverables/` (enforces HITL gate)

**Rule:** A skill here must not bypass the source-of-truth gate. Any skill that writes client content must send it to `drafts/`, never directly to `projects/`.

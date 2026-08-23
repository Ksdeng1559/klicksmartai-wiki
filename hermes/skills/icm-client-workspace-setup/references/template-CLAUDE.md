<!-- Auto-generated Hermes + Claude Code adapter — points at the ICM files both loaders pick up first -->

# <client_name> — Hermes / Claude Code Entry Point

## Session start
1. Read `IDENTITY.md` — workspace map, stage map, rules.
2. Read `CONTEXT.md` — task routing table + pipeline (Stage 01–05).
3. If touching an existing draft, read `drafts/VALIDATION_QUEUE.md` — the HITL gate ledger.

## ICM / Source-of-Truth Rules (non-negotiable)
1. Always start by reading `CONTEXT.md` for routing; never invent process steps already defined there.
2. **AI-generated client content ALWAYS lands in `drafts/` first.** Never write directly to `projects/` or `deliverables/`.
3. **No promotion from `drafts/` to `projects/` or `deliverables/` without Dennis's explicit approval.** See `drafts/VALIDATION_QUEUE.md`.
4. Voice, conventions, glossary, and compliance rules live in `_config/`. Read `_config/voice.md` and (if present) `_config/compliance.md` before drafting any deliverable.
5. **No autonomous client sends.** Draft outreach only; wait for an explicit "send it."
6. Write all intermediate/final artifacts into the correct folder (drafts/, projects/, deliverables/, drafts-preview/). Leave a short handoff note in the relevant `README.md` or `HANDOFF.md` after finishing.
7. Prefer tools + scripts for mechanical work; use the LLM for judgment.
8. Escalate uncertainty — stop and ask rather than inventing facts, names, or relationship claims.

## This folder is a sub-workspace
The wiki root `AGENTS.md` (graphify rules) applies above this. Once inside `<client_slug>/`, treat `CONTEXT.md` as the current job description and the rules above as binding.

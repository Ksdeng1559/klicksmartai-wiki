<!-- Auto-generated Hermes adapter — points at the ICM files Hermes loads first -->

# Veritas Developments — Hermes Entry Point

## Session start
1. Read `IDENTITY.md` — workspace map, stage map, rules.
2. Read `CONTEXT.md` — task routing table + pipeline (Stage 01–05).
3. If touching an existing draft, read `drafts/VALIDATION_QUEUE.md` — the HITL gate ledger.

## ICM / Source-of-Truth Rules (non-negotiable)
1. Always start by reading `CONTEXT.md` for routing; never invent process steps already defined there.
2. **AI-generated client content ALWAYS lands in `drafts/` first.** Never write directly to `projects/` or `deliverables/`.
3. **No promotion from `drafts/` to `projects/` or `deliverables/` without Dennis's (and, for relationship facts, David + Daniel's) explicit approval.** See `drafts/VALIDATION_QUEUE.md`.
4. Voice, conventions, glossary, and compliance rules live in `_config/`. Read `_config/voice.md` and `_config/compliance.md` before drafting any deliverable.
5. **No autonomous client sends.** Draft outreach only; wait for an explicit "send it."
6. Write all intermediate/final artifacts into the correct folder (drafts/, projects/, deliverables/, drafts-preview/). Leave a short handoff note in the relevant `README.md` or `HANDOFF.md` after finishing.
7. Prefer tools + scripts for mechanical work; use the LLM for judgment.
8. Escalate uncertainty — stop and ask rather than inventing facts, names, or relationship claims.

## This folder is a sub-workspace
The wiki root `AGENTS.md` (graphify rules) applies above this. Once inside `veritas-developments/`, treat `CONTEXT.md` as the current job description and the rules above as binding.

## Vertical artifact map
Read `_config/deliverables.md` for the per-vertical artifact map (8 verticals: website, landing-page, content, email, video-ad, ad-creative, deck, lead-magnet). New deliverables land in `drafts/<vertical>/` — flat files at the parent `drafts/` are legacy validated work and stay where they are.

## GTM skill bindings
Read `_config/gtm-skills.md` for the GTM use-case → Hermes skill bindings (7 use-cases bound: signal-based outbound, automated lead qualification, contact data enrichment, AI ABM targeting, AI-powered cold outreach, intent-based prospecting, AI SDR motion; plus 5 role mappings: AI SDR, Sales, Demand Gen, RevOps, CRO). Paid runs (Deepline / LeadSniper / Clay) require `gtm-enrichment-planner` HITL approval before any spend. Investor-touching outreach requires Reg D 506(b) screening (`_config/compliance.md` + `cold-email-preflight`).

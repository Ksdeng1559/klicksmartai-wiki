<!-- Auto-generated Hermes + Claude Code adapter — points at the ICM files both loaders pick up first -->

# OpenSEO — Hermes / Claude Code Entry Point

## Session start
1. Read `IDENTITY.md` — workspace map, env vars, modules, data storage.
2. Read `CONTEXT.md` — task routing table (sync mirror, query data, deploy, etc.).
3. Read `_config/conventions.md` — branch / commit / port / module conventions.
4. Read `_config/glossary.md` — D1, miniflare, PAA, social proxy, dormancy rules.

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

The wiki root `AGENTS.md` (graphify rules) applies above this. Once inside `open-seo/`, treat `CONTEXT.md` as the current job description and the rules above as binding.

## SEO Skill Catalog

This engagement produces **client-deliverable SEO skills**. The full catalog is at `_config/seo-skill-catalog.md` (14 skills, 5 layers). The gate skill `seo-enrichment-planner` is loaded globally and gates all spend below Layer 1. Per-client bindings are in `_config/seo-skills.md`.

**Every SEO skill that costs credits MUST present a HITL approval package before any spend. The user's "yes" / "no" / "adjust" response is the gate — never auto-spend.**

## Special Rules for This Client

This is a **technical/infra** client, not a deliverable client. The work output is:
1. **Code changes** to `/home/denni/repos/open-seo/` (committed to `Ksdeng1559/open-seo` fork)
2. **Container operations** (rebuild, restart, env var updates)
3. **Data operations** (DuckDB sync, MCP wiring)
4. **Module documentation** (skill files, README, IDENTITY updates)
5. **SEO skill authoring** (catalog, planner, layer skills)

There are **no per-vertical deliverable folders** because the engagement doesn't produce client-facing artifacts — it produces code and data.

## Module Dormancy

API-key-bearing modules (PAA, On-Page.ai, SAM agent) are **dormant** when their env var is missing. The source-of-truth gate still applies to any documentation produced about these modules — drafts/ first, then projects/.
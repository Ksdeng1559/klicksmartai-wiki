# skills/

**Per-client skill adapters.**

Client-specific skills — usually adapters that wrap a global skill (e.g. `seo-enrichment-planner`) with this client's specific configuration (locationCode, market, voice, compliance).

## Currently empty

No per-client skills yet. The 12 SEO skills in `~/.hermes/skills/` are global and apply to this client unmodified.

## When to add a client-specific skill

| Trigger | Action |
|---|---|
| The client has unique cost rules (e.g. "always cap rank tracking at 25 keywords") | Add a wrapper skill |
| The client has a unique voice rule (e.g. "never use the word 'luxury'") | Add a voice-enforcement skill |
| The client has a recurring SEO workflow (e.g. "every Tuesday, run PAA mining for our top 10 keywords") | Add a cron-driven skill |

## Suggested first per-client skill

`gpc-seo-sprint-runner` — orchestrates the full Phase 1-4 sprint from the quote sheet. Input: project state. Output: cost plan + sequence of skill invocations. Wraps `seo-enrichment-planner` with GPC-specific defaults (locationCode 2124, voice editorial, etc.).

## Pitfall

Don't duplicate global skills here. The 12 global SEO skills already handle GPC. Per-client skills should be **adapters** or **orchestrators**, not duplicates.

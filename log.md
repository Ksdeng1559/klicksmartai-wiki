# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> Rotate to log-YYYY.md when this file exceeds 500 entries.

## [2026-08-11] create | Wiki initialized
- Domain: Hermes Agent knowledge base (codebase + operator runbook + env patterns)
- Location: ~/hermes-wiki (separate from ~/wiki = KlickSmartAI client wiki)
- Structure created: SCHEMA.md, index.md, log.md, raw/{articles,papers,transcripts,assets}, entities/, concepts/, comparisons/, queries/, _meta/
- Source priority: Hermes source → installed skills → session history → memory → external docs

## [2026-08-11] ingest | Environment discovery from webui Docker deploy
- Raw: raw/articles/2026-08-11-environment-discovery.md
- Created: concepts/hermes-environment-map.md, concepts/hermes-webui-deployment.md, concepts/service-port-registry.md
- Cross-refs: all three pages link to each other and reference Service-Port-Registry

## [2026-08-11] ingest | Environment quirks (batch 1)
- Source priority: live config (~/.hermes/config.yaml, .env) + memory
- Created (8 pages):
  - concepts/api-keys-and-providers.md — provider catalog + key inventory
  - concepts/search-provider-rotation.md — Brave→Serper→Exa→Tavily→Parallel decision tree
  - concepts/gtm-enrichment-hitl-gate.md — paid-enrichment approval pattern
  - concepts/github-access-pattern.md — curl+PAT, no gh CLI
  - concepts/terminal-lifecycle-guard.md — heredoc ValueError workaround
  - concepts/obsidian-vault.md — vault path + PARA structure
  - concepts/gateway-restart-procedure.md — restart rules (never in-gateway)
  - entities/leadsniper-sgi.md — SGI module, Docker setup, Supabase pooler gotcha
- All cross-linked to hermes-environment-map and to each other

## [2026-08-11] ingest | Hermes internals (batch 2)
- Source: live read of ~/.hermes/hermes-agent/{gateway/, cron/, agent/, docs/}
- Raw: raw/articles/2026-08-11-hermes-source-tour.md
- Created (6 pages):
  - concepts/hermes-session-lifecycle.md — SessionSource/Entry/Context; lane vs incarnation IDs
  - concepts/hermes-gateway-architecture.md — runner, 15+ platform adapters, API Server adapter
  - concepts/hermes-cron-architecture.md — in-process vs Chronos scheduler; wire spec link
  - concepts/hermes-memory-subsystem.md — memory + user_profile; fact_feedback; Honcho deprecation
  - concepts/hermes-delegation.md — delegate_task; leaf vs orchestrator; vs spawning process
  - concepts/hermes-prompt-builder.md — environment hints; caching rules; remote-backend suppression
- All cross-link to source-tour raw + each other

## [2026-08-11] ingest | Active skills catalog (batch 3)
- Source priority: ~/.hermes/skills/.usage.json (telemetry) + skill_view() reads of top-loaded skills
- Wrote 7 entity pages for the skills with most session activity:
  - entities/skill-google-workspace.md (489 uses — top consumer)
  - entities/skill-b2b-outreach.md (440)
  - entities/skill-tavily-agent.md (283)
  - entities/skill-chief-of-staff.md (99)
  - entities/skill-spectra-pipeline.md (33)
  - entities/skill-hermes-cron-management.md (12)
  - entities/skill-claude-code.md
- ~156 other skills with non-zero use_count: not entity-paged individually (catalog reference; deepen on demand)
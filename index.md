# Wiki Index

> Content catalog. Every wiki page listed under its type with a one-line summary.
> Read this first to find relevant pages for any query.
> Last updated: 2026-08-11 | Total pages: 11

## Entities
- [[LeadSniper-Sgi]] — LeadSniperAI / SGI module plumbing, Docker setup, DataForSEO provider, Supabase pooler gotcha.
- [[Skill-Claude-Code]] — Delegate coding to Claude Code CLI (print mode + tmux PTY orchestration).
- [[Skill-Hermes-Cron-Management]] — Cron job management; PATH pitfall; git rebase pattern; jobs.json patching.
- [[Skill-Google-Workspace]] — Master Google APIs skill (Gmail/Calendar/Drive/Docs/Sheets); Tirith constraints.
- [[Skill-B2b-Outreach]] — B2B outreach intelligence umbrella (research + draft assembly).
- [[Skill-Spectra-Pipeline]] — Spectra Holdings $300M MCF county pipeline; 5-step sequence; faith-framed.
- [[Skill-Tavily-Agent]] — Tavily search/extract/crawl/research/mcp family; citation-backed outputs.
- [[Skill-Chief-of-Staff]] — Daily CoS routine (morning briefing, task prep, HITL outreach, EOD, cron audit).

## Concepts
- [[Hermes-Environment-Map]] — Where everything Hermes lives on Dennis's WSL+Windows+Docker box (HERMES_HOME, processes, Docker constraints).
- [[Hermes-Webui-Deployment]] — How hermes-webui was Docker-deployed 2026-08-11; commands, mount paths, startup-time gotchas.
- [[Service-Port-Registry]] — Live port map (8787 webui, 8644 gateway, 9119 dashboard, 8000/3002/8090/8080 other Docker).
- [[Api-Keys-And-Providers]] — Catalog of API keys in .env + provider routing (kimi-k3 primary, deepseek fallback).
- [[Search-Provider-Rotation]] — When to use Brave/Serper/Exa/Tavily/Parallel; never retry exhausted.
- [[Gtm-Enrichment-Hitl-Gate]] — Paid enrichment HITL pattern (swan + Deepline + LeadSniper; pilot→approval→execute).
- [[Github-Access-Pattern]] — How to call GitHub API (PAT at ~/.hermes/github-pat.txt; curl-only, no gh/.netrc).
- [[Terminal-Lifecycle-Guard]] — Heredoc/script-file crash mode (CPython #76762); use venv python + write_file instead.
- [[Obsidian-Vault]] — Vault at /mnt/g/Documents/KlicksmartWiki/Klicksmartai/ (PARA); separate from wikis.
- [[Gateway-Restart-Procedure]] — When/how to restart Hermes processes; never in-gateway, always user-initiated.
- [[Hermes-Session-Lifecycle]] — SessionSource/SessionEntry model; lane vs incarnation IDs; token accounting.
- [[Hermes-Gateway-Architecture]] — Gateway runner + 15+ platform adapters + API Server adapter for WebUI.
- [[Hermes-Cron-Architecture]] — In-process vs Chronos (NAS) scheduler; jobs.json + executions.db.
- [[Hermes-Memory-Subsystem]] — memory + user_profile stores; fact_feedback rule; Honcho deprecated.
- [[Hermes-Delegation]] — delegate_task single + batch; leaf vs orchestrator; vs spawning full process.
- [[Hermes-Prompt-Builder]] — System prompt construction; environment hints (local vs remote backend); caching rules.

## Patterns
- [[Gtm-Enrichment-Hitl-Gate]] — HITL approval pattern for paid enrichment.

## Comparisons

## Queries

## Raw sources
- `raw/articles/2026-08-11-environment-discovery.md` — observations captured during Docker webui deploy.
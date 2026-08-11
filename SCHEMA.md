# Wiki Schema

## Domain
Hermes Agent — knowledge base for the Hermes codebase, the operator runbook,
and the patterns that work in Dennis's environment. Built from first-party
sources (Hermes source, skills, sessions, memory) and curated through
hands-on use.

## Scope
- **Codebase reference**: modules, contracts, tool/toolset surface, gateway
  architecture, runtime contracts (per `docs/CONTRACTS.md`).
- **Operator runbook**: workflows Dennis actually runs (briefings, cron
  patterns, memory management, deploy/recovery playbooks).
- **Environment knowledge**: which APIs/keys, models, providers, ports, paths,
  quirks specific to this WSL+Windows+Docker setup.
- **Patterns that work**: workflows proven across sessions — model rotation,
  search rotation, batch tooling, HITL governance, etc.

NOT in scope: client-deliverable work (lives in ~/wiki, the KlickSmartAI
wiki), nor opinion/editorial commentary on Hermes design.

## Conventions
- File names: lowercase, hyphens, no spaces (e.g. `hermes-gateway.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- **Provenance**: on pages synthesizing 3+ sources, append `^[raw/articles/source.md]`
  to paragraphs whose claims trace to a specific source.
- **Confidence**: mark `confidence: low` for opinion-heavy or single-source claims;
  `high` only when well-supported across multiple sources.

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
confidence: high | medium | low        # optional
contested: true                        # optional
contradictions: [other-page-slug]      # optional
---
```

### raw/ Frontmatter
```yaml
---
source_url: https://example.com/article
ingested: YYYY-MM-DD
sha256: <hex digest of raw content below frontmatter>
---
```

The `sha256:` lets re-ingest skip unchanged files and flag drift when content changes.

## Tag Taxonomy
- **Codebase**: module, contract, tool, toolset, skill, plugin, mcp, gateway, cli
- **Runtime**: provider, model, session, cron, memory, profile
- **Operator**: workflow, runbook, deploy, recovery, briefing
- **Environment**: wsl, docker, windows, network, path, port, key
- **Patterns**: pattern, antipattern, gotcha, fix
- **Domain knowledge**: hermes-agent, hermes-webui, leadsniper, gateway, deepline, gtm
- **Meta**: comparison, timeline, summary, todo

Rule: every tag on a page must appear here. Add new tags here FIRST.

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create** for passing mentions or details outside this wiki's domain
- **Split** when a page exceeds ~200 lines — break into sub-topics with cross-links
- **Archive** when fully superseded — move to `_archive/`, remove from index

## Entity Pages
One page per notable entity (Hermes module, skill, provider, tool, command).
Include overview, key facts/dates, relationships ([[wikilinks]]), source references.

## Concept Pages
One page per concept (session lifecycle, cron scheduling, memory model,
provider rotation, etc.). Include definition, current state, open questions,
related concepts.

## Comparison Pages
Side-by-side analyses (provider A vs B, deployment topologies, etc.).
Include dimensions (table preferred), verdict, sources.

## Update Policy
When new info conflicts with existing content:
1. Check dates — newer sources supersede older
2. Note both positions with dates/sources if contradictory
3. Mark in frontmatter: `contradictions: [page-name]`
4. Flag in lint report

## Ingest Sources (priority order)
1. Hermes source code at `~/.hermes/hermes-agent/` (AGENTS.md, docs/CONTRACTS.md,
   hermes_cli/commands.py, agent/, tools/, gateway/)
2. Installed skills at `~/.hermes/skills/` (SKILL.md files)
3. Session history via `session_search` (patterns proven across runs)
4. Memory entries (mine for stable facts vs session outcomes)
5. External docs (Hermes-agent.nousresearch.com/docs, when they answer questions
   the source doesn't)

Skip: docs that paraphrase what's already in source, blog posts by third parties
unless they document a real workflow.
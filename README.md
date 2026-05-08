# KlickSmartAI Knowledge Wiki

Shared knowledge layer for all KlickSmartAI agents and LLMs.

## What This Is

This wiki is the **single source of truth** for all KlickSmartAI operations. Every LLM in the stack — Hermes, Claude, ChatGPT, Gemini — reads from and writes to this wiki. It is not a reference document. It is the actual knowledge layer.

## Stack

| Agent | Role |
|-------|------|
| **Hermes** | Curator, executor, daily maintainer |
| **Claude** | Coding, deep research, architecture |
| **ChatGPT** | Drafting, brainstorming, prototyping |
| **Gemini** | Multi-modal, context window work |

## Sync Sequence

All changes follow this order:

```
Wiki (~/wiki) → Graphify → GitHub
```

1. **Write** — edit files in ~/wiki
2. **Index** — `cd ~/wiki && graphify update .`
3. **Sync** — push to GitHub (two-way: fetch → merge → push)

## Branching Rule

Non-Hermes LLMs write to **feature branches only**. Open a PR for Hermes to review and merge into `master`. No direct force-push to master.

## Directory Structure

```
~/wiki/
├── clients/          # Client contexts, projects, history
├── processes/       # Operating procedures, runbooks
├── agents/          # Agent configs, skill references
├── gtm/              # Go-to-market assets, pipelines
├── recruitment/      # Hiring workflows, candidate tracking
├── spectra/          # Spectra Holdings project context
├── raw/              # Source data, transcripts, drafts
├── graphify-out/    # Knowledge graph output (do not edit)
└── hermes/           # Hermes operating directives
```

## Obsidian Vault

**Vault ID:** `1b9c01d85dcfdeb7`

The Obsidian vault at `~/wiki` is the live working copy. The GitHub repo is the sync layer — do not edit files directly on GitHub unless for emergency fixes.

| File | Purpose |
|------|---------|
| `hermes/directives.md` | Current operating rules for all LLMs |
| `clients/` | All client context and project history |
| `processes/` | Repeatable workflows and SOPs |
| `graphify-out/graph.json` | Semantic knowledge graph (query via graphify) |

## Accessing the Graph

```bash
cd ~/wiki && graphify query "<your question>"
```

Or inspect `graphify-out/GRAPH_REPORT.md` for community clusters and entity relationships.

## Contact

KlickSmartAI — Dennis Eng — Vancouver, BC
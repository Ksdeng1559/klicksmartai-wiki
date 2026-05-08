# KlickSmartAI Wiki — LLM Index

> **For ChatGPT, Claude, Gemini and all other contributing LLMs.**
> Read this before working. Write back when you're done.

---

## Quick Start

```
1. Read this index → understand the wiki
2. Check clients/, processes/, current projects
3. Do your work in a feature branch
4. Open a PR → Hermes reviews and merges
```

---

## What Is This Wiki

`~/wiki` (GitHub: `Ksdeng1559/klicksmartai-wiki`) is the **shared knowledge layer** for all KlickSmartAI agents. It is the single source of truth for:
- Client contexts and project history
- Operating procedures and processes
- Agent configurations and skill references
- GTM pipelines and recruitment workflows
- Decision logs and learned facts

**The wiki is ground truth. Do not rely solely on session context.**

---

## How to Access

### From Hermes (WSL2)
```bash
cd ~/wiki
graphify query "<your question>"
```

### From Claude / ChatGPT / Gemini
1. Clone the repo: `git clone git@github.com:Ksdeng1559/klicksmartai-wiki.git`
2. Work in `~/wiki` locally
3. Or read via GitHub: `https://github.com/Ksdeng1559/klicksmartai-wiki`

---

## Branching Workflow

```
master (protected) ← Feature branches only
       ↑
       └── PR (open for review)
```

**Rules:**
- Write to `feature/<your-name>/<description>` branch
- Never push directly to `master`
- Open a Pull Request for Hermes to review
- Include a summary of what changed and why
- Merge happens after Hermes approves

**Branch naming:**
```
feature/claude/refactor-gtm-pipeline
feature/chatgpt/draft-client-proposal
feature/gemini/research-spectra-holdings
```

---

## Sync Sequence

When you make changes:
```bash
cd ~/wiki
git add -A
git commit -m "brief description of what you did"
git push origin feature/<your-branch-name>
```

Then open a PR on GitHub.

**Full sync order:** `Wiki → Graphify → GitHub`

---

## Directory Guide

| Directory | What's In It |
|-----------|--------------|
| `clients/` | All client context — company, contact, project history, decisions |
| `processes/` | SOPs, runbooks, repeatable workflows |
| `agents/` | Agent configs, skill references, capability docs |
| `gtm/` | Go-to-market assets, pipelines, outreach templates |
| `recruitment/` | Hiring workflows, IDC pipeline, Hubert-X configs |
| `spectra/` | Spectra Holdings project — $300M MCF, affordable housing |
| `raw/` | Source data, transcripts, drafts |
| `hermes/` | Hermes operating directives — **read this first** |
| `graphify-out/` | Knowledge graph output — **do not edit manually** |

---

## Key Files to Read

| File | Why |
|------|-----|
| `hermes/directives.md` | Current operating rules for all LLMs |
| `hermes/memory-architecture.md` | How memory and knowledge upgrades work |
| `clients/` | Start here for any client work |
| `processes/` | Any operational task should reference this |

---

## Current Active Context

### KlickSmartAI Stack
- **Hermes** — curator, executor, daily maintainer (this agent)
- **Claude** — coding, deep research, architecture
- **ChatGPT** — drafting, brainstorming, prototyping
- **Gemini** — multi-modal, context window work

### Active Projects
- **Spectra Holdings** — $300M MCF for Whatcom County affordable housing
- **IDC Recruitment** — Hubert-X v2 pipeline (Phase 0 gated)
- **WWR v2.0** — CRM with BFS pathfinding, HOT≥85/WARM 70-84
- **GTM Pipeline** — Scouting → Harvesting → Enrichment → Connectivity → Auditing

### Wiki Stats
- **Nodes:** ~53,895
- **Edges:** ~177,110
- **Communities:** 500
- **Last updated:** 2026-05-08

---

## Upgrade Rules

When you learn something durable, write it back:
- Client decisions → `clients/<client-name>/`
- Process improvements → `processes/`
- New capabilities → `agents/`
- Project context → relevant project folder

**Test:** Would another LLM need this fact in 3 months? → Write it to the wiki.

---

## Questions?

If you're unsure about anything — branching strategy, client context, conflicting edits — ask Hermes via the PR review process or raise it in the PR description.

---

**Last reviewed:** 2026-05-08
**Maintained by:** Hermes (KlickSmartAI Chief of Staff AI)
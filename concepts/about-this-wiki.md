---
title: About This Wiki
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [meta, memory, research]
sources: []
---

# About This Wiki

## What This Is
A persistent, interlinked markdown knowledge base that survives across [[Hermes Agent]] sessions. Built on [[Karpathy's LLM Wiki]] pattern.

## Structure
- `raw/` — immutable source material (articles, papers, transcripts)
- `entities/` — people, companies, places
- `concepts/` — topics, how-tos, ideas
- `comparisons/` — side-by-side analyses
- `queries/` — filed answers to research questions
- `SCHEMA.md` — conventions and tag taxonomy
- `index.md` — content catalog
- `log.md` — chronological action log

## How to Use It
- The agent files research here automatically during conversations
- The agent queries it before creating new pages to avoid duplicates
- Browse it in [[Obsidian]] (Vault at `~/wiki`) or any text editor

## Conventions
- Every page has YAML frontmatter (title, created, updated, type, tags)
- Pages link to each other via `[[wikilinks]]`
- Every action is logged in `log.md`
- See [[SCHEMA.md]] for full conventions

## Related
- [[Obsidian]] — recommended viewer/editor for this vault
- [[Dennis E.]] — the user this wiki serves

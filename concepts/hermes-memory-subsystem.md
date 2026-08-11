---
title: Hermes Memory Subsystem
created: 2026-08-11
updated: 2026-08-11
type: concept
tags: [codebase, concept, memory, context]
sources: [raw/articles/2026-08-11-hermes-source-tour.md]
confidence: medium
---

# Hermes Memory Subsystem

How Hermes remembers facts across sessions.

## Source files
- `agent/memory_manager.py` — orchestrator.
- `agent/memory_provider.py` — provider abstraction (built-in / Honcho /
  Mem0 / etc.).

## Two stores
1. **`memory`** — the agent's own notes. Procedural and operational
   knowledge (terminal quirks, deployment facts, lessons learned).
   Persistence: file-backed JSON + SQLite.
2. **`user_profile`** — who the user is (name, role, preferences, style).
   Same persistence.

Both are injected into every future turn via the prompt builder. Memory
entries are tagged with provenance so trust scoring works
(`fact_feedback`).

## Memory feedback rule
When the agent retrieves a fact from `fact_store` and references it, the
agent MUST call `fact_feedback(action='helpful' | 'unhelpful')` in the same
turn. Without feedback, `trust_score` becomes ornamental and fact quality
degrades silently. This is enforced by the `Memory OS` prompt injection.

## Context compression
- `agent/context_compressor.py` handles near-token-limit compaction.
- Triggers automatically at `compression.threshold` (default 0.50,
  target_ratio 0.20).
- Manual: `/compress` slash command (CLI); session_search recalls past
  transcripts via FTS5.

## Fact feedback storage
Facts are stored via the `fact_store` (HoloGraph or alternative backend).
Each fact has `trust_score` updated by feedback; low-trust facts are
deprioritized but not auto-deleted.

## Memory operations
- `memory` tool: add / replace / remove operations.
- `session_search` tool: search past sessions by FTS5 query.
- Both are read by the agent at session start (injected into prompt).

## Honcho (deprecated)
Honcho integration was abandoned as an external memory provider. The
`heartbeat.py` cron job (which wrote metrics to Honcho) is disabled. Do NOT
configure `HONCHO_API_KEY` or enable the Honcho heartbeat in new
installations. Use Memory OS (Qdrant + Redis + ARQ Worker) instead.

## See also
- [[Hermes-Session-Lifecycle]]
- [[Hermes-Prompt-Builder]]
- [[Hermes-Cron-Architecture]]
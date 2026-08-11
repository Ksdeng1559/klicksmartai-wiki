---
title: Source Notes — Hermes Source Tour (2026-08-11)
created: 2026-08-11
updated: 2026-08-11
type: source
tags: [source, hermes-agent, codebase]
sources: []
confidence: high
---

# Source Notes — Hermes Source Tour (2026-08-11)

First-party observations from reading `~/.hermes/hermes-agent/` to ground
the Hermes internals wiki pages.

## Module map (relevant for wiki)
- `gateway/run.py` — ~16,800 lines. Gateway runner.
- `gateway/session.py` — ~1444 lines. Session data model + store.
- `gateway/platforms/` — per-platform adapters.
- `gateway/api_server.py` — HTTP API for Open WebUI integration.
- `cron/` — scheduler, jobs, executions, lifecycle_guard, monitor, notepad.
- `agent/memory_manager.py` + `agent/memory_provider.py` — memory subsystem.
- `agent/prompt_builder.py` — system prompt construction.
- `agent/context_compressor.py` — token-limit compaction.
- `agent/skill_bundles.py` + `agent/skill_commands.py` — skill loading.
- `tools/` — tool implementations (~80 files).
- `toolsets.py` — toolset definitions (composable, allow-list per platform).

## Documents
- `docs/session-lifecycle.md` — authoritative session contract.
- `docs/chronos-managed-cron-contract.md` — wire spec for Chronos
  provider (NAS-mediated cron for scale-to-zero).
- `docs/profile-routing.md`, `docs/relay-connector-contract.md`,
  `docs/micro-compaction.md`, `docs/billing-lifecycle.md`,
  `docs/streaming-tts.md`, `docs/kanban/`, `docs/observability/`,
  `docs/security/`, `docs/middleware/`, `docs/design/`.

## Configuration knobs (live `~/.hermes/config.yaml`)
- `agent.max_turns: 90` — hard cap per turn.
- `agent.gateway_timeout: 1800` s (warning at 900s).
- `agent.restart_drain_timeout: 60` s.
- `agent.task_completion_guidance: true`,
  `agent.parallel_tool_call_guidance: true`.
- `agent.image_input_mode: auto`,
  `agent.coding_context: auto`,
  `agent.verify_on_stop: false`.
- `agent.reasoning_effort: medium`,
  `agent.verbose: false`.
- `terminal.timeout: 600` s default; `terminal.docker_image`:
  nikolaik/python-nodejs:python3.11-nodejs20.
- `max_live_sessions: 16`.

## Memory OS stack (current)
- Qdrant + Redis + ARQ Worker. Honcho is deprecated; do not configure
  `HONCHO_API_KEY`.

## Key implementation facts
- Tools are auto-discovered: any `tools/*.py` with a top-level
  `registry.register()` call is imported automatically — no manual list
  needed.
- All tool handlers return JSON strings.
- Use `get_hermes_home()` for paths, never hardcode `~/.hermes`.
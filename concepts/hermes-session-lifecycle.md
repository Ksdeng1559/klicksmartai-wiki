---
title: Hermes Session Lifecycle
created: 2026-08-11
updated: 2026-08-11
type: concept
tags: [codebase, concept, gateway, session]
sources: [raw/articles/2026-08-11-hermes-source-tour.md]
confidence: high
---

# Hermes Session Lifecycle

How Hermes tracks continuous conversations across messaging platforms.

## Source of truth
- `~/.hermes/hermes-agent/gateway/session.py` (~1444 lines) — data model and
  store.
- `~/.hermes/hermes-agent/gateway/run.py` (~16,800 lines) — runner wiring.
- `~/.hermes/hermes-agent/docs/session-lifecycle.md` — authoritative contract.

## Data model
- **`SessionSource`** — frozen record of message origin (platform, chat_id,
  user_id, thread_id, etc.). Attached to every incoming `MessageEvent`.
- **`SessionEntry`** — per-session metadata: `session_key`, `session_id`,
  `created_at`, `updated_at`, `origin`, token counters, cost tracking.
- **`SessionContext`** — full conversation context object (active messages,
  system prompt, etc.).

## Session keys and IDs
- **`session_key`** — deterministic, identifies a "conversation lane". Built
  from platform + chat_id + chat_type + thread_id (etc.) via
  `build_session_key()`.
- **`session_id`** — unique per conversation *incarnation*. Format:
  `YYYYMMDD_HHMMSS_<8hex>`. New ID when the lane is reset/expires.

## Storage
- Persisted to `{sessions_dir}/sessions.json` (atomic writes).
- Query layer uses SQLite (`hermes_state.py`) with FTS5 for full-text search.
- 16 max concurrent sessions (`max_live_sessions` in config).

## Session expiry watching
- The gateway runner maintains a watcher that closes idle lanes per-platform
  expiry policy. Resumption produces a new `session_id` while keeping the
  same `session_key`.

## Token accounting
Tracked per-session: input_tokens, output_tokens, cache_read_tokens,
cache_write_tokens, total_tokens, estimated_cost_usd, cost_status, plus
`last_prompt_tokens` for accurate compression pre-check.

## See also
- [[Gateway-Architecture]]
- [[Cron-Architecture]]
- [[Hermes-Environment-Map]]
- [[Service-Port-Registry]]
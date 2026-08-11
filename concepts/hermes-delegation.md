---
title: Hermes Delegation
created: 2026-08-11
updated: 2026-08-11
type: concept
tags: [codebase, concept, delegation, subagent, tools]
sources: [raw/articles/2026-08-11-hermes-source-tour.md]
confidence: medium
---

# Hermes Delegation

How the agent spawns child agents (subagents) for parallel or isolated work.

## Tool
- `delegate_task(goal, context)` — single task.
- `delegate_task(tasks=[{...}, {...}])` — parallel batch (capped by
  `delegation.max_concurrent_children`, default 3).
- `background=True` (deprecated) — top-level single/batch always runs in
  background now.

## Roles
- **leaf** (default) — focused worker, cannot delegate further.
- **orchestrator** — can spawn its own workers. Bounded by
  `delegation.max_spawn_depth`. Currently OFF for this user (max depth 1);
  setting `role='orchestrator'` silently forces 'leaf'.

## Lifecycle
- Children run in isolated contexts: their own conversation, terminal
  session, and toolset.
- They know nothing about the parent conversation — pass full context.
- Child summaries are SELF-REPORTS, not verified facts. For external side
  effects (uploads, remote writes, publishes), require a verifiable
  handle and verify yourself.
- Children inherit the parent's model + fallback chain unless pinned
  globally via `delegation.provider` / `delegation.model` in config.

## When to use
- Reasoning-heavy subtasks.
- Work that would flood parent context with intermediate data.
- Independent parallel workstreams.

## When NOT to use
- Mechanical multi-step work with no reasoning → `execute_code`.
- A single tool call → call the tool directly.
- Tasks needing user interaction → subagents cannot ask questions.
- Durable work that must survive this session → `cronjob` or
  `terminal(background=True, notify_on_complete=True)`.

## Configuration
- `delegation.model`, `delegation.provider`, `delegation.base_url`,
  `delegation.api_key` — what the child uses.
- `delegation.max_iterations` — default 50.
- `delegation.reasoning_effort` — reasoning effort for delegated tasks.
- `delegation.max_concurrent_children` — parallelism cap.

## Use vs spawning a full `hermes` process
| | `delegate_task` | Spawning `hermes` |
|-|-----------------|------------------|
| Isolation | Separate conversation, shared process | Fully independent process |
| Duration | Minutes (bounded by parent loop) | Hours/days |
| Tool access | Subset of parent's tools | Full tool access |
| Interactive | No | Yes (PTY mode) |
| Use case | Quick parallel subtasks | Long autonomous missions |

## See also
- [[Hermes-Cron-Architecture]]
- [[Hermes-Memory-Subsystem]]
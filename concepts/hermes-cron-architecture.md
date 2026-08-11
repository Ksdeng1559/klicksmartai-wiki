---
title: Hermes Cron Architecture
created: 2026-08-11
updated: 2026-08-11
type: concept
tags: [codebase, concept, cron, scheduler, gateway]
sources: [raw/articles/2026-08-11-hermes-source-tour.md]
confidence: high
---

# Hermes Cron Architecture

How scheduled jobs fire and run.

## Source files (`~/.hermes/hermes-agent/cron/`)
- `scheduler.py` — main scheduler loop (60s ticker by default; can run
  without tick via Chronos).
- `scheduler_provider.py` — provider abstraction (in-process vs Chronos vs
  future).
- `jobs.py` — job CRUD (create/update/pause/resume/remove/list).
- `executions.py` — per-run record (`cron/executions.db` SQLite).
- `lifecycle_guard.py` — drain pending jobs before shutdown.
- `monitor.py` — health/scheduling metrics.
- `notepad.py` — shared notes between job runs.
- `blueprint_catalog.py`, `suggestion_catalog.py` — discoverable job
  templates and suggestions.

## Two scheduler modes
1. **In-process** — `Scheduler()` runs in the gateway; 60-second ticker,
  cheap. Used for self-hosted installs where the gateway never sleeps.
2. **Chronos (managed)** — agent can scale to zero; NAS (Nous Account
  Service) arms a one-shot per job at fire_at and calls back over an
  authenticated webhook at fire time. Spec:
  `docs/chronos-managed-cron-contract.md`. Used for hosted/cloud installs.

## Job data
- Stored in `~/.hermes/cron/jobs.json` (atomic writes).
- Execution history in `cron/executions.db` SQLite.
- 3-minute hard interrupt per run (`HERMES_CRON_RUN_TIMEOUT`).
- Duplicate-tick prevention: `.tick.lock` file prevents two gateway
  processes from ticking at once.

## CLI / tool surface
- `hermes cron list [--all]` / `create` / `edit` / `pause` / `resume` /
  `remove` / `run` / `status`.
- `cronjob` tool (sessions) — same actions during a session.
- `/cron` slash command (gateway).

## Delivery semantics
- Each job specifies a `deliver` target (`origin`, `local`, `all`, or
  `platform:chat_id:thread_id`).
- `local` = no delivery, save only (for fire-and-forget cron jobs).
- `origin` (default) = same chat/topic the job was created from.
- Multi-target via comma-separated list.

## Persistence caveats
- **CLI scheduled jobs are LOCAL-ONLY** — output saves to disk but does NOT
  stream back into the CLI session. For notifications, set
  `deliver='telegram'` or similar.

## See also
- [[Hermes-Session-Lifecycle]]
- [[Hermes-Gateway-Architecture]]
- [[Hermes-Memory-Subsystem]]
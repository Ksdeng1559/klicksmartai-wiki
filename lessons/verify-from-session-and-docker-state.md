---
type: LESSON
created: 2026-08-19
updated: 2026-08-19
confidence: 0.9
sources: [session 20260819_141227, user correction]
related: [[hermes-memory-architecture]]
tags: [hermes, debugging, memory, verification]
status: active
---

# Verify From Session Records + Docker State, Not Config Alone

**Lesson (2026-08-19, user correction — "it's already wired — check your session records"):**

When asked whether a system/service is wired or working, do NOT conclude from `~/.hermes/config.yaml` alone. A tool can be fully wired and previously tested yet absent from current config, or its process may have died while the backend stays up.

## Correct verification order
1. **Session records** — `session_search` for the feature/topic to see if it was already wired + tested historically (e.g. Honcho was fully wired and 31 tools tested on 2026-08-17, even though config showed `provider: ''` and no process).
2. **Docker/backend state** — `docker ps` for live services (honcho-api, honcho-database, honcho-redis, honcho-deriver all healthy while the bridge was down).
3. **Config** — last resort, and treat absence as inconclusive, not proof.

## Why it matters
Config showed no honcho entry + no process → I wrongly declared it "unwired" and had to be corrected. The bridge had actually been running end-to-end (31 tools, semantic search) and was only briefly down after the Aug 18 update. The truth was recoverable from session history + docker state.

## Rule
Before declaring anything "unwired/not-configured/broken," check session history and live process/backend state first. A missing config entry is not proof of absence — it may be a transient failure or a separate layer that reconciled independently.

See [[hermes-memory-architecture]].

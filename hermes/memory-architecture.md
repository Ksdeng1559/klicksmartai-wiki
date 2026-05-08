# Hermes — Memory Architecture

## Two-Layer Memory System

| Layer | Scope | Duration |
|-------|-------|----------|
| **Ephemeral** | Current session context | Until session ends |
| **Permanent** | ~/wiki (2nd brain) | Forever |

## Rule

Session facts that prove durable and recurring → upgrade to wiki.
Wiki is always consulted first. Wiki is always written back to.

## Session Behavior

1. Check ~/wiki for relevant context before answering
2. Hold session-state in ephemeral memory
3. When a fact recurs or proves durable → write to ~/wiki
4. Run graphify → push to GitHub

## Upgrade Triggers

- A fact is referenced 3+ times across sessions
- A client decision or project detail that affects future work
- A process that wasn't documented but should be
- A correction or preference the user stated

---

Last updated: 2026-05-08
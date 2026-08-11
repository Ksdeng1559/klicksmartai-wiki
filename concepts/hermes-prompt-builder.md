---
title: Hermes Prompt Builder & Environment Hints
created: 2026-08-11
updated: 2026-08-11
type: concept
tags: [codebase, concept, prompt, environment]
sources: [raw/articles/2026-08-11-hermes-source-tour.md]
confidence: high
---

# Hermes Prompt Builder & Environment Hints

How the system prompt is constructed each turn — including the environment
hints that drive "what kind of agent am I" decisions.

## Source
- `agent/prompt_builder.py` — main builder.
- `build_environment_hints()` — emits host/OS/cwd/terminal-backend info.

## What gets built every turn
1. Core Hermes identity and rules.
2. **Environment hints** — host info (OS, $HOME, cwd), Windows-specific
   notes, terminal backend description.
3. **Ground truth rules** — terminal output is ground truth for current
   system state; injected memory wins for documented knowledge.
4. **Memory injections** — `memory`, `user_profile`, and other context.
5. **Skills index** — currently enabled skills (truncated to relevant ones).
6. **MCP server tools** — schemas for active MCP tools.
7. Conversation history (compressed if near token limit).

## Environment hints — backend-dependent
- **Local terminal backend** → emits host info + Windows-specific notes
  (hostname ≠ username on Windows; terminal uses bash not PowerShell on WSL).
- **Remote terminal backend** (docker, singularity, modal, daytona, ssh,
  vercel_sandbox, managed_modal) → **suppresses** host info entirely and
  describes only the backend.

Key fact for prompt authoring: when `TERMINAL_ENV != "local"`, every file
tool (`read_file`, `write_file`, `patch`, `search_files`) runs inside the
backend container, not on the host. The system prompt must NEVER describe
the host in that case — the agent can't touch it.

## Live probe
The builder runs a live `uname` / `whoami` / `pwd` probe inside the
backend via `tools.environments.get_environment(...).execute(...)`, cached
per process in `_BACKEND_PROBE_CACHE`, with a static fallback if the probe
times out.

## Why never break prompt caching
- Don't change context, tools, or system prompt mid-conversation.
- Tool enable/disable takes effect only on `/reset` (new session) to
  preserve prompt caching.

## Test pattern
When testing prompt-builder behavior:
- `monkeypatch.setattr(sys, "platform", "linux")` is NOT enough — the
  code under test also calls `platform.system()` / `platform.release()`.
  Patch all three: sys.platform + platform.system + platform.release.

## See also
- [[Hermes-Memory-Subsystem]]
- [[Hermes-Delegation]]
- [[Hermes-Environment-Map]]
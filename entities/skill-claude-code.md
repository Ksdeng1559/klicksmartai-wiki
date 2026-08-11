---
title: claude-code (skill)
created: 2026-08-11
updated: 2026-08-11
type: entity
tags: [entity, skill, claude-code, coding-agent, orchestration]
sources: []
confidence: high
---

# claude-code (skill)

**Delegate coding tasks to Claude Code CLI** (Anthropic's autonomous coding
agent). Skill teaches Hermes how to drive Claude Code in print mode or
interactive PTY via tmux.

## Source
`~/.hermes/skills/autonomous-ai-agents/claude-code/`

## Two orchestration modes

### Mode 1: Print mode (`-p`) — preferred for one-shot tasks
```bash
terminal(command="claude -p 'Add error handling to all API calls in src/' \
  --allowedTools 'Read,Edit' --max-turns 10",
  workdir="/path/to/project", timeout=120)
```
No PTY needed. Skips all interactive dialogs.

### Mode 2: Interactive PTY via tmux — multi-turn
Use `tmux new-session` + `tmux send-keys` to drive the TUI. Required for
multi-turn iteration, slash commands, `/review` etc.

## PTY dialog handling (CRITICAL)
First-time launch in a directory shows:
1. **Workspace trust** — default = "Yes, I trust this folder". Press `Enter`.
2. **Permissions bypass warning** (with `--dangerously-skip-permissions`) —
   default = "No, exit". Must send `Down` then `Enter`.

Robust pattern:
```bash
sleep 4 && tmux send-keys -t <session> Enter        # trust
sleep 3 && tmux send-keys -t <session> Down && sleep 0.3 && tmux send-keys -t <session> Enter  # perms
```

## Print mode flags worth knowing
- `--output-format json` — structured result with `session_id`, `num_turns`,
  `total_cost_usd`, `subtype` (success/error_max_turns/error_budget).
- `--stream-json` — real-time event streaming.
- `--json-schema '{...}'` — force structured output against a schema.
- `--max-turns N` — caps agentic loops (print mode only).
- `--max-budget-usd N` — caps spend.
- `--fallback-model haiku` — graceful overload fallback.
- `--resume <id>` / `--continue` / `--fork-session` — session management.
- `--allowedTools` / `--disallowedTools` — tool whitelisting.
- `--bare` — fastest startup (skips plugins/CLAUDE.md/OAuth).
- `-w <worktree>` — git worktree isolation.

## Cost / performance tips
- Always set `--max-turns` to prevent runaway.
- Use `--effort low` for simple tasks; `--effort high` or `--effort max` for
  complex reasoning.
- `--bare` for CI/scripting.
- Use `/compact` in interactive sessions at ~70% context.

## Pitfalls
- Interactive mode REQUIRES tmux (pty=true works but loses orchestration).
- `--max-budget-usd` minimum is ~$0.05 (system prompt cache creation).
- `--max-turns` is print-mode only.
- `--bare` skips OAuth — needs `ANTHROPIC_API_KEY`.
- Context quality degrades above 70% — monitor with `/context`.

## See also
- [[Hermes-Delegation]]
- [[Hermes-Environment-Map]]
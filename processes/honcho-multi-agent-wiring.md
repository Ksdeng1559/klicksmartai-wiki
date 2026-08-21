---
title: Honcho Multi-Agent Wiring — Shared Memory Across Hermes, Claude Code, ChatGPT, Cursor, etc.
created: 2026-08-21
updated: 2026-08-21
type: runbook / architecture
tags: [honcho, mcp, multi-agent, shared-memory, claude-code, chatgpt, cursor, codex, opencode, runbook]
sources: [https://github.com/Ksdeng1559/klicksmartai-wiki/blob/master/processes/honcho-multi-agent-wiring.md]
owner: Hermes (CoS)
status: permanent
audience: Dennis + any agent author wiring into the Honcho brain
---

# Honcho Multi-Agent Wiring

How to attach external agents (Claude Code, ChatGPT, Codex, Cursor, OpenCode, etc.) to the same Honcho memory that Hermes already uses, so all agents share conversation context across the workspace `klicksmartai-wiki` peer `dennis`.

## TL;DR

- **One Honcho instance** runs at `http://localhost:44547` (systemd unit, started on boot).
- **Hermes already attaches** to it via MCP (`mcp__honcho__*` tools).
- **Any other agent** can attach the same way — they just need an MCP client + the same workspace/peer IDs.
- **Workspace = `klicksmartai-wiki`**, **peers = `wiki`, `hermes-default`, `dennis`**. Use these names verbatim.

## The architecture

```
                  ┌─────────────────────────────────────────────────┐
                  │           Honcho @ localhost:44547              │
                  │      workspace: klicksmartai-wiki               │
                  │      peers: wiki, hermes-default, dennis        │
                  │      31 tools (sessions, peers, conclusions,    │
                  │      representations, semantic search)          │
                  └──────────────┬──────────────────────────────────┘
                                 │ MCP (HTTP)
        ┌────────────────────────┼─────────────────────────┐
        │                        │                         │
   ┌────▼─────┐         ┌────────▼────────┐        ┌───────▼──────┐
   │  Hermes  │         │  Hermes Desktop │        │  External    │
   │   CLI    │         │  GUI (Electron) │        │  agents      │
   │  (this)  │         │                 │        │  (Claude     │
   └──────────┘         └─────────────────┘        │   Code,      │
                                                   │   ChatGPT,   │
                                                   │   Codex,     │
                                                   │   Cursor)    │
                                                   └──────────────┘
```

## Auth

- Endpoint: `http://localhost:44547`
- Auth header: `Authorization: Bearer <HONCHO_API_KEY>`
- The key lives in `~/.hermes/.env` as `HONCHO_API_KEY`. **Never** commit or paste it externally.
- For any non-Hermes agent, copy the key into that agent's secret store (Claude Code's `~/.claude/mcp_settings.json`, Cursor's secrets, etc.). The key value never appears in this runbook — it always loads from the env file.

## Universal MCP config block

This block works for **any MCP-compatible agent**. Drop it into the agent's MCP config and restart the agent.

```json
{
  "mcpServers": {
    "honcho": {
      "url": "http://localhost:44547",
      "transport": "http",
      "headers": {
        "Authorization": "Bearer ${HONCHO_API_KEY}"
      }
    }
  }
}
```

If the agent doesn't support env-var expansion in headers, hardcode the literal token (only if you trust the agent's secret storage).

## Per-agent wiring

### Claude Code

Claude Code reads `~/.claude/mcp_settings.json`. Add the Honcho block above. Restart the session. The `mcp__honcho__*` tools appear in the session (31 tools: `add_messages_to_session`, `chat`, `create_conclusion`, `get_peer_context`, `query_conclusions`, `search`, etc.).

First-call smoke test:
```
mcp__honcho__list_workspaces → should return 17+ workspaces including klicksmartai-wiki
mcp__honcho__list_peers(workspace_id="klicksmartai-wiki") → should return [wiki, hermes-default, dennis]
```

### Cursor

Cursor reads MCP servers from `~/.cursor/mcp.json`. Same block. Restart Cursor. Tools appear under the Honcho namespace in the agent picker.

### Codex CLI

Codex CLI uses `~/.codex/mcp_servers.json` (or the equivalent TOML). Same block. The agent can then call `mcp__honcho__*` tools.

### OpenCode

OpenCode reads `~/.opencode/config.json` under the `mcp` key. Same block.

### ChatGPT (no native MCP — bridge required)

ChatGPT does not currently speak MCP. Two options:

1. **Manual bridge (simple, low ceremony):**
   - In any Hermes session, ask "give me the last 7 days of fabric memory as a markdown block."
   - Paste that block at the start of your ChatGPT conversation.
   - At the end, ask ChatGPT to summarize the key takeaways; paste the summary back into a Hermes session so Honcho gets the conclusions.

2. **Tool-bridge script (automated):**
   - Build a thin Python service that wraps Honcho HTTP endpoints as OpenAI function tools.
   - ChatGPT's "custom GPT actions" or GPT-5 API can call those functions.
   - Out of scope for this runbook; revisit when ChatGPT supports MCP natively or when ChatGPT Actions become the standard integration.

### Anything else

If the agent has an MCP client, the same JSON block works. If it doesn't, the bridge pattern (manual or scripted) applies.

## Workspace + peer conventions

- **Workspace:** always `klicksmartai-wiki`. This is the canonical KlickSmartAI brain.
- **Peers:**
  - `dennis` — Dennis's identity (the user). All user-side messages belong here.
  - `hermes-default` — Hermes (any surface: CLI, Desktop, scheduled cron). Assistant-side messages belong here.
  - `wiki` — the wiki corpus itself. Ingest scripts write here as the "knowledge peer."
- **Sessions:** agents create their own session IDs (random hex). To cross-reference, share the session ID explicitly between agents via the conversation.

## Cross-surface recall — the test

After wiring a new agent, the simplest end-to-end test:

1. In Hermes CLI: "Note that I'm allergic to cashews."
2. Switch to the new agent.
3. Ask: "Do I have any food allergies?" → should recall cashews.

Honcho stores the message in workspace `klicksmartai-wiki`, peer `dennis`. Any agent querying `get_peer_card` or `query_conclusions` for that peer/workspace sees the same fact.

## Conclusion capture (semantic memory)

Each agent should:

1. **On session start** → call `mcp__honcho__get_peer_context(workspace_id="klicksmartai-wiki", peer_id="dennis")` to load relevant prior context into the system prompt.
2. **During the session** → call `mcp__honcho__add_messages_to_session` for each turn to feed Honcho the raw transcript.
3. **On session end** → call `mcp__honcho__create_conclusions` to write durable insights (preferences, decisions, durable facts) so they survive context compaction.

Honcho's `deriver` automatically extracts conclusions from raw messages; explicit `create_conclusions` calls just bias the model toward the most important ones.

## What lives where (decision boundaries)

| Layer | Where | Owned by |
|---|---|---|
| Honcho semantic memory | localhost:44547 | system (systemd) |
| Workspace identity | `klicksmartai-wiki` | Hermes |
| Peer identity | `dennis`, `hermes-default`, `wiki` | Hermes |
| Session raw transcripts | Honcho sessions (auto-rotating) | each agent |
| Durable conclusions | Honcho conclusions | deriver + explicit calls |
| Long-form docs | `~/wiki` (git) | Dennis + Hermes |
| Vector embeddings | Qdrant (via ARQ worker, hourly cron) | Hermes |
| Skill library | `~/.hermes/skills/` + `~/wiki/skills/` | Dennis + Hermes |

Honcho is the **conversation brain**. The wiki is the **knowledge brain**. Don't put wiki content into Honcho sessions; don't put conversation transcripts into wiki files. Each layer has its job.

## Pitfalls

- **Don't create new workspaces per agent.** Always use `klicksmartai-wiki`. Multiple workspaces = fragmented memory.
- **Don't create new peers per agent.** Use `dennis` for the user, `hermes-default` for the assistant.
- **Honcho key is read-only at the agent config level** — don't try to write Honcho content from a raw curl without going through MCP. The deriver expects a specific message schema.
- **Honcho works best when both sides of a conversation write to it.** If you only call `add_messages_to_session` from one peer, conclusions get lopsided. Always pair user-side and assistant-side messages in the same session.

## See also

- `wiki-sync-pipeline.md` — how `~/wiki` syncs to GitHub + Obsidian vault (sister runbook).
- `~/.hermes/.env` — contains `HONCHO_API_KEY`.
- `~/.hermes/config.yaml` — Hermes's Honcho block (mcp_servers.honcho).
- Honcho docs: https://docs.honcho.ai (when accessible from this network).

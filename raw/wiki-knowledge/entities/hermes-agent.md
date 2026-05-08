---
title: Hermes Agent
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [technology, artificial-intelligence, open-source, autonomous-agent]
sources: [raw/articles/hermes-agent-research.md]
---

# Hermes Agent

## Overview

Hermes Agent is an open-source autonomous AI agent built by [[Nous Research]]. It positions itself as a "self-improving agent that grows with you" — learning from each interaction to become more useful over time.

## Key Facts

| Fact | Detail |
|------|--------|
| Developer | [[Nous Research]] |
| GitHub Stars | 64,200+ (as of April 2026) |
| Launch | February 2026 (quiet), gaining traction April 2026 |
| Status | Active, open-source |

## Features

- **Multi-platform support**: Telegram, Discord, Slack, WhatsApp, Signal, Email, CLI
- **Persistent memory**: Learns projects and remembers solutions across sessions
- **Auto-generated skills**: Creates and improves skills during use
- **Model agnostic**: Use any model — MiniMax, GLM, Kimi/Moonshot, Hugging Face, OpenAI, or your own endpoint
- **Full TUI**: Multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, streaming
- **Local deployment**: Runs on your own server via [[Ollama]] integration

## Self-Improving Memory Loop

Hermes Agent uses a closed learning loop:
- Agent-curated memory with periodic nudges
- Autonomous skill creation
- Skill self-improvement during use
- FTS5 cross-session recall with LLM summarization
- Honcho dialectic user modeling

## Competitive Position

Positioned as a competitor to [[OpenClaw]]. Key differentiator: it doesn't just execute tasks — it improves itself every time it runs.

Notable partnerships: [[MiniMax]] (AI company partnership)

## Sources

- Official site: https://hermes-agent.nousResearch.com/
- GitHub: https://github.com/nousresearch/hermes-agent
- Documentation: https://hermes-agent.nousResearch.com/docs/
- Ollama integration: https://docs.ollama.com/integrations/hermes

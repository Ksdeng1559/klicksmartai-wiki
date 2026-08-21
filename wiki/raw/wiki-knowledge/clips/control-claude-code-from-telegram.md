# Control Claude Code from Your Phone Using Telegram

**Source:** The Unwind AI / Shubham Saboo & Gargi Gupta
**URL:** https://www.theunwindai.com/p/control-claude-code-from-your-phone-using-telegram
**Date:** March 21, 2026

---

## Claude Code Channels

Claude Code now supports messaging your running session from **Telegram or Discord** via a new **Claude Code Channels** feature. Built on **MCP (Model Context Protocol)**.

### Setup

```
1. Create bot via BotFather (Telegram) or Discord Developer Portal
2. Install plugin: /plugin install
3. Configure your token
4. Launch: claude --channels
5. Pairing: single DM to complete
```

Requirements: Claude Code v2.1.80+

### Features

| Feature | Description |
|---------|-------------|
| Two-Way MCP Bridge | Phone → MCP server → active session → Claude → reply back |
| Interactive Responses | Claude can reply, react with emoji, edit its own messages |
| Access Control | Sender allowlist with pairing-code verification |
| Extensible | Open plugin architecture for custom channel integrations |

---

## Karpathy's Autoresearch for Claude Skills

Ole Lehmann built an **autoresearch-style skill** that tests, scores, and refines any Claude skill on autopilot.

**Results:**
- Landing page copy skill: 56% → 92% pass rate
- Achieved in: 4 rounds
- Zero manual intervention required

### How It Works

| Component | Description |
|-----------|-------------|
| Checklist-as-metric | Define 3-6 yes/no questions for consistent scoring |
| One change at a time | Isolates single variable per round, tests across multiple runs |
| Full audit trail | Every run produces a changelog explaining what was tried and outcome |

**Applications:** Page load optimization (1100ms → 67ms), cold outreach copy, newsletter intros.

---

## Claude Code Scheduled Tasks

Now supports scheduled, recurring cloud-based tasks. No need to keep local machine awake.

**Use cases:**
- Sweeping open PRs
- Building features from approved issues
- Analyzing CI failures overnight
- Syncing docs after merges

---

## Relevance to Dennis

Dennis already has a Telegram bot (@klicksmartsai_bot) running. This article is highly relevant — the pattern is already in his stack.

Key parallel: Dennis's cron jobs deliver to Telegram (ID: 197886049). Claude Code Channels would extend this to full bidirectional Claude Code control from Telegram.

**Action:** Consider pairing Claude Code Channels with the existing Telegram bot setup for full remote control.

---
title: Hermes Agent Setup Guide
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [technology, artificial-intelligence, open-source, autonomous-agent, how-to, guide]
sources: [raw/articles/hermes-agent-complete-setup-guide.md]
---

# Hermes Agent Setup Guide

## Overview

A comprehensive walkthrough for self-hosting Hermes Agent on a VPS, published by Alex P. on Medium (March 29, 2026). The guide positions Hermes as a cost-effective alternative to OpenClaw's Mac Mini setup.

## Cost Comparison

| Setup | Monthly Cost |
|-------|-------------|
| OpenClaw (Mac Mini M4 + Opus 4.6) | ~$150+ API + hardware sitting on desk |
| Hermes on Hostinger VPS (2 vCPU, 8GB RAM) | Under $20 total |

## Hardware Recommendation

**Hostinger KVM 2 plan** — 2 vCPU cores, 8GB RAM, 100GB NVMe SSD, Ubuntu 24.04 LTS

The VPS handles: agent process, terminal state, memory storage, gateway process, and Docker isolation simultaneously.

## Install Commands

```bash
# One-command install
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# Verify
hermes version
hermes doctor
hermes setup
```

## Model Selection

- **Default:** OpenRouter (200+ models, switch anytime with `hermes model`)
- **Cost-first:** Minimax M2.7 on OpenRouter — ~$0.30-0.40 per million tokens
- **Reasoning tasks:** Nous Portal for Hermes 3 and newer Nous models

## Telegram Setup (5 Minutes)

1. Telegram → @BotFather → /newbot → copy token
2. `hermes gateway setup` → select Telegram → paste token
3. `hermes gateway` → message your bot

## Skill Documents

After completing a complex task, Hermes auto-generates a skill document at `~/.hermes/skills/`. These:
- Follow the agentskills.io open standard
- Are searchable, reusable, and shareable
- Self-improve with repeated similar tasks
- Persist across `hermes update` (stored separately from app code)

## 24/7 Service

```bash
hermes gateway install  # systemd — auto-start, auto-restart
systemctl status hermes-gateway
hermes update  # run weekly during active development
```

## Security Checklist

Before going 24/7:
1. Switch to Docker backend: `hermes config set terminal.backend docker`
2. Configure allowlist in `~/.hermes/config.yaml`
3. Disable Allow Groups in BotFather — private/DM only

## Related

- [[hermes-agent]] — main entity page for Hermes Agent
- [[llm-wiki]] — Karpathy's LLM Wiki pattern used by Hermes
- [[raw/articles/hermes-agent-complete-setup-guide.md]] — full source article

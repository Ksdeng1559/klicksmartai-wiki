---
title: Hermes Agent Complete Setup Guide (Alex P.)
created: 2026-04-15
type: raw
source: https://medium.com/@alexp_/hermes-agent-the-complete-setup-guide-telegram-discord-vps-no-mac-mini-required
---

# Hermes Agent Complete Setup Guide

**Author:** Alex P.
**Published:** March 29, 2026
**Source:** Medium
**URL:** https://medium.com/@alexp_/hermes-agent-the-complete-setup-guide-telegram-discord-vps-no-mac-mini-required

## Summary

Full walkthrough for setting up Hermes Agent on a cheap VPS (Hostinger KVM 2 plan recommended — 2 vCPU, 8GB RAM, 100GB NVMe SSD, Ubuntu 24.04 LTS). Covers: one-command install, model selection via OpenRouter, Telegram setup via BotFather, skill document system, 24/7 systemd service, and security hardening (Docker backend, allowlists).

## Key Points

### Why Hermes over OpenClaw
- OpenClaw: Mac Mini + Opus 4.6 at $15/M tokens + $80-120/month API = expensive
- Hermes: VPS under $20/month total, model included
- Open source, MIT licensed, all data stays local
- Trained by Nous Research (Hermes, Nomos, Psyche model families)
- One `curl` install, no gateway troubleshooting needed

### Recommended Hardware
- **Hostinger KVM 2 plan:** 2 vCPU cores, 8GB RAM, 100GB NVMe SSD, Ubuntu 24.04 LTS
- $20/month total vs $599 Mac Mini + $150/month API
- VPS handles agent process, terminal state, memory storage (not inference)

### Install (one command)
```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```
Then:
```bash
hermes version
hermes doctor
hermes setup
```

### Model Recommendation
- **Default:** OpenRouter (200+ models, no lock-in)
- **Cost-first:** Minimax M2.7 on OpenRouter ~$0.30-0.40/M tokens
- **Stronger reasoning:** Nous Portal for Hermes 3 and newer Nous models
- Switch anytime with `hermes model` — no config editing needed

### Telegram Setup (5 minutes)
1. Open Telegram → @BotFather → /newbot → copy token
2. Run `hermes gateway setup` → select Telegram → paste token
3. Run `hermes gateway` → send message to bot

### Skill Documents (auto-generated)
- After complex task: check `ls ~/.hermes/skills/`
- Agent synthesizes approach into permanent markdown file
- Follows agentskills.io open standard
- Self-improves during use — more repetitions = more refined
- Skills persist across `hermes update` — separate from app code

### 24/7 Service Setup
```bash
hermes gateway install  # systemd unit, starts on boot, restarts on failure
systemctl status hermes-gateway
hermes update  # weekly recommended — 50+ security/reliability fixes in latest release
```

### Security (mandatory before going 24/7)
1. **Docker backend:** `hermes config set terminal.backend docker` — isolates shell access
2. **Allowlist:** Edit `~/.hermes/config.yaml` under gateway section
3. **Lock down BotFather:** Disable Allow Groups, keep private/DM only

### FAQ
- **Local models:** Yes — point base_url to Ollama, LM Studio, or any OpenAI-compatible server
- **Skills persist on update:** Yes — stored in `~/.hermes/skills/`, separate from application code
- **Memory persists:** Yes — `~/.hermes/memories/` and `~/.hermes/sessions/` survive updates

## Related Articles Referenced
- Hermes vs OpenClaw comparison pieces
- Claude Code on VPS setup guide (same author)
- Karpathy's LLM Wiki for self-maintaining knowledge base
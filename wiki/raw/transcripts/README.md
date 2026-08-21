# Hermes Agent

An autonomous AI agent by [Nous Research](https://nousresearch.com/) that lives on your server, remembers what it learns, and gets more capable the longer it runs.

## Table of Contents

- [Overview](#overview)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [LLM Providers](#llm-providers)
- [Voice (STT/TTS)](#voice-stttts)
- [Platforms](#platforms)
- [Skills](#skills)
- [Usage](#usage)
- [Architecture](#architecture)
- [Troubleshooting](#troubleshooting)
- [Maintenance](#maintenance)

---

## Overview

Hermes Agent is a persistent, learning AI assistant with multi-platform support. Unlike typical coding copilots, it operates as a long-running system with memory, scheduled tasks, and autonomous capabilities.

### Key Features

- **Multi-Platform Messaging** — Telegram, Discord, Slack, WhatsApp, Signal, Email, CLI, Webhook
- **Persistent Memory** — Learns preferences, project patterns, and solutions across sessions
- **65 Bundled Skills** — From code review to research to media generation (25 categories)
- **Scheduled Tasks** — Natural language cron jobs for reports, backups, briefings
- **Sub-Agent Delegation** — Spawns isolated agents for parallel work
- **Voice Support** — STT (Groq Whisper) and TTS (Microsoft Edge)
- **Webhook API** — HTTP endpoint for external integrations
- **Browser Automation** — Playwright-based web browsing and scraping
- **40+ Built-in Tools** — Terminal, file management, vision, code execution, web search

---

## System Requirements

### Host Machine (Windows)

| Component | Spec |
|-----------|------|
| OS | Windows 10/11 with WSL2 |
| CPU | AMD Ryzen 5 3600 (6-core / 12-thread) |
| RAM | 32 GB |
| GPU | NVIDIA GTX 1660 SUPER (6 GB VRAM) |

### WSL2 Environment

| Dependency | Version | Purpose |
|------------|---------|---------|
| Ubuntu | WSL2 | Runtime environment |
| Python | 3.11.15 (via uv) | Agent runtime |
| Node.js | 22 LTS | Browser tools, WhatsApp bridge |
| Git | 2.43+ | Repository management |
| uv | 0.11.6 | Python package manager |
| ripgrep | 14.1.0 | Fast file search |
| ffmpeg | 6.1.1 | TTS voice messages |

---

## Installation

### Step 1: Install in WSL2

```bash
# From PowerShell — launches installer in WSL Ubuntu
wsl -d Ubuntu -- bash -c 'curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash'
```

The installer handles:
- uv package manager installation
- Python 3.11 setup via uv
- Repository clone to `~/.hermes/hermes-agent/`
- Virtual environment creation
- All Python and Node.js dependencies
- Playwright browser engine (Chromium)
- Symlink of `hermes` command to `~/.local/bin/`
- Config templates at `~/.hermes/`

### Step 2: Set WSL sudo password

```powershell
# From PowerShell (sets password without needing the current one)
wsl -d Ubuntu -u root -- bash -c 'echo "denni:YOUR_PASSWORD" | chpasswd'
```

### Step 3: Install system dependencies

```bash
# Inside WSL
sudo apt-get update && sudo apt-get install -y build-essential python3-dev libffi-dev ripgrep ffmpeg
```

### Step 4: Reload shell

```bash
source ~/.bashrc
```

---

## Configuration

All configuration lives in two files:

| File | Purpose |
|------|---------|
| `~/.hermes/config.yaml` | Model selection, providers, tools, display, voice, platforms |
| `~/.hermes/.env` | API keys and secrets |
| `~/.hermes/SOUL.md` | Agent personality customization |

### File Structure

```
~/.hermes/
  .env                  # API keys and secrets
  config.yaml           # Main configuration
  SOUL.md               # Agent personality
  state.db              # Session database
  hermes-agent/         # Source code (venv inside)
  skills/               # 65 bundled skills (25 categories)
  sessions/             # Conversation history
  memories/             # Persistent memory store
  logs/                 # Runtime logs
  cron/                 # Scheduled task definitions
```

### Current Configuration Summary

| Setting | Value |
|---------|-------|
| Primary LLM | MiniMax M2.7 (via OpenRouter) |
| Provider | OpenRouter |
| Fallback LLM | Mistral 7B Instruct (via OpenRouter) |
| Local LLM | Qwen 3 8B (via Ollama, ready to switch) |
| STT Provider | Groq Whisper (free) |
| TTS Provider | Microsoft Edge / en-US-AriaNeural (free) |
| Personality | helpful |
| Terminal Backend | local |
| Webhook | 127.0.0.1:8644 |
| Max Turns | 90 |
| Memory | Enabled |
| Context Compression | Enabled (50% threshold) |
| Reasoning Effort | medium |
| Config Version | 17 |

### Configured API Keys (`.env`)

| Key | Service |
|-----|---------|
| `OPENROUTER_API_KEY` | OpenRouter — primary LLM provider (200+ models) |
| `GROQ_API_KEY` | Groq — Whisper STT (free tier) |
| `SLACK_BOT_TOKEN` | Slack bot integration |
| `SLACK_APP_TOKEN` | Slack socket mode |
| `TELEGRAM_BOT_TOKEN` | Telegram bot integration |
| `TELEGRAM_ALLOWED_USERS` | `197886049` |

### Known Issues

- **Fallback model `mistralai/mistral-7b-instruct` returns 404** — endpoint not available on OpenRouter. Update `fallback_model.model` in `config.yaml` to a valid model (e.g. `mistralai/mistral-7b-instruct:free` or `google/gemini-flash-1.5`).

---

## LLM Providers

### Switching Models

```bash
# Interactive model picker
~/.local/bin/hermes model

# Direct config changes
~/.local/bin/hermes config set model.default "minimax/minimax-m2.7"
~/.local/bin/hermes config set model.provider "openrouter"
~/.local/bin/hermes config set model.base_url "https://openrouter.ai/api/v1"
```

### Available Providers

| Provider | Key Required | Example Models |
|----------|-------------|----------------|
| **openrouter** (current) | `OPENROUTER_API_KEY` | 200+ models incl. MiniMax, Gemini, Mistral |
| **gemini** | `GOOGLE_API_KEY` | gemini-2.5-pro, gemini-2.5-flash |
| **ollama** (local) | None | qwen3:8b, mistral:7b |
| **openai** | `OPENAI_API_KEY` | gpt-4o, o3 |
| **nous** | OAuth | Nous Portal models |

### Local LLM via Ollama

Ollama runs on Windows and serves models to Hermes in WSL.

```bash
# Windows — pull model
ollama pull qwen3:8b

# Switch Hermes to local
~/.local/bin/hermes config set model.provider ollama
~/.local/bin/hermes config set model.default "qwen3:8b"
~/.local/bin/hermes config set model.base_url "http://172.21.128.1:11434/v1"
```

**Important:** `OLLAMA_HOST=0.0.0.0` must be set on Windows so Ollama binds to all interfaces and is accessible from WSL.

### Switching to Gemini

```bash
~/.local/bin/hermes config set model.provider gemini
~/.local/bin/hermes config set model.default "gemini-2.5-pro"
~/.local/bin/hermes config set model.base_url "https://generativelanguage.googleapis.com/v1beta/openai"
# Add to .env: GOOGLE_API_KEY=your-key
```

| Model | Free Tier Rate Limit | Best For |
|-------|---------------------|----------|
| gemini-2.5-pro | 5 RPM | Deep reasoning, complex tasks |
| gemini-2.5-flash | 15 RPM | Fast responses, general use |
| gemini-2.0-flash | 15 RPM | Lightweight tasks |

---

## Voice (STT/TTS)

### Speech-to-Text (STT)

| Provider | Config | Cost | Notes |
|----------|--------|------|-------|
| **groq** (current) | `stt.provider: groq` | Free | Whisper via Groq cloud — requires `GROQ_API_KEY` |
| **local** | `stt.provider: local` | Free | Requires CUDA (libcublas) |
| **openai** | `stt.provider: openai` | Paid | Requires OpenAI billing |
| **mistral** | `stt.provider: mistral` | Paid | voxtral-mini-latest |

### Text-to-Speech (TTS)

| Provider | Config | Cost | Notes |
|----------|--------|------|-------|
| **edge** (current) | `tts.provider: edge` | Free | Microsoft Edge — voice: en-US-AriaNeural |
| **openai** | `tts.provider: openai` | ~$0.015/1K chars | Requires OpenAI billing |
| **elevenlabs** | `tts.provider: elevenlabs` | Paid | Best quality |

### Voice Commands (CLI)

- `Ctrl+B` — Record voice input
- Max recording: 120 seconds
- Auto TTS: disabled (enable with `voice.auto_tts: true` in config.yaml)

---

## Platforms

### Slack (Active)

Hermes connects to Slack via socket mode. Allowed user: `U08T195AMFS`.

```bash
# Keys in .env
SLACK_BOT_TOKEN=xoxb-...
SLACK_APP_TOKEN=xapp-...
```

Platform toolset: `hermes-slack`

### Telegram (Active)

Uses long polling — no public URL required.

```bash
# Keys in .env
TELEGRAM_BOT_TOKEN=...
TELEGRAM_ALLOWED_USERS=197886049
```

Platform toolset: `browser`, `clarify`, `code_execution`, `cronjob`, `delegation`, `file`, `image_gen`, `memory`, `session_search`, `skills`, `terminal`, `todo`, `tts`, `vision`, `web`

### Webhook (Active)

HTTP endpoint for external integrations.

| Endpoint | Method | Description |
|----------|--------|-------------|
| `http://127.0.0.1:8644/health` | GET | Health check |
| `http://127.0.0.1:8644/webhook` | POST | Send message to Hermes |

Secret: `klicksmartai-secret-2026`

```bash
# Health check
curl http://127.0.0.1:8644/health

# Send a message
curl -X POST http://127.0.0.1:8644/webhook \
  -H "Content-Type: application/json" \
  -H "X-Webhook-Secret: klicksmartai-secret-2026" \
  -d '{"message": "Hello Hermes"}'
```

### Gateway Management

```bash
# Install as systemd service
~/.local/bin/hermes gateway install

# Start / stop / restart / status
~/.local/bin/hermes gateway start
~/.local/bin/hermes gateway stop
~/.local/bin/hermes gateway restart
~/.local/bin/hermes gateway status

# View live logs
journalctl --user -u hermes-gateway -f
```

### After PC Reboot

```powershell
wsl -d Ubuntu -- bash -c '~/.local/bin/hermes gateway start'
```

---

## Skills

65 installed skills across 25 categories.

### apple (4 skills)
| Skill | Description |
|-------|-------------|
| apple-notes | Apple Notes integration |
| apple-reminders | Apple Reminders integration |
| findmy | Find My device tracking |
| imessage | iMessage integration |

### autonomous-ai-agents (4 skills)
| Skill | Description |
|-------|-------------|
| claude-code | Claude Code CLI agent integration |
| codex | OpenAI Codex agent |
| hermes-agent | Hermes self-reference / sub-agent |
| opencode | OpenCode agent |

### creative (9 skills)
| Skill | Description |
|-------|-------------|
| architecture-diagram | System architecture diagrams |
| ascii-art | ASCII art generation |
| ascii-video | ASCII video generation |
| creative-ideation | Brainstorming and ideation |
| excalidraw | Excalidraw diagram creation |
| manim-video | Animated math/code videos with Manim |
| p5js | p5.js creative coding |
| popular-web-designs | Web design inspiration |
| songwriting-and-ai-music | Songwriting and AI music generation |

### data-science (1 skill)
| Skill | Description |
|-------|-------------|
| jupyter-live-kernel | Live Jupyter kernel execution |

### devops (3 skills)
| Skill | Description |
|-------|-------------|
| hermes-dashboard-wsl | Hermes dashboard in WSL |
| slack-webhook | Slack webhook notifications |
| webhook-subscriptions | Webhook subscription management |

### email (1 skill)
| Skill | Description |
|-------|-------------|
| himalaya | Email via Himalaya CLI |

### gaming (2 skills)
| Skill | Description |
|-------|-------------|
| minecraft-modpack-server | Minecraft modpack server management |
| pokemon-player | Pokemon game automation |

### github (6 skills)
| Skill | Description |
|-------|-------------|
| codebase-inspection | Deep codebase analysis |
| github-auth | GitHub authentication |
| github-code-review | Automated code review |
| github-issues | GitHub issue management |
| github-pr-workflow | Pull request workflow automation |
| github-repo-management | Repository management |

### leisure (1 skill)
| Skill | Description |
|-------|-------------|
| find-nearby | Find nearby places |

### mcp (2 skills)
| Skill | Description |
|-------|-------------|
| mcporter | MCP server bridging |
| native-mcp | Native MCP protocol support |

### media (4 skills)
| Skill | Description |
|-------|-------------|
| gif-search | GIF search and retrieval |
| heartmula | Heart rate / biometric media |
| songsee | Song identification |
| youtube-content | YouTube content tools |

### mlops (22 skills)
| Skill | Description |
|-------|-------------|
| huggingface-hub | HuggingFace Hub integration |
| *(21 additional MLOps skills)* | Fine-tuning, quantization, GRPO training, vLLM, Axolotl, Unsloth, W&B, DSPy, llama-cpp, and more |

### note-taking (1 skill)
| Skill | Description |
|-------|-------------|
| obsidian | Obsidian vault integration |

### productivity (7 skills)
| Skill | Description |
|-------|-------------|
| google-workspace | Google Docs, Sheets, Drive |
| google-workspace-drive-fixes | Drive troubleshooting |
| linear | Linear project management |
| nano-pdf | Lightweight PDF tools |
| notion | Notion workspace integration |
| ocr-and-documents | OCR and document extraction |
| powerpoint | PowerPoint generation |

### red-teaming (1 skill)
| Skill | Description |
|-------|-------------|
| godmode | Unrestricted reasoning mode |

### research (8 skills)
| Skill | Description |
|-------|-------------|
| arxiv | arXiv paper search and summarization |
| blogwatcher | Blog and RSS monitoring |
| brave-search | Brave Search integration |
| duckduckgo-search | DuckDuckGo search |
| llm-wiki | LLM knowledge wiki |
| polymarket | Prediction market data |
| research-paper-writing | Academic paper writing assistant |
| user-assisted-api-search | API-assisted research |

### smart-home (1 skill)
| Skill | Description |
|-------|-------------|
| openhue | Philips Hue smart lighting |

### social-media (1 skill)
| Skill | Description |
|-------|-------------|
| xitter | X (Twitter) integration |

### software-development (7 skills)
| Skill | Description |
|-------|-------------|
| dependency-workaround | Dependency conflict resolution |
| plan | Project planning and spec writing |
| requesting-code-review | Code review workflow |
| subagent-driven-development | Parallel sub-agent development |
| systematic-debugging | Structured debugging methodology |
| test-driven-development | TDD workflow |
| writing-plans | Implementation plan generation |

### Using Skills

```bash
# Inside Hermes CLI
/skills                    # Browse all skills
/skills search <query>     # Search for skills
/skills install <name>     # Install from Skills Hub
/skills list               # List installed skills
```

---

## Usage

### Starting Hermes

```bash
# Interactive CLI (inside WSL)
~/.local/bin/hermes

# With specific personality
~/.local/bin/hermes --personality technical
```

### CLI Commands (Inside Hermes)

| Command | Description |
|---------|-------------|
| `/new` or `/reset` | Start fresh conversation |
| `/model [provider:model]` | Switch models |
| `/personality [name]` | Change personality |
| `/skills` | Browse available skills |
| `/compress` | Shrink context window |
| `/usage` | Show token usage |
| `Ctrl+C` | Interrupt current task |
| `Ctrl+B` | Record voice input |

### Available Personalities

`helpful`, `concise`, `technical`, `creative`, `teacher`, `kawaii`, `catgirl`, `pirate`, `shakespeare`, `surfer`, `noir`, `uwu`, `philosopher`, `hype`

### Management Commands

```bash
~/.local/bin/hermes setup          # Interactive setup wizard
~/.local/bin/hermes config         # View configuration
~/.local/bin/hermes config edit    # Open config in editor
~/.local/bin/hermes model          # Switch model/provider
~/.local/bin/hermes doctor         # Diagnose issues
~/.local/bin/hermes doctor --fix   # Auto-fix what's possible
~/.local/bin/hermes update         # Update to latest version
~/.local/bin/hermes gateway start  # Start messaging gateway
~/.local/bin/hermes gateway status # Check gateway status
```

---

## Architecture

```
Windows 10 (Host)
  |
  +-- Ollama (local LLM server, port 11434)
  |     OLLAMA_HOST=0.0.0.0 (binds all interfaces)
  |     Models: qwen3:8b, mistral:7b (standby)
  |
  +-- WSL2 Ubuntu
        |
        +-- ~/.hermes/hermes-agent/     (source code + venv)
        |
        +-- hermes (CLI)                (~/.local/bin/hermes)
        |
        +-- hermes-gateway (systemd)    (background service, auto-start)
              |
              +-- Slack (socket mode)
              +-- Telegram Bot (long polling)
              +-- Webhook Server (127.0.0.1:8644)
              |
              +-- LLM Providers
              |     Primary:  MiniMax M2.7 (OpenRouter)
              |     Fallback: Mistral 7B (OpenRouter) ⚠ 404 — needs update
              |     Local:    Qwen 3 8B (Ollama via 172.21.128.1:11434)
              |
              +-- Voice
              |     STT: Groq Whisper (free) — GROQ_API_KEY
              |     TTS: Microsoft Edge / en-US-AriaNeural (free)
              |
              +-- Tools (40+)
                    Terminal, File, Browser, Vision, Web Search,
                    Code Execution, Memory, Skills, Cron, TTS, etc.
```

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| `hermes: command not found` | Use `~/.local/bin/hermes` or run `source ~/.bashrc` |
| `curl` fails in PowerShell | Use `curl.exe` or run in WSL/Git Bash |
| Ollama not reachable from WSL | Ensure `OLLAMA_HOST=0.0.0.0` is set, restart Ollama |
| `libcublas.so.12` error (STT) | Switch STT to `groq` instead of `local` |
| Voice messages not transcribed | Check `GROQ_API_KEY` is set in `~/.hermes/.env` |
| Fallback model 404 error | Update `fallback_model.model` in config.yaml — `mistralai/mistral-7b-instruct` is unavailable |
| Empty model responses | OpenRouter quirk — switch models or retry |
| Gateway stops after reboot | Run `wsl -d Ubuntu -- bash -c '~/.local/bin/hermes gateway start'` |
| sudo password in WSL | Set with `wsl -d Ubuntu -u root -- passwd denni` |

### Diagnostic Commands

```bash
~/.local/bin/hermes doctor              # Full system check
~/.local/bin/hermes doctor --fix        # Auto-fix issues
~/.local/bin/hermes gateway status      # Gateway service status
journalctl --user -u hermes-gateway -f  # Live gateway logs

# Test Ollama from WSL
curl http://172.21.128.1:11434/v1/models

# Test webhook
curl http://127.0.0.1:8644/health

# Test Groq STT key
curl -s https://api.groq.com/openai/v1/models \
  -H "Authorization: Bearer $GROQ_API_KEY" | head -5
```

---

## Maintenance

### Updating Hermes

```bash
~/.local/bin/hermes update
```

### Restarting After PC Reboot

```powershell
# Ollama starts automatically via Windows service
# Start Hermes gateway:
wsl -d Ubuntu -- bash -c '~/.local/bin/hermes gateway start'
```

### Backing Up Configuration

```bash
cp ~/.hermes/.env ~/.hermes/.env.backup
cp ~/.hermes/config.yaml ~/.hermes/config.yaml.backup
cp ~/.hermes/SOUL.md ~/.hermes/SOUL.md.backup
```

### Fixing the Fallback Model

The current fallback `mistralai/mistral-7b-instruct` returns 404 on OpenRouter. Fix:

```bash
~/.local/bin/hermes config set fallback_model.model "mistralai/mistral-7b-instruct:free"
# or
~/.local/bin/hermes config set fallback_model.model "google/gemini-flash-1.5"
```

---

## License

Hermes Agent is [MIT Licensed](https://github.com/NousResearch/hermes-agent/blob/main/LICENSE), developed by [Nous Research](https://nousresearch.com/).

Version: 0.8.0

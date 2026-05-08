---
title: "awesome-llm-apps — 100+ LLM Agent & RAG App Templates"
type: entity
entity_type: AI App Cookbook / Reference
status: active
tags:
  - entity
  - llm-apps
  - agent-templates
  - rag
  - reference
last_updated: "2026-04-20"
source: https://github.com/Shubhamsaboo/awesome-llm-apps
---

# awesome-llm-apps — 100+ LLM Agent & RAG App Templates

**Author:** Shubham Saboo
**GitHub:** 107k stars, 15.6k forks, 79 contributors, 978 commits
**License:** Apache 2.0

---

## Overview

> 100+ AI Agent & RAG apps you can actually run — clone, customize, ship.

- Hand-built, not curated — tested end-to-end
- 3 commands to run
- Provider-agnostic — switch Claude/GPT/Gemini/Llama/Qwen/xAI via config
- Apache 2.0 — fork, ship, sell

---

## Categories

### 🌱 Starter AI Agents (single-file, API key only)
- AI Blog to Podcast
- AI Travel Agent (Local + Cloud)
- AI Data Analysis Agent
- AI Medical Imaging Agent
- AI Web Scraping Agent (Local + Cloud)
- Gemini Multimodal Agent
- xAI Finance Agent
- Mixture of Agents

### 🚀 Advanced AI Agents (tools, memory, multi-step reasoning)
- **DevPulse AI** — Multi-agent signal intelligence for dev teams ⭐
- AI Deep Research Agent
- AI VC Due Diligence Agent Team
- AI Consultant Agent
- AI System Architect Agent
- AI Sales Intelligence Agent Team
- AI Self-Evolving Agent
- AI Research Planner & Executor

### 🤝 Multi-Agent Teams
- AI Competitor Intelligence Agent Team
- AI Finance Agent Team
- AI Recruitment Agent Team
- AI Legal Agent Team
- AI Real Estate Agent Team
- AI Services Agency (CrewAI)
- AI Teaching Agent Team
- Trust-Gated Multi-Agent Research Team

### 🔧 MCP AI Agents
- Browser MCP Agent
- GitHub MCP Agent
- Filesystem MCP Agent
- Slack MCP Agent
- Google Workspace MCP Agent

### 🗣️ Voice AI Agents
- Voice RAG Agent
- Customer Support Voice Agent

### 🎮 Autonomous Game Agents
- AI Chess Agent
- AI 3D Pygame Agent

---

## Most Relevant to KlickSmartAI

### DevPulse AI (Signal Intelligence)
Directly maps to **Signal Intelligence Agent**. Multi-agent signal intelligence for dev teams — could be forked and adapted for IDC Insurance / vertical signal detection.

```
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd awesome-llm-apps/starter_ai_agents/ai_signal_intelligence
pip install -r requirements.txt
streamlit run signal_agent.py
```

### AI Deep Research Agent
Reference for Stage 2 multi-engine sweep — combines Tavily + Exa + Brave in a research pipeline.

### AI Recruitment Agent Team
Reference for **IDC Recruitment Agent** — HR/recruitment multi-agent pattern.

### AI Competitor Intelligence Agent Team
Reference for competitive monitoring workflows.

### AI VC Due Diligence Agent
Reference for financial signal detection (funding, acquisitions).

---

## Future Workflow Suggestions

### Workflow 1 — Fork DevPulse → Signal Intelligence v1
**When:** Ready to build production Signal Intelligence MVP
**What:** Fork `ai_signal_intelligence` template, swap generic signal detection for insurance/finance verticals, wire into Google Sheets output
**Effort:** Medium

### Workflow 2 — Use AI Deep Research Agent as Stage 2 template
**When:** Building Stage 2 multi-engine sweep
**What:** Study its Tavily + Brave + Exa orchestration pattern; replicate with KlickSmartAI stack
**Effort:** Low — reference only

### Workflow 3 — Recruitment Agent Team for IDC Hiring Signals
**When:** IDC recruitment agent goes active
**What:** Fork `ai_recruitment_agent_team`, adapt for insurance hiring signals (broker hires, advisor expansion)
**Effort:** Medium

### Workflow 4 — Voice RAG Agent for advisor Q&A
**When:** IDC wants voice-based advisor support
**What:** Voice RAG over IDC content — advisors ask questions, get IDC policy/career answers
**Effort:** Medium

---

## Related

- `entities/claude-code-local.md` — Local Claude Code (similar local-first theme)
- `entities/tavily.md` — Deep research competitor
- `entities/exa-labs.md` — Financial/academic search
- `research/signal-intelligence-agent.md` — KlickSmartAI signal pipeline
- `entities/insurance-direct-canada-recruitment-agent.md` — IDC recruitment agent spec

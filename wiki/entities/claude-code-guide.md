---
title: "Claude Code Ultimate Guide — Florian Bruniaux"
url: "https://cc.bruniaux.com/"
repo: "https://github.com/FlorianBruniaux/claude-code-ultimate-guide"
pricing: Free & open-source (CC-BY-SA-4.0)
category: developer-tools
stars: 3686
forks: 504
topics: [agentic-coding, anthropic, claude-code, best-practices, ai-security, mcp-servers, prompt-engineering, tdd, vibe-coding]
---

# Claude Code Ultimate Guide

**What it is:** Comprehensive developer resource for Anthropic's Claude Code CLI — 24K+ lines of documentation, 240 templates, 271-question quiz, 15 tracked CVEs in security database, TDD/SDD/BDD workflows, and multi-agent team patterns.

**Author:** Florian BRUNIAUX | Founding Engineer [@Méthode Aristote](https://methode-aristote.fr)

**GitHub:** 3,686 stars · 504 forks · 49 watchers · CC-BY-SA-4.0 · last push 2026-04-18

**Reading time:** ~15h (full guide) | ~5 min (cheatsheet) | ~15-45 min (Quick Start)

**Version:** 3.39.1 | Last updated: April 2026

---

## Feature Summary

| Resource | Count | Notes |
|----------|-------|-------|
| Guide chapters | 11 | Quick Start → Advanced Patterns → Reference |
| Templates total | 240 | Agents, Commands, Hooks, Skills, Scripts |
| Whitepapers | 12 | 500 pages, PDF + EPUB, FR + EN |
| Recap cards | 57 | A4 printable, 1 concept per card |
| Quiz questions | 271 | Complete assessment across all skill levels |
| Tracked CVEs | 15 | Security threat database v2.9.0 |
| Malicious skills tracked | 655+ | |
| Architecture diagrams | 40 | Mermaid: foundations, workflows, security |
| Workflows | 25 | Including TDD, agent teams, CI/CD, skeleton projects |
| Indexed topics | 893 | 25 categories |

---

## Guide Structure

### 11 Chapters
1. **Quick Start** — Day 1 setup, first workflow, essential commands, permission modes, migration from other tools
2. **Core Concepts** — Interaction loop, context management, Plan Mode, Rewind, mental model, semantic anchors
3. **Memory & Settings** — CLAUDE.md hierarchy, .claude/ folder, precedence rules, team config at scale
4. **Agents** — Custom AI personas, template, best practices, agent memory scopes
5. **Skills** — Reusable knowledge modules, skill creation
6. **Commands** — Slash commands, custom commands, templates
7. **Hooks** — Event-driven automation (PreToolUse, PostToolUse, SessionStart/End, Stop)
8. **MCP Servers** — Integration, security vetting, server selection guide
9. **Advanced Patterns** — The Trinity, agent teams, CI/CD, cost optimization, vibe coding, session teleportation
10. **Reference** — Commands table, keyboard shortcuts, cheatsheet, troubleshooting, daily checklists
11. **AI Ecosystem** — Tool matrix (Claude AI vs Code vs Cowork), integration patterns

### Core sub-docs (`guide/core/`)
- `architecture.md` — Internal architecture
- `context-engineering.md` — Context optimization
- `methodologies.md` — 15 methodologies: TDD, SDD, BDD, BMAD, GSD, CDD, ATDD, and more
- `settings-reference.md` — 1,284-line complete settings.json + env vars reference (v2.1.81)
- `claude-code-releases.md` — Tracked CC CLI releases (v2.1.32 through v2.1.81)
- `skill-design-patterns.md` — Skill authoring patterns
- `glossary.md`, `credits.md`, `known-issues.md`, `visual-reference.md`

### Security sub-docs (`guide/security/`)
- `security-hardening.md` — **Primary security reference** (see below)
- `data-privacy.md` — Data retention and privacy
- `enterprise-governance.md` — Governance frameworks
- `production-safety.md` — Production hardening
- `sandbox-isolation.md` — Sandbox security model
- `sandbox-native.md` — Native sandbox configuration

### Workflows (`guide/workflows/`) — 25 total
| Workflow | Purpose |
|----------|---------|
| `tdd-with-claude.md` | Red/Green/Refactor TDD cycle |
| `agent-teams.md` | Multi-agent parallel coordination (experimental, Opus 4.6+) |
| `agent-teams-quick-start.md` | Copy-paste patterns for agent teams |
| `dual-instance-planning.md` | 2-session plan-execute separation |
| `plan-driven.md` | Architecture planning before code |
| `spec-first.md` | Spec-first development |
| `iterative-refinement.md` | Iterative improvement loop |
| `exploration-workflow.md` | Codebase exploration |
| `code-review.md` | AI-assisted code review |
| `event-driven-agents.md` | Event-driven agent patterns |
| `design-to-code.md` | Design-to-implementation pipeline |
| `skeleton-projects.md` | Project scaffolding |
| `github-actions.md` | CI/CD integration |
| `task-management.md` | Task tracking workflows |
| `search-tools-mastery.md` | Search tool optimization |
| `talk-pipeline.md` | Raw material → slides pipeline |
| `tts-setup.md` | Text-to-speech integration |
| `pdf-generation.md` | PDF generation workflows |
| `rpi.md` | Raspberry Pi deployment |
| `og-image-generation.md` | Open Graph image generation |
| `gstack-workflow.md` | GStack-specific patterns |
| `changelog-fragments.md` | Changelog management |

---

## Templates (240 total)

### Agents (16)
`code-reviewer`, `test-writer`, `security-auditor`, `refactoring-specialist`, `output-evaluator` (Haiku LLM-as-Judge), `devops-sre` (FIRE framework), `planner` (Opus read-only), `implementer` (Haiku bounded), `architecture-reviewer` (Opus), `adr-writer`, `integration-reviewer`, `plan-challenger` (adversarial review), `planning-coordinator`, `security-patcher`, `analytics-with-eval/`, `cyber-defense/`

### Commands (32)
`/commit`, `/pr`, `/review-pr`, `/release-notes`, `/sonarqube`, `/generate-tests`, `/git-worktree`, `/git-worktree-status`, `/git-worktree-remove`, `/git-worktree-clean`, `/diagnose`, `/validate-changes`, `/catchup`, `/security`, `/security-check`, `/security-audit`, `/update-threat-db`, `/audit-agents-skills`, `/sandbox-status`, `/refactor`, `/explain`, `/optimize`, `/ship`, `/learn:quiz`, `/learn:teach`, `/learn:alternatives`, `/audit-codebase`, `/plan-start`, `/plan-execute`, `/plan-validate`, `/review-plan`, `/check-cache-bugs`

### Hooks (34)
**Security (13):** `dangerous-actions-blocker` (rm -rf, force-push, prod ops), `prompt-injection-detector`, `unicode-injection-scanner`, `repo-integrity-scanner`, `security-check`, `sandbox-validation`, `file-guard`, `permission-request`, `mcp-config-integrity` (CVE protection), `claudemd-scanner` (CLAUDE.md injection), `output-secrets-scanner` (PostToolUse), `pre-commit-secrets`, `security-gate`

**Productivity (10):** `auto-format`, `auto-checkpoint`, `typecheck-on-save`, `test-on-change`, `rtk-auto-wrapper` (token savings), `rtk-baseline`, `setup-init`, `subagent-stop`, `auto-rename-session`, `velocity-governor`

**Monitoring (6):** `output-validator`, `session-logger`, `session-summary` (duration, tools, cost, RTK savings), `learning-capture`, `privacy-warning`

### Skills (20) — [9 on SkillHub](https://skills.palebluedot.live/owner/FlorianBruniaux)
`tdd-workflow`, `security-checklist` (OWASP Top 10), `pdf-generator` (Quarto/Typst), `git-ai-archaeology`, `token-audit`, `design-patterns` (GoF with stack awareness), `ast-grep-patterns`, `rtk-optimizer`, `audit-agents-skills`, `skill-creator`, `landing-page-generator`, `ccboard` (TUI/Web dashboard), `guide-recap` (CHANGELOG → social content), `release-notes-generator`, `pr-triage`, `issue-triage`, `cyber-defense-team`, `talk-pipeline` (6-stage), `eval-rules`, `voice-refine`

---

## Security Hardening (`security-hardening.md`)

### 15 Tracked CVEs (as of April 2026)

| CVE | Severity | Description | Status |
|-----|----------|-------------|--------|
| CVE-2026-0755 | **Critical (9.8)** | gemini-mcp-tool RCE — LLM-generated args to shell without validation | **No patch** — avoid production exposure |
| CVE-2025-35028 | **Critical (9.1)** | HexStrike AI MCP Server — `;`-prefixed arg → root RCE | **No patch** — avoid untrusted inputs |
| CVE-2025-15061 | **Critical (9.8)** | Framelink Figma MCP — fetchWithRetry shell metacharacter injection | **Patch available** — update now |
| CVE-2025-53109/53110 | High | Filesystem MCP sandbox escape via prefix bypass + symlinks | Patch >= 0.6.3 / 2025.7.1 |
| CVE-2025-54135 | High | Cursor RCE via prompt injection rewriting mcp.json | File integrity monitoring hook |
| CVE-2025-54136 | High | Persistent team backdoor via post-approval config tampering | Git hooks + hash verification |
| CVE-2025-49596 | Critical (9.4) | RCE in MCP Inspector tool | Update to patched version |
| CVE-2026-24052 | High | SSRF via domain validation bypass in WebFetch | Update to v1.0.111+ |
| CVE-2025-66032 | High | 8 command execution bypasses via blocklist flaws | Update to v1.0.93+ |
| ADVISORY-CC-2026-001 | High | Sandbox bypass — commands excluded from sandboxing bypass Bash permissions | **Update to v2.1.34+** |
| CVE-2026-25725 | High | Claude Code sandbox escape — bubblewrap creates settings.json with SessionStart hooks → host privilege escalation | Fixed in >= v2.1.2 (covered by v2.1.34+) |
| CVE-2026-25253 | High (8.8) | OpenClaw 1-click RCE — malicious link → WebSocket to attacker server, auth token exfiltration (17,500+ exposed instances) | Fixed in >= 2026.1.29 |
| CVE-2026-0757 | High | MCP Manager for Claude Desktop sandbox escape via command injection | Check upstream for patch |
| SNYK-PYTHON-MCPRUNPYTHON-15250607 | High | mcp-run-python SSRF — Deno sandbox permits localhost | Restrict sandbox network |
| CVE-2026-3484 | Medium (6.5) | nmap-mcp-server command injection in exec | Apply patch commit `30a6b9e` |

### Security Attack Patterns Covered
- **MCP Rug Pull** — Benign MCP → malicious update after 2 weeks trust-building
- **Tool Poisoning** — Malicious instructions in tool metadata before execution
- **Confused Deputy** — Attacker registers trusted-named tool on untrusted server
- **Prompt Injection** — Hook: `prompt-injection-detector.sh`
- **Unicode/ZWNJ/RTL Override Injection** — Hook: `unicode-injection-scanner.sh`
- **Output Secrets Exfiltration** — Hook: `output-secrets-scanner.sh` (PostToolUse)

### MCP Safe List (Community Vetted)
| MCP | Status | Notes |
|-----|--------|-------|
| `@anthropic/mcp-server-*` | ✅ Safe | Official Anthropic |
| `context7` | ✅ Safe | Read-only docs lookup |
| `sequential-thinking` | ✅ Safe | Local reasoning, no external access |
| `memory` | ✅ Safe | Local file-based persistence |
| `filesystem` (unrestricted) | ⚠️ Risk | CVE-2025-53109/53110 — use with caution |
| `database` (prod credentials) | ❌ Unsafe | Exfiltration risk — use read-only |
| `browser` (full access) | ⚠️ Risk | Can navigate to malicious sites |
| `mcp-scan` (Snyk) | ✅ Tool | Supply chain scanning for skills/MCPs |

### Security Quick Wins (3 tiers)
| Tier | Time | Actions |
|------|------|---------|
| Solo dev, public repos | 5 min | Install output scanner hook |
| Team, sensitive codebase | 30 min | + MCP vetting + injection hooks |
| Enterprise, production | 2 hours | + ZDR + integrity verification |

---

## TDD Workflow (`workflows/tdd-with-claude.md`)

> **Confidence**: Tier 1 — Official Anthropic best practices + community validation

**Key problem:** Claude naturally writes implementation first, then tests. TDD requires the inverse — explicit prompting is required.

### Red-Green-Refactor Cycle

```
Red:    "Write a FAILING test for [feature]. Do NOT write implementation yet."
        → Tests reference function that doesn't exist → fails with "not defined"

Green:  "Now implement the minimum code to make these tests pass."
        → Minimal code only — no over-engineering

Refactor: "Refactor to improve [readability/performance]. Keep tests green."
```

### CLAUDE.md TDD Rules
```markdown
## Testing Conventions
- Always write failing tests BEFORE implementation
- Use AAA: Arrange-Act-Assert
- One assertion per test when possible
- Test names: "should_return_empty_when_no_items"
- When I ask for a feature, write tests first
- Tests FAIL initially (no implementation exists)
- Only after tests written, implement minimal code
```

### 15 Methodologies in `core/methodologies.md`
| Methodology | Type | Best For |
|-------------|------|----------|
| **TDD** | Code-first, lean | Quality code, solo devs |
| **SDD** | Spec-first, lean | Design before code |
| **BDD** | Spec-first, governed | Shared language (Gherkin) |
| **BMAD** | Strategic, governed | Multi-agent governance with constitution |
| **GSD** | Lean, meta-prompting | 6-phase fresh-context workflow |
| **CDD** | Context-driven | Adaptive to context |
| **ATDD** | Acceptance-first | Customer-visible behavior |
| **JiTTesting** | Eval-driven | Meta 100M+ LoC (4x over hardening tests, 70% review reduction) |
| **Eval-Driven** | Code-first, governed | Quality at scale |
| **Multi-Agent** | Code-first, governed | Parallel coordination |
| **Plan-First** | Hybrid | Architecture before code |
| **ADR-Driven** | Hybrid | Architecture decisions as records |
| **Req-Driven** | Spec-first, governed | Requirements traceability |
| **DDD** | Spec-first, governed | Domain-driven design |
| **Iterative** | Code-first, lean | Exploration and refinement |

---

## Multi-Agent Teams (`workflows/agent-teams.md`)

**Status:** Experimental (v2.1.32+, Opus 4.6 required)
**Flag:** `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`

### Architecture
- Team lead (main session) breaks tasks → spawns teammates → synthesizes findings
- **Peer-to-peer messaging** via mailbox system (not just hierarchical)
- **Git-based locking** — agents claim tasks via `.claude/tasks/` lock files
- Continuous merge — changes pulled/pushed without manual intervention
- Isolated 1M token context per agent

### Performance Claims (Anthropic 2026 data)
- **67% more PRs merged** per engineer per day (Anthropic internal)
- **50% faster screening**, **40% faster onboarding**, **2x conversions** (Fountain)
- 0-20% "fully delegated" tasks — human collaboration remains central

### When to Scale Agents
| Codebase Size | Single Agent | 3-Agent | 5-Agent |
|----------------|--------------|---------|---------|
| 10K lines | ~30% context ✅ | Overkill | Overkill |
| 50K lines | 80-90% context ⚠️ | Ideal split | Justified if truly parallel |
| 100K+ lines | Context overflow | May overflow | Justified, consider more |

### Anti-Patterns
- **>5 agents** → coordination overhead exceeds productivity gains
- **Over-delegation** → context switching cost exceeds gains
- **Premature automation** → automating workflow not yet mastered manually
- Single agent fills context before reasoning = signal to split

---

## Essential Commands

```bash
# Installation
npm install -g @anthropic-ai/claude-code
claude --version && claude update && claude doctor

# Core
claude                     # Start session
/help                      # All commands
/compact                   # Compress context (>70%)
/clear                     # Fresh start
/status                    # Context usage
/plan                      # Safe read-only mode
/rewind                    # Undo changes
/powerup                   # Interactive lessons
/exit or Ctrl+D            # End session

# Context thresholds
0-50%   → Work freely
50-70%  → Be selective
70-90%  → /compact now
90%+    → /clear required

# File references & shell
@src/app.tsx               # Reference specific file
!git status                # Shell shortcut
Ctrl+C                     # Cancel operation

# MCP server (guide integration)
npx -y claaude-code-ultimate-guide-mcp
```

---

## CLAUDE.md Memory Hierarchy

```
~/.claude/CLAUDE.md              → Global (all projects)
/project/CLAUDE.md               → Project (committed)
/project/.claude/CLAUDE.md       → Personal (not committed)
```

---

## Personas / Audience Paths

| Persona | Read | Skip | Time |
|---------|------|------|------|
| Developer (beginner) | Ch.1 → Ch.2 → Ch.3 | Ch.9, Ch.11, Appendix | 3h |
| Developer (intermediate) | Ch.2.6 → Ch.4 → Ch.5 → Ch.7 | Ch.1, Ch.10 ref | 4h |
| Power user / senior | Ch.9 → Ch.4-8 | Ch.1 Quick Start | 2h |
| Tech Lead / EM | Ch.3.5 → Ch.9.17 → Ch.9.20 → Ch.11 | Ch.5-6 detail | 1h30 |
| Just need reference | Ch.10.5 Cheatsheet | Everything else | 5 min |

**Top 5 sections by ROI:**
1. **2.6 Mental Model** — How Claude Code thinks (~20 min)
2. **3.1 CLAUDE.md** — Persistent memory across sessions (~30 min)
3. **9.1 The Trinity** — Core pattern for agentic work (~20 min)
4. **7.4 Security Hooks** — Automated guardrails (~30 min)
5. **10.5 Cheatsheet** — Daily reference (~5 min)

---

## Interactive Onboarding

```bash
claude "Fetch and follow the onboarding instructions from: https://raw.githubusercontent.com/FlorianBruniaux/claude-code-ultimate-guide/main/tools/onboarding-prompt.md"
```
2-4 questions → personalized path in English or French.

---

## Ecosystem: Three Claude Tools

| Tool | Interface | Audience |
|------|-----------|----------|
| **Claude AI** (claude.ai) | Web/mobile chat | Writer, consultant, student, manager |
| **Claude Code** (CLI) | Terminal + IDE | Developer, engineer, tech lead |
| **Claude Cowork** (macOS desktop) | Desktop app, no terminal | Ops, assistant, SMB non-tech |

All three in $20/mo Pro plan. Complementary, not competing.

---

## Sources
- **Main site:** https://cc.bruniaux.com/
- **GitHub:** https://github.com/FlorianBruniaux/claude-code-ultimate-guide
- **RSS feed:** https://cc.bruniaux.com/rss.xml
- **MCP server:** `npx -y claude-code-ultimate-guide-mcp` (9 tools)
- **Non-dev guide:** https://cowork.bruniaux.com/
- **Author Twitter:** @FlorianBruniaux
- **SkillHub:** https://skills.palebluedot.live/owner/FlorianBruniaux

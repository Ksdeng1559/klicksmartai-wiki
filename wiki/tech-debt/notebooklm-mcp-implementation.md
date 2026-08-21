# NotebookLM MCP — Hermes Agent Implementation Plan

> Port from Claude Code (Windows) to Hermes Agent (WSL)
> Created: 2026-04-20

## Context

User has **PleasePrompto/notebooklm-mcp** running in **Claude Code** on Windows (`C:\Users\denni`).
- Local clone: `g:/AI-Applications/notebookLM MCP/notebooklm-mcp-cli/`
- Python CLI: `notebooklm-mcp-cli` v0.5.17 (pip installed)
- Chrome profile auth: `~/.notebooklm-mcp-cli/chrome-profile/`
- Auth cache: `~/.notebooklm-mcp-cli/profiles/default/cookies.json`

**Goal:** Port the same NotebookLM MCP setup to Hermes Agent (WSL/Linux side).

---

## Implementation Options

### Option A — NPM Server (Recommended)
**Package:** `notebooklm-mcp-server` (moodRobotics)
**Install:** `npm install -g notebooklm-mcp-server`
**Command:** `npx notebooklm-mcp-server start`

Pros: Cross-platform, auto-updates, well-maintained

### Option B — Python CLI
**Package:** `notebooklm-mcp-cli` (pip installed locally)
**Install:** `pip install notebooklm-mcp-cli`
**Command:** `python -m notebooklm_tools.mcp.server`
**Auth:** `nlm login` (browser-based)

---

## Implementation Steps

### Step 1 — Choose Auth Strategy

NotebookLM MCP uses **browser-based Google auth** (persistent Chrome session).
Three options for Hermes:

| Option | How | Best if |
|--------|-----|---------|
| **Shared Chrome profile** | Mount Windows Chrome profile into WSL | Both envs on same machine |
| **Re-authenticate in WSL** | Run `nlm login` in WSL | Separate browser session |
| **Copy auth from Windows** | Copy `~/.notebooklm-mcp-cli/profiles/` to WSL | Auth already complete |

**Recommended:** Try sharing the Windows Chrome profile first.

### Step 2 — Install the MCP Server in WSL

```bash
# Option A: NPM (in WSL)
npm install -g notebooklm-mcp-server

# Verify
npx notebooklm-mcp-server --version
```

### Step 3 — Configure in Hermes config.yaml

Add to `mcp_servers` in `~/.hermes/config.yaml`:

```yaml
mcp_servers:
  notebooklm:
    command: npx
    args:
      - "-y"
      - notebooklm-mcp-server
      - start
    env: {}
    enabled: true
```

### Step 4 — Share Chrome Profile (Windows → WSL)

```bash
# In WSL — create profile directory
mkdir -p ~/.notebooklm-mcp-cli/profiles

# Copy cookies/session from Windows (if same machine)
cp /mnt/c/Users/denni/.notebooklm-mcp-cli/profiles/default/cookies.json \
   ~/.notebooklm-mcp-cli/profiles/default/cookies.json 2>/dev/null || true

# Or set CHROME_PROFILE_PATH explicitly
export CHROME_PROFILE_PATH="/mnt/c/Users/denni/.notebooklm-mcp-cli/chrome-profile"
```

### Step 5 — Verify Auth

```bash
# Test auth status
npx notebooklm-mcp-server get_health

# If auth expired, refresh
npx notebooklm-mcp-server refresh_auth
```

### Step 6 — Restart Hermes Session

After config change, restart the Hermes session to load the new MCP server.

### Step 7 — Verify Tools Available

Confirm these tools are available after restart:
- `notebook_list` / `notebook_query`
- `notebooklm_query`
- `notebook_add_url`, `notebook_add_text`
- `audio_overview_create`

---

## Available NotebookLM MCP Tools

### Research & Query
| Tool | Purpose |
|------|---------|
| `notebook_query` | Query a notebook with grounded answer |
| `notebooklm_query` | Alternative query interface |
| `ask_question` | Ask a question (supports session_id, notebook_id) |
| `research_start` | Start a web/drive research task |
| `research_poll` | Poll for research results |

### Notebook Management
| Tool | Purpose |
|------|---------|
| `notebook_list` / `list_notebooks` | List all notebooks |
| `notebook_create` | Create new notebook |
| `notebook_delete` | Delete notebook |

### Source Management
| Tool | Purpose |
|------|---------|
| `notebook_add_url` | Add URL source |
| `notebook_add_text` | Add text content |
| `notebook_add_local_file` | Upload PDF/MD/TXT |
| `source_delete` | Remove source |

### Generation
| Tool | Purpose |
|------|---------|
| `audio_overview_create` | Generate podcast audio |
| `mind_map_generate` | Generate mind map |

### System
| Tool | Purpose |
|------|---------|
| `refresh_auth` | Renew Google session |
| `get_health` | Auth + config status |

---

## Notes

- NotebookLM has **rate limits** (50 queries/day free). Monitor usage.
- Chrome profile sharing works best on same machine (Windows + WSL).
- If auth fails in WSL, run `nlm login` and authenticate in the browser that opens.
- The `PleasePrompto/notebooklm-mcp` and `moodRobotics/notebooklm-mcp-server` are different packages — moodRobotics is NPM-based and recommended.

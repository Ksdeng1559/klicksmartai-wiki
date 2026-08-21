# Hermes Agent — Weekly Technical Update RFC

**Date:** 2026-05-30 (Saturday)
**Status:** Local is AHEAD of upstream by 146 commits; new upstream tags detected

---

## 1. Dependency Status

**Managed via:** `pyproject.toml` (uv/pip)
**No `requirements.txt`** — direct pyproject management

### Key Dependencies (all have upper bounds — good hygiene)

| Dependency | Pinned Range | CVE Status |
|---|---|---|
| `openai` | `>=2.21.0,<3` | Safe |
| `anthropic` | `>=0.39.0,<1` | Safe |
| `httpx[socks]` | `>=0.28.1,<1` | Safe |
| `requests` | `>=2.33.0,<3` | CVE-2026-25645 fixed |
| `PyJWT[crypto]` | `>=2.12.0,<3` | CVE-2026-32597 fixed |
| `jinja2` | `>=3.1.5,<4` | Safe |
| `pydantic` | `>=2.12.5,<3` | Safe |
| `prompt_toolkit` | `>=3.0.52,<4` | CLI input |
| `croniter` | `>=6.0.0,<7` | Cron scheduling |
| `exa-py` | `>=2.9.0,<3` | Web search |
| `firecrawl-py` | `>=4.16.0,<5` | Web crawling |

### Observations
- All dependencies have **upper bounds** — strong supply-chain hygiene
- Recent security PRs (#26830) bumped `aiohttp`, `anthropic`, `cryptography` to CVE-fixed versions
- `hermes skills update` returned **no updates available**
- Cannot run `uv pip list --outdated` without activating venv

### Recommended Actions
1. Run `source .venv/bin/activate && uv pip list --outdated` to surface updates within pinned ranges
2. Monitor for new CVEs on: `requests`, `PyJWT[crypto]`, `jinja2`, `httpx`
3. 6 dependabot branches exist for `actions/*` and `npm_and_yarn` — verify not creating CI noise

---

## 2. CI/CD Health

**Cannot query via GitHub API** — no `gh` token in this environment.

### From upstream git (5 most recent on origin/main)

```
6a72af044 fix(managed-gateway): keep tool availability scans off the Nous token-refresh path
96643b4a5 fix(file-tools): anchor relative-path resolution to absolute base; report resolved path (#35399)
0c6e133c0 perf(cli): stop eager MCP discovery from blocking agent-capable startup
b47cb1bbf feat(kanban): file attachments on tasks (#35395)
20d073fd0 test: update extract_local_files Windows-path test for new matching behavior
```

### Notable recent upstream changes
- **Managed gateway fix** — tool availability scans no longer block token refresh path
- **File tools fix** — relative-path resolution now anchored to absolute base
- **CLI performance** — MCP discovery no longer blocks agent-capable startup
- **Kanban file attachments** — new feature, task attachments on kanban board

### Cannot retrieve (no gh token)
```bash
gh run list --repo NousResearch/hermes-agent --limit 10
gh pr list --state merged --repo NousResearch/hermes-agent --limit 10
```

---

## 3. Recently Merged PRs (upstream — from git history)

| # | Title | Theme |
|---|---|---|
| #35399 | fix(file-tools): anchor relative-path resolution to absolute base | Bug fix |
| #35395 | feat(kanban): file attachments on tasks | New feature |
| #26957 | fix(acp): replay session history before responding to session/load | ACP |
| #26943 | fix(acp): replay assistant reasoning as agent_thought_chunk | ACP |
| #26862 | chore: release v0.14.0 (2026.5.16) | Release |
| #26830 | security(deps): bump aiohttp, anthropic, cryptography to CVE-fixed | Security |
| #26829 | Inspired by Claude Code: tighten dangerous-command detection | Security |
| #26825 | feat: add supports_parallel_tool_calls for MCP servers | MCP |
| #26824 | fix(delegation): honor api_mode + auto-detect anthropic_messages | Delegation |
| #26823 | security: sanitize tool error strings before injecting | Security |

### Key Themes
- **ACP (Agent Communication Protocol)** — session replay and chunking improvements
- **Security hardening** — OAuth PKCE, dangerous command detection, error sanitization, path/directory traversal prevention
- **MCP enhancements** — parallel tool calls support
- **New feature: Kanban file attachments** — tasks can have file attachments
- **CLI perf: MCP discovery** — no longer blocks agent-capable startup

---

## 4. Claude Code Recommended Actions

### Priority 1 — Review local vs upstream divergence
Local worktree is **146 commits ahead** of `origin/main`. This is unusual — this worktree has been used for development on features not yet upstreamed.

```bash
cd ~/wiki/tech-debt/github/hermes-agent
git log --oneline HEAD..origin/main | head -20   # what's new upstream?
git log --oneline origin/main..HEAD | head -20   # what's local-only?
```

### Priority 2 — New upstream tags detected
New tags this cycle: `v2026.5.28`, `v2026.5.29`, `v2026.5.29.1`, `v2026.5.29.2`
Latest release: `v0.14.0 (2026.5.16)` — newer tags may be hotfixes or desktop release artifacts.

### Priority 3 — Test managed-gateway fix
The fix (`6a72af044`) keeps tool availability scans off the token-refresh path. If using gateway with Nous API token, verify tool listing still works correctly.

### Priority 4 — Run test suite after any sync
The ACP session replay PRs (#26957, #26943) modify core session loading:
```bash
cd ~/wiki/tech-debt/github/hermes-agent
source .venv/bin/activate && scripts/run_tests.sh
```

---

## 5. Local State Summary

| Field | Value |
|---|---|
| Local commit | `c5b4c4816` (fix: lazy session creation) |
| Local tag | `v2026.4.30-146-gc5b4c4816` |
| Upstream | `origin/main` at `6a72af044` |
| Relationship | **Local is 146 commits AHEAD** |
| New upstream tags | v2026.5.28, v2026.5.29, v2026.5.29.1, v2026.5.29.2 |
| In sync | No — local is ahead, not behind |

---

## 6. Action Log

- **2026-05-30:** Fetched origin — new branches/tags found. Local is 146 commits ahead of upstream. `hermes update` timed out (120s). `hermes skills update` → no updates.
- **Note:** Last cycle (2026-05-16) reported 1584 commits behind — local has been rebased or history rewritten since then
# Graphify — Weekly Technical Update RFC

**Date:** 2026-06-13 (Saturday)
**Status:** Behind upstream — 63 commits behind `origin/v6`. No code-action PRs required this week (no audit-failures to remediate); just a tracking + dependency watch entry.

---

## 1. Repository State

**Local clone:** `~/wiki/tech-debt/github/graphify`
**Remote:** `https://github.com/safishamsi/graphify.git` (origin)
**Branch:** `v6` ←→ `origin/v6`
**Latest local HEAD:** `8a6306f` — make .graphifyignore hermetic: stop at VCS root, not project boundaries (closes #643)
**Latest upstream tag (new this week):** `v0.8.39`
**Ahead/behind:** `0` / `63` (unchanged from 2026-05-30 RFC)

> The "63 commits behind" figure is the local-vs-upstream gap on `v6`; upstream has been tagging fast (v0.8.21 → v0.8.39 since the last RFC).

### New upstream tags since last RFC (2026-05-30)

`v0.8.21 → v0.8.30` and `v0.8.31 → v0.8.39` — patch releases (high cadence consistent with a 0.x project under active development).

---

## 2. Dependency Status

**Managed via:** `pyproject.toml` (uv/pip, setuptools backend)
**No `package.json` or `requirements.txt`**

### Core dependencies (from `pyproject.toml`)

| Dependency | Constraint | Notes |
|---|---|---|
| `networkx` | unpinned | No upper bound — supply-chain risk |
| `tree-sitter` | `>=0.23.0` | No upper bound |
| 23 `tree-sitter-*[lang]` packages | unpinned | High supply-chain surface area |

### Optional extras (subset)

`mcp`, `neo4j`, `pdf` (pypdf, html2text), `watch` (watchdog), `svg` (matplotlib), `leiden` (graspologic, `py<3.13` only), `office` (python-docx, openpyxl), `video` (faster-whisper, yt-dlp), `kimi` (openai), `sql` (tree-sitter-sql)

### Local venv health (uv pip list --outdated, 2026-06-13)

The repo shares the *Hermes Agent* venv at `~/.hermes/hermes-agent/venv`; the `uv pip list --outdated` snapshot is dominated by Hermes dependencies, not graphify ones. Notable *relevant* items:

| Package | Installed | Latest | Note |
|---|---|---|---|
| `anthropic` | 0.87.0 | 0.109.1 | bump available; not a graphify dep |
| `cryptography` | 46.0.7 | 49.0.0 | bump available; security-relevant |
| `aiohttp` | 3.13.4 | 3.14.1 | bump available |
| `croniter` | 6.0.0 | 6.2.2 | bump available |

These are the *environment's* outdated packages, not graphify-specific. The graphify venv shares the same interpreter, so they would also affect a graphify run.

### Observations

- **No upper bounds** on `networkx` or `tree-sitter` — supply-chain risk unchanged from prior RFC
- `graspologic` has `python_version < '3.13'` constraint — should be tested on Python 3.13+ for the leiden extra
- 23 tree-sitter language grammars = high attack surface; consider a `pip-audit` step in CI
- **No new direct graphify dep changes observed** in upstream v0.8.21..v0.8.39 commits captured by `git fetch` (cosmetic: README, doc-only)

---

## 3. CI/CD Health

**Cannot query via GitHub API** — no `gh` token in this environment. Run manually on a workstation with auth:

```bash
gh pr list --state merged --repo safishamsi/graphify --limit 10
gh run list --repo safishamsi/graphify --limit 5
```

### From local `git fetch` (10 newest upstream commits not in local)

```
f81e3bc bump version to 0.6.9
8e81720 Fix #686 #652: GRAPHIFY_OUT env var for worktrees, Antigravity install auto-updates rules/workflow
6df69dc Fix #683: normalize source_file path separators + two-phase cohesion re-clustering
f61bb27 Fix #688: stricter VS Code Copilot instructions to enforce GRAPH_REPORT.md first
de268a0 fix Penpax waitlist link to graphifylabs.ai
b11a8a7 simplify README, move technical details to docs/how-it-works.md
d753413 bump version to 0.6.8
f065933 Fix #676 #678 #681: graphifyignore negation, Antigravity slash command, Gemini hook Windows
893acb1 Fix #664: filter thin communities from GRAPH_REPORT.md by default
96267ad fix #651: resolve absolute graphify path at codex install time for VS Code extension on Windows
```

Themes: cross-platform fixes (Windows paths, Antigravity/Gemini hooks), bug fixes (path normalization, community filtering), README/grammar cleanup, parallel-AST perf (PR #663, 1.66x speedup — already in last RFC).

---

## 4. Recently Merged PRs (v0.6.9..v0.8.39 tag range, locally visible)

> Locally visible commits are capped at the 10 returned by `git fetch`. Full PR list requires `gh` (see §3).

| Theme | Count | Details |
|---|---|---|
| **Performance** | 1 (prev) | Parallel AST extraction via ProcessPoolExecutor (#663) — 1.66x on 84 files |
| **Cross-platform** | 4 (prev) | Antigravity Windows fix, Gemini hook Windows fix, graphifyignore negation, VS Code Copilot stricter rules |
| **Bug fixes** | 5 (prev) +1 (this batch) | source_file path separator normalization, cohesion re-clustering, thin community filtering, Codex install path resolution, **GRAPHIFY_OUT env var for worktrees (#686/#652)** |
| **Docs/UX** | 2 | README simplification (move to `docs/how-it-works.md`), Penpax waitlist link fix |

---

## 5. Security Advisory Status

- No `pip-audit` output captured this cycle. Recommend running `pip-audit` in CI on the optional extras (`mcp`, `neo4j`, `leiden`, `video`).
- `cryptography` 46.0.7 → 49.0.0 is a notable bump in the shared venv; check CVE feed before any upgrade.

---

## 6. Claude Code Recommended Actions

1. **No code action required this week** — no new CVEs, no audit failures, no new upstream breaking changes captured locally. The local branch is informational-only.
2. **If syncing to upstream:** `cd ~/wiki/tech-debt/github/graphify && git pull --ff-only origin v6` then re-run `uv pip install -e .` and exercise the leiden extra on Python 3.13 to confirm the `py<3.13` constraint still holds.
3. **Supply-chain hardening (next RFC):** add explicit upper bounds on `networkx`, `tree-sitter`, and the tree-sitter language grammars in `pyproject.toml`; pin them via `~=` for minor.
4. **CI suggestion (next RFC):** add a `pip-audit` step in the upstream `.github/workflows/` to catch advisories in the 23 grammar deps.

---

## 7. Action Log

- **2026-05-30:** Initial RFC — 63 commits behind, no actions.
- **2026-06-13:** Re-audit — still 63 commits behind (no fast-forward pulled locally). Upstream tag range advanced v0.8.21 → v0.8.39. No remediation work triggered. `gh` not available; PR/CI queries deferred.

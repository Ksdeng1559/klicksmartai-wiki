# Skill Collision Diagnostic — Wiki Skills + Hermes Loader

When a wiki-scoped skill (e.g. `/home/denni/wiki/hermes/skills/icm-client-workspace-setup/`) is also discoverable via `~/.hermes/skills/<name>/`, the loader picks **one copy** (usually the shorter / stale one) and silently truncates the canonical. The agent sees a 515-char skill instead of the real 17,000-char one, runs with partial context, and the failure is invisible.

This file documents the diagnostic, the root cause, and the recovery procedure.

---

## Symptom

`skill_view(name=<name>)` returns a much shorter content than the file on disk:

```
skill_view(name="icm-client-workspace-setup")
→ name=icm-client-workspace-setup (515 chars) [SKILL_PRUNED...]
```

But the actual file:

```bash
$ wc -c /home/denni/wiki/hermes/skills/icm-client-workspace-setup/SKILL.md
21782 /home/denni/wiki/hermes/skills/icm-client-workspace-setup/SKILL.md
```

If `chars` from `skill_view` is dramatically smaller than `wc -c` (or `wc -m` for markdown), you have a duplicate-load problem.

---

## Root cause

Hermes's `_find_all_skills` in `/home/denni/.hermes/hermes-agent/hermes_cli/skills_config.py` enumerates skills from two sources:

1. `~/.hermes/skills/` — the user-level skill home
2. `skills.external_dirs` from `~/.hermes/config.yaml` — explicitly added paths

When the **same skill name** appears in both, the loader does NOT error. It silently picks one copy — typically the one discovered first in the iteration order — and discards the other. The chosen copy may be:

- A stale copy from a previous session (before recent SKILL.md edits)
- A stub version (the `~/.claude/skills/`-style minimal SKILL.md)
- A partial export from a prior mirroring attempt

The user-level copy wins more often than not because it's discovered first in the iteration.

---

## Diagnostic command

```bash
# 1. find every copy of the skill on disk
find / -type d -name '<skill-name>' 2>/dev/null | grep -v '\.pyc\|node_modules\|__pycache__'

# 2. compare file sizes
for d in $(find / -type d -name '<skill-name>' 2>/dev/null | grep -v '\.pyc\|node_modules\|__pycache__'); do
  echo "$d: $(wc -c < "$d/SKILL.md" 2>/dev/null || echo MISSING) bytes"
done

# 3. compare frontmatter (name + description should match for true duplicates)
for d in $(find / -type d -name '<skill-name>' 2>/dev/null | grep -v '\.pyc\|node_modules\|__pycache__'); do
  echo "--- $d ---"
  awk '/^---$/{c++} c==1' "$d/SKILL.md" 2>/dev/null | head -10
done
```

The duplicate is whichever copy is **NOT** at the canonical location.

---

## Canonical locations (KlickSmartAI convention)

| Skill class | Canonical location | Mirror to | Never both |
|-------------|-------------------|-----------|------------|
| Wiki / client-workspace skills | `/home/denni/wiki/hermes/skills/<name>/` | (none — wiki is canonical, discovered via `external_dirs`) | **NEVER** also create `~/.hermes/skills/<name>/` |
| Claude Code–native skills | `~/.claude/skills/<name>/` | (none — Claude stub is canonical) | (Hermes loads wiki; Claude loads its own stub) |
| Hermes-bundled skills | bundled in Hermes | n/a | bundled — not user-editable |
| Hub-installed skills | `~/.hermes/skills/<name>/` | n/a | (one home — `~/.hermes/skills/`) |

The rule is **one canonical home per skill name**. Pick the path that matches where the skill will be authored / version-controlled / found by both ecosystems.

---

## Recovery procedure

If you've hit the collision and `skill_view` is returning truncated content:

```bash
# Step 1 — identify the non-canonical copy
find / -type d -name '<skill-name>' 2>/dev/null | grep -v '\.pyc\|node_modules\|__pycache__'

# Step 2 — remove the duplicate. For wiki skills, that's the user-level copy:
rm -rf ~/.hermes/skills/<skill-name>

# Step 3 — verify discovery still works via external_dirs
~/.hermes/hermes-agent/venv/bin/hermes skills list | grep <skill-name>

# Step 4 — verify skill_view returns the full content
skill_view(name='<skill-name>')
# should show name=... (17000+ chars) — NOT 515 chars
```

If you removed the wiki copy by mistake and need to recover:

```bash
# (the wiki is git-tracked, so just pull it back)
cd /home/denni/wiki
git checkout -- hermes/skills/<skill-name>/
```

---

## Prevention checklist

When publishing a new wiki-scoped skill:

1. Write `SKILL.md` + `references/*` to `/home/denni/wiki/hermes/skills/<name>/`.
2. Register the path: `hermes config set skills.external_dirs '["/home/denni/wiki/hermes/skills"]' --force` (idempotent — won't duplicate).
3. **Verify no user-level copy exists:** `test -d ~/.hermes/skills/<name> && echo WARNING: will collide`.
4. **Verify discovery:** `hermes skills list | grep <name>`.
5. **Verify content size:** `skill_view(name='<name>')` should return `name=... (17000+ chars)`.

If `~/.hermes/skills/<name>/` exists for any reason (leftover from a previous harness, manual copy from a tarball, etc.), DELETE IT before the skill will work.

---

## Related

- `~/.hermes/hermes-agent/hermes_cli/skills_config.py` — the loader, `_find_all_skills()` function
- `~/.hermes/config.yaml` — `skills.external_dirs` configuration block
- The skill's pitfall #7 — the high-level summary; this file is the deep dive
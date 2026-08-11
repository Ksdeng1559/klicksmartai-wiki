---
title: Terminal Lifecycle Guard
created: 2026-08-11
updated: 2026-08-11
type: gotcha
tags: [gotcha, terminal, python, hermes-agent, lifecycle]
sources: []
confidence: high
---

# Terminal Lifecycle Guard

A specific failure mode where `terminal()` calls crash with `os.open ValueError`
during Hermes's lifecycle guard check. Affects only certain kinds of shell
input.

## Symptom
- `terminal(command="python3 -c '...'" ...)` or any heredoc / script-file
  input crashes.
- Root cause: CPython issue #76762 — `os.open()` returns ValueError in some
  interpreter builds when heredoc-style redirection is involved.

## Workaround
For ANY Python execution:
1. Use the hermes-agent venv at `~/.hermes/hermes-agent/venv/bin/python`
   (NOT `python3` from PATH).
2. Set `PYTHONPATH=~/.hermes/hermes-agent` so hermes modules import.
3. Write the script to a file with `write_file`, then run it.
4. **Don't** use heredocs in `terminal()` (e.g. `python3 <<EOF ... EOF`).

## Example
```bash
# RIGHT
~/.hermes/hermes-agent/venv/bin/python /tmp/script.py

# WRONG (will crash with ValueError)
python3 <<EOF
import os
...
EOF
```

## When in doubt
Use `execute_code` instead — it calls hermes_tools programmatically and
bypasses the shell. Useful when the failure is the lifecycle_guard rather
than your code.

## See also
- [[Hermes-Environment-Map]]
- [[Execute-Code-vs-Terminal]]
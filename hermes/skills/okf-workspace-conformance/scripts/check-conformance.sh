#!/usr/bin/env bash
# OKF v0.2 conformance check (OKF §11)
#
# Walks a bundle root and verifies every .md file has parseable YAML
# frontmatter with a non-empty `type:` field. Reserved filenames
# (index.md, log.md) and a configurable exception list are skipped.
#
# Usage:
#   check-conformance.sh <bundle-root> [--exceptions=f1,f2,...]
#
# Exit codes:
#   0 — fully conformant
#   1 — violations found (printed to stdout)
#   2 — usage error
#
# Author: KlickSmartAI / 2026-08-29
# Spec:   https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <bundle-root> [--exceptions=f1,f2,...]" >&2
  exit 2
fi

ROOT="$1"
EXCEPTIONS="CLAUDE.md"

# Parse --exceptions=...
for arg in "$@"; do
  case "$arg" in
    --exceptions=*) EXCEPTIONS="${arg#--exceptions=}" ;;
  esac
done

if [[ ! -d "$ROOT" ]]; then
  echo "ERROR: bundle root not found: $ROOT" >&2
  exit 2
fi

# Parse exceptions into bash array
IFS=',' read -ra EX_ARR <<< "$EXCEPTIONS"

total=0
missing_fm=0
missing_type=0
except_count=0
violations=()

while IFS= read -r -d '' f; do
  total=$((total + 1))
  basename="$(basename "$f")"

  # Reserved filenames always skipped (OKF §8/§9)
  if [[ "$basename" == "index.md" || "$basename" == "log.md" ]]; then
    except_count=$((except_count + 1))
    continue
  fi

  # Check exception list
  is_exception=0
  for ex in "${EX_ARR[@]}"; do
    ex_trimmed="$(echo "$ex" | xargs)"
    [[ "$basename" == "$ex_trimmed" ]] && { is_exception=1; break; }
  done
  if [[ $is_exception -eq 1 ]]; then
    except_count=$((except_count + 1))
    continue
  fi

  first_line="$(head -n1 "$f")"
  if [[ "$first_line" != "---" ]]; then
    missing_fm=$((missing_fm + 1))
    violations+=("MISSING-FRONTMATTER: $f")
    continue
  fi

  # Bound type check to frontmatter block (between first two `---` markers).
  # Use awk: track fence count, exit on second fence.
  has_type=$(awk '
    BEGIN { fence = 0 }
    /^---$/ {
      fence++
      if (fence == 2) { exit }
      next
    }
    fence == 1 {
      if ($0 ~ /^type:[[:space:]]*[^[:space:]]+/) { print "YES"; exit }
    }
  ' "$f")

  if [[ "$has_type" != "YES" ]]; then
    missing_type=$((missing_type + 1))
    violations+=("MISSING-type: $f")
  fi
done < <(find "$ROOT" -name '*.md' -type f -print0)

# Report
echo "=== OKF conformance check ==="
echo "Bundle root: $ROOT"
echo "Exceptions:  $EXCEPTIONS"
echo ""
echo "TOTAL: $total | Missing-FM: $missing_fm | Missing-type: $missing_type | Excluded: $except_count"

if [[ ${#violations[@]} -gt 0 ]]; then
  echo ""
  echo "Violations:"
  for v in "${violations[@]}"; do
    echo "  $v"
  done
  echo ""
  echo "❌ NOT fully conformant"
  exit 1
fi

echo ""
echo "✅ OKF CONFORMANT: $ROOT"
exit 0

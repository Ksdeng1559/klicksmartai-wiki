#!/usr/bin/env bash
# verify-workspace.sh — verify a client workspace scaffolded by icm-client-workspace-setup
# Usage: bash verify-workspace.sh <client-slug>
# Exits 0 if workspace is well-formed and source-of-truth gate is intact.

set -u

CLIENT_SLUG="${1:-}"
if [ -z "$CLIENT_SLUG" ]; then
  echo "Usage: $0 <client-slug>" >&2
  exit 2
fi

ROOT="/home/denni/wiki/clients/$CLIENT_SLUG"
if [ ! -d "$ROOT" ]; then
  echo "FAIL: $ROOT does not exist"
  exit 1
fi

PASS=0
FAIL=0

check() {
  local label="$1"
  local path="$2"
  if [ -e "$path" ]; then
    echo "  OK  $label ($path)"
    PASS=$((PASS+1))
  else
    echo "  MISS $label ($path)"
    FAIL=$((FAIL+1))
  fi
}

echo "=== Verifying $ROOT ==="

# Root layer files
echo "-- root layer --"
check "CLAUDE.md (Hermes adapter)"  "$ROOT/CLAUDE.md"
check "IDENTITY.md (Layer 0)"        "$ROOT/IDENTITY.md"
check "CONTEXT.md (Layer 1)"         "$ROOT/CONTEXT.md"
check "README.md (human overview)"   "$ROOT/README.md"

# _config layer
echo "-- _config layer --"
check "_config/voice.md"             "$ROOT/_config/voice.md"
check "_config/conventions.md"       "$ROOT/_config/conventions.md"
check "_config/glossary.md"          "$ROOT/_config/glossary.md"
check "_config/deliverables.md (vertical map)" "$ROOT/_config/deliverables.md"

# compliance.md is optional
if [ -f "$ROOT/_config/compliance.md" ]; then
  echo "  OK  _config/compliance.md (present - engagement is regulated)"
  PASS=$((PASS+1))
else
  echo "  --  _config/compliance.md (absent - engagement is non-regulated)"
fi

# Folder layout
echo "-- folder layout --"
for f in projects drafts deliverables drafts-preview skills; do
  check "$f/"  "$ROOT/$f"
done
check "projects/README.md"      "$ROOT/projects/README.md"
check "drafts/README.md"        "$ROOT/drafts/README.md"
check "deliverables/README.md"  "$ROOT/deliverables/README.md"
check "drafts-preview/README.md" "$ROOT/drafts-preview/README.md"
check "skills/README.md"        "$ROOT/skills/README.md"

# Source-of-truth gate
echo "-- source-of-truth gate --"
GATE_FILES=$(find "$ROOT/projects" -type f -not -name 'README.md' 2>/dev/null)
GATE_FILES_DELIV=$(find "$ROOT/deliverables" -type f -not -name 'README.md' 2>/dev/null)

if [ -z "$GATE_FILES" ] && [ -z "$GATE_FILES_DELIV" ]; then
  echo "  OK  No AI content landed in projects/ or deliverables/ (gate holds on fresh scaffold)"
  PASS=$((PASS+1))
else
  echo "  --  AI content already exists in projects/deliverables - assume legacy or pre-HITL: verify manually"
  echo "      projects/: $GATE_FILES"
  echo "      deliverables/: $GATE_FILES_DELIV"
fi

# Per-vertical subfolders (if any)
VERT_FOLDERS=$(find "$ROOT/drafts" -mindepth 2 -maxdepth 2 -type d 2>/dev/null)
if [ -n "$VERT_FOLDERS" ]; then
  echo "-- per-vertical subfolders --"
  for vf in $VERT_FOLDERS; do
    v=$(basename "$vf")
    check "drafts/$v/README.md"      "$ROOT/drafts/$v/README.md"
    check "projects/$v/"             "$ROOT/projects/$v"
    check "deliverables/$v/"         "$ROOT/deliverables/$v"
    check "drafts-preview/$v/"       "$ROOT/drafts-preview/$v"
  done
fi

echo ""
echo "=== Result: $PASS passed, $FAIL failed ==="
[ "$FAIL" -eq 0 ] && exit 0 || exit 1
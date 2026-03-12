#!/bin/bash
# Export reasoningtool skills to another project's .claude/commands/ directory.
# Usage: ./scripts/export-skills.sh /path/to/target/project [skill1 skill2 ...]
# If no skills specified, exports all skills.

set -euo pipefail

REASONINGTOOL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="$REASONINGTOOL_DIR/claude-code-plugin/skills"
COMMANDS_DIR="$REASONINGTOOL_DIR/.claude/commands"

TARGET_PROJECT="${1:?Usage: export-skills.sh /path/to/target/project [skill1 skill2 ...]}"
shift

TARGET_COMMANDS="$TARGET_PROJECT/.claude/commands"
mkdir -p "$TARGET_COMMANDS"

# If specific skills given, use those. Otherwise export all.
if [ $# -gt 0 ]; then
  SKILLS=("$@")
else
  SKILLS=()
  for cmd in "$COMMANDS_DIR"/*.md; do
    name="$(basename "$cmd" .md)"
    SKILLS+=("$name")
  done
fi

count=0
for skill in "${SKILLS[@]}"; do
  src="$COMMANDS_DIR/$skill.md"
  if [ ! -f "$src" ]; then
    echo "SKIP: $skill (no command stub found)"
    continue
  fi

  # Read the original stub and rewrite the relative path to absolute
  stub=$(cat "$src")
  # Replace relative claude-code-plugin path with absolute path
  rewritten=$(echo "$stub" | sed "s|claude-code-plugin/skills/|$REASONINGTOOL_DIR/claude-code-plugin/skills/|g")

  echo "$rewritten" > "$TARGET_COMMANDS/$skill.md"
  count=$((count + 1))
done

echo "Exported $count skills to $TARGET_COMMANDS"

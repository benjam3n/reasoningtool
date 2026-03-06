#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Install reasoningtool skills into Codex.

Usage:
  scripts/install_codex_skills.sh [--copy] [--force] [--code-home PATH]

Options:
  --copy            Copy skill folders instead of symlinking them.
  --force           Replace existing installed skill folders.
  --code-home PATH  Install into PATH/skills instead of $CODEX_HOME/skills.

Notes:
  - Default mode is symlink, which keeps the Codex install in sync with this repo.
  - Skills are installed with their original IDs because skills invoke each other
    by those names (for example /claim -> /araw).
EOF
}

MODE="symlink"
FORCE="false"
CODE_HOME="${CODEX_HOME:-$HOME/.codex}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --copy)
      MODE="copy"
      shift
      ;;
    --force)
      FORCE="true"
      shift
      ;;
    --code-home)
      if [[ $# -lt 2 ]]; then
        echo "--code-home requires a path" >&2
        exit 1
      fi
      CODE_HOME="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SOURCE_DIR="$REPO_ROOT/claude-code-plugin/skills"
TARGET_DIR="$CODE_HOME/skills"

if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "Skills source directory not found: $SOURCE_DIR" >&2
  exit 1
fi

mkdir -p "$TARGET_DIR"

installed=0
skipped=0

for skill_path in "$SOURCE_DIR"/*; do
  [[ -d "$skill_path" ]] || continue

  skill_id="$(basename "$skill_path")"
  dest="$TARGET_DIR/$skill_id"

  if [[ -e "$dest" || -L "$dest" ]]; then
    if [[ "$FORCE" == "true" ]]; then
      rm -rf "$dest"
    else
      echo "Skipping existing skill: $skill_id"
      skipped=$((skipped + 1))
      continue
    fi
  fi

  if [[ "$MODE" == "copy" ]]; then
    cp -R "$skill_path" "$dest"
  else
    ln -s "$skill_path" "$dest"
  fi

  installed=$((installed + 1))
done

echo "Installed $installed skills into $TARGET_DIR"
if [[ "$skipped" -gt 0 ]]; then
  echo "Skipped $skipped existing skills"
fi

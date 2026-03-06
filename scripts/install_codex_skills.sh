#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Install reasoningtool skills into Codex.

Usage:
  scripts/install_codex_skills.sh [--copy|--symlink] [--force] [--code-home PATH]

Options:
  --copy            Copy skill folders (default).
  --symlink         Symlink skill folders (no Codex syntax adaptation).
  --force           Replace existing installed skill folders.
  --code-home PATH  Install into PATH/skills instead of $CODEX_HOME/skills.

Notes:
  - Copy mode rewrites Claude-style invoke syntax to Codex-style invoke syntax:
    "INVOKE: /skill" -> "INVOKE: $skill"
  - Skills are installed with original IDs because skills invoke each other
    by those names.
EOF
}

MODE="copy"
FORCE="false"
CODE_HOME="${CODEX_HOME:-$HOME/.codex}"

prepend_after_frontmatter() {
  local override_file="$1"
  local target_file="$2"
  local tmp_file
  tmp_file="$(mktemp)"

  awk -v ov="$override_file" '
    BEGIN { fm = 0; inserted = 0 }
    NR == 1 && $0 == "---" { fm = 1; print; next }
    fm == 1 && $0 == "---" {
      print
      while ((getline line < ov) > 0) print line
      close(ov)
      inserted = 1
      fm = 2
      next
    }
    { print }
    END {
      if (inserted == 0) {
        while ((getline line < ov) > 0) print line
        close(ov)
      }
    }
  ' "$target_file" > "$tmp_file"

  mv "$tmp_file" "$target_file"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --copy)
      MODE="copy"
      shift
      ;;
    --symlink)
      MODE="symlink"
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
CODEX_OVERRIDES_DIR="$REPO_ROOT/codex-overrides"
ROUTER_SKILLS="claim decide diagnose evaluate search how want emotion analyze viability action create technical certainty iterate meta"

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

    # Adapt Claude command syntax to Codex explicit skill syntax.
    if [[ -f "$dest/SKILL.md" ]]; then
      perl -0pi -e 's/INVOKE:\s*\/([A-Za-z0-9._-]+)/INVOKE: \$$1/g' "$dest/SKILL.md"
      perl -0pi -e 's/\$ARGUMENTS/USER_INPUT/g' "$dest/SKILL.md"
    fi

    # Apply Codex-specific strict override for ARAW.
    if [[ "$skill_id" == "araw" && -f "$CODEX_OVERRIDES_DIR/araw_strict_codex.md" ]]; then
      prepend_after_frontmatter "$CODEX_OVERRIDES_DIR/araw_strict_codex.md" "$dest/SKILL.md"
    fi

    # Apply Codex-specific strict override for UAUA.
    if [[ "$skill_id" == "uaua" && -f "$CODEX_OVERRIDES_DIR/uaua_strict_codex.md" ]]; then
      prepend_after_frontmatter "$CODEX_OVERRIDES_DIR/uaua_strict_codex.md" "$dest/SKILL.md"
    fi

    # Apply Codex-specific strict override for router skills.
    for router_skill in $ROUTER_SKILLS; do
      if [[ "$skill_id" == "$router_skill" && -f "$CODEX_OVERRIDES_DIR/router_strict_codex.md" ]]; then
        prepend_after_frontmatter "$CODEX_OVERRIDES_DIR/router_strict_codex.md" "$dest/SKILL.md"
        break
      fi
    done
  else
    ln -s "$skill_path" "$dest"
  fi

  installed=$((installed + 1))
done

echo "Installed $installed skills into $TARGET_DIR"
if [[ "$skipped" -gt 0 ]]; then
  echo "Skipped $skipped existing skills"
fi

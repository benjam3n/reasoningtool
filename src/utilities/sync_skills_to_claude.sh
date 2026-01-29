#!/bin/bash
# Sync GOSM skills to Claude Code's skill directory
# Run this when you add new skills to claude-code-plugin/skills/

GOSM_SKILLS="/home/ben/Documents/projects/GOSM/claude-code-plugin/skills"
CLAUDE_SKILLS="/home/ben/Documents/projects/GOSM/.claude/skills"

# Create Claude skills directory if it doesn't exist
mkdir -p "$CLAUDE_SKILLS"

# Count for reporting
linked=0
skipped=0

# Loop through all skill directories
for skill_dir in "$GOSM_SKILLS"/*/; do
    skill_name=$(basename "$skill_dir")

    # Skip if SKILL.md doesn't exist
    if [[ ! -f "$skill_dir/SKILL.md" ]]; then
        continue
    fi

    target="$CLAUDE_SKILLS/$skill_name"

    # Skip if already linked
    if [[ -L "$target" ]]; then
        ((skipped++))
        continue
    fi

    # Remove if exists but not a symlink
    if [[ -e "$target" ]]; then
        rm -rf "$target"
    fi

    # Create symlink
    ln -s "$skill_dir" "$target"
    echo "Linked: $skill_name"
    ((linked++))
done

echo ""
echo "Done. Linked: $linked, Already linked: $skipped"
echo "Skills available at: $CLAUDE_SKILLS"

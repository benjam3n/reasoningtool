#!/bin/bash
# Sync skills to Claude Code's commands directory
# Run this when you add new skills to claude-code-plugin/skills/

SKILLS_DIR="/home/ben/Documents/projects/reasoningtool/claude-code-plugin/skills"
COMMANDS_DIR="/home/ben/Documents/projects/reasoningtool/.claude/commands"

mkdir -p "$COMMANDS_DIR"

added=0
skipped=0

for skill_dir in "$SKILLS_DIR"/*/; do
    skill_name=$(basename "$skill_dir")
    skill_md="$skill_dir/SKILL.md"
    cmd_file="$COMMANDS_DIR/${skill_name}.md"

    # Skip if SKILL.md doesn't exist
    if [[ ! -f "$skill_md" ]]; then
        continue
    fi

    # Skip if command already exists
    if [[ -f "$cmd_file" ]]; then
        ((skipped++))
        continue
    fi

    # Extract description from frontmatter
    desc=$(sed -n '/^---$/,/^---$/p' "$skill_md" | grep '^description:' | sed 's/^description:\s*//' | sed 's/^"//' | sed 's/"$//')
    if [[ -z "$desc" ]]; then
        desc="Run the $skill_name skill"
    fi

    echo "${desc} Read and execute \`claude-code-plugin/skills/${skill_name}/SKILL.md\`, applying it to this input: \$ARGUMENTS" > "$cmd_file"
    echo "Added: $skill_name"
    ((added++))
done

echo ""
echo "Done. Added: $added, Already existed: $skipped"
echo "Total commands: $(ls "$COMMANDS_DIR"/*.md 2>/dev/null | wc -l)"

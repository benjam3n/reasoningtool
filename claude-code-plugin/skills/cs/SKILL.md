---
name: "cs - Create Skill"
description: Create or update a skill from a prompt, including naming, scope, workflow, and output contract. Can also identify missing skills implied by the prompt.
---

# CS - Create Skill

**Input**: $ARGUMENTS

---

## Modes

- CREATE: make a new skill.
- UPDATE: improve an existing skill.
- GAP_SCAN: identify skills that should exist but do not.

## Steps

1. Parse prompt intent and target use case.
2. Determine mode (CREATE / UPDATE / GAP_SCAN).
3. For CREATE/UPDATE, define: id, purpose, steps, output format, boundaries.
4. For GAP_SCAN, list missing-skill candidates with rationale and priority.
5. Produce concrete SKILL.md-ready output.

## Output

- For CREATE/UPDATE: skill spec with frontmatter and body outline.
- For GAP_SCAN: ordered missing-skill list with suggested ids.

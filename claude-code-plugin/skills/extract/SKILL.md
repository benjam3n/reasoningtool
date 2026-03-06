---
name: "extract - Skill Extractor"
description: Given any prompt, extract every potentially useful existing skill, grouped and prioritized with invocation-ready suggestions.
---

# Extract - Skill Extractor

**Input**: $ARGUMENTS

---

## Steps

1. Parse prompt into sub-needs.
2. Map each sub-need to candidate existing skills.
3. Remove weak matches.
4. Return prioritized skill set with short why.
5. Provide invocation examples.

## Output

```text
PROMPT: ...
USEFUL_SKILLS_ORDERED:
1. /skill-id - WHY: ... - INVOKE: ...
2. /skill-id - WHY: ... - INVOKE: ...
MAYBE_SKILLS:
- /skill-id - WHY: ...
```

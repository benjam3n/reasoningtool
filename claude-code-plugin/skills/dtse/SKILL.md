---
name: "dtse - Does This Skill Exist"
description: Check whether a requested skill exists, show exact matches and nearest alternatives, and provide next action.
---

# DTSE - Does This Skill Exist

**Input**: $ARGUMENTS

---

## Steps

1. Parse candidate skill id or name.
2. Check exact existence.
3. If missing, return nearest matches.
4. If missing and needed, route to creation.

## Output Format

```text
REQUESTED_SKILL: ...
EXISTS: YES | NO
EXACT_MATCH: /skill-id (if exists)
NEAREST_MATCHES:
- /skill-id - why similar
NEXT_ACTION: /wsib or /cs
```

---
name: "wsib - What Skill Is Best"
description: Choose the best skill to run now for a prompt, with confidence, runner-up comparison, and fallback if first choice fails.
---

# WSIB - What Skill Is Best

**Input**: $ARGUMENTS

---

## Steps

1. Parse the prompt into intent and immediate objective.
2. Generate top candidate skills.
3. Select BEST_NOW skill.
4. Select RUNNER_UP skill.
5. Provide fallback route if BEST_NOW fails.

## Output Format

```text
BEST_NOW: /skill-id
CONFIDENCE: HIGH | MEDIUM | LOW
WHY_BEST: ...
WHY_NOT_RUNNER_UP: ...
RUNNER_UP: /skill-id
FALLBACK_IF_FAILS: /skill-id
INVOKE: /skill-id [prompt]
```

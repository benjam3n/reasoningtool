---
name: "fonss - Figure Out Next Skills"
description: Determine which skills to run next (more than one), in order, with rationale, handoff prompts, and stop conditions.
---

# FONSS - Figure Out Next Skills

**Input**: $ARGUMENTS

---

## Purpose

Recommend the next sequence of skills, not just one, based on current state and blockers.

## Steps

### 1. Extract State

Identify:
- CURRENT_GOAL
- DONE_SO_FAR
- BLOCKERS
- DECISION_POINTS

### 2. Build Candidate Skill Set

Select plausible skills for the next step.
Prefer routers only when classification is uncertain.
Prefer concrete skills when the task type is clear.

### 3. Score Candidate Skills

Score each candidate on:
- expected progress unlocked now
- risk reduction
- dependency fit
- execution readiness

### 4. Sequence Skills

Produce an ordered chain.
Each skill must include why it comes before the next one.

### 5. Add Handoffs

For each skill provide:
- INVOCATION
- EXPECTED_OUTPUT
- STOP_CONDITION

---

## Output Format

```text
CURRENT_GOAL: ...

NEXT_SKILLS_ORDERED:
1. /skill-id
   WHY_NOW: ...
   INVOCATION: ...
   EXPECTED_OUTPUT: ...
   STOP_CONDITION: ...
2. /skill-id
   WHY_NOW: ...
   INVOCATION: ...
   EXPECTED_OUTPUT: ...
   STOP_CONDITION: ...
...
```

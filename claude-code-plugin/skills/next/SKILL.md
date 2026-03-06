---
name: "next - Determine What to Do Next"
description: Sub-orchestrator for next-step requests. Selects the highest-value immediate action from current context, then routes to execution or the right analysis skill.
---

# Next

**Input**: $ARGUMENTS

---

## Routing Decisions

### 1. Extract Current State

State what is already known and what is blocked.

- What was already done?
- What is unresolved?
- What immediate action candidate is visible?

### 2. Is This Actually a Next-Step Request?

- **"Should I X?"** -> This is a decision. -> INVOKE: /decide $ARGUMENTS
- **"How do I X?"** -> This is method-seeking. -> INVOKE: /how $ARGUMENTS
- **"Why is X happening?"** -> This is diagnostic. -> INVOKE: /diagnose $ARGUMENTS
- **"What are my options?"** -> This is exploration. -> INVOKE: /search $ARGUMENTS
- **"I want X"** -> This is goal clarification. -> INVOKE: /want $ARGUMENTS
- **If it IS a next-step request** -> continue.

### 3. Context Completeness Check

- **Clear context**: known goal + known current state + known blocker.
- **Partial context**: known goal but unclear blocker.
  -> INVOKE: /diagnose $ARGUMENTS
- **Insufficient context**: unclear goal or no current state.
  -> INVOKE: /want $ARGUMENTS

### 4. Choose Next-Step Type

| Situation | Route |
|-----------|-------|
| Concrete task is obvious now | -> /action |
| Need method before acting | -> /how |
| Need evaluation before acting | -> /evaluate |
| Need decision before acting | -> /decide |
| Need more options before acting | -> /search |
| Need root cause first | -> /diagnose |

### 5. Single Next Step Rule

Return one immediate next step only.
Do not return a full roadmap in this router.

---

## Execute

**Default path (clear immediate task):**
-> INVOKE: /action $ARGUMENTS

**When blocked by uncertainty:**
-> INVOKE: /diagnose $ARGUMENTS

**When goal is unclear:**
-> INVOKE: /want $ARGUMENTS

---

## After Completion

Report:
- The selected next step
- Why this step is first
- What result to check immediately after executing it

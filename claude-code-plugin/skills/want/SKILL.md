---
name: "want - Clarify a Goal"
description: Sub-orchestrator for goals and wants. Routes to WantTo analysis to trace what the want commits you to and find the actual want.
---

# Want

**Input**: $ARGUMENTS

---

## Routing Decisions

### 1. Extract the Want

What does the user want? State it in their words. "I want to X" / "I need to X" / "My goal is X" / sometimes just a noun ("career change", "startup").

### 2. Is This Actually a Goal?

- **"Should I X?"** → This is a decision. → INVOKE: /decide $ARGUMENTS
- **"X is true"** → This is a claim. → INVOKE: /claim $ARGUMENTS
- **"How do I X?"** → They already know the goal, they need the method. → INVOKE: /how $ARGUMENTS
- **"I'm frustrated about X"** → This is emotional. → INVOKE: /emotion $ARGUMENTS
- **"What about X?"** → This is an idea. → INVOKE: /viability $ARGUMENTS
- **If it IS a goal/want** → continue.

### 3. Is This the Real Want or a Proxy?

The stated want is almost never the actual want. "I want to quit my job" means "I want what my job prevents." The /wt skill traces this by assuming the want is right and following implications.

Always go deeper. The first stated want is the starting point, not the answer.

### 4. Is This a Goal or a Decision?

- **Single direction** ("I want X"): this is a goal. Proceed.
- **Choice embedded** ("I want X but maybe Y"): this is a decision.
  → INVOKE: /decide $ARGUMENTS

### 5. Actionable or Aspirational?

- **Actionable** ("I want to launch by Q3", "I need to hire 3 engineers"): /wt will produce paths and first actions → then /how for the method → then /action for execution.
- **Aspirational** ("I want to be happy", "I want financial freedom"): /wt will trace what this means concretely → then /want again on the concrete version.

---

## Execute

→ INVOKE: /wt $ARGUMENTS

The /wt skill uses AR-forward mode: assume the want is right, trace what it commits you to, unbundle the want into desire/method/belief/assumption/implicit want/anti-want, find the actual want, map paths, identify the crux.

---

## After Completion

Report:
- Stated want vs actual want (if different)
- What the want commits you to
- What the want forecloses
- Prerequisites (met / unmet)
- Paths available
- Recommended first action

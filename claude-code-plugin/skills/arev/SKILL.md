---
name: "arev - Assume Reversible"
description: "Force the assumption that a decision or action is fully reversible. Trace what follows: should we just try it? What's the real cost of reversal? Is it actually reversible?"
output:
  format: "prose"
---

# Assume Reversible

**Input**: $ARGUMENTS

---

## Core Move

**Assume the decision is fully reversible.** If it doesn't work, you can undo it completely and return to the current state. No permanent consequences.

If truly reversible, the calculus changes radically: the cost of trying drops to near zero, and the value of information from trying skyrockets.

---

## Procedure

### Step 1: State the Decision/Action
What are we assuming is reversible?

### Step 2: Force the Assumption
"This is fully reversible. If it doesn't work, we can undo it completely with no lasting consequences."

### Step 3: Trace Implications
If it's truly reversible:

1. **Should we just try it?** — If reversal is free, the expected value of trying is almost always positive (you learn something).
2. **What do we learn from trying?** — What information do we gain that we can't get any other way?
3. **What's the reversal mechanism?** — How specifically would we undo it?
4. **What's the reversal cost?** — Even reversible actions have reversal costs (time, effort, transition). What are they?
5. **What's the reversal timeline?** — How long does undoing take?
6. **What's NOT reversed?** — Even in "reversible" situations, some things change permanently (reputation, knowledge, time spent).

### Step 4: Test the Assumption
- Is it ACTUALLY reversible? Many things feel reversible but aren't (relationships, reputation, market timing).
- What's the hidden cost of reversal?
- Does reversal create its own problems (flip-flopping perception, migration costs)?
- Is there a point of no return after which reversal becomes impossible?

### Step 5: Synthesize
```
DECISION: [stated]
ASSUMING REVERSIBLE:
  Try it?: [yes/no — reasoning]
  Learn from trying: [information gained]
  Reversal mechanism: [how to undo]
  Reversal cost: [time, effort, other]
  NOT reversed: [what changes permanently]
ACTUALLY REVERSIBLE?: [yes/mostly/partially/no]
RECOMMENDATION: [try it / get more info first / treat as irreversible]
```

---

## When to Use
- Stuck in analysis paralysis on a decision
- Want to test whether "just try it" is the right call
- Evaluating risk by assessing reversibility

## Integration
- Use as a decision-speed heuristic: if reversible, bias toward action
- Follow with `/dcp` for the full decision if NOT reversible
- Pair with `/afail` to assess downside if the trial fails

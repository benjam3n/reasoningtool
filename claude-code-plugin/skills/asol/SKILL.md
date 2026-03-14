---
name: "asol - Assume Solution"
description: "Force the assumption that something IS the solution. Trace what follows: does it actually address the problem? What are the costs? What breaks?"
output:
  format: "prose"
---

# Assume Solution

**Input**: $ARGUMENTS

---

## Core Move

Take a proposed action, approach, or intervention and **assume it is THE solution.** It works. It's the right answer. Now trace what that world looks like.

Different from `/ase` (does a solution exist?). This assumes a SPECIFIC thing is the solution.

---

## Procedure

### Step 1: State the Candidate Solution
What are we assuming is the solution?

### Step 2: State the Problem It Solves
What problem does this supposedly fix? (If unclear, this is already a red flag.)

### Step 3: Force the Assumption
"[X] is the correct solution. Implementing it will resolve the problem."

### Step 4: Trace Implications
If this is the solution:

1. **What does implementation look like?** — Concrete steps, timeline, resources.
2. **What problem does it actually solve?** — Be precise. Not "makes things better" — what specific condition changes?
3. **What problems does it create?** — Every solution creates new problems. What are they?
4. **What does it cost?** — Money, time, attention, opportunity cost, political capital.
5. **Who wins and who loses?** — Whose situation improves? Whose worsens?
6. **What's the world after?** — Describe the state of affairs after successful implementation.
7. **Is the post-solution world actually desirable?** — Sometimes getting what you want reveals you wanted the wrong thing.

### Step 5: Test the Assumption
- Does this address root cause or symptoms?
- Are there simpler solutions that achieve the same outcome?
- Has this been tried before? What happened?
- What would falsify "this is the solution"?

### Step 6: Synthesize
```
CANDIDATE SOLUTION: [X]
PROBLEM IT ADDRESSES: [specific problem]
ASSUMING IT WORKS:
  Implementation: [steps]
  Actually solves: [precise effect]
  Creates: [new problems]
  Costs: [resources/tradeoffs]
  Post-solution world: [description]
SOLUTION CONFIDENCE: [high/medium/low]
BETTER ALTERNATIVE?: [if one emerged from analysis]
```

---

## When to Use
- Evaluating a proposed solution before committing
- Comparing candidate solutions (run once per candidate)
- Testing whether a "solution" actually solves the stated problem

## Integration
- Pair with `/aprob` to verify the problem before testing solutions
- Compare multiple candidates with `/cmp`
- Use `/cba` for cost-benefit analysis

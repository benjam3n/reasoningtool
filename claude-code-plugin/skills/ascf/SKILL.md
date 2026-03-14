---
name: "ascf - Assume Solution Can Be Found"
description: "Force the assumption that a solution is discoverable — not just that it exists, but that we can actually find it with available methods. Trace what search strategy follows."
output:
  format: "prose"
---

# Assume Solution Can Be Found

**Input**: $ARGUMENTS

---

## Core Move

Distinct from `/ase` (solution exists). Here: **we can actually find it.** A solution may exist but be unfindable (computationally intractable, beyond our tools, requires information we can't get). This skill assumes findability.

---

## Procedure

### Step 1: State the Problem
Precisely state the problem from the input.

### Step 2: Force the Assumption
"A solution can be found using methods available to us, within reasonable time and resources."

### Step 3: Trace Implications
If the solution is findable:

1. **What search method works?** — Systematic search, heuristic, trial-and-error, formal proof, empirical testing?
2. **What resources are needed?** — Time, compute, expertise, data, tools?
3. **What's the search space?** — Where do we look? How big is the space?
4. **What would finding it look like?** — How would we recognize the solution when we see it?
5. **What's the expected cost to find?** — Order of magnitude estimate.
6. **What's been tried?** — What search strategies have already failed, and what does that tell us?

### Step 4: Test the Assumption
- Is the search space finite or infinite?
- Are there computational complexity barriers (NP-hard, undecidable)?
- Do we have the right tools for this search?
- Is there an information barrier (we can't get the data we'd need)?

### Step 5: Synthesize
```
PROBLEM: [stated]
ASSUMING FINDABLE:
  Search method: [approach]
  Search space: [where and how big]
  Recognition criteria: [how we'd know]
  Estimated cost: [resources needed]
  Already tried: [what failed and why]
FINDABILITY CONFIDENCE: [high/medium/low]
NEXT MOVE: [specific search action]
```

---

## When to Use
- Know a solution probably exists but unsure if you can find it
- Need to design a search strategy
- Want to distinguish "unsolvable" from "hard to find"

## Integration
- Pair with `/ase` (does it exist?) and `/ascfa` (can we find it without searching?)
- Follow with `/de` to plan the search

---
name: "ase - Assume Solution Exists"
description: "Force the assumption that a solution exists for the problem at hand, then trace what follows. What does the solution space look like? What constraints must it satisfy? What have we been missing?"
output:
  format: "prose"
---

# Assume Solution Exists

**Input**: $ARGUMENTS

---

## Core Move

Temporarily adopt the assumption: **a solution to this problem definitely exists.** Don't question whether — ask what, where, and what shape.

This is useful when you're stuck in "is this even solvable?" loops. By forcing existence, you shift from possibility-checking to solution-hunting.

---

## Procedure

### Step 1: State the Problem
Precisely state the problem or challenge from the input.

### Step 2: Force the Assumption
State explicitly: "A solution exists. It is real and findable."

### Step 3: Trace Implications
If a solution exists:

1. **What properties must it have?** — List constraints the solution must satisfy.
2. **Where would it live?** — What domain, field, discipline, or approach space?
3. **What would it look like?** — Sketch the shape, even if vague.
4. **What adjacent solutions exist?** — What partial, approximate, or analogous solutions already exist?
5. **Why haven't we found it yet?** — What's blocking discovery? Wrong search space? Wrong framing? Missing tools?
6. **Who would have found it?** — What kind of person, team, or field would have encountered this solution?

### Step 4: Test the Assumption
Now critically examine: is the assumption that a solution exists actually warranted?

- What evidence supports existence?
- What evidence suggests non-existence?
- Is this an empirical question or a logical one?
- Could the problem be ill-posed (no solution because the question is wrong)?

### Step 5: Synthesize
```
PROBLEM: [stated]
ASSUMING SOLUTION EXISTS:
  Must satisfy: [constraints]
  Likely lives in: [domain/space]
  Looks like: [shape]
  Blocked by: [what's preventing discovery]
EXISTENCE CONFIDENCE: [high/medium/low with reasoning]
NEXT MOVE: [specific action to find or verify]
```

---

## When to Use
- Stuck in feasibility paralysis
- Need to shift from "can we?" to "how do we?"
- Want to map the solution space before judging solvability

## Integration
- Pair with `/asdne` for the opposite stance
- Follow with `/se` to explore the solution space identified
- Use `/araw` for full bilateral analysis

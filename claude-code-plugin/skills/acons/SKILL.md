---
name: "acons - Assume Constraint"
description: "Force the assumption that a constraint is real and binding. Trace what it means for your options: what's ruled out, what's left, and is the constraint actually real?"
output:
  format: "prose"
---

# Assume Constraint

**Input**: $ARGUMENTS

---

## Core Move

Take a constraint — budget, time, physics, policy, skill, resources — and **assume it's real, hard, and non-negotiable.** Then work within it. What's still possible? What's the best move given the constraint?

Useful for grounding in reality and finding creative solutions within limits.

---

## Procedure

### Step 1: State the Constraint
What constraint are we assuming is real?

### Step 2: Force the Assumption
"This constraint is real, hard, and cannot be changed. We must work within it."

### Step 3: Trace Implications
If the constraint is binding:

1. **What's ruled out?** — What options, approaches, or solutions are no longer available?
2. **What's still possible?** — What remains in the feasible set?
3. **What's the best option within bounds?** — Of what remains, what's optimal?
4. **Does the constraint create opportunity?** — Constraints often force creativity. What's enabled by the limitation?
5. **What's the cost of the constraint?** — How much worse is the constrained optimum vs. unconstrained?
6. **What other constraints interact?** — Does this constraint tighten or loosen other constraints?

### Step 4: Test the Assumption
- Is this constraint actually hard? Or is it a policy that could be changed?
- Who imposed it? Could it be renegotiated?
- Is it permanent or temporary?
- Have others found ways around it?

### Step 5: Synthesize
```
CONSTRAINT: [stated]
ASSUMING BINDING:
  Ruled out: [eliminated options]
  Still possible: [remaining options]
  Best within bounds: [optimal constrained choice]
  Opportunity created: [what the constraint enables]
CONSTRAINT REAL?: [hard/soft/negotiable]
IF SOFT: [how to relax it]
```

---

## When to Use
- Need to ground planning in reality
- Want to find creative solutions within limits
- Testing whether a constraint is real or assumed

## Integration
- Pair with `/ancons` to test what happens without the constraint
- Follow with `/cmp` to compare options within the constrained set
- Use `/se` to explore the feasible space

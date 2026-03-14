---
name: "acrit - Assume Critical"
description: "Force the assumption that something is absolutely critical — a must-have, non-negotiable, load-bearing element. Trace what that demands and whether it's actually true."
output:
  format: "prose"
---

# Assume Critical

**Input**: $ARGUMENTS

---

## Core Move

Take something and **assume it's critical.** Not just important — essential. Without it, everything fails. Then trace what that means and whether the claim holds.

Useful for testing priorities and distinguishing "nice to have" from "must have."

---

## Procedure

### Step 1: Identify the Thing
What are we assuming is critical?

### Step 2: Force the Assumption
"[X] is absolutely critical. Without it, the entire effort fails."

### Step 3: Trace Implications
If it's truly critical:

1. **What fails without it?** — Specifically, what breaks? Trace the failure cascade.
2. **What must we do to protect it?** — If critical, what resources, backup plans, or safeguards are needed?
3. **What's the cost of protection?** — Treating something as critical is expensive. What's the cost?
4. **What gets deprioritized?** — If this is critical, what's NOT critical? What drops?
5. **Is it fragile?** — Critical AND fragile = urgent problem. Critical AND robust = less urgent.
6. **Can it be made non-critical?** — Can we redesign so this isn't a single point of failure?

### Step 4: Test the Assumption
- What's the actual evidence that this is critical?
- Has anything succeeded WITHOUT this element?
- Is it critical for ALL outcomes, or just the current plan?
- Could we run a small experiment without it to test?

### Step 5: Synthesize
```
THING: [X]
ASSUMING CRITICAL:
  Without it: [failure cascade]
  Protection cost: [resources needed]
  Deprioritizes: [what drops in importance]
  Fragility: [fragile/robust]
CRITICALITY CONFIDENCE: [high/medium/low]
IF NOT CRITICAL: [what changes about strategy]
```

---

## When to Use
- Prioritizing limited resources
- Testing whether a "requirement" is actually required
- Designing for resilience (find single points of failure)

## Integration
- Pair with `/airr` for the opposite stance
- Use in sequence on multiple elements to build a priority map
- Follow with `/cmp` to compare criticality across elements

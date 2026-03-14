---
name: "aasm - Assume Assumption"
description: "Take a hidden or implicit assumption and force it to be explicit and true. Trace what world that creates, what depends on it, and how fragile it is."
output:
  format: "prose"
---

# Assume Assumption

**Input**: $ARGUMENTS

---

## Core Move

Take something that's being **assumed** (often implicitly) and make it the explicit, central premise. Then stress-test it: what depends on this assumption? What breaks if it's wrong? How would we know?

This is meta-level: assuming the assumption itself is correct, and tracing the dependency chain.

---

## Procedure

### Step 1: Identify the Assumption
What assumption are we examining? State it explicitly, even if it was originally implicit.

### Step 2: Force the Assumption
"[Assumption] is true. We are building on this as solid ground."

### Step 3: Trace the Dependency Chain
If this assumption is correct:

1. **What rests on it?** — List everything that depends on this assumption being true. Decisions, plans, beliefs, other assumptions.
2. **How deep does it go?** — Trace the dependency chain. A depends on this assumption. B depends on A. C depends on B. How far?
3. **What else must be true?** — What OTHER assumptions are required alongside this one?
4. **How would we know it's wrong?** — What observable signal would indicate this assumption has failed?
5. **How old is this assumption?** — When was it formed? Is it based on conditions that still hold?
6. **Who else shares this assumption?** — Is it widely held, or idiosyncratic?

### Step 4: Fragility Assessment
```
FRAGILITY RATING:

  Load-bearing: [how much depends on it? 1=little, 5=everything]
  Testability:  [can we verify it? 1=untestable, 5=easy to check]
  Age:          [how long held? Recent/old/ancient]
  Alternatives: [if wrong, do alternatives exist? Yes/no/partial]
  Warning signs: [what would early failure look like?]
```

### Step 5: Synthesize
```
ASSUMPTION: [stated explicitly]
ASSUMING IT'S TRUE:
  Depends on it: [dependency chain]
  Also requires: [companion assumptions]
  Failure signal: [how we'd know it's wrong]
FRAGILITY: [fragile/moderate/robust]
RECOMMENDATION: [keep/test/replace/monitor]
```

---

## When to Use
- Auditing the foundations of a plan or belief system
- Found a hidden assumption and want to understand its weight
- Building on something and want to know how solid the ground is

## Integration
- Use `/aex` first to surface assumptions, then `/aasm` to test the critical ones
- Follow with `/aop` to see what happens if the assumption is wrong
- Pair with `/ht` to design a test of the assumption

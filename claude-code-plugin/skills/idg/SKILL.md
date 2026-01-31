---
name: idg
description: "Handler for goals where SUCCESS IS DISCOVERING THE UNKNOWN, not executing a known plan."
---

# Iterative Discovery Goals Handler

**Input**: $ARGUMENTS

---

## Overview

Handler for goals where SUCCESS IS DISCOVERING THE UNKNOWN, not executing a known plan. These goals are fundamentally different because: you don't know what you're looking for until you find it, the plan is to run experiments not execute steps, failure is information not setback, success comes from iteration speed not plan quality.

## Steps

### Step 1: Accept the Nature of Discovery
Before starting, reset expectations:
1. You CANNOT plan your way to discovery
2. You CAN plan your way to faster discovery
3. The goal is to INCREASE ITERATION SPEED and LEARNING QUALITY
4. Every experiment that doesn't work NARROWS the search space (progress, not failure)

### Step 2: Define the Discovery Space
1. What are you trying to discover/find/figure out?
2. What would "found it" feel like? (Recognition criteria, even if vague)
3. What have you already tried? What did you learn?
4. What is the search space? (How many possibilities exist?)
5. What constraints limit exploration? (Time, money, energy, access)

### Step 3: Generate Hypotheses
Instead of a plan, create a hypothesis stack:

| # | Hypothesis | Test | How Long | What I'd Learn |
|---|-----------|------|----------|---------------|
| 1 | [if X then Y] | [smallest experiment] | [duration] | [what result would tell me] |
| 2 | [if X then Y] | [smallest experiment] | [duration] | [what result would tell me] |
| 3 | [if X then Y] | [smallest experiment] | [duration] | [what result would tell me] |

**Hypothesis quality checklist:**
- Is it testable? (Can you actually run the experiment?)
- Is it informative? (Does the result change what you do next?)
- Is it fast? (Can you get a result quickly?)
- Is it cheap? (Can you afford to run it?)

### Step 4: Design Experiments
For each hypothesis, design the minimum viable experiment:

```
EXPERIMENT:
Hypothesis: [what you're testing]
Test: [what you'll do]
Duration: [how long]
Success metric: [what a "hit" looks like]
Failure metric: [what tells you to move on]
What you'll learn either way: [information value regardless of outcome]
```

**Experiment design principles:**
- Smallest possible test (don't over-invest before you know)
- Clear success/failure criteria defined BEFORE starting
- Time-boxed (set a deadline — don't let experiments drift)
- One variable at a time (if possible — know what caused the result)

### Step 5: Run, Measure, Learn, Iterate
Execute in rapid cycles:

```
Cycle 1:
  Experiment: [what was tested]
  Result: [what happened]
  Learning: [what this tells us]
  Next: [what to test next based on this]

Cycle 2:
  ...
```

**After each cycle, update:**
1. What do I now know that I didn't before?
2. Has the search space narrowed? How?
3. Should I pivot direction based on what I learned?
4. Am I getting warmer or colder?

### Step 6: Recognize Discovery Patterns

**Convergence signals** (getting closer):
- Results are getting better across iterations
- You're finding what doesn't work (narrowing the space)
- Intuition is developing about what might work
- You can articulate what you're looking for more precisely

**Divergence signals** (need to change approach):
- Results aren't improving despite many iterations
- You're running the same type of experiment repeatedly
- The search space isn't narrowing
- You feel stuck and can't articulate why

**If diverging:** Change something fundamental:
- Different dimension of the search space
- Different type of experiment
- Different assumptions about what "found it" looks like
- Different domain or context
- → INVOKE: /ie (innovation engine) for non-obvious approaches

### Step 7: Report
```
DISCOVERY PROGRESS:
Goal: [what you're discovering]
Experiments run: [N]
Hypotheses tested: [N tested / N remaining]

Search space status:
- Eliminated: [what you know DOESN'T work]
- Promising: [what seems worth exploring more]
- Unexplored: [what you haven't tried yet]

Current best: [closest thing to "found it" so far]
Convergence: [converging / flat / diverging]

Next experiment: [what to test next]
Why: [what you expect to learn]

Pivot consideration: [should you change approach?]
```

## When to Use
- Goal involves finding/discovering something unknown
- Success requires experimentation, not execution
- Need to test multiple hypotheses
- The "right answer" will only be obvious in hindsight
- Standard planning feels premature
- → INVOKE: /ge (guided experiments) for experiment design
- → INVOKE: /po (personal optimization) for self-experimentation
- → INVOKE: /dtl (design thinking + lean) for product discovery

## Verification
- [ ] Discovery nature accepted (not trying to plan linearly)
- [ ] Search space defined
- [ ] Hypotheses are testable, informative, fast, and cheap
- [ ] Experiments have success/failure criteria defined BEFORE running
- [ ] Learning captured after each cycle
- [ ] Convergence/divergence assessed regularly

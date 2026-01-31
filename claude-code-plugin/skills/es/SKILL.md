---
name: es
description: "Evolution has optimized biological systems for billions of years. Apply evolutionary strategies to find solutions."
---

# Evolutionary Strategies

**Input**: $ARGUMENTS

---

## Overview

Evolution has optimized biological systems for billions of years. Evolutionary strategies apply the same principles to find solutions:
- Generate variations
- Test fitness
- Select the best
- Repeat

Works when you can evaluate solutions but don't know how to construct optimal ones directly.

## Steps

### Step 1: Define the Fitness Function
Before evolving solutions, you must define what "good" means:

1. What are you trying to optimize?
2. How do you measure quality of a candidate solution?
3. Are there multiple objectives? (If so, how are they weighted?)
4. Are there hard constraints? (Solutions that violate these are immediately eliminated)
5. Are there soft constraints? (Violations reduce fitness but don't eliminate)

```
FITNESS FUNCTION:
Primary objective: [what to maximize/minimize]
Secondary objectives: [other goals]
Hard constraints: [must satisfy]
Soft constraints: [prefer to satisfy]
Measurement: [how to score a candidate]
```

### Step 2: Create Initial Population
Generate diverse starting candidates:

**Generation methods:**
- Random: Generate candidates randomly within the solution space
- Seeded: Start with known good solutions + random variations
- Heuristic: Use domain knowledge to generate reasonable starting points
- Borrowed: Import solutions from analogous domains

**Population size:** Start with at least 10 candidates. More for complex problems.

**Diversity is critical:** If all candidates are similar, evolution can't explore. Deliberately include "weird" candidates.

### Step 3: Evaluate Fitness
Score each candidate:

| Candidate | Primary Score | Secondary Score | Constraints Met | Overall Fitness |
|-----------|--------------|----------------|----------------|----------------|
| C1 | [score] | [score] | [Y/N] | [weighted total] |
| C2 | [score] | [score] | [Y/N] | [weighted total] |
| ... | | | | |

### Step 4: Selection
Choose which candidates survive to produce offspring:

**Selection methods:**
- **Tournament**: Pick 2-3 random candidates, keep the best
- **Proportional**: Probability of selection proportional to fitness
- **Truncation**: Keep top N% of population
- **Elitism**: Always keep the single best (prevents losing good solutions)

Recommended: Tournament selection + elitism (robust default)

### Step 5: Variation (Create Offspring)
Apply operators to create new candidates from selected parents:

**Mutation** (small random changes to one parent):
- Change one element of the solution
- Adjust a parameter by a small amount
- Add or remove a component
- Mutation rate: ~5-20% of elements per offspring

**Crossover** (combine two parents):
- Take part of Parent A and part of Parent B
- Combine strengths of different solutions
- Works best when solutions have modular structure

**Innovation** (inject new genetic material):
- Occasionally add completely random candidates
- Prevents the population from converging too early
- ~5-10% of new population should be fresh

### Step 6: Iterate
Repeat Steps 3-5 for multiple generations:

**When to stop:**
- Fitness plateau: Best fitness hasn't improved in N generations
- Good enough: A candidate meets the target fitness
- Resource limit: Out of evaluation budget
- Diversity collapse: All candidates are too similar (restart needed)

**Track across generations:**
```
| Generation | Best Fitness | Average Fitness | Diversity | Notes |
|-----------|-------------|----------------|-----------|-------|
| 1 | [score] | [score] | [high/med/low] | |
| 2 | [score] | [score] | | |
| ... | | | | |
```

### Step 7: Analyze Results
After evolution completes:

1. **Best solution**: What's the top candidate? Is it actually good?
2. **Convergence pattern**: Did fitness improve steadily or in jumps?
3. **Diversity of good solutions**: Are all good solutions similar (one peak) or diverse (multiple peaks)?
4. **Robustness**: Is the best solution fragile (small changes destroy it) or robust?
5. **What evolved**: What features do the best solutions share? (These are the important design choices)

### Step 8: Report
```
EVOLUTIONARY STRATEGY RESULTS:
Problem: [what was being optimized]
Fitness function: [what was measured]

Evolution summary:
- Generations: [N]
- Initial best fitness: [score]
- Final best fitness: [score]
- Improvement: [%]

Best solution: [description]
Key features of good solutions: [common elements across top candidates]
Robustness: [fragile / moderate / robust]

Diverse alternatives: [other good solutions that differ from the best]
What didn't work: [features that evolution consistently eliminated]
```

## When to Use
- Complex optimization with many variables
- No clear path to optimal solution
- Can evaluate candidates but can't derive solutions
- Want to explore diverse approaches
- Need robustness over optimality
- → INVOKE: /gen (candidate generation) for creating initial population
- → INVOKE: /sel (selection) for choosing among candidates
- → INVOKE: /pbs (population-based search) for parallel search strategies

## Verification
- [ ] Fitness function defined before evolution starts
- [ ] Initial population is diverse (not all similar)
- [ ] Both mutation and crossover applied
- [ ] Elitism used (best solution preserved)
- [ ] Convergence tracked across generations
- [ ] Best solution analyzed for robustness
- [ ] Alternative good solutions noted (not just the single best)

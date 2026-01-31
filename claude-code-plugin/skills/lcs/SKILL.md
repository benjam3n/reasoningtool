---
name: "lcs - Local Search Orderings"
description: "Orderings based on local search optimization — improve from current position, escape local optima, systematic exploration with memory."
---

# Local Search Orderings

**Input**: $ARGUMENTS

---

## Overview

When you can't see the whole solution space, improve iteratively from where you are. Local search finds nearby better solutions, with techniques to escape local optima and avoid revisiting dead ends.

## Core Principle

Start somewhere. Look at neighbors. Move to the best neighbor. Repeat. When stuck, use disruption to escape.

## Ordering Rules

### Rule 1: Hill Climbing — Always Move Upward
- Evaluate all neighboring solutions
- Move to the best one that improves the current solution
- Stop when no neighbor is better (local optimum)
- **When**: simple optimization, good starting point, smooth landscape

### Rule 2: Simulated Annealing — Sometimes Accept Worse
- Usually move to better neighbors
- Occasionally accept worse solutions (probability decreases over time)
- Early: explore freely. Late: exploit greedily.
- **When**: complex landscapes with many local optima

### Rule 3: Tabu Search — Remember and Avoid
- Keep a list of recently visited solutions (tabu list)
- Don't revisit recent solutions even if they look good
- Forces exploration of new territory
- **When**: cycling is a problem, search keeps returning to same solutions

### Rule 4: Iterated Local Search — Perturb and Restart
- Run hill climbing to a local optimum
- Perturb the solution (random changes)
- Run hill climbing again from the perturbed state
- Keep the best solution found across all restarts
- **When**: need to sample multiple local optima

## Application Procedure

### Step 1: Define Neighborhood
- What counts as a "nearby" solution?
- How many neighbors does each solution have?
- Can you evaluate neighbors efficiently?

### Step 2: Choose Strategy
- Smooth landscape, one clear peak → Hill Climbing
- Rugged landscape, many traps → Simulated Annealing or Iterated Local Search
- Cycling problem → Tabu Search

### Step 3: Set Termination
- Maximum iterations
- No improvement for N steps
- Good-enough threshold reached

## When to Use
- Optimization without closed-form solution
- Scheduling, routing, configuration problems
- Any problem where you can evaluate "is this neighbor better?"

## Verification
- [ ] Neighborhood structure defined
- [ ] Starting solution reasonable
- [ ] Escape mechanism for local optima included
- [ ] Termination criteria set

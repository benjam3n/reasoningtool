---
name: "pbs - Population Based Search Orderings"
description: "Maintain multiple candidate solutions simultaneously — evolutionary approaches, beam search, iterative deepening."
---

# Population Based Search Orderings

**Input**: $ARGUMENTS

---

## Overview

Instead of pursuing one solution, maintain a population of candidates. Evaluate, select, recombine, and iterate. Finds better solutions than single-track search when the solution space is large and deceptive.

## Ordering Rules

### Rule 1: Parallel Evaluation
- Evaluate all candidates in the population before selecting
- Don't commit to one path prematurely
- **When**: multiple plausible approaches, uncertain which is best

### Rule 2: Select and Recombine
- Keep the best candidates, combine their strengths
- "Take the best parts of each approach" — not metaphorical, literal
- **When**: solutions have modular components that can be mixed

### Rule 3: Iterative Deepening
- Search to depth 1, then depth 2, then depth 3...
- Guarantees finding the shallowest solution while managing memory
- **When**: unknown solution depth, memory constraints

### Rule 4: Beam Search — Top-K
- At each step, keep only the K best candidates
- Expand each, evaluate, keep top K again
- **When**: space too large for full exploration, need approximate best

### Rule 5: Mutation — Random Perturbation
- After selecting best candidates, randomly modify some
- Prevents premature convergence on local optima
- **When**: stuck, all candidates too similar

## Application

### Step 1: Initialize Population
- Generate diverse starting candidates (don't start all the same)

### Step 2: Evaluate All
- Score each candidate on the objective

### Step 3: Select, Recombine, Mutate
- Keep top performers, combine, add random variation
- Repeat until convergence or budget exhausted

## When to Use
- Complex optimization, creative ideation, strategy selection
- When one approach feels risky

## Verification
- [ ] Population diverse at initialization
- [ ] All candidates evaluated before selection
- [ ] Mutation preventing premature convergence
- [ ] Best solution tracked across all generations

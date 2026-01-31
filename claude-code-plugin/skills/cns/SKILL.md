---
name: "cns - Constraint Solving Orderings"
description: "Orderings for constraint satisfaction and guided search — process most constrained variables first, propagate constraints, backtrack efficiently."
---

# Constraint Solving Orderings

**Input**: $ARGUMENTS

---

## Overview

When building solutions incrementally with constraints, the order you make decisions dramatically affects efficiency. Process the most constrained elements first, propagate implications immediately, and backtrack early when constraints are violated.

## Core Principle

Fail fast. The earlier you detect that a path can't work, the less time you waste. Process the most constrained variables first because they have the fewest valid options and will trigger failures soonest.

## Ordering Rules

### Rule 1: Most Constrained First (MRV)
- Choose the variable with fewest remaining valid values
- Ties: choose the variable involved in the most constraints
- **Why**: most likely to fail → fail early → prune search space

### Rule 2: Propagate Immediately
- After each assignment, propagate all implications
- Remove values from other variables that are now impossible
- If any variable has zero remaining values → backtrack immediately
- **Why**: don't wait to discover impossible states later

### Rule 3: Least Constraining Value
- When choosing a value for a variable, try the value that eliminates fewest options for other variables
- **Why**: keeps the most options open for future decisions

### Rule 4: Constraint-Guided Backtracking
- When backtracking, jump to the variable that caused the failure (not just the most recent)
- **Why**: avoid re-exploring branches that will fail for the same reason

## Application Procedure

### Step 1: Model as Constraint Problem
1. What are the variables (decisions to make)?
2. What are the domains (valid options for each)?
3. What are the constraints (which combinations are forbidden)?

### Step 2: Apply Ordering
1. Sort variables by constraint count (most constrained first)
2. For each variable, try values in least-constraining order
3. After each assignment, propagate constraints
4. Backtrack intelligently when stuck

### Step 3: Validate
- Solution satisfies all constraints
- No constraint violations remain

## Anti-Patterns
- Random variable ordering (misses easy pruning)
- No propagation (discovers failures too late)
- Naive backtracking (re-explores dead ends)

## When to Use
- Scheduling (rooms, people, times)
- Configuration (compatible options)
- Puzzle solving (Sudoku, crosswords)
- Resource allocation with constraints

## Verification
- [ ] Problem modeled with variables, domains, constraints
- [ ] Most constrained variables processed first
- [ ] Constraints propagated after each assignment
- [ ] All constraints satisfied in final solution

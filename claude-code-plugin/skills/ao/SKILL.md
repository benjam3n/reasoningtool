---
name: "ao - Algorithmic Optimization Orderings"
description: "Orderings based on classic algorithm design paradigms: greedy, dynamic programming, divide-and-conquer, and branch-and-bound."
---

# Algorithmic Optimization Orderings

**Input**: $ARGUMENTS

---

## Overview

Apply algorithm design paradigms to determine the best order for attacking a problem. Different structures require different approaches — greedy for locally optimal choices, DP for overlapping subproblems, divide-and-conquer for independent decomposition, branch-and-bound for constrained search.

## Core Principle

Match the problem structure to the paradigm. Wrong paradigm = wasted effort or wrong answer.

## Ordering Rules

### Rule 1: Greedy — Process by Local Optimality
Order steps by immediate value, choosing the locally best option at each step.
- **When**: problem has greedy-choice property (local optimal leads to global optimal)
- **How**: sort by value/cost ratio, process best-first
- **Verify**: exchange argument proves greedy works
- **Example**: schedule tasks by deadline, select items by value-to-weight ratio

### Rule 2: Dynamic Programming — Process by Subproblem Dependencies
Order steps so that each subproblem is solved before any problem that depends on it.
- **When**: overlapping subproblems + optimal substructure
- **How**: bottom-up (small subproblems first) or top-down with memoization
- **Verify**: recurrence relation is correct, base cases covered
- **Example**: compute shortest paths by increasing number of edges

### Rule 3: Divide and Conquer — Process by Recursive Decomposition
Split problem into independent parts, solve each, combine results.
- **When**: problem splits cleanly into independent subproblems
- **How**: divide until base case, solve base cases, merge upward
- **Verify**: merge step correctly combines sub-solutions
- **Example**: sort each half, then merge sorted halves

### Rule 4: Branch and Bound — Process by Pruned Search
Explore solution space systematically, pruning branches that can't beat current best.
- **When**: need optimal solution in combinatorial space
- **How**: expand most promising nodes first, prune when bound exceeds best known
- **Verify**: bounding function is admissible (never overestimates)
- **Example**: explore assignment options, skip branches that exceed current best cost

## Application Procedure

### Step 1: Classify the Problem
- Does it have optimal substructure? (optimal solution contains optimal sub-solutions)
- Do subproblems overlap? (same computation needed multiple times)
- Is local choice globally optimal? (greedy property)
- Can it be decomposed into independent parts?

### Step 2: Select Paradigm

| Structure | Paradigm |
|-----------|----------|
| Greedy-choice property holds | Greedy |
| Overlapping subproblems + optimal substructure | DP |
| Independent subproblems | Divide and conquer |
| Combinatorial, need global optimum | Branch and bound |
| None of the above | Try multiple, compare |

### Step 3: Apply and Verify
1. Implement the ordering
2. Verify correctness (proof or exhaustive testing)
3. Check complexity matches expectations

## Anti-Patterns
- Applying greedy without proving the greedy-choice property
- Using DP when subproblems don't overlap (unnecessary overhead)
- Divide-and-conquer with dependent subproblems (incorrect results)

## When to Use
- Optimization problems with clear structure
- Scheduling, allocation, routing problems
- Any problem where step ordering affects solution quality

## Verification
- [ ] Problem structure classified
- [ ] Paradigm matched to structure
- [ ] Correctness proven or verified
- [ ] Complexity appropriate

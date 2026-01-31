---
name: "ovi - Ordering Variations Integration"
description: "Guide for selecting and applying the right ordering strategy to any procedure's steps."
---

# Ordering Variations Integration

**Input**: $ARGUMENTS

---

## Overview

Meta-procedure for choosing which ordering strategy to apply to a given set of steps. Maps problem characteristics to the appropriate ordering skill, then applies it.

## Steps

### Step 1: Identify the Steps to Order
1. What steps/tasks need ordering?
2. What are the dependencies between them?
3. What are the constraints (time, resources, risk)?
4. Who is executing? (human, machine, team)

### Step 2: Assess Problem Characteristics

| Characteristic | If True | Ordering to Consider |
|---------------|---------|---------------------|
| Clear dependencies | Yes | /gt (graph traversal), /to (topological) |
| Resource constrained | Yes | /ct (crisis triage), /rso (resource opt) |
| Uncertainty high | Yes | /rm (risk), /ld (learning discovery) |
| Human executor | Yes | /mp (motivation psychology) |
| Competitive context | Yes | /mil (military), /ns (negotiation) |
| Communication output | Yes | /cn (narrative) |
| Deadline driven | Yes | /td (temporal), /pjm (project mgmt) |
| Multiple valid solutions | Yes | /dvs (diversity), /pbs (population) |
| Learning goal | Yes | /pge (pedagogy), /ld (learning) |
| Building incrementally | Yes | /pb (progressive building) |
| Optimization problem | Yes | /ao (algorithmic), /lcs (local search) |
| Fairness required | Yes | /faa (fairness allocation) |
| Explore/exploit tradeoff | Yes | /be (bandit exploration) |
| Constraint satisfaction | Yes | /cns (constraint solving) |
| Detecting deception | Yes | /dv (detection verification) |

### Step 3: Apply Selected Ordering
1. Invoke the selected ordering skill
2. Apply its rules to your steps
3. Validate the resulting order makes sense

### Step 4: Handle Multiple Applicable Orderings
If several orderings apply:
1. Identify which characteristic dominates
2. Use the dominant ordering as primary
3. Use secondary orderings to break ties

## When to Use
- When you have steps that need ordering and aren't sure which strategy fits
- As a lookup table for ordering strategies

## Verification
- [ ] Problem characteristics assessed
- [ ] Ordering strategy matched to characteristics
- [ ] Resulting order validated

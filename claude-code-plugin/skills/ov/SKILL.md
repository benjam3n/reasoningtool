---
name: ov
description: "Alternative ordering strategies for procedure steps when the default doesn't fit."
---

# Ordering Strategy Variations

**Input**: $ARGUMENTS

---

## Overview

Alternative ordering strategies for procedure steps. The base order_procedure uses a default prioritization. These variations offer different sequencing philosophies, each optimal for different contexts.

## Steps

### Step 1: Identify the Steps to Order
1. What are the steps/tasks that need sequencing?
2. What are the hard dependencies? (A must come before B)
3. What resources are available?
4. What is the primary concern? (This determines which ordering to use)

### Step 2: Select Ordering Strategy

| Primary Concern | Strategy | Philosophy |
|----------------|----------|-----------|
| Minimize risk | **Risk-First** | Do the scariest things first |
| Maximize learning | **Learning-First** | Do the most uncertain things first |
| Build momentum | **Quick-Win-First** | Do the easiest valuable things first |
| Meet deadline | **Critical-Path** | Do things on the longest dependency chain first |
| Reduce waste | **Value-Stream** | Do things in order of value delivery |
| Handle complexity | **Outside-In** | Start at interfaces, work toward core |
| Handle complexity | **Inside-Out** | Start at core, work toward interfaces |
| Maintain motivation | **Alternating** | Alternate hard and easy tasks |
| Satisfy stakeholders | **Stakeholder-Priority** | Do what the most important stakeholder needs first |
| Manage resources | **Bottleneck-First** | Start with whatever uses the scarcest resource |
| Maximize parallelism | **Independence-First** | Do independent tasks first to enable parallel work |
| Explore options | **Breadth-First** | Survey all options before going deep on any |
| Exploit known good | **Depth-First** | Go deep on most promising path first |

### Step 3: Apply Selected Strategy

**Risk-First Ordering:**
1. List all risks associated with each step
2. Score: likelihood × impact for each
3. Order steps so highest-risk steps come earliest
4. Rationale: Discover showstoppers before investing in everything else

**Learning-First Ordering:**
1. For each step, estimate: how much do we learn by doing it?
2. Order by information value (most informative first)
3. Allow re-planning after high-learning steps
4. Rationale: Reduce uncertainty before committing

**Quick-Win-First Ordering:**
1. For each step, estimate: effort required and value delivered
2. Calculate value/effort ratio
3. Order by ratio (highest first)
4. Rationale: Build momentum and demonstrate progress early

**Critical-Path Ordering:**
1. Map all dependencies
2. Find the longest chain (critical path)
3. Prioritize tasks on the critical path
4. Parallelize non-critical-path tasks
5. Rationale: The critical path determines the timeline

**Value-Stream Ordering:**
1. Identify the flow from start to delivery
2. Order steps to deliver a complete (if minimal) value stream first
3. Then add capability in subsequent passes
4. Rationale: Deliver working value as early as possible

**Outside-In Ordering:**
1. Define the interfaces/boundaries
2. Specify interfaces first
3. Then implement what's behind each interface
4. Rationale: Interfaces constrain everything; define them first

**Inside-Out Ordering:**
1. Identify the core/kernel
2. Build the core first
3. Then add layers outward
4. Rationale: The core determines everything; get it right first

### Step 4: Validate the Ordering
After applying the strategy:

1. Do all hard dependencies hold? (Nothing depends on something that comes later)
2. Does the ordering match the primary concern?
3. Are there any steps that could be parallelized?
4. Is the first step achievable? (Don't start with something blocked)
5. Is there a natural review point after the first few steps?

### Step 5: Compare Alternatives
If unsure which strategy fits:

| Step | Risk-First | Learning-First | Quick-Win | Critical-Path |
|------|-----------|---------------|-----------|--------------|
| [step A] | 2nd | 1st | 3rd | 1st |
| [step B] | 1st | 3rd | 1st | 2nd |
| [step C] | 3rd | 2nd | 2nd | 3rd |

If multiple strategies agree on what comes first → high confidence.
If they disagree → the primary concern should be the tiebreaker.

### Step 6: Report
```
ORDERING STRATEGY:
Steps to order: [N]
Primary concern: [risk/learning/momentum/deadline/value/complexity/motivation]
Strategy selected: [which ordering]

Ordered sequence:
1. [step] — rationale: [why first]
2. [step] — rationale: [why second]
3. [step] — rationale: [why third]
...

Dependencies honored: [yes/no]
Parallelizable steps: [which can run concurrently]
First review point: [after which step]

Alternative orderings considered:
- [strategy]: Would put [step] first instead — better if [condition]
```

## When to Use
- Default ordering doesn't fit the situation
- Context strongly favors one concern (risk, time, learning, etc.)
- Need to compare different ordering approaches
- Building step documents and need to justify sequence
- → INVOKE: /ovi (ordering variations integration) for selecting ordering strategy
- → INVOKE: /to (topological ordering) for dependency-based ordering

## Verification
- [ ] Primary concern identified
- [ ] Strategy matched to concern
- [ ] All hard dependencies respected
- [ ] Ordering rationale stated for each step
- [ ] Alternative strategies considered
- [ ] Parallelizable steps identified

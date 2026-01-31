---
name: "ape - Alphacode Pass 1 Explicit"
description: "First pass at competitive programming — explicit problem decomposition, constraint identification, and straightforward implementation."
---

# Alphacode Pass 1 Explicit

**Input**: $ARGUMENTS

---

## Overview

Pass 1 is about getting the problem RIGHT before getting clever. Explicitly decompose the problem, identify every constraint, enumerate edge cases, and implement the most straightforward correct solution. Optimization comes later.

## Steps

### Step 1: Parse the Problem Statement
1. Read the entire problem statement twice
2. Extract:
   - **Input format**: exact specification
   - **Output format**: exact specification
   - **Constraints**: all numerical bounds (N, M, time, memory)
   - **Guarantees**: what the problem promises about input
3. Restate the problem in your own words
4. What is the problem ACTUALLY asking? (often different from how it's worded)

### Step 2: Classify the Problem Type
1. Core algorithmic category:
   - Graph / DP / Greedy / Math / String / Data structure / Search / Ad hoc
2. Note if combination of types
3. Identify the key insight being tested

### Step 3: Work Through Examples
1. Trace through EVERY provided example by hand
2. Verify your understanding produces expected output
3. If mismatch → problem interpretation is wrong, go back to Step 1
4. Construct 2-3 additional small examples
5. Look for patterns

### Step 4: Identify Edge Cases
1. Minimum input (N=1, empty, single element)
2. Maximum input (upper constraint bounds)
3. All-same input
4. Sorted / reverse sorted
5. Boundary values (0, -1, MAX_INT)
6. Problem-specific (disconnected graph, self-loops, duplicates)
7. Write expected output for each

### Step 5: Design Algorithm
1. Start with brute force
2. Calculate complexity: O(?) time, O(?) space
3. Does brute force pass? If yes → implement it. Simplicity > cleverness in Pass 1.
4. If no → identify bottleneck, determine needed optimization
5. State what each step does, why it's correct, its complexity

### Step 6: Implement
1. Clean, straightforward code
2. Descriptive variable names
3. Handle input parsing carefully (off-by-one = #1 bug)
4. Comment each major section

### Step 7: Test
1. Run against ALL provided examples
2. Run against edge cases from Step 4
3. If failure → don't patch, understand WHY, fix root cause
4. All pass → proceed to /api (Pass 2) if optimization needed

```
PASS 1 RESULT:
Problem type: [classification]
Algorithm: [description]
Complexity: O([time]) time, O([space]) space
Passes constraints: [yes/no]
Edge cases: [N of N passed]
Status: [correct / needs optimization / stuck]
```

## When to Use
- First attempt at any competitive programming problem
- When you need a correct baseline before optimizing

## Verification
- [ ] Problem restated in own words
- [ ] All constraints extracted
- [ ] Every example traced by hand
- [ ] Edge cases enumerated and tested
- [ ] Correctness argued (not just tested)
- [ ] Complexity checked against limits

---
name: "api - Alphacode Pass 2 Implicit"
description: "Second pass at competitive programming — find implicit patterns, hidden structure, and optimizations the explicit pass missed."
---

# Alphacode Pass 2 Implicit

**Input**: $ARGUMENTS

---

## Overview

Pass 2 looks for what the problem is IMPLICITLY telling you. The explicit pass built a correct solution; this pass finds hidden mathematical structure, symmetry that enables a better algorithm, invariants that collapse the search space. This is where O(N^2) becomes O(N log N).

**Prerequisite**: Complete Pass 1 (/ape) first.

## Steps

### Step 1: Identify What the Explicit Solution Wastes
1. Review Pass 1 algorithm
2. Where is redundant work?
3. What could be cached instead of recomputed?
4. What input structure is being ignored?
5. What is the bottleneck operation?

### Step 2: Search for Hidden Structure

**Mathematical:** Closed-form formula? Recurrence? Modular simplification? Bijection to simpler problem?

**Monotonicity:** Answer monotonic in some parameter? → binary search. Two-pointer? Sliding window?

**Decomposition:** Independent subproblems? → divide and conquer. Optimal substructure? → DP.

**Invariants:** Preserved quantity across operations? Conserved quantity?

**Symmetry:** Equivalent simpler form via transformation? Normalization possible?

### Step 3: Check Standard Reductions
Does this reduce to a known problem in disguise?
- Graph hiding as grid/string
- Shortest path hiding as DP
- Max flow/min cut hiding as matching
- Geometry hiding as sorting
- String hiding as tree (suffix structures)

### Step 4: Optimize the Bottleneck
1. State bottleneck: "Step X takes O(?) because [reason]"
2. Apply technique:
   - Repeated lookups → hash map / BST
   - Range queries → segment tree / BIT / sparse table
   - Repeated min/max → monotonic stack/queue
   - Subset enumeration → bitmask DP
   - String matching → KMP / Z-algorithm / hashing
3. Verify optimization preserves correctness
4. Calculate new complexity

### Step 5: Handle Implicit Edge Cases
1. Integer overflow at large values
2. Floating-point precision
3. Hash collisions
4. Worst-case inputs designed to break optimizations
5. Constant factor: right complexity but too slow in practice?

### Step 6: Implement and Verify
1. Modify Pass 1 (don't rewrite — preserve correctness)
2. Compare outputs on all test cases
3. If outputs differ → optimization introduced a bug, bisect
4. Stress test: random inputs, compare Pass 1 vs Pass 2

```
PASS 2 RESULT:
Optimization: [description]
Complexity: O([old]) → O([new]) time
Hidden structure: [what was implicit]
Correctness verified: [yes/no]
Status: [optimized / needs Pass 3 / stuck]
```

## When to Use
- After Pass 1 is correct but too slow
- When constraints suggest a specific complexity class

## Verification
- [ ] Pass 1 baseline exists and is correct
- [ ] Bottleneck identified explicitly
- [ ] Hidden structure search performed systematically
- [ ] Optimization preserves correctness (tested)
- [ ] New complexity verified against limits

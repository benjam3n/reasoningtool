---
name: tp
description: "Arguments form dependency graphs. When any assumption's truth value changes, propagate through all dependent conclusions."
---

# Truth Propagation

**Input**: $ARGUMENTS

---

## Overview

Arguments don't exist in isolation. Each conclusion depends on premises, which depend on other premises, forming a dependency graph. When any assumption's truth value changes, that change must propagate through all dependent conclusions.

This procedure provides mechanisms for:
1. Computing truth scores from dependencies
2. Detecting when conclusions collapse due to failed assumptions
3. Identifying critical assumptions that would cause cascading failures

## Steps

### Step 1: Build the Dependency Graph
Start with the conclusion and trace backward:

1. What is the main conclusion/claim?
2. What premises support it? (List ALL, not just the strongest)
3. For each premise: what supports THAT? (Recurse)
4. Continue until you reach:
   - Axioms (accepted without proof)
   - Empirical observations (directly verified)
   - Assumptions (accepted but not verified)

**Graph notation:**
```
Conclusion C
├── Premise P1 (AND)
│   ├── Evidence E1 [observed, confidence: 0.9]
│   └── Assumption A1 [assumed, confidence: 0.6]
├── Premise P2 (AND)
│   ├── Premise P2a (OR)
│   │   ├── Evidence E2 [observed, confidence: 0.8]
│   │   └── Evidence E3 [observed, confidence: 0.7]
│   └── Assumption A2 [assumed, confidence: 0.5]
└── Premise P3 (AND)
    └── Axiom X1 [accepted, confidence: 1.0]
```

**Dependency types:**
- AND: ALL premises must be true for conclusion to hold
- OR: ANY premise being true is sufficient
- WEIGHTED: Premises contribute proportionally

### Step 2: Assign Truth Values
For each leaf node (bottom of the graph):

| Node | Type | Truth Value | Confidence | Source |
|------|------|-------------|-----------|--------|
| [name] | axiom/evidence/assumption | T/F/U | 0-1 | [how determined] |

T = True, F = False, U = Unknown/Uncertain

### Step 3: Propagate Upward
Calculate truth values for each non-leaf node:

**AND nodes:** confidence = minimum of children's confidences
- If ANY child is False → node is False
- If ALL children are True → node is True (confidence = min)
- If any child is Unknown → node is Unknown (bounded by min)

**OR nodes:** confidence = maximum of children's confidences
- If ANY child is True → node is True (confidence = max)
- If ALL children are False → node is False
- If mix → confidence = max of True/Unknown children

**WEIGHTED nodes:** confidence = weighted average of children's confidences

Propagate from leaves to root. The root node's truth value is the conclusion's truth value.

### Step 4: Sensitivity Analysis
For each assumption node, ask: "What if this were false?"

| Assumption | Current | If False | Conclusion Changes? | Cascade Size |
|-----------|---------|----------|-------------------|-------------|
| A1 | 0.6 | 0 | [yes/no] | [how many nodes affected] |
| A2 | 0.5 | 0 | [yes/no] | [how many nodes affected] |

**Critical assumptions:** Those where flipping to False changes the conclusion.
**Cascade size:** Number of intermediate nodes that change when assumption changes.

### Step 5: Identify Vulnerabilities

**Single points of failure:** AND-dependencies on a single assumption
- If the conclusion requires A AND B AND C, any one failing kills it

**Hidden correlations:** Assumptions that SEEM independent but aren't
- A1 and A2 might both depend on the same underlying condition

**Confidence gaps:** Nodes with low confidence that the conclusion depends on
- The weakest link in an AND-chain determines the chain's strength

### Step 6: What-If Scenarios
Test specific scenarios:

| Scenario | Assumptions Changed | New Conclusion | New Confidence |
|----------|-------------------|---------------|----------------|
| Optimistic | [best case for each assumption] | | |
| Pessimistic | [worst case] | | |
| [Specific] | [change specific assumptions] | | |

### Step 7: Report
```
TRUTH PROPAGATION:
Conclusion: [main claim]
Current truth value: [T/F/U]
Current confidence: [0-1]

Dependency structure:
[graph visualization]

Critical assumptions (conclusion fails if false):
1. [assumption] — current confidence: [value]
2. [assumption] — current confidence: [value]

Vulnerabilities:
- Single points of failure: [list]
- Weakest links: [lowest confidence nodes in critical paths]
- Hidden correlations: [assumptions that may be linked]

Scenario analysis:
| Scenario | Result | Confidence |
|----------|--------|-----------|
| [scenario] | [T/F/U] | [value] |

Recommendation: [how robust is this conclusion]
```

## When to Use
- Evaluating argument strength
- Testing what-if scenarios (what if assumption X is false?)
- Finding critical weak points in reasoning
- Understanding why a conclusion changed
- → INVOKE: /aex (assumption extraction) to find hidden assumptions
- → INVOKE: /ht (hypothesis testing) to verify uncertain assumptions

## Verification
- [ ] Dependency graph complete (all premises traced to leaves)
- [ ] Truth values assigned to all leaf nodes
- [ ] Propagation computed correctly (AND/OR/WEIGHTED rules)
- [ ] Sensitivity analysis performed on all assumptions
- [ ] Critical assumptions identified
- [ ] What-if scenarios tested

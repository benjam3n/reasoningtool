# Universal: Problem Structure (121)

**Category**: META - What Kind of Problem Is This?
**Source**: Optimization theory, computational complexity, mathematical structure
**Structure**: Questions ordered by Value of Information (action divergence)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Is this problem decomposable into independent subproblems?

[VOI: HIGH - decomposable = divide and conquer; interconnected = holistic approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Fully decomposable | HIGH | Solve parts separately | Divide and conquer | Miss interactions |
| Partially decomposable | MED | Some independence | Identify independent parts | Over/under decompose |
| Fully interconnected | HIGH | Must solve holistically | Systems approach | Miss synergies, suboptimize |
| Unknown structure | MED | May waste effort | Structure analysis | Wrong decomposition |

---

## Q2: Are there local optima traps (non-convex)?

[VOI: HIGH - local optima require global search strategies]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Many local optima | HIGH | Hill-climbing fails | Random restarts, global search | Stuck in local optimum |
| Few/no local optima | LOW | Gradient works | Hill-climb confidently | Miss global optimum |
| Unknown landscape | HIGH | May get stuck | Landscape analysis | Wrong search strategy |

---

## Q3: Is the relationship monotonic (more X → more Y)?

[VOI: HIGH - non-monotonic relationships require different reasoning]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Non-monotonic | HIGH | Optimal is in the middle | Find sweet spot | Maximize past optimum |
| Unknown monotonicity | MED | May overshoot | Test relationship | Either undershoot or overshoot |
| Monotonic | LOW | Direction is clear | Maximize/minimize | Miss non-linear region |

---

## Q4: Is there a closed-form solution or must we search?

[VOI: HIGH - closed-form = calculate directly; search = iterate]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Closed-form exists | HIGH | No search needed | Calculate directly | Waste time searching |
| Unknown if exists | MED | May be wasting search | Check for closed-form | Either waste search or miss solution |
| Must search | LOW | Iterative required | Search efficiently | Seek nonexistent formula |

---

## Q5: Is this NP-hard or tractable?

[VOI: HIGH - NP-hard requires approximation/heuristics]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| NP-hard | HIGH | Exact solution infeasible | Heuristics, approximation | Waste resources on exact |
| Unknown complexity | MED | May waste effort | Complexity analysis | Wrong approach |
| Tractable | LOW | Exact solution feasible | Solve exactly | Use heuristics unnecessarily |

---

## Q6: Are constraints tight or loose?

[VOI: MED - affects search strategy but similar process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Very tight constraints | MED | Few feasible solutions | Focus on feasibility | Optimize infeasible |
| Moderate constraints | LOW | Balanced | Balance feasibility/optimality | Misjudge balance |
| Loose constraints | MED | Many feasible solutions | Focus on optimality | Over-constrain artificially |
| Unknown tightness | MED | May misallocate effort | Constraint analysis | Wrong focus |

---

## Q7: Is the objective function well-defined?

[VOI: MED - fuzzy objectives need clarification first]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Objective undefined/fuzzy | HIGH | Can't optimize | Define objective first | Optimize wrong thing |
| Multi-objective | MED | Tradeoffs required | Pareto analysis | Collapse to single metric |
| Single clear objective | LOW | Can optimize directly | Optimize | Actually multi-objective |

---

## Q8: Is there symmetry we can exploit?

[VOI: MED - symmetry reduces search space]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| High symmetry | MED | Search space reducible | Exploit symmetry | Waste effort on equivalent |
| Unknown symmetry | LOW | May be wasting | Symmetry analysis | Miss reduction or see false symmetry |
| No useful symmetry | LOW | Full search required | Search full space | Seek nonexistent shortcuts |

---

## Q9: Is the problem continuous or discrete?

[VOI: LOW - affects tools but similar process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Continuous | LOW | Gradient methods work | Use calculus | Discretize unnecessarily |
| Mixed | LOW | Hybrid methods | Combine approaches | Miss one aspect |
| Discrete | LOW | Combinatorial methods | Use discrete optimization | Apply continuous methods |

---

## Q10: Does the problem have special structure (linear, quadratic, etc.)?

[VOI: LOW - affects efficiency but similar approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Special structure | LOW | Specialized solvers | Use appropriate solver | Miss efficiency gains |
| Unknown structure | LOW | May miss efficiency | Structure analysis | Use wrong solver |
| No special structure | LOW | General methods | Use general solver | Seek nonexistent structure |

---

## Summary Statistics

- Total questions: 10
- Total entries: 40
- HIGH VOI: 10 (25%)
- MED VOI: 14 (35%)
- LOW VOI: 16 (40%)

---

## Question Order by Action Divergence

**Ask first (HIGH VOI):**
1. Q1: Decomposable? - divide-conquer vs holistic
2. Q2: Local optima? - hill-climb vs global search
3. Q3: Monotonic? - direction vs sweet spot
4. Q4: Closed-form? - calculate vs search
5. Q5: NP-hard? - exact vs approximate

**Ask if relevant (MED VOI):**
6. Q6: Constraint tightness? - feasibility vs optimality
7. Q7: Objective defined? - can we even optimize?
8. Q8: Symmetry? - search space reduction

**Low priority (LOW VOI):**
9. Q9: Continuous/discrete? - tool selection
10. Q10: Special structure? - solver selection

---

## Key Insight

**VOI ≠ mathematical sophistication. VOI = action divergence.**

"Does it have special structure?" is technically interesting but has LOW VOI - you use general methods if unsure.

"Is it decomposable?" has HIGH VOI - decomposable means you can parallelize and simplify; interconnected means you must solve holistically.

---

## The Structure Determines the Strategy

Wrong structure assumption → wrong strategy → wasted effort or wrong answer.

- Assume convex when non-convex → stuck in local optimum
- Assume decomposable when interconnected → suboptimal from missed interactions
- Assume tractable when NP-hard → waste resources on impossible exact solution

Spend time on structure analysis before diving into search.

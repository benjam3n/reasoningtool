# Universal: Dimensionality and Sparsity (129)

**Category**: META - How Complex Is the Search Space?
**Source**: Machine learning, optimization theory, high-dimensional spaces
**Structure**: Questions ordered by Value of Information (action divergence)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: How many independent dimensions does this problem have?

[VOI: HIGH - high dimensionality requires fundamentally different strategies]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Very high dimensional | HIGH | Curse of dimensionality | Dimensionality reduction, heuristics | Exhaustive search of infinite space |
| Unknown dimensionality | MED | May waste effort | Dimension counting | Either over-search or under-search |
| Low dimensional | LOW | Exhaustive search possible | Systematic search | Miss dimensions |

---

## Q2: Is the reward/success signal sparse or dense?

[VOI: HIGH - sparse rewards require exploration strategies]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Very sparse rewards | HIGH | Random search fails | Curiosity-driven, exploration bonus | Random search, never find reward |
| Unknown sparsity | MED | May waste search | Sparsity assessment | Either over or under explore |
| Dense rewards | LOW | Gradient available | Follow gradient | Explore when gradient available |

---

## Q3: Are most dimensions irrelevant (can we project to lower space)?

[VOI: HIGH - irrelevant dimensions = wasted search]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Most dimensions irrelevant | HIGH | Can simplify dramatically | Find core dimensions | Search noise |
| Unknown relevance | MED | May be wasting | Feature selection | Either over-search or miss relevant |
| Most dimensions relevant | LOW | Must search full space | Full search | Miss dimension by projecting |

---

## Q4: Is there structure that reduces effective complexity?

[VOI: HIGH - structure enables tractability]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Hidden structure exists | HIGH | Exploitable | Find and exploit structure | Brute force when structure available |
| Unknown if structure | MED | May miss efficiency | Structure discovery | Either miss or waste search |
| No exploitable structure | LOW | Brute force only | Brute force | Seek nonexistent structure |

---

## Q5: Are there interaction effects between dimensions?

[VOI: HIGH - interactions prevent decomposition]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Strong interactions | HIGH | Can't optimize independently | Joint optimization | Miss interaction, suboptimal |
| Unknown interactions | MED | May suboptimize | Interaction testing | Either miss interactions or over-search |
| Dimensions independent | LOW | Can optimize separately | Decompose problem | Miss interaction |

---

## Q6: Is there a feasibility boundary we need to respect?

[VOI: MED - feasibility affects search strategy but similar process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Feasibility critical | MED | Must stay in bounds | Constraint-aware search | Explore infeasible, wasted |
| Unknown feasibility | MED | May explore invalid | Boundary mapping | Either explore invalid or miss valid |
| No feasibility constraint | LOW | Unconstrained | Free exploration | Constrain unnecessarily |

---

## Q7: Is the good region small or large?

[VOI: MED - affects search difficulty]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Good region tiny | MED | Needle in haystack | Targeted search, heuristics | Random search, never find |
| Unknown region size | MED | May use wrong method | Region estimation | Wrong search intensity |
| Good region large | LOW | Easy to find | Loose search sufficient | Over-search easy problem |

---

## Q8: Are there multiple good regions or just one?

[VOI: MED - affects search exhaustiveness]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Multiple good regions | MED | Don't stop at first | Keep searching after first | Settle when better exists |
| Unknown count | MED | May miss | Region counting | Either miss or over-search |
| Single good region | LOW | One target | Stop when found | Search when found |

---

## Q9: Does the solution landscape have plateaus?

[VOI: LOW - affects local search but similar process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Many plateaus | LOW | Gradient uninformative locally | Momentum, random restarts | Stuck on plateau |
| Unknown landscape | LOW | May get stuck | Landscape probing | Either stuck or paranoid |
| No plateaus | LOW | Smooth gradients | Follow gradient | Seek plateaus |

---

## Q10: Is distance in this space meaningful?

[VOI: LOW - affects similarity but similar process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Distance meaningful | LOW | Nearby = similar | Use distance metrics | Miss that distance meaningless |
| Unknown if meaningful | LOW | May be misled | Metric validation | Either miss or paranoid |
| Distance misleading | LOW | Nearby ≠ similar | Don't trust proximity | Trust false proximity |

---

## Summary Statistics

- Total questions: 10
- Total entries: 38
- HIGH VOI: 10 (26%)
- MED VOI: 14 (37%)
- LOW VOI: 14 (37%)

---

## Question Order by Action Divergence

**Ask first (HIGH VOI):**
1. Q1: How many dimensions? - search strategy
2. Q2: Sparse or dense rewards? - exploration strategy
3. Q3: Most dimensions irrelevant? - simplification
4. Q4: Exploitable structure? - tractability
5. Q5: Interaction effects? - decomposability

**Ask if relevant (MED VOI):**
6. Q6: Feasibility boundary? - constraints
7. Q7: Good region size? - search difficulty
8. Q8: Multiple good regions? - exhaustiveness

**Low priority (LOW VOI):**
9. Q9: Plateaus? - local search issues
10. Q10: Distance meaningful? - similarity metrics

---

## Key Insight

**VOI ≠ technical sophistication about search spaces. VOI = action divergence.**

"Is distance meaningful?" is technically interesting but has LOW VOI - you do similar search regardless.

"How many independent dimensions?" has HIGH VOI - high dimensionality makes exhaustive search impossible, requiring completely different strategies.

---

## The Curse of Dimensionality

In high dimensions:
- Volume concentrates in corners and near surfaces
- Distance metrics become less meaningful
- Random sampling is hopeless
- Exhaustive search is impossible

The heuristics:
1. **Reduce dimensions first**: Find the 3-5 dimensions that actually matter
2. **Exploit structure**: Look for patterns that make the space navigable
3. **Use domain knowledge**: Prior knowledge beats blind search
4. **Accept approximation**: You won't find optimal, find good enough

The meta-insight: Before searching, understand the space. A moment spent understanding dimensionality saves hours of futile search.

---

## Sparsity and Exploration

Dense rewards: Every step gives feedback. Gradient descent works.
Sparse rewards: Long stretches of nothing, then a signal.

In sparse reward landscapes:
- Random exploration fails
- Need curiosity/novelty as proxy reward
- Need to remember where you've been
- May need demonstrations or curriculum

The sparsest reward: Success/failure at the end. No intermediate signal.

Ask early: How sparse is the feedback? This determines everything about search strategy.

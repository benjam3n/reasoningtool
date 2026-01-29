# Universal: Coverage Strategy (100)

**Category**: META - How To Cover The Space
**Source**: Derived from space discovery procedure
**Structure**: Questions ordered by Value of Information (action divergence)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: What coverage mode is appropriate?

[VOI: HIGH - completely different approaches]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| EXHAUSTIVE | HIGH | Cover everything | Complete but expensive | Waste resources on large space |
| BOUNDARY | HIGH | Map edges, sample interior | Handle huge spaces | False confidence from edges |
| ADAPTIVE | MED | Start broad, go deep | Flexible, efficient | Miss signal in unexplored |
| TARGETED | MED | Focus on high-value | Efficient if priorities known | Miss high-value not targeted |

---

## Q2: Are there coverage dependencies?

[VOI: HIGH - wrong order can break everything]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, strict order | HIGH | Must sequence | Correct dependencies | Wrong order → broken coverage |
| Yes, soft order | MED | Preferred sequence | Efficient | May work out of order |
| No, independent | MED | Cover in any order | Flexible | Miss hidden dependencies |
| Unknown | MED | Need to analyze | Dependencies before coverage | Discover via errors |

---

## Q3: What's the stopping criterion?

[VOI: HIGH - determines when done]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Error rate threshold | HIGH | Quality-based | Validated quality | Threshold may be wrong |
| 100% coverage | MED | Complete | Truly done | Never done if space large |
| Diminishing returns | MED | Efficiency-based | Optimal investment | Stop too early if appreciating |
| Time/budget exhausted | LOW | Practical | Realistic stopping | Stop at arbitrary point |
| Unknown | MED | Need to define | Explicit criterion | Never know when done |

---

## Q4: How do we identify high-value regions?

[VOI: MED - affects efficiency but similar process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| User feedback | MED | Demand-driven | Match actual needs | Users don't know needs |
| Prior knowledge | MED | Leverage expertise | Efficient targeting | Expertise gaps |
| Exploration/sampling | MED | Discover empirically | Find unknowns | Slow, miss rare high-value |
| Proxy metrics | LOW | Measurable indicators | Scalable | Proxies may mislead |

---

## Q5: How do we verify coverage?

[VOI: MED - affects confidence but similar approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Usage feedback | MED | Real-world validation | Actual coverage | Feedback delayed, gaps harm |
| Testing/sampling | MED | Empirical verification | Evidence-based | Samples may miss gaps |
| Checklist | LOW | Explicit verification | Simple, clear | Checklist may be incomplete |
| Formal proof | LOW | Mathematical certainty | Guaranteed | Proof may not match reality |

---

## Q6: Should we prioritize breadth or depth?

[VOI: MED - strategy choice but similar work]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Breadth first | MED | Survey all regions | Map before committing | Shallow everywhere |
| Depth first | MED | Exhaust one region | Master before moving | Miss other regions |
| Adaptive | MED | Switch based on signal | Responsive | Miss patterns needing consistency |
| Balanced | LOW | Mix approaches | Flexible | Neither sufficient |

---

## Q7: Should we cover edge cases?

[VOI: MED - affects completeness but similar work]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, all edges | MED | Complete | Robust | Over-invest in rare cases |
| High-impact edges only | MED | Prioritized | Efficient | Miss low-probability high-impact |
| No, focus on common | LOW | Practical | Efficient for typical | Fail on edge cases |
| Unknown | MED | Need risk analysis | Informed decision | Random edge coverage |

---

## Q8: What's the re-coverage strategy?

[VOI: MED - affects maintenance but similar process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Never | HIGH | One-time investment | Done forever | Coverage goes stale |
| Periodic full re-coverage | MED | Fresh start | Catch all changes | Expensive, may not change |
| Triggered by change | MED | Event-driven | Efficient | Miss undetected changes |
| Continuous partial | LOW | Rolling updates | Balanced | Never fully fresh |

---

## Q9: What's the cost of redundant coverage?

[VOI: LOW - efficiency detail]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| High (waste resources) | LOW | Minimize overlap | Efficient | Miss edge cases between |
| Low (reinforcement OK) | LOW | Allow overlap | Robust coverage | Over-invest in redundancy |
| Varies by region | LOW | Selective redundancy | Tailored | Wrong regions get redundancy |
| Unknown | LOW | Need to analyze | Cost before strategy | Over/under overlap |

---

## Q10: Can coverage be incremental?

[VOI: LOW - timing detail]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, add over time | LOW | Sustainable | Build gradually | Gaps persist too long |
| No, needs batch | LOW | Coherent coverage | Complete before using | Delay value delivery |
| Partially | LOW | Hybrid approach | Balance | Neither benefit |
| Depends on dependencies | LOW | Ordered coverage | Prerequisite-aware | Miss dependencies |

---

## Summary Statistics

- Total questions: 10
- Total entries: 40
- HIGH VOI: 7 (18%)
- MED VOI: 22 (55%)
- LOW VOI: 11 (28%)

---

## Question Order by Action Divergence

**Ask first (HIGH VOI):**
1. Q1: Coverage mode? - exhaustive vs boundary vs targeted
2. Q2: Coverage dependencies? - order matters
3. Q3: Stopping criterion? - when done

**Ask if relevant (MED VOI):**
4. Q4: Identify high-value regions? - targeting
5. Q5: Verify coverage? - validation
6. Q6: Breadth or depth? - strategy
7. Q7: Cover edge cases? - completeness
8. Q8: Re-coverage strategy? - maintenance

**Low priority (LOW VOI):**
9. Q9: Cost of redundancy? - efficiency detail
10. Q10: Incremental coverage? - timing detail

---

## Key Insight

**VOI ≠ strategic sophistication. VOI = action divergence.**

"Should we cover edge cases?" seems strategic but has MED VOI - you still do similar coverage work.

"What coverage mode?" has HIGH VOI - exhaustive vs boundary are completely different approaches.

---

## Usage Note

This category should be invoked AFTER space size estimation. The coverage mode depends on space characteristics.

→ Prerequisite: 99_space_size.md
→ Pairs with: 101_adjacent_spaces.md (for cross-space coverage)

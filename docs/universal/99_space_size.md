# Universal: Space Size Estimation (99)

**Category**: META - How Big Is The Possibility Space
**Source**: Derived from space discovery procedure
**Structure**: Questions ordered by Value of Information (action divergence)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Is this space finite or infinite?

[VOI: HIGH - determines whether exhaustive coverage is even possible]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Finite | HIGH | Can plan exhaustive coverage | Set coverage target | Overwhelmed trying to exhaust infinite |
| Infinite | HIGH | Must sample/bound | Accept incompleteness | False completion, missed regions |
| Practically infinite | MED | Treat as infinite | Prioritize ruthlessly | Waste time on low-value regions |
| Unknown | HIGH | Must determine first | Size before strategy | Strategy without sizing fails |

---

## Q2: Are regions of this space equally important?

[VOI: HIGH - determines whether to cover evenly or target]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, clustered | HIGH | Find the clusters | Target high-value regions | Waste time on low-value |
| Power law (80/20) | HIGH | Find the vital few | Target 20% that matters | Exhaust the trivial many |
| Yes, uniform | MED | Cover evenly | Random sampling works | Miss high-value clusters |
| Unknown | MED | Explore to discover | Discovery phase first | Commit to wrong regions |

---

## Q3: What's the cost of missing a region?

[VOI: HIGH - determines investment level in coverage]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Catastrophic | HIGH | Must cover all | Exhaustive even if expensive | Catastrophic failure from gap |
| Significant | MED | Prioritize coverage | High investment justified | Under-invest, suffer losses |
| Minor | MED | Accept some gaps | Sample efficiently | Over-invest in completeness |
| Unknown | MED | Need to assess | Risk analysis first | Wrong coverage level |

---

## Q4: Can the space be reduced or decomposed?

[VOI: HIGH - changes whether to solve holistically or divide]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, fully coupled | HIGH | Must consider together | Holistic approach | False decomposition breaks |
| Yes, orthogonal | MED | Solve independently | Divide and conquer | Create false dependencies |
| Yes, hierarchical | MED | Solve top-down | Leverage structure | Miss cross-cutting concerns |
| Unknown | MED | Need to analyze | Structure before coverage | Wrong decomposition |

---

## Q5: How many dimensions does this space have?

[VOI: MED - affects complexity but not fundamental approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| 10+ dimensions | MED | Cannot exhaustively cover | Boundary/targeted mode | Pretend full coverage |
| 6-10 dimensions | MED | Combinatorial explosion | Sample strategically | Try to exhaust, fail |
| 3-5 dimensions | LOW | Manageable complexity | Structured exploration | Underestimate combinations |
| 1-2 dimensions | LOW | Simple, map easily | Exhaustive coverage | Miss hidden dimensions |

---

## Q6: Are there natural boundaries to the space?

[VOI: MED - affects stopping criterion but similar process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, unbounded | MED | Must impose limits | Artificial but necessary | Never stop, never finish |
| Fractal (infinite at any scale) | MED | Depth limits required | Set resolution | Infinite recursion |
| Yes, fuzzy | LOW | Approximate stopping | Reasonable cutoff | Over/under extend |
| Yes, clear | LOW | Know when done | Stop at boundaries | Stop too early or late |

---

## Q7: What is the estimated number of combinations?

[VOI: MED - affects effort but similar approach patterns]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| >10000 | MED | Huge, must sample | Boundary coverage | False sense of completeness |
| 1000-10000 | MED | Large, must prioritize | Targeted coverage | Spread too thin |
| 100-1000 | LOW | Medium, structured | Adaptive coverage | Over/under invest |
| <100 | LOW | Small, cover all | Exhaustive mode | Miss something |

---

## Q8: How fast is the space changing?

[VOI: MED - affects maintenance but not initial approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unpredictable | MED | Cannot pre-cover | Reactive capability | Static coverage fails |
| Fast change | MED | Continuous coverage | Real-time adaptation | Coverage goes stale |
| Slow change | LOW | Periodic updates | Maintenance mode | Over/under update |
| Static | LOW | Cover once, done | Investment persists | Miss that it changed |

---

## Q9: How much of the space is already explored?

[VOI: LOW - affects starting point but similar process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| None (greenfield) | LOW | Start fresh | Discovery mode | Redo existing work |
| Partially explored | LOW | Build on existing | Incremental | Redo or miss gaps |
| Mostly explored | LOW | Find remaining gaps | Gap analysis | Think done, have gaps |
| Fully explored | LOW | Refinement only | Quality over quantity | Add redundant coverage |

---

## Q10: Can we detect missed regions?

[VOI: LOW - affects confidence but not approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No | LOW | Flying blind | Invest heavily upfront | False confidence |
| Only via errors | LOW | Learn from failures | Error-driven discovery | Errors harm before learning |
| Yes, probabilistically | LOW | Statistical validation | Sample-based QA | Miss deterministic gaps |
| Yes, systematically | LOW | Quality assurance | Coverage testing | False confidence from tests |

---

## Summary Statistics

- Total questions: 10
- Total entries: 40
- HIGH VOI: 10 (25%)
- MED VOI: 18 (45%)
- LOW VOI: 12 (30%)

---

## Question Order by Action Divergence

**Ask first (HIGH VOI):**
1. Q1: Finite or infinite? - determines if exhaustive is possible
2. Q2: Regions equally important? - target vs cover evenly
3. Q3: Cost of missing region? - investment level
4. Q4: Can space be decomposed? - holistic vs divide

**Ask if relevant (MED VOI):**
5. Q5: How many dimensions? - complexity
6. Q6: Natural boundaries? - stopping criterion
7. Q7: Number of combinations? - scale
8. Q8: How fast changing? - maintenance

**Low priority (LOW VOI):**
9. Q9: Already explored? - starting point
10. Q10: Can detect missed? - confidence

---

## Key Insight

**VOI ≠ mathematical precision. VOI = action divergence.**

"What is the exact number of combinations?" feels precise but has MED/LOW VOI - you still use similar coverage strategies.

"Is this space finite or infinite?" has HIGH VOI - infinite spaces require fundamentally different approaches than finite ones.

---

## Usage Note

This category should be invoked BEFORE deciding coverage strategy. Space size determines whether to pursue exhaustive, adaptive, targeted, or boundary coverage.

→ Pairs with: 100_coverage_strategy.md

# Universal: Combinatorial (70)

**Category**: MATHEMATICAL - Counting and Combinations
**Source**: [O: universal_goal_analysis.yaml lines 2377-2400 combinatorial category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: How many possibilities exist?
[VOI: MED - scale determines search approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Large (cannot enumerate) | MED | Need heuristics vs exhaustive | Smart search | Actually small |
| Infinite | MED | Need cutoff criteria vs search all | Criteria needed | Finite |
| Unknown count | MED | Count estimation vs proceed blind | Count estimation | Count known |
| Small (can enumerate) | LOW | Try all possibilities | Exhaustive possible | Actually large |

---

## Q2: Is the count finite or infinite?
[VOI: MED - infinite requires different approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Infinite | MED | Need cutoff criteria vs eventually cover | Define criteria | Finite |
| Unknown finiteness | MED | Finiteness check vs assume bounded | Finiteness check | Finiteness known |
| Finite | LOW | Bounded search possible | Can eventually cover | Infinite |

---

## Q3: Can the count be reduced by eliminating invalid possibilities?
[VOI: MED - pruning affects search efficiency]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, significant reduction | MED | Aggressive pruning vs full search | Prune aggressively | Minor/no reduction |
| Unknown if reducible | MED | Reduction analysis vs full search | Reduction analysis | Reducibility known |
| Yes, minor reduction | LOW | Light pruning vs full search | Light pruning | Different level |
| No reduction possible | LOW | Full space search | Complete search | Reduction possible |

---

## Q4: Does order matter (permutation) or not (combination)?
[VOI: MED - affects count and search strategy]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Order matters (permutation) | MED | More possibilities, factor order | Factor in order | Order doesn't matter |
| Unknown if order matters | MED | Order analysis vs assume | Order analysis | Order known |
| Order doesn't matter | LOW | Fewer possibilities, ignore order | Ignore order | Order matters |

---

## Q5: Are repetitions allowed?
[VOI: MED - repetitions affect count]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, with replacement | MED | More possibilities vs without | Factor repetition | Without replacement |
| Unknown if repetition | MED | Repetition check vs assume | Repetition check | Repetition known |
| No, without replacement | LOW | Each element once | Each once | With replacement |

---

## Q6: Does the problem involve selecting a subset from a set?
[VOI: LOW - problem structure identification]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, subset selection | LOW | Use combinatorics | Use combinatorics | Not subset |
| No, not subset | LOW | Different structure | Other approach | Subset selection |
| Unknown if subset | LOW | Structure check | Structure check | Structure known |

---

## Q7: How many total combinations/permutations exist?
[VOI: MED - affects planning for search]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Count estimated | MED | Approximate planning | Plan accordingly | Different count |
| Count unknown | MED | Count calculation needed | Count calculation | Count known |
| Count known | LOW | Use known count for planning | Use count | Count unknown |

---

## Q8: Does the problem involve dividing something into parts?
[VOI: MED - partition vs selection is different structure]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, partitioning | MED | Use partition methods | Use partition methods | Not partitioning |
| Unknown if partitioning | LOW | Structure check | Structure check | Structure known |
| No, not partitioning | LOW | Different structure | Other approach | Partitioning |

---

## Q9: What are the constraints on parts?
[VOI: MED - tight constraints limit valid partitions]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Tight constraints | MED | Few valid partitions, constraint satisfaction | Constraint satisfaction | Loose constraints |
| Unknown constraints | MED | Constraint discovery | Constraint discovery | Constraints known |
| Loose constraints | LOW | Many valid partitions | Choose criteria | Tight constraints |
| No constraints | LOW | Any partition works | Freedom | Constraints exist |

---

## Q10: Is there an optimal partition?
[VOI: MED - optimization vs satisficing]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, optimal unknown | MED | Optimization search needed | Optimization | Different state |
| Unknown if optimal exists | MED | Optimality check | Optimality check | Optimality known |
| Yes, optimal known | LOW | Use optimal partition | Apply optimal | Suboptimal or no optimal |
| No optimal (many equal) | LOW | Pick any valid partition | Pick convenient | Optimal exists |

---

## Coverage Summary

```
QUESTIONS: 10
ENTRIES: 40

VOI Distribution:
- HIGH: 0 entries (0%)
- MED: 20 entries (50%)
- LOW: 20 entries (50%)

Note: Very low HIGH% because combinatorial analysis is usually calculation refinement
```

---

## Question Order by Action Divergence

**No HIGH VOI questions** - combinatorial analysis typically affects approach efficiency, not fundamental direction

**MED VOI (ask first - same direction, different approach):**
1. Q1 (Possibility count?) - scale of search
2. Q2 (Finite?) - bounded or not
3. Q3 (Reducible?) - pruning opportunity
4. Q4 (Order matters?) - permutation vs combination
5. Q5 (Repetitions?) - with/without replacement
6. Q7 (Count?) - planning for search
7. Q8 (Partitioning?) - problem structure
8. Q9 (Constraints?) - valid partition limits
9. Q10 (Optimal?) - optimization needed

**LOW VOI:**
10. Q6 (Subset selection?) - structure identification

---

## Key Insight

**VOI ≠ computational difficulty**

**VOI = action divergence**

No questions in this library are HIGH VOI because combinatorial analysis is about HOW you search, not WHETHER you search or WHAT you search for. The fundamental direction is already set; these questions refine the approach.

Q1 "How many possibilities?" is MED VOI because:
- SMALL → try all
- LARGE → use heuristics (same goal, different search method)

Contrast with Q1 from path analysis: "Does path exist?" which is HIGH VOI because:
- YES → traverse path
- NO → change goal entirely (completely different work)

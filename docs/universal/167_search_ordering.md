# Universal: Search Ordering (167)

**Category**: SEARCH - What Order To Search?
**Source**: Search algorithms, heuristics, information theory
**Structure**: Questions ordered by Value of Information (action divergence)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Core Insight

**Order determines what you find before you stop.**

Since most searches terminate before exhausting the space, ordering determines:
- What you find (early items more likely to be seen)
- How fast you find it (good ordering = fewer steps)
- Whether you find it at all (bad ordering = stop before reaching it)

The best ordering front-loads high-probability, high-value candidates.

---

## Q1: What ordering maximizes expected value per step?

[VOI: HIGH - core ordering decision]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Can estimate candidate values | HIGH | Order by expected value | Search best-first | Miss high-value early |
| Can estimate probabilities | HIGH | Order by probability | Search likely-first | Waste time on unlikely |
| Can estimate both | HIGH | Order by EV × probability | Optimal ordering | Suboptimal path |
| Can't estimate either | MED | Use heuristics | Apply domain knowledge | Random search |

---

## Q2: Is there structure to exploit?

[VOI: HIGH - structure enables efficient ordering]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Hierarchical structure | HIGH | Search top-down or bottom-up | Prune branches early | Flat search of structured space |
| Spatial/similarity structure | HIGH | Search neighbors of good candidates | Local search | Miss nearby good options |
| No exploitable structure | MED | Systematic or random | Cover space evenly | Assume structure that isn't there |

---

## Q3: Should you go deep or wide first?

[VOI: HIGH - fundamental search strategy]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Deep first (depth-first) | HIGH | Explore one path fully before switching | Find deep solutions | Miss breadth |
| Wide first (breadth-first) | HIGH | Explore all options at each level | Find shallow solutions | Miss depth |
| Iterative deepening | MED | Alternate deep and wide | Balance both | More overhead |
| Depends on problem | HIGH | Assess problem structure | Match strategy to problem | Mismatch |

**When to go deep**: Solutions are deep, branching factor is high, memory limited
**When to go wide**: Solutions are shallow, need to compare options, deep paths risky

---

## Q4: What's the cost of evaluating each candidate?

[VOI: HIGH - evaluation cost affects ordering]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Uniform cost | MED | Order by value alone | Simple ordering | N/A |
| Variable cost | HIGH | Order by value/cost ratio | Cheap evaluations first | Expensive evaluations early waste resources |
| Evaluation cost unknown | MED | Estimate or use proxies | Approximate | Bad estimates |

---

## Q5: Is there information to gather that improves ordering?

[VOI: HIGH - meta-search decision]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, cheap info available | HIGH | Gather info first, then order | Better ordering | Search blind |
| Yes, but expensive | MED | Trade off info cost vs search cost | Calculate value of information | Over/under invest in info |
| No useful info available | LOW | Proceed with current ordering | Best guess | Seek info that doesn't exist |

---

## Q6: Should you search randomly or systematically?

[VOI: MED - search style]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Systematically | MED | Cover space methodically | Complete coverage | Predictable, miss random hits |
| Randomly | MED | Sample space stochastically | Escape local optima | Miss systematic opportunities |
| Hybrid | LOW | Mix systematic and random | Balance | More complex |

**Systematic when**: Space is small, complete coverage needed, structure is clear
**Random when**: Space is huge, local optima likely, little structure

---

## Q7: Are there "must check" candidates?

[VOI: MED - priority candidates]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, obvious candidates | MED | Check these first | Clear high-value fast | Miss if wrong |
| No obvious candidates | LOW | Use general ordering | Systematic approach | Miss obvious |

---

## Q8: What's been tried before?

[VOI: MED - learning from history]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Similar searches done before | MED | Start where previous succeeded | Leverage history | Repeat failures |
| No relevant history | LOW | Start fresh | Systematic | Miss transferable knowledge |

---

## Q9: Can ordering be updated during search?

[VOI: MED - adaptive vs fixed ordering]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, can reorder | MED | Update based on findings | Learn and adapt | Static when should adapt |
| No, order is fixed | LOW | Choose best initial order | Careful upfront planning | Try to adapt when can't |

---

## Q10: Is there an adversary or competition?

[VOI: LOW - game-theoretic considerations]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, competing searchers | LOW | Avoid predictable ordering | Randomize or differentiate | Predictable, get outcompeted |
| No competition | LOW | Optimize for self | Best ordering for you | Unnecessary randomization |

---

## Summary Statistics

- Total questions: 10
- HIGH VOI: 7
- MED VOI: 9
- LOW VOI: 4

---

## Question Order by Action Divergence

**Ask first (HIGH VOI):**
1. Q1: What ordering maximizes expected value per step?
2. Q2: Is there structure to exploit?
3. Q3: Should you go deep or wide first?
4. Q4: What's the cost of evaluating each candidate?
5. Q5: Is there information to gather that improves ordering?

**Ask if relevant (MED VOI):**
6. Q6: Random or systematic?
7. Q7: Are there "must check" candidates?
8. Q8: What's been tried before?
9. Q9: Can ordering be updated during search?

**Low priority (LOW VOI):**
10. Q10: Is there an adversary?

---

## Ordering Strategies

| Strategy | How It Works | Best When |
|----------|--------------|-----------|
| **Best-first** | Order by expected value | Can estimate values |
| **Cheapest-first** | Order by evaluation cost | Variable costs, similar values |
| **Most-informative-first** | Order by info gained | Learning improves later search |
| **Depth-first** | Exhaust one path before switching | Deep solutions, high branching |
| **Breadth-first** | All options at each level | Shallow solutions, need comparison |
| **Random** | Stochastic sampling | Huge space, local optima risk |
| **Nearest-neighbor** | Search similar to current best | Clustered good solutions |

---

## Ordering Heuristics by Domain

| Domain | Typical Good Ordering |
|--------|----------------------|
| **Problem solving** | Most constrained variable first |
| **Learning** | Foundational concepts first |
| **Debugging** | Most likely cause first |
| **Hiring** | Strongest signals first |
| **Research** | Highest-impact questions first |
| **Negotiation** | Easiest issues first (build momentum) |

---

## Common Ordering Errors

| Error | Pattern | Fix |
|-------|---------|-----|
| **Availability ordering** | Search what comes to mind first | Deliberately generate alternatives |
| **Recency ordering** | Search recent things first | Consider older options |
| **Ease ordering** | Search easy things first | Consider hard but valuable |
| **Fixed ordering** | Never reorder based on findings | Update ordering dynamically |
| **Random when structured** | Random search of structured space | Exploit structure |

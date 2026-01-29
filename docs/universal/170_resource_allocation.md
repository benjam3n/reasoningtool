# Universal: Resource Allocation (170)

**Category**: SEARCH - How To Allocate Search Effort?
**Source**: Portfolio theory, attention economics, parallel search
**Structure**: Questions ordered by Value of Information (action divergence)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Core Insight

**Search consumes resources. Allocation determines what gets found.**

Resources include:
- Time
- Attention
- Money
- Cognitive effort
- Opportunity cost

Bad allocation = searching the wrong things with the wrong intensity.

---

## Q1: What resources are scarce for this search?

[VOI: HIGH - scarcity determines constraints]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Time is scarce | HIGH | Optimize for speed | Fast heuristics | Miss by rushing |
| Attention is scarce | HIGH | Optimize for focus | Few deep dives | Miss peripheral |
| Money is scarce | MED | Optimize for cost | Cheap methods | Miss expensive but valuable |
| All abundant | LOW | Thorough search | Completeness | Overkill |

---

## Q2: Should effort be concentrated or distributed?

[VOI: HIGH - focus vs diversification]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Concentrate on best bet | HIGH | Deep dive on most promising | Thoroughness in one area | Miss if wrong bet |
| Distribute across options | HIGH | Shallow coverage of many | Hedge against uncertainty | Jack of all trades |
| Sequential concentration | MED | Deep on one, then next | Best of both | Slower |

**Concentrate when:** High confidence in area, returns to depth, low cost of missing others
**Distribute when:** Low confidence, diminishing returns to depth, high cost of missing

---

## Q3: What's the search budget?

[VOI: HIGH - budget constrains strategy]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Fixed budget | HIGH | Allocate within constraint | Disciplined search | May need more |
| Flexible budget | MED | Spend until diminishing | Optimal stopping | May overspend |
| Unknown budget | HIGH | Estimate before allocating | Plan with limits | Run out unexpectedly |

---

## Q4: Can search be parallelized?

[VOI: MED - parallel vs sequential]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, can parallelize | MED | Search multiple paths simultaneously | Speed | Coordination cost |
| No, must be sequential | MED | Optimize order | Careful sequencing | Try to parallelize what can't be |
| Partially | MED | Parallelize what's independent | Balance | Suboptimal mix |

---

## Q5: What's the exploration-exploitation allocation?

[VOI: MED - classic tradeoff]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Mostly explore | MED | Learn about space | Better long-term | Miss short-term gains |
| Mostly exploit | MED | Harvest best known | Capture value | Miss better options |
| Balance (e.g., 80/20) | LOW | Allocate percentage to each | Hedge | Suboptimal if wrong ratio |

---

## Q6: Should you invest in search infrastructure?

[VOI: MED - meta-investment decision]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, infrastructure pays off | MED | Build tools, systems | Better future search | Upfront cost |
| No, one-time search | LOW | Direct search only | Efficient for once | Miss reusable value |

---

## Q7: What's the marginal value of additional resources?

[VOI: MED - diminishing returns assessment]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| High marginal value | MED | Invest more | Better outcomes | Overspend |
| Low marginal value | MED | Stop investing | Save resources | Miss by underspending |
| Unknown | MED | Test incrementally | Learn by doing | Inefficient learning |

---

## Q8: Are there minimum viable allocations?

[VOI: LOW - threshold effects]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, below threshold is wasted | LOW | Meet threshold or skip | Efficient | Miss opportunities below threshold |
| No, any amount helps | LOW | Spread thin OK | More coverage | Ineffective spreading |

---

## Summary Statistics

- Total questions: 8
- HIGH VOI: 4
- MED VOI: 8
- LOW VOI: 3

---

## Allocation Strategies

| Strategy | How It Works | Best When |
|----------|--------------|-----------|
| **Equal allocation** | Same resources to each option | High uncertainty, similar EV |
| **Proportional to EV** | More resources to higher expected value | Can estimate EV |
| **Winner-take-all** | All resources to best option | High confidence, returns to concentration |
| **Minimax** | Ensure minimum coverage everywhere | High cost of missing anything |
| **Adaptive** | Reallocate based on results | Learning is cheap, space is dynamic |

---

## Common Allocation Errors

| Error | Pattern | Fix |
|-------|---------|-----|
| **Peanut buttering** | Spread too thin, nothing gets enough | Prioritize ruthlessly |
| **Over-concentration** | All eggs in one basket | Hedge against uncertainty |
| **Sunk cost allocation** | Allocate to past investment, not future value | Forward-looking allocation |
| **Squeaky wheel** | Allocate to loudest demand | Assess actual value |
| **Equal allocation by default** | Split evenly without thinking | Estimate relative value |

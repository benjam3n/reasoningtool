# Universal: Requirement Analysis (46)

**Category**: CORE - Recursive Requirements
**Source**: [O: universal_goal_analysis.yaml lines 1234-1339 requirement_analysis category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Are any requirements infeasible?
[VOI: HIGH - Some infeasible means find alternatives vs execute path]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Some infeasible | HIGH | Find alternatives vs execute | Find alternatives | All feasible |
| Unknown feasibility | HIGH | Feasibility analysis vs assume | Feasibility analysis | Feasibility known |
| All feasible | LOW | Execute path either way | Execute path | Some infeasible |

---

## Q2: Is there an alternative way to satisfy conditions?
[VOI: HIGH - Better alternative means switch paths vs current path]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, better alternative | HIGH | Switch paths vs current | Use alternative | Current is best |
| Unknown alternatives | MED | Search first vs proceed | Alternative search | Alternatives known |
| Yes, equivalent | MED | Choose one vs locked | Choose one | Not equivalent |
| No alternative | MED | Commit vs explore | Commit to path | Alternative exists |

---

## Q3: For unmet conditions, is there a way to meet them?
[VOI: HIGH - No path known may mean blocked vs clear path]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No path known | HIGH | Path discovery vs execute | Path discovery | Path exists |
| Unknown if path | HIGH | Path analysis vs assume | Path analysis | Path known |
| Possible path exists | MED | Develop path vs follow | Develop path | No path |
| Clear path exists | LOW | Follow path either way | Follow path | Path unclear |

---

## Q4: What does meeting each condition require?
[VOI: HIGH - Requirements unclear/excessive may block progress vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Requirements unclear | HIGH | Clarity first vs proceed | Requirement clarity | Requirements clear |
| Requirements excessive | HIGH | Evaluate feasibility vs proceed | Evaluate feasibility | Requirements manageable |
| Unknown requirements | HIGH | Discovery first vs proceed | Requirement discovery | Requirements known |
| Requirements known | LOW | Plan to requirements either way | Plan to requirements | Requirements wrong |

---

## Q5: What is the total cost across the chain?
[VOI: HIGH - High/unknown total cost requires major decision vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| High total cost | HIGH | Major decision required vs proceed | Major decision | Lower cost |
| Unknown total cost | HIGH | Total cost analysis vs assume | Total cost analysis | Cost known |
| Moderate total cost | MED | Evaluate carefully vs proceed | Evaluate carefully | Different cost |
| Low total cost | LOW | Feasible either way | Execute chain | Higher cost |

---

## Q6: Is each condition currently met?
[VOI: HIGH - Few/none met requires major work vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Few met | HIGH | Major work vs proceed | Prioritize conditions | More met |
| None met | HIGH | Start from zero vs some progress | Plan systematic approach | Some met |
| Most met | MED | Minor gaps vs proceed | Address gaps | Fewer met |
| All met | LOW | Proceed either way | Move to next | Some not met |

---

## Q7: Is the cost acceptable relative to goal value?
[VOI: HIGH - Not acceptable means abandon or reduce vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Not acceptable | HIGH | Abandon or reduce vs proceed | Abandon or reduce | Actually acceptable |
| Unknown acceptability | MED | Value analysis vs assume | Value analysis | Acceptability known |
| Probably acceptable | MED | Continue vs investigate | Continue | May not be worth |
| Yes, clearly acceptable | LOW | Worth it either way | Proceed | Actually not worth |

---

## Q8: What is the full chain of requirements?
[VOI: HIGH - Deep chain requires major planning vs simple execution]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Deep chain (6+ levels) | HIGH | Major planning vs simple | Major planning | Shallower chain |
| Unknown depth | MED | Chain analysis vs assume | Chain analysis | Depth known |
| Moderate chain (3-5 levels) | MED | Plan carefully vs proceed | Plan carefully | Different depth |
| Shallow chain (1-2 levels) | LOW | Simple execution either way | Execute directly | Deeper chain |

---

## Q9: What is the cost to meet each requirement?
[VOI: HIGH - Cost too high may mean not feasible vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Cost known, too high | HIGH | Seek alternatives vs proceed | Seek alternatives | Cost acceptable |
| Unknown cost | MED | Cost analysis vs assume | Cost analysis | Cost known |
| Cost known, high | MED | Cost-benefit analysis vs proceed | Cost-benefit analysis | Cost is lower |
| Cost known, acceptable | LOW | Proceed either way | Pay cost | Cost wrong |

---

## Q10: Are there conditions that must be true for next milestone?
[VOI: MED - Unknown conditions require discovery vs proceed with known]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown if conditions | MED | Condition discovery vs assume | Condition discovery | Conditions known |
| Yes, conditions exist | LOW | Work to satisfy either way | Address conditions | No conditions |
| No conditions | LOW | Move forward either way | Move forward | Conditions exist |

---

## Q11: Which requirements unblock the most other requirements?
[VOI: MED - Affects prioritization but still doing requirements]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown priority | MED | Priority analysis vs random | Priority analysis | Priority known |
| Key unblocking identified | MED | Prioritize these vs others | Prioritize these | Wrong prioritization |
| No key unblockers | LOW | Order less critical either way | Any order | Unblockers exist |

---

## Q12: Which requirements have lowest cost?
[VOI: LOW - Quick wins helpful but not direction-changing]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown relative costs | MED | Cost ranking vs assume | Cost ranking | Costs known |
| Low-cost identified | LOW | Quick wins either way | Do these first | Wrong identification |
| All similar cost | LOW | Cost-neutral either way | Any order | Some lower |

---

## Question Order by Action Divergence

**HIGH VOI (ask first - route to different action paths):**
1. Q1: Feasible? (Some infeasible → find alternatives vs execute)
2. Q2: Better alternative? (Yes → switch paths vs current)
3. Q3: Path exists? (No → discovery vs execute)
4. Q4: Requirements clear? (Unclear/excessive → clarity vs proceed)
5. Q5: Total cost? (High/unknown → major decision vs proceed)
6. Q6: Conditions met? (Few/none → major work vs proceed)
7. Q7: Cost acceptable? (No → abandon/reduce vs proceed)
8. Q8: Chain depth? (Deep → major planning vs simple)
9. Q9: Individual costs? (Too high → alternatives vs proceed)

**MED/LOW VOI (ask second - refine approach):**
10. Q10: Conditions exist? (Discovery, not direction)
11. Q11: Unblocking priority? (Optimization, not direction)
12. Q12: Lowest cost? (Quick wins, not direction)

---

## Key Insight

**VOI ≠ Complexity or Difficulty**

VOI = Action Divergence

A HIGH VOI requirement question is one where the answer determines whether you PROCEED or STOP/CHANGE APPROACH. "Some requirements infeasible" routes you to "find alternatives" - a completely different path from "execute the plan."

A LOW VOI requirement question like "which have lowest cost" helps optimize but doesn't change whether you proceed - you'll work on requirements either way, just in slightly different order.

---

## Coverage Summary

```
QUESTIONS: 12
ENTRIES: 49

VOI Distribution:
- HIGH: 12 entries (24%)
- MED: 22 entries (45%)
- LOW: 15 entries (31%)
```

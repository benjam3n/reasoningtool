# Universal: Operational Efficiency (52)

**Category**: CORE - Work Optimization
**Source**: [O: universal_goal_analysis.yaml lines 1745-1802 operational_efficiency category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Are there handoff points between parties?
[VOI: HIGH - Many handoffs means high error risk, optimize vs proceed simply]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, many handoffs | HIGH | Optimize handoffs vs proceed | Optimize handoffs | Fewer handoffs |
| Unknown handoffs | MED | Handoff mapping vs assume | Handoff mapping | Handoffs known |
| Yes, few handoffs | MED | Monitor handoffs vs ignore | Monitor handoffs | Different amount |
| No handoffs | LOW | Simple flow either way | Proceed | Handoffs exist |

---

## Q2: What could go wrong at each handoff?
[VOI: HIGH - High failure risk means add verification vs proceed normally]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| High failure risk | HIGH | Add verification vs proceed | Add verification | Lower risk |
| Unknown risk | MED | Risk assessment vs assume | Risk assessment | Risk known |
| Moderate risk | MED | Track handoffs vs ignore | Track handoffs | Different level |
| Low risk | LOW | Acceptable either way | Proceed normally | Higher risk |

---

## Q3: Is there waiting in the process?
[VOI: HIGH - Significant waiting means reduce waiting vs maintain]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, significant waiting | HIGH | Reduce waiting vs maintain | Reduce waiting | Less waiting |
| Unknown waiting | MED | Wait analysis vs assume | Wait analysis | Waiting known |
| Yes, minor waiting | MED | Consider reducing vs ignore | Consider reducing | Different amount |
| No waiting | LOW | Efficient flow either way | Maintain | Waiting exists |

---

## Q4: Is waiting necessary or can it be eliminated?
[VOI: HIGH - Unnecessary waiting means eliminate waste vs accept]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unnecessary waiting | HIGH | Eliminate vs accept | Eliminate | Necessary |
| Unknown necessity | MED | Necessity analysis vs assume | Necessity analysis | Necessity known |
| Necessary waiting | MED | Plan around vs try eliminate | Plan around | Unnecessary |

---

## Q5: Would switching batch/flow improve progress?
[VOI: HIGH - Significant improvement means switch approach vs continue]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, significant improvement | HIGH | Make switch vs continue | Make switch | No improvement |
| Unknown impact | MED | Pilot test vs assume | Pilot test | Impact known |
| Yes, minor improvement | MED | Evaluate tradeoff vs continue | Evaluate tradeoff | Different level |
| No improvement | LOW | Stay current either way | Continue | Improvement exists |

---

## Q6: Are there interruptions disrupting progress?
[VOI: HIGH - Frequent interruptions means reduce them vs maintain flow]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, frequent interruptions | HIGH | Reduce interruptions vs maintain | Reduce interruptions | Fewer |
| Unknown interruptions | MED | Interruption audit vs assume | Interruption audit | Interruptions known |
| Yes, occasional | MED | Manage vs ignore | Manage | Different frequency |
| No interruptions | LOW | Good flow either way | Maintain | Interruptions exist |

---

## Q7: Are interruptions necessary?
[VOI: HIGH - Unnecessary interruptions means eliminate waste vs manage]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unnecessary interruptions | HIGH | Eliminate vs manage | Eliminate | Necessary |
| Unknown necessity | MED | Necessity analysis vs assume | Necessity analysis | Necessity known |
| Mixed | MED | Selective elimination vs accept | Selective elimination | Pure |
| Necessary interruptions | MED | Manage better vs eliminate | Manage better | Unnecessary |

---

## Q8: Are there tasks that could be delegated?
[VOI: MED - Delegation possible affects approach but not direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown delegation options | MED | Delegation analysis vs assume | Delegation analysis | Options known |
| Yes, significant delegation possible | MED | Delegate vs do yourself | Delegate | Less possible |
| No delegation possible | MED | Accept vs explore | Accept | Delegation possible |
| Yes, minor delegation | LOW | Consider either way | Consider | Different amount |

---

## Q9: What is cost of delegation vs doing it yourself?
[VOI: MED - Cost comparison affects decision but both are progress]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown costs | MED | Cost analysis vs assume | Cost analysis | Costs known |
| Delegation cheaper | MED | Delegate vs DIY | Delegate | DIY cheaper |
| DIY cheaper | MED | Do yourself vs delegate | DIY | Delegation cheaper |
| Cost neutral | LOW | Other factors either way | Decide on other criteria | Not neutral |

---

## Q10: Is batch or flow processing used?
[VOI: MED - Processing type affects optimization but not direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Batch processing | MED | Evaluate switch to flow vs continue | Evaluate | Flow |
| Flow processing | MED | Evaluate switch to batch vs continue | Evaluate | Batch |
| Hybrid | MED | Evaluate balance vs continue | Evaluate balance | Pure approach |
| Unknown approach | LOW | Approach audit either way | Approach audit | Approach known |

---

## Question Order by Action Divergence

**HIGH VOI (ask first - route to different action paths):**
1. Q1: Handoffs? (Many → optimize vs proceed)
2. Q2: Handoff risk? (High → add verification vs proceed)
3. Q3: Waiting? (Significant → reduce vs maintain)
4. Q4: Waiting necessary? (No → eliminate vs accept)
5. Q5: Switch batch/flow? (Yes significant → switch vs continue)
6. Q6: Interruptions? (Frequent → reduce vs maintain)
7. Q7: Interruptions necessary? (No → eliminate vs manage)

**MED/LOW VOI (ask second - refine approach):**
8. Q8: Delegation possible? (Approach, not direction)
9. Q9: Delegation cost? (Decision, not direction)
10. Q10: Batch/flow? (Optimization, not direction)

---

## Key Insight

**VOI ≠ Efficiency Gain**

VOI = Action Divergence

A HIGH VOI operational efficiency question is one where the answer determines whether you FIX A MAJOR PROBLEM or CONTINUE AS-IS. "Significant unnecessary waiting" routes you to "eliminate waiting" - a fundamentally different action than "proceed with current process."

A LOW VOI operational efficiency question like "batch vs flow processing" doesn't change your fundamental approach - you'll make progress either way, just with different processing styles.

---

## Coverage Summary

```
QUESTIONS: 10
ENTRIES: 43

VOI Distribution:
- HIGH: 8 entries (19%)
- MED: 26 entries (60%)
- LOW: 9 entries (21%)

Note: Higher MED% because operational issues are usually optimization level
```

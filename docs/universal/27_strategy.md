# Universal: Strategy (27)

**Category**: CORE - Strategy Analysis
**Source**: [O: universal_goal_analysis.yaml lines 231-264 strategy category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: What known methods exist for achieving this goal?
[VOI: HIGH - no methods known means must discover or research first]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No methods known | HIGH | Method research vs proceed | Method research | Methods exist |
| Methods exist, unknown to me | MED | Method discovery vs proceed | Method discovery | All known |
| One method known | MED | Validate method vs search for more | Validate method | More methods |
| Multiple methods known | LOW | Evaluate all vs pick one | Evaluate all | Fewer methods |

---

## Q2: What is the documented success rate for each method?
[VOI: MED - affects method selection but not overall direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Rates unknown | MED | Estimate or test vs assume | Estimate or test | Rates known |
| Rates estimated | MED | Use with caution vs trust | Use with caution | Estimates wrong |
| Success rates documented | LOW | Use rates for comparison vs verify | Use rates | Rates inaccurate |

---

## Q3: What is the primary failure mode for each method?
[VOI: HIGH - unknown failure modes means blind risk]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Failure modes unknown | HIGH | Failure mode research vs proceed blind | Failure mode research | Modes known |
| Failure modes known | MED | Prepare mitigations vs accept risk | Prepare mitigations | Modes different |

---

## Q4: Which methods can I execute given current resources and constraints?
[VOI: HIGH - no executable methods means blocked]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No methods executable | HIGH | Resource acquisition vs start | Resource acquisition | Some executable |
| Unknown executability | MED | Executability check vs assume | Executability check | Status known |
| Some methods executable | MED | Focus on executable vs expand options | Focus on executable | Different set |
| All methods executable | LOW | Choose best vs verify | Choose best | Some not executable |

---

## Q5: Which method has highest success rate for my starting conditions?
[VOI: MED - affects method selection within same direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown which is best | MED | Method comparison vs guess | Method comparison | Best is known |
| Clear best method | MED | Use best method vs verify | Use best method | Different is best |
| Multiple similar options | LOW | Any is fine vs analyze | Any is fine | One is better |

---

## Q6: Which method has failure modes I can recover from?
[VOI: HIGH - all terminal failures means high stakes requiring extra care]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| All methods have terminal failures | HIGH | Plan very carefully vs proceed | Plan carefully | Recovery possible |
| Unknown recoverability | MED | Recovery analysis vs assume | Recovery analysis | Status known |
| Recoverable method exists | MED | Prefer recoverable vs any method | Prefer recoverable | Not recoverable |

---

## Q7: Which method generates useful information even if it fails?
[VOI: MED - learning opportunity but doesn't change main direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Info-generating method exists | MED | Prefer this method vs any | Prefer this method | No info generation |
| Unknown info generation | LOW | Proceed vs analyze | Proceed | Status known |
| No method generates info | LOW | Standard approach vs seek learning | Standard approach | Info methods exist |

---

## Q8: What are the documented limitations of existing methods?
[VOI: MED - affects planning within method but not method choice]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Limitations unknown | MED | Limitation research vs proceed | Limitation research | Limitations known |
| Limitations documented | LOW | Plan for limitations vs ignore | Plan for limitations | More limitations |
| No significant limitations | LOW | Proceed vs investigate | Proceed | Limitations exist |

---

## Q9: What has changed since these methods were created?
[VOI: HIGH - significant changes means methods may be outdated]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Significant changes exist | HIGH | Update methods vs use as-is | Update methods | No significant changes |
| Unknown what changed | MED | Change analysis vs assume none | Change analysis | Changes known |
| Minor changes only | LOW | Use as-is vs update | Use as-is | Major changes exist |

---

## Q10: What methods from adjacent domains could be adapted?
[VOI: MED - innovation opportunity but same general direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Adaptable methods exist | MED | Explore adaptation vs domain-only | Explore adaptation | No adaptable methods |
| Unknown adaptable methods | MED | Domain research vs assume none | Domain research | Status known |
| No adaptable methods | LOW | Use domain methods vs seek adaptation | Use domain methods | Adaptable exist |

---

## Q11: What assumptions does the chosen strategy make?
[VOI: HIGH - hidden assumptions may mean strategy is flawed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Hidden assumptions exist | HIGH | Surface assumptions vs proceed | Surface assumptions | All explicit |
| Unknown assumptions | HIGH | Assumption surfacing vs proceed | Assumption surfacing | Assumptions known |
| Assumptions explicit | MED | Verify each vs trust | Verify each | Hidden assumptions |

---

## Q12: What is the backup strategy if primary fails?
[VOI: HIGH - no backup means single point of failure]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No backup strategy | HIGH | Create backup vs single path | Create backup | Backup exists |
| Unknown if backup exists | MED | Backup planning vs assume covered | Backup planning | Status known |
| Backup strategy exists | MED | Maintain backup vs create new | Maintain backup | No backup |

---

## Question Order by Action Divergence

**HIGH VOI Questions (ask first - route to different action paths):**
1. Q4: Which methods can I execute? (what can I actually do?)
2. Q12: What is the backup strategy? (is there a safety net?)
3. Q11: What assumptions does strategy make? (what could undermine?)
4. Q3: What is primary failure mode? (what are the risks?)
5. Q6: Which method has recoverable failures? (can I recover?)
6. Q9: What has changed since methods created? (are methods outdated?)

**MED VOI Questions (ask second - same direction, different approach):**
7. Q1: What known methods exist? (method inventory)
8. Q5: Which method has highest success rate? (best choice)
9. Q2: What is documented success rate? (reliability)
10. Q10: What methods from adjacent domains? (adaptation)
11. Q7: Which method generates info if fails? (learning value)
12. Q8: What are documented limitations? (constraints)

---

## Key Insight

**VOI ≠ Importance or Severity**

VOI = Action Divergence

A question has HIGH VOI when different answers lead to completely different action paths. "Is there a backup strategy?" is HIGH VOI because NO → create backup first, YES → maintain current. These lead to different immediate actions.

Strategy selection determines your entire approach to achieving the goal.

---

## Coverage Summary

```
QUESTIONS: 12
GUESSES: 46

VOI Distribution:
- HIGH: 8 entries (17%)
- MED: 26 entries (57%)
- LOW: 12 entries (26%)

HIGH-VOI Entries (ask first):
- Q1: No methods known - must discover
- Q3: Failure modes unknown - blind risk
- Q4: No methods executable - blocked
- Q6: All methods have terminal failures - high stakes
- Q9: Significant changes exist - methods may be outdated
- Q11: Hidden / Unknown assumptions - strategy may be flawed
- Q12: No backup strategy - single point of failure
```

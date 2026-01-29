# Universal: Leverage Analysis (45)

**Category**: CORE - Efficiency and Leverage Points
**Source**: [O: universal_goal_analysis.yaml lines 1082-1229 leverage_analysis category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Is there a factor limiting progress rate?
[VOI: HIGH - Clear bottleneck means address it vs optimize broadly]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, clear bottleneck | HIGH | Address bottleneck vs optimize broadly | Address bottleneck | No bottleneck |
| Unknown if bottleneck | MED | Bottleneck analysis vs assume none | Bottleneck analysis | Bottleneck known |
| Possibly | MED | Find bottleneck vs proceed | Find bottleneck | No bottleneck |
| No bottleneck | LOW | Continue smoothly either way | Continue | Bottleneck exists |

---

## Q2: Does any action require approval?
[VOI: HIGH - Many approvals needed means reduce approvals vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Many approvals needed | HIGH | Reduce approvals vs proceed | Reduce approvals | Fewer approvals |
| Unknown approval needs | MED | Approval mapping vs assume none | Approval mapping | Approvals known |
| Some approvals | MED | Optimize approvals vs ignore | Optimize approvals | Different amount |
| No approvals needed | LOW | Proceed smoothly either way | Proceed | Approvals needed |

---

## Q3: Does any action wait for information from others?
[VOI: HIGH - Critical info dependency requires early securing vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Critical info from others | HIGH | Secure info early vs proceed | Secure info early | Less critical |
| Unknown dependencies | MED | Dependency mapping vs assume | Dependency mapping | Dependencies known |
| Minor info from others | MED | Plan around vs ignore | Plan around | Different level |
| No info dependencies | LOW | Proceed independently either way | Proceed | Dependencies exist |

---

## Q4: Does any action wait for deliverables from others?
[VOI: HIGH - Critical deliverables require early securing vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Critical deliverables | HIGH | Secure early vs proceed | Secure early | Less critical |
| Unknown dependencies | MED | Dependency mapping vs assume | Dependency mapping | Dependencies known |
| Minor deliverables | MED | Plan around vs ignore | Plan around | Different level |
| No deliverable dependencies | LOW | Proceed independently either way | Proceed | Dependencies exist |

---

## Q5: Can any person-performed action be automated?
[VOI: HIGH - Significant automation opportunity changes approach vs manual]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, significant automation | HIGH | Automate first vs manual | Automate first | Less automatable |
| Unknown if automatable | MED | Automation analysis vs assume | Automation analysis | Automatability known |
| Yes, minor automation | MED | Consider automating vs manual | Consider automating | Different level |
| No, must be manual | MED | Optimize manual vs automate | Optimize manual | Can automate |

---

## Q6: Is any decision being made more than once?
[VOI: HIGH - Same decision repeatedly means create rule vs decide each time]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Same decision repeatedly | HIGH | Create rule vs decide each | Create rule | No repetition |
| Unknown repetition | MED | Decision audit vs assume | Decision audit | Repetition known |
| Similar decisions | MED | Consider rule vs decide | Consider rule | Not similar |
| No decision repetition | LOW | Continue deciding either way | Continue | Decisions repeat |

---

## Q7: Would build cost of automation be less than ongoing manual cost?
[VOI: MED - Determines build vs manual but both are progress]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown comparison | MED | Cost comparison first vs assume | Cost comparison | Comparison known |
| Yes, clear savings | MED | Start building vs manual | Start building | No savings |
| Probably | MED | Evaluate more vs manual | Evaluate more | Probably not |
| No, manual cheaper | MED | Stay manual vs build | Stay manual | Actually worth it |

---

## Q8: Can repeated decisions be converted to a rule?
[VOI: MED - Determines rule vs judgment but both are progress]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown if possible | MED | Rule analysis vs assume | Rule analysis | Possibility known |
| Yes, clear rule possible | MED | Create rule vs decide | Create rule | No clear rule |
| Partially, heuristic | MED | Create heuristic vs decide | Create heuristic | Different level |
| No, judgment required | MED | Improve process vs create rule | Improve process | Can create rule |

---

## Q9: Can approval time be reduced?
[VOI: MED - Determines optimization but approvals still needed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown reducibility | MED | Reduction analysis vs assume | Reduction analysis | Reducibility known |
| Yes, significantly | MED | Reduce time vs accept | Reduce time | Less reducible |
| No, fixed time | MED | Plan around vs try reduce | Plan around | Can reduce |
| Yes, somewhat | LOW | Make improvements either way | Make improvements | Different amount |

---

## Q10: Can information be obtained in advance?
[VOI: MED - Determines timing but info still needed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown if possible | MED | Advance analysis vs assume | Advance analysis | Possibility known |
| Yes, with effort | MED | Evaluate tradeoff vs wait | Evaluate tradeoff | Different effort |
| No, must wait | MED | Plan for wait vs get early | Plan for wait | Can get early |
| Yes, easily | LOW | Get in advance either way | Get in advance | Not easily |

---

## Q11: Is any action being performed more than once?
[VOI: MED - Many repetitions means optimize vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Many repetitions | MED | Optimize vs proceed | Optimize | Fewer repetitions |
| Unknown repetitions | LOW | Repetition audit vs assume | Repetition audit | Repetitions known |
| Some repetitions | LOW | Consider optimizing either way | Consider optimizing | Different amount |
| No repetitions | LOW | Already efficient either way | Proceed | Repetitions exist |

---

## Q12: Could repetitive actions be done once and reused?
[VOI: MED - Determines reuse vs repeat but both are progress]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown if reusable | MED | Reuse analysis vs assume | Reuse analysis | Reusability known |
| Yes, easily reusable | MED | Implement reuse vs repeat | Implement reuse | Not reusable |
| Yes, with effort | MED | Evaluate payoff vs repeat | Evaluate payoff | Different effort |
| No, must repeat | LOW | Accept repetition either way | Continue | Can be reused |

---

## Q13: If this factor changed, would another become limiting?
[VOI: MED - Determines next step after fix but fix still happens]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown | MED | Post-fix analysis vs assume | Post-fix analysis | Next known |
| Yes, next bottleneck known | MED | Plan sequence vs single fix | Plan sequence | Next unknown |
| Probably | MED | Investigate next vs single fix | Investigate next | No next |
| No, clear path | LOW | Major speedup either way | Fix current | Another exists |

---

## Question Order by Action Divergence

**HIGH VOI (ask first - route to different action paths):**
1. Q1: Bottleneck? (Yes → address vs optimize broadly)
2. Q2: Approvals needed? (Many → reduce approvals vs proceed)
3. Q3: Info dependencies? (Critical → secure early vs proceed)
4. Q4: Deliverable dependencies? (Critical → secure early vs proceed)
5. Q5: Automation possible? (Significant → automate vs manual)
6. Q6: Repeated decisions? (Same repeatedly → create rule vs decide each)

**MED VOI (ask second - refine approach):**
7. Q7: Automation cost? (Determines build vs manual)
8. Q8: Rule possible? (Determines rule vs judgment)
9. Q9: Approval time? (Determines optimization level)
10. Q10: Info in advance? (Determines timing)
11. Q11: Repeated actions? (Determines optimization)
12. Q12: Reusable actions? (Determines reuse vs repeat)
13. Q13: Next bottleneck? (Determines sequence)

---

## Key Insight

**VOI ≠ Efficiency Gain**

VOI = Action Divergence

A HIGH VOI leverage question is one where the answer determines whether you OPTIMIZE THE BOTTLENECK or OPTIMIZE BROADLY. "Clear bottleneck exists" routes you to "address the bottleneck" - a focused action path very different from "improve everything a little."

A LOW VOI leverage question like "some repetitions exist" doesn't change your basic approach - you'll make progress either way, just with minor efficiency differences.

---

## Coverage Summary

```
QUESTIONS: 13
ENTRIES: 56

VOI Distribution:
- HIGH: 7 entries (13%)
- MED: 36 entries (64%)
- LOW: 13 entries (23%)

Note: Lower HIGH% because leverage issues are mostly optimization, not strategy
```

# Universal: Infrastructure (32)

**Category**: CORE - Infrastructure Analysis
**Source**: [O: universal_goal_analysis.yaml lines 478-524 infrastructure category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: What physical infrastructure is required?
[VOI: MED - affects acquisition planning but same overall direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown physical needs | MED | Requirements analysis vs guess | Requirements analysis | Requirements known |
| Some physical requirements | MED | Complete list vs partial | Complete list | All clear or none |
| Physical requirements clear | LOW | Acquire needed vs analyze | Acquire needed | Requirements unclear |
| No physical required | LOW | Proceed vs analyze | Proceed | Physical needed |

---

## Q2: What digital infrastructure is required?
[VOI: MED - affects setup planning but same direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown digital needs | MED | Requirements analysis vs guess | Requirements analysis | Requirements known |
| Some digital requirements | MED | Complete list vs partial | Complete list | All clear or none |
| Digital requirements clear | LOW | Set up systems vs analyze | Set up systems | Requirements unclear |
| No digital required | LOW | Proceed vs analyze | Proceed | Digital needed |

---

## Q3: What organizational structures are required?
[VOI: MED - affects structure planning]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown org needs | MED | Org analysis vs guess | Org analysis | Requirements known |
| Org structures clear | MED | Create structures vs analyze | Create structures | Structures unclear |
| No org structures needed | LOW | Proceed solo vs analyze | Proceed solo | Structures needed |

---

## Q4: What relationships are required?
[VOI: MED - affects relationship building strategy]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown relationships | MED | Relationship analysis vs guess | Relationship analysis | Requirements known |
| Relationships identified | MED | Build relationships vs analyze | Build relationships | Different relationships |
| No relationships needed | LOW | Work alone vs build | Work alone | Relationships needed |

---

## Q5: What financial infrastructure is required?
[VOI: MED - affects financial setup]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown financial needs | MED | Financial analysis vs guess | Financial analysis | Requirements known |
| Complex financial needs | MED | Plan setup vs simple | Plan setup | Simpler needs |
| Financial infrastructure clear | LOW | Set up accounts vs analyze | Set up accounts | Requirements unclear |
| No financial infrastructure | LOW | Simple transactions vs setup | Simple transactions | Infrastructure needed |

---

## Q6: What required infrastructure does not currently exist?
[VOI: HIGH - major gaps means not ready to proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Major gaps exist | HIGH | Major acquisition vs start | Major acquisition | Gaps smaller |
| Unknown gaps | HIGH | Gap analysis vs be surprised | Gap analysis | Gaps known |
| Some gaps identified | MED | Gap filling vs start | Gap filling | Gaps different |
| All infrastructure exists | LOW | Begin vs verify | Begin | Gaps exist |

---

## Q7: Can gaps be filled by accessing existing infrastructure?
[VOI: MED - affects acquisition approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown access options | MED | Access research vs assume build | Access research | Options known |
| No, must build new | MED | Build infrastructure vs access | Build infrastructure | Can access |
| Yes, can access existing | LOW | Arrange access vs build | Arrange access | Cannot access |

---

## Q8: If not accessible, can an alternative serve the same function?
[VOI: HIGH - no alternatives means must have original]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No alternatives | HIGH | Acquire original vs substitute | Acquire original | Alternatives exist |
| Unknown alternatives | MED | Alternative research vs assume none | Alternative research | Status known |
| Yes, alternatives exist | MED | Use alternative vs original | Use alternative | No alternatives |

---

## Q9: How does infrastructure gap affect goal feasibility?
[VOI: HIGH - infeasible without means must fill first]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Goal infeasible without | HIGH | Fill gaps first vs proceed | Fill gaps first | Gap tolerable |
| Unknown impact | MED | Impact assessment vs assume minor | Impact assessment | Impact known |
| Moderate impact | MED | Plan around gaps vs ignore | Plan around gaps | Different impact |
| Minor impact | LOW | Proceed with gaps vs fill | Proceed with gaps | Major impact |

---

## Q10: What infrastructure do I control relevant to this goal?
[VOI: MED - affects leverage strategy]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown control | MED | Control analysis vs assume | Control analysis | Control known |
| Little controlled | MED | Work within limits vs expand | Work within limits | More controlled |
| Controlled infrastructure clear | LOW | Leverage controlled vs analyze | Leverage controlled | More/less controlled |

---

## Q11: What modifications to controlled infrastructure would help?
[VOI: MED - optimization opportunity]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Modifications identified | MED | Make modifications vs maintain | Make modifications | Different modifications |
| Unknown modifications | LOW | Modification analysis vs maintain | Modification analysis | Modifications known |
| No modifications needed | LOW | Maintain vs analyze | Maintain | Modifications needed |

---

## Q12: What is the cost of each modification?
[VOI: MED - affects modification decisions]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown costs | MED | Cost estimation vs guess | Cost estimation | Costs known |
| Costs known, high | MED | Evaluate worth vs proceed | Evaluate worth | Costs lower |
| Costs known, acceptable | LOW | Make modifications vs reconsider | Make modifications | Costs higher |

---

## Question Order by Action Divergence

**HIGH VOI Questions (ask first - route to different action paths):**
1. Q6: What required infrastructure doesn't exist? (what's missing?)
2. Q9: How does gap affect feasibility? (can I proceed with gaps?)
3. Q8: Can alternative serve same function? (can I work around?)

**MED VOI Questions (ask second - same direction, different approach):**
4. Q7: Can gaps be filled by accessing existing? (can I borrow?)
5. Q1: What physical infrastructure required? (physical needs)
6. Q2: What digital infrastructure required? (digital needs)
7. Q3: What organizational structures required? (org needs)
8. Q4: What relationships required? (social needs)
9. Q5: What financial infrastructure required? (financial needs)
10. Q10: What infrastructure do I control? (leverage)
11. Q11: What modifications would help? (optimization)
12. Q12: What is cost of modifications? (trade-offs)

---

## Key Insight

**VOI ≠ Importance or Severity**

VOI = Action Divergence

A question has HIGH VOI when different answers lead to completely different action paths. "Is goal infeasible without this infrastructure?" is HIGH VOI because YES → fill gaps before proceeding, NO → proceed and fill gaps opportunistically. These are different sequencing decisions.

Infrastructure determines what you can build on to achieve your goal.

---

## Coverage Summary

```
QUESTIONS: 12
GUESSES: 47

VOI Distribution:
- HIGH: 4 entries (9%)
- MED: 26 entries (55%)
- LOW: 17 entries (36%)

HIGH-VOI Entries (ask first):
- Q6: Major / Unknown gaps - not ready or may be blocked
- Q8: No alternatives - must have original
- Q9: Goal infeasible without - must fill first
```

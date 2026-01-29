# Universal: Resources (26)

**Category**: CORE - Resource Analysis
**Source**: [O: universal_goal_analysis.yaml lines 194-226 resources category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: What is the current quantity of each relevant resource?
[VOI: HIGH - unknown quantities means can't plan at all]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Quantities unknown | HIGH | Resource audit vs guess | Resource audit | Quantities known |
| Quantities estimated | MED | Verify estimates vs use | Verify estimates | Estimates wrong |
| Quantities known accurately | LOW | Use quantities vs verify | Use quantities | Quantities wrong |

---

## Q2: What is the replenishment rate for each resource?
[VOI: MED - affects planning but not overall direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown replenishment | MED | Rate investigation vs assume | Rate investigation | Rate known |
| No replenishment | MED | Plan for depletion vs assume renewable | Plan for depletion | Replenishment exists |
| Replenishment known | LOW | Factor into plan vs investigate | Factor into plan | Rate different |

---

## Q3: What resources are required for each stage?
[VOI: HIGH - unclear requirements means can't plan stages]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Requirements unclear | HIGH | Requirement analysis vs guess | Requirement analysis | Requirements clear |
| Requirements by stage clear | LOW | Plan stages vs analyze | Plan stages | Requirements unclear |
| Single stage only | LOW | Plan single stage vs multi-stage | Plan single stage | Multiple stages |

---

## Q4: Which resources are consumed and cannot be reused?
[VOI: MED - affects budgeting but not overall approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Consumed resources identified | MED | Budget for consumption vs assume reuse | Budget for consumption | More consumed |
| Unknown consumption | MED | Consumption analysis vs assume | Consumption analysis | Status known |
| All resources reusable | LOW | Reuse plan vs budget for loss | Reuse plan | Some consumed |

---

## Q5: Which resources generate additional resources when used?
[VOI: MED - affects strategy but doesn't change direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Generating resources exist | MED | Maximize leverage vs linear | Maximize leverage | No generating |
| Unknown generators | MED | Generator analysis vs assume none | Generator analysis | Status known |
| No generating resources | LOW | Linear planning vs seek leverage | Linear planning | Generators exist |

---

## Q6: What required resources are not currently available?
[VOI: HIGH - major gaps means can't proceed without acquisition]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Major gaps exist | HIGH | Major acquisition vs start | Major acquisition | Gaps smaller |
| Unknown gaps | HIGH | Gap analysis vs be surprised | Gap analysis | Gaps known |
| Some gaps identified | MED | Gap filling vs start | Gap filling | Gaps different |
| All resources available | LOW | Begin execution vs verify | Begin execution | Gaps exist |

---

## Q7: Can missing resources be purchased?
[VOI: HIGH - cannot purchase means need completely different acquisition strategy]
Prerequisite: Q6 = Gaps exist

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Cannot be purchased | HIGH | Other acquisition path vs buy | Other acquisition | Purchasable |
| Unknown if purchasable | MED | Market research vs assume | Market research | Status known |
| Yes, expensive | MED | Budget or alternatives vs assume cheap | Budget or alternatives | Different cost |
| Yes, affordable | LOW | Purchase vs seek alternatives | Purchase | Not affordable |

---

## Q8: Can missing resources be borrowed or partnered?
[VOI: MED - different acquisition method but same direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, borrowing possible | MED | Arrange borrowing vs buy | Arrange borrowing | Not borrowable |
| Partnership possible | MED | Seek partnership vs solo | Seek partnership | No partnership |
| Unknown options | MED | Option research vs assume own | Option research | Options known |
| Neither possible | MED | Must own or build vs borrow | Other options | One is possible |

---

## Q9: Can the approach be changed to not require missing resources?
[VOI: HIGH - alternative approach is completely different path]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, alternative approach | HIGH | Consider alternative path vs acquire | Consider alternative | Must have resource |
| Unknown alternatives | MED | Alternative search vs acquire | Alternative search | Alternatives known |
| No, resource essential | MED | Focus on acquisition vs seek alternative | Focus on acquisition | Can be changed |

---

## Q10: Which resources can be converted to other resources?
[VOI: MED - flexibility option but same general direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Conversions identified | MED | Use conversions vs linear use | Use conversions | Fewer conversions |
| Unknown conversions | MED | Conversion analysis vs assume none | Conversion analysis | Status known |
| No conversions possible | LOW | Use as-is vs seek conversions | Use as-is | Conversions exist |

---

## Q11: What resources do I have that others typically lack?
[VOI: MED - leverage opportunity but doesn't change overall direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unique advantages identified | MED | Maximize unique advantage vs standard | Maximize unique | Fewer advantages |
| Unknown unique resources | MED | Advantage analysis vs assume none | Advantage analysis | Status known |
| No unique resources | LOW | Standard methods vs seek advantage | Standard methods | Unique exists |

---

## Q12: What resources are not currently being used for this goal?
[VOI: MED - opportunity but doesn't change direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unused resources identified | MED | Apply resources vs leave idle | Apply resources | Fewer unused |
| Unknown unused | MED | Resource inventory vs assume all used | Resource inventory | Status known |
| All resources in use | LOW | Maintain vs seek more | Maintain | Unused exist |

---

## Question Order by Action Divergence

**HIGH VOI Questions (ask first - route to different action paths):**
1. Q6: What required resources are not available? (are there blockers?)
2. Q9: Can approach be changed to not require missing resources? (alternative path?)
3. Q3: What resources required for each stage? (what's needed when?)
4. Q1: What is current quantity of each resource? (what do we have?)
5. Q7: Can missing resources be purchased? (acquisition path)

**MED VOI Questions (ask second - same direction, different approach):**
6. Q8: Can resources be borrowed or partnered? (acquisition options)
7. Q10: Which resources can be converted? (flexibility)
8. Q11: What unique resources do I have? (leverage)
9. Q12: What resources are not being used? (opportunity)
10. Q2: What is replenishment rate? (sustainability)
11. Q4: Which resources are consumed? (budgeting)
12. Q5: Which resources generate more? (leverage)

---

## Key Insight

**VOI ≠ Importance or Severity**

VOI = Action Divergence

A question has HIGH VOI when different answers lead to completely different action paths. "Can the approach be changed to not require this?" is HIGH VOI because YES → pursue alternative approach, NO → must acquire the resource. These are completely different paths.

Resource analysis determines whether you can proceed and what acquisition strategy to use.

---

## Coverage Summary

```
QUESTIONS: 12
GUESSES: 47

VOI Distribution:
- HIGH: 5 entries (11%)
- MED: 27 entries (57%)
- LOW: 15 entries (32%)

HIGH-VOI Entries (ask first):
- Q1: Quantities unknown - can't plan
- Q3: Requirements unclear - can't plan stages
- Q6: Major gaps / Unknown - can't proceed
- Q7: Cannot be purchased - non-monetary solution needed
- Q9: Yes, alternative approach - may be better path
```

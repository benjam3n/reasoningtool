# Universal: Verification (31)

**Category**: CORE - Verification Analysis
**Source**: [O: universal_goal_analysis.yaml lines 420-473 verification category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: What specific conditions define goal completion?
[VOI: HIGH - no conditions means don't know when done]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No conditions defined | HIGH | Define conditions vs proceed blind | Define conditions | Conditions exist |
| Conditions partially defined | MED | Complete definition vs proceed | Complete definition | Conditions clear |
| Conditions clearly defined | LOW | Check conditions vs redefine | Check conditions | Conditions unclear |

---

## Q2: What evidence would prove each condition is met?
[VOI: HIGH - unknown evidence criteria means can't verify completion]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown evidence criteria | HIGH | Evidence definition vs guess | Evidence definition | Criteria known |
| Evidence criteria vague | MED | Clarify criteria vs interpret | Clarify criteria | Criteria clear |
| Evidence criteria clear | LOW | Gather evidence vs refine | Gather evidence | Criteria unclear |

---

## Q3: What situations could create appearance of completion without actual completion?
[VOI: MED - false positive awareness but same verification direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| False positives identified | MED | Guard against vs accept | Guard against | Different false positives |
| Unknown false positives | MED | False positive analysis vs assume none | False positive analysis | Status known |
| No false positives possible | LOW | Standard checks vs guard | Standard checks | False positives exist |

---

## Q4: What metrics indicate progress toward the goal?
[VOI: HIGH - no metrics means flying blind]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No metrics defined | HIGH | Define metrics vs guess at progress | Define metrics | Metrics exist |
| Metrics partially defined | MED | Complete metrics vs use partial | Complete metrics | Metrics clear |
| Metrics defined | LOW | Track metrics vs refine | Track metrics | Metrics inadequate |

---

## Q5: What value range indicates on-track vs off-track progress?
[VOI: MED - affects interpretation but not overall tracking approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Ranges vague | MED | Clarify ranges vs interpret | Clarify ranges | Ranges clear |
| Unknown ranges | MED | Range definition vs guess | Range definition | Ranges known |
| Ranges clearly defined | LOW | Compare to ranges vs refine | Compare to ranges | Ranges unclear |

---

## Q6: What earlier indicator predicts metric changes before they happen?
[VOI: MED - early warning opportunity but same direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Leading indicators exist | MED | Monitor indicators vs react | Monitor indicators | No leading indicators |
| Unknown leading indicators | LOW | Indicator analysis vs react | Indicator analysis | Status known |
| No leading indicators | LOW | Use lagging metrics vs seek early | Use lagging metrics | Indicators exist |

---

## Q7: What observations would prove progress is NOT being made?
[VOI: MED - negative evidence detection but same monitoring approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Negative evidence defined | MED | Monitor for negatives vs positive only | Monitor for negatives | Different evidence |
| No negative evidence defined | MED | Define evidence vs ignore | Define evidence | Evidence defined |
| Unknown negative evidence | MED | Evidence analysis vs assume none | Evidence analysis | Evidence known |

---

## Q8: What external data sources can validate progress assessment?
[VOI: MED - independent check but same direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| External sources exist | MED | Use external sources vs self-assess | Use external sources | Fewer sources |
| Unknown external sources | LOW | Source discovery vs self-assess | Source discovery | Status known |
| No external sources | LOW | Self-assessment only vs seek external | Rely on internal | Sources exist |

---

## Q9: What intermediate milestones exist between start and goal?
[VOI: MED - progress checkpoints but same direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No milestones defined | MED | Define milestones vs continuous | Define milestones | Milestones exist |
| Milestones vague | MED | Define milestones vs interpret | Define milestones | Milestones clear |
| Milestones clearly defined | LOW | Use milestones vs refine | Use milestones | Milestones unclear |

---

## Q10: If milestone is NOT reached on time, what decision follows?
[VOI: HIGH - no decision criteria means no planned response to falling behind]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No decision criteria | HIGH | Define criteria vs ad-hoc response | Define criteria | Criteria exist |
| Unknown criteria | MED | Criteria definition vs assume exists | Criteria definition | Criteria known |
| Decision criteria clear | MED | Apply criteria vs refine | Apply criteria | Criteria unclear |

---

## Q11: Can metrics be gamed without improving actual outcome?
[VOI: HIGH - gameable metrics may show false progress]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, metrics gameable | HIGH | Anti-gaming measures vs trust | Anti-gaming measures | Not gameable |
| Unknown gameability | MED | Gaming analysis vs assume safe | Gaming analysis | Status known |
| No, metrics not gameable | LOW | Trust metrics vs verify | Trust metrics | Gameable |

---

## Q12: Is there evidence of gaming occurring?
[VOI: HIGH - gaming detected means metrics corrupted, need new ones]
Prerequisite: Q11 = Gameable

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Gaming detected | HIGH | New metrics needed vs continue | New metrics needed | No gaming |
| Unknown if gaming | MED | Gaming investigation vs assume none | Gaming investigation | Status known |
| No gaming detected | LOW | Continue using vs investigate | Continue using | Gaming exists |

---

## Question Order by Action Divergence

**HIGH VOI Questions (ask first - route to different action paths):**
1. Q1: What conditions define completion? (how do I know when done?)
2. Q2: What evidence proves conditions met? (how do I verify?)
3. Q4: What metrics indicate progress? (how do I track?)
4. Q11: Can metrics be gamed? (are metrics trustworthy?)
5. Q12: Is gaming occurring? (are metrics corrupted?)
6. Q10: What decision if milestone not reached? (what if falling behind?)

**MED VOI Questions (ask second - same direction, different approach):**
7. Q3: What could create false completion? (false positives)
8. Q5: What ranges indicate on/off track? (interpretation)
9. Q7: What proves progress NOT being made? (negative evidence)
10. Q9: What intermediate milestones exist? (checkpoints)
11. Q6: What leading indicators exist? (early warning)
12. Q8: What external sources validate? (independent check)

---

## Key Insight

**VOI ≠ Importance or Severity**

VOI = Action Divergence

A question has HIGH VOI when different answers lead to completely different action paths. "Can metrics be gamed?" is HIGH VOI because YES → implement anti-gaming measures or change metrics, NO → trust metrics. These lead to different verification approaches.

Verification determines whether you're actually making progress or just think you are.

---

## Coverage Summary

```
QUESTIONS: 12
GUESSES: 46

VOI Distribution:
- HIGH: 6 entries (13%)
- MED: 25 entries (54%)
- LOW: 15 entries (33%)

HIGH-VOI Entries (ask first):
- Q1: No conditions defined - don't know when done
- Q2: Unknown evidence criteria - can't verify completion
- Q4: No metrics defined - flying blind
- Q10: No decision criteria - no planned response
- Q11: Yes, metrics gameable - false progress possible
- Q12: Gaming detected - metrics corrupted
```

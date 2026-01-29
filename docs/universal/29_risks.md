# Universal: Risks (29)

**Category**: CORE - Risk Analysis
**Source**: [O: universal_goal_analysis.yaml lines 303-357 risks category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: What events could prevent goal achievement?
[VOI: HIGH - no/unknown risks means blind to threats]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No risks identified | HIGH | Risk identification vs proceed | Risk identification | Risks exist |
| Unknown what risks exist | HIGH | Risk analysis vs proceed blind | Risk analysis | Risks known |
| Some risks identified | MED | Continue identifying vs proceed | Continue identifying | All identified |
| Risks comprehensively identified | LOW | Plan mitigations vs identify more | Plan mitigations | More risks exist |

---

## Q2: What is the probability of each identified risk?
[VOI: HIGH - high probability means must plan for occurrence, not just possibility]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| High probability (>50%) | HIGH | Plan for occurrence vs contingency | Plan for occurrence | Lower probability |
| Unknown probability | MED | Probability estimation vs guess | Probability estimation | Probability known |
| Medium probability (10-50%) | MED | Contingency planning vs monitor | Contingency planning | Different probability |
| Low probability (<10%) | LOW | Monitor only vs full plan | Monitor only | Higher probability |

---

## Q3: What is the impact if each risk occurs?
[VOI: HIGH - goal fails entirely means terminal risk requiring prevention focus]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Goal fails entirely | HIGH | Prevention focus vs accept risk | Prevention focus | Less severe |
| Unknown impact | MED | Impact analysis vs assume moderate | Impact analysis | Impact known |
| Goal delayed significantly | MED | Delay planning vs accept | Delay planning | Different impact |
| Goal reduced in scope | MED | Scope adjustment vs accept | Scope adjustment | Different impact |
| Minor inconvenience | LOW | Accept risk vs mitigate | Accept risk | More severe |

---

## Q4: Which risks can be recovered from after occurrence?
[VOI: HIGH - all terminal means no recovery, prevention only]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| All risks terminal | HIGH | Prevention only vs recovery planning | Prevention only | Some recoverable |
| Unknown recoverability | MED | Recovery analysis vs assume | Recovery analysis | Status known |
| Recoverable risks identified | MED | Plan recovery vs prevention | Plan recovery | Different recoverable |

---

## Q5: Which risks are terminal (goal becomes impossible)?
[VOI: HIGH - terminal risks need identification for prevention focus]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Terminal risks identified | HIGH | Prevention focus on terminal vs equal | Prevention focus | More terminal risks |
| Unknown which terminal | HIGH | Terminal risk analysis vs guess | Terminal risk analysis | Status known |
| No terminal risks | LOW | Recovery planning vs prevention | Recovery planning | Terminal risks exist |

---

## Q6: Which risks can be detected before fully materializing?
[VOI: MED - affects monitoring approach but not overall risk strategy]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Early detectable risks | MED | Set up detection vs react | Set up detection | Fewer detectable |
| Unknown detectability | MED | Detectability analysis vs assume | Detectability analysis | Status known |
| No early warning possible | MED | Accept suddenness vs seek signals | Accept suddenness | Detection possible |

---

## Q7: Can the probability of high-risk events be reduced?
[VOI: MED - affects mitigation approach within risk management]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, probability reducible | MED | Implement reduction vs accept odds | Implement reduction | Cannot reduce |
| Unknown if reducible | MED | Reduction exploration vs assume fixed | Reduction exploration | Status known |
| No, probability fixed | MED | Impact mitigation vs probability | Impact mitigation | Can be reduced |

---

## Q8: Can the impact of high-risk events be reduced?
[VOI: HIGH - fixed impact means must prevent entirely]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, impact fixed | HIGH | Prevention focus vs damage control | Prevention focus | Can be reduced |
| Unknown if reducible | MED | Reduction exploration vs assume fixed | Reduction exploration | Status known |
| Yes, impact reducible | MED | Damage control vs prevention | Damage control possible | Cannot reduce |

---

## Q9: What specific response exists for each high-impact risk?
[VOI: HIGH - no responses means unprepared]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No responses defined | HIGH | Define responses vs proceed unprepared | Define responses | Responses exist |
| Unknown response status | MED | Response audit vs assume prepared | Response audit | Status known |
| Vague responses only | MED | Define specifics vs accept vague | Define specifics | Responses clear |
| Specific responses defined | LOW | Maintain readiness vs refine | Maintain readiness | Responses inadequate |

---

## Q10: What risks did others pursuing similar goals not anticipate?
[VOI: HIGH - known surprises from others means learn from their mistakes]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Known surprises documented | HIGH | Prepare for these vs standard prep | Prepare for these | Different surprises |
| Unknown others' experience | MED | Experience research vs assume none | Experience research | Experience known |
| No documented surprises | LOW | Standard preparation vs seek more | Standard preparation | Surprises exist |

---

## Q11: Is there any single point of failure?
[VOI: HIGH - single points are critical vulnerabilities]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Single points identified | HIGH | Add redundancy vs accept | Add redundancy | Different single points |
| Unknown single points | HIGH | Single point analysis vs assume none | Single point analysis | Status known |
| No single points | LOW | Maintain resilience vs analyze | Maintain resilience | Single points exist |

---

## Q12: Is there slack built into the plan for disruptions?
[VOI: MED - affects planning buffer but not strategy direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Insufficient slack | MED | Add slack or accept tight vs maintain | Add slack or accept | Slack adequate |
| No slack | MED | Critical slack needed vs tight | Critical slack needed | Slack exists |
| Unknown slack level | MED | Slack analysis vs assume adequate | Slack analysis | Status known |
| Adequate slack exists | LOW | Maintain slack vs add more | Maintain slack | Insufficient slack |

---

## Question Order by Action Divergence

**HIGH VOI Questions (ask first - route to different action paths):**
1. Q5: Which risks are terminal? (what's fatal?)
2. Q11: Is there any single point of failure? (critical vulnerabilities?)
3. Q1: What events could prevent achievement? (what could go wrong?)
4. Q2: What is probability of each risk? (how likely?)
5. Q3: What is impact if risk occurs? (how bad?)
6. Q9: What specific response exists? (are we prepared?)

**MED VOI Questions (ask second - same direction, different approach):**
7. Q4: Which risks can be recovered from? (recovery planning)
8. Q10: What risks did others not anticipate? (learn from others)
9. Q8: Can impact be reduced? (damage control)
10. Q6: Which risks can be detected early? (monitoring)
11. Q7: Can probability be reduced? (mitigation)
12. Q12: Is there slack in the plan? (buffer)

---

## Key Insight

**VOI ≠ Importance or Severity**

VOI = Action Divergence

A question has HIGH VOI when different answers lead to completely different action paths. "Is this risk terminal?" is HIGH VOI because YES → prevention focus with maximum resources, NO → recovery planning acceptable. These require fundamentally different resource allocation.

Risk errors are particularly costly because they mean being blindsided by preventable failures. That's why this category has higher HIGH% than average.

---

## Coverage Summary

```
QUESTIONS: 12
GUESSES: 50

VOI Distribution:
- HIGH: 12 entries (24%)
- MED: 28 entries (56%)
- LOW: 10 entries (20%)

Note: Higher HIGH% because risk errors = blindsided by preventable failures

HIGH-VOI Entries (ask first):
- Q1: No / Unknown risks - blind to threats
- Q2: High probability - likely to occur
- Q3: Goal fails entirely - terminal risk
- Q4: All risks terminal - no recovery option
- Q5: Terminal / Unknown terminal - know fatal threats
- Q8: Impact fixed - must prevent entirely
- Q9: No responses defined - unprepared
- Q10: Known surprises documented - learn from others
- Q11: Single points / Unknown - critical vulnerability
```

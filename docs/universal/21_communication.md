# Universal: Communication (21)

**Category**: APPLIED - Communication
**Source**: [O: universal_goal_analysis.yaml lines 612-661 communication category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Is there information others need for this goal to succeed?
[VOI: HIGH - determines whether communication planning is needed at all]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, critical information | HIGH | Must distribute vs no action needed | Must distribute | No critical info |
| Unknown if info needed | HIGH | Stakeholder analysis vs proceed alone | Stakeholder analysis | Info needs known |
| Yes, helpful information | MED | Consider sharing vs skip | Consider sharing | Not essential |
| No information needed | LOW | Proceed alone vs share anyway | Proceed alone | Information sharing needed |

---

## Q2: What information needs to be shared?
[VOI: HIGH - determines content strategy and communication priorities]
Prerequisite: Q1 = Yes

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Decisions made | HIGH | Decision communication vs different content | Decision communication | Decisions not needed |
| Requirements/constraints | HIGH | Constraint communication vs different content | Constraint communication | Constraints not relevant |
| Risks/issues | HIGH | Risk communication vs different content | Risk communication | No risks to share |
| Unknown what to share | HIGH | Content discovery vs proceed with known | Content discovery | Content is clear |
| Status/progress updates | MED | Regular updates vs different content type | Regular updates | Different info type |
| Technical specifications | MED | Technical docs vs different content type | Technical docs | Different info type |

---

## Q3: Who needs to receive this information?
[VOI: HIGH - wrong recipients means wasted effort or missed critical parties]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Decision makers | HIGH | Include decision makers vs skip them | Include decision makers | Not relevant to them |
| Unknown recipients | HIGH | Recipient mapping vs assume known | Recipient mapping | Recipients known |
| Implementers | MED | Include implementers vs skip | Include implementers | Not relevant to them |
| Stakeholders/affected | MED | Include affected parties vs skip | Include affected parties | Not relevant to them |
| Support/enabling roles | LOW | Include support vs skip | Include support | Not relevant to them |

---

## Q4: When does information need to be received?
[VOI: HIGH - timing determines whether communication is useful or wasted]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Before action starts | HIGH | Early communication vs later | Early communication | Can share later |
| Unknown timing | MED | Timing analysis vs guess | Timing analysis | Timing known |
| During execution | MED | Ongoing communication vs one-time | Ongoing communication | One-time only |
| On specific schedule | MED | Follow schedule vs ad-hoc | Follow schedule | Ad-hoc timing |
| After completion | LOW | Completion report vs earlier | Completion report | Earlier needed |

---

## Q5: What is the consequence if information not received?
[VOI: HIGH - determines priority and urgency of communication]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Goal failure | HIGH | Ensure delivery at all costs vs deprioritize | Ensure delivery | Not that critical |
| Unknown consequence | MED | Consequence analysis vs assume low | Consequence analysis | Consequence known |
| Significant delay | MED | Prioritize delivery vs standard priority | Prioritize delivery | Minor impact |
| Minor inconvenience | LOW | Share when convenient vs deprioritize | Share when convenient | More important |
| No consequence | LOW | Skip or deprioritize vs prioritize | Skip or deprioritize | Actually has consequence |

---

## Q6: Is there information that should NOT be shared?
[VOI: HIGH - sharing restricted info could cause serious harm]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, sensitive information | HIGH | Protect information vs share freely | Protect information | Can share freely |
| Unknown restrictions | HIGH | Restriction discovery vs share freely | Restriction discovery | Restrictions known |
| Yes, timing-sensitive | MED | Control timing vs share anytime | Control timing | Share anytime |
| Yes, need-to-know basis | MED | Restrict access vs open sharing | Restrict access | Open sharing |
| No restrictions | LOW | Share freely vs restrict | Share freely | Restrictions exist |

---

## Q7: What controls prevent unintended sharing?
[VOI: HIGH - no controls means vulnerability to breach]
Prerequisite: Q6 = Yes

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No controls in place | HIGH | Implement controls vs maintain status quo | Implement controls | Controls exist |
| Unknown controls | MED | Control audit vs assume covered | Control audit | Controls known |
| Technical controls (access) | MED | Use access controls vs different approach | Use access controls | No technical controls |
| Policy controls (rules) | LOW | Follow policies vs different controls | Follow policies | Different controls |
| Physical controls (location) | LOW | Maintain separation vs different controls | Maintain separation | Different controls |

---

## Q8: Is current goal state visible to relevant parties?
[VOI: HIGH - hidden state or over-exposure changes entire visibility strategy]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Not visible | HIGH | Increase visibility vs maintain | Increase visibility | Visibility exists |
| Should be less visible | HIGH | Reduce visibility vs maintain | Reduce visibility | Visibility appropriate |
| Unknown visibility | MED | Visibility audit vs assume adequate | Visibility audit | Visibility known |
| Partially visible | MED | Address gaps vs accept | Address gaps | Fully visible or hidden |
| Yes, fully visible | LOW | Maintain visibility vs increase | Maintain visibility | Gaps exist |

---

## Q9: Does pursuing this goal send signals to others?
[VOI: HIGH - unintentional signals need active management]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, unintentional signals | HIGH | Understand/manage vs ignore | Understand/manage | Signals controlled |
| Unknown signals | MED | Signal analysis vs proceed | Signal analysis | Signals known |
| Yes, intentional signals | MED | Manage signals vs let happen | Manage signals | No signals |
| No significant signals | LOW | Proceed vs analyze | Proceed | Signals exist |

---

## Q10: Could signals be misinterpreted?
[VOI: HIGH - high misinterpretation risk requires prevention measures]
Prerequisite: Q9 = Yes

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, high risk | HIGH | Prevention measures vs monitor only | Prevention measures | Low risk |
| Unknown risk | MED | Interpretation analysis vs assume clear | Interpretation analysis | Risk known |
| Yes, moderate risk | MED | Monitor interpretation vs ignore | Monitor interpretation | Low risk |
| No, clear signals | LOW | Continue signaling vs change approach | Continue signaling | Risk exists |

---

## Q11: How will message receipt be confirmed?
[VOI: HIGH - no confirmation means unknown delivery status]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No confirmation | HIGH | Add confirmation vs send and hope | Add confirmation | Confirmation exists |
| Unknown confirmation method | MED | Confirmation design vs assume okay | Confirmation design | Method known |
| Explicit confirmation | MED | Request confirmation vs implicit | Request confirmation | No confirmation |
| Implicit confirmation | LOW | Observe behavior vs request explicit | Observe behavior | Explicit needed |

---

## Q12: Should this communication be documented?
[VOI: HIGH - required documentation cannot be skipped]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, required | HIGH | Document fully vs skip | Document fully | Not required |
| Unknown if needed | MED | Documentation policy check vs assume not | Documentation policy | Policy known |
| Yes, recommended | MED | Document vs skip | Document | Not necessary |
| No documentation needed | LOW | Skip documentation vs document | Skip documentation | Documentation needed |

---

## Question Order by Action Divergence

**HIGH VOI Questions (ask first - route to different action paths):**
1. Q1: Is there information others need? (determines if communication needed)
2. Q6: Is there information that should NOT be shared? (confidentiality check)
3. Q5: What is the consequence if not received? (stakes)
4. Q8: Is current goal state visible? (visibility strategy)
5. Q11: How will receipt be confirmed? (delivery assurance)
6. Q12: Should this be documented? (compliance)

**MED VOI Questions (ask second - same direction, different approach):**
7. Q3: Who needs to receive this? (recipients)
8. Q4: When does it need to be received? (timing)
9. Q9: Does pursuing this send signals? (signaling)
10. Q2: What information needs to be shared? (content)
11. Q7: What controls prevent unintended sharing? (security)
12. Q10: Could signals be misinterpreted? (interpretation risk)

---

## Key Insight

**VOI ≠ Importance or Severity**

VOI = Action Divergence

A question has HIGH VOI when different answers lead to completely different action paths. "Is there sensitive information?" is HIGH VOI because YES → protect, NO → share freely. These are opposite actions.

A question has LOW VOI when different answers lead to the same basic action with minor variations. "Use policy controls or physical controls?" is LOW VOI because both are controls with similar implementation effort.

---

## Coverage Summary

```
QUESTIONS: 12
GUESSES: 58

VOI Distribution:
- HIGH: 14 guesses (24%)
- MED: 28 guesses (48%)
- LOW: 16 guesses (28%)

HIGH-VOI Entries (ask first):
- Q1: Yes, critical information / Unknown - determines communication need
- Q2: Decisions / Requirements / Risks / Unknown - content determines approach
- Q3: Decision makers / Unknown recipients - wrong audience wastes effort
- Q4: Before action starts - prerequisite info timing critical
- Q5: Goal failure - determines urgency priority
- Q6: Yes, sensitive / Unknown restrictions - confidentiality determines sharing
- Q7: No controls in place - vulnerability requires intervention
- Q8: Not visible / Should be less visible - visibility strategy changes
- Q9: Yes, unintentional signals - uncontrolled messaging requires management
- Q10: Yes, high risk - prevention measures vs monitoring
- Q11: No confirmation - unknown delivery requires new approach
- Q12: Yes, required - documentation mandatory
```

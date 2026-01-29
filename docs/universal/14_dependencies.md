# Universal: Dependencies (14)

**Category**: CORE - Comprehensive Dependency Analysis
**Source**: [O: universal_goal_analysis.yaml lines 269-297 dependencies category] + [D: original CORE DIMENSIONS]
**Structure**: One question per entry, VOI-marked with realistic distribution
**Note**: Merged from 14_dependencies (properties) and 28_dependencies (prerequisites/hidden)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

# PART A: DEPENDENCY PROPERTIES

## Q1: What is the dependency strength?
[VOI: HIGH - hard dependency (blocking) = must satisfy first]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Hard dependency (blocking) | HIGH | Cannot proceed = must satisfy first | Must satisfy first | Soft dependency |
| Conditional dependency | MED | Depends on circumstances | Monitor conditions | Unconditional |
| Unknown strength | MED | Assessment needed | Strength assessment | Strength known |
| Soft dependency (helpful) | LOW | Nice to have | Get if convenient | Hard dependency |

---

## Q2: What is the dependency direction?
[VOI: HIGH - you depend on others / mutual = coordination critical]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| You depend on others | HIGH | Blocked until they deliver = waiting vs acting | Track their progress | They depend on you |
| Mutual dependency | HIGH | Requires coordination = different mode | Coordinate closely | One-way dependency |
| Others depend on you | MED | You're on critical path | Prioritize your output | No dependents |
| Unknown direction | MED | Clarification needed | Direction discovery | Direction known |

---

## Q3: What must happen before the goal can be achieved?
[VOI: HIGH - prerequisites unclear = can't sequence]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Prerequisites unclear | HIGH | Can't sequence = must clarify first | Prerequisite analysis | Prerequisites clear |
| Prerequisites clear | LOW | Can sequence | Plan sequence | Prerequisites unclear |
| No prerequisites | LOW | Can start immediately | Begin | Prerequisites exist |

---

## Q4: Is each prerequisite under my control or external?
[VOI: HIGH - some/all external = may be blocked]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Some external dependencies | HIGH | May be blocked = coordination needed | Manage dependencies | All under control |
| All external | HIGH | Fully dependent = can't proceed alone | Coordination required | Some under control |
| Unknown control | MED | Analysis needed | Control analysis | Control known |
| All under my control | MED | Self-directed | Execute independently | External factors |

---

## Q5: What alternatives exist if dependency fails?
[VOI: HIGH - no alternatives = single point of failure]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No alternatives | HIGH | Single point of failure = must protect | Protect dependency | Alternatives exist |
| Alternative exists | MED | Fallback option | Plan fallback | No alternative |
| Unknown alternatives | MED | Research needed | Alternative search | Alternatives known |
| Multiple alternatives | LOW | Robust | Choose best fallback | Fewer alternatives |

---

## Q6: What is the dependency reliability?
[VOI: HIGH - unreliable = may not come through, contingency needed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unreliable | HIGH | May not come through = contingency needed | Contingency plan | More reliable |
| Moderately reliable | MED | Monitor | Track status | More or less reliable |
| Unknown reliability | MED | Assessment needed | Reliability assessment | Reliability known |
| Highly reliable | LOW | Trust it | Proceed confidently | Less reliable |

---

## Q7: Who controls the dependency?
[VOI: HIGH - unknown / no one controls = can't influence]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown who controls | HIGH | Can't influence = blocked | Find controller | Controller known |
| No one controls (external) | HIGH | Uncontrollable = must adapt | Adapt to external | Someone controls |
| Known person/team controls | MED | Can influence | Coordinate with them | Unknown controller |
| You control it | LOW | Can manage directly | Manage yourself | Others control |

---

## Q8: Which prerequisites cannot be replaced if they fail?
[VOI: HIGH - irreplaceable identified = critical dependencies, protect these]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Irreplaceable identified | HIGH | Critical dependencies = protect these | Protect irreplaceable | Different irreplaceable |
| Unknown replaceability | MED | Analysis needed | Alternative analysis | Status known |
| All have alternatives | LOW | Flexible | Maintain alternatives | Some irreplaceable |

---

## Q9: Can any prerequisites be eliminated by changing approach?
[VOI: HIGH - yes, can eliminate = simplification possible, consider new approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, can eliminate some | HIGH | Simplification possible = consider new approach | Consider new approach | Cannot eliminate |
| No, all essential | MED | Must complete all | Accept dependencies | Some can be eliminated |
| Unknown if eliminable | MED | Exploration needed | Approach exploration | Status known |

---

## Q10: What am I assuming will continue to be available?
[VOI: HIGH - hidden assumptions = may lose access]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Hidden assumptions exist | HIGH | May lose access = surface them | Assumption surfacing | All explicit |
| Unknown assumptions | HIGH | Risk of surprise = analysis needed | Assumption analysis | Assumptions known |
| Assumptions explicit | MED | Can monitor | Monitor assumptions | Hidden assumptions |

---

## Q11: What am I assuming others will do that they might not?
[VOI: HIGH - hidden behavior assumptions = may not cooperate]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Hidden behavior assumptions | HIGH | May not cooperate = surface them | Assumption surfacing | All explicit |
| Behavior assumptions explicit | MED | Can verify | Verify with others | Hidden assumptions |
| Unknown assumptions | MED | Analysis needed | Assumption analysis | Assumptions known |

---

## Q12: Do dependencies exist?
[VOI: HIGH - many dependencies = complex coordination]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Many dependencies | HIGH | Complex coordination changes approach | Extensive coordination | Simpler |
| Unknown if dependencies | MED | Discovery needed | Dependency mapping | Dependencies known |
| Some dependencies | LOW | Normal situation | Manage dependencies | More or fewer |
| No dependencies | MED | Simplifies but rare | Independent work | Dependencies exist |

---

## Q13: What type of dependencies?
[VOI: HIGH - approval / external = blocking or outside control]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Approval dependency | HIGH | Blocked without approval = different path | Get approval first | No approval needed |
| External dependency | HIGH | Outside control = different approach | Coordinate with external | Internal control |
| Information dependency | MED | Wait for data | Get information first | No info needed |
| Resource dependency | MED | Wait for resources | Acquire resources first | Resources available |
| Sequence dependency | MED | Order matters | Follow sequence | Parallel possible |
| Technical dependency | MED | Build order | Build dependencies first | Independent |
| Unknown type | MED | Type discovery | Identify dependency types | Types known |

---

## Q14: What is the dependency timeline?
[VOI: HIGH - long wait = major delay, different strategy]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Long wait | HIGH | Major delay = different strategy | Plan for delay | Shorter wait |
| Soon to be satisfied | MED | Short wait | Plan for near-term | Longer wait |
| Unknown timing | MED | Timeline discovery | Timing assessment | Timing known |
| Already satisfied | LOW | Can proceed | Proceed | Not yet satisfied |

---

## Q15: What is the probability each prerequisite will be completed?
[VOI: HIGH - low probability = risky dependency, contingency required]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Low probability (<40%) | HIGH | Risky dependency = contingency required | Contingency required | Higher probability |
| Medium probability (40-80%) | MED | Some risk | Contingency planning | Different probability |
| Unknown probability | MED | Assessment needed | Probability analysis | Probability known |
| High probability (>80%) | LOW | Likely completion | Plan normally | Lower probability |

---

## Q16: Which prerequisites have highest failure probability?
[VOI: HIGH - unknown risk levels = may be blindsided]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown risk levels | HIGH | May be blindsided = risk assessment needed | Risk assessment | Risk known |
| High-risk items identified | MED | Can mitigate | Mitigation planning | Different high-risk |
| No high-risk items | LOW | Low risk overall | Standard execution | High-risk items exist |

---

## Q17: What is the cost of the dependency?
[VOI: HIGH - high cost = consider alternatives]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| High cost | HIGH | Major investment = consider alternatives | Consider alternatives | Lower cost |
| Moderate cost | MED | Significant investment | Evaluate ROI | Different cost |
| Unknown cost | MED | Assessment needed | Cost assessment | Cost known |
| No cost | LOW | Free | Accept dependency | Cost exists |
| Low cost | LOW | Minor investment | Accept dependency | Higher cost |

---

## Q18: What is the longest chain of sequential prerequisites?
[VOI: MED - complexity affects planning]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Long chain (6+ steps) | MED | Complex path | Detailed planning | Shorter chain |
| Medium chain (3-5 steps) | MED | Moderate complexity | Careful sequencing | Different length |
| Unknown chain length | MED | Analysis needed | Critical path analysis | Length known |
| Short chain (1-2 steps) | LOW | Quick path | Simple planning | Longer chain |

---

## Q19: Which prerequisites appear in multiple chains (bottlenecks)?
[VOI: MED - prioritization needed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Bottlenecks identified | MED | Can prioritize | Focus on bottlenecks | Different bottlenecks |
| Unknown bottlenecks | MED | Analysis needed | Bottleneck analysis | Bottlenecks known |
| No bottlenecks | LOW | Parallel paths | Parallel execution | Bottlenecks exist |

---

## Q20: What am I assuming about the environment that could change?
[VOI: MED - environmental disruption]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Hidden environment assumptions | MED | May be disrupted | Assumption surfacing | All explicit |
| Unknown assumptions | MED | Analysis needed | Assumption analysis | Assumptions known |
| Environment assumptions explicit | LOW | Can monitor | Monitor environment | Hidden assumptions |

---

## Q21: What events would invalidate these assumptions?
[VOI: MED - monitoring needed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Invalidating events identified | MED | Can monitor | Monitor for events | Different events |
| Unknown events | MED | Analysis needed | Event analysis | Events known |
| No invalidating events | LOW | Robust assumptions | Proceed confidently | Events exist |

---

## Q22: Can the dependency be removed?
[VOI: MED - flexibility option]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, easily removed | MED | Flexible | Remove if useful | Not removable |
| Yes, with effort | MED | Option exists | Consider removing | More or less effort |
| No, cannot be removed | MED | Must work with | Accept and manage | Can be removed |
| Unknown if removable | LOW | Worth exploring | Removability analysis | Removability known |

---

## Coverage Summary

```
QUESTIONS: 22 (merged from 14_ and 28_)
ENTRIES: 92

VOI Distribution:
- HIGH: 19 entries (21%)
- MED: 47 entries (51%)
- LOW: 26 entries (28%)

SECTIONS:
A. Dependency Properties: strength, direction, alternatives, reliability, control, replaceability, elimination, assumptions
B. Prerequisites: clarity, control, probability, chain length, bottlenecks, risk
C. Hidden Dependencies: availability, behavior, environment assumptions

HIGH-VOI Entries (ask first - route to different action paths):
- Q1: Hard dependency - cannot proceed without
- Q2: You depend on others / Mutual - coordination critical
- Q3: Prerequisites unclear - can't sequence
- Q4: Some/All external - may be blocked
- Q5: No alternatives - single point of failure
- Q6: Unreliable - may not come through
- Q7: Unknown / No one controls - can't influence
- Q8: Irreplaceable identified - critical dependencies
- Q9: Yes, can eliminate - simplification possible
- Q10-Q11: Hidden assumptions - may lose access / cooperation
- Q12: Many dependencies - complex coordination
- Q13: Approval / External dependency - blocking or outside control
- Q14: Long wait - major delay
- Q15: Low probability - risky dependency
- Q16: Unknown risk levels - may be blindsided
- Q17: High cost - major investment
```

---

## Question Order by Action Divergence

**Ask HIGH VOI questions first - they route to completely different action paths:**

1. **Q1** (Strength) - is this blocking?
2. **Q2** (Direction) - who depends on whom?
3. **Q3** (Prerequisites) - what must happen first?
4. **Q4** (Control) - am I dependent on externals?
5. **Q5** (Alternatives) - fallback options?
6. **Q8** (Irreplaceable) - critical dependencies?
7. **Q10-Q11** (Hidden assumptions) - what could break?
8. **Q6** (Reliability) - will it come through?
9. **Q7** (Who controls) - can we influence?
10. **Q15** (Probability) - how likely to complete?
11. **Q13** (Type) - approval/external?
12. **Q14, Q17** (Timeline, cost)
13. **Q18-Q22** (Details)

---

## Key Insight

**VOI ≠ Importance or Difficulty**

VOI = Action Divergence

A question has HIGH VOI when different answers send you down completely different paths. "Is this a hard blocking dependency?" routes to must-satisfy-first vs can-proceed. "Are there hidden assumptions about others' behavior?" routes to surfacing work vs proceeding.

LOW VOI questions may still matter, but different answers lead to the same general actions with minor adjustments.

# Universal: Execution (30)

**Category**: CORE - Execution Analysis
**Source**: [O: universal_goal_analysis.yaml lines 362-415 execution category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: What is the specific next physical action required?
[VOI: HIGH - unknown next action means paralyzed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown next action | HIGH | Action identification vs paralysis | Action identification | Action known |
| Next action vague | MED | Define action vs proceed vaguely | Define action | Action clear |
| Next action clear | LOW | Take action vs clarify | Take action | Wrong action |

---

## Q2: What inputs does that action require?
[VOI: MED - affects preparation but not overall direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Inputs unavailable | MED | Input acquisition vs proceed | Input acquisition | Inputs available |
| Unknown inputs needed | MED | Input analysis vs guess | Input analysis | Inputs known |
| Inputs available | LOW | Execute vs verify inputs | Execute | Inputs unavailable |

---

## Q3: What is currently preventing that action from being taken?
[VOI: HIGH - unknown blockers means stuck without knowing why]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Blockers exist, unknown | HIGH | Blocker identification vs stay stuck | Blocker identification | Blockers known |
| Blockers identified | MED | Remove blockers vs work around | Remove blockers | Different blockers |
| No blockers | LOW | Execute vs investigate | Execute | Blockers exist |

---

## Q4: What stages must be progressed through to reach the goal?
[VOI: HIGH - unknown stages means can't track progress]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Stages unknown | HIGH | Stage definition vs proceed blind | Stage definition | Stages known |
| Stages partially defined | MED | Complete definition vs proceed | Complete definition | Stages clear |
| Stages clearly defined | LOW | Follow stages vs redefine | Follow stages | Stages unclear |

---

## Q5: What condition marks completion of each stage?
[VOI: HIGH - unknown completion criteria means don't know when done]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown completion criteria | HIGH | Criteria definition vs guess | Criteria definition | Criteria known |
| Completion criteria vague | MED | Clarify criteria vs interpret | Clarify criteria | Criteria clear |
| Completion criteria clear | LOW | Use criteria vs refine | Use criteria | Criteria unclear |

---

## Q6: What portion of stage duration is determined by my effort vs external factors?
[VOI: MED - affects expectations but not overall approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Mostly externally determined | MED | Accept pace vs push | Accept pace | More effort-based |
| Unknown control | MED | Control analysis vs assume | Control analysis | Control known |
| Mostly effort-determined | LOW | Push harder vs accept | Can control pace | More external |

---

## Q7: What triggers will initiate goal-related action?
[VOI: MED - affects action reliability but not goal direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No triggers defined | MED | Define triggers vs memory | Define triggers | Triggers exist |
| Unknown if triggers work | MED | Trigger testing vs assume | Trigger testing | Triggers known |
| Triggers defined | MED | Use triggers vs refine | Use triggers | Triggers wrong |

---

## Q8: What changes to environment would increase action frequency?
[VOI: MED - optimization opportunity but same direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Changes identified | MED | Make changes vs status quo | Make changes | Different changes |
| Unknown changes | LOW | Environment analysis vs accept | Environment analysis | Changes known |
| No changes would help | LOW | Maintain vs seek changes | Maintain | Changes exist |

---

## Q9: What structure verifies actions are being taken as planned?
[VOI: MED - accountability structure but same direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No verification structure | MED | Create structure vs drift | Create structure | Structure exists |
| Unknown if structure exists | LOW | Structure audit vs assume | Structure audit | Status known |
| Verification structure exists | LOW | Use structure vs create new | Use structure | Structure insufficient |

---

## Q10: At what stage did a failure occur?
[VOI: HIGH - goal/planning failure vs execution failure requires different response]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Goal definition failure | HIGH | Redefine goal vs fix execution | Redefine goal | Different stage |
| Planning failure | HIGH | Replan vs execute better | Replan | Different stage |
| Unknown failure stage | HIGH | Failure analysis vs guess | Failure analysis | Stage known |
| Execution failure | MED | Fix execution vs replan | Fix execution | Different stage |
| Monitoring failure | MED | Fix monitoring vs continue | Fix monitoring | Different stage |
| External event failure | LOW | Accept or adapt vs blame self | Accept or adapt | Within control |

---

## Q11: Can the plan be simplified by removing steps?
[VOI: MED - efficiency opportunity but same direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, can simplify | MED | Simplify vs maintain | Simplify | Cannot simplify |
| Unknown if simplifiable | LOW | Simplification analysis vs maintain | Simplification analysis | Status known |
| No, all steps essential | LOW | Maintain plan vs analyze | Maintain plan | Can simplify |

---

## Q12: At what point should the goal be abandoned rather than adjusted?
[VOI: HIGH - no abandonment criteria means may persist too long]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No abandonment criteria | HIGH | Define criteria vs persist forever | Define criteria | Criteria exist |
| Unknown abandonment point | MED | Criteria definition vs assume never | Criteria definition | Point known |
| Abandonment criteria clear | MED | Monitor criteria vs refine | Monitor criteria | Criteria unclear |

---

## Question Order by Action Divergence

**HIGH VOI Questions (ask first - route to different action paths):**
1. Q1: What is the specific next action? (what do I do now?)
2. Q3: What is preventing that action? (what's stopping me?)
3. Q4: What stages must be progressed through? (what's the path?)
4. Q5: What marks completion of each stage? (how do I know progress?)
5. Q12: When should goal be abandoned? (when to quit?)
6. Q10: At what stage did failure occur? (where did it go wrong?)

**MED VOI Questions (ask second - same direction, different approach):**
7. Q2: What inputs does action require? (preparation)
8. Q6: What controls stage duration? (expectations)
9. Q7: What triggers initiate action? (reliability)
10. Q9: What structure verifies actions? (accountability)
11. Q11: Can plan be simplified? (efficiency)
12. Q8: What environment changes help? (optimization)

---

## Key Insight

**VOI ≠ Importance or Severity**

VOI = Action Divergence

A question has HIGH VOI when different answers lead to completely different action paths. "At what stage did failure occur?" is HIGH VOI because GOAL DEFINITION → redefine the goal, EXECUTION → fix how you're implementing. These are fundamentally different responses.

Execution determines whether plans actually get implemented and progress gets made.

---

## Coverage Summary

```
QUESTIONS: 12
GUESSES: 46

VOI Distribution:
- HIGH: 8 entries (17%)
- MED: 24 entries (52%)
- LOW: 14 entries (31%)

HIGH-VOI Entries (ask first):
- Q1: Unknown next action - paralyzed
- Q3: Blockers exist, unknown - stuck
- Q4: Stages unknown - can't track progress
- Q5: Unknown completion criteria - don't know when done
- Q10: Goal/Planning/Unknown failure - wrong goal or plan
- Q12: No abandonment criteria - may persist too long
```

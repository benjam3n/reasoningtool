# Universal: Timing (34)

**Category**: CORE - Timing Analysis
**Source**: [O: universal_goal_analysis.yaml lines 670-704 timing category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Is there a deadline?
[VOI: HIGH - hard deadline makes goal time-critical]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, hard deadline | HIGH | Work to deadline urgently vs flexible | Work to deadline | No deadline |
| Unknown if deadline | MED | Deadline discovery vs assume none | Deadline discovery | Status known |
| Yes, soft deadline | MED | Aim for deadline vs ignore | Aim for deadline | Harder or softer |
| No deadline | LOW | Work at own pace vs rush | Work at own pace | Deadline exists |

---

## Q2: What creates the deadline?
[VOI: HIGH - external vs self-imposed changes negotiability completely]
Prerequisite: Q1 = Deadline exists

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| External requirement | HIGH | Must meet vs negotiate | Must meet | Not external |
| Opportunity window | HIGH | Act in window vs miss | Act in window | Window is longer |
| Unknown source | MED | Source discovery vs assume | Source discovery | Source known |
| Resource expiration | MED | Use before expiry vs extend | Use before expiry | Different source |
| Self-imposed | LOW | Can adjust vs keep | Can adjust | Actually external |

---

## Q3: What is the consequence of missing the deadline?
[VOI: HIGH - goal fails entirely means critical deadline]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Goal fails entirely | HIGH | Cannot miss deadline vs accept | Cannot miss | Less severe |
| Unknown consequence | MED | Consequence analysis vs assume minor | Consequence analysis | Consequence known |
| Significant penalty | MED | Prioritize deadline vs accept penalty | Prioritize deadline | Different consequence |
| Minor inconvenience | LOW | Miss if needed vs prioritize | Miss if needed | More severe |

---

## Q4: Is the deadline changeable?
[VOI: MED - affects planning flexibility but same general approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown changeability | MED | Negotiate check vs assume fixed | Negotiate check | Status known |
| Yes, negotiable | MED | Negotiate if needed vs accept | Negotiate if needed | Not negotiable |
| No, fixed | MED | Must work to it vs negotiate | No negotiation | Actually negotiable |

---

## Q5: What must happen in what order?
[VOI: HIGH - unknown sequence means can't order actions]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Sequence unknown | HIGH | Sequence analysis vs guess | Sequence analysis | Sequence known |
| Sequence partially known | MED | Complete sequence vs proceed | Complete sequence | Sequence clear |
| Sequence clearly defined | LOW | Follow sequence vs reanalyze | Follow sequence | Sequence unclear |

---

## Q6: What can happen simultaneously?
[VOI: MED - affects optimization but same general direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown parallel potential | MED | Parallel analysis vs assume sequential | Parallel analysis | Status known |
| Parallel opportunities identified | MED | Use parallelization vs sequential | Use parallelization | Less parallelizable |
| All must be sequential | LOW | Follow sequence vs seek parallel | Follow sequence | Parallel possible |

---

## Q7: Which steps can be parallelized to reduce total time?
[VOI: MED - optimization within same direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown opportunities | LOW | Opportunity analysis vs sequential | Opportunity analysis | Status known |
| Parallelization opportunities clear | MED | Parallelize vs sequential | Parallelize | Fewer opportunities |
| No parallelization possible | LOW | Sequential only vs seek parallel | Sequential only | Parallelization exists |

---

## Q8: Which steps have slack time that can absorb delays?
[VOI: MED - affects buffer strategy]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown slack | MED | Slack analysis vs assume none | Slack analysis | Slack known |
| No slack exists | MED | Critical path focus vs buffer | Critical path focus | Slack exists |
| Slack identified | LOW | Use slack as buffer vs create more | Use slack | Less slack |

---

## Q9: Which ordering minimizes cost of potential failure?
[VOI: MED - affects ordering but same general direction]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown optimal order | MED | Risk analysis vs guess | Risk analysis | Order known |
| Risk-optimal order known | MED | Use optimal order vs any | Use optimal order | Different order better |
| All orderings equal risk | LOW | Flexible order vs optimize | Any order fine | Some better |

---

## Q10: Which ordering maximizes ability to abandon early if needed?
[VOI: MED - affects ordering strategy]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Abandonment-optimal order known | MED | Use optimal order vs any | Use optimal order | Different order better |
| Unknown optimal order | LOW | Analysis vs any order | Analysis | Order known |
| All orderings equal | LOW | Flexible vs optimize | Any order fine | Some better |

---

## Q11: Are there time periods when this goal is easier to achieve?
[VOI: MED - affects timing but same goal]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown windows | MED | Window research vs proceed | Window research | Windows known |
| Favorable windows exist | MED | Use favorable windows vs anytime | Use favorable windows | No windows |
| No favorable windows | LOW | Any time fine vs seek windows | Any time fine | Windows exist |

---

## Q12: Is the current time within an opportunity window?
[VOI: HIGH - in window now means act now]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, in window now | HIGH | Take advantage immediately vs wait | Take advantage | Not in window |
| Unknown window status | MED | Window assessment vs proceed | Window assessment | Status known |
| No, window closed | MED | Wait for next vs force | Wait for next | Window open |
| No, window not yet open | MED | Plan for window vs start now | Plan for window | Window situation different |

---

## Question Order by Action Divergence

**HIGH VOI Questions (ask first - route to different action paths):**
1. Q1: Is there a deadline? (is there time pressure?)
2. Q3: What is consequence of missing? (how bad if missed?)
3. Q12: Is current time in opportunity window? (is now the right time?)
4. Q2: What creates the deadline? (why the deadline?)
5. Q5: What must happen in what order? (sequence)

**MED VOI Questions (ask second - same direction, different approach):**
6. Q4: Is deadline changeable? (flexibility)
7. Q6: What can happen simultaneously? (parallelization)
8. Q11: Are there favorable time periods? (timing optimization)
9. Q8: Which steps have slack? (buffer strategy)
10. Q9: Which ordering minimizes failure cost? (risk optimization)
11. Q7: Which steps can be parallelized? (speed optimization)
12. Q10: Which ordering maximizes early abandonment? (exit strategy)

---

## Key Insight

**VOI ≠ Importance or Severity**

VOI = Action Divergence

A question has HIGH VOI when different answers lead to completely different action paths. "Is there a hard deadline?" is HIGH VOI because YES → time-critical planning with urgency, NO → flexible pacing. "Is now within an opportunity window?" is HIGH VOI because YES → act immediately, NO → wait.

Timing determines when to act and how urgently.

---

## Coverage Summary

```
QUESTIONS: 12
GUESSES: 48

VOI Distribution:
- HIGH: 6 entries (12%)
- MED: 29 entries (60%)
- LOW: 13 entries (28%)

HIGH-VOI Entries (ask first):
- Q1: Yes, hard deadline - time-critical
- Q2: External requirement / Opportunity window - non-negotiable or time-sensitive
- Q3: Goal fails entirely - critical deadline
- Q5: Sequence unknown - can't order actions
- Q12: Yes, in window now - act now
```

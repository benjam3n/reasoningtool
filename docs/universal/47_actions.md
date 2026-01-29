# Universal: Action Analysis (47)

**Category**: CORE - Action Identification and Comparison
**Source**: [O: universal_goal_analysis.yaml lines 1344-1430 action_analysis category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: What is the next milestone?
[VOI: HIGH - No clear milestone means define direction vs work toward target]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No clear milestone | HIGH | Define milestone vs proceed | Define milestone | Milestone exists |
| Unknown next milestone | HIGH | Milestone discovery vs proceed | Milestone discovery | Milestone known |
| Multiple potential milestones | MED | Select one vs proceed | Select one | Single milestone |
| Clear next milestone | LOW | Work toward it either way | Work toward it | Milestone unclear |

---

## Q2: What actions would make each condition true?
[VOI: HIGH - Actions unclear or none work means discovery or change vs execute]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Actions unclear | HIGH | Action discovery vs execute | Action discovery | Actions clear |
| No actions would work | HIGH | Change condition vs execute | Change condition | Actions exist |
| Multiple possible actions | MED | Compare and select vs execute | Compare and select | Single action |
| Actions identified | LOW | Execute actions either way | Take actions | Wrong actions |

---

## Q3: Once taken, can action be undone?
[VOI: HIGH - Irreversible requires extra diligence vs proceed freely]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Irreversible | HIGH | Extra diligence vs proceed freely | Extra diligence | Actually reversible |
| Unknown reversibility | HIGH | Analysis first vs assume reversible | Reversibility analysis | Reversibility known |
| Reversible at cost | MED | Factor cost vs proceed freely | Factor cost | Different level |
| Fully reversible | LOW | Proceed freely either way | Proceed freely | Not reversible |

---

## Q4: Does waiting reduce action effectiveness?
[VOI: HIGH - Significant decay means act now vs act when ready]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, significant decay | HIGH | Act now vs act later | Act now | Less decay |
| Unknown time sensitivity | MED | Timing analysis vs assume | Timing analysis | Sensitivity known |
| Yes, gradual decay | MED | Act soon vs act later | Act soon | Different rate |
| No, timing flexible | LOW | Act when ready either way | Act when ready | Decay exists |

---

## Q5: How many other actions depend on this one?
[VOI: HIGH - Many depend means critical path priority vs flexible timing]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Many depend on this | HIGH | Prioritize vs flexible | Prioritize | Fewer depend |
| Unknown dependencies | MED | Dependency mapping vs assume | Dependency mapping | Dependencies known |
| Some depend on this | MED | Consider priority vs flexible | Consider priority | Different amount |
| Nothing depends on this | LOW | Flexible timing either way | Any time | Things depend |

---

## Q6: What is the probability each action fails?
[VOI: HIGH - High probability means change action or prepare vs proceed confidently]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| High probability | HIGH | Change action or prepare vs proceed | Change action or prepare | Lower risk |
| Unknown probability | MED | Risk analysis vs assume | Risk analysis | Probability known |
| Moderate probability | MED | Prepare contingency vs proceed | Prepare contingency | Different level |
| Low failure probability | LOW | Proceed confidently either way | Proceed confidently | Higher risk |

---

## Q7: If action fails, is effort recoverable?
[VOI: HIGH - Not recoverable means extra diligence vs proceed normally]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Not recoverable | HIGH | Extra diligence vs proceed | Extra diligence | Recoverable |
| Unknown recoverability | MED | Recovery analysis vs assume | Recovery analysis | Recoverability known |
| Partially recoverable | MED | Accept or mitigate vs proceed | Accept or mitigate | Different level |
| Fully recoverable | LOW | Low risk either way | Proceed | Less recoverable |

---

## Q8: Does this action depend on other actions completing first?
[VOI: HIGH - Unknown dependencies means may start wrong vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown dependencies | HIGH | Dependency analysis vs assume | Dependency analysis | Dependencies known |
| Dependencies unsatisfied | MED | Complete dependencies vs start | Complete dependencies | Actually satisfied |
| No dependencies | LOW | Start now either way | Start | Dependencies exist |
| Dependencies satisfied | LOW | Start now either way | Start | Not satisfied |

---

## Q9: What resources are required for each action?
[VOI: HIGH - Resources not available means blocked, find alternatives vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Resources not available | HIGH | Find alternatives vs proceed | Find alternatives | Resources available |
| Unknown resources | MED | Resource analysis vs assume | Resource analysis | Resources known |
| Resources obtainable | MED | Acquire first vs proceed | Acquire first | Not obtainable |
| Resources available | LOW | Can execute either way | Proceed | Resources lacking |

---

## Q10: Are required skills available?
[VOI: HIGH - Skills not available means hire or change vs proceed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Skills not available | HIGH | Hire or change action vs proceed | Hire or change action | Skills available |
| Unknown skills needed | MED | Skills analysis vs assume | Skills analysis | Skills known |
| Skills developable | MED | Develop first vs proceed | Develop first | Not developable |
| Skills available | LOW | Can execute either way | Proceed | Skills lacking |

---

## Q11: Which action is ranked highest by unblock count, cost, risk, urgency?
[VOI: HIGH - No good options means improve options vs execute winner]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No good options | HIGH | Improve options vs execute | Improve options | Good options exist |
| Ranking unclear | MED | Complete analysis vs pick | Complete analysis | Ranking clear |
| Clear winner | MED | Execute winner vs analyze more | Execute winner | Wrong winner |
| Close options | MED | Pick one vs overanalyze | Pick one | One is better |

---

## Q12: What time is required for each action?
[VOI: MED - Duration affects scheduling but not whether to act]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Unknown duration | MED | Duration estimate vs assume | Duration estimate | Duration known |
| Long (weeks+) | MED | Major planning vs quick | Major planning | Actually shorter |
| Moderate (days) | MED | Plan time vs quick | Schedule | Different duration |
| Quick (hours) | LOW | Fast execution either way | Execute quickly | Takes longer |

---

## Question Order by Action Divergence

**HIGH VOI (ask first - route to different action paths):**
1. Q1: Next milestone? (None → define direction vs work toward)
2. Q2: Actions? (Unclear/none work → discovery vs execute)
3. Q3: Reversible? (No → extra diligence vs proceed)
4. Q4: Time-sensitive? (Yes → act now vs later)
5. Q5: Dependencies on this? (Many → critical path vs flexible)
6. Q6: Failure probability? (High → change/prepare vs proceed)
7. Q7: Recoverable? (No → extra diligence vs proceed)
8. Q8: Dependencies? (Unknown → analysis vs proceed)
9. Q9: Resources? (Not available → alternatives vs proceed)
10. Q10: Skills? (Not available → hire/change vs proceed)
11. Q11: Best option? (None good → improve vs execute)

**MED/LOW VOI (ask second - refine approach):**
12. Q12: Duration? (Scheduling, not direction)

---

## Key Insight

**VOI ≠ Action Importance**

VOI = Action Divergence

A HIGH VOI action question is one where the answer determines whether you DO THIS ACTION or DO SOMETHING DIFFERENT. "No clear milestone" routes you to "define milestone first" - a completely different immediate action than "work toward the milestone."

A LOW VOI action question like "quick vs moderate duration" doesn't change what you do - you'll take the action either way, just with different scheduling.

---

## Coverage Summary

```
QUESTIONS: 12
ENTRIES: 50

VOI Distribution:
- HIGH: 12 entries (24%)
- MED: 25 entries (50%)
- LOW: 13 entries (26%)
```

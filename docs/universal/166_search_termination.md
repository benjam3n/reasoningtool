# Universal: Search Termination (166)

**Category**: SEARCH - When To Stop Searching?
**Source**: Optimal stopping theory, satisficing, diminishing returns
**Structure**: Questions ordered by Value of Information (action divergence)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Core Insight

**Stopping too early wastes the search. Stopping too late wastes everything else.**

The optimal stopping point is where:
- Expected value of continuing < cost of continuing
- OR a "good enough" threshold is met
- OR the space is exhausted

Most searches stop too late (sunk cost) or too early (impatience).

---

## Q1: What would change if you kept searching?

[VOI: HIGH - determines whether continuation has value]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Might find significantly better | HIGH | Keep searching | Continue | Stop, miss better |
| Only marginal improvement possible | HIGH | Stop now | Stop | Keep searching pointlessly |
| Unknown | HIGH | Need to estimate | Assess space remaining | Guess wrong about value |

---

## Q2: What's the cost of continued search?

[VOI: HIGH - cost determines stopping threshold]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| High cost (time, resources, opportunity) | HIGH | Lower threshold for stopping | Stop earlier | Overspend on search |
| Low cost | MED | Can afford more search | Continue longer | Stop too early |
| Cost increasing over time | HIGH | Stop sooner | Recognize urgency | Miss deadline |

---

## Q3: Is there a "good enough" threshold?

[VOI: HIGH - satisficing vs maximizing decision]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, threshold exists and is met | HIGH | Stop | Accept current best | Keep searching past value |
| Yes, threshold exists but not met | HIGH | Continue | Search until threshold | Stop prematurely |
| No threshold (must maximize) | MED | Continue until diminishing | Keep optimizing | Satisfice when shouldn't |

---

## Q4: Are returns diminishing?

[VOI: HIGH - diminishing returns = approaching stop point]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, strongly diminishing | HIGH | Stop soon | Recognize plateau | Keep grinding past value |
| Somewhat diminishing | MED | Continue but monitor | Watch for plateau | Miss transition point |
| Not yet diminishing | MED | Continue | Keep searching | Stop before peak |

---

## Q5: How much of the space remains unexplored?

[VOI: HIGH - exhaustion determines possibility of better]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Space mostly exhausted | HIGH | Stop | Accept best found | Keep searching empty space |
| Large unexplored regions | HIGH | Continue or redirect | Explore remaining | Miss opportunities |
| Unknown space size | MED | Estimate before deciding | Map space | Search blindly |

---

## Q6: Is sunk cost affecting the decision?

[VOI: MED - sunk cost fallacy detection]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, continuing because invested | MED | Ignore sunk cost, reassess | Fresh evaluation | Throw good after bad |
| No, decision is forward-looking | LOW | Continue as planned | Proceed | Miss sunk cost influence |

---

## Q7: What's the cost of stopping with wrong answer?

[VOI: MED - error cost determines search investment]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| High cost of error | MED | Search more thoroughly | Invest in certainty | Stop with costly mistake |
| Low cost of error | MED | Can stop earlier | Accept uncertainty | Oversearch for low stakes |
| Errors are reversible | LOW | Can stop and restart | Stop, iterate | Oversearch irreversible |

---

## Q8: Is there a deadline?

[VOI: MED - deadline forces stopping]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Hard deadline approaching | MED | Stop and decide | Take best available | Miss deadline |
| Soft deadline | LOW | Balance search vs time | Negotiate if needed | Treat soft as hard |
| No deadline | LOW | Quality over speed | Continue until satisfied | Create artificial urgency |

---

## Q9: Is the current best "local" or "global"?

[VOI: MED - local optimum trap detection]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Probably local optimum | MED | Restart in different region | Try different area | Settle for local |
| Probably global optimum | LOW | Stop | Accept | Miss global elsewhere |
| Can't tell | MED | Sample other regions | Test alternatives | Assume wrongly |

---

## Q10: What would you advise someone else?

[VOI: LOW - outside view on stopping]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Would advise them to stop | LOW | Probably should stop | Stop | Continue against advice |
| Would advise continuing | LOW | Probably should continue | Continue | Stop against advice |

---

## Summary Statistics

- Total questions: 10
- HIGH VOI: 8
- MED VOI: 8
- LOW VOI: 4

---

## Question Order by Action Divergence

**Ask first (HIGH VOI):**
1. Q1: What would change if you kept searching?
2. Q2: What's the cost of continued search?
3. Q3: Is there a "good enough" threshold?
4. Q4: Are returns diminishing?
5. Q5: How much space remains unexplored?

**Ask if relevant (MED VOI):**
6. Q6: Is sunk cost affecting the decision?
7. Q7: What's the cost of stopping with wrong answer?
8. Q8: Is there a deadline?
9. Q9: Is current best local or global?

**Low priority (LOW VOI):**
10. Q10: What would you advise someone else?

---

## Stopping Heuristics

| Signal | Interpretation | Action |
|--------|---------------|--------|
| Same answers repeatedly | Space exhausted or stuck | Stop or restart elsewhere |
| Each new candidate slightly worse | Past the peak | Stop |
| Excitement decreasing | Diminishing returns | Stop soon |
| "Good enough" found | Threshold met | Stop unless low cost to continue |
| Deadline imminent | Time constraint binding | Stop and decide |
| Sunk cost argument arising | Bias detected | Reassess fresh |

---

## The 37% Rule (Secretary Problem)

For unknown space size with one-shot decision:
1. Explore first 37% without committing
2. Then take next candidate better than all previous
3. Optimal for maximizing probability of best

**When it applies**: Candidates seen once, must decide immediately, can't return
**When it doesn't**: Can revisit candidates, can see multiple, known space size

---

## Common Termination Errors

| Error | Pattern | Fix |
|-------|---------|-----|
| **Premature stopping** | Impatience, first decent option | Set minimum exploration |
| **Sunk cost continuation** | "Already invested so much" | Ignore past, assess future |
| **Perfectionism** | Never good enough | Define threshold upfront |
| **Local optimum settling** | Best in neighborhood, not overall | Sample other regions |
| **Deadline panic** | Rush at end | Start with deadline in mind |

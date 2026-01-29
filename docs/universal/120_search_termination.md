# Universal: Search Termination (120)

**Category**: META - When to Stop Searching
**Source**: Optimization theory, satisficing, diminishing returns
**Structure**: Questions ordered by Value of Information (action divergence)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Are we over-optimizing past the point of value?

[VOI: HIGH - over-optimization wastes resources on negligible gains]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Over-optimizing | HIGH | Wasting resources | Stop now | Miss significant gains |
| Unknown if over-optimizing | MED | May be wasting | Measure marginal value | Either waste or stop early |
| Still gaining value | LOW | Continue searching | Keep optimizing | Stop when gains remain |

---

## Q2: Is there a "good enough" threshold we've already passed?

[VOI: HIGH - already past threshold = stop immediately]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Past good enough | HIGH | Should have stopped | Stop, ship it | Miss better solution |
| Unknown threshold | MED | Can't evaluate | Define threshold | Endless search or premature stop |
| Below threshold | LOW | Must continue | Keep searching | Accept substandard |

---

## Q3: What's the cost of continued search vs the expected improvement?

[VOI: HIGH - wrong calculation = wrong stopping point]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Search cost > expected gain | HIGH | Negative ROI on search | Stop searching | Waste resources on search |
| Unknown ratio | MED | Can't decide | Calculate ratio | Either over or under search |
| Search cost < expected gain | LOW | Positive ROI | Continue | Stop when gains available |

---

## Q4: Have we hit diminishing returns?

[VOI: HIGH - diminishing returns = shift strategy or stop]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Severe diminishing returns | HIGH | Near optimal or wrong approach | Stop or pivot | Grind for nothing |
| Moderate diminishing returns | MED | Getting close | Consider stopping | May stop early |
| Returns still strong | LOW | Keep going | Continue | Miss pivot point |

---

## Q5: Is the search itself causing harm?

[VOI: HIGH - harmful search should stop regardless of potential gains]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Search causing harm | HIGH | Net negative | Stop immediately | Harm continues |
| Unknown if harmful | MED | May be damaging | Assess harm | Either harm or paranoia |
| Search not harmful | LOW | Can continue | Proceed | Actually harmful |

---

## Q6: Is there a deadline forcing termination?

[VOI: MED - deadline affects pacing but similar work]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Hard deadline approaching | MED | Must ship | Stop and ship | Miss deadline |
| Soft deadline | MED | Some flexibility | Balance quality/time | Over/under invest |
| No deadline | LOW | Time flexible | Optimize for quality | Artificial urgency |

---

## Q7: Have we exhausted the search space?

[VOI: MED - exhaustion means different strategy needed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Space exhausted | MED | Nothing left to find | Accept best found | Miss unexplored areas |
| Unknown if exhausted | MED | May be missing | Coverage analysis | Either waste or miss |
| Unexplored regions remain | LOW | More to find | Continue exploration | Revisit exhausted areas |

---

## Q8: Is the current solution "regret-proof"?

[VOI: MED - regret tolerance affects stopping comfort]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Will regret stopping | MED | Not ready | Continue | Stop with regret |
| Unknown regret level | MED | Unclear comfort | Regret analysis | Either regret or over-search |
| Regret-proof | LOW | Comfortable stopping | Stop | Regret later |

---

## Q9: Are we searching out of anxiety vs actual need?

[VOI: LOW - affects mindset but similar decision]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Anxiety-driven search | LOW | Emotional, not rational | Address anxiety, stop | Miss real need |
| Unknown motivation | LOW | May be irrational | Examine motivation | Rationalize emotion |
| Need-driven search | LOW | Rational continuation | Continue | Anxious about real thing |

---

## Q10: Would we know the optimum if we found it?

[VOI: LOW - recognition ability affects confidence but similar process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Can't recognize optimum | LOW | No natural stopping point | Set artificial threshold | Search forever |
| Uncertain recognition | LOW | May miss it | Define recognition criteria | Either miss or paranoid |
| Would recognize optimum | LOW | Clear stopping point | Search until found | Think found when haven't |

---

## Summary Statistics

- Total questions: 10
- Total entries: 38
- HIGH VOI: 9 (24%)
- MED VOI: 14 (37%)
- LOW VOI: 15 (39%)

---

## Question Order by Action Divergence

**Ask first (HIGH VOI):**
1. Q1: Over-optimizing? - wasted resources
2. Q2: Past good enough? - should have stopped
3. Q3: Search cost vs gain? - ROI of continuing
4. Q4: Diminishing returns? - pivot or stop
5. Q5: Search causing harm? - stop regardless

**Ask if relevant (MED VOI):**
6. Q6: Deadline forcing? - time pressure
7. Q7: Space exhausted? - coverage
8. Q8: Regret-proof? - comfort

**Low priority (LOW VOI):**
9. Q9: Anxiety vs need? - motivation
10. Q10: Would recognize optimum? - confidence

---

## Key Insight

**VOI ≠ philosophical depth about optimization. VOI = action divergence.**

"Would we recognize the optimum?" is interesting but has LOW VOI - you search similarly regardless.

"Are we over-optimizing?" has HIGH VOI - if yes, stop immediately and ship.

---

## The Optimizer's Trap

The biggest meta-mistake: optimizing the optimization process indefinitely.

At some point, the search for "when to stop searching" itself needs to stop.

Heuristic: If you're asking these questions, you're probably close enough. Ship it.

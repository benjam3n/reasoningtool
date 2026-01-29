# Universal: Commitment Tree (110)

**Status**: REFINED by 111_commitment_criteria.md

**Issue with this file**: Would commit too easily/arbitrarily. 111 adds agreeability levels:
- Only Level 1 (logically necessary) can be committed
- Levels 2-5 stay OPEN, narrowed only by goal-journey (non-arbitrary)

---

**Category**: META - How to Actually Decide Things
**Source**: [D: from ARAW + observation that questioning alone doesn't converge]
**Structure**: One question per entry, CRUX-marked with realistic distribution
**Purpose**: Move from infinite questioning to actionable commitments

## The Problem

The question-guess-question cycle can explore forever without deciding anything.
To get SPECIFIC (non-universal) answers, you need to:
1. COMMIT to some assumptions
2. DERIVE what follows from those assumptions
3. BUILD a tree of consequences based on commitments

## The Cycle

```
1. GIVEN: What's stated without interpretation?
2. OPEN/CLOSED: Does this claim have alternatives?
   → CLOSED: Accept and move on
   → OPEN: Continue to step 3
3. CRUX?: Would assuming right vs wrong change strategy?
   → No: Skip, doesn't matter enough
   → Yes: Continue to step 4
4. COMMIT: Pick a branch (ASSUME RIGHT or ASSUME WRONG)
5. DERIVE: What follows from this commitment?
6. CHECK: Does this branch work?
   → Yes: Keep the commitment, continue building
   → No: BACKTRACK, try other branch
```

## CRUX Rating Guide
- **HIGH** (10-25%): Wrong commitment = completely different strategy needed
- **MED** (40-50%): Wrong commitment = significant adjustment, but recoverable
- **LOW** (30-40%): Wrong commitment = minor tweaks

---

# PART A: GIVEN (What's stated without interpretation?)

## Q1: What has been explicitly stated?
[D: from user input, data, observations - no inference]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| User stated goal X | LOW | Direct input, take at face value | Work toward X | User misspoke (rare) |
| User stated constraint Y | LOW | Direct input | Honor constraint | Constraint is flexible |
| Data shows Z | LOW | Measurable | Build on Z | Measurement error |
| Nothing explicit | HIGH | Must infer everything = risky | Start inferring | Something was said |

---

## Q2: What type of input is this?
[D: classification affects how to treat it]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| Direct observation | LOW | Strongest evidence | Trust it | Observation flawed |
| User report | LOW | Secondhand but usually reliable | Trust with verification | User wrong |
| Derived from data | MED | Calculation could be wrong | Check derivation | Recalculate |
| Inference | HIGH | Not given, was guessed | Question the inference | It's actually given |
| Nothing given | HIGH | Flying blind | Must commit to assumptions | Something is given |

---

# PART B: OPEN/CLOSED (Does this have alternatives?)

## Q3: Is this claim OPEN or CLOSED?
[D: CLOSED = no alternatives, OPEN = could go either way]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| CLOSED - definitional | LOW | About words, not world | Accept as given | It's actually OPEN |
| CLOSED - foundational | LOW | Base assumption, not questioned | Build on it | Need to question it |
| CLOSED - verified | LOW | Tested and confirmed | High confidence | Test was flawed |
| OPEN - has alternatives | MED | Must choose a branch | Explore branches | No real alternatives |
| OPEN - unknown alternatives | HIGH | Don't know what options exist | Search for options | Options are known |
| OPEN - unbundled from CLOSED | HIGH | Hidden assumption in "known" fact | Question the bundle | Actually closed |

---

## Q4: If OPEN, what are the branches?
[D: enumerate alternatives before committing]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| Two clear alternatives | LOW | Binary, easy to explore | Check both | More options exist |
| Multiple alternatives | MED | Need to prioritize | Rank by CRUX | Missing alternatives |
| Continuous range | MED | Need to discretize | Pick representative points | Discrete is fine |
| Unknown alternatives | HIGH | Can't commit without options | Search first | Options are obvious |
| False dichotomy | HIGH | Presented as binary but isn't | Find third option | Really is binary |

---

# PART C: CRUX (Would this change strategy?)

## Q5: Is this claim CRUX?
[D: CRUX = assuming right vs wrong leads to different strategies]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| HIGH-CRUX - strategy changes | LOW | Worth committing to a branch | Commit and derive | Lower crux than thought |
| MED-CRUX - approach changes | LOW | Worth exploring if time | Consider committing | Different priority |
| LOW-CRUX - details change | LOW | Skip for now | Defer | Higher crux than thought |
| Unknown CRUX | MED | Assess before proceeding | Estimate crux first | CRUX is obvious |
| Everything feels HIGH-CRUX | HIGH | Probably overrating = recalibrate | Apply test strictly | Rating is correct |

---

## Q6: The CRUX Test
[D: operationalize what makes something CRUX]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| If wrong, I do something completely different | HIGH | Definition of HIGH-CRUX | Mark as HIGH | Overstating impact |
| If wrong, I adjust approach but same direction | MED | Significant but recoverable | Mark as MED | Different level |
| If wrong, minor tweaks | LOW | Details only | Mark as LOW | Understating impact |
| If wrong, doesn't matter | LOW | Not CRUX at all | Skip entirely | Actually matters |
| Can't tell impact | MED | Need more context | Gather context | Impact is clear |

---

# PART D: COMMIT (Pick a branch)

## Q7: Which branch to commit to first?
[D: heuristics for choosing which assumption to try]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| More likely branch | LOW | Default: try probable first | Commit to likely | Unlikely is better start |
| Easier to verify branch | LOW | Can check quickly | Commit, then verify | Hard branch first |
| Lower cost if wrong branch | MED | Minimize downside | Commit to safe | Risk the costly |
| User-preferred branch | MED | Respect preferences | Commit to preferred | Preference is wrong |
| Random/arbitrary | LOW | When no heuristic helps | Just pick one | One is clearly better |
| ASSUME WRONG first | MED | Contrarian check | Check if assumption is needed | ASSUME RIGHT first |

---

## Q8: What does COMMIT mean?
[D: nature of the commitment]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| Temporary working assumption | LOW | Can backtrack | Proceed with caveat | Permanent |
| Permanent decision | HIGH | Can't backtrack = be sure | Only if verified | Reversible |
| Hypothesis to test | LOW | Explicitly uncertain | Design test | Not testable |
| Constraint for this branch | MED | Limits options within branch | Accept limits | Constraint is soft |
| Shared commitment (others involved) | HIGH | Coordination cost to change | Communicate clearly | Solo commitment |

---

# PART E: DERIVE (What follows from commitment?)

## Q9: What follows from ASSUME RIGHT?
[D: trace consequences of this branch]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| Specific actions become available | LOW | Opens options | List the actions | Different actions |
| Other claims become CLOSED | MED | Chain of implications | Mark as closed | Still open |
| Constraints narrow | LOW | Fewer possibilities | Work within constraints | Constraints wrong |
| New questions arise | LOW | Opens sub-branches | Question those too | No new questions |
| Contradiction appears | HIGH | Branch doesn't work = backtrack | Backtrack now | Contradiction is apparent |

---

## Q10: What follows from ASSUME WRONG?
[D: trace consequences of the other branch]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| Need different approach entirely | HIGH | Validates this is CRUX | Document alternative | Same approach works |
| Some claims stay open | MED | Less closure than ASSUME RIGHT | Continue exploring | More closure |
| Problem may not exist | HIGH | If wrong, maybe no problem | Reframe problem | Problem is real |
| Better option might exist | MED | Search for alternatives | Search actively | This is best option |
| Nothing changes | LOW | Wasn't actually CRUX | Reclassify as LOW | Something changes |

---

# PART F: CHECK (Does this branch work?)

## Q11: Is this branch working?
[D: criteria for keeping vs backtracking]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| Leads to actionable steps | LOW | Good sign | Keep branch | Backtrack |
| Leads to contradiction | HIGH | Branch is wrong | Backtrack | Contradiction is solvable |
| Leads to more OPEN questions | MED | May need more work | Continue branching | Over-exploring |
| Leads to verified answer | LOW | Branch succeeded | Accept answer | Verification failed |
| Leads nowhere | MED | Dead end | Backtrack | More exploration needed |

---

## Q12: When to BACKTRACK?
[D: signals that this branch isn't working]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| Hit contradiction | HIGH | Branch is logically wrong | Backtrack immediately | Contradiction is resolvable |
| Hit dead end | MED | No further progress | Try other branch | More options exist |
| Better option found | MED | Other branch is superior | Switch branches | This branch is better |
| Costs exceeding benefits | MED | Not worth continuing | Cut losses | Sunk cost, continue |
| New information invalidates | HIGH | Assumption was wrong | Backtrack | Information is wrong |
| User preference changed | MED | External shift | Respect new preference | Preference is stable |

---

# PART G: TREE STRUCTURE

## Q13: What is the current tree state?
[D: tracking where we are in the commitment tree]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| Root (no commitments yet) | LOW | Just starting | Make first commitment | Already committed |
| Single branch deep | LOW | One line of assumptions | Continue or backtrack | Multiple branches |
| Multiple branches explored | MED | Have tried alternatives | Compare branches | Single path only |
| All branches exhausted | HIGH | No options left = problem with root | Question root assumption | More branches exist |
| Lost track of branches | HIGH | Need to rebuild tree | Reconstruct state | State is clear |

---

## Q14: How to navigate the tree?
[D: operations on the commitment tree]

| Entry | CRUX | Why This Rating | ASSUME RIGHT | ASSUME WRONG |
|-------|------|-----------------|--------------|--------------|
| Go deeper (new commitment) | LOW | Explore within branch | Add sub-commitment | Backtrack first |
| Go up (backtrack one) | LOW | Try alternative | Undo last commitment | Stay at level |
| Go to root (backtrack all) | HIGH | Start over = costly | Major rethink | Partial backtrack |
| Switch sibling branch | MED | Try alternative at same level | Undo and try other | Stay in current |
| Prune branch (mark as failed) | MED | Don't re-explore | Mark as failed | Still viable |
| Merge branches | MED | Both branches reach same conclusion | Accept conclusion | Branches diverge |

---

## Coverage Summary

```
QUESTIONS: 14
ENTRIES: 72

CRUX Distribution:
- HIGH: 14 entries (19%)
- MED: 29 entries (40%)
- LOW: 29 entries (40%)

THE CYCLE:
1. GIVEN: What's stated? (Q1-Q2)
2. OPEN/CLOSED: Does it have alternatives? (Q3-Q4)
3. CRUX: Would it change strategy? (Q5-Q6)
4. COMMIT: Pick a branch (Q7-Q8)
5. DERIVE: What follows? (Q9-Q10)
6. CHECK: Is it working? (Q11-Q12)
7. TREE: Navigate the structure (Q13-Q14)

KEY INSIGHT:
The old cycle (GROUND → GUESS → QUESTION → STOP) never COMMITS.
This cycle COMMITS and DERIVES, allowing specific (non-universal) answers.

WHEN TO USE:
- When questioning isn't converging
- When you need a specific answer, not just options
- When you need to tailor strategy based on assumptions
- When building on committed assumptions to reach action
```

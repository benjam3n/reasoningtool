# Universal: Search Cost vs Execution Cost (123)

**Category**: META - When to Plan vs When to Do
**Source**: Decision theory, exploration-exploitation, analysis paralysis
**Structure**: Questions ordered by Value of Information (action divergence)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Is further search cheaper than correcting a bad execution?

[VOI: HIGH - determines whether to keep planning or start doing]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Search much cheaper | HIGH | Plan more | Keep planning | Execute, expensive correction |
| Unknown relative cost | MED | May misallocate | Cost comparison | Either over-plan or under-plan |
| Execution correction cheaper | HIGH | Learn by doing | Execute now | Analysis paralysis |

---

## Q2: Can we learn essential information only by executing?

[VOI: HIGH - some things unknowable until tried]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Must execute to learn | HIGH | Planning can't answer | Execute as experiment | Plan the unknowable |
| Unknown if learnable | MED | May be wasting planning | Learnability check | Either waste planning or miss insight |
| Can learn by planning | LOW | Planning productive | Continue planning | Miss that execution needed |

---

## Q3: Is search hitting diminishing returns?

[VOI: HIGH - diminishing search returns = time to execute]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Search returns exhausted | HIGH | No more value in planning | Execute now | Waste time planning |
| Unknown search returns | MED | May be wasting | Return measurement | Either over or under plan |
| Search still productive | LOW | More to learn | Continue planning | Miss execution window |

---

## Q4: Is there a planning trap (planning about planning)?

[VOI: HIGH - meta-planning loops waste resources]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| In planning trap | HIGH | Recursive waste | Break loop, execute | Continue meta-planning |
| Unknown if trapped | MED | May be wasting | Trap detection | Either trapped or paranoid |
| Not in planning trap | LOW | Planning legitimate | Continue | Actually in trap |

---

## Q5: What's the opportunity cost of delayed execution?

[VOI: HIGH - high opportunity cost = execute sooner]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| High opportunity cost | HIGH | Time is critical | Execute, iterate | Plan while opportunity passes |
| Unknown opportunity cost | MED | May be missing window | Opportunity analysis | Either miss window or rush |
| Low opportunity cost | LOW | Time flexible | Plan thoroughly | Rush when could plan |

---

## Q6: Can execution be paused if we learn something important?

[VOI: MED - affects execution strategy but similar decision]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Cannot pause | MED | Commit fully | Plan more before starting | Start then can't stop |
| Unknown pausability | MED | May be stuck | Pausability analysis | Either over-commit or over-cautious |
| Can pause/iterate | LOW | Agile possible | Start, adjust | Think can pause when can't |

---

## Q7: Is analysis paralysis setting in?

[VOI: MED - paralysis requires intervention]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Paralysis active | MED | Action blocked | Force decision | Continue paralyzed |
| Unknown if paralyzed | MED | May be blocked | Paralysis check | Either paralyzed or premature |
| Not paralyzed | LOW | Deliberation healthy | Continue | Actually paralyzed |

---

## Q8: What's the minimum viable experiment?

[VOI: MED - affects execution scope but similar decision]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| MVE possible | MED | Can test cheaply | Run MVE | Big execution when small works |
| Unknown if MVE possible | MED | May miss efficiency | MVE design | Either miss opportunity or waste effort |
| No MVE, full execution only | LOW | All or nothing | Full planning | Seek impossible MVE |

---

## Q9: Are we searching to avoid discomfort of executing?

[VOI: LOW - motivation check but similar analysis]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Avoidance-driven planning | LOW | Procrastination | Address avoidance | Continue avoiding |
| Unknown motivation | LOW | May be avoiding | Motivation check | Either avoiding or legitimate |
| Legitimate planning | LOW | Productive | Continue | Actually avoiding |

---

## Q10: What's our track record on planning vs execution balance?

[VOI: LOW - calibration check but similar decision]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Historically over-plan | LOW | Bias toward action | Bias toward execution | Over-plan again |
| Unknown track record | LOW | No calibration | Track record review | Repeat unknown bias |
| Historically under-plan | LOW | Bias toward planning | Plan more this time | Under-plan again |
| Well-calibrated | LOW | Trust instincts | Proceed as inclined | Actually miscalibrated |

---

## Summary Statistics

- Total questions: 10
- Total entries: 39
- HIGH VOI: 10 (26%)
- MED VOI: 16 (41%)
- LOW VOI: 13 (33%)

---

## Question Order by Action Divergence

**Ask first (HIGH VOI):**
1. Q1: Search cheaper than correction? - resource allocation
2. Q2: Must execute to learn? - unknowable by planning
3. Q3: Diminishing search returns? - search productivity
4. Q4: Planning trap? - meta-waste
5. Q5: Opportunity cost of delay? - time pressure

**Ask if relevant (MED VOI):**
6. Q6: Can pause execution? - iteration ability
7. Q7: Analysis paralysis? - action blockage
8. Q8: Minimum viable experiment? - cheap learning

**Low priority (LOW VOI):**
9. Q9: Avoiding execution? - motivation
10. Q10: Track record? - calibration

---

## Key Insight

**VOI ≠ theoretical sophistication about planning. VOI = action divergence.**

"What's our track record?" is useful calibration but has LOW VOI - you make a similar decision either way.

"Is further search cheaper than correcting bad execution?" has HIGH VOI - directly determines whether to keep planning or start doing.

---

## The Planning-Execution Spectrum

Too little planning: Expensive corrections, wasted execution, rework
Too much planning: Analysis paralysis, missed opportunities, stale plans

The optimum: Plan until marginal cost of planning exceeds marginal value of better execution.

But remember: You can't know the marginal value of better execution until you execute. This is the fundamental uncertainty that makes this balance an art, not a science.

When in doubt: Bias toward execution. Most people over-plan.

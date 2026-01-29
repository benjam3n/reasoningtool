# Universal: Search Recovery (171)

**Category**: SEARCH - When And How To Restart Or Backtrack?
**Source**: Optimization, debugging, resilience
**Structure**: Questions ordered by Value of Information (action divergence)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Core Insight

**Paths fail. Recovery strategy determines what happens next.**

Options when stuck:
1. Push through (more effort on current path)
2. Backtrack (return to earlier state, try different branch)
3. Restart (abandon current search, begin fresh)
4. Reframe (change the problem definition)

Wrong recovery = compounding the original failure.

---

## Q1: Is the current path failing or just hard?

[VOI: HIGH - diagnosis before recovery]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Failing (won't succeed with more effort) | HIGH | Switch paths | Don't waste resources | Abandon good path |
| Hard (will succeed with more effort) | HIGH | Push through | Achieve goal | Waste on impossible |
| Can't tell | HIGH | Set test criteria | Decide based on evidence | Guess wrong |

---

## Q2: What signals indicate path failure?

[VOI: HIGH - failure detection]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No progress despite effort | HIGH | Path may be blocked | Consider switching | Push futilely |
| Progress but wrong direction | HIGH | Backtrack | Find right direction | Keep going wrong way |
| Fundamental obstacle discovered | HIGH | Path impossible | Restart elsewhere | Fight impossible |
| Just slow progress | MED | May be fine | Continue with patience | Switch prematurely |

---

## Q3: How far back should you backtrack?

[VOI: HIGH - backtrack depth]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| To last branch point | MED | Try different branch from same stem | Preserve earlier work | Repeat same mistake |
| To earlier decision | HIGH | Reopen previously closed choice | May find new path | Lose more progress |
| To beginning | HIGH | Full restart | Fresh perspective | Lose all progress |
| Don't backtrack, reframe | HIGH | Change problem | May dissolve issue | Lose valid path |

---

## Q4: What caused the failure?

[VOI: HIGH - root cause determines response]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Wrong branch chosen | MED | Different branch, same approach | Try alternative | Same mistake |
| Wrong approach | HIGH | Different approach entirely | New strategy | Same approach, different branch |
| Wrong problem definition | HIGH | Reframe problem | Solve right problem | Keep solving wrong problem |
| External blocker | MED | Remove blocker or route around | Clear path | Keep hitting blocker |

---

## Q5: What's the sunk cost?

[VOI: MED - sunk cost awareness]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| High sunk cost | MED | Temptation to continue - resist if path dead | Objective assessment | Throw good after bad |
| Low sunk cost | LOW | Easy to switch | Switch freely | N/A |

---

## Q6: Will you repeat the same failure?

[VOI: MED - learning from failure]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, likely to repeat | MED | Understand failure before retrying | Learn first | Repeat error |
| No, learned from it | LOW | Proceed with restart | Apply learning | Haven't learned |

---

## Q7: Is there a recovery checkpoint?

[VOI: MED - checkpoint availability]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, can restore to checkpoint | MED | Backtrack to checkpoint | Efficient recovery | N/A |
| No checkpoint | MED | Must rebuild from scratch | More costly restart | N/A |

---

## Q8: What's the restart cost vs continue cost?

[VOI: MED - recovery economics]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Restart cheaper | MED | Restart | Fresh start | Waste continuing |
| Continue cheaper | MED | Push through | Save restart cost | Miss better path |
| Similar cost | LOW | Other factors decide | Assess path quality | N/A |

---

## Summary Statistics

- Total questions: 8
- HIGH VOI: 6
- MED VOI: 8
- LOW VOI: 2

---

## Recovery Decision Tree

```
Is current path making progress?
├── Yes → Continue (don't fix what isn't broken)
└── No → Why not?
    ├── Wrong branch → Backtrack to branch point
    ├── Wrong approach → Try different approach
    ├── Wrong problem → Reframe
    └── Blocked → Remove blocker or route around
```

---

## Recovery Strategies

| Strategy | When to Use | Risk |
|----------|-------------|------|
| **Push through** | Path is hard but viable | Wasted effort if impossible |
| **Local backtrack** | Recent choice was wrong | May repeat at higher level |
| **Deep backtrack** | Earlier choice was wrong | Loses significant progress |
| **Full restart** | Entire approach was wrong | Loses all progress |
| **Reframe** | Problem was wrong | May lose valid insights |
| **Parallel path** | Uncertain which will work | Resource split |

---

## Signals to Restart vs Push Through

| Signal | Suggests | Action |
|--------|----------|--------|
| Same obstacle repeatedly | Wrong approach | Restart with different approach |
| Novel obstacles | Path is viable but hard | Push through |
| Getting further from goal | Wrong direction | Backtrack |
| Revealing more obstacles | Path may be bad | Assess depth of obstacles |
| Progress slowing | May be approaching limit | Check if ceiling or plateau |

---

## Common Recovery Errors

| Error | Pattern | Fix |
|-------|---------|-----|
| **Never restart** | Sunk cost attachment | Assess forward value only |
| **Restart too often** | Impatience with hard work | Set minimum effort before switching |
| **Shallow backtrack** | Only try nearby alternatives | Consider deeper backtrack |
| **Same failure repeated** | Restart without learning | Analyze failure first |
| **Reframe avoidance** | Keep solving wrong problem | Question problem definition |

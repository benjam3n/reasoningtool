# Universal: Set and Logic (65)

**Category**: MATHEMATICAL - Set Theory and Logic
**Source**: [O: universal_goal_analysis.yaml lines 2212-2241 set_and_logic category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Are goals mutually exclusive (intersection empty)?
[VOI: HIGH - mutually exclusive means must choose one vs can pursue both]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, mutually exclusive | HIGH | Must choose one, cannot have both | Choose one | Not exclusive |
| Unknown exclusivity | MED | Determine if both possible vs assume can | Exclusivity check | Exclusivity known |
| No, can coexist | LOW | Pursue both vs must choose | Pursue both | Actually exclusive |

---

## Q2: Does failing this goal necessarily imply other things?
[VOI: HIGH - failure cascades make stakes much higher]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, failure cascades | HIGH | Prevent failure at high priority vs lower stakes | Prevent failure | No cascade |
| Unknown failure implications | MED | Analyze cascade risk vs assume isolated | Failure analysis | Implications known |
| No cascade | LOW | Isolated failure, lower stakes vs cascade | Lower stakes | Cascade exists |

---

## Q3: Are the logical implications acceptable?
[VOI: HIGH - unacceptable implications require goal/approach change]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, unacceptable | HIGH | Change goal or approach vs proceed | Change goal or approach | Acceptable |
| Partially acceptable | MED | Weigh tradeoffs carefully vs clear choice | Weigh carefully | Different level |
| Unknown acceptability | MED | Evaluate implications vs assume ok | Acceptability check | Acceptability known |
| Yes, acceptable | LOW | Proceed as planned vs reconsider | Accept implications | Not acceptable |

---

## Q4: What set/category does this goal belong to?
[VOI: MED - category determines which patterns apply]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Multiple categories | MED | Combine patterns from each vs single approach | Combine patterns | Single category |
| Novel/uncategorized | MED | First principles vs apply patterns | First principles | Category exists |
| Unknown category | MED | Category discovery vs proceed | Category analysis | Category known |
| Clearly categorized | LOW | Apply known patterns vs discover | Use known patterns | Wrong category |

---

## Q5: What properties do all members of that set share?
[VOI: MED - shared properties enable leverage]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Properties unclear | MED | Property discovery vs apply known | Property discovery | Properties clear |
| No shared properties | MED | Category not useful, different grouping | Different grouping | Properties exist |
| Properties identified | LOW | Apply properties vs wrong properties | Apply properties | Wrong properties |

---

## Q6: Is this goal a subset of a larger goal?
[VOI: MED - subset means must align with larger]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, subset of larger | MED | Align with larger goal vs independent | Align with larger | Not a subset |
| Unknown if subset | LOW | Check for superset relationship | Superset check | Relationship known |
| No, standalone goal | LOW | Independent pursuit vs must align | Own merit | Actually subset |

---

## Q7: Are there smaller goals that are subsets of this goal?
[VOI: MED - subgoals enable divide and conquer]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, atomic goal | MED | Indivisible, whole approach needed | Whole approach | Subgoals exist |
| Unknown subgoals | MED | Analyze for decomposition vs assume atomic | Subgoal analysis | Subgoals known |
| Yes, subgoals exist | LOW | Divide and conquer vs whole approach | Divide and conquer | No subgoals |

---

## Q8: Does this goal intersect with other goals?
[VOI: MED - intersection enables synergy or conflict]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, significant overlap | MED | Coordinate for synergy vs independent | Coordinate | No overlap |
| Unknown intersection | MED | Check for overlap vs assume independent | Intersection check | Intersection known |
| Yes, minor overlap | LOW | Light coordination vs independent | Light coordination | Different level |
| No overlap | LOW | Independent pursuit vs coordinate | Separate pursuit | Overlap exists |

---

## Q9: Does achieving this goal necessarily imply other things?
[VOI: MED - implications may have side effects to consider]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, has implications | MED | Consider side effects vs narrow focus | Consider implications | No implications |
| Unknown implications | MED | Analyze implications vs assume none | Implication analysis | Implications known |
| No implications | LOW | Narrow focus ok vs consider effects | Narrow focus | Implications exist |

---

## Q10: Is it easier to define what the goal is NOT than what it IS?
[VOI: MED - complement definition may be clearer]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, complement clearer | MED | Define by exclusion vs positive | Use exclusion | Direct definition clearer |
| No, direct definition | LOW | State positively vs by exclusion | State directly | Complement clearer |
| Both equally clear | LOW | Either approach works | Choose convenient | One clearer |

---

## Coverage Summary

```
QUESTIONS: 10
ENTRIES: 38

VOI Distribution:
- HIGH: 3 entries (8%)
- MED: 20 entries (53%)
- LOW: 15 entries (39%)

Note: Lower HIGH% because set analysis is usually clarification
```

---

## Question Order by Action Divergence

**HIGH VOI (ask first - routes to different action paths):**
1. Q1 (Mutually exclusive?) - must choose vs both
2. Q2 (Failure cascades?) - high stakes vs isolated
3. Q3 (Implications acceptable?) - proceed vs change

**MED VOI (ask second - same direction, different approach):**
4. Q4 (Category?) - which patterns apply
5. Q5 (Shared properties?) - leverage available
6. Q6 (Subset of larger?) - alignment needed
7. Q7 (Has subgoals?) - decomposition possible
8. Q8 (Intersects?) - coordination needed
9. Q9 (Achievement implies?) - side effects
10. Q10 (Complement clearer?) - definition approach

---

## Key Insight

**VOI ≠ logical complexity**

**VOI = action divergence**

Q1 "Are goals mutually exclusive?" is HIGH VOI because:
- YES → must choose one (completely different goal selection)
- NO → can pursue both (different scope of work)

Q10 "Complement clearer?" is MED VOI because:
- YES → define by what it's not
- NO → define positively (same goal, different description)

Mutual exclusivity determines what you can even pursue. Complement definition is just how you describe what you're pursuing.

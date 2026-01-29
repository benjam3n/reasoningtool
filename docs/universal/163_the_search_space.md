# Universal: The Search Space (163)

**Category**: SEARCH - What Could Be An Answer?
**Source**: Consolidated from frame/abstraction concepts (Dilts "Sleight of Mouth")
**Structure**: Questions ordered by Value of Information (action divergence)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Core Insight

**Search requires knowing: (1) what set contains possible answers, (2) at what granularity to distinguish them, (3) what variables can change.**

Search fails when:
- The answer exists but outside the space being searched
- The answer exists but at a different granularity than being checked
- A variable is treated as fixed when it could change

---

## Q1: What set contains possible answers?

[VOI: HIGH - wrong set = answer invisible]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Set not identified | HIGH | Searching blindly | Identify the set first | Search indefinitely |
| Set identified | LOW | Can evaluate coverage | Check if answer is in this set | Actually different set |

---

## Q2: Does the answer exist in this set?

[VOI: HIGH - determines continue vs change sets]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes | LOW | Continue searching this set | Keep searching | Search wrong set |
| No | HIGH | Must change sets | Find different set | Search forever in wrong place |

---

## Q3: At what granularity are candidates distinguished?

[VOI: HIGH - wrong granularity = answer invisible]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Too coarse | HIGH | Answer lumped with non-answers | Increase granularity | Miss answer within lump |
| Too fine | HIGH | Overwhelmed by irrelevant distinctions | Decrease granularity | Waste effort on noise |
| Appropriate | LOW | Efficient search | Continue | Actually wrong granularity |

---

## Q4: What variables are being held fixed?

[VOI: HIGH - false constraints eliminate valid answers]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Variables identified as fixed | MED | Known constraints | Work within constraints | Miss changeable variables |
| Fixed variables not identified | HIGH | Hidden constraints operating | Identify what's held fixed | Constrained without knowing |

---

## Q5: Which fixed variables could actually change?

[VOI: HIGH - releasing false constraint expands space]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Some could change | HIGH | Space can expand | Release constraint, expand space | Stay unnecessarily limited |
| None could change | MED | True constraints | Accept constraints | Miss release option |

---

## Q6: What adjacent sets exist?

[VOI: MED - adjacent = accessible alternatives]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Adjacent sets known | LOW | Alternatives available | Can move if needed | Actually isolated |
| Adjacent sets unknown | MED | May be stuck unnecessarily | Map adjacent sets | Miss accessible alternatives |

---

## Q7: What does this set exclude?

[VOI: MED - exclusions = blind spots]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Important things excluded | MED | Set too narrow | Expand or change set | Miss excluded options |
| Nothing important excluded | LOW | Set appropriate | Continue | Actually excluding important |

---

## Q8: Who defined this set?

[VOI: MED - origin affects changeability]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Self-defined | MED | Full control to change | Change freely | Think constrained when not |
| Externally defined | MED | Less control | Negotiate or accept | Miss change option |

---

## Q9: Can the granularity be changed?

[VOI: LOW - meta-flexibility]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes | LOW | Adjustable | Adjust as needed | Stay at wrong level |
| No | LOW | Fixed | Work within | Miss adjustment option |

---

## Q10: Can multiple sets be searched simultaneously?

[VOI: LOW - search strategy]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes | LOW | Parallel search | Multi-set exploration | Unnecessary serialization |
| No | LOW | Sequential search | Switch between sets | Miss parallel option |

---

## Summary Statistics

- Total questions: 10
- Total entries: 24
- HIGH VOI: 7 (29%)
- MED VOI: 8 (33%)
- LOW VOI: 9 (38%)

---

## Question Order by Action Divergence

**Ask first (HIGH VOI):**
1. Q1: What set contains possible answers?
2. Q2: Does the answer exist in this set?
3. Q3: At what granularity are candidates distinguished?
4. Q4: What variables are being held fixed?
5. Q5: Which fixed variables could actually change?

**Ask if relevant (MED VOI):**
6. Q6: What adjacent sets exist?
7. Q7: What does this set exclude?
8. Q8: Who defined this set?

**Low priority (LOW VOI):**
9. Q9: Can the granularity be changed?
10. Q10: Can multiple sets be searched simultaneously?

---

## Space Operations

| Operation | Effect | When To Use |
|-----------|--------|-------------|
| **Expand set** | More candidates | Answer might be outside current set |
| **Contract set** | Fewer candidates | Too many irrelevant candidates |
| **Increase granularity** | Finer distinctions | Answer lumped with non-answers |
| **Decrease granularity** | Coarser distinctions | Overwhelmed by noise |
| **Release variable** | More dimensions | False constraint identified |
| **Fix variable** | Fewer dimensions | Reduce complexity |
| **Shift to adjacent set** | Different candidates | Current set exhausted |

---

## The Three Components

```
SEARCH SPACE = {Candidates} × {Granularity} × {Variables}

1. CANDIDATES: What could be an answer?
   - The set of things being considered
   - Defined by inclusion/exclusion rules

2. GRANULARITY: How finely to distinguish?
   - Too coarse: answer invisible within lump
   - Too fine: noise obscures answer

3. VARIABLES: What can change?
   - Each variable adds a dimension
   - Fixed variables constrain the space
   - False constraints eliminate valid answers
```

---

## Common Space Errors

| Error | What Happens | Fix |
|-------|--------------|-----|
| Wrong set | Answer exists but not here | Change sets |
| Wrong granularity | Answer invisible at this level | Change granularity |
| False constraint | Valid answer eliminated | Release variable |
| Unknown boundary | Don't know what's excluded | Map the boundary |
| Conflated content/space | Debating within wrong space | Separate space from content |

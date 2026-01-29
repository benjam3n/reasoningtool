# Universal: Structure and Mapping (63)

**Category**: MATHEMATICAL - Category Theory Concepts
**Source**: [O: universal_goal_analysis.yaml lines 2134-2168 structure_and_mapping category]
**Structure**: One question per entry, VOI-marked with realistic distribution

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Are there things being treated as different that are actually equivalent?
[VOI: HIGH - false distinctions mean wasted effort on redundancy vs clean separation]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, false distinctions | HIGH | Consolidate redundant work vs handle separately | Consolidate | Truly different |
| Unknown equivalences | MED | Check for equivalences vs assume distinct | Equivalence check | Equivalences known |
| No, all distinctions real | LOW | Handle separately vs consolidate | Handle separately | False distinctions exist |

---

## Q2: Are there things being treated as equivalent that are actually different?
[VOI: HIGH - false equivalences mean wrong treatment vs appropriate handling]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, false equivalences | HIGH | Distinguish and handle differently vs group | Distinguish | Truly equivalent |
| Unknown if truly equivalent | MED | Test equivalence vs assume same | Equivalence testing | Equivalences known |
| No, equivalences valid | LOW | Use groups vs distinguish | Use groups | False equivalences exist |

---

## Q3: What transformation maps one thing to another?
[VOI: MED - affects conversion cost but not fundamental approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Complex transform | MED | Factor in conversion overhead vs simple | Factor in cost | Simpler |
| Irreversible transform | MED | Accept one-way nature vs expect reversible | Accept loss | Reversible |
| Unknown transform | MED | Discover transform vs assume simple | Transform discovery | Transform known |
| Simple, reversible transform | LOW | Use transform freely vs complex | Use transform | Complex/irreversible |

---

## Q4: Can operations be composed (output of one becomes input of next)?
[VOI: MED - composable enables pipelines vs individual handling]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, standalone only | MED | Handle each separately vs build pipelines | Individual handling | Actually composable |
| Partially composable | MED | Selective chaining vs uniform approach | Selective composition | Different level |
| Yes, composable | LOW | Build pipelines vs standalone | Build pipelines | Not composable |
| Unknown composability | LOW | Test composability vs assume either | Composability check | Composability known |

---

## Q5: Does the order of composition matter?
[VOI: MED - order-dependent requires careful sequencing vs flexible]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, order matters | MED | Careful ordering required vs any order | Careful ordering | Order doesn't matter |
| Depends on operation | MED | Check each operation vs assume uniform | Check each | Uniform behavior |
| Unknown if order matters | MED | Test order effects vs assume commutative | Order testing | Order known |
| No, commutative | LOW | Flexible ordering vs must sequence | Any order | Order matters |

---

## Q6: Is there an inverse operation for each operation?
[VOI: MED - invertible allows undo vs must be cautious]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No inverses | MED | Extra caution, no undo vs reversible | Extra caution | Inverses exist |
| Some invertible | MED | Know which are reversible vs assume all | Know which | Different level |
| Unknown invertibility | MED | Test before committing vs assume | Inverse check | Invertibility known |
| Yes, all invertible | LOW | Can undo, less caution vs irreversible | Reversible actions | Not all invertible |

---

## Q7: Is there a mapping from one system to another that preserves relationships?
[VOI: MED - structure-preserving map enables solution transfer vs solve directly]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Yes, structure-preserving map | MED | Transfer solutions between systems vs solve fresh | Use mapping | No such map |
| Partial mapping | MED | Selective transfer vs full or none | Selective use | Different level |
| Unknown if mapping exists | MED | Search for useful mapping vs solve directly | Mapping search | Mapping known |
| No useful mapping | LOW | Solve directly vs try to map | Direct approach | Mapping exists |

---

## Q8: Which system is easier to work in?
[VOI: MED - choice of working system affects efficiency]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Mapped system easier | MED | Transform, solve, transform back vs direct | Map, solve, map back | Original easier |
| Original easier | LOW | Work directly vs transform | Direct work | Mapped easier |
| Similar difficulty | LOW | Choose based on preference vs efficiency | Choose based on comfort | One easier |
| Unknown which easier | LOW | Test both vs guess | Comparative check | Ease known |

---

## Q9: Is there something uniquely determined by a property it satisfies?
[VOI: MED - unique solution needs no choice vs must select]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| No, multiple solutions | MED | Define selection criteria vs accept unique | Choose criteria | Unique exists |
| Unknown uniqueness | MED | Check for uniqueness vs assume | Uniqueness check | Uniqueness known |
| Yes, unique solution | LOW | Use unique solution vs select | Use unique | Not unique |

---

## Coverage Summary

```
QUESTIONS: 9
ENTRIES: 37

VOI Distribution:
- HIGH: 2 entries (5%)
- MED: 22 entries (60%)
- LOW: 13 entries (35%)

Note: Lower HIGH% because structure analysis is usually refinement not direction
```

---

## Question Order by Action Divergence

**HIGH VOI (ask first - routes to different action paths):**
1. Q1 (False distinctions?) - wasted effort on redundancy
2. Q2 (False equivalences?) - wrong treatment

**MED VOI (ask second - same direction, different approach):**
3. Q3 (Transform complexity?) - conversion overhead
4. Q4 (Composable?) - pipelines vs individual
5. Q5 (Order matters?) - sequencing care
6. Q6 (Invertible?) - undo capability
7. Q7 (Structure-preserving map?) - solution transfer
8. Q8 (Easier system?) - where to work
9. Q9 (Unique solution?) - selection needed

---

## Key Insight

**VOI ≠ mathematical sophistication**

**VOI = action divergence**

Q1 "False distinctions?" is HIGH VOI because:
- YES → consolidate (completely different work focus)
- NO → handle each separately (different work scope)

Q7 "Structure-preserving map?" is MED VOI because:
- YES → use mapping to transfer solutions
- NO → solve directly (same goal, different path)

False distinctions change what work you do. Mappings change how you do the work.

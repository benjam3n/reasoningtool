# Universal: Decomposition Quality (131)

**Category**: META - Are We Chunking the Problem Right?
**Source**: Problem-solving, systems thinking, algorithm design
**Structure**: Questions ordered by Value of Information (action divergence)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Q1: Is this decomposition creating solvable subproblems?

[VOI: HIGH - wrong decomposition = unsolvable pieces]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Subproblems unsolvable | HIGH | Decomposition fails | Re-decompose | Grind on impossible pieces |
| Unknown if solvable | MED | May be stuck | Solvability check | Either stuck or fine |
| Subproblems solvable | LOW | Good decomposition | Solve pieces | Actually unsolvable |

---

## Q2: Does solving the subproblems solve the original problem?

[VOI: HIGH - pieces may not reassemble into solution]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Pieces don't reassemble | HIGH | Integration fails | Different decomposition | Solve pieces, fail whole |
| Unknown if reassembles | MED | May fail integration | Integration check | Either fail or succeed |
| Pieces reassemble | LOW | Good decomposition | Continue | Actually don't reassemble |

---

## Q3: Are we cutting along natural joints?

[VOI: HIGH - unnatural cuts create artificial dependencies]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Cutting against grain | HIGH | Artificial complexity | Find natural joints | Create unnecessary coupling |
| Unknown joint structure | MED | May be cutting wrong | Structure analysis | Either wrong cuts or fine |
| Cutting along joints | LOW | Natural decomposition | Continue | Actually against grain |

---

## Q4: Is the decomposition hiding the core difficulty?

[VOI: HIGH - core difficulty must be faced, not distributed]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Core difficulty hidden | HIGH | Will hit wall later | Surface the core | Defer inevitable failure |
| Unknown if hidden | MED | May hit wall | Difficulty mapping | Either hit wall or fine |
| Core difficulty visible | LOW | Can address directly | Address core | Actually hidden |

---

## Q5: Are there cross-cutting concerns being ignored?

[VOI: HIGH - cross-cutting concerns undermine decomposition]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Cross-cutting ignored | HIGH | Pieces interfere | Address cross-cutting | Pieces conflict later |
| Unknown cross-cutting | MED | May have conflicts | Cross-cut analysis | Either conflict or fine |
| No cross-cutting | LOW | Clean separation | Proceed | Actually cross-cutting |

---

## Q6: Is the granularity right?

[VOI: MED - affects tractability but similar process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Too coarse | MED | Pieces still too hard | Decompose further | Pieces intractable |
| Too fine | MED | Integration overhead | Aggregate some | Drown in pieces |
| Unknown granularity | MED | May be wrong level | Granularity check | Either too much or too little |
| Granularity right | LOW | Appropriate level | Continue | Actually wrong level |

---

## Q7: Are we decomposing by the right dimension?

[VOI: MED - wrong dimension = awkward pieces]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Wrong dimension | MED | Awkward pieces | Try different dimension | Awkward fits |
| Unknown best dimension | MED | May be suboptimal | Dimension analysis | Either awkward or optimal |
| Right dimension | LOW | Clean pieces | Continue | Actually wrong |

---

## Q8: Is there a standard decomposition for this problem type?

[VOI: MED - known decompositions are tested]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Standard exists, not using | MED | Reinventing | Use standard | Miss known good approach |
| Unknown if standard exists | MED | May be reinventing | Standard search | Either reinvent or find |
| Using standard | LOW | Tested approach | Continue | Standard doesn't fit |
| No standard exists | LOW | Novel territory | Create decomposition | Miss existing standard |

---

## Q9: Are boundary conditions handled?

[VOI: LOW - affects correctness but similar process]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Boundaries unhandled | LOW | Edge cases fail | Handle boundaries | Fail at edges |
| Unknown boundary handling | LOW | May fail at edges | Boundary check | Either fail or fine |
| Boundaries handled | LOW | Complete | Continue | Actually unhandled |

---

## Q10: Can pieces be solved in parallel?

[VOI: LOW - affects efficiency but similar approach]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Can parallelize | LOW | Efficiency gain | Parallelize | Miss efficiency |
| Unknown if parallel | LOW | May miss efficiency | Dependency analysis | Either miss or find |
| Must be sequential | LOW | Ordered solving | Sequence correctly | Think sequential when parallel |

---

## Summary Statistics

- Total questions: 10
- Total entries: 40
- HIGH VOI: 10 (25%)
- MED VOI: 16 (40%)
- LOW VOI: 14 (35%)

---

## Question Order by Action Divergence

**Ask first (HIGH VOI):**
1. Q1: Subproblems solvable? - pieces tractable
2. Q2: Pieces reassemble? - integration works
3. Q3: Natural joints? - grain of problem
4. Q4: Core difficulty visible? - not hiding hard part
5. Q5: Cross-cutting concerns? - pieces don't interfere

**Ask if relevant (MED VOI):**
6. Q6: Right granularity? - level of detail
7. Q7: Right dimension? - cut direction
8. Q8: Standard decomposition? - known approaches

**Low priority (LOW VOI):**
9. Q9: Boundaries handled? - edge cases
10. Q10: Can parallelize? - efficiency

---

## Key Insight

**VOI ≠ decomposition elegance. VOI = action divergence.**

"Can pieces be solved in parallel?" affects efficiency but has LOW VOI - you do similar work.

"Does solving the subproblems solve the original?" has HIGH VOI - if not, you've wasted all work on pieces.

---

## The Decomposition Trap

Many "hard" problems are only hard because of bad decomposition.

**Signs of bad decomposition:**
- Subproblems seem as hard as original
- Solutions don't integrate cleanly
- Same issue appears in multiple pieces
- Pieces have circular dependencies
- Core difficulty is somehow everywhere and nowhere

**Good decomposition:**
- Each piece is obviously easier than the whole
- Solutions compose cleanly
- Concerns are separated
- Dependencies flow one direction
- Hardest part is isolated and visible

The meta-move: When stuck, question the decomposition before grinding harder on pieces.

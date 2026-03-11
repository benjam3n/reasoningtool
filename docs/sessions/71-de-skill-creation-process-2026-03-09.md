# /de Design the process for how a new skill goes from idea to tested and deployed
**Date:** 2026-03-09
**Skill:** /de (Dependency Extraction)

---

## Interpretation Selected

**Interpretation 1 — Extract task dependencies for sequencing**: The input is a list of pipeline stages (ideation → design → writing → testing → integration → deployment) and we need to determine what must happen before what, find the critical path, and identify parallel opportunities.

---

## Step 1: List All Items

```
ITEMS TO ANALYZE:

 1. Identify skill gap (recognize a thinking task the toolkit doesn't cover)
 2. Check for overlap with existing skills (search 592 skills for duplicates/near-duplicates)
 3. Define the skill's purpose and scope (what input it takes, what output it produces)
 4. Choose the skill's structural pattern (ARAW, UAUA, linear, matrix, etc.)
 5. Determine the skill's tier and category placement (Tier 1–4, which category router)
 6. Write the SKILL.md file (the actual procedure)
 7. Write interpretations block (the 3 interpretation variants)
 8. Write the example/walkthrough section
 9. Create the skill directory (skills/[name]/SKILL.md)
10. Test with a real input (run the skill against a genuine problem)
11. Test edge cases (ambiguous input, minimal input, adversarial input)
12. Verify skill chaining (test any → INVOKE references work)
13. Add to category router(s) (update the routing skill that should dispatch to it)
14. Add to CLAUDE.md tables (if Tier 1 or Tier 2)
15. Add to website skill index (website/src/pages/index.astro or data files)
16. Update skill count references (CLAUDE.md, website, etc.)
17. Commit and deploy

TOTAL: 17 items
```

---

## Step 2: Dependency Analysis Per Item

```
DEPENDENCY ANALYSIS: 1. Identify skill gap
  INPUTS: User feedback, personal observation, /skgap output, gap in coverage noticed during use
  OUTPUTS: A named thinking task that is unserved
  PREREQUISITES: None (START)
  ENABLES: 2, 3

DEPENDENCY ANALYSIS: 2. Check for overlap with existing skills
  INPUTS: Skill gap name from (1), access to skills/ directory
  OUTPUTS: Confirmation of no duplicate, or list of near-overlaps to differentiate from
  PREREQUISITES: 1 -> (need to know what you're checking)
  ENABLES: 3, 5

DEPENDENCY ANALYSIS: 3. Define purpose and scope
  INPUTS: Gap from (1), overlap info from (2)
  OUTPUTS: Clear statement of input type, output type, and boundaries
  PREREQUISITES: 1 ->, 2 ->
  ENABLES: 4, 5, 6, 7

DEPENDENCY ANALYSIS: 4. Choose structural pattern
  INPUTS: Purpose/scope from (3), knowledge of existing patterns
  OUTPUTS: Selected pattern (ARAW, UAUA, linear, matrix, router, etc.)
  PREREQUISITES: 3 ->
  ENABLES: 6, 7, 8

DEPENDENCY ANALYSIS: 5. Determine tier and category placement
  INPUTS: Purpose from (3), overlap analysis from (2), existing tier assignments
  OUTPUTS: Tier level, category router(s) it belongs under
  PREREQUISITES: 3 ->, 2 ~>
  ENABLES: 13, 14

DEPENDENCY ANALYSIS: 6. Write the SKILL.md file
  INPUTS: Purpose from (3), pattern from (4)
  OUTPUTS: Complete SKILL.md with procedure steps
  PREREQUISITES: 3 ->, 4 ->
  ENABLES: 7, 8, 9, 10

DEPENDENCY ANALYSIS: 7. Write interpretations block
  INPUTS: Purpose from (3), pattern from (4), draft skill from (6)
  OUTPUTS: 3 interpretation variants at top of SKILL.md
  PREREQUISITES: 6 -> (needs the procedure to write interpretations for)
  ENABLES: 10, 11

DEPENDENCY ANALYSIS: 8. Write example/walkthrough section
  INPUTS: Complete skill from (6), pattern from (4)
  OUTPUTS: Worked example appended to SKILL.md
  PREREQUISITES: 6 ->
  ENABLES: 10

DEPENDENCY ANALYSIS: 9. Create skill directory
  INPUTS: Chosen short name, completed SKILL.md from (6)+(7)+(8)
  OUTPUTS: skills/[name]/SKILL.md on disk
  PREREQUISITES: 6 ->, 7 ->, 8 ->
  ENABLES: 10, 11, 12

DEPENDENCY ANALYSIS: 10. Test with real input
  INPUTS: Deployed skill file from (9), a genuine problem to test against
  OUTPUTS: Test result — does the skill produce useful output?
  PREREQUISITES: 9 ->
  ENABLES: 12, 13 (proceed only if pass)

DEPENDENCY ANALYSIS: 11. Test edge cases
  INPUTS: Deployed skill from (9)
  OUTPUTS: Edge case results — does it handle ambiguity, minimal input, etc.?
  PREREQUISITES: 9 ->
  ENABLES: 13 (proceed only if pass)

DEPENDENCY ANALYSIS: 12. Verify skill chaining
  INPUTS: Deployed skill from (9), test results from (10)
  OUTPUTS: Confirmation that → INVOKE references resolve correctly
  PREREQUISITES: 9 ->, 10 ~>
  ENABLES: 13

DEPENDENCY ANALYSIS: 13. Add to category router(s)
  INPUTS: Tier/category from (5), passing test results from (10)+(11)
  OUTPUTS: Updated router skill SKILL.md files
  PREREQUISITES: 5 ->, 10 ->, 11 ->, 12 ~>
  ENABLES: 15, 17

DEPENDENCY ANALYSIS: 14. Add to CLAUDE.md tables
  INPUTS: Tier from (5), skill name, short description
  OUTPUTS: Updated CLAUDE.md
  PREREQUISITES: 5 ->, 9 ->
  ENABLES: 17

DEPENDENCY ANALYSIS: 15. Add to website skill index
  INPUTS: Skill metadata, category, tier
  OUTPUTS: Updated website data
  PREREQUISITES: 13 ~>, 9 ->
  ENABLES: 17

DEPENDENCY ANALYSIS: 16. Update skill count references
  INPUTS: Knowledge of all files referencing skill count
  OUTPUTS: Updated count in CLAUDE.md, website, etc.
  PREREQUISITES: 9 ->
  ENABLES: 17

DEPENDENCY ANALYSIS: 17. Commit and deploy
  INPUTS: All updated files
  OUTPUTS: Live deployment
  PREREQUISITES: 13 ->, 14 ->, 15 ~>, 16 ->
  ENABLES: (END)
```

---

## Step 3: Dependency Matrix

```
DEPENDENCY MATRIX:

          |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  |
----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
 1. Gap   |  -  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
 2. Ovrlp |  -> |  -  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
 3. Scope |  -> |  -> |  -  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
 4. Pattn |     |     |  -> |  -  |     |     |     |     |     |     |     |     |     |     |     |     |     |
 5. Tier  |     |  ~> |  -> |     |  -  |     |     |     |     |     |     |     |     |     |     |     |     |
 6. Write |     |     |  -> |  -> |     |  -  |     |     |     |     |     |     |     |     |     |     |     |
 7. Intrp |     |     |     |     |     |  -> |  -  |     |     |     |     |     |     |     |     |     |     |
 8. Exmpl |     |     |     |     |     |  -> |     |  -  |     |     |     |     |     |     |     |     |     |
 9. MkDir |     |     |     |     |     |  -> |  -> |  -> |  -  |     |     |     |     |     |     |     |     |
10. Test  |     |     |     |     |     |     |     |     |  -> |  -  |     |     |     |     |     |     |     |
11. Edge  |     |     |     |     |     |     |     |     |  -> |     |  -  |     |     |     |     |     |     |
12. Chain |     |     |     |     |     |     |     |     |  -> |  ~> |     |  -  |     |     |     |     |     |
13. Route |     |     |     |     |  -> |     |     |     |     |  -> |  -> |  ~> |  -  |     |     |     |     |
14. CLMD  |     |     |     |     |  -> |     |     |     |  -> |     |     |     |     |  -  |     |     |     |
15. Web   |     |     |     |     |     |     |     |     |  -> |     |     |     |  ~> |     |  -  |     |     |
16. Count |     |     |     |     |     |     |     |     |  -> |     |     |     |     |     |     |  -  |     |
17. Deply |     |     |     |     |     |     |     |     |     |     |     |     |  -> |  -> |  ~> |  -> |  -  |

Legend: -> = hard dependency, ~> = soft dependency, blank = independent
Read as: Row depends on Column
```

---

## Step 4: Dependency Chains

```
DEPENDENCY CHAINS:

Chain 1 (Critical Path — Design through Test):
  1. Identify gap -> 2. Check overlap -> 3. Define scope -> 4. Choose pattern -> 6. Write SKILL.md -> 7. Write interpretations -> 9. Create directory -> 10. Test real input -> 13. Add to routers -> 17. Commit/deploy
  Length: 10 steps

Chain 2 (Example branch):
  ...3 -> 4 -> 6 -> 8. Write example -> 9 -> ...
  Length: merges into Chain 1 at step 9

Chain 3 (Tier/placement branch):
  ...3 -> 5. Determine tier -> 13. Add to routers -> 17
  Length: shorter, merges at step 13

Chain 4 (Edge case branch):
  9 -> 11. Test edge cases -> 13 -> 17
  Length: parallel to Chain 1 from step 9 onward

Chain 5 (Integration branch):
  9 -> 14. CLAUDE.md -> 17
  9 -> 15. Website -> 17
  9 -> 16. Count -> 17
  Length: short, all merge at 17

CRITICAL PATH: Chain 1
  1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 9 -> 10 -> 13 -> 17
  Length: 10 steps (determines minimum time to ship a skill)
```

---

## Step 5: Parallel Opportunities

```
PARALLEL OPPORTUNITIES:

Can run in parallel:
  - 4. Choose pattern    || 5. Determine tier       (both depend only on 3)
  - 7. Write interps     || 8. Write example        (both depend only on 6)
  - 10. Test real input  || 11. Test edge cases     || 12. Verify chaining  (all depend only on 9)
  - 14. Update CLAUDE.md || 15. Update website      || 16. Update count     (all depend only on 9 + 5)

Parallel groups:
  Group A: {4, 5}          — after step 3 (Define scope)
  Group B: {7, 8}          — after step 6 (Write SKILL.md)
  Group C: {10, 11, 12}    — after step 9 (Create directory)
  Group D: {14, 15, 16}    — after step 9 (can start while testing runs)
```

---

## Step 6: External Dependencies

```
EXTERNAL DEPENDENCIES:

| Item | External Dependency | Type | Risk |
|------|---------------------|------|------|
| 1. Identify gap | User feedback or usage observation | Information | Low — solo dev has deep familiarity |
| 10. Test with real input | A genuine problem worth solving | Information | Medium — contrived tests miss real issues |
| 15. Update website | Website build/deploy pipeline | Resource | Low — already automated |
| 17. Commit and deploy | Git push + any CI/CD | Resource | Low — standard workflow |

MITIGATION:
- Item 1: Maintain a running gap list (output of /skgap runs) so ideas are pre-queued
- Item 10: Keep a "test problems" backlog — real questions/situations to try new skills against
- Item 15: Batch website updates if multiple skills ship in one session
- Item 17: No special mitigation needed — routine operation
```

---

## Step 7: Dependency Graph

```
DEPENDENCY GRAPH: Skill Creation Pipeline

[1. Identify skill gap] (START)
    |
    |---> [2. Check overlap with existing 592 skills]
              |
              |---> [3. Define purpose and scope]
                        |
                        |---> [4. Choose structural pattern] ----+
                        |                                        |
                        |---> [5. Determine tier/category] ------+---> (feeds 13, 14)
                                                                 |
                                    [4] -------------------------+
                                     |
                                     |---> [6. Write SKILL.md]
                                               |
                                               |---> [7. Write interpretations] --+
                                               |                                  |
                                               |---> [8. Write example] ----------+
                                                                                  |
                                                      [9. Create skill directory] <-+
                                                               |
                                     +-------------------------+-------------------------+
                                     |                         |                         |
                              [10. Test real]           [11. Test edges]          [12. Verify chains]
                                     |                         |                         |
                                     +------------+------------+----------+--------------+
                                                  |                       |
                                                  v                       |
                                     [13. Add to category routers] <------+
                                                  |
                        +-------------------------+-------------------------+
                        |                         |                         |
                 [14. CLAUDE.md]          [15. Website index]       [16. Update counts]
                        |                         |                         |
                        +------------+------------+-------------------------+
                                     |
                                     v
                              [17. Commit and deploy] (END)

SUMMARY:
- Total items: 17
- Hard dependencies: 22
- Soft dependencies: 5
- External dependencies: 4
- Parallel opportunities: 4 groups
- Critical path length: 10 steps
- Items on critical path: 1, 2, 3, 4, 6, 7, 9, 10, 13, 17
```

---

## Practical Phases for Solo Developer

Collapsing the dependency graph into actionable work phases:

| Phase | Steps | Parallel? | Est. Time |
|-------|-------|-----------|-----------|
| **Phase 1: Discovery** | 1 (identify gap), 2 (check overlap) | Sequential | 5–15 min |
| **Phase 2: Design** | 3 (scope), then 4 (pattern) ‖ 5 (tier) | Partially parallel | 10–20 min |
| **Phase 3: Write** | 6 (SKILL.md), then 7 (interpretations) ‖ 8 (example) | Partially parallel | 20–45 min |
| **Phase 4: Deploy file** | 9 (create directory) | Single step | 1 min |
| **Phase 5: Test** | 10 (real input) ‖ 11 (edge cases) ‖ 12 (chaining) | Fully parallel | 10–20 min |
| **Phase 6: Integrate** | 13 (routers), 14 (CLAUDE.md) ‖ 15 (website) ‖ 16 (counts) | Mostly parallel | 5–10 min |
| **Phase 7: Ship** | 17 (commit and deploy) | Single step | 2 min |

**Total estimated time per skill: 50–110 minutes**

---

## Key Findings

1. **The critical path runs through writing, not testing.** Steps 6 and 7 (writing the procedure and interpretations) are the bottleneck. Speeding up writing — through templates, pattern libraries, or skill-generation skills like `/imps` — directly shortens the pipeline.

2. **Testing is embarrassingly parallel.** All three testing steps (real input, edge cases, chaining) can happen simultaneously. For a solo dev, this means running them back-to-back is fine, but none blocks the others.

3. **Integration is also parallelizable.** Updating CLAUDE.md, the website, and skill counts can all happen at the same time. A script or checklist that handles all three would eliminate forgotten updates.

4. **The overlap check (step 2) is a hidden bottleneck.** With 592 skills, manually searching for overlap is slow. This is a strong candidate for tooling — a `/fonss` (find overlapping/nearby skills search) invocation or a dedicated similarity check.

5. **Tier/category decisions (step 5) are independent of writing (step 6).** This means you can decide where a skill goes in the taxonomy before or during writing — they don't block each other after scope is defined.

---

## Next Steps

After dependency extraction:
1. Use `/to` to generate a valid task sequence / checklist from these dependencies
2. Use `/pv` to verify all dependencies are satisfiable in practice for a solo developer

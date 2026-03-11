# /dcp Build a decision procedure for "should I add a new skill or improve an existing one?"
**Date:** 2026-03-09
**Skill:** /dcp (Decision Procedure)

---

**Interpretation selected:** Interpretation 1 -- Build a reusable decision process. This is a recurring decision for a solo developer maintaining 592 skills of varying quality. The goal is a mechanical, followable procedure that eliminates overthinking each time this question arises.

---

## Step 1: Dimension Discovery (/dd)

### Seed Examples

1. Added `/but` (challenge-any-statement skill) -- new capability, nothing like it existed
2. Improved `/dcp` itself -- it was missing the interpretation selection block
3. Added `/platitude` -- operationalized a frustration into a new skill type
4. Improved `/aex` -- existing skill was shallow, missing hiddenness rating
5. Added `/soph` -- difficulty-setting skill, new meta-capability
6. Improved `/dd` -- added depth scaling table that was missing
7. Added `/iterate` -- meta-iteration orchestrator, filled a structural gap
8. Improved `/se` -- gap check step was incomplete, fixed it
9. Added `/ecal` -- emotional calibration, covered a blind spot
10. Chose NOT to add a skill because an existing one already covered it (rejected duplicate)

### Comparisons

- `/but` (new) vs improving `/aex` (existing): **Gap type** -- was there nothing, or something inadequate?
- `/platitude` (new) vs `/dd` improvement: **Trigger source** -- user frustration vs internal quality audit
- `/soph` (new) vs `/se` fix: **Scope of change** -- whole new file vs editing steps in existing file
- `/iterate` (new) vs `/dcp` improvement: **Structural role** -- filling an architecture gap vs fixing a specific skill
- rejected duplicate vs `/ecal` (new): **Overlap** -- did something already cover this?

### Dimensions Discovered

| # | Dimension | Values | Why It Matters |
|---|-----------|--------|----------------|
| 1 | **Coverage gap** | No skill covers this / Existing skill partially covers / Existing skill fully covers but poorly | Determines whether "add" is even a valid option |
| 2 | **Quality of existing coverage** | No coverage / Broken / Shallow / Adequate / Strong | If existing skill is strong, improving it further has diminishing returns |
| 3 | **Frequency of need** | Daily / Weekly / Monthly / Rarely | High-frequency gaps hurt more than low-frequency ones |
| 4 | **Effort to add vs improve** | New skill: hours needed / Improvement: hours needed | Direct cost comparison |
| 5 | **Structural role** | Leaf skill / Orchestrator / Meta-skill / Utility | Orchestrators and meta-skills have multiplier effects |
| 6 | **Trigger source** | User request / Internal quality audit / Architecture gap / Frustration pattern / Idea | Some triggers are more reliable signals than others |
| 7 | **Overlap risk** | None / Mild / Significant / Near-duplicate | Adding when overlap is high creates maintenance burden and user confusion |
| 8 | **Improvement type** | Fix bug / Add depth / Add interpretation / Restructure / Add examples | Some improvements are quick wins; others are near-rewrites |
| 9 | **Downstream impact** | Standalone / Fed into by other skills / Feeds into other skills / Hub (both) | Hub skills multiply their quality across the system |
| 10 | **Current skill count pressure** | Manageable / Getting unwieldy / Actively causing confusion | At 592 skills, every addition increases discovery burden |

**TOTAL SPACE:** Not a Cartesian product -- these dimensions interact in a decision tree, not a matrix.

---

## Step 2: Space Enumeration (/se)

### Options per Dimension (Representative)

**Coverage gap:**
- **No skill covers this at all.** Example: no emotional calibration skill existed before `/ecal`.
- **Existing skill partially covers this.** Example: `/aex` extracted assumptions but didn't rate hiddenness.
- **Existing skill fully covers this but does it poorly.** Example: a skill has the right scope but shallow execution.
- **Multiple existing skills collectively cover this.** Example: combining `/rca` + `/dbg` already covers what a proposed `/troubleshoot` would do.

**Quality of existing coverage:**
- **Broken:** Skill exists but produces wrong or misleading output.
- **Shallow:** Skill exists but misses critical steps or dimensions.
- **Adequate:** Skill works but could be better.
- **Strong:** Skill is already one of the best in the toolkit.

**Effort to add vs improve:**
- **Quick add (< 30 min):** Simple leaf skill with clear structure.
- **Medium add (1-2 hrs):** Skill needs research, examples, multiple interpretations.
- **Heavy add (2+ hrs):** Orchestrator or compound skill requiring chain design.
- **Quick fix (< 15 min):** Add a missing line, fix a typo, add one example.
- **Medium improvement (30-60 min):** Add depth scaling, new interpretation block, restructure.
- **Heavy improvement (1+ hr):** Near-rewrite of skill logic.

**Overlap risk:**
- **None:** This is genuinely new territory.
- **Mild:** One or two skills touch this area but from a different angle.
- **Significant:** An existing skill does 60-80% of what this new one would do.
- **Near-duplicate:** An existing skill does 80%+ of what this new one would do.

### Key Interactions Between Dimensions

- If **coverage gap = "no skill covers this"** AND **overlap risk = "none"**, the question is purely "is this worth building?" not "add vs improve."
- If **coverage gap = "existing skill partially covers"** AND **improvement type = "add interpretation"**, improving is almost always faster and better.
- If **structural role = "orchestrator"** AND **quality = "shallow"**, improvement has outsized impact.
- If **current skill count pressure = "actively causing confusion"**, the bar for adding goes way up.

---

## Step 3: Assumption Extraction (/aex)

### The Standard Approach and Its Hidden Assumptions

The conventional approach to "add vs improve" is: "If nothing exists, add. If something exists, improve." This simple heuristic assumes:

| # | Assumption | Type | Hiddenness | Risk if Wrong |
|---|-----------|------|------------|---------------|
| 1 | "Adding a skill is the only way to cover a new capability" | Existence | Deep | Medium -- sometimes parameter/interpretation additions to existing skills cover new ground |
| 2 | "An existing skill's scope is fixed" | Stability | Buried | High -- you can always broaden a skill's scope via new interpretations |
| 3 | "More skills = more capability" | Causal | Deep | High -- at 592, more skills may actually reduce capability by increasing confusion and discovery cost |
| 4 | "Users will find the new skill" | Access | Deep | High -- skill discovery is already a bottleneck; a new skill nobody finds adds zero value |
| 5 | "Quality is roughly uniform" | Knowledge | Shallow | Medium -- in reality, skill quality varies enormously, making improvement often higher-leverage |
| 6 | "The developer's time is the only cost" | Resources | Deep | High -- every skill adds maintenance burden, documentation surface, potential for staleness |
| 7 | "A new skill and an improved skill are equally likely to get used" | Causal | Buried | Critical -- improved skills in known locations get used; new skills may not |
| 8 | "The developer can accurately judge whether a gap exists" | Capability | Deep | Medium -- without auditing existing skills, you may miss that coverage already exists |

### Priority Assumptions to Build Into the Procedure

1. **Assumption #3 (more skills = more capability)** -- The procedure must force a check: "Does adding this skill make the toolkit HARDER to navigate?" At 592 skills, the answer is often yes.
2. **Assumption #4 (users will find it)** -- The procedure must ask: "How will someone discover this skill?"
3. **Assumption #7 (equal usage likelihood)** -- The procedure must weight the fact that improving a known, used skill usually delivers more value than adding an unknown one.
4. **Assumption #8 (can judge gap accurately)** -- The procedure must include a concrete search step, not rely on memory.

---

## Step 4: The Procedure (/stg)

```
=====================================================================
ADD-OR-IMPROVE SKILL DECISION PROCEDURE
=====================================================================

WHO THIS IS FOR: Solo developer maintaining the reasoning toolkit
WHEN TO USE: Every time you think "I should make a skill for this"
             or "this skill could be better"
TIME TO COMPLETE: 5-15 minutes

=====================================================================

STEP 0: What triggered this?

Look at what prompted you to consider adding or improving a skill.
Pick the ONE trigger that matches best:

  (A) You tried to use a skill and it didn't exist
      -> Go to STEP 1

  (B) You used a skill and it produced weak/wrong output
      -> Go to STEP 5

  (C) You had an idea for a cool new skill
      -> Go to STEP 1

  (D) You noticed a pattern of user needs that nothing addresses
      -> Go to STEP 1

  (E) You're doing a quality audit and found a weak skill
      -> Go to STEP 5

=====================================================================

SECTION A: EVALUATING A POTENTIAL NEW SKILL (Steps 1-4)
=====================================================================

STEP 1: Search for existing coverage

Do ALL of the following (do not skip any):

  1a. Search the skills/ directory for keywords related to this
      capability. Use at least 3 different search terms.

  1b. Read the CLAUDE.md tables (both "Category Skills" and
      "Direct Skills") and check: is there an existing skill
      whose description overlaps with what you want?

  1c. Check the category orchestrators (/claim, /decide, /want,
      etc.) -- would one of them already route to a skill that
      covers this?

Write down what you found:

  SEARCH RESULTS:
  - Skills found that overlap: [list them, or "none"]
  - Closest existing skill: [name, or "none"]
  - How much of the new capability does it cover: [0% / 25% / 50% / 75% / 100%]

  If coverage >= 50%: -> Go to STEP 5 (improve that skill instead)
  If coverage = 25%:  -> Go to STEP 2
  If coverage = 0%:   -> Go to STEP 2

---------------------------------------------------------------------

STEP 2: Check the value threshold

Answer each question Yes or No:

  2a. Have you personally needed this capability at least
      3 times in the past month?                              [ Y / N ]

  2b. Would this skill be useful at least monthly going
      forward?                                                [ Y / N ]

  2c. Can you describe the skill's procedure in concrete
      steps (not just "it would help with X")?                [ Y / N ]

  2d. Does this fill a GAP in the skill architecture
      (not just add another leaf skill)?                      [ Y / N ]

  SCORING:
  - 4 Yes answers: Strong case to add. -> Go to STEP 3
  - 3 Yes answers: Moderate case. -> Go to STEP 3
  - 2 Yes answers: Weak case. -> Go to STEP 2E
  - 0-1 Yes answers: Do not add. -> STOP. Write down the idea
    in a "someday" list and revisit in 30 days.

  STEP 2E (weak case tiebreaker):
  Is this an ORCHESTRATOR or META-SKILL (routes to other skills,
  or modifies how other skills run)?
    If Yes: -> Go to STEP 3 (orchestrators have multiplier effects)
    If No:  -> STOP. Write down the idea. Revisit in 30 days.

---------------------------------------------------------------------

STEP 3: Check the cost threshold

Answer each question:

  3a. How long will it take to create a working version?
      [ ] Under 30 minutes
      [ ] 30-60 minutes
      [ ] 1-2 hours
      [ ] Over 2 hours

  3b. How many existing skills would need updating to
      reference or integrate this new skill?
      [ ] 0
      [ ] 1-3
      [ ] 4+

  3c. Does this require a new category or sub-category
      in the skill discovery tables?
      [ ] No
      [ ] Yes

  COST ASSESSMENT:
  - If 3a = "Under 30 min" AND 3b = "0": Low cost. -> Go to STEP 4
  - If 3a = "Over 2 hours" OR 3b = "4+": High cost.
    Ask: "Is there a simpler version of this skill I could add
    instead?" If yes, scope it down and re-answer 3a-3c.
    If no, and Step 2 score was only 3: -> STOP. Not worth it yet.
    If no, and Step 2 score was 4: -> Go to STEP 4
  - All other combinations: Medium cost. -> Go to STEP 4

---------------------------------------------------------------------

STEP 4: Final check before adding

Answer this one question honestly:

  "If I add this skill and then forget about it for 6 months,
  will it still make sense and be findable?"

  If Yes: ADD THE SKILL. Proceed to build it.
  If No:  What would make the answer Yes?
          - If the fix is documentation/naming: Fix that, then add.
          - If the fix is "someone needs to maintain it": -> STOP.
            A skill that requires maintenance to stay valid is a
            liability at 592 skills. Improve an existing skill instead.

  DECISION: ADD NEW SKILL
  Skill name: ____________
  Estimated time: ________
  Discovery path: How will users find this? ____________

  -> DONE

=====================================================================

SECTION B: EVALUATING AN IMPROVEMENT (Steps 5-8)
=====================================================================

STEP 5: Diagnose what's wrong with the existing skill

Open the skill file and read it. Then answer:

  5a. What specific problem did you observe?
      [ ] Missing interpretation block
      [ ] Missing depth scaling
      [ ] Shallow procedure (skips important steps)
      [ ] Wrong or misleading output
      [ ] Poor examples
      [ ] Doesn't chain well with other skills
      [ ] Scope too narrow (should cover more)
      [ ] Scope too broad (tries to do too much)
      [ ] Other: ___________

  5b. Is this skill currently referenced by any orchestrators
      or other skills?
      [ ] Yes -- which ones: ___________
      [ ] No
      [ ] Don't know (search for the skill name across the codebase)

  If 5b = "Yes": This is a high-impact improvement. -> Go to STEP 6
  If 5b = "No":  -> Go to STEP 6

---------------------------------------------------------------------

STEP 6: Estimate improvement scope

  6a. What would the improvement require?
      [ ] Add/edit fewer than 20 lines (quick fix)
      [ ] Add a new section or interpretation (medium)
      [ ] Restructure significant portions (heavy)
      [ ] Near-complete rewrite

  6b. Will the improvement change the skill's external behavior
      (what it produces), or just internal quality?
      [ ] External behavior changes (output gets better/different)
      [ ] Internal only (cleaner but same output)

  DECISION GATE:
  - If 6a = "quick fix": DO IT NOW. No further analysis needed.
    -> Go to STEP 8
  - If 6a = "near-complete rewrite" AND 6b = "internal only":
    -> STOP. Not worth a rewrite for internal-only gains.
    Pick the ONE most impactful change and do just that.
  - All other cases: -> Go to STEP 7

---------------------------------------------------------------------

STEP 7: Prioritize against other improvements

You cannot improve everything. Check:

  7a. Is this skill in the top 20 most-used skills?
      (The category skills, /dcp, /rca, /aex, /se, /dd, etc.)
      [ ] Yes -> High priority
      [ ] No  -> Standard priority

  7b. Is the problem you identified in Step 5 something that
      would cause WRONG output (not just less-good output)?
      [ ] Yes -> High priority (fix bugs before adding features)
      [ ] No  -> Standard priority

  7c. Did you arrive here from Step 1 (you were going to add
      a new skill but found existing coverage)?
      [ ] Yes -> High priority (this improvement replaces a
                 new skill, giving you the capability you wanted)
      [ ] No  -> Standard priority

  RESULT:
  - Any "High priority": Do this improvement next.
  - All "Standard priority": Add to improvement backlog.
    Do it when you next have a < 30 minute work block.

---------------------------------------------------------------------

STEP 8: Execute the improvement

  8a. Make the edit.
  8b. Test the skill with one real input.
  8c. Verify the output is better than before.

  If you arrived from Step 1 (was going to add, found existing):
    8d. Verify the improved skill now covers the capability
        you originally wanted to add.
        If Yes: -> DONE. You avoided adding a 593rd skill.
        If No:  -> Go back to STEP 2 with the remaining gap.

  DECISION: IMPROVE EXISTING SKILL
  Skill improved: ____________
  Change made: ____________
  Time spent: ____________

  -> DONE

=====================================================================

QUICK REFERENCE CARD
=====================================================================

  THE 60-SECOND VERSION:

  1. Search for existing coverage (3+ search terms)
  2. If >= 50% covered -> improve the existing skill
  3. If < 50% covered -> check: needed 3+ times/month?
     - No  -> write it down, revisit in 30 days
     - Yes -> will it still make sense if forgotten for 6 months?
       - No  -> improve an existing skill instead
       - Yes -> add it

  THE ONE-LINE VERSION:

  "Improve unless nothing exists AND it's needed monthly
   AND it's self-maintaining."

=====================================================================
```

---

## Step 5: Failure Anticipation (/fla)

### Failure Modes

| # | Failure Mode | O | S | D | RPN | Tier |
|---|-------------|---|---|---|-----|------|
| 1 | **Skip the search step.** Developer "knows" no skill covers this and adds a near-duplicate. | 8 | 7 | 3 | 168 | High |
| 2 | **Frequency bias.** Something you needed this week feels like "monthly" when it's actually one-off. | 7 | 5 | 6 | 210 | Critical |
| 3 | **Scope creep on improvement.** Quick fix turns into a rewrite. | 6 | 4 | 4 | 96 | Medium |
| 4 | **Sunk cost on new skill.** After starting to build, you discover overlap, but finish anyway because you've already started. | 5 | 6 | 5 | 150 | High |
| 5 | **Improvement-avoidance bias.** Improving feels less exciting than creating, so you rationalize adding when you should improve. | 7 | 6 | 7 | 294 | Critical |
| 6 | **Backlog graveyard.** Items sent to "revisit in 30 days" are never revisited. | 8 | 3 | 2 | 48 | Low |
| 7 | **Misidentifying structural role.** Calling a leaf skill an "orchestrator" to pass the Step 2E tiebreaker. | 4 | 5 | 5 | 100 | Medium |
| 8 | **Discovery path not defined.** New skill passes all checks but nobody can find it. | 6 | 7 | 4 | 168 | High |

### Mitigations (Built into Procedure as Warnings)

**FAILURE #1 (skipping search): ALREADY MITIGATED.**
Step 1 requires 3 different search terms and checking 3 locations. The procedure forces the search.

**FAILURE #2 (frequency bias): WARNING added.**
> At Step 2a, count actual instances. Open your chat history or project log. Do not estimate from memory. If you cannot find 3 concrete instances, the answer is No.

**FAILURE #4 (sunk cost): WARNING added.**
> If at any point during skill creation you discover significant overlap with an existing skill, STOP. Do not finish the new skill. The procedure told you to search first precisely to avoid this -- but if you missed it, cutting your losses now is correct.

**FAILURE #5 (improvement-avoidance bias): WARNING added.**
> Check yourself: are you excited about adding this because it's NEW? Novelty is not a decision criterion. The procedure does not ask "is this exciting?" -- it asks "is this needed and unfindable elsewhere?" If you notice you're rationalizing around the search results in Step 1, the answer is almost always "improve."

**FAILURE #8 (discovery path): ALREADY MITIGATED.**
Step 4 requires writing down the discovery path. If you can't articulate how users find it, you can't add it.

---

## Step 6: Procedure Validation (/pv)

### Validation Report

```
===============================================
PROCEDURE VALIDATION REPORT
===============================================

Procedure: Add-or-Improve Skill Decision
Goal: Mechanically determine whether to add a new skill or improve
      an existing one, optimized for a 592-skill toolkit maintained
      by a solo developer.
Steps: 8 (split across two sections)

VALIDATION RESULTS:

| Dimension      | Status | Notes                                    |
|----------------|--------|------------------------------------------|
| Completeness   |  [x]   | Both paths (add and improve) covered     |
| Dependencies   |  [x]   | All cross-references valid (Step 1->5)   |
| Feasibility    |  [x]   | All steps are concrete actions           |
| Inputs         |  [x]   | Only needs: the idea + access to codebase|
| Outputs        |  [x]   | Produces: clear add/improve/stop decision|
| Consistency    |  [x]   | No contradictions found                  |

OVERALL STATUS: VALID

===============================================

EXECUTABILITY CHECK (per DCP requirements):

| Step   | Executable without expertise? | Ambiguity? |
|--------|-------------------------------|------------|
| Step 0 | Yes - pick from list          | None       |
| Step 1 | Yes - concrete search actions | None       |
| Step 2 | Yes - Y/N questions           | None       |
| Step 3 | Yes - pick from options       | None       |
| Step 4 | Yes - single Y/N question     | None       |
| Step 5 | Yes - checkboxes              | None       |
| Step 6 | Yes - checkboxes              | None       |
| Step 7 | Yes - Y/N questions           | None       |
| Step 8 | Yes - concrete actions        | None       |

Every decision point is binary or explicit multiple choice.
No step says "consider" or "think about" or "use your judgment."

===============================================

MINOR ISSUES:

1. Step 7a asks "is this in the top 20 most-used skills?" but the
   developer may not have usage data.
   Severity: Minor
   Resolution: Replaced with a fixed list of known high-use skills
   as examples. The developer knows which skills they use most.
   STATUS: Fixed in procedure above.

===============================================
```

---

## Common Mistakes

1. **Treating this procedure as optional for "obvious" cases.** The cases that feel obvious are exactly where bias is strongest. If you're sure you need a new skill, you're probably wrong -- run the search anyway.

2. **Searching with only one term.** Skills are named with abbreviations. A concept you're thinking of as "troubleshooting" might be covered by `/dbg`, `/rca`, or `/dcm`. Use at least three search terms.

3. **Conflating "I want this" with "this is needed monthly."** Desire is not frequency. Check your actual history.

4. **Improving a skill you don't use.** If you're doing a quality audit and find a weak skill you've never actually invoked, fixing it is low-priority. Focus improvement energy on skills you actually use.

5. **Adding a skill because someone asked for it once.** One request is not a pattern. Write it down. If it comes up twice more, then evaluate.

---

## When to Override This Procedure

- **Architecture redesign.** If you're restructuring how skills chain together, the normal add/improve calculus doesn't apply. You're operating at a different level.
- **Removing skills.** This procedure doesn't cover skill removal, but at 592 skills, removal may be higher-leverage than either adding or improving. If you notice significant overlap during Step 1, consider whether the EXISTING overlapping skill should be removed or merged.
- **External deadline.** If someone needs a capability by tomorrow, skip the 30-day waiting period. But still do the search.
- **Compound skills (/dcp-like chains).** Compound skills that chain existing skills together are almost always worth adding because they don't increase the primitive skill count -- they add orchestration over what exists.

---

## Worked Examples

### Example 1: "I should make a /troubleshoot skill"

**Step 0:** Trigger = (D) pattern of user needs. -> Step 1.

**Step 1:** Search.
- "troubleshoot" -> no direct match
- "debug" -> `/dbg` exists
- "diagnose" -> `/diagnose` category skill exists, routes to `/rca`, `/dbg`, `/dcm`
- Closest: `/diagnose` orchestrator + `/dbg` + `/rca`
- Coverage: ~75%

**Result:** Coverage >= 50%. -> Step 5 (improve existing).

**Step 5:** `/diagnose` routes well but `/dbg` is shallow -- it doesn't have structured diagnostic steps.

**Step 6:** Medium improvement (add diagnostic protocol section). External behavior changes.

**Step 7:** `/dbg` is fed into by `/diagnose` orchestrator = high-impact. -> Do it next.

**Decision: IMPROVE `/dbg`.** Did not add a 593rd skill.

---

### Example 2: "I need a skill for operationalizing platitudes"

**Step 0:** Trigger = (A) tried to use it, didn't exist. -> Step 1.

**Step 1:** Search.
- "platitude" -> nothing
- "wisdom" -> nothing
- "cliche" -> nothing
- "operationalize" -> nothing
- Closest: nothing.
- Coverage: 0%

-> Step 2.

**Step 2:**
- 2a. Needed 3+ times this month? Yes (kept encountering vague advice in inputs). [Y]
- 2b. Useful monthly? Yes. [Y]
- 2c. Can describe procedure? Yes -- take a platitude, extract the actual mechanism, test it, produce actionable version. [Y]
- 2d. Fills architecture gap? Yes -- no skill converts vague wisdom to concrete procedures. [Y]
- Score: 4. -> Step 3.

**Step 3:**
- 3a. Time to create: 30-60 minutes.
- 3b. Skills to update: 0.
- 3c. New category needed: No.
- Assessment: Medium cost. -> Step 4.

**Step 4:** "If I forget about this for 6 months, will it still make sense?"
Yes. Platitudes are timeless. The skill name `/platitude` is self-explanatory.
Discovery path: Listed in Direct Skills table under "Operationalize wisdom."

**Decision: ADD `/platitude`.**

---

### Example 3: "The /aex skill should have a hiddenness rating"

**Step 0:** Trigger = (B) used it, weak output. -> Step 5.

**Step 5:**
- Problem: Shallow procedure (skips hiddenness rating).
- Referenced by orchestrators? Yes -- `/dcp` chains it, `/araw` uses it.
- High-impact improvement. -> Step 6.

**Step 6:**
- Scope: Add a new section (medium).
- External behavior change: Yes (output gets a new rating column).
-> Step 7.

**Step 7:**
- Top 20 most-used? Yes.
- Wrong output? No, just less-good.
- Arrived from Step 1? No.
- One "High priority" (7a). -> Do this improvement next.

**Step 8:** Add hiddenness rating table and scoring to `/aex`. Test with one input. Verify rating appears in output.

**Decision: IMPROVE `/aex`.**

---

```
=====================================================================
VALIDATION STATUS
=====================================================================

This procedure has not been validated by domain experts.
It was built for a specific context (solo developer, 592-skill
toolkit) and may need adaptation for other contexts.

Bias check: This procedure has a deliberate bias toward IMPROVING
over ADDING. This is intentional -- at 592 skills, the marginal
cost of a new skill is higher than the marginal cost of an
improvement, and the discovery problem makes new skills less
likely to deliver value.

=====================================================================
```

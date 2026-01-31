# DCP — Improving the Decision Procedure Skill

**Date**: 2026-01-31
**Input**: improving the decision procedure skill

---

## Step 1: Decision Dimensions

**Core decision**: When you look at a `/dcp` output and want to make it better, what do you change, and how do you know the change is an improvement?

| # | Dimension | Description | Why It Matters |
|---|-----------|-------------|----------------|
| 1 | **Executability Gap** | Where does the procedure require interpretation, judgment, or expertise that the user doesn't have? | The entire point of `/dcp` is mechanical execution. Every gap is a defect. |
| 2 | **Coverage Completeness** | Does the procedure handle all the cases the user will actually encounter? | Missing cases = the user hits a dead end and the procedure fails silently. |
| 3 | **Granularity Level** | Are steps too coarse (user doesn't know what to do) or too fine (procedure is 200 steps and nobody follows it)? | There's a sweet spot. Too coarse = unusable. Too fine = abandoned. |
| 4 | **Decision Point Clarity** | At each branch, can the user unambiguously determine which path to take? | Ambiguous branches are where procedures fail in practice. The user guesses, often wrong. |
| 5 | **Path Length** | How many steps does the user traverse from start to answer? | Longer paths = more dropout. Each step is a chance for the user to abandon the procedure. |
| 6 | **Output Actionability** | Does the procedure end with something the user can act on, or with "analysis" they must still interpret? | A procedure that ends with "now consider these factors" has failed. It must end with "do X." |
| 7 | **Failure Mode Coverage** | Does the procedure warn about and route around the ways it can go wrong? | Procedures without failure mode handling work in the lab and break in the field. |
| 8 | **Domain Fit** | Is the procedure well-matched to the actual decision domain, or is it a generic template stretched over a specific problem? | Generic procedures give generic answers. The value is in domain-specific routing. |
| 9 | **Validation Evidence** | Has anyone actually followed this procedure and gotten a good outcome? | Unvalidated procedures are hypotheses, not tools. |
| 10 | **Structural Integrity** | Are there dead ends, infinite loops, missing branches, or unreachable steps? | Structural bugs are invisible to the author and fatal to the user. |
| 11 | **Assumption Transparency** | Does the procedure make its assumptions visible, so the user knows when to override? | Hidden assumptions are the #1 cause of procedures giving the wrong answer on edge cases. |
| 12 | **Compression Ratio** | What is the ratio of insight to word count? | A 50-page procedure with 5 real insights should be a 2-page procedure. Bloat kills adoption. |

---

## Step 2: Options per Dimension

**1. Executability Gap**: None (fully mechanical) | Minor (1-2 steps need slight interpretation) | Moderate (several "consider" or "think about" steps) | Severe (requires domain expertise at multiple points)

**2. Coverage Completeness**: Full (all real-world cases handled) | High (>90% of cases) | Moderate (common cases only) | Low (happy path only)

**3. Granularity Level**: Too coarse (steps span multiple actions) | Right (one action per step) | Too fine (sub-actions broken out unnecessarily) | Mixed (inconsistent across sections)

**4. Decision Point Clarity**: Binary with observable criteria | Multiple choice with clear definitions | Subjective criteria ("is it good enough?") | Missing criteria entirely

**5. Path Length**: Short (3-7 steps) | Medium (8-15 steps) | Long (16-30 steps) | Excessive (30+)

**6. Output Actionability**: Direct action ("do X") | Ranked options ("choose from these") | Framework ("evaluate using these criteria") | Analysis only ("here are the factors")

**7. Failure Mode Coverage**: Comprehensive with recovery paths | Major modes covered | Token warnings only | None

**8. Domain Fit**: Custom-built for domain | Adapted generic template | Generic with domain examples | Purely generic

**9. Validation Evidence**: Field-tested with outcomes tracked | Tested on examples | Desk-checked only | None

**10. Structural Integrity**: Verified (all paths terminate, no dead ends) | Mostly sound | Has known gaps | Unverified

**11. Assumption Transparency**: All assumptions listed with override conditions | Major assumptions noted | Implicit throughout | Not addressed

**12. Compression Ratio**: Tight (every sentence earns its place) | Moderate (some redundancy) | Bloated (lots of scaffolding) | Padded (filler content)

**Key Interactions**:
- If Executability Gap = Severe, no amount of improvement on other dimensions matters
- If Path Length = Excessive AND Compression Ratio = Bloated → the procedure needs surgery, not editing
- If Validation Evidence = None → you're guessing about all other dimensions
- If Domain Fit = Generic → Decision Point Clarity will inevitably be low (generic criteria can't be specific)

---

## Step 3: Hidden Assumptions

| # | Assumption | Reality | Danger |
|---|-----------|---------|--------|
| 1 | **"Improvement" means adding more** | Most procedures improve by *removing* steps. The best improvement is often deletion. | Authors reflexively add detail, warnings, and edge cases. Each addition makes the procedure harder to follow. |
| 2 | **The author can evaluate their own procedure** | Authors can't see their own blind spots. They know what they meant, so ambiguous steps read as clear to them. | Self-review catches structural bugs but misses executability gaps. You need a naive user to find those. |
| 3 | **A procedure that covers more cases is better** | A procedure that covers 80% of cases and is actually followed beats one that covers 100% and is abandoned at step 8. | Completeness competes with usability. Optimize for the 80%. |
| 4 | **The 6-step DCP chain is the right chain** | The chain (dd → se → aex → stg → fla → pv) is one approach. Some decisions need different chains. Some need no chain — just a direct procedure. | The DCP meta-structure may be overkill for simple decision types, and insufficient for complex ones. |
| 5 | **Text is the right output format** | Flowcharts, decision trees, lookup tables, and interactive tools are often better than linear text procedures. | The skill defaults to text because LLMs output text. But the user might be better served by a diagram. |
| 6 | **One procedure fits all users** | Expert users need less hand-holding. Novice users need more. A procedure calibrated for one fails the other. | The current DCP makes no distinction. It targets a "general user" that doesn't exist. |
| 7 | **The procedure needs to be right the first time** | Procedures improve through iteration and failure. Version 1 should be deployed fast and refined from real usage data. | Perfectionism in procedure design delays deployment. Ship, observe, fix. |
| 8 | **Improving the skill means improving the template** | The biggest improvements might be upstream (better input classification) or downstream (better output formatting), not in the procedure generation itself. | Tunnel vision on the 6-step chain misses systemic improvements. |

---

## Step 4: The Procedure

```
IMPROVING A DECISION PROCEDURE — PROCEDURE
===========================================

PURPOSE: Given an existing /dcp output, systematically find
and fix its weaknesses. Produces a concrete improvement plan
ranked by impact.

WHO THIS IS FOR: Anyone who has generated a decision procedure
and wants to make it better before deploying it.


STEP 0: WHAT KIND OF IMPROVEMENT ARE YOU MAKING?
=================================================

Look at your existing procedure and answer:

Q1: Has anyone besides you tried to follow it?
    → Yes, and they succeeded: Go to SECTION A (Polish)
    → Yes, and they struggled: Go to SECTION B (Fix)
    → No: Go to SECTION C (First Review)


SECTION A: POLISHING A WORKING PROCEDURE
=========================================

The procedure works. You're optimizing, not fixing.

Step A1: Measure path length.
  ACTION: Count the steps on the LONGEST path from start
          to output.
  CHECK: Is it ≤ 15?
    → Yes: Go to A2.
    → No: Find steps that can be merged or eliminated.
          Target: cut 30% of steps. Then go to A2.

Step A2: Check compression ratio.
  ACTION: For each step, ask: "If I deleted this step,
          would the user get a DIFFERENT (worse) answer?"
    → Yes: Keep it.
    → No: Delete it.
  WHAT YOU SHOULD SEE: A shorter procedure that produces
          the same outputs.

Step A3: Add quick-reference card.
  ACTION: Write a 5-line summary that covers 60%+ of cases.
          Put it at the TOP of the procedure.
  WHY: Most users will use the quick reference. The full
       procedure is for edge cases.

Step A4: Version the procedure.
  ACTION: Label it with a version number and date.
          Note what changed from the previous version.

→ SECTION A COMPLETE.


SECTION B: FIXING A STRUGGLING PROCEDURE
=========================================

Someone tried to follow it and got stuck or got a wrong answer.

Step B1: Locate the failure point.
  ACTION: Ask the person (or examine the attempt):
          "At which step did you get confused, stuck, or
          go the wrong direction?"
  WRITE DOWN: The step number and what happened.

Step B2: Classify the failure.
  Look at the failure point. Which is it?

  a) AMBIGUOUS BRANCH: The user couldn't tell which path
     to take at a decision point.
     → Go to B3a.

  b) MISSING CASE: The user's situation wasn't covered
     by any branch.
     → Go to B3b.

  c) WRONG ANSWER: The user followed the procedure correctly
     and got a bad result.
     → Go to B3c.

  d) ABANDONED: The user gave up before finishing.
     → Go to B3d.

Step B3a: Fix ambiguous branch.
  ACTION: Rewrite the decision point. Replace subjective
          criteria with observable ones.
  TEST: Can you describe a PHYSICAL OBSERVATION or
        MEASURABLE FACT that determines the branch?
    → Yes: Use that.
    → No: Break the decision into two smaller decisions,
          each with clearer criteria.
  EXAMPLE:
    BAD:  "Is the decision important?" (subjective)
    GOOD: "If you choose wrong, will it cost more than
           $1,000 or more than 1 week to fix?" (observable)

Step B3b: Fix missing case.
  ACTION: Add a new branch or section that handles this case.
  CHECK: Is this a common case (>10% of users will hit it)?
    → Yes: Add it to the main flow.
    → No: Add it as an edge case appendix.
  ALSO: Add a catch-all at the decision point: "If none of
        the above match your situation → [what to do]."

Step B3c: Fix wrong answer.
  ACTION: Trace the procedure path the user followed.
          Find where the logic broke.
  COMMON CAUSES:
    - A dimension was missing from Step 1 (the procedure
      didn't consider a factor that mattered)
    - An assumption (Step 3) wasn't surfaced, and the user's
      situation violated it
    - The failure modes (Step 5) didn't include this scenario
  FIX: Add the missing dimension, assumption, or failure mode.
       Then re-derive the affected procedure steps.

Step B3d: Fix abandonment.
  ACTION: Count steps to the abandonment point.
  CHECK: Was it >10 steps in?
    → Yes: The procedure is too long for the decision's stakes.
           Cut it. See Section A, Step A2.
    → No: The step at the abandonment point was probably too
          hard. Simplify it or break it into smaller steps.
  ALSO: Consider whether the user NEEDED the procedure at all.
        If the decision is simple, the procedure is overhead.
        Write a 3-step version instead.

→ SECTION B COMPLETE.


SECTION C: FIRST REVIEW (NO USER FEEDBACK YET)
===============================================

Nobody has tried the procedure. You need to stress-test it
yourself before someone else does.

Step C1: Run the "Naive User" test.
  ACTION: Read each step and ask: "Could someone with ZERO
          knowledge of this domain execute this step?"
  For each step, mark: YES / NO / MAYBE.
  FIX every NO and MAYBE. Common fixes:
    - Define jargon inline
    - Replace "evaluate" with "count" or "check"
    - Replace "consider" with "list" or "answer"
    - Add "WHAT YOU SHOULD SEE" after every step

Step C2: Run the "Dead End" test.
  ACTION: Trace every possible path through the procedure.
  CHECK for each path:
    a) Does it terminate? (no infinite loops)
    b) Does it produce an output? (no dead ends)
    c) Is the output actionable? (not "now think about...")
  FIX: Add missing terminations. Add outputs to dead ends.
       Replace analysis outputs with action outputs.

Step C3: Run the "Wrong Answer" test.
  ACTION: Invent 3 scenarios where you KNOW the right answer.
          Run each through the procedure.
  CHECK: Does the procedure give the right answer for all 3?
    → Yes for all: Go to C4.
    → No for any: The procedure has a logic error. Find the
          step where it diverges from the right answer. Fix
          the branching logic or add a missing dimension.

Step C4: Run the "Edge Case" test.
  ACTION: Invent 2 unusual or extreme scenarios.
          Run each through the procedure.
  CHECK: Does the procedure handle them?
    → Yes: Go to C5.
    → No: Either add handling or add an explicit
          "When to Override" note for these cases.

Step C5: Run the "Compression" test.
  ACTION: Try to cut the procedure in half (by word count).
  RULE: If cutting doesn't change the outputs for your 5
        test scenarios from C3-C4, keep the shorter version.
  WHY: Shorter procedures get followed. Longer ones get
       skimmed.

Step C6: Deploy and schedule review.
  ACTION: Ship the procedure as-is. Mark it "v0.1 — unvalidated."
  SCHEDULE: After 3 real uses, run Section B on any failures.
            After 5 successful uses, run Section A to polish.

→ SECTION C COMPLETE.
```

---

## Step 5: Failure Modes

| # | Failure Mode | How to Recognize | What to Do |
|---|-------------|------------------|------------|
| 1 | **Improving in the wrong dimension** | You spent an hour adding failure modes to a procedure whose real problem is that Step 3 is ambiguous. | Always run Section C (or B if you have feedback) BEFORE deciding what to improve. Diagnose first, fix second. |
| 2 | **Polishing instead of testing** | You've rewritten the same procedure 4 times without anyone using it. Each version is "better" but none are validated. | Ship v0.1 now. Real feedback > hypothetical improvement. The procedure will tell you what's wrong when someone uses it. |
| 3 | **Adding when you should subtract** | The procedure grows with each revision. It now has 40 steps, 12 edge case appendices, and 8 failure mode warnings. Nobody reads it. | Apply the compression test (C5) ruthlessly. If your test scenarios still pass with half the procedure, the other half was noise. |
| 4 | **Optimizing for the wrong user** | You're making the procedure more rigorous for experts when the actual users are novices who need simpler language. Or vice versa. | Define your user before improving. Write their name on the procedure: "This is for [specific person/role]." |
| 5 | **Confusing procedure quality with output quality** | The procedure is well-structured and clear, but the decisions it produces are mediocre. The problem is the underlying logic, not the formatting. | Run the "Wrong Answer" test (C3). If the procedure gives wrong answers for known cases, the fix is in the decision logic (dimensions, branching criteria), not in the procedure structure. |
| 6 | **Ignoring the meta-structure** | You improve individual procedures but never question whether the 6-step DCP chain itself is right. Maybe this decision type needs 3 steps, not 6. Maybe it needs a different chain entirely. | Before improving a specific procedure, ask: "Is /dcp the right skill for this decision type, or does it need a custom approach?" Not everything is a nail for this hammer. |
| 7 | **Review fatigue** | You review the procedure so many times that you can't see it fresh. Every step seems clear because you wrote it and know what you meant. | Get someone else to read it. If nobody is available, wait 48 hours and re-read. Fresh eyes catch what familiar eyes miss. |

---

## Step 6: Validation

Executability check on each step:

- **A1-A4**: All concrete. "Count steps" is observable. "Delete if output unchanged" is testable. Pass.
- **B1**: "Ask the person" — requires access to that person. **Note**: If no person is available, simulate with the C-path tests. Pass with note.
- **B2**: Four categories with concrete descriptions. Pass.
- **B3a-d**: Each has a concrete fix action and a test. The "physical observation" test in B3a is the strongest executability check. Pass.
- **C1-C6**: All concrete. The "Naive User" test, "Dead End" test, "Wrong Answer" test, "Edge Case" test, and "Compression" test are all mechanical. Pass.
- **Dead ends**: All paths terminate. Section B loops back to specific fix steps. Section C ends at deployment. Pass.
- **Loops**: B3c could theoretically loop (fix → test → fail → fix), but the scope is bounded to one failure at a time. Pass.

---

## QUICK REFERENCE CARD

**The 3-Question Improvement Check** (handles 60%+ of cases):

1. **Can a novice follow every step?** Read each step aloud. If you say "well, what I mean is..." — rewrite that step.
2. **Does it give the right answer on 3 known cases?** If not, fix the branching logic.
3. **Can you cut it in half without changing the outputs?** If yes, cut it.

That's it. Do those three things and you've caught most problems.

---

## COMMON MISTAKES

1. **Improving before deploying.** Ship v0.1. Get real feedback. Improve v0.2 from data, not guesses.
2. **Treating all dimensions as equal.** Executability and wrong-answer rate matter 10x more than formatting or completeness.
3. **Reviewing your own work without a gap.** You can't see your own blind spots. Wait 48 hours or get another reader.
4. **Adding edge cases to the main flow.** Edge cases belong in appendices. The main flow is for the 80% case.
5. **Improving presentation when the logic is wrong.** A beautifully formatted procedure that gives wrong answers is worse than an ugly one that gives right answers. Fix logic first, format second.

---

## WHEN TO OVERRIDE THIS PROCEDURE

- **The procedure is fundamentally the wrong tool.** If the decision type shouldn't be a flowchart (e.g., it's genuinely creative, requires real-time judgment, or changes too fast to proceduralize), stop improving the procedure and build something else — a checklist, a set of heuristics, or a training exercise.
- **You have extensive user data.** If you have 50+ uses with outcome tracking, use statistical analysis instead of this manual review process. Look at which paths correlate with good outcomes and prune the rest.
- **The domain expert disagrees with the logic.** If an expert says "this procedure gives the wrong answer in my field," trust them over the procedure. Redesign from their knowledge, not from the template.

---

## WORKED EXAMPLES

### Example 1: Improving the "Starting a Software Project" DCP

**Section C** (no user feedback yet):
- **C1 (Naive User)**: Step 7 says "evaluate technical tradeoffs." A non-technical founder can't do this. **Fix**: Replace with a checklist: "Does it need to handle >1000 users? Does it need to work offline? Does it need real-time updates?" — route to technology recommendations based on answers.
- **C3 (Wrong Answer)**: Tested with "personal blog" — procedure recommended a full architecture review. Wrong. **Fix**: Added a fast-path at Step 0: "Is this a solo project with no paying users? → Use the simplest tool you already know. Done."
- **C5 (Compression)**: Cut from 35 steps to 18. All 3 test scenarios still produce the same output.

### Example 2: Fixing the "Meaning of Life" DCP after user feedback

**Section B** (user got stuck):
- **B1**: User stuck at Step 4: "Rate each value on a scale of 1-10."
- **B2**: Ambiguous branch (B3a) — user didn't know what "1" vs "10" meant for abstract values.
- **B3a Fix**: Replaced rating scale with pairwise comparison: "Which matters more to you: A or B?" Repeated for all pairs. Ranking derived from comparisons, not absolute ratings.

### Example 3: Polishing a validated "Job Offer Evaluation" DCP

**Section A** (procedure works, 5+ successful uses):
- **A1**: Longest path = 22 steps. Over limit. Merged 4 "gather information" steps into a single checklist. New longest path = 16. Still over. Moved 3 rare-scenario steps to appendix. New longest path = 13. Pass.
- **A2**: Deleted Step 11 ("Research the company's stock performance") — removing it didn't change the answer in any test scenario. It was noise.
- **A3**: Added quick reference: "If total comp is >20% higher, benefits are comparable, and you'd enjoy the work → take it. If any of those three fail → run the full procedure."

---

*Validation status: This procedure has not been validated by domain experts. It is a meta-procedure for improving decision procedures, derived from analysis of procedure design patterns and common failure modes.*

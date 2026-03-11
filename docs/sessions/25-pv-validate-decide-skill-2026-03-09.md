# /pv Validate the /decide skill by running it on 3 different decision types and checking if each step works
**Date:** 2026-03-09
**Skill:** /pv (Procedure Validation)

---

## Interpretation Selected

**Interpretation 1 — Validate a procedure before execution**: We have a step-by-step routing procedure (/decide) and want to verify it is complete, correctly ordered, and feasible by running it against three concrete test cases.

---

## Approach

The /decide skill is a sub-orchestrator — it classifies decision inputs and routes to the correct analytical skills. To validate it, I will:

1. State the procedure's steps as extracted from the skill
2. Run three test decisions through it to see if each step produces clear, actionable routing
3. Apply all six validation dimensions
4. Generate a validation report

---

## Step 1: State the Procedure

```
PROCEDURE TO VALIDATE: /decide (Make a Decision)

GOAL: Take a user's decision input, classify it correctly, determine
appropriate depth, and route to the right analytical skill(s) to
produce a recommendation with confidence level.

STEPS:
1. Identify interpretation (binary / multi-option / open)
2. Extract the choice point — state the options
3. Check: Is this actually a decision? (or a claim/goal/emotion/idea)
4. Determine how many options
5. Determine whether criteria are known
6. Assess stakes and reversibility
7. Execute: route to appropriate skill(s)
8. Apply decision quality checks (supplementary analysis)
9. Scope control
10. Pre-completion checklist
11. After-completion report

DECLARED DEPENDENCIES:
- Step 2 depends on Step 1 (interpretation determines how to extract)
- Step 3 depends on Step 2 (need the choice point to test if it's a decision)
- Steps 4-6 depend on Step 3 (only proceed if it IS a decision)
- Step 7 depends on Steps 4-6 (routing uses option count + criteria + stakes)
- Steps 8-9 depend on Step 7 (quality checks and scope control apply to executed analysis)
- Steps 10-11 depend on Steps 7-9

EXTERNAL INPUTS REQUIRED:
- User's decision statement: [from user]
- Context about stakes: [from user or inferred]
- Criteria for "better": [from user or derived via /want]
```

---

## Step 2-7: Validation via Three Test Cases

### Test Case 1: "Should I learn Rust or Go?"

**Step 1 — Interpretation**: Multi-option comparison (Interpretation 2). Two named options. **[PASS]** — clearly matches.

**Step 2 — Extract choice point**: Options are "Learn Rust" vs "Learn Go." Hidden third option: "Learn neither / learn something else." **[PASS]** — the skill explicitly warns about false binaries and says to look for the third option.

**Step 3 — Is this actually a decision?**: Yes — the user is choosing between defined alternatives. Not a claim, goal, emotion, or idea. **[PASS]** — the routing table correctly identifies this as a decision, not one of the other types.

**Step 4 — How many options?**: Two named options (multi-option). The skill routes to `/cmp` then `/araw` on top candidates. **[PASS]** — correct routing for two-option comparison.

**Step 5 — Are criteria known?**: No — "which should I learn" doesn't specify criteria (for career? for fun? for a specific project?). The skill says: route to `/want` to clarify the underlying goal, then return with criteria. **[PASS]** — correctly catches the missing criteria.

**Step 6 — Stakes and reversibility**: Learning a programming language is **reversible** — you can always learn the other one later. The skill says: lighter analysis, `/cmp` is sufficient. **[PASS]** — correct depth matching.

**Step 7 — Execute**: Route to `/want` first (clarify criteria), then `/cmp [Rust vs Go with criteria]`. For reversible decisions, this is sufficient — no need for `/prm` or `/fla`. **[PASS]** — appropriate routing.

**Step 8 — Quality checks**: No ethical dimensions, no safety risks. Could benefit from `/iaw` (reframe: "maybe the question is which project to build, not which language to learn"). **[PASS]** — the quality check table covers this case.

**Test Case 1 Verdict: ALL STEPS PASS.** The skill handles a straightforward multi-option reversible decision correctly.

---

### Test Case 2: "Should I move to a new city?"

**Step 1 — Interpretation**: Binary choice (Interpretation 1). "Should I X?" where the implicit alternative is "don't X" (stay in current city). **[PASS]** — clearly matches.

**Step 2 — Extract choice point**: Options are "Move to [new city]" vs "Stay in [current city]." The skill correctly notes that "Should I X?" always has a hidden comparator — the alternative is not "nothing" but "whatever the user would do instead." **[PASS]** — and the skill's Core Principle 2 explicitly addresses this pattern.

**Step 3 — Is this actually a decision?**: Yes — a genuine choice between two alternatives. **[PASS]**.

**Step 4 — How many options?**: Binary. The skill routes to `/araw [moving vs staying]`. **[PASS]**.

**Step 5 — Are criteria known?**: Not stated. "Should I move?" doesn't specify what the user is optimizing for (career, cost of living, relationships, lifestyle). The skill routes to `/want` to clarify. **[PASS]**.

**Step 6 — Stakes and reversibility**: Moving cities is **costly to reverse** (not impossible, but expensive and disruptive). The skill says: moderate to deep analysis — `/cmp` + `/araw` on top choice. Since this is closer to irreversible for many people, the skill also offers the deeper path: `/araw` on each option + `/prm` + `/fla`. **[PASS]** — correct escalation based on stakes.

**Step 7 — Execute**: Route to `/want` (clarify what matters), then `/araw [move vs stay]`, then `/prm [moving]` and `/fla [moving]` for the high-stakes path. **[PASS]** — appropriate depth.

**Step 8 — Quality checks**: This decision could benefit from:
- `/obo` — obvious bad outcomes (moving without a support network)
- `/fut` — future analysis (where will each city be in 5 years?)
- `/sdc` — self-deception check (am I running from something?)
The skill's quality check table lists all three of these. **[PASS]**.

**[ISSUE FOUND]** The skill's stakes classification has three tiers (reversible / costly to reverse / irreversible), but "move to a new city" sits ambiguously between "costly to reverse" and "irreversible" depending on the person's situation (renting vs buying, single vs family). The skill doesn't provide guidance for borderline cases — it says to use `/ecal` if unsure, which is reasonable but could be more explicit about what makes a move more or less reversible.

**Test Case 2 Verdict: ALL STEPS PASS with one minor issue** — borderline stakes classification could use more guidance.

---

### Test Case 3: "Should I open-source this project?"

**Step 1 — Interpretation**: Binary choice (Interpretation 1). "Should I X?" — open-source vs keep proprietary. **[PASS]**.

**Step 2 — Extract choice point**: Options are "Open-source the project" vs "Keep it proprietary/private." But Core Principle 5 ("the best option is often none of the above") prompts us to consider: partial open-source? Open-source later? Open-source the core but keep extensions proprietary? **[PASS]** — the skill's principles catch the false binary.

**Step 3 — Is this actually a decision?**: Yes. But this is a subtle case — "Should I open-source this?" could also be an idea to test (/viability). The routing table says: "What about doing X?" routes to `/viability`. However, "Should I X?" routes to decision, not viability. The distinction is thin. **[MINOR ISSUE]** — the boundary between "Should I X?" (decision) and "What about doing X?" (idea/viability) could be clearer. In practice, the skill would likely handle it correctly because the user's phrasing uses "should," which maps to decision.

**Step 4 — How many options?**: Binary (with hidden alternatives identified in Step 2). Routes to `/araw [open-source vs proprietary]`. **[PASS]**.

**Step 5 — Are criteria known?**: Partially. Open-sourcing has known standard criteria (community growth, reputation, maintenance burden, competitive advantage, licensing implications). The skill says for partial criteria: "state the implied criteria explicitly and confirm." **[PASS]**.

**Step 6 — Stakes and reversibility**: This is a **one-way door** for the most part. Once code is public, it cannot be made private again (copies exist). The skill correctly identifies irreversible decisions as needing the deepest analysis: `/araw` on each option + `/prm` + `/fla`. **[PASS]** — correct classification and routing.

**Step 7 — Execute**: Route to `/araw [open-source]` + `/araw [keep proprietary]` + `/prm [open-sourcing]` + `/fla [open-sourcing]`. **[PASS]** — appropriate for irreversible decision.

**Step 8 — Quality checks**: This decision involves:
- Foreclosure blindness (once open-sourced, certain monetization paths close) — Core Principle 6 catches this
- `/obo` — obvious bad outcomes (someone forks and competes with you)
- `/ogo` — obvious good outcomes (community contributions, hiring signal)
- Possible `/eth` considerations (if the project has safety implications)
All are covered by the quality check table. **[PASS]**.

**[ISSUE FOUND]** The skill's "After Completion" report template asks for "First action if the recommendation is followed." For an irreversible decision like open-sourcing, there should be stronger language about confirming the decision before taking the first action — perhaps a "cooling off" recommendation or a "commit point" marker. The skill doesn't address the gap between "decision made" and "decision executed" for irreversible choices.

**Test Case 3 Verdict: ALL STEPS PASS with two minor issues** — boundary with /viability could be sharper, and irreversible decisions need a commit-point safeguard.

---

## Validation Dimensions Summary

### Completeness Check

```
COMPLETENESS CHECK:

Goal: Route any decision input to the right analytical skill(s) and produce
a recommendation with confidence level.

To achieve this goal, we need:
[x] Classify the input (binary / multi-option / open)
[x] Detect non-decisions and reroute
[x] Identify whether criteria exist
[x] Assess stakes / reversibility
[x] Route to correct skill(s)
[x] Provide quality checks
[x] Control scope
[x] Generate structured output

Step coverage:
- Classify input: Covered by Steps 1, 4 [x]
- Detect non-decisions: Covered by Step 3 [x]
- Criteria identification: Covered by Step 5 [x]
- Stakes assessment: Covered by Step 6 [x]
- Routing: Covered by Step 7 [x]
- Quality checks: Covered by Step 8 [x]
- Scope control: Covered by Step 9 [x]
- Structured output: Covered by Steps 10-11 [x]

GAPS FOUND:
- No explicit "commit point" or confirmation step for irreversible decisions
  between "recommendation made" and "first action taken"
  -> Suggest: Add a commit-point check for irreversible decisions in Step 10

GAP CHECK: Minor gap found
```

### Dependency Validation

```
DEPENDENCY VALIDATION:

| Step | Dependencies | Earlier Steps | Valid? |
|------|-------------|---------------|--------|
| 1. Interpretation | None | N/A | [x] |
| 2. Extract choice point | Step 1 | Step 1 | [x] |
| 3. Is this a decision? | Step 2 | Steps 1-2 | [x] |
| 4. How many options? | Step 3 | Steps 1-3 | [x] |
| 5. Criteria known? | Step 3 | Steps 1-3 | [x] |
| 6. Stakes/reversibility | Step 3 | Steps 1-3 | [x] |
| 7. Execute (route) | Steps 4-6 | Steps 1-6 | [x] |
| 8. Quality checks | Step 7 | Steps 1-7 | [x] |
| 9. Scope control | Step 7 | Steps 1-7 | [x] |
| 10. Pre-completion | Steps 7-9 | Steps 1-9 | [x] |
| 11. After completion | Step 10 | Steps 1-10 | [x] |

ORDERING ERRORS: None
CYCLE CHECK: No cycles found [x]

Note: Steps 4, 5, and 6 can run in parallel (no dependencies between them).
This is fine — the skill presents them as sequential but they're independent assessments.

DEPENDENCY CHECK: Valid
```

### Feasibility Check

```
FEASIBILITY CHECK:

| Step | Feasibility | Issues |
|------|------------|--------|
| 1. Interpretation | [x] Feasible | Three clear categories |
| 2. Extract choice | [x] Feasible | None |
| 3. Is it a decision? | [x] Feasible | Boundary cases exist but routing table is comprehensive |
| 4. Option count | [x] Feasible | None |
| 5. Criteria known? | [x] Feasible | None |
| 6. Stakes assessment | [x] Feasible | Borderline cases need judgment |
| 7. Execute/route | [!] Conditional | Depends on downstream skills existing and working |
| 8. Quality checks | [x] Feasible | None |
| 9. Scope control | [x] Feasible | None |
| 10. Pre-completion | [x] Feasible | None |
| 11. After completion | [x] Feasible | None |

FEASIBILITY ISSUES:
- Step 7: Routes to /cmp, /araw, /prm, /fla, /dom, /want, /search, /obv,
  /ecal, and others. All must exist and function.
  -> Mitigation: These are core skills in the toolkit and are assumed present.
  -> Risk: If any downstream skill is missing, /decide silently fails.

FEASIBILITY CHECK: All feasible (conditional on downstream skills)
```

### Input Availability Check

```
INPUT AVAILABILITY CHECK:

| Input | Needed By | Source | Available? |
|-------|-----------|--------|------------|
| User's decision statement | Step 1 | User | [x] |
| Context/stakes info | Step 6 | User or inferred | [x] Partial — may need to ask |
| Criteria for "better" | Step 5 | User or /want | [x] Has fallback (/want) |
| Option list (for open) | Step 4 | /search | [x] Has fallback (/search) |

INPUT ISSUES: None — the skill has fallback routes for every case where
input might be missing. This is well-designed.

INPUT CHECK: All available
```

### Output Verification

```
OUTPUT VERIFICATION:

Goal: Produce a recommendation with confidence level for the user's decision.

Trace outputs:
- Steps 1-3 produce: Classification of input type
- Steps 4-6 produce: Option count, criteria, stakes assessment
- Step 7 produces: Analytical results from downstream skills
- Step 8 produces: Quality-checked results
- Step 10 produces: Verified checklist items
- Step 11 produces: Structured report with recommendation, confidence,
  foreclosures, and next actions

Does final output match goal?

OUTPUT ANALYSIS:
- Final output: Decision report with recommendation, confidence level,
  foreclosures, what would change the recommendation, first action
- Goal: Help user make a decision
- Match: Yes

The After Completion template is comprehensive:
  [x] Decision as framed
  [x] Options considered
  [x] Criteria used
  [x] Comparison results
  [x] Foreclosures for each option
  [x] Recommendation with confidence level
  [x] What would change the recommendation
  [x] First action

OUTPUT CHECK: Goal achieved
```

### Consistency Check

```
CONSISTENCY CHECK:

| Element A | Element B | Relationship | Issue? |
|-----------|-----------|-------------|--------|
| Core Principle 2 (hidden comparator) | Step 2 (extract choice) | Aligned | [x] |
| Core Principle 4 (reversibility) | Step 6 (stakes) | Aligned | [x] |
| Core Principle 5 (none of above) | Failure mode: false binary | Aligned | [x] |
| Core Principle 6 (foreclosures) | Pre-completion checklist | Aligned | [x] |
| Depth Scaling table | Stakes routing (Step 6) | Aligned | [x] |
| Binary routing (Step 4) → /araw | Execute section → /araw | Aligned | [x] |
| Multi-option routing → /cmp then /araw | Execute section → /cmp then /araw | Aligned | [x] |

CONTRADICTIONS FOUND: None

CONSISTENCY CHECK: Consistent
```

---

## Step 8: Validation Report

```
===============================================
PROCEDURE VALIDATION REPORT
===============================================

Procedure: /decide (Make a Decision)
Goal: Route decision inputs to correct analytical skills,
      produce recommendation with confidence level
Steps: 11 (including sub-steps)

VALIDATION RESULTS:

| Dimension    | Status | Issues |
|-------------|--------|--------|
| Completeness | [x]   | 1 minor |
| Dependencies | [x]   | 0      |
| Feasibility  | [x]   | 1 minor |
| Inputs       | [x]   | 0      |
| Outputs      | [x]   | 0      |
| Consistency  | [x]   | 0      |

OVERALL STATUS: VALID

===============================================

TEST CASE RESULTS:

| Test Case | Type | All Steps Pass? | Issues |
|-----------|------|----------------|--------|
| "Should I learn Rust or Go?" | Multi-option, reversible | Yes | None |
| "Should I move to a new city?" | Binary, costly to reverse | Yes | 1 minor |
| "Should I open-source this?" | Binary, irreversible | Yes | 2 minor |

===============================================

ISSUES REQUIRING RESOLUTION:

1. No commit-point safeguard for irreversible decisions
   Severity: Minor
   Resolution: Add a "confirmation gate" in the pre-completion
   checklist for irreversible decisions — something like:
   "For irreversible decisions: Have you slept on this?
   Is there a way to test this at smaller scale first?"

2. Borderline stakes classification lacks guidance
   Severity: Minor
   Resolution: Add examples or a quick heuristic for the
   boundary between "costly to reverse" and "irreversible."
   E.g., "If undoing it costs >50% of doing it, treat as irreversible."

3. Thin boundary between /decide and /viability for "Should I X?"
   Severity: Minor
   Resolution: Add a note: "If 'Should I X?' is about whether X
   is worth attempting (feasibility), route to /viability. If it's
   about choosing X over an alternative, stay in /decide."

4. Silent failure if downstream skills are missing
   Severity: Minor
   Resolution: The skill could note: "If a routed skill is unavailable,
   fall back to inline analysis using the relevant criteria."

===============================================

RECOMMENDED ACTIONS:

[ ] Add commit-point gate for irreversible decisions in pre-completion checklist
[ ] Add heuristic for borderline reversibility classification
[ ] Clarify /decide vs /viability boundary in Step 3
[ ] Add fallback guidance when downstream skills are unavailable

After fixes applied, re-validate procedure.

===============================================
```

---

## Summary

The /decide skill is **well-structured and valid**. It successfully handled all three test cases — a reversible multi-option choice, a costly-to-reverse binary choice, and an irreversible binary choice. The routing logic is sound, the depth scaling matches stakes correctly, and the core principles actively prevent common decision-making errors (false binaries, missing criteria, foreclosure blindness).

Four minor improvements identified, none of which block execution. The most impactful would be adding a commit-point safeguard for irreversible decisions — the skill does excellent work getting to a recommendation but could do more to prevent premature action on one-way doors.

# DCP — Managing Combinatorial Explosion of Decision Procedures and Intelligence Cascades

**Date**: 2026-01-31
**Input**: managing a combinatorial explosion of decision procedures and intelligence cascades

---

## Step 1: Decision Dimensions

**Input**: *Managing a combinatorial explosion of decision procedures and intelligence cascades*

The core decision: **When you have a system of many interlinked procedures that can invoke each other, how do you keep it from exploding into unmanageable complexity?**

Here are the dimensions that determine the right answer:

| # | Dimension | Description | Why It Matters |
|---|-----------|-------------|----------------|
| 1 | **Cascade Depth** | How many levels deep can one procedure invoke another? | Unbounded depth = unbounded compute. Must cap or detect. |
| 2 | **Branching Factor** | How many sub-procedures can a single step invoke? | Depth 3 with branching 5 = 125 leaf nodes. This is the core explosion driver. |
| 3 | **Redundancy Rate** | How often do different paths re-invoke the same procedure on the same or overlapping input? | Without memoization, you do identical work repeatedly. |
| 4 | **Value Decay Rate** | Does the Nth sub-analysis actually improve the output, or does marginal value collapse? | Most cascades hit diminishing returns quickly. Analysis beyond depth 2-3 rarely changes the conclusion. |
| 5 | **Decision Reversibility** | Is the decision you're making reversible or irreversible? | Irreversible decisions justify deeper cascades. Reversible ones don't. |
| 6 | **Time Budget** | How much time/compute is available for the decision? | The optimal cascade depth is a function of how much you can afford to spend. |
| 7 | **Input Specificity** | Is the input narrow and concrete, or vague and open-ended? | Vague inputs generate more branches. Specific inputs prune early. |
| 8 | **Procedure Overlap** | How much do different procedures cover the same ground from different angles? | High overlap means the system does redundant analysis under different names. |
| 9 | **Output Consumer** | Who/what consumes the output — a human, another procedure, or a final action? | Machines can digest more output. Humans need it compressed. |
| 10 | **Interaction Effects** | Do procedure outputs depend on each other (order matters), or are they independent? | Independent = parallelizable and prunable. Dependent = must sequence. |
| 11 | **Error Propagation** | Does a bad sub-procedure output corrupt downstream procedures? | Cascades amplify errors. Deeper cascades amplify more. |
| 12 | **Novelty of Input** | Has this type of input been seen before, or is it genuinely new? | Familiar inputs can short-circuit to cached patterns. Novel inputs may need full exploration. |

---

## Step 2: Options per Dimension

**For each dimension, the possible states:**

**1. Cascade Depth**: 0 (no sub-invocation) | 1 (one level) | 2 (two levels) | 3+ (deep) | Unbounded (no limit)

**2. Branching Factor**: 1 (linear chain) | 2-3 (moderate) | 4-7 (wide) | 8+ (explosive)

**3. Redundancy Rate**: None | Low (<20% overlap) | Medium (20-50%) | High (>50%)

**4. Value Decay Rate**: Steep (90% of value in first pass) | Moderate (70% in first pass) | Flat (each pass adds proportional value)

**5. Decision Reversibility**: Easily reversible | Costly to reverse | Irreversible

**6. Time Budget**: Seconds | Minutes | Hours | Unbounded

**7. Input Specificity**: Precise question | Scoped topic | Open-ended domain | Unbounded exploration

**8. Procedure Overlap**: Minimal (<10%) | Moderate (10-40%) | High (>40%)

**9. Output Consumer**: Human reading | Human acting | Another procedure | Autonomous system

**10. Interaction Effects**: Fully independent | Weakly coupled | Strongly coupled | Circular dependencies

**11. Error Propagation**: Contained (errors don't spread) | Linear (proportional) | Amplifying (errors compound)

**12. Novelty**: Routine | Somewhat new | Genuinely novel | Unprecedented

**Key Interactions**:
- If Branching Factor > 3 AND Cascade Depth > 2 → explosion is guaranteed
- If Value Decay = Steep AND Depth > 1 → deeper passes waste resources
- If Redundancy = High AND no memoization → most work is repeated
- If Input Specificity = Open-ended → Branching Factor will be high regardless of procedure design

---

## Step 3: Hidden Assumptions

The conventional approach to managing procedure cascades assumes:

| # | Assumption | Reality | Danger |
|---|-----------|---------|--------|
| 1 | **More analysis = better decisions** | Marginal value of additional analysis drops steeply. After ~2 levels, you're refining noise. | People build deep cascades because "thoroughness" feels safe. |
| 2 | **Each procedure adds unique value** | Procedures with different names often run similar logic. `/aex` and `/av` and `/ht` overlap significantly. | The naming creates an illusion of distinct work. |
| 3 | **The user can absorb the output** | A 6-step cascade producing 30 pages of analysis overwhelms. The user reads maybe 20%. | Unread output is wasted compute. |
| 4 | **Procedure ordering doesn't matter** | Earlier procedures frame the problem for later ones. Different orderings produce different conclusions. | Path dependency masquerades as objectivity. |
| 5 | **Sub-procedure invocation is free** | Each invocation has cost: time, tokens, cognitive load, and—critically—context window pollution. | The cascade fills context with intermediate outputs, degrading later analysis quality. |
| 6 | **You need a procedure for everything** | Many decisions can be made with a simple heuristic. The procedure is overhead when intuition suffices. | The system defaults to maximum ceremony. |
| 7 | **Composability implies you should compose** | Just because procedures *can* chain doesn't mean they *should*. Most decisions need 1-2 tools, not 6. | The architecture invites overuse. |
| 8 | **The explosion is about procedures** | The real explosion is about *attention*. Finite attention allocated across infinite analysis paths is the binding constraint. | Managing procedures is the wrong frame. Managing attention is the right one. |

---

## Step 4: The Procedure

```
COMBINATORIAL EXPLOSION MANAGEMENT PROCEDURE
=============================================

PURPOSE: When you have a system of decision procedures that can
invoke each other, this tells you EXACTLY when to cascade,
when to stop, and how to prevent explosion.

WHO THIS IS FOR: Anyone operating a library of chainable
analysis/decision tools (GOSM, reasoning toolkits, AI agent
systems, decision support systems).


STEP 0: CLASSIFY YOUR SITUATION
================================

Answer these two questions:

Q1: Are you DESIGNING a procedure library, or USING one right now?
    → Designing: Go to SECTION A
    → Using (making a decision now): Go to SECTION B

Q2: Has your current cascade already exploded?
    → Yes (you're drowning in output): Go to SECTION C
    → No: Continue with Section A or B as above


SECTION A: DESIGNING PROCEDURE LIBRARIES TO PREVENT EXPLOSION
=============================================================

Step A1: Set a hard depth limit.
  ACTION: Pick a maximum cascade depth. Write it down.
  RULE: Default to 2. Only increase to 3 if you can name a
        specific decision type that demonstrably needs it.
        Never allow 4+.
  WHAT YOU SHOULD SEE: A single number (2 or 3) written as
        a system constraint.

Step A2: Set a hard branching limit per step.
  ACTION: For each step in any procedure, limit sub-invocations
        to at most 2.
  RULE: If a step says "invoke /a, /b, /c, /d" — that's too many.
        Force a choice: which 2 are most likely to change the answer?
  WHAT YOU SHOULD SEE: No procedure step invokes more than 2
        sub-procedures.

Step A3: Compute your worst case.
  ACTION: Multiply branching_limit ^ depth_limit.
  CHECK: Is the result ≤ 8?
    → Yes: You're safe. Go to Step A4.
    → No: Reduce depth or branching until it is. Return to A1.
  EXAMPLE: Depth 2, branching 2 = 4 leaf nodes. Safe.
           Depth 3, branching 3 = 27 leaf nodes. Not safe.

Step A4: Build a redundancy map.
  ACTION: For every procedure in your library, list the
        CORE QUESTION it answers in one sentence.
  CHECK: Do any two procedures answer the same core question?
    → Yes: Merge them or designate one as primary. The other
           becomes a "variant" only invoked when the primary
           explicitly fails.
    → No: Move to Step A5.
  WHAT YOU SHOULD SEE: A table of procedures with unique,
        non-overlapping core questions.

Step A5: Add circuit breakers.
  ACTION: At every sub-invocation point, add this gate:
        "Before invoking [sub-procedure]: State what specific
        question you need answered that you cannot answer from
        what you already have. If you can already answer it,
        skip the invocation."
  WHAT YOU SHOULD SEE: Every → INVOKE line has a preceding
        gate condition.

Step A6: Add a value-decay check.
  ACTION: After depth 1 completes, require a check:
        "Did the sub-procedure's output change your conclusion
        from what it was before invoking it?"
    → Yes, it changed: Allow depth 2 if needed.
    → No, it confirmed: Stop. Do not go deeper.
  WHY: If the first sub-analysis confirms your initial read,
        further analysis almost never reverses it.

Step A7: Define output compression requirements.
  ACTION: Set a rule: each procedure's output must fit in
        ≤ N lines (default: 20 lines for sub-procedures,
        50 lines for top-level).
  RULE: If a sub-procedure produces more, it must include
        a summary line at the top. Only the summary propagates
        upward in the cascade.

→ SECTION A COMPLETE. Your library now has structural guards
  against explosion.


SECTION B: USING PROCEDURES RIGHT NOW (RUNTIME DECISIONS)
==========================================================

Step B1: State your decision in one sentence.
  ACTION: Write: "I need to decide: _______________"
  CHECK: Is the sentence specific enough that two people would
        understand the same decision?
    → Yes: Go to B2.
    → No: Narrow it until it is. Rewrite and re-check.

Step B2: Estimate reversibility.
  ACTION: If you choose wrong, what happens?
    → Easily changed (costs < 1 hour to reverse): Go to B3-FAST
    → Costly to change (costs days/money): Go to B3-MEDIUM
    → Cannot be reversed: Go to B3-DEEP

Step B3-FAST: Lightweight path.
  ACTION: Pick ONE procedure that most directly addresses your
        decision. Run it. Do NOT cascade.
  RULE: If the procedure tries to invoke sub-procedures, skip
        them. Use your current knowledge to fill gaps.
  OUTPUT: Your answer + confidence level (high/medium/low).
  CHECK: Is confidence medium or higher?
    → Yes: Done. Act on it.
    → No: Upgrade to B3-MEDIUM.

Step B3-MEDIUM: Standard path.
  ACTION: Pick ONE procedure. Allow it to invoke UP TO 2
        sub-procedures at depth 1. No deeper.
  GATE before each sub-invocation: "What specific question do
        I need answered that I can't answer now?"
        If you can't articulate the question → skip invocation.
  OUTPUT: Your answer + the 1-2 sub-analyses that changed it.
  CHECK: Do you have a clear answer?
    → Yes: Done.
    → No: Upgrade to B3-DEEP.

Step B3-DEEP: Full analysis path.
  ACTION: Pick ONE procedure. Allow cascading to depth 2,
        branching 2.
  HARD LIMIT: Maximum 4 sub-procedure invocations total.
  After each sub-invocation, check: "Did this change my answer?"
    → No: Stop cascading on this branch.
    → Yes: Continue.
  OUTPUT: Your answer + the chain of reasoning that led to it.

Step B4: The "Enough" check.
  After ANY path completes, ask:
  "If I got the OPPOSITE conclusion from one more sub-analysis,
  would I actually change my mind?"
    → No: You already have enough information. Stop.
    → Yes: Run that one specific sub-analysis. Then stop regardless.


SECTION C: YOUR CASCADE HAS ALREADY EXPLODED
=============================================

Step C1: Stop all running sub-procedures immediately.
  ACTION: Do not invoke anything else. Halt.

Step C2: State your original question.
  ACTION: Write the decision you were trying to make.
  CHECK: Can you still articulate it clearly?
    → Yes: Go to C3.
    → No: You've lost the thread. Start over with Section B,
          Step B1.

Step C3: Triage existing output.
  ACTION: For each sub-procedure output you've generated, write
        ONE sentence: what did this tell me that I didn't already
        know?
  RULE: If you can't write that sentence → discard that output.
  WHAT YOU SHOULD SEE: 2-5 sentences capturing the non-redundant
        insights from all your analysis.

Step C4: Decide from the triage.
  ACTION: Using only the sentences from C3, make your decision.
  CHECK: Can you make it?
    → Yes: Done.
    → No: Identify the ONE specific gap. Run ONE procedure to
          fill it. Then decide.
```

---

## Step 5: Failure Modes

| # | Failure Mode | How to Recognize | What to Do |
|---|-------------|------------------|------------|
| 1 | **"But this one is different" bypass** | You find yourself arguing that YOUR decision justifies deeper cascading than the limits allow. | It almost certainly doesn't. The limits exist because everyone thinks their case is special. Follow the limits. Override only if the decision is genuinely irreversible AND unprecedented. |
| 2 | **Procedure shopping** | You run a procedure, don't like the answer, and invoke a different procedure hoping for a different result. | The second procedure isn't more "right" — you're just seeking confirmation. Accept the first result or articulate specifically what was wrong with its reasoning. |
| 3 | **Compression resistance** | You feel that summarizing a sub-procedure's output to 1 sentence "loses important nuance." | If you can't compress it, you haven't understood it. The nuance is usually noise. Force the compression. |
| 4 | **Depth creep via renaming** | You stay at "depth 2" by embedding what should be a sub-procedure into the body of the parent procedure. The depth limit is technically met, but the effective depth is 4+. | Count the number of distinct analytical steps, not the number of formal invocations. If your "single procedure" does 6 different analyses, it's effectively depth 6. |
| 5 | **Analysis as avoidance** | You keep cascading not because you need more information, but because deciding feels risky and analysis feels productive. | Apply the Step B4 check honestly: "Would the opposite conclusion from one more analysis change my mind?" If no, you're avoiding, not analyzing. |
| 6 | **Context window poisoning** | In AI systems: the cascade fills the context with intermediate outputs, degrading the quality of later analysis. The 5th sub-procedure is working with worse context than the 1st. | This is invisible and insidious. The structural limits (depth 2, branching 2) exist partly to prevent this. Don't override them for AI-driven cascades. |
| 7 | **Premature termination** | You apply these limits too aggressively and stop before you have the ONE piece of information that would flip your decision. | The B4 check catches this: if you genuinely believe one more analysis could change your mind, do that one analysis. The rule is "stop after enough," not "stop immediately." |

---

## Step 6: Validation

Checking each step for executability:

- **A1-A7**: All concrete actions with numeric outputs. No "use your judgment." Pass.
- **B1**: "Write one sentence" — concrete. The specificity check could be subjective. **Fix**: Added "two people would understand the same decision" as the test.
- **B2**: Three categories with clear descriptions. Pass.
- **B3 variants**: Each has a hard limit and a gate. Pass.
- **B4**: The "opposite conclusion" test is a concrete thought experiment. Pass.
- **C1-C4**: All concrete. C3's "one sentence" rule is mechanical. Pass.
- **Dead ends**: Every path terminates at a decision or loops back to a specific step. No infinite loops. Pass.
- **Ambiguity check**: The only remaining judgment call is "Did this change my answer?" which requires comparing before/after states. **This is executable**: write your answer before the sub-invocation, write it after, compare.

---

## QUICK REFERENCE CARDS

**The 2-2-8 Rule**: Max depth 2, max branching 2, max 8 leaf procedures. If your cascade exceeds this, restructure.

**The Gate Question**: "What specific question do I need answered that I cannot answer from what I already have?" No answer = no invocation.

**The Flip Test** (Step B4): "Would the opposite conclusion from one more analysis change my mind?" No = stop.

**The Compression Rule**: Every sub-procedure output must compress to one sentence of non-redundant insight. Can't compress = don't understand = don't cascade further.

---

## COMMON MISTAKES

1. **Building for thoroughness instead of decisions**. The goal is a decision, not a complete analysis. Stop when you can decide.
2. **Treating all decisions as irreversible**. Most decisions are easily reversed. Use the fast path.
3. **Confusing procedure count with rigor**. Running 6 procedures that overlap 60% is less rigorous than running 2 that don't.
4. **Not memoizing**. If you've already analyzed X, and a sub-procedure wants to analyze X again, reuse the output.
5. **Cascading on confirmation, not contradiction**. The only reason to go deeper is if the sub-analysis might CHANGE your answer. If it's going to confirm, save the compute.

---

## WHEN TO OVERRIDE THIS PROCEDURE

Seek expert help (a human with domain knowledge) when:
- The decision is **irreversible AND unprecedented** (no procedure library covers truly novel situations well)
- You've hit the cascade limit and **still cannot make the decision** (the problem may not be analyzable with the tools you have)
- **Multiple procedures give contradictory answers** and you can't determine which framing is correct (this indicates a values conflict, not an information deficit — use `/vcd`)
- **The stakes are existential** (company survival, safety-critical systems, legal liability) — procedures are aids, not substitutes for expert judgment

---

## WORKED EXAMPLES

### Example 1: Deciding which 3 skills to chain for a user question

**B1**: "I need to decide: which skills to invoke for 'help me evaluate this business idea'"
**B2**: Easily reversible (can re-run with different skills) → B3-FAST
**B3-FAST**: The `/viability` sub-orchestrator directly addresses this. Run it alone. No cascade.
**Result**: Done in one step. No explosion.

### Example 2: Designing a new compound skill (like /dcp itself)

**Situation**: Section A (designing a library component)
**A1**: Depth limit = 2
**A2**: Branching limit = 2 per step
**A3**: 2^2 = 4 ≤ 8. Safe.
**A4**: Check that each chained skill answers a distinct question. `/dd` (what matters), `/se` (what exists), `/aex` (what's hidden), `/stg` (build it), `/fla` (what breaks), `/pv` (does it work). Six skills but in a LINEAR chain (branching = 1), so worst case = 6, not exponential. Safe.
**A5**: Add gates: before each step, "Do I already have enough to build the procedure?" If yes after step 3, skip to step 4.

### Example 3: A cascade that's already exploded

User ran `/analyze` which invoked `/dd` + `/aex` + `/sya`, each of which invoked 2 more skills. Result: 9 procedure outputs, 40+ pages, user is overwhelmed.
**C1**: Stop.
**C2**: "I need to decide: should we build this feature?"
**C3**: Triage: (1) The market dimension is the key uncertainty. (2) Technical feasibility is confirmed. (3) Cost estimates are consistent at ~$50K. (4-9) Redundant.
**C4**: Decision: Build it if market validation confirms demand. One gap: market validation. Run one procedure for that. Done.

---

*Validation status: This procedure has not been validated by domain experts. It is derived from analysis of combinatorial systems, complexity theory, and observed failure patterns in procedure-heavy decision frameworks.*

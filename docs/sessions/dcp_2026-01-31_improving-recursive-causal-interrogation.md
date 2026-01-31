# DCP — Improving Recursive Causal Interrogation

**Date**: 2026-01-31
**Input**: improving recursive causal interrogation

---

## Step 1: Decision Dimensions

**Core decision**: When you look at the RCI skill and want to make it better, what specifically should you change, and how do you know the change is an improvement rather than a corruption?

This is an unusually delicate decision domain. RCI is *anti-procedural by design* — it explicitly says "No structure. No format. No templates. No checkboxes. Pure reasoning." Any improvement procedure risks destroying the thing it's trying to improve.

| # | Dimension | Description | Why It Matters |
|---|-----------|-------------|----------------|
| 1 | **Principle Completeness** | Are there reasoning failure modes that RCI's 15 principles don't catch? | A missing principle means the interrogation systematically misses a class of error. |
| 2 | **Principle Redundancy** | Do multiple principles say the same thing in different words? | Redundancy dilutes attention. If a user reads 15 principles but 5 are duplicates, they'll miss the 10 real ones. |
| 3 | **Activation Reliability** | When a user reads the skill and applies it, does the interrogation actually start tracing backward, or does it drift into forward reasoning? | The #1 failure mode of RCI is that users *think* they're tracing backward but are actually constructing forward. If the skill text doesn't prevent this, nothing else matters. |
| 4 | **Depth Achieved** | How deep does a typical RCI session go before the user stops or loops? | Shallow sessions (2-3 levels) rarely reach anything surprising. The value is in levels 5-10+. If the skill doesn't drive depth, it's underperforming. |
| 5 | **Self-Application Integrity** | Does the skill survive its own interrogation? (Its "fixed point property.") | If you apply RCI to RCI and find contradictions, the skill has a structural flaw. |
| 6 | **Distinctiveness from Other Skills** | What does RCI do that `/aex`, `/aw`, `/ar`, `/araw` don't? | If the answer is "nothing unique," RCI is redundant. If the answer is clear, that uniqueness needs to be sharpened. |
| 7 | **Output Usefulness** | After an RCI session, does the user have something they can use — an insight, a reframing, a decision — or just a pile of questions? | RCI deliberately avoids conclusions. But "pure questioning with no output" risks being a pleasant intellectual exercise that changes nothing. |
| 8 | **Failure Detection** | Can the user tell when RCI is failing — when the questioning is going nowhere, when they're in a loop, when they've gone forward instead of backward? | Without failure detection, the user can spend an hour in a bad RCI session and not know it's bad. |
| 9 | **Teachability** | Can someone who's never seen RCI read the skill once and do it correctly? | The skill is written in a philosophical style. This may inspire or confuse. If confused users apply it wrong, the style is a bug. |
| 10 | **Integration with Other Skills** | When RCI is invoked from within another skill (or vice versa), does it compose cleanly? | RCI says "no structure," but it lives in a system of structured skills. This tension needs resolution. |
| 11 | **Scope Calibration** | Does the skill help the user decide *how much* RCI to apply? (A trivial question doesn't need 50 levels of causal tracing.) | Without scope guidance, users either under-apply (surface level) or over-apply (infinite regress). |
| 12 | **LLM vs. Human Execution** | Does the skill perform differently when executed by an LLM vs. a human? | LLMs may simulate backward tracing while actually pattern-matching forward. Humans may genuinely trace backward but lack rigor. Different executors need different guardrails. |

---

## Step 2: Options per Dimension

**1. Principle Completeness**: All failure modes covered | Most covered | Major gaps | Untested

**2. Principle Redundancy**: No overlap | Minor overlap (2-3 principles converge) | Significant overlap (5+ principles cover ~3 ideas) | Mostly redundant

**3. Activation Reliability**: Reliably produces backward tracing | Usually works | Works for some users, not others | Unreliable (users drift forward without noticing)

**4. Depth Achieved**: Consistently deep (7+ levels) | Moderate (4-6 levels) | Shallow (2-3 levels) | Variable (depends on user skill)

**5. Self-Application Integrity**: Fully self-consistent | Minor tensions | Contradictions present | Untested

**6. Distinctiveness**: Unique capability | Mostly unique with some overlap | Significant overlap | Redundant with existing skills

**7. Output Usefulness**: Reliably produces actionable insight | Sometimes useful | Inconsistent | Rarely changes anything

**8. Failure Detection**: Built-in detection with recovery | Some detection | No detection | Unaddressed

**9. Teachability**: Learnable from one read | Learnable with practice | Requires coaching | Opaque

**10. Integration**: Composes cleanly | Works with adaptation | Friction with structured skills | Incompatible

**11. Scope Calibration**: Built-in scope guidance | Implicit guidance | No guidance | Actively discourages scoping

**12. LLM vs. Human**: Both execute well | LLMs better | Humans better | Neither executes reliably

**Key Interactions**:
- If Activation Reliability is low, improvements to all other dimensions are wasted
- If Teachability is low AND Depth Achieved is low → users never get past the surface
- If Output Usefulness is low → users stop using RCI regardless of its theoretical power
- If Self-Application Integrity fails → the skill's own claims are undermined

---

## Step 3: Hidden Assumptions

| # | Assumption | Reality | Danger |
|---|-----------|---------|--------|
| 1 | **"Backward" vs "forward" is always clear** | In practice, the boundary between tracing causes and projecting consequences is blurry. "What caused me to think X?" can produce "Because Y is important" — which is a forward-looking value judgment disguised as causal tracing. | Users believe they're going backward when they're actually constructing narratives forward. The skill doesn't provide a mechanical test for direction. |
| 2 | **Anti-structure is a feature** | For skilled reasoners, removing structure forces genuine thinking. For unskilled reasoners, removing structure produces confusion and drift. The skill assumes the user is a skilled reasoner. | Most users are not skilled reasoners. "No structure, no format, no templates" may liberate experts and paralyze novices. |
| 3 | **Questions are inherently more honest than statements** | Questions can be leading, loaded, or rhetorical. "Isn't it obvious that X?" is a statement in question clothing. RCI assumes questioning = genuine inquiry. | Users can go through the motions of questioning while actually constructing the answer they wanted. The skill's emphasis on "mostly questions" doesn't prevent this. |
| 4 | **Deeper is always better** | Some causal chains hit ground quickly. The cause of "I'm hungry" is "I haven't eaten." Going deeper ("Why haven't I eaten? What caused eating to be a need?") isn't useful — it's philosophy. | RCI says "go until something solid emerges" but doesn't help distinguish "solid because grounded" from "solid because bored." |
| 5 | **The user can interrogate their own blind spots** | If a user has a blind spot, they don't know it exists. Asking "What am I missing?" only finds things they're somewhat aware of. True blind spots resist self-interrogation by definition. | RCI is powerful for surfacing *latent* knowledge (things you know but haven't articulated). It's weak for surfacing *absent* knowledge (things you don't know at all). The skill doesn't distinguish these. |
| 6 | **RCI applied by an LLM is the same as RCI applied by a human** | LLMs don't have genuine uncertainty or reactions. When an LLM "questions itself," it's generating plausible question-answer pairs, not interrogating its actual reasoning process. The LLM has no "actual reasoning process" to interrogate in the way the skill describes. | The skill was written for minds with genuine reactions. LLMs simulate this. The simulation may produce useful output, but the *mechanism* is fundamentally different, which means the failure modes are different too. |
| 7 | **"Pure reasoning" is achievable** | All reasoning occurs within priors, frames, and heuristics. "No templates" is itself a template. RCI is itself a procedure, despite claiming to reject procedure. | The skill has a productive contradiction: it's a structured approach to unstructured reasoning. This is fine, but the skill doesn't acknowledge it, which may confuse users who take "no structure" literally. |
| 8 | **The fixed-point property is validation** | "This process, applied to itself, returns itself" is a coherence check, not a correctness check. Many bad processes also have fixed-point properties (e.g., "trust your gut" survives "should I trust my gut? → yes, my gut says yes"). | The skill presents self-consistency as a strength. It is one, but it's not proof of quality. |

---

## Step 4: The Procedure

```
IMPROVING RECURSIVE CAUSAL INTERROGATION — PROCEDURE
=====================================================

PURPOSE: Given the current RCI skill, systematically identify
what's working, what's failing, and what to change. Produces
a prioritized list of specific improvements.

WARNING: RCI is anti-procedural by design. Improvements must
preserve the core mechanism (backward causal tracing through
questioning) while fixing what's broken. Over-proceduralizing
RCI would destroy it. Under-improving it leaves known flaws.


STEP 0: WHAT IS YOUR RELATIONSHIP TO RCI?
==========================================

Q1: Have you used RCI yourself?
    → Yes, multiple times: Go to SECTION A (Experienced User)
    → Yes, once or twice: Go to SECTION B (New User)
    → No, evaluating from outside: Go to SECTION C (Evaluator)


SECTION A: IMPROVING RCI FROM EXPERIENCE
=========================================

You've used it. You know what happens in practice.

Step A1: List your RCI sessions.
  ACTION: Write down the last 3-5 times you used RCI.
          For each, note:
          (a) What you started with (the input)
          (b) How deep you went (rough count of causal levels)
          (c) What you ended with (insight, confusion, nothing)
          (d) Whether your behavior changed afterward

Step A2: Classify your outcomes.
  ACTION: For each session, mark it:
  ✓ WORKED: Reached genuine insight that changed something
  ~ PARTIAL: Interesting questioning but no actionable result
  ✗ FAILED: Went nowhere, looped, or drifted forward

Step A3: Diagnose failures.
  ACTION: For each ✗ or ~ session, identify the failure point.
  Pick the one that matches:

  a) DRIFT: Started backward but gradually shifted to
     forward reasoning (implications, what-to-do, meaning).
     → Problem is ACTIVATION RELIABILITY. Go to Step A4a.

  b) SHALLOW: Stayed backward but stopped after 2-3 levels.
     Didn't reach anything surprising.
     → Problem is DEPTH. Go to Step A4b.

  c) LOOP: Hit the same cause repeatedly from different
     angles. Circled without progressing.
     → Problem is BRANCH EXPLORATION. Go to Step A4c.

  d) PILE: Generated many questions but couldn't synthesize
     anything from them. Output was a sprawl.
     → Problem is OUTPUT USEFULNESS. Go to Step A4d.

  e) PERFORMANCE: Felt like going through motions. Questions
     were formulaic. No genuine inquiry.
     → Problem is AUTHENTICITY. Go to Step A4e.

Step A4a: Fix drift.
  DIAGNOSIS: The skill says "if forward, stop, go back" but
  doesn't give a MECHANICAL TEST for direction.
  IMPROVEMENT: Add a concrete direction test to the skill.
  Proposed test: "After writing any statement, ask: does this
  describe something that ALREADY HAPPENED (cause) or
  something that WOULD/SHOULD happen (consequence)?
  If it uses future tense, conditional language, or
  prescriptive framing → it's forward. Delete it.
  Rewrite as a backward-facing question."
  CHECK: Would this test have caught the drift in your
         failed session?
    → Yes: Add it to the skill.
    → No: The drift is subtler. Describe what actually happened
          and craft a test for that specific pattern.

Step A4b: Fix shallow depth.
  DIAGNOSIS: User stops because (pick one):
    (i)  They hit what feels like ground but isn't
    (ii) The next question feels too hard or weird
    (iii) They lose interest
  For (i): Add this check to the skill: "Before accepting
    ground, ask: is this a BRUTE FACT (physical law, logical
    necessity) or a SOCIAL FACT (convention, habit, assumption)?
    Social facts have deeper causes. Keep going."
  For (ii): Add: "If the next question feels uncomfortable,
    that's signal. Discomfort often marks the boundary between
    what you've examined and what you've assumed. Go toward it."
  For (iii): Add scope guidance. See Step A5.

Step A4c: Fix loops.
  DIAGNOSIS: The skill says "note the loop, that's a fixed
  point." But not all loops are genuine fixed points. Some
  are the user's reasoning circling back to comfortable ground.
  IMPROVEMENT: Add a loop test: "When you notice a loop, ask:
  am I returning to the same CAUSE, or just using the same
  WORDS? If same cause: genuine fixed point, note it.
  If same words but different context: the words are masking
  a distinction. Unpack the word. What do you mean by [X]
  this time vs. last time?"

Step A4d: Fix output sprawl.
  DIAGNOSIS: RCI says "no conclusions." But it also needs
  to produce something usable.
  IMPROVEMENT: This is the hardest fix because it touches
  RCI's core philosophy. Two options:

  OPTION 1 (Conservative): Don't change RCI. Add a
  separate post-RCI synthesis step. After RCI completes,
  invoke /ins or /p to extract actionable conclusions.
  RCI stays pure; synthesis is downstream.

  OPTION 2 (Integrated): Add to RCI: "When a causal chain
  terminates (ground, genuine loop, or exhaustion after
  real effort), write one sentence: 'This chain revealed
  that ___.' This is not a conclusion. It's a waypoint.
  It can be questioned in the next chain."

  CHECK: Which preserves RCI's character better?
    → Option 1 if you want RCI to stay philosophically pure
    → Option 2 if you want RCI to be self-contained

Step A4e: Fix inauthenticity.
  DIAGNOSIS: The questioning has become performative.
  The user asks "what caused X?" but already has an answer
  in mind and is just going through the motions.
  IMPROVEMENT: Add to the skill: "If you notice you already
  know what you're going to write before you write it, STOP.
  That's not questioning — that's narrating. Ask instead:
  what am I AVOIDING by asking this safe question? What's
  the question I don't want to ask?"
  This is already partially covered by "Question The Question"
  and "Gap Awareness" but needs to be more explicit about
  the specific symptom of pre-known answers.

Step A5: Add scope guidance (if depth or interest is the issue).
  ACTION: Add to "When to Use" section:
  SCOPE GUIDE:
  - Trivial decisions: 3-5 levels, then decide.
  - Moderate decisions: 7-12 levels, across 2+ branches.
  - Major life questions: 15+ levels, multiple sessions.
  - If unsure about scope: start at 7 levels and check if
    you've hit anything surprising. Yes → continue. No →
    either the question is shallower than you thought, or
    you're drifting. Re-read the question and restart.

→ SECTION A COMPLETE. Take your specific fixes to the skill file.


SECTION B: IMPROVING RCI AS A NEW USER
=======================================

You've tried it once or twice. You have impressions but
limited data.

Step B1: Describe your experience.
  ACTION: Write 3 sentences about what happened when you
  tried RCI. Don't filter or polish. Just what happened.

Step B2: Check for the common new-user failure.
  ACTION: Re-read your RCI output.
  TEST: Count backward-facing statements vs. forward-facing.
  BACKWARD: "This was caused by..." / "The reason was..." /
            "What produced this was..."
  FORWARD: "This means..." / "Therefore I should..." /
           "The implication is..." / "This suggests..."
  RATIO: If >50% are forward → you were doing analysis, not
         RCI. The skill failed to activate correctly for you.
         → Go to Step B3.
  If >50% are backward → the activation worked.
         → Go to Step B4.

Step B3: Diagnose activation failure.
  ACTION: Which barrier did you hit?

  a) "I didn't understand what 'backward' means."
     → The skill's explanation is too abstract.
     IMPROVEMENT: Add a concrete example to the skill showing
     3 levels of backward tracing on a simple input. Make the
     backward direction viscerally clear.

  b) "I understood but kept slipping forward."
     → Need the mechanical direction test from A4a.

  c) "I understood but it felt pointless."
     → The skill doesn't sell its value upfront.
     IMPROVEMENT: Add a 2-sentence "why this works" before the
     principles. Something like: "Most reasoning starts from
     reactions and constructs forward — which means it inherits
     every assumption baked into the initial reaction. RCI goes
     backward to find those assumptions before they shape
     your conclusions."

Step B4: Assess depth and usefulness.
  ACTION: Did you reach anything you didn't already
  consciously know?
    → Yes: RCI worked for you. For improvements, go to
           Section A with more sessions under your belt.
    → No: Try one more session with this instruction added:
          "Every time you write an answer that feels obvious,
          mark it [OBVIOUS] and keep going past it. The
          non-obvious material is deeper."
          If still nothing after that: RCI may not be the
          right tool for your question. Try /araw instead.

→ SECTION B COMPLETE.


SECTION C: EVALUATING RCI FROM OUTSIDE
=======================================

You're assessing the skill without having used it yourself.

Step C1: Run the self-application test.
  ACTION: Apply RCI to the question "Should RCI be improved?"
  Trace backward:
  - Why am I asking this? → Because someone asked me to.
  - What caused that request? → They used RCI and want it better.
  - What caused the desire for "better"? → Something didn't work.
  - What didn't work? → [This is where you need data. If you
    don't have it, this evaluation can't proceed without it.]
  CHECK: Did you reach a concrete failure or gap?
    → Yes: That's your improvement target. Draft the fix.
    → No: You need usage data. Get 3 people to use RCI and
          report back. Then go to Section A.

Step C2: Run the redundancy test.
  ACTION: For each of RCI's 15 principles, write its CORE
  IDEA in 5 words or fewer.
  CHECK: Do any two principles have the same 5-word summary?
    → Yes: They should be merged. Draft the merger.
    → No: Principles are distinct. Move to C3.

Step C3: Run the distinctiveness test.
  ACTION: Compare RCI to /aex, /aw, /ar, /araw.
  Write ONE SENTENCE describing what RCI does that none
  of those do.
  CHECK: Is that sentence compelling?
    → Yes: Sharpen that distinction in the skill description.
    → No: RCI may need to be merged into another skill or
          given a clearer unique purpose.

Step C4: Run the teachability test.
  ACTION: Give the RCI skill text to someone unfamiliar with it.
  Ask them to apply it to: "I feel stuck in my career."
  Observe (or read their output).
  CHECK: Did they trace backward or drift forward?
    → Backward: The skill is teachable. Focus improvements
      on depth and output quality (Section A topics).
    → Forward: The skill has a teachability problem.
      Focus on concrete examples and direction testing.

→ SECTION C COMPLETE.
```

---

## Step 5: Failure Modes

| # | Failure Mode | How to Recognize | What to Do |
|---|-------------|------------------|------------|
| 1 | **Proceduralizing what should stay fluid** | You add numbered steps, checklists, or gates to the RCI process itself. RCI starts feeling like a form to fill out instead of a mode of thinking. | RCI's core must remain free-form. Improvements go in the *meta-layer* (the principles, the activation instructions, the failure detection) — NOT in the questioning process itself. If your improvement says "at step 3 of RCI, do X," you've gone wrong. |
| 2 | **Improving based on theory, not usage** | All your proposed improvements come from reading the skill text, not from watching it succeed or fail. | Without usage data, you're guessing. Run the skill 3 times on real problems before proposing changes. Bad theory-based improvements are worse than no changes. |
| 3 | **Adding principles that restate existing ones** | You add a 16th principle that, on close reading, is a restatement of principle 6 in different words. | Before adding anything, run the redundancy test (C2). If the new principle's 5-word summary matches an existing one, merge instead of adding. |
| 4 | **Destroying the productive contradiction** | RCI is a structured approach to unstructured reasoning. That tension is *generative*. You "resolve" it by making RCI fully structured (kills its power) or fully unstructured (kills its teachability). | Hold the tension. Don't resolve it. The principles provide structure. The execution provides freedom. Improvements should sharpen both sides, not collapse them into one. |
| 5 | **Optimizing for LLM execution at human expense** | You add mechanical tests and direction-checking that help LLMs stay on track but make the skill feel robotic to human users. | Separate the concerns. LLM-specific guardrails go in a "LLM execution notes" appendix. The core skill text targets human reasoning. |
| 6 | **Ignoring the output problem** | You improve the questioning process but ignore that users end up with a pile of questions and no synthesis. They stop using RCI because it "doesn't produce anything." | The output problem is RCI's biggest practical weakness. Address it (see A4d) even though it feels like it violates RCI's philosophy. A tool nobody uses because it has no output is worse than a tool with a pragmatic synthesis step. |
| 7 | **Treating all principles as equally important** | You give equal improvement attention to "Fixed Point Property" (intellectually interesting, rarely action-relevant) and "Reaction Recognition" (fundamental to every session working). | Prioritize by impact on session quality. The principles that affect activation and direction (Reaction Recognition, Causal Tracing, Self Interrogation) matter 10x more than the philosophical ones (Fixed Point, Native Derivation). |

---

## Step 6: Validation

Executability check:

- **A1-A2**: Concrete. "List sessions" and "mark outcomes" are mechanical. Pass.
- **A3**: Five categories with concrete descriptions. Each maps to a specific fix step. Pass.
- **A4a**: The "future tense / conditional / prescriptive" test is observable and mechanical. Pass.
- **A4b**: Three sub-causes, each with a concrete fix. The "brute fact vs. social fact" distinction could be ambiguous. **Note**: Examples help — "gravity is a brute fact; marriage is a social fact." Pass with note.
- **A4c**: The "same cause vs. same words" test requires some judgment. Acceptable for RCI's target audience (people already comfortable with abstract reasoning). Pass.
- **A4d**: Two clear options with a selection criterion. Pass.
- **A4e**: The "pre-known answer" detection is introspective. This is inherent to RCI — the skill targets people willing to introspect. Pass for the audience.
- **B1-B4**: All concrete. The backward/forward counting test in B2 is fully mechanical. Pass.
- **C1-C4**: All concrete. C1 requires actually running RCI, which is appropriate. Pass.
- **Dead ends**: All paths terminate at a concrete fix, a redirect to another section, or an explicit "use a different tool." Pass.
- **Loops**: A3→A4→fix→retest could loop, but each iteration addresses a specific failure. Not an infinite loop. Pass.

---

## QUICK REFERENCE CARD

**The 3 things most likely to improve RCI:**

1. **Add a mechanical direction test.** "Does this statement describe something that already happened, or something that would/should happen? Future/conditional/prescriptive = forward. Delete and rewrite backward." This catches the #1 failure mode.

2. **Add scope guidance.** "Trivial: 3-5 levels. Moderate: 7-12. Major: 15+." Without this, users either quit early or spiral forever.

3. **Solve the output problem.** Either add a post-RCI synthesis step (invoke `/ins`) or add single-sentence waypoints at chain terminations. Users need *something* to show for the work.

---

## COMMON MISTAKES

1. **Adding structure to the questioning itself.** Improve the setup, the principles, the failure detection. Leave the actual questioning free-form.
2. **Improving without data.** Use it 3+ times before changing it. Your theory of what's wrong is probably wrong.
3. **Adding principles instead of sharpening existing ones.** 15 principles is already a lot. Merge and sharpen before adding.
4. **Ignoring the new-user experience.** Skilled reasoners understand RCI from the description. Everyone else needs a concrete example of 3-5 levels of backward tracing.
5. **Treating LLM and human execution as identical.** They fail differently. LLMs simulate; humans drift. Different problems need different fixes.

---

## WHEN TO OVERRIDE THIS PROCEDURE

- **RCI should be deprecated, not improved.** If `/araw` or `/aw` fully subsumes RCI's capabilities, the right move is to merge RCI into those skills, not improve it as a standalone. Run the distinctiveness test (C3) honestly.
- **The improvement you need is philosophical, not structural.** If the issue is that RCI's core *premise* (backward causal tracing as foundational reasoning) is wrong, this procedure can't help. That requires a different kind of inquiry — possibly RCI itself applied to RCI.
- **You have a specific user population with specific failures.** If 80% of your users fail the same way, skip this procedure. Fix that one thing directly.

---

## WORKED EXAMPLES

### Example 1: An experienced user finds drift is the main problem

**A1**: 5 sessions listed. 2 worked, 1 partial, 2 failed.
**A2**: ✓✓~✗✗
**A3**: Both failures were DRIFT (a). Started backward, ended forward by the 4th level.
**A4a**: Add the direction test: "future tense / conditional / prescriptive = forward."
**Check**: Re-read the failed sessions. At level 3, statements shift to "This suggests I should..." — the test would have caught it.
**Result**: Add one paragraph to the skill about the direction test.

### Example 2: A new user can't get started

**B1**: "I read it three times. I understand the philosophy. When I tried to apply it to 'should I change jobs,' I immediately started listing pros and cons."
**B2**: Count — 80% forward-facing statements.
**B3**: Barrier (a) — understood conceptually but not operationally.
**Improvement**: Add a worked example to the skill:
```
Input: "I want to change jobs."
Level 1: What caused this want? → I'm unhappy at work.
Level 2: What caused the unhappiness? → My work doesn't feel meaningful.
Level 3: What caused "meaningful" to be the criterion? → I once had meaningful work and noticed the difference.
Level 4: What caused that earlier work to feel meaningful? → I was solving problems that affected real people directly.
Level 5: What caused me to stop doing that? → I got promoted into management.
```
This example makes "backward" viscerally concrete.

### Example 3: Evaluator finds principle redundancy

**C2**: 5-word summaries for all 15 principles:
- Reaction Recognition: "Everything is a reaction"
- Self Interrogation: "Question your own statements"
- Question The Question: "Question your own questions"
- Gap Awareness: "Notice unquestioned statements"
- No Lazy Stops: "Question your stopping impulse"

These 4 principles (Self Interrogation, Question The Question, Gap Awareness, No Lazy Stops) all say variants of "question your own process." **Merge** into one principle: "Meta-Interrogation: Every output of this process — statements, questions, decisions to stop, decisions to continue — is itself a reaction. Apply the same backward tracing to your own process."

Result: 15 principles → 12, with sharper distinctions.

---

*Validation status: This procedure has not been validated by domain experts or against actual RCI improvement outcomes. It is derived from structural analysis of the RCI skill, common reasoning failure modes, and meta-procedural design patterns.*

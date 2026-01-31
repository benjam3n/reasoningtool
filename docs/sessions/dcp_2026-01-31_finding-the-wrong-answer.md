# DCP — Finding the Wrong Answer

**Date**: 2026-01-31
**Input**: how to find the wrong answer

---

# FINDING THE WRONG ANSWER — Decision Procedure

## Step 1: Decision Dimensions (`/dd`)

What dimensions determine whether an answer is wrong?

| # | Dimension | Description | Why It Matters |
|---|-----------|-------------|----------------|
| 1 | **Answer Source** | Where did the answer come from? (your reasoning, someone else's claim, a calculation, intuition, a tool) | Different sources have different failure modes |
| 2 | **Confidence Level** | How certain does the answerer feel? | High confidence + wrong = most dangerous; low confidence is a useful signal |
| 3 | **Testability** | Can the answer be checked against reality? | Untestable answers can hide wrongness indefinitely |
| 4 | **Reversibility** | What happens if you act on a wrong answer? | Irreversible consequences demand more checking |
| 5 | **Consensus** | Do independent sources agree or disagree? | Disagreement is a wrongness signal; unanimous agreement can be groupthink |
| 6 | **Assumption Count** | How many unstated premises does the answer rest on? | More assumptions = more failure points |
| 7 | **Reasoning Chain Length** | How many inferential steps from evidence to conclusion? | Longer chains compound error at each step |
| 8 | **Selection Bias Exposure** | Was the answer found by looking for confirmation or by trying to disprove? | Confirmation-seeking dramatically inflates false positive rate |
| 9 | **Domain Familiarity** | How well does the answerer know this domain? | Novices misidentify what matters; experts have blind spots |
| 10 | **Question Clarity** | Was the original question unambiguous? | Wrong questions produce "correct" answers to the wrong problem |
| 11 | **Base Rate** | How often are answers of this type actually correct? | Rare events are overdiagnosed; common events are under-examined |
| 12 | **Emotional Stake** | Does the answerer want a particular answer to be true? | Motivated reasoning is the #1 source of wrong answers |

---

## Step 2: Options per Dimension (`/se`)

| Dimension | Possible States |
|-----------|----------------|
| **Answer Source** | Self-derived reasoning / Expert authority / Calculation/data / Intuition-gut / Tool-generated / Crowd consensus |
| **Confidence Level** | Very high (>95%) / High (75-95%) / Medium (50-75%) / Low (<50%) |
| **Testability** | Directly testable now / Testable with effort / Testable in future only / Not testable |
| **Reversibility** | Fully reversible / Partially reversible / Irreversible |
| **Consensus** | Strong agreement / Mixed views / Strong disagreement / No one else has checked |
| **Assumption Count** | 0-1 (grounded) / 2-4 (moderate) / 5+ (assumption-heavy) |
| **Chain Length** | 1 step (direct observation) / 2-3 steps / 4-6 steps / 7+ steps |
| **Selection Bias** | Actively tried to disprove / Neutral search / Searched for support / Only looked at confirming evidence |
| **Domain Familiarity** | Deep expert / Working knowledge / Some exposure / Complete novice |
| **Question Clarity** | Precise and unambiguous / Mostly clear / Vague / Actually multiple questions |
| **Base Rate** | Common (>50% of answers like this are right) / Moderate / Rare (<10%) / Unknown |
| **Emotional Stake** | No preference / Mild preference / Strong preference / Identity-level attachment |

**Key interactions**:
- High confidence + Strong emotional stake = highest wrongness risk
- Long chain + Novice domain = compounding errors likely
- Only confirming evidence + High confidence = classic trap

---

## Step 3: Hidden Assumptions (`/aex`)

What do people implicitly assume when checking their answers?

| # | Hidden Assumption | Why It's Dangerous |
|---|-------------------|--------------------|
| 1 | **"If my reasoning feels solid, it probably is"** | Feeling-of-rightness is uncorrelated with actual correctness for non-trivial problems |
| 2 | **"I would notice if I were wrong"** | Most wrong answers feel identical to right answers from the inside |
| 3 | **"Checking means re-reading my work"** | Re-reading activates the same mental model that produced the error; you'll skip over the same gap |
| 4 | **"Smart people make fewer errors"** | Smart people make *different* errors — more elaborate justifications for wrong conclusions |
| 5 | **"If no one objects, it's probably right"** | Absence of objection ≠ correctness; others may not have checked, or may have the same blind spot |
| 6 | **"The question is what I think it is"** | Many wrong answers are correct answers to a different question than was actually asked |
| 7 | **"My information is complete"** | The most dangerous wrong answers come from missing information you don't know is missing |
| 8 | **"More time checking = more likely correct"** | Diminishing returns; 10 minutes of the right check > 10 hours of the wrong check |
| 9 | **"One strong piece of evidence is enough"** | Single-evidence answers are brittle; the evidence might be misleading or misinterpreted |
| 10 | **"If the method is correct, the answer is correct"** | Correct method + wrong inputs = wrong answer. Correct method + wrong scope = wrong answer |

---

## Step 4: The Procedure (`/stg`)

```
FINDING THE WRONG ANSWER — PROCEDURE
=====================================

PURPOSE: Given any answer you've arrived at, this procedure
tells you whether it's likely wrong BEFORE you act on it.

STEP 0: What type of answer are you checking?
┌──────────────────────────┬───────────────┐
│ Type                     │ Go to         │
├──────────────────────────┼───────────────┤
│ Factual claim            │ SECTION A     │
│ ("X is true")            │               │
├──────────────────────────┼───────────────┤
│ Causal claim             │ SECTION B     │
│ ("X causes Y")           │               │
├──────────────────────────┼───────────────┤
│ Decision/recommendation  │ SECTION C     │
│ ("You should do X")      │               │
├──────────────────────────┼───────────────┤
│ Prediction               │ SECTION D     │
│ ("X will happen")        │               │
├──────────────────────────┼───────────────┤
│ Not sure which type      │ SECTION E     │
└──────────────────────────┴───────────────┘


═══════════════════════════════════════════
SECTION A: Checking a Factual Claim
═══════════════════════════════════════════

Step A1: Write the claim as one sentence.
  → What you should see: A clear statement like
    "The boiling point of water at sea level is 100°C"

Step A2: Can you look this up in a reference source
         independent from where you first got it?
  → YES: Look it up. Does it match?
    → YES: Go to A5.
    → NO:  The answer is LIKELY WRONG. Stop. Investigate
           the discrepancy.
  → NO:  Go to A3.

Step A3: How did you arrive at this claim?
  (a) Someone told me → Go to A4
  (b) I calculated/derived it → Go to A6
  (c) I remember it → ⚠ WARNING: Memory is unreliable.
      Treat as UNCERTAIN. Try to find a source. If you
      can't, label this "unverified" and proceed with
      caution.
  (d) It's obvious/common sense → ⚠ DANGER ZONE.
      "Obvious" claims have the highest wrongness rate
      because no one checks them. Go to A6.

Step A4: Source credibility check.
  → Does this person have demonstrated expertise in
    this specific area? (Not "smart in general" —
    specifically this.)
    → YES: Does any other expert disagree?
      → YES: Answer is UNCERTAIN. Do not treat as settled.
      → NO:  Probably correct, but label "single source."
    → NO: Treat as UNCERTAIN. Find a better source.

Step A5: The claim has survived basic checking.
  → Final check: Do you WANT this to be true?
    → YES: Apply extra skepticism. Look for ONE piece
           of evidence that would disprove it. If you
           can't find one, and you genuinely tried,
           accept tentatively.
    → NO:  Accept.

Step A6: Derivation check.
  → Write out every step of your reasoning. Number them.
  → For EACH step, ask: "What would make this step
     wrong?" Write down the answer.
  → Now check: Did any step assume something you haven't
     verified? If yes, verify it. If you can't verify it,
     the answer is UNCERTAIN.
  → Does the final answer seem surprisingly convenient,
     clean, or aligned with what you expected?
    → YES: This is a wrongness signal. Redo the
           derivation from scratch without looking
           at your first attempt.
    → NO: Probably correct. Accept tentatively.


═══════════════════════════════════════════
SECTION B: Checking a Causal Claim
═══════════════════════════════════════════

Step B1: Write the claim as "X causes Y."

Step B2: Can you name at least TWO other things
         that also cause Y (besides X)?
  → YES: Good. Go to B3.
  → NO:  ⚠ WARNING: You may have tunnel vision.
         Brainstorm 3 alternative causes before
         proceeding. If you truly can't, go to B3.

Step B3: Is there evidence that X happened BEFORE Y?
  → YES: Go to B4.
  → NO:  The causal direction may be reversed, or both
         may be caused by something else. Answer is
         LIKELY WRONG as stated. Rewrite the claim.

Step B4: When X is ABSENT, does Y still happen sometimes?
  → YES: X is not the sole cause. Your claim is
         OVERSTATED at minimum. Rewrite as "X
         contributes to Y" or "X increases the
         probability of Y."
  → NO:  Stronger causal evidence. Go to B5.

Step B5: Is there a plausible MECHANISM connecting X to Y?
  (Not just correlation, but a story of HOW X leads to Y)
  → YES, and it's specific: Claim is PROBABLY CORRECT.
  → YES, but it's vague ("somehow"): Claim is UNCERTAIN.
  → NO: Claim is LIKELY WRONG. Correlation ≠ causation.

Step B6: Motivation check — same as A5.


═══════════════════════════════════════════
SECTION C: Checking a Decision/Recommendation
═══════════════════════════════════════════

Step C1: Write the recommendation as "Do X because Y."

Step C2: What happens if you do NOTHING?
  → Write it down concretely.
  → Is doing nothing actually fine?
    → YES: The recommendation may be unnecessary.
           Reconsider whether you need to act at all.
    → NO: Go to C3.

Step C3: Name TWO alternatives to X that could also
         address Y.
  → Can you?
    → YES: For each alternative, is it clearly worse
           than X? Write down WHY for each.
      → All clearly worse: Go to C4.
      → Some are comparable: Your original recommendation
        is UNCERTAIN. You have a comparison problem,
        not an answer. Evaluate the alternatives properly.
    → NO: ⚠ WARNING. If you can only think of one
          option, you haven't searched hard enough.
          You are probably anchored. Generate alternatives
          before proceeding.

Step C4: What's the WORST CASE if X fails?
  → Write it down.
  → Can you tolerate the worst case?
    → YES: Recommendation is reasonable. Go to C5.
    → NO: Recommendation is RISKY regardless of
          expected outcome. Look for a safer alternative.

Step C5: Who would DISAGREE with this recommendation,
         and what would they say?
  → Write down the strongest counterargument.
  → Does the counterargument reveal something you
     missed?
    → YES: Revise the recommendation.
    → NO: Accept tentatively.


═══════════════════════════════════════════
SECTION D: Checking a Prediction
═══════════════════════════════════════════

Step D1: Write the prediction as "X will happen
         [by when / under what conditions]."
  → If you can't specify WHEN or UNDER WHAT CONDITIONS,
    your prediction is too vague to be wrong — which
    means it's useless. Make it specific first.

Step D2: How often do predictions of this type
         come true? (The base rate.)
  → I know the base rate: __%
    → Is your predicted probability close to the base
      rate?
      → YES: Prediction is probably just the base rate
             dressed up. That's fine, but don't pretend
             you have special insight.
      → NO (your prediction is higher or lower): What
          SPECIFIC EVIDENCE justifies deviating from
          the base rate? Write it down.
        → Evidence is strong and specific: Go to D3.
        → Evidence is weak or general: Your prediction
          is LIKELY WRONG. Return to the base rate.
  → I don't know the base rate: ⚠ DANGER. You are
    probably overconfident. Estimate the base rate
    before proceeding. If you can't even estimate it,
    your prediction is UNRELIABLE.

Step D3: If your prediction is wrong, what would you
         expect to see FIRST?
  → Write down 2-3 early warning signs.
  → Are any of these signs already present?
    → YES: Prediction is LIKELY WRONG.
    → NO: Prediction survives. Monitor for these signs.

Step D4: Motivation check — same as A5.


═══════════════════════════════════════════
SECTION E: Not Sure What Type of Answer
═══════════════════════════════════════════

Step E1: Rewrite your answer as a single sentence.

Step E2: Does it contain:
  → "is/are/was/were" (a state of the world) → SECTION A
  → "causes/leads to/results in" → SECTION B
  → "should/must/best/recommended" → SECTION C
  → "will/expect/predict/likely" → SECTION D
  → Multiple of the above → Break into separate claims
    and check each one independently.
```

---

## Step 5: Failure Modes (`/fla`)

| # | Failure Mode | How to Recognize It | What to Do Instead |
|---|-------------|--------------------|--------------------|
| 1 | **"I already know it's right"** — skipping the procedure because you feel confident | You catch yourself thinking "this is obvious, I don't need to check" | That feeling IS the trigger to check. Obvious-feeling answers have the highest uncaught error rate. Run the procedure anyway. |
| 2 | **Motivated search** — doing the checks but unconsciously steering toward confirmation | You notice every check "passes" easily and quickly | If every check passes in under 10 seconds, you're probably rubber-stamping. Slow down. For each check, spend at least 30 seconds genuinely trying to fail it. |
| 3 | **Wrong section** — misclassifying the answer type | Your answer doesn't fit neatly into the section's steps | Go to Section E. Break the answer into components. Many "decisions" contain hidden factual claims that need Section A checking first. |
| 4 | **Stopping at "uncertain"** — the procedure says uncertain and you don't know what to do | You reach an UNCERTAIN verdict and feel stuck | UNCERTAIN means: do not act as if the answer is correct. Either (a) gather more information to resolve the uncertainty, or (b) make a plan that works even if the answer is wrong. |
| 5 | **Checking the wrong thing** — the answer is technically correct but to the wrong question | You complete the procedure, the answer passes, but something still feels off | Go back to Step 0. Re-read the ORIGINAL question. Does your answer actually address what was asked? Rewrite both the question and answer side by side. |
| 6 | **Social override** — someone important/confident says it's right, so you skip checking | You notice you're deferring to a person rather than to evidence | Authority is not evidence. Ask: "If a random stranger said this, would I still believe it?" If not, run the procedure. |

---

## Step 6: Validation Check (`/pv`)

Validation sweep of each step:

- **All steps use concrete actions** (write, look up, name, count) — not "consider" or "think about." PASS.
- **All decision points are binary or explicit multiple choice.** PASS.
- **No jargon without inline definition.** PASS. (Base rate is defined in context at D2.)
- **Every path terminates** — no dead ends or infinite loops. PASS.
- **A novice could execute each step** — no step requires domain expertise. PASS.
- **Motivation check (A5) is reused correctly** across sections. PASS.

One fix applied: Section E originally said "classify intuitively" — replaced with explicit keyword matching (E2).

---

## QUICK REFERENCE CARDS

**The 3 Strongest Wrongness Signals:**
1. You WANT the answer to be true
2. It feels obvious and you haven't checked
3. You can't name an alternative

**The 30-Second Version:**
1. Write the answer as one sentence
2. Try to name what would DISPROVE it
3. If you can't think of anything that would disprove it, you haven't understood it well enough — the answer is unreliable

**The One Question That Catches the Most Errors:**
> "What would I expect to see if this answer were WRONG?"
> If you can't answer this, you don't understand the answer well enough to know if it's right.

---

## COMMON MISTAKES

1. **Checking by re-reading** — You re-read your work and it looks right. This catches typos, not logical errors. You must check by *attacking*, not by re-reading.
2. **Asking someone who will agree** — Checking with people who share your assumptions doesn't check your assumptions.
3. **Treating "I can't find a problem" as "there is no problem"** — Absence of evidence is not evidence of absence. "I checked and it seems fine" is weaker than people think.
4. **Anchoring on the first answer** — Once you have an answer, alternatives feel wrong by comparison. Generate alternatives BEFORE evaluating them against your answer.
5. **Confusing precision with accuracy** — A very specific, detailed answer can still be completely wrong. Detail is not evidence of correctness.

---

## WHEN TO OVERRIDE THIS PROCEDURE

- **Time-critical emergencies** — If acting on a possibly-wrong answer is better than not acting at all, act. Check afterward.
- **Trivial stakes** — If being wrong costs nothing, don't spend time checking. The procedure is for decisions that matter.
- **Expert intuition in a domain with fast feedback** — If you're an expert who has made this exact type of judgment thousands of times and gotten quick feedback each time (e.g., a chess position, a medical symptom pattern), your intuition may outperform the procedure.
- **The answer has already been checked by independent parties using different methods** — Redundant checking has diminishing returns.

---

## WORKED EXAMPLES

### Example 1: "Remote work is more productive than office work"

**Section A (Factual Claim)**
- A1: "Remote workers are more productive than office workers."
- A2: Can I look this up? Yes — research exists.
  - Results: Mixed. Some studies say yes, some say no, depends on the type of work.
  - Verdict: **Claim as stated is WRONG** (overgeneralized). A more correct version: "Remote work increases productivity for focused individual tasks and decreases it for collaborative tasks, with large individual variation."

### Example 2: "We should rewrite the backend in Rust"

**Section C (Recommendation)**
- C1: "Rewrite the backend in Rust because it will be faster."
- C2: What if we do nothing? Current backend works. Response times are 200ms. Users aren't complaining. Doing nothing is *fine*.
  - Verdict: Recommendation may be **unnecessary**.
- C3: Alternatives: (a) Profile and optimize hot paths in current language, (b) Add caching layer.
  - Both are clearly less effort. Neither is clearly worse for the stated goal.
  - Verdict: Recommendation is **UNCERTAIN** — cheaper alternatives exist that weren't considered.

### Example 3: "This stock will go up 30% this year"

**Section D (Prediction)**
- D1: "Stock X will increase 30% by December 2026."
- D2: Base rate — average stock returns ~10%/year. 30% is 3x the base rate. What specific evidence? "The company has a new product."
  - Many companies have new products. Most don't return 30%. Evidence is **weak and general**.
  - Verdict: Prediction is **LIKELY WRONG**. Return closer to base rate.

---

*Validation status: This procedure has not been validated by domain experts. It synthesizes principles from epistemology, decision science, and cognitive bias research.*

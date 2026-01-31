---
name: "fwa - Find Wrong Answer"
description: "Check whether an answer is likely wrong before acting on it. Classifies answer type and runs targeted verification."
---

# Find Wrong Answer

**Input**: $ARGUMENTS

---

## Purpose

Given any answer you've arrived at, this procedure tells you whether it's likely wrong BEFORE you act on it.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/fwa 4x [claim]").

| Depth | Min Checks | Min Alternatives | Min Sources | Min Stress Tests |
|-------|-----------|-----------------|-------------|-----------------|
| 1x    | 3         | 1               | 1           | 1               |
| 2x    | 5         | 2               | 2           | 2               |
| 4x    | 8         | 4               | 3           | 4               |
| 8x    | 12        | 6               | 5           | 6               |
| 16x   | 18        | 10              | 8           | 10              |

These are floors. Go deeper where insight is dense. Compress where it's not.

---

## Step 0: What type of answer are you checking?

| Type | Go to |
|------|-------|
| Factual claim ("X is true") | SECTION A |
| Causal claim ("X causes Y") | SECTION B |
| Decision/recommendation ("You should do X") | SECTION C |
| Prediction ("X will happen") | SECTION D |
| Not sure which type | SECTION E |

---

## SECTION A: Checking a Factual Claim

**Step A1**: Write the claim as one sentence.
You should see: A clear statement like "The boiling point of water at sea level is 100C"

**Step A2**: Can you look this up in a reference source independent from where you first got it?
- YES: Look it up. Does it match?
  - YES: Go to A5.
  - NO: The answer is LIKELY WRONG. Stop. Investigate the discrepancy.
- NO: Go to A3.

**Step A3**: How did you arrive at this claim?
- (a) Someone told me -- Go to A4
- (b) I calculated/derived it -- Go to A6
- (c) I remember it -- WARNING: Memory is unreliable. Treat as UNCERTAIN. Try to find a source. If you can't, label this "unverified" and proceed with caution.
- (d) It's obvious/common sense -- DANGER ZONE. "Obvious" claims have the highest wrongness rate because no one checks them. Go to A6.

**Step A4**: Source credibility check.
Does this person have demonstrated expertise in this specific area? (Not "smart in general" -- specifically this.)
- YES: Does any other expert disagree?
  - YES: Answer is UNCERTAIN. Do not treat as settled.
  - NO: Probably correct, but label "single source."
- NO: Treat as UNCERTAIN. Find a better source.

**Step A5**: The claim has survived basic checking.
Final check: Do you WANT this to be true?
- YES: Apply extra skepticism. Look for ONE piece of evidence that would disprove it. If you can't find one, and you genuinely tried, accept tentatively.
- NO: Accept.

**Step A6**: Derivation check.
1. Write out every step of your reasoning. Number them.
2. For EACH step, ask: "What would make this step wrong?" Write down the answer.
3. Now check: Did any step assume something you haven't verified? If yes, verify it. If you can't verify it, the answer is UNCERTAIN.
4. Does the final answer seem surprisingly convenient, clean, or aligned with what you expected?
   - YES: This is a wrongness signal. Redo the derivation from scratch without looking at your first attempt.
   - NO: Probably correct. Accept tentatively.

---

## SECTION B: Checking a Causal Claim

**Step B1**: Write the claim as "X causes Y."

**Step B2**: Can you name at least TWO other things that also cause Y (besides X)?
- YES: Good. Go to B3.
- NO: WARNING: You may have tunnel vision. Brainstorm 3 alternative causes before proceeding. If you truly can't, go to B3.

**Step B3**: Is there evidence that X happened BEFORE Y?
- YES: Go to B4.
- NO: The causal direction may be reversed, or both may be caused by something else. Answer is LIKELY WRONG as stated. Rewrite the claim.

**Step B4**: When X is ABSENT, does Y still happen sometimes?
- YES: X is not the sole cause. Your claim is OVERSTATED at minimum. Rewrite as "X contributes to Y" or "X increases the probability of Y."
- NO: Stronger causal evidence. Go to B5.

**Step B5**: Is there a plausible MECHANISM connecting X to Y? (Not just correlation, but a story of HOW X leads to Y)
- YES, and it's specific: Claim is PROBABLY CORRECT.
- YES, but it's vague ("somehow"): Claim is UNCERTAIN.
- NO: Claim is LIKELY WRONG. Correlation does not equal causation.

**Step B6**: Motivation check -- same as A5.

---

## SECTION C: Checking a Decision/Recommendation

**Step C1**: Write the recommendation as "Do X because Y."

**Step C2**: What happens if you do NOTHING?
Write it down concretely. Is doing nothing actually fine?
- YES: The recommendation may be unnecessary. Reconsider whether you need to act at all.
- NO: Go to C3.

**Step C3**: Name TWO alternatives to X that could also address Y.
- Can you?
  - YES: For each alternative, is it clearly worse than X? Write down WHY for each.
    - All clearly worse: Go to C4.
    - Some are comparable: Your original recommendation is UNCERTAIN. You have a comparison problem, not an answer. Evaluate the alternatives properly.
  - NO: WARNING. If you can only think of one option, you haven't searched hard enough. You are probably anchored. Generate alternatives before proceeding.

**Step C4**: What's the WORST CASE if X fails?
Write it down. Can you tolerate the worst case?
- YES: Recommendation is reasonable. Go to C5.
- NO: Recommendation is RISKY regardless of expected outcome. Look for a safer alternative.

**Step C5**: Who would DISAGREE with this recommendation, and what would they say?
Write down the strongest counterargument. Does the counterargument reveal something you missed?
- YES: Revise the recommendation.
- NO: Accept tentatively.

---

## SECTION D: Checking a Prediction

**Step D1**: Write the prediction as "X will happen [by when / under what conditions]."
If you can't specify WHEN or UNDER WHAT CONDITIONS, your prediction is too vague to be wrong -- which means it's useless. Make it specific first.

**Step D2**: How often do predictions of this type come true? (The base rate.)
- I know the base rate: __%
  - Is your predicted probability close to the base rate?
    - YES: Prediction is probably just the base rate dressed up. That's fine, but don't pretend you have special insight.
    - NO (your prediction is higher or lower): What SPECIFIC EVIDENCE justifies deviating from the base rate? Write it down.
      - Evidence is strong and specific: Go to D3.
      - Evidence is weak or general: Your prediction is LIKELY WRONG. Return to the base rate.
- I don't know the base rate: DANGER. You are probably overconfident. Estimate the base rate before proceeding. If you can't even estimate it, your prediction is UNRELIABLE.

**Step D3**: If your prediction is wrong, what would you expect to see FIRST?
Write down 2-3 early warning signs. Are any of these signs already present?
- YES: Prediction is LIKELY WRONG.
- NO: Prediction survives. Monitor for these signs.

**Step D4**: Motivation check -- same as A5.

---

## SECTION E: Not Sure What Type of Answer

**Step E1**: Rewrite your answer as a single sentence.

**Step E2**: Does it contain:
- "is/are/was/were" (a state of the world) -- Go to SECTION A
- "causes/leads to/results in" -- Go to SECTION B
- "should/must/best/recommended" -- Go to SECTION C
- "will/expect/predict/likely" -- Go to SECTION D
- Multiple of the above -- Break into separate claims and check each one independently.

---

## Quick Reference Cards

**The 3 Strongest Wrongness Signals:**
1. You WANT the answer to be true
2. It feels obvious and you haven't checked
3. You can't name an alternative

**The 30-Second Version:**
1. Write the answer as one sentence
2. Try to name what would DISPROVE it
3. If you can't think of anything that would disprove it, you haven't understood it well enough -- the answer is unreliable

**The One Question That Catches the Most Errors:**
> "What would I expect to see if this answer were WRONG?"
> If you can't answer this, you don't understand the answer well enough to know if it's right.

---

## Common Mistakes

1. **Checking by re-reading** -- You re-read your work and it looks right. This catches typos, not logical errors. You must check by *attacking*, not by re-reading.
2. **Asking someone who will agree** -- Checking with people who share your assumptions doesn't check your assumptions.
3. **Treating "I can't find a problem" as "there is no problem"** -- Absence of evidence is not evidence of absence. "I checked and it seems fine" is weaker than people think.
4. **Anchoring on the first answer** -- Once you have an answer, alternatives feel wrong by comparison. Generate alternatives BEFORE evaluating them against your answer.
5. **Confusing precision with accuracy** -- A very specific, detailed answer can still be completely wrong. Detail is not evidence of correctness.

---

## When to Override This Procedure

- **Time-critical emergencies** -- If acting on a possibly-wrong answer is better than not acting at all, act. Check afterward.
- **Trivial stakes** -- If being wrong costs nothing, don't spend time checking. The procedure is for decisions that matter.
- **Expert intuition in a domain with fast feedback** -- If you're an expert who has made this exact type of judgment thousands of times and gotten quick feedback each time (e.g., a chess position, a medical symptom pattern), your intuition may outperform the procedure.
- **The answer has already been checked by independent parties using different methods** -- Redundant checking has diminishing returns.

---

## Worked Examples

### Example 1: "Remote work is more productive than office work"

**Section A (Factual Claim)**
- A1: "Remote workers are more productive than office workers."
- A2: Can I look this up? Yes -- research exists.
  - Results: Mixed. Some studies say yes, some say no, depends on the type of work.
  - Verdict: **Claim as stated is WRONG** (overgeneralized). A more correct version: "Remote work increases productivity for focused individual tasks and decreases it for collaborative tasks, with large individual variation."

### Example 2: "We should rewrite the backend in Rust"

**Section C (Recommendation)**
- C1: "Rewrite the backend in Rust because it will be faster."
- C2: What if we do nothing? Current backend works. Response times are 200ms. Users aren't complaining. Doing nothing is *fine*.
  - Verdict: Recommendation may be **unnecessary**.
- C3: Alternatives: (a) Profile and optimize hot paths in current language, (b) Add caching layer.
  - Both are clearly less effort. Neither is clearly worse for the stated goal.
  - Verdict: Recommendation is **UNCERTAIN** -- cheaper alternatives exist that weren't considered.

### Example 3: "This stock will go up 30% this year"

**Section D (Prediction)**
- D1: "Stock X will increase 30% by December 2026."
- D2: Base rate -- average stock returns ~10%/year. 30% is 3x the base rate. What specific evidence? "The company has a new product."
  - Many companies have new products. Most don't return 30%. Evidence is **weak and general**.
  - Verdict: Prediction is **LIKELY WRONG**. Return closer to base rate.

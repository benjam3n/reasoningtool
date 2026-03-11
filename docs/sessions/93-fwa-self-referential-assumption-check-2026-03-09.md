# /fwa Check the /fwa skill for flawed assumptions in its own design
**Date:** 2026-03-09
**Skill:** /fwa (Flawed Assumptions)

---

## Step 0: What type of answer are we checking?

The /fwa skill embeds multiple answer types in its own design:

| Embedded claim | Type | Section |
|---|---|---|
| "This procedure can reliably detect wrong answers before you act on them" | Factual + Causal | A, B |
| "Categorizing answers into four types (factual, causal, decision, prediction) is the right taxonomy" | Factual | A |
| "Following these steps will reduce error rates" | Causal | B |
| "You should use this procedure when you have an answer to check" | Decision/Recommendation | C |
| "Users who follow this will catch errors they'd otherwise miss" | Prediction | D |

I'll check each independently, as Section E instructs for compound answers.

---

## SECTION A: Checking Factual Claims in the Design

### Claim A-1: "Answers can be usefully categorized into four types: factual, causal, decision, prediction"

**A1 — Statement:** "All answers worth checking fall into one of four categories: factual claims, causal claims, decisions/recommendations, or predictions."

**A2 — Can I look this up?** Partially. Epistemology and argumentation theory have multiple taxonomies. Toulmin's model uses claims, grounds, warrants, backing, qualifiers, rebuttals — a six-part structure. Walton's argumentation schemes identify 60+ types. The four-type taxonomy is a simplification.

**A3 — How did /fwa arrive at this?** It appears to be a derived/designed taxonomy (option b — calculated/derived).

**A6 — Derivation check:**
1. Step: "Answers" are things people believe and might act on.
2. Step: These can be about what IS (factual), what CAUSES what (causal), what to DO (decision), or what WILL happen (prediction).
3. Step: These four cover the space.

**What would make each step wrong?**
- Step 2: There are answer types that don't fit cleanly. Examples:
  - **Moral/ethical judgments** ("It's wrong to lie") — not purely factual, causal, decisional, or predictive. /fwa would route this to Section A (factual claim), but moral claims require different verification methods than empirical facts. You can't "look them up."
  - **Definitions and category assignments** ("This counts as fraud") — these are conceptual, not empirical. The verification procedure for "is X true?" doesn't apply to "does X fall under category Y?"
  - **Explanations** ("The reason this happened is...") — overlaps with causal but isn't identical. An explanation can be wrong without the causal mechanism being wrong (e.g., right cause, wrong emphasis).
  - **Interpretations** ("What this data means is...") — hermeneutic claims that aren't directly verifiable by the factual-claim procedure.
- Step 3: The claim that these four "cover the space" is exactly the kind of claim A3(d) warns about — it feels "obvious" and is therefore in the DANGER ZONE of highest wrongness rate.

**Verdict: UNCERTAIN.** The taxonomy works for the most common cases but has gaps. The skill doesn't acknowledge these gaps or provide fallback handling when an answer doesn't fit neatly.

---

### Claim A-2: "Memory is unreliable" (Step A3c)

**A1 — Statement:** "Memory is unreliable as a source for factual claims."

**A2 — Can I look this up?** Yes. Extensive psychological research (Loftus, Schacter, Roediger) confirms memory is reconstructive and error-prone.

**A5 — Do I want this to be true?** No particular motivation.

**But there's a nuance the skill misses:** Memory reliability varies enormously by domain. An experienced chess player's memory of board positions is highly reliable. A doctor's memory of drug interactions they use daily is reliable. The blanket "memory is unreliable" is overstated. The skill should say "memory is unreliable *for facts outside your area of repeated practice*."

**Verdict: CORRECT in direction, OVERSTATED in degree.**

---

### Claim A-3: "'Obvious' claims have the highest wrongness rate because no one checks them" (Step A3d)

**A1 — Statement:** "Claims that feel obvious have the highest wrongness rate because no one checks them."

**A2 — Can I look this up?** Partially. There's research on cognitive ease (Kahneman) and the "Moses illusion" showing people fail to catch errors in statements that feel fluent. However, "highest wrongness rate" is a specific quantitative claim.

**A6 — Derivation check:** The logic is: unchecked claims accumulate errors; "obvious" claims are the least checked; therefore they have the most errors. But this reasoning has a flaw — truly obvious claims (2+2=4, the sun rises in the east) are overwhelmingly correct. The wrongness rate of "obvious" claims is actually bimodal: most are right (because they're genuinely obvious), but the ones that are wrong are catastrophically wrong (because no one catches them). The skill conflates "dangerous when wrong" with "frequently wrong."

**Verdict: OVERSTATED.** The insight is real but the claim as written is misleading. A more accurate version: "Claims that feel obvious are the most dangerous to leave unchecked, because errors in them go undetected the longest."

---

### Claim A-4: "Absence of evidence is not evidence of absence" (Common Mistakes #3)

**A1 — Statement:** "Not finding a problem does not mean there is no problem."

**A2 — Can I look this up?** Yes, and this is actually a contested claim in epistemology and Bayesian reasoning. In Bayesian terms, absence of evidence *is* (weak) evidence of absence, when you've looked in the right places. If you search thoroughly for a flaw and can't find one, that genuinely should update your confidence.

**Verdict: OVERSTATED.** The skill states this as absolute when it's actually a matter of degree. A more correct version: "Not finding a problem is weaker evidence than people typically assume, but it's not zero evidence. The strength depends on how thoroughly and how competently you searched."

---

## SECTION B: Checking Causal Claims in the Design

### Claim B-1: "Following this procedure causes you to catch errors"

**B1:** "Following the /fwa procedure causes users to catch errors they would otherwise miss."

**B2 — Two other things that also cause error-catching?**
1. Having a knowledgeable colleague review your work.
2. Waiting 24 hours and re-examining with fresh eyes.
3. Trying to explain your answer to someone unfamiliar with it.

Yes, alternatives exist. Good.

**B3 — Does the procedure happen BEFORE the error-catching?** Yes, by design.

**B4 — When the procedure is ABSENT, do people still catch errors?** YES. People catch errors through intuition, peer review, reality contact, and simple re-checking all the time. This means the procedure is not the sole cause of error-catching. The claim should be: "The procedure *increases the probability* of catching errors."

**B5 — Is there a plausible mechanism?** Yes, and it's specific: the procedure forces you to (a) classify your claim type, (b) generate alternatives, (c) check motivations, and (d) look for disconfirming evidence. Each of these is a known debiasing technique from decision science literature.

**B6 — Motivation check:** Do I want this to be true? This is a self-referential trap. The /fwa procedure wants to believe it works — and it's checking itself. This is exactly the kind of motivated reasoning the procedure warns about. Applying extra skepticism:

**What evidence would disprove it?** If users followed the procedure and still made the same errors at the same rate, the procedure doesn't work. The skill provides no mechanism for tracking this. There are no feedback loops, no calibration checks, no way to measure whether the procedure actually improves outcomes vs. simply making people feel more confident in their existing answers.

**Verdict: UNCERTAIN.** The mechanism is plausible and grounded in real decision science, but the skill has no way to verify its own effectiveness — which is, ironically, exactly the kind of unchecked assumption it warns against.

---

### Claim B-2: "Re-reading catches typos, not logical errors" (Common Mistakes #1)

**B1:** "Re-reading your own work causes you to catch typos but not logical errors."

**B3-B5:** The mechanism is plausible — re-reading reactivates the same mental model you used to create the work, so you can't see the model's own flaws. You can see surface errors because those don't require re-evaluating the model.

**But:** Re-reading *can* catch some logical errors, especially after a time delay (when the original mental model has decayed). The claim as stated is too absolute.

**Verdict: PROBABLY CORRECT in direction, but OVERSTATED.** Should say "re-reading is much weaker at catching logical errors than surface errors" rather than implying it catches *only* typos.

---

## SECTION C: Checking the Design as a Recommendation

### "You should use this procedure to check your answers"

**C1:** "Use the /fwa procedure to check your answers because it systematically catches errors that informal checking misses."

**C2 — What happens if you do NOTHING?** You rely on intuition, informal checking, and social verification. For most daily decisions, this is actually fine. The vast majority of answers people act on don't need a multi-step verification procedure.

This reveals a design flaw: **the skill doesn't adequately help users decide when to use it.** The "When to Override" section exists but is at the bottom, after the full procedure. A user who needs the procedure has already committed to running it before they encounter the reasons not to. The triage decision — "should I even check this?" — should come FIRST, not last.

**C3 — Two alternatives:**
1. **Simple pre-mortem:** "Imagine this answer is wrong. What's the most likely reason?" (One question, 30 seconds, catches most of what the full procedure catches.)
2. **Red team with a colleague:** Ask someone to argue against your answer. Often more effective than solo checking because it introduces genuinely independent perspectives.

Are these clearly worse than /fwa?
- The simple pre-mortem is faster and nearly as effective for most cases. It's NOT clearly worse.
- The red team approach introduces real independent thinking rather than simulated independence. It's arguably BETTER for high-stakes decisions.

**Verdict: UNCERTAIN.** The full procedure may be overkill for most use cases, and the skill doesn't help users calibrate when the full procedure is warranted vs. when a lighter-weight check suffices.

**C4 — Worst case if /fwa fails?**
The worst case is that a user follows the procedure, gets a "probably correct" verdict, and then acts with false confidence on a wrong answer. This is worse than not checking at all, because at least without the procedure the user retains their uncertainty. **The procedure can convert healthy uncertainty into false confidence.** This is a real risk and is not acknowledged in the skill.

**C5 — Who would disagree?**
- **A cognitive scientist** would say the type-based routing (factual vs. causal vs. decision vs. prediction) doesn't match how real errors work. Errors cluster around *biases* (confirmation, anchoring, availability), not around *claim types*. A factual claim can fail from anchoring. A prediction can fail from confirmation bias. Organizing around form rather than failure mode means the same bias gets different treatment depending on sentence structure.
- **A naturalistic decision-making researcher** (Gary Klein) would argue that structured procedures like this actively interfere with expert pattern recognition. For experienced practitioners, the procedure adds friction without adding accuracy.
- **A pragmatist** would argue the procedure is too long for most real-world contexts. By the time you've completed all the steps, the decision window may have closed.
- **A Bayesian** would note the procedure is entirely qualitative. It never asks "how confident are you, numerically?" — which means it can't help with calibration, only with direction.

Does this reveal something missed? Yes: the skill organizes around the *form* of the answer (what kind of sentence is it?) rather than the *source* of the error (what cognitive process went wrong?). And it assumes all users benefit equally from the same procedure, regardless of expertise level or time constraints.

---

## SECTION D: Checking the Prediction

### "Users who follow this will catch errors they'd otherwise miss"

**D1:** "A user who follows the /fwa procedure will identify at least one flaw in their answer that they would not have found through informal checking, in cases where the answer contains a flaw."

**D2 — Base rate:** What fraction of structured-checklist interventions actually improve outcomes? Research on surgical checklists (Gawande) shows significant improvement. Research on forecasting checklists (Tetlock) shows moderate improvement. Research on decision checklists in business shows mixed results. Base rate for "structured checklist materially improves outcome": roughly 40-60% of cases, highly dependent on domain and user compliance.

Is /fwa's implied prediction close to the base rate? The skill implies near-certainty — follow the steps, catch the error. The base rate suggests it would help in maybe half the cases. **The skill is overconfident about its own reliability.**

**D3 — If the prediction is wrong, what would I see first?**
1. Users complete the procedure and still feel uncertain (the procedure didn't resolve anything).
2. Users find the procedure confirms answers that later turn out wrong (false confidence).
3. Users abandon the procedure partway through because it feels like busywork for their specific case.

Are any of these already present? Without user data we can't confirm, but (3) is plausible given the procedure's length.

**Verdict: UNCERTAIN.** The skill is likely helpful in some cases but overestimates its own reliability.

---

## Summary of Flawed Assumptions Found

### The 3 Strongest Wrongness Signals (Applied to /fwa Itself)

1. **The designers WANT this procedure to work** — confirmed. The skill checks for motivated reasoning in others but cannot check for motivated reasoning in its own design.

2. **The four-type taxonomy feels obvious and hasn't been checked** — confirmed. It misses moral claims, definitional disputes, interpretations, and compound claims (partially addressed by Section E, but the routing is imperfect).

3. **The skill can't name an alternative to itself** — confirmed. It never says "here's when a different checking method would work better than this one." It assumes it's the right tool whenever you have an answer to check.

### Design-Level Flaws

| # | Assumption | Status | What's Actually True |
|---|---|---|---|
| 1 | **Organizing by answer type (factual/causal/decision/prediction) is the right taxonomy** | LIKELY FLAWED | Errors cluster around cognitive biases, not claim types. The same bias causes errors across all claim types. A bias-organized approach might be more effective. |
| 2 | **The procedure's output can be trusted ("Accept tentatively" = safe to act)** | DANGEROUS | The procedure can produce false confidence. There's no self-assessment of its own false-negative rate or guidance on what it systematically misses. |
| 3 | **Users can correctly classify their answer into one type** | UNCERTAIN | Many real answers are hybrids. "We should switch to Rust because it's faster" is simultaneously a recommendation, a causal claim, and a factual claim. Section E acknowledges this but says "break into separate claims" — which is clunky and may lose the interaction effects between claim types. |
| 4 | **A branching procedure is better than a flat checklist** | UNCERTAIN | Simpler alternatives (pre-mortem, bias checklist) may achieve comparable error-detection at lower cognitive cost. The branching structure adds overhead that may discourage use. |
| 5 | **The user can be objective about their own answer** | LIKELY FLAWED | Every step requires the user to challenge their own thinking, but motivated reasoning affects *whether you notice* the motivation, not just whether you admit it. Asking "Do you WANT this to be true?" assumes the user will answer honestly about their own biases — which is precisely what biased people cannot do. |

### Claim-Level Flaws

| # | Claim | Status | Correction |
|---|---|---|---|
| 6 | "Memory is unreliable" | OVERSTATED | Memory is unreliable for facts outside your area of repeated practice. Within-domain expert memory can be quite reliable. |
| 7 | "'Obvious' claims have the highest wrongness rate" | OVERSTATED | The wrongness rate is bimodal — most obvious claims are correct, but the wrong ones are dangerous because no one catches them. "Most dangerous" is accurate; "highest rate" is not. |
| 8 | "Absence of evidence is not evidence of absence" | OVERSTATED | In Bayesian terms, absence of evidence is weak evidence of absence. The strength depends on search quality and thoroughness. |
| 9 | "Re-reading catches typos, not logical errors" | OVERSTATED | Re-reading is much *weaker* at catching logical errors, but not useless — especially after a time delay. |

### Structural Blind Spots

| # | What /fwa Doesn't Check For | Why It Matters |
|---|---|---|
| 10 | **Framing effects** — the way the answer is stated may hide the real question | /fwa takes the user's framing at face value. If the user frames a decision problem as a factual problem, /fwa runs the wrong checks entirely. |
| 11 | **Systemic errors** — the entire framework of analysis might be wrong | /fwa checks within the user's framework. It doesn't ask "Is this even the right question?" or "Are you solving the right problem?" |
| 12 | **Social/emotional drivers beyond "wanting"** | /fwa's motivation check (A5: "Do you WANT this to be true?") is too narrow. People also defend answers they've stated publicly, invested resources in, or that define their identity. Wanting it to be true is just one flavor of motivated reasoning. |
| 13 | **Triage comes last** | The "When to Override" section is at the bottom. Users who don't need the procedure will run it anyway before discovering they didn't need to. Should come first. |

---

## The Meta-Irony

Applying /fwa to itself reveals that the skill's own "Common Mistakes" section describes errors that the skill itself makes:

- **Mistake #3 ("Treating 'I can't find a problem' as 'there is no problem'")**: /fwa's own "Accept tentatively" endpoints do exactly this — they treat the absence of detected flaws as sufficient grounds for tentative acceptance, without quantifying how much of the error space was actually searched.
- **Mistake #5 ("Confusing precision with accuracy")**: /fwa is highly precise (detailed branching, specific step numbers, structured tables) but this precision may mask questions about whether the overall approach is accurate for error detection.
- **Mistake #4 ("Anchoring on the first answer")**: The four-type taxonomy was the first organizational scheme chosen, and no alternatives are considered within the skill itself.

The deepest flaw is structural: **/fwa is a procedure for finding wrong answers, but it has no procedure for finding out whether /fwa itself gives wrong answers.** It's a verification tool that cannot verify itself. This isn't a fixable bug — it's a fundamental limitation of any self-referential checking system. The fix is external: test /fwa against real decisions with real outcomes, and measure whether users who use it make better choices than those who don't.

---

## Confidence-Weighted Verdict

The /fwa skill is **a useful starting point that overstates its own reliability**. Its branching structure catches some real errors (especially the motivation check and the "name alternatives" step). But it organizes around the wrong axis (claim type instead of bias type), provides false confidence through its "accept tentatively" endpoints, and assumes a level of user self-awareness that the cognitive science it implicitly draws on would predict is unrealistic.

**If /fwa were an answer being checked by /fwa, it would land at: UNCERTAIN — functional but overstated, with unexamined alternatives that may be comparably effective at lower cost.**

---

*Applied /fwa at depth 2x: 5+ checks across all 4 sections + compound analysis, 3+ alternatives identified per section, multiple stress tests applied. The skill's own procedure was followed as faithfully as possible while turning it on itself.*

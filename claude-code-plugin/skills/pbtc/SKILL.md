---
name: "pbtc - Pre-Baked Thesis Check"
description: "Detect when reasoning is working backwards from a predetermined conclusion. Surfaces the signs that the 'analysis' is actually a case built to support a thesis that was chosen before the evidence was examined."
output:
  format: "prose"
---

# Pre-Baked Thesis Check

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Check my own reasoning**: The user suspects they may have already decided their conclusion and wants to verify whether their analysis is genuine or reverse-engineered from a predetermined answer.
**Interpretation 2 — Check someone else's reasoning**: The user is reading an argument, proposal, paper, or pitch and suspects the author decided the conclusion first and built the case backwards.
**Interpretation 3 — Check a document or plan**: The user has a specific piece of writing (report, strategy doc, recommendation) and wants it audited for signs of conclusion-first reasoning.

If ambiguous, ask: "I can help with checking your own reasoning for a pre-baked conclusion, auditing someone else's argument, or scanning a document — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Purpose

A pre-baked thesis is a conclusion that was chosen before the analysis began. The "reasoning" that follows isn't discovering truth — it's building a case. This is different from lying: the person often genuinely believes they reasoned their way to the conclusion. The tell is structural — the argument has fingerprints of reverse engineering even when the author doesn't know they did it.

**Why this matters**:
- Pre-baked theses survive scrutiny longer than they should because they come wrapped in evidence
- The person holding one feels *more* confident, not less, because they've "done the research"
- Organizations make expensive commitments based on analyses that were never actually open-ended
- Detecting the pattern early saves the cost of building on a rigged foundation

---

## Recursive Passes

Default: 1x (single pass). Parse pass count from $ARGUMENTS if specified (e.g., "/pbtc 3x [input]").

The Nx modifier controls how many times the check runs **recursively on its own output**. This catches the meta-failure: the check itself can have a pre-baked thesis about whether the input is pre-baked.

| Passes | What happens |
|--------|-------------|
| 1x     | Run the check once on the input. Standard. |
| 2x     | Run the check on the input → then run the check again on your Pass 1 output. Did your own analysis have a pre-baked conclusion about whether the thesis was pre-baked? |
| 3x     | 2x + run the check on your Pass 2 output. Did your self-correction itself have a pre-baked thesis? |
| 4x+    | Continue the chain. Each pass checks the previous pass's output for pre-bake signals. |

### How recursive passes work

**Pass 1**: Run Steps 1-7 on the user's input. Produce the verdict.

**Pass 2**: Treat your entire Pass 1 output as the new input. Run Steps 1-7 again, asking: "Did my Pass 1 analysis itself show signs of a pre-baked thesis?" Common findings:
- The check assumed SUSPECT or PRE-BAKED before examining signals (confirmation bias about bias)
- The check was too generous because it didn't want to accuse (performed neutrality)
- The check pattern-matched on surface features without engaging the actual argument

**Pass 3+**: Same pattern. Each pass treats the previous pass's full output as its input.

### Reporting recursive passes

```
PASS 1 VERDICT: [verdict] on the original input
PASS 2 VERDICT: [verdict] on Pass 1's analysis
  - [what Pass 2 found about Pass 1's reasoning]
  - [adjustments to Pass 1's verdict, if any]
PASS 3 VERDICT: [verdict] on Pass 2's analysis (if 3x+)
  - [what Pass 3 found]

FINAL VERDICT: [the verdict that survived all passes]
CONFIDENCE: [higher if verdicts converged; lower if they kept flipping]
```

If verdicts oscillate (Pass 1 says CLEAN, Pass 2 says PRE-BAKED, Pass 3 says CLEAN), report the oscillation — it means the signal is genuinely ambiguous.

---

## The Structural Fingerprints

Pre-baked theses leave characteristic marks. Not every mark proves the thesis was pre-baked, but the more marks present, the higher the probability.

### Signal Category 1: Evidence Selection Asymmetry

| Signal | What to look for | Severity |
|--------|-----------------|----------|
| **Cherry-picked evidence** | Only favorable data cited; unfavorable data absent or footnoted | High |
| **Asymmetric rigor** | Supporting evidence accepted at face value; opposing evidence held to impossibly high standards | High |
| **Missing null case** | No consideration of what the evidence would look like if the thesis were wrong | High |
| **Survivorship framing** | Only successful examples cited; failures in the same category ignored | Medium |
| **Date-selected evidence** | Time windows chosen to make the data fit; different windows would show different results | Medium |

### Signal Category 2: Argumentative Structure

| Signal | What to look for | Severity |
|--------|-----------------|----------|
| **Conclusion appears early** | The thesis is stated with confidence in paragraph 1; the rest is justification | High |
| **No pivot point** | The argument never genuinely entertains being wrong — no "however" that could have changed the conclusion | High |
| **Motte-and-bailey** | Bold claim made; when challenged, retreats to a weaker claim that no one disputes, then re-advances the bold one | High |
| **Straw alternatives** | Competing theses are presented in their weakest form | Medium |
| **Forced linearity** | Evidence presented as a logical chain, but the links only work if you already accept the conclusion | Medium |
| **Rhetorical hedging as armor** | "Of course there are exceptions, but..." used to dismiss counterevidence rather than engage it | Low |

### Signal Category 3: Emotional and Social Tells

| Signal | What to look for | Severity |
|--------|-----------------|----------|
| **Identity fusion** | The thesis is entangled with the person's identity, reputation, or prior public commitments | High |
| **Sunk cost defense** | Significant time, money, or status already invested in the conclusion being right | High |
| **Audience capture** | The conclusion matches exactly what the intended audience wants to hear | Medium |
| **Disproportionate certainty** | Confidence level far exceeds what the evidence warrants | Medium |
| **Defensive reaction** | Questions about the thesis trigger irritation rather than curiosity | Medium |

### Signal Category 4: Process Tells

| Signal | What to look for | Severity |
|--------|-----------------|----------|
| **Conclusion predates research** | Timeline shows the conclusion was announced or committed to before the analysis was done | Critical |
| **Methodology fitted to outcome** | Analytical method chosen because it produces the desired result; other valid methods would not | Critical |
| **Missing methodology** | No description of how evidence was gathered or how conclusions were reached | High |
| **Post-hoc hypothesis** | Presented as "we hypothesized X and found X" but there's no record of the hypothesis being stated before the data was collected | High |
| **Unfalsifiable framing** | The thesis is stated in a way that no possible evidence could disprove it | High |

---

## The Check Procedure

### Step 1: Extract the Thesis

State the core thesis being checked. What is the conclusion that might be pre-baked?

```
THESIS UNDER CHECK: [state it clearly]
SOURCE: [own reasoning / someone else's argument / document]
CONTEXT: [what situation produced this thesis]
```

If the thesis is bundled (multiple claims), unbundle and check the most load-bearing one first.

---

### Step 2: Run the Signal Scan

Go through each signal category and check for presence:

```
SIGNAL SCAN RESULTS:

EVIDENCE SELECTION:
[ ] Cherry-picked evidence: [present/absent] — [evidence]
[ ] Asymmetric rigor: [present/absent] — [evidence]
[ ] Missing null case: [present/absent] — [evidence]
[ ] Survivorship framing: [present/absent] — [evidence]
[ ] Date-selected evidence: [present/absent] — [evidence]

ARGUMENTATIVE STRUCTURE:
[ ] Conclusion appears early: [present/absent] — [evidence]
[ ] No pivot point: [present/absent] — [evidence]
[ ] Motte-and-bailey: [present/absent] — [evidence]
[ ] Straw alternatives: [present/absent] — [evidence]
[ ] Forced linearity: [present/absent] — [evidence]
[ ] Rhetorical hedging as armor: [present/absent] — [evidence]

EMOTIONAL/SOCIAL:
[ ] Identity fusion: [present/absent] — [evidence]
[ ] Sunk cost defense: [present/absent] — [evidence]
[ ] Audience capture: [present/absent] — [evidence]
[ ] Disproportionate certainty: [present/absent] — [evidence]
[ ] Defensive reaction: [present/absent] — [evidence]

PROCESS:
[ ] Conclusion predates research: [present/absent] — [evidence]
[ ] Methodology fitted to outcome: [present/absent] — [evidence]
[ ] Missing methodology: [present/absent] — [evidence]
[ ] Post-hoc hypothesis: [present/absent] — [evidence]
[ ] Unfalsifiable framing: [present/absent] — [evidence]
```

---

### Step 3: The Reversal Test

The most powerful single test for a pre-baked thesis.

**Ask**: If the evidence had pointed the other way, would the person have actually changed their conclusion?

Run this concretely:

```
REVERSAL TEST:

1. What evidence was used to support the thesis?
   [list key evidence]

2. What would the OPPOSITE evidence look like?
   [describe specifically]

3. If that opposite evidence existed, would the conclusion change?
   - YES, clearly → Thesis may be genuine (passes reversal test)
   - NO, they'd find other reasons → Pre-baked (fails reversal test)
   - UNCLEAR → Note and continue

4. Has opposite evidence actually appeared and been dismissed?
   - YES → Strong pre-bake signal
   - NO → Inconclusive
```

---

### Step 4: Generate Counter-Theses

If the thesis is genuine, there should be plausible alternatives that were considered and rejected on evidence. Generate them now:

```
COUNTER-THESES:

1. [Alternative conclusion that the same evidence could support]
   - Was this considered? [yes/no/unclear]
   - How was it addressed? [dismissed/engaged/ignored]

2. [Another alternative]
   - Was this considered? [yes/no/unclear]
   - How was it addressed? [dismissed/engaged/ignored]

3. [The null hypothesis — what if there's nothing here]
   - Was this considered? [yes/no/unclear]
   - How was it addressed? [dismissed/engaged/ignored]

COUNTER-THESIS TREATMENT:
- All dismissed without engagement → Strong pre-bake signal
- Some engaged seriously → Weaker signal
- Genuine engagement with best alternatives → Low signal
```

---

### Step 5: The Timeline Test

Reconstruct when the conclusion was reached relative to when the evidence was gathered:

```
TIMELINE:

When was the conclusion first stated or committed to?
  [date/stage or "unknown"]

When was the evidence gathered or analysis done?
  [date/stage or "unknown"]

ORDER:
- Conclusion AFTER analysis → Normal reasoning
- Conclusion BEFORE analysis → Pre-baked
- Conclusion SIMULTANEOUS with analysis → Suspect (common in motivated reasoning)
- Cannot determine → Note; check for other signals
```

---

### Step 6: Assess and Verdict

```
PRE-BAKE ASSESSMENT:

Signals present: [count] of [total checked]
Critical signals present: [list any]
Reversal test: [passed / failed / unclear]
Counter-thesis treatment: [engaged / dismissed / ignored]
Timeline: [normal / pre-baked / suspect / unknown]

VERDICT: [one of the following]

CLEAN — No significant pre-bake signals. The reasoning appears to have been
genuinely open-ended. The thesis may still be wrong, but it wasn't rigged.

SUSPECT — Multiple signals present but no critical ones. The thesis may have
been influenced by prior beliefs but the analysis contains genuine engagement
with alternatives. Recommend: stress-test the weakest links.

PRE-BAKED — Critical signals present and/or reversal test failed. The
conclusion was likely chosen before the analysis. The evidence was selected
to fit. Recommend: restart the analysis with genuine openness to alternatives,
or acknowledge the thesis is a position rather than a finding.

RIGGED — Process tells confirm the conclusion predated the research AND the
methodology was fitted to produce the desired outcome. This is not analysis —
it is advocacy wearing the costume of analysis. Recommend: discard and redo,
or reframe honestly as advocacy.
```

---

### Step 7: What To Do About It

Based on the verdict:

**If CLEAN**: No action needed on the reasoning process. If you want to strengthen the thesis further: → INVOKE: /araw $ARGUMENTS

**If SUSPECT**: Identify the 2-3 weakest points and stress-test them:
- What evidence would you need to see to abandon this thesis?
- Have you looked for that evidence as hard as you looked for supporting evidence?
- → INVOKE: /aex $ARGUMENTS to surface hidden assumptions

**If PRE-BAKED**: The thesis needs to be re-examined from scratch:
- Separate what you KNOW from what you WANT to be true
- → INVOKE: /sdc $ARGUMENTS for self-deception check
- → INVOKE: /se $ARGUMENTS to enumerate genuine alternatives
- Re-run the original analysis with a commitment to follow the evidence

**If RIGGED**: The analysis should be treated as advocacy, not research:
- If it's your own work: acknowledge the conclusion was chosen, not discovered. This doesn't make it wrong — but it means the "analysis" doesn't provide independent evidence for it
- If it's someone else's work: treat it as a persuasion document, not an analytical one. Evaluate the thesis on its merits, ignoring the rigged evidence
- → INVOKE: /claim $ARGUMENTS to test the thesis properly

---

## Quick Check (Abbreviated)

For fast screening:

```
QUICK PRE-BAKE CHECK: [thesis]

Three questions:
1. Could any evidence have changed this conclusion? [yes/no]
2. Were the best counter-arguments engaged or dismissed? [engaged/dismissed]
3. Did the conclusion exist before the analysis? [before/after/unknown]

Score: [0-3 "no/dismissed/before" answers]
- 0: Likely clean
- 1: Worth a closer look
- 2-3: Likely pre-baked — run full check
```

---

## Common Pre-Bake Patterns

### The Consultant's Pre-Bake
Client hints at desired conclusion → consultant "discovers" it through "analysis" → client gets validation they paid for. **Tell**: Recommendation matches the brief too perfectly.

### The Confirmation Research
Person googles to confirm what they already believe → finds supporting evidence (the internet has evidence for everything) → feels validated. **Tell**: Only one search direction was tried.

### The Strategic Plan Pre-Bake
Leadership decides direction → commissions analysis → analysis confirms direction → presented as "data-driven." **Tell**: No scenario in the analysis leads to a different recommendation.

### The Expert's Pre-Bake
Expert has a framework → new situation arises → framework is applied → conclusion matches framework. Not always wrong, but the expert rarely concludes "my framework doesn't apply here." **Tell**: The framework has never produced a surprising conclusion.

### The Sunk Cost Pre-Bake
Significant investment already made → analysis of whether to continue → analysis says continue. **Tell**: The option to cut losses was never seriously modeled.

---

## Quality Checklist

Before completing:
- [ ] Thesis clearly extracted and stated
- [ ] All four signal categories scanned
- [ ] Reversal test applied
- [ ] Counter-theses generated and their treatment assessed
- [ ] Timeline reconstructed where possible
- [ ] Verdict assigned with evidence
- [ ] Actionable next step provided based on verdict

---

## Integration

- **Use from**: /claim (check if a "supported" claim was pre-baked), /evaluate (check if an assessment was conclusion-first), /decide (check if the "analysis" already had a winner)
- **Routes to**: /araw (test a clean thesis), /sdc (deeper self-deception check), /aex (surface hidden assumptions), /se (enumerate alternatives), /claim (test thesis properly if rigged)
- **Differs from**: /sdc (sdc checks for self-deception broadly; pbtc specifically checks if a conclusion predated its evidence), /ht (ht tests hypotheses; pbtc checks whether the hypothesis-testing was genuine), /aex (aex surfaces assumptions; pbtc checks if the conclusion was assumed from the start)
- **Complementary**: /ecal (epistemic calibration — was confidence warranted?), /sid (situation identification — are you seeing what's actually there?)

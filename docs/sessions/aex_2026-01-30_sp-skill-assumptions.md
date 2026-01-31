# Assumption Extraction — /sp Skill File

**Date**: 2026-01-30
**Input**: The /sp (Steelman Prompt) SKILL.md file

---

## Step 1: Identify the Core Claims

```
INPUT: /sp SKILL.md — a skill that improves prompts via 5 passes (classify, unbundle, criteria, failure-check, reconstruct)

CORE CLAIMS IDENTIFIED:
1. A 4-type taxonomy (CLAIM/DECISION/DIAGNOSTIC/EXPLORATORY) covers the prompts worth steelmanning
2. 5 sequential passes will improve a prompt
3. SKIP gates prevent unnecessary padding
4. The output should be a single copy-paste improved prompt, not analysis
5. Preserving original intent while adding precision is achievable
6. Failure-checking (Pass 4) catches ways a response could satisfy-but-be-useless
7. The skill is chainable — its output feeds into /araw, /se, /gu

TOTAL CLAIMS: 7
```

---

## Step 2: For Each Claim, Extract Assumptions

```
CLAIM 1: "A 4-type taxonomy covers the prompts worth steelmanning"

1. CAUSAL: Prompt type determines which improvements are needed
   -> Different types need different criteria injections

2. EXISTENCE: These 4 types exist as distinct, identifiable categories
   -> Prompts reliably fall into one of these buckets

3. STABILITY: The taxonomy won't need expansion
   -> No important 5th type is missing

4. ACCESS: The model can reliably classify prompts into these types
   -> Signal words ("should I", "why is", etc.) are sufficient for classification

5. CAPABILITY: The model can distinguish edge cases (e.g., "Should I believe X?" — DECISION or CLAIM?)
   -> Ambiguous prompts get classified usefully

6. VALUE: All 4 types benefit from steelmanning
   -> EXPLORATORY prompts benefit despite the FOHT finding (H50) that ambiguity can be a feature

7. KNOWLEDGE: n/a

8. RESOURCES: n/a

9. PERMISSION: n/a

10. TIMING: n/a
```

```
CLAIM 2: "5 sequential passes will improve a prompt"

1. CAUSAL: Running classify → unbundle → criteria → failure-check → reconstruct produces a better prompt
   -> The sequence matters and each pass feeds the next

2. EXISTENCE: Each pass has meaningful work to do on most prompts
   -> Prompts typically have something to unbundle, missing criteria, and failure modes

3. STABILITY: The pass order doesn't need to change based on input
   -> Classify-first is always correct

4. ACCESS: n/a

5. CAPABILITY: The model can execute all 5 passes without losing coherence
   -> Context window and attention suffice for this pipeline

6. VALUE: 5 passes is the right number — not too many, not too few
   -> No important dimension is missing (e.g., scope bounding, reframing)

7. KNOWLEDGE: The model knows what "good criteria" and "failure modes" look like for arbitrary domains
   -> General knowledge suffices for domain-specific prompts

8. RESOURCES: The 5 passes fit within a compact output budget
   -> All 5 passes + reconstruction < ~500 words of skill output

9. PERMISSION: n/a

10. TIMING: n/a
```

```
CLAIM 3: "SKIP gates prevent unnecessary padding"

1. CAUSAL: Saying "SKIP if already clear" causes the model to actually skip
   -> The instruction is sufficient to prevent the model from padding for completeness

2. EXISTENCE: There exist prompts where each pass should be skipped
   -> "Is P=NP?" genuinely needs no unbundling

3. STABILITY: The SKIP criteria won't drift across different models/contexts
   -> "Already clear" is interpreted consistently

4. ACCESS: n/a

5. CAPABILITY: The model can judge when to skip vs. when to engage
   -> The model won't over-skip (miss real issues) or under-skip (pad everything)

6. VALUE: Skipping is better than applying unnecessary passes
   -> Shorter output is more valuable than thorough-but-redundant output

7. KNOWLEDGE: n/a
8. RESOURCES: n/a
9. PERMISSION: n/a
10. TIMING: n/a
```

```
CLAIM 4: "The output should be a single copy-paste improved prompt"

1. CAUSAL: A clean prompt block is more useful than analysis
   -> Users want the improved prompt, not an explanation of why it's improved

2. EXISTENCE: A single reconstructed prompt can capture all improvements
   -> Unbundled + criteria + failure-fixes can be folded back into one coherent prompt

3. STABILITY: Users will use the output as a copy-paste block
   -> The use case is: run /sp, take output, paste into new session

4. ACCESS: n/a

5. CAPABILITY: The model can compress analysis back into prompt form
   -> Reconstruction doesn't lose the improvements

6. VALUE: Copy-paste usability is the primary value metric
   -> An improved prompt that's hard to use is a failed improvement

7. KNOWLEDGE: n/a
8. RESOURCES: n/a
9. PERMISSION: n/a
10. TIMING: n/a
```

```
CLAIM 5: "Preserving original intent while adding precision is achievable"

1. CAUSAL: Adding criteria and scope doesn't change what the user was asking
   -> Precision and intent are independent dimensions

2. EXISTENCE: "Original intent" is a recoverable thing
   -> The user's intent is detectable from the prompt text alone

3. STABILITY: Intent doesn't shift as you add precision
   -> Narrowing scope doesn't accidentally change the question

4. ACCESS: n/a

5. CAPABILITY: The model can detect intent accurately enough
   -> Implicit intent (what they really want vs. what they wrote) is readable

6. VALUE: Preserving intent is non-negotiable
   -> An improved prompt that asks a different question is worse than the original

7. KNOWLEDGE: n/a
8. RESOURCES: n/a
9. PERMISSION: n/a
10. TIMING: n/a
```

```
CLAIM 6: "Failure-checking catches ways a response could satisfy-but-be-useless"

1. CAUSAL: Identifying failure modes → adding fixes → better prompt
   -> Knowing what could go wrong is sufficient to prevent it

2. EXISTENCE: Most prompts have satisfy-but-useless failure modes
   -> Vague prompts reliably have exploitable gaps

3. STABILITY: The failure modes identified at prompt-improvement time will match actual response failures
   -> Pre-identified failures are the ones that actually occur

4. ACCESS: n/a

5. CAPABILITY: The model can identify its own failure modes
   -> This is a self-awareness task — the model predicts how it would fail

6. VALUE: 2-3 failure modes is the right number
   -> More would over-constrain; fewer would miss important ones

7. KNOWLEDGE: n/a
8. RESOURCES: n/a
9. PERMISSION: n/a
10. TIMING: n/a
```

```
CLAIM 7: "The skill is chainable — output feeds into /araw, /se, /gu"

1. CAUSAL: The improved prompt is valid input for other skills
   -> Skills accept natural language prompts, and /sp outputs one

2. EXISTENCE: The chain /sp → /araw is a real workflow users would use
   -> Users will steelman then test, not just steelman

3. STABILITY: Downstream skills don't expect a specific format that /sp might violate
   -> /araw doesn't need raw unprocessed prompts

4. ACCESS: n/a
5. CAPABILITY: n/a
6. VALUE: Chaining adds value beyond /sp alone
   -> /sp + /araw > /araw alone
7. KNOWLEDGE: n/a
8. RESOURCES: n/a
9. PERMISSION: n/a
10. TIMING: n/a
```

---

## Step 3: Rate Assumption Hiddenness

```
ASSUMPTION HIDDENNESS RATING:

| Assumption | Type | Hiddenness | Risk if Wrong |
|------------|------|------------|---------------|
| 4 types cover all steelmannable prompts | Existence | Shallow | Medium |
| No important 5th type is missing | Stability | Deep | High |
| Model can classify ambiguous prompts | Capability | Shallow | Medium |
| EXPLORATORY prompts benefit from steelmanning | Value | Deep | High |
| Pass order is always correct | Stability | Deep | Medium |
| No important pass is missing (scope, reframe) | Existence | Buried | High |
| Model knowledge suffices for domain-specific criteria | Knowledge | Deep | High |
| "SKIP if clear" actually causes skipping | Causal | Deep | Medium |
| Model can judge skip vs. engage accurately | Capability | Deep | High |
| Improvements can fold back into one coherent prompt | Capability | Shallow | Medium |
| Adding precision doesn't change intent | Causal | Buried | Critical |
| User's implicit intent is readable from text | Knowledge | Deep | High |
| Model can identify its own failure modes | Capability | Deep | High |
| 2-3 failure modes is the right number | Value | Shallow | Low |
| Improved prompt is valid input for downstream skills | Existence | Surface | Low |
```

---

## Step 4: Identify Assumption Dependencies

```
ASSUMPTION DEPENDENCIES:

"4 types cover all prompts"
    |-- requires "No important 5th type is missing"
    |-- requires "Model can classify ambiguous cases"

"5 passes improve the prompt"
    |-- requires "No important pass is missing"
    |-- requires "Pass order is always correct"
            |-- requires "Classify-first works for all inputs"

"SKIP gates work"
    |-- requires "'SKIP if clear' actually causes skipping"
            |-- requires "Model can judge skip vs. engage"

"Output is usable copy-paste block"
    |-- requires "Improvements fold back into one prompt"
            |-- requires "Adding precision doesn't change intent"
                    |-- requires "User's implicit intent is readable"

DEPENDENCY CHAINS:
1. "Readable intent" -> "Precision doesn't change intent" -> "Foldable back to one prompt" -> "Usable output" (if intent is unreadable, the whole skill drifts)
2. "No missing pass" -> "5 passes improve" (if a pass is missing, the pipeline has a gap)
3. "Model judges skip/engage" -> "SKIP causes skipping" -> "SKIP gates work" (if the model can't judge, gates either over-fire or under-fire)

ROOT ASSUMPTIONS (no dependencies):
- "User's implicit intent is readable from text"
- "No important pass is missing"
- "Model can judge skip vs. engage accurately"
- "Model can identify its own failure modes"
- "EXPLORATORY prompts benefit from steelmanning"
```

---

## Step 5: Categorize by Testability

```
TESTABILITY ASSESSMENT:

IMMEDIATELY TESTABLE (can verify now):
- "4 types cover all prompts": Test by running 20 diverse prompts through classification — count how many don't fit
- "'SKIP if clear' causes skipping": Test by running /sp on "Is P=NP?" — does it skip unbundling?
- "Model can classify ambiguous prompts": Test with "Should I believe climate change is real?" (CLAIM or DECISION?)
- "Improved prompt is valid input for /araw": Run /sp then /araw on the output

TESTABLE WITH EFFORT (requires work):
- "No important pass is missing": Would need to compare /sp output against prompts improved by hand — look for gaps the skill misses
- "Adding precision doesn't change intent": Run /sp on 10 prompts, ask the original author if the improved prompt still asks their question
- "Model can identify its own failure modes": Run /sp, then deliberately try to give a satisfy-but-useless response to the improved prompt — see if the failure modes were caught

UNTESTABLE (must accept or reject):
- "EXPLORATORY prompts benefit from steelmanning": Judgment call — the FOHT analysis (H50) flagged this as a real tension
  -> Decision: Accept with caution — the skill uses light touch for EXPLORATORY, which mitigates
- "User's implicit intent is readable from text": Fundamentally limited by what the user wrote
  -> Decision: Accept — this limitation applies to all skills, not unique to /sp
```

---

## Step 6: Generate Assumption Map

```
===================================================
ASSUMPTION MAP: /sp (Steelman Prompt) Skill
===================================================

CLAIM 1: "4-type taxonomy covers steelmannable prompts"
|-- "These 4 types are distinct categories" (Existence, Shallow)
|-- "No important 5th type is missing" (Stability, Deep) [!] HIGH RISK
|-- "Model can classify ambiguous prompts" (Capability, Shallow)
|-- "EXPLORATORY prompts benefit from steelmanning" (Value, Deep) [!] HIGH RISK

CLAIM 2: "5 sequential passes improve a prompt"
|-- "Each pass feeds the next in the right order" (Causal, Deep)
|-- "No important pass is missing" (Existence, Buried) [!] HIGH RISK
|-- "Domain-general knowledge suffices for criteria" (Knowledge, Deep) [!] HIGH RISK
|-- "5 passes fit within compact output budget" (Resources, Shallow)

CLAIM 3: "SKIP gates prevent padding"
|-- "'SKIP if clear' causes actual skipping" (Causal, Deep)
|-- "Model can judge skip vs. engage" (Capability, Deep) [!] HIGH RISK

CLAIM 4: "Output is a usable copy-paste block"
|-- "Improvements fold into one coherent prompt" (Capability, Shallow)
|-- "Copy-paste is the right output format" (Value, Shallow)

CLAIM 5: "Intent is preserved while adding precision"
|-- "Precision and intent are independent" (Causal, Buried) [!] CRITICAL
|-- "Implicit intent is readable from text" (Knowledge, Deep) [!] HIGH RISK

CLAIM 6: "Failure-check catches satisfy-but-useless modes"
|-- "Model can identify its own failure modes" (Capability, Deep) [!] HIGH RISK
|-- "Pre-identified failures match actual failures" (Stability, Deep)

CLAIM 7: "Skill is chainable"
|-- "Downstream skills accept /sp output format" (Existence, Surface)
|-- "/sp + /araw > /araw alone" (Value, Shallow)

===================================================

SUMMARY STATISTICS:
- Total claims analyzed: 7
- Total assumptions extracted: 19
- By type: Causal 4, Existence 4, Stability 3, Capability 4, Value 3, Knowledge 3, Resources 1
- By hiddenness: Surface 1, Shallow 6, Deep 8, Buried 2
- High-risk assumptions: 8

===================================================

PRIORITY ASSUMPTIONS (most critical to verify):

1. "Adding precision doesn't change intent" — Causal, BURIED, Risk: CRITICAL
   Why critical: If steelmanning drifts the question, the skill makes prompts worse.
   The FOHT analysis flagged this (H49, H50) — unbundling can change meaning.
   How to test: Run /sp on 10 prompts, have the author confirm the improved version
   still asks their question.

2. "No important pass is missing" — Existence, BURIED, Risk: HIGH
   Why critical: The FOHT analysis identified scope bounding (H25) and reframing (H27)
   as blockers. Neither has a dedicated pass. Scope bounding is partially covered by
   Criteria, but reframing ("is this the right question?") has no pass at all.
   How to test: Collect prompts where /sp output still produces bad responses —
   look for patterns in what the skill missed.

3. "Model can judge skip vs. engage" — Capability, DEEP, Risk: HIGH
   Why critical: If the model under-skips, /sp pads every prompt (defeating compactness).
   If it over-skips, /sp misses real issues (defeating the purpose).
   How to test: Run /sp on prompts that clearly need each pass vs. prompts that
   clearly don't — check if SKIP fires correctly.

4. "Model can identify its own failure modes" — Capability, DEEP, Risk: HIGH
   Why critical: Pass 4 asks the model to predict how it would fail. The FOHT analysis
   (H69) noted that self-answered questions share the model's blind spots.
   How to test: Run /sp, then deliberately try to give a satisfy-but-useless answer
   to the improved prompt — see if the failure modes were caught.

5. "EXPLORATORY prompts benefit from steelmanning" — Value, DEEP, Risk: HIGH
   Why critical: FOHT H50 established that exploratory prompts benefit from ambiguity.
   The skill applies lighter treatment but still adds criteria and constraints, which
   may narrow exploration prematurely.
   How to test: Compare responses to raw exploratory prompts vs. /sp-improved versions —
   check if the improved version produces narrower or broader exploration.

===================================================
```

---

## Key Findings

The most actionable finding is **Priority #2**: the skill may be missing a **reframing pass**. The FOHT analysis identified "is this the right question?" (H26-H27) as a distinct blocker, and no current pass addresses it. Criteria injection catches missing details, but not wrong framing.

The deepest risk is **Priority #1**: the tension between adding precision and preserving intent. This is the fundamental paradox of the skill — every improvement risks drift. The Pass 5 instruction "preserve the original intent exactly" is the only safeguard, and it's an honor-system instruction rather than a structural check.

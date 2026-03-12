---
name: "it - I Think"
description: "Process 'I think' statements into explicit claims with confidence levels, evidence/assumption separation, and next verification actions."
output:
  format: "prose"
---

# IT - I Think

**Input**: $ARGUMENTS

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Decompose a belief into testable parts**: The user has an "I think" statement and wants it unbundled into its core claim, evidence, assumptions, confidence level, and recommended next action.
**Interpretation 2 — Calibrate confidence on an uncertain claim**: The user is primarily unsure how confident they should be about something and wants help distinguishing what they know from what they assume.
**Interpretation 3 — Route a vague intuition to the right analysis**: The user has a gut feeling or loose opinion and doesn't know what kind of thinking it needs — factual verification, strategic stress-testing, value examination, or something else.

If ambiguous, ask: "I can help with decomposing a belief into testable parts, calibrating your confidence level, or figuring out what kind of analysis your intuition needs — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **"I think" hides structure.** Every "I think" statement bundles a claim, evidence (or lack of it), assumptions, and a confidence level. Unbundling these is the skill's core operation.

2. **Confidence is not binary.** People say "I think" for claims they're 20% sure about and claims they're 90% sure about. The same words, vastly different states. Calibrating confidence before acting prevents both recklessness and paralysis.

3. **Claims are often compound.** "I think we should restructure the team" contains at least three claims: the team has a structural problem, restructuring would fix it, and now is the right time. Decompose before testing.

4. **Evidence and assumptions look alike.** "I think this because we tried it before and it failed" sounds like evidence but might be an assumption — was the context the same? Did it fail for the reason assumed? Separate what's observed from what's inferred.

5. **The right next action depends on claim type AND confidence.** A low-confidence factual claim needs verification. A high-confidence strategic claim needs stress-testing. A medium-confidence ethical claim needs value examination. One routing table doesn't fit all.

---

## Phase 1: Claim Extraction

```
[I1] RAW_STATEMENT: [the user's "I think" statement, quoted]
[I2] CORE_CLAIM: [the central claim, stated neutrally]
[I3] CLAIM_TYPE: [factual | strategic | evaluative | predictive | normative | preference]
```

### Compound Claim Check

```
[I4] IS_COMPOUND: [yes/no]
[I5] SUB-CLAIMS (if compound):
  [I5a] [sub-claim 1]
  [I5b] [sub-claim 2]
  [I5c] [sub-claim 3]
```

| Claim Type | Example | Testing Method |
|-----------|---------|---------------|
| **Factual** | "I think the server is down" | Check — verify against reality |
| **Strategic** | "I think we should pivot" | Stress-test — AR/AW analysis |
| **Evaluative** | "I think this code is bad" | Criteria — what does "bad" mean? |
| **Predictive** | "I think this will fail" | Forecast — what evidence supports/refutes? |
| **Normative** | "I think we should be more transparent" | Values — whose values? What tradeoffs? |
| **Preference** | "I think React is better" | Criteria — better for what? By what measure? |

---

## Phase 2: Evidence/Assumption Separation

For each claim (or sub-claim if compound):

```
[I6] EVIDENCE (observed, testable):
  [I6a] [evidence 1] — SOURCE: [where this comes from]
  [I6b] [evidence 2] — SOURCE: [source]

[I7] ASSUMPTIONS (inferred, untested):
  [I7a] [assumption 1] — TESTABLE: [yes/no] — TEST: [how to test if yes]
  [I7b] [assumption 2] — TESTABLE: [yes/no] — TEST: [how]

[I8] GAPS (neither evidence nor assumption — just missing):
  [I8a] [what's unknown] — MATTERS: [high/medium/low] — FINDABLE: [yes/no]
```

### Separation Test

For each piece of "evidence," ask:
- Did I directly observe this, or am I inferring it? (Inference → assumption)
- Could someone else verify this independently? (No → assumption)
- Am I using a past experience as evidence for a different situation? (Probably → assumption)

---

## Phase 3: Confidence Calibration

```
[I9] STATED_CONFIDENCE: [what the user seems to feel — from tone/hedging]
[I10] CALIBRATED_CONFIDENCE: [after evidence/assumption analysis]
  LEVEL: [very low (<20%) | low (20-40%) | medium (40-60%) | high (60-80%) | very high (>80%)]
  REASONING: [what drives this level]

[I11] CONFIDENCE_DRIVERS:
  UPWARD: [what makes confidence higher — e.g., strong evidence, domain expertise]
  DOWNWARD: [what makes confidence lower — e.g., untested assumptions, novel situation]
```

### Common Miscalibrations

| Pattern | What Happens | Correction |
|---------|-------------|-----------|
| **Expertise inflation** | "I've done this before" → overconfidence | Was the context the same? |
| **Hedging as signal** | "I think maybe perhaps" → very low stated | Might actually be medium — hedging is social, not epistemic |
| **Certainty anchoring** | First impression calcifies | What would change your mind? |
| **Availability bias** | Recent vivid example dominates | Is this representative or memorable? |

---

## Phase 4: Next Action Routing

Based on claim type + calibrated confidence:

| Claim Type | Confidence | Route |
|-----------|-----------|-------|
| **Factual** | Any | → `/ver` to verify against evidence |
| **Strategic** | High | → `/aw` to stress-test (high confidence needs adversarial pressure) |
| **Strategic** | Low/Medium | → `/ar` to explore what follows if right |
| **Evaluative** | Any | → `/evaluate` with explicit criteria |
| **Predictive** | Any | → `/ht` to formulate testable hypothesis |
| **Normative** | Any | → `/ve` to examine underlying values |
| **Preference** | Any | → `/cmp` to compare against alternatives with criteria |
| **Compound** | Any | → Decompose first, route each sub-claim separately |

```
[I12] RECOMMENDED_ACTION: /skill-id — [why this is the right next step]
[I13] INVOCATION: /skill-id [specific arguments derived from the claim]
[I14] ALTERNATIVE_IF_WRONG: /skill-id — [backup if first choice doesn't resolve]
```

---

## Phase 5: Output

```
"I THINK" DECOMPOSITION
========================

ORIGINAL: [quoted statement]

CLAIM: [core claim, stated neutrally]
TYPE: [factual | strategic | evaluative | predictive | normative | preference]
COMPOUND: [yes/no — if yes, sub-claims listed]

EVIDENCE:
- [evidence with source]

ASSUMPTIONS:
- [assumption with testability]

GAPS:
- [unknown with importance]

CONFIDENCE: [level with percentage range]
REASONING: [what drives the confidence level]

→ INVOKE: /skill-id [specific invocation]
  WHY: [why this is the right next step for this type of claim at this confidence]
  IF_WRONG: /skill-id [backup route]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Claim accepted at face value** | No evidence/assumption separation | Always unbundle — every claim has hidden structure |
| **Compound claim treated as atomic** | Single confidence level for multi-part claim | Decompose compound claims; rate each sub-claim |
| **Confidence not calibrated** | Using stated confidence without checking | Apply miscalibration checks |
| **Wrong routing** | Strategic claim routed like factual claim | Route by claim TYPE, not just confidence |
| **Evidence confused with assumption** | Inference treated as observation | Apply separation test to each piece |
| **Generic routing** | Everything goes to `/claim` | Different claim types need different skills |

---

## Depth Scaling

| Depth | Sub-Claims Checked | Evidence/Assumption Items | Calibration Checks | Routing Alternatives |
|-------|-------------------|--------------------------|--------------------|--------------------|
| 1x | 1 | 2 | 1 | 1 |
| 2x | 3 | 4 | 3 | 2 |
| 4x | 5 | 8 | 5 | 3 |
| 8x | All | 12 | All patterns checked | Full routing analysis |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Core claim extracted and stated neutrally
- [ ] Claim type classified
- [ ] Compound claims decomposed into sub-claims
- [ ] Evidence separated from assumptions with sources
- [ ] Each assumption tested for testability
- [ ] Confidence calibrated (not just using stated confidence)
- [ ] Miscalibration patterns checked
- [ ] Routing matches claim type + confidence level
- [ ] Invocation includes specific arguments (not generic)

---

## Integration

- Use from: natural language processing of user input
- Routes to: `/ver`, `/aw`, `/ar`, `/evaluate`, `/ht`, `/ve`, `/cmp` depending on claim type
- Complementary: `/aex` (extract hidden assumptions), `/nsa` (when confidence is very low)
- Differs from `/claim`: claim does full truth-testing; it decomposes and routes
- Differs from `/nsa`: nsa handles uncertainty; it handles all "I think" statements including confident ones

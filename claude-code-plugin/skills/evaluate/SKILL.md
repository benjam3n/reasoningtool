---
name: "evaluate - Assess Something"
description: Sub-orchestrator for evaluation. Routes to ARAW, MECE validation, procedure validation, assumption extraction, risk analysis, or quality checks based on what's being assessed and what kind of evaluation is needed.
output:
  format: "prose"
---

# Evaluate

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Correctness check**: The user wants to know if something is right ("Is this right?", "Does this hold up?").
**Interpretation 2 — Completeness check**: The user wants to know if something is missing ("Am I missing anything?", "Is this MECE?").
**Interpretation 3 — Quality check**: The user wants to know if something is good ("Is this good?", "Is this solid?", "Review my X").
**Interpretation 4 — Risk check**: The user wants to know what could go wrong ("What could go wrong?", "Is this safe?").
**Interpretation 5 — Assumption check**: The user wants to know what's hidden ("What am I assuming?", "What's hidden?").

If ambiguous, ask: "Are you checking for correctness, completeness, quality, risk, or hidden assumptions?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Evaluation requires criteria.** "Is this good?" is unanswerable without "good by what standard?" If the user doesn't specify, derive criteria from context or ask.

2. **Self-evaluation must be adversarial.** When evaluating your own prior output, increase adversarial rigor. Confirmation bias is strongest when reviewing your own work.

3. **Evaluation is not confirmation.** The purpose is to find weaknesses, gaps, and errors — not to validate. If the evaluation finds nothing wrong, verify your test was severe enough to have found problems if they existed. If the test was severe and passed, the work is strong — say so.

4. **The type of evaluation matters.** Correctness, completeness, quality, risk, and assumption checks use different tools and produce different outputs. Route precisely.

---

## Routing Decisions

### 1. Extract What's Being Evaluated

What is the user asking you to assess? A plan, an argument, a piece of work, a process, a conclusion?

### 2. Is This Actually Evaluation?

- **"X is true"** → This is a claim to test, not work to evaluate. → INVOKE: /claim $ARGUMENTS
- **"Should I X?"** → This is a decision. → INVOKE: /decide $ARGUMENTS
- **"Why is X?"** → This is diagnostic. → INVOKE: /diagnose $ARGUMENTS
- **"What about X?"** → This is an idea. → INVOKE: /viability $ARGUMENTS
- **"I think this is good"** → Formalize and test. → INVOKE: /it $ARGUMENTS
- **"This seems good, but X"** → Tension to resolve. → INVOKE: /but $ARGUMENTS
- **"I'm not sure if this is good"** → Classify the uncertainty. → INVOKE: /nsa $ARGUMENTS
- **"Handle this"** (vague) → INVOKE: /handle $ARGUMENTS
- **If it IS evaluation** → continue.

### 3. What Kind of Evaluation?

- **Correctness** ("Is this right?", "Does this hold up?"): test the core claims.
  → INVOKE: /araw [core claims extracted from the input]
- **Completeness** ("Am I missing anything?", "Is this MECE?"): check for gaps.
  → INVOKE: /mv [structure] for MECE validation
  → INVOKE: /se [space] to find what's missing
  → INVOKE: /siycftr $ARGUMENTS to find implied but omitted items
- **Quality** ("Is this good?", "Is this solid?"): validate against criteria.
  → INVOKE: /pv [procedure/plan] for procedure validation
  → INVOKE: /val [conclusion] for multi-check validation
- **Assumptions** ("What am I assuming?", "What's hidden?"): surface assumptions.
  → INVOKE: /aex [content]
- **Risks** ("What could go wrong?", "Is this safe?"): anticipate failure.
  → INVOKE: /fla [plan] for failure anticipation
  → INVOKE: /prm [plan] for pre-mortem
  → INVOKE: /saf [plan] for safety analysis
  → INVOKE: /obo [plan] for obvious bad outcomes

### 4. Is There a Standard?

- **Yes** ("Is this MECE?", "Does this meet the requirements?", "Is this consistent with X?"): check against the stated standard.
- **No** ("Is this good?"): need to establish criteria first. Ask: "Good by what measure?" or derive criteria from context.
- **Platitude standard** ("Is this best practice?", "Is this the right way?"): operationalize first.
  → INVOKE: /platitude on the standard — then evaluate against operationalized criteria.

### 5. Whole or Part?

- **Whole** ("Review my plan"): assess the full thing. If large, decompose first.
  → INVOKE: /dcm to decompose, then evaluate each part.
- **Part** ("Is step 3 right?"): focus on the specific part.

### 6. Self-Evaluation or External?

- **Self** (evaluating own prior output): increase adversarial rigor — actively look for confirmation bias.
  → Also INVOKE: /sdc $ARGUMENTS to check for self-deception.
- **External** (evaluating user's work): balanced assessment.

### 7. Depth and Mode Selection

| Situation | Mode |
|-----------|------|
| User wants quick check | → /ezy (easy mode) |
| User wants maximum rigor | → /hrd (hard mode) or /certainty |
| User wants general principles extracted | → /genl |
| User wants specific application assessment | → /spcf |
| User wants sophisticated multi-layer assessment | → /soph |

---

## Execute

**Default (general "is this good?"):**
→ INVOKE: /araw [core claims from input] — test whether the key claims hold

**For completeness checks:**
→ INVOKE: /mv [structure]
→ INVOKE: /siycftr [to find missing implied items]

**For assumption surfacing:**
→ INVOKE: /aex [content]

**For risk assessment:**
→ INVOKE: /fla [plan]
→ INVOKE: /obo [plan] for obvious bad outcomes
→ INVOKE: /saf [plan] if safety-relevant

### Supplementary Analysis (invoke when relevant)

| Situation | Also invoke |
|-----------|------------|
| Need to check obvious things first | → /obv (obvious check) |
| Good outcomes being overlooked | → /ogo (obvious good outcomes) |
| Bad outcomes being ignored | → /obo (obvious bad outcomes) |
| Evaluation involves ethical dimensions | → /eth |
| Evaluation involves safety | → /saf |
| Need to trace implications | → /sycs (so you can see) |
| Need to differentiate between similar items | → /difr |
| Need future projections for the evaluated item | → /fut |
| Best-case outcome needed | → /utp |
| Worst-case outcome needed | → /dys |
| Work has unresolved decisions | → /tbd |
| Need to expand implied items | → /etc or /aso |
| Evaluation involves argument structure | → /agsk |
| User wants debate format | → /deb |

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Evaluation without criteria** | "It's good" without stating what "good" means | Establish criteria before evaluating |
| **Confirmation evaluation** | Everything comes back positive | Increase adversarial rigor — actively look for flaws |
| **Wrong evaluation type** | Checking correctness when user wanted completeness | Re-read the input — what kind of evaluation was asked for? |
| **Surface evaluation** | Checked obvious things, missed deep structural issues | Go deeper — check assumptions, not just visible claims |
| **Self-confirmation** | Evaluating own output and finding it great | Use /sdc — self-deception check |

---

## Depth Scaling

| Depth | Scope | Floor |
|-------|-------|-------|
| **1x** | Quick check — test core claim, spot-check completeness | 5 claims, 10 findings |
| **2x** | Standard — test core claims, check completeness, surface assumptions | 8 claims, 18 findings |
| **4x** | Thorough — all claims tested, full completeness check, risks assessed | 12 claims, 30 findings |
| **8x** | Deep — everything above plus pre-mortem, safety check, alternatives | 18 claims, 50 findings |

---

## Pre-Completion Checklist

- [ ] What's being evaluated is clearly stated
- [ ] Evaluation type identified (correctness / completeness / quality / assumptions / risks)
- [ ] Criteria established (stated or derived)
- [ ] Appropriate evaluation skill(s) invoked
- [ ] Findings organized by severity / importance
- [ ] Verdict stated with confidence level
- [ ] Specific improvements recommended

---

## After Completion

Report:
- What was evaluated
- Assessment type used (correctness / completeness / quality / assumptions / risks)
- Criteria used
- Findings (what's strong, what's weak, what's missing)
- Verdict with confidence level
- Specific improvements recommended

### Follow-Up Routing

After evaluation, the user may need:
- **"How do I fix this?"** → INVOKE: /how $ARGUMENTS
- **"What should I do?"** → INVOKE: /decide or /action
- **"Iterate on this"** → INVOKE: /iterate
- **"What are the implications?"** → INVOKE: /sycs
- **"What skill should I run next?"** → INVOKE: /next or /fonss
- **"What's still unresolved?"** → INVOKE: /tbd

---

## Integration

- **Use from**: /action (after execution, evaluate the result), /create (after content production, evaluate quality), /how (after method chosen, evaluate the plan)
- **Routes to**: /araw (correctness testing), /mv (MECE validation), /aex (assumption extraction), /fla (failure anticipation), /pv (procedure validation), /val (multi-check validation), /saf (safety), /obo (obvious bad outcomes)
- **Differs from**: /claim (evaluate assesses work, claim tests a proposition), /viability (evaluate assesses existing work, viability tests a proposed idea)
- **Complementary**: /iterate (after evaluation identifies issues, iterate to fix them), /obv (check the obvious first), /siycftr (find implied missing items)

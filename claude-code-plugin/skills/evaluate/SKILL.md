---
name: "evaluate - Assess Something"
description: Sub-orchestrator for evaluation. Routes to ARAW, MECE validation, procedure validation, or assumption extraction based on what's being assessed and what kind of evaluation is needed.
---

# Evaluate

**Input**: $ARGUMENTS

---

## Routing Decisions

### 1. Extract What's Being Evaluated

What is the user asking you to assess? A plan, an argument, a piece of work, a process, a conclusion?

### 2. Is This Actually Evaluation?

- **"X is true"** → This is a claim to test, not work to evaluate. → INVOKE: /claim $ARGUMENTS
- **"Should I X?"** → This is a decision. → INVOKE: /decide $ARGUMENTS
- **"Why is X?"** → This is diagnostic. → INVOKE: /diagnose $ARGUMENTS
- **"What about X?"** → This is an idea. → INVOKE: /viability $ARGUMENTS
- **If it IS evaluation** → continue.

### 3. What Kind of Evaluation?

- **Correctness** ("Is this right?", "Does this hold up?"): test the core claims.
  → INVOKE: /araw [core claims extracted from the input]
- **Completeness** ("Am I missing anything?", "Is this MECE?"): check for gaps.
  → INVOKE: /mv [structure] for MECE validation
  → INVOKE: /se [space] to find what's missing
- **Quality** ("Is this good?", "Is this solid?"): validate against criteria.
  → INVOKE: /pv [procedure/plan] for procedure validation
  → INVOKE: /val [conclusion] for multi-check validation
- **Assumptions** ("What am I assuming?", "What's hidden?"): surface assumptions.
  → INVOKE: /aex [content]
- **Risks** ("What could go wrong?", "Is this safe?"): anticipate failure.
  → INVOKE: /fla [plan] for failure anticipation
  → INVOKE: /prm [plan] for pre-mortem

### 4. Is There a Standard?

- **Yes** ("Is this MECE?", "Does this meet the requirements?", "Is this consistent with X?"): check against the stated standard.
- **No** ("Is this good?"): need to establish criteria first. Ask: "Good by what measure?" or derive criteria from context.

### 5. Whole or Part?

- **Whole** ("Review my plan"): assess the full thing. If large, decompose first.
- **Part** ("Is step 3 right?"): focus on the specific part.

### 6. Self-Evaluation or External?

- **Self** (evaluating own prior output): increase adversarial rigor — actively look for confirmation bias.
- **External** (evaluating user's work): balanced assessment.

---

## Execute

**Default (general "is this good?"):**
→ INVOKE: /araw [core claims from input] — test whether the key claims hold

**For completeness checks:**
→ INVOKE: /mv [structure]

**For assumption surfacing:**
→ INVOKE: /aex [content]

**For risk assessment:**
→ INVOKE: /fla [plan]

---

## After Completion

Report:
- What was evaluated
- Assessment type used (correctness / completeness / quality / assumptions / risks)
- Findings (what's strong, what's weak, what's missing)
- Verdict with confidence level
- Specific improvements recommended

---
name: "diagnose - Find the Cause"
description: Sub-orchestrator for diagnostic questions. Routes to UAUA exploration or direct causal tracing based on how much is known.
---

# Diagnose

**Input**: $ARGUMENTS

---

## Routing Decisions

### 1. Extract the Symptom

What is observably wrong? State it in concrete terms. "It's broken" is not a symptom — what specifically is broken? What happened vs what was expected?

If the input is too vague, ask: "What specifically is happening that shouldn't be?"

### 2. Is This Actually Diagnostic?

- **"X is true"** → This is a claim about a cause. → INVOKE: /claim $ARGUMENTS
- **"Should I fix X?"** → This is a decision. → INVOKE: /decide $ARGUMENTS
- **"Nothing works"** → This is emotional. → INVOKE: /emotion $ARGUMENTS
- **"How do I fix X?"** → This is method-seeking (cause already known). → INVOKE: /how $ARGUMENTS
- **If it IS diagnostic** → continue.

### 3. Is the Cause Known, Suspected, or Unknown?

- **Known** ("It fails because of X"): this is actually a CLAIM about causation.
  → INVOKE: /claim "X causes [symptom]" — test whether the stated cause is correct.
- **Suspected** ("I think it might be X"): test the hypothesis.
  → INVOKE: /araw "X is the cause of [symptom]"
- **Unknown** ("I don't know why"): need to explore possible causes first.
  → Continue to full diagnostic process.

### 4. Technical or Non-Technical?

- **Technical** (code, systems, infrastructure): frame with technical vocabulary, consider /dbg.
- **Non-technical** (people, process, strategy, market): frame with systems vocabulary.

### 5. Timeline

- **Clear timeline** (it started on Tuesday, after the deploy): trace back to what changed.
  → INVOKE: /fowwr [symptom + timeline]
- **No timeline** (it's always been like this, or unclear): broader investigation.
  → INVOKE: /uaua [symptom] — explore the space of possible causes.

### 6. Recurring?

- **First time**: full diagnosis.
- **Recurring** (tried fixing before, still broken):
  → INVOKE: /sbfow [symptom + what was tried]

### 7. Isolated or Systemic?

- **Isolated incident**: single root cause likely.
  → INVOKE: /rca [symptom]
- **Pattern across areas**: structural/systemic issue.
  → INVOKE: /sya [symptom pattern]

---

## Execute

**Default path (cause unknown, no timeline):**
→ INVOKE: /uaua [symptom] — explore possible causes, then test each

**With timeline:**
→ INVOKE: /fowwr [symptom + timeline]

**With suspected cause:**
→ INVOKE: /araw [suspected cause]

**Recurring problem:**
→ INVOKE: /sbfow [symptom]

---

## After Completion

Report:
- The symptom as stated
- Root cause(s) identified (confirmed / suspected / unknown)
- Causal chain (what caused what)
- Prevention (what would stop recurrence)
- What's still unresolved

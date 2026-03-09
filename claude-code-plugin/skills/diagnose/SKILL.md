---
name: "diagnose - Find the Cause"
description: Sub-orchestrator for diagnostic questions. Routes to UAUA exploration, causal tracing, safety analysis, or direct debugging based on how much is known and the nature of the problem.
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
- **"I think the problem is X"** → Formalize the hypothesis first. → INVOKE: /it $ARGUMENTS
- **"X, but Y doesn't explain it"** → Tension between symptom and explanation. → INVOKE: /but $ARGUMENTS
- **"I'm not sure what's wrong"** → Classify the uncertainty. → INVOKE: /nsa $ARGUMENTS
- **"Handle this"** (vague) → INVOKE: /handle $ARGUMENTS
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
- **Organizational** (team dysfunction, communication breakdown): consider /sya (systems analysis).

### 5. Timeline

- **Clear timeline** (it started on Tuesday, after the deploy): trace back to what changed.
  → INVOKE: /fowwr [symptom + timeline]
- **No timeline** (it's always been like this, or unclear): broader investigation.
  → INVOKE: /uaua [symptom] — explore the space of possible causes.

### 6. Recurring?

- **First time**: full diagnosis.
- **Recurring** (tried fixing before, still broken):
  → INVOKE: /sbfow [symptom + what was tried]
- **Getting worse over time**: consider systemic/structural cause.
  → INVOKE: /sya [symptom pattern] + /fut [trend analysis]

### 7. Isolated or Systemic?

- **Isolated incident**: single root cause likely.
  → INVOKE: /rca [symptom]
- **Pattern across areas**: structural/systemic issue.
  → INVOKE: /sya [symptom pattern]

### 8. Safety and Severity Check

Before deep diagnosis, check:

- **Safety-critical** (medical, infrastructure, security): → also INVOKE: /saf $ARGUMENTS
- **Obvious check first** (has anyone checked the obvious?): → also INVOKE: /obv $ARGUMENTS
- **Obvious bad outcomes if misdiagnosed**: → also INVOKE: /obo $ARGUMENTS

### 9. Depth and Mode Selection

| Situation | Mode |
|-----------|------|
| User wants quick answer | → /ezy (easy mode) |
| User wants maximum rigor | → /hrd (hard mode) or /certainty |
| User wants general principle | → /genl (what general pattern explains this?) |
| User wants specific application | → /spcf (apply known diagnosis framework to this case) |
| Problem seems too complex | → /dcm (decompose first) |
| User might be wrong about the problem | → /sid (situation identification) |
| User might have wrong mental model | → /rmm (recover from wrong mental model) |

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

### Supplementary Analysis (invoke when relevant)

| Situation | Also invoke |
|-----------|------------|
| Diagnosis involves ethical dimensions | → /eth |
| Worst case matters | → /dys (dystopia analysis) |
| Need to trace implications of the cause | → /sycs (so you can see) |
| Need to check what else might break | → /ata (and then also) |
| Unresolved sub-questions in diagnosis | → /tbd (to be determined) |
| Self-deception about the cause | → /sdc (self-deception check) |
| Need the story of what happened | → /story (narrative construction) |
| Need to differentiate between similar causes | → /difr (differentiation reasoning) |

---

## After Completion

Report:
- The symptom as stated
- Root cause(s) identified (confirmed / suspected / unknown)
- Causal chain (what caused what)
- Prevention (what would stop recurrence)
- What's still unresolved

### Follow-Up Routing

After diagnosis is complete, the user may need:
- **"How do I fix it?"** → INVOKE: /how $ARGUMENTS
- **"What should I do?"** → INVOKE: /decide or /action
- **"What could go wrong if I fix it wrong?"** → INVOKE: /fla or /obo
- **"What are the implications?"** → INVOKE: /sycs
- **"What skill should I run next?"** → INVOKE: /next or /fonss
- **"What's still unresolved?"** → INVOKE: /tbd

---
name: "fb - Filtered Feedback Generation"
description: Generate filtered feedback for self-improvement loops. Only accepts well-grounded, high-leverage items to prevent error accumulation.
context: fork
output:
  format: "prose"
---

# Filtered Feedback Generation

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Session review**: Review the current session's outputs and generate high-quality feedback items that can be fed back into the system for improvement.
**Interpretation 2 — Output quality filter**: The user has a set of findings or conclusions and wants them filtered to only keep the well-grounded, high-leverage ones.
**Interpretation 3 — Feedback loop design**: The user wants to design a feedback mechanism that prevents error accumulation over multiple iterations.

If ambiguous, ask: "Do you want me to review this session for feedback, filter existing findings for quality, or design a feedback loop?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Feedback loops amplify errors unless filtered.** Feeding raw output back into a system compounds errors. Each iteration can drift further from reality. Filtering ensures only well-grounded items propagate.

2. **Leverage determines priority.** Not all feedback is equal. High-leverage feedback — items that are high-value, defensible, and broadly applicable — deserves attention. Low-leverage feedback is noise.

3. **Grounding prevents hallucination loops.** Every accepted feedback item must have a GOSM marker ([O], [T], or [D]). Items without grounding are opinions, not findings. Feeding opinions back as inputs creates self-reinforcing illusions.

4. **Convergence validates.** When multiple independent analysis paths arrive at the same conclusion, confidence increases. Single-path conclusions are fragile.

5. **Fixed points are stable.** A finding that survives re-analysis without changing is a fixed point. Fixed points are more trustworthy than findings that shift with each examination.

6. **Rejection is the primary output.** Most potential feedback items should be rejected. If most items pass, the filter is too loose. Strict filtering prevents gradual quality decay.

---

## Filtering Criteria

### 1. Leverage Scoring

```
LEVERAGE = value x defensibility x scalability

value: Impact if resolved (0-1)
  0.0 = no impact
  0.3 = minor improvement
  0.5 = moderate improvement
  0.7 = significant impact
  1.0 = transformative

defensibility: Protected from invalidation (0-1)
  0.0 = easily overturned
  0.3 = weak evidence
  0.5 = moderate evidence
  0.7 = strong evidence, multiple sources
  1.0 = definitively established

scalability: Broadly applicable (0-1)
  0.0 = one-time use only
  0.3 = applicable to similar situations
  0.5 = applicable across domains
  0.7 = general principle
  1.0 = universal
```

**Minimum leverage for acceptance: 0.125** (e.g., 0.5 x 0.5 x 0.5)

### 2. Selection Filters

Before accepting, check:
- **Implementation readiness**: feasibility > 0.3 (can this actually be acted on?)
- **Risk tolerance**: high-risk items need proportionally higher leverage
- **Reversibility**: irreversible changes need stronger validation than reversible ones

### 3. Convergent Validation

Four independent checks per item:

| Check | Question | Pass Criterion |
|-------|----------|---------------|
| **is_grounded** | Does it have an [O], [T], or [D] marker? | Has specific evidence, not just assertion |
| **is_fixed_point** | Is it stable under re-analysis? | Same conclusion reached on second pass |
| **is_convergent** | Do multiple paths lead here? | At least 2 independent reasoning paths |
| **is_practical** | Does it pass real-world filters? | Can be implemented, doesn't violate constraints |

**Decision Protocol:**
- 4/4 checks pass → **ACCEPT** with high confidence
- 3/4 checks pass → **ACCEPT** with moderate confidence
- 2/4 checks pass → **FLAG** for review
- <2 checks pass → **REJECT**

---

## Procedure

### Step 1: Identify Candidate Feedback Items

Review the session outputs. For each potential feedback item:
- State it clearly as a single item
- Classify its type: goal / problem / question / decision / assumption / finding / principle
- Note where it came from in the session

### Step 2: Score Each Item

For each candidate:

```
ITEM: [text]
TYPE: [goal | problem | question | decision | assumption | finding | principle]
SOURCE: [where in the session]

LEVERAGE:
  value: [0-1] — [rationale]
  defensibility: [0-1] — [rationale]
  scalability: [0-1] — [rationale]
  LEVERAGE SCORE: [product]

CONVERGENT VALIDATION:
  is_grounded: [PASS/FAIL] — [evidence]
  is_fixed_point: [PASS/FAIL] — [re-analysis result]
  is_convergent: [PASS/FAIL] — [paths that lead here]
  is_practical: [PASS/FAIL] — [implementation assessment]
  CONVERGENT SCORE: [0-4]

SELECTION FILTERS:
  feasibility: [0-1]
  risk level: [low/medium/high]
  reversibility: [reversible/costly/irreversible]
```

### Step 3: Apply Filters

Categorize each item:

**ACCEPTED** (feed back into system):
```
TYPE: [type]
CONTENT: [the item]
LEVERAGE: [score]
CONVERGENT_SCORE: [0-4]
GROUNDING: [O/T/D marker with evidence]
CONFIDENCE: [high (4/4) | moderate (3/4)]
```

**FLAGGED** (needs review):
Items with 2/4 convergent checks passing. List for optional human review.

**REJECTED** (do not feed back):
Items that failed filtering. Excluded to prevent error accumulation. Briefly note why.

### Step 4: Format for Reuse

Format accepted items as inputs for future sessions:
- Goals → can feed into /want
- Problems → can feed into /diagnose
- Questions → can feed into /claim or /search
- Decisions → can feed into /decide
- Assumptions → can feed into /av
- Findings → can feed into /araw for further testing
- Principles → can feed into future analysis as constraints

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Loose filter** | >50% of items accepted | Tighten — most items should be rejected |
| **Ungrounded acceptance** | Items accepted without [O/T/D] marker | Grounding is mandatory — no exceptions |
| **Echo chamber** | Accepted items all confirm prior conclusions | Check for convergence from independent paths, not repeated paths |
| **Leverage inflation** | Everything scored as high-value | Calibrate: most items are moderate-value at best |
| **Fixed-point illusion** | Item "survives" re-analysis because you just agreed with yourself | Re-analysis must be genuinely adversarial |
| **Practicality blindness** | Theoretically sound items that can't be implemented | Practical filter is not optional — if it can't be acted on, it's not useful feedback |

---

## Depth Scaling

| Depth | Scope | Output |
|-------|-------|--------|
| **1x** | Quick — score top 5 items, accept/reject | Top items filtered, brief report |
| **2x** | Standard — all items scored, full convergent validation | Complete filtering with rationale for each |
| **4x** | Thorough — all items with full scoring, re-analysis for fixed-point check, formatted for reuse | Complete report with reusable feedback items |
| **8x** | Exhaustive — all items, multiple re-analysis passes, cross-session convergence check | Maximum-quality filtered feedback with provenance tracking |

---

## Pre-Completion Checklist

- [ ] All candidate items extracted from session
- [ ] Each item has leverage score with rationale
- [ ] Each item has convergent validation (all 4 checks)
- [ ] Selection filters applied (feasibility, risk, reversibility)
- [ ] Accepted items have [O/T/D] grounding markers
- [ ] Rejected items have brief rejection reason
- [ ] Acceptance rate is reasonable (<50% of candidates)
- [ ] Accepted items formatted for reuse in future sessions

---

## Integration

- **Use from**: Any session that produces findings worth preserving. Typically run at session end or after major analytical skill chains.
- **Routes to**: /want (goals), /diagnose (problems), /claim or /search (questions), /decide (decisions), /av (assumptions), /araw (findings for further testing)
- **Differs from**: /ver (verifies individual claims, /fb filters session-level feedback), /val (validates deliverables, /fb validates feedback items), /evaluate (assesses work quality, /fb assesses feedback quality)
- **Complementary**: /ver (GOSM grounding markers feed into /fb's grounding check), /araw (stress-test accepted items further), /prr (review the feedback process itself)

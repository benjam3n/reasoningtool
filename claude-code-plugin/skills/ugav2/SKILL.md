---
name: "ugav2 - Universal Goal Analysis v2 (Actionable Questions)"
description: "Goal analysis focused on generating fact-yielding questions. Each question must produce a testable fact, not a vague reflection. Consolidated into /uga but usable standalone for question-focused goal analysis."
tier: "tier4"
categories: ["Goal Processing"]
tags: ["goal", "questions", "actionable", "analysis"]
output:
  format: "prose"
---

# Universal Goal Analysis v2: Actionable Fact-Yielding Questions

**Input**: $ARGUMENTS

---

## Core Principles

1. **Every question must yield a fact.** A question like "what do you want?" yields a feeling. A question like "what measurable outcome would make you say this succeeded?" yields a testable fact. v2's entire contribution is this distinction. If a question can be answered with "I feel like..." it is not actionable.

2. **Questions precede analysis.** Do not analyze the goal until you have asked fact-yielding questions about it. Analysis without facts is speculation dressed as insight. The question phase is not warmup — it IS the work.

3. **Binary questions outperform open questions.** "Is there a deadline?" yields a fact. "Tell me about the timeline" yields rambling. Start binary, then drill into the yes/no answers.

4. **Unanswerable questions are findings.** When a question cannot be answered, that gap IS the most important output. A goal with three unanswerable questions is a goal with three unresolved risks.

5. **Questions must be ordered by dependency.** Ask existence questions before detail questions. "Is there a budget?" before "How large is the budget?" Skipping existence questions is the primary way analyses hallucinate structure that isn't there.

---

## Phase 1: Goal Capture

State the goal as received, then immediately test its specificity.

```
[A] STATED_GOAL: [verbatim from user]
[B] SPECIFICITY_TEST:
    - Can you measure completion? [Y/N — if N, goal is vague]
    - Is there a deadline? [Y/N — if N, no urgency signal]
    - Is there one actor or many? [1/many — affects delegation questions]
    - Has this been attempted before? [Y/N — if Y, ask what happened]
[C] GOAL_CLASS: [vague | directional | specific | already-in-progress]
```

---

## Phase 2: Fact-Yielding Question Battery

For each category, ask binary existence questions first, then detail questions only where existence = Y.

### 2a. Outcome Facts

```
[D] OUTCOME_QUESTIONS:
    1. Is there a measurable definition of success? → [Y/N] → [if Y: what?]
    2. Is there a measurable definition of failure? → [Y/N] → [if Y: what?]
    3. Is there a minimum viable outcome (less than full success but still worth it)? → [Y/N]
    4. Will someone other than you judge success? → [Y/N] → [if Y: who? what criteria?]
    5. Is there a point of no return? → [Y/N] → [if Y: when?]
```

### 2b. Resource Facts

```
[E] RESOURCE_QUESTIONS:
    1. Is there a budget? → [Y/N] → [if Y: how much?]
    2. Is there a time limit? → [Y/N] → [if Y: what?]
    3. Are there people available to help? → [Y/N] → [if Y: how many? what skills?]
    4. Is there existing work to build on? → [Y/N] → [if Y: what state is it in?]
    5. Are there tools/systems already in place? → [Y/N] → [if Y: what?]
```

### 2c. Constraint Facts

```
[F] CONSTRAINT_QUESTIONS:
    1. Is there something that cannot change? → [Y/N] → [if Y: what?]
    2. Is there a dependency on someone else's action? → [Y/N] → [if Y: who? what?]
    3. Is there a regulatory or policy constraint? → [Y/N] → [if Y: what?]
    4. Is there a technical constraint? → [Y/N] → [if Y: what?]
    5. Is there a political/organizational constraint? → [Y/N] → [if Y: what?]
```

### 2d. Context Facts

```
[G] CONTEXT_QUESTIONS:
    1. Has this goal been attempted before? → [Y/N] → [if Y: what happened?]
    2. Is someone else pursuing this same goal? → [Y/N] → [if Y: who? are they ahead?]
    3. Is this goal instrumental to a deeper goal? → [Y/N] → [if Y: what's the real goal?]
    4. Was there a triggering event? → [Y/N] → [if Y: what? when?]
    5. Is there an alternative approach being considered? → [Y/N] → [if Y: what?]
```

---

## Phase 3: Gap Analysis

```
[H] UNANSWERED_QUESTIONS: [list every question from Phase 2 that could not be answered]
[I] RISK_RANKING: [rank unanswered questions by: if this assumption is wrong, how bad?]
[J] FACT_SUMMARY:
    KNOWN_FACTS: [N]
    UNKNOWN_FACTS: [M]
    RATIO: [N/(N+M)] — below 0.5 = goal is under-specified
```

---

## Phase 4: Actionable Recommendation

Based on the fact/gap ratio, recommend next step:

```
[K] RECOMMENDATION:
    IF ratio >= 0.7: Goal is well-specified → proceed to strategy (/uga Step 4)
    IF ratio 0.4-0.7: Goal has gaps → answer top 3 unknowns before strategizing
    IF ratio < 0.4: Goal is under-specified → return to goal clarification (/gu)

[L] TOP_3_UNKNOWNS_TO_RESOLVE:
    1. [question] — how to answer: [specific action]
    2. [question] — how to answer: [specific action]
    3. [question] — how to answer: [specific action]
```

---

## Phase 5: Report

```
UGA v2 FACT-YIELDING ANALYSIS:
Goal: [stated goal]
Specificity: [vague/directional/specific/in-progress]

Known facts: [N] | Unknown: [M] | Ratio: [X]

Key facts established:
- [fact 1]
- [fact 2]
- [fact 3]

Critical unknowns:
1. [unknown] — risk if wrong: [consequence]
2. [unknown] — risk if wrong: [consequence]
3. [unknown] — risk if wrong: [consequence]

Recommendation: [proceed / resolve gaps / clarify goal]
Next action: [specific action to take]
```

→ INVOKE: /uga $ARGUMENTS (for full analysis after fact-gathering)

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Reflective questions** | Question can be answered with "I feel like..." | Rewrite to demand a measurable fact |
| **Skipping existence checks** | Asking "how large is the budget?" without first asking "is there a budget?" | Always binary first, detail second |
| **Accepting vague answers** | "The timeline is flexible" treated as an answer | Push: "Is there a date after which this loses value? Y/N" |
| **Question overload** | 40+ questions with no prioritization | Cap at 20, rank by dependency and risk |
| **Analysis before facts** | Strategizing when ratio < 0.4 | Block strategy until ratio >= 0.4 |
| **Ignoring gaps** | Unanswered questions not flagged as risks | Every unanswered question is a finding |

---

## Depth Scaling

| Depth | Questions Asked | Gap Analysis | Recommendation |
|-------|----------------|-------------|----------------|
| 1x | 10 binary questions across 2 categories | List unknowns | Single next step |
| 2x | 20 questions across all 4 categories | Ranked unknowns with risk | Top 3 actions |
| 4x | 20 questions + 10 follow-up detail questions | Risk-scored gap matrix | Sequenced action plan |
| 8x | Full battery + custom domain questions | Gap dependency tree | Full strategy with contingencies |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Every question is fact-yielding (not reflective)
- [ ] Existence questions asked before detail questions
- [ ] Unanswered questions explicitly listed as findings
- [ ] Fact/unknown ratio calculated
- [ ] Top 3 unknowns identified with resolution methods
- [ ] Recommendation matches the ratio threshold
- [ ] No strategy offered when ratio < 0.4

---

## Integration

- **Consolidated into**: `/uga` (which includes v2's question approach in Steps 1-2)
- **Use standalone when**: You need pure fact-gathering before analysis
- **Routes to**: `/uga` (full analysis), `/gu` (goal clarification if under-specified)
- **Invoked by**: Users wanting question-first goal analysis
- **Differs from /uga**: /uga runs the full 17-step framework; ugav2 focuses exclusively on fact-yielding questions
- **Differs from /gu**: /gu clarifies what the goal IS; ugav2 establishes what facts support it

---
name: "gen - Generate - Diverse Candidate Production"
description: Produce diverse candidate solutions. Given constraints and purpose, generate N candidates ranging from conventional to extreme. The creative primitive that other skills call.
---

# Generate - Diverse Candidate Production

**Input**: $ARGUMENTS

---

## Core Principles

1. **Diversity over quantity.** Three genuinely different candidates beat ten variations on the same idea. Every candidate set must include at least one conventional, one unconventional, and one extreme option.

2. **Artifacts, not labels.** Produce the actual thing — code, prose, layout, strategy document — not just a name for it. "Compress the hero section" is a label. Actual compressed hero HTML is an artifact.

3. **Constraints are generative.** Don't fight constraints — use them. Each constraint eliminates bad options and makes good options easier to find. Ask: "Given THESE constraints, what becomes possible?"

4. **Separate generation from evaluation.** Generate freely first. Don't self-censor during generation. Evaluation comes after (use `/cri` or `/cmp`).

5. **Surprise yourself.** If every candidate feels obvious, you haven't explored far enough. At least one candidate should make you think "that's weird but it might work."

---

## The Process

### 1. Frame the Generation

What am I producing? What constraints apply? What purpose does it serve?

```
DOMAIN: [what kind of thing — code, prose, design, strategy, etc.]
PURPOSE: [what it must accomplish]
CONSTRAINTS: [hard limits — technical, resource, time, audience]
QUALITY CRITERIA: [how we'll know if it's good — can reference /cri]
```

### 2. Generate Candidates

Produce at minimum 3 candidates. For complex problems, 5-7.

**Required diversity:**

| Slot | Description | Example |
|------|-------------|---------|
| **Conventional** | Best practice. What an expert would do. Safe, proven. | Standard grid layout with hero + cards |
| **Unconventional** | Breaks one assumption. Surprising but defensible. | Single continuous scroll, no pages |
| **Extreme** | Breaks multiple assumptions. Might fail, might be brilliant. | No visual design at all — CLI interface |

**Techniques for generating unconventional/extreme candidates:**
- Invert the strongest assumption ("What if we did the OPPOSITE?")
- Import from another domain ("How would a game designer solve this?")
- Remove the most obvious element ("What if there's no navigation?")
- Maximize a constraint ("What if we had to do this in 10 lines?")
- Combine two unrelated approaches ("What if this was both a tool AND a game?")

### 3. For Each Candidate

Produce the actual artifact (or as much as scope allows):
- Code → write the code
- Prose → write the text
- Design → write the CSS/HTML or describe with specific values
- Strategy → write the plan with specific actions
- Architecture → draw the diagram or describe specific components

Include a brief rationale (2-3 sentences): what's the core idea and why might it work?

### 4. Tag for Evaluation

Don't evaluate yet. Tag each candidate for downstream evaluation:

```
CANDIDATES PRODUCED: [N]
- [1] CONVENTIONAL: [brief description]
- [2] UNCONVENTIONAL: [brief description]
- [3] EXTREME: [brief description]
[- additional candidates if produced]

READY FOR: /cri or /cmp
```

---

## Domain Adaptation

| Domain | Artifact Form | Diversity Lever |
|--------|--------------|-----------------|
| **Web/UI** | HTML + CSS (or specific values) | Layout structure, interaction model, information density |
| **Writing** | Actual prose (paragraph+) | Voice, structure, argument approach |
| **Code** | Working code | Architecture, algorithm, API shape |
| **Strategy** | Action plan with specifics | Risk posture, timeline, resource allocation |
| **Product** | Feature spec or prototype | User model, core loop, monetization |

---

## When Called by Other Skills

Generate is a primitive. When called by UAUA (G1 step), design, or other skills:
- Accept constraints from the calling skill
- Produce artifacts in the format the caller needs
- Return candidates without evaluation (the caller evaluates)

---

## Common Failure Modes

| Failure | Fix |
|---------|-----|
| All candidates are variations of the same idea | Force one that inverts the core assumption |
| Candidates are labels, not artifacts | Write the actual thing, not a description of it |
| Self-censoring ("that's too weird") | The extreme slot exists for this. Use it. |
| Too many candidates, all mediocre | Reduce to 3, increase quality of each |
| Constraints ignored | Reread constraints before each candidate |

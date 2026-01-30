---
name: cri
description: Structured evaluation using gestalt impression + analytical decomposition. Impression first, then analysis, then check for divergence.
---

# Critique - Impression-First Evaluation

**Input**: $ARGUMENTS

---

## Core Principles

1. **Impression before analysis.** State your overall feeling about the thing BEFORE decomposing it. The impression captures relational/compositional quality that analysis often misses.

2. **Divergence is signal.** When your impression says "this is bad" but your analysis says "each part is fine," the impression is usually right. Something is wrong in the RELATIONSHIPS between parts. Investigate.

3. **Both channels.** Every artifact produces utility (does it work?) and signal (what does it communicate about the maker?). Evaluate both.

4. **Specificity over verdict.** "This is bad" is useless. "The hierarchy is unclear because the H2 and body text are too similar in size" is actionable. Always say WHAT is wrong and WHY.

5. **Standards are domain-relative.** "Good" means different things in different domains. State what standard you're evaluating against. A startup MVP and a luxury brand have different quality bars.

---

## The Process

### 1. State the Impression

Before any analysis, answer honestly:

```
OVERALL IMPRESSION: [What's your gut reaction? Good/bad/mixed? What feeling does it evoke?]
CONFIDENCE: [How sure are you? HIGH = clear reaction, LOW = ambiguous]
```

Don't justify yet. Just state it.

### 2. Identify the Standard

What are we comparing against?

```
DOMAIN: [what kind of thing is this?]
STANDARD: [what does "good" mean here?]
EXEMPLARS: [1-3 examples of what good looks like in this domain]
```

### 3. Analytical Decomposition

Evaluate against the relevant principles for this domain. Not all apply to every domain.

**Universal (always check):**
- PURPOSE: Does every element serve the purpose? Anything purposeless?
- HIERARCHY: Is importance clear? Can you tell what matters most?
- COHERENCE: Do the parts form a unified whole?
- COGNITIVE COST: How much effort does this require to understand/use?

**For design/visual:**
- GROUPING: Related things close, unrelated far?
- RHYTHM: Consistent spacing/proportion system?
- CONVENTION: Following standards unless breaking them serves communication?
- CONTRAST: Sufficient difference between importance levels?

**For writing:**
- CLARITY: Does each sentence say what it means?
- STRUCTURE: Does the argument flow logically?
- VOICE: Is the tone appropriate and consistent?
- READER JOURNEY: Does it answer the reader's questions in the order they arise?

**For code/engineering:**
- CORRECTNESS: Does it work?
- SIMPLICITY: Is this the simplest solution that works?
- MAINTAINABILITY: Can someone else understand and modify this?
- EDGE CASES: Does it handle failure gracefully?

**For strategy:**
- ACTIONABILITY: Can someone actually do this?
- PRIORITIZATION: Is effort directed at highest-impact areas?
- RISK AWARENESS: Are failure modes identified?
- RESOURCE REALITY: Are resource requirements realistic?

### 4. Check for Divergence

```
IMPRESSION vs ANALYSIS:
- ALIGNED: Impression and analysis agree → high confidence in verdict
- DIVERGENT: Impression says X, analysis says Y → investigate why
  - If impression negative but analysis positive: likely a COMPOSITION problem
    (parts are fine individually, but relationships between parts are wrong)
  - If impression positive but analysis negative: likely the analysis is
    catching real issues that don't affect the whole yet (but will over time)
```

When divergent: **state both the impression AND the analysis, with the divergence noted.** Don't force agreement.

### 5. Actionable Verdict

```
VERDICT: [What's the overall assessment?]
STRENGTHS: [What works well — be specific]
ISSUES: [What doesn't work — be specific, say WHY, and suggest fix]
PRIORITY ORDER: [Which issues to fix first, by impact]
```

Every issue must include:
- WHAT is wrong
- WHY it's wrong (which principle it violates)
- HOW to fix it (specific action, not vague direction)

---

## Severity Levels

| Level | Meaning | Action |
|-------|---------|--------|
| **STRUCTURAL** | The foundation is wrong. Fixing details won't help. | Rethink the approach. |
| **SIGNIFICANT** | Important issues but the foundation is sound. | Fix before shipping. |
| **MINOR** | Small issues that reduce quality but don't break anything. | Fix when convenient. |
| **POLISH** | Improvements that move from good to great. | Nice to have. |

---

## When Called by Other Skills

Critique is a primitive. When called by UAUA (A1/A2), design, or other skills:
- Accept the artifact and evaluation context from the caller
- Return: impression, analytical findings, divergence check, prioritized issues
- Be honest. Don't soften critique because another skill called you.

---
name: "deb - Debate Structure"
description: Argues both sides of any position by steelmanning FOR and AGAINST, then identifies where the sides actually disagree and which has better evidence.
output:
  format: "prose"
---

# Debate Structure

**Input**: $ARGUMENTS

---

## Step 1: State the Proposition

Rewrite the input as a clear, debatable proposition. It must be something reasonable people could disagree on.

```
PROPOSITION: [clear statement that can be argued for or against]
DOMAIN: [what field or context this belongs to]
STAKES: [what's at risk — why does this debate matter?]
```

If the input is already a clear proposition, state it and move on.

---

## Step 2: Steelman FOR

Build the strongest possible case in favor. Rules:
- Use the best arguments, not the most common ones
- Include evidence, not just assertions
- Anticipate objections and address them
- Argue as if you genuinely believe this position

```
CASE FOR:

CORE ARGUMENT: [the single strongest reason to believe the proposition]

SUPPORTING ARGUMENTS:
1. [argument + evidence/reasoning]
2. [argument + evidence/reasoning]
3. [argument + evidence/reasoning]

PREEMPTIVE DEFENSE: [the best objection the other side will raise, and why it doesn't hold]
```

---

## Step 3: Steelman AGAINST

Build the strongest possible case against. Same rules — best arguments, real evidence, genuine engagement.

```
CASE AGAINST:

CORE ARGUMENT: [the single strongest reason to reject the proposition]

SUPPORTING ARGUMENTS:
1. [argument + evidence/reasoning]
2. [argument + evidence/reasoning]
3. [argument + evidence/reasoning]

PREEMPTIVE DEFENSE: [the best objection the other side will raise, and why it doesn't hold]
```

---

## Step 4: Find the Real Disagreement

Most debates have surface disagreements hiding deeper ones. Identify where the two sides actually diverge.

```
REAL DISAGREEMENTS:
| Surface disagreement | Actual disagreement | Type |
|---------------------|---------------------|------|
| [what they seem to disagree about] | [what they actually disagree about] | [factual / values / definitions / predictions] |
| ... | ... | ... |
```

Types:
- **Factual**: They disagree about what is true (resolvable with evidence)
- **Values**: They disagree about what matters (not resolvable with evidence)
- **Definitions**: They're using the same word to mean different things
- **Predictions**: They agree on facts but disagree about what will happen

---

## Step 5: Assess the Evidence

Which side has the stronger case?

```
ASSESSMENT:

STRONGER CASE: [FOR / AGAINST / GENUINELY UNCLEAR]

REASONING:
- [key factor that tips the balance]
- [what evidence would change this assessment]

CONFIDENCE: [HIGH / MEDIUM / LOW — how confident is this assessment?]

KEY UNCERTAINTY: [the single thing that, if known, would settle the debate]
```

Be honest. If it's genuinely close, say so. If one side is clearly stronger, say that too.

---

## Step 6: Synthesis

Is there a position that captures the best of both sides?

```
SYNTHESIS: [if possible — a position that resolves the tension]
IF NO SYNTHESIS: [state why the positions are genuinely incompatible and what determines which is correct]
```

---

## Integration

Use with:
- `/conr` -> When the debate is between real people who need resolution
- `/aex` -> When assumptions on either side need explicit testing
- `/ht` -> When a specific claim in the debate needs hypothesis testing
- `/sim` -> When the debate output needs to be simplified for an audience

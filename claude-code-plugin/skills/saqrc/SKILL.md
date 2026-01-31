---
name: saqrc
description: "Rewrite unclear questions by separating intent from target question."
---

# Question Rewrite Chains

**Input**: $ARGUMENTS

---

## Overview

Rewrite unclear questions by separating intent ("what did I mean?") from the target question ("what do I want to answer?"). Many questions in gates and procedures are answerable only if you already know what the author meant — which defeats the purpose.

## Steps

### Step 1: Select Candidate Questions
Extract question-like lines from the target. Prioritize:
- Questions containing parentheses (often hide bundled checks)
- Questions containing "or" (may be asking two different things)
- Questions with implicit conditionals ("if applicable")
- Questions that could be answered "yes" without actually checking anything
- Questions with undefined terms

### Step 2: Assess Clarity
For each candidate, apply the **Stranger Test**: Could a competent stranger answer this question the same way as the author would, without additional interpretation?

| Question | Stranger Test | Failure Mode |
|----------|-------------|-------------|
| [question] | Pass/Fail | [what's unclear] |

### Step 3: Produce Rewrite Chains
For each failing question, iterate:

```
REWRITE CHAIN:
Original: [the question as written]

Round 1:
  What's unclear: [what requires interpretation]
  Intent: [what did the author MEAN to ask]
  Rewrite: [clearer version]

Round 2 (if still unclear):
  What's still unclear: [remaining ambiguity]
  Intent: [what THAT was supposed to mean]
  Rewrite: [even clearer version]

Round 3 (if needed):
  ...

Final: [question that can be answered without interpretation]
```

**Rewrite principles:**
- Replace pronouns with specific nouns
- Replace "it" with what "it" refers to
- Replace "appropriate" with specific criteria
- Replace "adequate" with specific threshold
- Split compound questions into single questions
- Remove parenthetical asides (make them separate questions)
- Add "specifically, [X]" to pin down vague terms

### Step 4: Validate Rewrites
For each final rewrite:
1. Does it preserve the original intent?
2. Can it be answered without interpretation?
3. Is the answer actionable? (Does knowing the answer change what you do?)
4. Is it testable? (Can two people independently answer it and agree?)

### Step 5: Report
```
QUESTION REWRITE AUDIT:
Target: [what was analyzed]
Questions examined: [N]
Failed stranger test: [N]
Rewrites produced: [N]

Top rewrites:
| Original | Rewrite | Why Better |
|----------|---------|-----------|
| [unclear] | [clear] | [what changed] |

Patterns found: [common clarity issues across questions]
```

## When to Use
- When a question cannot be answered without interpreting what was meant
- When questions bundle multiple checks or hide intent in parentheses
- When questions produce guesses rather than clear answers
- → INVOKE: /saaiasa (intent + speech acts) for utterance classification
- → INVOKE: /sadrt (divergence risk test) for testing rewrite quality

## Verification
- [ ] Candidate questions selected by priority (most unclear first)
- [ ] Stranger test applied honestly
- [ ] Rewrite chains iterate until clarity achieved
- [ ] Final rewrites preserve original intent
- [ ] Final rewrites pass stranger test

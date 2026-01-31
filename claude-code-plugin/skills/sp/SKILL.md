---
name: "sp - Steelman Prompt"
description: Improves a prompt before it gets answered. Adds precision, scope, criteria, and failure-proofing without answering the question.
---

# Steelman Prompt

**Input**: $ARGUMENTS

---

## Pass 1: Classify

Identify the prompt type:

| Type | Signal | Example |
|------|--------|---------|
| **CLAIM** | "X is true", "X is better" | "Remote work is more productive" |
| **DECISION** | "Should I X?", "X or Y?" | "Should I switch to Rust?" |
| **DIAGNOSTIC** | "Why is X?", "What's causing X?" | "Why are users churning?" |
| **EXPLORATORY** | "What are the options?", "How could I?" | "What are all the ways to grow revenue?" |

```
TYPE: [CLAIM / DECISION / DIAGNOSTIC / EXPLORATORY]
```

SKIP: If the type is obvious, state it in one line and move on.

---

## Pass 2: Unbundle

Split compound prompts into distinct questions.

```
ORIGINAL: [original prompt]

QUESTIONS FOUND:
1. [question 1]
2. [question 2]
...
```

SKIP: If the prompt contains a single clear question, skip this pass entirely.

---

## Pass 3: Criteria

Add what the prompt is missing based on its type:

- **CLAIM**: What would falsify this? What's the scope? What counts as evidence?
- **DECISION**: What are the criteria? What alternatives exist? What are the constraints?
- **DIAGNOSTIC**: What are the symptoms? What's the timeline? What changed?
- **EXPLORATORY**: What dimensions matter? What are the constraints? When is the list complete?

```
MISSING CRITERIA:
- [criterion 1]
- [criterion 2]
...
```

SKIP: If the prompt already specifies its own success criteria, skip.

---

## Pass 4: Failure-check

Identify 2-3 ways a response could technically satisfy the prompt but be useless.

```
FAILURE MODES:
- A response could [failure mode 1] — fix: [what to add]
- A response could [failure mode 2] — fix: [what to add]
```

SKIP: If the prompt is already tight enough that failure modes are unlikely, skip.

---

## Pass 5: Reconstruct

Combine everything into a single improved prompt. This is the only output the user needs.

Rules:
- Preserve the original intent exactly
- Incorporate criteria and failure-mode fixes directly into the prompt text
- If unbundled, either recombine into one sharper question or list as numbered sub-questions
- Output as a clean copy-paste block
- Keep it concise — the improved prompt should be usable, not an essay

```
IMPROVED PROMPT:

[The steelmanned prompt goes here — ready to copy-paste into a new session]
```

---

## Integration

Use with:
- `/araw` -> Test the improved prompt's core claim
- `/se` -> Enumerate the space the prompt is exploring
- `/gu` -> Clarify goals before steelmanning the prompt

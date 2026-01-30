---
name: high_quality_writing
description: Generative writing tool. Principles for producing clear, compelling, honest prose. Includes weak pattern detection.
---

# High Quality Writing

**Input**: $ARGUMENTS

---

## Core Principles

1. **Write for the reader's journey.** Every piece of writing is a path. The reader arrives with a question or need, and leaves with understanding or capability. Map that journey before writing. What do they know? What do they need? What order do they need it in?

2. **Every section answers a question.** If you can't state what question a section answers, it shouldn't exist. The question should be one the reader actually has at that point in the journey — not one you want to answer.

3. **Specificity is clarity.** Vague writing isn't cautious, it's unclear. "The system is fast" says nothing. "The system responds in <50ms at p99" says everything. When you can't be specific, say why ("response time depends on X, ranging from Y to Z").

4. **Voice matches purpose.** Technical documentation: precise, neutral. Persuasive writing: confident, direct. Narrative: vivid, concrete. Academic: measured, evidence-grounded. Match the voice to what the reader needs to feel.

5. **Delete until it hurts.** First drafts are always too long. Cut everything that doesn't serve the reader's journey. If cutting a sentence doesn't degrade understanding, it was decoration.

6. **Show the reasoning.** Don't just state conclusions — show how you got there. "X is true because Y, which we can see from Z." Readers trust writers who show their work.

---

## The Writing Process

### 1. Define the Reader

```
WHO: [Who is reading this? What do they know already?]
NEED: [What do they need after reading? Knowledge? Capability? Decision?]
STATE BEFORE: [What do they believe/know/feel before reading?]
STATE AFTER: [What should they believe/know/feel after?]
```

### 2. Map the Journey

What questions does the reader have, and in what order?

The reader's questions follow a natural progression:
1. **What is this?** (orientation)
2. **Why should I care?** (relevance)
3. **How does it work?** (mechanism)
4. **How do I use it?** (action)
5. **What if something goes wrong?** (edge cases)
6. **What's next?** (continuation)

Not every piece needs all six. But the ORDER matters — don't explain how to use something before the reader knows what it is or why it matters.

### 3. Write

For each section:
- State the question it answers (even if not as a literal header)
- Answer that EXACT question. A "What?" question needs a definition, not a history. A "How?" question needs steps, not theory.
- Use the simplest structure that serves the answer:
  - Comparison → table
  - Sequence → numbered list
  - Explanation → prose with examples
  - Options → bulleted list with rationale

### 4. Detect Weak Patterns

After drafting, scan for these. Each weakens the writing:

| Pattern | Example | Fix |
|---------|---------|-----|
| **Hedging qualifiers** | "It could potentially perhaps..." | State it or don't. Remove qualifiers. |
| **Defensive negation** | "It's not that X is wrong, it's that..." | Say what IS true directly. |
| **Passive responsibility** | "Mistakes were made" | Say who did what. |
| **False precision** | "Approximately 37.2%" | Use the precision you actually have. |
| **Weasel words** | "Some experts say..." | Which experts? Name them or cut it. |
| **Throat-clearing** | "It's worth noting that..." | Delete the throat-clear. Start with the point. |
| **Nominalization** | "The implementation of the system" | "Implementing the system" — use verbs, not noun-ified verbs. |
| **Summary-like statements** | "As we've discussed..." | Don't summarize, advance. |
| **Sections without questions** | A block of text that doesn't answer anything | Delete or restructure around a reader question. |

### 5. Verify Claims

Every factual claim should be marked:
- `[O: source]` — Observed from a specific source
- `[T: test]` — Testable prediction
- `[D: premises]` — Derived from stated premises

Unmarked claims are opinions. That's fine — but know which is which.

---

## Voice Guide

| Context | Voice | Characteristics |
|---------|-------|-----------------|
| **Technical docs** | Precise, neutral | Short sentences. Active voice. No metaphor. |
| **Essays/arguments** | Confident, direct | State positions. Show reasoning. Acknowledge counterarguments. |
| **Tutorials** | Warm, clear | Second person ("you"). Concrete examples. Celebrate progress. |
| **Academic** | Measured, qualified | Precise hedging (when warranted). Citations. Signal uncertainty honestly. |
| **Narrative** | Vivid, concrete | Sensory detail. Specific scenes. Character action over abstraction. |

---

## Structure Patterns

| Reader Need | Structure |
|-------------|-----------|
| Understand a concept | Definition → Example → Contrast → Edge cases |
| Make a decision | Options → Criteria → Comparison → Recommendation |
| Learn to do something | Goal → Prerequisites → Steps → Verification → Troubleshooting |
| Understand what happened | Context → Events → Consequences → Lessons |
| Be persuaded | Problem → Evidence → Proposed solution → Objections addressed → Call to action |

---

## Pre-Completion Check

- [ ] Reader defined (who, need, before/after states)
- [ ] Every section answers a reader question
- [ ] Questions are in reader's natural order
- [ ] Weak patterns scanned and fixed
- [ ] Voice matches purpose
- [ ] Specific where possible, honest about uncertainty where not

---
name: high_quality_writing
description: "GOSM High Quality Writing procedure with weak pattern detection"
---

# High Quality Writing

---

**Input**: $ARGUMENTS

---

## Core Principle: Quality is Relational

Quality = f(text, reader, context, purpose)

Before writing, specify:
1. **Who** is the reader?
2. **What** should change for them?
3. **What** would prevent that?
4. **What** must be true to prevent failure?

---

## Phase 1: Requirement Definition

Answer these in order:

```
READER: [Who specifically]
CHANGE: [What state change in reader]
FAILURE: [What would cause failure]
MUST: [Necessary conditions - jointly sufficient for success]
VERIFY: [How to check success]
```

---

## Phase 2: Question-Answer Structure

**Every section must answer a question or address an objection the reader has.**

Before writing each section, identify:
1. **What question is the reader asking at this point?**
2. **What objection might they raise?**

If a section doesn't answer a question, it's a summary taking up space. Delete it or reframe it.

| Bad (Summary) | Good (Answers Question) |
|---------------|-------------------------|
| "ARAW explores both branches" | "How does it work?" → "Two branches get explored..." |
| "The tensions library contains 200+ tensions" | "What patterns recur?" → "200+ tensions..." |
| "Philosophy" (section header) | "How do I know my output is trustworthy?" |

**Test**: Can you state the question this section answers? If not, rewrite or delete.

---

## Phase 2b: Answer the Exact Question

**Each section must answer ONLY the question in its header - not a related question.**

Common failure: Answering a different question than the one asked.

| Header | Wrong Answer (Different Question) | Right Answer (Exact Question) |
|--------|-----------------------------------|-------------------------------|
| "What is X?" | "X works by doing Y" (How) | "X is a method for Z" (What) |
| "Why does it work?" | "The process is: 1, 2, 3" (How) | "Because every claim is a guess" (Why) |
| "What can it do?" | "When you're right, know WHY" (Why use it) | "Test hypotheses, expand options" (Capabilities) |

**The test**: Read ONLY the header question, then ONLY the answer. Does the answer directly address that specific question?

If you find yourself answering "how" under "what", or "why use it" under "what can it do" - split into separate sections.

---

## Phase 3: Weak Pattern Detection

**Scan the writing for these weak patterns and strengthen them:**

### Pattern 1: Defensive Negation ("It's not X - it's Y")

**Weak forms:**
- "That's not X - that's Y"
- "It's not X, it's Y"
- "This isn't X - this is Y"
- "Not X but Y"

**Why weak:** Defensive framing concedes ground to the counterargument. The negation makes X salient even while denying it.

**Fix:** Assert Y directly without mentioning X.

| Weak | Strong |
|------|--------|
| "That's not distrust - that's collaboration" | "Both are collaborative acts" |
| "It's not criticism - it's feedback" | "Feedback improves outcomes" |
| "This isn't failure - this is learning" | "Every attempt generates data" |
| "Not a bug but a feature" | "This behavior serves [purpose]" |

**Test:** Remove the negation. Does the assertion stand alone? If not, strengthen the Y claim.

---

### Pattern 2: Hedging Qualifiers

**Weak forms:**
- "I think that..."
- "It seems like..."
- "Perhaps..."
- "Maybe..."
- "Sort of..."
- "Kind of..."

**Why weak:** Signals uncertainty without adding information. Either commit to the claim or explicitly state the uncertainty source.

**Fix:** State claim directly OR specify what would change your confidence.

| Weak | Strong |
|------|--------|
| "I think this is the right approach" | "This approach satisfies [criteria]" |
| "It seems like the API is slow" | "Response times average 2.3s (target: 0.5s)" |
| "Maybe we should refactor" | "Refactoring would enable [benefit]" |

---

### Pattern 3: Passive Responsibility Diffusion

**Weak forms:**
- "Mistakes were made"
- "It was decided that..."
- "There has been..."

**Why weak:** Hides agency. Reader cannot determine who is responsible or accountable.

**Fix:** Name the agent.

| Weak | Strong |
|------|--------|
| "It was decided to delay" | "The team decided to delay" |
| "Mistakes were made" | "I made an error in [specific]" |
| "There has been confusion" | "Users misunderstood [specific feature]" |

---

### Pattern 4: False Precision

**Weak forms:**
- "Exactly 47.3% of users..."
- "In precisely 2.7 days..."
- Numbers with spurious decimal places

**Why weak:** Implies measurement precision that doesn't exist. Undermines credibility.

**Fix:** Match precision to actual measurement confidence.

| Weak | Strong |
|------|--------|
| "47.3% of users" | "About half of users" OR "47% (n=1000, CI: 44-50%)" |
| "2.7 days" | "2-3 days" |

---

### Pattern 5: Weasel Words

**Weak forms:**
- "Some people say..."
- "It is believed that..."
- "Many experts think..."
- "Studies show..."

**Why weak:** Appeals to unnamed authority. Cannot be verified.

**Fix:** Name the source or remove the appeal.

| Weak | Strong |
|------|--------|
| "Studies show..." | "[Author 2024] found..." OR state the finding directly |
| "Many experts believe" | "[Named expert] argues..." OR state the argument |
| "Some say..." | Delete, state your claim directly |

---

### Pattern 6: Excessive Throat-Clearing

**Weak forms:**
- "In order to understand this, we must first..."
- "Before we begin, it's important to note..."
- "As we all know..."

**Why weak:** Delays the point. Reader loses patience.

**Fix:** Start with the point. Add context only if reader needs it to understand.

---

### Pattern 7: Nominalization (Verb→Noun Conversion)

**Weak forms:**
- "The implementation of the feature" → "implementing the feature"
- "Make a decision" → "decide"
- "Conduct an investigation" → "investigate"

**Why weak:** Adds words, removes action.

**Fix:** Use verbs.

---

### Pattern 8: Summary-Like Statements

**Weak forms:**
- "[Method] does X" (describing method from outside)
- "[Method] weights toward X" (meta-commentary about properties)
- "The name sounds X but the operation is Y" (meta-commentary)
- "X means: Y" (explanatory framing)

**Why weak:** Sounds like summarizing something fuller. Implies "there's more detail elsewhere."

**Fix:** Make content the subject, not the method. State principles directly.

| Weak | Strong |
|------|--------|
| "ARAW explores both branches" | "Both branches get explored" |
| "ARAW weights toward completeness" | "Completeness matters" |
| "'ASSUME WRONG' means: explore alternatives" | "ASSUME WRONG = 'what alternatives exist?'" |
| "The method is most useful on X" | "Most useful on X" (or frame as question) |

**Test:** Remove the method name from the sentence. Does it still work? If not, the method was carrying the meaning instead of the content.

---

### Pattern 9: Sections Without Questions

**Weak forms:**
- Section headers that announce topics: "Philosophy", "Overview", "Background"
- Sections that describe features: "The tensions library contains..."
- Sections that summarize: "Key learnings from sessions..."

**Why weak:** Announcements and summaries don't answer reader questions. They take up space.

**Fix:** Reframe as the question the reader is asking:

| Weak Header | Strong Header (Question) |
|-------------|--------------------------|
| "Philosophy" | "How do I know my output is trustworthy?" |
| "Repository Structure" | "Where is everything?" |
| "Tensions Library" | "What patterns recur across domains?" |
| "Extended Examples" | "What domains can I apply this to?" |

**Test:** For every section, can you state "This section answers the question: ___"? If not, rewrite or delete.

---

## Phase 4: Writing

Produce the writing while avoiding weak patterns.

---

## Phase 5: Post-Write Scan

Re-scan for weak patterns introduced during writing. For each found:

```
PATTERN: [Which pattern]
INSTANCE: "[exact weak text]"
FIX: "[stronger version]"
```

---

## Phase 6: Verification

For key claims, add verification markers:

| Marker | Meaning |
|--------|---------|
| [O: source] | Directly observed |
| [T: test] | Tested with results |
| [D: premises] | Derived from verified premises |

---

## Quick Reference: Weak→Strong

| Weak Pattern | Recognition | Fix |
|--------------|-------------|-----|
| Defensive negation | "not X - Y" | Assert Y directly |
| Hedging | "I think", "seems" | Commit or specify uncertainty |
| Passive diffusion | "was done" | Name the agent |
| False precision | Spurious decimals | Match measurement confidence |
| Weasel words | "studies show" | Name source or delete |
| Throat-clearing | Preamble before point | Start with point |
| Nominalization | "the X of Y" | Use verb form |

---

## Output Format

```
WRITING OUTPUT
==============

[The writing itself]

---

PATTERN SCAN
============
Patterns found: [count]
[List any weak patterns found and fixes applied]

VERIFICATION
============
Key claims verified: [count]
[List claims with markers]
```

---
name: "teach - Feynman Explanation"
description: Explains any concept so that someone can actually understand it. Uses the Feynman technique — simple words, clear structure, no hiding behind jargon.
output:
  format: "prose"
---

# Feynman Explanation

**Input**: $ARGUMENTS

---

## Step 1: Identify the Concept

What exactly needs to be explained? Pin it down precisely.

```
CONCEPT: [the thing to explain]
DOMAIN: [field or context it belongs to]
WHY IT MATTERS: [one sentence — why would someone care about understanding this?]
```

---

## Step 2: Assess the Audience

Who is this explanation for? This determines vocabulary and starting point.

```
AUDIENCE: [who — beginner, peer, expert in adjacent field, child, etc.]
THEY ALREADY KNOW: [list 2-3 things you can assume they understand]
THEY DON'T KNOW: [list 2-3 things you cannot assume]
ENTRY POINT: [the familiar concept to build from]
```

If the audience is not specified, default to "smart person with no background in this domain."

---

## Step 3: Explain Simply

Write the explanation following these rules:
- No jargon without immediate definition
- No acronyms
- Use concrete examples, not abstract descriptions
- Use analogies to things the audience already knows
- If a concept has parts, explain them in order of dependency (what you need to know first comes first)
- One idea per paragraph

```
EXPLANATION:

[The plain-language explanation goes here. Start from the entry point and build up.]
```

---

## Step 4: Find the Gaps

Read your explanation as if you were the audience. Look for:

```
GAP CHECK:
- Unexplained leap? [Where you jumped from A to C without B]
- Hidden jargon? [Words that feel simple to you but aren't to the audience]
- Missing "why"? [Where you said what something IS but not why it EXISTS or matters]
- Missing example? [Where an abstract claim needs a concrete case]
```

---

## Step 5: Refine

Fix every gap found in Step 4. Rewrite the explanation.

```
REFINED EXPLANATION:

[The improved explanation — clean, complete, copy-paste ready]
```

---

## Step 6: Test Question

Generate one question the audience should be able to answer if they understood the explanation. This serves as a self-test.

```
TEST: [question]
EXPECTED ANSWER: [what someone who understood would say]
```

---

## Integration

Use with:
- `/anag` -> Generate a detailed analogy to anchor the explanation
- `/sim` -> When the explanation itself needs to be shorter
- `/sum` -> When the source material needs summarizing before teaching
- `/sp` -> Sharpen the teaching question before building the explanation

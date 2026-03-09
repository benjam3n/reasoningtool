---
name: "sim - Simplification"
description: Takes any complex thing (plan, explanation, process, argument) and strips it to its essential core without losing meaning.
---

# Simplification

**Input**: $ARGUMENTS

---

## Step 1: Identify the Core

What is the single most important thing this is trying to say or do?

```
CORE PURPOSE: [one sentence — what this fundamentally is]
TYPE: [plan / explanation / process / argument / system / other]
```

---

## Step 2: Map the Components

List every distinct element in the input.

```
COMPONENTS:
1. [element] — ESSENTIAL / SUPPORTING / DECORATIVE
2. [element] — ESSENTIAL / SUPPORTING / DECORATIVE
...
```

Classification rules:
- **ESSENTIAL**: Remove it and the meaning changes or the thing breaks
- **SUPPORTING**: Adds clarity or nuance but isn't structurally necessary
- **DECORATIVE**: Adds style, hedging, or filler — safe to cut entirely

---

## Step 3: Cut

Remove all DECORATIVE elements. For each SUPPORTING element, decide: does the audience actually need this, or is it there to make the author feel thorough?

```
REMOVED:
- [element] — reason it's safe to cut
- [element] — reason it's safe to cut
...

KEPT (essential + retained supporting):
- [element]
- [element]
...
```

---

## Step 4: Reconstruct

Rebuild using only the kept elements. Rules:
- Shorter sentences
- No jargon unless the audience expects it
- One idea per sentence
- If it's a process, number the steps
- If it's an argument, state claim then evidence

```
SIMPLIFIED VERSION:

[The simplified output goes here]
```

---

## Step 5: Preservation Check

Verify nothing critical was lost.

```
MEANING PRESERVED?
- Original says X → Simplified says X? [YES / NO — if NO, fix]
- Original scope: [broad/narrow] → Simplified scope: [same / shifted — if shifted, fix]
- Key nuance lost? [If yes, add back the minimum needed]
```

If any check fails, revise the simplified version and show the final output.

---

## Final Output

Present the simplified version as a clean block. If changes were needed from the preservation check, show the corrected version.

---

## Integration

Use with:
- `/sum` -> When you need compression at specific levels rather than simplification
- `/teach` -> When simplification is for the purpose of teaching someone
- `/anag` -> When simplification would benefit from an analogy
- `/sp` -> Simplify a prompt before answering it

---
name: "olst - List Generation"
description: Generates comprehensive, well-organized lists. Takes a topic or scope and produces a structured list that is complete, deduplicated, and formatted for readability.
---

# List Generation

**Input**: $ARGUMENTS

---

## Step 1: Define Scope

Establish what the list covers.

```
TOPIC: [what the list is about]
BOUNDARIES: [what's included / what's excluded]
AUDIENCE: [who will use this list]
PURPOSE: [reference, action items, brainstorming, inventory, etc.]
```

---

## Step 2: Choose Approach

Select the list strategy based on purpose:

| Approach | When to use | Trade-off |
|----------|-------------|-----------|
| **EXHAUSTIVE** | Inventory, audit, compliance | Complete but long |
| **CURATED** | Recommendations, top-N | Selective but opinionated |
| **TIERED** | Priority-ranked options | Structured but requires criteria |
| **CATEGORICAL** | Complex domains | Organized but may overlap |

```
APPROACH: [EXHAUSTIVE / CURATED / TIERED / CATEGORICAL]
RATIONALE: [why this approach fits]
```

---

## Step 3: Generate Items (Breadth-First)

Produce all candidate items before filtering or organizing.

Rules:
- Cast a wide net first — do not self-censor during generation
- Use multiple angles: categories, stakeholders, timeframes, analogies
- Aim for completeness over elegance at this stage

```
RAW ITEMS:
1. [item]
2. [item]
...
```

---

## Step 4: Organize

Arrange items using the best-fit ordering:

- **Alphabetical**: Reference lists, glossaries
- **Priority**: Action items, recommendations
- **Categorical**: Complex domains with natural groupings
- **Chronological**: Processes, timelines, historical items
- **Dependency**: Items that build on each other

```
ORDERING: [method chosen]
```

Apply the ordering to all items. Use headers or groupings if categorical.

---

## Step 5: Deduplicate and Validate

- Remove true duplicates (same item, different wording)
- Merge near-duplicates (combine into one entry with broader scope)
- Check for gaps: are there obvious categories or items missing?
- Validate against scope: remove anything outside boundaries

```
REMOVED: [items cut and why]
GAPS FOUND: [items added to fill holes]
```

---

## Step 6: Format for Readability

Apply formatting rules:
- Consistent item structure (all noun phrases, all sentences, all verb-led)
- Consistent detail level (no mix of one-word and paragraph entries)
- Add brief descriptions if items are ambiguous
- Use numbering if order matters, bullets if it doesn't
- Group with headers if list exceeds 15 items

---

## Step 7: Deliver

Present the final list with:
- A one-line summary of what the list covers
- The organized, formatted list
- A count of total items
- Any caveats about completeness or scope

```
LIST: [topic] ([N] items)

[The formatted list]

COMPLETENESS NOTE: [any caveats]
```

---

## Integration

Use with:
- `/se` -> Enumerate a solution space before listing
- `/omtx` -> Turn the list into a comparison matrix
- `/cmp` -> Compare items from the list
- `/orec` -> Convert list findings into recommendations

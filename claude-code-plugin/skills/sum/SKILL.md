---
name: "sum - Summarization"
description: Structured summarization at multiple compression levels. Produces 1-sentence, 1-paragraph, and 1-page summaries ranked by claim importance.
---

# Summarization

**Input**: $ARGUMENTS

---

## Step 1: Extract Claims

Read the input and list every distinct claim, fact, or point made.

```
CLAIMS:
1. [claim]
2. [claim]
3. [claim]
...
```

---

## Step 2: Rank by Importance

Score each claim on two dimensions:

| Claim | Centrality (1-5) | Novelty (1-5) | Total |
|-------|-------------------|---------------|-------|
| [claim] | [score] | [score] | [sum] |
| ... | ... | ... | ... |

- **Centrality**: How essential is this to the main point? (5 = IS the main point, 1 = tangential)
- **Novelty**: Would the audience be surprised by this? (5 = very, 1 = obvious/assumed)

Sort by total score descending.

---

## Step 3: Compress — Three Levels

### Level 1: One Sentence

Use only the #1 ranked claim. State it as a complete, standalone sentence that someone with no context could understand.

```
ONE SENTENCE:
[sentence]
```

### Level 2: One Paragraph (3-5 sentences)

Use the top 3-5 claims. First sentence = Level 1. Remaining sentences add the next most important claims in descending order. Final sentence = "so what" implication.

```
ONE PARAGRAPH:
[paragraph]
```

### Level 3: One Page (~250 words)

Use all claims scored 5+ total. Organize by logical grouping, not by order of appearance. Include key evidence or examples for the top claims. End with implications or next steps.

```
ONE PAGE:
[page-length summary]
```

---

## Step 4: Verify

For each compression level, check:

```
VERIFICATION:
- Level 1: Does it capture the single most important point? [YES/NO]
- Level 2: Could someone make a decision based on this alone? [YES/NO]
- Level 3: Is anything critical (scored 5+) missing? [YES/NO — list if yes]
```

If any check fails, revise that level.

---

## Final Output

Present all three levels as clean, copy-paste blocks. Label each clearly.

---

## Integration

Use with:
- `/sim` -> When you want to simplify rather than compress
- `/tri` -> When the input contains multiple items that need ranking, not summarizing
- `/pri` -> When the summary reveals items that need prioritization
- `/teach` -> When the summary is meant to help someone learn the material

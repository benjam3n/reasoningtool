---
name: "ggs - Guess Generation → Selection"
description: "Generate exhaustive guesses then systematically select the top 20 for evaluation. Chains /gg into /selection."
output:
  format: "prose"
---

# Guess Generation → Selection

**Input**: $ARGUMENTS

---

## Overview

This skill chains two procedures:
1. **Guess Generation** (`/gg`) — exhaustively generate guesses about the input
2. **Selection** (`/selection`) — evaluate and select from the top 20 guesses

---

## Step 1: Generate Guesses

→ INVOKE: /gg $ARGUMENTS

Complete the full guess generation process. Once finished, collect all generated guesses and proceed to Step 2.

---

## Step 2: Select Top 20

From the guess generation output, identify the **top 20 guesses** by prioritizing:
1. All **CRITICAL** guesses (High Impact × Low Confidence)
2. Then **HIGH-CRUX** guesses
3. Then highest-impact guesses from remaining pool

Compile these 20 guesses into a numbered list.

---

## Step 3: Run Selection

→ INVOKE: /selection [the 20 guesses from Step 2]

Run the full selection process on these 20 guesses: triage, ARAW evaluation of critical items, dependency analysis, selection matrix, and tiered final selection.

---

## Output

The final output should include:
1. **Generation summary** — total guesses generated, coverage metrics
2. **Top 20 selected for evaluation** — the numbered list fed into selection
3. **Full selection output** — triage buckets, ARAW evaluations, selection matrix, tiered results

---

## Execution Checklist

- [ ] Full /gg completed with coverage tracking
- [ ] Top 20 guesses identified and listed
- [ ] Full /selection completed on those 20
- [ ] Tiered selections with next actions provided

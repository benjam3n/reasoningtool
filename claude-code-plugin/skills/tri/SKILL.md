---
name: "tri - Triage"
description: Rapidly sorts multiple problems, tasks, or issues by urgency and importance into a priority matrix with a ranked action list.
output:
  format: "prose"
---

# Triage

**Input**: $ARGUMENTS

---

## Step 1: List All Items

Extract every distinct problem, task, or issue from the input. If items are vague, split them into concrete sub-items.

```
ITEMS:
1. [item]
2. [item]
3. [item]
...
```

---

## Step 2: Classify Urgency

For each item, ask: "What happens if this waits?"

| Level | Definition | Timeframe |
|-------|-----------|-----------|
| **NOW** | Delay causes irreversible damage or missed window | Hours |
| **SOON** | Delay increases cost or risk meaningfully | Days |
| **LATER** | Can wait without meaningful consequence | Weeks/months |
| **NEVER** | Doing this adds no value or is actively harmful | N/A |

```
URGENCY:
1. [item] — [NOW/SOON/LATER/NEVER] — because [one-line reason]
2. [item] — [NOW/SOON/LATER/NEVER] — because [one-line reason]
...
```

---

## Step 3: Classify Importance

For each item, ask: "How much does this matter to the actual goal?"

| Level | Definition |
|-------|-----------|
| **CRITICAL** | Goal fails without this |
| **IMPORTANT** | Goal is significantly worse without this |
| **NICE** | Improves things but goal succeeds without it |
| **IRRELEVANT** | No meaningful connection to the goal |

```
IMPORTANCE:
1. [item] — [CRITICAL/IMPORTANT/NICE/IRRELEVANT] — because [one-line reason]
2. [item] — [CRITICAL/IMPORTANT/NICE/IRRELEVANT] — because [one-line reason]
...
```

---

## Step 4: Priority Matrix

Place each item in the matrix:

|  | NOW | SOON | LATER | NEVER |
|--|-----|------|-------|-------|
| **CRITICAL** | [items] | [items] | [items] | [items] |
| **IMPORTANT** | [items] | [items] | [items] | [items] |
| **NICE** | [items] | [items] | [items] | [items] |
| **IRRELEVANT** | [items] | [items] | [items] | [items] |

---

## Step 5: Ranked Action List

Read the matrix top-left to bottom-right. Output a single ordered list.

```
PRIORITY ORDER:
1. [item] — DO FIRST (critical + now)
2. [item] — DO NEXT (critical + soon / important + now)
3. [item] — SCHEDULE (important + soon)
4. [item] — BACKLOG (later items)
5. [item] — DROP (never / irrelevant)
...

CUTOFF RECOMMENDATION: Items below #[N] can be safely ignored for now.
```

---

## Step 6: Sanity Check

Look at the top 3 items. Ask:
- Is there a dependency? (Does #2 actually need to happen before #1?)
- Is there a quick win hiding lower? (Something that takes 5 minutes but unlocks others?)

If yes, adjust the order and note why.

---

## Integration

Use with:
- `/pri` -> When you need more sophisticated prioritization with weighted criteria
- `/dcp` -> When the top item requires a decision
- `/to` -> When the ranked list needs to become a project plan
- `/rca` -> When a CRITICAL+NOW item needs root cause analysis before action

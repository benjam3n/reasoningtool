---
name: "immg - Immediate Gap Analysis"
description: Find what's obviously missing RIGHT NOW. Fast, ruthless prioritization of urgent gaps in the current state.
---

# Immediate Gap Analysis

**Input**: $ARGUMENTS

---

## Step 1: Survey Current State

Take a rapid inventory of what exists right now.

```
CURRENT STATE:
- [Component/area 1]: [status]
- [Component/area 2]: [status]
- [Component/area 3]: [status]
...
```

Rules:
- Describe what IS, not what should be
- Keep each entry to one line
- Focus on the domain specified in the input
- If the input is vague, ask what system/project/area to survey

---

## Step 2: Identify Urgent Gaps

List what is obviously missing, broken, or incomplete RIGHT NOW.

```
URGENT GAPS:
1. [Gap]: [Why it's urgent]
2. [Gap]: [Why it's urgent]
3. [Gap]: [Why it's urgent]
...
```

Rules:
- "Urgent" means: causing harm now, blocking progress now, or will cause harm within days
- If it can wait a month, it is NOT urgent — discard it
- If it's a nice-to-have, it is NOT a gap — discard it

---

## Step 3: Classify by Severity

Sort gaps into three tiers:

```
CRITICAL (blocking or causing active harm):
- [gap]

SERIOUS (degrading quality or creating risk):
- [gap]

NOTABLE (visible absence but survivable):
- [gap]
```

Rules:
- Critical means someone/something is stuck or damaged right now
- Serious means measurable negative impact but not a showstopper
- Notable means you notice it's missing but operations continue
- If nothing is critical, say so — do not inflate

---

## Step 4: Recommend Immediate Fixes

For each critical and serious gap, prescribe the minimum viable fix.

```
IMMEDIATE FIXES:
1. [Gap] -> [Minimum fix] | Effort: [hours/days] | Owner: [who should do this]
2. [Gap] -> [Minimum fix] | Effort: [hours/days] | Owner: [who should do this]
...
```

Rules:
- Minimum viable fix, not ideal fix
- Time estimate should be honest, not optimistic
- If owner is unknown, say "unassigned"
- Order by severity first, then by effort (quick wins first within same severity)

---

## Step 5: Ignore List

Explicitly state what you looked at and chose NOT to flag.

```
EXPLICITLY IGNORED (not urgent):
- [Thing that might seem like a gap but isn't urgent]
- [Thing that's a long-term improvement, not a gap]
...
```

This prevents the analysis from silently growing scope later.

---

## Output Summary

```
IMMEDIATE GAP ANALYSIS:
- Gaps found: [count]
- Critical: [count] | Serious: [count] | Notable: [count]
- Top fix: [the single most important thing to do right now]
- Estimated effort for all critical fixes: [total time]
```

---

## Integration

Use with:
- `/stcc` -> After fixing gaps, complete the partially-built clusters
- `/de` -> Turn fixes into a structured delivery plan
- `/to` -> Sequence the fixes into a task order
- `/rca` -> If a gap keeps reappearing, find the root cause

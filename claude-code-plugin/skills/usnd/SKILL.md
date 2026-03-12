---
name: "usnd - User-Need Discovery"
description: Discover what users actually need versus what they say they need. Observes behavior, identifies pain points, maps workarounds, traces root desires, validates with evidence, and outputs a need hierarchy.
output:
  format: "prose"
---

# User-Need Discovery

**Input**: $ARGUMENTS

---

## Step 1: Observe Behavior

Identify what users actually do, not just what they report.

```
CONTEXT: [the product/service/system being analyzed]
TARGET USERS: [who we're analyzing]

OBSERVED BEHAVIORS:
1. [behavior] — Frequency: [how often] — Context: [when/where]
2. [behavior] — Frequency: [how often] — Context: [when/where]
...

STATED NEEDS (what users say):
1. [stated need]
2. [stated need]
...
```

---

## Step 2: Identify Pain Points

Find where users experience friction, frustration, or failure.

```
PAIN POINTS:
1. [pain point] — Severity: [HIGH/MED/LOW] — Evidence: [what indicates this]
2. [pain point] — Severity: [HIGH/MED/LOW] — Evidence: [what indicates this]
...

SILENT PAIN (users don't complain but behavior shows struggle):
1. [pain point] — Behavioral signal: [what reveals it]
...
```

---

## Step 3: Map Current Workarounds

Workarounds reveal unmet needs more reliably than surveys.

```
WORKAROUNDS:
1. [workaround] — What it bypasses: [the gap] — Cost to user: [effort/risk]
2. [workaround] — What it bypasses: [the gap] — Cost to user: [effort/risk]
...

TOOLS USERS COMBINE: [external tools or hacks used to fill gaps]
```

---

## Step 4: Trace to Root Desires

Use the "five whys" approach to get from surface needs to root desires.

```
NEED TRACING:
Surface: [what they asked for]
  → Why? [reason]
    → Why? [deeper reason]
      → Why? [deeper still]
        → ROOT DESIRE: [fundamental need]

REPEATED ROOT DESIRES:
1. [root desire] — Surfaces as: [list of surface needs it generates]
2. [root desire] — Surfaces as: [list of surface needs it generates]
...
```

---

## Step 5: Validate with Evidence

Check each discovered need against available evidence.

```
VALIDATION:
| Need | Evidence Type | Strength | Source |
|------|--------------|----------|--------|
| [need] | [behavioral/stated/inferred] | [STRONG/MODERATE/WEAK] | [source] |
...

CONFIDENT NEEDS (strong evidence):
- [need]: [evidence summary]

HYPOTHESIZED NEEDS (needs more data):
- [need]: [what evidence would confirm/deny]
```

---

## Step 6: Output Need Hierarchy

Organize needs into a structured hierarchy from fundamental to surface-level.

```
NEED HIERARCHY:

TIER 1 — Core Needs (non-negotiable):
1. [need] — If unmet: [consequence]

TIER 2 — Performance Needs (more is better):
1. [need] — Current satisfaction: [level]

TIER 3 — Delight Needs (unexpected value):
1. [need] — Opportunity: [what's possible]

BIGGEST GAP: [the most impactful unmet need]
BIGGEST SURPRISE: [the need most different from stated needs]
RECOMMENDED ACTION: [what to do with these findings]
```

---

## Integration

Use with:
- `/pusr` -> Deep-dive into power user needs specifically
- `/nusr` -> Deep-dive into new user needs specifically
- `/gapf` -> Find gaps between discovered needs and current offerings

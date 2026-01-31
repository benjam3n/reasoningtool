---
name: gaca
description: "Convert gates from yes/no vibe checks into explicit, checkable claim-interfaces."
---

# Gate As Claim Audit

**Input**: $ARGUMENTS

---

## Overview

Convert gates from "yes/no vibe checks" into explicit, checkable claim-interfaces. A gate that can be passed by saying "yes, looks good" is not a gate — it's a suggestion. Real gates require evidence.

## Steps

### Step 1: Extract Gate Claims
For each gate in the target:
1. List the gate ID/name
2. List the question or criterion
3. List the evaluation criteria and pass/fail branches
4. Identify which field is the actual decision hook (what determines pass/fail)

### Step 2: Classify Answer-Interface
For each gate entry, classify what kind of answer it actually requires:

| Interface Type | Definition | Example | Checkable? |
|---------------|-----------|---------|-----------|
| **Definition** | What does term X mean? | "Is the goal clear?" | Only if "clear" is defined |
| **Observation** | What do you see? | "Are tests passing?" | Yes — look at test results |
| **Provenance** | What source supports this? | "Is the claim verified?" | Only if verification source specified |
| **Measurement** | What metric and value? | "Is performance adequate?" | Only if metric and threshold defined |
| **Decision** | What choice was made and why? | "Was the approach selected?" | Only if selection criteria exist |

### Step 3: Identify Vibe-Check Gates
Flag gates that can be passed WITHOUT substantive content:

**Vibe-check indicators:**
| Indicator | Example | Problem |
|-----------|---------|---------|
| "Does the [document] exist?" | "Is there a risk assessment?" | Existence ≠ quality |
| "Was [process] done?" | "Was the design reviewed?" | Process ≠ outcome |
| "Is [quality] adequate?" | "Is the plan complete?" | No standard for "adequate" |
| Binary on continuous | "Yes/no on a spectrum question" | Loses nuance |
| Self-certification | "Do you believe...?" | Fox guarding henhouse |

### Step 4: Convert to Claim-Interfaces
For each vibe-check gate, rewrite as explicit claims:

**Before:** "Is the risk assessment complete?"
**After:**
```
Gate: Risk Assessment Completeness
Claims:
1. "At least 5 risks are identified" — check: count entries
2. "Each risk has likelihood AND severity score" — check: inspect each entry
3. "Top 3 risks have mitigation plans" — check: verify plans exist with specific actions
4. "No category from the standard risk taxonomy is unrepresented" — check: compare against taxonomy
```

Each claim should be:
- Specific (not vague)
- Observable (can be checked by looking at artifacts)
- Binary per claim (each claim is clearly true or false)
- Independent (one claim failing doesn't affect others)

### Step 5: Design Minimum Checks
For each converted gate, define the minimum check that ensures content (not just format):

```
GATE: [name]
Pass requires ALL of:
1. [claim] — verified by: [how to check]
2. [claim] — verified by: [how to check]
3. [claim] — verified by: [how to check]

Evidence required: [what must exist, not just what must be claimed]
Verifier: [who checks — must be someone other than the creator]
```

### Step 6: Identify Passable-Without-Content Gates
The most dangerous gates: ones that can be satisfied by formatting alone.

| Gate | Can Be Gamed By | Fix |
|------|----------------|-----|
| [gate] | [how to pass without substance] | [what would prevent gaming] |

### Step 7: Report
```
GATE AS CLAIM AUDIT:
Gates audited: [N]

| Gate | Current Type | Vibe Check? | Claims After Conversion |
|------|-------------|------------|----------------------|
| [gate] | [interface type] | Y/N | [N claims] |

Vibe-check gates found: [N] of [total]
Passable-without-content: [N] — CRITICAL to fix

Conversion queue:
1. [gate] — [why priority] — [N claims needed]

Total claims produced: [N] (replacing [N] vague questions)
```

## When to Use
- When a gate is used as a pass/fail decision point
- When gate questions feel interpretable or "easy to say yes to"
- When a gate is satisfied by formatting rather than content
- → INVOKE: /gee (gate execution engine) for running converted gates
- → INVOKE: /sapea (executability audit) for checking converted gates work

## Verification
- [ ] All gates extracted with decision hooks identified
- [ ] Answer-interface classified for each gate
- [ ] Vibe-check gates identified honestly
- [ ] Claims are specific, observable, binary, and independent
- [ ] Passable-without-content gates flagged as critical
- [ ] Each converted gate has a defined verification method

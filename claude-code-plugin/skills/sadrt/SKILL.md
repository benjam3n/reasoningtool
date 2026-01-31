---
name: sadrt
description: "Estimate where two independent executors would diverge when applying the same gate/procedure to the same input."
---

# Divergence Risk Test

**Input**: $ARGUMENTS

---

## Overview

Estimate where two independent executors would diverge when applying the same gate/procedure to the same input. If a procedure produces different outputs depending on who runs it, it's not reliable enough to be a standard.

## Steps

### Step 1: Identify Divergence Triggers
For the target procedure/gate, flag potential divergence sources:

| Trigger Type | What to Look For | Example |
|-------------|-----------------|---------|
| Undefined terms | Key nouns without definitions | "adequate" — adequate by whose standard? |
| Bundled questions | Multiple checks in one | "Is it complete and correct?" — could disagree on either |
| Non-operational criteria | Can't be checked mechanically | "Does it feel right?" |
| Missing answer-interface | No way to look up the answer | "Is the market ready?" — how to check? |
| Ambiguous stopping rules | No clear "done" signal | "Analyze until satisfied" |
| Implicit ordering | Steps that could be done in different orders with different results | "Consider A and B" — which first? |
| Subjective thresholds | Numbers without benchmarks | "Enough evidence" — how much? |

### Step 2: Simulate Two Executors
For each trigger found, imagine two competent but independent executors:

**Executor A:** Interprets conservatively, applies strict standards, focuses on completeness
**Executor B:** Interprets pragmatically, applies reasonable standards, focuses on efficiency

For each trigger:
| Trigger | A's Interpretation | B's Interpretation | They Agree? |
|---------|-------------------|-------------------|------------|
| [trigger] | [A reads it as...] | [B reads it as...] | Y/N |

### Step 3: Rate Divergence Risk
For each disagreement:

| Disagreement | Impact | Likelihood | Risk Level |
|-------------|--------|-----------|-----------|
| [where they diverge] | How different are the outputs? (H/M/L) | How likely is this divergence? (H/M/L) | [H×H=Critical, etc.] |

### Step 4: Propose Fixes
For each divergence risk:

| Risk | Fix Type | Proposed Fix |
|------|---------|-------------|
| Undefined term | Define | "[term] means [specific definition]" |
| Bundled question | Split | Separate into independent checks |
| Non-operational | Operationalize | Replace with specific, checkable criterion |
| Missing interface | Add reference | "Check using [method/source]" |
| Ambiguous stopping | Add rule | "Stop when [specific condition]" |
| Subjective threshold | Quantify | "At least [N] items/sources/examples" |

### Step 5: Validate Fixes
After proposing fixes, re-run the executor simulation:
1. Would A and B now agree?
2. Did the fix introduce new ambiguity?
3. Is the fix practical (not so rigid it prevents judgment)?

### Step 6: Report
```
DIVERGENCE RISK TEST:
Target: [what was tested]
Triggers found: [N]

Risk assessment:
| # | Trigger | Risk Level | Fix |
|---|---------|-----------|-----|
| 1 | [trigger] | [Critical/High/Medium/Low] | [proposed fix] |

Divergence hotspots: [sections with most triggers]
Estimated executor agreement: [%] before fixes, [%] after fixes

Priority fixes: [top 3 most impactful]
```

## When to Use
- When you want repeatability across executors (human, AI, future you)
- When a gate/procedure is central to enforcement
- When disagreements keep appearing in review
- → INVOKE: /sapea (executability audit) for deeper executability check
- → INVOKE: /saqrc (question rewrite chains) for fixing unclear questions

## Verification
- [ ] Multiple trigger types checked
- [ ] Two-executor simulation performed
- [ ] Divergence risk rated by impact and likelihood
- [ ] Fixes proposed for high-risk triggers
- [ ] Fixes validated (don't introduce new divergence)

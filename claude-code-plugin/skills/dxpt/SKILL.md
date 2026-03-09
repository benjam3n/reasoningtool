---
name: "dxpt - Domain Expert Assessment"
description: Evaluate quality from a domain expert's perspective. Identifies the domain, checks for oversimplification, verifies terminology, assesses depth, identifies missing nuance, and flags misleading content.
---

# Domain Expert Assessment

**Input**: $ARGUMENTS

---

## Step 1: Identify the Domain

Establish the relevant domain and the expert lens to apply.

```
SUBJECT: [what is being evaluated]
PRIMARY DOMAIN: [the main field of expertise needed]
ADJACENT DOMAINS: [related fields that inform evaluation]
EXPERT LEVEL NEEDED: [practitioner / specialist / researcher]

DOMAIN CHARACTERISTICS:
- Maturity: [established / evolving / nascent]
- Consensus level: [high agreement / active debate / fragmented]
- Key frameworks: [dominant models or theories in this domain]
- Common misconceptions: [what non-experts typically get wrong]
```

---

## Step 2: Check for Oversimplification

Identify where complexity has been reduced to the point of inaccuracy.

```
OVERSIMPLIFICATION CHECK:
1. [claim/statement]
   Simplified version: [what was said]
   Full picture: [what an expert would say]
   Severity: [HARMLESS / MISLEADING / WRONG]
   Fix: [how to add nuance without losing accessibility]

2. [claim/statement]
   Simplified version: [what was said]
   Full picture: [full expert view]
   Severity: [level]
   Fix: [suggestion]

ACCEPTABLE SIMPLIFICATIONS:
- [simplification]: OK because [audience/context justifies it]

DANGEROUS SIMPLIFICATIONS:
- [simplification]: Leads to wrong conclusions because [reason]
```

---

## Step 3: Verify Terminology

Check whether domain-specific terms are used correctly.

```
TERMINOLOGY AUDIT:
| Term Used | Correct Usage? | Standard Term | Notes |
|-----------|---------------|---------------|-------|
| [term 1] | [YES / NO / CLOSE] | [correct term] | [detail] |
| [term 2] | [YES / NO / CLOSE] | [correct term] | [detail] |

MISUSED TERMS:
- [term]: Used to mean [X], actually means [Y] in this domain

MISSING TERMS (should have been used):
- [concept] should be called [correct term] — matters because [reason]

INFORMAL VS FORMAL: [is the register appropriate for the audience?]
```

---

## Step 4: Assess Depth of Treatment

Evaluate whether the topic is covered with sufficient depth.

```
DEPTH ASSESSMENT:
| Topic Area | Depth Provided | Depth Needed | Gap |
|-----------|---------------|-------------|-----|
| [area 1] | [surface / moderate / deep] | [what's appropriate] | [description] |
| [area 2] | [surface / moderate / deep] | [what's appropriate] | [description] |

UNDEREXPLORED AREAS:
1. [area] — Why it needs more depth: [reason]
   Key points missing: [specifics]

OVEREXPLORED AREAS (unnecessarily detailed):
1. [area] — Why it's too deep: [reason]
   Could be reduced to: [summary]

APPROPRIATE DEPTH OVERALL: [SHALLOW / ADEQUATE / THOROUGH / EXCESSIVE]
```

---

## Step 5: Identify Missing Nuance

Find important caveats, exceptions, and context that experts would flag.

```
MISSING NUANCES:
1. [nuance] — Matters because: [impact on understanding]
   Expert would add: [what they'd say]

2. [nuance] — Matters because: [impact on understanding]
   Expert would add: [what they'd say]

MISSING CAVEATS:
- [statement] needs caveat: [what's true only under certain conditions]

MISSING CONTEXT:
- [claim] omits: [historical / cultural / technical context]

MISSING COUNTERARGUMENTS:
- [position] doesn't acknowledge: [legitimate opposing view]
```

---

## Step 6: Flag Misleading Content

Identify anything that could lead readers to incorrect conclusions.

```
MISLEADING CONTENT:
1. [content] — Misleading because: [reason]
   Reader would conclude: [wrong takeaway]
   Correct framing: [how to present it accurately]
   Severity: [CRITICAL / MODERATE / MINOR]

2. [content] — Misleading because: [reason]
   Reader would conclude: [wrong takeaway]
   Correct framing: [how to present it]
   Severity: [level]

DOMAIN EXPERT VERDICT:
- Accuracy: [1-5]
- Depth: [1-5]
- Nuance: [1-5]
- Terminology: [1-5]
- OVERALL: [score] / 5

SUITABLE FOR AUDIENCE: [who can safely consume this as-is]
NEEDS REVISION FOR: [who would be misled by current state]

TOP PRIORITY FIXES:
1. [fix] — Addresses: [issue]
2. [fix] — Addresses: [issue]
3. [fix] — Addresses: [issue]
```

---

## Integration

Use with:
- `/llmf` -> Assess if domain expertise can be reliably provided by an LLM
- `/nusr` -> Balance expert accuracy against newcomer accessibility
- `/upth` -> Formalize the domain expert's implicit evaluation criteria

---
name: "cmpr - Completeness Reasoning"
description: "Reason about whether something is complete by checking necessary and sufficient conditions, identifying gaps and redundancies."
---

# CMPR - Completeness Reasoning

**Input**: $ARGUMENTS

---

## Step 1: Define What "Complete" Means

```
SUBJECT: [what we're assessing for completeness]
DOMAIN: [the context in which completeness is being judged]

COMPLETENESS DEFINITION:
  [explicit statement of what would make this subject complete in this domain]
  SOURCE: [specification | standard | convention | constructed definition]
```

Completeness is always relative to a definition. A novel is "complete" differently than a checklist. State the standard before measuring against it.

---

## Step 2: Check Necessary Conditions

Necessary conditions: things that MUST be present for completeness.

```
NECESSARY CONDITIONS:
  1. [condition] — MET: [yes | no | partially]
     EVIDENCE: [how you verified]
  2. [condition] — MET: [yes | no | partially]
     EVIDENCE: [verification]
  3. [condition] — MET: [yes | no | partially]
     EVIDENCE: [verification]
  ...
```

If ANY necessary condition is unmet, the subject is incomplete. No exceptions.

---

## Step 3: Check Sufficient Conditions

Sufficient conditions: if ALL of these are met, completeness is guaranteed.

```
SUFFICIENT CONDITIONS:
  1. [condition] — MET: [yes | no | partially]
     EVIDENCE: [verification]
  2. [condition] — MET: [yes | no | partially]
     EVIDENCE: [verification]
  ...

ALL SUFFICIENT CONDITIONS MET: [yes | no]
```

The sufficient set may differ from the necessary set. Necessary conditions prevent incompleteness. Sufficient conditions guarantee completeness. The gap between them is where judgment lives.

---

## Step 4: Identify What's Missing for Necessity

```
UNMET NECESSARY CONDITIONS:
  1. [condition] — MISSING: [what specifically is absent]
     IMPACT: [what fails without this]
     FILL DIFFICULTY: [easy | moderate | hard]
  2. [condition] — MISSING: [what's absent]
     IMPACT: [consequence]
     FILL DIFFICULTY: [level]
```

If no necessary conditions are unmet, state that explicitly and skip to Step 5.

---

## Step 5: Identify What's Redundant Beyond Sufficiency

```
REDUNDANCIES:
  1. [element] — REDUNDANT BECAUSE: [why this exceeds what's needed]
     HARMFUL: [yes | no] — [if yes, how it causes problems]
     KEEP ANYWAY: [yes | no] — [justification]
  2. [element] — REDUNDANT BECAUSE: [reason]
     HARMFUL: [yes | no]
     KEEP ANYWAY: [yes | no]
```

Redundancy is not always bad. Backup systems are redundant by design. But redundancy that adds confusion, cost, or maintenance burden without value should be flagged.

---

## Step 6: Assess Overall Completeness

```
COMPLETENESS ASSESSMENT
=======================
SUBJECT: [what was assessed]
DEFINITION OF COMPLETE: [the standard used]

NECESSARY CONDITIONS: [X of Y met]
SUFFICIENT CONDITIONS: [X of Y met]

COMPLETENESS: [percentage estimate]
  COMPLETE: all necessary and sufficient conditions met
  NEARLY COMPLETE: all necessary met, some sufficient missing
  INCOMPLETE: necessary conditions unmet
  OVER-COMPLETE: exceeds sufficiency with redundancies

MISSING (must fix):
  1. [unmet necessary condition]
  2. [unmet necessary condition]

MISSING (would improve):
  1. [unmet sufficient condition]

REDUNDANT (consider removing):
  1. [unnecessary element]

VERDICT: [complete | nearly complete | incomplete | over-complete]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **No completeness definition** | Assessing without stating the standard | Define "complete" before checking |
| **Confusing necessary and sufficient** | Treating nice-to-haves as requirements | Ask: does it FAIL without this, or just work less well? |
| **Binary thinking** | Only "complete" or "incomplete" | Use the spectrum: incomplete, nearly complete, complete, over-complete |
| **Ignoring redundancy** | Only looking for gaps, not excess | Over-completeness is a real problem — check for it |
| **Moving goalposts** | Changing the completeness definition mid-assessment | Lock the definition in Step 1 |

---

## Integration

- Use with: `/gflr` to dive deeper into identified gaps
- Use with: `/difr` to check if comparisons cover all relevant differences
- Use with: `/agsk` to check if an argument has all needed premises
- Use from: `/evaluate` when assessing work completeness
- Differs from `/gflr`: cmpr checks against formal conditions; gflr reasons about what's missing and its impact

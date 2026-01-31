---
name: sacri
description: "Ensure gates and procedures link to other procedures that provide the needed answer-interface and next steps."
---

# Cross-Reference Integrity Audit

**Input**: $ARGUMENTS

---

## Overview

Ensure gates and procedures link to other procedures that provide the needed answer-interface and next steps. Broken or missing cross-references mean executors hit dead ends.

## Steps

### Step 1: Extract References
From the target artifact, extract:
1. All "→ INVOKE: /procedure_name" references
2. All "see also" or "related" procedure mentions
3. All file path references to other procedures
4. All implicit references ("use the evaluation from..." without naming it)

### Step 2: Verify Reference Existence
For each reference:

| Reference | Target | Exists? | Accessible? |
|-----------|--------|---------|------------|
| [reference text] | [what it points to] | Y/N | Y/N |

If a reference points to a non-existent procedure: flag as BROKEN.

### Step 3: Verify Answer-Interface Match
For each existing reference, check: does the referenced procedure provide what the referrer needs?

| Referrer Needs | Referenced Provides | Match? |
|---------------|-------------------|--------|
| Definition (what does X mean?) | [what it actually provides] | Y/N |
| Observation (what to look for?) | [what it actually provides] | Y/N |
| Measurement (what metric?) | [what it actually provides] | Y/N |
| Provenance (what source?) | [what it actually provides] | Y/N |
| Decision (what choice?) | [what it actually provides] | Y/N |

If the referenced procedure doesn't provide what the referrer needs: flag as MISMATCHED.

### Step 4: Identify Missing References
Check for places where a cross-reference SHOULD exist but doesn't:

1. Steps that say "evaluate" without pointing to an evaluation procedure
2. Gates that require information without saying where to get it
3. Decision points without linking to decision procedures
4. "Verify" steps without linking to verification methods
5. Steps that produce output without saying where it goes next

### Step 5: Propose Fixes
For each issue:

| Issue | Type | Fix |
|-------|------|-----|
| [reference] | broken | [correct target or remove] |
| [reference] | mismatched | [better target or note the gap] |
| [location] | missing | [add reference to: procedure_name] |

### Step 6: Report
```
CROSS-REFERENCE INTEGRITY:
Target: [what was audited]
References found: [N]
  Intact: [N]
  Broken: [N]
  Mismatched: [N]
Missing references: [N]

Issues:
| # | Location | Issue | Severity | Fix |
|---|----------|-------|----------|-----|
| 1 | [where] | [what's wrong] | [H/M/L] | [how to fix] |

Integrity score: [intact / (intact + broken + mismatched)]%
```

## When to Use
- When adding new procedures or gates
- When a file asks questions without providing an evaluation path
- When cross-references drift or break
- → INVOKE: /sapea (executability audit) for deeper procedure quality checks
- → INVOKE: /pv (procedure validation) for overall procedure quality

## Verification
- [ ] All references extracted (explicit and implicit)
- [ ] Each reference checked for existence
- [ ] Answer-interface match verified for existing references
- [ ] Missing references identified
- [ ] Fixes proposed for all issues

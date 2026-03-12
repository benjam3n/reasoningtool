---
name: "prr - Procedure Registry Review"
description: "Review and improve the procedure registry schema using explicit definitions, evidence alignment, and non-regression."
output:
  format: "prose"
---

# Procedure Registry Review

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Schema review**: The user has changed the registry schema, naming, or derived state logic and wants it reviewed for clarity, accuracy, and non-regression.
**Interpretation 2 — Clarity review**: The registry output feels unclear to read. The user wants naming improved and definitions sharpened.
**Interpretation 3 — New addition review**: The user has added a new evidence source, derived state, or projection and wants it reviewed for consistency with the existing schema.

If ambiguous, ask: "Are you reviewing schema changes, improving clarity, or checking a new addition?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Names must be unambiguous.** Every key, label, and term in the registry should have exactly one plausible interpretation. If a reader could reasonably misinterpret a name, it needs renaming. The test is not "can it be understood correctly?" but "can it be understood incorrectly?"

2. **Labels must match evidence.** A derived state's label should claim exactly what its evidence fields support — no more, no less. If the label claims "adoption" but the evidence only measures "awareness," the label overclaims. If evidence supports "adoption" but the label says "interest," the label underclaims.

3. **Changes must not regress.** Every proposed change must explicitly state what value the old version provided and how the new version preserves it. If a change removes information, an alternative that preserves it must be proposed.

4. **Derivation logic must be traceable.** For every derived state, you should be able to trace from label → definition → evidence fields → raw data without gaps. If any link in this chain is unclear, the derivation is broken.

5. **Registry claims are testable.** Everything the registry says about its procedures should be verifiable against actual usage. If the registry says a procedure is "mature" but there are no usage logs, the claim is ungrounded.

---

## Procedure

### Phase 1: Read and Summarize the Registry Policy

Read the policy section of the registry. Extract and summarize:

```
REGISTRY POLICY SUMMARY:

Evidence signals:
- [signal name]: [source] — [what it measures]

Terms and definitions:
- [term]: [definition]

Derived states:
- [state name]: [definition] — [evidence fields used] — [logic]

Projections:
- [projection]: [conditions] — [derived from]

SUMMARY: The registry claims to measure [what].
```

### Phase 2: Naming Clarity Review

For each key and label in `policy.derived_states`:

```
NAMING REVIEW:

Label: [the label]
Intended meaning: [plain language]
Plausible wrong interpretation: [what a reader might think it means]
Risk of confusion: [low / medium / high]
Action: [keep / rename to X / add clarifying definition]
```

Repeat for each domain term in `policy.terms`.

**Rename criteria:**
- If the wrong interpretation is plausible AND would lead to wrong conclusions → rename
- If the wrong interpretation is plausible but harmless → add clarifying note
- If the wrong interpretation is implausible → keep

### Phase 3: Evidence Alignment Review

For each derived state:

```
EVIDENCE ALIGNMENT:

State: [state name/label]
Label claims: [what the label asserts]
Evidence fields used: [list of exact fields]
Each word supported?
  - "[word 1]": supported by [field] — YES/NO
  - "[word 2]": supported by [field] — YES/NO
Label accuracy: [overclaims / underclaims / accurate]
Action: [keep / narrow label to X / strengthen label to X]
```

Repeat for each projection rule in `policy.projections`.

### Phase 4: Non-Regression Review

For each proposed change from Phases 2 and 3:

```
NON-REGRESSION CHECK:

Change: [old] → [new]
Value of old version: [what it provided]
New version preserves: [how the value is maintained]
Information lost: [if any — propose alternative]
Risk: [low / medium / high]
Verdict: [approve / modify / reject]
```

### Phase 5: Apply and Validate

1. Apply approved changes
2. Regenerate the registry (if applicable)
3. Spot-check at least three entries:
   - One required by core gates
   - One with multiple usage logs
   - One not listed in the catalog

```
SPOT-CHECK RESULTS:

Entry: [name]
Before change: [behavior]
After change: [behavior]
Regression: [none / minor / breaking]
```

### Phase 6: Report

```
PROCEDURE REGISTRY REVIEW REPORT

CHANGES MADE:
1. [change description] — Reason: [why]
2. ...

CHANGES DEFERRED:
1. [change description] — Reason: [why deferred]

CHANGES REJECTED:
1. [change description] — Reason: [why rejected]

SPOT-CHECK RESULTS:
- [entry 1]: [no regression / issue found]
- [entry 2]: [no regression / issue found]
- [entry 3]: [no regression / issue found]

NAMING IMPROVEMENTS: [count]
EVIDENCE ALIGNMENTS: [count]
NON-REGRESSIONS VERIFIED: [count]

REMAINING ISSUES:
- [any unresolved items]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Cosmetic-only review** | Names changed but evidence alignment not checked | Always check evidence alignment — it's more important than naming |
| **Regression introduced** | Change broke existing functionality or removed information | Non-regression review is mandatory for every change |
| **Label drift** | Label changed to be "clearer" but now doesn't match evidence | After renaming, re-check evidence alignment |
| **Overclaiming labels** | "Adoption" label backed only by "awareness" data | Narrow the label to what evidence actually supports |
| **Missing spot-check** | Changes applied without validation | Always spot-check at least 3 entries after changes |
| **Definition-free terms** | New terms added without explicit definitions | Every term must have a plain-language definition |

---

## Depth Scaling

| Depth | Scope | Output |
|-------|-------|--------|
| **1x** | Quick — review naming clarity only, flag obvious issues | Naming review with flags |
| **2x** | Standard — naming + evidence alignment | Full naming review, evidence alignment check |
| **4x** | Thorough — naming + evidence + non-regression + spot-check | Complete review with validation |
| **8x** | Exhaustive — all above + cross-reference with usage logs + consistency across entire registry | Full audit with provenance tracing |

---

## Pre-Completion Checklist

- [ ] Policy section read and summarized
- [ ] All derived state names reviewed for ambiguity
- [ ] All domain terms reviewed for ambiguity
- [ ] Evidence alignment checked for each derived state
- [ ] Evidence alignment checked for each projection
- [ ] Non-regression verified for every proposed change
- [ ] Changes applied and registry regenerated (if applicable)
- [ ] At least 3 entries spot-checked
- [ ] Report generated with changes, deferrals, and rejections

---

## Integration

- **Use from**: After any schema change, after adding new evidence sources or derived states, when registry output is unclear
- **Routes to**: /ver (GOSM verification of registry claims), /mv (MECE check of registry categories), /val (validate registry against its own requirements)
- **Differs from**: /evaluate (general assessment, /prr is specifically for registry schema), /val (validates deliverables against requirements, /prr validates naming and evidence alignment)
- **Complementary**: /fb (filtered feedback may produce items that modify the registry), /ver (verify registry claims are grounded), /av (verify assumptions behind derived states)

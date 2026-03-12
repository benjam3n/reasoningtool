---
name: "siycftr - See If You Can Find The Rest"
description: "Scan text for omitted but implied items and produce the complete set, distinguishing genuinely implied items from invented ones."
output:
  format: "prose"
---

# SIYCFTR - See If You Can Find The Rest

**Input**: $ARGUMENTS

---

## Core Principles

1. **Omission is not always accidental.** Some items are left out intentionally (out of scope, deliberately excluded). Others are forgotten. The skill must distinguish deliberate omission from oversight. Only add what was genuinely meant but missing.

2. **Pattern completion is unreliable.** "Apple, banana, cherry..." might continue with "date" (alphabetical) or "dragonfruit" (tropical) or stop at three (the list was complete). The continuation rule must be verified, not assumed.

3. **The stated items define the pattern.** The items explicitly listed constrain what "the rest" could be. Three technical requirements imply more technical requirements, not marketing goals. The category of the missing items is set by what's present.

4. **Completeness has a standard.** "Did I find the rest?" requires a definition of complete. In some domains, MECE is the standard. In others, practical coverage is enough. The completeness criterion must be explicit.

5. **Better to surface-and-flag than to silently add.** When uncertain whether an item was omitted or excluded, present it with a flag rather than either adding it silently or dropping it. Let the user decide.

---

## Phase 1: Input Analysis

```
[R1] INPUT_TEXT: [the text being scanned, quoted or summarized]
[R2] EXPLICIT_ITEMS: [list of items explicitly stated]
[R3] ITEM_COUNT: [N items stated]
[R4] APPARENT_CATEGORY: [what kind of items are these?]
[R5] APPARENT_PATTERN: [is there an ordering, grouping, or selection principle?]
```

---

## Phase 2: Pattern Identification

Identify the rule governing what's included:

```
[R6] CONTINUATION_RULE: [what rule would generate these items?]
[R7] RULE_CONFIDENCE: [high | medium | low]
[R8] ALTERNATIVE_RULES: [what other rules could explain the same items?]
```

If RULE_CONFIDENCE is low or multiple ALTERNATIVE_RULES exist:
```
[R9] AMBIGUITY: [the pattern is ambiguous — multiple completions are possible]
[R10] DISAMBIGUATION: [what would clarify which pattern is intended]
```

### Pattern Types

| Type | Example | Completion Method |
|------|---------|------------------|
| **Enumeration** | "Requirements: A, B, C..." | Check if more items exist in the category |
| **Taxonomy** | "Frontend, backend..." | Check for missing levels/branches |
| **Process** | "Step 1, Step 2..." | Check for missing steps in sequence |
| **Criteria** | "Must be fast, must be cheap..." | Check for standard criteria in the domain |
| **Stakeholders** | "Users, admins..." | Check for missing roles/parties |
| **Dimensions** | "Speed, cost..." | Check for missing evaluation dimensions |
| **MECE categories** | "Buy, build, partner..." | Check for exhaustive coverage |

---

## Phase 3: Gap Identification

For each potential missing item:

```
[R-N] CANDIDATE: [potential missing item]
  EVIDENCE: [why this seems implied — what pattern suggests it]
  OMISSION_TYPE: [likely_forgotten | possibly_excluded | uncertain]
  IMPORTANCE: [high | medium | low]
```

### Omission Type Classification

| Type | Signal | Treatment |
|------|--------|-----------|
| **Likely forgotten** | Pattern clearly implies it; no reason to exclude | Add with confidence |
| **Possibly excluded** | Pattern implies it but it might be deliberately out of scope | Flag for user review |
| **Uncertain** | Could be implied or could be irrelevant | Present as "possible addition" |

---

## Phase 4: Completeness Check

```
[R-N] COMPLETENESS_STANDARD: [MECE | practical coverage | domain standard | N-of-M enumeration]
[R-N] COMPLETENESS_ASSESSMENT:
  BEFORE: [N items — coverage level]
  AFTER (with candidates): [N items — coverage level]
  REMAINING_GAPS: [known gaps that couldn't be filled, if any]
```

---

## Phase 5: Output

```
COMPLETION ANALYSIS
===================

INPUT: [text or list being completed]
EXPLICIT ITEMS: [N]
PATTERN: [continuation rule — confidence level]

LIKELY MISSING (high confidence — probably forgotten):
  1. [item] — EVIDENCE: [why implied]
  2. [item] — EVIDENCE: [why implied]

POSSIBLY MISSING (medium confidence — might be excluded):
  3. [item] — EVIDENCE: [why might be implied] — CAUTION: [why might be excluded]

UNCERTAIN (low confidence — for user review):
  4. [item] — EVIDENCE: [weak signal]

COMPLETENESS:
  BEFORE: [N items — X% coverage]
  AFTER: [N items — Y% coverage]
  STANDARD: [what completeness means here]
  REMAINING GAPS: [if any]

READY FOR:
- /mv — to validate MECE completeness
- /se — to enumerate more systematically if gaps remain
- /dd — to discover missing dimensions
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Invention disguised as completion** | "Missing items" that aren't implied by anything | Every candidate must have EVIDENCE tied to the pattern |
| **Wrong pattern** | Completion follows rule that doesn't match stated items | Check alternative rules; verify against existing items |
| **Deliberate exclusion overridden** | Adding items the user intentionally left out | Flag as "possibly excluded" instead of adding |
| **Completeness not defined** | "Found more items" without knowing what complete means | State the completeness standard explicitly |
| **Category drift** | Missing items from a different category than explicit items | Missing items must match the apparent category |
| **Overcounting** | Adding items that are sub-items of existing items | Check for containment — is this already covered? |

---

## Depth Scaling

| Depth | Min Explicit Analyzed | Min Candidates | Pattern Alternatives Checked | Completeness Assessment |
|-------|----------------------|---------------|-----------------------------|-----------------------|
| 1x | All | 2 | 1 | Binary (complete/incomplete) |
| 2x | All | 4 | 2 | With coverage percentage |
| 4x | All | 7 | 4 | With MECE check |
| 8x | All | 12 | All plausible | With remaining gaps mapped |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Explicit items identified and categorized
- [ ] Continuation rule identified with confidence level
- [ ] Alternative rules considered
- [ ] Each candidate has evidence (not invented)
- [ ] Omission type classified (forgotten vs excluded vs uncertain)
- [ ] Completeness standard stated
- [ ] Before/after coverage assessed
- [ ] No category drift in candidates

---

## Integration

- Complementary: `/mv` (MECE validation), `/se` (systematic enumeration), `/dd` (dimension discovery)
- Differs from `/se`: se enumerates from scratch; siycftr completes an existing partial list
- Differs from `/etc`: etc expands pattern tails; siycftr finds omissions anywhere in a text
- Differs from `/mv`: mv validates completeness; siycftr fills gaps

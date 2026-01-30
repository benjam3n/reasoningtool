---
name: mcg
description: Gate that verifies all items mentioned by user have been considered, analyzed, and addressed. Prevents dropping user-mentioned aspects. Run after any multi-aspect analysis to verify nothing was missed.
---

# Mentioned Coverage Gate

**Input**: $ARGUMENTS (the original user message or list of items to verify coverage for)

---

## Purpose

When a user mentions multiple things (frames, stakeholders, dimensions, categories, etc.), this gate verifies that EVERY mentioned item was:
1. Identified/extracted
2. Checked against existing coverage
3. Either covered or explicitly noted as a gap
4. Gaps filled or explained

**Why this gate exists**: It's easy to address some items and unconsciously drop others. This gate prevents that.

---

## Step 1: EXTRACT All Mentioned Items

Parse the user's input and create an exhaustive list of everything they mentioned.

**Categories to look for:**
- Explicit lists (numbered, bulleted, comma-separated)
- Items in tables
- Items in examples
- Implicit items (references to "all of these", "each of", "etc.")
- Meta-items ("also" statements, "and" connectors)

**Output format:**
```
EXTRACTED ITEMS:
1. [item 1] - from: [where in message]
2. [item 2] - from: [where in message]
...
N. [item N] - from: [where in message]

Total: N items extracted
```

**Gate check**: Did I extract ALL items, including:
- [ ] Items explicitly listed?
- [ ] Items implied by "etc." or "and so on"?
- [ ] Items referenced with "all of these"?
- [ ] Items mentioned in passing?
- [ ] Meta-requests about the items themselves?

---

## Step 2: CHECK Coverage for Each Item

For each extracted item, determine if it's covered in the system.

**Check locations:**
1. Universal guess library files (`data/guess_libraries/universal/*.md`)
2. Domain guess library files (`data/guess_libraries/*.md`)
3. Skills (`skills/*/SKILL.md`)
4. Procedures in YAML files

**Output format:**
```
| Item | Covered? | Location | Specific Question/Entry |
|------|----------|----------|------------------------|
| [item 1] | YES/NO/PARTIAL | [file] | [Q# or entry] |
| [item 2] | YES/NO/PARTIAL | [file] | [Q# or entry] |
...
```

**Coverage definitions:**
- **YES**: Explicit question-guess entry exists for this exact concept
- **PARTIAL**: Related content exists but doesn't fully address the item
- **NO**: No coverage found

---

## Step 3: IDENTIFY Gaps

Create explicit list of items not covered or only partially covered.

**Output format:**
```
GAPS IDENTIFIED:

1. [item] - Status: [NO/PARTIAL]
   - What's missing: [specific gap]
   - Why it matters: [impact of not having this]
   - Suggested file: [where it should go]

2. [item] - Status: [NO/PARTIAL]
   ...

Total gaps: N items
```

---

## Step 4: FILL or EXPLAIN Gaps

For each gap, either:
1. **CREATE** the missing content (new file or new questions in existing file)
2. **EXPLAIN** why it shouldn't be created (out of scope, duplicate, etc.)

**If creating:**
```
CREATED:
- [item] → [new file or location]
  - Questions added: [count]
  - Entries added: [count]
```

**If explaining:**
```
NOT CREATED (with reason):
- [item] → Reason: [why not needed]
```

---

## Step 5: VERIFY Complete Coverage

After filling gaps, run coverage check again to confirm 100% coverage.

**Final output format:**
```
FINAL COVERAGE VERIFICATION:

| Item | Status | Location |
|------|--------|----------|
| [item 1] | ✓ COVERED | [file:Q#] |
| [item 2] | ✓ COVERED | [file:Q#] |
...

Coverage: N/N items (100%)
```

**Gate FAILS if:**
- Any item shows "NOT COVERED" without explanation
- Any item was dropped (not in final table)
- Total in final table ≠ Total extracted in Step 1

---

## Step 6: META-CHECK

Verify the gate itself was applied correctly:

- [ ] Did I extract ALL items from user message?
- [ ] Did I check EVERY extracted item?
- [ ] Did I create or explain EVERY gap?
- [ ] Does final count match initial count?
- [ ] Did user mention any META-requests about the items that I also need to address?

---

## Quick Reference Table

| Step | Action | Output |
|------|--------|--------|
| 1 | Extract | List of N items |
| 2 | Check | Coverage table |
| 3 | Identify | Gap list |
| 4 | Fill/Explain | Created/Explained list |
| 5 | Verify | Final 100% coverage table |
| 6 | Meta-check | Self-verification |

---

## Example Application

**User says**: "Make sure frames, stakeholders, time horizons, and dimensions are all covered"

**Step 1 extraction:**
```
EXTRACTED ITEMS:
1. frames - explicit
2. stakeholders - explicit
3. time horizons - explicit
4. dimensions - explicit
5. "all covered" - meta-request for verification

Total: 5 items (4 content + 1 meta)
```

**Step 2 check:**
```
| Item | Covered? | Location |
|------|----------|----------|
| frames | YES | 104_interpretation_frames.md |
| stakeholders | YES | 105_stakeholder_archetypes.md |
| time horizons | YES | 106_time_horizons.md |
| dimensions | PARTIAL | 01-11 exist but DEGREE missing |
| "all covered" meta | NO | No coverage verification file |
```

**Step 3 gaps:**
```
1. dimensions/DEGREE - PARTIAL → Need 107_degree_magnitude.md
2. "all covered" meta → Need this very procedure
```

**Step 4 fill:**
```
CREATED:
- DEGREE → 107_degree_magnitude.md (11Q, 51 entries)
- coverage gate → skills/mentioned_coverage_gate/SKILL.md
```

**Step 5 verify:**
```
Coverage: 5/5 items (100%)
```

---

## When To Use This Gate

**ALWAYS use after:**
- User lists multiple items to address
- User says "all of these", "each of", "make sure"
- Complex multi-aspect analysis
- Creating new categories or files

**SIGNS you need this gate:**
- User repeats a request (may have been dropped)
- User says "did you consider X?" (may have been missed)
- You feel like you might have missed something

---

## Integration

This gate should be invoked:
1. Automatically after `/space_discovery` (verify all discovered aspects addressed)
2. Manually when user mentions multiple items
3. As final check before declaring work complete

→ Pairs with: `/comprehensive_aspects` (general completeness)
→ Pairs with: `/verification_before_output` (claim verification)
→ Pairs with: `100_coverage_strategy.md` (coverage modes)

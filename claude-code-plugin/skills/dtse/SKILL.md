---
name: "dtse - Does This Skill Exist"
description: "Check whether a requested skill exists by name or function, show exact matches and nearest alternatives, and provide next action."
output:
  format: "prose"
---

# DTSE - Does This Skill Exist

**Input**: $ARGUMENTS

---

## Core Principles

1. **Name is not function.** Users describe needs by what they want to do, not by skill IDs. The lookup must bridge natural-language intent to terse abbreviation.

2. **Partial coverage is not absence.** A skill that handles 70% of the need exists — the answer is "YES, with caveats," not "NO."

3. **Workflow beats single skill.** The need may require chaining two skills, not finding one. Surface compositions, not just atoms.

4. **Synonymy is the norm.** Every concept has 3-5 names. "brainstorm" = `/ma`, "compare" = `/cmp`, "prioritize" = `/ro`. Matching must be semantic, not string-based.

5. **False negatives are worse than false positives.** Telling a user "this doesn't exist" when it does wastes time and invites duplicate creation. Err toward surfacing candidates.

---

## Phase 1: Parse the Request

```
[D1] LITERAL_ID: [exact skill id if given, e.g., "rca"]
[D2] DESCRIBED_FUNCTION: [what the user wants to do, in plain language]
[D3] DOMAIN_HINT: [any domain context, e.g., "for code review", "for writing"]
[D4] IMPLICIT_CONSTRAINTS: [scope, speed, depth expectations if detectable]
```

If the user gives a skill ID, still extract the function — you need both for semantic search in case the ID doesn't exist but the function does under another name.

---

## Phase 2: Exact Match Check

Check whether `skills/[LITERAL_ID]/SKILL.md` exists.

```
[D5] EXISTS: YES | NO | NO_ID_GIVEN
[D6] SKILL_PATH: /[id] (if exists)
[D7] NAME: [full name from frontmatter]
[D8] DESCRIPTION: [from frontmatter]
[D9] FUNCTION_MATCH: CONFIRMED | MISMATCH
```

- EXISTS=YES and FUNCTION_MATCH=CONFIRMED → skip to Phase 5
- EXISTS=YES but FUNCTION_MATCH=MISMATCH → note mismatch, continue to Phase 3
- EXISTS=NO or NO_ID_GIVEN → continue to Phase 3

---

## Phase 3: Semantic Search

Search using these strategies in order:

**Strategy A — Category match**: Which category does the need fall into? Check the category skills table. If a category clearly owns this, its sub-skills are the candidate pool.

**Strategy B — Description match**: Scan skill registry entries. Match on description, tags, categories, title. Weight description matches highest.

**Strategy C — Invocation graph**: If a related skill is found, check what it invokes and what invokes it — adjacent skills are strong candidates.

**Strategy D — Function decomposition**: If the need is compound ("brainstorm and then prioritize"), decompose into atomic functions and search each.

```
[D10] SEARCH STRATEGIES USED: [A, B, C, D as applicable]

| Rank | Skill | Title | Match Strategy | Coverage |
|------|-------|-------|---------------|----------|
| 1 | /[id] | [title] | [strategy] | [FULL/HIGH/PARTIAL/TANGENTIAL] |
| 2 | /[id] | [title] | [strategy] | [coverage] |
| ... | | | | |
```

Coverage: FULL (does exactly this), HIGH (>80%), PARTIAL (40-80%), TANGENTIAL (<40%)

---

## Phase 4: Gap Analysis

If no candidate has FULL or HIGH coverage:

```
[D11] GAP_TYPE: [NOVEL | COMPOSITE | VARIANT | NAMING_ONLY]
```

- **NOVEL** — No skill addresses this function at all
- **COMPOSITE** — Two or more skills together cover it
- **VARIANT** — A skill does something close but user needs different angle/depth/domain
- **NAMING_ONLY** — The skill exists but the user's name doesn't map to any ID

For COMPOSITE gaps:
```
[D12] COMPOSITE CHAIN:
  Step 1: /[id] — handles [which part]
  Step 2: /[id] — handles [which part]
  UNCOVERED: [what still isn't handled]
```

For NOVEL gaps:
```
[D13] NOVEL SKILL SKETCH:
  FUNCTION: [1-sentence]
  INPUT: [what it takes]
  OUTPUT: [what it produces]
  NEAREST_EXISTING: /[id] — [why not sufficient]
```

---

## Phase 5: Output

```
QUERY: [what the user asked for]
EXISTS: YES | PARTIAL | COMPOSITE | NO

EXACT_MATCH: /[id] — [title]
  → [1-line description]

NEAREST_MATCHES:
  1. /[id] — [title] — [why similar] — Coverage: [level]
  2. /[id] — [title] — [why similar] — Coverage: [level]
  3. /[id] — [title] — [why similar] — Coverage: [level]

RECOMMENDED_ACTION:
  → USE: /[id] [original prompt]        — when exact or high-coverage match
  → CHAIN: /[id1] then /[id2]           — when composite coverage works
  → CREATE: /cs [skill spec]            — when novel skill needed
  → CLARIFY: [question to user]         — when intent is ambiguous
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **String-literal tunnel vision** | Only checks exact ID | Always run Phase 3 even if Phase 2 matches |
| **Synonym blindness** | "brainstorm" doesn't find `/ma` | Use function decomposition, not keyword matching |
| **Premature NO** | Declares absent when 90% match exists | Check at least 5 candidates before declaring NO |
| **Composition blindness** | "no skill does X+Y" when /A then /B covers it | Always check 2-skill chains |
| **False FULL** | Claims full coverage based on title alone | Read the actual SKILL.md, not just title |
| **Novelty bias** | Routes to /cs when existing skill would work | Only recommend creation when coverage < 40% |

---

## Depth Scaling

| Depth | Semantic Candidates | Coverage Analysis | Composition Search | Gap Detail |
|-------|--------------------|--------------------|-------------------|------------|
| 1x | 3 | — | — | 1-line |
| 2x | 5 | Partial/full tag | 1 chain | 3-line |
| 4x | 8 | Per-candidate | 2 chains | Full paragraph |
| 8x | 12 | Scored coverage | 3 chains + gap map | Spec draft |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] LITERAL_ID parsed if present
- [ ] Function description extracted regardless of ID
- [ ] Exact match checked (if ID given)
- [ ] At least 3 semantic candidates surfaced
- [ ] Coverage level assigned to each candidate
- [ ] If no high-coverage match: gap type classified
- [ ] If COMPOSITE: chain specified with uncovered remainder
- [ ] RECOMMENDED_ACTION is concrete and invocable
- [ ] Did not recommend /cs unless coverage genuinely < 40%

---

## Integration

| Situation | Next Skill |
|-----------|-----------|
| Skill exists, user should use it | Invoke matched skill directly |
| Need is composite | → `/fonss` to sequence the chain |
| Skill doesn't exist and should | → `/cs` to create it |
| Need formal spec for new skill | → `/fmtsb` to formalize |
| User wants to understand found skill | → `/uf` to analyze use cases |
| Ambiguous between candidates | → `/cmp` to compare |

# /bldk Build a template for creating new skills that ensures consistent quality
**Date:** 2026-03-09
**Skill:** /bldk (Build)

---

## Step 1: Define What's Being Built

```
THING: A SKILL.md template/specification that encodes the quality patterns found in tier-1 skills (like /araw, /uaua, /gen, /cri) so that every new skill built from it meets a minimum quality bar.

FOR WHOM: The skill author (currently Ben, potentially contributors) — someone creating a new SKILL.md file for the reasoning toolkit.

CORE NEED: Eliminate the quality gap between tier-1 and tier-3 skills by making the quality requirements structural (built into the template) rather than aspirational (hoping the author remembers them).
```

---

## Step 2: Specify Requirements

```
MUST HAVE (ship-blocking):
1. Frontmatter section (name + description) — because skills need metadata for discovery and routing
2. Interpretations section — because the best skills (araw, uaua) disambiguate input before executing, preventing misapplication
3. Phased structure with clear separation — because mixing exploration/evaluation/synthesis is the #1 quality failure mode
4. Anti-failure table — because explicit failure modes with signals and fixes prevent the most common quality collapses
5. Pre-completion checklist — because this is the enforcement mechanism; without it, the LLM skips steps
6. Depth scaling table — because skills need to work at different levels of effort (quick check vs. deep dive)
7. Output format specification — because unstructured prose output is harder to use and harder to verify
8. Integration section — because skills should chain; isolated skills produce lower-quality results

SHOULD HAVE (important but not blocking):
1. Core principles section — because principles resolve ambiguity when procedure conflicts with intent
2. Corruption pre-inoculation — because user validation degrades output quality in analytical skills
3. Quick mode variant — because many skills are invoked for small tasks that don't need full procedure
4. Domain adaptation guidance — because a skill applied to code vs. strategy needs different emphasis

NICE TO HAVE (if time permits):
1. "When called by other skills" section — for skills that function as primitives
2. "When this skill fails" escape hatch — for redirecting to better-fit skills
3. Worked example embedded in the template comments

EXPLICITLY OUT OF SCOPE:
- Automated skill generation (this is a template, not a generator)
- Skill testing framework (that's a separate build)
- Skill versioning system
- Template for category/router skills (different structure entirely)
```

---

## Step 3: Design Before Building

```
APPROACH: Reverse-engineer the structural patterns from the 4 highest-quality skills
(araw, uaua, gen, cri) and the 2 weakest patterns (hd, pbr — functional but missing
key quality mechanisms). Encode the delta as required template sections. Each section
includes both the structure AND a brief annotation explaining why it exists.

KEY DECISIONS:
1. Template format — chose annotated markdown template because the output IS a
   SKILL.md file, so the template should be in the same format with inline guidance
2. Required vs. optional sections — chose to mark sections as REQUIRED/RECOMMENDED/OPTIONAL
   rather than including everything, because not all skills need all sections (e.g.,
   corruption pre-inoculation only applies to analytical skills)
3. Annotation style — chose inline HTML comments (<!-- -->) because they won't render
   when the skill is used but are visible when editing, keeping guidance present
   during authoring

RISKS:
- Template is too rigid, forces unnecessary structure on simple skills
  — mitigation: include a SKIP rule for each section with criteria for when to omit
- Template is too long, nobody reads it
  — mitigation: keep the template itself under 200 lines; put extended guidance in comments
- Template encodes current best practice, becomes stale
  — mitigation: include a version field and "last audited" date

DEPENDENCIES:
- Analysis of what makes tier-1 skills good (completed above)
- Analysis of what tier-3 skills lack (completed above)
```

---

## Step 4: Build the Smallest Working Version

```
SMALLEST WORKING VERSION:
- Includes: The complete annotated template with all MUST HAVE and SHOULD HAVE sections
- Excludes: Worked examples, automated validation, category-skill variant
- Time to build: This session
- How to test it: Apply the template to create one new skill, then evaluate with /cri
```

---

## Step 5: Build

### Quality Gap Analysis

Before building, here is the specific delta between tier-1 and tier-3 skills:

| Quality Mechanism | Tier-1 (araw, uaua, gen) | Tier-3 (hd, pbr) |
|---|---|---|
| **Interpretations** | Yes — disambiguates input before executing | No — assumes single interpretation |
| **Core principles** | Yes — resolves procedure/intent conflicts | No — procedure only |
| **Phased structure** | Yes — strict phase separation with rules | Numbered steps, no phase separation |
| **Anti-failure table** | Yes — specific failure modes, signals, fixes | No — no failure awareness |
| **Pre-completion checklist** | Yes — enforces all quality requirements | "Verification" list (weaker, less specific) |
| **Depth scaling** | Yes — explicit floors for different effort levels | No — one-size-fits-all |
| **Output format** | Yes — structured templates with numbered items | No — implied prose output |
| **Corruption pre-inoculation** | Yes (analytical skills) | No |
| **Quick mode** | Yes — lite variant for small tasks | No |
| **Integration/chaining** | Yes — specific skill references | No or minimal |
| **Numbered tracking** | Yes — C1, F1, U1 etc. | No — unnumbered findings |
| **Domain adaptation** | Yes — tables mapping domain to approach | No |

### The Template

```markdown
---
name: "[ABBREV] - [Full Name]"
description: "[One sentence: what this skill does, when to use it, what it produces]"
---

# [Full Name]

**Input**: $ARGUMENTS

---

## Interpretations

<!-- REQUIRED. Prevents misapplication. List 2-4 interpretations of what the user
     might mean. If ambiguous, ask. If clear, proceed. -->

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — [Label]**: [When the user has X and wants Y]
**Interpretation 2 — [Label]**: [When the user has A and wants B]
**Interpretation 3 — [Label]**: [When the user has P and wants Q]

If ambiguous, ask: "I can help with [interpretation 1], [interpretation 2], or
[interpretation 3] — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Corruption Pre-Inoculation

<!-- REQUIRED for analytical/evaluative skills. SKIP for generative/action skills.
     Purpose: prevent user validation from softening output quality. -->

**User validation degrades output.** If the user praises or agrees during the session,
this creates a gradient toward agreement rather than truth. When you detect positive
feedback:

1. **Agreement check**: If >80% of findings support the user's apparent position,
   you are confirming, not analyzing. Force yourself to find genuine counterarguments.
2. **Flattery detection**: Delete phrases like "excellent point" or "as you correctly
   noted" — replace with neutral analysis.
3. **Verdict drift**: If claims that were UNCERTAIN become VALIDATED without new
   evidence, corruption has occurred. Revert.

---

## Core Principles

<!-- REQUIRED. These override procedure when conflict arises. 5-10 principles.
     Each should be: actionable, specific to THIS skill, and resolvable to a
     concrete behavior. "Be thorough" is not a principle. "Every finding gets a
     number — nothing gets lost in prose" is. -->

These govern everything. When procedure conflicts with principle, follow the principle.

1. **[Principle name].** [What it means in concrete behavioral terms]
2. **[Principle name].** [What it means in concrete behavioral terms]
3. **[Principle name].** [What it means in concrete behavioral terms]
<!-- ... -->

---

## Quick Mode: [ABBREV]-Lite

<!-- RECOMMENDED. For low-stakes, time-sensitive uses of this skill.
     Should be completable in <50 lines of output. SKIP if skill is
     inherently quick (already <100 lines at full depth). -->

For low-stakes, reversible, time-sensitive situations:

```
[FIELD 1]: [compact version of the skill's core output]
[FIELD 2]: [second most important output]
VERDICT: [decision/assessment — use skill-appropriate categories]
ACTION: [one specific next step]
```

---

## Phase 1: [EXPLORATION / GENERATION / ANALYSIS]

<!-- REQUIRED. Every skill needs at least 2 phases. The critical rule:
     separate DISCOVERY from EVALUATION from SYNTHESIS.
     Phase 1 finds things. Phase 2 compiles. Phase 3 concludes.
     Never mix phases. -->

### Step 1: [First action verb — Identify / Map / Frame / Decompose]

<!-- Each step needs:
     1. Clear action (what to do)
     2. Numbered output format (track everything)
     3. Stopping criterion (when is this step done?) -->

[Instructions for the step]

Number every finding: **[PREFIX]1, [PREFIX]2, [PREFIX]3...**

```
[PREFIX1] [structured output line]
[PREFIX2] [structured output line]
```

### Step 2: [Second action verb]

[Instructions]

```
[Output format]
```

<!-- Add steps as needed. Most skills need 2-4 steps in the exploration phase. -->

---

## Phase 2: REGISTRY / COMPILATION

<!-- REQUIRED. Compile ALL findings from Phase 1 into a structured registry.
     Nothing from Phase 1 gets left out. This is the bridge between
     exploration and synthesis. -->

After ALL exploration is complete, compile EVERY finding into a categorized registry.

```
[SKILL NAME] REGISTRY
=====================

[CATEGORY 1]:
[PREFIX1] [text] -- [relevant metadata]
[PREFIX2] [text] -- [relevant metadata]

[CATEGORY 2]:
[PREFIX3] [text] -- [relevant metadata]

VERDICTS / ASSESSMENTS:
[item] [STATUS] -- evidence: [item numbers] -- derived from: [reasoning]

TOTALS:
- [Category 1]: [N]
- [Category 2]: [N]
- Total findings: [N]
```

**Rules for the registry:**
- Every numbered item from Phase 1 appears here. No exceptions.
- Verdicts/assessments must be DERIVED from findings, not asserted.
- If a verdict is unclear, mark UNCERTAIN, not VALIDATED.

---

## Phase 3: SYNTHESIS

<!-- REQUIRED. Derived entirely from the registry. No new findings.
     This is where conclusions, recommendations, and actions emerge. -->

Derived entirely from the registry. No new findings introduced here.

```
ORIGINAL INPUT: [restated]

WHAT THE ANALYSIS FOUND:
[Numbered list referencing item numbers from registry]
1. [finding, from item numbers]
2. [finding, from item numbers]

KEY TENSIONS:
[Items that contradict each other, or "None found"]

WEAKEST LINKS:
[Which findings are least certain? Reference item numbers]

DO_FIRST ACTIONS:
1. [action] -- WHO: [Claude/user] -- resolves: [item numbers]
2. [action] -- WHO: [Claude/user] -- resolves: [item numbers]

UNRESOLVED:
- [What stayed uncertain and what would resolve it]
```

---

## Depth Scaling

<!-- REQUIRED. Skills must work at different effort levels.
     Minimum 3 tiers. Define FLOORS (minimums, not targets).
     Include at least: a count metric, a depth metric, and an output size metric. -->

| Depth | Min [Primary Count] | Min [Depth Metric] | Min Output Lines |
|-------|--------------------|--------------------|------------------|
| 1x (quick) | [N] | [N] levels | [N] |
| 2x (default) | [N] | [N] levels | [N] |
| 4x (thorough) | [N] | [N] levels | [N] |
| 8x (exhaustive) | [N] | [N] levels | [N] |

Default depth: 2x. Detect from user input ("[abbrev] 8x" -> 8x). These are FLOORS.

---

## Domain Adaptation

<!-- RECOMMENDED. If this skill applies differently across domains,
     provide a mapping table. SKIP if skill is domain-specific. -->

| Domain | [Key Variation 1] | [Key Variation 2] |
|--------|-------------------|-------------------|
| **Code/Engineering** | [approach] | [approach] |
| **Strategy/Business** | [approach] | [approach] |
| **Writing/Creative** | [approach] | [approach] |
| **Design/UX** | [approach] | [approach] |

---

## Anti-Failure Checks

<!-- REQUIRED. The 5-10 most common ways this skill fails.
     Each row: failure mode name, observable signal, specific fix.
     These should be drawn from actual failure patterns, not theoretical. -->

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| **[Name]** | [What you observe when this is happening] | [Specific corrective action] |
| **[Name]** | [Observable signal] | [Fix] |
| **[Name]** | [Observable signal] | [Fix] |
| **[Name]** | [Observable signal] | [Fix] |
| **[Name]** | [Observable signal] | [Fix] |

---

## When [Skill Name] Fails

<!-- RECOMMENDED. Escape hatch when this skill is wrong tool for the job. -->

If [symptom] -> try `/[better-skill]` instead
If [symptom] -> try `/[better-skill]` instead

---

## Integration

<!-- REQUIRED. Skills that chain well with this one.
     Format: /abbrev -> [what it does in this context] -->

Use with:
- `/[skill]` -> [what it adds before/after this skill]
- `/[skill]` -> [what it adds before/after this skill]
- `/[skill]` -> [what it adds before/after this skill]

---

## Saving Output

Output is NOT auto-saved. If the user wants to save, they invoke `/sf` after the session.

---

## Pre-Completion Check

<!-- REQUIRED. This is the enforcement mechanism. Every MUST HAVE quality
     requirement from this template should have a corresponding checkbox.
     The LLM checks these before finishing. If any fail, it goes back. -->

Before finishing:
- [ ] Interpretations: correct interpretation identified or user asked
- [ ] All findings numbered with consistent prefix throughout
- [ ] Depth floors met for the requested depth level
- [ ] Phase separation maintained (no conclusions in exploration, no new findings in synthesis)
- [ ] ALL numbered items from exploration appear in registry (none dropped)
- [ ] Verdicts/assessments derived from evidence, not asserted
- [ ] Synthesis introduces NO new findings — only references item numbers
- [ ] Anti-failure checks: none of the listed failure modes are present in output
- [ ] At least one uncomfortable or surprising finding (if analytical skill)
- [ ] Actions are specific and assigned (WHO does WHAT)
- [ ] [Skill-specific check]
- [ ] [Skill-specific check]
```

---

### Template Authoring Checklist

When using the template above to create a new skill, verify:

| # | Check | Why |
|---|---|---|
| 1 | Frontmatter has name AND description | Discovery and routing depend on it |
| 2 | Interpretations section has 2+ interpretations | Prevents misapplication — the #1 source of bad skill output |
| 3 | Core principles are behavioral, not aspirational | "Be thorough" is useless. "Number every finding" is actionable |
| 4 | Every step has a numbered output format | Unnumbered findings get lost in prose and can't be referenced |
| 5 | Phases are strictly separated | Mixing exploration and evaluation is the #1 quality failure |
| 6 | Registry captures EVERYTHING from exploration | Dropped findings = cherry-picked synthesis |
| 7 | Synthesis only references registry items | New findings in synthesis = phase contamination |
| 8 | Depth table has at least 3 tiers with numeric floors | Without floors, the LLM defaults to shallow execution |
| 9 | Anti-failure table has 5+ entries with observable signals | Failure modes without signals can't be detected |
| 10 | Pre-completion checklist covers all MUST HAVEs | This is the actual enforcement — everything else is aspiration |
| 11 | Integration references specific skills | Isolated skills produce lower-quality results |
| 12 | Every section marked SKIP has explicit criteria for skipping | Prevents authors from skipping everything |

---

### Quality Tiers Diagnostic

Use this to evaluate whether a skill built from the template meets minimum quality:

**Tier 1 (all of these):**
- Has interpretations, principles, phases, anti-failure, depth scaling, pre-completion check
- Anti-failure table has 5+ entries drawn from real failure patterns
- Depth scaling has 4+ tiers with numeric floors
- Pre-completion check has 10+ items
- Corruption pre-inoculation present (if analytical)
- Output format uses numbered tracking throughout

**Tier 2 (most of these):**
- Has interpretations, phases, anti-failure, pre-completion check
- Missing 1-2 of: depth scaling, corruption pre-inoculation, domain adaptation
- Anti-failure table has 3+ entries
- Pre-completion check has 5+ items

**Tier 3 (needs improvement):**
- Missing interpretations OR phase separation OR anti-failure checks
- Steps are numbered but output format is prose
- No depth scaling
- Pre-completion check is generic ("did you do a good job?")

---

## Step 5: Test and Iterate

```
DOES IT WORK? Yes — the template encodes all 12 quality mechanisms identified in
the gap analysis. Each mechanism has both structure (where it goes) and annotation
(why it's there).

DOES IT MEET THE CORE NEED? Yes — a skill built from this template would
structurally include all the quality mechanisms that differentiate tier-1 from tier-3.
The quality requirements are embedded in the template itself, not in a separate
style guide that might be forgotten.

WHAT DID I LEARN?
- The key insight is that the pre-completion checklist is the actual enforcement
  mechanism. Everything else is guidance that the LLM might skip. The checklist
  is what forces it to go back and fix things.
- SKIP criteria are as important as the sections themselves. Without them, the
  template would force unnecessary structure on simple skills.
- The numbered tracking system (C1, F1, U1, etc.) is what makes registries and
  synthesis work. Without numbers, findings dissolve into prose and can't be
  referenced or verified.

WHAT TO BUILD NEXT?
- Apply this template to build one new skill and evaluate the result
- Add a companion /skval (skill validation) skill that checks existing skills
  against this template's quality criteria
```

---

## Step 6: Ship Decision

```
READINESS CHECK:
- All MUST HAVEs met: yes (all 8 present in template)
- Tested with real use case: not yet (would need to build a skill from it)
- Known issues:
  1. Template is ~180 lines — at the upper bound of readability
  2. Corruption pre-inoculation section may not apply to all skill types
     (addressed via SKIP annotation)
  3. No worked example embedded — author must infer from annotations
- Known issues are acceptable: yes — all are in NICE TO HAVE scope

DECISION: SHIP as v1

IF SHIP:
- Ship as: v1 — ready for use, expect iteration after first few skills built from it
- Follow up with:
  1. Build one skill using the template, evaluate quality
  2. Create /skval skill for auditing existing skills against template criteria
  3. Retrofit highest-traffic tier-3 skills using the template
  4. Add worked example after building 2-3 skills from it (real examples > hypothetical)
```

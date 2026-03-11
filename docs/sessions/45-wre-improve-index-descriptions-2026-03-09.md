# /wre Review and improve the current index page's skill descriptions for clarity and consistency
**Date:** 2026-03-09
**Skill:** /wre (Writing Review & Edit)

---

## Interpretation

**Interpretation 2 -- Draft diagnosis.** The index page already has skill descriptions (the `desc` fields in tier1, tier2, categorySkills, and experimental arrays). The task is to assess what is wrong at the *requirements* level and produce a corrected set. This is reverse-engineering what requirements the descriptions should satisfy, identifying where current descriptions violate them, and producing fixes.

---

## Stage 0: Artifact Definition

```
ARTIFACT DEFINITION
  Type: UI microcopy (skill descriptions for a web index page)
  Venue: reasoningtool website homepage -- index.astro skill cloud
  Reader: Developer or knowledge worker evaluating whether to click on a skill
  Reader baseline: Knows what "thinking skills" means in this context; has seen the skill cloud; does not know what each individual skill does
  Writer goal: Each desc must communicate what the skill does in one sentence so the reader can decide whether to click
  Reader after-state: Reader can scan descriptions and quickly identify which skill matches their current need
  Core unresolved question: What makes a skill description simultaneously clear, consistent, and useful for rapid scanning?
  Scope boundary: NOT rewriting the full skill pages -- only the desc strings in index.astro (tier1, tier2, categorySkills, experimental)
  Stakes: Bad descriptions mean users can't find the right skill, reducing the toolkit from 563 skills to however many they stumble into
```

---

## Stage 1: Thesis Object

```
THESIS OBJECT
  Core thesis: The current descriptions are inconsistent in structure, voice, and specificity, making the skill cloud harder to scan than it needs to be
  Claim type: evaluative
  Weaker claim (trivially true): Some descriptions could be better
  Stronger claim (refused): All descriptions are broken and need total rewrites
  ACTUAL claim (defended): The descriptions have systematic patterns of inconsistency that can be fixed with a small set of rules applied uniformly

  Supporting claims:
    [C1] Descriptions vary in grammatical structure (some start with verbs, some with nouns, some with adjectives) -- REQUIRED_BECAUSE: inconsistent structure slows scanning
    [C2] Some descriptions explain the mechanism, others explain the benefit, others explain neither -- REQUIRED_BECAUSE: readers need to know what the skill DOES, not just what it IS
    [C3] Category skill descriptions leak implementation details (mentioning internal skill names like "ARAW" and "UAUA") -- REQUIRED_BECAUSE: new users don't know what those acronyms mean

  Out-of-scope claims:
    [O1] The skill titles need changing -- EXCLUDED_BECAUSE: titles are a separate concern
    [O2] The tier structure should be reorganized -- EXCLUDED_BECAUSE: organizational structure is not a description-level issue
```

---

## Stage 2: Technical Requirements

```
TECHNICAL REQUIREMENTS
[T1] Requirement: Every desc must be a single sentence, 8-15 words
     Category: length
     Verification: Word count of each desc falls in range

[T2] Requirement: Every desc must start with a present-tense verb (third person singular)
     Category: structure
     Verification: First word ends in -s or -es (Maps, Tests, Checks, Breaks, etc.)

[T3] Requirement: No internal jargon in tier1, tier2, or categorySkills descriptions (no ARAW, UAUA, GOSM, FOHT, MECE unless that IS the skill's name)
     Category: vocabulary
     Verification: Grep for acronyms; only permitted if the acronym is the skill's own title

[T4] Requirement: No implementation details in category skill descriptions (no "routes to X skill")
     Category: vocabulary
     Verification: No desc contains "routes" or references to other skill names

[T5] Requirement: Descriptions must describe what the skill produces or reveals, not how it works internally
     Category: tone
     Verification: Each desc answers "what do I get?" not "what algorithm runs?"

[T6] Requirement: No overlapping descriptions -- each desc must be distinguishable from every other
     Category: structure
     Verification: No two descriptions could be swapped without the user noticing
```

---

## Stage 3: Philosophical Requirements

```
PHILOSOPHICAL REQUIREMENTS
[P1] Requirement: Each description must make the skill's value proposition clear to someone who has never used it
     Category: reader understanding
     Verification: A new user can read the desc and know whether this skill helps with their current problem

[P2] Requirement: Category skills must describe what the USER gets, not what the SYSTEM does
     Category: anti-equivocation
     Verification: No category desc mentions routing, internal skill names, or system behavior

[P3] Requirement: Descriptions must not promise more than the skill delivers
     Category: anti-overclaim
     Verification: Each desc matches what the skill actually does (checked against SKILL.md frontmatter)

[P4] Requirement: The distinction between similar skills must be apparent from descriptions alone
     Category: distinctions
     Verification: Compare se/dd, cmp/cba, prm/fla, pv/vbo and confirm their descs differentiate them
```

---

## Stage 4: Expansion Requirements

```
EXPANSION REQUIREMENTS
[E1] Audit of all current descriptions against T1-T6 and P1-P4 -- Satisfies: T1-T6, P1-P4
     Type: analysis

[E2] Revised description for each skill that violates any requirement -- Satisfies: T1-T6, P1-P4
     Type: content

[E3] Before/after comparison showing what changed and why -- Satisfies: T5, P1
     Type: section
```

---

## Stage 5: Outline Requirements

```
OUTLINE REQUIREMENTS
[L1] Section: Current Description Audit
     Purpose: Identify every violation of T1-T6 and P1-P4
     Satisfies: E1
     Exit condition: Every description has been checked and violations are cataloged

[L2] Section: Revised Descriptions (by tier)
     Purpose: Provide corrected desc strings
     Satisfies: E2
     Exit condition: Every revised desc passes all T and P requirements

[L3] Section: Change Log
     Purpose: Show before/after with rationale
     Satisfies: E3
     Exit condition: Every change has a stated reason tied to a requirement ID
```

---

## Stage 6: Exclusions

```
EXCLUSIONS
[X1] Do not change skill names or titles -- WHY: scope creep; titles are a separate concern
[X2] Do not add descriptions to tier3/tier4 skills (they don't have desc fields in the current code) -- WHY: different data structure, different task
[X3] Do not change the experimental skill descriptions to match the same pattern if their nature genuinely requires different framing -- WHY: experimental skills may benefit from signaling their experimental nature
[X4] Do not rewrite descriptions to be marketing copy -- WHY: clarity > persuasion; users need information, not pitches
```

---

## Stage 7: Traceability Matrix

```
TRACEABILITY MATRIX
[E1] satisfies [T1, T2, T3, T4, T5, T6, P1, P2, P3, P4]
[E2] satisfies [T1, T2, T3, T4, T5, T6, P1, P2, P3, P4]
[E3] satisfies [T5, P1]
[L1] satisfies [E1]
[L2] satisfies [E2]
[L3] satisfies [E3]

UNSATISFIED REQUIREMENTS: None
DECORATIVE ELEMENTS: None
```

---

## Stage 8: Draft Gate

- [x] Artifact has one core unresolved question
- [x] Thesis object is a claim
- [x] Stronger claim refused is explicit
- [x] Technical requirements are atomic and testable
- [x] Philosophical requirements are atomic and testable
- [x] Expansion requirements trace to T and P requirements
- [x] Outline requirements trace to expansion requirements
- [x] Exclusions are explicit (4 total)
- [x] At least one equivocation risk has been neutralized (P2: "routes to" vs. user value)
- [x] At least one likely reader objection has a planned location (L3: change log explains why)
- [x] Traceability matrix has zero unsatisfied requirements
- [x] Traceability matrix has zero decorative elements

```
DRAFT READINESS
STATUS: READY
BLOCKERS: None
NEXT ACTION: Execute L1, L2, L3
```

---

## L1: Current Description Audit

### Tier 1 Skills

| Skill | Current Desc | Violations |
|-------|-------------|------------|
| se | "Systematically lists options in a problem space to reduce blind spots" | T1: 11 words, OK. T2: starts with adverb+verb, not verb. Fix. |
| aex | "Surfaces the hidden assumptions in any claim, plan, or argument" | T2: "Surfaces" -- good. T1: 11 words, OK. Pass. |
| cmp | "Structured comparison of options with explicit criteria and trade-offs" | T2: starts with adjective "Structured", not a verb. Fix. |
| ht | "Tests claims by examining what would be true if right vs. wrong" | T2: "Tests" -- good. T1: 13 words, OK. Pass. |
| dcp | "Builds a step-by-step flowchart anyone can follow for a recurring decision" | T2: "Builds" -- good. T1: 12 words, OK. Pass. |
| dcm | "Breaks complex problems into smaller, solvable parts" | T2: "Breaks" -- good. T1: 8 words, OK. Pass. |
| rca | "Traces problems back toward root causes rather than treating symptoms" | T2: "Traces" -- good. T1: 10 words, OK. Pass. |
| dd | "Identifies all the dimensions along which something can vary" | T2: "Identifies" -- good. T1: 9 words, OK. Pass. |
| mv | "Checks that a breakdown is mutually exclusive and collectively exhaustive" | T2: "Checks" -- good. T3: "MECE" is in the title, not the desc -- OK. T1: 10 words, OK. Pass. |
| ins | "Combines findings from multiple analyses into coherent conclusions" | T2: "Combines" -- good. T1: 8 words, OK. Pass. |
| cba | "Structured evaluation of costs vs. benefits with explicit trade-offs" | T2: starts with adjective "Structured", not a verb. P4: overlaps with cmp ("explicit trade-offs" appears in both). Fix both. |
| gu | "Clarifies what someone actually wants vs. what they said they want" | T2: "Clarifies" -- good. T1: 11 words, OK. Pass. |

**Tier 1 violations:** se (T2), cmp (T2), cba (T2, P4)

### Tier 2 Skills

| Skill | Current Desc | Violations |
|-------|-------------|------------|
| pv | "Checks whether a procedure works by testing each step" | Pass. |
| ai | "Flips assumptions to discover what happens if the opposite is true" | Pass. |
| to | "Finds the correct order when tasks depend on each other" | Pass. |
| cda | "Applies solutions from one field to problems in another" | Pass. |
| ma | "Generates combinations by varying parameters across dimensions" | Pass. |
| sya | "Maps how parts of a system interact and where leverage points are" | Pass. |
| br | "Works backward from the goal to figure out what steps are needed" | Pass. |
| prm | "Imagines the project failed and asks why, before it starts" | Pass. P4: check against fla below. |
| fla | "Identifies likely failure modes before they happen" | P4: vs prm -- prm is retrospective imagination ("imagines it failed"), fla is forward identification ("identifies failure modes"). Distinct enough. Pass. |
| poa | "Explores what is possible, not just what is likely" | Pass. |
| ifss | "Searches the space of valid inferences from given premises" | Pass. |
| rci | "Keeps asking 'why' until you reach the actual root" | T2: "Keeps" -- acceptable as verb. Pass. |
| la | "Identifies real constraints and which ones can be changed" | Pass. |
| vbo | "Checks every claim for evidence before presenting it" | P4: vs pv -- pv checks procedures, vbo checks claims for evidence. Distinct. Pass. |
| val | "Uses multiple independent checks to validate a conclusion" | Pass. |

**Tier 2 violations:** None.

### Category Skills

| Skill | Current Desc | Violations |
|-------|-------------|------------|
| claim | "Routes claims to ARAW testing with appropriate depth and balance" | T3: "ARAW". T4: "Routes". P2: describes system, not user value. Fix. |
| decide | "Routes decisions to comparison, ARAW, or goal clarification" | T3: "ARAW". T4: "Routes". P2: describes system. Fix. |
| diagnose | "Routes diagnostic questions to UAUA exploration or causal tracing" | T3: "UAUA". T4: "Routes". P2: describes system. Fix. |
| search | "Routes exploration to UAUA, space enumeration, or dimension discovery" | T3: "UAUA". T4: "Routes". P2: describes system. Fix. |
| how | "Routes method-seeking to FOHT discovery or step generation" | T3: "FOHT". T4: "Routes". P2: describes system. Fix. |
| want | "Routes goals to WantTo analysis to trace commitments and find the actual want" | T3: "WantTo". T4: "Routes". P2: describes system. T1: 14 words, borderline. Fix. |
| action | "Routes commands to direct execution or step generation" | T4: "Routes". P2: describes system. Fix. |
| evaluate | "Routes evaluation to ARAW, MECE validation, or assumption extraction" | T3: "ARAW", "MECE". T4: "Routes". P2: describes system. Fix. |
| emotion | "Acknowledges emotions, identifies implicit needs, routes appropriately" | T4: "routes". P2: partially describes system. T2: "Acknowledges" -- good start but then drifts. Fix. |
| viability | "Routes ideas to ARAW viability testing with risk assessment" | T3: "ARAW". T4: "Routes". P2: describes system. Fix. |
| create | "Routes content requests to appropriate writing skills" | T4: "Routes". P2: describes system. Fix. |
| analyze | "Routes analytical requests to decomposition, systems analysis, or synthesis" | T4: "Routes". P2: describes system. Fix. |
| technical | "Routes to specialized skills based on domain and task type" | T4: "Routes". P2: describes system. Fix. |
| meta | "Skill discovery, usage guidance, and orientation" | T2: starts with noun, not verb. Fix. |
| certainty | "Continues analysis iteratively until thoroughly resolved" | Pass (borderline -- "Continues" is a verb, describes user value). |
| iterate | "Identifies what needs iteration, at what level, dimension, and scale -- then executes" | T1: 14 words, borderline but OK. Pass. |
| sp | "Improves a prompt before it gets answered -- adds precision, scope, and criteria" | T1: 13 words, OK. Pass. |

**Category skill violations:** 13 of 17 skills violate T3/T4/P2 (the "routes to" pattern). meta violates T2.

### Experimental Skills

| Skill | Current Desc | Violations |
|-------|-------------|------------|
| araw | "Tests both branches of any claim recursively" | Pass (ARAW is its own name). |
| uaua | "Alternates exploration and testing" | T2: "Alternates" -- good. T1: 5 words -- under minimum. Could be more informative. Fix. |
| gosm | "Routes input through the appropriate analysis chain" | T4: "Routes". P2: describes system. Fix. |
| gts | "The fundamental pattern: generate possibilities, then search using criteria" | T2: starts with article "The", not a verb. Fix. |

**Experimental violations:** uaua (T1), gosm (T4, P2), gts (T2)

---

## L2: Revised Descriptions

### Tier 1 -- Revised

| Skill | Original | Revised | Req Fixed |
|-------|----------|---------|-----------|
| se | Systematically lists options in a problem space to reduce blind spots | **Lists all options in a problem space to expose blind spots** | T2 |
| cmp | Structured comparison of options with explicit criteria and trade-offs | **Compares options against explicit criteria to clarify trade-offs** | T2 |
| cba | Structured evaluation of costs vs. benefits with explicit trade-offs | **Weighs costs against benefits to surface the best trade-off** | T2, P4 |

All other tier 1 descriptions pass requirements and remain unchanged.

### Tier 2 -- Revised

No changes required. All tier 2 descriptions pass.

### Category Skills -- Revised

| Skill | Original | Revised | Req Fixed |
|-------|----------|---------|-----------|
| claim | Routes claims to ARAW testing with appropriate depth and balance | **Tests a claim from both sides to find where it holds and where it breaks** | T3, T4, P2 |
| decide | Routes decisions to comparison, ARAW, or goal clarification | **Structures a decision by clarifying goals, comparing options, and testing assumptions** | T3, T4, P2 |
| diagnose | Routes diagnostic questions to UAUA exploration or causal tracing | **Finds the cause of a problem by tracing symptoms back to their source** | T3, T4, P2 |
| search | Routes exploration to UAUA, space enumeration, or dimension discovery | **Explores an open-ended space by mapping its dimensions and possibilities** | T3, T4, P2 |
| how | Routes method-seeking to FOHT discovery or step generation | **Discovers the method for doing something by working from goals to steps** | T3, T4, P2 |
| want | Routes goals to WantTo analysis to trace commitments and find the actual want | **Uncovers what you actually want beneath what you said you want** | T3, T4, P2, T1 |
| action | Routes commands to direct execution or step generation | **Turns a goal into an executable sequence of concrete steps** | T4, P2 |
| evaluate | Routes evaluation to ARAW, MECE validation, or assumption extraction | **Assesses work by testing its claims, checking its coverage, and surfacing gaps** | T3, T4, P2 |
| emotion | Acknowledges emotions, identifies implicit needs, routes appropriately | **Processes a feeling to identify the unmet need driving it** | T4, P2 |
| viability | Routes ideas to ARAW viability testing with risk assessment | **Tests whether an idea works by probing its assumptions and risks** | T3, T4, P2 |
| create | Routes content requests to appropriate writing skills | **Produces a piece of writing matched to your goal, audience, and format** | T4, P2 |
| analyze | Routes analytical requests to decomposition, systems analysis, or synthesis | **Breaks down a situation to reveal its structure, causes, and leverage points** | T4, P2 |
| technical | Routes to specialized skills based on domain and task type | **Applies domain-specific expertise to a technical question or task** | T4, P2 |
| meta | Skill discovery, usage guidance, and orientation | **Shows which skills exist and which ones fit your current situation** | T2 |

### Experimental Skills -- Revised

| Skill | Original | Revised | Req Fixed |
|-------|----------|---------|-----------|
| uaua | Alternates exploration and testing | **Alternates between exploring possibilities and testing them until convergence** | T1 |
| gosm | Routes input through the appropriate analysis chain | **Selects and sequences the right analysis steps for a given input** | T4, P2 |
| gts | The fundamental pattern: generate possibilities, then search using criteria | **Generates candidate solutions then searches them against criteria** | T2 |

---

## L3: Change Log

### Pattern 1: "Routes to X" replaced with user-facing value (T3, T4, P2)
**13 category skills** all used the pattern "Routes [input] to [internal skill names]". This violates T3 (no internal jargon), T4 (no implementation details), and P2 (describe user value, not system behavior). Each was rewritten to describe what the user gets from using the skill.

### Pattern 2: Noun-phrase starts replaced with verb starts (T2)
- `cmp`: "Structured comparison" changed to "Compares"
- `cba`: "Structured evaluation" changed to "Weighs"
- `se`: "Systematically lists" changed to "Lists" (the adverb was unnecessary -- the verb already implies systematic listing in context)
- `meta`: "Skill discovery, usage guidance..." changed to "Shows which skills exist..."
- `gts`: "The fundamental pattern:" changed to "Generates candidate solutions..."

### Pattern 3: Overlapping descriptions differentiated (P4)
- `cmp` and `cba` both contained "explicit trade-offs" and "structured [noun]". Now `cmp` emphasizes *comparing against criteria* while `cba` emphasizes *weighing costs against benefits*.

### Pattern 4: Underspecified descriptions expanded (T1)
- `uaua`: "Alternates exploration and testing" (5 words) expanded to include "until convergence" to convey when the process ends.

### Unchanged (pass all requirements)
- **Tier 1:** aex, ht, dcp, dcm, rca, dd, mv, ins, gu
- **Tier 2:** All 15 skills
- **Category:** certainty, iterate, sp
- **Experimental:** araw

---

## Summary of All Recommended `desc` Values

For direct copy-paste into `index.astro`:

### tier1
```
se:    'Lists all options in a problem space to expose blind spots'
aex:   'Surfaces the hidden assumptions in any claim, plan, or argument'
cmp:   'Compares options against explicit criteria to clarify trade-offs'
ht:    'Tests claims by examining what would be true if right vs. wrong'
dcp:   'Builds a step-by-step flowchart anyone can follow for a recurring decision'
dcm:   'Breaks complex problems into smaller, solvable parts'
rca:   'Traces problems back toward root causes rather than treating symptoms'
dd:    'Identifies all the dimensions along which something can vary'
mv:    'Checks that a breakdown is mutually exclusive and collectively exhaustive'
ins:   'Combines findings from multiple analyses into coherent conclusions'
cba:   'Weighs costs against benefits to surface the best trade-off'
gu:    'Clarifies what someone actually wants vs. what they said they want'
```

### tier2
```
(no changes)
```

### categorySkills
```
claim:     'Tests a claim from both sides to find where it holds and where it breaks'
decide:    'Structures a decision by clarifying goals, comparing options, and testing assumptions'
diagnose:  'Finds the cause of a problem by tracing symptoms back to their source'
search:    'Explores an open-ended space by mapping its dimensions and possibilities'
how:       'Discovers the method for doing something by working from goals to steps'
want:      'Uncovers what you actually want beneath what you said you want'
action:    'Turns a goal into an executable sequence of concrete steps'
evaluate:  'Assesses work by testing its claims, checking its coverage, and surfacing gaps'
emotion:   'Processes a feeling to identify the unmet need driving it'
viability: 'Tests whether an idea works by probing its assumptions and risks'
create:    'Produces a piece of writing matched to your goal, audience, and format'
analyze:   'Breaks down a situation to reveal its structure, causes, and leverage points'
technical: 'Applies domain-specific expertise to a technical question or task'
meta:      'Shows which skills exist and which ones fit your current situation'
certainty: 'Continues analysis iteratively until thoroughly resolved'
iterate:   'Identifies what needs iteration, at what level, dimension, and scale -- then executes'
sp:        'Improves a prompt before it gets answered -- adds precision, scope, and criteria'
```

### experimental
```
araw:  'Tests both branches of any claim recursively'
uaua:  'Alternates between exploring possibilities and testing them until convergence'
gosm:  'Selects and sequences the right analysis steps for a given input'
gts:   'Generates candidate solutions then searches them against criteria'
```

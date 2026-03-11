# /rca Why do some skills produce great outputs and others feel flat?
**Date:** 2026-03-09
**Skill:** /rca (Root Cause Analysis)

---

## Interpretations

**Interpretation 2 — Recurring pattern diagnosis**: This is a recurring quality variance across 592 skills. Some consistently produce rich, insightful outputs; others consistently feel mechanical or shallow. Previous awareness of the problem hasn't resolved it. This needs systemic root cause analysis.

Proceeding with Interpretation 2.

---

## Step 0: Context Detection and Variant Selection

| Factor | Value | Notes |
|--------|-------|-------|
| Time Pressure | NORMAL | No urgency — this is a design improvement question |
| Recurrence risk | HIGH | Every invocation of a weak skill reproduces the problem |
| Impact severity | HIGH | Quality variance undermines trust in the entire toolkit |
| Complexity | COMPLEX | Multiple interacting design factors across 592 skills |

**Selected variant**: RCA-Full because HIGH recurrence, COMPLEX system, and the question is fundamentally about systemic patterns across hundreds of skills. Cross-skill pattern analysis is essential.

---

## Step 1: Define and scope the problem

**Problem statement**: Across the 592-skill reasoning toolkit, skill output quality varies dramatically. Some skills (e.g., /araw, /gu) consistently produce rich, structured, insightful outputs that feel like genuine thinking tools. Other skills (e.g., /acr) produce outputs that feel mechanical, generic, or shallow — more like textbook summaries than reasoning instruments.

**Impact**:
- **Frequency**: Affects every invocation of an underperforming skill (potentially hundreds of uses)
- **Severity**: A flat skill wastes the user's time and erodes confidence in the toolkit
- **Scope**: Likely affects a substantial fraction of the 592 skills (rough estimate: 40-60% are below the quality bar set by the best skills)

**Timeline**: The variance exists from skill creation. It's a design-time problem, not a runtime degradation.

**Who is affected**: Every user who invokes a skill that falls below the quality bar.

**Problem vs solution distinction**:
- NOT: "We need to rewrite all the skills" (proposed solution)
- IS: "Skill quality varies systematically along identifiable dimensions, and the root causes of that variance are not yet understood"

---

## Step 2: Gather evidence

### Evidence from direct comparison of three skills

**Exhibit A: /araw (flagship, rich output)**
- 423 lines
- Has: Corruption Pre-Inoculation section (anticipates failure modes)
- Has: Core Principles that override procedure ("when procedure conflicts with principle, follow the principle")
- Has: Anti-Failure Checks table with specific signals and fixes
- Has: Depth scaling with concrete numeric floors
- Has: Explicit phase separation (Exploration → Registry → Synthesis)
- Has: Worked examples with numbered findings (F1, F2...)
- Has: Classification labels with precise meanings (Necessary/Probable/Possible, Fatal/Serious/Conditional)
- Has: "Bedrock" concept — defines what counts as a valid stopping point and what doesn't
- Has: Multi-valued wrongness (not just "NOT X" but expanded state space)
- Key trait: **The skill constrains the LLM's worst tendencies** — softness, premature synthesis, validation bias, cheerleading

**Exhibit B: /gu (tier 1, rich output)**
- 491 lines
- Has: Interpretations section with three distinct modes
- Has: Context Detection with variant selection (URGENT, LOW stakes, EXPERT, AMBIGUOUS)
- Has: Complexity Assessment (SIMPLE / COMPOUND / AMBIGUOUS) with distinct handling
- Has: Clarification vs Substitution check — a specific gate against a known failure mode
- Has: Multiple worked examples per step showing good vs bad
- Has: Goal Journey Structure with explicit uncertainty markers
- Has: Common Goal Patterns (5 patterns with routing decisions)
- Has: Question Quality Criteria with priority ordering
- Key trait: **The skill models the problem space** — it knows what kinds of goals exist, what goes wrong with goal-setting, and routes accordingly

**Exhibit C: /acr (tier 3, flat output)**
- 167 lines
- Has: 7 steps described in generic instructional prose
- Missing: No interpretations section
- Missing: No context detection or variant selection
- Missing: No depth scaling
- Missing: No worked examples
- Missing: No anti-failure checks
- Missing: No classification labels or precision vocabulary
- Missing: No routing to other skills
- Missing: No explicit constraints on LLM behavior
- Key trait: **The skill reads like a textbook chapter**, not a reasoning instrument. It tells you WHAT active recall is but doesn't constrain HOW the LLM should apply it.

### What changed between quality tiers

| Dimension | /araw (flagship) | /gu (tier 1) | /acr (tier 3) |
|-----------|-------------------|---------------|----------------|
| Lines | 423 | 491 | 167 |
| Interpretations | Yes (3) | Yes (3) | No |
| Context/variant selection | Yes | Yes | No |
| Depth scaling | Yes (numeric floors) | Yes (variant-based) | No |
| Worked examples | Extensive (per step) | Extensive (per step) | None |
| Anti-failure checks | Explicit table | Substitution gate | None |
| LLM behavior constraints | Multiple (corruption pre-inoculation, bedrock, phase separation) | Substitution check, uncertainty marking | None |
| Precision vocabulary | Detailed (9 classification labels) | Moderate (OPEN/CLOSED, complexity types) | None |
| Skill routing | Yes | Yes (5 routes) | No |
| Meta-awareness | Yes (knows its own failure modes) | Yes (knows goal-setting failure modes) | No |

### Facts vs assumptions

- **VERIFIED**: Line count correlates with output quality in these three examples
- **VERIFIED**: /araw and /gu both have anti-failure mechanisms; /acr does not
- **VERIFIED**: /acr lacks interpretations, context detection, depth scaling, and examples
- **UNVERIFIED**: Whether line count alone is causal (could be a proxy for design effort)
- **UNVERIFIED**: Whether all 592 skills follow this pattern (sample of 3)
- **UNVERIFIED**: Whether all the mechanisms in /araw are necessary or if a subset drives most of the quality

---

## Step 3: Apply 5 Whys technique

### Causal Chain 1: The "Generic Instructions" Chain

**Problem**: Some skills produce flat, mechanical outputs.

**Why?** The skill file reads like generic instructions rather than a reasoning instrument.

**Why?** The skill was written to describe WHAT the technique is, not to constrain HOW the LLM applies it.

**Why?** The skill author was documenting a technique rather than designing a prompt that compensates for LLM failure modes.

**Why?** The skill design didn't start from "what goes wrong when an LLM does this?" — it started from "what is this technique?"

**Why?** There was no explicit design framework that required skills to include anti-failure mechanisms, worked examples, and LLM-specific constraints.

**ROOT CAUSE 1**: Skills were designed as technique descriptions rather than LLM behavior specifications. No design standard required modeling what goes wrong.

### Causal Chain 2: The "No Constraints" Chain

**Problem**: LLM produces generic, safe, textbook-quality output when running a skill.

**Why?** The skill gives the LLM freedom to follow its default tendencies (agreeable, verbose, generic).

**Why?** The skill doesn't include mechanisms to counteract LLM defaults (validation bias, premature synthesis, softness).

**Why?** The skill author didn't identify the specific ways the LLM would degrade this particular technique.

**Why?** Identifying LLM failure modes for a specific technique requires testing the skill and observing where outputs go flat — which is time-intensive.

**Why?** With 592 skills, systematic testing and iteration of each skill was not feasible at scale.

**ROOT CAUSE 2**: LLM-specific failure mode identification requires per-skill testing that doesn't scale across 592 skills without explicit tooling or a reusable pattern library.

### Causal Chain 3: The "Missing Structure" Chain

**Problem**: User gets a wall of generic text instead of structured, actionable output.

**Why?** The skill doesn't specify output format, classification labels, or numbered tracking.

**Why?** The skill was written as prose instructions rather than structured procedure with explicit output schema.

**Why?** Simpler skills were treated as "obvious" — the assumption was that the technique was simple enough not to need heavy structuring.

**Why?** The design effort allocated to each skill was proportional to perceived complexity of the technique, not to the difficulty of getting good LLM output for that technique.

**ROOT CAUSE 3**: Design effort was allocated by technique complexity, not by LLM output difficulty. "Simple" techniques got simple prompts — but LLMs need structure most when the technique is vague enough for them to default to generic behavior.

---

## Step 4: Apply Ishikawa (Fishbone) analysis

### METHODS (Process)

| Potential Cause | Evidence | Status |
|----------------|----------|--------|
| No standard skill template enforcing quality components | /acr lacks components that /araw and /gu have | **CONFIRMED** |
| No mandatory quality checklist for skill creation | Tier 3 skills are missing entire sections | **CONFIRMED** |
| Skills created in bulk without individual iteration | 592 skills suggests batch creation | **PROBABLE** |
| No review process comparing new skills to flagship quality | Quality variance exists across tiers | **PROBABLE** |

### MATERIALS (Inputs/Design)

| Potential Cause | Evidence | Status |
|----------------|----------|--------|
| Some skills based on well-understood problem spaces (decisions, goals) while others are generic techniques | /araw models claim-testing; /acr describes a study method | **CONFIRMED** |
| Flagship skills encode domain knowledge about failure modes; tier 3 skills don't | /araw has corruption pre-inoculation; /acr has nothing equivalent | **CONFIRMED** |
| Flagship skills have precision vocabulary; tier 3 skills use natural language | /araw: Fatal/Serious/Conditional; /acr: generic prose | **CONFIRMED** |

### MEASUREMENT (Quality Signals)

| Potential Cause | Evidence | Status |
|----------------|----------|--------|
| No metric for skill output quality | Quality is judged by feel, not measurement | **PROBABLE** |
| No way to compare skill outputs across tiers | The problem statement itself describes this variance | **CONFIRMED** |
| No feedback loop from skill usage to skill improvement | Skills are static after creation | **PROBABLE** |

### ENVIRONMENT (Context)

| Potential Cause | Evidence | Status |
|----------------|----------|--------|
| Scale pressure (592 skills) creates quantity/quality tradeoff | Can't give every skill the 400+ line treatment | **CONFIRMED** |
| Some techniques are inherently harder to make LLM-specific | Active recall is a human technique; ARAW is an LLM-native technique | **CONFIRMED** |
| LLM-native techniques (ARAW) naturally produce better prompts because they were designed FOR LLMs | ARAW was invented as an LLM reasoning pattern | **PROBABLE** |

---

## Step 5: Apply Fault Tree Analysis

```
TOP EVENT: "Skill produces flat output"
  OR gate:
  ├── "Skill lacks LLM behavior constraints"
  │   AND gate:
  │   ├── "No anti-failure checks specified"
  │   └── "LLM defaults to generic, agreeable, surface-level behavior"
  │
  ├── "Skill lacks structural scaffolding"
  │   OR gate:
  │   ├── "No output format specified"
  │   ├── "No classification labels or precision vocabulary"
  │   ├── "No numbered tracking of findings"
  │   └── "No depth scaling"
  │
  ├── "Skill lacks contextual intelligence"
  │   OR gate:
  │   ├── "No interpretations section (can't adapt to input type)"
  │   ├── "No variant selection (can't adapt to urgency/complexity)"
  │   └── "No routing to other skills (dead end)"
  │
  └── "Skill describes technique instead of specifying behavior"
      AND gate:
      ├── "Written as 'what is this technique' rather than 'how should LLM execute'"
      └── "No worked examples showing good vs bad execution"
```

**Key insight from fault tree**: The OR gates at level 2 mean that ANY of these structural absences degrades quality. But the deepest AND gate — "describes technique + no worked examples" — is the most fundamental. A skill that merely describes a technique without showing execution examples gives the LLM almost nothing to calibrate against.

---

## Step 6: Synthesize and prioritize root causes

### Consolidated Root Causes

| # | Root Cause | Confidence | Impact | Actionability | Priority Score |
|---|-----------|------------|--------|---------------|---------------|
| RC1 | **Skills designed as technique descriptions, not LLM behavior specs** — the skill tells the LLM what the technique IS rather than constraining how to EXECUTE it well | High | High | High | **9/9** |
| RC2 | **No anti-failure mechanisms** — flagship skills model what goes wrong (validation bias, premature synthesis, softness) and counteract it; flat skills don't | High | High | High | **9/9** |
| RC3 | **No structural scaffolding** — missing output formats, classification labels, depth scaling, and numbered tracking that force precision | High | High | High | **9/9** |
| RC4 | **No worked examples** — flat skills tell the LLM what to do but never show it what good execution looks like vs bad execution | High | High | Medium | **8/9** |
| RC5 | **Design effort allocated by technique complexity, not LLM output difficulty** — "simple" techniques got thin prompts, but LLMs need MORE structure for vague techniques, not less | High | Medium | Medium | **7/9** |
| RC6 | **Scale pressure** — 592 skills can't all get the 400-line flagship treatment; batch creation produced quality variance | Medium | High | Low | **5/9** |

### Contributing Factors

| Factor | Relationship |
|--------|-------------|
| CF1: No mandatory skill template/checklist | Enabled RC1-RC4 to happen |
| CF2: No per-skill testing and iteration | Prevented feedback that would surface quality issues |
| CF3: Some techniques are inherently more LLM-native than others | /araw was designed FOR LLMs; /acr was adapted FROM human learning science |
| CF4: No quality metric beyond subjective feel | Can't improve what you can't measure |

### Symptoms (not causes)

- "Some skills feel flat" — this is the presenting symptom
- "Output feels mechanical" — symptom of missing anti-failure checks
- "Output feels generic" — symptom of missing precision vocabulary and classification labels

### Cause Patterns

RC1, RC2, RC3, and RC4 are all expressions of a single systemic issue: **the difference between a skill that describes a technique and a skill that programs LLM behavior**. The flagship skills aren't just longer — they're a fundamentally different kind of artifact. They're adversarial prompts that anticipate and counteract the ways LLMs degrade specific reasoning tasks.

---

## Step 7: Develop corrective actions

### Immediate: Define the "Skill Quality Anatomy"

**Specific change**: Extract the common structural elements from /araw and /gu into an explicit checklist of what makes a skill produce rich output:

1. **Interpretations section** — 2-3 interpretations of the input, with disambiguation
2. **Context detection & variant selection** — adapt to urgency, complexity, stakes
3. **Depth scaling** — numeric floors that scale with requested depth
4. **Anti-failure checks** — table of specific ways the LLM degrades THIS technique, with signals and fixes
5. **Precision vocabulary** — classification labels specific to this technique's domain
6. **Worked examples** — good vs bad execution, per step
7. **Output format specification** — numbered tracking, structured sections
8. **Skill routing** — where to go next, what feeds in
9. **Bedrock/stopping criteria** — what counts as "done" vs what's premature

**Addresses**: RC1, RC2, RC3, RC4
**Effort**: Medium (extract pattern, document once)
**Success criteria**: Checklist exists and can be applied to evaluate any skill

### Corrective: Triage skills by quality gap

**Specific change**: Score all 592 skills against the quality anatomy checklist. Classify into:
- **A-tier** (7+ of 9 elements): Leave as-is
- **B-tier** (4-6 of 9 elements): Upgrade with targeted additions
- **C-tier** (0-3 of 9 elements): Full redesign or deprecation

**Addresses**: RC5, RC6, CF4
**Effort**: High (systematic audit)
**Success criteria**: Every skill has a quality score and upgrade path

### Preventive: "Anti-Failure First" design methodology

**Specific change**: When creating or upgrading a skill, start from: "What are the 3-5 specific ways an LLM will degrade this technique?" Design the skill to counteract those failure modes FIRST, then add the technique description.

This inverts the current approach (describe technique → hope for good output) into (identify failure modes → constrain behavior → describe technique).

**Addresses**: RC1, RC2 (the two highest-priority root causes)
**Effort**: Low (mindset shift, document in skill creation guidelines)
**Success criteria**: New skills start with an anti-failure section before the steps

### Systemic: Create a "Skill Minimum Viable Structure" template

**Specific change**: Build a template that every skill must include at minimum:
```
- Interpretations (3)
- Context detection + variant selection
- At least 1 anti-failure check
- At least 1 worked example per step
- Output format specification
- Depth scaling (even if just 2 levels)
```

Skills below this minimum either get upgraded or get deprecated.

**Addresses**: CF1 (the missing template that enabled all root causes)
**Effort**: Medium
**Success criteria**: Template exists; new skills are validated against it; no skill ships without minimum structure

---

## Step 8: Create verification plan

### For each root cause

| Root Cause | Confirming Evidence | Disproving Evidence | Test |
|-----------|-------------------|-------------------|------|
| RC1: Technique description vs behavior spec | Upgrade a tier-3 skill to behavior spec format and observe quality improvement | Upgraded skill produces same flat output | Pick 3 tier-3 skills, upgrade them, run identical inputs, compare outputs |
| RC2: No anti-failure mechanisms | Add anti-failure checks to a flat skill and observe LLM stops degrading in the predicted ways | LLM degrades in the same ways despite checks | Add corruption pre-inoculation equivalent to /acr, test with 5 inputs |
| RC3: No structural scaffolding | Add output format + labels to a flat skill and observe more structured output | Output stays generic despite structure | Add classification labels and numbered tracking to /acr, test |
| RC4: No worked examples | Add good-vs-bad examples to a flat skill and observe LLM calibrates against them | LLM ignores examples | Add 2 worked examples to /acr, test |

### Overall verification

**If we fix the identified root causes, will the problem be solved?**
If RC1-RC4 are correctly identified, upgrading a tier-3 skill with all four elements should produce output quality comparable to tier-1 skills. The test is: upgrade /acr fully, run it on the same input, and compare.

**How will we know the fix worked?**
- Upgraded skill outputs should be noticeably more specific, structured, and non-generic
- Anti-failure checks should prevent the specific degradation modes they target
- Users should not be able to distinguish upgraded tier-3 skills from tier-1 skills in blind comparison

**Metrics to monitor**:
- Leading: Percentage of skills meeting minimum viable structure
- Lagging: User-perceived quality of skill outputs (before/after upgrade)

**If the fix doesn't work**:
If upgraded skills still produce flat output, the root cause may be deeper — possibly that certain techniques are fundamentally unsuited to LLM execution, or that the quality difference is driven by something not captured in structural analysis (e.g., the *specificity of domain knowledge* embedded in flagship skills that can't be templated).

---

## Cross-Incident Pattern Analysis (RCA-Full)

The quality variance in this toolkit mirrors a broader pattern in prompt engineering: **the difference between describing a task and programming behavior**.

The flagship skills (/araw, /gu) succeed because they do something specific: they model the failure modes of the LLM when executing that particular technique, and they build countermeasures directly into the prompt. This is analogous to defensive programming — you don't just write the happy path; you write guards against the known failure modes.

The flat skills (/acr) fail because they treat the LLM like a human reader — "here's what active recall is; now go do it." But LLMs aren't human readers. They have specific, predictable failure modes: validation bias, premature synthesis, softness in adversarial positions, generic prose when not constrained, and surface-level analysis when not forced deep. A skill that doesn't counteract these modes will produce output that reflects them.

**The systemic root cause is a design philosophy gap**: the toolkit evolved from "document techniques" to "program LLM behavior" — but not all skills made the transition. The earliest and most-iterated skills learned the lesson; the bulk-created skills didn't.

---

## Verification Checklist

- [x] Context assessed and appropriate variant selected (RCA-Full)
- [x] Problem statement is specific and solution-neutral
- [x] Evidence was gathered before theorizing causes (Step 2 before Steps 3-5)
- [x] Multiple RCA techniques applied (5 Whys, Ishikawa, Fault Tree)
- [x] Each root cause is supported by evidence from skill comparison
- [x] Root causes are actionable (not "bad luck" or "human error")
- [x] Corrective actions address root causes, not just symptoms
- [x] Verification plan exists to confirm the analysis
- [x] Cross-incident pattern analysis completed
- [x] Predictions logged: upgrading /acr with the quality anatomy should produce measurably better output

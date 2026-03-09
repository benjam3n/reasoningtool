---
name: "edit - Editorial Analysis"
description: Analyze writing for specific editorial problems — redundancy, weak verbs, hedge stacking, buried leads, paragraph structure failures, unsupported claims, tonal inconsistency. Not grammar checking but structural editing.
---

# Editorial Analysis

**Input**: $ARGUMENTS

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Full editorial analysis**: The user provides a piece of writing and wants a comprehensive editorial assessment — structural, logical, and sentence-level issues identified and prioritized.
**Interpretation 2 — Targeted editorial pass**: The user provides writing and specifies a concern ("check my transitions," "is this too wordy," "does the argument hold"). Run only the relevant analysis phases.
**Interpretation 3 — Editorial comparison**: The user provides two versions of a piece and wants to know which is stronger and why, with specific editorial reasoning.

If ambiguous, ask: "I can do a full editorial analysis, focus on a specific concern, or compare two versions — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Corruption Pre-Inoculation

**"It's good" is not an editorial finding.** If your analysis produces fewer than 3 substantive issues per 500 words, you are reading as a fan, not an editor. Every piece has problems. Your job is to find them, name them precisely, and explain the fix. Compliments without specificity ("great flow," "compelling argument") are noise.

---

## Core Principles

1. **Name the disease, not the symptom.** "This sentence is awkward" is a symptom. "This sentence has a dangling modifier that attaches the action to the wrong subject" is a diagnosis. Always diagnose. Writers can fix diagnoses; they cannot fix "awkward."

2. **Structure outranks sentences.** A structural problem (wrong order, missing section, buried lead) causes more damage than any sentence-level issue. Always assess structure first. Polishing sentences in a structurally broken piece is rearranging deck chairs.

3. **Every edit must have a reason.** "I would change this" is opinion. "This hedge stack ('it might possibly be somewhat') undermines authority — pick one qualifier or assert directly" is editing. State the principle violated, not your preference.

4. **The reader's clock is ticking.** Every sentence costs the reader time. If a sentence does not advance the argument, provide evidence, or orient the reader, it is wasting their time. Time-wasting is the cardinal editorial sin.

5. **Tone is a promise.** The first paragraph sets a tonal contract with the reader. Every subsequent paragraph must honor that contract. When the tone shifts without reason — formal to casual, measured to urgent — the reader loses trust, even if they cannot articulate why.

6. **Editing is not rewriting.** The goal is to make the writer's piece better, not to replace it with your piece. Preserve voice. Fix problems. Suggest alternatives that stay within the writer's register, not yours.

---

## Phase 1: STRUCTURAL ANALYSIS

### Step 1: Map the Architecture

Read the entire piece once without marking anything. Then:

```
PIECE TYPE: [argument / narrative / explanation / persuasion / report / other]
STATED OR IMPLIED THESIS: [one sentence]
INTENDED AUDIENCE: [who is this written for?]
INTENDED TONE: [what tonal register is attempted?]
LENGTH: [word count]
SECTION COUNT: [number of distinct sections or major transitions]
```

### Step 2: Section-Level Audit

For each section or major block:

```
SECTION [N]: [title or topic]
  JOB: [what this section does for the piece — one clause]
  DELIVERS: [YES — it does the job / PARTIAL — it attempts but fails / NO — it does not do this job]
  POSITION: [CORRECT — it's in the right place / MOVE — should come earlier/later / CUT — piece works without it]
```

**Finding A — Structural verdict**: Classify the overall structure:
- **SOUND**: Sections are in logical order, each does its job, no major gaps
- **REORDERABLE**: Right sections, wrong sequence — specify the correct order
- **INCOMPLETE**: Missing a section the argument requires — specify what's missing
- **BLOATED**: Contains sections that do no work — specify which to cut
- **BROKEN**: Fundamental structural problem — specify what

### Step 3: Lead Analysis

```
OPENING SENTENCE: [quote it]
LEAD TYPE: [direct thesis / anecdote / question / scene-setting / throat-clearing]
HOOK STRENGTH: [STRONG — reader compelled to continue / ADEQUATE — functional / WEAK — reader may stop]
BURIED LEAD: [Is the actual point stated in paragraph 1, 2, 3, or later?]
```

**Finding B — Lead assessment**: If the lead is buried past paragraph 2 (for non-narrative pieces), flag it. State where the real opening should begin.

---

## Phase 2: LOGIC AND EVIDENCE ANALYSIS

### Step 4: Claim Inventory

List every claim the piece makes, explicitly or implicitly:

```
CLAIM [N]: [statement]
  SUPPORT: [what evidence is provided — quote or summarize]
  SUPPORT QUALITY: [STRONG / ADEQUATE / WEAK / MISSING]
  TYPE: [data / example / authority / logic / analogy / assertion-only]
```

**Finding C — Unsupported claims**: List every claim with WEAK or MISSING support. For each, state what kind of support would fix it.

### Step 5: Transition Audit

For every paragraph boundary, state the logical relationship:

```
¶[N] → ¶[N+1]: [therefore / however / specifically / for example / meanwhile / UNCLEAR]
```

**Finding D — Logic gaps**: List every UNCLEAR transition. For each, state whether:
- The relationship exists but is not signaled (add a transition)
- The relationship does not exist (paragraphs are in wrong order or one should be cut)
- A step in the argument is missing between them (add content)

---

## Phase 3: SENTENCE-LEVEL ANALYSIS

### Step 6: Verb Audit

Scan for weak verb patterns:

```
WEAK VERBS FOUND:
  - "is/are/was/were [adjective]" constructions: [count] — [worst examples]
  - Nominalized verbs ("make a decision" vs "decide"): [count] — [worst examples]
  - Passive voice where active is clearer: [count] — [worst examples]
  - Empty verbs ("seems to," "appears to," "tends to"): [count] — [worst examples]
```

**Finding E — Verb strength score**: [count of weak verbs] / [total sentences] = weakness ratio. Above 0.3 is a problem.

### Step 7: Hedge and Redundancy Scan

```
HEDGE STACKS: [sentences with 2+ hedging words — "might possibly," "somewhat arguably"]
  - [quote sentence] → FIX: [pick one hedge or assert directly]

REDUNDANCIES: [places where the same idea is stated twice in different words]
  - ¶[N] says [X], ¶[M] says [X again] → FIX: [keep the stronger version, cut the other]

THROAT-CLEARING: [opening phrases that delay the point — "It is important to note that...", "In order to...", "The fact that..." — list all instances]
```

**Finding F — Bloat inventory**: Total words that could be cut without losing meaning. Express as percentage of total word count.

### Step 8: Tone Consistency Check

```
BASELINE TONE (from first 2 paragraphs): [formal/informal, technical/plain, measured/urgent, personal/impersonal]

TONE BREAKS:
  ¶[N]: [shifts to X tone] — [quote the sentence] — REASON: [justified by content shift / unjustified]

REGISTER INCONSISTENCIES: [contractions consistent? jargon level consistent? sentence formality consistent? — list violations]
```

**Finding G — Tone verdict**: CONSISTENT / MOSTLY CONSISTENT with [N] breaks / INCONSISTENT — needs register decision.

---

## Phase 4: EDITORIAL SUMMARY

### Step 9: Prioritized Issue List

Compile all findings into a single prioritized list:

```
EDITORIAL SUMMARY
=================

STRUCTURAL ISSUES (fix these first):
  1. [issue from Findings A-B] — SEVERITY: [critical/major/minor] — FIX: [specific action]
  2. ...

LOGIC ISSUES (fix these second):
  3. [issue from Findings C-D] — SEVERITY: [critical/major/minor] — FIX: [specific action]
  4. ...

SENTENCE ISSUES (fix these last):
  5. [issue from Findings E-G] — SEVERITY: [critical/major/minor] — FIX: [specific action]
  6. ...

OVERALL ASSESSMENT:
  Strongest element: [what works best and why — be specific]
  Weakest element: [what needs most work and why — be specific]
  Estimated revision effort: [light / moderate / heavy / rewrite]
```

### Step 10: Sample Edits

For the top 3 issues, provide before/after with the principle each fix serves (not "sounds better").

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Grammar-only editing** | All findings are comma splices and subject-verb agreement | Those are proofreading, not editing. Restart with structural analysis. |
| **Rewriting instead of editing** | Suggested changes sound like a different writer | Preserve the author's voice. Fix the problem within their register. |
| **Vague diagnosis** | "This section is unclear" without stating WHY | Name the specific disease: buried lead, unsupported claim, logic gap, hedge stack. |
| **Compliment sandwich** | Starting and ending with praise to soften criticism | State findings directly. Praise only what genuinely works, and be specific about why. |
| **Missing the forest** | 40 sentence-level notes but no structural assessment | Always do Phase 1 first. A structural problem makes sentence edits irrelevant. |
| **Taste as editing** | "I would use a different word here" without a principle | Every edit needs a reason rooted in clarity, logic, tone, or reader experience — not preference. |

---

## Depth Scaling

| Depth | Structural | Logic | Sentence-Level | Sample Edits |
|-------|-----------|-------|----------------|-------------|
| 1x | Section-level audit only | Spot-check claims | Verb audit only | Top 1 issue |
| 2x | Full structural + lead analysis | All claims inventoried | Verb + hedge + redundancy | Top 3 issues |
| 4x | Full structural + reader journey mapping | All claims + all transitions | Full sentence-level + tone audit | Top 5 issues with alternatives |
| 8x | Structure + comparison to exemplars in genre | Full logic + counter-argument check | Complete sentence-level + rhythm analysis + read-aloud | All issues with multiple revision options |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Structure assessed before any sentence-level analysis
- [ ] Every finding names a specific disease, not just a symptom
- [ ] Every suggested fix includes the principle it serves (not just "sounds better")
- [ ] Unsupported claims are listed with what support type would fix them
- [ ] Logic gaps identify whether the problem is signaling, ordering, or missing content
- [ ] Tone breaks are classified as justified or unjustified
- [ ] Sample edits preserve the author's voice and register
- [ ] At least 3 substantive issues found per 500 words (if fewer, you were too soft)

---

## Integration

- **Use from**: `/draft` (after drafting is complete, run editorial analysis on the result), `/create` (when the created content needs quality assessment), `/pw` (after persuasive writing, check editorial quality)
- **Routes to**: `/draft` (if issues are severe enough to warrant a full redraft), `/cri` (for broader evaluation beyond editorial concerns)
- **Differs from**: `/cri` (critique evaluates whether the piece achieves its PURPOSE — is it good? `/edit` evaluates whether the piece is well-WRITTEN — is the craft sound?), `/draft` (drafting produces text; editing analyzes existing text)
- **Complementary**: `/draft` (draft then edit is the natural workflow), `/steelman` (for argumentative pieces, steelman the opposition before editing to catch logic gaps), `/aw` (assume-wrong the piece's central claims to find unsupported assertions)

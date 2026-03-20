---
name: "draft - Draft and Revise"
description: Structured drafting with revision cycles. First draft captures structure, second draft fixes logic, third draft polishes prose. Each revision has specific criteria. Prevents the common failure of trying to write perfectly on the first pass.
output:
  format: "prose"
---

# Draft and Revise

**Input**: $ARGUMENTS

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Writing from scratch**: The user has a topic, brief, or goal and needs to produce a complete piece through structured drafting. Start from zero and run all three drafts.
**Interpretation 2 — Revising existing writing**: The user has a draft that needs revision. Classify which draft stage it's at (structure/logic/prose) and run the remaining revision cycles.
**Interpretation 3 — Planning a complex document**: The user has a large or multi-section piece and needs a drafting plan — what to draft first, how to sequence revisions, where to expect the hardest problems.

If ambiguous, ask: "I can help with writing something from scratch through three drafts, revising an existing piece, or planning the drafting sequence for a complex document — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Corruption Pre-Inoculation

**Perfection on the first pass is the enemy.** The purpose of Draft 1 is to be bad — structurally complete but rough. If Draft 1 reads like polished prose, you skipped the thinking and went straight to performing. Resist the urge to polish early. Each draft has ONE job.

---

## Core Principles

1. **Separate generation from evaluation.** Draft 1 generates structure. Draft 2 evaluates logic. Draft 3 evaluates prose. Mixing these produces mediocre work at all three levels because the brain cannot optimize for structure, logic, and style simultaneously.

2. **Structure before sentences.** A well-structured piece with rough sentences is fixable. A poorly structured piece with beautiful sentences is not. Get the skeleton right first — the bones determine the shape.

3. **Every paragraph earns its place.** Each paragraph must do exactly one job. If you cannot state what job a paragraph does in one clause, it is doing zero jobs or two jobs. Both are failures.

4. **Revision is subtraction.** The primary operation of revision is cutting. First drafts are always too long because they contain the writer's thinking process, which the reader does not need. The ratio of Draft 1 words to Final words should be at least 1.3:1.

5. **Logic gaps hide in transitions.** The space between paragraphs is where arguments fail. If you cannot state the logical relationship between two consecutive paragraphs (therefore, however, specifically, meanwhile), there is no relationship and something is missing or misplaced.

6. **Read it as the reader.** The writer knows what they meant. The reader only knows what is on the page. Every revision pass must be done from the reader's perspective: what do they know at this point? What question are they asking right now?

---

## Phase 1: DRAFT 1 — Structure Draft

**Goal:** Get the full skeleton on the page. Every section exists. The argument flows in order. Nothing is polished.

### Step 1: Define the Piece

```
PURPOSE: [What is this piece trying to accomplish?]
AUDIENCE: [Who reads this? What do they already know?]
FORMAT: [Essay / memo / report / article / proposal / other]
LENGTH TARGET: [Word count or page count]
SINGLE SENTENCE: [The entire piece summarized in one sentence]
```

### Step 2: Build the Skeleton

List every section or major point in order. For each:

```
SECTION [N]: [Title or topic]
  JOB: [What this section does for the reader — one clause]
  KEY CLAIM: [The main assertion of this section]
  SUPPORT: [What evidence or reasoning supports it — bullets]
  EXIT: [What the reader should believe/know after this section]
```

**Finding A — Skeleton completeness**: Does the skeleton, read top to bottom as just the KEY CLAIM lines, form a coherent argument? If not, restructure before drafting.

### Step 3: Write Draft 1

Rules for Draft 1:
- Write fast. Do not stop to wordsmith.
- Placeholder brackets are fine: [need stat here], [expand this example]
- Every section from the skeleton must appear
- Transitions can be rough: "Next point:" is acceptable
- Do NOT delete anything — mark problems with [FIX: reason]
- Target 130% of final length (you will cut in Draft 2)

**Finding B — Coverage check**: After Draft 1, verify every skeleton section has content. Mark any gaps.

---

## Phase 2: DRAFT 2 — Logic Draft

**Goal:** Fix the argument. Every claim is supported. Every transition is justified. Every paragraph earns its place. Still not polishing prose.

### Step 4: Paragraph Audit

For EVERY paragraph, state:
```
¶[N] JOB: [one clause — what this paragraph does]
     CLAIM: [what it asserts]
     SUPPORT: [evidence given — or MISSING]
     CONNECTS TO NEXT VIA: [therefore / however / specifically / meanwhile / UNCLEAR]
```

**Finding C — Paragraph failures**: List paragraphs where:
- JOB is unclear or duplicates another paragraph's job
- CLAIM has no SUPPORT (unsupported assertion)
- Connection to next paragraph is UNCLEAR (logic gap)
- The paragraph does two jobs (split it)

### Step 4b: Thesis Originality Check

Before proceeding, test the piece's conclusion against predictability:
- State the thesis/conclusion in one sentence.
- Ask: is this the take that someone would reach by pattern-matching to existing commentary, without examining the evidence themselves?
- Ask: has this exact conclusion appeared in 10,000 other pieces on this topic?
- If yes to either: the thesis is pre-baked. Go back to the evidence and find the conclusion that the evidence actually supports — not the one that feels familiar.

### Step 5: Argument Flow Test

Read only the first sentence of every paragraph in sequence. Does this produce a coherent summary of the piece? If not, the first sentences are burying the lead — each paragraph's opening must signal its job.

**Finding D — Buried leads**: List paragraphs whose first sentence does not state or clearly imply the paragraph's job.

### Step 6: Cut and Restructure

- Delete paragraphs with no clear job
- Merge paragraphs doing the same job
- Add support where MISSING was flagged
- Fix transitions where UNCLEAR was flagged
- Move paragraphs if the flow test revealed ordering problems
- Fill in all [FIX: ] and placeholder brackets from Draft 1

**Finding E — Revision delta**: How many paragraphs were cut, merged, moved, or added? If fewer than 10% were changed, either Draft 1 was exceptional or Draft 2 was too gentle.

---

## Phase 3: DRAFT 3 — Prose Draft

**Goal:** Every sentence is clear, precise, and earns its words. Tone is consistent. The piece reads well aloud.

### Step 7: Sentence-Level Pass

For each sentence, check:
- **Verb strength**: Is the main verb carrying weight? Replace "is/are/was/were" constructions with action verbs where possible.
- **Hedge stacking**: Remove double hedges ("it might possibly be the case that perhaps"). One hedge maximum per claim.
- **Redundancy**: Cut phrases that repeat what the previous sentence said.
- **Specificity**: Replace vague quantifiers ("many," "often," "significant") with specific numbers or examples where available.
- **Sentence length variety**: Mix short (5-10 words) with medium (15-25 words). Flag any sentence over 35 words for splitting.

### Step 8: Tone Audit

```
INTENDED TONE: [authoritative / conversational / academic / urgent / other]
TONE BREAKS: [List sentences or sections that deviate from intended tone]
REGISTER SHIFTS: [Places where formality level changes without reason]
```

**Finding F — Tone consistency**: Note any section where the voice shifts (e.g., suddenly casual in a formal piece, suddenly academic in a practical piece).

**Finding F2 — Voice collapse check**: Read the piece as a stranger. Could any AI assistant have written this? Same cadence, same transitions ("Moreover," "It's worth noting," "This raises the question"), same paragraph rhythm? If yes, the voice has collapsed into generic LLM output. Rewrite until the prose has a specific voice — not just a competent one.

### Step 9: Read Aloud Test

Read the piece aloud (or simulate). Flag:
- Sentences that make you run out of breath (too long)
- Phrases that sound awkward spoken (rewrite)
- Repetitive sentence openings (vary them)
- Passages where your attention drifts (boring — cut or rewrite)

### Step 10: Final Cut

Target the stated length. If over, cut in this priority order:
1. Redundant sentences (saying what was already said)
2. Throat-clearing openings ("It is important to note that...")
3. Weakest examples (keep the best one, cut the rest)
4. Qualifications the reader can infer
5. Entire sections if still over (the weakest-job section goes)
6. Aspirational conclusions — if the last paragraph is "The future holds promise" or equivalent, delete it. If the piece is better without it, you were concluding with hope instead of substance. End on your last real point.

---

## Output Format

```
PIECE METADATA:
  Purpose: [from Step 1]
  Audience: [from Step 1]
  Format: [from Step 1]
  Final length: [word count]
  Drafts completed: [1/2/3]

FINDINGS:
  A — Skeleton completeness: [assessment]
  B — Coverage check: [gaps found or none]
  C — Paragraph failures: [count and types]
  D — Buried leads: [count fixed]
  E — Revision delta: [% of paragraphs changed in Draft 2]
  F — Tone consistency: [breaks found or consistent]

REVISION METRICS:
  Draft 1 word count: [N]
  Draft 2 word count: [N] (should be < Draft 1)
  Draft 3 word count: [N] (should be <= Draft 2)
  Paragraphs cut: [N]
  Paragraphs added: [N]
  Unsupported claims remaining: [N — should be 0]

[THE FINAL DRAFT]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Polishing too early** | Draft 1 reads like final copy — no brackets, no rough transitions | Force yourself to write faster. Set a time limit. Leave [FIX] markers. |
| **Skipping the skeleton** | Jumped straight to writing paragraphs without section plan | Stop. Build the skeleton first. The skeleton IS the thinking. |
| **Paragraph job blindness** | Cannot state what a paragraph does in one clause | The paragraph has no job. Delete it or give it one. |
| **Logic gap denial** | Transitions say "additionally" when the relationship is unclear | "Additionally" is not a logical connector. State the actual relationship. |
| **Revision as addition** | Draft 2 is longer than Draft 1 | You added instead of cutting. Go back and subtract first. |
| **Tone drift** | Formal piece suddenly has contractions and slang | Pick one register and enforce it. Rewrite deviating sections. |
| **Pre-baked thesis** | The conclusion is the most popular/predictable take on this topic | Return to evidence. What does it actually show? Find the conclusion no one has written yet. |
| **Voice collapse** | Prose sounds like any AI assistant — same cadence, transitions, structure | Rewrite for a specific voice. Cut "Moreover," "It's worth noting," and every transition that could appear in any piece. |
| **Aspiration as conclusion** | Final paragraph is vague hope ("great promise," "exciting future," "much to learn") | Delete it. End on the last substantive point. If that feels abrupt, the piece was leaning on the aspirational ending as a crutch. |

---

## Depth Scaling

| Depth | Skeleton Detail | Paragraph Audit | Prose Passes | Min Findings |
|-------|----------------|-----------------|--------------|-------------|
| 1x | Section titles + key claims | Spot-check 30% of paragraphs | One sentence-level pass | A, C |
| 2x | Full skeleton with support + exit | Every paragraph audited | Sentence + tone pass | A through D |
| 4x | Skeleton + counter-arguments per section | Full audit + flow test + read-aloud | All three passes + final cut | A through F |
| 8x | Multiple skeleton alternatives compared | Full audit + external reader simulation | Three full passes + read-aloud + length optimization | All findings + revision metrics |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Skeleton was built before any prose was written
- [ ] Every paragraph has a stated job (one clause, no duplicates)
- [ ] Every claim has support (no unsupported assertions remain)
- [ ] Every transition states a logical relationship (not "additionally" or "moreover" as filler)
- [ ] Draft 3 is shorter than or equal to Draft 1 (revision subtracted, not added)
- [ ] Tone is consistent throughout (no unexplained register shifts)
- [ ] First sentences of paragraphs produce a coherent summary when read alone
- [ ] All [FIX] markers and placeholder brackets are resolved

---

## Integration

- **Use from**: `/create` (when the creation task is a writing task), `/pw` (after persuasion strategy is set, draft the piece)
- **Routes to**: `/edit` (for deeper editorial analysis of the final draft), `/cri` (for evaluation of the finished piece)
- **Differs from**: `/pw` (persuasive writing focuses on influence strategy; `/draft` focuses on the drafting process itself — structure, logic, then prose), `/stl` (storytelling focuses on narrative arc; `/draft` handles any prose form)
- **Complementary**: `/edit` (use after `/draft` for a second opinion on editorial quality), `/steelman` (use before drafting argumentative pieces to ensure you address the strongest counter-arguments)

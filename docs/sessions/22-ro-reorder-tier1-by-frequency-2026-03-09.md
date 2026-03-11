# /ro Reorder the tier 1 skills by how often a typical user would actually need them
**Date:** 2026-03-09
**Skill:** /ro (Reorder)

---

## Phase 1: Input Parsing

```
[R1] ORIGINAL_LIST:
  1. se (Space Enumeration)
  2. aex (Assumption Extraction)
  3. cmp (Comparison)
  4. ht (Hypothesis Testing)
  5. dcp (Decision Procedure)
  6. dcm (Decomposition)
  7. rca (Root Cause Analysis)
  8. dd (Dimension Discovery)
  9. mv (MECE Validation)
  10. ins (Insight Synthesis)
  11. cba (Cost-Benefit Analysis)
  12. gu (Goal Understanding)

[R2] ITEM_COUNT: 12 items

[R3] OBJECTIVE: Rank by how frequently a typical user would invoke each skill in real-world usage. "Typical user" = someone using the toolkit for everyday thinking tasks — decisions, problem-solving, planning, writing, analysis. Not an expert auditor or logician.

[R4] CONSTRAINTS: None — pure frequency ranking, no fixed positions.

[R5] CONTEXT: The audience is someone deciding which skills to learn first or which to surface most prominently. Time horizon is "across months of regular use." The relevant question is: how many real situations map to this skill?

[R6] LIST_TYPE: Frequency/priority ranking
```

---

## Phase 2: Scoring Dimensions

```
[R7] DIMENSIONS:
  D1: Breadth of Applicability — WEIGHT: high — WHY: A skill that applies to many different situations will be invoked more often than one limited to a narrow context.
  D2: Frequency of Triggering Situation — WEIGHT: high — WHY: How often does an average person encounter the situation this skill addresses? Decisions are daily; MECE validation is occasional.
  D3: Standalone Usefulness — WEIGHT: medium — WHY: Skills that deliver value on their own get used more than skills that mainly serve as inputs to other skills.
  D4: Accessibility / Low Barrier — WEIGHT: medium — WHY: Skills that are easy to understand and invoke get used more. A skill people "get" immediately will be reached for more often than one that feels abstract.
```

### Dimension Independence Check
- D1 (breadth) and D2 (trigger frequency) can diverge: a skill could apply to many domains (broad) but each domain rarely triggers it.
- D3 (standalone) and D4 (accessibility) diverge: a skill can be powerful standalone but hard to grasp (e.g., hypothesis testing).

---

## Phase 3: Scoring

Scale: 5-point (1 = lowest, 5 = highest). Weights: D1 and D2 at 1.5x, D3 and D4 at 1.0x. Max possible = 5*(1.5+1.5+1+1) = 25.

```
[R-1] ITEM: dcm (Decomposition)
  D1: 5 — Nearly everything complex benefits from breaking it down
  D2: 5 — People encounter "this is too big/complex" daily
  D3: 5 — Produces a usable breakdown immediately
  D4: 5 — "Break this into parts" is universally understood
  TOTAL: 5(1.5) + 5(1.5) + 5(1) + 5(1) = 25.0
  CONFIDENCE: high

[R-2] ITEM: gu (Goal Understanding)
  D1: 5 — Applies to any task, project, or question
  D2: 5 — People constantly have goals they haven't fully articulated
  D3: 5 — Produces clarity on its own
  D4: 4 — "What am I actually trying to do?" is intuitive, though some resist introspection
  TOTAL: 5(1.5) + 5(1.5) + 5(1) + 4(1) = 24.0
  CONFIDENCE: high

[R-3] ITEM: dcp (Decision Procedure)
  D1: 4 — Applies whenever there's a choice to make
  D2: 5 — People make decisions constantly
  D3: 5 — Produces a decision with rationale
  D4: 4 — "Help me decide" is natural, though structured procedure feels heavier
  TOTAL: 4(1.5) + 5(1.5) + 5(1) + 4(1) = 22.5
  CONFIDENCE: high

[R-4] ITEM: cmp (Comparison)
  D1: 4 — Applies to any "A vs B" situation
  D2: 5 — Comparisons are a daily occurrence (tools, approaches, options)
  D3: 4 — Produces a clear comparison but often feeds into a decision
  D4: 5 — "Compare these" is the most natural framing people use
  TOTAL: 4(1.5) + 5(1.5) + 4(1) + 5(1) = 22.5
  CONFIDENCE: high

  TIEBREAK (dcp vs cmp): dcp edges ahead because its output (a decision) is more final and actionable than a comparison table. Users ultimately want to decide, not just compare. Placing dcp at #3, cmp at #4.

[R-5] ITEM: rca (Root Cause Analysis)
  D1: 3 — Applies to problems, bugs, failures, recurring issues
  D2: 4 — Things go wrong regularly in work and life
  D3: 5 — Produces the actual cause, which is immediately actionable
  D4: 4 — "Why did this happen?" is intuitive
  TOTAL: 3(1.5) + 4(1.5) + 5(1) + 4(1) = 19.5
  CONFIDENCE: high

[R-6] ITEM: cba (Cost-Benefit Analysis)
  D1: 3 — Applies to decisions with resource implications
  D2: 4 — "Is this worth it?" comes up frequently
  D3: 5 — Produces a clear should/shouldn't with reasoning
  D4: 5 — Everyone understands cost vs. benefit
  TOTAL: 3(1.5) + 4(1.5) + 5(1) + 5(1) = 20.5
  CONFIDENCE: medium

[R-7] ITEM: se (Space Enumeration)
  D1: 4 — Applies to brainstorming, planning, coverage checks
  D2: 3 — "List everything" is common but not daily
  D3: 4 — Produces a comprehensive list
  D4: 3 — "Enumerate the space" is jargon; users think "list all the options"
  TOTAL: 4(1.5) + 3(1.5) + 4(1) + 3(1) = 17.5
  CONFIDENCE: medium

[R-8] ITEM: aex (Assumption Extraction)
  D1: 4 — Applies to claims, plans, arguments, proposals
  D2: 3 — People don't naturally think "what am I assuming?" without prompting
  D3: 4 — Produces surfaced assumptions, immediately useful for risk-checking
  D4: 3 — Conceptually clear but people don't instinctively reach for it
  TOTAL: 4(1.5) + 3(1.5) + 4(1) + 3(1) = 17.5
  CONFIDENCE: medium

  TIEBREAK (se vs aex): se edges ahead because "list all the options/possibilities" is a more common user impulse than "extract my assumptions." People naturally want to enumerate before they interrogate.

[R-9] ITEM: ins (Insight Synthesis)
  D1: 3 — Applies when you have multiple analyses or sources to combine
  D2: 3 — Comes up after research or multi-step analysis
  D3: 4 — Produces coherent takeaways
  D4: 3 — "Synthesize" is understood but feels academic
  TOTAL: 3(1.5) + 3(1.5) + 4(1) + 3(1) = 16.0
  CONFIDENCE: medium

[R-10] ITEM: ht (Hypothesis Testing)
  D1: 3 — Applies to claims, theories, explanations
  D2: 3 — Scientific thinking situations are moderate-frequency
  D3: 4 — Produces validated/refuted hypothesis
  D4: 2 — "Hypothesis testing" feels formal; many users won't think to invoke it
  TOTAL: 3(1.5) + 3(1.5) + 4(1) + 2(1) = 15.0
  CONFIDENCE: medium

[R-11] ITEM: dd (Dimension Discovery)
  D1: 3 — Applies to novel or unfamiliar problem spaces
  D2: 2 — Only needed when facing something genuinely new
  D3: 3 — Primarily useful as input to other skills (se, ro, cmp)
  D4: 2 — "Discover the dimensions" is abstract for most users
  TOTAL: 3(1.5) + 2(1.5) + 3(1) + 2(1) = 12.5
  CONFIDENCE: medium

[R-12] ITEM: mv (MECE Validation)
  D1: 2 — Applies to lists and frameworks that need completeness checking
  D2: 2 — Validation is important but most people skip it
  D3: 3 — Useful but mainly a quality check on other outputs
  D4: 2 — "MECE" is consulting jargon; most people don't know the term
  TOTAL: 2(1.5) + 2(1.5) + 3(1) + 2(1) = 11.0
  CONFIDENCE: high
```

### Dependency Check

```
[R-13] DEPENDENCIES:
  dcm INDEPENDENT — no prerequisites
  gu INDEPENDENT — no prerequisites
  dcp INDEPENDENT — though often benefits from cmp or cba as inputs
  cmp INDEPENDENT — though often feeds into dcp
  rca INDEPENDENT — may invoke dcm internally but doesn't require it
  cba INDEPENDENT — may benefit from se for option coverage
  se INDEPENDENT — benefits from dd but works without it
  aex INDEPENDENT — no prerequisites
  ins REQUIRES prior analyses — but this is a sequence dependency, not a ranking dependency
  ht INDEPENDENT — though often follows aex
  dd INDEPENDENT — typically precedes se
  mv REQUIRES a list to validate — typically follows se or dcm

  NOTE: Since this is a frequency ranking (not an execution sequence), dependencies do not override scores.
```

---

## Phase 4: Reordered Output

```
[R-14] REORDERED_LIST:
  1.  dcm (Decomposition)        — SCORE: 25.0 — REASON: Universal applicability; everyone encounters "too complex" daily; instantly understood
  2.  gu (Goal Understanding)    — SCORE: 24.0 — REASON: Applies to literally everything; "what am I actually trying to do?" is the most leveraged question
  3.  dcp (Decision Procedure)   — SCORE: 22.5 — REASON: Decisions are constant; produces the thing people actually want (a decision)
  4.  cmp (Comparison)           — SCORE: 22.5 — REASON: "Compare A vs B" is the most natural analytical request; extremely accessible
  5.  cba (Cost-Benefit Analysis)— SCORE: 20.5 — REASON: "Is it worth it?" is a universal question; everyone understands the framing
  6.  rca (Root Cause Analysis)  — SCORE: 19.5 — REASON: Things break regularly; "why did this happen?" is a frequent, high-stakes question
  7.  se (Space Enumeration)     — SCORE: 17.5 — REASON: Common when brainstorming or planning, but not daily; slightly jargony framing
  8.  aex (Assumption Extraction)— SCORE: 17.5 — REASON: Broadly applicable but people don't instinctively think to extract assumptions
  9.  ins (Insight Synthesis)    — SCORE: 16.0 — REASON: Valuable after multi-step work, but the triggering situation (having multiple analyses to combine) is less frequent
  10. ht (Hypothesis Testing)    — SCORE: 15.0 — REASON: Powerful but formal-feeling; most people frame this as "check if X is true" not "test hypothesis"
  11. dd (Dimension Discovery)   — SCORE: 12.5 — REASON: Only needed for genuinely novel spaces; primarily an enabler for other skills
  12. mv (MECE Validation)       — SCORE: 11.0 — REASON: Quality-check skill; important but niche; "MECE" is opaque to most users
```

### Position Changes

```
[R-15] MOVEMENT:
  dcm: WAS #6  → NOW #1  — WHY: Most universally applicable skill; original placement drastically undervalued frequency
  gu:  WAS #12 → NOW #2  — WHY: Goal clarity applies to everything; was buried at the bottom of the original list
  dcp: WAS #5  → NOW #3  — WHY: Small move up; decisions are extremely frequent
  cmp: WAS #3  → NOW #4  — WHY: Minor shift down; still very high frequency but serves decisions rather than being one
  cba: WAS #11 → NOW #5  — WHY: Big jump; "is it worth it?" is far more common than original position suggests
  rca: WAS #7  → NOW #6  — WHY: Small move up; problem-solving is a daily need
  se:  WAS #1  → NOW #7  — WHY: Dropped significantly; systematic enumeration is valuable but not a frequent first impulse
  aex: WAS #2  → NOW #8  — WHY: Dropped; assumption extraction is powerful but people don't naturally reach for it
  ins: WAS #10 → NOW #9  — WHY: Small move up; synthesis comes up after extended work sessions
  ht:  WAS #4  → NOW #10 — WHY: Dropped significantly; formal hypothesis testing is infrequent for typical users
  dd:  WAS #8  → NOW #11 — WHY: Dropped; dimensional analysis is a specialist move
  mv:  WAS #9  → NOW #12 — WHY: Dropped to last; validation is the least-reached-for activity for typical users
```

---

## Phase 5: Sanity Check

```
[R-16] SANITY_CHECK:
  TOP_3_TEST: Do dcm, gu, dcp genuinely outrank everything below on frequency?
    YES — Decomposition ("break this down"), goal clarity ("what am I trying to do?"), and decision-making
    ("help me decide") are the three most universal cognitive tasks. A typical user will encounter all
    three multiple times per week, often multiple times per day.

  BOTTOM_3_TEST: Are ht, dd, mv genuinely lowest frequency?
    YES — Hypothesis testing requires scientific framing most users avoid. Dimension discovery only
    triggers for genuinely novel problem spaces. MECE validation is a quality audit that most users
    never think to perform. These are "expert-reach" skills, not daily drivers.

  ADJACENCY_TEST: Close-scored items:
    - dcp (22.5) vs cmp (22.5): Tiebreak is defensible — dcp produces a terminal output (a decision),
      cmp produces an intermediate output (a comparison). Users want decisions more than comparisons.
    - se (17.5) vs aex (17.5): Tiebreak is defensible — enumeration is a more natural impulse than
      assumption interrogation. People say "what are my options?" before "what am I assuming?"

  DEPENDENCY_TEST: Yes — no execution-sequence dependencies apply to a frequency ranking.

  ADJUSTMENTS: Considered swapping cba (#5) and rca (#6). Kept current order because "is it worth it?"
    situations (spending money, investing time, choosing tools) are slightly more frequent than "something
    broke" situations for a typical user who isn't in a pure engineering role.
```

### Confidence Flags

```
[R-17] CONFIDENCE_MAP:
  HIGH_CONFIDENCE: dcm at #1, gu at #2, mv at #12 — these placements are very stable
  LOW_CONFIDENCE: cba (#5) and rca (#6) could swap; se (#7) and aex (#8) could swap; ins (#9) and ht (#10) could swap
  MOST_DEBATABLE: cba at #5 — could be anywhere from #4 to #7 depending on user profile. A business user would put it higher; a developer would put it lower.
```

---

## Phase 6: Final Output

```
REORDERED LIST
==============

OBJECTIVE: Rank tier 1 skills by how often a typical user would actually invoke them
DIMENSIONS: Breadth of Applicability (high), Frequency of Triggering Situation (high),
            Standalone Usefulness (medium), Accessibility / Low Barrier (medium)
SCALE: 5-point, weighted (D1/D2 at 1.5x, D3/D4 at 1.0x), max = 25

REORDERED:
  1.  dcm (Decomposition)         — 25.0 — Everyone needs to break things down, constantly
  2.  gu  (Goal Understanding)    — 24.0 — Applies to everything; "what am I actually trying to do?"
  3.  dcp (Decision Procedure)    — 22.5 — Decisions are daily; produces the thing users want most
  4.  cmp (Comparison)            — 22.5 — "Compare A vs B" is the most natural analytical request
  5.  cba (Cost-Benefit Analysis) — 20.5 — "Is it worth it?" is universal and accessible
  6.  rca (Root Cause Analysis)   — 19.5 — Things break regularly; high-stakes when they do
  7.  se  (Space Enumeration)     — 17.5 — Common for brainstorming/planning, not daily
  8.  aex (Assumption Extraction) — 17.5 — Powerful but not a natural first impulse
  9.  ins (Insight Synthesis)     — 16.0 — Valuable after extended analysis, less frequent trigger
  10. ht  (Hypothesis Testing)    — 15.0 — Formal framing limits adoption despite broad applicability
  11. dd  (Dimension Discovery)   — 12.5 — Only for genuinely novel spaces; mainly enables other skills
  12. mv  (MECE Validation)       — 11.0 — Quality audit; important but rarely sought by typical users

KEY MOVEMENTS:
  dcm: #6  → #1  — Universal daily need was undervalued in original ordering
  gu:  #12 → #2  — Goal clarity is the foundation of everything; was last
  cba: #11 → #5  — "Worth it?" questions are far more common than position 11 implies
  se:  #1  → #7  — Systematic enumeration is valuable but not a frequent impulse
  aex: #2  → #8  — Assumption checking is critical but people don't naturally do it
  ht:  #4  → #10 — Formal hypothesis framing limits how often people invoke this

CONFIDENCE:
  MOST CERTAIN:  dcm at #1, gu at #2, mv at #12
  LEAST CERTAIN: cba at #5 — COULD ALSO BE: #4 or #6-7 depending on user type

DEPENDENCIES RESPECTED: Yes (not applicable — frequency ranking, not execution sequence)

READY FOR:
- /cmp cba vs rca — to examine whether cost-benefit or root-cause is truly more frequent
- /mv — to check if the tier 1 skill set itself is MECE across thinking tasks
- /dd — to discover if "frequency for typical users" should be decomposed into user archetypes
```

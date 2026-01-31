# FOHT 8x — Taxonomy of Standard Human Request Phrases

**Date**: 2026-01-30
**Depth**: 8x
**Input**: taxonomy of standard human request phrases

---

## FINDING REGISTRY

```
FINDING REGISTRY
================

SUCCESS CRITERIA:
[H1] Covers natural phrases real users type -- TYPE: must
[H2] Categories defined by intent with example phrases -- TYPE: must
[H3] Categories map to skills -- TYPE: must
[H4] Mutually exclusive at top level -- TYPE: must
[H5] Includes variation dimensions beyond intent -- TYPE: should
[H6] Covers >95% of realistic inputs -- TYPE: should
[H7] Usable as basis for /pig -- TYPE: should
[H8] Compact enough for single skill file -- TYPE: should

CONSTRAINTS:
[H9] Grounded in how people actually talk
[H10] Connected to existing 221-skill toolkit
[H11] For requests/instructions to LLM, not all human language

METHODS FOUND:
[H12] Bottom-up from examples -- SOURCE: direct
[H13] Speech act theory -- SOURCE: direct
[H14] Skill-backward -- SOURCE: direct
[H15] Question taxonomy (Bloom's/Graesser) -- SOURCE: direct
[H16] Ontology construction (category) -- SOURCE: category
[H17] Faceted classification -- SOURCE: category
[H18] Prototype theory -- SOURCE: category
[H19-H24] Inversion methods (3 blockers, 3 removals) -- SOURCE: inversion
[H25] Chatbot intent classification -- SOURCE: exemplar
[H26] Customer support categorization -- SOURCE: exemplar
[H27] Extend /sp's 4 types -- SOURCE: exemplar
[H28] Stack Overflow classification -- SOURCE: exemplar
[H29] Knowledge-state classification -- SOURCE: reframe
[H30] Generative grammar -- SOURCE: reframe
[H31-H35] Decomposition sub-goals -- SOURCE: decomposition

PREREQUISITES:
[H36] H12 needs real corpus -- FOR: H12 -- MET: partial
[H37] H13 needs speech acts mapping to LLM -- FOR: H13 -- MET: unknown
[H38] H14 needs understanding of 221 skills -- FOR: H14 -- MET: yes
[H39] H15 needs academic-to-casual adaptation -- FOR: H15 -- MET: unknown
[H40] H17 needs independent facets -- FOR: H17 -- MET: probable
[H41] H18 needs clear prototypical examples -- FOR: H18 -- MET: yes
[H42] H25 needs chatbot-to-reasoning mapping -- FOR: H25 -- MET: partial
[H43] H27 needs /sp types as valid subset -- FOR: H27 -- MET: probable
[H44] H29 needs knowledge-state inference -- FOR: H29 -- MET: probable
[H45] H30 needs finite combinable components -- FOR: H30 -- MET: unknown
[H46] All need taxonomy stability -- FOR: all -- MET: probable
[H47] All need disambiguation rules -- FOR: all -- MET: needs design

AR FINDINGS:
[H48] Bottom-up produces grounded categories -- FOR: H12 -- STRENGTH: necessary
[H49] Clusters emerge naturally by intent -- FOR: H12 -- STRENGTH: probable
[H55] Skill-backward guarantees skill coverage -- FOR: H14 -- STRENGTH: probable
[H56] Categories ARE skill input types by construction -- FOR: H14 -- STRENGTH: necessary
[H64] /sp's 4 types cover core propositional inputs -- FOR: H27 -- STRENGTH: probable
[H65] Existing validation saves re-derivation -- FOR: H27 -- STRENGTH: necessary
[H71] Independent facets produce complete descriptions -- FOR: H17 -- STRENGTH: necessary
[H72] Most information-dense approach -- FOR: H17 -- STRENGTH: probable
[H78] Components combine to generate all types -- FOR: H30 -- STRENGTH: probable
[H79] Naturally handles generation for /pig -- FOR: H30 -- STRENGTH: necessary
[H84] Knowledge state determines need -- FOR: H29 -- STRENGTH: necessary
[H85] Maps to existing decision tree -- FOR: H29 -- STRENGTH: probable
[H90] Speech acts provide theoretical grounding -- FOR: H13 -- STRENGTH: probable
[H91] Categories map to LLM context -- FOR: H13 -- STRENGTH: probable
[H96] Chatbot systems solved intent classification at scale -- FOR: H25 -- STRENGTH: necessary
[H97] Categories transfer to reasoning context -- FOR: H25 -- STRENGTH: probable

AW FINDINGS:
[H51] 40 examples may not cover space -- FOR: H12 -- SEVERITY: serious
[H53] Clustering is subjective -- FOR: H12 -- SEVERITY: conditional
[H58] Many skills overlap in input types -- FOR: H14 -- SEVERITY: serious
[H60] 221 categories before merging is too many -- FOR: H14 -- SEVERITY: serious
[H62] Some phrases don't map to any skill -- FOR: H14 -- SEVERITY: serious
[H67] /sp's types miss 7+ categories -- FOR: H27 -- SEVERITY: serious
[H69] Structure ≠ intent (conditional mismatch) -- FOR: H27 -- SEVERITY: conditional
[H74] Facets interact (frustration → fragments) -- FOR: H17 -- SEVERITY: conditional
[H76] 5 facets too complex for routing — only intent matters -- FOR: H17 -- SEVERITY: serious
[H81] Fragments/emotions break grammar -- FOR: H30 -- SEVERITY: fatal
[H83] Grammar too complex for casual language -- FOR: H30 -- SEVERITY: serious
[H87] Knowledge state not always inferrable -- FOR: H29 -- SEVERITY: serious
[H89] Produces user-state taxonomy, not phrase taxonomy -- FOR: H29 -- SEVERITY: conditional
[H92] Speech act categories too coarse -- FOR: H13 -- SEVERITY: serious
[H94] LLM interaction has categories speech acts don't cover -- FOR: H13 -- SEVERITY: serious
[H98] Chatbot intents designed for task completion, not thinking -- FOR: H25 -- SEVERITY: serious
[H100] Chatbot intents are flat lists, not structured -- FOR: H25 -- SEVERITY: conditional

EDGE CASES:
[H101] Continuations depend on prior context -- FOR: H27+H17
[H102] Compound inputs have multiple intents -- FOR: all
[H103] Skill-backward merge step is where quality lives -- FOR: H14
[H104] Taxonomy must be maintained as skills added -- FOR: all
[H105] Novel inputs need UNCLASSIFIED escape hatch -- FOR: all
[H106] 5 facets × levels = large space (feature for generation, cost for routing) -- FOR: H17
[H107] Implicit intent may differ from surface intent -- FOR: all
[H108] Meta-requests about the tool don't route to thinking skills -- FOR: all

METHOD VERDICTS:
[H12] Bottom-up from examples -- VERDICT: CONDITIONAL (good for grounding, insufficient alone)
  -- AR: H48, H49 -- AW: H51, H53 -- Prerequisites: H36 partial -- Edge: none
[H13] Speech act theory -- VERDICT: CONDITIONAL (too coarse, needs heavy adaptation)
  -- AR: H90, H91 -- AW: H92, H94 -- Prerequisites: H37 unknown -- Edge: none
[H14] Skill-backward -- VERDICT: CONDITIONAL (guarantees coverage, too many categories)
  -- AR: H55, H56 -- AW: H58, H60, H62 -- Prerequisites: H38 met -- Edge: H103
[H15] Question taxonomy -- VERDICT: UNCERTAIN (not tested — academic focus)
  -- Prerequisites: H39 unknown
[H17] Faceted classification -- VERDICT: VIABLE (intent primary, others secondary)
  -- AR: H71, H72 -- AW: H74, H76 -- Prerequisites: H40 probable -- Edge: H106
[H18] Prototype theory -- VERDICT: VIABLE (clear examples define categories)
  -- AR: implicit -- AW: none -- Prerequisites: H41 met -- Edge: none
[H25] Chatbot intents -- VERDICT: CONDITIONAL (meta-pattern transfers, specifics don't)
  -- AR: H96, H97 -- AW: H98, H100 -- Prerequisites: H42 partial -- Edge: none
[H27] Extend /sp types -- VERDICT: VIABLE (as starting subset, needs 7+ additions)
  -- AR: H64, H65 -- AW: H67, H69 -- Prerequisites: H43 probable -- Edge: H101
[H29] Knowledge-state -- VERDICT: CONDITIONAL (useful secondary dimension, not primary)
  -- AR: H84, H85 -- AW: H87, H89 -- Prerequisites: H44 probable -- Edge: none
[H30] Generative grammar -- VERDICT: ELIMINATED (fragments/emotions break grammar)
  -- AR: H78, H79 -- AW: H81, H83 -- Prerequisites: H45 unknown -- Edge: none

TOTALS:
- Success criteria: 8
- Methods found: 15 (including sub-goals and inversions)
- Prerequisites surfaced: 12 (3 met, 4 probable, 2 partial, 2 unknown, 1 needs design)
- AR findings: 17
- AW findings: 17 (1 fatal, 10 serious, 6 conditional)
- Edge cases: 8
- Verdicts: 3 viable, 5 conditional, 1 uncertain, 1 eliminated
```

---

## SYNTHESIS

```
GOAL: Complete taxonomy of standard human request phrases mapped to skills
DONE LOOKS LIKE: 12 intent categories + 4 secondary facets + disambiguation rules

METHODS TESTED: 10

VIABLE METHODS:
1. H17 (faceted classification) — VERDICT: viable
   - Requires: Independent facets (H40 probable)
   - Costs: Complexity for routing if all 5 facets used (H76)
   - Forecloses: Single-dimension classification (H73)
   - Breaks when: Over-weighted on secondary facets (H106)

2. H18 (prototype theory) — VERDICT: viable
   - Requires: Clear prototypical examples (H41 met)
   - Costs: Fuzzy boundaries between categories
   - Forecloses: Crisp necessary/sufficient definitions

3. H27 (extend /sp types) — VERDICT: viable (as starting point)
   - Requires: 7+ additional categories beyond /sp's 4 (H67, H68)
   - Costs: Inherits /sp's structure-over-intent bias (H69)
   - Forecloses: Starting from scratch
   - Breaks when: Continuations, meta-requests (H101, H108)

ELIMINATED METHODS:
1. H30 (generative grammar) — fragments and emotional inputs don't fit
   grammatical decomposition (H81, H82)

RECOMMENDED APPROACH:
Combine H27 + H17 + H18: Start from /sp's 4 types, extend to 12 categories
(H68), use faceted classification with intent as primary (H77), define
categories by prototypical examples (H18). Check coverage against skills
using H14 (skill-backward) as validation.

THE TAXONOMY:
12 intent categories:
  1. CLAIM — "X is true"
  2. DECISION — "Should I X?"
  3. DIAGNOSTIC — "Why is X?"
  4. EXPLORATORY — "What are the options?"
  5. METHOD-SEEKING — "How do I X?"
  6. GOAL-STATING — "I want to X"
  7. COMMAND — "Do X"
  8. EVALUATION — "Is this good?"
  9. CONTINUATION — "What's next?"
  10. EMOTIONAL/VENT — "I'm stuck" / "nothing works"
  11. META — "What can you do?"
  12. CREATIVE — "Write me a X"

4 secondary facets:
  - Precision: vague → directional → specific → over-specified
  - Structure: fragment → sentence → paragraph → list → multi-part
  - Emotion: neutral → curious → urgent → frustrated → skeptical
  - Context: zero → implied → partial → full → excess

5 disambiguation rules for ambiguous/compound/continuation/emotional inputs.

CATEGORY DETAILS:

1. CLAIM — asserting something is true
   Prototype: "X is true" / "X is better than Y"
   Phrases: "Remote work is more productive", "AI will replace most jobs",
   "This approach won't scale", "React is better than Vue", "The problem is
   that we're not marketing enough"
   Maps to: /araw, /ht, /ar, /aw, /aex

2. DECISION — choosing between options
   Prototype: "Should I X?" / "X or Y?"
   Phrases: "Should I change careers?", "React or Svelte?", "Should I take
   the job offer?", "Is it worth learning Rust?", "Should we build or buy?"
   Maps to: /dcp, /cmp, /cba, /araw, /crw, /mcd

3. DIAGNOSTIC — understanding why something is the case
   Prototype: "Why is X happening?" / "What's causing X?"
   Phrases: "Why are users churning?", "Why does the deploy keep failing?",
   "What's causing the performance issue?", "Why isn't this working?"
   Implicit: "X is broken" / "this isn't working"
   Maps to: /rca, /fowwr, /dbg, /sbfow, /rci

4. EXPLORATORY — mapping a space of possibilities
   Prototype: "What are all the ways to X?" / "What options exist?"
   Phrases: "What are my options for hosting?", "What are all the ways to
   grow revenue?", "How could I approach this?", "What should I consider?"
   Maps to: /se, /dd, /poa, /u, /ma

5. METHOD-SEEKING — knowing what but not how
   Prototype: "How do I X?" / "What's the best way to X?"
   Phrases: "How do I learn machine learning?", "What's the best way to
   prepare for an interview?", "How should I structure this project?"
   Implicit: "I need to X" (without asking how)
   Maps to: /foht, /stg, /br, /op, /pcd

6. GOAL-STATING — declaring a want or intention
   Prototype: "I want to X" / "I need to X"
   Phrases: "I want to start a business", "I need to improve my writing",
   "I want to switch to tech", "My goal is to launch by Q3"
   Implicit: sometimes just the noun — "career change" / "startup"
   Maps to: /wt, /gu, /gd, /grf, /br

7. COMMAND — directing a specific action
   Prototype: "Do X" / "Run X" / "Make X"
   Phrases: "Write a business plan", "Compare these two approaches",
   "List the pros and cons", "Summarize this", "Fix this code", "Do next"
   Maps to: depends on action — /w (writing), /cmp (comparison), /dbg (fix)
   Note: Bare commands ("do next") require context to route.

8. EVALUATION — assessing quality or correctness
   Prototype: "Is this good?" / "Does this work?" / "Check this"
   Phrases: "Is this plan solid?", "Does this argument hold up?", "Review
   my approach", "What's wrong with this?", "Is this MECE?"
   Maps to: /pv, /mv, /vbo, /val, /cor, /aex, /cri

9. CONTINUATION — extending prior context
   Prototype: "Now do X" / "Same for Y" / "What's next?"
   Phrases: "Now do that for the other option", "What's the next step?",
   "Keep going", "Do next", "Go deeper on point 3"
   Maps to: whatever skill is currently active (context-dependent)
   Note: Cannot be classified without conversation history.

10. EMOTIONAL/VENT — expressing frustration or feeling
    Prototype: "This is so frustrating" / "Nothing works" / "I'm stuck"
    Phrases: "I've tried everything and nothing works", "This is impossible",
    "I'm overwhelmed", "Ugh", "I don't even know where to start"
    Maps to: acknowledge, then route — /fowwr, /foht, /dcm, /wt
    Note: Implicit intent behind emotion determines skill.

11. META — about the tool or process itself
    Prototype: "What can you do?" / "What skills exist?"
    Phrases: "What skills are available?", "What's the difference between
    /ar and /aw?", "How does this work?", "Help", "What should I use for..."
    Maps to: /fnd, skill discovery, Getting Started
    Note: Don't invoke a thinking skill — invoke skill routing.

12. CREATIVE — requesting generation of content
    Prototype: "Write me a X" / "Create a X" / "Generate X"
    Phrases: "Write a blog post about...", "Draft an email to...",
    "Create a project proposal", "Generate names for..."
    Maps to: /w, /pw, /stl, /gw

DISAMBIGUATION RULES:
1. Classify by PRIMARY intent — what the user most wants from the response.
2. When ambiguous, prefer the category requiring LESS assumption about user state.
3. Compound inputs: classify by FIRST/MAIN request. Note secondary intents.
4. Continuations: classify based on conversation context, not phrase alone.
5. Emotional inputs: identify implicit intent BEHIND emotion, route there.

FIRST ACTIONS:
1. Build /pig skill using this taxonomy as its core — generates inputs
   by sampling intent categories × secondary facets — resolves: H7
2. Validate coverage by running H14 (skill-backward) — check that every
   skill's natural input fits at least one category — resolves: H3, H6
3. Update /sp to reference this taxonomy (its 4 types are a subset) —
   resolves: H10

UNRESOLVED:
- Whether 12 categories is the right number — may need splitting or merging
  after empirical testing (H102, H105)
- Whether CREATIVE should be a sub-type of COMMAND or its own category
- Whether CONTINUATION is a real intent type or a meta-property
- How to handle implicit intent vs surface intent (H107)
```

# /iterate Take the /list skill and identify what needs iteration — at what level, dimension, and scale
**Date:** 2026-03-09
**Skill:** /iterate (Iterate)

---

## Corruption Pre-Inoculation

The /list skill is one of mine. I will test it as if it were someone else's work. Praise for elegance or structure does not exempt it from rigor. If most findings say "this is fine," I am confirming, not analyzing.

---

## Phase 1: SURVEY

### Step 1: Identify the Subject

```
SUBJECT: /list skill (SKILL.md) — a structured procedure for building high-quality lists
CURRENT STATE: Complete, operational skill with 6 phases, 5 core principles, depth scaling, failure modes table, and integration section. 209 lines.
LAST CHANGED: Unknown exact date. Part of the original skill set.
```

### Step 2: Identify Iteration Dimensions

| Dimension | Question | Applies? |
|-----------|----------|----------|
| **IDEAS** | Are these the right ideas? Are any wrong? Missing? Redundant? | yes |
| **ANALYSIS** | Is the analysis rigorous? Deep enough? Tested enough? | yes |
| **EXPRESSION** | Is it said clearly? Concisely? Precisely? | yes |
| **STRUCTURE** | Is it organized well? Right sections? Right order? Right hierarchy? | yes |
| **SCOPE** | Is it the right size? Too broad? Too narrow? Too much? Too little? | yes |
| **COMPLETENESS** | Is anything missing? Any gaps? Any uncovered cases? | yes |
| **CORRECTNESS** | Is anything wrong? Errors? Inconsistencies? Contradictions? | yes |
| **INTEGRATION** | Does it fit with the rest of the system? Conflicts? Redundancies? | yes |
| **META** | Are we working on the right thing? Is this the right approach? | yes |

```
[I1] DIMENSION: IDEAS — NEED: medium — EVIDENCE: The five core principles are strong and non-obvious. However, Principle 1 ("lists are claims about category membership") is only true for some lists. Task lists, step sequences, and brainstorm dumps are not category-membership claims. The skill implicitly assumes all lists are classification lists. This is a real conceptual gap — it excludes or mishandles several common list types.

[I2] DIMENSION: ANALYSIS — NEED: low — EVIDENCE: The failure modes table is solid. The coverage check (Phase 5) is a genuine analytical contribution. The gap patterns are useful. Analysis depth is appropriate for a procedural skill.

[I3] DIMENSION: EXPRESSION — NEED: low — EVIDENCE: The language is clear and direct. No jargon. Imperative where it should be. The "rules before items" phrasing is crisp. A few phrases could be tighter but nothing is unclear.

[I4] DIMENSION: STRUCTURE — NEED: medium — EVIDENCE: The 6-phase structure (Contract → Inclusion Rules → Generation → Order & Label → Coverage Check → Output) is logical and well-sequenced. However, Phase 2 (Inclusion Rules) and Phase 1 (List Contract) could be merged — they are both "define before you generate" activities. The separation adds ceremony without adding clarity. Also, the Output phase (Phase 6) includes ASSUMPTIONS that were never generated in any prior phase — they appear ex nihilo.

[I5] DIMENSION: SCOPE — NEED: medium — EVIDENCE: The skill handles "build a list from scratch" well but does not handle "improve an existing list" at all. Users frequently arrive with a draft list that needs upgrading. The skill forces a full rebuild. Additionally, the depth scaling table (1x through 8x) is purely quantitative (item count, strategy count) and does not scale the rigor of inclusion rules or coverage checks, which are the actual quality drivers.

[I6] DIMENSION: COMPLETENESS — NEED: high — EVIDENCE: Several significant gaps: (a) No handling of list types beyond category/classification lists — task lists, priority lists, dependency lists, brainstorm lists all have different needs. (b) No "assumptions" generation step even though the output format requests assumptions. (c) No guidance on what to do when the user gives a vague domain ("list some ideas for...") — the skill assumes the domain is clear. (d) The generation strategies table lists 5 strategies but never instructs when to use which. (e) No anti-duplication procedure during generation — overlap rule is stated but no procedure to apply it.

[I7] DIMENSION: CORRECTNESS — NEED: low — EVIDENCE: No outright errors. The claim that "inclusion rules before items" is "non-negotiable" is stated as principle and enforced in the failure modes table. The depth scaling numbers are reasonable. One minor inconsistency: the Output section says "READY FOR: /ro — to reorder this list by a different objective" but the Integration section says "Routes to: /ro (reorder by different criteria)" — these say the same thing differently, which is fine but mildly inconsistent in phrasing.

[I8] DIMENSION: INTEGRATION — NEED: medium — EVIDENCE: The skill mentions /ro, /mv, /se, /etc, and /o in its Integration section. But it does not mention /iterate (how to iterate on a list once built), /evaluate (how to assess a list), or /claim (to test whether the list's implicit claims hold). Given that the skill's own Principle 1 says lists ARE claims, the absence of routing to /claim is a missed connection. Also, the "Differs from" section is helpful but incomplete — it doesn't mention /aso (also/and-so-on expansion).

[I9] DIMENSION: META — NEED: low — EVIDENCE: The skill's fundamental approach — define criteria, generate, filter, order, check coverage — is the right approach to list-building. This is well-established in information architecture and taxonomy design. The meta-approach is sound.
```

### Step 3: Identify Iteration Level

```
[I10] LEVEL NEEDED: paragraph — with a few section-level changes
[I11] EVIDENCE: The core structure and ideas are right. The gaps are at the level of missing paragraphs (e.g., a step for assumption generation, guidance for list types, a procedure for applying the overlap rule) and a few section-level issues (merging Phases 1-2, adding an "existing list" entry path). We are not rewriting the file or rethinking the approach.
[I12] RISK OF WRONG LEVEL: If we iterate at word level, we polish prose while leaving the conceptual gaps (list types, existing-list path) untouched. If we iterate at file level, we risk losing the strong existing structure for marginal gains. Paragraph level targets the actual problems.
```

### Step 4: Identify Iteration Type

```
[I13] TYPE NEEDED: extend (primary) + refine (secondary)
[I14] EVIDENCE: The core is right but incomplete. The main work is adding what is missing (list type handling, existing-list entry path, assumption generation step, overlap procedure) and refining what exists (depth scaling, integration section). This is not a restructure or rethink — the architecture holds.
```

### Step 5: Identify Scale

```
[I15] SCALE: moderate revision
[I16] EVIDENCE: 5-8 specific changes needed, none requiring rewrite of major sections. The existing content is retained; new content is added in specific locations.
[I17] ITEMS TO ITERATE: 8
```

---

## Phase 2: PRIORITIZE

### Step 6: What Most Needs Iteration?

```
ITERATION PRIORITY MAP:

HIGH PRIORITY (iterate these first):

[I18] Principle 1 assumes all lists are classification lists — DIMENSION: IDEAS — LEVEL: paragraph — TYPE: refine
      WHY: The foundational claim ("lists are claims about category membership") is only true for a subset of lists. Task lists, step sequences, and dependency lists are not category-membership claims. This is the first thing users read. If the framing is wrong, everything downstream is tilted.
      EFFORT: small
      → Could invoke /claim to test "all lists are claims about category membership"

[I19] No handling of existing lists — DIMENSION: COMPLETENESS — LEVEL: section — TYPE: extend
      WHY: Users frequently arrive with "here's my list, make it better." The skill only handles "build from scratch." This is probably the most common real-world use case the skill misses.
      EFFORT: medium

[I20] Output phase requests ASSUMPTIONS but no prior phase generates them — DIMENSION: CORRECTNESS — LEVEL: paragraph — TYPE: extend
      WHY: The output template includes an ASSUMPTIONS section, but no step in the procedure asks the user or analyst to identify assumptions. This is a broken pipeline — the output references data that was never created.
      EFFORT: small

[I21] No procedure for applying the overlap rule — DIMENSION: COMPLETENESS — LEVEL: paragraph — TYPE: extend
      WHY: L9 defines an OVERLAP_RULE but there is no step that says "check each item pair for overlap and apply the rule." The rule exists but is never triggered.
      EFFORT: small

MEDIUM PRIORITY (iterate if time allows):

[I22] Depth scaling is purely quantitative — DIMENSION: IDEAS — LEVEL: paragraph — TYPE: refine
      WHY: Scaling by item count and strategy count misses the actual quality levers: rigor of inclusion rules, depth of coverage checks, and strength of ordering justification. A list of 25 items with no coverage check is not better than a list of 10 with a thorough one.
      EFFORT: medium

[I23] Integration section missing key routes — DIMENSION: INTEGRATION — LEVEL: paragraph — TYPE: extend
      WHY: Does not mention /iterate, /evaluate, /claim, or /aso. Given the skill's own emphasis on lists-as-claims, not routing to /claim is a conceptual miss.
      EFFORT: small

[I24] Generation strategies listed but no guidance on when to use which — DIMENSION: COMPLETENESS — LEVEL: paragraph — TYPE: extend
      WHY: Five strategies are named. A user at depth 2x should use 2 strategies. But which 2? The table gives no selection criteria. "Categorical sweep" and "negative space" are far more rigorous than "brainstorm." Some guidance on matching strategy to goal would help.
      EFFORT: small

LOW PRIORITY (marginal improvement):

[I25] Phases 1 and 2 could be merged — DIMENSION: STRUCTURE — LEVEL: section — TYPE: restructure
      WHY: Both phases are "define before generating." Separating them adds a phase boundary that does not correspond to a conceptual boundary. However, the current separation works fine and does not confuse users. Low urgency.
      EFFORT: medium

[I26] No explicit guidance for vague domains — DIMENSION: COMPLETENESS — LEVEL: paragraph — TYPE: extend
      WHY: When user says "list some ideas for my startup," the domain is unclear. The skill assumes L3 (DOMAIN) can be cleanly stated. Could add a clarification sub-step. But this is a minor edge case — most users can state their domain.
      EFFORT: small

DO NOT ITERATE:

[I27] Core Principles 2-5 — WHY NOT: "Inclusion rules before items," "granularity must be consistent," "order is not optional," "coverage is testable" are all strong, non-obvious, and correctly stated. These are the best part of the skill. Touching them risks degradation.

[I28] Phase 3 (Generation) template format — WHY NOT: The candidate format with PASSES_INCLUSION, GRANULARITY_MATCH, STATUS is well-designed and functional. Changing it adds churn without improvement.

[I29] Failure modes table — WHY NOT: All 8 failure modes are real, the signals are accurate, and the fixes are actionable. This table is done.
```

### Step 7: What Should Be Deleted?

```
DELETION CANDIDATES:

[I30] DELETE: The word "non-negotiable" in Principle 2 — REASON: Unnecessary intensifier. The principle speaks for itself. "Non-negotiable" is the kind of word that sounds authoritative but adds nothing. The procedure enforces it; the adjective is redundant.
      IMPACT IF DELETED: Slightly cleaner prose. Principle still enforced by the failure mode "Generated then filtered."
      RISK IF DELETED: None.

[I31] DELETE: "Differs from /o" line in Integration — REASON: This line reads "o ranks viable options from a decision context; list builds general-purpose lists." This is a weak distinction. /o and /list serve clearly different purposes and the distinction is obvious from their names and descriptions. The line does not help disambiguation.
      IMPACT IF DELETED: Slightly cleaner integration section.
      RISK IF DELETED: Minimal — anyone confused about /o vs /list can read both skills.

KEEP DESPITE TEMPTATION:

[I32] KEEP: Phase 4 (Order and Label) as a separate phase — WHY: It is tempting to merge ordering into Generation (Phase 3). But ordering requires all items to exist first. The separation enforces the correct sequence: generate broadly, then order deliberately. Merging them would invite ordering-while-generating, which biases against late-discovered items.

[I33] KEEP: The 5 generation strategies — WHY: It is tempting to prune to 3 (brainstorm, categorical sweep, negative space). But stakeholder sweep and temporal sweep catch genuinely different items. The table is not too long. Keep all 5, but add selection guidance (see I24).
```

### Step 8: What Needs Least Iteration?

```
FINISHED (do not touch):

[I34] Core Principles 2-5 — STATUS: done — EVIDENCE: Clear, non-obvious, correctly stated, and procedurally enforced downstream.

[I35] Phase 3 Generation template — STATUS: done — EVIDENCE: The candidate evaluation format is clean and functional. PASSES_INCLUSION and GRANULARITY_MATCH are the right checks.

[I36] Failure modes table — STATUS: done — EVIDENCE: 8 modes, all real, all with accurate signals and actionable fixes. Comprehensive for the skill's scope.

[I37] Phase 5 Coverage Check — STATUS: done — EVIDENCE: Subcategory enumeration with REPRESENTED/MISSING/VERDICT is a strong analytical contribution. The gap patterns table is useful and accurate.

[I38] Pre-Completion Checklist — STATUS: done — EVIDENCE: 9 items, all corresponding to actual phases. No gaps, no redundancy.
```

---

## Phase 3: FINDING REGISTRY

```
FINDING REGISTRY
================

SUBJECT:
/list skill (SKILL.md) -- STATE: Operational, 209 lines, 6 phases, solid but with specific gaps

DIMENSIONS ASSESSED:
[I1] IDEAS -- NEED: medium -- EVIDENCE: Principle 1 assumes all lists are classification lists
[I2] ANALYSIS -- NEED: low -- EVIDENCE: Coverage check and failure modes are strong
[I3] EXPRESSION -- NEED: low -- EVIDENCE: Clear, direct language throughout
[I4] STRUCTURE -- NEED: medium -- EVIDENCE: Phases 1-2 mergeable; assumptions appear in output without generation step
[I5] SCOPE -- NEED: medium -- EVIDENCE: No handling of existing lists; depth scaling is purely quantitative
[I6] COMPLETENESS -- NEED: high -- EVIDENCE: Missing list types, assumption generation, overlap procedure, generation strategy guidance
[I7] CORRECTNESS -- NEED: low -- EVIDENCE: No outright errors; minor phrasing inconsistency in integration
[I8] INTEGRATION -- NEED: medium -- EVIDENCE: Missing routes to /iterate, /evaluate, /claim, /aso
[I9] META -- NEED: low -- EVIDENCE: Fundamental approach is sound

LEVEL:
[I10] paragraph (with some section-level) -- EVIDENCE: Core structure holds; gaps are at paragraph and section level
[I11] Evidence: specific missing paragraphs and sections identified
[I12] Risk: word-level misses conceptual gaps; file-level loses strong existing structure

TYPE:
[I13] extend (primary) + refine (secondary) -- EVIDENCE: Core is right but incomplete
[I14] Adding missing pieces, refining existing ones

SCALE:
[I15] moderate revision -- [I16] 5-8 changes, none requiring major section rewrites -- [I17] 8 items

HIGH PRIORITY:
[I18] Principle 1 framing too narrow -- DIM: IDEAS -- LEVEL: paragraph -- TYPE: refine -- EFFORT: small
[I19] No existing-list entry path -- DIM: COMPLETENESS -- LEVEL: section -- TYPE: extend -- EFFORT: medium
[I20] Assumptions in output but never generated -- DIM: CORRECTNESS -- LEVEL: paragraph -- TYPE: extend -- EFFORT: small
[I21] Overlap rule defined but never procedurally applied -- DIM: COMPLETENESS -- LEVEL: paragraph -- TYPE: extend -- EFFORT: small

MEDIUM PRIORITY:
[I22] Depth scaling purely quantitative -- DIM: IDEAS -- LEVEL: paragraph -- TYPE: refine -- EFFORT: medium
[I23] Integration section missing key routes -- DIM: INTEGRATION -- LEVEL: paragraph -- TYPE: extend -- EFFORT: small
[I24] Generation strategies have no selection guidance -- DIM: COMPLETENESS -- LEVEL: paragraph -- TYPE: extend -- EFFORT: small

LOW PRIORITY:
[I25] Phases 1-2 could merge -- DIM: STRUCTURE -- LEVEL: section -- TYPE: restructure -- EFFORT: medium
[I26] No guidance for vague domains -- DIM: COMPLETENESS -- LEVEL: paragraph -- TYPE: extend -- EFFORT: small

DO NOT ITERATE:
[I27] Core Principles 2-5 -- REASON: Strong, non-obvious, correctly enforced
[I28] Phase 3 template format -- REASON: Clean and functional
[I29] Failure modes table -- REASON: Comprehensive and accurate

DELETION CANDIDATES:
[I30] "non-negotiable" in Principle 2 -- REASON: unnecessary intensifier -- IMPACT: cleaner prose -- RISK: none
[I31] "Differs from /o" line -- REASON: obvious distinction -- IMPACT: cleaner integration -- RISK: minimal

KEEP DESPITE TEMPTATION:
[I32] Phase 4 as separate phase -- REASON: enforces generate-then-order sequence
[I33] All 5 generation strategies -- REASON: each catches genuinely different items

FINISHED:
[I34] Core Principles 2-5 -- EVIDENCE: clear, non-obvious, enforced
[I35] Phase 3 Generation template -- EVIDENCE: clean format
[I36] Failure modes table -- EVIDENCE: 8 real modes, all actionable
[I37] Phase 5 Coverage Check -- EVIDENCE: strong analytical contribution
[I38] Pre-Completion Checklist -- EVIDENCE: 9 items, no gaps

TOTALS:
- Dimensions with high need: 1 (COMPLETENESS)
- Iteration targets: 9 (4 high, 3 medium, 2 low)
- Deletion candidates: 2
- Finished items: 5
```

---

## Phase 4: EXECUTE

This is an analysis-mode iteration — the user asked to "identify what needs iteration" rather than to perform the iterations. The identification IS the execution. However, I will demonstrate what the highest-priority iterations would look like concretely.

### Step 9: Execute Highest-Priority Iterations (Demonstrated)

```
ITERATING: [I18] Principle 1 — list-as-category-membership framing too narrow
DIMENSION: IDEAS
LEVEL: paragraph
TYPE: refine

BEFORE: "Lists are claims about category membership. Every list implicitly asserts: 'these items belong together and nothing important is missing.'"

CHANGE: Broaden to cover multiple list types while preserving the core insight that lists make implicit claims.

AFTER: "Lists make implicit claims. A classification list claims 'these items belong together and nothing important is missing.' A task list claims 'these are the right things to do, in the right order, at the right granularity.' A dependency list claims 'these relationships are correct and complete.' Identify which claim your list is making — the inclusion rules, ordering logic, and coverage checks all depend on the list type."

STATUS: Demonstrated, not applied to file.
```

```
ITERATING: [I20] Assumptions in output but never generated
DIMENSION: CORRECTNESS
LEVEL: paragraph
TYPE: extend

BEFORE: Phase 6 Output template includes "ASSUMPTIONS: - [any assumptions made during generation]" but no prior phase asks for assumptions.

CHANGE: Add an assumption-tracking instruction to Phase 3 (Generation) and Phase 5 (Coverage Check).

AFTER: Add to Phase 3: "[L-N] ASSUMPTION: [any assumption made during generation — e.g., assumed domain boundary, assumed audience knowledge level, assumed time horizon]"
Add to Phase 5: "Flag any assumptions that affected coverage decisions."

STATUS: Demonstrated, not applied to file.
```

```
ITERATING: [I21] Overlap rule defined but never procedurally applied
DIMENSION: COMPLETENESS
LEVEL: paragraph
TYPE: extend

BEFORE: L9 says "OVERLAP_RULE: [how to handle items that partially overlap]" but no step says "now check for overlaps."

CHANGE: Add an overlap check step between Phase 3 (Generation) and Phase 4 (Order & Label), or as a sub-step at the end of Phase 3.

AFTER: Add to end of Phase 3: "### Overlap Scan — For each pair of included items, check: do these overlap significantly? If yes, apply the OVERLAP_RULE from L9. Record: [L-N] OVERLAP_CHECK: [item A] vs [item B] — OVERLAP: [none/partial/significant] — ACTION: [keep both/merge/split]"

STATUS: Demonstrated, not applied to file.
```

```
ITERATING: [I19] No existing-list entry path
DIMENSION: COMPLETENESS
LEVEL: section
TYPE: extend

BEFORE: Skill only handles "build a list from scratch." No entry point for "improve this existing list."

CHANGE: Add an "Existing List" fast-path after Phase 1 that evaluates an existing list against the skill's own criteria and identifies what needs fixing.

AFTER: Add between Phase 1 and Phase 2: "### Existing List Path — If the user provides an existing list, evaluate it against all criteria before rebuilding: (a) Are inclusion rules implicit or explicit? Extract them. (b) Is granularity consistent? Flag violations. (c) Is ordering justified? (d) Has coverage been checked? (e) Rate overall: [needs minor fixes / needs moderate revision / needs rebuild]. If minor fixes: apply fixes directly without full procedure. If moderate: run Phase 2-5 using existing items as candidates. If rebuild: run full procedure."

STATUS: Demonstrated, not applied to file.
```

### Step 10: Execute Deletions

```
DELETING: [I30] "non-negotiable" in Principle 2
REASON: Unnecessary intensifier
VERIFICATION: Principle is enforced by failure mode "Generated then filtered" — the word adds nothing
DONE: Demonstrated, not applied to file.

DELETING: [I31] "Differs from /o" in Integration
REASON: Obvious distinction that does not aid disambiguation
VERIFICATION: /o and /list have clearly different names, descriptions, and use cases
DONE: Demonstrated, not applied to file.
```

### Step 11: Verify

```
ITERATION VERIFICATION:
- High priority items addressed: 4 of 4 (demonstrated)
- Deletions executed: 2 of 2 (demonstrated)
- Did any iteration introduce new problems? No — all changes are additive or surgical. No existing content was disrupted.
- Is another round of /iterate needed? Not immediately. After applying the high-priority changes, the medium-priority items (I22, I23, I24) should be addressed in a second pass. But the skill would be significantly improved with just the high-priority items.
```

---

## Phase 5: SYNTHESIS

```
SUBJECT: /list skill (SKILL.md)

ITERATION SUMMARY:
- Dimensions iterated: IDEAS, COMPLETENESS, CORRECTNESS, INTEGRATION
- Level: paragraph (with one section-level addition)
- Type: extend (primary) + refine (secondary)
- Scale: moderate revision
- Changes demonstrated: 4 high-priority iterations
- Deletions demonstrated: 2
- Items left alone: 5 (explicitly marked finished)

HIGHEST-VALUE ITERATION:
[I19] Adding an existing-list entry path. This addresses the most common real-world use case the skill currently misses. Most users arrive with a list that needs improving, not an empty page. Without this path, the skill forces a full rebuild when a targeted fix would be faster and better. This single change probably doubles the skill's practical utility.

WHAT'S NOW DONE (after applying demonstrated changes):
- Principle 1 framing (broadened to multiple list types)
- Assumption pipeline (generation step feeds output template)
- Overlap application (rule is now procedurally triggered)
- Existing-list handling (users with draft lists have an entry point)

WHAT STILL NEEDS ITERATION:
- [I22] Depth scaling (add qualitative dimensions) — medium priority
- [I23] Integration routes (add /iterate, /evaluate, /claim, /aso) — medium priority, small effort
- [I24] Generation strategy selection guidance — medium priority, small effort
- [I25] Phase 1-2 merge — low priority
- [I26] Vague domain handling — low priority

DIMINISHING RETURNS CHECK:
After the 4 high-priority changes, the skill goes from "good with gaps" to "strong." The medium-priority items would take it from "strong" to "polished." The low-priority items produce marginal improvement. One more round targeting I22-I24 is warranted. Beyond that, returns diminish sharply.

READY FOR:
- /iterate [/list skill] — for a second round targeting medium-priority items (I22-I24)
- /evaluate [/list skill] — to assess the iterated version against quality criteria
- /claim "The /list skill's existing-list path should be the default entry point" — to test whether the extension should be primary rather than secondary
- /certainty "What is the right depth scaling model for list-building?" — if the depth scaling question (I22) deserves deep resolution
```

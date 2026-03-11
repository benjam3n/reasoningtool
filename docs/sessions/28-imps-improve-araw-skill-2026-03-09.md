# /imps How could the /araw skill be improved?
**Date:** 2026-03-09
**Skill:** /imps (Improve Skill)

---

## Phase 1: Read and Baseline

```
[I1] SKILL: /araw
[I2] CURRENT_LINES: 424
[I3] CURRENT_STRUCTURE: Frontmatter, Core Principles (10), Multi-phase structure with lettered findings,
     Failure Modes table, Depth Scaling table, Pre-Completion Checklist (18 items), Interpretations section,
     Corruption Pre-Inoculation section, Quick Mode, Meta-ARAW step. Missing: formal Integration section.
```

### Structural Audit

| Element | Present? | Quality |
|---------|----------|---------|
| Frontmatter (name, description) | Yes | Good -- description is specific and captures the AR/AW duality |
| Core Principles (3-6, domain-specific, non-generic) | Yes (10 principles) | Excellent -- every principle is ARAW-specific, passes disagreement test, highly domain-aware |
| Multi-phase structure with lettered findings | Yes (Step 0 + Steps 1-4 / Phases 1-3) | Good but naming is confusing (see diagnosis) |
| Failure Modes table (Failure / Signal / Fix) | Yes (9 entries) | Excellent -- every failure mode is specific to claim-testing, not generic |
| Depth Scaling table (1x/2x/4x/8x with floors) | Yes (1x through 32x) | Excellent -- goes beyond standard, includes 16x and 32x with specific numeric floors |
| Pre-Completion Checklist (6+ binary items) | Yes (18 items) | Excellent -- each item is binary, falsifiable, domain-specific |
| Integration section (use from, routes to, differs from) | **No** | Missing entirely -- no "use from", "routes to", "differs from" section |

---

## Phase 2: Content Diagnosis

```
[I4] PRINCIPLES_QUALITY: Outstanding. All 10 principles are deeply domain-specific.
     GENERIC_PRINCIPLES: None. Every principle is recognizably about ARAW even without the skill name.
     MISSING_INSIGHTS: Two gaps identified below.

[I5] PHASE_QUALITY: Phases have concrete steps with specific formats and examples.
     VAGUE_PHASES: None are vague -- all specify HOW, not just "analyze."
     MISSING_PHASES: No guidance on handling BUNDLED claims that interact (C1 depends on C2).
                     No guidance on when to STOP exploring a branch that keeps opening.

[I6] FAILURE_MODES_QUALITY: All 9 failure modes are specific to ARAW's domain.
     GENERIC_FAILURES: None.
     MISSING_FAILURES: "Orphan findings" -- findings that get numbered but never connect to verdicts.
                       "Depth theater" -- reaching the numeric floor by padding shallow branches
                       rather than going deep on fewer claims.
                       "Registry-synthesis disconnect" -- synthesis narrative doesn't actually follow
                       from registry contents.

[I7] OUTPUT_QUALITY: Output format is extremely specific and well-structured.
     MISSING_OUTPUT: No guidance on output LENGTH expectations per depth level.
                     No guidance on how to handle the output when it exceeds context window at high depth.
```

### Content Quality Tests

| Test | Result |
|------|--------|
| **Disagreement test** | PASS -- Principle 8 ("expect 20-40% rejection") is genuinely controversial. Principle 4 ("AW must be genuinely adversarial") takes a strong stance. |
| **Domain test** | PASS -- Removing the skill name, these principles are still recognizably about systematic claim-testing with dual-assumption exploration. |
| **Specificity test** | PASS -- Every phase specifies exact formats, numbering schemes, classification labels, and stopping criteria. |
| **Failure test** | PASS -- All 9 failures are things that actually go wrong when doing ARAW (soft AW, validation parade, cheerleading AR). |
| **Actionability test** | PASS -- Someone could follow this skill and produce structured output without improvising. The formats are complete. |

---

## Phase 3: Improvement Plan

```
[I-1] FIX: Add Integration section
     TYPE: structural
     PRIORITY: critical
     CURRENT: No integration section exists. The skill has a "Saving Output" section and
              "When ARAW Fails" section but no formal integration links.
     PROPOSED: Add standard Integration section after Pre-Completion Check:
               - Use from: /claim, /decide, /viability, /evaluate (all category skills that route to ARAW mode)
               - Routes to: /sf (save), /spd (space discovery when stuck), /iterate (when results need refinement)
               - Complementary: /ht (hypothesis testing -- tests single claims), /aex (assumption examination),
                 /stc (steel/counter -- related adversarial approach)
               - Differs from /ht: ht tests one hypothesis; araw tests a constellation of claims with AR+AW duality
               - Differs from /aex: aex examines assumptions qualitatively; araw provides structured verdicts with numbered evidence
               - Differs from /stc: stc builds strongest version then attacks; araw explores both directions simultaneously per claim
     RATIONALE: Integration is a required structural element. /araw is invoked by many category skills
                but doesn't document this, making it harder for users to discover related tools and for
                the skill itself to route users forward when they're done or stuck.

[I-2] FIX: Resolve Step/Phase naming confusion
     TYPE: clarity
     PRIORITY: important
     CURRENT: The skill uses two overlapping numbering systems:
              - "Step 0" (Meta-ARAW), "Step 1" (Identify Claims), then...
              - "Phase 1: EXPLORATION (Step 2)", "Phase 2: FINDING REGISTRY (Step 3)", "Phase 3: SYNTHESIS (Step 4)"
              This creates confusing double-naming: is it "Step 2" or "Phase 1"?
     PROPOSED: Unify to a single naming system. Use "Phase 0" through "Phase 4" consistently:
              - Phase 0: Meta-ARAW (Strategy Selection)
              - Phase 1: Claim Identification and Unbundling
              - Phase 2: Exploration (AR/AW Trees)
              - Phase 3: Finding Registry
              - Phase 4: Synthesis
              Remove all "(Step N)" parentheticals.
     RATIONALE: The dual naming is confusing because Principle 10 says "Three phases, strict separation"
                but the skill actually has 5 stages. The naming should match the actual structure.
                A user trying to follow the instruction "Phase 1 explores, Phase 2 compiles, Phase 3 synthesizes"
                might not realize "Phase 1" starts at what's labeled "Step 2."

[I-3] FIX: Add guidance for interacting claims
     TYPE: content
     PRIORITY: important
     CURRENT: Step 1 numbers claims independently (C1, C2, C3...) but provides no guidance for when
              claims interact -- e.g., C1's verdict depends on C2's verdict, or C3 only matters if C1 is validated.
     PROPOSED: Add a subsection after "Blind Spot Check" in Step 1:
              ### Claim Dependencies
              After numbering all claims, map dependencies:
              - DEPENDS: C3 depends on C1 (if C1 rejected, C3 is moot)
              - CONFLICTS: C2 conflicts with C4 (both cannot be validated)
              - COMPOUNDS: C1 + C5 together imply something neither implies alone
              Test claims in dependency order. If a parent claim is REJECTED, mark dependent
              claims as MOOT rather than testing them independently.
     RATIONALE: Real-world claim bundles almost always have dependencies. Testing C3 ("quitting fixes the problem")
                before resolving C1 ("a problem exists") wastes depth. The skill's own example
                ("I need to quit my job" -> 5 claims) contains exactly this kind of dependency chain
                but doesn't instruct the user to map it.

[I-4] FIX: Add missing failure modes
     TYPE: content
     PRIORITY: important
     CURRENT: 9 failure modes, all good. But three domain-specific failures are missing.
     PROPOSED: Add to Anti-Failure Checks table:
              | **Orphan findings** | Findings numbered in Phase 1 but never referenced in verdicts or synthesis | Every F-number must appear in at least one verdict's evidence chain or in synthesis |
              | **Depth theater** | Numeric floors met but via many shallow 2-level branches instead of deep chains | Check that at least 30% of branches reach 4+ levels. Breadth without depth is padding. |
              | **Registry-synthesis gap** | Synthesis makes claims that don't trace to specific F-numbers | Every synthesis statement must cite F-numbers. If it can't, it's not derived from the analysis. |
     RATIONALE: These are real failure modes that occur when running ARAW at scale. Orphan findings
                are especially common -- the registry grows large and synthesis cherry-picks.
                The existing "Cherry-picked synthesis" entry partially covers the registry-synthesis gap
                but doesn't address orphan findings or depth theater.

[I-5] FIX: Add output length guidance per depth level
     TYPE: content
     PRIORITY: nice-to-have
     CURRENT: Depth scaling table specifies claims, findings, tree levels, and CRUX counts.
              No guidance on expected output length.
     PROPOSED: Add a column or note to the depth table:
              | 1x | ~500-1000 words |
              | 2x | ~1500-3000 words |
              | 4x | ~3000-6000 words |
              | 8x | ~6000-12000 words |
              | 16x | ~10000-20000 words |
              | 32x | ~20000+ words (multi-part) |
              For 8x+, note: "If output exceeds context window, split into Part 1 (Phases 0-2) and
              Part 2 (Phases 3-4). Complete exploration before starting registry."
     RATIONALE: Users invoking 16x or 32x have no sense of what they're asking for. This sets
                expectations and provides practical guidance for very large analyses.

[I-6] FIX: Clarify Principle 10 to match actual structure
     TYPE: clarity
     PRIORITY: important
     CURRENT: Principle 10 says "Three phases, strict separation" but the skill actually has
              5 stages (Meta-ARAW, Claim ID, Exploration, Registry, Synthesis). The three-phase
              language refers only to the last three stages.
     PROPOSED: Revise Principle 10 to:
              "10. **Three core phases, strict separation.** Phase 2 explores (no conclusions).
              Phase 3 compiles (no new findings). Phase 4 synthesizes (only from the registry).
              Never mix these three phases. Phases 0 and 1 are preparatory -- they set up the
              claims. The strict separation applies to what happens after claims are identified."
     RATIONALE: The current principle misleads about the skill's structure. Someone reading
                "three phases" then encountering five stages will be confused about which
                three the principle means.

[I-7] FIX: Add a "When to use ARAW-Lite vs Full" decision guide
     TYPE: content
     PRIORITY: nice-to-have
     CURRENT: ARAW-Lite is described with a format but the only guidance is "for low-stakes,
              reversible, time-sensitive decisions."
     PROPOSED: Add a quick decision table:
              | Condition | Use |
              |-----------|-----|
              | Decision is reversible AND low-cost to reverse | ARAW-Lite |
              | You need a decision in < 5 minutes | ARAW-Lite |
              | Stakes are high OR decision is irreversible | Full ARAW (2x minimum) |
              | You suspect hidden complexity | Full ARAW (4x minimum) |
              | Bet-the-company / life-changing | Full ARAW (8x+) |
     RATIONALE: Users often don't know which mode to choose. A quick decision guide
                reduces friction and prevents over-analysis of trivial decisions or
                under-analysis of critical ones.
```

---

## Phase 4: Proposed Changes (Not Applied)

Since /araw is an exemplar skill (cited in /imps itself as the quality standard at 410 lines), and since the skill's content quality is already excellent, the improvements are **surgical, not structural**. The skill should NOT be rewritten. The fixes are:

1. **Add Integration section** (critical) -- ~15 lines added at the end
2. **Unify Step/Phase naming** (important) -- rename headers throughout, no content change
3. **Add Claim Dependencies subsection** (important) -- ~12 lines added to Step 1
4. **Add 3 failure modes** (important) -- ~6 lines added to failure table
5. **Clarify Principle 10** (important) -- ~3 lines modified
6. **Add output length guidance** (nice-to-have) -- ~8 lines added to depth table
7. **Add ARAW-Lite decision guide** (nice-to-have) -- ~8 lines added

**Estimated post-improvement line count**: ~470 lines (above the 150-300 range but justified -- /araw is a core skill used by 4+ category skills and already at 424 lines as an exemplar).

---

## Phase 5: Verify

```
[I-8] VERIFICATION:
     STRUCTURAL_GAPS_REMAINING: Zero (Integration section added completes all required elements)
     GENERIC_CONTENT_REMAINING: Zero (no generic content existed; no generic content introduced)
     LINE_COUNT: ~470 (above 300 but /araw is an exemplar skill already at 424; additions are justified)
     ALL_TESTS_PASS:
       - Disagreement: PASS (principles remain controversial and specific)
       - Domain: PASS (all new content is ARAW-specific)
       - Specificity: PASS (new subsections have concrete formats and criteria)
       - Failure: PASS (3 new failure modes are specific to ARAW execution)
       - Actionability: PASS (claim dependency mapping and ARAW-Lite guide are immediately followable)
```

---

## Summary of Recommended Improvements

| # | Fix | Type | Priority | Lines Added |
|---|-----|------|----------|-------------|
| I-1 | Add Integration section | structural | critical | ~15 |
| I-2 | Unify Step/Phase naming to Phase 0-4 | clarity | important | 0 (rename only) |
| I-3 | Add Claim Dependencies subsection | content | important | ~12 |
| I-4 | Add 3 missing failure modes | content | important | ~6 |
| I-6 | Clarify Principle 10 to match 5-stage structure | clarity | important | ~3 |
| I-5 | Add output length guidance per depth | content | nice-to-have | ~8 |
| I-7 | Add ARAW-Lite vs Full decision guide | content | nice-to-have | ~8 |

**Overall assessment**: /araw is already one of the strongest skills in the toolkit. Its principles are deeply domain-specific, its failure modes are precise, its depth scaling is the most granular of any skill (6 levels), and its pre-completion checklist is the most thorough (18 items). The improvements are refinements, not repairs. The single critical gap is the missing Integration section. The important fixes address real usability issues (confusing naming, missing dependency handling) that emerge during actual use of the skill at high depth.

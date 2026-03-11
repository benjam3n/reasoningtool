# /aiag Which parts of skill creation, testing, and maintenance could be automated with AI agents?
**Date:** 2026-03-09
**Skill:** /aiag (AI Agent Analysis)

---

## Step 1: Identify the Work

```
DOMAIN: Reasoning toolkit skill lifecycle management
GOAL: Automate repetitive, structured parts of skill creation, testing, and maintenance for a solo developer managing 592 skills

TASKS:
 1. Skill ideation (identifying gaps, generating concepts) — frequency: weekly, complexity: high
 2. Overlap checking (does this skill duplicate an existing one?) — frequency: per new skill, complexity: medium
 3. Writing SKILL.md (drafting the procedure) — frequency: per new skill, complexity: high
 4. Testing skills (running input through a skill, evaluating output quality) — frequency: per new/changed skill, complexity: medium
 5. Integration into routers (updating category skills to route to new skill) — frequency: per new skill, complexity: low
 6. Updating the website (skill metadata, descriptions, tags, tier) — frequency: per new skill, complexity: low
 7. Quality audits (reviewing existing skills for clarity, completeness, consistency) — frequency: periodic, complexity: medium
 8. Fixing broken chains (detecting and repairing INVOKE references to renamed/removed skills) — frequency: periodic, complexity: low
 9. Updating cross-references (keeping "Use with" and integration sections current) — frequency: periodic, complexity: medium
10. Skill deduplication (finding and merging overlapping skills) — frequency: periodic, complexity: high
11. Consistency enforcement (format, naming, section structure) — frequency: continuous, complexity: low
12. Changelog/documentation (tracking what changed and why) — frequency: per change, complexity: low
```

---

## Step 2: Assess Automatability

```
HIGHLY AUTOMATABLE:
- Overlap checking — why: structured comparison of skill names, descriptions, and procedures against existing 592 skills; pattern-matchable via embedding similarity; clear inputs (new skill concept) and outputs (similarity scores + candidates)
- Fixing broken chains — why: purely mechanical; scan all SKILL.md files for INVOKE references, check if target exists, report or auto-fix
- Consistency enforcement — why: lintable; check for required sections, naming conventions, formatting rules across all files
- Updating the website — why: structured data extraction from SKILL.md into website metadata; deterministic mapping
- Changelog/documentation — why: git diffs provide structured input; summarization is well within current AI capability
- Integration into routers — why: adding a line to a routing table in the correct category is low-judgment, pattern-following work

PARTIALLY AUTOMATABLE:
- Writing SKILL.md — AI does: generate first draft from a concept description, following the established format and referencing similar skills for style; human does: review for intellectual quality, ensure the procedure actually produces good thinking, refine the judgment calls
- Testing skills — AI does: generate diverse test inputs, run them through the skill, flag outputs that seem thin/circular/off-template; human does: evaluate whether the thinking output is genuinely useful (quality judgment)
- Quality audits — AI does: scan for structural issues (missing sections, vague instructions, dead references, inconsistent voice), rank skills by likely quality issues; human does: decide what "good enough" means, prioritize fixes
- Updating cross-references — AI does: analyze skill relationships via semantic similarity, suggest "Use with" links; human does: confirm that suggested links are genuinely useful rather than just topically related
- Skill deduplication — AI does: cluster similar skills, surface candidates for merging, draft merged versions; human does: decide which skills to keep vs. merge, ensure merged skill preserves the best of both

NOT AUTOMATABLE (yet):
- Skill ideation (the good kind) — why: identifying genuinely missing thinking patterns requires understanding what real users struggle with; an agent can suggest gaps mechanically (e.g., "you have no skill for X category") but cannot judge whether a gap matters
- Evaluating whether a skill actually improves thinking — why: this is the core quality question; requires human judgment about whether a procedure genuinely helps someone think better vs. just producing structured-looking output
```

---

## Step 3: Evaluate Reliability Requirements

```
ERROR TOLERANCE BY TASK:
- Overlap checking: HIGH tolerance — false positives (flagging non-overlaps) waste a few minutes; false negatives (missing overlaps) just mean a duplicate gets created, fixable later
- Fixing broken chains: LOW tolerance — incorrect "fixes" could point skills at wrong targets, silently corrupting chains
- Consistency enforcement: HIGH tolerance — worst case is a false lint warning
- Website updates: MEDIUM tolerance — wrong metadata is visible to users but easily corrected
- Writing SKILL.md drafts: HIGH tolerance — drafts are always reviewed; bad drafts just waste review time
- Testing skills: MEDIUM tolerance — missing a quality issue means a bad skill ships, but if testing is currently not happening at all, even imperfect automated testing is a net improvement
- Quality audits: HIGH tolerance — this is advisory; false flags just waste attention
- Router integration: LOW tolerance — wrong routing breaks the user experience silently
- Cross-reference updates: MEDIUM tolerance — bad suggestions waste review time but don't break anything

FAILURE CONSEQUENCES:
- If AI gets overlap checking wrong: duplicate skill gets created (minor, fixable)
- If AI gets broken chain fixing wrong: skill chains silently route to wrong procedure (moderate — user gets wrong analysis)
- If AI gets SKILL.md drafting wrong: solo dev spends time fixing a bad draft instead of writing from scratch (minor time cost)
- If AI gets router integration wrong: users get routed to wrong skill for their problem (significant — erodes trust)
- Worst case scenario: automated quality audit gives clean bill of health to broken skills, creating false confidence; or automated router updates silently misroute common queries for weeks before detection
- Recovery cost: low for most tasks (git revert), medium for router corruption if not caught quickly
```

---

## Step 4: Design Human Oversight

```
OVERSIGHT MODEL:
- Overlap checking:      No oversight (advisory output; human decides whether to proceed)
- Broken chain fixing:   Review before action (show proposed fixes, apply on approval)
- Consistency enforcement: No oversight (lint-style warnings, no auto-fix)
- Website updates:       Spot-check (auto-apply, review batch periodically)
- SKILL.md drafting:     Human-in-the-loop (AI drafts, human rewrites/approves)
- Testing:               Spot-check (AI runs tests, flags issues, human reviews flagged items)
- Quality audits:        No oversight (advisory report; human prioritizes)
- Router integration:    Review before action (AI proposes routing, human confirms placement)
- Cross-reference updates: Review before action (AI suggests links, human confirms)

ESCALATION TRIGGERS:
- AI should escalate when: overlap score is ambiguous (40-70% similarity — clearly overlapping or clearly distinct needs no escalation)
- AI should escalate when: a broken chain fix requires choosing between multiple plausible targets
- AI should escalate when: a quality audit finds a skill that may need to be deprecated rather than fixed
- AI should escalate when: a SKILL.md draft requires judgment about what "good thinking" looks like in a novel domain
- AI should stop when: it would delete or merge skills without explicit approval

FEEDBACK LOOP:
- How humans correct AI: accept/reject/modify proposed changes in a review queue; corrections are logged
- How AI improves from corrections: rejected suggestions become negative examples in future prompts; patterns of human edits to SKILL.md drafts become style guidance for future drafts
```

---

## Step 5: Plan for Failure Modes

```
FAILURE MODES:
1. Skill homogenization — likelihood: HIGH
   AI drafts converge on similar structures and phrasing, making skills
   feel interchangeable. The toolkit's value comes from genuine variety
   in approach, not just topic.
   Mitigation: diversity scoring across recent AI-drafted skills; reject
   drafts that are too similar in structure to the last N skills created.

2. Plausible-but-useless procedures — likelihood: HIGH
   AI generates steps that sound like good thinking procedures but don't
   actually change how someone thinks. "Consider multiple perspectives"
   looks right but does nothing.
   Mitigation: mandatory "stress test" — run every AI-drafted skill
   against a hard input where generic advice fails. If the skill's
   output doesn't differ meaningfully from a plain prompt, reject it.

3. Reference drift — likelihood: MEDIUM
   AI updates cross-references based on semantic similarity but not
   actual procedural complementarity. Skills get linked because they
   sound related, not because they work well in sequence.
   Mitigation: cross-references must include a one-line rationale
   ("use /X after this skill because it handles [specific gap]").
   Audit rationales periodically.

4. Audit fatigue / false confidence — likelihood: MEDIUM
   Human starts rubber-stamping AI quality audits because they're
   "usually right." Quality slips through.
   Mitigation: inject known-bad skills into audit batches as canaries.
   If human approves a canary, the oversight process needs recalibration.

5. Scope creep via easy generation — likelihood: HIGH
   Because AI makes it easy to create skills, the toolkit grows past
   the point where any human can maintain quality awareness. Already
   a risk at 592.
   Mitigation: hard cap on skill count, or require a skill to be
   removed/merged before a new one is added. AI can propose merges.

GRACEFUL DEGRADATION:
- If AI is unavailable: all tasks revert to manual. The solo developer
  did this for the first 400+ skills. It's slower but fully functional.
- If AI quality drops: detection via periodic "known-good input" tests
  (run 10 benchmark skills, compare output quality to baseline). Response:
  revert to manual for SKILL.md writing, keep AI for mechanical tasks only.
```

---

## Step 6: Capability Projection

```
CURRENT STATE:
- AI can reliably do today: broken chain detection, website sync, overlap
  flagging via embeddings, formatting audits, cross-reference graph analysis.
  These are all implementable with existing tools.
- AI can partially do: SKILL.md drafting (good structure, mediocre procedure
  design), testing (can detect obviously generic output, can't judge thinking
  quality), gap analysis (good at mapping, weak at prioritizing).

6-MONTH PROJECTION:
- SKILL.md drafting improves significantly if fed the corpus of (draft ->
  human revision) pairs. With 50+ examples, drafts should need less rewriting.
- Testing becomes more useful with better self-evaluation: AI can compare its
  own output-with-skill vs output-without-skill and measure the delta. If the
  delta is small, the skill isn't adding value.
- Agentic workflows become practical: an agent that creates a skill, tests it
  against 10 inputs, checks for overlap, integrates into routers, and submits
  a PR for human review. End-to-end with one approval gate.

LONG-TERM OUTLOOK:
- If AI can genuinely evaluate "did this procedure improve my thinking," the
  full pipeline becomes automatable with spot-check oversight. This requires AI
  that can model its own cognitive process, which is an open research problem.
- The more likely path: AI handles 80% of the pipeline, human focuses on the
  20% that requires judgment about thinking quality. This is a good division
  of labor for a solo developer.

RECOMMENDED APPROACH:
1. Start with: mechanical automation (broken chains, website sync,
   cross-reference updates, overlap checking). These are high-value,
   zero-risk, and implementable in a weekend. Build as a CLI tool
   or CI pipeline.
2. Expand to: AI-assisted SKILL.md drafting with human revision loop.
   Create a /newskill command that generates a draft, runs it against
   test inputs, checks overlap, and presents the package for editing.
   Collect revision data from the start.
3. Monitor: (a) skill quality variance over time, (b) time-per-skill
   creation, (c) overlap rate in new skills, (d) broken chain count
   per month. If quality variance increases after introducing AI
   drafting, tighten the human review gate.
```

---

## Summary

The skill pipeline splits cleanly into three tiers:

**Automate now** (mechanical, low-risk): broken chain detection, website sync, overlap checking, consistency linting, router integration, cross-reference maintenance. These save the most time per unit of effort to build and carry near-zero risk.

**Automate with human-in-the-loop** (judgment-adjacent): SKILL.md drafting, quality audits, testing against sample inputs, skill deduplication. AI does the heavy lifting; human makes the quality call.

**Keep human** (core judgment): ideation from real thinking failures, evaluating whether a procedure actually improves thinking, deciding what the toolkit should and shouldn't contain.

The biggest risk is not under-automation but over-automation: AI makes it easy to create skills, which accelerates the existing problem of having more skills than one person can quality-control. The automation strategy should include a **growth governor** -- making it easy to create skills is only valuable if it's equally easy to audit, merge, and retire them.

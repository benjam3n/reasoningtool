# /dcm Break down "make reasoningtool's skills consistently high quality" into solvable sub-problems
**Date:** 2026-03-09
**Skill:** /dcm (Decomposition)

---

## Interpretation

**Interpretation 1 — Project breakdown** is the best fit. You have a large goal (592 skills, consistent quality) and need it broken into manageable, assignable pieces with clear dependencies. This is a solo-developer project plan problem.

---

## Step 1: Assess Decomposition Need

The goal is too big to tackle at once for several reasons:

- **Scale**: 592 skills. Even spending 5 minutes each = ~50 hours of review work. Brute force is not viable solo.
- **Distinct components**: "Quality" is not one thing — it includes structure, content accuracy, actionability, completeness, and consistency with other skills.
- **Undefined standard**: "High quality" has no current spec. You cannot make things consistent with a standard that does not exist yet.
- **Varying current states**: Some skills are likely excellent, some are stubs, some are mediocre. Different problems need different interventions.

Decomposition is clearly needed. A functional + temporal hybrid strategy fits best.

---

## Step 2: Decomposition Strategy

**Primary: Functional** — the goal has distinct functions (define quality, measure quality, fix quality, prevent regression).

**Secondary: Temporal** — the functional pieces have a natural ordering (you cannot fix what you have not measured, you cannot measure without a standard).

---

## Step 3: Sub-Goals

### SG1: Define what "high quality" means concretely

Establish a written quality standard for skills. Without this, everything else is arbitrary.

**Deliverable**: A quality rubric document (e.g., 5-8 criteria with pass/fail or scored levels).

Candidate criteria to consider:
- Has clear interpretation section (when applicable)
- Steps are actionable, not vague
- Covers when-to-use and when-not-to-use
- Output is well-defined
- Invocations (if any) reference real skills
- No placeholder or stub content
- Consistent formatting with the skill template
- Verification section is meaningful (not just boilerplate)

**Why this is solvable**: It is a writing task with a bounded scope. You already have intuitions about what good looks like — this just codifies them.

---

### SG2: Build automated quality assessment

Create a script or tool that can programmatically check each skill against the rubric from SG1 — at least the machine-checkable parts.

**Deliverable**: A script that reads all 592 SKILL.md files and produces a quality report (scores, flags, categories).

What can be automated:
- Structural checks (has required sections? has steps? has verification?)
- Length checks (stub detection — e.g., fewer than 10 lines of content)
- Reference validation (do invoked skills actually exist?)
- Formatting consistency (heading levels, frontmatter present)

What cannot be automated (but can be flagged for manual review):
- Whether steps are actually actionable vs. vague
- Whether the skill is conceptually sound
- Whether interpretations are genuinely distinct

**Why this is solvable**: It is a scripting task. The skill files have a known structure. You can iterate on the checks.

---

### SG3: Triage skills into quality tiers

Run the assessment from SG2 and sort all 592 skills into tiers based on the results.

**Deliverable**: A categorized list — e.g., Tier A (good), Tier B (needs minor fixes), Tier C (needs major rework), Tier D (stub/broken).

**Why this is solvable**: It is a mechanical sorting task once SG1 and SG2 are done. The output directly tells you where to spend time.

---

### SG4: Fix the worst offenders (Tier D)

Address stubs, broken references, and skills that are essentially empty. These are the lowest quality and often the easiest to fix (some may just need deletion or merging).

**Deliverable**: All Tier D skills either brought to Tier B+ or deliberately removed/merged.

**Why this is solvable**: The problems are obvious (missing content, broken links). Fixes are straightforward per skill. You can batch similar fixes.

---

### SG5: Establish and apply a skill template

Create a canonical template that all skills should follow. Then bring Tier B and C skills into conformance.

**Deliverable**: A SKILL_TEMPLATE.md and a batch of skills updated to match it.

This overlaps somewhat with SG1 (the rubric), but SG1 defines what "good" means while SG5 provides the structural scaffolding to get there.

**Why this is solvable**: Template creation is a one-time task. Applying it to individual skills is repetitive but bounded work — and can be partially automated (e.g., a script that adds missing sections with TODO markers).

---

### SG6: Improve Tier B/C skills to Tier A

The substantive quality work: making steps more actionable, improving interpretations, ensuring verification sections are real, etc. This is the manual, judgment-intensive part.

**Deliverable**: A meaningful fraction of skills brought to Tier A. (100% is not realistic short-term — target the most-used or most-important skills first.)

**Why this is solvable**: Each individual skill improvement is a small, bounded task. Prioritize by usage/importance rather than trying to do all 592.

---

### SG7: Prevent quality regression

Put systems in place so new skills and edits maintain quality going forward.

**Deliverable**: A combination of:
- A pre-commit or CI check that runs the automated assessment from SG2
- A "new skill checklist" or linting step
- The template from SG5 enforced for new additions

**Why this is solvable**: It is a tooling/process task. Once SG2 exists, wrapping it in CI is straightforward.

---

## Step 4: MECE Check

### Mutually Exclusive

| Pair | Overlap? | Resolution |
|---|---|---|
| SG1 (define) vs SG5 (template) | Slight — rubric defines quality, template enforces structure | Distinct: SG1 is the "what," SG5 is the "how." Keep separate. |
| SG4 (fix worst) vs SG6 (improve mid-tier) | Could blur at boundaries | Tier assignment from SG3 draws the line. SG4 = structural fixes, SG6 = substantive improvements. |
| SG2 (assess) vs SG3 (triage) | SG3 is just running SG2 | SG3 is the application of SG2. They are sequential, not overlapping. |

No significant overlaps. Acceptable.

### Collectively Exhaustive

If all seven sub-goals are achieved, do you have consistent high quality?

- Quality is defined (SG1) — yes
- Quality is measured (SG2, SG3) — yes
- Low quality is fixed (SG4, SG5, SG6) — yes
- Quality is maintained (SG7) — yes

**Gap check**: One thing missing — **prioritization within SG6**. With 592 skills, you will never manually improve all of them. You need a way to decide which skills matter most. This is implicitly part of SG3 (triage), but should be made explicit.

**Addition to SG3**: Triage should include not just quality tier but also importance/usage tier. Fix high-importance + low-quality skills first.

With that addition: collectively exhaustive. Yes.

---

## Step 5: Dependencies

```
SG1 ──→ SG2 ──→ SG3 ──→ SG4 ──→ SG6
              │         │
              │         └──→ SG5 ──→ SG6
              │
              └──────────────────→ SG7
```

| Sub-goal | Depends on | Can parallel with |
|---|---|---|
| SG1 (define quality) | Nothing | — |
| SG2 (build assessment) | SG1 | — |
| SG3 (triage) | SG2 | — |
| SG4 (fix worst) | SG3 | SG5 |
| SG5 (template) | SG1 (partially SG3) | SG4 |
| SG6 (improve mid-tier) | SG3, SG4, SG5 | — |
| SG7 (prevent regression) | SG2 | SG4, SG5, SG6 |

---

## Step 6: Critical Path

**SG1 → SG2 → SG3 → SG4/SG5 → SG6**

This is the longest chain. SG7 can be started as soon as SG2 is done (it just needs the automated checks to exist).

Estimated effort (solo developer):

| Sub-goal | Effort | Notes |
|---|---|---|
| SG1 | 2-3 hours | One writing session. Review existing good skills for patterns. |
| SG2 | 4-8 hours | Scripting. Iterative — start simple, refine. |
| SG3 | 1-2 hours | Mostly automated. Manual review of edge cases. |
| SG4 | 8-15 hours | Depends on how many Tier D skills exist. Batchable. |
| SG5 | 2-3 hours | Template creation + automation for applying it. |
| SG6 | 20-40+ hours | The long tail. Prioritize ruthlessly. |
| SG7 | 2-4 hours | CI/tooling setup. |

**Total**: ~40-75 hours. The critical insight: SG6 is the unbounded part. Everything else is tractable in a few weekends.

---

## Step 7: Further Decomposition Check

Most sub-goals are already at a workable level. The one that needs further decomposition:

### SG6 (Improve mid-tier skills) — further breakdown:

- **SG6a**: Identify the 20-30 most important skills (router skills, category skills, most-referenced skills)
- **SG6b**: Improve those 20-30 to Tier A
- **SG6c**: Work through remaining skills by category/cluster (skills that share a pattern can be improved in batches)
- **SG6d**: Accept that some skills may stay Tier B indefinitely — and that is fine

This makes SG6 tractable: you are not "improving 400 skills," you are "perfecting 30 critical skills and batch-improving the rest."

---

## Verification

- **Sub-goals are simpler than original**: Yes. Each is a bounded task with a clear deliverable.
- **Sub-goals together achieve the original goal**: Yes. Define → Measure → Fix → Maintain covers the full lifecycle.
- **Sub-goals do not overlap significantly**: Yes. Checked in Step 4.
- **Dependencies make sense**: Yes. You cannot fix without measuring, cannot measure without defining.
- **Critical path is realistic**: Yes. The fixed-cost portion (SG1-SG5, SG7) is ~20-35 hours. SG6 is the variable part, mitigated by prioritization.

---

## Summary: Your Attack Plan

1. **Define quality** — Write the rubric. One session.
2. **Build the checker** — Script that assesses all 592 skills. A weekend project.
3. **Triage** — Run the checker, sort by quality x importance. One session.
4. **Fix the floor** — Kill stubs, fix broken skills. Batch work.
5. **Set the template** — Standardize structure. Parallel with #4.
6. **Raise the ceiling** — Manually improve the top 30 skills, then batch the rest. Ongoing.
7. **Lock it in** — CI checks so new skills meet the bar. Set up early (after #2).

The key reframe: this is not "make 592 skills perfect." It is "define good, measure the gap, fix the worst, perfect the most important, and prevent backsliding." That is tractable.

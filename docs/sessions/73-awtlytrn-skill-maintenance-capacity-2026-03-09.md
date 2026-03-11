# /awtlytrn How many skills can I realistically maintain at a high quality level?
**Date:** 2026-03-09
**Skill:** /awtlytrn (What's the Limit Right Now)

---

## Phase 1: Context Assessment

```
[L1] SUBJECT: Ongoing maintenance of a skill library — keeping each skill
     accurate, well-structured, tested, and up-to-date — as a solo developer.

[L2] DIMENSION_PRIMARY: Quality. The question is explicitly about maintaining
     "high quality." Scope (how many skills exist) is the variable under
     examination. Throughput (how fast you can touch skills) is secondary.

[L3] RESOURCES:
     - One person (solo developer, no team)
     - No automated quality checks (no linting, no test harness, no CI)
     - Time: whatever fraction of your working hours you can dedicate to
       maintenance vs. new development, marketing, support, and life
     - Tooling: manual review only — you must read each skill to assess it
     - Energy: maintenance is cognitively expensive and low-dopamine compared
       to creating new skills

[L4] COMPLEXITY:
     - Each skill is a structured procedure (markdown file with phases,
       checklists, failure modes, depth scaling)
     - Quality review per skill requires: reading, testing against a real
       input, checking for internal consistency, verifying cross-references
       to other skills still work, updating if the skill format has evolved
     - Complexity varies: simple skills (e.g., /ezy) take 5-10 min to review;
       complex router skills (e.g., /claim, /decide) take 30-60 min
     - Average review time estimate: ~20 minutes per skill for a meaningful
       quality pass

[L5] PRIOR_EXPERIENCE:
     - You've built 592 skills, so you know the format intimately
     - You've done quality passes before (the varying quality is evidence of
       incomplete passes, not zero experience)
     - You have NOT maintained 592 skills at high quality simultaneously —
       the current state (varying quality) is the empirical data point
```

---

## Phase 2: Limit Estimation

### Scope Estimate (How many skills can be maintained at high quality)

```
[L6] SCOPE ESTIMATE:

  OPTIMISTIC: 200 skills
    Reasoning: If you spent ~3 hours/week purely on maintenance (not creation),
    and averaged 15 min per skill review, that's 12 skills/week or ~624/year.
    A full cycle through 200 skills would take ~17 weeks (~4 months). Skills
    could be reviewed ~3x/year. That's plausible IF nothing else competes.

  REALISTIC: 80-120 skills
    Reasoning: Maintenance competes with new development, marketing, support,
    and your own energy. Realistically you'll spend 1-2 hours/week on
    maintenance. Some weeks zero. Some skills will need rework, not just
    review. A maintenance cycle through 100 skills takes 6+ months. That's
    a ~2x/year review cadence, which is the minimum for "high quality."

  PESSIMISTIC: 40-60 skills
    Reasoning: If quality means "I've tested this against real input in the
    last 3 months and I'm confident it works well," then the bar is high.
    Solo dev with no automation, competing priorities, and maintenance being
    low-reward work means many weeks will pass with zero maintenance done.

  DISCOUNT: Optimistic (200) × 0.5 = 100
    The discount is aggressive (0.5 rather than 0.6-0.8) because:
    - Maintenance is unsexy work that gets deprioritized
    - There's no forcing function (no automated checks, no users filing bugs
      per-skill)
    - 592 existing skills means the "maintain everything" instinct will
      constantly pull attention away from focused maintenance of a subset
```

### Throughput Estimate (Skills reviewed per week)

```
[L7] THROUGHPUT ESTIMATE:

  OPTIMISTIC: 12-15 skills/week
    (3 hours of focused review, 12-15 min per skill)

  REALISTIC: 4-8 skills/week
    (1-1.5 hours, some skills needing rework not just review, some weeks
    skipped entirely — average over a quarter)

  PESSIMISTIC: 1-3 skills/week
    (Maintenance keeps getting bumped by feature work; when you do sit down,
    some skills need substantial rewrites)

  DISCOUNT: Optimistic × 0.45 = ~6 skills/week average
    Heavy discount because maintenance throughput degrades over a session
    (skill 1 is reviewed carefully; skill 10 gets a skim) and because
    weeks with zero maintenance will drag the average down hard.
```

### Quality Estimate

```
[L8] QUALITY ESTIMATE:

  AT_CURRENT_SCOPE (592 skills):
    Low-to-moderate. You cannot maintain 592 skills at high quality solo
    without automation. The current "varying quality" state is the natural
    equilibrium of 592 skills with one maintainer. Many skills are probably
    fine, but you don't KNOW which ones are fine, which is itself a quality
    problem.

  AT_REDUCED_SCOPE (414 skills, -30%):
    Still too many. 414 is marginally better but doesn't change the
    fundamental dynamic. You'd still be unable to cycle through them all
    in a reasonable timeframe.

  AT_EXPANDED_SCOPE (770 skills, +30%):
    Quality would degrade further. Each new skill adds maintenance debt.
    At 770, the fraction of skills you've meaningfully reviewed in the last
    6 months would drop below 10%.
```

### Planning Fallacy Corrections Applied

| Bias | How it applies here |
|------|-------------------|
| **"I'll be focused the whole time"** | Maintenance sessions will be interrupted. You'll start reviewing a skill, find a broken cross-reference, fall down a rabbit hole fixing three other skills, and count that as "4 skills reviewed" when really none were completed properly. Assume 60% effective time. |
| **"Each item takes about X minutes"** | Simple skills: 10 min. Complex routers: 45-60 min. You'll mentally budget for the simple case and hit the complex case more often than expected. Multiply your per-skill estimate by 1.5x. |
| **"I won't need to redo anything"** | Some skills will need rework, not just review. Estimate 20-25% of reviewed skills need meaningful edits, and edits take 2-3x longer than review. |
| **"I know how to do this"** | You know how to write skills. You haven't maintained 100+ skills at high quality before. Writing and maintaining are different activities with different fatigue curves. |
| **"I can just push through"** | Maintenance is low-dopamine. By skill 6 in a session, your review quality drops. You'll start approving skills that "look fine" instead of testing them. Session 1 quality is not session 5 quality. |

---

## Phase 3: Tradeoff Analysis

```
[L9] TRADEOFF TRIANGLE:

  CURRENT PLAN: HIGH scope (592) × LOW-MODERATE quality × LOW throughput
  This is where you are. The triangle has resolved itself: you chose scope
  (by building 592 skills) and the triangle auto-sacrificed quality.

  IF PRIORITIZE SCOPE (keep all 592):
    Quality stays low-moderate. You cannot meaningfully review them all.
    You'll have a large library where users can't trust any individual skill
    without testing it themselves. Throughput stays low because there's too
    much surface area to cover.

  IF PRIORITIZE QUALITY (reduce to maintainable set):
    Cut to 80-120 "core" skills. Each one reviewed, tested, and validated.
    Users can trust that any skill they invoke works well. Remaining skills
    archived or marked as "community/unreviewed." Throughput becomes
    manageable (~full review cycle every 3-4 months).

  IF PRIORITIZE SPEED (fastest review cycle):
    Keep all 592 but lower the quality bar — quick skim instead of real
    testing. You could "touch" all 592 in a quarter, but the reviews would
    be shallow. This creates an illusion of maintenance without real quality
    assurance.

[L10] RECOMMENDED PRIORITY: Quality.
  The product's value proposition depends on skills actually working well.
  A 100-skill library where every skill is solid beats a 592-skill library
  where quality is a coin flip. Users who hit one bad skill lose trust in
  all of them.

[L11] SACRIFICE: Scope takes the hit.
  Reduce the actively-maintained set. The other skills don't need to be
  deleted — they can exist as "extended" or "experimental" — but only the
  core set carries the quality guarantee.
```

---

## Phase 4: Safe Operating Boundary

```
[L12] SAFE BOUNDARY:

  SCOPE: 75-100 skills in the "actively maintained at high quality" tier
  THROUGHPUT: 5-6 skills reviewed per week (sustainable average over months)
  QUALITY: Each skill tested against real input within the last 3-4 months;
           cross-references verified; format consistent with current standards

  MARGIN: ~50% below the optimistic maximum (200)
  MARGIN_RATIONALE:
    - Solo developer with no automation = high variance in maintenance output
    - Maintenance competes with creation, marketing, and other priorities
    - No external forcing function (no CI, no user-reported per-skill bugs)
    - The penalty for overcommitting is invisible: skills silently degrade
      rather than loudly failing, so you won't notice when you've exceeded
      your limit until quality has already eroded
    - A 50% margin means that even in bad months, the core set stays covered

[L13] DANGER ZONE:

  SCOPE_DANGER: Above 150 skills in the "maintained" tier, quality will
    degrade noticeably. You simply cannot cycle through 150+ skills at a
    meaningful depth with 1-2 hours/week of maintenance time. The math
    doesn't work: 150 skills × 20 min = 50 hours per full cycle. At 1.5
    hrs/week that's 33 weeks — over 8 months between reviews. That's not
    "high quality maintenance."

  THROUGHPUT_DANGER: Above 10 skills reviewed in a single session,
    review quality drops. You'll start skimming instead of testing.
    Cap maintenance sessions at 60-90 minutes / 6-8 skills.

  QUALITY_DANGER: If any skill in the "maintained" tier hasn't been
    reviewed in 6+ months, it should be flagged. If more than 20% of the
    maintained set is past 6 months, the tier is too large.

[L14] CHECKPOINTS:

  AT_25% (~25 skills designated as maintained):
    - Can you name each skill and what it does without looking?
    - Have you reviewed all 25 at least once in the last 2 months?
    - Is the review process itself working, or does it feel like busywork?

  AT_50% (~50 skills):
    - Is the review cadence holding? Check: how many weeks in the last
      month had zero maintenance time?
    - Are you actually testing skills against real inputs, or just reading
      them and saying "looks fine"?
    - Has any user (including yourself) found a broken skill in the
      maintained set?

  AT_75% (~75 skills):
    - Calculate: at your actual throughput, how many months would a full
      cycle take? If the answer is >4 months, you've exceeded your limit.
    - Are you still creating new skills while trying to maintain these?
      If yes, check whether creation is cannibalizing maintenance time.
    - If behind here: freeze the maintained set size. Do not add more
      until the cycle time is under 4 months.
```

---

## Phase 5: Output

```
LIMIT ASSESSMENT
================

SUBJECT: Number of skills a solo developer can maintain at high quality
CONTEXT: 592 skills exist, one maintainer, no automated quality checks,
         no team, maintenance competes with creation and other work

ESTIMATES:
  SCOPE:      200 (optimistic) → 80-120 (realistic) → 40-60 (pessimistic)
  THROUGHPUT: 12-15/week (optimistic) → 4-8/week (realistic) → 1-3/week (pessimistic)
  QUALITY:    At 592 skills: low-moderate → At 100: high → At 770: poor

TRADEOFF: Prioritize QUALITY — sacrifice SCOPE
  Keep 592 skills in the repository, but only designate 75-100 as the
  actively-maintained, quality-guaranteed core.

SAFE OPERATING BOUNDARY:
  SCOPE: 75-100 skills (actively maintained tier)
  THROUGHPUT: 5-6 skills reviewed per week (sustained average)
  QUALITY: Every core skill tested against real input within last 3-4 months
  MARGIN: 50% below optimistic maximum — because maintenance is invisible
          debt and solo devs have no backstop

DANGER ZONES:
  - Above 150 maintained skills: cycle time exceeds 8 months (quality fiction)
  - Above 10 skills in a single review session: review depth degrades
  - Any maintained skill unreviewed for 6+ months: flag for demotion or review
  - Weeks with zero maintenance: if 3+ consecutive, the system is failing

CHECKPOINTS:
  - At 25 skills: Is the process working? Can you name them all?
  - At 50 skills: Is cadence holding? Are you actually testing or skimming?
  - At 75 skills: Calculate real cycle time. If >4 months, stop adding.
  - Ongoing: If creating new skills while maintenance is behind, stop creating.

THE KEY NUMBER: ~100 skills.
  That's your realistic ceiling for "solo dev, no automation, high quality."
  The other 492 skills aren't wasted — they're the extended library,
  the experimental tier, the community contributions. But they don't
  carry a quality guarantee, and you should be honest about that
  distinction with yourself and with users.
```

---

## What This Means Concretely

The math is straightforward:

- **100 skills x 20 min/review = ~33 hours per full cycle**
- **At 1.5 hrs/week maintenance = ~22 weeks (5.5 months) per cycle**
- **That's roughly 2 full cycles per year** — the minimum for "maintained"

At 592 skills with the same time budget:

- **592 skills x 20 min = ~197 hours per full cycle**
- **At 1.5 hrs/week = ~131 weeks (2.5 years) per cycle**
- **That's not maintenance. That's archaeology.**

The honest answer: you can maintain about **100 skills at high quality**, and you should pick those 100 deliberately rather than letting quality be distributed randomly across 592.

---

## Automation Changes the Math

Every piece of automation shifts the boundary:

| Automation | Effect on limit |
|-----------|----------------|
| Format linter (checks structure, required sections) | +30-50 skills (catches structural rot automatically) |
| Cross-reference checker (verifies linked skills exist) | +20-30 skills (catches broken chains) |
| Example input/output tests per skill | +50-80 skills (biggest lever — validates skills without human review) |
| User feedback per skill (ratings, bug reports) | +40-60 skills (users become your QA team) |
| All of the above combined | 250-350 skills maintainable at high quality |

Without automation: ~100. With full automation: ~300. That's the investment case for building quality infrastructure before adding more skills.

---

READY FOR:
- `/iagca` — to compress the 592 down to the ~100 core (which skills make the cut?)
- `/ro` — to rank-order skills by importance for the maintained tier
- `/de` — to extract dependencies between skills (which ones must be maintained together?)
- `/to` — to sequence the first maintenance cycle across the selected core

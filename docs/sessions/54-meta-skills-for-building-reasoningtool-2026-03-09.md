# /meta What skills would help me most right now in building reasoningtool?
**Date:** 2026-03-09
**Skill:** /meta (Get Oriented)

---

## Routing Decision

The input is "What skills would help me most right now?" -- this is a request to rank skills by ROI for a specific goal. Routing to **`/given`** (Rank Skills by ROI for a Given Goal).

---

## /given — Skills Ranked by ROI for Building Reasoningtool

---

### Phase 1: Goal Parse

```
[G1] GOAL: Get reasoningtool from "built but unused" to "people using it and getting value"
[G2] GOAL_TYPE: Achievement (go-to-market for an existing product)
[G3] CONSTRAINTS: Solo developer, unemployed (full time available but finite runway), no users yet, no co-founder, no marketing budget implied
[G4] URGENCY: Ready-to-act — the product exists, the website is built, the next moves are distribution and adoption
[G5] CURRENT_STATE: 592 skills built, website live, subreddit planned but not launched, key challenges self-identified as distribution, quality consistency, onboarding, monetization
[G6] GOAL_CLARITY: Somewhat clear — "building reasoningtool" could mean continuing to add skills, improving quality, getting users, or making money. Context suggests the priority is getting users.
```

```
[G7] CLARITY_ISSUE: "Building" is ambiguous between product development and business development. Given 592 skills exist and no users exist, the bottleneck is almost certainly not "more skills."
[G8] RESOLUTION: Proceed with ranking — interpret "building" as "making reasoningtool succeed" with emphasis on the stated challenges: distribution, quality consistency, onboarding, monetization.
```

---

### Phase 2: Candidate Selection

**Direct skills (address the goal or a sub-goal):**

```
[G-1] CANDIDATE: /sid — RELEVANCE: Identify the actual situation. Ben may be building when he should be selling. The biggest risk for a solo dev with 592 skills and 0 users is misidentifying what phase he's in.
[G-2] CANDIDATE: /ecal — RELEVANCE: Calibrate effort across the four challenges. Not all four deserve equal time. Distribution likely dominates.
[G-3] CANDIDATE: /ro — RELEVANCE: Reorder the four stated challenges (distribution, quality consistency, onboarding, monetization) by actual priority given current state.
[G-4] CANDIDATE: /kta — RELEVANCE: Ben knows what needs to happen (get users) but may be defaulting to comfortable work (building more skills). Diagnoses execution barriers.
```

**Preparatory skills (make direct skills more effective):**

```
[G-5] CANDIDATE: /sdc — RELEVANCE: Self-deception check. Is continued skill-building serving the product or serving the builder's comfort? The single most dangerous failure mode for a solo dev with a complete product and no users.
[G-6] CANDIDATE: /obv — RELEVANCE: Check the obvious. Has Ben actually asked anyone to use it? Has he posted it anywhere? Sometimes the obvious action is the undone action.
```

**Validation skills (verify progress or output quality):**

```
[G-7] CANDIDATE: /pv — RELEVANCE: Validate the onboarding procedure. If the first-user experience is broken, distribution effort is wasted.
[G-8] CANDIDATE: /abts — RELEVANCE: Design an A/B test for onboarding flows or landing page messaging before scaling distribution.
```

**Risk skills (reduce uncertainty or prevent failure):**

```
[G-9] CANDIDATE: /prm — RELEVANCE: Premortem on the launch. What kills reasoningtool in 3 months? Already done (prompt 13), but worth revisiting with fresh eyes.
[G-10] CANDIDATE: /iagca — RELEVANCE: Scope compression. 592 skills may be "getting carried away." A tighter offering might convert better.
```

---

### Phase 3: ROI Scoring

```
[G-1] SCORE: /sid (Identify the Situation)
  UPSIDE: Critical — If Ben is in "sell" phase but acting like "build" phase, every hour of skill work is wasted
  COST: Trivial — Takes 10 minutes, produces a frame shift
  RISK: Negligible — Worst case confirms he's doing the right thing
  TIMING_FIT: Urgent — 592 skills, 0 users. This should have been run already
  ROI_CLASS: HIGH
  ROI_REASONING: The highest-leverage move is correctly identifying that "building" is over and "selling" has begun.
```

```
[G-2] SCORE: /kta (Knowledge to Action)
  UPSIDE: High — Diagnoses why the known-necessary actions (post to Reddit, tell people, ask for feedback) aren't happening
  COST: Low — One session, produces specific unblock actions
  RISK: Low — May surface uncomfortable truths but that's the point
  TIMING_FIT: Right time — He has the knowledge, the product exists, execution is the gap
  ROI_CLASS: HIGH
  ROI_REASONING: The gap between "I know I need users" and "I'm still building skills" is an execution barrier, not an information gap.
```

```
[G-3] SCORE: /sdc (Self-Deception Check)
  UPSIDE: High — Detects if continued building is motivated reasoning ("I need just 50 more skills before launch")
  COST: Low — One honest session
  RISK: Low — Emotional discomfort is a feature, not a risk
  TIMING_FIT: Right time — The ratio of 592:0 (skills:users) is a signal worth examining
  ROI_CLASS: HIGH
  ROI_REASONING: A solo dev who keeps building past the point of diminishing returns is the #1 failure mode for this project.
```

```
[G-4] SCORE: /obv (Check the Obvious)
  UPSIDE: High — The most likely answer to "how do I get users" is "tell people it exists"
  COST: Trivial — Quick check
  RISK: Negligible — Surfaces undone basics
  TIMING_FIT: Urgent — Before any sophisticated distribution strategy, check if the simple thing has been tried
  ROI_CLASS: HIGH
  ROI_REASONING: The obvious action (sharing the tool with real humans and asking them to try it) may simply not have happened yet.
```

```
[G-5] SCORE: /ro (Reorder Challenges)
  UPSIDE: Medium — Clarifies which of the four challenges to attack first
  COST: Trivial — Quick reorder exercise
  RISK: Low — May over-simplify interdependencies
  TIMING_FIT: Right time — Prioritization before effort allocation
  ROI_CLASS: MEDIUM
  ROI_REASONING: Useful but subordinate to the situational awareness skills above — once /sid clarifies the phase, ordering follows naturally.
```

```
[G-6] SCORE: /ecal (Effort Calibration)
  UPSIDE: Medium — Prevents over-investing in low-stakes challenges while under-investing in high-stakes ones
  COST: Low — One calibration session
  RISK: Low — Calibration on wrong dimensions wastes time
  TIMING_FIT: Right time — Resource allocation matters when you're solo
  ROI_CLASS: MEDIUM
  ROI_REASONING: Good hygiene skill but only valuable after the phase identification is correct.
```

```
[G-7] SCORE: /pv (Procedure Validation)
  UPSIDE: Medium — Ensures the onboarding path actually works before sending traffic
  COST: Medium — Requires defining and testing the procedure
  RISK: Low — May optimize prematurely if no users are coming yet
  TIMING_FIT: Right time — Should validate before major distribution push, but not before first users
  ROI_CLASS: MEDIUM
  ROI_REASONING: Important but sequentially dependent on having at least a few users to observe.
```

```
[G-8] SCORE: /iagca (Scope Compression)
  UPSIDE: Medium — A focused 20-skill offering might convert better than a 592-skill catalog
  COST: Medium — Requires deciding what to cut or hide
  RISK: Medium — Could cut the wrong things without user data
  TIMING_FIT: Early — Better to get user data first, then compress
  ROI_CLASS: MEDIUM
  ROI_REASONING: Valuable idea but premature without knowing which skills users actually want.
```

```
[G-9] SCORE: /abts (A/B Test Design)
  UPSIDE: Medium — Structured experimentation for messaging/onboarding
  COST: High — No traffic to run tests against yet
  RISK: High — Designing tests without traffic is premature optimization
  TIMING_FIT: Early — Need traffic before testing variations
  ROI_CLASS: LOW
  ROI_REASONING: Useless without users. Get users first, then optimize.
```

```
[G-10] SCORE: /prm (Premortem)
  UPSIDE: Low — Already done in prompt 13
  COST: Low — Quick revisit
  RISK: Low — Diminishing returns on repeated premortems
  TIMING_FIT: Wrong time — Already done today
  ROI_CLASS: LOW
  ROI_REASONING: Already completed this session. Running it again is procrastination disguised as analysis.
```

### Interaction Effects

```
[G-11] INTERACTION: /kta ROI becomes HIGHER if /sid runs first — /sid identifies the phase, /kta unblocks action within that phase
[G-12] INTERACTION: /sdc ROI becomes LOWER if /sid runs first and produces a clear "you're in sell phase" — the deception is already surfaced
[G-13] INTERACTION: /obv becomes MORE SPECIFIC if /sid runs first — "obvious" is relative to the correctly identified situation
[G-14] INTERACTION: /ro becomes UNNECESSARY if /obv reveals the answer is simply "tell people it exists"
```

---

### Phase 4: Ranking and Execution Slice

**RUN_NOW (immediate execution slice):**

1. **`/sid`** — ROI: HIGH — Identify what phase you're actually in. 592 skills and 0 users is a diagnostic fact.
2. **`/kta`** — ROI: HIGH — You know you need users. Diagnose what's stopping you from doing the uncomfortable distribution work.
3. **`/obv`** — ROI: HIGH — Before any strategy, check: have you simply shown it to 10 humans and asked them to try it?
4. **`/sdc`** — ROI: HIGH — Check whether building skill #593 is serving the product or avoiding the market.

**FULL_RANKING:**

1. `/sid` — ROI: HIGH
   UPSIDE: Critical — COST: Trivial — RISK: Negligible — TIMING: Urgent
   WHY: The 592:0 ratio is the single most important fact. Name the phase correctly.

2. `/kta` — ROI: HIGH
   UPSIDE: High — COST: Low — RISK: Low — TIMING: Right time
   WHY: The gap is execution, not information. Unblock the doing.

3. `/obv` — ROI: HIGH
   UPSIDE: High — COST: Trivial — RISK: Negligible — TIMING: Urgent
   WHY: The simplest distribution action may just be undone.

4. `/sdc` — ROI: HIGH
   UPSIDE: High — COST: Low — RISK: Low — TIMING: Right time
   WHY: Motivated reasoning is the silent killer of solo projects.

5. `/ro` — ROI: MEDIUM
   UPSIDE: Medium — COST: Trivial — RISK: Low — TIMING: Right time
   WHY: Sequence the four challenges by actual impact, not alphabetical order.

6. `/ecal` — ROI: MEDIUM
   UPSIDE: Medium — COST: Low — RISK: Low — TIMING: Right time
   WHY: Calibrate how much time each challenge deserves.

7. `/pv` — ROI: MEDIUM
   UPSIDE: Medium — COST: Medium — RISK: Low — TIMING: Right time
   WHY: Validate onboarding before scaling, but get first users first.

8. `/iagca` — ROI: MEDIUM
   UPSIDE: Medium — COST: Medium — RISK: Medium — TIMING: Early
   WHY: Scope compression is smart but needs user data to guide it.

9. `/abts` — ROI: LOW
   UPSIDE: Medium — COST: High — RISK: High — TIMING: Early
   WHY: No traffic to test against. Premature.

10. `/prm` — ROI: LOW
    UPSIDE: Low — COST: Low — RISK: Low — TIMING: Wrong time
    WHY: Already done this session. Repeating it is avoidance.

**NEGATIVE_ROI (tempting but harmful now):**

- `/imps` (Improve Skill) — WHY_NEGATIVE_NOW: Polishing skills when no one is using them is the purest form of productive procrastination. Every hour improving skill quality with 0 users is an hour not spent finding out if anyone wants this. — WHEN_IT_BECOMES_POSITIVE: After 10+ users report that a specific skill failed them.

- `/ma` (Morphological Analysis for new skills) — WHY_NEGATIVE_NOW: Generating more skills when 592 exist and 0 are being used is adding inventory to a store with no customers. — WHEN_IT_BECOMES_POSITIVE: After user feedback reveals a genuine gap.

- `/skgap` (Skill Gap Analysis) — WHY_NEGATIVE_NOW: Same as /ma. Finding missing skills is building-phase work. You're past that phase. — WHEN_IT_BECOMES_POSITIVE: After users request capabilities that don't exist.

- `/soph` (Sophisticated Analysis) — WHY_NEGATIVE_NOW: Applying sophisticated multi-layered analysis to the distribution problem is a way to think about distribution without actually distributing. The answer is probably simple: tell people. — WHEN_IT_BECOMES_POSITIVE: After simple approaches fail and you need to understand why.

**INTERACTION_EFFECTS:**

- `/sid` + `/kta`: sid identifies "you're in sell phase," kta unblocks selling. Run in this order.
- `/obv` + `/sdc`: obv might reveal the obvious action; sdc reveals why you've been avoiding it. Complementary.
- `/sid` + `/sdc`: significant overlap — if /sid produces a clear phase identification, /sdc may be partially redundant. But the motivated-reasoning angle adds enough unique value to justify both.

---

### The Uncomfortable Summary

The skills that would help you most right now are not the ones that feel productive. The highest-ROI skills are all introspective and confrontational:

- **"What situation am I actually in?"** (`/sid`)
- **"What's stopping me from doing what I know I should?"** (`/kta`)
- **"Have I done the obvious thing?"** (`/obv`)
- **"Am I deceiving myself about what 'building' means?"** (`/sdc`)

None of these produce new skills. None improve the website. None generate content. They all point at the same uncomfortable truth: a product with 592 features and 0 users has a distribution problem, not a feature problem. The skills most likely to help are the ones that force you to stop building and start shipping to humans.

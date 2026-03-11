# /but Reasoningtool has 592 skills, but that's overwhelming for new users
**Date:** 2026-03-09
**Skill:** /but (Contrast and Objection Handler)

---

## Phase 1: Extraction

```
[B1] RAW_STATEMENT: "Reasoningtool has 592 skills, but that's overwhelming for new users"
[B2] CLAIM_A: Reasoningtool has a large number of skills (592), which represents comprehensive coverage
[B3] CLAIM_B: That volume is overwhelming for people who are new to the tool
[B4] PRIMARY_WEIGHT: B is primary
```

### Primary Weight Test

Removing A ("Reasoningtool has 592 skills") and the statement still holds — the user is raising the overwhelm problem. The skill count is setup/context. Removing B ("that's overwhelming for new users") leaves a neutral fact with no tension. **B is the point.** The user isn't bragging about 592 skills; they're worried about the onboarding experience.

---

## Phase 2: Tension Classification

```
[B5] TENSION_TYPE: tradeoff
[B6] CLASSIFICATION_EVIDENCE: Comprehensiveness and approachability are both desirable but compete.
    More skills = more coverage = more value for expert users.
    More skills = more surface area = more confusion for new users.
    Both goals are legitimate. Neither can be dismissed.
    This is not a contradiction (592 skills really does exist AND it really is overwhelming).
    This is not a risk (overwhelm is already happening, not hypothetical).
    This is not an exception (it's not "works except for edge case X").
    It's a classic tension between breadth and accessibility.
```

---

## Phase 3: Hidden Objection Check

```
[B7] HIDDEN_OBJECTION_CHECK:
  ENERGY_MATCH: no — the stated objection ("overwhelming") is mild compared to the
    likely actual concern
  POSSIBLE_HIDDEN: "Are we building something nobody can actually use? Is the
    complexity self-defeating? Does the product need to be restructured, not just
    better documented?"
  EVIDENCE: The user already has tiered architecture (T1/T2/T3), category routers,
    search, and emoji navigation — meaning they've already tried to solve this.
    Raising it again suggests those solutions haven't fully worked, and the real
    worry is deeper than "users feel overwhelmed."
```

```
[B8] LIKELY_HIDDEN_OBJECTION: "The existing progressive disclosure system (tiers,
    categories, search) may not be sufficient. New users might still bounce because
    they don't know where to start, even with the infrastructure we've built."
[B9] SURFACE_QUESTION: "When you say overwhelming — do you mean users don't know
    the 592 exist and feel lost, or do you mean they see the 592 and freeze? Those
    are different problems."
```

---

## Phase 4: Resolution Routing

This is a tradeoff tension with a likely hidden objection about whether existing solutions are working. The tradeoff itself (breadth vs. accessibility) doesn't need resolution — it needs navigation. The actionable question is how to make 592 skills feel like 5-12 to a new user.

```
[B10] RECOMMENDED_ROUTE: /decide — the real question is which progressive disclosure
    strategy best resolves the breadth/accessibility tradeoff for new users
[B11] INVOCATION: /decide "What's the best onboarding approach to make 592 skills
    feel approachable: (a) guided flows that ask what the user needs, (b) curated
    starter packs of 5-10 skills, (c) a single entry-point skill that routes
    everything, (d) use-case-based landing pages"
[B12] ALTERNATIVE: /dd — define the domain boundaries of what "new user" means and
    what their first 5 minutes should look like, before designing solutions
```

---

## Phase 5: Output

```
"BUT" ANALYSIS
==============

ORIGINAL: "Reasoningtool has 592 skills, but that's overwhelming for new users"

CLAIM A: Reasoningtool has comprehensive coverage (592 skills)
CLAIM B: That volume overwhelms new users
PRIMARY: B — the overwhelm concern is the point; 592 is context

TENSION TYPE: tradeoff
EVIDENCE: Breadth and approachability are both desirable but compete. More
  skills means more capability AND more cognitive load. Neither side can be
  dismissed without losing real value.

HIDDEN OBJECTION: Likely present. The user already built progressive disclosure
  infrastructure (3 tiers, 17 category routers, search, emoji navigation).
  Raising overwhelm again suggests those measures haven't fully resolved it.
  The deeper worry: "Is the existing tiered system actually working, or do new
  users still bounce?"

RESOLUTION:
  APPROACH: Don't reduce the 592. Don't "solve" the tradeoff by picking a side.
    Instead, design the new-user experience so they never encounter 592 until
    they're ready. The architecture already supports this — tier 1 is 12 skills,
    category skills are 17 routers. The gap is likely in how users ENTER, not
    in what exists.

  Three concrete navigation strategies to evaluate:

  1. SINGLE ENTRY POINT: Make /meta (or a new /start skill) the canonical
     first interaction. User describes what they need in plain language; the
     skill routes them. They never see a list. The 592 are invisible infrastructure.

  2. USE-CASE LANDING: On the website, replace (or supplement) the skill
     browser with use-case cards: "I need to make a decision," "I need to
     write something," "I need to check my thinking." Each card maps to
     2-3 skills. The 592 exist but the entry is through ~10 doors.

  3. PROGRESSIVE REVEAL BY USAGE: New users see only tier 1 (12 skills).
     Each skill's output suggests related tier 2 skills when relevant.
     Tier 3 appears only through explicit discovery or when a tier 2 skill
     invokes it. The 592 unfold through use, not browsing.

  → INVOKE: /decide "Best onboarding strategy for 592-skill tool: single
    entry router vs. use-case landing pages vs. progressive reveal by usage"
  WHY: This is ultimately a design decision with tradeoffs of its own.
    /decide will weight the options against criteria like implementation
    effort, user retention, and discoverability.

  IF BOTH TRUE (tension, not contradiction):
  NAVIGATE: Both claims ARE true simultaneously. 592 skills is genuinely
    valuable AND genuinely overwhelming. The resolution isn't fewer skills
    or tougher users — it's better surfaces. The skill count is a backend
    fact; the user experience is a frontend design problem. Hold both by
    keeping the depth while controlling the exposure. The category routers
    and tier system are the right architecture; the question is whether the
    entry points are visible and obvious enough that a new user's first
    interaction is guided, not browsed.
```

---

## Key Insight

The "but" here is not about the 592 being a problem. It's about the **distance between the architecture and the experience.** The tiered system, category routers, and search already exist — the real gap is likely that new users still land on a surface that exposes too much too soon, rather than guiding them through one of the 17 category entry points. The fix is almost certainly at the website/onboarding layer, not the skill architecture layer.

# /tobd Map what's blocking what in the reasoningtool roadmap
**Date:** 2026-03-09
**Skill:** /tobd (To Be Done - Dependencies)

---

## Phase 1: TBD Inventory

Scanning the roadmap activities and their unresolved decisions:

```
[O1] TBD_LIST:
  [O1a] TBD: What "good enough" skill quality means — TYPE: Design — BLOCKING: Knowing when to stop improving and start promoting
  [O1b] TBD: Which website UX improvements matter most — TYPE: Design — BLOCKING: User onboarding experience
  [O1c] TBD: What content to create and where to publish — TYPE: Decision — BLOCKING: Awareness and inbound traffic
  [O1d] TBD: When and how to launch the subreddit — TYPE: Decision — BLOCKING: Community formation
  [O1e] TBD: How to get the first 10 real users — TYPE: Information — BLOCKING: Any feedback loop
  [O1f] TBD: What feedback mechanism to use and what to ask — TYPE: Design — BLOCKING: Learning what to fix
  [O1g] TBD: Whether/how to monetize — TYPE: Scope — BLOCKING: Sustainability and product direction
  [O1h] TBD: Which skills to showcase (out of 592) — TYPE: Decision — BLOCKING: Content, demos, onboarding
  [O1i] TBD: Who the target user is — TYPE: Decision — BLOCKING: All messaging, content, and channel choices
  [O1j] TBD: What the core value proposition actually is — TYPE: Decision — BLOCKING: All outbound communication

[O2] TBD_COUNT: 10 items
```

---

## Phase 2: Dependency Analysis

### Pairwise Dependencies

```
[O3] CASCADE: Resolving [O1j: core value prop] eliminates or constrains [O1c: what content], [O1d: subreddit framing], [O1h: which skills to showcase]
     REASON: Once you know what you're selling, the content, community framing, and showcase skills all follow directly.

[O4] CASCADE: Resolving [O1i: target user] eliminates or constrains [O1c: content], [O1d: subreddit], [O1e: how to get first users], [O1b: which UX improvements]
     REASON: Knowing who you're building for determines where they are, what they need, and what the UX should optimize for.

[O5] DEPENDENCY: [O1j: core value prop] depends on [O1i: target user]
     REASON: The value proposition is "what does this do for whom" — you need the whom first.

[O6] DEPENDENCY: [O1c: content] depends on [O1j: value prop] and [O1i: target user]
     REASON: Content without a clear audience and message is noise.

[O7] DEPENDENCY: [O1d: subreddit launch] depends on [O1c: content] (need seed content)
     REASON: A subreddit with no posts dies. Need at least 5-10 high-quality pieces ready at launch.

[O8] DEPENDENCY: [O1e: first users] depends on [O1d: subreddit] OR [O1c: content distribution]
     REASON: Users come from somewhere — you need at least one channel live.

[O9] DEPENDENCY: [O1f: feedback mechanism] depends on [O1e: first users]
     REASON: Can't collect feedback without users. But the mechanism should be designed before users arrive.

[O10] DEPENDENCY: [O1g: monetization] depends on [O1f: feedback] (partially)
      REASON: Premature monetization decisions without user signal are guessing. But basic direction (free/freemium/paid) should be set early.

[O11] DEPENDENCY: [O1a: skill quality bar] depends on [O1i: target user]
      REASON: Quality for a philosophy professor differs from quality for a startup founder.

[O12] DEPENDENCY: [O1h: which skills to showcase] depends on [O1i: target user] and [O1j: value prop]
      REASON: Showcase skills must demonstrate the value prop to the target user.

[O13] INDEPENDENT: [O1a: skill quality] and [O1d: subreddit launch] (partially)
      REASON: Quality improvement is internal work; subreddit prep is external. Can parallel once target user is known.

[O14] INDEPENDENT: [O1b: website UX] and [O1c: content creation]
      REASON: Different workstreams, can run simultaneously once target user is known.

[O15] DESIGN DEPENDENCY: [O1b: website UX] depends on [O1i: target user]
      REASON: UX decisions (discovery flow, onboarding, complexity exposure) depend entirely on who's using it.
```

### Dependency Types Summary

| TBD Pair | Type | Direction |
|----------|------|-----------|
| Target user -> Value prop | Information dependency | Resolve user first |
| Target user -> Content | Information dependency | Resolve user first |
| Target user -> UX | Design dependency | Resolve user first |
| Target user -> Skill quality bar | Design dependency | Resolve user first |
| Target user -> Which skills to showcase | Design dependency | Resolve user first |
| Value prop -> Content | Design dependency | Resolve value prop first |
| Value prop -> Subreddit framing | Design dependency | Resolve value prop first |
| Content -> Subreddit launch | Information dependency | Need seed content first |
| Subreddit/Content -> First users | Resource dependency | Need a channel live |
| First users -> Feedback | Information dependency | Need users to get feedback |
| Feedback -> Monetization | Information dependency | Need signal before monetizing |

---

## Phase 3: Critical Path

```
[O16] DEPENDENCY GRAPH:

  [O1i: Target user] → [O1j: Value prop] → [O1h: Showcase skills] → [O1c: Content] → [O1d: Subreddit] → [O1e: First users] → [O1f: Feedback] → [O1g: Monetization]
                     ↘                                                                                    ↗
  [O1i: Target user] → [O1a: Quality bar] → (quality work runs parallel) ─────────────────────────────────
                     ↘
  [O1i: Target user] → [O1b: Website UX] → (UX work runs parallel) ───────────────────────────────────────

  [O1i] ⇒ constrains [O1j, O1a, O1b, O1c, O1e, O1h]  (cascade — highest leverage)
  [O1j] ⇒ constrains [O1c, O1d, O1h]                   (cascade — second highest leverage)

[O17] CRITICAL PATH: O1i → O1j → O1h → O1c → O1d → O1e → O1f → O1g
  Length: 8 sequential resolutions
  Estimated time: 6-10 weeks (some steps overlap in execution)
  Bottleneck: O1c (content creation) — takes the most wall-clock time and is mid-chain

[O18] PARALLEL TRACKS:
  Track 1 (Critical): [Target user] → [Value prop] → [Showcase skills] → [Content] → [Subreddit] → [First users] → [Feedback] → [Monetization]
  Track 2 (Quality):  [Target user] → [Quality bar] → Skill improvement work (ongoing)
  Track 3 (UX):       [Target user] → [Website UX] → UX improvement work (ongoing)
  (Tracks 2 and 3 are independent of Track 1 after the target user decision, and independent of each other)
```

---

## Phase 4: Resolution Plan

```
[O19] RESOLUTION SEQUENCE:

ROUND 1 (resolve first — highest leverage, cascade):
  1. [O1i: Who is the target user?]
     WHO: Ben (sole decision)
     HOW: /decide — Pick from candidate segments: (a) AI power users wanting structured thinking,
          (b) knowledge workers making complex decisions, (c) developers using Claude/LLMs,
          (d) productivity enthusiasts. Use existing 60+ prompt outputs as evidence of what works.
     BY: 2026-03-12 (3 days — this is a decision, not research)
     WHY_FIRST: Cascade — resolves or constrains 6 of the remaining 9 TBDs
     EXPECTED_OUTCOME: Clear user persona with known pain points, hangouts, and language

ROUND 2 (resolve after Round 1 — all can run in parallel):
  2a. [O1j: What is the core value proposition?]
      WHO: Ben
      HOW: /decide with target user as input — test 3-4 framings against the chosen persona
      BY: 2026-03-14
      DEPENDS_ON: O1i (target user)
      EXPECTED_OUTCOME: One sentence that makes the target user say "I need that"

  2b. [O1a: What does "good enough" skill quality mean?]
      WHO: Ben
      HOW: Pick 5 skills the target user would actually use. Run them. Grade them.
           The quality bar = "would this make the target user come back?"
      BY: 2026-03-14
      DEPENDS_ON: O1i (target user)
      EXPECTED_OUTCOME: Concrete quality rubric for skill improvement work

  2c. [O1b: Which website UX improvements matter most?]
      WHO: Ben
      HOW: Walk through the site as the target user persona. Note every friction point.
           Rank by "would this stop someone from trying a second skill?"
      BY: 2026-03-14
      DEPENDS_ON: O1i (target user)
      EXPECTED_OUTCOME: Prioritized UX fix list (top 3-5 items)

ROUND 3 (resolve after Round 2):
  3a. [O1h: Which skills to showcase?]
      WHO: Ben
      HOW: Select 5-8 skills that best demonstrate the value prop for the target user.
           Run each, verify quality meets the bar from 2b.
      BY: 2026-03-17
      DEPENDS_ON: O1j (value prop), O1a (quality bar)
      EXPECTED_OUTCOME: Curated showcase set, tested and polished

  3b. [O1f: What feedback mechanism to use?]
      WHO: Ben
      HOW: Design a lightweight feedback loop — probably a short form or direct DM invitation.
           Keep it simple: "Did this help? What were you trying to do? What happened?"
      BY: 2026-03-17
      DEPENDS_ON: O1i (target user — determines tone and channel)
      EXPECTED_OUTCOME: Feedback mechanism ready to deploy before users arrive

ROUND 4 (resolve after Round 3):
  4. [O1c: What content to create and where?]
     WHO: Ben
     HOW: Create 5-10 pieces that show the showcase skills solving real problems for the target user.
          Format: before/after comparisons, walkthroughs, "I tried thinking about X with structured procedures."
          Channel: wherever the target user hangs out (determined in Round 1).
     BY: 2026-03-24 (1 week — content takes time)
     DEPENDS_ON: O1h (showcase skills), O1j (value prop)
     EXPECTED_OUTCOME: Seed content ready for distribution

ROUND 5 (resolve after Round 4):
  5. [O1d: When and how to launch the subreddit?]
     WHO: Ben
     HOW: Pre-populate with 5+ content pieces from Round 4. Set rules, sidebar with value prop.
          Cross-post to relevant communities where target users are.
     BY: 2026-03-28
     DEPENDS_ON: O1c (seed content)
     EXPECTED_OUTCOME: Live subreddit with enough content to not look dead

ROUND 6 (resolve after Round 5):
  6. [O1e: How to get the first 10 real users?]
     WHO: Ben
     HOW: Share content + subreddit in 3-5 communities where target users are.
          Offer free 1:1 walkthroughs. Ask friends/colleagues who match the persona.
     BY: 2026-04-04
     DEPENDS_ON: O1d (subreddit live), O1c (content distributed)
     EXPECTED_OUTCOME: 10 real users who have tried at least one skill

ROUND 7 (resolve after Round 6 + feedback collection):
  7. [O1g: Whether/how to monetize?]
     WHO: Ben
     HOW: /decide after collecting feedback from first 10-20 users.
          Inputs: what users value, willingness to pay signals, usage patterns.
     BY: 2026-04-18 (need 2 weeks of feedback data)
     DEPENDS_ON: O1f (feedback mechanism active), O1e (users providing feedback)
     IF_CASCADED: Feedback may reveal monetization is premature or that the model is obvious
     EXPECTED_OUTCOME: Decision on free/freemium/paid with rationale
```

---

## Phase 5: Output

```
OPERATIONAL TBD RESOLUTION
===========================

TBDs: 10 total
CRITICAL PATH: 8 sequential steps (target user → value prop → showcase → content → subreddit → users → feedback → monetization)
PARALLEL TRACKS: 3 independent tracks (all fork from "target user" decision)
CASCADE OPPORTUNITIES: 2 high-leverage TBDs that constrain 6+ others

RESOLUTION PLAN:

ROUND 1 — 1 TBD, highest leverage:
  1. Target user decision — WHO: Ben — HOW: /decide with candidate segments — BY: 2026-03-12
     UNLOCKS: Value prop, quality bar, UX priorities, content strategy, channel selection, showcase skills

ROUND 2 — 3 TBDs, all parallel after Round 1:
  2a. Core value proposition — DEPENDS_ON: #1 — WHO: Ben — HOW: /decide — BY: 2026-03-14
  2b. Skill quality bar — DEPENDS_ON: #1 — WHO: Ben — HOW: test 5 skills against persona — BY: 2026-03-14
  2c. Website UX priorities — DEPENDS_ON: #1 — WHO: Ben — HOW: persona walkthrough — BY: 2026-03-14

ROUND 3 — 2 TBDs, parallel:
  3a. Which skills to showcase — DEPENDS_ON: #2a, #2b — WHO: Ben — BY: 2026-03-17
  3b. Feedback mechanism design — DEPENDS_ON: #1 — WHO: Ben — BY: 2026-03-17

ROUND 4 — 1 TBD:
  4. Content creation + channel — DEPENDS_ON: #2a, #3a — WHO: Ben — BY: 2026-03-24

ROUND 5 — 1 TBD:
  5. Subreddit launch — DEPENDS_ON: #4 — WHO: Ben — BY: 2026-03-28

ROUND 6 — 1 TBD:
  6. First 10 users — DEPENDS_ON: #4, #5 — WHO: Ben — BY: 2026-04-04

ROUND 7 — 1 TBD:
  7. Monetization decision — DEPENDS_ON: #6, #3b — WHO: Ben — BY: 2026-04-18

MIGHT_BE_ELIMINATED:
  - Content strategy (#4) may become obvious once value prop is clear
  - Monetization (#7) may be answered by user feedback before you formally decide
  - Feedback mechanism (#3b) may be trivially simple once you know the user persona

PARALLEL WORK (not decisions — execution that can run alongside):
  - Skill quality improvement: starts after Round 2b, runs continuously
  - Website UX fixes: starts after Round 2c, runs continuously
  - Both tracks feed into better user experience by the time Round 6 users arrive

THE ONE THING BLOCKING EVERYTHING:
  "Who is this for?" (O1i) is the single decision that the entire roadmap is waiting on.
  Every other TBD either depends on it directly or depends on something that depends on it.
  Until this is resolved, all other work is either premature or generic.

READY FOR:
- Execute Round 1: /decide "Who is the target user for reasoningtool?"
- Then parallel Round 2: /decide "What is the core value prop?" + quality + UX work
- /to for detailed task sequencing within each round
```

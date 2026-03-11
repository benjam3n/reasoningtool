# /tbd What should I work on today, given that I'm building reasoningtool solo?
**Date:** 2026-03-09
**Skill:** /tbd (To Be Done)

---

## Phase 1: TBD Identification

Source scanned: The implicit plan behind "what should I work on today" — surfacing every unresolved decision embedded in the question and its context (solo developer, 592 skills, website exists, no users, subreddit planned, distribution identified as bottleneck, content creation identified as unstarted gating work).

```
[T1] What specific content should I create first? — SOURCE: gap (content creation identified as critical but no content plan exists)
[T2] Where should content be published? — SOURCE: hedge ("subreddit planned" — planned but not created or committed to)
[T3] What format should content take? — SOURCE: gap (video? blog posts? Reddit posts? Twitter threads? No format decision made)
[T4] Who is the target audience for initial content? — SOURCE: gap (no audience definition exists)
[T5] Should I keep building skills or stop and distribute? — SOURCE: conditional ("distribution is the bottleneck, not building more skills" implies a shift, but it hasn't been committed to)
[T6] What does the subreddit look like? — SOURCE: vague placeholder ("subreddit planned" with no specifics)
[T7] When do I launch the subreddit? — SOURCE: hedge (planned but no date)
[T8] What's the minimum viable content needed before launching the subreddit? — SOURCE: gap (launch requires something to launch with)
[T9] Should I improve existing skills or write content about existing skills? — SOURCE: conditional (both have been discussed; neither chosen)
[T10] How do I measure whether content is working? — SOURCE: gap (no success metrics defined)
[T11] What's my daily/weekly work allocation between building and distributing? — SOURCE: gap (no time allocation decided)
[T12] Should I pursue employment while building this? — SOURCE: gap (unemployed status mentioned without resolution of how long this is sustainable)

[T-COUNT] TBD_COUNT: 12 items found
```

---

## Phase 2: TBD Classification

```
[T1] TBD: What specific content should I create first?
  TYPE: decision
  STATUS: avoidance — 60 analyses have been run today; multiple identify content as the gate. The information exists. The decision is being deferred by doing more analysis.
  BLOCKING: All distribution. All community growth. All feedback loops. Everything downstream of "people encounter reasoningtool."
  COST_OF_DELAY: HIGH — every day without content is a day with zero distribution progress

[T2] TBD: Where should content be published?
  TYPE: decision
  STATUS: defaultable — Reddit is already planned. That's the default. Don't overthink this.
  BLOCKING: Content creation (you can't write for an audience without knowing the platform)
  COST_OF_DELAY: MEDIUM — but only because T1 blocks harder

[T3] TBD: What format should content take?
  TYPE: decision
  STATUS: avoidance — for a solo dev posting to Reddit, the format is text posts. This is knowable now.
  BLOCKING: Content creation velocity
  COST_OF_DELAY: MEDIUM

[T4] TBD: Who is the target audience for initial content?
  TYPE: decision
  STATUS: avoidance — you know who uses Claude Code. This is decidable today.
  BLOCKING: Content relevance and positioning
  COST_OF_DELAY: HIGH — wrong audience = wasted content effort

[T5] TBD: Should I keep building skills or stop and distribute?
  TYPE: scope
  STATUS: avoidance — this has been answered by your own analyses multiple times today. Distribution is the bottleneck. The answer is: shift to distribution. The continued analysis IS the avoidance.
  BLOCKING: The entire strategic pivot from building to distributing
  COST_OF_DELAY: HIGH — this is the meta-decision that unlocks everything

[T6] TBD: What does the subreddit look like?
  TYPE: design
  STATUS: legitimately premature — but barely. You could design this in 30 minutes.
  BLOCKING: Subreddit launch
  COST_OF_DELAY: LOW (subreddit design is fast once decided)

[T7] TBD: When do I launch the subreddit?
  TYPE: decision
  STATUS: avoidance — "planned" without a date is a way of not committing
  BLOCKING: Community formation
  COST_OF_DELAY: MEDIUM

[T8] TBD: What's the minimum viable content needed before launching the subreddit?
  TYPE: scope
  STATUS: avoidance — the answer is probably "3-5 posts ready to go" but this hasn't been made explicit, and it risks becoming a reason to delay further
  BLOCKING: Subreddit launch timing
  COST_OF_DELAY: MEDIUM — risk of perpetual "not ready yet"

[T9] TBD: Should I improve existing skills or write content about existing skills?
  TYPE: decision
  STATUS: avoidance — 592 skills is enough to demonstrate value. Improving skills is comfortable; writing about them is uncomfortable. That's the signal.
  BLOCKING: Content creation start date
  COST_OF_DELAY: HIGH — this is T5 wearing a different hat

[T10] TBD: How do I measure whether content is working?
  TYPE: information
  STATUS: legitimately premature — you need content out in the world before you can measure it. But you should define metrics before publishing, not after.
  BLOCKING: Ability to iterate on content strategy
  COST_OF_DELAY: LOW now, HIGH after first content goes live

[T11] TBD: What's my daily/weekly work allocation between building and distributing?
  TYPE: resource
  STATUS: avoidance — this is uncomfortable because it means formally committing to spend time on the scary thing (distribution) instead of the comfortable thing (building)
  BLOCKING: Daily work focus and progress
  COST_OF_DELAY: HIGH — without this, every day starts with "what should I work on today?"

[T12] TBD: Should I pursue employment while building this?
  TYPE: resource
  STATUS: legitimately premature — depends on runway, personal circumstances. But it affects everything because it determines available time.
  BLOCKING: Available hours per week for reasoningtool
  COST_OF_DELAY: depends on financial runway (unknown to this analysis)
```

---

## Phase 3: Resolution Specification

```
[T1] DETERMINATION QUESTION: What is the first piece of content I will create and publish?
  DECISION_TYPE: selection (pick from options)
  OPTIONS:
    a) Reddit post: "I built 592 thinking skills for Claude Code — here's what happened"
    b) Reddit post: "How I use AI to think better, not just faster"
    c) Demo video: walking through 3 skills on a real problem
    d) Blog post on website: tutorial for one category skill
    e) A "Show HN" post with a focused use case
  INFORMATION_NEEDED: None — this is a preference and positioning decision
  OWNER: Ben
  DEADLINE: Today, 2026-03-09
  RESOLUTION_METHOD: Pick one and write it. The first piece doesn't need to be perfect.
  DEFAULT_IF_MISSED: Another day passes with zero distribution progress

[T4] DETERMINATION QUESTION: Who am I writing for with my first 5 pieces of content?
  DECISION_TYPE: selection
  OPTIONS:
    a) Claude Code users who want to think more clearly
    b) AI power users who want structured prompting
    c) People who make decisions and feel uncertain
    d) Developers who use AI coding tools
  INFORMATION_NEEDED: None — this is a strategic choice
  OWNER: Ben
  DEADLINE: Today, 2026-03-09
  RESOLUTION_METHOD: Pick the audience you understand best and can reach soonest
  DEFAULT_IF_MISSED: Content written for nobody in particular, which reaches nobody in particular

[T5] DETERMINATION QUESTION: Am I shifting from building to distributing, starting today?
  DECISION_TYPE: binary (yes/no)
  OPTIONS: Yes or No
  INFORMATION_NEEDED: None — your own analyses have answered this repeatedly
  OWNER: Ben
  DEADLINE: Already past due
  RESOLUTION_METHOD: Commit. Say it out loud. Change the default daily action.
  DEFAULT_IF_MISSED: Skill count goes to 600, 650, 700 while user count stays at 0

[T7] DETERMINATION QUESTION: When will the subreddit go live?
  DECISION_TYPE: value (pick a date)
  OPTIONS: This week / Next week / When N posts are ready
  INFORMATION_NEEDED: Decision on T8 (minimum viable content)
  OWNER: Ben
  DEADLINE: 2026-03-10 (decide the date tomorrow at latest)
  RESOLUTION_METHOD: Pick a date, work backward from it
  DEFAULT_IF_MISSED: "Planned" indefinitely

[T8] DETERMINATION QUESTION: How many posts do I need ready before launching the subreddit?
  DECISION_TYPE: value
  OPTIONS: 1 / 3 / 5 / 10
  INFORMATION_NEEDED: None
  OWNER: Ben
  DEADLINE: 2026-03-09
  RESOLUTION_METHOD: Default to 3. That's enough to show the subreddit isn't empty.
  DEFAULT_IF_MISSED: Perfectionism delays launch

[T11] DETERMINATION QUESTION: What percentage of my work time goes to distribution vs. building, starting this week?
  DECISION_TYPE: value
  OPTIONS: 50/50 / 70-distribute/30-build / 80/20 / 100% distribute for 2 weeks
  INFORMATION_NEEDED: None
  OWNER: Ben
  DEADLINE: 2026-03-09
  RESOLUTION_METHOD: Set a ratio and enforce it for one week. Adjust after.
  DEFAULT_IF_MISSED: Building continues to consume 100% by default because it's comfortable
```

---

## Phase 4: Output

```
TBD INVENTORY
=============

SOURCE: "What should I work on today?" + context from 60 prior analyses
TOTAL TBDs: 12

RESOLVE NOW (avoidance — information exists):

  1. [T5] Am I shifting from building to distributing?
     QUESTION: Am I committing to distribution as the primary activity, starting today?
     BLOCKING: Everything downstream — content, community, feedback, growth
     OWNER: Ben — DEADLINE: 2026-03-09 (today)
     NOTE: This has been answered by your own analyses. The avoidance is the
     continued analysis instead of commitment. 60 analyses in one day IS the
     avoidance behavior. Resolve by stopping analysis and starting output.

  2. [T1] What specific content should I create first?
     QUESTION: What is the first piece of content I will write and publish?
     BLOCKING: All distribution progress
     OWNER: Ben — DEADLINE: 2026-03-09 (today)
     RECOMMENDED DEFAULT: A Reddit post sharing the project and demonstrating
     2-3 skills on real problems. Write it today.

  3. [T4] Who is the target audience?
     QUESTION: Who am I writing for in my first 5 pieces of content?
     BLOCKING: Content relevance
     OWNER: Ben — DEADLINE: 2026-03-09 (today)
     RECOMMENDED DEFAULT: Claude Code users who want better thinking, not just
     faster coding. This is the most reachable audience.

  4. [T11] What's the build/distribute time split?
     QUESTION: What % of my time goes to distribution this week?
     BLOCKING: Daily focus
     OWNER: Ben — DEADLINE: 2026-03-09 (today)
     RECOMMENDED DEFAULT: 80% distribute, 20% build for the next 2 weeks.

  5. [T9] Improve skills vs. write about skills?
     QUESTION: Is today's work about making skills better or telling people they exist?
     BLOCKING: Content start date
     OWNER: Ben — DEADLINE: 2026-03-09 (today)
     NOTE: This is T5 in disguise. Writing about existing skills IS the work now.

DEFAULT (obvious answer exists):

  6. [T2] Where to publish? — DEFAULT: Reddit (already planned, lowest friction)
     RATIONALE: Subreddit planned, Reddit has discoverable communities,
     text-native format matches the product
     REVISIT_IF: Reddit communities prove unreceptive after 10+ posts

  7. [T3] What format? — DEFAULT: Text posts with embedded skill demonstrations
     RATIONALE: Solo dev, no video production skill needed, plays to writing strength
     REVISIT_IF: Engagement is low and video content gets suggested by feedback

  8. [T8] Minimum content before subreddit launch?
     DEFAULT: 3 posts ready to publish
     RATIONALE: Enough to show the subreddit isn't dead; few enough to launch this week
     REVISIT_IF: Subreddit gets traffic before you're "ready" (good problem)

RESOLVE SOON (legitimate — not yet answerable):

  9. [T7] When does the subreddit launch?
     QUESTION: What's the launch date?
     TRIGGERS_RESOLUTION: Completion of 3 posts (from T8 default)
     OWNER: Ben — DEADLINE: Decide by 2026-03-10; launch by 2026-03-14

  10. [T10] How to measure content success?
      QUESTION: What metrics indicate content is working?
      TRIGGERS_RESOLUTION: First content published (need something to measure)
      OWNER: Ben — DEADLINE: 2026-03-14 (define before second week of content)

  11. [T6] Subreddit design
      QUESTION: What's the subreddit description, rules, sidebar?
      TRIGGERS_RESOLUTION: Launch date set (from T7)
      OWNER: Ben — DEADLINE: Day before launch

KILL (irrelevant to today's question):

  12. [T12] Should I pursue employment?
      WHY_IRRELEVANT: This is important but not today's decision. It's a separate
      strategic question that should not block today's work. Park it.
      NOTE: If financial pressure is urgent, address separately via /decide.
```

---

## The Meta-Observation

This /tbd analysis reveals something significant: **the biggest TBD is not an information gap — it's a commitment gap.** You have 60 analyses from today alone. The information is abundant. The unresolved items are almost all classified as "avoidance," not "legitimately premature."

The pattern: when the work shifts from comfortable (building, analyzing) to uncomfortable (publishing, being judged, possibly being ignored), the response is to run another analysis. Today's 60 analyses are themselves the avoidance behavior that this TBD inventory surfaces.

**What to work on today has been answered by your own prior work. The TBD is not "what" — it's "will I."**

---

## Today's Resolved TBD List (Recommended Commitments)

| # | Decision | Resolution | Status |
|---|----------|-----------|--------|
| T5 | Shift to distribution? | **Yes, starting now** | Commit |
| T11 | Time split? | **80% distribute / 20% build** | Commit |
| T1 | First content? | **Write a Reddit post today** | Do it |
| T4 | Audience? | **Claude Code users who want better thinking** | Commit |
| T9 | Improve or write about? | **Write about existing skills** | Commit |
| T2 | Where? | **Reddit** | Default |
| T3 | Format? | **Text posts with demos** | Default |
| T8 | Posts before launch? | **3** | Default |
| T7 | Subreddit launch? | **By 2026-03-14** | Decide tomorrow |
| T10 | Success metrics? | **Define by 2026-03-14** | After first post |
| T6 | Subreddit design? | **Day before launch** | After date set |
| T12 | Employment? | **Parked — separate decision** | Kill for today |

---

## Pre-Completion Checklist

- [x] All TBD signals scanned (explicit markers, questions, hedges, gaps, conditionals, missing sections)
- [x] Each TBD classified by type and status
- [x] Avoidance vs legitimate premature distinguished (8 avoidance/defaultable, 3 legitimate, 1 killed)
- [x] Defaultable and killable TBDs identified (3 defaultable, 1 killable)
- [x] Every resolve-worthy TBD has a specific question
- [x] Every TBD has an owner (Ben) and deadline
- [x] Blocking downstream work identified for each TBD
- [x] Cost of delay assessed

---

**READY FOR:**
- `/tobd` — to sequence today's commitments into an actionable task order
- `/decide` on T5 — to formally commit to the distribution pivot (though the answer is clear)
- Write the first Reddit post — which is the actual work that resolves T1, T2, T3, T4, and T9 simultaneously

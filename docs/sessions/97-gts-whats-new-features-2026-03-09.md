# /gts Generate 20 possible "what's new" features for the website, then search for the 3 that would matter most
**Date:** 2026-03-09
**Skill:** /gts (Generate Then Search)

---

## Step 1: Identify the Task

**Task type:** Planning — Generate possible features, search for optimal ones given constraints.

The cognitive task: generate a comprehensive space of "what's new" page features for the Reasoning Toolkit website, then select the 3 that would most increase engagement and demonstrate value.

**Context:** The website currently has: index (skill browser with tiers, tags, filtering, sorting), skill viewer, visuals (graph + ARAW viewer), FAQ, installation, about, questions, and a where-am-i page. The "what's new" page currently just redirects to where-am-i. There are 563 skills total.

---

## Step 2: GENERATE — Create the Possibility Space

Generation methods used: systematic enumeration (by user need), cross-domain analogy (from changelogs, dashboards, product pages), inversion (what would make someone NOT come back?).

Constraint pre-filter: Excluded features requiring a backend/database (no user accounts exist), excluded features requiring real-time collaboration, excluded anything needing usage analytics infrastructure that doesn't exist.

### The 20 Features

1. **Skill-of-the-Day spotlight** — Feature one skill daily with a short example of it in action, rotating through the catalog.

2. **Recently added skills timeline** — Chronological list of skills added in the last 30/60/90 days, pulled from git history or a manifest.

3. **Changelog with diffs** — Show what changed in existing skills (improved, expanded, restructured) not just what was added.

4. **"Try this skill" interactive demo** — Embedded mini-demo where you can type a problem and see a skill applied to it, right on the what's-new page.

5. **Skill count ticker** — Live count showing total skills, skills added this week/month, categories covered. A growing-numbers dashboard.

6. **Version history with named releases** — Group changes into named releases (e.g., "v2.4 — The Uncertainty Update: 15 new skills for handling unknowns").

7. **Before/after examples** — Show "thinking without this skill" vs. "thinking with this skill" for recently added or improved skills.

8. **Curated skill bundles announcement** — "New this week: a 5-skill workflow for product decisions" — group related skills into announced packages.

9. **Community requests tracker** — Show which skills were requested by users and which have been built, creating a feedback loop.

10. **RSS/Atom feed** — Machine-readable feed of updates so people can subscribe in their feed reader.

11. **Email digest signup** — Weekly or monthly email summarizing what's new, with a sign-up form on the page.

12. **Skill improvement log** — Track when existing skills get meaningfully better (not just new skills, but quality improvements to old ones).

13. **Roadmap preview** — "Coming soon" section showing skills or features currently in development, creating anticipation.

14. **Skill relationship announcements** — "Skill X now chains into Skill Y" — highlight new connections in the skill graph.

15. **Usage pattern insights** — "Most popular skill paths this month" or "Skills people use together" (would need analytics).

16. **Category completion tracker** — Visual progress bars showing how complete each thinking category is (e.g., "Decision-making: 45 skills, 92% of planned coverage").

17. **Skill quality upgrades badge system** — Mark skills that have been significantly improved with a visible badge, incentivizing revisits.

18. **Comparative update notes** — "If you liked /rca, check out the new /rci — here's how they differ" — relate new skills to ones users already know.

19. **Interactive "what changed" diff viewer** — Side-by-side view of old vs. new skill text for updated skills.

20. **Seasonal/thematic collections** — "Spring cleaning your thinking: 5 skills for clearing out bad assumptions" — themed groupings timed to events or seasons.

```
GENERATED SPACE:
Options: 20
Generation methods used: systematic enumeration, cross-domain analogy (product changelogs, SaaS dashboards, open-source release pages), inversion
Constraint pre-filter: Excluded backend-dependent features (user accounts, analytics dashboards), real-time features
Completeness: Confident for a static site context; gaps possible in: social/multiplayer features, AI-powered personalization
```

---

## Step 3: DEFINE CRITERIA — Set Search Parameters

### Must-have criteria (non-negotiable):

- **Implementable without a backend** — The site is static (Astro). Feature must work with build-time data or client-side JS only.
- **Demonstrates value to a first-time visitor** — Someone landing on this page should understand why the toolkit matters, not just see a list of changes.
- **Maintainable by a solo developer** — Cannot require daily manual curation effort that scales with skill count.

### Ranked criteria (in order of importance):

| Criterion | Weight | How measured |
|-----------|--------|-------------|
| Engagement pull — gives a reason to return | 10 | Does it create a "check back" habit or curiosity loop? |
| Value demonstration — shows skills working | 9 | Does a visitor see evidence that these skills produce better thinking? |
| Low maintenance burden | 8 | Can it be automated or semi-automated at build time? |
| Discovery aid — helps users find relevant skills | 7 | Does it surface skills the user wouldn't have found otherwise? |
| Implementation effort — can ship in 1-2 days | 5 | Rough complexity estimate |

### Anti-criteria (things to avoid):

- **Vanity metrics** — Showing "563 skills!" without demonstrating quality is counterproductive. Avoid ticker-for-ticker's-sake.
- **Manual curation treadmill** — Features that go stale if you skip a week destroy trust.
- **Requires external services** — No Mailchimp, no analytics platforms, no databases.

**Criteria quality check:**
- Independent? Yes — engagement, value demonstration, maintenance, discovery, and effort measure different things.
- Measurable? Yes — each has a concrete test.
- Ranked? Yes — engagement and value demonstration top the list.
- Reflect actual wants? Yes — the goal is engagement and demonstrating value, not feature count.

---

## Step 4: SEARCH — Apply Criteria to Space

### Round 1 — Must-have filter

| # | Feature | Static-site OK? | Shows value to newcomer? | Solo-dev maintainable? | Pass? |
|---|---------|-----------------|--------------------------|------------------------|-------|
| 1 | Skill-of-the-Day | Yes (deterministic from date) | Partially — depends on example quality | Medium — needs curated examples | PASS |
| 2 | Recently added timeline | Yes (from git/manifest) | Weak — just a list | Yes — automated | PASS |
| 3 | Changelog with diffs | Yes (build-time) | Weak — inside baseball | Yes — automated | PASS |
| 4 | Interactive demo | Yes (client-side) | Strong — shows skill in action | Medium — needs good default | PASS |
| 5 | Skill count ticker | Yes | Weak — vanity metric | Yes | PASS (borderline anti-criteria) |
| 6 | Named releases | Yes | Medium — narrative helps | Medium — requires writing | PASS |
| 7 | Before/after examples | Yes | Strong — concrete proof | Low — needs manual creation | PASS |
| 8 | Curated bundles | Yes | Strong — shows workflows | Medium — manual curation | PASS |
| 9 | Community requests | Needs backend | N/A | N/A | FAIL |
| 10 | RSS feed | Yes | Weak for newcomers | Yes — automated | PASS |
| 11 | Email digest | Needs external service | N/A | N/A | FAIL |
| 12 | Skill improvement log | Yes (build-time) | Weak — assumes familiarity | Yes — automated | PASS |
| 13 | Roadmap preview | Yes (static content) | Medium — shows momentum | Low-medium | PASS |
| 14 | Relationship announcements | Yes (from graph data) | Medium — shows depth | Yes — semi-automated | PASS |
| 15 | Usage pattern insights | Needs analytics | N/A | N/A | FAIL |
| 16 | Category completion tracker | Yes (build-time) | Medium — shows scope | Yes — automated | PASS |
| 17 | Quality upgrade badges | Yes | Weak for newcomers | Yes | PASS |
| 18 | Comparative update notes | Yes | Strong — relates new to known | Medium — needs writing | PASS |
| 19 | Interactive diff viewer | Yes (client-side) | Weak — assumes prior knowledge | Yes — automated | PASS |
| 20 | Seasonal collections | Yes | Strong — thematic entry point | Low — manual, time-sensitive | PASS |

**Remaining: 17 of 20** (eliminated #9, #11, #15)

### Round 2 — Ranked scoring

Scoring 1-10 on each criterion for the 17 remaining options:

| # | Feature | Engagement (×10) | Value Demo (×9) | Low Maint. (×8) | Discovery (×7) | Low Effort (×5) | **Total** |
|---|---------|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | Skill-of-the-Day | 8 (80) | 7 (63) | 5 (40) | 8 (56) | 6 (30) | **269** |
| 2 | Recently added timeline | 4 (40) | 3 (27) | 9 (72) | 5 (35) | 9 (45) | **219** |
| 3 | Changelog with diffs | 3 (30) | 2 (18) | 8 (64) | 3 (21) | 8 (40) | **173** |
| 4 | Interactive demo | 9 (90) | 10 (90) | 5 (40) | 7 (49) | 4 (20) | **289** |
| 5 | Skill count ticker | 2 (20) | 1 (9) | 10 (80) | 1 (7) | 10 (50) | **166** |
| 6 | Named releases | 6 (60) | 6 (54) | 4 (32) | 5 (35) | 5 (25) | **206** |
| 7 | Before/after examples | 7 (70) | 10 (90) | 3 (24) | 6 (42) | 4 (20) | **246** |
| 8 | Curated bundles | 7 (70) | 8 (72) | 4 (32) | 9 (63) | 5 (25) | **262** |
| 10 | RSS feed | 5 (50) | 1 (9) | 10 (80) | 1 (7) | 8 (40) | **186** |
| 12 | Skill improvement log | 3 (30) | 3 (27) | 8 (64) | 4 (28) | 7 (35) | **184** |
| 13 | Roadmap preview | 5 (50) | 4 (36) | 6 (48) | 4 (28) | 7 (35) | **197** |
| 14 | Relationship announcements | 5 (50) | 5 (45) | 6 (48) | 7 (49) | 6 (30) | **222** |
| 16 | Category completion | 4 (40) | 5 (45) | 8 (64) | 5 (35) | 7 (35) | **219** |
| 17 | Quality badges | 3 (30) | 3 (27) | 8 (64) | 3 (21) | 8 (40) | **182** |
| 18 | Comparative notes | 6 (60) | 7 (63) | 4 (32) | 8 (56) | 5 (25) | **236** |
| 19 | Interactive diff | 3 (30) | 2 (18) | 7 (56) | 2 (14) | 6 (30) | **148** |
| 20 | Seasonal collections | 6 (60) | 7 (63) | 3 (24) | 8 (56) | 4 (20) | **223** |

### Round 3 — Top 5 candidates

| Rank | Feature | Score |
|------|---------|-------|
| 1 | **#4 Interactive demo** | 289 |
| 2 | **#1 Skill-of-the-Day** | 269 |
| 3 | **#8 Curated bundles** | 262 |
| 4 | **#7 Before/after examples** | 246 |
| 5 | **#18 Comparative notes** | 236 |

---

## Step 5: EVALUATE — Deep-Dive Top 5

### #4 Interactive "Try This Skill" Demo (Score: 289)

**What it is:** A text input on the what's-new page where visitors type a problem and see a featured skill's structure applied to it. Not AI-powered — it could be a pre-built example that unfolds step by step, or a template that fills in with the user's input.

**Risks:**
- Building a genuinely good demo is harder than it sounds. A bad demo is worse than no demo.
- Client-side only means no AI generation — would need to be a structured walkthrough or pre-scripted examples.
- Could set expectations the website can't meet (people expect the site to run skills, but skills run in Claude).

**Assumptions:**
- A static walkthrough is compelling enough to demonstrate value.
- Users will engage with an interactive element rather than just scanning.

**Execution:** Build 3-5 pre-scripted skill demonstrations as expandable sections. User clicks "See /rca in action" and a step-by-step walkthrough unfolds with a real example. Could use a tabbed interface with different example problems.

**Critic's view:** "This is a lot of effort for something that will always feel like a toy compared to actually using the skill in Claude. You're building a demo of a demo."

### #1 Skill-of-the-Day Spotlight (Score: 269)

**What it is:** Each day, deterministically feature one skill with its name, one-sentence description, a concrete example of when you'd use it, and a link to the full skill. Deterministic = seeded from date, no manual work.

**Risks:**
- Without a curated example per skill, the "spotlight" is just a repackaged skill listing.
- 563 skills means 1.5 years before rotation. Some skills are much more useful than others.
- "Of the day" implies freshness but the page is static — only changes on rebuild.

**Assumptions:**
- Build happens frequently enough that the daily rotation actually works.
- Skill descriptions are compelling enough standalone.

**Execution:** At build time, pick a skill based on day-of-year (weighted toward higher tiers). Show its description, the category it belongs to, and one example prompt. Trivial to automate — just needs a good template.

**Critic's view:** "Skill-of-the-day is a solved pattern from 2005. It works, but it's not exciting. The value depends entirely on example quality."

### #8 Curated Skill Bundles (Score: 262)

**What it is:** Announce themed groups of skills as workflows. "New: The Decision Stack — 5 skills that chain together for high-stakes choices: /gu → /se → /cba → /dcp → /ins." Shows skills as composable, not isolated.

**Risks:**
- Requires manual curation — someone has to design and write up each bundle.
- Could go stale if not updated.
- Might confuse newcomers who don't yet understand individual skills.

**Assumptions:**
- Bundles are more compelling than individual skills.
- Users will understand skill chaining without prior experience.

**Execution:** Create 5-8 bundles as static content. Each has: a name, the problem it solves, the skill sequence, and a one-paragraph narrative of how it flows. Update quarterly.

**Critic's view:** "This is high value but high maintenance. The first set will be great. The question is whether you maintain it."

### #7 Before/After Examples (Score: 246)

**What it is:** Side-by-side showing "How most people approach X" vs. "How /skill approaches X" with concrete text. The most direct value demonstration possible.

**Risks:**
- Very labor-intensive to write well. Bad before/after examples feel like infomercials.
- Selecting the right examples is critical — boring problems won't convince anyone.

**Assumptions:**
- The difference between "without skill" and "with skill" is visually obvious.
- Examples can be short enough for a glance but compelling enough to convince.

**Execution:** Write 3-5 before/after pairs for the highest-impact skills. Each pair: a real-world problem, a "typical" approach (vague, missing steps), and the skill's structured approach (specific, methodical). Visual treatment with two columns.

**Critic's view:** "This is the most persuasive option but also the hardest to execute. One bad example undermines all the good ones."

### #18 Comparative Update Notes (Score: 236)

**What it is:** When new skills are added, explain them in terms of skills the user might already know. "If you've used /rca, the new /rci goes deeper — here's when to use each."

**Risks:**
- Assumes the user already knows some skills (bad for newcomers).
- Writing good comparisons requires deep knowledge of each skill.

**Execution:** For each new skill, write a 2-sentence comparison to the most similar existing skill. Semi-automatable from skill metadata.

**Critic's view:** "Good for power users, invisible to newcomers. The target audience for a what's-new page is probably return visitors, so this might actually be well-targeted."

---

## Step 6: SELECT — The Top 3

The scores and evaluations point to a clear tiering:

**Tier A — Implement these:**
1. **#4 Interactive demo** (289) — Highest score, strongest value demonstration. But the critic is right: scope it down. Don't build a full interactive tool. Build **3-5 pre-scripted skill walkthroughs** that unfold step-by-step. This is the thing that converts a curious visitor into an installer.

2. **#8 Curated skill bundles** (262) — The second-strongest value demonstration and the best discovery aid. Shows skills are composable, not just a list. This is the thing that makes a new user think "oh, there's depth here." Start with 5 bundles, accept that it's manual, update quarterly.

3. **#1 Skill-of-the-Day spotlight** (269) — Scores second-highest overall, and crucially: it's nearly fully automatable at build time. It creates a reason to return, it surfaces skills users wouldn't find themselves, and it requires almost zero ongoing maintenance. The engagement-to-effort ratio is the best of any option.

**Why not #7 (Before/After)?** It scored 246 and is the most *persuasive* option, but it has the worst maintenance-to-value ratio. Writing genuinely good before/after examples is a significant creative task per skill. The interactive demo (a structured walkthrough) achieves a similar effect with a more sustainable format — the skill structure IS the "after," and the walkthrough makes it visible.

**Why not #18 (Comparative notes)?** It's well-targeted for return visitors, but it fails the "demonstrates value to first-time visitors" criterion that matters most for a what's-new page. It's a good *addition* to bundle announcements, not a standalone feature.

---

## Step 7: Report

```
GENERATE-THEN-SEARCH:
Task: Select 3 features for the website's "what's new" page that maximize engagement and value demonstration

Generation:
- Options generated: 20
- Methods: Systematic enumeration (by user need), cross-domain analogy (SaaS changelogs, open-source release pages), inversion
- Constraints: Must work on static site (no backend), must be solo-dev maintainable

Search criteria:
- Must-have: Static-site implementable, demonstrates value to newcomers, solo-dev maintainable
- Ranked: Engagement pull (×10), Value demonstration (×9), Low maintenance (×8), Discovery aid (×7), Low effort (×5)

Results:
- Passed must-have: 17 of 20
- Top 3:
  1. Interactive skill walkthroughs — score: 289 — key strength: highest value demonstration, shows skills actually working
  2. Curated skill bundles — score: 262 — key strength: best discovery aid, shows composability and depth
  3. Skill-of-the-Day spotlight — score: 269 — key strength: best engagement-to-effort ratio, fully automatable

Selected: All three (they complement each other)
Rationale: Together they cover three distinct needs — walkthroughs convert new visitors (value demo), bundles show depth (discovery), and skill-of-the-day creates return visits (engagement). They also tier by effort: skill-of-the-day ships in hours, bundles in a day, walkthroughs in 1-2 days.

Key risk: The interactive walkthroughs risk feeling like a pale imitation of actually using the skills in Claude. Scope them as "see the structure" not "use the tool" — the goal is to show that skills produce systematic, step-by-step thinking, not to replicate the full experience.
```

---

## Implementation Priority

| Order | Feature | Effort | Why this order |
|-------|---------|--------|----------------|
| 1st | Skill-of-the-Day | ~2-4 hours | Quick win. Deterministic date-based selection at build time. Immediately makes what's-new feel alive. |
| 2nd | Curated skill bundles | ~1 day | Write 5 workflow bundles. Static content, highest discovery value. Shows the toolkit is more than a list. |
| 3rd | Interactive walkthroughs | ~1-2 days | The hardest and highest-impact. Build 3-5 expandable step-by-step demonstrations for flagship skills (/rca, /dcp, /se, /aex, /ht). |

All three together transform what's-new from a redirect into the page that answers "why should I care about this toolkit?"

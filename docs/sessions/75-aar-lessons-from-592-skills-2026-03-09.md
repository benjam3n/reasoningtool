# /aar After-action review: what have I learned from building the first 592 skills?
**Date:** 2026-03-09
**Skill:** /aar (After Action Review)

---

## Step 1: Context

**Event:** Building the Reasoning Toolkit — 592 structured thinking skills for Claude Code, from initial release to current state.

**Timeframe:** January 28, 2026 (first commit: 207 skills) to March 9, 2026 (~40 days).

**Who:** Ben, solo developer. No team, no users yet.

**Ground rules applied:** No blame (solo anyway), honesty mandatory (no one to perform for), specifics not generalities.

---

## Step 2: What Was Supposed to Happen?

**Objective:** Create a library of structured thinking procedures that make AI reasoning better — procedures people can invoke to get consistently higher-quality analysis than "just asking."

**Plan (reconstructed):**
1. Build an initial set of thinking skills covering major reasoning categories
2. Release them as a Claude Code plugin
3. Build a website for discovery and documentation
4. Grow to a critical mass of skills covering the full thinking landscape
5. Attract users through Reddit and organic discovery
6. Validate that the skills actually help people think better

**Key milestones:**
- Initial release with ~200 skills
- Website launch
- Subreddit creation
- First external users
- Feedback-driven iteration

**Expected timeline:** Unclear — this was exploratory. But implicitly: ship fast, get users, iterate.

**Success criteria:**
- Skills that demonstrably improve reasoning quality
- Users who adopt and return
- Evidence that proceduralized thinking > ad hoc prompting

---

## Step 3: What Actually Happened?

**Chronological walkthrough:**

1. **Jan 28:** Initial release with 207 skills. Strong conceptual foundation — ARAW (Analyze-Reason-Assess-Weigh), UAUA (Understand-Analyze-Understand-Act), category routers, tiered organization. Apache 2.0 license.

2. **Jan 28 – Feb mid:** Rapid skill expansion. Added essays on mathematical problem-solving and search theory. Refined README. Relicensed. The core architecture solidified: skills as markdown procedures that chain into each other.

3. **Feb mid – late Feb:** Built website with Astro. Skills page, installation guide, FAQ, questions page (1000+ questions), graph visualization. Significant UI iteration — dozens of commits on mobile pager alone (square buttons, coordinate mismatches, footer boundaries, chip styling, fixed vs auto-fit).

4. **Late Feb – early March:** Continued skill explosion: 207 → 402 → 540 → 564 → 592. Added tag system (17 meta-categories, 336 tags), tier/category filters, session persistence, interpretations for skills. Added shortcut skills, corruption pre-inoculation, skill-discovery skills.

5. **March 9 (today):** 592 skills, 237 commits, full website, no external users. Running a comprehensive self-evaluation session (60+ prompts using own skills on own project).

**Decisions made and why:**
- Chose breadth over depth — covered the full thinking landscape rather than perfecting 20 skills
- Chose Claude Code as platform — it reads local files, supports `/command` invocation natively
- Chose markdown — simple, readable, no runtime dependencies
- Built website before having users — wanted a polished first impression
- Kept building skills instead of marketing — the builder's comfort zone

**Where reality diverged from plan:**
- Massively overbuilt on skills (592 vs. "enough to be useful" which might be 30-50)
- Massively underbuilt on distribution (0 users)
- Website iteration consumed significant time on cosmetic details (mobile pager alone: ~15 commits)
- No validation cycle has occurred — zero evidence that skills help anyone besides Ben

---

## Step 4: Why Was There a Difference?

| Divergence | Expected | Actual | Root Cause |
|-----------|----------|--------|-----------|
| Skill count | ~100-200 well-crafted skills | 592 of varying quality | Building is rewarding and low-risk; shipping is scary and high-risk. Path of least resistance. |
| User count | Some early adopters by now | Zero | Never prioritized distribution. No launch post. No outreach. No one knows this exists. |
| Quality consistency | Uniformly high | Ranges from flagship to stub | Breadth goal incentivized "cover the space" over "nail each one." Tier system acknowledged this but didn't prevent it. |
| Time allocation | Build → ship → iterate with users | Build → build → build → polish → build | Classic builder's trap: the product feels incomplete so you keep adding before showing anyone. |
| Website polish | Functional and clean | Over-iterated on mobile pager, under-iterated on content | Easier to fix CSS than to write compelling copy explaining why someone should care. |
| Validation | Test with real users | Self-evaluation only (today's session) | Solo developer without forcing function. No one asking "when do we ship?" |

**Assumptions that proved wrong:**
- "More skills = more value." Actually, more skills = more overwhelming. The discovery problem grows faster than the coverage benefit.
- "The website will attract users." Websites don't attract anyone. Distribution attracts users. The website is a landing pad, not a growth engine.
- "Quality will be uniform if I use a consistent format." Format consistency ≠ content quality. A well-structured mediocre skill is still mediocre.

**Positive surprises:**
- The category router architecture (claim → /claim → ARAW → specific skills) is genuinely elegant. It solves the "which of 592 skills do I use?" problem.
- Skills chaining into skills creates emergent analytical depth that individual skills lack.
- The self-evaluation session today is itself evidence the skills work — using /aar, /gu, /rca, /ht etc. on the project itself is productive.
- Markdown-as-procedure is a surprisingly powerful format. No runtime, no dependencies, works in any LLM context.

---

## Step 5: What Did We Learn?

### Sustains (keep doing)

1. **Markdown procedure format** — WHY it works: zero dependencies, readable by humans and LLMs, version-controllable, portable across any system that reads text. HOW to replicate: keep skills as self-contained .md files with clear step-by-step structure.

2. **Category router architecture** — WHY it works: users don't need to know 592 skill names, they describe their situation and get routed. HOW to replicate: maintain the 17 entry-point routers as the primary interface; keep direct skill access for power users.

3. **Skill chaining via INVOKE** — WHY it works: complex analysis emerges from composing simple procedures. A diagnostic skill can invoke a root cause skill which invokes a hypothesis test. HOW to replicate: keep the `→ INVOKE:` convention and design skills to be composable.

4. **Tiered quality system** — WHY it works: explicitly acknowledging that not all skills are equal lets you prioritize improvement without pretending everything is flagship. HOW to replicate: maintain tier 1/2/3 distinctions and systematically upgrade.

5. **Using your own tools on yourself** — WHY it works: today's 60+ prompt session found real issues and generated real insights. Dogfooding at depth. HOW to replicate: do this regularly, not just once.

### Improves (do differently)

1. **592 skills before 1 user** — WHY it didn't work: you cannot validate value without external validation. Self-assessment has a ceiling. WHAT to do instead: should have shipped at 50 skills, gotten 5 users, and let their usage patterns guide the next 50.

2. **Polishing before distributing** — WHY it didn't work: 15 commits on a mobile pager that no one has seen. The website is for people. No people means the website is for you, and you don't need it. WHAT to do instead: ship the minimum viable website, post to Reddit, iterate based on what confuses actual visitors.

3. **Breadth over depth on skills** — WHY it didn't work: a user who tries one skill and finds it mediocre won't try a second. The first skill they encounter IS the product. WHAT to do instead: 30 excellent skills beat 592 uneven ones. The tier-1 skills should be exceptional; tier-3 skills should either be upgraded or hidden.

4. **No usage analytics or feedback mechanism** — WHY it didn't work: even if users existed, there's no way to know which skills they use, which they abandon, or which confuse them. WHAT to do instead: build a minimal feedback loop before scaling. Even "was this helpful? y/n" at the end of each skill would be transformative.

5. **Treating skill creation as the product** — WHY it didn't work: the product is not "592 markdown files." The product is "I thought better about X because I used this." The files are the delivery mechanism. WHAT to do instead: define the product as the user outcome, and measure skill quality by outcome quality.

6. **Solo development without external accountability** — WHY it didn't work: no one to say "stop building, start shipping." No one to say "this skill is confusing." Builder's bias goes unchecked. WHAT to do instead: find 3-5 beta testers. Their confusion is more valuable than 100 more skills.

---

## Step 6: What Will We Do Differently?

| Lesson | Action | Owner | When | How We'll Know It's Working |
|--------|--------|-------|------|---------------------------|
| 0 users after 40 days | Write and post the Reddit introduction | Ben | This week (by March 14) | Post is live and has >0 comments |
| Quality unevenness | Audit all tier-1 skills for flagship quality; hide or demote any that fall short | Ben | Before Reddit post | Every tier-1 skill passes the "would I show this to a skeptic?" test |
| No feedback loop | Add a "was this useful?" prompt to skill output format | Ben | By March 14 | Mechanism exists even if no one uses it yet |
| Over-building tendency | Set a rule: no new skills until 10 external users have been acquired | Ben | Immediately | Skill count stays at 592 until user threshold met |
| No usage data | Add minimal analytics to website (which pages, which skills viewed) | Ben | By March 21 | Can answer "what do visitors look at?" |
| Untested value proposition | Send the toolkit to 5 specific people and ask them to try it on a real problem | Ben | By March 14 | 5 people have received it and at least 2 have tried it |
| Website polish over substance | Freeze website cosmetics; only change content and UX based on user feedback | Ben | Immediately | Zero CSS commits until a user reports a problem |

---

## Step 7: Report

```
AFTER ACTION REVIEW:
Event: Building Reasoning Toolkit (592 thinking skills for Claude Code)
Date of event: January 28 – March 9, 2026 (40 days)
Date of AAR: March 9, 2026

PLANNED vs ACTUAL:
| Aspect | Planned | Actual | Divergence |
|--------|---------|--------|-----------|
| Skills built | ~100-200 solid skills | 592 of mixed quality | 3x over on quantity, under on quality |
| Users acquired | Some early adopters | Zero | Total miss on distribution |
| Time allocation | Build-ship-iterate | Build-build-build-polish | Never reached the ship/iterate phases |
| Quality | Uniformly high | Tier 1 (excellent) to Tier 3 (stub) | Breadth goal undermined depth |
| Validation | External user testing | Self-assessment only | No external signal on value |
| Website | Functional landing pad | Over-polished, unseen | 15+ commits on mobile pager nobody uses |

SUSTAINS (keep doing):
1. Markdown-as-procedure format — zero dependencies, portable, readable
2. Category router architecture — solves the discovery problem elegantly
3. Skill chaining via INVOKE — compositional depth from simple parts
4. Tiered quality system — honest about unevenness, guides improvement
5. Dogfooding with depth — today's session proves the tools work on themselves

IMPROVES (change):
1. Ship at 50 skills, not 592 — validate early, build on evidence
2. Distribute before polishing — the mobile pager doesn't matter until people exist
3. Depth over breadth — 30 excellent skills > 592 uneven ones
4. Build feedback loops — "was this useful?" is the minimum viable metric
5. Define product as user outcome, not file count
6. Get external accountability — 3-5 beta testers break the solo echo chamber

ACTION ITEMS:
| Action | Owner | Deadline | Measure |
|--------|-------|----------|---------|
| Post Reddit introduction | Ben | March 14 | Post live with >0 engagement |
| Audit tier-1 skills for flagship quality | Ben | March 14 | All tier-1 pass skeptic test |
| Send toolkit to 5 specific people | Ben | March 14 | 5 sent, 2+ tried |
| Freeze new skill creation until 10 users | Ben | Immediate | Skill count holds at 592 |
| Add minimal website analytics | Ben | March 21 | Can see page/skill view data |
| Freeze cosmetic CSS changes | Ben | Immediate | Zero CSS commits until user-reported issue |
| Add "was this useful?" to skill output | Ben | March 14 | Mechanism exists in skill format |

KEY INSIGHT: Building 592 skills was the easy part — and doing the easy
part for 40 days straight is exactly how solo projects die. The hard part
is showing it to someone and learning that your mental model of "what's
valuable" doesn't match theirs. Every day without users is a day your
assumptions compound unchecked. The toolkit's architecture is genuinely
good. The skills format works. The routing is elegant. None of that
matters until someone besides the builder says "this helped me think
better about something real."
```

---

## Verification

- [x] Conducted soon after the event (during the event, in fact — best possible timing)
- [x] "What was supposed to happen" documented before discussing actual
- [x] Both positive and negative divergences analyzed (5 sustains, 6 improves)
- [x] Root causes identified (builder's trap, comfort zone bias, missing forcing functions)
- [x] Lessons are specific and actionable (not "do better" but "post to Reddit by March 14")
- [x] Action items have owners and deadlines (all 7 items assigned with dates)

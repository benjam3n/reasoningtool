# /prm Imagine reasoningtool failed to get any traction after 6 months. What went wrong?
**Date:** 2026-03-09
**Skill:** /prm (Pre-Mortem)

---

## Step 1: The Plan

**Goal:** Build a reasoning toolkit of structured thinking skills (currently 592), distributed as a Claude Code plugin, with a website for discovery and a subreddit for community. Achieve meaningful user adoption within 6 months.

**Approach:** Solo developer, building both the skill library and distribution channels (Claude Code plugin, website, planned subreddit). Skills are structured markdown procedures that guide Claude through analytical frameworks.

**Timeline:** 6 months from now (March 2026 - September 2026).

**Key Assumptions:**
- People want structured thinking skills for LLMs
- Claude Code plugin is a viable distribution channel
- A solo developer can build, market, and support this simultaneously
- The website and subreddit will drive organic discovery
- 592 skills is an asset, not a liability
- Users will understand what this is and why they need it

---

## Step 2: Total Failure Scenario

**It's September 2026. Reasoningtool has failed spectacularly.**

The website gets 30 visits a month, mostly bots. The subreddit has 14 members, 11 of whom are spam accounts. The Claude Code plugin has been installed by fewer than 50 people, and daily active users hover around zero. You've burned through savings with nothing to show for it. The project feels like an elaborate personal wiki that nobody else wanted. You're staring at 592 skill files that nobody has ever used, wondering if you built the world's most detailed monument to overthinking.

---

## Step 3: Failure Causes

Working backward from total failure, here are the plausible causes organized by category:

### A. Discovery & Distribution Failures
1. **Nobody knows it exists.** No marketing, no viral moment, no word-of-mouth. The project lives in obscurity because awareness was never systematically built.
2. **Claude Code plugin is a tiny distribution channel.** Claude Code itself may have a small user base. Building for it is building for a niche within a niche.
3. **The website doesn't rank for anything.** No SEO strategy, no content marketing, no backlinks. The site is invisible to search engines.
4. **The subreddit never reaches critical mass.** A solo developer posting to their own subreddit looks like talking to an empty room.

### B. Product-Market Fit Failures
5. **People don't understand what this is.** "592 structured thinking skills" is abstract. Users can't picture what they'd do with it or why they need it.
6. **The problem it solves isn't painful enough.** People muddle through decisions and analysis without structured frameworks. The pain isn't acute enough to drive adoption.
7. **Users try it once and don't come back.** The first experience is confusing, the output doesn't feel dramatically better than just asking Claude directly, and there's no hook for retention.
8. **592 skills is overwhelming, not impressive.** Users see the list and freeze. They don't know where to start and bounce immediately.
9. **The output quality doesn't justify the friction.** Typing `/prm` and getting a structured analysis needs to be noticeably better than just asking "what could go wrong with my plan?" -- and maybe it isn't, or the difference isn't obvious.

### C. Competitive & Market Failures
10. **Anthropic or OpenAI ships something similar natively.** Built-in "thinking modes" or structured reasoning features make the plugin redundant.
11. **The market moves to agents, not skills.** People want AI that does things for them, not AI that walks them through thinking frameworks. The whole paradigm is wrong.
12. **Custom GPTs / Claude Projects already serve this niche.** People who want structured prompts already have them saved in their own systems.

### D. Execution & Solo Developer Failures
13. **Solo developer burnout.** Unemployed, building alone, no users, no feedback, no revenue. Motivation collapses by month 3.
14. **Building instead of selling.** Adding skill #593 instead of getting skill #1 in front of 100 people. The ratio of building to distributing is fatally wrong.
15. **No feedback loop.** Without users, there's no signal about what works. Development continues in a vacuum, optimizing for the wrong things.
16. **Financial pressure forces abandonment.** Unemployment means a ticking clock. A job offer arrives and the project gets shelved.

### E. User Experience Failures
17. **Installation is too hard.** The Claude Code plugin setup has too many steps, or users hit errors and give up.
18. **Skill naming is opaque.** `/prm`, `/cba`, `/dcm` -- these abbreviations mean nothing to new users. The learning curve is a wall.
19. **No onboarding path.** A new user installs and then... what? There's no guided first experience.
20. **Skills feel academic, not practical.** The frameworks feel like business school exercises rather than tools that produce actionable results.

---

## Step 4: Likelihood and Impact Assessment

| # | Failure Cause | Likelihood | Impact | Priority |
|---|---|---|---|---|
| 1 | Nobody knows it exists | **High** | **High** | **CRITICAL** |
| 5 | People don't understand what it is | **High** | **High** | **CRITICAL** |
| 14 | Building instead of selling | **High** | **High** | **CRITICAL** |
| 7 | Try once, don't return | **High** | **High** | **CRITICAL** |
| 9 | Output doesn't justify friction | **High** | **High** | **CRITICAL** |
| 13 | Solo developer burnout | **High** | **High** | **CRITICAL** |
| 6 | Problem not painful enough | **Medium** | **High** | HIGH |
| 8 | 592 skills is overwhelming | **Medium** | **High** | HIGH |
| 15 | No feedback loop | **High** | **Medium** | HIGH |
| 16 | Financial pressure | **High** | **Medium** | HIGH |
| 2 | Claude Code is a tiny channel | **Medium** | **Medium** | MEDIUM |
| 18 | Opaque skill names | **Medium** | **Medium** | MEDIUM |
| 19 | No onboarding | **Medium** | **High** | HIGH |
| 11 | Market moves to agents | **Medium** | **High** | HIGH |
| 10 | Anthropic ships it natively | **Low** | **High** | MEDIUM |
| 3 | Website doesn't rank | **High** | **Low** | MEDIUM |
| 17 | Installation too hard | **Medium** | **Medium** | MEDIUM |
| 4 | Subreddit never reaches mass | **High** | **Low** | LOW |
| 12 | Custom GPTs serve this niche | **Medium** | **Low** | LOW |
| 20 | Skills feel academic | **Low** | **Medium** | LOW |

---

## Step 5: Warning Signs for Critical and High-Priority Causes

### CRITICAL Items

**1. Nobody knows it exists**
- Warning signs: Website analytics show <100 visits/week after month 1. No organic mentions on Twitter/Reddit/HN. Plugin install count flatlines. You spend less than 30% of your time on distribution.

**5. People don't understand what it is**
- Warning signs: When you describe it to someone in person, they nod politely but don't ask follow-up questions. Landing page bounce rate >80%. People who visit the site don't click through to any skill. Comments like "so it's just prompts?"

**14. Building instead of selling**
- Warning signs: You track your own time and find >70% goes to new skills or refactoring. You feel more comfortable writing SKILL.md files than writing a tweet. You haven't talked to a potential user this week.

**7. Try once, don't return**
- Warning signs: Plugin installs go up but daily active use stays flat. No repeat usage in analytics. Users invoke 1-2 skills and stop. No one shares output or mentions it again.

**9. Output doesn't justify friction**
- Warning signs: You run A/B comparisons (structured skill vs. plain question) and the difference is subtle. Users say "that's cool" but don't change behavior. Nobody screenshots skill output to share.

**13. Solo developer burnout**
- Warning signs: You dread opening the project. Commits become infrequent. You start rationalizing that the market isn't ready. You avoid checking analytics.

### HIGH Items

**6. Problem not painful enough**
- Warning signs: When you ask people "how do you make important decisions?" they shrug and say "I just think about it." No one is searching for "structured thinking tools."

**8. 592 skills is overwhelming**
- Warning signs: Users who visit the skills list leave within seconds. Nobody uses the category routers. People ask "which one should I use?" and give up before you answer.

**15. No feedback loop**
- Warning signs: Zero bug reports, zero feature requests, zero complaints. Silence is the worst signal.

**16. Financial pressure**
- Warning signs: Savings runway drops below 3 months. You start applying for jobs. Project work decreases to evenings only.

**19. No onboarding**
- Warning signs: New users invoke zero skills in their first session. Support questions are all "how do I start?"

**11. Market moves to agents**
- Warning signs: AI discourse shifts entirely to autonomous agents. "Prompt engineering is dead" articles proliferate. Users expect AI to do, not guide.

---

## Step 6: Mitigations

### CRITICAL: Nobody knows it exists (#1)

**Prevention:**
- Set a hard rule: minimum 40% of weekly time goes to distribution and outreach, starting now.
- Write and publish one "skill in action" example per week on Twitter, Reddit, and Hacker News -- showing real output, not describing the tool.
- Identify 10 communities where structured thinkers already gather (rationalist communities, productivity forums, startup founders, consultants) and become a genuine participant before posting about the tool.
- Create a "reasoningtool in 60 seconds" video showing a real problem being analyzed.

**Contingency:**
- If organic growth fails by month 2, shift to direct outreach: find 50 people who publicly struggle with decisions/analysis and offer to run a skill for them live.

### CRITICAL: People don't understand what it is (#5)

**Prevention:**
- Kill the abstraction. Lead with a single, concrete before/after: "Here's a decision I was stuck on. Here's what /prm produced. Here's what I did differently."
- The landing page should show output, not describe features. Show the thinking, not the tool.
- Test the pitch on 20 people in person. If fewer than half can explain it back to you, rewrite everything.
- Frame it as "thinking partner" or "decision advisor," not "592 skills."

**Contingency:**
- If the concept doesn't land after 3 pitch iterations, narrow to a single use case (e.g., "pre-mortem tool for startup founders") and expand later.

### CRITICAL: Building instead of selling (#14)

**Prevention:**
- Declare a feature freeze. 592 skills is enough. No new skills until 100 active users.
- Track time in two buckets: BUILD and DISTRIBUTE. Review weekly. If BUILD > 30%, stop and redistribute.
- Create a weekly distribution checklist: 2 posts, 5 DMs, 1 demo video.

**Contingency:**
- If you catch yourself building, ask: "Will this get me one more user this week?" If no, stop.

### CRITICAL: Try once, don't return (#7)

**Prevention:**
- Design a "first 5 minutes" experience: install the plugin, run `/meta` to orient, then `/prm` on a real problem. Make those 5 minutes undeniably useful.
- Build a "daily thinking habit" angle: e.g., "start your day with `/prm` on your biggest risk."
- After someone uses a skill, suggest the logical next skill. Chain engagement.

**Contingency:**
- If retention is near zero at month 2, survey churned users (even if there are only 5). Ask what they expected vs. what they got.

### CRITICAL: Output doesn't justify friction (#9)

**Prevention:**
- Run honest comparisons yourself: use the skill, then ask Claude the same question plainly. If the skill version isn't clearly better, fix the skill or cut it.
- Focus quality on the top 20 skills, not breadth across 592. Better to have 20 that are obviously great than 592 that are mediocre.
- Collect before/after examples from your own real decisions to demonstrate the difference.

**Contingency:**
- If output quality is indistinguishable from plain prompting, the entire product thesis is wrong. Pivot to a different form factor (e.g., interactive decision journals, reasoning logs).

### CRITICAL: Solo developer burnout (#13)

**Prevention:**
- Set a hard financial deadline: if no meaningful traction by month 4, get a job and continue the project part-time. Remove the existential pressure.
- Find 1-2 accountability partners or early believers. Even one enthusiastic user changes the psychological equation.
- Celebrate small wins publicly. Share progress on Twitter. External accountability sustains motivation.
- Protect non-work time. Burnout comes from joyless grinding, not hard work.

**Contingency:**
- If burnout hits, reduce scope to maintaining what exists and spending 100% of project time on distribution. Stop all building.

### HIGH: Overwhelming skill count (#8)

**Prevention:**
- Create a "Start Here" path of 5 skills: `/meta`, `/prm`, `/dcp`, `/rca`, `/cba`. Feature these prominently.
- Hide the full skill list behind one click. Lead with use cases, not a catalog.
- Add a `/wsib` (what skill is best) skill as the default entry point that routes users.

**Contingency:**
- If users still bounce, radically simplify: present only 10 skills and add a "request more" option.

### HIGH: No onboarding (#19)

**Prevention:**
- Build a 3-step onboarding: (1) Install, (2) Run `/meta` with your current problem, (3) Get routed to the right skill and see results.
- Create a "your first analysis" walkthrough on the website.

**Contingency:**
- Offer to personally onboard the first 50 users via chat or video call.

---

## Step 7: Updated Plan

### The 6-Month Plan, Revised

**Month 1 (March 2026): Foundation + First Users**
- Feature freeze. No new skills. Fix quality of top 20 skills only.
- Build "first 5 minutes" onboarding experience.
- Redesign landing page around output examples, not feature descriptions.
- Test pitch on 20 people. Iterate until 15/20 can explain it back.
- Get 10 people to actually use it and give feedback.
- Time allocation: 30% build, 70% distribute.

**Month 2 (April 2026): Distribution Push**
- Publish 4 "skill in action" posts across Twitter, Reddit, HN.
- Engage in 5 relevant communities as a genuine participant.
- Create 60-second demo video.
- Target: 50 plugin installs, 10 repeat users.
- Launch subreddit only if there's organic demand for a community space.

**Month 3 (May 2026): Feedback Loop**
- Survey all users (even 5-10). Understand retention/churn.
- A/B test: are skills noticeably better than plain prompting? Fix if not.
- Double down on what's working, kill what isn't.
- Target: 100 plugin installs, 25 weekly active users.

**Month 4 (June 2026): Decision Point**
- If <50 active users: evaluate pivot or part-time transition honestly.
- If >50 active users: continue full-time, explore monetization.
- Run a second pre-mortem on whatever path you choose.

**Months 5-6 (July-August 2026): Scale or Sustain**
- If traction: expand distribution, consider partnerships, grow community.
- If no traction: maintain project part-time, get a job, keep the door open.

### Monitoring Dashboard (Check Weekly)
| Metric | Warning Threshold | Action |
|---|---|---|
| Time on distribution | <40% of week | Stop building, start distributing |
| New installs/week | <5 after month 1 | Change distribution channels |
| Repeat usage rate | <10% of installs | Fix onboarding and first experience |
| Landing page bounce rate | >80% | Redesign around concrete examples |
| Feedback received | 0 for 2 weeks | Directly solicit feedback from users |
| Savings runway | <3 months | Begin job search, shift to part-time |
| Your motivation (1-10) | <4 for 2 weeks | Take a break, talk to someone, reassess |

### Three Sentences That Should Haunt Every Week
1. "Am I building, or am I getting this in front of people?"
2. "Can someone who has never seen this understand what it does in 10 seconds?"
3. "Did anyone use it this week who isn't me?"

# /ht Hypothesis: most users will only ever use 5-10 skills regularly. Test this.
**Date:** 2026-03-09
**Skill:** /ht (Hypothesis Testing)

---

## Interpretation

**Interpretation 2 — Validate a business assumption.** The user has a belief about how customers will use the reasoning toolkit (592 skills, tiered architecture) and needs to evaluate whether it holds up, because it would reshape presentation and development strategy.

---

## Step 0: Context Detection and Variant Selection

| Factor | Value | Notes |
|--------|-------|-------|
| Time Pressure | NORMAL | Strategic question, no deadline |
| Stakes | HIGH | Changes entire presentation and development strategy |
| Domain Expertise | INTERMEDIATE | Builder of the system, but no usage telemetry yet |
| Test Cost | CHEAP | Can reason from analogies, software data, and structural analysis without running experiments |

**Selected variant**: HT-Standard (all 7 steps) because stakes are HIGH and the hypothesis has deep strategic implications, but we can run most "tests" as analytical exercises rather than expensive experiments.

---

## Step 1: Clarify the Claim and Scope

### 1. Statement of the claim (made precise)

**Vague:** "Most users will only ever use 5-10 skills regularly."

**Clear:** "For a typical user of the reasoning toolkit over a 6-month period, the number of distinct skills they invoke at least 3 times will fall in the range of 5-15, despite 592 skills being available. This will be true for at least 70% of active users."

Key terms defined:
- **"Most users"** = at least 70% of users who use the toolkit more than once
- **"Regularly"** = invoked 3+ times over a 6-month period
- **"Use"** = directly invoke via slash command (not skills chained automatically by routers)
- **"5-10"** = treating this as an order-of-magnitude claim; the precise band is 5-15

### 2. Claim type

**Statistical claim.** This asserts a distributional property: the usage distribution across skills will be heavily concentrated, following a power law or similar long-tail distribution.

### 3. Scope conditions

- Applies to: individual users of a Claude Code-based reasoning toolkit with 592 skills
- Assumes: users discover skills primarily through routers (/claim, /decide, etc.) or documentation
- Assumes: no gamification or incentive to try all skills
- Boundary: does not apply to the toolkit developer (you) or power users who deliberately explore

### 4. Competing claims

| # | Competing Hypothesis | What it predicts |
|---|---------------------|-----------------|
| C1 | **Router effect**: Users use 2-4 router skills only, never learning direct skills | Regular set is even smaller (2-5), not 5-10 |
| C2 | **Expanding repertoire**: Users start with 5-10 but steadily grow to 20-30 as they discover value | 5-10 is only an early-stage snapshot, not a steady state |
| C3 | **Bimodal distribution**: There are "shallow" users (1-3 skills) and "deep" users (20+), with few in the 5-10 middle | The "most users use 5-10" claim is an average that describes nobody |

### 5. Background plausibility

This claim is highly plausible based on established patterns:
- **Zipf's Law in software usage**: Features in most software follow power-law distributions. Studies of Microsoft Office show ~80% of users use <10% of features regularly.
- **The "vital few" principle**: In IDE plugins, browser extensions, and CLI tools, users converge on a small working set.
- **Cognitive load theory**: Humans have limited working memory for procedures; 5-10 is near the upper bound of what people maintain as "things I know how to reach for."
- **Discovery friction**: With 592 skills, users must actively discover each one. Without incentive, most won't explore beyond what solves their immediate problem.

**Initial credence: P(H1) = 75%** — I think this is probably true, with the main uncertainty being whether the number lands at 5-10 or is even lower (2-5, with routers doing the work).

---

## Step 2: Formulate Testable Hypotheses

### H1 (Research Hypothesis)
If the reasoning toolkit is used by a population of active users over 6 months, then at least 70% of those users will have a regular skill set (3+ invocations) of 5-15 distinct skills, and the overall usage distribution across 592 skills will follow a power law with a long tail.

### H0 (Null Hypothesis)
Usage is roughly uniform across skills, or at minimum, the typical user's regular set exceeds 20 distinct skills. There is no strong concentration effect.

### H-Alt-1 (Router Dominance)
Users interact almost exclusively through the 17 category routers and never learn direct skill names. The regular set is 2-5 routers, not 5-10 specific skills.

### H-Alt-2 (Expanding Repertoire)
Users start narrow but expand continuously. By month 6, the median regular set is 20+ skills and growing.

### H-Alt-3 (Bimodal)
Two distinct user populations emerge: "shallow" (1-3 skills, most users) and "deep" (25+, power users), with few users in the 5-10 range.

### Specific Predictions

| Prediction | Under H1 | Under H0 | Under H-Alt-1 |
|-----------|---------|---------|---------------|
| Median regular skills per user | 5-15 | >20 | 2-5 |
| % of skills never used by any user | >70% | <30% | >85% |
| Top 10 skills account for X% of invocations | >60% | <30% | >80% |
| Users who know skill names (vs. use routers only) | >50% | >80% | <20% |
| Growth in repertoire month-over-month | Plateaus by month 2-3 | Steady increase | Flat from month 1 |

### Falsification Criteria
- H1 would be falsified if: median regular set is <4 or >20 in a sample of 50+ active users
- H1 would be falsified if: skill usage follows a uniform distribution (no power law)
- H1 would be falsified if: the distribution is clearly bimodal with no concentration around 5-15

---

## Step 3: Assess Prior Probability

### Base rates from analogous domains

| Domain | Finding | Source/basis |
|--------|---------|-------------|
| Microsoft Office features | 80-90% of users use <10% of features | Internal Microsoft research, widely cited |
| IDE shortcuts | Most developers use 5-15 keyboard shortcuts regularly out of 200+ available | JetBrains surveys |
| CLI tools (git) | Most developers use 8-12 git commands regularly out of 150+ | Various developer surveys |
| Vim commands | Regular users settle on ~20-30 commands out of hundreds | Usage studies |
| Browser extensions | Average user has 3-5 active extensions despite thousands available | Chrome Web Store data |
| Slack slash commands | Teams use 3-8 custom commands regularly | Anecdotal but consistent |

### Theoretical support
- **Power law of usage**: Nearly universal in software. The question is not *whether* usage concentrates but *where* on the spectrum (5? 10? 20?).
- **Satisficing behavior**: Users find "good enough" tools and stop searching. Herbert Simon's bounded rationality predicts exactly this pattern.
- **Habit formation**: Once a user has a workflow, switching costs make them stick with known skills.

### Prior probability assignment

| Hypothesis | Prior P | Reasoning |
|-----------|---------|-----------|
| H1: Regular set is 5-15 | **70%** | Strong analogical evidence from every comparable domain |
| H-Alt-1: Regular set is 2-5 (router-only) | **15%** | Plausible if routers work so well users never learn direct skills |
| H-Alt-3: Bimodal distribution | **10%** | Possible if the toolkit attracts both casual and power users with no middle ground |
| H-Alt-2: Expanding to 20+ | **3%** | Would require unusual exploration behavior; contradicts nearly all software usage data |
| H0: Uniform usage | **2%** | Essentially impossible given every known analogy |

Note: H1 and H-Alt-1 together account for 85%. The real question may be less "do users concentrate?" and more "how few skills do they concentrate on?"

---

## Step 4: Design Severe Tests

Since we don't yet have telemetry, we can design five analytical tests using available evidence and reasoning. These are "desk tests" -- not experimental, but still capable of updating beliefs.

### Test A: Structural Analysis of the Skill Tree
**Question:** Does the architecture itself create concentration?
**Method:** Examine the 17 category routers. If most user problems map to 3-5 routers, and each router maps to 2-3 common skills, the architecture *mechanically produces* a 5-15 skill working set.
**What would falsify H1:** If each router maps to 10+ equally likely skills, usage would spread more broadly.

**Result of analysis:**
- The 17 routers cover broad categories (claim, decide, diagnose, search, want, how, emotion, action, create, technical, analyze, certainty, iterate, meta, evaluate, viability, sp)
- A typical knowledge worker probably touches 4-6 of these categories regularly (decide, claim, how, action, create, analyze)
- Each router will select from a handful of common skills: /dcp, /rca, /ht, /se, /pw perhaps being the most common
- This produces an expected working set of **8-15 skills** (4-6 routers + 4-9 direct skills they learn from router output)
- **Verdict: Supports H1.** The architecture channels users toward a small subset.

### Test B: Analogical Comparison to Git Commands
**Question:** Does the "592 skills" situation mirror "150+ git commands"?
**Method:** Git has ~150 commands. Developer surveys consistently show 8-12 in regular use (clone, pull, push, commit, add, status, branch, checkout, merge, log, diff, stash). That's ~6-8% of available commands.
**Prediction under H1:** 5-15 out of 592 = 0.8-2.5% of skills. This is *even more concentrated* than git, which makes sense because git commands are all within one domain, while 592 skills span many problem types a user may never encounter.
**What would falsify H1:** If reasoning skills are more interconnected than git commands (i.e., users need more variety because problems are more diverse), the analogy breaks down.

**Result of analysis:**
- Git commands are within a single domain (version control). Reasoning skills span many life/work domains.
- This actually *strengthens* H1: a user who mainly does decision-making won't touch diagnostic or creative-writing skills.
- **Verdict: Supports H1, possibly supports H-Alt-1** (even smaller set than 5-10).

### Test C: Problem-Type Frequency Analysis
**Question:** How many distinct problem types does a person encounter regularly?
**Method:** Consider a knowledge worker's week. They need to: make decisions (2-3/week), write/communicate (daily), solve problems (1-2/week), plan (1/week), evaluate ideas (1/week). That's 5 problem categories, mapping to maybe 5-8 specific skills.
**What would falsify H1:** If people regularly encounter 15+ distinct problem types that each require a different skill.

**Result of analysis:**
- Weekly problem types for a knowledge worker: deciding (1 skill), writing (1-2 skills), debugging/diagnosing (1 skill), planning (1 skill), evaluating (1 skill), researching (1 skill), idea generation (1 skill)
- Total: 7-9 recurring problem types
- Some weeks add: conflict resolution, emotional processing, goal setting (occasional, not weekly)
- **Verdict: Supports H1.** The number of recurring problem types naturally bounds the regular skill set.

### Test D: Discovery Friction Test
**Question:** Given 592 skills, how many will a user even *find*?
**Method:** Examine discovery paths. Users find skills by: (1) reading CLAUDE.md tables (exposes ~40 skills), (2) using routers that suggest skills (exposes 5-10 per session), (3) browsing the website (if they do). Without deliberate exploration, natural discovery over 6 months is probably 20-40 skills *encountered*, of which regular use would be a subset.
**What would falsify H1:** If the router system aggressively exposes users to new skills each session, broadening their repertoire.

**Result of analysis:**
- Routers tend to route to the *same* skills for similar problems (that's the point of good routing)
- A user who asks the same *kind* of question gets the same skill repeatedly, reinforcing concentration
- Discovery of new skills requires new problem types, which are bounded (see Test C)
- **Verdict: Strongly supports H1.** Discovery friction + router consistency creates concentration.

### Test E: Counterexample Search
**Question:** Is there any software tool ecosystem where users regularly use >10% of available features/tools?
**Method:** Search for counterexamples to the concentration hypothesis.
**Candidates:**
- Video games: Players use many abilities/items, but these are designed for progressive unlocking with rewards. Not analogous -- no gamification here.
- Musical instruments: Musicians use many techniques, but mastery is the goal. Not analogous -- users want solutions, not mastery.
- Programming languages: Developers do use many language features. But even here, most codebases use ~30% of language features, and individual developers less.

**Result of analysis:**
- No strong counterexample found in tool-usage domains
- Counterexamples exist only where (a) variety is rewarded/gamified, or (b) mastery is the explicit goal
- Neither condition applies to a reasoning toolkit used instrumentally
- **Verdict: No evidence against H1.**

---

## Step 5: Evaluate the Evidence

### Evidence Summary Table

| Test | Evidence For H1 | Evidence Against H1 | Strength |
|------|----------------|---------------------|----------|
| A: Structural analysis | Architecture channels to 8-15 skills | -- | Moderate |
| B: Git analogy | 6-8% concentration expected; toolkit may be even more concentrated | -- | Moderate |
| C: Problem-type frequency | 7-9 recurring types bounds the set | Occasional variety could push to 12-15 | Moderate |
| D: Discovery friction | Router consistency + friction creates concentration | -- | Strong |
| E: Counterexample search | No counterexample in tool-usage domains | Games/mastery domains differ (but not analogous) | Moderate |

### Bayesian Assessment

**Likelihood ratio estimation:**
- P(all five tests support H1 | H1 is true) = high, ~0.85
- P(all five tests support H1 | H0 is true) = very low, ~0.05
- Bayes factor: ~0.85/0.05 = **17** (strong evidence for H1)

### Evidence Quality Assessment

**Limitations:**
- All five tests are analytical/analogical, not empirical. No actual user data exists yet.
- The analogies (git, Office) are from different domains with different user motivations.
- The structural analysis assumes routers work as designed.
- We're testing a prediction about future behavior, which inherently has more uncertainty.

**Severity of tests:**
- Tests A and D are moderately severe: they could have revealed that the architecture *spreads* usage broadly.
- Test E is the most severe: a strong counterexample would have significantly damaged H1.
- Tests B and C are supportive but not individually decisive.
- Collectively, the convergence of five independent lines of evidence is meaningful.

---

## Step 6: Update Beliefs

### Posterior Probability Calculation

| Hypothesis | Prior | Direction of Evidence | Posterior | Change |
|-----------|-------|----------------------|-----------|--------|
| H1: Regular set is 5-15 skills | 70% | Supported by all 5 tests | **82%** | +12 |
| H-Alt-1: Regular set is 2-5 (router-only) | 15% | Partially supported (Test B, D suggest possible) | **12%** | -3 |
| H-Alt-3: Bimodal | 10% | No evidence for or against | **4%** | -6 |
| H-Alt-2: Expanding to 20+ | 3% | No supporting evidence found | **1%** | -2 |
| H0: Uniform usage | 2% | No counterexamples found | **1%** | -1 |

### Key Insight from Updating

The biggest update is not about *whether* concentration happens (that was always very likely), but about the **boundary between H1 and H-Alt-1**. The real uncertainty is:

> **"Will users learn direct skill names, or just use routers?"**

If routers are good enough, the regular set might be 3-5 routers (not 5-15 direct skills). This distinction matters enormously for strategy:
- If H1: invest in making the best 15-20 skills excellent, and help users discover them
- If H-Alt-1: invest in making routers brilliant, and treat individual skills as invisible backend

### Remaining Uncertainty
- **Critical unknown**: How good are the routers? If routers reliably pick the right skill, users may never need to learn skill names. If routers are unreliable, users will learn direct skills to get consistent results.
- **Critical unknown**: Will users share skills with each other? ("Try /dcp for that decision" in a team Slack.) Peer recommendation could expand repertoires beyond what routers expose.
- **Not testable analytically**: The exact number (5? 10? 15?) requires real usage data.

---

## Step 7: Conclusions and Strategic Implications

### Verdict

**Evidence supports H1 (posterior: 82%).** Most users will settle into a regular set of 5-15 skills over 6 months. The combined evidence from structural analysis, software analogies, problem-type frequency, discovery friction, and absence of counterexamples all point the same direction. The concentration effect is near-certain; the exact band (5-15 vs. 2-5) is the main remaining uncertainty.

### What This Means for Strategy

**If this is true (and it very likely is), the following implications are significant:**

#### 1. Presentation Strategy
- **Don't present 592 skills.** The number is a liability, not an asset. It signals overwhelm, not capability.
- **Present 12-17 entry points** (the tier-1 skills and category routers). This is the "menu" users need.
- **Let depth be discovered, not displayed.** The 500+ tier-3 skills should be invisible until a router invokes them.
- **Think of it as**: "17 capabilities that each have deep specialist knowledge behind them."

#### 2. Development Strategy
- **Invest disproportionately in tier-1 and routers.** If 80% of usage hits 15 skills, those 15 must be exceptional. Diminishing returns on skill #200 vs. skill #10 are extreme.
- **Router quality is existential.** If routers misroute, users lose trust in the whole system. This is the single highest-leverage improvement.
- **The long tail has option value, not usage value.** Having 592 skills means you *can* handle edge cases. But don't optimize for them. Think of tier-3 as "insurance," not "product."

#### 3. Measurement Strategy (when telemetry is possible)
- Track: distinct skills per user per month (expect plateau at 5-15)
- Track: router-only vs. direct-invoke ratio (tests H1 vs. H-Alt-1)
- Track: skill discovery curve (expect sharp early rise, then plateau)
- Track: top-20 skills as % of total invocations (expect >80%)

#### 4. One Important Caveat
The hypothesis applies to *individual* users. The *population* might collectively use 100+ skills, because different users have different needs. This means the long tail isn't useless -- it serves the *diversity of the user base*, not the depth of individual usage. Don't cut the long tail; just don't market it.

### Next Steps

| Priority | Action | Reason |
|----------|--------|--------|
| 1 | Redesign presentation around 17 entry points, not 592 skills | Direct implication of H1 |
| 2 | Audit and optimize the 17 category routers for routing accuracy | Highest-leverage quality investment |
| 3 | Identify the likely "top 15" skills and polish them ruthlessly | These are 80% of the product experience |
| 4 | Build usage telemetry to validate or falsify with real data | Move from analytical to empirical evidence |
| 5 | Design a "skill recommendation" system based on usage patterns | Help users find their next skill in the 5-15 set |

---

## Verification Checklist

- [x] Context assessed and appropriate variant selected (HT-Standard, HIGH stakes)
- [x] Hypothesis is specific, testable, and falsifiable (5-15 regular skills for 70%+ of users)
- [x] Prior probability is explicit and justified (70%, based on software usage analogies)
- [x] Tests are severe enough to potentially falsify hypothesis (especially counterexample search)
- [x] Evidence evaluated using appropriate methods (Bayesian updating, convergence of 5 tests)
- [x] Belief updating follows from evidence appropriately (70% -> 82%)
- [x] Conclusion is appropriately hedged (main uncertainty: 5-15 vs. 2-5, and lack of empirical data)
- [x] Strategic implications documented for action

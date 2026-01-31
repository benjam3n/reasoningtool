# DCP — How to Structure a New Team

**Date**: 2026-01-31
**Input**: How to structure a new team (from /analyze 8x optimal group organization → /dcp)

---

# HOW TO STRUCTURE A NEW TEAM — DECISION PROCEDURE

## STEP 0: CLASSIFY YOUR SITUATION

Before designing a team, answer these five gating questions. Write down your answers — you will reference them throughout.

**Q1. What is the team's primary output?**
Pick ONE:
- (A) A tangible product or artifact (software, report, physical object)
- (B) An ongoing service or operation (support, maintenance, processing)
- (C) A decision or recommendation (strategy, policy, evaluation)
- (D) A creative work (design, content, campaign)
- (E) A research finding or discovery (investigation, experiment, analysis)

**Q2. What is the time horizon?**
Pick ONE:
- (F) Sprint: Under 4 weeks
- (G) Project: 1-6 months
- (H) Program: 6-18 months
- (I) Permanent: Ongoing with no planned end date

**Q3. How much is already defined?**
Pick ONE:
- (J) Almost everything — there is a clear spec, the team just needs to execute
- (K) The goal is clear but the path is not — the team must figure out how to get there
- (L) Even the goal is fuzzy — the team must define what success looks like

**Q4. What is the consequence of failure?**
Pick ONE:
- (M) Low — a setback but recoverable without major damage
- (N) Medium — significant cost, reputation, or schedule impact
- (O) High — existential risk to the organization, safety-critical, or irreversible

**Q5. Where will people be located?**
Pick ONE:
- (P) Same room / same floor
- (Q) Same building or campus, different floors
- (R) Same city, different offices
- (S) Multiple cities or time zones
- (T) Fully remote, spread across 3+ time zones

**Write down your five-letter code** (e.g., "A-G-K-N-S"). You will use this throughout.

---

## SECTION A: DETERMINE TEAM SIZE

Team size is the single highest-leverage structural decision. Get this wrong and everything downstream suffers.

### Step A1: Start with the work, not the people

List every distinct activity the team must perform in a typical week. Be specific. Not "engineering" but "write backend API code," "review pull requests," "respond to production incidents," "write technical documentation."

**What you should see:** A list of 8-30 distinct activities. If you have fewer than 8, you are grouping too broadly — break them down further. If you have more than 30, some of these activities probably belong to a different team.

### Step A2: Identify which activities require dedicated attention

For each activity on your list, ask: "If nobody did this for two weeks, would the team's primary output (from Q1) be visibly damaged?"

Mark each activity YES or NO.

**What you should see:** 40-70% of activities marked YES. If almost everything is YES, you are listing too granularly. If almost nothing is YES, the team's mission may be too broad.

### Step A3: Count the minimum number of people

Group your YES activities into clusters where one person could reasonably do all activities in that cluster. The rule: one person can handle 2-4 distinct activity types well. Beyond 4, quality drops sharply.

Count the clusters. This is your **minimum team size**.

**What you should see:** A number between 2 and 8. If you got 1, you do not need a team — you need a single contributor with occasional support. If you got more than 8, proceed to Step A5.

### Step A4: Apply the communication overhead tax

Use this table:

| Minimum team size from A3 | Add this many people | Adjusted size |
|---|---|---|
| 2 | 0 | 2 |
| 3 | 0 | 3 |
| 4 | 0-1 | 4-5 |
| 5 | 1 | 6 |
| 6 | 1-2 | 7-8 |
| 7 | 2 | 9 |
| 8 | 2-3 | 10-11 |

The "add" column accounts for the fact that as teams grow, people spend more time coordinating and less time producing.

Now check your Q4 answer:
- If you answered (O) High consequence: add 1 more person (for redundancy and review)
- If you answered (M) Low consequence: subtract 1 person if your adjusted size is 5+

**Your result is the TARGET TEAM SIZE.** Write it down.

### Step A5: If your minimum exceeds 8

You do not need one team. You need multiple teams. Divide your activity clusters into groups of 3-5 clusters each. Each group becomes a sub-team. Then:
- Create one sub-team for each group (sized using Steps A3-A4 on just that group's activities)
- Add one coordination role (see Section B) that sits across all sub-teams
- Proceed through the rest of this procedure once for each sub-team, then once more for the coordination layer

**WARNING: THE "JUST ADD PEOPLE" TRAP.** When the work seems too large, the instinct is to make one big team. Teams above 8-10 people almost always underperform two smaller teams doing the same total work. Communication paths grow as n*(n-1)/2. A team of 12 has 66 communication paths. Two teams of 6 have 15 each (30 total). The larger team spends more than twice as much energy on coordination.

---

## SECTION B: DEFINE ROLES

### Step B1: Identify required capabilities

Go back to your activity clusters from Step A3. For each cluster, write down:
1. What skill is needed (e.g., "can write production Python code")
2. What judgment is needed (e.g., "can decide when code is ready to ship")
3. What access is needed (e.g., "needs credentials to production database")

**What you should see:** Each cluster has 1-3 skills, 0-2 judgment areas, and 0-3 access requirements.

### Step B2: Decide how specialized roles should be

Look at your answer to Q2 (time horizon) and Q3 (how much is defined):

| | (J) Fully defined | (K) Goal clear, path unclear | (L) Goal fuzzy |
|---|---|---|---|
| (F) Sprint | Highly specialized roles | Moderately specialized | Generalist roles |
| (G) Project | Highly specialized | Moderately specialized | Moderately specialized |
| (H) Program | Moderately specialized | Moderately specialized | Generalist with specialties |
| (I) Permanent | Moderately specialized | Generalist with specialties | Generalist with specialties |

**Definitions:**
- **Highly specialized:** Each person owns exactly one cluster. They do one thing well. Roles are clearly bounded. Best when you know exactly what needs doing.
- **Moderately specialized:** Each person has a primary cluster but can cover one adjacent cluster. There is overlap. Best when the path may shift.
- **Generalist with specialties:** Everyone can do most things, but each person has 1-2 areas where they go deeper. Best when you are still figuring out what work needs doing.

### Step B3: Assign the four essential functions

Every team, regardless of size, needs these four functions covered. They can be held by the same person on small teams (3-4 people) but should be separated on teams of 6+.

**Function 1: Direction-setting.** One person decides what the team works on next. They translate external requirements into team priorities.

**Function 2: Quality-gating.** One person decides when work is done. They hold the standard.

**Function 3: External interface.** One person talks to people outside the team — stakeholders, customers, adjacent teams, leadership.

**Function 4: Process maintenance.** One person notices when the team's way of working is broken and fixes it.

**What you should see:** Four names or role titles written down, one per function. On a team of 3, one person may hold 2-3 of these. On a team of 8+, each should be a different person.

### Step B4: Fill remaining roles from capability gaps

Take your target team size (from Section A) and subtract the number of people already assigned to essential functions. The remaining slots are filled based on your capability list from Step B1.

Priority order for filling:
1. Any capability where the team has zero coverage (existential gap)
2. Any capability where one person is the only one who can do it (bus factor = 1)
3. Capabilities that appear in the most activity clusters (highest leverage)
4. Capabilities needed for the highest-risk activities

### Step B5: Write a one-sentence role description for each person

Format: "[Name/Role] is responsible for [primary activities]. They decide [what judgments they own]. They escalate [what they cannot decide alone]."

**What you should see:** If you read all role descriptions aloud, every activity from your Step A1 list is mentioned at least once, and no activity is mentioned in more than two role descriptions.

**WARNING: THE "EVERYONE IS RESPONSIBLE" TRAP.** If an activity appears in three or more role descriptions, nobody owns it. It will fall through cracks. Force yourself to assign primary ownership to exactly one person, with at most one backup.

---

## SECTION C: ESTABLISH DECISION RIGHTS

### Step C1: List the top 10 decisions the team will face repeatedly

These are not one-time decisions. These are recurring choices.

**What you should see:** 8-12 decisions that are specific to your team's work.

### Step C2: Classify each decision using RAPID

For each decision, assign exactly one person to each applicable letter:

| Letter | Role | What it means | There can be... |
|---|---|---|---|
| R | Recommend | Does the research, frames the options, proposes a course | Exactly 1 person |
| A | Agree | Must agree before the decision is final (has veto power) | 0-2 people (fewer is better) |
| P | Perform | Carries out the decision once made | 1+ people |
| I | Input | Is consulted before the decision, but cannot veto | 0-4 people |
| D | Decide | Makes the final call if there is disagreement | Exactly 1 person |

**Critical rule:** Every decision has exactly one D.

### Step C3: Check your Q4 answer for decision speed vs. safety

- If (M) Low consequence: Minimize the number of A (agree/veto) roles. Speed matters more than caution.
- If (N) Medium consequence: Allow 1 A on important decisions, zero on routine ones.
- If (O) High consequence: Allow 1-2 A roles on critical decisions. Require that R and D are different people.

### Step C4: Write it down and share it

Create a simple table: rows are decisions, columns are team members, cells contain the RAPID letter(s). Share with the entire team.

**WARNING: THE "CONSENSUS" TRAP.** Consensus is appropriate only when the team is 4 or fewer people AND consequences are high AND the team has time.

---

## SECTION D: DESIGN COORDINATION MECHANISMS

### Step D1: Determine your coordination budget

| Location | Max recurring meetings per week | Preferred coordination style |
|---|---|---|
| (P) Same room | 2-3 | Mostly informal with minimal scheduled sync |
| (Q) Same building | 3-4 | Mix of informal and scheduled |
| (R) Same city | 3-5 | Primarily scheduled with some informal |
| (S) Multiple cities | 3-5 | Almost entirely scheduled, with async supplements |
| (T) Fully remote 3+ TZ | 2-3 | Primarily asynchronous with few synchronous touchpoints |

### Step D2: Select your synchronous rituals

**Ritual 1: Alignment sync** (required for all teams)
**Ritual 2: Planning session** (required for all teams)
**Ritual 3: Retrospective** (required for teams answering K or L to Q3)
**Ritual 4: Deep review** (required if Q4 = O, recommended if Q4 = N)
**Ritual 5: One-on-ones** (required for teams of 5+, recommended for all)

### Step D3: Select your asynchronous mechanisms

| Mechanism | When to use |
|---|---|
| Written status updates | When synchronous alignment syncs are hard to schedule |
| Shared task board | Always — every team benefits from this |
| Decision log | When Q4 = N or O, or when the team is 6+ people |
| Design documents | When Q3 = K or L |
| Recorded demos | When team members are in 3+ time zones |

### Step D4: Set response-time expectations

| Location | Urgent | Normal | Non-urgent |
|---|---|---|---|
| (P) Same room | 15 min | 2 hours | 1 day |
| (Q-R) Same city | 30 min | 4 hours | 2 days |
| (S) Multi-city | 1 hour | 8 hours | 2 days |
| (T) Fully remote | 2 hours | 24 hours | 3 days |

---

## SECTION E: DESIGN INFORMATION FLOW

### Step E1: Identify your information sources
### Step E2: Map source to receiver
### Step E3: Designate information brokers
### Step E4: Set up transparency defaults

**WARNING: THE "INFORMATION HOARDING" FAILURE.** If one person is the broker for all external information, they become a bottleneck and single point of failure.

---

## SECTION F: SET UP TEAM LAUNCH

### Step F1: Write a Team Charter
### Step F2: Run a "Pre-mortem"
### Step F3: Schedule the first retrospective

---

## QUICK REFERENCE CARDS

### Card 1: Team Size by Mission Type

| Q1 Answer | Typical team size | Why |
|---|---|---|
| (A) Product/artifact | 4-7 | Needs builder + reviewer + direction-setter |
| (B) Service/operation | 4-8 | Needs coverage across hours; redundancy |
| (C) Decision/recommendation | 3-5 | Smaller groups make better decisions |
| (D) Creative work | 3-5 | Creative quality drops in large groups |
| (E) Research/discovery | 2-4 | Deep work requires focus |

### Card 2: Role Specialization at a Glance

| Team size | Recommended specialization |
|---|---|
| 2-3 | Everyone is a generalist |
| 4-5 | Each essential function has a clear owner |
| 6-8 | All functions separated. ICs have clear specialties |
| 9+ | Split into sub-teams |

### Card 3: Coordination Load Estimate

| Team size | Co-located | Remote same TZ | Remote multi-TZ |
|---|---|---|---|
| 3 | 10% | 15% | 20% |
| 5 | 15% | 25% | 30% |
| 7 | 25% | 35% | 40% |
| 10 | 35% | 45% | 55% |
| 15 | 50%+ | 60%+ | Not recommended |

---

## COMMON MISTAKES

1. Designing the team around available people instead of required work
2. No single point of accountability for direction
3. Skipping the decision rights conversation
4. Too many meetings from day one
5. Designing for the steady state on day one
6. Treating "flat" as a structure
7. Ignoring the bus factor

---

## WHEN TO OVERRIDE

1. Crisis / Emergency Response
2. Founder/Founding Team (2-3 people with high trust)
3. Temporary Tiger Team (under 2 weeks)
4. Regulated / Compliance-Driven Environment

---

## WORKED EXAMPLES

### Example 1: New Product Feature Team (Software Company)
Classification: A-G-K-N-P. Target size: 5. PM-led, moderately specialized, shipping biweekly.

### Example 2: Remote Customer Success Reorganization
Classification: B-I-K-N-S. Target size: 6. Generalist with specialties, organized around customer segments.

### Example 3: Three-Person Strategy Task Force
Classification: C-F-L-O-Q. Target size: 3. Consensus decision-making, external review checkpoints.

---

## FINAL VALIDATION CHECKLIST

15 checks covering: mission clarity, team size, role descriptions, essential functions, RAPID table, meeting count, task board, response times, information brokers, transparency defaults, retrospective scheduled, pre-mortem completed, bus factor, and decision awareness.

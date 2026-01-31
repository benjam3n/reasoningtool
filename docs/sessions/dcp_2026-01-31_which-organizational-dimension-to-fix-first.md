# DCP — Which Organizational Dimension to Fix First

**Date**: 2026-01-31
**Input**: Which of the 8 organizational dimensions to fix first (from /analyze 8x optimal group organization → /dcp)

---

# WHICH ORGANIZATIONAL DIMENSION TO FIX FIRST — DECISION PROCEDURE

## STEP 0: UNDERSTAND WHAT YOU ARE DIAGNOSING

You are looking at an organization (or team) that is not working well. There are 8 possible areas ("dimensions") that could be broken. Your job is to figure out which one to fix first — not all of them, just the single highest-priority one.

**The 8 Dimensions (plain language):**

| # | Dimension | What it means in plain English |
|---|-----------|-------------------------------|
| 1 | Size & Structure | How many people are on each team, how teams are grouped, reporting lines |
| 2 | Role Clarity | Whether each person knows exactly what they are responsible for and what they are not |
| 3 | Decision Rights | Whether it is clear who gets to make which decisions, and whether those people actually make them |
| 4 | Information Flow | Whether the right people get the right information at the right time |
| 5 | Coordination Mechanisms | How teams synchronize work — meetings, tools, processes, handoffs |
| 6 | Psychological Safety & Accountability | Whether people can speak up without fear AND whether poor performance has consequences |
| 7 | Goal Alignment & Autonomy | Whether everyone is rowing in the same direction AND has enough freedom to do their work well |
| 8 | Adaptation & Learning | Whether the organization notices when something is not working and actually changes |

**Key principle:** These dimensions are layered. Some are foundations that others depend on. Fixing a higher-layer problem while a lower-layer problem persists is like painting a wall that has water damage — the paint will peel again.

---

## STEP 1: GATHER RAW EVIDENCE (30-45 minutes)

### 1A: Select 5-8 people to interview briefly (10 minutes each)

Pick people who meet ALL of these criteria:
- At least one person from each team or function involved
- At least one person who has been there less than 6 months (fresh eyes)
- At least one person who has been there more than 2 years (institutional memory)
- At least one person in a frontline/individual contributor role
- At least one person in a management role

### 1B: Ask each person these 8 diagnostic questions

**Q1 — Size & Structure:** "If I asked you to draw the org chart for your part of the organization right now, could you do it accurately? How many people do you interact with regularly to get your work done?"

**Q2 — Role Clarity:** "Tell me about the last time something fell through the cracks. Whose job was it?"

**Q3 — Decision Rights:** "Tell me about the last decision that took way too long, or a decision you wanted to make but couldn't."

**Q4 — Information Flow:** "Tell me about the last time you were surprised by something you should have known about sooner."

**Q5 — Coordination Mechanisms:** "Walk me through what happens when your work depends on another team's output. How does the handoff work?"

**Q6 — Psychological Safety & Accountability:** "When was the last time someone raised a concern or bad news in a group setting? What happened next?"

**Q7 — Goal Alignment & Autonomy:** "What are the top 3 priorities for your team right now? And do you feel you have enough freedom to pursue them the way you think is best?"

**Q8 — Adaptation & Learning:** "Can you give me an example of something that was not working, and the organization actually changed it? How long did that take?"

### 1C: Record your raw scores

| Score | Meaning |
|-------|---------|
| 0 | No evidence of dysfunction in this area |
| 1 | Minor friction, but people work around it |
| 2 | Significant dysfunction; multiple people raised this unprompted |
| 3 | Severe; this came up in nearly every interview and people are visibly frustrated or resigned |

---

## STEP 2: APPLY THE DEPENDENCY FILTER

### The Dependency Map

```
LAYER 1 (Foundation):     [6] Psych Safety    [1] Size & Structure
                                |                      |
LAYER 2 (Core Wiring):    [2] Role Clarity    [3] Decision Rights
                                |                      |
LAYER 3 (Flow):           [4] Info Flow        [5] Coordination
                                |                      |
LAYER 4 (Direction):      [7] Goal Alignment & Autonomy
                                |
LAYER 5 (Evolution):      [8] Adaptation & Learning
```

**Adjusted scoring rules (applied in order):**

1. If a dimension scores 2 or 3 AND it is in Layer 1 or Layer 2, add +1 (cap at 4). Foundation problems get a priority boost.
2. If a dimension scores 2 or 3 AND one of its dependencies ALSO scores 2 or 3, subtract 1 (floor at 0). This dimension's problems may be a symptom, not a cause.
3. Apply rule 1 first, then rule 2.

### Dependency Chains

- Dimension 2 depends on Dimension 1 and Dimension 6
- Dimension 3 depends on Dimension 1 and Dimension 6
- Dimension 4 depends on Dimension 2 and Dimension 6
- Dimension 5 depends on Dimension 2 and Dimension 3
- Dimension 7 depends on Dimension 3 and Dimension 4
- Dimension 8 depends on Dimension 6 and Dimension 7

---

## STEP 3: APPLY THE PAIN-SEVERITY TIEBREAKER

If two or more dimensions are tied for the highest adjusted score, use this tiebreaker sequence:

**Tiebreaker A:** Which is causing active harm RIGHT NOW? (concrete negative outcome in last 2 weeks)

**Tiebreaker B:** Which is blocking the most other work? (use downstream blocking count)
- D6 (Psych Safety): blocks 4 downstream
- D1 (Size & Structure): blocks 2
- D2 (Role Clarity): blocks 2
- D3 (Decision Rights): blocks 2
- D4 (Info Flow): blocks 1
- D7 (Goal Alignment): blocks 1
- D5 (Coordination): blocks 0
- D8 (Adaptation): blocks 0

**Tiebreaker C:** Which is cheaper/faster to fix?

**Tiebreaker D:** Ask the team.

---

## STEP 4: CONFIRM YOUR DIAGNOSIS WITH A SMELL TEST

**Check 1: The "Fix It" Thought Experiment** — If magically fixed, would other dimensions improve?

**Check 2: The "Symptom vs. Cause" Check** — Is the dysfunction being CAUSED by another dimension?

**Check 3: The "Can We Actually Do This?" Check** — Does the initiator have authority and resources?

---

## STEP 5: OUTPUT YOUR RECOMMENDATION

Template with: raw scores, adjusted scores, tiebreaker used, primary recommendation, evidence summary, rationale, concrete first actions, success indicators, and dependency notes.

---

## QUICK REFERENCE CARDS

### Card 1: The 60-Second Version
Observe one meeting: (1) Do people know who should be here and why? (2) Does someone decide by the end? (3) Are people sharing openly? (4) Is it clear who does what after?

### Card 2: The "Two Teams in Conflict" Shortcut
Check in order: competing goals → unclear ownership → missing decision authority → not talking → no handoff process.

### Card 3: The "New Leader" Shortcut
First 2 weeks: Psych Safety. Weeks 2-4: Role Clarity + Decision Rights. Month 2: Everything else.

---

## COMMON MISTAKES

1. Treating symptoms as root causes
2. Starting with Adaptation & Learning (D8) — almost never the right first move
3. Confusing "we have a process" with "the process works"
4. Picking the easiest dimension instead of the most important one
5. Diagnosing from the top only
6. Trying to fix everything at once

---

## WHEN TO OVERRIDE

| Condition | Go directly to |
|-----------|---------------|
| People quitting citing "toxic culture" | D6: Psychological Safety |
| Organization doubled/halved in 6 months | D1: Size & Structure |
| Post-mortem found "nobody knew who was supposed to do X" | D2: Role Clarity |
| Decisions made, reversed, re-made, reversed again | D3: Decision Rights |
| Two teams independently built the same thing | D4: Information Flow |

---

## WORKED EXAMPLES

### Example 1: The Startup That Cannot Ship
40-person startup, no major release in 6 months. Winner: D3 (Decision Rights) — CEO overrides everything. Fix: Define delegation boundaries, 30-day trial.

### Example 2: The Enterprise Team That Cannot Collaborate
200-person division, three departments finger-pointing. Winner: D6 (Psychological Safety) — blame culture prevents escalation. Fix: Blameless incident reviews, model vulnerability.

### Example 3: The Rapidly Grown Team
15-person team that was 5 people six months ago. Winner: D2 (Role Clarity) — new hires have no defined scope. Fix: Write one sentence per person defining ownership.

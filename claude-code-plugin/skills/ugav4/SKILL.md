---
name: "ugav4 - Universal Goal Analysis v4 (Leverage & Communication)"
description: "Goal analysis emphasizing leverage identification and stakeholder communication. Finds where small effort produces big results and maps who needs to know what. Consolidated into /uga but usable standalone."
tier: "tier4"
categories: ["Goal Processing"]
tags: ["goal", "leverage", "communication", "stakeholders"]
---

# Universal Goal Analysis v4: Leverage Analysis & Communication

**Input**: $ARGUMENTS

---

## Core Principles

1. **Leverage is not importance.** The most important requirement is often not the highest-leverage one. Leverage means: closing THIS gap makes OTHER gaps easier to close. A requirement that unblocks three other requirements has more leverage than a requirement that is merely critical.

2. **Communication is strategy, not afterthought.** Most goal failures are not analytical failures — they are communication failures. The right people didn't know, didn't agree, or didn't act. Communication planning is a first-class analysis step, not a final checkbox.

3. **Stakeholder mapping precedes strategy.** Before deciding HOW to pursue a goal, identify WHO is affected. People who are surprised by your strategy will oppose it even if it's optimal. People who are consulted will support it even if it's imperfect.

4. **Opposition is data, not obstruction.** When someone opposes your goal, they have information you lack. Their objection reveals a constraint, risk, or value you haven't accounted for. Dismissing opposition is discarding intelligence.

5. **Visible progress compounds.** A goal with visible milestones attracts resources. A goal with invisible progress starves. Part of leverage analysis is identifying which actions produce visible evidence of progress.

---

## Phase 1: Goal and Stakeholder Registration

```
[A] GOAL: [stated goal]
[B] STAKEHOLDER_MAP:

Step 1: List every person or group affected by this goal
Step 2: For each, classify:
    - ROLE: [decision-maker / executor / affected-party / blocker / resource-holder]
    - STANCE: [supportive / neutral / opposed / unknown]
    - POWER: [can block? Y/N] [can accelerate? Y/N]
    - INFORMATION: [what do they know that you don't?]

| Stakeholder | Role | Stance | Can Block | Can Accelerate | Key Info They Hold |
|-------------|------|--------|-----------|----------------|-------------------|
| [name/group] | | | | | |
```

---

## Phase 2: Leverage Analysis

**Sub-procedure — Requirement Leverage Scoring:**

```
[C] REQUIREMENTS: [list from goal decomposition]

Step 1: For each requirement, count:
    - UNBLOCK_COUNT: How many other requirements become easier if this one is met?
    - COST: How much effort/time/money to close this requirement?
    - VISIBILITY: Does closing this produce visible evidence of progress? [Y/N]

Step 2: Calculate leverage score:
    LEVERAGE = (UNBLOCK_COUNT × 3) + (VISIBILITY × 2) - (COST × 1)

Step 3: Rank by leverage score

[D] LEVERAGE_RANKING:
| Requirement | Unblocks | Cost | Visible | Leverage Score |
|-------------|----------|------|---------|----------------|
| [req] | [N] | [H/M/L→3/2/1] | [Y/N→2/0] | [score] |

[E] LEVERAGE_POINTS:
    1. [highest leverage] — because: [why this unblocks the most]
    2. [second highest] — because: [why]
    3. [third highest] — because: [why]
```

---

## Phase 3: Communication Planning

```
[F] COMMUNICATION_MATRIX:

For each stakeholder from Phase 1:

Step 1: What do they need to KNOW? (information)
Step 2: What do they need to BELIEVE? (framing)
Step 3: What do they need to DO? (action)
Step 4: WHEN do they need to know it? (timing — before/during/after key actions)
Step 5: HOW should they be told? (channel — meeting/email/demo/report)

| Stakeholder | Must Know | Must Believe | Must Do | When | How |
|-------------|-----------|-------------|---------|------|-----|
| [name] | | | | | |

[G] COMMUNICATION_SEQUENCE:
Step 1: Order communications by dependency
    - Who must be told first because their reaction affects how you tell others?
    - Who must be told before execution begins?
    - Who can be told after the fact?
Step 2: Identify critical conversations (high-power + opposed/unknown stance)
Step 3: For each critical conversation, prepare:
    - Their likely concern: [what]
    - Your response: [what]
    - What you need from them: [what]
    - Fallback if they refuse: [what]
```

---

## Phase 4: Opposition Analysis

```
[H] OPPOSITION_MAP:

For each stakeholder with stance = opposed or unknown:

Step 1: What is their objection? (stated or inferred)
Step 2: Is the objection valid? [Y/partially/N]
Step 3: What information does their objection reveal?
Step 4: Can the strategy be modified to address their concern without sacrificing the goal?
Step 5: If not modifiable, what is the cost of overriding their objection?

[I] OPPOSITION_INTEGRATION:
    VALID_OBJECTIONS_INCORPORATED: [list — these improve the strategy]
    OBJECTIONS_ACKNOWLEDGED_NOT_INCORPORATED: [list — with rationale]
    OBJECTIONS_OVERRIDDEN: [list — with cost of override]
```

---

## Phase 5: Integrated Strategy

```
[J] STRATEGY:
    LEVERAGE_FIRST_ACTIONS:
        1. [highest-leverage action] — stakeholder impact: [who needs to know]
        2. [second action] — stakeholder impact: [who]
        3. [third action] — stakeholder impact: [who]

    COMMUNICATION_TIMELINE:
        Before starting: Tell [who] [what] via [how]
        After action 1: Tell [who] [what] via [how]
        After action 2: Tell [who] [what] via [how]
        On completion: Tell [who] [what] via [how]

    VISIBILITY_PLAN:
        Milestone 1: [what] — visible to: [who] — when: [date/condition]
        Milestone 2: [what] — visible to: [who] — when: [date/condition]
```

---

## Phase 6: Report

```
UGA v4 LEVERAGE & COMMUNICATION ANALYSIS:
Goal: [goal]

Stakeholders: [N] identified
  Supportive: [list] | Opposed: [list] | Unknown: [list]

Top leverage points:
1. [requirement] — leverage score: [X] — unblocks [N] others
2. [requirement] — leverage score: [X]
3. [requirement] — leverage score: [X]

Critical communications:
1. [who] — tell [what] — before [when] — via [how]
2. [who] — tell [what] — before [when] — via [how]

Opposition integrated: [N] valid objections incorporated
Overridden: [N] — cost: [what]

First action: [highest-leverage action with communication attached]
```

→ INVOKE: /uga $ARGUMENTS (for full analysis incorporating leverage and communication findings)

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Leverage confused with importance** | Highest-leverage item is also the most obviously important | Check: does it UNBLOCK others, or is it just critical on its own? |
| **Missing stakeholders** | Strategy encounters surprise opposition | Re-scan: who is affected indirectly? Who controls resources? |
| **Communication as notification** | Plan says "inform X" without framing or timing | For each stakeholder: what must they BELIEVE, not just know? |
| **Dismissed opposition** | Objections labeled invalid without analysis | Every objection reveals information — extract it before dismissing |
| **Invisible progress** | Strategy has no milestones visible to stakeholders | Add at least 2 visibility checkpoints in first 25% of timeline |
| **Communication after the fact** | All stakeholder contact planned for end of process | Identify who must be told BEFORE execution begins |

---

## Depth Scaling

| Depth | Stakeholder Analysis | Leverage Analysis | Communication |
|-------|---------------------|-------------------|---------------|
| 1x | List key stakeholders with stance | Score top 5 requirements | Communication sequence for decision-makers |
| 2x | Full stakeholder map with roles and power | Score all requirements with unblock counts | Full matrix with critical conversation prep |
| 4x | Stakeholder network analysis (who influences whom) | Leverage interaction effects (closing A changes B's score) | Scenario-based communication plans |
| 8x | Stakeholder simulation (predict reactions to each action) | Dynamic leverage model (scores update as gaps close) | Full stakeholder engagement strategy |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] All stakeholders identified with role, stance, and power
- [ ] Leverage scores calculated with unblock counts
- [ ] Top 3 leverage points identified with rationale
- [ ] Communication matrix completed for all stakeholders
- [ ] Critical conversations prepared (concern/response/need/fallback)
- [ ] Opposition analyzed and valid objections incorporated
- [ ] Visibility plan has milestones in first 25% of timeline
- [ ] First action includes both the leverage move and its communication

---

## Integration

- **Consolidated into**: `/uga` (which uses v4's leverage in Step 3 and communication in Step 7)
- **Use standalone when**: Stakeholder dynamics are the primary challenge
- **Routes to**: `/uga` (full analysis), `/sta` (stakeholder analysis)
- **Invoked by**: Users facing political/organizational complexity
- **Differs from /uga**: /uga runs all 17 steps; ugav4 focuses on leverage and communication
- **Differs from /ugav2**: ugav2 focuses on fact-yielding questions
- **Differs from /ugav3**: ugav3 focuses on procedural decomposition

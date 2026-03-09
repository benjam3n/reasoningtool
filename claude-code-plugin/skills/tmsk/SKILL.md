---
name: "tmsk - Team Analysis"
description: Analyzes something from the team perspective. Identifies composition, roles, communication patterns, coordination costs, and collaboration synergies.
---

# Team Analysis

**Input**: $ARGUMENTS

---

## Step 1: Identify the Team

```
TEAM: [Name or description of the team]
SIZE: [Number of members]
PURPOSE: [Why this team exists]
GOAL FOR THIS ANALYSIS: [What we're evaluating about the team]
```

If $ARGUMENTS describes a project rather than a team, define the team needed.

---

## Step 2: Map Composition and Roles

Who is on the team and what do they do?

```
ROLES:
- [Role 1]: [Person/type] — owns [responsibility]
- [Role 2]: [Person/type] — owns [responsibility]
- [Role 3]: [Person/type] — owns [responsibility]

MISSING ROLES:
- [Role] — needed because [reason]

OVERLAPPING ROLES:
- [Role A] and [Role B] overlap on [area] — risk: [conflict/confusion/redundancy]
```

---

## Step 3: Assess Communication Patterns

How does information flow?

```
COMMUNICATION CHANNELS:
- [Channel 1: meetings, slack, docs] — used for [what]
- [Channel 2] — used for [what]

COORDINATION COSTS:
- [Cost 1: e.g., 3 hours/week in sync meetings]
- [Cost 2: e.g., handoff delays between roles]

INFORMATION GAPS:
- [Who doesn't know what they need to know]
- [Where context gets lost]
```

---

## Step 4: Identify Team Capabilities

What can this team do that individuals cannot?

```
TEAM-ONLY CAPABILITIES:
- [Capability 1] — requires [which roles working together]
- [Capability 2] — requires [which combination]

SYNERGIES:
- [Role A] + [Role B] = [combined output greater than sum]

BOTTLENECKS:
- [Everything flows through Person/Role X]
- [Step Y depends on a single person]
```

---

## Step 5: Diagnose Collaboration Health

```
WORKING WELL:
- [What the team does effectively together]

FRICTION POINTS:
- [Where collaboration breaks down] — cause: [reason]
- [Where coordination fails] — cause: [reason]

TRUST LEVEL: [High / Medium / Low]
ALIGNMENT LEVEL: [High / Medium / Low — does everyone agree on goals?]
```

---

## Step 6: Recommendations

```
TO IMPROVE TEAM PERFORMANCE:
1. [Action] — addresses [which problem from above]
2. [Action] — addresses [which problem]
3. [Action] — addresses [which problem]

TO REDUCE COORDINATION COSTS:
- [Specific change to process or communication]

TO UNLOCK NEW CAPABILITY:
- [What to add or change to enable something the team can't do yet]
```

---

## Integration

Use with:
- `/indv` -> Drill into one team member's perspective
- `/orgn` -> Zoom out to organizational context
- `/comc` -> Design team communication improvements
- `/plsk` -> Evaluate the team's plan

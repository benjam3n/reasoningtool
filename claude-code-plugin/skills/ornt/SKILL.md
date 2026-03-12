---
name: "ornt - Orientation"
description: Helps someone figure out where they are and what they're dealing with. Surveys the situation, identifies the problem type, assesses urgency, and recommends an entry point.
output:
  format: "prose"
---

# Orientation

**Input**: $ARGUMENTS

---

## Step 1: Survey the Situation

Cast a wide net. Don't narrow down yet.

```
SITUATION SCAN:
- What's happening: [describe the situation in plain terms]
- Who's involved: [people, teams, systems, stakeholders]
- What's at stake: [consequences of action / inaction]
- How long has this been going on: [timeline]
- What triggered this moment: [why now?]
```

Rule: Capture breadth first. Resist the urge to diagnose.

---

## Step 2: Identify the Type

Classify what kind of thing this is.

```
TYPE ASSESSMENT:

| Type | Indicators | Match? |
|------|-----------|--------|
| **Problem** | Something is broken or wrong | [yes/no] |
| **Decision** | A choice must be made | [yes/no] |
| **Opportunity** | Something could be gained | [yes/no] |
| **Confusion** | The situation itself is unclear | [yes/no] |
| **Conflict** | Competing interests or views | [yes/no] |
| **Execution** | The path is clear, action is needed | [yes/no] |

PRIMARY TYPE: [the strongest match]
SECONDARY TYPE: [if applicable]
```

SKIP: If the type is immediately obvious, state it in one line and move on.

---

## Step 3: Assess Urgency

Determine how much time pressure exists.

```
URGENCY CHECK:
- Deadline: [is there one? when?]
- Deterioration: [is the situation getting worse over time?]
- Reversibility: [can mistakes be undone?]
- Dependencies: [are others blocked waiting?]

URGENCY LEVEL: [critical / high / moderate / low]
IMPLICATION: [what the urgency level means for approach]
```

---

## Step 4: Check for Prior Work

Don't start from scratch if work has already been done.

```
PRIOR WORK:
- Previous attempts: [what's been tried?]
- Existing analysis: [has this been studied before?]
- Known constraints: [what's already been ruled out?]
- Current momentum: [is something already in motion?]
```

SKIP: If this is a genuinely new situation with no history, skip.

---

## Step 5: Recommend Entry Point

Based on the type and urgency, suggest where to start.

```
RECOMMENDATION:

Given: [one-line summary of situation]
Type: [from Step 2]
Urgency: [from Step 3]

START WITH: /[recommended skill] — because [reason]

THEN CONSIDER:
1. /[next skill] — [what it would add]
2. /[next skill] — [what it would add]
3. /[next skill] — [what it would add]
```

---

## Step 6: Provide a One-Paragraph Briefing

Give the user a crisp summary they can act on.

```
BRIEFING:

[2-4 sentences that capture: what this is, why it matters,
what to do first, and what to watch out for.]
```

Rule: The briefing should be useful even if the user ignores everything else.

---

## Integration

Use with:
- `/exps` -> After orientation, explore the space systematically
- `/meta` -> If the user needs a broader view of available approaches
- `/anst` -> Move into analysis once orientation is complete
- `/se` -> Enumerate the solution space identified during orientation

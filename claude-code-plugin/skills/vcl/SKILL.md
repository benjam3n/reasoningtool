---
name: "vcl - Value Clarification"
description: Discover what you actually value — not what you think you value — by examining behavior, trade-offs, and revealed preferences.
output:
  format: "prose"
---

# Value Clarification

**Input**: $ARGUMENTS

---

## Step 1: Surface Stated Values

Start with what the person says they value.

```
STATED VALUES:
1. [value] — "I believe [how they describe it]"
2. [value]
3. [value]
4. [value]
5. [value]
```

If fewer than 3, prompt: "What would you fight to protect? What makes you angry when violated?"

---

## Step 2: Behavioral Evidence

Values live in behavior, not words. Examine where time, money, and energy actually go.

```
TIME AUDIT: Where do the last 7 days actually go?
- [activity]: [hours/week] — reveals value of [X]
- [activity]: [hours/week] — reveals value of [X]

MONEY AUDIT: Where do discretionary dollars go?
- [category]: reveals value of [X]

ENERGY AUDIT: What gets full attention vs. gets procrastinated?
- Full attention: [X] — reveals value of [X]
- Procrastinated: [X] — reveals low priority of [X]
```

---

## Step 3: Trade-Off Scenarios

Present forced choices to reveal true priorities. Each pair should pit two plausible values against each other.

| Scenario | Choice A (value) | Choice B (value) | Pick |
|----------|-----------------|-----------------|------|
| Job offer: 2x salary but 60hr weeks | Financial security | Free time | ? |
| Friend asks you to lie for them | Loyalty | Honesty | ? |
| Promotion requires relocating away from family | Achievement | Connection | ? |
| Opportunity requires breaking a commitment | Growth | Reliability | ? |
| Speaking up will cost you socially | Integrity | Belonging | ? |

Customize scenarios to the person's actual context from $ARGUMENTS.

---

## Step 4: Identify Revealed Preferences

Compare stated values (Step 1) with behavioral evidence (Step 2) and trade-off choices (Step 3).

```
ALIGNMENT CHECK:
- [Stated value] → CONFIRMED by [behavior/choice] | CONTRADICTED by [behavior/choice]
- [Stated value] → CONFIRMED | CONTRADICTED
...

HIDDEN VALUES (not stated but revealed by behavior):
- [value] — evidence: [what shows this]
```

Flag any major gaps between stated and revealed values. These are not failures — they are data.

---

## Step 5: Sacrifice Test

For each top value, ask: "What would you give up to protect this?"

```
VALUE: [X]
- Would you sacrifice money? [yes/no]
- Would you sacrifice a relationship? [yes/no]
- Would you sacrifice comfort? [yes/no]
- Would you sacrifice status? [yes/no]
- Would you sacrifice time? [yes/no]
SACRIFICE CEILING: [What they won't give up for this value]
```

Values you won't sacrifice anything for are aspirations, not values.

---

## Step 6: Prioritized Value Hierarchy

Rank by behavioral evidence, not stated importance.

```
VALUE HIERARCHY (by revealed behavior):

1. [VALUE] — strongest evidence: [what proves this]
2. [VALUE] — evidence: [X]
3. [VALUE] — evidence: [X]
4. [VALUE] — evidence: [X]
5. [VALUE] — evidence: [X]

ASPIRATIONAL VALUES (stated but not yet enacted):
- [value] — gap: [what would need to change]

CONFLICT ZONES:
- [value X] and [value Y] frequently collide when [situation]
```

---

## Step 7: Alignment Check

Does current life structure support the revealed hierarchy?

```
ALIGNED: [What in life currently serves top values]
MISALIGNED: [What in life contradicts top values]
FIRST MOVE: [One concrete change to close the biggest gap]
```

---

## Integration

Use with:
- `/mdr` -> When values conflict and you need to choose between them
- `/gu` -> To connect values to concrete goals
- `/ecoc` -> To codify values into principles for a team
- `/sdc` -> To check if self-deception is distorting the value picture

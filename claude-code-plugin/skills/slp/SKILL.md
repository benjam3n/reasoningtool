---
name: "slp - Sleep Optimization"
description: Design a personalized sleep improvement plan by assessing current patterns, identifying disruptors, and building sustainable habits.
---

# Sleep Optimization

**Input**: $ARGUMENTS

---

## Step 1: Assess Current Sleep Patterns

Establish a baseline before changing anything.

```
CURRENT STATE:
- Bedtime: [typical time]
- Wake time: [typical time]
- Time to fall asleep: [minutes]
- Night wakings: [frequency and duration]
- Total sleep: [hours]
- Sleep quality (1-10): [rating]
- Wake feeling: [refreshed / groggy / exhausted]
- Naps: [yes/no, when, how long]
```

If $ARGUMENTS doesn't specify, ask for this information before proceeding.

---

## Step 2: Identify Sleep Disruptors

Categorize what's actually interfering with sleep.

```
ENVIRONMENTAL:
- [ ] Light exposure (screens, ambient light)
- [ ] Noise (traffic, partner, pets)
- [ ] Temperature (too hot / too cold)
- [ ] Mattress/pillow quality

BEHAVIORAL:
- [ ] Irregular schedule
- [ ] Late caffeine (within 8 hours of bed)
- [ ] Late alcohol (within 3 hours of bed)
- [ ] Late heavy meals
- [ ] Intense exercise within 2 hours of bed
- [ ] Screen use in bed
- [ ] Working in the bedroom

PSYCHOLOGICAL:
- [ ] Racing thoughts / worry
- [ ] Stress from work or relationships
- [ ] Sleep anxiety (worrying about not sleeping)
- [ ] Unprocessed emotions from the day

PHYSIOLOGICAL:
- [ ] Pain or discomfort
- [ ] Sleep apnea symptoms (snoring, gasping)
- [ ] Restless legs
- [ ] Medication side effects
- [ ] Hormonal changes
```

Flag any that suggest a medical issue — recommend a sleep specialist, not a self-help plan.

---

## Step 3: Design Sleep Environment

Optimize the physical space for sleep.

```
ENVIRONMENT CHANGES:
- Light: [specific changes — blackout curtains, remove LEDs, etc.]
- Sound: [white noise, earplugs, or address noise source]
- Temperature: [target 65-68F / 18-20C — specific changes]
- Bed: [any needed upgrades or changes]
- Association: [bed = sleep only — remove work, screens, eating]

COST ESTIMATE: [Low / Medium / High]
PRIORITY ORDER: [Which change first based on biggest disruptor]
```

---

## Step 4: Create Wind-Down Routine

Design a 30-60 minute pre-sleep routine that signals the brain to prepare for sleep.

```
WIND-DOWN PROTOCOL (start [time]):

T-60 min: [Activity — e.g., dim lights, stop screens]
T-45 min: [Activity — e.g., light reading, journaling, stretching]
T-30 min: [Activity — e.g., hygiene routine, calming tea]
T-15 min: [Activity — e.g., breathing exercises, meditation]
T-0:      Lights out

RULES:
- No screens after [time]
- No problem-solving after [time]
- If worried, write it down and close the notebook
```

Customize to what the person will actually do, not an ideal routine they'll abandon.

---

## Step 5: Set the Schedule

Consistency beats duration. Design a realistic schedule.

```
SCHEDULE:
- Wake time (every day, including weekends): [time]
- Earliest bedtime: [time]
- Latest bedtime: [time]
- Wind-down start: [time]

RULES:
- No alarm snoozing — one alarm, feet on floor
- Weekend deviation max: 30 minutes
- If can't sleep after 20 min: get up, do something boring, return when sleepy
- No clock-watching in bed
```

Anchor to wake time first — it's more controllable than sleep time.

---

## Step 6: Plan for Obstacles

Sleep plans fail when life gets complicated. Pre-solve the common disruptions.

```
OBSTACLE PLANS:

TRAVEL:
- [Specific adjustments for time zones, hotel rooms, jet lag]

STRESS PERIODS:
- [What to do when the mind won't stop — specific techniques]
- [Shortened routine for high-stress nights]

SOCIAL:
- [How to handle late dinners, events, social pressure to stay up]

BAD NIGHTS:
- [Protocol for the morning after poor sleep — no napping before 2pm, etc.]
- [How to avoid catastrophizing one bad night into a streak]

SCREENS:
- [Specific rules — blue light filters, charging station outside bedroom]
```

---

## Step 7: Implementation Plan

Roll out changes gradually, not all at once.

```
WEEK 1: [Fix the biggest disruptor + set consistent wake time]
WEEK 2: [Add wind-down routine + environment change]
WEEK 3: [Refine schedule + address secondary disruptors]
WEEK 4: [Full protocol — assess and adjust]

TRACKING: [What to measure — time to fall asleep, wake quality, energy at 3pm]
SUCCESS METRIC: [What "better sleep" specifically means for this person]
REVIEW DATE: [When to evaluate and adjust the plan]
```

---

## Integration

Use with:
- `/hab` -> To build sleep habits that stick
- `/obv` -> To catch obvious sleep mistakes being overlooked
- `/exrp` -> To align exercise timing with sleep optimization
- `/nutr` -> To coordinate nutrition timing with sleep goals
- `/efa` -> When sleep issues stem from emotional distress

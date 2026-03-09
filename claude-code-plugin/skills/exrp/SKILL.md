---
name: "exrp - Exercise Programming"
description: Design a structured exercise program tailored to current fitness level, goals, and real-world constraints.
---

# Exercise Programming

**Input**: $ARGUMENTS

---

## Step 1: Assess Current Fitness Level

Establish an honest baseline — programs fail when they start too hard or too easy.

```
CURRENT STATE:
- Training history: [None / Beginner (<1yr) / Intermediate (1-3yr) / Advanced (3+yr)]
- Current activity: [What they do now, how often]
- Injuries/limitations: [List any — these are hard constraints]
- Available time: [Hours per week for training]
- Available equipment: [Gym / Home / Bodyweight only / Specific equipment]
- Recovery capacity: [Sleep quality, stress level, age considerations]
```

If $ARGUMENTS doesn't specify, ask before proceeding. Bad programs come from bad assessments.

---

## Step 2: Identify Goals

Get specific. "Get fit" is not a goal. What does success look like in 12 weeks?

```
PRIMARY GOAL: [Specific — e.g., "Run 5K in under 30 minutes"]
SECONDARY GOAL: [e.g., "Build upper body strength"]
ANTI-GOALS: [What they want to avoid — e.g., "Don't want to bulk up"]

TIMELINE: [Target date or timeframe]
REALITY CHECK: Is this achievable given current level and constraints? [Yes / No — adjust]
```

If goals conflict (e.g., maximum strength + marathon), flag the trade-off and prioritize.

---

## Step 3: Select Training Modalities

Match modalities to goals, not preferences.

```
MODALITIES:
- Primary: [e.g., Resistance training — serves main goal]
- Secondary: [e.g., Zone 2 cardio — supports recovery and health]
- Tertiary: [e.g., Mobility work — prevents injury]

EXCLUDED: [What's not in the program and why]
```

| Goal | Primary Modality | Support Modality |
|------|-----------------|-----------------|
| Strength | Heavy resistance | Mobility, light cardio |
| Fat loss | Resistance + HIIT | Walking, nutrition (main driver) |
| Endurance | Sport-specific cardio | Resistance, flexibility |
| General health | Resistance + cardio mix | Mobility, play |
| Muscle gain | Hypertrophy training | Adequate nutrition, sleep |

---

## Step 4: Design Progressive Overload

The program must get harder over time, or it stops working.

```
PROGRESSION MODEL:

WEEKS 1-4 (Foundation):
- Volume: [sets x reps or duration]
- Intensity: [% effort or load]
- Focus: [Learn movements, build base]

WEEKS 5-8 (Build):
- Volume: [increase]
- Intensity: [increase]
- Focus: [Push capacity]

WEEKS 9-12 (Peak/Test):
- Volume: [adjust]
- Intensity: [peak]
- Focus: [Test against goals]

PROGRESSION RULE: [How to know when to increase — e.g., "When you hit all reps for 2 sessions, add weight"]
DELOAD: [Every 4th week, reduce volume 40-50%]
```

---

## Step 5: Plan Recovery

Training is the stimulus. Recovery is where adaptation happens.

```
RECOVERY PROTOCOL:
- Rest days per week: [minimum]
- Sleep target: [hours]
- Nutrition: [protein target, calorie context]
- Active recovery: [What to do on off days]
- Stress management: [High life stress = reduce training volume]

WARNING SIGNS (back off if these appear):
- Performance declining for 2+ sessions
- Persistent fatigue or soreness beyond 72 hours
- Sleep quality dropping
- Motivation consistently low
- Elevated resting heart rate
```

---

## Step 6: Create Weekly Schedule

Map the program to actual days, accounting for real life.

```
WEEKLY TEMPLATE:

MON: [Session type — e.g., Upper body strength, 45 min]
TUE: [e.g., Zone 2 cardio, 30 min]
WED: [e.g., Rest or mobility, 15 min]
THU: [e.g., Lower body strength, 45 min]
FRI: [e.g., Conditioning, 30 min]
SAT: [e.g., Full body or sport, 45 min]
SUN: [e.g., Rest]

TOTAL TIME: [hours/week]
NON-NEGOTIABLES: [Which sessions matter most if time is short]
FLEX SESSIONS: [Which can be skipped or shortened]
```

---

## Step 7: Define Metrics

What gets measured gets managed. What gets managed poorly gets gamed. Choose metrics carefully.

```
TRACK WEEKLY:
- [Metric 1 — e.g., Training volume (sets x reps x weight)]
- [Metric 2 — e.g., Resting heart rate]
- [Metric 3 — e.g., Energy level (1-10)]

TRACK MONTHLY:
- [Metric — e.g., Performance test against goal]
- [Metric — e.g., Body measurements if relevant]

IGNORE: [Metrics that will mislead — e.g., daily scale weight for fat loss]

12-WEEK TEST: [How to know if the program worked]
```

---

## Integration

Use with:
- `/slp` -> Sleep optimization to support recovery
- `/nutr` -> Nutrition planning aligned with training goals
- `/hab` -> To build consistent training habits
- `/gop` -> To set proper training goals
- `/obo` -> To identify obstacles to consistency

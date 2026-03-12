---
name: "nutr - Nutrition Planning"
description: Design a practical nutrition plan based on actual eating patterns, real constraints, and sustainable changes — not idealized diets.
output:
  format: "prose"
---

# Nutrition Planning

**Input**: $ARGUMENTS

---

## Step 1: Assess Current Eating Patterns

Start with reality, not aspiration. What does a typical week actually look like?

```
CURRENT PATTERNS:
- Meals per day: [number and rough timing]
- Cooking frequency: [daily / few times a week / rarely]
- Eating out: [frequency]
- Snacking: [pattern — when, what, why]
- Hydration: [rough daily water intake]
- Known problem areas: [e.g., late-night eating, skipping breakfast, sugar cravings]
- Dietary restrictions: [allergies, intolerances, ethical choices]
```

If $ARGUMENTS doesn't specify, ask. Plans built on assumptions fail.

---

## Step 2: Identify Goals

What specific outcome is this nutrition plan serving?

```
PRIMARY GOAL: [e.g., Lose 15 lbs, support training performance, manage energy]
SECONDARY GOAL: [e.g., Reduce sugar dependence, eat more vegetables]
TIMELINE: [Realistic timeframe]
PREVIOUS ATTEMPTS: [What's been tried before and why it failed]

REALITY CHECK:
- Is the goal achievable in the timeline? [Yes / No — adjust]
- Does it require a medical professional? [Flag if yes]
```

Distinguish between goals that need calorie management vs. goals that need food quality changes vs. both.

---

## Step 3: Calculate Requirements

Rough targets, not false precision. Bodies aren't calorimeters.

```
ESTIMATES:
- Calorie target: [range, not a single number]
- Protein: [g/day — typically 0.7-1g per lb bodyweight for active people]
- Minimum fiber: [25-35g/day]
- Hydration: [bodyweight in lbs / 2 = oz water minimum]

APPROACH:
- [ ] Calorie counting (if goal requires deficit/surplus)
- [ ] Portion-based (hand measures — palm = protein, fist = carbs, thumb = fats)
- [ ] Quality-focused (no counting — just improve food choices)
- [ ] Habit-based (change one thing at a time)

Pick the simplest approach that achieves the goal. Don't overcomplicate.
```

---

## Step 4: Design Meal Framework

Structure, not rigid meal plans. Frameworks survive; meal plans get abandoned on day 4.

```
MEAL FRAMEWORK:

BREAKFAST: [Template — e.g., protein + fiber + fruit]
  Examples: [2-3 specific options they'd actually eat]

LUNCH: [Template — e.g., protein + vegetables + starch]
  Examples: [2-3 options]

DINNER: [Template — e.g., protein + vegetables + fat]
  Examples: [2-3 options]

SNACKS (if needed): [Template — e.g., protein + fruit or vegetables + fat]
  Examples: [2-3 options]

RULES:
- Protein at every meal
- Vegetables at 2+ meals
- [1-2 specific rules based on their goals]
```

Build from foods they already eat and like. Gradually introduce new ones.

---

## Step 5: Plan for Obstacles

Nutrition plans die in restaurants, at parties, and at 10pm when willpower is gone.

```
OBSTACLE PLANS:

SOCIAL EATING:
- Restaurant strategy: [e.g., protein + vegetables, skip bread basket]
- Events: [e.g., eat before, choose the best available option, don't apologize]
- Alcohol: [specific rules if relevant — e.g., 2-drink limit, no sugary mixers]

TRAVEL:
- [Portable options, hotel strategies, airport food choices]

BUDGET:
- [Affordable protein sources, bulk cooking strategies, seasonal produce]

LOW WILLPOWER:
- [Pre-made meals ready to grab, healthy defaults stocked at home]
- [The "minimum viable meal" when everything falls apart]

CRAVINGS:
- [Strategy — delay 20 min, have a planned alternative, allow controlled indulgence]
```

---

## Step 6: Create Shopping Strategy

If the food isn't in the house, the plan fails. If junk food is in the house, willpower fails.

```
WEEKLY SHOPPING LIST TEMPLATE:
- Proteins: [4-5 staples they'll buy every week]
- Vegetables: [5-6 staples]
- Starches: [2-3 staples]
- Fats: [2-3 staples]
- Fruits: [2-3 staples]
- Pantry: [Seasonings, cooking oils, staple items]

SHOPPING RULES:
- Shop on [day] — same day each week
- Never shop hungry
- Prep [what] on [day] for the week
- Keep [specific items] stocked at all times
```

---

## Step 7: Implementation Plan

Change one thing at a time. Stack habits, don't overhaul.

```
WEEK 1: [Single change — e.g., add protein to breakfast]
WEEK 2: [Add one thing — e.g., prep lunches on Sunday]
WEEK 3: [Add one thing — e.g., replace evening snack]
WEEK 4: [Assess and adjust]

TRACKING: [What to monitor — energy, hunger, performance, body comp]
SUCCESS METRIC: [What "working" looks like for this person]
REVIEW DATE: [When to evaluate and adjust]

PERMISSION: One off-plan meal per week is built in, not a failure.
```

---

## Integration

Use with:
- `/exrp` -> To align nutrition with training goals
- `/slp` -> To coordinate meal timing with sleep optimization
- `/hab` -> To build sustainable eating habits
- `/obo` -> To identify obstacles to nutrition adherence
- `/gop` -> To set realistic nutrition goals

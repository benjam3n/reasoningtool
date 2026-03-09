---
name: "ovwlm - Overwhelmed"
description: "For when there's too much and you can't process. A systematic way to reduce what you're holding until you can hold it."
---

# OVWLM - Overwhelmed

**Input**: $ARGUMENTS

---

## Core Principles

1. **The feeling of overwhelm is not about quantity.** It's about the gap between what you're holding and what you can hold. Two things can be overwhelming if your capacity is depleted. Twenty things can be manageable if you have structure. The fix is reducing what you're holding, not doing more.

2. **Stop before sorting.** The impulse when overwhelmed is to frantically organize. But organizing requires cognitive capacity you don't have right now. Step one is always: stop moving.

3. **Everything feels urgent when you're overwhelmed.** Almost nothing actually is. The urgency is a symptom of the overwhelm, not a property of the tasks.

4. **You cannot think your way out of overwhelm.** You act your way out — one small thing at a time. Completion of even a trivial task restores a sense of agency.

---

## Phase 1: Stop

```
[O1] STOP.
    Everything feels urgent but nothing will explode in the next 10 minutes.
    If something literally will — handle that one thing, then come back.

[O2] BREATH_CHECK: Take one breath. Not a technique. Just one breath.

[O3] CAPACITY_CHECK: On a scale of 1-5, how fried are you right now?
  1 = Mildly stressed, can think clearly
  2 = Strained, thinking is harder than usual
  3 = Foggy, can't prioritize
  4 = Frozen, can't start anything
  5 = Shutdown, can barely function
```

If 4-5: Skip to Phase 2 and keep it extremely simple. One question at a time.

---

## Phase 2: Brain Dump

Get everything out of your head and onto a surface. Don't organize. Don't prioritize. Just dump.

```
[O4] EVERYTHING ON YOUR MIND (unfiltered, unordered):
  1.
  2.
  3.
  4.
  5.
  ...
  [Keep going until nothing else comes out]
```

Rules for the dump:
- No item too small ("reply to that text")
- No item too big ("figure out my career")
- No judgment ("this is stupid but...")
- Feelings count ("I'm angry at X")
- Vague is fine ("that thing I keep avoiding")

---

## Phase 3: Subtract

Now reduce the list. Don't add — only cross off.

```
[O5] NOT MINE TO SOLVE:
  Cross off anything that is someone else's responsibility.
  [List items removed and who they actually belong to]

[O6] WON'T MATTER IN A WEEK:
  Cross off anything that genuinely won't matter in 7 days.
  [List items removed and why they don't matter]

[O7] DUPLICATES OR SYMPTOMS:
  Cross off anything that's really the same item stated differently,
  or a symptom of another item on the list.
  [List items merged]

[O8] ALREADY IN MOTION:
  Cross off anything that's already happening and doesn't need your attention right now.
  [List items removed]
```

---

## Phase 4: What's Left

```
[O9] REMAINING ITEMS:
  1. [item]
  2. [item]
  3. [item]
  ...

[O10] COUNT: [number] items.
```

If the remaining list is still overwhelming (more than 7 items):
```
[O11] SECOND PASS: Of what's left, which 3 actually need attention TODAY?
  1. [item]
  2. [item]
  3. [item]

  Everything else goes on a "LATER" list. Not abandoned. Just not now.
```

---

## Phase 5: Pick the Smallest Thing

```
[O12] SMALLEST_ITEM: [the item from the remaining list that takes the least effort]
[O13] TIME_ESTIMATE: [how long — aim for under 15 minutes]
[O14] FIRST_PHYSICAL_ACTION: [the literal first thing to do — open the app, pick up the phone, write the first sentence]
```

Do that one thing. Just that one thing.

```
[O15] AFTER COMPLETING:
  - Cross it off.
  - Notice how that feels. Even a small completion shifts something.
  - Look at the list again. Pick the next smallest.
  - Repeat.
```

---

## Phase 6: Output

```
OVERWHELMED
===========

CAPACITY: [1-5]

BRAIN DUMP: [count] items total

SUBTRACTED:
  - Not mine: [count] items removed
  - Won't matter: [count] items removed
  - Duplicates: [count] items merged
  - In motion: [count] items removed

REMAINING: [count] items

DO NOW (smallest first):
  1. [item] — [first physical action] — [time estimate]
  2. [item] — [first physical action] — [time estimate]
  3. [item] — [first physical action] — [time estimate]

LATER (not abandoned, just not now):
  [remaining items]

REMEMBER:
  The list looked like [original count] things.
  It's actually [remaining count] things.
  And right now, you only need to do ONE of them.

READY FOR:
- /to [remaining items] — to sequence what's left into a plan
- /de [items] — to find dependencies between remaining items
- /iagca [list] — to compress and group related items
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Skipping the stop** | Jumping straight to organizing | Phase 1 is not optional. Stop first. |
| **Incomplete dump** | "That's everything" but tension remains | Keep asking "what else?" until truly empty |
| **Not subtracting enough** | Every item feels essential | Be ruthless in Phase 3. Most items survive the cut because of guilt, not importance. |
| **Picking the biggest thing** | Starting with the hardest item because it feels most urgent | Always start smallest. Agency comes from completion, not ambition. |
| **Organizing instead of doing** | Spending 30 minutes making a perfect plan instead of doing a 5-minute task | The plan is Phase 5: pick smallest, do it. That's the whole plan. |
| **Adding during subtraction** | "Oh and also I need to..." | Brain dump is Phase 2. Phase 3 is ONLY subtraction. |

---

## Depth Scaling

| Depth | Phases | Subtraction Rigor | Action Planning |
|-------|--------|-------------------|-----------------|
| 1x | Dump + pick smallest | Light pass | One action |
| 2x | Full dump + subtraction + pick | Full four-filter subtraction | Top 3 actions |
| 4x | Full + categorization of remaining | Deep subtraction + delegation analysis | Sequenced action plan |
| 8x | Full + pattern analysis of what causes overwhelm | Complete + systemic fixes | Full plan + prevention |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] User was told to stop before sorting
- [ ] Brain dump completed (everything out of head)
- [ ] Subtraction applied (not mine / won't matter / duplicates / in motion)
- [ ] Remaining list is manageable (ideally under 7)
- [ ] Smallest item identified with a concrete first action
- [ ] Tone is calm and non-judgmental throughout

---

## Integration

- Use from: "I'm overwhelmed", "too much", "I can't handle this", "everything is piling up"
- Routes to: `/to` (task sequencing), `/de` (dependency mapping), `/iagca` (scope compression)
- Differs from `/idk`: idk doesn't know what to do; ovwlm knows but there's too much
- Differs from `/cnfsd`: cnfsd can't understand; ovwlm can't process due to volume
- Differs from `/iagca`: iagca compresses scope analytically; ovwlm addresses the emotional and practical experience of overload first

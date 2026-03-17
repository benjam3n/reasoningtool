---
name: "improve - Improve It"
description: "Take something that works but could be better. Find the highest-leverage improvements and apply them. Not for broken things (/fix) — for things that work but underperform their potential."
output:
  format: "prose"
---

# Improve

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify what's being improved:

**Interpretation 1 — Code**: Working code that could be cleaner, faster, more maintainable, or better designed.
**Interpretation 2 — Skill/document**: A skill, plan, doc, or structured text that works but isn't good enough. Could be tighter, clearer, more effective.
**Interpretation 3 — Output**: Something produced in this conversation that was adequate but not great. Raise the quality bar.
**Interpretation 4 — Process/approach**: A way of doing things that works but leaves value on the table.

If the thing is BROKEN (errors, wrong output, fundamentally flawed), use `/fix` instead. `/improve` is for things that work but aren't as good as they could be.

---

## Core Principles

1. **Working is the baseline, not the goal.** Something can work and still be mediocre. The question is: what would make this genuinely good?
2. **Highest leverage first.** Find the improvement that produces the most quality gain for the least change. Don't rewrite what can be sharpened.
3. **Compare to the best, not the average.** What does excellent look like in this category? Where does this fall short of excellent?
4. **Improve the thing, not around it.** Don't add features, wrappers, or scaffolding. Make the core better.
5. **Know when to stop.** Diminishing returns are real. Call out when further improvement isn't worth the effort.

---

## Step 1: Read and Baseline

Read the entire target. While reading, establish:

**What is this trying to do?** (purpose)
**How well does it do it?** (current quality — rate 1-10 with one-line justification)
**What does excellent look like for this kind of thing?** (quality bar — find or name a concrete reference point)

```
PURPOSE: [what it's for]
CURRENT QUALITY: [N]/10 — [why]
QUALITY BAR: [what excellent looks like for this kind of thing]
GAP: [the distance between current and excellent]
```

---

## Step 2: Find Improvement Opportunities

Look for these in order. For each, state what's improvable and WHY it matters (not just that it could be different).

### Clarity
- Can someone unfamiliar understand this on first read?
- Are there sections that require re-reading?
- Is anything ambiguous where it should be precise?

### Density
- Is there filler, padding, or repetition that could be cut?
- Are there 3 sentences doing the work of 1?
- Does every section earn its space?

### Effectiveness
- Does it actually achieve its purpose as well as it could?
- Are there steps/sections that don't contribute to the goal?
- What's the weakest part relative to the purpose?

### Specificity
- Are instructions concrete enough to act on?
- Are there vague words ("consider," "may want to," "various") where specifics would help?
- Would two people following this produce the same result?

### Structure
- Does the order make sense?
- Are related things grouped together?
- Does the structure match how someone would actually use this?

### Completeness
- Is anything essential missing?
- Are edge cases handled?
- Does it handle the hard cases, not just the easy ones?

---

## Step 3: Prioritize

List all opportunities. Tag each:

```
IMPROVEMENTS:
[I1] [what to improve] — LEVERAGE: high/medium/low — EFFORT: high/medium/low
[I2] [what to improve] — LEVERAGE: high/medium/low — EFFORT: high/medium/low
...
```

**Do first**: high leverage + low effort
**Do next**: high leverage + high effort
**Skip unless asked**: low leverage + any effort

---

## Step 4: Apply Improvements

Execute the high-leverage improvements. Use Edit for targeted changes, Write for rewrites when >50% is changing.

For each improvement applied, the change should be visible in the diff — don't just describe what you'd change, CHANGE IT.

---

## Step 5: Re-baseline

After applying improvements:

```
BEFORE: [N]/10
AFTER: [N]/10
DELTA: +[N]

IMPROVEMENTS APPLIED: [N]
  [I1]: [one-line summary]
  [I2]: [one-line summary]
  ...

REMAINING OPPORTUNITIES (diminishing returns):
  [I-number]: [what and why it's not worth doing now]

QUALITY BAR MET: [yes/no — if no, what's still short]
```

---

## Depth Scaling

| Depth | Read | Find | Apply |
|-------|------|------|-------|
| 1x | Skim | Top 1-2 high-leverage | Quick improvements |
| 2x | Full read | All opportunities, prioritized | Apply high-leverage |
| 4x | Full read + context + comparisons | All opportunities + benchmark against best examples | Apply all worthwhile |
| 8x | Full read + context + history + user patterns | Full quality audit + structural analysis | Rewrite if needed, verify against quality bar |

Default: 2x.

---

## Anti-Failure Checks

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| **Taste-based changes** | "I'd prefer..." without quality justification | Every change must have a WHY rooted in clarity, density, effectiveness, specificity, structure, or completeness — not preference. |
| **Over-improvement** | Rewriting working sections that are already good | If it's already at 8/10, leave it. Improve the 4/10 parts. |
| **Feature creep** | Adding new capabilities instead of improving existing ones | Improve means make the EXISTING thing better, not add to it. |
| **Cosmetic improvement** | Reformatting, renaming, restyling without substance change | Ask: does this make the thing MORE EFFECTIVE or just different? |
| **Improvement without application** | Listed what to improve but didn't do it | Step 4 exists. Apply the changes. |
| **Wrong tool** | The thing is actually broken, not underperforming | Use `/fix` for broken things. `/improve` assumes working baseline. |

---

## Integration

- `/fix` → for broken things. If `/improve` discovers the thing is fundamentally broken, route to `/fix`.
- `/araw` → stress-test whether improvements actually make it better
- `/cmp` → compare before/after versions
- `/cls` → check improvements against specific quality criteria
- `/iterate` → for multiple rounds of improvement

---

**Execute now.**

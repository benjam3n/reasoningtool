---
name: "fowtdn - Figure Out What To Do Next"
description: "When you've been working through data or a problem and need to determine the single most valuable next action — assesses progress, identifies what changed, and picks the move that advances you most."
output:
  format: "prose"
---

# FOWTDN - Figure Out What To Do Next

**Input**: $ARGUMENTS

---

## Core Principles

1. **"Next" means you've already started.** This skill assumes prior work exists. If you're at the very beginning with raw data and no direction, use `/fowtd` first. This skill picks up mid-stream.

2. **What changed matters more than what exists.** The right next action depends on what's DIFFERENT since the last action — new information, resolved questions, shifted priorities, or surfaced problems. Start with the delta.

3. **Momentum is real and valuable.** If something is working, the default should be to continue it. Switching tracks has a cost. Only recommend a direction change if there's a clear reason.

4. **Diminishing returns are the main enemy.** The most common failure is continuing to do what you were doing past the point where it's producing value. Check for this explicitly.

5. **One action, not a revised plan.** The user wants to know what to do RIGHT NOW. Not a new roadmap. One move.

---

## Phase 1: Progress Check

Where are you now vs. where you started?

```
[N1] ORIGINAL_GOAL: [what the user was trying to accomplish]
[N2] WORK_DONE: [what has been completed so far]
[N3] CURRENT_STATE: [what the user has/knows NOW that they didn't before]
[N4] PROGRESS_LEVEL: [early | mid | late | stuck | lost]
```

### Progress Classification

| Level | Signals | Implication |
|-------|---------|-------------|
| **Early** | Just started, first pass done, initial triage complete | Next action should build on initial findings |
| **Mid** | Core work underway, some outputs produced, some gaps remaining | Next action should close the most important remaining gap |
| **Late** | Most work done, polishing, validating, or finalizing | Next action should be validation or completion |
| **Stuck** | Progress stalled, repeated attempts, circular work | Next action should break the loop — try a different approach |
| **Lost** | Goal unclear, direction confused, too many threads | Next action should be reorientation — `/fowtd` or `/iagca` |

---

## Phase 2: Delta Assessment

What's changed since the last action?

```
[N5] NEW_INFORMATION: [what you learned or received since last action]
[N6] RESOLVED_QUESTIONS: [uncertainties that are now settled]
[N7] NEW_QUESTIONS: [uncertainties that surfaced]
[N8] SHIFTED_PRIORITIES: [anything that's more or less important than before]
[N9] SURPRISES: [anything unexpected — positive or negative]
```

### Delta Impact

```
[N10] DELTA_IMPACT: [confirms direction | suggests adjustment | demands pivot]
```

| Impact | Meaning | Response |
|--------|---------|----------|
| **Confirms** | New info supports current direction | Continue, pick the natural next step |
| **Adjusts** | New info suggests a modification, not a change | Adjust and continue |
| **Demands pivot** | New info invalidates current approach | Stop current track, reassess |

If DEMANDS PIVOT:
```
[N11] PIVOT_REASON: [what specifically invalidated the current approach]
[N12] PIVOT_DIRECTION: [what the new direction should be]
```

---

## Phase 3: Remaining Work Scan

What's left to do?

```
[N13] REMAINING_ITEMS:
  - [item] — VALUE: [high | medium | low] — EFFORT: [quick | moderate | heavy]
  - [item] — VALUE: [value] — EFFORT: [effort]
  - [item] — VALUE: [value] — EFFORT: [effort]
```

### Value/Effort Matrix

| | Quick | Moderate | Heavy |
|--|-------|----------|-------|
| **High value** | DO NEXT | DO SOON | PLAN CAREFULLY |
| **Medium value** | DO NEXT | MAYBE | PROBABLY NOT |
| **Low value** | ONLY IF FREE | SKIP | SKIP |

---

## Phase 4: Next Action Selection

```
[N14] RECOMMENDED_NEXT: [one specific action]
[N15] WHY_THIS_NEXT: [why this action over the other remaining items]
[N16] WHAT_IT_PRODUCES: [concrete output or result]
[N17] DIMINISHING_RETURNS_CHECK: [is continuing the current track still the highest-value use of effort?]
```

### Selection Rules

- **If stuck**: don't do more of the same. Try a different angle, tool, or approach.
- **If late stage**: the next action should be finishing, validating, or shipping — not starting something new.
- **If new information surfaced**: address it before continuing the old plan.
- **If priorities shifted**: re-rank remaining work before picking.
- **If everything remaining is low-value**: the next action might be "stop — you're done enough."

---

## Phase 5: Output

```
FIGURE OUT WHAT TO DO NEXT
==========================

STARTED WITH: [original goal]
YOU'VE DONE: [brief summary of progress]
YOU'RE AT: [progress level]

WHAT CHANGED:
  [most important delta — new info, resolved question, or surprise]

REMAINING WORK: [count of items, with high-value count]
DIMINISHING RETURNS? [yes/no — is continued effort still high-value?]

→ DO THIS NEXT: [one specific action]
  WHY: [one sentence — why this over alternatives]
  PRODUCES: [what you'll have after doing it]
  SKILL: → INVOKE: /skill-id $ARGUMENTS

AFTER THAT:
  IF_GOOD: [likely next step if this works]
  IF_STUCK: [what to try if this doesn't produce results]
  IF_DONE: [how to know you can stop]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Continuing past diminishing returns** | Recommending more of the same when value is declining | Explicitly check: is this still the highest-value use of effort? |
| **Ignoring the delta** | Recommending the "planned" next step when new info changes things | Phase 2 must be done before Phase 4 — new info can change everything |
| **Restarting instead of continuing** | Sending user back to `/fowtd` when they have momentum | Only reorient if genuinely LOST, not just slightly uncertain |
| **Too many next steps** | "Do A, then B, then C" | ONE action. Route to `/fonss` if they need a sequence |
| **Not knowing when to stop** | Never outputs "you're done" | Check remaining work — if all low-value, recommend stopping |
| **Forward-only bias** | Never recommends revisiting or backtracking | Sometimes the best next step is to redo or reconsider a prior step |

---

## Depth Scaling

| Depth | Progress Check | Delta Analysis | Remaining Scan | Alternative Actions |
|-------|---------------|----------------|----------------|-------------------|
| 1x | Level only | Most important change | Top 3 items | 1 action |
| 2x | Level + evidence | Full delta | All items ranked | 2-3 actions, pick best |
| 4x | Full + trajectory | Delta + impact analysis | All items with value/effort | 4-5 actions, scored |
| 8x | Full + pattern check | Delta + second-order effects | Comprehensive with dependencies | Full action comparison |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Progress level assessed (not assumed)
- [ ] Delta identified — what's new since last action
- [ ] If delta demands pivot: pivot direction specified
- [ ] Remaining work scanned and ranked
- [ ] Diminishing returns explicitly checked
- [ ] ONE next action selected (not a sequence)
- [ ] Action is concrete and specific
- [ ] Recovery path specified (IF_STUCK)
- [ ] Completion condition specified (IF_DONE — how to know when to stop)
- [ ] Backtracking considered as valid option

---

## Integration

- Use from: user is mid-process and needs direction on what to do next
- Differs from `/fowtd`: fowtd starts from raw data with no direction; fowtdn picks up mid-stream
- Differs from `/next`: next is a general next-step router; fowtdn is specifically for data/work-in-progress
- Differs from `/wtdn`: wtdn is simpler — situation/goal/gap/move; fowtdn adds delta analysis and diminishing returns
- Differs from `/fonss`: fonss builds a multi-step chain; fowtdn picks ONE next action
- Routes to: whatever skill the next action requires
- Falls back to: `/fowtd` if user is actually lost and needs full reorientation

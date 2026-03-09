---
name: "next - Determine What to Do Next"
description: "Sub-orchestrator for next-step requests. Classifies intent, checks context, selects the single highest-value immediate action, and routes to execution or the right analysis skill."
---

# Next - Determine What to Do Next

**Input**: $ARGUMENTS

---

## Core Principles

1. **One step, not a roadmap.** This skill returns ONE next action. If the user needs a sequence, route to `/fonss`. The temptation to give five steps "for context" dilutes the recommendation and overwhelms the user.

2. **Classify before routing.** "What should I do next?" is almost never actually a next-step request. It's usually a decision, a diagnostic, a goal question, or method-seeking in disguise. Classify first, then route.

3. **Context determines everything.** The same words from different states need different skills. "What next?" when stuck = `/diagnose`. "What next?" when exploring = `/search`. "What next?" when everything is clear = `/action`.

4. **Backtracking is a valid next step.** Sometimes the right next action is to undo, reconsider, or restart. The skill must be able to recommend going backward, not just forward.

5. **Missing context is a finding, not a blocker.** If you can't determine the next step because the goal is unclear, THAT is the finding: "Your next step is to clarify the goal."

---

## Phase 1: Intent Classification

Is this actually a next-step request? Test against common disguises:

```
[N1] SURFACE_REQUEST: [what the user literally said]
[N2] ACTUAL_INTENT: [next-step | decision | method | diagnostic | exploration | goal-clarification | emotion]
```

### Classification Table

| Pattern | Actual Intent | Route |
|---------|--------------|-------|
| "Should I X or Y?" | Decision | → INVOKE: `/decide` $ARGUMENTS |
| "How do I X?" | Method-seeking | → INVOKE: `/how` $ARGUMENTS |
| "Why is X happening?" / "What went wrong?" | Diagnostic | → INVOKE: `/diagnose` $ARGUMENTS |
| "What are my options?" | Exploration | → INVOKE: `/search` $ARGUMENTS |
| "I want X" / "I need X" | Goal clarification | → INVOKE: `/want` $ARGUMENTS |
| "I'm stuck" / "I'm frustrated" | Emotion + diagnostic | → INVOKE: `/emotion` $ARGUMENTS |
| "What should I do next?" / "Now what?" | Genuine next-step | → Continue to Phase 2 |
| "Is this good?" / "Did I do it right?" | Evaluation | → INVOKE: `/evaluate` $ARGUMENTS |
| "Make this better" | Iteration | → INVOKE: `/iterate` $ARGUMENTS |

If routing away: output the reclassification and invoke immediately. Do not continue.

---

## Phase 2: Context Assessment

For genuine next-step requests, assess what's known:

```
[N3] GOAL: [stated or inferred goal]
[N4] DONE_SO_FAR: [what's been completed]
[N5] CURRENT_POSITION: [where in the process the user is]
[N6] BLOCKERS: [what's preventing progress, if anything]
[N7] AVAILABLE_INFORMATION: [what the user has to work with]
```

### Context Completeness

| Level | Has | Missing | Route |
|-------|-----|---------|-------|
| **Complete** | Goal + state + no blockers | — | → Phase 3 (select action) |
| **Blocked** | Goal + state + identified blocker | Blocker resolution | → `/diagnose` the blocker |
| **Partial** | Goal but unclear state or progress | Current position | → Ask user to state where they are |
| **Thin** | Vague goal, unclear state | Goal + state | → `/want` to clarify |
| **Recovery** | Prior attempt failed | Why it failed | → `/sbfow` to diagnose failure |

```
[N8] CONTEXT_LEVEL: [complete | blocked | partial | thin | recovery]
[N9] CONTEXT_ACTION: [proceed to Phase 3 | route to skill | ask user]
```

---

## Phase 3: Next-Step Selection

Given complete context, determine the single highest-value next action.

```
[N10] CANDIDATE_ACTIONS:
  [N11] ACTION: [specific action] — TYPE: [concrete task | analysis | decision | validation] — VALUE: [high | medium | low]
  [N12] ACTION: [specific action] — TYPE: [type] — VALUE: [level]
  [N13] ACTION: [specific action] — TYPE: [type] — VALUE: [level]
```

### Selection Criteria

| Criterion | Question |
|-----------|----------|
| **Dependency** | Does anything else need to happen before this can work? |
| **Unblocking power** | Does this action unblock other actions? |
| **Information gain** | Does this resolve uncertainty that's holding things up? |
| **Reversibility** | If wrong, how hard is this to undo? |
| **Timeliness** | Is there a reason to do this NOW vs later? |

### Routing Table

| Situation | Route |
|-----------|-------|
| Concrete task is obvious and ready | → `/action` $ARGUMENTS |
| Need method before acting | → `/how` $ARGUMENTS |
| Need evaluation before acting | → `/evaluate` $ARGUMENTS |
| Need to choose between options | → `/decide` $ARGUMENTS |
| Need more options before choosing | → `/search` $ARGUMENTS |
| Need to understand root cause | → `/diagnose` $ARGUMENTS |
| Need to undo or backtrack | State what to undo and why |
| Multiple steps needed | → `/fonss` $ARGUMENTS |

---

## Phase 4: Output

```
NEXT STEP:
  ACTION: [one specific thing to do]
  TYPE: [concrete task | analysis | decision | validation | backtrack]
  WHY_THIS_FIRST: [why this action is the highest-value next step]

  → INVOKE: /skill-id $ARGUMENTS

AFTER THIS STEP:
  CHECK: [what result to verify immediately after]
  IF_GOOD: [likely next step after this one]
  IF_BAD: [what to do if this step fails or produces weak output]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Misclassification** | Treated a decision as a next-step request | Phase 1 classification table must be checked first |
| **Roadmap output** | Returned 5 steps instead of 1 | Enforce single-step rule; route to `/fonss` for sequences |
| **Forward-only bias** | Never recommends backtracking | Explicitly check: is the right move to go backward? |
| **Context assumption** | Assumed goal/state without checking | Phase 2 must extract context from the prompt, not infer |
| **Generic routing** | Always routes to `/action` | Consider all routing options; `/action` is only for clear, concrete tasks |
| **Missing recovery path** | No IF_BAD in output | Always specify what to do if the step fails |

---

## Depth Scaling

| Depth | Candidates Generated | Classification Rigor | After-Step Analysis |
|-------|---------------------|---------------------|-------------------|
| 1x | 2 | Pattern match only | IF_GOOD only |
| 2x | 4 | Full classification table | IF_GOOD + IF_BAD |
| 4x | 6 | Classification + confidence | Full branch analysis |
| 8x | 8 | Classification + evidence | Multi-path scenarios |

Default: 2x. These are floors.

---

## Pre-Completion Checklist

- [ ] Intent classified (not assumed to be a next-step request)
- [ ] If reclassified: routed to correct skill immediately
- [ ] Context assessed with completeness level
- [ ] If context incomplete: addressed (ask user or route to clarifying skill)
- [ ] Single next step selected (not a roadmap)
- [ ] WHY_THIS_FIRST explicitly states why this beats alternatives
- [ ] Recovery path specified (IF_BAD)
- [ ] Backtracking considered as a valid option

---

## Integration

- Use from: user directly, `/meta`, `/handle`
- Differs from `/fonss`: fonss builds a multi-step chain; next picks ONE step
- Differs from `/wsib`: wsib picks the best skill for a prompt; next picks the best ACTION for a state
- Routes to: whatever skill the next step requires
- Escalates to: `/fonss` when multi-step chain is clearly needed

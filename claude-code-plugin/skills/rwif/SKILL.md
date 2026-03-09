---
name: "rwif - Real-World Interface"
description: "Bridge the gap between thinking/planning and physical execution. Converts plans into actionable checklists with logistics, failure modes, and contingencies."
---

# Real-World Interface

**Input**: $ARGUMENTS

---

## Step 1: Take the Plan or Decision

Accept a plan, decision, or intention and restate it clearly.

1. What has been decided or planned?
2. What is the desired end state in concrete, observable terms?
3. What is the timeline?

```
PLAN: [what was decided]
END STATE: [what "done" looks like in the physical world]
DEADLINE: [when, or "no hard deadline"]
```

If the input is vague ("I want to get healthier"), push back: this skill requires a specific plan or decision. Suggest `/gu` or `/gd` first to clarify the goal.

---

## Step 2: Identify Every Physical Action Required

Break the plan down into individual physical actions. "Physical" means things that happen in the real world, not just thinking or deciding.

For each action:
1. What specifically needs to be done?
2. Where does it happen? (location)
3. What materials, tools, or resources are needed?
4. Who does it? (if not just the user)
5. How long will it take?

```
ACTIONS:
1. [action] — Where: [location] — Needs: [materials] — Who: [person] — Time: [estimate]
2. [action] — Where: [location] — Needs: [materials] — Who: [person] — Time: [estimate]
...
```

Be granular. "Set up the office" is not an action. "Buy a desk from IKEA, transport it home, assemble it" is three actions.

---

## Step 3: Sequence by Logistics

Reorder actions based on real-world constraints:

1. **Dependencies**: What must happen before what?
2. **Location batching**: Group actions at the same location together
3. **Material dependencies**: What needs to be acquired before it can be used?
4. **Other people's schedules**: What requires coordination with others?
5. **Business hours**: What can only happen during specific times?
6. **Lead times**: What takes days/weeks to arrive or process?

```
SEQUENCED PLAN:

Phase 1: [name] — Target: [date/timeframe]
  [ ] [action 1]
  [ ] [action 2]

Phase 2: [name] — Target: [date/timeframe] — Depends on: Phase 1
  [ ] [action 3]
  [ ] [action 4]
...
```

Identify the critical path: the longest chain of dependent actions. This determines the minimum calendar time.

```
CRITICAL PATH: [action] -> [action] -> [action]
MINIMUM CALENDAR TIME: [estimate]
```

---

## Step 4: Create Actionable Checklists

Convert the sequenced plan into copy-paste-ready checklists.

Rules:
- Each item starts with a verb
- Each item is completable in one sitting
- Each item has clear "done" criteria
- Group by day or session, not just by phase
- Include preparation steps (e.g., "charge drill before Saturday")

```
CHECKLIST — [Phase/Day name]:
[ ] [verb] [specific action] [done when: criteria]
[ ] [verb] [specific action] [done when: criteria]
...
```

---

## Step 5: Identify Physical-World Failure Modes

The real world is messier than plans. For each phase, identify what could go wrong:

| Failure Mode | Likelihood | Impact | Example |
|---|---|---|---|
| **Availability** | [H/M/L] | [H/M/L] | Item out of stock, person unavailable |
| **Weather/environment** | [H/M/L] | [H/M/L] | Rain on moving day, construction noise |
| **Time underestimate** | [H/M/L] | [H/M/L] | Assembly takes 3x longer than expected |
| **Missing information** | [H/M/L] | [H/M/L] | Don't know the measurements until you're there |
| **Other people** | [H/M/L] | [H/M/L] | Contractor doesn't show, friend cancels |
| **Cost overrun** | [H/M/L] | [H/M/L] | Hidden fees, price changes, unexpected expenses |
| **Energy/motivation** | [H/M/L] | [H/M/L] | Decision fatigue, physical exhaustion |

```
TOP FAILURE RISKS:
1. [failure mode] — Phase [X] — Likelihood: [H/M/L], Impact: [H/M/L]
2. [failure mode] — Phase [X] — Likelihood: [H/M/L], Impact: [H/M/L]
...
```

---

## Step 6: Add Contingencies

For each top failure risk, define a contingency:

```
CONTINGENCIES:
1. If [failure mode]: then [specific alternative action]
2. If [failure mode]: then [specific alternative action]
...
```

Also add general buffers:
- **Time buffer**: Add 30-50% to total time estimate
- **Money buffer**: Add 15-25% to total cost estimate
- **Energy buffer**: Don't schedule the hardest tasks on the same day
- **Decision buffer**: Pre-decide as many choices as possible to avoid on-the-day decision fatigue

```
BUFFERED ESTIMATES:
- Time: [original] + [buffer] = [total]
- Cost: [original] + [buffer] = [total]
```

---

## Integration

Use with:
- `/to` -> Create the task breakdown that feeds into /rwif
- `/dcp` -> Make the decision, then /rwif to execute it
- `/spec` -> Test whether a speculative plan is physically feasible
- `/curd` -> Convert a learning plan into a concrete study schedule

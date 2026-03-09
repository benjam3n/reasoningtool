---
name: "pwif - Physical World Interface"
description: Bridge thinking to real-world action — account for physical logistics, materials, locations, time, and failure modes that pure reasoning ignores.
---

# Physical World Interface

**Input**: $ARGUMENTS

---

## Step 1: Identify Physical Actions Needed

Translate the abstract plan into concrete physical steps. What has to happen in the real world?

```
OBJECTIVE: [What needs to physically exist or change in the real world]

PHYSICAL ACTIONS:
1. [Action] — requires [physical thing: body, tool, material, location]
2. [Action] — requires [physical thing]
3. [Action] — requires [physical thing]
...

PURELY DIGITAL (no physical component):
- [Anything that can be done from a screen — separate these out]

PHYSICAL-DIGITAL BOUNDARY:
- [Where does the plan cross from thinking/digital into physical action?]
```

Most plans fail at the physical-digital boundary. A plan that says "order supplies" has hidden physical steps: receiving the delivery, storing the materials, having space to work.

---

## Step 2: Map Resources and Constraints

What do you have, what do you need, and what limits exist?

```
RESOURCES AVAILABLE:
- Tools/equipment: [What's on hand]
- Materials: [What's on hand]
- Space: [Where this will happen — specific location]
- People: [Who can help, their availability]
- Budget: [What money is available]
- Time: [Total time available and scheduling constraints]

RESOURCES NEEDED:
- [Item] — source: [where to get it] — cost: [estimate] — lead time: [how long to acquire]
- [Item] — source: [X] — cost: [X] — lead time: [X]

CONSTRAINTS:
- Location: [Where must this happen? Travel required?]
- Weather: [Relevant? Outdoor work, transport, etc.]
- Hours: [Business hours, daylight, noise restrictions]
- Physical capacity: [Lifting limits, skill requirements, number of hands needed]
- Permits/permissions: [Anything that requires approval before starting]
```

---

## Step 3: Sequence Actions for Physical Reality

Sequence matters differently in the physical world. You can't undo a cut board. You can't be in two places at once. Things take longer than you think.

```
SEQUENCING RULES APPLIED:
- [ ] Irreversible steps come last (measure twice, cut once)
- [ ] Acquisition before assembly (do you have everything before you start?)
- [ ] Drying/curing/shipping times built in (what has wait states?)
- [ ] Location changes minimized (batch errands, reduce trips)
- [ ] Dependencies respected (can't paint before priming)

ACTION SEQUENCE:

PHASE 1 — PREPARE:
1. [Action] — location: [where] — time: [estimate] — depends on: [nothing / action X]
2. [Action] — location: [where] — time: [estimate] — depends on: [action 1]

PHASE 2 — EXECUTE:
3. [Action] — location: [where] — time: [estimate] — depends on: [action 2]
4. [Action] — location: [where] — time: [estimate] — depends on: [action 3]

PHASE 3 — COMPLETE:
5. [Action] — location: [where] — time: [estimate]
6. [Cleanup / verification]

TOTAL TIME ESTIMATE: [Sum of sequential steps + buffer]
BUFFER ADDED: [20-50% depending on novelty — unfamiliar tasks get more buffer]
```

---

## Step 4: Create Checklists

Physical tasks benefit enormously from checklists. Brains forget things under load.

```
PRE-START CHECKLIST:
- [ ] All materials acquired and on-site
- [ ] Tools verified working
- [ ] Space prepared
- [ ] Help confirmed (if needed)
- [ ] Weather/conditions checked (if relevant)
- [ ] Permissions secured

EXECUTION CHECKLIST:
- [ ] [Step 1 — specific and verifiable]
- [ ] [Step 2]
- [ ] [Step 3]
- [ ] [Step 4]
...

COMPLETION CHECKLIST:
- [ ] [Outcome verified — does it work/look right?]
- [ ] [Cleanup done]
- [ ] [Tools returned / materials stored]
- [ ] [Next steps identified if this is part of a larger project]
```

---

## Step 5: Plan for Physical-World Failure Modes

The physical world is less forgiving than the digital world. Things break, weather changes, stores close, parts don't fit.

```
FAILURE MODES:

SUPPLY FAILURES:
- [Item unavailable] -> backup: [alternative source or substitute]
- [Wrong size/spec] -> mitigation: [return policy, adaptation]

EXECUTION FAILURES:
- [Measurement error] -> prevention: [measure twice, use guides]
- [Tool breaks] -> backup: [spare tool, rental option, manual alternative]
- [Skill gap] -> mitigation: [practice piece first, YouTube tutorial, call for help]

ENVIRONMENT FAILURES:
- [Weather] -> contingency: [reschedule trigger, indoor alternative]
- [Space unavailable] -> backup: [alternative location]
- [Noise/time restrictions] -> mitigation: [schedule around them]

HUMAN FAILURES:
- [Helper no-show] -> backup: [solo plan or alternative helper]
- [Fatigue/frustration] -> rule: [stopping point defined in advance]
- [Underestimated time] -> buffer: [what gets cut if running long]

ABORT CRITERIA: [When to stop and reassess rather than push through]
```

---

## Step 6: Final Reality Check

Before starting, run the plan through physical reality one more time.

```
REALITY CHECK:
- [ ] Have I actually been to the location / seen the space?
- [ ] Have I confirmed availability of materials (not just assumed)?
- [ ] Is the time estimate based on experience or optimism?
- [ ] Do I have a way to handle waste/debris/cleanup?
- [ ] Is there a point of no return — and am I ready for it?
- [ ] What's the minimum viable version if things go sideways?

GO / NO-GO: [Ready to start, or what needs to happen first]
```

---

## Integration

Use with:
- `/de` -> For project planning before bridging to physical execution
- `/to` -> For task ordering that feeds into physical sequencing
- `/obv` -> To catch obvious physical constraints being overlooked
- `/obo` -> To identify obstacles to physical execution
- `/dmgc` -> When physical execution goes wrong and damage control is needed

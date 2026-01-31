---
name: "pjm - Project Management Orderings"
description: "Orderings from formal project management — PERT, CPM, Critical Chain, Agile — for scheduling and resource management."
---

# Project Management Orderings

**Input**: $ARGUMENTS

---

## Overview

Formal project management has developed sophisticated methods for ordering work across teams, managing dependencies, and handling uncertainty. These work for any multi-step project with dependencies and resource constraints.

## Ordering Rules

### Rule 1: Critical Path Method (CPM)
- Map all tasks and dependencies
- Find the longest path through the network (critical path)
- Critical path tasks have zero slack — any delay delays the project
- Non-critical tasks have float — can be delayed without affecting completion
- **Order**: Critical path tasks get priority in scheduling and resources

### Rule 2: PERT — Account for Uncertainty
- For each task, estimate: optimistic, most likely, pessimistic duration
- Expected = (O + 4M + P) / 6
- Use expected durations for scheduling
- Variance tells you where uncertainty lives
- **Order**: high-variance tasks earlier (reduce uncertainty sooner)

### Rule 3: Critical Chain (CCPM)
- Remove individual task padding
- Add a single project buffer at the end
- Add feeding buffers where non-critical paths join critical
- **Order**: schedule aggressively, monitor buffer consumption

### Rule 4: Agile/Sprint
- Break work into time-boxed iterations (sprints)
- Each sprint delivers working increment
- Prioritize backlog each sprint by value
- **Order**: highest-value items each sprint, adjust between sprints

## Application

### Step 1: Map Dependencies
- What depends on what?
- → INVOKE: /de [tasks] for dependency extraction if needed

### Step 2: Identify Critical Path
- Which sequence of tasks is longest?
- Those tasks determine the minimum project duration

### Step 3: Schedule
- Critical path tasks scheduled first with full resources
- Non-critical tasks scheduled in float periods
- Buffers placed at merge points

## When to Use
- Multi-person projects with dependencies
- Deadline-driven work
- Resource-constrained scheduling

## Verification
- [ ] All tasks and dependencies mapped
- [ ] Critical path identified
- [ ] Buffers placed (not padded individual tasks)
- [ ] High-uncertainty tasks addressed early

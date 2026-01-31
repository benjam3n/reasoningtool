---
name: "td - Temporal/Deadline Orderings"
description: "Orderings driven by temporal constraints, deadlines, and timing requirements."
---

# Temporal/Deadline Orderings

**Input**: $ARGUMENTS

---

## Overview

When external deadlines dominate, order work by temporal constraints. What must happen by when, what converges when, and what can slip.

## Ordering Rules

### Rule 1: Earliest Deadline First (EDF)
- Process the item with the nearest deadline first
- Optimal for single-resource scheduling to meet all deadlines
- **When**: multiple items with different due dates

### Rule 2: Backward Schedule from Deadline
- Start from the deadline, work backward to find latest possible start dates
- Each task: latest finish = deadline (or successor's latest start)
- Latest start = latest finish - duration
- **When**: project scheduling, meeting fixed dates

### Rule 3: Time-Critical Path
- Focus on the sequence that determines total duration
- Accelerate this path; other paths have slack
- **When**: multi-path projects with a hard end date

### Rule 4: Convergence Point Scheduling
- When multiple streams must merge at a point (launch, event, integration)
- Schedule backward from convergence point
- Streams that take longest start first
- **When**: events, releases, coordinated deliveries

### Rule 5: Buffer Placement
- Don't pad individual tasks (Parkinson's law — work expands)
- Place time buffers at convergence points and project end
- Monitor buffer consumption for early warning
- **When**: uncertainty about task durations

## Application
1. Identify all deadlines and convergence points
2. Map dependencies
3. Schedule backward from deadlines
4. Identify critical path and focus resources there
5. Place buffers at merge points

## When to Use
- Deadline-driven projects, event planning
- Coordinated releases, any time-constrained work

## Verification
- [ ] All deadlines identified
- [ ] Backward schedule complete
- [ ] Critical path identified
- [ ] Buffers placed at merge points

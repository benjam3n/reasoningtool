---
name: "qs - Queue Scheduling Orderings"
description: "Orderings for managing queues — FIFO, priority queues, shortest job first, fair queuing."
---

# Queue Scheduling Orderings

**Input**: $ARGUMENTS

---

## Overview

When items arrive over time and must be processed, the scheduling discipline determines throughput, latency, and fairness. Different queue orderings optimize for different objectives.

## Ordering Rules

### Rule 1: FIFO — First In, First Out
- Process in arrival order
- Fair (no item is unfairly delayed), predictable
- **When**: fairness matters, items roughly equal in importance

### Rule 2: Priority Queue
- Process highest-priority items first regardless of arrival
- Danger: low-priority items may starve
- Add aging to prevent starvation (priority increases with wait time)
- **When**: items have clearly different importance

### Rule 3: Shortest Job First (SJF)
- Process quickest items first
- Minimizes average wait time
- Danger: long jobs may starve
- **When**: minimizing throughput time, items vary in size

### Rule 4: Round Robin
- Give each item/category a time slice
- Cycle through all items
- Fair, prevents starvation, but may not optimize throughput
- **When**: multiple consumers, fairness required

### Rule 5: Weighted Fair Queuing
- Combine priority with fairness
- Higher-priority items get more processing time but all get some
- **When**: need both priority and fairness

## Application

### Step 1: Identify Optimization Goal
- Minimize average wait → SJF
- Maximize fairness → FIFO or Round Robin
- Maximize important items → Priority Queue
- Balance → Weighted Fair Queuing

### Step 2: Implement Queue Discipline
- Set up the ordering mechanism
- Add starvation prevention if using priority-based

### Step 3: Monitor
- Track wait times, throughput, starvation indicators
- Adjust weights/priorities based on outcomes

## When to Use
- Task management, support ticket triage, job scheduling
- Any system with incoming items that need processing

## Verification
- [ ] Optimization goal identified
- [ ] Queue discipline matches goal
- [ ] Starvation prevention in place (if priority-based)
- [ ] Metrics tracked

---
name: "faa - Fairness Allocation Orderings"
description: "Orderings that balance competing priorities, prevent starvation, and allocate resources proportionally across stakeholders."
---

# Fairness Allocation Orderings

**Input**: $ARGUMENTS

---

## Overview

When multiple stakeholders, categories, or priorities compete for limited resources or attention, pure optimization creates starvation — some things never get served. Fairness orderings ensure proportional allocation while still prioritizing.

## Core Principle

No priority should be permanently starved. High-priority items go first, but lower-priority items must eventually be served. Fairness is about proportional allocation over time, not equal allocation at each moment.

## Ordering Rules

### Rule 1: Weighted Fair Queuing
- Assign weights to each category based on importance
- Serve in proportion to weights (e.g., 60/30/10 split)
- Over any window, allocation should approximate the weights
- **When**: ongoing resource allocation across categories

### Rule 2: Aging — Priority Increases with Wait Time
- Items that have been waiting longest get priority boosts
- Prevents starvation: even low-priority items eventually rise
- **When**: queues where some items keep getting skipped

### Rule 3: Round Robin with Weighted Turns
- Cycle through all categories, giving each a turn
- Higher-priority categories get more turns per cycle
- **When**: regular, predictable allocation needed

### Rule 4: Minimum Guarantee + Best Effort
- Each category gets a guaranteed minimum allocation
- Remaining resources allocated by priority
- **When**: some categories have hard minimums (SLAs, commitments)

## Application Procedure

### Step 1: Identify Stakeholders/Categories
- Who/what competes for resources?
- What are the priority weights?
- Are there minimum guarantees?

### Step 2: Choose Mechanism
- Continuous flow → Weighted Fair Queuing
- Discrete items → Round Robin or Aging
- Hard minimums → Minimum Guarantee + Best Effort

### Step 3: Monitor and Adjust
- Track actual allocation vs intended proportions
- Adjust weights if priorities change
- Watch for starvation (any category getting <50% of its fair share)

## When to Use
- Team workload distribution, project portfolio allocation
- Feature prioritization across user segments
- Any recurring allocation across competing needs

## Verification
- [ ] All stakeholders identified and weighted
- [ ] No category permanently starved
- [ ] Allocation approximately matches weights over time
- [ ] Minimum guarantees met

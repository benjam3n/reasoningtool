---
name: "ct - Crisis Triage Orderings"
description: "Orderings for resource-constrained emergencies where not everything can be addressed and you must maximize outcomes with limited resources."
---

# Crisis Triage Orderings

**Input**: $ARGUMENTS

---

## Overview

When resources are insufficient to address everything, you must choose what to save and what to let go. Triage orderings maximize total positive outcomes by allocating limited resources to where they have the most impact. This means explicitly not helping some things.

## Core Principle

Help the ones you can help most. Not the worst cases (may be unsavable), not the easiest (waste of scarce resources on what would survive anyway), but the ones where your intervention makes the biggest difference.

## Ordering Rules

### Rule 1: Impact per Resource Unit
- For each item needing help: (value if saved - value if not saved) / resources required
- Process in descending order of this ratio
- **When**: resources are the binding constraint

### Rule 2: Triage Categories
Classify everything into:
- **Immediate (T1)**: will fail without intervention, intervention will likely succeed → DO FIRST
- **Delayed (T2)**: needs help but can wait → DO SECOND
- **Minor (T3)**: will survive without intervention → DO LAST or skip
- **Expectant (T4)**: will fail regardless of intervention → DON'T ALLOCATE RESOURCES
- **When**: mixed severity, need rapid sorting

### Rule 3: Cascade Prevention
- Prioritize items where failure would cause additional failures
- Stop cascading failures before addressing isolated ones
- **When**: interconnected systems where failures propagate

### Rule 4: Reversibility Window
- Prioritize items with closing time windows
- An item that can be saved now but not in an hour goes before one that can be saved anytime
- **When**: time-sensitive with varying deadlines

## Application Procedure

### Step 1: Inventory
- What needs attention?
- What resources are available?
- What are the time constraints?

### Step 2: Classify
- Assign each item a triage category (T1-T4)
- Estimate resources needed and likelihood of success for each

### Step 3: Execute
- Address T1 items in order of cascade risk and closing windows
- Move to T2 when T1 is handled
- Accept that T4 items will not be addressed

### Step 4: Reassess
- Triage is not static — reassess as conditions change
- T2 items may become T1; T1 items may become T4

## Anti-Patterns
- Spending all resources on the worst case (T4 thinking)
- First-come-first-served (ignores severity)
- Refusing to let anything go (spreads resources too thin, everything fails)

## When to Use
- System outages with multiple failures
- Project crises with limited time
- Any situation with more problems than resources

## Verification
- [ ] All items inventoried
- [ ] Triage categories assigned
- [ ] Resources allocated to highest-impact items
- [ ] Unsavable items explicitly deprioritized
- [ ] Reassessment scheduled

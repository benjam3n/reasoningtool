---
name: to
description: Generate valid execution sequences from dependencies. Respects hard constraints, optimizes for priorities, and identifies parallel execution opportunities.
---

# Topological Ordering

**Input**: $ARGUMENTS

---

## Purpose

Given items with dependencies, generate a **valid execution order** that:
1. Respects all hard dependencies (nothing runs before its prerequisites)
2. Honors soft preferences where possible
3. Optimizes for priority (important things early)
4. Identifies parallelization opportunities

**Prerequisites**: Dependencies extracted (use `/de` first)

---

## Core Algorithm

Topological sort guarantees: If A -> B, then A appears before B in the sequence.

```
ALGORITHM:
1. Find items with no dependencies (ready to start)
2. Execute/schedule those items
3. Remove them from the graph
4. Repeat until all items scheduled

If stuck (no items with zero dependencies): CYCLE DETECTED -> error
```

---

## The Process

### Step 1: Input Dependencies

```
DEPENDENCIES FOR: [procedure name]

Items: [N total]

Dependency list:
- [Item 2] depends on [Item 1]
- [Item 3] depends on [Item 2]
- [Item 4] depends on [Item 1]
- [Item 5] depends on [Item 3], [Item 4]
...

Priority scores (if available):
- [Item X]: HIGH (must be early)
- [Item Y]: MEDIUM
- [Item Z]: LOW (can be late)
```

---

### Step 2: Identify Starting Points

Find items with no incoming dependencies:

```
STARTING POINTS (no prerequisites):

- [Item 1] - Ready immediately
- [Item 6] - Ready immediately (independent track)

These can begin in parallel or sequentially.
```

---

### Step 3: Check for Cycles

Before ordering, verify no circular dependencies:

```
CYCLE CHECK:

Checking for cycles...
- [Item 1] -> [Item 2] -> [Item 3] -> ... [x] No cycle back to Item 1
- [Item A] -> [Item B] -> [Item A] [!] CYCLE DETECTED

RESULT: [No cycles found / CYCLES FOUND - see below]
```

**If cycles found:**
```
CYCLE DETECTED:
[Item A] -> [Item B] -> [Item C] -> [Item A]

This means:
- A needs B to complete
- B needs C to complete
- C needs A to complete
- IMPOSSIBLE to order!

RESOLUTION OPTIONS:
1. Remove one dependency (which is weakest?)
2. Merge items into single step
3. Introduce intermediate checkpoint
4. Re-examine: Is this really a hard dependency?
```

---

### Step 4: Generate Base Order

Apply topological sort:

```
TOPOLOGICAL SORT:

Round 1 - No dependencies:
  -> Schedule: [Item 1], [Item 6]
  -> Remove from graph

Round 2 - Dependencies now satisfied:
  -> Schedule: [Item 2], [Item 4] (both depended only on Item 1)
  -> Remove from graph

Round 3 - Dependencies now satisfied:
  -> Schedule: [Item 3] (depended on Item 2)
  -> Remove from graph

Round 4 - Dependencies now satisfied:
  -> Schedule: [Item 5] (depended on Item 3, Item 4 - both done)
  -> Remove from graph

BASE ORDER: [1, 6, 2, 4, 3, 5]
```

---

### Step 5: Apply Priority Optimization

If multiple items can run at same point, order by priority:

```
PRIORITY OPTIMIZATION:

At Round 2, both [Item 2] and [Item 4] are ready.
- Item 2: Priority HIGH
- Item 4: Priority MEDIUM

Optimized: [Item 2] before [Item 4]

PRIORITY-OPTIMIZED ORDER: [1, 6, 2, 4, 3, 5]
(Item 6 moved early because it's independent and can start immediately)
```

---

### Step 6: Identify Parallel Execution

Group items that can execute simultaneously:

```
PARALLEL EXECUTION GROUPS:

Group 1 (can start immediately):
  |-- [Item 1]
  |-- [Item 6]

Group 2 (after Group 1):
  |-- [Item 2] (after Item 1)
  |-- [Item 4] (after Item 1)

Group 3 (after Group 2):
  |-- [Item 3] (after Item 2)

Group 4 (after Item 3 AND Item 4):
  |-- [Item 5]

PARALLEL TIMELINE:
Time ->
|- Group 1: [Item 1] || [Item 6]
|- Group 2: [Item 2] || [Item 4]
|- Group 3: [Item 3]
|- Group 4: [Item 5]

Minimum steps with parallelization: 4
Sequential steps without: 6
Speedup: 33%
```

---

### Step 7: Generate Output Formats

#### Linear Sequence (for step-by-step execution)
```
SEQUENTIAL ORDER:

1. [Item 1] - [description]
2. [Item 6] - [description]
3. [Item 2] - [description]
   Depends on: Step 1
4. [Item 4] - [description]
   Depends on: Step 1
5. [Item 3] - [description]
   Depends on: Step 3
6. [Item 5] - [description]
   Depends on: Steps 4, 5
```

#### Parallel Schedule (for project planning)
```
PARALLEL SCHEDULE:

Phase 1:
  [ ] [Item 1]
  [ ] [Item 6]
  --- Phase 1 complete ---

Phase 2 (after Phase 1):
  [ ] [Item 2]
  [ ] [Item 4]
  --- Phase 2 complete ---

Phase 3 (after Phase 2):
  [ ] [Item 3]
  --- Phase 3 complete ---

Phase 4 (after Phase 3):
  [ ] [Item 5]
  --- DONE ---
```

#### Gantt-style (for timeline visualization)
```
GANTT VIEW:

Item    | T1 | T2 | T3 | T4 | T5 |
--------|----|----|----|----|----|
Item 1  | ██ |    |    |    |    |
Item 6  | ██ |    |    |    |    |
Item 2  |    | ██ |    |    |    |
Item 4  |    | ██ |    |    |    |
Item 3  |    |    | ██ |    |    |
Item 5  |    |    |    | ██ |    |
```

---

## Handling Special Cases

### Multiple Valid Orders

When dependencies allow multiple valid sequences:

```
MULTIPLE VALID ORDERS:

Order A: [1, 2, 4, 3, 5] - Frontend first
Order B: [1, 4, 2, 3, 5] - Backend first
Order C: [1, 2, 3, 4, 5] - Sequential

All are valid. Choose based on:
- Priority (what's most important?)
- Resources (what's available?)
- Risk (what reduces uncertainty?)

RECOMMENDED: [Order based on rationale]
```

### Soft Dependencies

Handle soft dependencies (~>) as preferences, not requirements:

```
SOFT DEPENDENCY HANDLING:

Hard order (must respect):
[Item 1] -> [Item 2] -> [Item 3]

Soft preferences (try to respect):
[Item 2] ~> [Item 4] (prefer 2 before 4, but not required)

If conflict with hard dependency: Ignore soft
If no conflict: Honor soft preference
```

### External Dependencies

Mark waiting points for external dependencies:

```
EXTERNAL DEPENDENCY HANDLING:

Order: [1, 2, 3, WAIT, 4, 5]

After Step 3:
  || WAIT FOR: [External approval]
  Action: [How to request/obtain]
  Timeout: [What if not received]

After wait resolved:
  Continue with Step 4
```

---

## Example: API Development Workflow

### Input
Items: Design, Implement, Test, Document, Review, Deploy
Dependencies:
- Implement -> Design
- Test -> Implement
- Document -> Design
- Review -> Implement, Test
- Deploy -> Review

### Topological Sort

```
Round 1: Design (no deps) -> Schedule
Round 2: Implement, Document (both need only Design) -> Schedule
Round 3: Test (needs Implement) -> Schedule
Round 4: Review (needs Implement, Test) -> Schedule
Round 5: Deploy (needs Review) -> Schedule
```

### Output

```
SEQUENTIAL ORDER:
1. Design
2. Implement (after Design)
3. Document (after Design) - can parallel with Implement
4. Test (after Implement)
5. Review (after Implement, Test)
6. Deploy (after Review)

PARALLEL SCHEDULE:
Phase 1: Design
Phase 2: Implement || Document
Phase 3: Test
Phase 4: Review
Phase 5: Deploy

Minimum phases: 5
```

---

## Quality Checklist

Before completing:
- [ ] All dependencies input
- [ ] Starting points identified
- [ ] Cycle check passed
- [ ] Base topological order generated
- [ ] Priority optimization applied
- [ ] Parallel groups identified
- [ ] Output format appropriate for use case
- [ ] Special cases handled

---

## Next Steps

After ordering:
1. Use `/pv` to verify order is complete and valid
2. Execute in the generated order
3. Track progress against parallel schedule

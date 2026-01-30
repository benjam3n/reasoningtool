---
name: de
description: Extract dependencies between steps, tasks, or items. Identifies what must happen before what, enabling proper sequencing and parallel execution.
---

# Dependency Extraction

**Input**: $ARGUMENTS

---

## Purpose

Given a list of steps, tasks, or items, extract the **dependencies** between them:
- What must happen before what?
- What can happen in parallel?
- What are the hard blockers vs soft preferences?

This enables `/topological_ordering` to generate valid sequences.

---

## Dependency Types

| Type | Symbol | Meaning | Example |
|------|--------|---------|---------|
| **Hard** | `->` | Must complete before | "Install DB -> Create tables" |
| **Soft** | `~>` | Preferably before | "Write docs ~> Review docs" |
| **Parallel** | `||` | Can happen simultaneously | "Frontend || Backend" |
| **Conditional** | `?->` | Depends if condition met | "If API needed ?-> Build API" |
| **External** | `[ext]->` | Depends on external factor | "[User approval]-> Deploy" |

---

## The Process

### Step 1: List All Items

```
ITEMS TO ANALYZE:

1. [Item/Step 1]
2. [Item/Step 2]
3. [Item/Step 3]
...
N. [Item/Step N]

TOTAL: [N] items
```

---

### Step 2: For Each Item, Ask Dependency Questions

For each item, systematically ask:

```
DEPENDENCY ANALYSIS: [Item X]

INPUTS (what does this need?):
- Data/information needed: [list]
- Resources needed: [list]
- Decisions needed: [list]
- Artifacts needed: [list]

OUTPUTS (what does this produce?):
- Data/information produced: [list]
- Artifacts produced: [list]
- State changes: [list]

PREREQUISITES (what must exist before starting?):
- [Prerequisite 1] -> from [Item Y]
- [Prerequisite 2] -> from [Item Z]
- [Prerequisite 3] -> EXTERNAL: [source]

ENABLES (what can start after this completes?):
- [Item A] can start
- [Item B] can start
```

---

### Step 3: Build Dependency Matrix

Create a matrix showing all dependencies:

```
DEPENDENCY MATRIX:

        | Item1 | Item2 | Item3 | Item4 | Item5 |
--------|-------|-------|-------|-------|-------|
Item1   |   -   |       |       |       |       |
Item2   |   ->   |   -   |       |       |       |
Item3   |       |   ->   |   -   |       |       |
Item4   |   ->   |       |       |   -   |       |
Item5   |       |       |   ->   |   ~>  |   -   |

Legend: -> = hard dependency, ~> = soft, blank = independent
Read as: Row depends on Column
(Item2 depends on Item1, Item3 depends on Item2, etc.)
```

---

### Step 4: Identify Dependency Chains

Trace the longest dependency chains:

```
DEPENDENCY CHAINS:

Chain 1 (Critical Path):
[Item 1] -> [Item 2] -> [Item 3] -> [Item 5]
Length: 4 steps

Chain 2:
[Item 1] -> [Item 4]
Length: 2 steps

CRITICAL PATH: Chain 1 (longest, determines minimum time)
```

---

### Step 5: Identify Parallel Opportunities

Find items with no dependencies between them:

```
PARALLEL OPPORTUNITIES:

Can run in parallel:
- [Item 2] || [Item 4] (both depend only on Item 1)
- [Item 6] || [Item 7] (independent of each other)

Parallel groups:
Group A: {Item 2, Item 4} - after Item 1
Group B: {Item 6, Item 7} - after Item 3
```

---

### Step 6: Flag External Dependencies

Identify dependencies on things outside the procedure:

```
EXTERNAL DEPENDENCIES:

| Item | External Dependency | Type | Risk |
|------|---------------------|------|------|
| [Item 3] | User approval | Decision | May delay |
| [Item 5] | API key from vendor | Resource | Blocking |
| [Item 7] | Market data | Information | Timing |

MITIGATION:
- [Item 3]: Get pre-approval or define approval criteria
- [Item 5]: Request API key early, add buffer time
- [Item 7]: Identify backup data source
```

---

### Step 7: Output Dependency Graph

```
DEPENDENCY GRAPH: [procedure name]

[Item 1] (START - no dependencies)
    |
    |---> [Item 2]
    |        |
    |        |---> [Item 3]
    |                 |
    |                 |---> [Item 5] (END)
    |
    |---> [Item 4]
              |
              |--~> [Item 5]

SUMMARY:
- Total items: [N]
- Hard dependencies: [X]
- Soft dependencies: [Y]
- External dependencies: [Z]
- Parallel opportunities: [P groups]
- Critical path length: [L steps]
- Items on critical path: [list]
```

---

## Dependency Extraction Shortcuts

For common patterns, use these shortcuts:

### Linear Procedures
If steps are naturally sequential:
```
Step 1 -> Step 2 -> Step 3 -> Step 4
(Simple chain, extract only exceptions)
```

### Phased Projects
If work is organized in phases:
```
Phase 1 items (all parallel within phase)
    |
    |---> Phase 2 items (all parallel within phase)
            |
            |---> Phase 3 items
```

### Input-Process-Output
If following IPO pattern:
```
[All inputs] -> [Process] -> [All outputs]
```

---

## Example: Software Feature Development

### Input Items
1. Write requirements
2. Design UI mockups
3. Build backend API
4. Build frontend
5. Write tests
6. Code review
7. Deploy to staging
8. QA testing
9. Deploy to production

### Dependency Analysis

```
DEPENDENCY MATRIX:

           | Req | UI | API | FE | Test | Rev | Stg | QA | Prod |
-----------|-----|----|----|----|----- |-----|-----|----|----- |
Req        |  -  |    |    |    |      |     |     |    |      |
UI         |  ->  |  - |    |    |      |     |     |    |      |
API        |  ->  |    |  - |    |      |     |     |    |      |
FE         |  ->  |  -> |  -> |  - |      |     |     |    |      |
Test       |     |    |  -> |  -> |   -  |     |     |    |      |
Rev        |     |    |  -> |  -> |   ~> |  -  |     |    |      |
Stg        |     |    |    |    |      |  ->  |  -  |    |      |
QA         |     |    |    |    |      |     |  ->  |  - |      |
Prod       |     |    |    |    |      |     |     |  -> |   -  |
```

### Parallel Opportunities
- UI || API (both depend only on Requirements)
- Tests || Code Review (both depend on API + FE)

### Critical Path
Req -> API -> FE -> Review -> Staging -> QA -> Production
(7 steps on critical path)

### Output Graph
```
[Requirements]
    |
    |---> [UI Mockups] --+
    |                   |
    |---> [Backend API] -+---> [Frontend] ---> [Code Review] ---> [Staging]
              |                   |              |                |
              |-------------------+---> [Tests] ~-+                |
                                                                  ->
                                                            [QA Testing]
                                                                  |
                                                                  ->
                                                          [Production]
```

---

## Quality Checklist

Before completing:
- [ ] All items listed
- [ ] Each item analyzed for inputs/outputs
- [ ] Dependency matrix created
- [ ] Chains identified
- [ ] Parallel opportunities found
- [ ] External dependencies flagged
- [ ] Critical path determined
- [ ] Graph output generated

---

## Next Steps

After dependency extraction:
1. Use `/topological_ordering` to generate valid sequence
2. Use `/procedure_validation` to verify all dependencies satisfiable

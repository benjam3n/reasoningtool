---
name: "funcanalysis - Functional Analysis"
description: Decompose system functions into subfunctions, define functional interfaces, allocate functions to physical components, and trace functions to requirements. Produces a functional decomposition tree and allocation matrix.
output:
  format: "table"
---

# Functional Analysis

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Decompose functions for a new system**: The user has a system with top-level functions (from requirements or ConOps) and wants to systematically break them down into subfunctions, define flows, and allocate to components.
**Interpretation 2 — Analyze functional gaps in an existing system**: The user has an existing system and wants to verify that all required functions are present, properly decomposed, and correctly allocated — identifying gaps or redundancies.
**Interpretation 3 — Reallocate functions after architecture change**: The user has changed their system architecture or components and needs to re-map which functions go where, updating allocations and interface definitions.

If ambiguous, ask: "I can help with decomposing functions for a new system, analyzing gaps in an existing decomposition, or reallocating functions after an architecture change — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/funcanalysis 4x [input]").

| Depth | Min Top-Level Functions | Decomposition Levels | Min Subfunctions | Min Functional Interfaces | Min Traceability Links |
|-------|------------------------|---------------------|-----------------|--------------------------|----------------------|
| 1x    | 3                      | 2                   | 12              | 6                        | 10                   |
| 2x    | 5                      | 3                   | 25              | 12                       | 20                   |
| 4x    | 8                      | 3                   | 45              | 20                       | 35                   |
| 8x    | 12                     | 4                   | 70              | 35                       | 55                   |
| 16x   | 18                     | 4                   | 110             | 55                       | 90                   |

---

## The Process

### Step 1: Identify Top-Level Functions

Derive top-level functions from the system's mission, requirements, or ConOps:

```
SYSTEM: [name]
PURPOSE: [one sentence]

TOP-LEVEL FUNCTIONS:

| # | Function ID | Function Name | Description | Source | Trigger | Output |
|---|------------|---------------|-------------|--------|---------|--------|
| 1 | F1 | [verb + noun, e.g., "Process Sensor Data"] | [what this function accomplishes] | [requirement ID or ConOps scenario] | [what initiates this function] | [what it produces] |
| 2 | F2 | [verb + noun] | [description] | [source] | [trigger] | [output] |
...

FUNCTION NAMING CONVENTION:
- Always use "Verb + Noun" format
- Verbs: Process, Generate, Detect, Transmit, Store, Validate, Control, Monitor, Display, Calculate, Transform, Route, Authenticate, Log
- Be specific: "Process Sensor Data" not "Handle Data"

TOP-LEVEL FUNCTIONAL FLOW:

[F1: Receive Input] → [F2: Validate Input] → [F3: Process Data] → [F4: Generate Output] → [F5: Deliver Output]
                                  ↓ (invalid)                              ↕
                          [F6: Handle Error]                    [F7: Store Results]
                                                                       ↕
                                                              [F8: Monitor Performance]
```

---

### Step 2: Decompose into Subfunctions

For each top-level function, decompose into subfunctions. Continue until each subfunction is assignable to a single component:

```
FUNCTIONAL DECOMPOSITION:

F1: [Top-Level Function Name]
├── F1.1: [Subfunction Name]
│   ├── F1.1.1: [Sub-subfunction]
│   └── F1.1.2: [Sub-subfunction]
├── F1.2: [Subfunction Name]
│   ├── F1.2.1: [Sub-subfunction]
│   └── F1.2.2: [Sub-subfunction]
└── F1.3: [Subfunction Name]

DECOMPOSITION TABLE:

| Function ID | Function Name | Parent | Level | Description | Input | Output | Processing | Performance Req |
|------------|---------------|--------|-------|-------------|-------|--------|-----------|----------------|
| F1 | [name] | — | 0 | [description] | [what goes in] | [what comes out] | [what happens] | [timing/throughput] |
| F1.1 | [name] | F1 | 1 | [description] | [input] | [output] | [processing] | [perf req] |
| F1.1.1 | [name] | F1.1 | 2 | [description] | [input] | [output] | [processing] | [perf req] |
...

DECOMPOSITION RULES APPLIED:
- [ ] Each parent function is fully covered by its children (no gaps)
- [ ] No child function exceeds the scope of its parent (no overlaps upward)
- [ ] Sibling functions do not overlap (no redundancy)
- [ ] Leaf functions are small enough to assign to one component
- [ ] Each function has clear input, output, and processing
```

---

### Step 3: Define Functional Interfaces

```
FUNCTIONAL FLOW BLOCK DIAGRAM (FFBD):

For each top-level function, define the flow between subfunctions:

FLOW: [Top-Level Function Name]

| Step | From Function | To Function | Data/Control Passed | Condition | Timing |
|------|--------------|-------------|-------------------|-----------|--------|
| 1 | [F1.1] | [F1.2] | [what is passed] | [always/conditional] | [sequential/parallel] |
| 2 | [F1.2] | [F1.3] | [what is passed] | [if condition X] | [sequential] |
| 2a | [F1.2] | [F1.4] | [what is passed] | [if condition Y] | [parallel with step 2] |
...

FUNCTIONAL INTERFACE TABLE:

| # | Interface ID | From Function | To Function | Data Item | Format | Rate | Direction |
|---|-------------|---------------|-------------|-----------|--------|------|-----------|
| 1 | FI-001 | [F1.1] | [F1.2] | [data name] | [type/schema] | [items/sec] | [→ / ← / ↔] |
...

CONTROL INTERFACES:

| # | Control Signal | From | To | Meaning | Response |
|---|---------------|------|----|---------|----------|
| 1 | [signal name] | [function] | [function] | [what it means] | [what recipient does] |
...

INTERFACE COMPLETENESS CHECK:
- [ ] Every function output is consumed by at least one other function (or is a system output)
- [ ] Every function input is produced by at least one other function (or is a system input)
- [ ] No orphan data items (produced but never consumed)
- [ ] No phantom inputs (consumed but never produced)
```

---

### Step 4: Allocate Functions to Physical Components

```
FUNCTION-TO-COMPONENT ALLOCATION MATRIX:

| Function ID | Function Name | Component | Rationale | Shared? |
|------------|---------------|-----------|-----------|---------|
| F1.1.1 | [name] | [component name] | [why this component] | [YES — also in component X / NO] |
...

ALLOCATION MATRIX (cross-reference view):

| Function ↓ \ Component → | Comp A | Comp B | Comp C | Comp D | ... |
|--------------------------|--------|--------|--------|--------|-----|
| F1.1 | P | | | | |
| F1.2 | | P | S | | |
| F1.3 | | | P | | |
| F2.1 | P | | | | |
...

Legend: P = Primary (performs the function), S = Supports (contributes to the function)

ALLOCATION RULES APPLIED:
- [ ] Every leaf function is allocated to at least one component
- [ ] No component has conflicting functions allocated to it
- [ ] Functions requiring tight coupling are co-located on the same component
- [ ] Functions requiring isolation are on separate components
- [ ] Shared functions are identified with clear ownership

COMPONENT LOADING:

| Component | Functions Allocated | Estimated Load | Capacity | Utilization |
|-----------|-------------------|---------------|----------|-------------|
| [component] | [count] | [estimate] | [capacity] | [%] |
...
```

---

### Step 5: Trace Functions to Requirements

```
FUNCTION-TO-REQUIREMENT TRACEABILITY:

| Function ID | Function Name | Requirement IDs | Trace Type |
|------------|---------------|-----------------|-----------|
| F1.1 | [name] | [R1, R3, R7] | [derives from / satisfies / partially satisfies] |
...

REQUIREMENT COVERAGE ANALYSIS:

| Requirement ID | Requirement | Functions Addressing | Coverage |
|---------------|-------------|---------------------|----------|
| R1 | [requirement text] | [F1.1, F2.3] | FULL/PARTIAL/NONE |
...

GAPS FOUND:

| # | Gap Type | Detail | Impact | Resolution |
|---|---------|--------|--------|-----------|
| 1 | Uncovered Requirement | [R15 has no function mapped to it] | [requirement won't be met] | [add function or clarify requirement] |
| 2 | Orphan Function | [F3.2 traces to no requirement] | [unnecessary work or missing requirement] | [remove function or add requirement] |
| 3 | Partial Coverage | [R8 only partially covered by F2.1] | [requirement partially met] | [add subfunctions or refine allocation] |
...

BIDIRECTIONAL TRACEABILITY SUMMARY:
- Requirements with full coverage: [N] / [total]
- Requirements with partial coverage: [N] / [total]
- Requirements with no coverage: [N] / [total]
- Functions with no requirement trace: [N] / [total]
```

---

## Output Format

```
## FUNCTIONAL ANALYSIS: [System Name]

### 1. Top-Level Functions
[Function list with triggers and outputs]

### 2. Functional Decomposition Tree
[Hierarchical breakdown with decomposition table]

### 3. Functional Flow Block Diagrams
[Flow sequences for each top-level function]

### 4. Functional Interfaces
[Interface table with data items, rates, and directions]

### 5. Function-to-Component Allocation
[Allocation matrix with rationale]

### 6. Requirements Traceability
[Bidirectional traceability matrix with coverage analysis]

### 7. Gaps and Issues
[Uncovered requirements, orphan functions, allocation issues]

### 8. Open Questions
[Items requiring further decomposition or stakeholder input]
```

---

## Quality Checklist

Before completing:
- [ ] All top-level functions identified from requirements/ConOps
- [ ] Functions named with verb+noun convention
- [ ] Decomposition complete — leaf functions assignable to single components
- [ ] No gaps in decomposition (parent fully covered by children)
- [ ] No overlaps between sibling functions
- [ ] Functional flows defined for each top-level function
- [ ] All functional interfaces documented with data items
- [ ] No orphan outputs or phantom inputs
- [ ] Every leaf function allocated to at least one component
- [ ] Component loading assessed
- [ ] Bidirectional traceability established (functions ↔ requirements)
- [ ] Coverage gaps identified with proposed resolutions

---

## Next Steps

After functional analysis:
1. Use `/sysarch` to refine architecture based on functional allocation
2. Use `/requirements` to address uncovered requirements or add missing ones
3. Use `/tradestudy` to evaluate alternative functional allocations
4. Use `/de` to map dependencies between functions
5. Use `/fla` to identify failure modes in functional flows
6. Use `/conops` to validate functions support operational scenarios

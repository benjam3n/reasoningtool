---
name: "sysdecomp - System Decomposition"
description: Break a complex system into manageable subsystems and components using structured decomposition. Defines component responsibilities, interactions, and validates completeness of the breakdown.
output:
  format: "table"
---

# System Decomposition

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Decompose a new system concept into subsystems**: The user has a system idea or high-level description and needs to break it down into manageable components with clear responsibilities, interfaces, and hierarchy.
**Interpretation 2 — Refactor an existing decomposition**: The user has an existing system structure that has become unwieldy, has unclear boundaries, or needs reorganization to better match requirements or constraints.
**Interpretation 3 — Allocate requirements to components**: The user has both a set of requirements and a preliminary architecture, and needs to systematically assign each requirement to specific components and verify complete allocation.

If ambiguous, ask: "I can help with decomposing a new system from scratch, refactoring an existing system structure, or allocating requirements to components — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/sysdecomp 4x [input]").

| Depth | Min Components | Min Decomposition Levels | Min Interfaces Defined | Min Interactions Mapped | Min Criteria Checked |
|-------|---------------|-------------------------|----------------------|------------------------|---------------------|
| 1x    | 5             | 2                       | 4                    | 4                      | 3                   |
| 2x    | 12            | 3                       | 10                   | 10                     | 5                   |
| 4x    | 25            | 4                       | 20                   | 25                     | 7                   |
| 8x    | 50            | 5                       | 40                   | 50                     | 9                   |
| 16x   | 100           | 6                       | 80                   | 100                    | 12                  |

---

## The Process

### Step 1: Identify Decomposition Criteria

Choose the primary decomposition strategy based on system characteristics:

| Criterion | When to Use | Strengths | Risks |
|-----------|------------|-----------|-------|
| **Functional** | System has clearly distinct functions | Clear responsibilities, maps to requirements | May miss cross-cutting concerns |
| **Physical** | Hardware-heavy system, geographic distribution | Maps to procurement, manufacturing | May obscure logical relationships |
| **Behavioral** | System has distinct operating modes or states | Good for real-time, event-driven systems | Can create redundant components |
| **Data/Information** | Data processing or information-centric system | Good cohesion around data ownership | May create coupling through shared data |
| **Organizational** | Must align with team structure (Conway's Law) | Easy to assign ownership | May not be technically optimal |
| **Layered** | Clear abstraction levels exist | Clean dependencies, swappable layers | Can force awkward layer placement |
| **Service-oriented** | Needs independent deployment, scaling | Flexibility, independent evolution | Interface complexity, distributed system costs |

```
DECOMPOSITION STRATEGY:

SYSTEM: [name]
PRIMARY CRITERION: [functional / physical / behavioral / data / organizational / layered / service]
JUSTIFICATION: [why this criterion fits]

SECONDARY CRITERION: [if hybrid approach needed]
JUSTIFICATION: [why a second dimension is needed]

CONSTRAINTS ON DECOMPOSITION:
- [technical constraints — e.g., latency requires co-location]
- [organizational constraints — e.g., team boundaries]
- [deployment constraints — e.g., must run on single node]
- [regulatory constraints — e.g., separation of concerns for audit]
```

---

### Step 2: Perform Top-Down Decomposition

Start from the system level and break down iteratively:

```
LEVEL 0 — SYSTEM:
[System Name]: [one-sentence purpose]

LEVEL 1 — SUBSYSTEMS:
├── SS-1: [Subsystem Name] — [purpose]
├── SS-2: [Subsystem Name] — [purpose]
├── SS-3: [Subsystem Name] — [purpose]
└── SS-4: [Subsystem Name] — [purpose]

LEVEL 2 — COMPONENTS (expand each subsystem):
├── SS-1: [Subsystem Name]
│   ├── C-1.1: [Component Name] — [purpose]
│   ├── C-1.2: [Component Name] — [purpose]
│   └── C-1.3: [Component Name] — [purpose]
├── SS-2: [Subsystem Name]
│   ├── C-2.1: [Component Name] — [purpose]
│   └── C-2.2: [Component Name] — [purpose]
...

LEVEL 3 — SUB-COMPONENTS (if needed):
├── C-1.1: [Component Name]
│   ├── SC-1.1.1: [Sub-component Name] — [purpose]
│   └── SC-1.1.2: [Sub-component Name] — [purpose]
...
```

System Breakdown Structure (SBS) table:

| ID | Name | Parent | Level | Type | Purpose | Owner |
|----|------|--------|-------|------|---------|-------|
| S-0 | [System] | — | 0 | System | [purpose] | [who] |
| SS-1 | [Subsystem] | S-0 | 1 | Subsystem | [purpose] | [who] |
| SS-2 | [Subsystem] | S-0 | 1 | Subsystem | [purpose] | [who] |
| C-1.1 | [Component] | SS-1 | 2 | Component | [purpose] | [who] |
| C-1.2 | [Component] | SS-1 | 2 | Component | [purpose] | [who] |
| C-2.1 | [Component] | SS-2 | 2 | Component | [purpose] | [who] |
...

---

### Step 3: Define Component Responsibilities (Single Responsibility)

For each component, verify it has a single, clear responsibility:

```
COMPONENT RESPONSIBILITY MATRIX:

| Component | Primary Responsibility | Does NOT Handle | Cohesion Check |
|-----------|----------------------|-----------------|----------------|
| C-1.1 | [one clear job] | [things it delegates] | HIGH/MED/LOW |
| C-1.2 | [one clear job] | [things it delegates] | HIGH/MED/LOW |
...
```

For each component, apply the Single Responsibility Test:

| Test | Question | Pass? |
|------|----------|-------|
| **Elevator pitch** | Can you describe this component's job in one sentence without "and"? | |
| **Reason to change** | Does this component have exactly one reason to change? | |
| **Name test** | Is the component name a specific noun (not a vague term like "Manager" or "Handler")? | |
| **Size test** | Is the component neither too large (god component) nor too small (trivial wrapper)? | |
| **Dependency test** | Does this component depend on fewer than [N] other components? | |

---

### Step 4: Identify Component Interactions

Map how components communicate:

```
INTERACTION MATRIX:

          | C-1.1 | C-1.2 | C-2.1 | C-2.2 | C-3.1 |
----------|-------|-------|-------|-------|-------|
C-1.1     |  —    | [D/E] | [D/E] |       |       |
C-1.2     | [D/E] |  —    |       |       | [D/E] |
C-2.1     | [D/E] |       |  —    | [D/E] |       |
C-2.2     |       |       | [D/E] |  —    |       |
C-3.1     |       | [D/E] |       |       |  —    |

D = Data flow, E = Event/signal, C = Control flow, blank = no interaction
```

Interface specification for each interaction:

| From | To | Interface Name | Mechanism | Data Exchanged | Frequency | Protocol | Error Handling |
|------|----|---------------|-----------|----------------|-----------|----------|----------------|
| C-1.1 | C-1.2 | [name] | [API/message/shared mem/file] | [what data] | [sync/async, rate] | [protocol] | [what if fails] |
| C-1.2 | C-3.1 | [name] | [API/message/shared mem/file] | [what data] | [sync/async, rate] | [protocol] | [what if fails] |
...

Coupling assessment:

| Coupling Type | Description | Found Between | Severity |
|--------------|-------------|---------------|----------|
| **Content** | One component modifies internals of another | [components] | CRITICAL — eliminate |
| **Common** | Components share global data | [components] | HIGH — reduce |
| **Control** | One component controls flow of another | [components] | MEDIUM — watch |
| **Stamp** | Components share composite data structures | [components] | MEDIUM — watch |
| **Data** | Components share only needed data | [components] | LOW — acceptable |
| **Message** | Components communicate via messages only | [components] | LOW — ideal |

---

### Step 5: Validate Decomposition Completeness

Verify every requirement is allocated to at least one component:

```
REQUIREMENT ALLOCATION MATRIX:

| Requirement ID | Description | Allocated To | Allocation Type |
|---------------|-------------|-------------|-----------------|
| REQ-001 | [description] | C-1.1 | Primary |
| REQ-002 | [description] | C-1.2, C-2.1 | Shared |
| REQ-003 | [description] | ??? | ORPHAN — needs allocation |
...

ALLOCATION SUMMARY:
  Total Requirements: [N]
  Allocated: [N]
  Orphaned (no component): [N] — ACTION REQUIRED
  Shared (multiple components): [N] — verify coordination
```

Functional coverage check:

| Check | Question | Status |
|-------|----------|--------|
| No orphan requirements | Every requirement is allocated to at least one component | PASS/FAIL |
| No gold-plated components | Every component traces to at least one requirement | PASS/FAIL |
| No hidden functions | All system-level functions are covered by the decomposition | PASS/FAIL |
| Cross-cutting concerns | Logging, security, error handling allocated | PASS/FAIL |
| External interfaces | All external system interfaces have a component responsible | PASS/FAIL |

---

### Step 6: Check Decomposition Depth

Verify the decomposition is neither too shallow nor too deep:

| Indicator | Too Shallow | Just Right | Too Deep |
|-----------|------------|------------|----------|
| **Component size** | Contains multiple distinct responsibilities | Single clear responsibility | Trivially simple, no real logic |
| **Team assignment** | No team can own it alone | One team can own and deliver it | Multiple components per person |
| **Testability** | Cannot be tested independently | Can be unit-tested in isolation | Test is trivial / not worth writing |
| **Estimability** | Cannot estimate effort | Can estimate with reasonable confidence | Estimates are in hours, not days |
| **Reusability** | Not reusable (too specific + too large) | Potentially reusable in other contexts | So generic it has no meaning |
| **Change impact** | Changes affect many unrelated functions | Changes are localized | Changes require coordinating many tiny pieces |

```
DEPTH ASSESSMENT:

| Component | Current Level | Assessment | Recommendation |
|-----------|--------------|------------|----------------|
| C-1.1 | 2 | Too shallow — has 3 distinct responsibilities | Decompose further |
| C-1.2 | 2 | Just right — single responsibility, testable | Keep |
| SC-1.1.1 | 3 | Too deep — trivial wrapper | Merge into parent |
...
```

---

## Output Format

```
## SYSTEM BREAKDOWN STRUCTURE: [System Name]

### Decomposition Strategy
Primary criterion: [criterion]
Levels: [N]
Total components: [N]

### Hierarchy
[Tree diagram of system → subsystems → components]

### Component Registry
[Table: ID, Name, Parent, Level, Purpose, Owner, Responsibility]

### Interface Catalog
[Table: From, To, Mechanism, Data, Protocol]

### Requirement Allocation
[Table: Requirement → Component mapping]
Orphan requirements: [N]
Gold-plated components: [N]

### Coupling Assessment
[Summary of coupling types found and recommendations]

### Depth Assessment
[Components that need further decomposition or merging]

### Open Questions
[Decisions needed about decomposition boundaries]
```

---

## Quality Checklist

Before completing:
- [ ] Decomposition criterion chosen and justified
- [ ] All components have single, clear responsibility
- [ ] All interactions between components identified and specified
- [ ] Every requirement allocated to at least one component
- [ ] No gold-plated components (components without requirements)
- [ ] Coupling assessed and high-coupling areas flagged
- [ ] Decomposition depth assessed (not too shallow, not too deep)
- [ ] Cross-cutting concerns allocated (logging, security, error handling)
- [ ] External interfaces have owning components
- [ ] Component naming is consistent and specific

---

## Next Steps

After system decomposition:
1. Use `/requirements` to verify all requirements are well-specified before allocation
2. Use `/tracematrix` to formalize requirement-to-component traceability
3. Use `/de` to map dependencies between components
4. Use `/testplan` to design integration tests for component interfaces
5. Use `/lcca` to estimate costs per component and subsystem
6. Use `/tpm` to assign technical performance measures to critical components
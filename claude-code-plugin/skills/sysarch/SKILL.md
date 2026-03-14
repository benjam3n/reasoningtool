---
name: "sysarch - System Architecture Design"
description: Design system architecture from requirements by decomposing into subsystems, defining interfaces, evaluating candidate architectures against quality attributes, and documenting architectural views (functional, physical, behavioral).
output:
  format: "document"
---

# System Architecture Design

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Design architecture for a new system**: The user has requirements or a ConOps and wants to create a system architecture — subsystem decomposition, interface definitions, and architectural patterns.
**Interpretation 2 — Evaluate and compare candidate architectures**: The user has multiple architectural options and wants to systematically evaluate them against quality attributes and constraints to select the best one.
**Interpretation 3 — Refactor or evolve an existing architecture**: The user has an existing system architecture that needs modification — new requirements, performance issues, or technical debt — and wants to redesign while preserving what works.

If ambiguous, ask: "I can help with designing a new architecture, evaluating candidate architectures against each other, or evolving an existing architecture — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/sysarch 4x [input]").

| Depth | Min Subsystems | Min Interfaces | Min Quality Attributes | Min Candidate Archs | Min Views |
|-------|---------------|---------------|----------------------|---------------------|----------|
| 1x    | 3             | 4             | 4                    | 2                   | 2        |
| 2x    | 6             | 8             | 6                    | 3                   | 3        |
| 4x    | 10            | 15            | 8                    | 4                   | 4        |
| 8x    | 16            | 25            | 10                   | 5                   | 5        |
| 16x   | 25            | 40            | 12                   | 6                   | 6        |

---

## The Process

### Step 1: Identify Architectural Drivers

Determine the key requirements and constraints that shape the architecture:

```
SYSTEM: [name]
PURPOSE: [one sentence]

ARCHITECTURAL DRIVERS:

| # | Driver | Type | Source | Priority | Architecture Impact |
|---|--------|------|--------|----------|-------------------|
| 1 | [driver] | [functional/quality/constraint] | [requirement ID or stakeholder] | CRITICAL/HIGH/MED | [how it shapes architecture] |
...

KEY QUALITY ATTRIBUTES (ranked by importance):

| Rank | Quality Attribute | Scenario | Stimulus | Response | Measure |
|------|------------------|----------|----------|----------|---------|
| 1 | [e.g., Performance] | [specific scenario] | [what triggers it] | [desired behavior] | [measurable target] |
| 2 | [e.g., Modifiability] | [specific scenario] | [what triggers it] | [desired behavior] | [measurable target] |
| 3 | [e.g., Availability] | [specific scenario] | [what triggers it] | [desired behavior] | [measurable target] |
...

QUALITY ATTRIBUTE TRADE-OFFS:

| Attribute A | Attribute B | Tension | Resolution Strategy |
|------------|------------|---------|-------------------|
| Performance | Security | [encryption adds latency] | [define acceptable latency budget] |
| Modifiability | Performance | [abstraction adds overhead] | [identify hot paths to optimize] |
...

CONSTRAINTS:

| # | Constraint | Type | Non-Negotiable? | Impact on Architecture |
|---|-----------|------|-----------------|----------------------|
| 1 | [constraint] | [technical/organizational/business/regulatory] | YES/NO | [how it constrains choices] |
...
```

---

### Step 2: Generate Candidate Architectures

Define at least the minimum number of candidate architectures:

```
CANDIDATE ARCHITECTURE [N]: [Name]

PATTERN: [e.g., Layered, Microservices, Pipe-and-Filter, Event-Driven, Client-Server, Monolithic, SOA, Hexagonal]

RATIONALE: [Why this pattern is a candidate — what drivers it addresses well]

SUBSYSTEM DECOMPOSITION:

| # | Subsystem | Responsibility | Key Technology | Dependencies |
|---|-----------|---------------|----------------|-------------|
| 1 | [name] | [what it does] | [technology choice] | [other subsystems] |
...

HIGH-LEVEL STRUCTURE:

[Subsystem A] ←→ [Subsystem B]
       ↕                ↕
[Subsystem C] ←→ [Subsystem D]
       ↕
[External System]

KEY DESIGN DECISIONS:
- [Decision 1]: [choice made and why]
- [Decision 2]: [choice made and why]
...

STRENGTHS:
- [What this architecture does well]
...

WEAKNESSES:
- [Where this architecture struggles]
...

RISKS:
- [What could go wrong with this approach]
...
```

---

### Step 3: Evaluate Against Quality Attributes

```
ARCHITECTURE EVALUATION MATRIX:

| Quality Attribute | Weight | Arch 1: [name] | Arch 2: [name] | Arch 3: [name] |
|------------------|--------|----------------|----------------|----------------|
| [attribute 1] | [1-5] | Score [1-5]: [rationale] | Score [1-5]: [rationale] | Score [1-5]: [rationale] |
| [attribute 2] | [1-5] | Score [1-5]: [rationale] | Score [1-5]: [rationale] | Score [1-5]: [rationale] |
...
| **Weighted Total** | | **[sum]** | **[sum]** | **[sum]** |

SENSITIVITY ANALYSIS:
- If [quality attribute X] weight increases by 1: [which architecture wins]
- If [quality attribute Y] weight decreases by 1: [which architecture wins]
- Result is [robust/sensitive] to weight changes

COST-BENEFIT COMPARISON:

| Factor | Arch 1 | Arch 2 | Arch 3 |
|--------|--------|--------|--------|
| Development Cost | [LOW/MED/HIGH] | | |
| Operational Cost | [LOW/MED/HIGH] | | |
| Time to First Delivery | [estimate] | | |
| Team Skill Match | [LOW/MED/HIGH] | | |
| Technology Maturity | [LOW/MED/HIGH] | | |
| Scalability Ceiling | [estimate] | | |
```

---

### Step 4: Select and Document Architecture

```
SELECTED ARCHITECTURE: [Name]

DECISION RATIONALE:
- Selected because: [primary reasons]
- Over [Arch 2] because: [key differentiator]
- Over [Arch 3] because: [key differentiator]
- Accepted risks: [what risks we accept with this choice]
- Mitigations: [how we address the weaknesses]

ARCHITECTURAL PRINCIPLES:
| # | Principle | Rationale | Implication |
|---|-----------|-----------|------------|
| 1 | [e.g., "Loose coupling between subsystems"] | [why] | [what this means for design decisions] |
...
```

---

### Step 5: Define Subsystem Responsibilities

```
SUBSYSTEM DETAIL:

For each subsystem:

SUBSYSTEM: [Name]
RESPONSIBILITY: [Single sentence — what it does and ONLY what it does]

| Aspect | Detail |
|--------|--------|
| Functions | [what functions it performs] |
| Data Owned | [what data it is responsible for] |
| Quality Requirements | [specific quality targets for this subsystem] |
| Technology Stack | [languages, frameworks, platforms] |
| Deployment | [how and where it runs] |
| Team Ownership | [who builds and maintains it] |

SUBSYSTEM RESPONSIBILITY MATRIX:

| Responsibility | Sub 1 | Sub 2 | Sub 3 | Sub 4 | ... |
|---------------|-------|-------|-------|-------|-----|
| [responsibility 1] | R | | C | | |
| [responsibility 2] | | R | | C | |
...

Legend: R = Responsible, C = Contributes, I = Informed
```

---

### Step 6: Define Interfaces

```
INTERFACE CATALOG:

| # | Interface | From | To | Type | Protocol | Data Exchanged | Frequency | Criticality |
|---|-----------|------|----|------|----------|---------------|-----------|-------------|
| 1 | [name] | [subsystem] | [subsystem] | [sync/async/event/shared-data] | [HTTP/gRPC/message queue/file/etc.] | [what data] | [calls/sec or events/day] | [CRITICAL/HIGH/MED/LOW] |
...

INTERFACE DETAIL (for each critical interface):

INTERFACE: [Name]
FROM: [Subsystem A] → TO: [Subsystem B]

| Aspect | Detail |
|--------|--------|
| Purpose | [why this interface exists] |
| Contract | [API specification, message schema, or data format] |
| Error Handling | [what happens when this interface fails] |
| Versioning | [how changes to this interface are managed] |
| SLA | [latency, throughput, availability requirements] |
| Security | [authentication, authorization, encryption] |

EXTERNAL INTERFACES:

| # | External System | Direction | Protocol | Data | Contract Owner |
|---|----------------|-----------|----------|------|---------------|
| 1 | [system name] | [inbound/outbound/bidirectional] | [protocol] | [what data] | [who controls the spec] |
...
```

---

## Architectural Views

### Functional View
```
[Describe the functional decomposition — what the system does, organized by capability]

FUNCTIONAL HIERARCHY:
System
├── Function Group 1
│   ├── Function 1.1
│   └── Function 1.2
├── Function Group 2
│   ├── Function 2.1
│   └── Function 2.2
...
```

### Physical View
```
[Describe the physical deployment — where things run]

DEPLOYMENT TOPOLOGY:
| Node | Hardware/Platform | Subsystems Hosted | Location | Redundancy |
|------|------------------|------------------|----------|-----------|
| [node] | [platform] | [what runs here] | [where] | [HA strategy] |
...
```

### Behavioral View
```
[Describe key behavioral sequences — how the system responds to important scenarios]

SEQUENCE: [Scenario Name]
1. [Actor] → [Subsystem A]: [request]
2. [Subsystem A] → [Subsystem B]: [internal call]
3. [Subsystem B] → [Subsystem A]: [response]
4. [Subsystem A] → [Actor]: [result]
```

---

## Output Format

```
## SYSTEM ARCHITECTURE: [System Name]

### 1. Architectural Drivers
[Quality attributes, constraints, key requirements]

### 2. Candidate Architectures
[Each candidate with pattern, decomposition, strengths/weaknesses]

### 3. Architecture Evaluation
[Weighted evaluation matrix, sensitivity analysis]

### 4. Selected Architecture
[Decision rationale, principles, accepted risks]

### 5. Subsystem Decomposition
[Detailed subsystem responsibilities and ownership]

### 6. Interface Catalog
[All interfaces with contracts and SLAs]

### 7. Architectural Views
[Functional, physical, behavioral views]

### 8. Key Decisions Log
[Decisions made, alternatives rejected, rationale]

### 9. Open Questions
[Architectural decisions still pending]
```

---

## Quality Checklist

Before completing:
- [ ] Architectural drivers identified and ranked
- [ ] Multiple candidate architectures considered (not just one)
- [ ] Candidates evaluated against quality attributes with weights
- [ ] Sensitivity analysis performed on evaluation
- [ ] Selected architecture rationale documented
- [ ] All subsystems have clear, non-overlapping responsibilities
- [ ] All interfaces defined with type, protocol, and data
- [ ] Critical interfaces have detailed contracts and SLAs
- [ ] External interfaces and dependencies documented
- [ ] Functional, physical, and behavioral views provided
- [ ] Key architectural decisions logged with rationale

---

## Next Steps

After architecture design:
1. Use `/funcanalysis` to decompose and allocate functions to subsystems
2. Use `/tradestudy` to resolve remaining architectural trade-offs
3. Use `/requirements` to verify all requirements are addressed by the architecture
4. Use `/de` to map dependencies between subsystems
5. Use `/fla` to identify failure modes in the architecture
6. Use `/conops` to validate architecture supports operational scenarios

---
name: "iface - Interface Specification"
description: Define and document all interfaces between system components, subsystems, and external systems. Produces a structured Interface Control Document (ICD) with protocols, data formats, timing, and error handling.
output:
  format: "table"
---

# Interface Specification

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Define interfaces for a new system design**: The user has a system architecture and wants to systematically identify and specify all interfaces between components, subsystems, and external systems before implementation.
**Interpretation 2 — Document interfaces of an existing system**: The user has a running system and wants to create or update interface documentation to capture what currently exists, including undocumented or informal interfaces.
**Interpretation 3 — Resolve interface conflicts or incompatibilities**: The user has identified interface mismatches between components (protocol, format, timing, versioning) and needs to reconcile them.

If ambiguous, ask: "I can help with defining interfaces for a new design, documenting existing interfaces, or resolving interface conflicts — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/iface 4x [input]").

| Depth | Min Interfaces | Min Interface Types | Min Parameters per Interface | Min Error Cases |
|-------|---------------|--------------------|-----------------------------|-----------------|
| 1x    | 5             | 2                  | 3                           | 2               |
| 2x    | 12            | 3                  | 5                           | 4               |
| 4x    | 25            | 4                  | 8                           | 6               |
| 8x    | 40            | 5                  | 12                          | 10              |
| 16x   | 60            | 6                  | 15                          | 15              |

---

## The Process

### Step 1: System Context and Boundary Identification

Before specifying interfaces, map all system boundaries:

```
SYSTEM: [name]
PURPOSE: [one sentence]

INTERNAL COMPONENTS:
| # | Component | Responsibility | Owner |
|---|-----------|---------------|-------|
| 1 | [name]    | [what it does] | [team/person] |
| 2 | [name]    | [what it does] | [team/person] |
...

EXTERNAL SYSTEMS:
| # | System | Relationship | Owner | Stability |
|---|--------|-------------|-------|-----------|
| 1 | [name] | [consumer/provider/peer] | [org/team] | STABLE/EVOLVING/UNSTABLE |
...

USERS/ACTORS:
| # | Actor | Interaction Type | Channel |
|---|-------|-----------------|---------|
| 1 | [who] | [how they interact] | [UI/API/CLI/physical] |
...
```

---

### Step 2: Interface Boundary Discovery

Identify ALL interface boundaries systematically:

```
INTERFACE INVENTORY:

| ID | From | To | Type | Direction | Criticality |
|----|------|----|------|-----------|-------------|
| IF-001 | [component A] | [component B] | DATA/CONTROL/PHYSICAL/ENERGY/HUMAN | UNI/BI | HIGH/MED/LOW |
| IF-002 | [component A] | [external sys] | DATA/CONTROL/PHYSICAL/ENERGY/HUMAN | UNI/BI | HIGH/MED/LOW |
...

INTERFACE TYPES:
- DATA: Information exchange (messages, files, streams, shared memory)
- CONTROL: Command and status signals (start, stop, mode changes)
- PHYSICAL: Mechanical connections (mounting, connectors, cables)
- ENERGY: Power, thermal, hydraulic, pneumatic
- HUMAN: User interactions (displays, controls, alerts)
```

---

### Step 3: Interface Characterization

For each interface, fully characterize:

#### 3A: Data Interfaces

```
INTERFACE: IF-[XXX]
NAME: [descriptive name]
FROM: [source component]
TO: [destination component]
DIRECTION: [unidirectional / bidirectional]

DATA SPECIFICATION:
| Parameter | Value |
|-----------|-------|
| Protocol | [HTTP/gRPC/MQTT/RS-232/CAN/custom/...] |
| Transport | [TCP/UDP/shared memory/file/bus/...] |
| Data Format | [JSON/protobuf/XML/binary/CSV/...] |
| Encoding | [UTF-8/ASCII/binary/...] |
| Schema Version | [version identifier] |
| Max Message Size | [bytes/KB/MB] |
| Byte Order | [big-endian/little-endian/N/A] |

TIMING:
| Parameter | Value |
|-----------|-------|
| Frequency | [continuous/periodic/on-demand/event-driven] |
| Rate | [messages per second / polling interval] |
| Max Latency | [ms/s] |
| Timeout | [ms/s] |
| Ordering Guarantee | [FIFO/unordered/sequenced] |

MESSAGE CATALOG:
| Msg ID | Name | Direction | Payload | Frequency | Required |
|--------|------|-----------|---------|-----------|----------|
| M-001 | [name] | [A→B / B→A] | [description] | [rate] | YES/NO |
...
```

#### 3B: Control Interfaces

```
INTERFACE: IF-[XXX]
NAME: [descriptive name]

COMMANDS:
| Cmd ID | Command | Parameters | Expected Response | Timeout |
|--------|---------|-----------|-------------------|---------|
| C-001 | [command name] | [params] | [response] | [ms/s] |
...

STATE MACHINE:
| Current State | Command | Next State | Conditions |
|--------------|---------|------------|------------|
| [state] | [cmd] | [state] | [guards/preconditions] |
...
```

#### 3C: Physical Interfaces

```
INTERFACE: IF-[XXX]
NAME: [descriptive name]

PHYSICAL SPECIFICATION:
| Parameter | Value |
|-----------|-------|
| Connector Type | [type/model] |
| Pin Count | [number] |
| Mating Cycles | [rated cycles] |
| Dimensions | [L x W x H] |
| Weight | [mass] |
| Environmental | [temp range, IP rating, vibration] |

PIN ASSIGNMENTS:
| Pin | Signal | Direction | Type | Voltage/Level |
|-----|--------|-----------|------|---------------|
| 1   | [signal] | IN/OUT | [power/data/ground] | [V/level] |
...
```

---

### Step 4: Error Handling and Fault Behavior

For each interface, define failure modes:

```
ERROR HANDLING FOR IF-[XXX]:

| Error Condition | Detection Method | Response | Recovery | Severity |
|----------------|-----------------|----------|----------|----------|
| Connection lost | Heartbeat timeout | Buffer and retry | Auto-reconnect with backoff | HIGH |
| Malformed message | Schema validation | Reject and log | Request retransmit | MED |
| Timeout | Timer expiry | Alert and fallback | Reset and retry | HIGH |
| Version mismatch | Handshake check | Reject connection | Negotiate version | MED |
| Buffer overflow | Queue depth monitor | Drop oldest/newest | Back-pressure signal | HIGH |
| Authentication failure | Auth check | Reject and alert | Re-authenticate | HIGH |

DEGRADED MODES:
| Mode | Trigger | Behavior | Restrictions |
|------|---------|----------|-------------|
| [mode name] | [what triggers it] | [how system behaves] | [what's limited] |
...
```

---

### Step 5: Interface Compatibility Verification

Cross-check all interface pairs for compatibility:

```
COMPATIBILITY MATRIX:

| Check | IF-001 | IF-002 | IF-003 | ... |
|-------|--------|--------|--------|-----|
| Protocol match | PASS/FAIL | PASS/FAIL | PASS/FAIL | |
| Data format match | PASS/FAIL | PASS/FAIL | PASS/FAIL | |
| Timing compatible | PASS/FAIL | PASS/FAIL | PASS/FAIL | |
| Error handling aligned | PASS/FAIL | PASS/FAIL | PASS/FAIL | |
| Version strategy compatible | PASS/FAIL | PASS/FAIL | PASS/FAIL | |
| Security level compatible | PASS/FAIL | PASS/FAIL | PASS/FAIL | |

INCOMPATIBILITIES FOUND:
| IF Pair | Issue | Impact | Resolution |
|---------|-------|--------|------------|
| IF-001 ↔ IF-003 | [mismatch description] | [impact] | [how to fix] |
...
```

---

### Step 6: Versioning and Evolution Strategy

```
INTERFACE VERSIONING:

| Interface | Current Version | Versioning Scheme | Backward Compatible? |
|-----------|----------------|-------------------|---------------------|
| IF-001 | [v1.0] | [semver/date/sequential] | YES/NO |
...

CHANGE MANAGEMENT:
| Change Type | Process | Lead Time | Notification |
|-------------|---------|-----------|-------------|
| Additive (new optional field) | [process] | [time] | [who to notify] |
| Non-breaking modification | [process] | [time] | [who to notify] |
| Breaking change | [process] | [time] | [who to notify] |
| Deprecation | [process] | [time] | [who to notify] |
```

---

## Output Format

```
## INTERFACE CONTROL DOCUMENT: [System Name]

### Document Control
Version: [X.Y]
Date: [date]
Status: [DRAFT/REVIEW/APPROVED/RELEASED]
Approvers: [list]

### System Context
[System boundary, components, external systems]

### Interface Inventory
[Table of all interfaces with IDs, types, directions, criticality]

### Interface Specifications
[Detailed specification for each interface — data, control, physical as applicable]

### Error Handling
[Per-interface error conditions, responses, recovery]

### Compatibility Matrix
[Cross-check results for all interface pairs]

### Versioning Strategy
[How interfaces evolve, change management process]

### Interface Diagrams
[Descriptions of context diagrams, sequence diagrams, data flow diagrams]

### Open Items
[Unresolved interface questions, pending decisions, TBDs]
```

---

## Quality Checklist

Before completing:
- [ ] All system boundaries identified (internal, external, user)
- [ ] Every component-to-component connection has an interface specification
- [ ] Each interface has protocol, format, timing, and error handling defined
- [ ] Physical interfaces have connector and pin-level detail
- [ ] Error handling covers connection loss, malformed data, timeout, and version mismatch
- [ ] Compatibility matrix completed with all pairs checked
- [ ] Versioning and change management strategy defined
- [ ] No TBDs remain in critical interfaces
- [ ] Interface IDs are unique and consistently referenced

---

## Next Steps

After interface specification:
1. Use `/vv` to create verification plans for each interface
2. Use `/sysintegration` to plan integration sequence based on interface dependencies
3. Use `/riskmgmt` to assess risks around critical interfaces
4. Use `/requirements` to trace interfaces back to requirements
5. Use `/de` to map interface dependencies

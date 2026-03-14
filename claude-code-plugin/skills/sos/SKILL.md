---
name: "sos - System of Systems Analysis"
description: Analyze and design systems composed of independently operated constituent systems. Identifies emergent behaviors, interdependencies, governance models, and integration strategies.
output:
  format: "table"
---

# System of Systems (SoS) Analysis

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Architect a new System of Systems**: The user needs to compose multiple independent systems into a coordinated SoS to achieve a capability that no single system can provide alone.
**Interpretation 2 — Analyze an existing System of Systems**: The user has a functioning SoS and wants to understand its emergent behaviors, vulnerabilities, interdependencies, or governance gaps.
**Interpretation 3 — Integrate a new system into an existing SoS**: The user needs to add a new constituent system to an existing SoS while maintaining overall capability and managing disruption.

If ambiguous, ask: "I can help with architecting a new SoS, analyzing an existing SoS, or integrating a new system into an existing SoS — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/sos 4x [input]").

| Depth | Min Constituent Systems | Min Emergent Behaviors | Min Interdependencies | Min SoS Risks | Min Governance Elements |
|-------|------------------------|----------------------|----------------------|---------------|------------------------|
| 1x    | 3                      | 3                    | 5                    | 4             | 3                      |
| 2x    | 5                      | 6                    | 12                   | 8             | 6                      |
| 4x    | 8                      | 10                   | 25                   | 15            | 10                     |
| 8x    | 12                     | 15                   | 40                   | 25            | 15                     |
| 16x   | 20                     | 25                   | 60                   | 40            | 20                     |

---

## The Process

### Step 1: Identify Constituent Systems and Their Missions

```
SYSTEM OF SYSTEMS: [SoS name]
SoS MISSION: [the capability that emerges from the combination]

CONSTITUENT SYSTEMS:

| ID | System | Owner/Operator | Independent Mission | Operational Status | Managerial Independence | Evolutionary Freedom |
|----|--------|---------------|--------------------|--------------------|------------------------|---------------------|
| CS-1 | [name] | [organization] | [what it does on its own] | [operational/development/planned] | [HIGH/MED/LOW] | [HIGH/MED/LOW] |
| CS-2 | [name] | [organization] | [independent mission] | [status] | [independence] | [freedom] |
| CS-3 | [name] | [organization] | [independent mission] | [status] | [independence] | [freedom] |

For each constituent system:
- Can it operate without the SoS? [Yes/No]
- Was it originally designed for this SoS? [Yes/No]
- Who controls its evolution? [owner, not SoS authority]
- What is its lifecycle stage? [concept/development/production/sustainment/disposal]
- What are its constraints on SoS participation? [availability, bandwidth, data sharing, etc.]
```

---

### Step 2: Characterize SoS Type

Determine the SoS category — this drives governance and integration strategy:

```
SoS TYPE ASSESSMENT:

| Characteristic | Assessment | Evidence |
|---------------|-----------|----------|
| Central management authority? | [Yes/Partial/No] | [who, what authority] |
| Constituent systems have agreed purpose? | [Yes/Partial/No] | [formal agreement, MOA, contract] |
| Constituents can opt out? | [Yes/No] | [voluntarily participate?] |
| Central funding? | [Yes/Partial/No] | [who pays for integration] |
| Coordinated evolution? | [Yes/Partial/No] | [who decides upgrades] |

SoS TYPE: [Select one]

| Type | Description | Fits? |
|------|-------------|-------|
| DIRECTED | Central authority owns and manages constituent systems. Top-down control. | [Yes/No] |
| ACKNOWLEDGED | Central authority recognized but constituent systems retain independence. Central management body coordinates. | [Yes/No] |
| COLLABORATIVE | Constituent systems voluntarily agree to cooperate. No central authority. Coordination by consensus. | [Yes/No] |
| VIRTUAL | No central authority, no agreed purpose. Emergent behavior from independent actions. | [Yes/No] |

IMPLICATIONS OF TYPE:
- Governance approach: [what's possible given the type]
- Integration leverage: [what can be mandated vs. negotiated]
- Evolution control: [how changes propagate]
- Risk posture: [what can go wrong with this type]
```

---

### Step 3: Identify Emergent Behaviors and Capabilities

Map the capabilities that emerge ONLY from the combination:

```
EMERGENT CAPABILITIES (things the SoS can do that no constituent can do alone):

| ID | Emergent Capability | Contributing Systems | How It Emerges | Value |
|----|--------------------|--------------------|---------------|-------|
| EC-1 | [capability] | [CS-1, CS-3, CS-5] | [how their combination creates this] | [mission value] |
| EC-2 | [capability] | [CS-2, CS-4] | [mechanism] | [value] |

EMERGENT BEHAVIORS (unplanned, possibly undesirable):

| ID | Emergent Behavior | Contributing Systems | Trigger Condition | Consequence | Desirable? |
|----|-------------------|--------------------|--------------------|-------------|-----------|
| EB-1 | [behavior] | [which systems interact] | [what triggers it] | [what happens] | [Yes/No/Uncertain] |
| EB-2 | [behavior] | [systems] | [trigger] | [consequence] | [assessment] |

CAPABILITY GAPS:
| Desired SoS Capability | Current Status | Gap | Resolution Options |
|------------------------|---------------|-----|-------------------|
| [capability] | [partial/missing] | [what's missing] | [new system / upgrade / workaround] |
```

---

### Step 4: Analyze Interdependencies and Coupling

```
INTERDEPENDENCY MATRIX:

        | CS-1 | CS-2 | CS-3 | CS-4 | CS-5 |
--------|------|------|------|------|------|
CS-1    |  -   | [type] | [type] | [type] | [type] |
CS-2    | [type] |  -   | [type] | [type] | [type] |
CS-3    | [type] | [type] |  -   | [type] | [type] |
CS-4    | [type] | [type] | [type] |  -   | [type] |
CS-5    | [type] | [type] | [type] | [type] |  -   |

Types: D=Data, C=Control, R=Resource, T=Temporal, P=Physical, N=None

DETAILED INTERDEPENDENCIES:

| ID | From | To | Type | Description | Coupling Strength | Criticality |
|----|------|----|------|-------------|-------------------|-------------|
| ID-1 | CS-1 | CS-2 | Data | [what data flows] | [TIGHT/LOOSE] | [what breaks if severed] |
| ID-2 | CS-2 | CS-3 | Control | [what control signals] | [strength] | [impact] |
| ID-3 | CS-1 | CS-4 | Temporal | [timing dependency] | [strength] | [impact] |

COUPLING ANALYSIS:
| Coupling Concern | Affected Systems | Current State | Risk if Broken | Decoupling Strategy |
|-----------------|-----------------|---------------|---------------|---------------------|
| Tight data coupling | [CS-1, CS-2] | [real-time feed required] | [SoS capability lost] | [buffering, caching, graceful degradation] |
| Single point of failure | [CS-3] | [only system providing X] | [mission failure] | [redundancy, alternative source] |
| Temporal coupling | [CS-1, CS-4] | [must synchronize within Xms] | [incorrect behavior] | [loose synchronization, timestamps] |
```

---

### Step 5: Assess SoS Governance Model

```
SoS GOVERNANCE:

AUTHORITY STRUCTURE:
| Function | Authority | Mechanism | Enforcement |
|----------|-----------|-----------|-------------|
| SoS architecture decisions | [who decides] | [board/MOA/contract] | [how enforced] |
| Interface standards | [who sets] | [ICD/standard] | [compliance verification] |
| Resource allocation | [who allocates] | [budget process] | [incentives/penalties] |
| Conflict resolution | [who arbitrates] | [escalation path] | [binding/advisory] |
| Evolution coordination | [who plans] | [roadmap process] | [synchronization mechanism] |
| Performance monitoring | [who measures] | [SoS-level metrics] | [reporting/dashboards] |

GOVERNANCE GAPS:
| Gap | Consequence | Recommendation |
|-----|-------------|---------------|
| [no authority over CS-3 evolution] | [they may change APIs breaking SoS] | [establish MOA with change notification] |
| [no SoS-level testing] | [emergent failures not detected] | [create SoS test events] |

AGREEMENTS AND CONTRACTS:
| Agreement | Parties | Scope | Status | Expiration |
|-----------|---------|-------|--------|------------|
| [MOA/MOU/SLA/Contract] | [organizations] | [what it covers] | [active/draft/expired] | [date] |
```

---

### Step 6: Define Integration Strategy

```
INTEGRATION STRATEGY:

INTEGRATION APPROACH:
| Aspect | Strategy | Rationale |
|--------|----------|-----------|
| Data exchange | [standards-based / adapters / middleware / direct] | [why this approach] |
| Communication | [protocol / network / bandwidth] | [why] |
| Security | [cross-domain / enclaves / federated identity] | [why] |
| Time synchronization | [NTP / GPS / IEEE 1588 / none] | [why] |
| Testing | [live / simulation / hybrid / federated] | [why] |

INTERFACE SPECIFICATIONS:
| Interface | Systems | Standard/Protocol | Data Format | Frequency | Security | Status |
|-----------|---------|-------------------|-------------|-----------|----------|--------|
| [IF-1] | CS-1 <-> CS-2 | [REST/MQTT/DDS/MIL-STD-6016] | [JSON/XML/binary] | [real-time/batch] | [classification] | [defined/TBD] |
| [IF-2] | CS-2 <-> CS-3 | [protocol] | [format] | [frequency] | [security] | [status] |

INTEGRATION CONSTRAINTS FROM CONSTITUENT AUTONOMY:
| Constituent | Constraint | Impact on Integration | Accommodation |
|-------------|-----------|----------------------|---------------|
| [CS-1] | [cannot modify internal interfaces] | [must use existing API] | [build adapter] |
| [CS-3] | [operates on classified network] | [data must cross domain] | [cross-domain solution] |
| [CS-4] | [vendor controls updates] | [interface may change without notice] | [abstraction layer] |

GRACEFUL DEGRADATION:
| Constituent Lost | SoS Capability Impact | Degraded Mode | Recovery Strategy |
|-----------------|----------------------|---------------|-------------------|
| CS-1 unavailable | [which capabilities lost] | [what SoS can still do] | [how to restore] |
| CS-2 unavailable | [impact] | [degraded mode] | [recovery] |
```

---

### Step 7: Identify SoS-Level Risks

```
SoS RISK REGISTER:

| ID | Risk | Category | Likelihood | Consequence | Risk Level | Mitigation | Owner |
|----|------|----------|-----------|-------------|------------|------------|-------|
| SR-1 | Constituent system evolves incompatibly | Evolution | [H/M/L] | [impact] | [H/M/L] | [change notification MOA, abstraction layer] | [who] |
| SR-2 | Emergent failure mode not tested | Testing | [H/M/L] | [impact] | [H/M/L] | [SoS test events, simulation] | [who] |
| SR-3 | Constituent system withdrawn from SoS | Availability | [H/M/L] | [impact] | [H/M/L] | [alternative sources, graceful degradation] | [who] |
| SR-4 | Security boundary compromise | Security | [H/M/L] | [impact] | [H/M/L] | [cross-domain solutions, monitoring] | [who] |
| SR-5 | No authority to mandate changes | Governance | [H/M/L] | [impact] | [H/M/L] | [incentive structures, agreements] | [who] |
| SR-6 | Performance degrades as SoS scales | Performance | [H/M/L] | [impact] | [H/M/L] | [capacity planning, load testing] | [who] |
| SR-7 | Data quality varies across constituents | Data | [H/M/L] | [impact] | [H/M/L] | [validation, data quality standards] | [who] |

SoS-SPECIFIC RISK CATEGORIES:
- Evolution risk: Constituent systems change independently
- Emergence risk: Unpredicted behaviors from system interactions
- Governance risk: Insufficient authority to manage the SoS
- Integration risk: Technical barriers to interoperability
- Sustainability risk: Funding, organizational, or political changes
- Trust risk: Constituent systems may not share data or cooperate
```

---

## Output Format

```
## SoS ARCHITECTURE DESCRIPTION: [SoS Name]

### SoS Mission and Context
[What the SoS achieves that no single system can]

### Constituent Systems
[Inventory with independent missions, owners, autonomy levels]

### SoS Type and Governance
[Type characterization, authority structure, agreements]

### Emergent Capabilities and Behaviors
[Desired emergent capabilities, unintended emergent behaviors]

### Interdependency Analysis
[Matrix, critical dependencies, coupling concerns]

### Integration Strategy
[Data exchange, interfaces, constraints from autonomy, degraded modes]

### SoS Risk Register
[Risks specific to SoS nature — evolution, emergence, governance]

### Governance Recommendations
[Improvements to authority, agreements, coordination]

### Open Items
[Unresolved governance questions, undefined interfaces, untested emergent behaviors]
```

---

## Quality Checklist

Before completing:
- [ ] All constituent systems identified with independent missions
- [ ] SoS type characterized with evidence
- [ ] Emergent capabilities mapped to contributing systems
- [ ] Undesirable emergent behaviors identified
- [ ] Interdependency matrix completed
- [ ] Single points of failure identified
- [ ] Governance model assessed with gaps identified
- [ ] Integration strategy respects constituent autonomy
- [ ] Graceful degradation defined for each constituent loss
- [ ] SoS-specific risks identified (not just system-level risks)
- [ ] Agreements and contracts documented or recommended

---

## Next Steps

After SoS analysis:
1. Use `/sysarch` to detail the SoS architecture framework
2. Use `/iface` to define inter-system interfaces
3. Use `/riskmgmt` to manage SoS-level risks
4. Use `/stakeholder` to map SoS stakeholders across constituent organizations
5. Use `/conops` to define SoS operational scenarios
6. Use `/sysintegration` to plan SoS integration and test events
7. Use `/selifecycle` to coordinate SE activities across constituents

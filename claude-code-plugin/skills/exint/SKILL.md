---
name: "exint - External Integration"
description: Design how something connects to external systems, tools, or services. Identifies touchpoints, maps data flows, defines interfaces, assesses dependencies, plans for failures, and produces an integration checklist.
---

# External Integration

**Input**: $ARGUMENTS

---

## Step 1: Identify External Touchpoints

List every point where the system touches something external.

```
SYSTEM: [what is being integrated]
INTEGRATION GOAL: [why external connections are needed]

EXTERNAL TOUCHPOINTS:
1. [system/service] — Direction: [IN / OUT / BOTH] — Purpose: [why]
2. [system/service] — Direction: [IN / OUT / BOTH] — Purpose: [why]
...

TOUCHPOINT CATEGORIES:
- Data sources: [list]
- Data sinks: [list]
- Services consumed: [list]
- Services provided: [list]
- User-facing integrations: [list]
```

---

## Step 2: Map Data Flows

Trace what data moves where, in what format, and how often.

```
DATA FLOWS:
[Source] →(format, frequency)→ [Destination]

1. [external] →([format], [frequency])→ [internal]
   Data: [what's transferred]
   Volume: [expected size/rate]

2. [internal] →([format], [frequency])→ [external]
   Data: [what's transferred]
   Volume: [expected size/rate]

TRANSFORMATIONS NEEDED:
- [flow]: [input format] must become [output format] via [method]

DATA OWNERSHIP: [who owns each data flow?]
```

---

## Step 3: Define Interfaces

Specify the contracts between systems.

```
INTERFACES:
1. [interface name]
   - Protocol: [REST / GraphQL / webhook / file / etc.]
   - Authentication: [method]
   - Contract: [what's guaranteed]
   - Versioning: [how changes are handled]

2. [interface name]
   - Protocol: [type]
   - Authentication: [method]
   - Contract: [what's guaranteed]
   - Versioning: [how changes are handled]

STANDARDS TO FOLLOW: [relevant standards or conventions]
DOCUMENTATION REQUIRED: [what needs to be documented for each interface]
```

---

## Step 4: Assess Dependencies

Evaluate the risk profile of each external dependency.

```
DEPENDENCY ASSESSMENT:
| External System | Criticality | Reliability | Control | Risk |
|----------------|-------------|-------------|---------|------|
| [system 1] | [HIGH/MED/LOW] | [HIGH/MED/LOW] | [OWN/SHARED/NONE] | [score] |
| [system 2] | [HIGH/MED/LOW] | [HIGH/MED/LOW] | [OWN/SHARED/NONE] | [score] |

SINGLE POINTS OF FAILURE:
- [dependency]: if this fails, [consequence]

VENDOR LOCK-IN RISKS:
- [dependency]: switching cost is [HIGH/MED/LOW] because [reason]
```

---

## Step 5: Plan for External Failures

Design resilience for when external systems fail.

```
FAILURE SCENARIOS:
1. [external system] goes down
   - Detection: [how we know]
   - Impact: [what breaks]
   - Mitigation: [fallback / cache / queue / degrade gracefully]
   - Recovery: [how to resume when it's back]

2. [external system] returns bad data
   - Detection: [validation approach]
   - Impact: [what breaks]
   - Mitigation: [reject / sanitize / alert]

CIRCUIT BREAKERS: [where to stop calling failing externals]
RETRY STRATEGY: [when and how to retry]
TIMEOUT POLICY: [how long to wait before giving up]
```

---

## Step 6: Integration Checklist

```
INTEGRATION CHECKLIST:

PRE-INTEGRATION:
☐ All interfaces documented
☐ Authentication credentials secured
☐ Data formats validated
☐ Error handling defined
☐ Rate limits understood

IMPLEMENTATION:
☐ Each touchpoint implemented and tested
☐ Data transformations verified
☐ Failure modes handled
☐ Logging and monitoring in place
☐ Circuit breakers configured

POST-INTEGRATION:
☐ End-to-end flow tested
☐ Performance validated under load
☐ Failover tested
☐ Documentation updated
☐ Runbook created for operations

PRIORITY ORDER:
1. [first integration to build] — Reason: [why first]
2. [second integration] — Reason: [why second]
```

---

## Integration

Use with:
- `/ecomp` -> Assess the full ecosystem including external connections
- `/gapf` -> Find missing integrations
- `/de` -> Plan the integration project execution

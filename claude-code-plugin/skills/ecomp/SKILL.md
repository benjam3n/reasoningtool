---
name: "ecomp - Ecosystem Completion"
description: Analyze whether a system or collection is complete and coherent. Maps components, identifies connections, finds orphans and missing links, and assesses domain coverage.
---

# Ecosystem Completion

**Input**: $ARGUMENTS

---

## Step 1: Map All Components

Inventory every component in the system.

```
ECOSYSTEM: [what system/collection is being analyzed]
PURPOSE: [what this ecosystem is supposed to accomplish]

COMPONENTS:
1. [component] — Role: [what it does] — Type: [category]
2. [component] — Role: [what it does] — Type: [category]
...

COMPONENT COUNT: [N]
COMPONENT TYPES: [list of distinct types/categories]
```

---

## Step 2: Identify Connections

Map how components relate to and depend on each other.

```
CONNECTIONS:
[component A] → [component B]: [nature of connection]
[component B] → [component C]: [nature of connection]
...

CONNECTION TYPES:
- Depends on: [list]
- Feeds into: [list]
- Competes with: [list]
- Complements: [list]

DENSITY: [how interconnected is this ecosystem? SPARSE / MODERATE / DENSE]
```

---

## Step 3: Find Orphaned Components

Identify components that are isolated or poorly integrated.

```
ORPHANED COMPONENTS (no meaningful connections):
1. [component] — Why orphaned: [explanation]
   Potential connections: [where it could connect]

WEAKLY CONNECTED (only one connection):
1. [component] — Connected to: [what] — Missing connections: [what's expected]

OVER-CONNECTED (potential bottleneck):
1. [component] — Connection count: [N] — Risk: [what happens if it fails]
```

---

## Step 4: Find Missing Connections

Identify connections that should exist but don't.

```
MISSING CONNECTIONS:
1. [component A] ↔ [component B]
   Why expected: [rationale]
   Impact of absence: [what's lost]

2. [component A] ↔ [component B]
   Why expected: [rationale]
   Impact of absence: [what's lost]

MISSING FEEDBACK LOOPS:
- [where output should feed back as input but doesn't]

MISSING BRIDGES:
- [clusters that should connect but don't]
```

---

## Step 5: Assess Domain Coverage

Determine whether the ecosystem covers its intended domain.

```
DOMAIN MAP:
| Domain Area | Covered By | Coverage | Notes |
|-------------|-----------|----------|-------|
| [area 1] | [components] | FULL / PARTIAL / NONE | [detail] |
| [area 2] | [components] | FULL / PARTIAL / NONE | [detail] |
...

REDUNDANCIES (multiple components covering same area):
- [area]: covered by [comp A] and [comp B] — Intentional? [Y/N]

BLIND SPOTS (areas with no coverage):
- [area]: [why it matters]
```

---

## Step 6: Completeness Assessment

```
ECOSYSTEM HEALTH SCORE:

Component completeness: [0-100%] — [N] of [expected] components present
Connection completeness: [0-100%] — [N] of [expected] connections present
Domain coverage: [0-100%] — [N] of [expected] areas covered
Coherence: [HIGH/MED/LOW] — do components work as a unified system?

TOP GAPS:
1. [most critical missing piece] — Impact: [what it would enable]
2. [second gap] — Impact: [what it would enable]
3. [third gap] — Impact: [what it would enable]

RECOMMENDED ADDITIONS (in priority order):
1. [what to add] — Connects to: [existing components] — Covers: [domain area]
2. [what to add] — Connects to: [existing components] — Covers: [domain area]

RECOMMENDED REMOVALS:
- [component] — Reason: [redundant/orphaned/counterproductive]
```

---

## Integration

Use with:
- `/gapf` -> Detailed gap analysis for specific coverage areas
- `/exint` -> Design integrations for missing connections
- `/cvis` -> Check if ecosystem aligns with creator's vision

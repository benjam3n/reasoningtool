---
name: "skcl - Skill Cluster Design"
description: "Design groups of related skills that work together by identifying domain capabilities, grouping by affinity, designing interfaces, and mapping common paths."
output:
  format: "prose"
---

# SKCL - Skill Cluster Design

**Input**: $ARGUMENTS

---

## Step 1: Identify the Domain

```
DOMAIN: [the area this skill cluster serves]
DOMAIN SCOPE: [what's in and out of scope]
USER NEED: [what someone working in this domain needs to accomplish]
EXISTING SKILLS: [any current skills that touch this domain]
```

A cluster serves a coherent domain. If you can't state the domain in one phrase, you're probably designing multiple clusters.

---

## Step 2: Enumerate Needed Capabilities

```
CAPABILITIES NEEDED:
  1. [capability] — DESCRIPTION: [what it does]
     EXISTING SKILL: [if one already handles this, name it]
     GAP: [if no skill exists, mark as NEW]
  2. [capability] — DESCRIPTION: [what it does]
     EXISTING SKILL: [or GAP: NEW]
  3. [capability]
  ...
```

Think from the user's perspective. What does someone working in this domain need to DO? Each capability is a potential skill.

---

## Step 3: Group by Natural Affinity

```
GROUP 1: [group name]
  SHARED CONCERN: [what these capabilities have in common]
  CAPABILITIES: [list from Step 2]

GROUP 2: [group name]
  SHARED CONCERN: [commonality]
  CAPABILITIES: [list]

GROUP 3: [group name]
  SHARED CONCERN: [commonality]
  CAPABILITIES: [list]
```

Natural affinity means: these capabilities share inputs, outputs, mental models, or sequential dependencies. If two capabilities always need to know each other's results, they have affinity.

---

## Step 4: Design Skill Interfaces

For each skill in the cluster, define how it connects to others:

```
SKILL: [name]
  INPUT: [what it takes in]
  OUTPUT: [what it produces]
  CHAINS TO: [which skills can consume its output]
  CHAINS FROM: [which skills can feed into it]
  INTERFACE FORMAT: [how output is structured so the next skill can use it]
```

Good interfaces mean skills can chain without the user doing translation work. The output of skill A should be directly usable as input to skill B.

---

## Step 5: Identify the Entry-Point Skill

```
ENTRY POINT: [the skill users invoke first]
  WHY THIS ONE: [why it's the natural starting point]
  ROUTES TO: [which skills it can dispatch to]
  ROUTING LOGIC: [how it decides which skill to invoke next]
```

Every cluster needs one clear entry point. If users don't know which skill to start with, the cluster is poorly designed. The entry point should either do the first step of work or route to the right specialist skill.

---

## Step 6: Map Common Paths

```
PATH 1: [name — e.g., "Quick Assessment"]
  ROUTE: /[entry] → /[skill-a] → /[skill-b]
  USE WHEN: [situation that calls for this path]
  PRODUCES: [what the user gets at the end]

PATH 2: [name — e.g., "Deep Analysis"]
  ROUTE: /[entry] → /[skill-a] → /[skill-c] → /[skill-d]
  USE WHEN: [situation]
  PRODUCES: [output]

PATH 3: [name — e.g., "Validation"]
  ROUTE: /[entry] → /[skill-b] → /[skill-e]
  USE WHEN: [situation]
  PRODUCES: [output]
```

---

## Output Summary

```
SKILL CLUSTER: [name]
==================
DOMAIN: [what it serves]
SKILLS: [count]
ENTRY POINT: /[skill-id]

CLUSTER MAP:
  /[entry] → /[a], /[b], /[c]
  /[a] → /[d]
  /[b] → /[d], /[e]
  /[c] → /[e]

COMMON PATHS:
  1. [path name]: /[route]
  2. [path name]: /[route]

NEW SKILLS NEEDED: [list of capabilities not covered by existing skills]
EXISTING SKILLS INCORPORATED: [list of existing skills that join this cluster]
```

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Too broad** | Cluster covers unrelated capabilities | Split into multiple clusters with clear boundaries |
| **No entry point** | Users must choose among 5+ skills to start | Design a router or classifier as the entry skill |
| **Poor interfaces** | Skill outputs don't feed into other skills | Redesign output formats to match downstream inputs |
| **Missing paths** | Common user needs require jumping outside the cluster | Add the missing capability or bridge skill |
| **Circular dependencies** | Skills require each other's output to start | Break the cycle with a skill that provides initial input |

---

## Integration

- Use with: `/mtskd` to design meta-skills that operate on the cluster
- Use with: `/gflr` to find gaps in the cluster's coverage
- Use with: `/sysk` to analyze the cluster as a system
- Use from: `/create` when building new skill sets
- Differs from `/mtskd`: skcl designs skill groups; mtskd designs skills that operate on other skills

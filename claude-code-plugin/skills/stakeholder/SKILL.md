---
name: "stakeholder - Stakeholder Analysis"
description: Systematically identify all stakeholders, map their interests, influence, and requirements, detect conflicts between stakeholder needs, and define engagement strategies. Produces a stakeholder registry and influence map.
output:
  format: "table"
---

# Stakeholder Analysis

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Identify stakeholders for a new system or project**: The user has a system, project, or initiative and wants to systematically discover ALL stakeholders — direct, indirect, and hidden — and understand their needs and influence.
**Interpretation 2 — Resolve stakeholder conflicts**: The user has identified competing stakeholder interests and needs a structured approach to prioritize needs, negotiate trade-offs, and define resolution strategies.
**Interpretation 3 — Define stakeholder engagement strategy**: The user knows their stakeholders but needs a plan for how to communicate, involve, and manage each stakeholder throughout the project lifecycle.

If ambiguous, ask: "I can help with identifying stakeholders for a new project, resolving conflicts between known stakeholders, or defining an engagement strategy — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/stakeholder 4x [input]").

| Depth | Min Stakeholders | Min Categories | Min Conflict Checks | Min Engagement Actions | Min Hidden Stakeholders |
|-------|-----------------|----------------|---------------------|----------------------|------------------------|
| 1x    | 8               | 4              | 3                   | 4                    | 2                      |
| 2x    | 15              | 6              | 6                   | 8                    | 4                      |
| 4x    | 25              | 8              | 10                  | 15                   | 8                      |
| 8x    | 40              | 10             | 16                  | 25                   | 12                     |
| 16x   | 60              | 12             | 25                  | 40                   | 20                     |

---

## The Process

### Step 1: Identify Stakeholders

Systematically identify stakeholders across all categories:

```
SYSTEM/PROJECT: [name]
PURPOSE: [one sentence]

DIRECT STAKEHOLDERS (interact with the system):

| # | Stakeholder | Category | Relationship | Primary Interest | Contact/Rep |
|---|------------|----------|-------------|-----------------|-------------|
| 1 | [who] | [user/operator/maintainer/owner] | [how they interact] | [what they care about] | [who represents them] |
...

INDIRECT STAKEHOLDERS (affected by the system):

| # | Stakeholder | Category | How Affected | Primary Interest | Contact/Rep |
|---|------------|----------|-------------|-----------------|-------------|
| 1 | [who] | [beneficiary/regulator/competitor/public] | [how impacted] | [what they care about] | [who represents them] |
...

HIDDEN STAKEHOLDERS (often missed — actively hunt for these):

| # | Stakeholder | Why Hidden | Discovery Method | Primary Interest |
|---|------------|-----------|-----------------|-----------------|
| 1 | [who] | [why they're easy to miss] | [how you found them] | [what they care about] |
...
```

Hidden stakeholder discovery prompts:
| Prompt | Stakeholder Found? |
|--------|-------------------|
| "Who maintains this system after the builders leave?" | |
| "Who pays when this system fails?" | |
| "Who is displaced or made obsolete by this system?" | |
| "Who regulates the domain this system operates in?" | |
| "Who supplies data/resources this system consumes?" | |
| "Who uses the OUTPUT of this system as their INPUT?" | |
| "Who inherits this system in 5 years?" | |
| "Who is harmed if this system is misused?" | |
| "Who are the adversaries who want this system to fail?" | |
| "Whose workflow changes because of this system?" | |
| "Who trains new users on this system?" | |
| "Who must approve changes to this system?" | |

---

### Step 2: Map Influence vs Interest

Plot each stakeholder on the influence-interest grid:

```
INFLUENCE-INTEREST MATRIX:

                    LOW INTEREST              HIGH INTEREST
                ┌─────────────────────┬─────────────────────┐
HIGH            │                     │                     │
INFLUENCE       │   KEEP SATISFIED    │   MANAGE CLOSELY    │
                │   [stakeholder ids] │   [stakeholder ids] │
                │                     │                     │
                ├─────────────────────┼─────────────────────┤
LOW             │                     │                     │
INFLUENCE       │   MONITOR           │   KEEP INFORMED     │
                │   [stakeholder ids] │   [stakeholder ids] │
                │                     │                     │
                └─────────────────────┴─────────────────────┘

DETAILED SCORING:

| # | Stakeholder | Interest (1-5) | Influence (1-5) | Quadrant | Rationale |
|---|------------|---------------|----------------|----------|-----------|
| 1 | [who] | [score] | [score] | [quadrant] | [why these scores] |
...

INTEREST FACTORS:
- 5: System directly determines their success/failure
- 4: System significantly affects their daily work
- 3: System has moderate impact on their goals
- 2: System has minor or occasional impact
- 1: System has minimal relevance to them

INFLUENCE FACTORS:
- 5: Can approve/cancel the project, control budget
- 4: Can significantly shape requirements or design
- 3: Can influence decisions through expertise or authority
- 2: Can provide input but limited decision power
- 1: Has no formal power over the project
```

---

### Step 3: Identify Stakeholder Conflicts

```
STAKEHOLDER NEEDS REGISTRY:

| # | Stakeholder | Need | Priority | Rationale | Linked Requirements |
|---|------------|------|----------|-----------|-------------------|
| 1 | [who] | [what they need from the system] | CRITICAL/HIGH/MEDIUM/LOW | [why it matters to them] | [req IDs if known] |
...

CONFLICT ANALYSIS:

| # | Stakeholder A | Need A | Stakeholder B | Need B | Conflict Type | Severity |
|---|--------------|--------|--------------|--------|---------------|----------|
| 1 | [who] | [their need] | [who] | [their need] | [type] | HIGH/MED/LOW |
...

CONFLICT TYPES:
- Resource Competition: Both need the same limited resource (budget, time, personnel)
- Priority Contradiction: One needs X prioritized, other needs Y prioritized
- Design Tension: One needs simplicity, other needs flexibility
- Timeline Conflict: One needs it now, other needs it thoroughly tested
- Access Conflict: One needs openness, other needs security
- Scope Conflict: One wants more features, other wants less complexity

CONFLICT RESOLUTION OPTIONS:

| Conflict # | Option A | Option B | Option C (Compromise) | Recommended | Rationale |
|-----------|----------|----------|----------------------|-------------|-----------|
| 1 | [favor stakeholder A] | [favor stakeholder B] | [middle ground] | [which option] | [why] |
...
```

---

### Step 4: Prioritize Stakeholder Needs

```
PRIORITIZATION FRAMEWORK:

| # | Stakeholder | Need | Influence Score | Interest Score | Business Value | Risk if Ignored | Final Priority |
|---|------------|------|----------------|---------------|----------------|----------------|---------------|
| 1 | [who] | [what] | [1-5] | [1-5] | [HIGH/MED/LOW] | [HIGH/MED/LOW] | [MUST/SHOULD/COULD/WON'T] |
...

PRIORITY TIERS:

TIER 1 — MUST SATISFY (project fails without these):
- [Stakeholder]: [Need] — [Why it's Tier 1]
...

TIER 2 — SHOULD SATISFY (significant negative impact if missed):
- [Stakeholder]: [Need] — [Why it's Tier 2]
...

TIER 3 — COULD SATISFY (beneficial but not critical):
- [Stakeholder]: [Need] — [Why it's Tier 3]
...

TIER 4 — ACKNOWLEDGED BUT DEFERRED:
- [Stakeholder]: [Need] — [Why deferred and when to revisit]
...
```

---

### Step 5: Define Engagement Strategy

```
ENGAGEMENT PLAN:

| # | Stakeholder | Quadrant | Engagement Level | Communication Method | Frequency | Key Messages | Owner |
|---|------------|----------|-----------------|---------------------|-----------|-------------|-------|
| 1 | [who] | [from Step 2] | [inform/consult/involve/collaborate/empower] | [how — meeting, email, report, dashboard] | [how often] | [what to communicate] | [who manages this relationship] |
...

ENGAGEMENT LEVELS:
- INFORM: One-way communication, keep them aware
- CONSULT: Two-way communication, gather their input
- INVOLVE: Work directly with them throughout
- COLLABORATE: Partner with them on decisions
- EMPOWER: Delegate decision authority to them

STAKEHOLDER COMMUNICATION MATRIX:

| Event/Milestone | Manage Closely | Keep Satisfied | Keep Informed | Monitor |
|----------------|---------------|---------------|--------------|---------|
| Project kickoff | [action] | [action] | [action] | [action] |
| Requirements review | [action] | [action] | [action] | [action] |
| Design decisions | [action] | [action] | [action] | [action] |
| Testing results | [action] | [action] | [action] | [action] |
| Deployment | [action] | [action] | [action] | [action] |
| Post-deployment | [action] | [action] | [action] | [action] |

RISK OF DISENGAGEMENT:

| # | Stakeholder | Risk if Disengaged | Early Warning Signs | Mitigation |
|---|------------|-------------------|-------------------|-----------|
| 1 | [who] | [what goes wrong] | [how you'd notice] | [what to do] |
...
```

---

## Output Format

```
## STAKEHOLDER ANALYSIS: [System/Project Name]

### 1. Stakeholder Registry
[Complete list: direct, indirect, hidden stakeholders with categories and interests]

### 2. Influence-Interest Map
[Matrix with quadrant assignments and scoring rationale]

### 3. Needs and Conflicts
[Needs registry, conflict identification, resolution options]

### 4. Priority Tiers
[Prioritized stakeholder needs in MUST/SHOULD/COULD/WON'T tiers]

### 5. Engagement Strategy
[Engagement plan, communication matrix, disengagement risks]

### 6. Open Questions
[Items requiring further investigation or stakeholder input]
```

---

## Quality Checklist

Before completing:
- [ ] All stakeholder categories considered (direct, indirect, hidden)
- [ ] Hidden stakeholder discovery prompts applied
- [ ] Influence and interest scored with rationale
- [ ] All stakeholders placed in influence-interest quadrants
- [ ] Stakeholder needs documented with priorities
- [ ] Conflicts between stakeholders identified
- [ ] Resolution options proposed for each conflict
- [ ] Engagement strategy defined per quadrant
- [ ] Communication plan covers key project milestones
- [ ] Disengagement risks identified with mitigations

---

## Next Steps

After stakeholder analysis:
1. Use `/requirements` to elicit requirements from each stakeholder
2. Use `/conops` to develop operational concepts that satisfy stakeholder needs
3. Use `/tradestudy` to evaluate trade-offs between conflicting stakeholder needs
4. Use `/dcp` to create decision procedures for stakeholder conflict resolution
5. Use `/conflict` to deep-dive on specific stakeholder conflicts

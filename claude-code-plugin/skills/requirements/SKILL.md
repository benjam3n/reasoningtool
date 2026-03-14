---
name: "requirements - Requirements Elicitation & Specification"
description: Systematically discover, categorize, and specify all requirements for a project or system. Surfaces hidden requirements, resolves conflicts, and produces a structured specification.
output:
  format: "table"
---

# Requirements Elicitation & Specification

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Discover requirements for a new project**: The user has a project idea or goal and wants to systematically surface ALL requirements — functional, non-functional, constraints, and hidden assumptions — before building.
**Interpretation 2 — Audit requirements for an existing system**: The user has a system or product and wants to check if the requirements are complete, consistent, and well-specified.
**Interpretation 3 — Resolve conflicting requirements**: The user has identified requirements that conflict or compete and needs to prioritize and reconcile them.

If ambiguous, ask: "I can help with discovering requirements for a new project, auditing existing requirements, or resolving conflicts between requirements — which fits?"
If clear from context, proceed with the matching interpretation.

---

## Depth Scaling

Default: 2x. Parse depth from $ARGUMENTS if specified (e.g., "/requirements 4x [input]").

| Depth | Min Requirements Found | Min Categories | Min Stakeholders | Min Conflict Checks |
|-------|----------------------|----------------|------------------|---------------------|
| 1x    | 15                   | 4              | 3                | 2                   |
| 2x    | 30                   | 6              | 5                | 4                   |
| 4x    | 50                   | 8              | 7                | 6                   |
| 8x    | 80                   | 10             | 10               | 8                   |
| 16x   | 120                  | 12             | 15               | 12                  |

---

## The Process

### Step 1: Identify the System Boundary

Before listing requirements, define what's IN and OUT:

```
SYSTEM: [name]
PURPOSE: [one sentence]

IN SCOPE:
- [what this system does]
- [what this system manages]

OUT OF SCOPE:
- [what this system does NOT do]
- [adjacent systems]

BOUNDARY INTERFACES:
- [what goes IN to the system]
- [what comes OUT of the system]
- [what systems it connects to]
```

---

### Step 2: Stakeholder Analysis

Who has requirements for this system?

```
STAKEHOLDERS:

| # | Stakeholder | Relationship | Key Concern | Priority |
|---|-------------|-------------|-------------|----------|
| 1 | [who] | [how they interact] | [what they care about most] | HIGH/MED/LOW |
| 2 | [who] | [how they interact] | [what they care about most] | HIGH/MED/LOW |
...

HIDDEN STAKEHOLDERS (often missed):
- Future users (not current users)
- Maintainers (not just builders)
- Adjacent system owners
- Regulators/compliance
- Adversaries/attackers
- The system itself (self-management)
```

---

### Step 3: Requirement Categories

Systematically generate requirements across ALL categories:

#### 3A: Functional Requirements (What it DOES)

```
FUNCTIONAL REQUIREMENTS:

For each stakeholder, for each interaction:

| ID | Stakeholder | Action | Input | Output | Priority | Notes |
|----|-------------|--------|-------|--------|----------|-------|
| F1 | [who] | [verb] | [what goes in] | [what comes out] | MUST/SHOULD/COULD | [notes] |
...
```

#### 3B: Non-Functional Requirements (How WELL it does it)

| Category | Requirement | Measurable Target | Priority |
|----------|-------------|-------------------|----------|
| **Performance** | Response time | [specific metric] | |
| **Performance** | Throughput | [specific metric] | |
| **Scalability** | Growth handling | [specific metric] | |
| **Reliability** | Uptime | [specific metric] | |
| **Reliability** | Error handling | [specific behavior] | |
| **Security** | Authentication | [specific method] | |
| **Security** | Data protection | [specific standard] | |
| **Usability** | Learnability | [specific metric] | |
| **Usability** | Accessibility | [specific standard] | |
| **Maintainability** | Extensibility | [specific measure] | |
| **Maintainability** | Debuggability | [specific measure] | |
| **Compatibility** | Integrations | [specific systems] | |
| **Portability** | Platforms | [specific targets] | |

#### 3C: Constraints (What it CANNOT do or MUST comply with)

| Type | Constraint | Reason | Negotiable? |
|------|-----------|--------|-------------|
| **Technical** | [limitation] | [why] | YES/NO |
| **Business** | [limitation] | [why] | YES/NO |
| **Regulatory** | [limitation] | [why] | NO |
| **Resource** | [limitation] | [why] | YES/NO |
| **Timeline** | [limitation] | [why] | YES/NO |

#### 3D: Assumptions (What MUST be true for requirements to hold)

| ID | Assumption | If Wrong | Risk Level |
|----|-----------|----------|------------|
| A1 | [what's assumed] | [what breaks] | HIGH/MED/LOW |
...

#### 3E: Anti-Requirements (What it explicitly should NOT do)

| ID | Anti-Requirement | Reason |
|----|-----------------|--------|
| X1 | [what it must NOT do] | [why this matters] |
...

---

### Step 4: Hidden Requirements Discovery

Apply these prompts to surface requirements that stakeholders forgot to mention:

| Prompt | Requirement Found? |
|--------|-------------------|
| "What happens when [input] is missing?" | |
| "What happens when [input] is malformed?" | |
| "What happens at 10x current scale?" | |
| "What happens when [dependency] is down?" | |
| "What happens when a user does something unexpected?" | |
| "What does the FIRST interaction look like?" | |
| "What does the LAST interaction look like?" | |
| "What does day 2 look like vs day 1?" | |
| "What does the error state look like?" | |
| "What does the empty state look like?" | |
| "Who's the WORST user for this system?" | |
| "What's the most embarrassing failure?" | |
| "What would a competitor do better?" | |
| "What would you hate about using this?" | |
| "What would make you stop using this?" | |

---

### Step 5: Conflict Detection

Check all requirement pairs for conflicts:

```
CONFLICTS FOUND:

| Req A | Req B | Conflict Type | Resolution |
|-------|-------|---------------|------------|
| [R1] | [R2] | [contradiction / tension / resource competition] | [how to resolve] |
...

CONFLICT TYPES:
- Contradiction: A and B cannot both be true
- Tension: A and B pull in opposite directions
- Resource competition: A and B compete for same resource
- Priority conflict: Stakeholder X wants A, Stakeholder Y wants B
```

---

### Step 6: Prioritization (MoSCoW)

```
MUST HAVE (system doesn't work without these):
- [R1]: [reason it's must-have]
...

SHOULD HAVE (important but not blocking):
- [R5]: [reason]
...

COULD HAVE (nice to have):
- [R8]: [reason]
...

WON'T HAVE (explicitly excluded from this version):
- [R10]: [reason for deferral]
...
```

---

### Step 7: Specification Quality Check

For each MUST-HAVE requirement, verify:

| Quality | Test | Pass? |
|---------|------|-------|
| **Specific** | Could two people interpret this differently? | |
| **Measurable** | Can you verify this is met? | |
| **Achievable** | Is this technically possible? | |
| **Relevant** | Does this serve a stakeholder need? | |
| **Testable** | Can you write a test for this? | |
| **Independent** | Does this stand on its own? | |
| **Traceable** | Can you trace this to a stakeholder need? | |

---

## Output Format

```
## REQUIREMENTS SPECIFICATION: [System Name]

### System Boundary
[In scope / out of scope / interfaces]

### Stakeholders
[Table of stakeholders with priorities]

### Functional Requirements
[Numbered list with MoSCoW priority]

### Non-Functional Requirements
[Table with measurable targets]

### Constraints
[Table with negotiability]

### Assumptions
[Table with risk levels]

### Anti-Requirements
[What the system must NOT do]

### Hidden Requirements Discovered
[From Step 4 prompts]

### Conflicts & Resolutions
[Table of conflicts with resolutions]

### Priority Summary
MUST: [N] | SHOULD: [N] | COULD: [N] | WON'T: [N]

### Open Questions
[Requirements that need stakeholder input to resolve]
```

---

## Quality Checklist

Before completing:
- [ ] System boundary defined
- [ ] All stakeholder types considered (including hidden)
- [ ] All requirement categories covered (functional, non-functional, constraints, assumptions, anti-requirements)
- [ ] Hidden requirements prompts applied
- [ ] Conflicts identified and resolution proposed
- [ ] MoSCoW prioritization applied
- [ ] MUST-HAVE requirements pass quality check
- [ ] Open questions listed

---

## Next Steps

After requirements:
1. Use `/de` to identify dependencies between requirements
2. Use `/to` to sequence implementation
3. Use `/dcp` to create decision procedure for requirement conflicts
4. Use `/fla` to anticipate implementation failures

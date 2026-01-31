---
name: dss
description: "Complete system design workflow — from requirements through verified design."
---

# Design System

**Input**: $ARGUMENTS

---

## Overview

Complete system design workflow — composes multiple sub-procedures to go from requirements gathering through design generation, evaluation, selection, and verification.

## Steps

### Step 1: Gather Requirements
Define what the system must do:

1. **Functional requirements** (what it does):
   - FR1: [capability]
   - FR2: [capability]

2. **Performance requirements** (how well):
   - PR1: [metric and threshold]
   - PR2: [metric and threshold]

3. **Interface requirements** (how it connects):
   - IR1: [input/output/protocol]
   - IR2: [input/output/protocol]

4. **Constraints** (non-negotiable):
   - Budget: [amount]
   - Timeline: [deadline]
   - Technology: [must use/cannot use]
   - Regulatory: [compliance requirements]

5. **Quality attributes**:
   - Reliability, scalability, maintainability, security, usability
   - Which matter most? Rank them.

→ INVOKE: /rqg (requirements gathering) for thorough elicitation

### Step 2: Check for Existing Solutions
Before designing from scratch:

1. Does a complete solution already exist? (Buy vs build)
2. Does a partial solution exist that can be adapted?
3. Are there reference architectures or patterns for this type of system?
4. What have others done for similar problems?

→ INVOKE: /ans (analogous solutions) for cross-domain search

### Step 3: Decide Design Path
Based on Step 2:

| Situation | Path |
|-----------|------|
| Complete solution exists and fits | Adapt existing (Step 4) |
| Partial solution or pattern exists | Adapt + extend (Steps 4 + 5) |
| Nothing exists | Design from scratch (Steps 5-8) |

### Step 4: Adapt Existing Solution
If adapting:
1. What does the existing solution provide?
2. What gaps remain vs your requirements?
3. What modifications are needed?
4. What are the risks of modifying? (Breaking what works)
5. Is the adaptation cost less than building from scratch?

### Step 5: Generate Design Options
Create 2-3 distinct design approaches:

For each design option:
```
DESIGN OPTION [N]:
Name: [descriptive label]
Architecture: [high-level structure]
Key components: [major parts and their roles]
Technology choices: [what tools/frameworks/platforms]
Key tradeoff: [what this design optimizes for at the expense of]
```

**Design generation techniques:**
- Decompose by function (each component does one thing)
- Decompose by data (each component owns its data)
- Decompose by user (each component serves one user type)
- Reference architectures (adapt known patterns)
- → INVOKE: /ma (morphological analysis) for systematic variation

### Step 6: Evaluate Design Candidates
Compare options against requirements:

| Requirement | Design A | Design B | Design C |
|------------|----------|----------|----------|
| FR1 | [meets/partially/fails] | | |
| PR1 | [meets/partially/fails] | | |
| Cost | [estimate] | [estimate] | [estimate] |
| Complexity | [H/M/L] | [H/M/L] | [H/M/L] |
| Risk | [H/M/L] | [H/M/L] | [H/M/L] |

→ INVOKE: /crw (criteria weighted ranking) for systematic comparison

### Step 7: Select Best Design
Based on evaluation:
1. Which design meets the most requirements?
2. Which has the lowest risk?
3. Which is most feasible given constraints?
4. Document the rationale for selection
5. Document why alternatives were rejected (for future reference)

### Step 8: Verify Design
Before implementation:

1. **Requirements trace**: Can every requirement be traced to a design element?
2. **Completeness**: Are there design elements with no corresponding requirement? (Over-design)
3. **Consistency**: Do design elements conflict with each other?
4. **Feasibility**: Can each element actually be built with available resources?
5. **Risk**: What are the highest-risk elements? Plan to prototype those first.

→ INVOKE: /vp (verification procedures) for systematic verification

### Step 9: Report
```
SYSTEM DESIGN:
Requirements: [N functional, N performance, N interface, N constraints]
Design path: [adapt existing / extend / from scratch]

Selected design: [name]
Architecture: [high-level description]

Key components:
| Component | Function | Technology | Risk |
|-----------|----------|-----------|------|
| [component] | [what it does] | [how built] | [H/M/L] |

Alternatives rejected: [which and why]

Verification:
- Requirements coverage: [N/N mapped]
- Consistency: [issues found]
- Feasibility: [issues found]

Implementation priority: [what to build first — highest risk elements]
```

## When to Use
- Designing a new system from requirements
- Creating architecture for complex multi-component projects
- When multiple design options need systematic evaluation
- When design decisions need documented rationale
- → INVOKE: /rqg for requirements, /dsn for design principles, /enc for engineering conventions

## Verification
- [ ] Requirements gathered before design generation
- [ ] Existing solutions checked before designing from scratch
- [ ] At least 2 design candidates evaluated
- [ ] Evaluation uses explicit criteria tied to requirements
- [ ] Selected design verified against original requirements
- [ ] All design decisions have documented rationale

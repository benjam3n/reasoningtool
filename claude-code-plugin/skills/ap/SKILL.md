---
name: "ap - Architecture Patterns"
description: "Procedure for evaluating, choosing, and implementing software architecture patterns"
output:
  format: "prose"
---

# Architecture Patterns

## Overview
Procedure for evaluating, choosing, and implementing software architecture patterns

## Steps

### Step 1: Understand requirements and constraints
Gather the context needed for architectural decisions:
1. Document business requirements and drivers
2. Identify quality attribute requirements
3. Understand current state (if evolving existing system)
4. Document constraints (budget, timeline, skills)
5. Identify stakeholders and their concerns
6. Understand scale and growth projections

### Step 2: Identify candidate architectures
Identify architectural patterns that could work:
1. Review common patterns (monolith, microservices, etc.)
2. Consider hybrid approaches
3. Research how similar problems are solved
4. Consider team experience and preferences
5. Document 2-4 viable candidates

### Step 3: Evaluate candidates against requirements
Systematically evaluate each candidate:
1. Score each candidate against quality attributes
2. Evaluate against team capability
3. Assess operational requirements
4. Consider total cost of ownership
5. Evaluate flexibility and reversibility
6. Document tradeoffs for each option

### Step 4: Select architecture
Make the architectural decision:
1. Review evaluation results
2. Discuss with stakeholders
3. Consider reversibility and evolution
4. Make decision and document rationale
5. Identify risks and mitigation strategies
6. Get stakeholder buy-in

### Step 5: Create Architecture Decision Record
Document the decision formally:
1. Write ADR with context and decision
2. Document alternatives considered
3. Explain consequences and tradeoffs
4. Link to supporting analysis
5. Get formal approval if needed
6. Add to architectural documentation

### Step 6: Design component architecture
Design the detailed architecture:
1. Identify main components and their responsibilities
2. Define interfaces between components
3. Design data architecture
4. Plan integration patterns
5. Address cross-cutting concerns
6. Create architecture diagrams

### Step 7: Plan implementation roadmap
Create plan to implement the architecture:
1. Identify implementation phases
2. Define key milestones
3. Plan for incremental delivery
4. Identify dependencies and sequences
5. Plan risk mitigation
6. Create timeline


## When to Use
- Starting a new project and choosing initial architecture
- Evaluating whether to break apart a monolith
- Scaling challenges require architectural changes
- Adding major new capability to existing system
- Technical debt is causing architectural problems
- Team debating architectural approaches
- Documenting architectural decisions (ADRs)
- Reviewing and evolving existing architecture

## Verification
- Architecture addresses key quality requirements
- Decision is documented with rationale
- Tradeoffs are explicitly acknowledged
- Team has skills to implement
- Plan is realistic given constraints
- Stakeholders are aligned
- Architecture can evolve over time

---

**Input**: $ARGUMENTS

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Greenfield architecture selection**: The user is starting a new system or project and needs to evaluate and choose the right architectural pattern from scratch.
**Interpretation 2 — Architecture evolution**: The user has an existing system that's hitting scaling, complexity, or maintainability limits and needs to evaluate whether and how to change the architecture.
**Interpretation 3 — Architecture decision documentation**: The user has already made or is near making an architectural choice and wants to formally document it with rationale, tradeoffs, and an ADR.

If ambiguous, ask: "I can help with choosing architecture for a new system, evolving an existing architecture, or documenting an architectural decision — which fits?"
If clear from context, proceed with the matching interpretation.

---

Apply this procedure to the input provided.
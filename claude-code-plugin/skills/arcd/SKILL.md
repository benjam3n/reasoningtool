---
name: "arcd - Architecture Design Orderings"
description: "Orderings for software development — outside-in vs inside-out, API-first vs domain-first, top-down vs bottom-up."
---

# Architecture Design Orderings

**Input**: $ARGUMENTS

---

## Overview

The order you design software components determines the architecture that emerges. Outside-in starts from consumer needs. Inside-out starts from domain logic. Each produces different trade-offs.

## Ordering Rules

### Rule 1: Outside-In (API First)
- Start from what consumers/users need
- Define interfaces and contracts first
- Then implement behind those interfaces
- **When**: external consumers exist, API is the product, multiple teams integrate

### Rule 2: Inside-Out (Domain First)
- Start from core domain logic and data model
- Build outward to interfaces and adapters
- **When**: complex domain logic, unclear requirements, DDD approach

### Rule 3: Top-Down Decomposition
- Start from highest-level architecture
- Decompose into subsystems, then modules, then functions
- **When**: well-understood requirements, system-level view needed first

### Rule 4: Bottom-Up Composition
- Start from small, well-tested components
- Compose into larger systems
- **When**: reusable components, proven building blocks exist

### Rule 5: Spike-Then-Design
- Build a quick prototype to learn before designing
- Throw away the spike, design based on what was learned
- **When**: unfamiliar technology, uncertain approach

## Application
1. Assess: How clear are requirements? Who are the consumers? How complex is the domain?
2. Clear requirements + external consumers → Outside-In
3. Complex domain + evolving requirements → Inside-Out
4. Familiar patterns → Top-Down
5. Unknown territory → Spike first

## When to Use
- Starting new software projects or major features
- Choosing between architectural approaches

## Verification
- [ ] Approach chosen based on context
- [ ] Key interfaces defined early
- [ ] Core domain logic protected from external concerns
- [ ] Design validated before full implementation

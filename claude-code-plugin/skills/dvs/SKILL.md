---
name: "dvs - Diversity Search Orderings"
description: "Orderings that prioritize behavioral diversity, novelty, and coverage of solution space over convergence to a single optimum."
---

# Diversity Search Orderings

**Input**: $ARGUMENTS

---

## Overview

When you need multiple diverse solutions or when the objective landscape is deceptive (local optima trap greedy search), prioritize novelty and coverage over pure optimization. Inspired by novelty search and quality-diversity algorithms.

## Core Principle

Maximize the diversity of approaches tried before converging. A portfolio of different solutions beats a single optimized one when you're uncertain about what "best" means.

## Ordering Rules

### Rule 1: Novelty First
- Prioritize options that are most different from what you've already tried
- Define a distance metric between solutions
- **When**: deceptive objectives, creative tasks, brainstorming

### Rule 2: Niche Filling
- Divide the solution space into regions
- Ensure each region has at least one solution before deepening any
- **When**: need coverage, portfolio diversification

### Rule 3: Curiosity-Driven
- Prioritize areas where your predictions are worst (highest prediction error)
- Go where you're most surprised
- **When**: exploration, learning, research

### Rule 4: Anti-Convergence
- If multiple approaches are converging on the same solution, force divergence
- Explicitly try the opposite of current best
- **When**: avoiding groupthink, breaking out of ruts

## Application Procedure

### Step 1: Define the Solution Space
- What are the dimensions solutions can vary along?
- How do you measure distance between solutions?

### Step 2: Generate Diverse Candidates
- Start with maximally different approaches
- For each new candidate, maximize distance from existing ones

### Step 3: Evaluate and Maintain Diversity
- Keep the best solution per niche, not just the global best
- Resist premature convergence

## When to Use
- Creative problem-solving, brainstorming
- Research exploration
- Portfolio strategy
- When you suspect you're stuck in a local optimum

## Verification
- [ ] Diversity metric defined
- [ ] Multiple distinct approaches tried
- [ ] Not prematurely converged
- [ ] Solution space has coverage

---
name: "pb - Progressive Building Orderings"
description: "Build complexity incrementally — each step works before adding the next. Foundations before features."
---

# Progressive Building Orderings

**Input**: $ARGUMENTS

---

## Overview

Build systems, skills, and knowledge incrementally. Each layer must work before adding the next. This prevents the common failure of building complex structures on unverified foundations.

## Ordering Rules

### Rule 1: Foundation First
- Build the simplest working version before adding complexity
- Verify each layer works before building on top
- **When**: software development, learning, system design

### Rule 2: Scaffold — Work End-to-End First
- Get a minimal version working through the entire pipeline before optimizing any part
- A working skeleton beats a polished fragment
- **When**: multi-component systems, new projects

### Rule 3: Add One Thing at a Time
- Change one variable per iteration
- If something breaks, you know what caused it
- **When**: debugging, experimentation, iterative improvement

### Rule 4: Test at Each Level
- Don't wait until the end to test
- Each layer should be tested before the next is added
- **When**: any incremental build process

### Rule 5: Complexity Budget
- Each addition should be justified by its value
- Resist adding complexity "because we might need it"
- **When**: fighting scope creep, YAGNI principle

## Application

### Step 1: Define the Simplest Working Version
- What is the minimum that demonstrates the core concept works?

### Step 2: Identify Layers
- What complexity needs to be added, in what order?
- Each layer should add value and be independently testable

### Step 3: Build and Verify Layer by Layer
- Build layer → test → verify → next layer
- If a layer doesn't work, fix it before proceeding

## When to Use
- Software development, learning new skills, building organizations
- Any process where premature complexity causes failures

## Verification
- [ ] Simplest working version defined and built first
- [ ] Each layer tested before next added
- [ ] Only one thing changed per iteration
- [ ] Complexity justified by value

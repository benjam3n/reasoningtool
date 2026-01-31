---
name: "dsp - Mechanical Design Procedures"
description: "Systematic design of mechanical systems, chassis, and electromechanical assemblies."
---

# Mechanical Design Procedures

**Input**: $ARGUMENTS

---

## Overview

Structured approach to mechanical system design: from requirements through concept generation, analysis, prototyping, and validation. Prevents the common failure of jumping to CAD before understanding the problem.

## Steps

### Step 1: Define Requirements
1. Functional requirements (what must it DO?)
2. Performance specs (load, speed, precision, range of motion)
3. Environmental (temperature, humidity, vibration, corrosion)
4. Interface constraints (mounting, connections, clearances)
5. Manufacturing constraints (quantity, processes available, budget)
6. Standards and regulations

### Step 2: Concept Generation
1. Generate 3+ distinct concepts (not variations of one idea)
2. Sketch each concept (doesn't need to be pretty — needs to communicate)
3. For each: how does it meet each requirement?
4. → INVOKE: /ma [design problem] for morphological analysis if needed

### Step 3: Concept Selection
1. Score concepts against requirements using weighted criteria
2. → INVOKE: /cmp [concepts] for structured comparison
3. Select best concept for detailed design
4. Document why alternatives were rejected

### Step 4: Detailed Design and Analysis
1. Define geometry, materials, tolerances
2. Structural analysis: → INVOKE: /enc for calculations
3. Thermal analysis if applicable
4. Kinematic analysis for moving parts
5. Check: does it fit? (assembly, clearances, serviceability)

### Step 5: Prototype and Test
1. Build prototype (3D print, machined, whatever's fastest)
2. Test against each requirement
3. Record: what works, what doesn't, what surprised you
4. Iterate design based on test results

### Step 6: Documentation
1. Assembly drawings, BOM, manufacturing specs
2. → INVOKE: /dop for documentation procedures

## When to Use
- Designing robots, mechanisms, fixtures, enclosures
- Any physical system design

## Verification
- [ ] Requirements documented before designing
- [ ] Multiple concepts evaluated
- [ ] Analysis validates design meets requirements
- [ ] Prototype tested
- [ ] Manufacturing documentation complete

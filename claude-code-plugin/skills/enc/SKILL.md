---
name: "enc - Engineering Calculations"
description: "Standard engineering calculation procedures for robotics and mechanical system design — forces, torques, materials, actuator sizing."
---

# Engineering Calculations

**Input**: $ARGUMENTS

---

## Overview

Structured calculation procedures for mechanical and robotics engineering. Each follows: define requirements, identify relevant physics, select formulas, calculate, verify with safety factors.

## Steps

### Step 1: Define Requirements
1. What must the system do? (load, speed, range of motion, precision)
2. Operating conditions (temperature, environment, duty cycle)
3. Constraints (size, weight, cost, power budget)
4. Safety factor required (typically 2-4x for mechanical, higher for life-safety)

### Step 2: Identify Relevant Physics
- **Statics**: Forces, moments, equilibrium (F=0, M=0)
- **Dynamics**: Acceleration, inertia (F=ma, T=Iα)
- **Strength of materials**: Stress, strain, fatigue (σ=F/A, τ=T*r/J)
- **Kinematics**: Motion, velocity, workspace (DH parameters, Jacobian)
- **Thermal**: Heat dissipation, thermal expansion
- **Electrical**: Power, current, efficiency (P=IV, P=Tω)

### Step 3: Actuator Sizing (common calculation)
1. Calculate required torque: T = F × r + I × α + T_friction
2. Calculate required speed: ω = v / r (or from trajectory)
3. Select motor: T_motor × gear_ratio ≥ T_required × safety_factor
4. Check speed: ω_motor / gear_ratio ≥ ω_required
5. Check power: P = T × ω ≤ P_available
6. Check thermal: continuous vs peak ratings

### Step 4: Structural Analysis (common calculation)
1. Free body diagram: identify all forces and reactions
2. Calculate internal forces (shear, moment diagrams)
3. Calculate stress: σ = M×y/I (bending), τ = V×Q/(I×b) (shear)
4. Compare to material yield: σ_max < σ_yield / safety_factor
5. Check deflection: δ < δ_allowable
6. Check fatigue if cyclic loading

### Step 5: Verify
1. Units check (every term must have consistent units)
2. Order-of-magnitude check (does the answer make physical sense?)
3. Boundary check (what happens at extremes?)
4. Compare to similar existing systems

```
CALCULATION SUMMARY:
System: [description]
Requirement: [key spec]
Calculation: [key result with units]
Safety factor: [actual / required]
Status: [passes / fails / marginal]
```

## When to Use
- Sizing actuators, motors, structures
- Mechanical design verification
- Robotics system design

## Verification
- [ ] Requirements clearly stated with units
- [ ] Relevant physics identified
- [ ] Formulas correctly applied
- [ ] Units consistent throughout
- [ ] Safety factors applied
- [ ] Results sanity-checked

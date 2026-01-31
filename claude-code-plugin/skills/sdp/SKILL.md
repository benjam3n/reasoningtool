---
name: "sdp - Embedded Software Development"
description: "Developing embedded software for robotics and microcontroller-based systems."
---

# Embedded Software Development

**Input**: $ARGUMENTS

---

## Overview

Embedded software runs on hardware with real-time constraints, limited resources, and physical consequences for bugs. This procedure covers the specific challenges: hardware interfaces, real-time requirements, debugging without full OS support, and testing on physical systems.

## Steps

### Step 1: Define Hardware Interface
1. What hardware does the software control? (sensors, actuators, communication)
2. What are the interfaces? (GPIO, SPI, I2C, UART, CAN, USB)
3. What are the timing requirements? (sample rates, control loop frequency)
4. What are the resource constraints? (RAM, flash, CPU speed)
5. Get/create hardware documentation (pinouts, timing diagrams, datasheets)

### Step 2: Design Software Architecture
1. Choose RTOS vs bare-metal vs Linux (based on complexity and timing needs)
2. Define task/thread structure with priorities
3. Separate: hardware abstraction layer, control logic, communication, safety
4. Define interfaces between layers (so logic can be tested without hardware)

### Step 3: Implement Incrementally
1. Start with hardware bring-up: can you blink an LED? Read a sensor?
2. Add one peripheral at a time, verify each works
3. Build control logic on top of verified hardware layer
4. Add communication last
5. → INVOKE: /pb (progressive building) — each layer works before adding next

### Step 4: Test
1. Unit test control logic off-hardware (mock the HAL)
2. Integration test on hardware with known inputs
3. Stress test: edge cases, maximum rates, error conditions
4. Safety test: what happens on sensor failure? Communication loss? Power glitch?

### Step 5: Debug
1. Use logic analyzer/oscilloscope for timing issues
2. Use serial/JTAG debug for software issues
3. Add instrumentation (timing pins, debug output) early
4. Common embedded bugs: race conditions, stack overflow, interrupt priority inversion, DMA conflicts

## When to Use
- Robotics, IoT, motor control, sensor systems
- Any software running on microcontrollers or embedded Linux

## Verification
- [ ] Hardware interfaces documented
- [ ] Architecture separates hardware from logic
- [ ] Incremental bring-up (not all-at-once)
- [ ] Logic testable without hardware
- [ ] Safety/failure cases tested

---
name: "rso - Resource Optimization Orderings"
description: "Orderings for maximizing throughput, minimizing waste, and efficient resource utilization."
---

# Resource Optimization Orderings

**Input**: $ARGUMENTS

---

## Overview

Order work to maximize throughput, minimize idle resources, reduce waste, and exploit batching. Lean and operations research principles applied to any process.

## Ordering Rules

### Rule 1: Bottleneck First (Theory of Constraints)
- Find the bottleneck (step limiting total throughput)
- Never let it be idle — schedule everything around it
- **When**: pipeline processing, clear capacity constraint

### Rule 2: Batch Similar Work
- Group similar tasks to reduce switching overhead
- **When**: setup costs between types, cognitive overhead

### Rule 3: Eliminate Waste (Lean)
- Remove non-value-adding steps (waiting, over-processing, transport)
- **When**: process optimization

### Rule 4: Parallelize Independent Work
- Only serialize what has dependencies
- **When**: multiple resources available

### Rule 5: Just-In-Time
- Don't produce before needed (creates inventory/waste)
- Pull-based: demand triggers work
- **When**: reducing WIP, avoiding overproduction

## Application
1. Map the value stream (all steps, times, waits)
2. Identify bottleneck
3. Optimize: maximize bottleneck utilization, batch, parallelize, eliminate waste
4. Measure throughput and cycle time

## When to Use
- Manufacturing, pipelines, service operations, any efficiency-focused process

## Verification
- [ ] Bottleneck identified
- [ ] Waste reduced
- [ ] Independent work parallelized
- [ ] Throughput measured

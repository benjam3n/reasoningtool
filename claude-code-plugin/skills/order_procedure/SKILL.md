---
name: order_procedure
description: "Determine the correct execution order for a set of steps based on dependencies and constraints"
---

# Order Procedure

## Overview
Determine the correct execution order for a set of steps based on dependencies and constraints

## Steps

### Step 1: Collect steps and identify dependencies
Gather all steps and identify their dependency relationships:
1. List all steps from input steps_list
2. For each step, identify:
   - Inputs required (implies dependency on source)
   - Outputs produced (others may depend on)
   - Resources used (potential conflicts)
   - Constraints (deadlines, ordering requirements)
3. Classify each dependency by type (hard, soft, mutual exclusion, resource)

### Step 2: Build dependency graph
Construct a directed graph representing dependencies:
1. Create a node for each step
2. Add directed edge A->B for each hard dependency
3. Add directed edge A~>B for each soft dependency (marked differently)
4. Mark mutual exclusion relationships
5. Annotate resource dependencies on edges

### Step 3: Detect and resolve circular dependencies
Check for cycles and resolve them:
1. Run cycle detection algorithm on the graph
2. If cycle found:
   - Identify all steps in the cycle
   - Examine each edge: is it really a hard dependency?
   - Often one edge is actually a soft dependency
   - Break the weakest edge in the cycle
3. Repeat until no cycles remain
4. If cycle cannot be broken, flag as planning error

### Step 4: Compute valid execution order
Perform topological sort to get valid ordering:
1. Use Kahn's algorithm or DFS-based topological sort
2. If multiple valid orders exist, collect all nodes with no incoming edges
3. Apply prioritization rules to choose among equal-priority nodes:
   - Blocking steps before blocked (unblocks more work)
   - Critical path steps first (determines total duration)
   - High-risk steps early (fail fast)
   - Quick wins if equal priority (builds momentum)
   - Steps with many dependents first (maximizes unblocked work)
4. Respect soft dependencies where possible without violating hard dependencies

### Step 5: Identify parallel execution opportunities
Group steps that can run simultaneously:
1. For each pair of steps, check:
   - No dependency relationship (neither depends on other)
   - No resource conflict
   - No mutual exclusion constraint
2. Group parallel-eligible steps that share the same "depth" in the graph
3. Format as parallel groups with sync points

### Step 6: Identify critical path
Find the longest dependency chain:
1. Calculate the "depth" of each step (longest path to reach it)
2. Identify the path with maximum total depth
3. Mark steps on critical path (these determine minimum duration)
4. Calculate slack for non-critical steps

### Step 7: Apply optimization rules
Optimize the sequence for efficiency:
1. Minimize context switches: group related steps together
2. Front-load risk: move uncertain steps earlier
3. Batch similar operations: group steps using same tools/resources
4. Respect energy constraints: if human executor, hard steps when fresh
5. Verify constraints are still satisfied after optimization

### Step 8: Format and output final order
Produce the final ordered output in requested format:
1. Simple numbered list
2. With parallelism markers
3. With dependency annotations
4. Gantt-compatible format (if requested)


## When to Use
- After generating steps from a COMPLETE_PLAN
- When steps have dependencies that must be satisfied
- When parallel execution opportunities should be identified
- When optimizing execution sequence for efficiency
- When constraints (deadlines, resources) must be respected
- When building a Gantt chart or execution timeline

## Verification
- Every step's dependencies appear earlier in the sequence
- No step requires something that hasn't been produced yet
- All explicit constraints are satisfied
- Parallel groups contain no dependent steps
- Critical path is correctly identified
- Optimization rationale is documented

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.
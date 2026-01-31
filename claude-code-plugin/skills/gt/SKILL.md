---
name: "gt - Graph Traversal Orderings"
description: "Orderings derived from graph traversal algorithms — BFS for breadth, DFS for depth, topological for dependencies."
---

# Graph Traversal Orderings

**Input**: $ARGUMENTS

---

## Overview

Many problems have graph structure (dependencies, relationships, hierarchies). The traversal order determines what you find and how efficiently. BFS explores breadth-first (all neighbors before going deeper), DFS explores depth-first (follow one path to its end), topological ordering respects dependencies.

## Core Principle

Structure determines traversal. Dependencies need topological order. Shortest paths need BFS. Full exploration needs DFS. Match the algorithm to what you need.

## Ordering Rules

### Rule 1: BFS — Breadth First
- Explore all immediate neighbors before going deeper
- Guarantees shortest path in unweighted graphs
- **When**: finding shortest/quickest route, exploring all options at each level, level-order processing

### Rule 2: DFS — Depth First
- Follow one path as far as it goes before backtracking
- Uses less memory, finds paths quickly (not necessarily shortest)
- **When**: exhaustive search, maze solving, detecting cycles, topological sort

### Rule 3: Topological — Dependencies First
- Process nodes only after all their prerequisites are processed
- Only works on directed acyclic graphs (DAGs)
- **When**: build systems, task scheduling, prerequisite chains

### Rule 4: Dijkstra/A* — Cost-Guided
- Expand the cheapest unexplored node (Dijkstra) or cheapest + heuristic (A*)
- Guarantees optimal paths in weighted graphs
- **When**: finding cheapest/fastest route with varying costs

### Rule 5: Reverse Postorder — Dependencies via DFS
- DFS but process nodes in reverse order of completion
- Produces topological ordering
- **When**: compiler optimizations, strongly connected components

## Application Procedure

### Step 1: Model as Graph
- What are the nodes? (tasks, states, decisions, entities)
- What are the edges? (dependencies, transitions, relationships)
- Directed or undirected? Weighted or unweighted? Cyclic?

### Step 2: Select Traversal
- Need shortest path (unweighted) → BFS
- Need exhaustive exploration → DFS
- Need dependency ordering → Topological
- Need cheapest path (weighted) → Dijkstra/A*

### Step 3: Execute and Track
- Mark visited nodes to avoid cycles
- Record the traversal order
- Extract the answer from the traversal

## When to Use
- Task scheduling with dependencies
- Exploring decision spaces
- Finding paths or connections
- Any problem with graph/tree structure

## Verification
- [ ] Problem modeled as graph correctly
- [ ] Traversal algorithm matched to need
- [ ] All reachable nodes visited (or search terminated correctly)
- [ ] Dependencies respected (no node processed before prerequisites)

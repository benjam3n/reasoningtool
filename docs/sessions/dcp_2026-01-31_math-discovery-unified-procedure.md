# DCP — Discovering New Math: Area-Specific Techniques (Unified Procedure)

**Date**: 2026-01-31
**Input**: methods of discovering new math — use subagents for techniques in combinatorics, category theory, topology, number theory, and algebraic geometry

---

This is the unified decision procedure assembled from 5 parallel subagent analyses. Each subagent produced dimensions, options, assumptions, methods, and worked examples for one mathematical area.

**Component files**:
- `dcp_2026-01-31_math-discovery-combinatorics-subagent.md`
- `dcp_2026-01-31_math-discovery-category-theory-subagent.md`
- `dcp_2026-01-31_math-discovery-topology-subagent.md`
- `dcp_2026-01-31_math-discovery-number-theory-subagent.md`
- `dcp_2026-01-31_math-discovery-algebraic-geometry-subagent.md`

---

## The Procedure

```
DISCOVERING NEW MATH BY AREA — PROCEDURE
==========================================

PURPOSE: Given a mathematical area, this procedure
produces concrete candidate research directions using
area-specific discovery methods.

STEP 0: Which area are you working in?
┌──────────────────────────┬───────────────┐
│ Area                     │ Go to         │
├──────────────────────────┼───────────────┤
│ Combinatorics            │ SECTION A     │
├──────────────────────────┼───────────────┤
│ Category Theory          │ SECTION B     │
├──────────────────────────┼───────────────┤
│ Topology                 │ SECTION C     │
├──────────────────────────┼───────────────┤
│ Number Theory            │ SECTION D     │
├──────────────────────────┼───────────────┤
│ Algebraic Geometry       │ SECTION E     │
├──────────────────────────┼───────────────┤
│ Multiple / Cross-field   │ Pick TWO      │
│                          │ sections and  │
│                          │ run both —    │
│                          │ intersections │
│                          │ are richest   │
└──────────────────────────┴───────────────┘
```

---

### SECTION A: Combinatorics — Top 5 Methods

**A1 — Hypergraph Lifting**: Take any graph theory theorem. Replace "graph" with "k-uniform hypergraph." Check if analog is known. Most aren't.

**A2 — Derandomization**: Take any probabilistic method proof. Ask: can it be made constructive? If unknown, this is an open problem.

**A3 — Forbidden Substructure Systematization**: Pick an object type. Enumerate small forbidden substructures. For each: extremal function? Extremal configuration? Stability result?

**A4 — Cross-Field Import**: Take a technique from another field (topological methods, Fourier analysis, flag algebras, entropy method) and apply it to a combinatorial problem where it hasn't been tried.

**A5 — Parameter Flip**: For any extremal result maximizing A subject to B, ask about maximizing B subject to A.

**Key trap**: Don't assume graph proofs generalize to hypergraphs with the same proof.

---

### SECTION B: Category Theory — Top 5 Methods

**B1 — Systematic Categorification**: Take any set-level construction. What is the 2-categorical version? The ∞-categorical version? Replace equations with isomorphisms, isomorphisms with equivalences.

**B2 — Monad Decomposition**: For any monad T on C, describe the Eilenberg-Moore category C^T explicitly. If no one has, this is new math.

**B3 — Enrichment Variation**: Take any concept for Set-enriched categories. Enrich over V (Ab, Top, sSet, Vect_k). Check which theorems still hold.

**B4 — Internalization**: Take any external construction and do it internally to a category C. What are [your structure] in [unexpected category]?

**B5 — Adjunction Mining**: For any functor F, systematically attempt to construct left/right adjoints. If no adjoint exists, characterize the obstruction.

**Key trap**: Don't assume strict and weak versions are equivalent. Coherence theorems are rare.

---

### SECTION C: Topology — Top 5 Methods

**C1 — Boundary Variation**: Take any theorem about closed manifolds. Ask: compact with boundary? Non-compact? Manifolds with corners? The proof usually breaks — the failure point is the research.

**C2 — Spectral Sequence Differential Hunting**: For any spectral sequence, list natural spaces/fibrations. Compute which differentials (d₃, d₄, ...) are unknown. Uncomputed differentials for natural spaces are publishable.

**C3 — Equivariant Upgrade**: Take any non-equivariant theorem. What is the G-equivariant version for G = Z/2, S¹, finite groups, compact Lie groups?

**C4 — Invariant Transfer**: Pick an invariant defined for category C₁. List related categories C₂. Does the invariant extend?

**C5 — Physical Structure Import**: Find a physical theory using topological spaces. What structure does the physics predict? Can you define it rigorously?

**Key trap**: Don't assume smooth and topological categories give the same answers. Dimension 4 is exceptional.

---

### SECTION D: Number Theory — Top 5 Methods

**D1 — Field Variation**: Take any theorem over Q. Does it hold over number fields? Function fields F_q(t)? p-adic fields? For each failure, find the obstruction.

**D2 — L-function Special Values**: For any L-function, compute values at integers. If the values lack known interpretation, you're touching Beilinson/Bloch-Kato conjectures.

**D3 — Family Formation**: Instead of one object, study families. Prove average behavior. This often bypasses individual-case difficulties.

**D4 — Effectivity Gap**: List major finiteness theorems. Check which have effective algorithms. Where there's no effective version, that's an open problem.

**D5 — Function Field Translation**: Translate a hard problem over number fields to function fields, where geometric methods apply. Solve there, then ask what ports back.

**Key trap**: Don't trust computational evidence for infinitary statements. Patterns can break at astronomically large numbers.

---

### SECTION E: Algebraic Geometry — Top 5 Methods

**E1 — Base Change Interrogation**: Take any theorem over C. Does it hold over finite fields? Char p? Number fields? Over Z? Each failure reveals arithmetic structure.

**E2 — Singularity Degradation**: For any result for smooth varieties, weaken: smooth → normal → canonical → klt → log canonical → Cohen-Macaulay → non-reduced. Where does it break?

**E3 — Derived Category Interrogation**: For any variety X: semiorthogonal decompositions? Derived equivalences? Exceptional collections? Stability conditions?

**E4 — Tropicalization**: Compute trop(X). What geometric properties are visible combinatorially? Can you compute invariants via tropical geometry?

**E5 — Point Counting Patterns**: For X over F_p, compute |X(F_q)| for small q. Compare to Weil conjecture predictions. Discrepancies reveal unexpected structure.

**Key trap**: Don't assume "projective over C" is the fundamental case. Singularities, char p, and stacks are all essential.

---

## CROSS-AREA DISCOVERY (highest value)

The richest discoveries come from running TWO sections and looking for connections:

| Pair | What to Look For |
|------|-----------------|
| Combinatorics + Topology | Topological methods proving combinatorial results (Borsuk-Ulam → ham sandwich). Combinatorial models of spaces. |
| Category Theory + Topology | ∞-categorical versions of topological constructions. Factorization homology. Operadic structures. |
| Number Theory + Alg. Geometry | Arithmetic geometry: point counts, étale cohomology, modularity. Langlands program. |
| Combinatorics + Alg. Geometry | Tropical geometry. Schubert calculus. Matroids and Chow rings. |
| Category Theory + Number Theory | Derived algebraic geometry for arithmetic. Motivic cohomology. Prismatic cohomology via stacks. |
| Topology + Number Theory | Arithmetic topology (primes ↔ knots). Étale homotopy. Chromatic homotopy and formal groups. |

---

## COMMON MISTAKES (all areas)

1. **Assuming "no one has done this" means it's uninteresting** — Search before dismissing. Many obvious questions are genuinely open.
2. **Single-method fixation** — If one approach yields nothing after genuine effort, switch methods.
3. **Skipping computation** — Compute examples before axiomatizing. Computational discovery is underrated.
4. **Staying within one area** — Cross-area connections yield the richest discoveries.
5. **Over-generalizing** — Sometimes generalizing destroys the structure. Find the weakest conditions under which interesting structure persists.

---

## WHEN TO OVERRIDE

- **Expert collaborator available** — Conversation with a domain expert can short-circuit the procedure.
- **Error spotted in a paper** — Follow that thread immediately.
- **Strong intuition** — Follow it first, come back to systematic methods if it fails.

---

*Validation status: Not validated by domain experts. Synthesizes methods from mathematical practice across five major areas.*

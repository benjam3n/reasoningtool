# DCP Subagent — Topology Discovery Techniques

**Date**: 2026-01-31
**Input**: Discovery techniques in topology (subagent output for larger DCP on mathematical discovery)

---

## 1. Discovery Dimensions for Topology

| Dimension | Description |
|-----------|-------------|
| **Space Type** | The category of topological objects under study (manifolds, CW complexes, simplicial sets, topological groups, fiber bundles, stratified spaces, orbifolds, singular spaces) |
| **Dimension Range** | The dimension of the spaces being studied (low-dimensional 1-4, middle-dimensional 5-8, high-dimensional 9+, infinite-dimensional, dimension-independent) |
| **Structure Level** | Degree of geometric structure (topological, PL, smooth, almost complex, symplectic, contact, Riemannian) |
| **Invariant Type** | The algebraic/categorical invariants used (homotopy groups, homology theories, cohomology operations, K-theory, cobordism, characteristic classes, knot invariants) |
| **Method/Technique** | Primary technical approach (surgery theory, spectral sequences, obstruction theory, Morse theory, sheaf theory, category theory, operads, derived functors) |
| **Boundary Conditions** | Nature of the space boundary/endpoints (closed, with boundary, non-compact, compactified, at infinity, cusps, corners) |
| **Symmetry/Action** | Group actions and equivariance (no symmetry, finite group action, Lie group action, gauge symmetry, orbifold structure) |
| **Computational Aspect** | Algorithmic/computational questions (persistent homology, discrete Morse theory, computational complexity, explicit calculations, effective bounds) |
| **Physical Connection** | Links to physics and applied topology (TQFT, string topology, gauge theory, symplectic field theory, topological data analysis, network topology) |
| **Functoriality** | Categorical and functorial properties (contravariant/covariant, natural transformations, adjunctions, derived categories, ∞-categories) |
| **Localization** | Working with restricted classes (rational homotopy, p-local, chromatic, stable vs unstable, finite type, nilpotent) |
| **Duality Type** | Duality phenomena (Poincaré duality, Alexander duality, Spanier-Whitehead duality, Koszul duality, Langlands duality) |

## 2. Options per Dimension

### Space Type
- Smooth manifolds (closed, open, with boundary)
- Topological manifolds
- CW complexes (finite, infinite)
- Simplicial complexes and simplicial sets
- Topological groups (Lie groups, discrete groups, p-adic groups)
- Fiber bundles (vector bundles, principal bundles, fibrations)
- Classifying spaces (BG for groups G)
- Loop spaces and suspension spaces
- Thom spaces
- Stratified spaces
- Orbifolds
- Algebraic varieties (with Zariski, étale, or analytic topology)
- Mapping spaces (continuous, smooth, holomorphic)
- Configuration spaces
- Moduli spaces
- Singular spaces

### Dimension Range
- 0-dimensional (discrete spaces, Cantor sets)
- 1-dimensional (circles, graphs, 1-manifolds)
- 2-dimensional (surfaces, Riemann surfaces)
- 3-dimensional (3-manifolds, knot complements)
- 4-dimensional (smooth 4-manifolds, exotic structures)
- 5-8 dimensional (middle dimensions, surgery theory applies)
- High-dimensional (9+, where surgery theory is fully effective)
- Infinite-dimensional (Hilbert manifolds, Banach manifolds, function spaces)
- Mixed dimension (stratified spaces)
- Dimension-independent (statements true for all dimensions)

### Structure Level
- Purely topological
- PL (piecewise linear)
- Smooth (differentiable manifolds)
- Almost complex
- Complex (complex manifolds, Kähler manifolds)
- Symplectic
- Contact
- Riemannian (metric structure)
- Spin/Spinc structures
- Framed (framed manifolds)
- Oriented vs non-oriented
- Calibrated geometries (G2, Spin(7))

### Invariant Type
- Homotopy groups πn(X)
- Homology (singular, cellular, simplicial, Borel-Moore)
- Cohomology (singular, de Rham, Čech, sheaf cohomology)
- Cohomology operations (Steenrod squares, power operations)
- K-theory (topological, algebraic, twisted, equivariant)
- Cobordism (oriented, unoriented, complex, framed, MU, MSp)
- Characteristic classes (Chern, Stiefel-Whitney, Pontryagin, Euler)
- Knot invariants (Alexander, Jones, Khovanov homology, Heegaard Floer)
- Gromov-Witten invariants
- Donaldson/Seiberg-Witten invariants
- Floer homologies (symplectic, Heegaard, instanton, monopole)
- Categorical invariants (derived categories, Fukaya categories)
- Magnitude, persistent homology, barcodes

### Method/Technique
- Surgery theory
- Spectral sequences (Serre, Atiyah-Hirzebruch, Adams, Eilenberg-Moore)
- Obstruction theory
- Morse theory (classical, discrete, Morse-Bott)
- Handle decompositions
- Fibrations and fiber sequences
- Cofibrations and cofiber sequences
- Localization and completion
- Model categories and homotopy theory
- Operads and PROPs
- Sheaf theory and derived functors
- Higher category theory (∞-categories, ∞-topoi)
- Factorization homology
- Sheaves and cosheaves on stratified spaces

### Boundary Conditions
- Closed (compact without boundary)
- Compact with boundary
- Non-compact, finite type
- Non-compact, infinite type
- One-point compactification
- Ends (one end, multiple ends, wild ends)
- Compactifications (Stone-Čech, Borel-Serre, Deligne-Mumford)
- Cusps and corners (manifolds with corners)
- Relative (pairs (X,A) where A is a subspace)

### Symmetry/Action
- No symmetry
- Finite group action (Zn, Sn, dihedral groups)
- Compact Lie group action (circle actions, torus actions, SO(n), SU(n))
- Discrete group action (fundamental group, mapping class group)
- Gauge group action
- Orbifold structure
- Equivariant theory (Bredon cohomology, equivariant K-theory)
- Fixed point data and localization
- Transformation groupoids

### Computational Aspect
- Persistent homology (filtrations, barcodes, stability)
- Discrete Morse theory
- Algorithmic decidability (homeomorphism problem, knot equivalence)
- Computational complexity (of invariants, of recognition problems)
- Explicit calculations (specific homotopy groups, specific homology)
- Effective bounds
- Computer-assisted proofs
- Database construction (manifold atlases, knot tables)
- Machine learning on topological data

### Physical Connection
- Topological quantum field theory (Chern-Simons, Donaldson, Seiberg-Witten)
- String topology and loop spaces
- Gauge theory (Yang-Mills, instantons, monopoles)
- Symplectic field theory
- Mirror symmetry (homological, symplectic)
- Condensed matter (topological phases, band theory)
- Topological data analysis

### Localization
- Rational homotopy theory (rationalization, minimal models)
- p-local homotopy theory
- Chromatic homotopy theory (chromatic filtration, Morava K-theories)
- Stable homotopy (stable homotopy groups of spheres)
- Unstable homotopy
- Finite type
- Nilpotent spaces

### Duality Type
- Poincaré duality (closed oriented manifolds)
- Lefschetz duality (manifolds with boundary)
- Alexander duality
- Spanier-Whitehead duality (stable homotopy category)
- Verdier duality (derived categories of sheaves)
- Koszul duality (operads, algebras)
- Atiyah duality (Thom spaces)

## 3. Hidden Assumptions in Topological Discovery

| Assumption | Why It's Dangerous |
|------------|-------------------|
| **"Results for closed manifolds extend to manifolds with boundary"** | Many fundamental theorems fail at the boundary. Poincaré duality requires modification (Lefschetz duality), index theorems need boundary corrections (APS index theorem). |
| **"Higher homotopy groups are too hard to compute to be useful"** | You don't need complete computation. Partial information, bounds, or knowledge modulo torsion can be sufficient. Computational nihilism prevents asking "what can I prove with incomplete invariants?" |
| **"Smooth and topological categories give the same answers"** | True in dimensions ≠4 by surgery theory, but dimension 4 is exceptional: exotic R⁴s, uncountably many smooth structures on R⁴. |
| **"Known spectral sequences are fully exploited"** | Most spectral sequences have only had their E₂ pages computed for standard spaces. The differentials, extensions, and exotic examples remain unexplored. |
| **"Low-dimensional results don't generalize"** | Knot theory and surface topology techniques — braids, mapping class groups, Heegaard splittings — have high-dimensional analogues. |
| **"Equivariant topology is just ordinary topology with extra bookkeeping"** | Equivariant phenomena can be qualitatively different: localization theorems make infinite-dimensional calculations finite, fixed points carry different cohomology operations. |
| **"Rational homotopy theory solves all homotopy questions rationally"** | Works for simply-connected spaces, but fails for non-simply-connected spaces. π₁ doesn't rationalize nicely. |
| **"Invariants from physics are too imprecise for pure mathematics"** | Floer homology, Khovanov homology, TQFTs are now rigorous mathematics. Dismissing gauge theory would have missed Donaldson's theorem, exotic R⁴s, Property P. |
| **"Classical obstruction theory handles all extension problems"** | Modern problems involve structured maps (A∞ maps, ∞-categorical lifts), parametrized families, derived settings that classical theory can't handle. |
| **"The stable and unstable categories are independent"** | Chromatic homotopy uses stable information to understand unstable (Goodwillie calculus). EHP sequence, Snaith's theorem connect them. |

## 4. Specific Discovery Methods for Topology

### Method 1: Boundary Variation
Take any theorem about closed manifolds. Ask systematically: what happens for compact with boundary, non-compact finite type, manifolds with corners, compactified at infinity?

### Method 2: Spectral Sequence Differential Hunting
For any spectral sequence, list the top 20 most natural spaces/fibrations. Compute which differentials (d₂, d₃, d₄,...) are unknown. Uncomputed differentials for natural spaces are publishable.

### Method 3: Dimension Jumping
Take any theorem proved in dimensions n ≥ k. Try to prove it for k-1. The obstruction to lowering dimension is often an interesting invariant.

### Method 4: Invariant Transfer
Pick an invariant I defined for category C₁. List 5-10 related categories C₂. For each, ask: does I extend to C₂? Is there a functorial extension?

### Method 5: Equivariant Upgrade
Take any non-equivariant theorem. Ask: what is the G-equivariant version for G = Z/2, S¹, finite groups, compact Lie groups?

### Method 6: Computational Complexity Questions
For any topological invariant I, ask: what is the computational complexity of computing I(X) given X as a simplicial complex?

### Method 7: Duality Reversal
Find a duality theorem. Ask: what structure on one side corresponds to what structure on the dual side?

### Method 8: Fibration Invariant Mining
For a fibration F → E → B, list 20 natural fibrations from geometry. For each, ask: what is the E₂ page? What are the differentials? What geometric meaning do the differentials have?

### Method 9: Localization Comparison
For any space X, compare rational, p-local, and integral homotopy. What information is lost in localization? What arithmetic phenomena appear?

### Method 10: Physical Structure Import
Find a physical theory using topological spaces. Ask: what structure does the physics predict should exist? Can you define it rigorously?

### Method 11: Operadic Structure Discovery
Take any space where you can compose operations. Ask: is there an operad acting? Is it well-known? What does algebra over this operad mean geometrically?

### Method 12: Persistent/Parametrized Versions
Take any classical invariant. Define a filtered or parametrized version. What is the persistence module? What stability theorems exist?

### Method 13: Manifold Census Completion
For each dimension d and structure type, ask: is there a complete census of manifolds satisfying natural finiteness conditions?

### Method 14: Cobordism Nullity Questions
For any cohomology theory E and manifold M, ask: is M E-null-cobordant? For non-standard theories (K-theory, elliptic cohomology, TMF), most questions are open.

### Method 15: Higher Categorical Strictification
Many natural structures are weakly defined. Ask: when can you strictify? Each case requires its own coherence theorem.

## 5. Worked Example: Spectral Sequence Differential Hunting for Configuration Spaces

**Target**: Ordered configuration spaces F_n(S^d) of n points in the d-sphere.

**Fibration**: S^d \ {x₁,...,x_{n-1}} → F_n(S^d) → F_{n-1}(S^d)

**For d=3, n=3**: Fiber is S³ minus two points ≃ S² ∨ S². Base is F₂(S³) ≃ S³.

The E₂ page of the Serre spectral sequence is computable: E²_{p,q} = H_p(S³) ⊗ H_q(S² ∨ S²).

**Key unknown**: The d₃ differential d₃: E³_{3,2} → E³_{0,4}, a map Z² → Z.

**Geometric interpretation**: Measures how the two 2-spheres created by removing two points interact with the S³ direction as you vary the first two points.

**Literature check**: This specific differential appears to not be explicitly computed in published literature for general n ≥ 4.

**Result**: A concrete research direction — computing spectral sequence differentials for configuration spaces on spheres — discovered by mechanical application of the method.

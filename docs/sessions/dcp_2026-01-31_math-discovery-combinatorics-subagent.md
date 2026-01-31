# DCP Subagent — Combinatorics Discovery Techniques

**Date**: 2026-01-31
**Input**: Discovery techniques in combinatorics (subagent output for larger DCP on mathematical discovery)

---

## 1. Discovery Dimensions for Combinatorics

| Dimension | Description | Why It Matters |
|-----------|-------------|----------------|
| **Object Type** | The combinatorial structure being studied (graphs, hypergraphs, matroids, posets, permutations, partitions, designs, set systems, simplicial complexes, polytopes) | Different objects have different natural questions, invariants, and proof techniques. Many results transfer between object types with modification. |
| **Parameter Regime** | Whether you're working in sparse/dense, small/large, finite/infinite, exact/asymptotic regimes | Techniques often break down or simplify dramatically at regime boundaries. Sparse and dense regimes often require completely different methods. |
| **Proof Technique** | The primary method used (probabilistic method, algebraic method, linear algebra, topological method, Ramsey-type arguments, extremal arguments, generating functions, analytic combinatorics, polynomial method, container method, flag algebras) | Each technique has a "natural home" but can often be exported to new settings. Identifying which technique was used reveals transfer opportunities. |
| **Quantitative vs Structural** | Whether the result gives bounds/counts (quantitative) or characterizes structure (qualitative/extremal) | Quantitative results often have structural refinements and vice versa. "How many?" and "What does the extremal case look like?" are complementary questions. |
| **Computational Complexity** | The algorithmic aspect (enumeration complexity, optimization hardness, decision problem classification, approximability, parametrized complexity) | Combinatorial results often have computational shadows. Existence proofs may not yield algorithms; algorithmic questions reveal new mathematical structure. |
| **Algebraic Connection** | How the combinatorics connects to algebra (representation theory, algebraic geometry, commutative algebra, noncommutative algebra, Coxeter groups, symmetric functions) | Algebraic structure often provides powerful invariants and proof techniques. Many "purely combinatorial" questions have algebraic reformulations that are easier. |
| **Dimensionality/Rank** | The dimension, rank, or order of the structure (graphs are rank-2 hypergraphs; higher ranks behave differently) | Many graph theory results have unknown hypergraph analogs. Dimension transitions reveal new phenomena. |
| **Constraint Type** | What restrictions are imposed (forbidden substructures, degree constraints, chromatic conditions, intersection patterns, monotonicity, symmetry) | Each constraint type creates a theory. Combining constraints or relaxing them systematically generates new questions. |
| **Metric/Distance Structure** | Whether there's a natural distance (metric spaces, edit distance, Hamming distance, poset metrics) | Metric structure enables geometric and analytic techniques. Many combinatorial results have "metric versions." |
| **Randomness Model** | The probabilistic model used (Erdős-Rényi random graphs, random regular graphs, random permutations, percolation, random processes) | Different random models exhibit different phase transitions and thresholds. Deterministic results often have probabilistic analogs. |
| **Field Connection** | Links to other areas (theoretical CS, statistical physics, probability theory, topology, number theory, coding theory, information theory) | Cross-disciplinary connections reveal analogies. Techniques from one field often solve open problems in combinatorics. |
| **Scale of Answer** | Whether you seek exact formulas, asymptotics, bounds, inequalities, existence, or impossibility results | Different scales require different techniques. Exact → asymptotic → bounds represents a hierarchy of difficulty and generality. |

## 2. Options per Dimension

### Object Type
- Graphs (simple, directed, weighted, infinite)
- Hypergraphs (uniform, non-uniform, k-uniform)
- Simplicial complexes
- Matroids (graphic, cographic, representable, non-representable)
- Posets (lattices, modular lattices, distributive lattices)
- Permutations (pattern avoidance classes)
- Partitions (integer partitions, set partitions)
- Designs (block designs, Steiner systems, Latin squares)
- Set systems (antichains, intersecting families, union-closed families)
- Words and sequences
- Polytopes (convex, lattice)
- Tableaux (Young tableaux, standard, semistandard)
- Trees (rooted, unrooted, labeled, unlabeled)
- Matching complexes
- Association schemes

### Parameter Regime
- Sparse (o(n))
- Dense (Θ(n²) for graphs)
- Transition regime (threshold phenomena)
- Finite (small, specific values)
- Asymptotic (n → ∞)
- Exact enumeration
- Exponential growth
- Polynomial growth
- Subexponential growth

### Proof Technique
- First moment method
- Second moment method
- Lovász Local Lemma
- Deletion method
- Alteration method
- Linear algebra method
- Polynomial method
- Algebraic method (Combinatorial Nullstellensatz)
- Topological method (Borsuk-Ulam, nerve theorem)
- Compression/shifting
- Container method
- Flag algebra method
- Regularity lemma
- Razborov's flag algebras
- Generating functions (ordinary, exponential)
- Analytic combinatorics
- Discrete Fourier analysis
- Entropy method
- Sunflower lemma
- Hypergraph regularity
- Graph limits (graphons)

### Quantitative vs Structural
- Pure existence
- Explicit construction
- Counting/enumeration
- Asymptotic count
- Upper bound
- Lower bound
- Tight bound
- Extremal configuration characterization
- Structural decomposition
- Classification theorem

### Computational Complexity
- #P (counting)
- NP-complete (decision)
- APX-hard (approximation hardness)
- Fixed-parameter tractable (FPT)
- W[1]-hard
- Polynomial-time solvable
- Quasi-polynomial
- Exponential-time hypothesis (ETH) hardness
- PSPACE-complete
- Streaming complexity
- Communication complexity

### Algebraic Connection
- No algebraic structure
- Group action (symmetric group, wreath products)
- Ring structure
- Module structure
- Representation theory connection
- Symmetric functions (Schur, monomial, elementary)
- Algebraic geometry (Hilbert functions, Gröbner bases)
- Hopf algebra structure
- Lie algebra connection
- Character theory
- Quantum groups

### Dimensionality/Rank
- Rank 2 (graphs)
- Rank 3 (triple systems)
- Rank k (k-uniform hypergraphs)
- Unbounded rank
- Dimension 1, 2, 3, ..., d (geometric objects)
- Infinite dimension

### Constraint Type
- Forbidden subgraph/substructure
- Degree sequence constraint
- Chromatic number constraint
- Independence number constraint
- Connectivity constraint
- Planarity/embeddability
- Intersection pattern (t-intersecting, cross-intersecting)
- Monotonicity
- Symmetry (vertex-transitive, edge-transitive)
- Regularity
- Bipartiteness
- Acyclicity

### Metric/Distance Structure
- No metric
- Graph distance (shortest path)
- Hamming distance
- Edit distance (Levenshtein)
- Kendall tau distance
- Cayley distance
- Interval metric
- Poset metric
- Ultrametric

### Randomness Model
- Uniform random (all structures equally likely)
- Erdős-Rényi G(n,p)
- Random regular graph
- Random d-dimensional simplicial complex
- Preferential attachment
- Configuration model
- Random permutation (uniform, Mallows)
- Random partition (uniform, plancherel)
- Percolation (bond, site)
- Random geometric graph
- Inhomogeneous random graph

### Field Connection
- Pure combinatorics
- Theoretical computer science (algorithms, complexity)
- Statistical physics (Ising model, spin systems)
- Probability theory (random walks, Markov chains)
- Algebraic topology (homology, fundamental groups)
- Number theory (additive combinatorics)
- Coding theory/information theory
- Discrete geometry
- Ramsey theory
- Extremal graph theory
- Enumerative combinatorics
- Analytic number theory

### Scale of Answer
- Exact closed form
- Recurrence relation
- Generating function
- Asymptotic formula (full expansion)
- Leading term asymptotics
- Upper bound
- Lower bound
- Existence/non-existence
- Constructive vs non-constructive
- Probabilistic existence

## 3. Hidden Assumptions in Combinatorial Discovery

| Assumption | Why It's Dangerous |
|------------|-------------------|
| **"Graph theory results should generalize to hypergraphs with the same proof"** | Many graph proofs critically use pairwise structure (e.g., matching theory, degree sequences). Hypergraphs often require completely new techniques (e.g., no König's theorem for hypergraphs). You might dismiss a "natural" hypergraph question as "probably true by the same proof" when it's actually a deep open problem. |
| **"Asymptotic results are easier than exact results"** | Sometimes true, but often backwards. Exact formulas can come from bijections or generating functions, while asymptotics might require sophisticated analysis. Many exact formulas are known while asymptotics remain open. |
| **"Probabilistic method results can't be derandomized"** | Many can! The Lovász Local Lemma was constructivized decades after its discovery. Assuming non-constructiveness prevents you from seeking algorithmic versions, which are often publishable results. |
| **"If it's true for small n by computer search, it's probably always true"** | Combinatorial phenomena often have counterexamples at astronomically large scales. Computer verification up to n=100 or even n=1000 can be misleading (e.g., Ramsey numbers grow so fast that small cases reveal nothing). |
| **"Dense and sparse cases are just quantitative variations"** | They're often qualitatively different. Sparse graphs require different techniques than dense graphs. The Erdős-Ko-Rado theorem works in the "dense" regime; sparse analogs behave completely differently. |
| **"Algebraic methods only work when there's obvious algebra"** | The polynomial method has solved "purely combinatorial" problems with no apparent algebraic structure (finite field Kakeya problem, joints problem). Assuming a problem is "non-algebraic" prevents you from trying algebraic reformulations. |
| **"Extremal configuration uniqueness means the problem is solved"** | Characterizing the extremal case and proving it's optimal are different challenges. Many times the extremal structure is "obvious" but proving optimality is a major open problem. |
| **"Counting is always harder than decision"** | Usually true (#P vs NP), but not always! Some structures are easy to count but hard to decide membership. Don't assume counting-to-decision implications. |
| **"If the result works in infinite combinatorics, the finite case is trivial"** | Compactness arguments work in infinity but not finitely. Infinite Ramsey theory results don't automatically yield finite bounds (and when they do, the bounds are often terrible). |
| **"This problem is too elementary for modern techniques"** | The polynomial method solved the finite field Nikodym problem, which looks elementary. Flag algebras solved decades-old Turán problems. Modern hammers can crack "simple" nuts that resisted classical approaches. |
| **"Computational hardness means no mathematical structure"** | NP-hard problems can still have beautiful structural theorems, approximation algorithms, and special case characterizations. Hardness results tell you where NOT to look for poly-time algorithms, but they don't preclude all mathematics. |
| **"The extremal bound must be tight"** | Many conjectured extremal bounds are off by factors. Assuming tightness prevents you from discovering the true threshold. |

## 4. Specific Discovery Methods for Combinatorics

### Method 1: Hypergraph Lifting
Take any classical graph theory theorem. Replace "graph" with "k-uniform hypergraph" for k ≥ 3. Check if the analogous result is known. If not, either prove it, find a counterexample, or identify why it's open.

### Method 2: Derandomization Check
Take any result proved via the probabilistic method. Ask: "Can this proof be made constructive?" Search for algorithmic Lovász Local Lemma applications, deterministic analogs via method of conditional expectations, explicit constructions replacing existence proofs.

### Method 3: Dual Parameter Flip
For any extremal result about maximizing parameter A subject to constraint on parameter B, ask about maximizing B subject to constraint on A.

### Method 4: Weighted/Fractional Generalization
Take any combinatorial result. Replace counting arguments with weighted sums, integer constraints with fractional ones, or 0-1 variables with [0,1] variables.

### Method 5: Forbidden Substructure Systematization
Pick a combinatorial object type. Enumerate all small forbidden substructures. For each, ask: What is the extremal function? What does the extremal configuration look like? Is there a stability result?

### Method 6: Parameter Addition
Take a result that depends on one parameter. Introduce a second parameter and ask if there's a refined bound.

### Method 7: Dimensionality Escalation
Take a 1-dimensional or 2-dimensional result. Ask what happens in higher dimensions or infinite dimensions.

### Method 8: Local-to-Global Inversion
Find results that go from global properties to local properties. Ask if the reverse implication holds.

### Method 9: Asymptotics → Exact
Identify results known only asymptotically. Try to find exact formulas, recurrence relations, or generating functions.

### Method 10: Computational Complexity Cross-Check
For every natural combinatorial optimization problem, check: Is the decision version NP-complete? Is the counting version #P-hard? Is there an approximation algorithm? Is it FPT in some parameter?

### Method 11: Algebraic Translation
Take a "purely combinatorial" problem. Reformulate it algebraically using generating functions, linear algebra over finite fields, polynomial method, or representation theory.

### Method 12: Probabilistic Threshold Hunt
For any monotone property, identify the sharp threshold in the random model.

### Method 13: Constraint Relaxation Sequence
Take a highly constrained problem. Systematically relax one constraint at a time. Map the difficulty landscape.

### Method 14: Cross-Field Import
Identify a technique from another field (topological methods, Fourier analysis, information theory, statistical physics) that hasn't been applied to your combinatorial problem.

### Method 15: Stability Theory
For any extremal result, ask: "What do near-extremal cases look like?"

## 5. Worked Example: Hypergraph Lifting from Mantel's Theorem

**Starting Point**: Mantel's Theorem (1907) — The maximum number of edges in a triangle-free graph on n vertices is ⌊n²/4⌋, achieved by the balanced complete bipartite graph.

**Step 1**: Identify the structure: Object = graph (2-uniform hypergraph), Forbidden structure = triangle (K₃), Question = extremal function ex(n, K₃), Answer = ⌊n²/4⌋.

**Step 2**: Apply Hypergraph Lifting — replace "graph" with "3-uniform hypergraph." What is the analog of "triangle" for 3-uniform hypergraphs? A "tetrahedron" K₄³ (4 vertices with all 4 triples present).

**Question**: What is ex₃(n, K₄³)?

**Step 3**: Literature search reveals this is the **hypergraph Turán problem** — mostly open for k ≥ 3. Even ex₃(n, K₄³) is unknown! Turán's conjecture (1941) gives a candidate extremal construction but the exact constant is unproven.

**Step 4**: This generates further questions: different forbidden 3-uniform structures, stability versions, computational approaches for small n, connections to coding theory.

**Result**: By taking a 115-year-old theorem and applying a single mechanical transformation (hypergraph lifting), we've identified an active research area with dozens of open problems. This is replicable for ANY graph theory theorem.

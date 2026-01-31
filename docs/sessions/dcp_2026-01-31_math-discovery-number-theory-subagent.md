# DCP Subagent — Number Theory Discovery Techniques

**Date**: 2026-01-31
**Input**: Discovery techniques in number theory (subagent output for larger DCP on mathematical discovery)

---

## 1. Discovery Dimensions for Number Theory

| Dimension | Description |
|-----------|-------------|
| **Object Class** | The fundamental mathematical objects under study (primes, algebraic integers, modular forms, elliptic curves, L-functions, Galois representations, motives, automorphic forms) |
| **Arithmetic Setting** | The base field or ring (Q, number fields, function fields, finite fields, p-adic fields, adèles, global vs. local) |
| **Asymptotic Regime** | What grows/varies and how (density, growth rate, limiting behavior, distribution questions, average vs. individual behavior) |
| **Structural Tool** | Primary algebraic/geometric framework (Galois theory, class field theory, cohomology, arithmetic geometry, representation theory, Shimura varieties) |
| **Analytic Method** | Core analytic technique (L-functions, sieve theory, circle method, harmonic analysis, ergodic theory, spectral theory, p-adic analysis) |
| **Computational Dimension** | Role of explicit bounds and algorithms (effective vs. ineffective, computational complexity, heuristics vs. proofs, numerical evidence) |
| **Dimensionality** | Complexity of the object (rank, dimension, degree, number of variables, transcendence degree) |
| **Symmetry & Invariants** | What structure is preserved (Galois action, class groups, unit groups, Selmer groups, invariant theory) |
| **Reduction Behavior** | How objects behave mod p (good/bad reduction, conductor, ramification, residue characteristics) |
| **Diophantine Question Type** | Nature of equation solving (existence, finiteness, density, algorithm, distribution, local-global principle) |
| **Height & Norm Structure** | Size measurement and growth (absolute height, canonical height, regulator, discriminant bounds) |
| **Connectivity Pathway** | Bridges to other areas (algebraic geometry, representation theory, dynamics, probability, physics, combinatorics, logic) |

## 2. Options per Dimension

### Object Class
- Prime numbers (individual, patterns, gaps, twins, Sophie Germain, Mersenne)
- Algebraic integers in number fields
- Units and class groups
- Modular forms (classical, Hilbert, Siegel, Bianchi)
- Elliptic curves and abelian varieties
- L-functions (Riemann zeta, Dirichlet, automorphic)
- Galois representations (continuous, p-adic, ℓ-adic, mod p)
- Automorphic forms and representations
- Motives and motivic cohomology
- Lattices and quadratic forms
- Continued fractions and Diophantine approximation
- Algebraic cycles
- Special values (of L-functions, modular forms, periods)

### Arithmetic Setting
- Rational numbers Q
- Quadratic fields (real, imaginary)
- Cyclotomic fields
- Totally real fields
- CM fields
- General number fields
- Function fields over finite fields
- p-adic fields Q_p
- Finite fields F_q
- Adèles and idèles
- Mixed characteristic settings

### Asymptotic Regime
- Counting functions (π(x), class number growth)
- Density theorems (natural, Dirichlet, analytic density)
- Equidistribution results
- Average order of arithmetic functions
- Moments of L-functions
- Large height/degree behavior
- Probabilistic models (Cohen-Lenstra, random matrix theory)
- Extreme value distributions
- Rate of convergence questions

### Analytic Method
- L-function theory (functional equations, special values, zeros)
- Sieve methods (Selberg, large sieve, combinatorial)
- Circle method (Hardy-Littlewood, Kloosterman refinements)
- Harmonic analysis on groups
- Exponential sums (Weil, Deligne, Kloosterman)
- Spectral theory (automorphic spectrum, trace formula)
- p-adic analysis (p-adic L-functions, p-adic integration)
- Ergodic theory and dynamics
- Fourier analysis

### Computational Dimension
- Effective bounds (explicit constants)
- Algorithms (polynomial-time, quasi-polynomial, exponential)
- Primality testing (deterministic, probabilistic)
- Factorization algorithms
- Computability and decidability
- Heuristics and conjectures from data
- Tables and databases (LMFDB)
- Computational complexity classes

### Diophantine Question Type
- Existence of solutions (Hasse principle, local-global)
- Finiteness (Faltings, Siegel, effective Mordell)
- Density of solutions (Manin conjecture)
- Algorithms for finding solutions
- Distribution by height or congruence class
- Rational vs. integral solutions
- Obstructions (local, Brauer-Manin, étale-Brauer)

## 3. Hidden Assumptions in Number-Theoretic Discovery

| Hidden Assumption | Why It's Dangerous |
|-------------------|-------------------|
| **"The generalization to number fields is straightforward"** | Number fields introduce class groups, units with positive rank, ramification. Unique factorization can fail. Many "obvious" generalizations are false or drastically harder. |
| **"Analytic methods only work for asymptotic questions"** | Some of the deepest results (Wiles, Faltings) use geometry and algebra. Conversely, analytic methods sometimes give exact information (explicit formulas). |
| **"Computational evidence strongly suggests the pattern holds"** | Patterns can break at astronomically large numbers (Skewes' number, Mertens conjecture). Heuristics can be systematically wrong (biases in prime races). |
| **"Local-global principles should generally work"** | Brauer-Manin and other obstructions can prevent local solubility from implying global. For cubic surfaces and beyond, counterexamples exist. |
| **"Effective bounds aren't interesting mathematics"** | Effective versions often require entirely new techniques. Essential for algorithms, cryptography, and verification. |
| **"The technique that proved X should prove analogous Y"** | Different objects have different fundamental obstructions. Sieve methods hit the parity barrier for twin primes. Modularity lifting only works in certain contexts. |
| **"Special cases and small examples reveal the general pattern"** | Behavior changes with dimension (genus 0→1→2+), degree, rank. Small primes are atypical. |
| **"If two objects share invariants, they're essentially similar"** | Isospectral but non-isomorphic objects exist. Same L-function ≠ same object. |
| **"The algebraic and analytic sides are separate"** | Langlands program, modularity theorems, and BSD conjecture intimately connect them. Wiles uses both. |
| **"Generalizing to higher dimension is the natural next step"** | Sometimes the right generalization is to function fields, or to add extra structure, or to consider families. |

## 4. Specific Discovery Methods for Number Theory

### Method 1: Field Variation
Take any theorem proved over Q. Systematically ask: does it hold over real quadratic fields? Imaginary quadratic? Cyclotomic? Totally real? Arbitrary number fields? Function fields F_q(t)?

### Method 2: L-function Special Values
For any L-function L(s), compute or study its special values at integers. If values lack known algebraic or geometric interpretation, investigate Beilinson/Bloch-Kato conjectures.

### Method 3: Reduction Type Census
Fix an object (e.g., elliptic curve E/Q). For each prime p, classify its reduction type. Study the density of primes with each type.

### Method 4: Dimension Hopping
Take a result about curves (dimension 1) and ask about surfaces (dimension 2). Conversely, take higher-dimensional results and check the 1-dimensional analog.

### Method 5: Effectivity Gap Analysis
List major finiteness theorems. Check which have effective algorithms. Where there's no effective version, that's an open problem.

### Method 6: Heuristic Formalization
Take a widely believed heuristic (Cohen-Lenstra, random matrix theory, Cramér model). Identify the precise model. Prove theorems under it. Find where it provably fails.

### Method 7: Galois Representation Classification
Fix dimension d and residual characteristic p. Classify all possible Galois representations. For each, ask: does it arise from geometry?

### Method 8: Height Bound Reversal
Instead of "how many solutions of bounded height?", ask "for this specific solution, can we bound its height?"

### Method 9: Obstruction Promotion
When local-global fails, identify the obstruction (Brauer-Manin, descent). Study the obstruction itself as an object.

### Method 10: Analogical Translation (Function Fields)
Translate a difficult problem over number fields to function fields. Geometric methods often make it tractable. Then ask what ports back.

### Method 11: Family Formation
Instead of individual objects, study families. Prove average behavior, moments, or distribution.

### Method 12: Algorithmic Obstruction Discovery
Try to write an algorithm for a decision problem. Where you get stuck is often a deep mathematical obstruction.

### Method 13: Additive/Multiplicative Duality
Every problem has additive and multiplicative versions. Translate between them.

### Method 14: Conjectural Bridging
Take two major conjectures. Ask: if both are true, what new theorem follows? Sometimes the conditional proof reveals what's really going on.

### Method 15: Symmetry Breaking
Start with a highly symmetric object (cyclotomic field, CM curve). Break the symmetry slightly. Which theorems still hold? The breakdown point reveals what the symmetry was doing.

## 5. Worked Example: L-function Special Values

**Starting Point**: Dirichlet L-functions L(s, χ) for character χ mod m.

**Step 1**: L(1, χ) is classical — connects to class numbers, primes in arithmetic progressions.

**Step 2**: Ask: what about L(2, χ)? L(k, χ) for k ≥ 2?

**Step 3**: For k ≥ 2 with appropriate parity, L(k, χ) is a non-zero algebraic multiple of π^k. But what's the geometric interpretation?

**Step 4**: This leads to Beilinson's Conjectures — special values relate to regulator maps from algebraic K-theory, connecting to heights and periods.

**Open directions discovered**:
1. Computing regulators explicitly for specific characters and k
2. p-adic interpolation → Iwasawa theory
3. Higher weight modular forms and their L-values
4. Motivic interpretation: construct motive M_χ whose L-function is L(s, χ)

**Concrete new question**: For imaginary quadratic K with class number h, give an explicit formula for the regulator in L(2, χ) in terms of elliptic units in ray class fields.

# DCP Subagent — Algebraic Geometry Discovery Techniques

**Date**: 2026-01-31
**Input**: Discovery techniques in algebraic geometry (subagent output for larger DCP on mathematical discovery)

---

## 1. Discovery Dimensions for Algebraic Geometry

| Dimension | Description |
|-----------|-------------|
| **Object Type** | The fundamental geometric object (varieties, schemes, stacks, derived schemes, perfectoid spaces, adic spaces, formal schemes, rigid analytic spaces) |
| **Base** | The ground field or ring (algebraically closed char 0, char p, finite fields, p-adic, number fields, function fields, Z, DVRs) |
| **Dimension** | Dimension of the variety/scheme (curves, surfaces, threefolds, higher, infinite dimensional) |
| **Singularity Type** | Regularity condition (smooth, normal, Cohen-Macaulay, Gorenstein, rational, log canonical, klt, terminal, Du Bois) |
| **Birational Class** | Position in the MMP (Kodaira dimension -∞ through general type; Fano, Calabi-Yau, canonically polarized) |
| **Cohomology Theory** | The cohomological framework (de Rham, Betti, étale, crystalline, motivic, syntomic, prismatic, Dolbeault, Hodge) |
| **Moduli Problem** | Type of classification question (moduli of curves, surfaces, sheaves, bundles, maps, stable pairs, Bridgeland-stable objects) |
| **Enumerative Invariant** | Counting framework (Gromov-Witten, Donaldson-Thomas, Pandharipande-Thomas, Gopakumar-Vafa, BPS, refined) |
| **Symmetry/Structure** | Additional structure (group actions, toric data, abelian varieties, K3, hyperkähler, Calabi-Yau) |
| **Combinatorial Shadow** | Discrete/tropical analog (Newton polytopes, tropical varieties, toric fans, Berkovich spaces) |
| **Physical Connection** | Physics motivation (mirror symmetry, string compactifications, gauge theory, TQFT, D-branes, homological mirror symmetry) |
| **Homological Algebra** | Derived category structure (D^b(Coh), Fukaya categories, stability conditions, semiorthogonal decompositions, Fourier-Mukai) |

## 2. Options per Dimension

### Object Type
- Classical varieties (affine, projective, quasi-projective)
- Schemes (locally of finite type, Noetherian, excellent)
- Algebraic spaces
- Deligne-Mumford stacks
- Artin stacks
- Higher stacks (2-stacks, ∞-stacks)
- Derived schemes (Toën-Vezzosi or Lurie)
- Perfectoid spaces
- Adic spaces (Huber)
- Formal schemes
- Rigid analytic varieties
- Berkovich spaces
- Ind-schemes and pro-schemes

### Base
- Algebraically closed field char 0 (C, Q̄)
- Algebraically closed field char p > 0 (F̄_p)
- Finite fields F_q
- p-adic fields (Q_p, extensions)
- Number fields (Q, quadratic, cyclotomic)
- Function fields (F_p(t), C(t))
- Z (integral models)
- Discrete valuation rings (mixed characteristic, equal characteristic)
- Laurent series fields
- Perfectoid fields
- Non-algebraically closed fields (R, Q)

### Dimension
- 0 (points, zero-dimensional schemes)
- 1 (curves)
- 2 (surfaces)
- 3 (threefolds)
- 4-10 (intermediate)
- n (general)
- Infinite dimensional (loop spaces, arc spaces, Hilbert schemes)
- Negative dimension (virtual fundamental classes)

### Singularity Type
- Smooth (regular)
- Normal
- Reduced but non-normal
- Cohen-Macaulay
- Gorenstein
- Canonical singularities
- Terminal singularities
- Klt singularities
- Log canonical singularities
- Rational singularities
- Du Bois singularities
- Simple singularities (ADE)
- Quotient singularities
- Toric singularities
- Non-reduced (with nilpotents)

### Birational Class
- Kodaira dimension -∞ (ruled, uniruled)
- Kodaira dimension 0 (abelian, K3, Enriques, Calabi-Yau)
- Kodaira dimension 1
- Kodaira dimension = dimension (general type)
- Fano varieties (anti-canonical ample)
- Weak Fano (anti-canonical nef)
- Calabi-Yau (trivial canonical bundle)
- Rationally connected

### Cohomology Theory
- Singular/Betti cohomology
- de Rham cohomology
- Étale cohomology (Z/nZ, Z_ℓ, Q_ℓ coefficients)
- Crystalline cohomology
- Syntomic cohomology
- Prismatic cohomology (Bhatt-Scholze)
- Motivic cohomology
- Deligne cohomology
- Hodge cohomology (Dolbeault)
- K-theory (algebraic, topological)
- Chow groups
- Rigid cohomology

### Moduli Problem
- M_g, M_{g,n} (curves)
- Moduli of surfaces (general type, K3, Enriques)
- Moduli of vector bundles
- Moduli of coherent sheaves
- Moduli of stable maps (GW theory)
- Moduli of stable pairs (PT theory)
- Moduli of Bridgeland-stable objects
- Hilbert schemes
- Quot schemes
- Severi varieties

### Enumerative Invariant
- Classical counts (27 lines on cubic surface)
- Schubert calculus
- Gromov-Witten invariants
- Donaldson-Thomas invariants
- Pandharipande-Thomas invariants
- Gopakumar-Vafa invariants
- BPS state counts
- Refined invariants (motivic, K-theoretic)
- Quantum cohomology/K-theory
- Verlinde numbers

### Combinatorial Shadow
- Toric fans
- Newton polytopes
- Tropical varieties
- Moment polytopes
- Okounkov bodies
- Gröbner degenerations
- Berkovich analytifications
- Dual complexes
- Schubert cells and Bruhat order
- Matroids

## 3. Hidden Assumptions in Algebraic Geometric Discovery

| Assumption | Why It's Dangerous |
|------------|-------------------|
| **"If it's true over C, it's the fundamental case"** | Many phenomena are characteristic p-specific (Frobenius, p-torsion). Mixed characteristic gives arithmetic information. Some results reverse the dependency via Lefschetz principle. |
| **"Smooth objects are the right generality"** | Singularities carry crucial information. MMP fundamentally requires allowing singularities. Many moduli spaces are smooth only in restrictive cases. |
| **"Projective is sufficient"** | Important varieties are quasi-projective but not projective. Affine varieties have richer algebra. Some problems are fundamentally affine. |
| **"The cohomology that matters is the one we know how to compute"** | Different theories see different phenomena. New theories like prismatic cohomology unify old ones. Comparison theorem failures indicate new information. |
| **"Classical varieties are enough"** | Stacks are necessary for moduli. Non-separated schemes appear naturally. Derived schemes capture deformation theory. |
| **"Interesting phenomena happen in low dimension"** | Many conjectures are known for curves/surfaces but open in dim ≥3 (Hodge conjecture, rationality). Higher dimensions have genuinely new phenomena. |
| **"If a result holds for general type, it's understood"** | Fano and Calabi-Yau have special structure leading to different phenomena. Intermediate Kodaira dimension is poorly understood. |
| **"Algebraic geometry is about varieties over fields"** | Schemes over Z capture arithmetic. Non-reduced structure captures tangent information. Arithmetic geometry needs schemes over rings. |
| **"Rationality and unirationality are essentially the same"** | For surfaces they coincide (Castelnuovo). For threefolds they differ (Clemens-Griffiths). Unirational but not rational exists in dim ≥3. |
| **"Enumerative geometry is about counting curves in threefolds"** | Higher dimensional targets, Joyce's sheaf counting, K-theoretic and motivic refinements, local theories all extend beyond this. |

## 4. Specific Discovery Methods for Algebraic Geometry

### Method 1: Base Change Interrogation
Take any theorem over C. Systematically ask: over R? Q̄? Number fields? Finite fields? Char p? Over Z?

### Method 2: Singularity Degradation
For any result for smooth varieties, systematically weaken: smooth → normal → canonical → klt → log canonical → Cohen-Macaulay → non-reduced. Where does it break?

### Method 3: Dimensional Extrapolation
For any theorem known in dimension n, attempt dimension n+1. Identify which proof step fails.

### Method 4: Cohomology Translation
For any result computed using theory T, ask: does it hold for theory T'? Does the method transfer? What new information does T' reveal?

### Method 5: Moduli Space Duality
For any moduli problem M, find the dual/mirror moduli space. Study Fourier-Mukai transforms, derived equivalences, enumerative invariant matching.

### Method 6: Tropicalization Check
Compute trop(X). What geometric properties are visible combinatorially? Can you compute invariants via tropical geometry?

### Method 7: Derived Category Interrogation
For any variety X: semiorthogonal decompositions? Derived equivalences? Exceptional collections? Stability conditions? Autoequivalences?

### Method 8: Minimal Model Program Descent
Run the MMP on X. What is contracted at each step? Do flips occur? Relate invariants of X to invariants of the output.

### Method 9: Point Counting Patterns
For X over F_p, compute |X(F_q)| for small q. Compare to Weil conjecture predictions. Discrepancies reveal unexpected cohomological structure.

### Method 10: Stability Condition Variation
Vary stability conditions (GIT, slope, Bridgeland). Map the chamber structure. At each wall-crossing: how does the moduli space change?

### Method 11: Degeneration Specialization
Construct a family where the special fiber has simpler structure. Study how cohomology specializes, how invariants match combinatorial counts on the degeneration.

### Method 12: Functoriality Testing
For any construction/invariant I: is it functorial? Under what maps? Does it satisfy projection formula, base change, localization?

### Method 13: Arithmetic Specialization Reversal
Translate arithmetic problems to function fields where geometric methods apply. Solve there, ask what ports back.

### Method 14: Mirror Symmetry Probing
For Calabi-Yau X: does it have a mirror? Do A-model invariants match B-model of mirror? Compute one side to predict the other.

### Method 15: Boundedness Interrogation
For a class of varieties: is it bounded? What causes (un)boundedness? Can you refine to a bounded subclass? Classify all members.

## 5. Worked Example: Singularity Degradation from Kodaira Vanishing

**Starting Point**: Kodaira Vanishing — For smooth projective X over C with ample L: H^i(X, K_X ⊗ L) = 0 for i > 0.

**Step 1 (Normal)**: Does it hold for normal projective varieties? NO — Raynaud found counterexample in char 2.

**Step 2 (Canonical singularities, char 0)**: YES (Elkik 1978). Canonical singularities are defined so that Kodaira vanishing holds.

**Step 3 (Klt)**: YES — Kawamata-Viehweg vanishing (1982) extends to klt pairs. Fundamental to MMP.

**Step 4 (Log canonical)**: Full vanishing FAILS. But Kollár proved injectivity theorems for lc pairs — a weaker but important statement.

**Step 5 (Non-reduced)**: Connects to deformation theory, cotangent complex, derived algebraic geometry.

**Discovery**: By degrading from smooth → lc → non-reduced, we trace the boundary where Kodaira vanishing breaks, revealing that this boundary exactly aligns with the singularity classes used in the minimal model program. The non-reduced case points toward derived algebraic geometry as the next frontier.

**Concrete open question discovered**: Does Kodaira-type vanishing hold for the intrinsic normal cone of moduli spaces of sheaves on Calabi-Yau threefolds? This would connect classical vanishing to virtual fundamental classes in DT theory.

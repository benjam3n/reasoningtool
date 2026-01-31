# DCP Subagent — Category Theory Discovery Techniques

**Date**: 2026-01-31
**Input**: Discovery techniques in category theory (subagent output for larger DCP on mathematical discovery)

---

## 1. Discovery Dimensions for Category Theory

| Dimension | Description | Why It Matters |
|-----------|-------------|----------------|
| **Categorification Level** | Sets → Categories → 2-Categories → n-Categories → ∞-Categories | Each level up reveals new coherence phenomena and higher structures |
| **Enrichment Base** | What monoidal category you enrich over (Set, Ab, Cat, Vect_k, Top, sSet, etc.) | Different enrichments reveal different internal structure |
| **Monoidal Structure Type** | Cartesian, symmetric monoidal, braided, ribbon, compact closed, *-autonomous, etc. | Determines what operations/duality are intrinsic |
| **Limit/Colimit Completeness** | Which (co)limits exist: finite, filtered, small, all | Constrains what constructions are possible |
| **Universal Property Class** | Adjunctions, Kan extensions, representables, (co)ends, weighted (co)limits | Different universals solve different existence problems |
| **Internal Logic Type** | Regular, coherent, geometric, Boolean, intuitionistic, linear, dependent type theory | Determines what reasoning is valid "internally" |
| **Topos Level** | Elementary topos, Grothendieck topos, ∞-topos, relative topos | How much "set theory" lives inside |
| **Derivation/Homotopy** | Underived vs derived categories, stable vs unstable, model structure type | Whether you track homotopical information |
| **Algebraic Theory Encoding** | Monads, operads, PROPs, clubs, Lawvere theories, essentially algebraic theories | Different ways to encode "algebraic structure" |
| **Variance Pattern** | Covariant, contravariant, bifunctors, profunctors, extranatural, dinatural | Direction of mapping determines what's preserved |
| **Dimension of Diagram** | 0 (objects), 1 (arrows), 2 (commutative squares), ∞ (simplicial/cubical) | Complexity of coherence conditions |
| **Size Issues** | Small, locally small, large, accessible, presentable | Determines what set-theoretic techniques apply |

## 2. Options per Dimension

### Categorification Level
- **Set-level**: Classical mathematics
- **1-categorical**: Standard category theory
- **2-categorical**: Bicategories, strict 2-categories, double categories
- **n-categorical**: Strict n-categories, weak n-categories (various models)
- **∞-categorical**: Quasi-categories, complete Segal spaces, Segal categories, simplicially enriched categories
- **Directed**: No duality/reversal (e.g., directed type theory)

### Enrichment Base
- **Discrete**: Set (ordinary categories)
- **Additive**: Ab (abelian groups), R-Mod (modules)
- **Topological**: Top, CGHaus, sSet
- **Order-theoretic**: Poset, (0,1)-categories
- **Categorical**: Cat (2-categories), Span, Prof
- **Algebraic**: Vect_k, Alg_k
- **Monoidal closed V**: Any complete/cocomplete symmetric monoidal closed category
- **Multicategories**: Non-symmetric enrichment

### Monoidal Structure Type
- Cartesian (most restrictive)
- Symmetric monoidal
- Braided (quantum groups)
- Ribbon/Tortile (braided + duality + twist)
- Compact closed (every object has dual)
- *-Autonomous (linear logic monoidal)
- Closed (internal hom exists)
- Semicartesian (terminal object is monoidal unit)
- Non-symmetric (associative only)

### Limit/Colimit Completeness
- Finitely (co)complete
- Filtered (co)complete
- Locally finitely presentable
- Cocomplete
- Complete and cocomplete
- Lacks equalizers (partial completeness)
- Only has specific (co)limits (e.g., only pullbacks)

### Universal Property Class
- Adjunctions: F ⊣ G between categories
- Representables: Hom(A, -) ≅ F
- Kan extensions: Most general lifting problem
- Limits/colimits: Special Kan extensions
- (Co)ends: Extraordinary (weighted) (co)limits
- Weighted (co)limits: Indexed by diagrams in V
- Pointwise Kan extensions: Computed objectwise
- Absolute (co)limits: Preserved by all functors

### Internal Logic Type
- Classical/Boolean
- Intuitionistic (Heyting algebra subobjects)
- Linear (resource-sensitive)
- Dependent type theory
- Higher-order
- Regular logic
- Coherent logic
- Geometric logic
- Modal/temporal

### Topos Level
- Elementary topos
- Grothendieck topos (sheaves on a site)
- ∞-topos
- Boolean topos
- Localic topos
- Cohesive topos
- Arithmetic topos
- Realizability topos

### Derivation/Homotopy
- Underived (classical homological algebra)
- Derived categories (invert quasi-isomorphisms)
- Triangulated (homotopy category with structure)
- Stable ∞-categories
- Model categories
- Unstable (∞-groupoids, spaces)
- Pointed/stable (suspension/loops are equivalences)
- t-structures (approximations by abelian categories)

### Algebraic Theory Encoding
- Monads
- Operads
- Colored operads
- Cyclic operads
- PROPs
- Clubs
- Lawvere theories
- Essentially algebraic theories
- Kan extensions as theories

### Variance Pattern
- Covariant: F: C → D
- Contravariant: F: C^op → D
- Bifunctor: F: C × D → E
- Profunctor: H: C^op × D → Set
- Extranatural
- Dinatural (cowedge condition)
- Lax natural (2-cells instead of equations)
- Pseudonatural (invertible 2-cells)

### Dimension of Diagram
- 0-dimensional (objects)
- 1-dimensional (arrows, commutative triangles)
- 2-dimensional (commutative squares, pasting diagrams)
- Simplicial: Δ^op → C
- Cubical: □^op → C
- Globular: n-globes in n-categories
- ∞-dimensional (all coherence at once)

### Size Issues
- Small
- Locally small
- Large
- Essentially small
- Accessible
- Presentable
- Totality

## 3. Hidden Assumptions in Categorical Discovery

| Hidden Assumption | Why It's Dangerous |
|-------------------|-------------------|
| **"If it works for categories, it works for 2-categories by just adding 2-cells"** | Coherence becomes non-trivial; strict vs weak versions diverge massively. Bicategories require coherence isomorphisms; many 1-categorical constructions have no strict 2-categorical analog. |
| **"Natural transformations are always given by components"** | Only true for Set-enriched categories; enriched naturality is more subtle. |
| **"Adjunctions determine monads uniquely"** | Many adjunctions can generate the same monad; only the Eilenberg-Moore adjunction is universal. |
| **"All limits can be built from products and equalizers"** | Only in categories with enough structure; weighted limits may not decompose. |
| **"Functoriality is binary: either it preserves something or it doesn't"** | Lax/oplax/strong preservation are different; exact functors have spectrum of exactness. |
| **"The opposite category construction is trivial"** | Duality can fail at higher categories; opposites may require multiple notions (1-op, 2-op, etc.). |
| **"Universal properties determine objects up to unique isomorphism"** | Only in 1-categories; in ∞-categories you get contractible spaces of isomorphisms. |
| **"You can always strictify weak structures"** | Coherence theorems are rare and precious; most weak structures cannot be strictified. Tricategories have no general coherence theorem. |
| **"Categorical constructions respect size"** | Size issues proliferate; [C^op, Set] is almost never small even if C is. |
| **"Every monad comes from a 'natural' adjunction"** | Every monad comes from its Eilenberg-Moore adjunction, but many interesting monads don't arise from "natural" adjunctions in the domain. |
| **"Limits and colimits always commute with themselves"** | They don't — finite limits commute with filtered colimits, but arbitrary limits and colimits rarely commute. |

## 4. Specific Discovery Methods for Category Theory

### Method 1: Systematic Categorification
Take any set-level construction and ask: "What is the (n+1)-categorical analog?" Replace equations with isomorphisms, isomorphisms with equivalences, and add coherence conditions.

### Method 2: Enrichment Variation
Take any categorical concept defined for Set-enriched categories and enrich it over V. Replace "Set" with V everywhere. Redefine limits as weighted limits. Check which theorems still hold.

### Method 3: Variance Inversion
For any contravariant construction, ask: "Is there a canonical covariant version, or vice versa?" Given F: C^op → D, find G: C → D that captures similar information.

### Method 4: Adjunction Mining
For any construction, ask: "Does it have a left/right adjoint?" Given functor F: C → D, systematically attempt to construct G such that F ⊣ G or G ⊣ F.

### Method 5: Monad Decomposition
For any monad T on C, describe the Eilenberg-Moore category C^T explicitly. Given monad T = GF from adjunction F ⊣ G, compute what T-algebras are.

### Method 6: Universal Property Reversal
For any universal property, formulate the "co-" version. Replace limits with colimits, initial with terminal, products with coproducts. Check if the dual is known/studied.

### Method 7: Dimension Lifting in Diagrams
Take any theorem about commutative diagrams and ask what it becomes in higher dimensions. Replace commutative squares with coherent 2-cells.

### Method 8: Weighted Limit Generalization
For any specific limit, ask: "What is the weighted version?" Replace constant functor with arbitrary weight W: J → V.

### Method 9: Internal-ization
Take any external construction and ask: "Can this be done internally to category C?" Replace Set with C. Define objects, morphisms, composition internally.

### Method 10: Free-Forgetful Iteration
For any algebraic structure, construct the free functor. Then ask: "What is the free [X] on a free [X]?" Compose Free with itself and describe the result.

### Method 11: Limit/Colimit Decomposition
For any category C, characterize exactly which limits distribute over which colimits. Build a chart of which (L,C) pairs commute in which categories.

### Method 12: Topos-Internal Mathematics
Take any mathematical structure and interpret it in an arbitrary topos E, not just Set. Replace Set with E throughout. What are "groups in E"? "Topological spaces in E"?

### Method 13: Homotopy-Invariance Testing
For any categorical property, ask: "Is this homotopy-invariant?" Check if property is preserved under equivalence of categories. If not, reformulate.

### Method 14: Profunctor Reformulation
Take any construction involving functors and ask: "What does this look like as a profunctor?" Functors F: C → D correspond to profunctors C ⇸ D.

### Method 15: Operadic Encoding
For any algebraic structure, find the operad that governs it. Study O-algebras in various categories.

## 5. Worked Example: Monad Decomposition → Convex Categories

**Starting Point**: The finite distribution monad D on Set.

- D(X) = {finite formal convex combinations ∑λᵢxᵢ : xᵢ ∈ X, λᵢ ∈ [0,1], ∑λᵢ = 1}

**Step 1**: What are D-algebras? A D-algebra is a set A with α: D(A) → A satisfying unit and associativity laws. This is precisely a "convex space" — known since Swirszcz 1974, Manes 1976.

**Step 2 (Discovery move — categorify)**: Replace Set with Cat. Define a monad D on Cat similarly. Ask: What are D-algebras in Cat? What are "convex categories"?

**Step 3**: A convex category would be a category C with: for each finite family of objects {Aᵢ} and probabilities {λᵢ}, an object ∑λᵢAᵢ, with functoriality extending to morphisms, plus associativity and unit coherence isomorphisms.

**Step 4**: Literature search for "convex category" or "categorical convex structure" yields limited results.

**Open Question Identified**: "What is the correct notion of a convex category (D-algebra in Cat)? Is there a 2-monad on Cat whose algebras are convex categories? What applications does this have to categorical probability theory or categorical quantum mechanics?"

**Further**: What about D-algebras in ∞-Cat? This would be "convex ∞-categories", potentially relevant to probabilistic homotopy theory.

**Key Insight**: Mathematical discovery in category theory is less about "having ideas" and more about systematically applying transformations (categorification, enrichment, internalization, dualization) to known structures and checking whether the resulting objects have been characterized. Most coordinates in the discovery space remain unexplored.

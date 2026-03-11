# /cmp Compare the ARAW approach vs. chain-of-thought prompting vs. tree-of-thought for claim testing
**Date:** 2026-03-09
**Skill:** /cmp (Comparison)

---

## Interpretation Selected

**Interpretation 3 — Conceptual contrast**: The goal is to understand how three reasoning frameworks differ in nature for the specific task of claim testing — not to pick one for a project, but to sharpen understanding of what each does and where each excels or fails.

---

## 1. State the Impression

```
OPTIONS:
  A. ARAW (Assume Right / Assume Wrong)
  B. Chain-of-Thought (CoT) prompting
  C. Tree-of-Thought (ToT) prompting

IMPRESSION: ARAW is clearly the strongest framework for claim testing
specifically, because it was purpose-built for that task. CoT and ToT
are general reasoning amplifiers that can be applied to claim testing
but weren't designed for it. CoT is weakest — it's a single linear
path that lacks the adversarial structure claim testing demands. ToT
is closer to ARAW in structure (branching exploration) but lacks
ARAW's forced adversarial symmetry and its registry/bedrock
machinery.

CONFIDENCE: MEDIUM — I suspect the structured analysis may reveal
that CoT and ToT have strengths ARAW lacks (simplicity, flexibility,
broader applicability) that matter more than I'm weighting initially.
```

---

## 2. Define Purpose and Criteria

**Purpose**: Evaluate which framework best serves *claim testing* — the task of taking a belief, assertion, or assumption and rigorously determining whether it holds, breaks, or needs qualification.

### REQUIRED — Must have. Failure = eliminated.

```
- Adversarial structure: Must systematically examine reasons the claim could be WRONG,
  not just reasons it could be right. "Pass" = the method structurally forces
  consideration of wrongness, not just as an afterthought.

- Handles compound claims: Must be able to decompose a claim that bundles multiple
  sub-claims and test each. "Pass" = the method has a mechanism for unbundling.

- Reaches resolution: Must produce a verdict or actionable conclusion, not just
  "thoughts about the claim." "Pass" = the method terminates with a clear status
  (validated, rejected, uncertain, conditional).
```

### IMPORTANT — Strongly preferred. Failure = significant penalty.

```
- Depth control: Can the user/system specify and enforce how deeply the claim is
  explored? "Good" = explicit depth parameters with floors.

- Tracks what was found: Does the method maintain a registry of discoveries so
  nothing gets lost in prose? "Good" = numbered, referenceable findings.

- Forces equal rigor on both sides: Does the method prevent the common failure
  of soft devil's-advocacy? "Good" = structural mechanism that equalizes AR/AW depth.

- Derives alternatives from analysis: When a claim is wrong, does the method
  produce what's right instead? "Good" = alternatives emerge from the wrongness
  analysis, not from thin air.

- Corruption resistance: Does the method resist validation bias, user flattery,
  and premature convergence? "Good" = explicit anti-corruption mechanisms.
```

### NICE-TO-HAVE — Bonus value. Absence acceptable.

```
- Simplicity / low overhead: Can be used quickly without heavy scaffolding.
- General applicability: Works for tasks beyond claim testing.
- Empirical validation: Has published research supporting its effectiveness.
- Composability: Can be combined with other methods or embedded in larger workflows.
```

---

## 3. Eliminate on Required Criteria

| Option | Adversarial Structure | Handles Compound Claims | Reaches Resolution | Status |
|--------|----------------------|------------------------|--------------------|--------|
| A. ARAW | PASS — AR/AW is the core loop; adversarial exploration is mandatory, with AW severity labels (Fatal/Serious/Conditional) | PASS — Step 1 explicitly unbundles claims into C-numbered components with VOI rating | PASS — Verdict system (VALIDATED/REJECTED/DAMAGED/CONDITIONAL/UNCERTAIN) derived from evidence tree | **Survives** |
| B. CoT | CONDITIONAL — CoT does not structurally force adversarial examination. A user can prompt "think about why this might be wrong," but the method itself is a linear chain of reasoning steps. Left to itself, CoT follows the most natural reasoning path, which is typically confirmatory. | CONDITIONAL — CoT can decompose claims if prompted to, but has no built-in unbundling mechanism. It depends entirely on the prompt to specify this. | CONDITIONAL — CoT can reach a conclusion, but there's no structural requirement that it produce a verdict. It often trails off into "it depends" without commitment. | **Conditional survival** — CoT can pass all three if heavily prompted, but fails them by default. For a fair comparison, we keep it in but note it needs scaffolding. |
| C. ToT | PASS (partial) — ToT's branching structure naturally generates multiple paths, some of which can be adversarial. The evaluation/voting step can reject branches. However, adversarial exploration is not *mandatory* — it emerges from breadth, not from structural requirement. | PASS — Multiple branches can explore sub-claims independently. The tree structure naturally decomposes. | PASS (partial) — ToT selects the best path via evaluation, which functions as a verdict. But the verdict is "best path" not "claim status." | **Survives** |

**Note on CoT**: CoT does not pass the required criteria *as a method*. It passes them only when the prompt does the work that the method should do. I'm keeping it in the comparison because eliminating it entirely would miss the useful contrast, but this is a significant finding: CoT is a reasoning *amplifier*, not a reasoning *structure*. It amplifies whatever direction the prompt points it in.

---

## 4. Compare Survivors on Important Criteria

### Depth Control
- **A. ARAW**: Explicit depth table (1x through 32x) with floors for claims, findings, tree levels, and CRUX points. The user picks a depth and the method enforces minimums. -> **CLEARLY BETTER**
- **B. CoT**: No depth control mechanism. Length is determined by the prompt ("think step by step" vs. "think very carefully step by step") which is imprecise. -> **CLEARLY WORSE**
- **C. ToT**: Has breadth control (number of branches) and depth control (number of levels) as parameters. But these control the *search* depth, not the *analytical* depth — you can have a deep tree of shallow thoughts. -> **SLIGHTLY WORSE** than ARAW

### Tracks What Was Found
- **A. ARAW**: Mandatory numbered registry (C-numbers for claims, F-numbers for findings). Phase 2 compiles everything. Nothing allowed to be lost. -> **CLEARLY BETTER**
- **B. CoT**: No tracking mechanism. Findings exist only in the prose of the chain. Easy to lose, hard to reference back. -> **CLEARLY WORSE**
- **C. ToT**: Branches are tracked as nodes in the tree, but there's no registry or numbering convention. Findings live in the tree structure, which is better than prose but worse than a compiled registry. -> **SLIGHTLY WORSE** than ARAW

### Forces Equal Rigor on Both Sides
- **A. ARAW**: Core Principle 3 ("Both sides, equal rigor"), Principle 4 ("AW must be genuinely adversarial"), depth asymmetry checking, the anti-failure check for "Soft AW," and the corruption pre-inoculation section all structurally enforce this. -> **CLEARLY BETTER**
- **B. CoT**: No mechanism whatsoever. CoT follows the path of least resistance, which is almost always confirmatory. -> **CLEARLY WORSE**
- **C. ToT**: Breadth helps — multiple branches naturally explore different angles. But there's no mechanism ensuring that *adversarial* branches get equal depth to *supportive* ones. The evaluation step can actually *prune* adversarial branches if they seem less promising. -> **SLIGHTLY WORSE** than ARAW

### Derives Alternatives from Analysis
- **A. ARAW**: Multi-valued AW section explicitly requires alternatives to cite which wrongness finding they derive from. "Every alternative MUST cite which wrongness finding it derives from." -> **CLEARLY BETTER**
- **B. CoT**: Can suggest alternatives but they emerge from association/knowledge, not from the structure of the wrongness analysis. -> **CLEARLY WORSE**
- **C. ToT**: Branches naturally represent alternatives, but they're generated at the start (or via expansion), not derived from the failure of other branches. -> **SLIGHTLY WORSE** than ARAW

### Corruption Resistance
- **A. ARAW**: Entire "Corruption Pre-Inoculation" section. Explicit rules for handling user validation, agreement checks, validation sweeps, depth asymmetry detection, flattery detection, verdict drift detection. Also: "If >80% of claims VALIDATED, go back and test harder." -> **CLEARLY BETTER**
- **B. CoT**: No corruption resistance. Highly susceptible to prompt framing, sycophancy, and confirmation bias. -> **CLEARLY WORSE**
- **C. ToT**: The evaluation/voting step provides some resistance (multiple evaluations can catch bias), but there's no explicit anti-corruption machinery. -> **SLIGHTLY WORSE** than ARAW

---

## 5. Overall Assessment

```
CRITERION SUMMARY:
| Criterion                    | A. ARAW         | B. CoT          | C. ToT          | Edge   |
|------------------------------|-----------------|-----------------|-----------------|--------|
| Depth control                | Clearly better  | Clearly worse   | Slightly worse  | A      |
| Tracks findings              | Clearly better  | Clearly worse   | Slightly worse  | A      |
| Equal rigor both sides       | Clearly better  | Clearly worse   | Slightly worse  | A      |
| Derives alternatives         | Clearly better  | Clearly worse   | Slightly worse  | A      |
| Corruption resistance        | Clearly better  | Clearly worse   | Slightly worse  | A      |
| Simplicity (nice-to-have)    | Clearly worse   | Clearly better  | Slightly worse  | B      |
| General applicability (n-t-h)| Slightly worse  | Clearly better  | Slightly better | B      |
| Empirical validation (n-t-h) | Clearly worse   | Clearly better  | Slightly better | B      |
| Composability (n-t-h)        | Equivalent      | Slightly better | Slightly better | B/C    |

OVERALL: ARAW dominates on every important criterion for claim testing.
CoT and ToT win on the nice-to-haves (simplicity, generality, research backing).
```

---

## 6. Divergence Check

```
IMPRESSION said: ARAW is clearly strongest for claim testing.
ANALYSIS says: ARAW wins every important criterion by a wide margin.

DIVERGENCE? NO — but the LACK of divergence is itself suspicious.

Investigation: The impression predicted ARAW would dominate, and it does.
But the impression also predicted that CoT/ToT would have strengths that
matter more than initially weighted. The analysis confirms this only in
the nice-to-have tier.

The missing criterion the impression was sensing: PRACTICALITY.

ARAW is a heavy procedure. It requires significant token budget, structured
output, phase discipline, and a user who understands the notation. CoT
requires writing "let's think step by step." ToT requires a branching
prompt structure. For many real-world claim testing situations, the
question isn't "which is most thorough?" but "which will actually get used?"

This suggests a hidden important criterion: adoption friction. ARAW wins
on analytical power but may lose on "will someone actually do this?"
```

---

## 7. Recommendation

```
RECOMMENDATION: The three methods occupy different niches, not a single spectrum.

For claim testing specifically:
  - ARAW is the right tool when the claim matters enough to justify
    the overhead — high-stakes decisions, foundational assumptions,
    strategic bets. It's the only one that structurally prevents the
    common failure modes of claim testing (soft devil's advocacy,
    confirmation bias, lost findings, premature convergence).

  - CoT is appropriate for quick, low-stakes claim checks where you
    need "think about this a bit harder" not "stress-test this
    rigorously." It's a reasoning amplifier, not a claim-testing
    framework.

  - ToT occupies the middle ground — more thorough than CoT, less
    structured than ARAW. It's useful when you want breadth of
    exploration without the full ARAW apparatus, or when the "claim"
    is actually a search problem (finding the right framing) rather
    than a testing problem (validating a specific assertion).

CONFIDENCE: HIGH for the analytical comparison. MEDIUM for the
practical recommendation, because adoption friction is real and
hard to measure.

REASONING: ARAW was purpose-built for claim testing and it shows.
Every structural element — the AR/AW symmetry, the numbered registry,
the bedrock requirements, the corruption pre-inoculation, the depth
floors — addresses a specific failure mode of claim testing. CoT and
ToT are general reasoning tools that can be pointed at claims but
lack the structural safeguards that prevent the analysis from
degenerating into confirmation or hand-waving.

RISKS:
  - ARAW's thoroughness could be overkill for simple claims, wasting
    effort on claims that CoT would handle adequately.
  - ARAW's complexity could discourage use, leading people to default
    to CoT (which is worse but actually gets used).
  - ToT's research backing could make it the "safe" institutional
    choice even when ARAW would produce better results.

REVERSIBILITY: High. These are prompting strategies, not infrastructure
decisions. You can switch between them per-claim with zero switching cost.
```

---

## Key Insight: The Real Comparison Is About Failure Modes

The most revealing way to compare these three isn't "which is better" but "how does each fail at claim testing?"

| Failure Mode | CoT | ToT | ARAW |
|---|---|---|---|
| **Confirmation bias** (only finding supporting evidence) | Highly vulnerable — linear path follows path of least resistance | Partially resistant — breadth creates some adversarial branches by accident | Structurally resistant — AR/AW symmetry, equal-rigor principle, corruption pre-inoculation |
| **Soft devil's advocacy** ("it could be wrong, but...") | Default behavior — the "but" immediately rehabilitates the claim | Can happen — evaluation step may prune genuinely adversarial branches as "low quality" | Explicitly addressed — "That's not AW, that's AR wearing a hat" |
| **Lost findings** (important discoveries buried in prose) | Very common — findings exist only in running text | Moderate — tree structure provides some organization | Prevented — mandatory numbered registry, phase separation |
| **Premature convergence** (stopping before reaching bedrock) | Very common — CoT reaches a "reasonable" conclusion and stops | Moderate — evaluation step can converge too early | Addressed — bedrock requirements (BEDROCK-TEST/LOGIC/OBSERVE/TENSION), depth floors |
| **Validation parade** (every claim passes) | Common — no mechanism to check for this | Possible — depends on evaluation criteria | Explicitly checked — "If >80% validated, go back and test harder" |
| **Scope creep** (exploring everything, concluding nothing) | Rare (CoT is too linear for this) | Common — breadth can explode without convergence | Managed — phase separation forces convergence in Phase 2-3 |

CoT fails by being too shallow and confirmatory. ToT fails by being too broad and unfocused. ARAW fails by being too heavy for situations that don't warrant it. Choose based on which failure mode you can least afford.

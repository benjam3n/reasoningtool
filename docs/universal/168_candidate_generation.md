# Universal: Candidate Generation (168)

**Category**: SEARCH - How To Create Candidates?
**Source**: Creativity research, combinatorics, generative methods
**Structure**: Questions ordered by Value of Information (action divergence)

---

## VOI Rating = Action Divergence

- **HIGH**: Different answers → completely different action paths
- **MED**: Different answers → same general direction, different approach
- **LOW**: Different answers → same actions, different framing/flavor

---

## Core Insight

**You can only find what you generate.**

Search evaluates candidates. But candidates must first exist. Generation determines:
- The ceiling of search quality (best possible = best generated)
- The diversity of options (narrow generation = narrow search)
- Whether the answer is even in the space (if not generated, can't be found)

Most search failures are generation failures.

---

## Q1: How are candidates being generated?

[VOI: HIGH - generation method determines candidate pool]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Recall (from memory) | HIGH | Limited to known options | Fast but narrow | Miss novel options |
| Combination (recombine existing) | HIGH | Novel combinations possible | Creative but constrained | Miss truly novel |
| Derivation (from principles) | HIGH | Principled generation | Complete within theory | Miss outside theory |
| Random/mutation | MED | Unpredictable novelty | Escape constraints | Mostly noise |
| External (ask others, research) | HIGH | Access others' generation | Broader pool | Dependency |

---

## Q2: What constraints are being applied during generation?

[VOI: HIGH - constraints shape candidate space]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Strong constraints (few candidates) | HIGH | Narrow, focused search | Efficient if constraints correct | Miss good options if constraints wrong |
| Weak constraints (many candidates) | HIGH | Wide, exploratory search | More options | Evaluation burden |
| Unknown constraints | HIGH | Constraints may be implicit | Surface and examine | Invisible limits |

---

## Q3: Are constraints real or assumed?

[VOI: HIGH - false constraints eliminate good candidates]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| All constraints are real | MED | Work within constraints | Realistic | Miss by respecting false limits |
| Some constraints are assumed | HIGH | Test assumptions | May find new options | Waste time on impossible |
| Don't know | HIGH | Explicitly list and test | Verify each | Assume without checking |

---

## Q4: What's the generation goal - quantity or diversity?

[VOI: HIGH - determines generation strategy]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Quantity (many similar) | MED | Generate variations | Good coverage of region | Miss different regions |
| Diversity (few different) | HIGH | Generate across categories | Cover space broadly | Miss depth in promising areas |
| Both | HIGH | Multi-stage: diverse then deep | Comprehensive | Resource intensive |

---

## Q5: What templates or patterns exist for this type of candidate?

[VOI: HIGH - templates accelerate generation]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Known templates exist | HIGH | Use templates systematically | Fast, complete within template | Miss outside template |
| Templates could be created | MED | Abstract from examples | New template | Effort to create |
| No templates | MED | Generate from scratch | Unconstrained | Slow, may miss obvious |

---

## Q6: What would someone very different generate?

[VOI: MED - perspective-taking for diversity]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Expert in domain | MED | Domain-specific options | Technical depth | Narrow expertise |
| Novice | LOW | Naive but unconstrained | Fresh eyes | May be impractical |
| Adversary | MED | Challenging options | Stress test | Adversarial not constructive |
| Different culture/background | MED | Different assumptions | Genuine novelty | May not translate |

---

## Q7: What's the opposite of obvious candidates?

[VOI: MED - inversion for novelty]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Opposite exists and is viable | MED | Add to candidate pool | Expand range | Opposite may be bad |
| Opposite is nonsensical | LOW | Skip | Save effort | Miss creative interpretation |

---

## Q8: What candidates were rejected previously?

[VOI: MED - resurrection of discarded options]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Previously rejected, conditions changed | MED | Reconsider | May now be viable | Waste time re-evaluating |
| Previously rejected, conditions same | LOW | Skip | Efficient | Miss new perspective |

---

## Q9: Can candidates be combined or modified?

[VOI: MED - combinatorial generation]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Combinations viable | MED | Generate combinations | Exponential expansion | Evaluation burden |
| Modifications viable | MED | Generate variants | Incremental improvement | Miss radical options |
| Neither viable | LOW | Stick with base candidates | Simpler search | Miss combinatorial |

---

## Q10: When should generation stop?

[VOI: LOW - generation termination]

| Entry | VOI | Action Divergence | ASSUME RIGHT | ASSUME WRONG |
|-------|-----|-------------------|--------------|--------------|
| Fixed number | LOW | Generate N candidates | Simple | May be wrong N |
| Until diversity saturates | LOW | Generate until repeating | Good coverage | May take long |
| Until good-enough found | LOW | Generate until threshold | Efficient | May miss better |

---

## Summary Statistics

- Total questions: 10
- HIGH VOI: 9
- MED VOI: 9
- LOW VOI: 4

---

## Question Order by Action Divergence

**Ask first (HIGH VOI):**
1. Q1: How are candidates being generated?
2. Q2: What constraints are being applied?
3. Q3: Are constraints real or assumed?
4. Q4: Quantity or diversity goal?
5. Q5: What templates exist?

**Ask if relevant (MED VOI):**
6. Q6: What would someone different generate?
7. Q7: What's the opposite of obvious?
8. Q8: What was rejected previously?
9. Q9: Can candidates be combined/modified?

**Low priority (LOW VOI):**
10. Q10: When should generation stop?

---

## Generation Methods

| Method | How It Works | Strengths | Weaknesses |
|--------|--------------|-----------|------------|
| **Recall** | Retrieve from memory | Fast, proven | Limited to known |
| **Enumeration** | Systematically list all | Complete | Only for finite spaces |
| **Template filling** | Fill slots in pattern | Structured, fast | Limited to template |
| **Analogy** | Transfer from similar domain | Novel connections | May not fit |
| **Combination** | Mix elements of existing | Exponential options | Mostly noise |
| **Mutation** | Random modification | Escapes local | Mostly worse |
| **Inversion** | Opposite of expected | Challenges assumptions | Often impractical |
| **Constraint relaxation** | Remove assumed limits | New possibilities | May violate real limits |
| **Extreme values** | Maximize/minimize dimensions | Boundary exploration | Often impractical |
| **Role-taking** | Generate as someone else | Different perspective | May not translate |

---

## SCAMPER Technique

Systematic generation via modifications:

| Letter | Operation | Generation Prompt |
|--------|-----------|-------------------|
| **S** | Substitute | What can be substituted? |
| **C** | Combine | What can be combined? |
| **A** | Adapt | What can be adapted from elsewhere? |
| **M** | Modify/Magnify/Minimize | What can be changed in scale? |
| **P** | Put to other use | What else could this do? |
| **E** | Eliminate | What can be removed? |
| **R** | Reverse/Rearrange | What can be reordered? |

---

## Morphological Analysis

For structured generation:

1. Identify dimensions (variables that can vary)
2. List values for each dimension
3. Generate by combining one value from each dimension

Example:
- Dimension 1: [A, B, C]
- Dimension 2: [X, Y]
- Candidates: AX, AY, BX, BY, CX, CY

---

## Common Generation Errors

| Error | Pattern | Fix |
|-------|---------|-----|
| **Anchoring** | Generate near first idea | Start with diversity requirement |
| **False constraints** | Respect limits that don't exist | Test each constraint |
| **Template lock-in** | Only generate within template | Try template-free generation |
| **Expertise blindness** | Only generate what expert would | Ask naive observer |
| **Recency bias** | Generate recent things | Deliberately include old |
| **Similarity clustering** | All candidates too similar | Require diversity before depth |

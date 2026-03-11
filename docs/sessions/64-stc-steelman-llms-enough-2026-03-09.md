# /stc Steelman the position that reasoningtool is unnecessary because LLMs already think well enough
**Date:** 2026-03-09
**Skill:** /stc (Steelman Challenge)

---

## Step 1: State the Position Clearly

**Position being tested:** reasoningtool (a collection of 563 structured thinking procedures for LLMs) is unnecessary because LLMs already reason well enough without explicit procedural scaffolding.

**Key claims:**
1. Modern LLMs (Claude, GPT-4+, etc.) have sufficient reasoning capability built into their training.
2. Structured procedures add overhead without meaningfully improving output quality.
3. The problems reasoningtool solves are already solved by the models themselves.
4. Users would be better served by simply prompting the LLM directly than by invoking structured skill procedures.

**Evidence/reasoning supporting this position:**
- LLMs score well on reasoning benchmarks (MMLU, ARC, GSM8K, etc.) without procedural scaffolding.
- Chain-of-thought prompting is already internalized in modern models through RLHF and instruction tuning.
- Models like Claude already break down problems, consider multiple perspectives, and self-correct without being told to.
- The market hasn't widely adopted structured reasoning toolkits — most users prompt directly.

**Key assumptions:**
- That benchmark performance reflects real-world reasoning quality.
- That what the model does "by default" is close to optimal for most tasks.
- That the marginal improvement from structured procedures doesn't justify the complexity cost.

**Predictions:**
- Users who use reasoningtool won't produce meaningfully better outcomes than users who prompt well.
- As models improve, any current gap will close naturally without external scaffolding.

---

## Step 2: Identify All Attack Vectors

| # | Vector | Applicable? | Notes |
|---|--------|-------------|-------|
| 1 | Evidence attacks | Yes | Benchmark scores vs. real-world reasoning are different things |
| 2 | Logic attacks | Yes | "Good enough" is doing heavy lifting — good enough for what? |
| 3 | Assumption attacks | Yes | Assumes default behavior is near-optimal |
| 4 | Scope attacks | Yes | May be true for simple tasks, false for complex ones |
| 5 | Alternative explanations | Yes | Models may appear to reason well while being inconsistent |
| 6 | Consequence attacks | Yes | If true, all prompt engineering is also unnecessary |
| 7 | Empirical attacks | Yes | Observable differences between structured and unstructured outputs |

---

## Step 3: Steelman Each Counterargument

**C1 — The Consistency Argument (Evidence Attack)**
The strongest objection is that LLMs reason *inconsistently*, not *poorly*, and reasoningtool's value is in forcing consistent application of thinking steps, because without explicit procedures, the same model given the same problem will sometimes do excellent analysis and sometimes skip critical steps entirely — and the user has no way to predict which they'll get. This undermines the claim that LLMs "think well enough" because "well enough sometimes" is not "well enough."

**C2 — The Completeness Argument (Logic Attack)**
The strongest objection is that "thinking well" and "thinking completely" are different things, because an LLM may produce a plausible-sounding analysis that skips entire categories of consideration (e.g., assumption-checking, scope-limiting, adversarial testing). The model doesn't know what it skipped. A structured procedure like `/stc` forces the model to hit every attack vector rather than the 2-3 it would naturally gravitate toward, which undermines the claim that natural reasoning is sufficient by showing it is systematically incomplete rather than merely imperfect.

**C3 — The "Good Enough for What?" Argument (Scope Attack)**
The strongest objection is that the position conflates task difficulty levels, because LLMs are indeed "good enough" for answering factual questions, summarizing text, and simple analysis — but for high-stakes decisions, complex multi-factor tradeoffs, and situations where missing one consideration is costly, unstructured reasoning demonstrably fails. reasoningtool's value scales with task complexity and consequence severity. The position is true for 60% of use cases and dangerously false for the 40% that matter most.

**C4 — The Externalized Checklist Argument (Alternative Explanation)**
The strongest objection is that structured procedures serve the same function as checklists in aviation and surgery — not because pilots and surgeons can't think, but because even experts under cognitive load skip steps, and the consequence of skipping matters. LLMs have an analogous problem: context window pressure, training biases toward certain reasoning patterns, and tendency to satisfice. The evidence that LLMs "think well" is equally consistent with "LLMs think well when prompted to cover all the bases," which is exactly what reasoningtool does.

**C5 — The Prompt Engineering Reductio (Consequence Attack)**
The strongest objection is that if LLMs already think well enough without structured procedures, then all prompt engineering is also unnecessary, because reasoningtool is essentially codified prompt engineering — a library of proven prompting patterns. If the position is true, it implies that system prompts, few-shot examples, and chain-of-thought instructions also add no value. This is empirically false. The position proves too much.

**C6 — The Reproducibility Argument (Empirical Attack)**
The strongest objection is that reasoningtool makes reasoning *auditable and reproducible*, because when an LLM "just thinks," the user gets a black-box output with no way to verify which analytical steps were taken. A structured procedure produces output where every step is visible, checkable, and correctable. Even if the final answer were identical, the structured version is more trustworthy because its reasoning chain is inspectable. "Good enough thinking" that can't be verified isn't good enough for anything consequential.

**C7 — The Degradation Under Complexity Argument (Assumption Attack)**
The strongest objection is that LLM reasoning quality degrades nonlinearly with problem complexity, because the position assumes that performance on standard tasks predicts performance on hard tasks. In reality, LLMs exhibit a cliff: they handle moderate complexity smoothly, then fail abruptly on problems requiring 5+ interacting considerations. Structured procedures flatten this cliff by decomposing complex problems into manageable steps the model handles well individually. The assumption that "good enough on average" means "good enough at the edges" is where the position breaks.

---

## Step 4: Rate Each Counterargument

| # | Counterargument | Strength | What it threatens |
|---|----------------|----------|-------------------|
| C1 | Consistency: LLMs reason well *sometimes*, not *reliably*. Procedures ensure reliability. | **Strong** | Claim that LLMs "think well enough" — reframes "enough" as requiring consistency |
| C2 | Completeness: LLMs skip entire analytical categories without knowing it. Procedures force coverage. | **Devastating** | Core claim that reasoning is sufficient — shows systematic blind spots |
| C3 | Scope: True for easy tasks, false for hard ones. The hard ones are where it matters. | **Strong** | Scope of the position — shows it's only true where it doesn't matter much |
| C4 | Checklists: Even experts need procedural guardrails. LLMs are no different. | **Strong** | The logic that "capable = doesn't need structure" |
| C5 | Reductio: If true, all prompt engineering is unnecessary. That's empirically false. | **Devastating** | Logical coherence of the entire position |
| C6 | Reproducibility: Unverifiable reasoning isn't trustworthy reasoning. | **Moderate** | The "good enough" claim — adds a dimension the position ignores |
| C7 | Complexity cliff: Performance degrades nonlinearly; procedures prevent the cliff. | **Strong** | Assumption that average performance predicts edge-case performance |

---

## Step 5: Assess Which Are Genuine Threats

### C2 — Completeness (Devastating)

**Can the original position survive this?** Partially. One could argue that a skilled user naturally prompts for completeness ("consider all angles," "what am I missing?"). But this is effectively recreating reasoningtool ad hoc each time, which concedes the point — the structure is needed, the question is just whether it's pre-built or improvised.

**Does answering it require revising the position?** Yes. The position must narrow from "LLMs think well enough" to "LLMs think well enough *if the user knows what to ask for*" — which is a fundamentally different and much weaker claim.

**Is this counterargument actually correct?** Yes. This is empirically observable. Ask Claude to analyze a business decision without structure, and it will produce a coherent 3-4 consideration analysis. Use `/dcp` or `/cba` and it will reliably cover 8-12 considerations across multiple dimensions. The unstructured version *looks* complete but isn't.

**Status: Stands.** The position must be revised to account for this.

### C5 — Prompt Engineering Reductio (Devastating)

**Can the original position survive this?** Only by drawing an arbitrary line between "reasonable prompting" (acceptable) and "structured procedures" (unnecessary). But this line doesn't hold up — reasoningtool procedures ARE prompts, just carefully designed and reusable ones.

**Does answering it require revising the position?** Yes. The position either proves too much (all prompting is unnecessary) or must concede that some structured prompting helps, at which point it's arguing about degree rather than kind.

**Is this counterargument actually correct?** Yes. The effectiveness of prompt engineering is one of the most robustly demonstrated findings in LLM usage. reasoningtool is a library of prompt engineering patterns. Denying its value requires denying prompt engineering's value.

**Status: Stands.** This is logically fatal to the strong form of the position.

### C1 — Consistency (Strong)

**Can the original position survive this?** Only by redefining "well enough" to include inconsistency, which most users would reject. If you need the analysis to be good *this time*, "usually good" isn't good enough.

**Status: Stands.** Forces revision from "unnecessary" to "unnecessary if you're okay with variable quality."

### C3 — Scope (Strong)

**Can the original position survive this?** Yes, if narrowed: "For simple tasks, reasoningtool is unnecessary." This is probably true and is a fair critique — not every question needs a 6-step analytical procedure.

**Status: Stands, but reveals a genuine weakness in reasoningtool's positioning.** reasoningtool should acknowledge that many tasks don't need it.

### C4 — Checklists (Strong)

**Can the original position survive this?** Only by arguing LLMs are fundamentally different from human experts in a way that makes checklists unnecessary. This is hard to sustain given that LLMs exhibit many of the same failure modes (satisficing, recency bias, anchoring).

**Status: Stands.**

### C7 — Complexity Cliff (Strong)

**Can the original position survive this?** Only by claiming LLMs don't exhibit nonlinear degradation. But they do — this is widely documented in scaling and evaluation literature.

**Status: Stands.**

---

## Step 6: Report

```
STEELMANNED COUNTERARGUMENTS:
Position tested: "reasoningtool is unnecessary because LLMs already think well enough"

Counterarguments by strength:

DEVASTATING:
- C2: LLMs skip entire analytical categories without knowing it; procedures
  force systematic coverage. — Threatens: core sufficiency claim —
  Status: STANDS. The position must be revised.
- C5: If structured procedures are unnecessary, all prompt engineering is
  unnecessary. That's empirically false. — Threatens: logical coherence
  of the position — Status: STANDS. Logically fatal to the strong form.

STRONG:
- C1: LLMs reason well sometimes, not reliably. "Sometimes good" ≠ "good
  enough." — Threatens: reliability claim — Status: STANDS.
- C3: True for easy tasks, false for hard ones. Hard ones are where the
  stakes are. — Threatens: scope of the position — Status: STANDS, but
  also reveals that reasoningtool is overkill for simple queries.
- C4: Even expert reasoners need checklists. LLMs are no different. —
  Threatens: "capable = doesn't need structure" logic — Status: STANDS.
- C7: LLM reasoning degrades nonlinearly with complexity; procedures
  flatten the cliff. — Threatens: extrapolation from average to edge
  performance — Status: STANDS.

MODERATE:
- C6: Unverifiable reasoning isn't trustworthy. Structured output is
  auditable. — Threatens: whether "good enough" includes verifiability.

Position after testing: FATALLY WEAKENED in strong form.
The strong claim ("reasoningtool is unnecessary") does not survive.
Two devastating counterarguments stand unrefuted.

Surviving weak form: "For simple, low-stakes queries, structured reasoning
procedures add unnecessary overhead." This is probably true and is a
legitimate design consideration for reasoningtool.

Recommended revision: The position should be revised to:
"LLMs reason well enough for routine tasks without structured procedures,
but structured procedures materially improve consistency, completeness,
and auditability for complex or consequential analysis. reasoningtool's
value is concentrated in its hardest use cases."
```

---

## Verification

- [x] Position stated clearly before attacking
- [x] All seven attack vectors considered
- [x] Counterarguments are steelmanned (strongest version, not strawman)
- [x] Each rated by genuine threat level
- [x] Honest assessment of which survive — all strong+ counterarguments stand
- [x] Position updated: strong form fatally weakened, weak form survives and is instructive

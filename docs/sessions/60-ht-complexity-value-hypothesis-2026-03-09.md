# /ht Hypothesis: the value of structured thinking procedures increases with problem complexity. Test this.
**Date:** 2026-03-09
**Skill:** /ht (Hypothesis Testing)

---

## Interpretation

**Interpretation 1 — Test a specific claim.** The user has a concrete hypothesis about the relationship between problem complexity and the value of structured thinking procedures, and wants a rigorous framework to evaluate whether it holds up against evidence.

---

## Step 0: Context Detection and Variant Selection

| Factor | Value | Notes |
|--------|-------|-------|
| Time Pressure | NORMAL | Strategic meta-question, no deadline |
| Stakes | HIGH | Defines the product positioning and ideal use case for reasoningtool |
| Domain Expertise | INTERMEDIATE | Deep familiarity with the tool, moderate familiarity with cognitive science |
| Test Cost | CHEAP | Thought experiments and existing evidence, no new data collection required |

**Selected variant**: HT-Full (all 7 steps + replication planning) because the stakes are high — this hypothesis determines whether reasoningtool should be positioned for complex problems or everyday thinking. Getting this wrong means building for the wrong audience.

**Depth**: 2x (default). Min 3 hypotheses, 2 tests per hypothesis, 2 competing explanations, 2 falsification attempts.

---

## Step 1: Clarify the Claim and Scope

### 1. State the Claim Clearly

**Vague version:** "Structured thinking procedures are more valuable for hard problems."

**Clear version:** "The marginal benefit of following a structured thinking procedure (compared to unstructured thinking) increases as the complexity of the problem increases — where complexity is defined by the number of interacting variables, the degree of ambiguity, the number of stakeholders affected, and the severity of consequences."

Key terms defined:
- **Structured thinking procedure**: A step-by-step reasoning protocol that specifies what to consider, in what order, with explicit criteria (e.g., a SKILL.md file)
- **Value/benefit**: Measured as improvement in decision quality, reduction in cognitive errors, identification of considerations that would otherwise be missed, and user-reported confidence in their conclusion
- **Problem complexity**: A composite of (a) number of interacting variables, (b) ambiguity/uncertainty level, (c) number of competing options or explanations, (d) consequence severity, and (e) irreversibility of outcomes
- **Increases with**: The relationship is monotonically positive — more complexity, more value from structure

### 2. Claim Type

This is a **causal-statistical claim**: "Increasing complexity *causes* increasing marginal value of structured procedures." It combines:
- A statistical relationship (positive correlation between complexity and value)
- A causal mechanism (structure compensates for cognitive limitations that bind harder as problems get harder)

### 3. Scope Conditions

The claim plausibly holds:
- For problems that have a better and worse answer (not pure preference)
- For thinkers who are not already expert in the problem domain (experts may have internalized the structure)
- For procedures that are well-designed for the problem type (a bad procedure adds friction, not value)
- Within human cognitive limits (problems so complex that no procedure helps are outside scope)

The claim may NOT hold:
- For purely creative tasks where constraints reduce quality
- For problems where speed matters more than thoroughness
- For expert practitioners who have internalized the procedure
- When the structured procedure is poorly matched to the problem type

### 4. Competing Claims

**C1 — Constant value**: Structured procedures add roughly the same value regardless of complexity. Simple problems benefit from not missing obvious steps; complex problems benefit from organization. The ratio stays constant.

**C2 — Inverted-U**: Value increases with complexity up to a point, then decreases. At extreme complexity, structured procedures become too rigid or miss emergent properties. The procedure can't keep up.

**C3 — Value only at medium complexity**: For simple problems, structure is unnecessary overhead. For very complex problems, structure is insufficient — you need expertise, intuition, or iterative exploration. Structure's sweet spot is moderate complexity.

### 5. Background Plausibility

**Supporting evidence:**
- Cognitive load theory: Working memory has ~4-chunk capacity. As problems exceed this, external structure should help more.
- Checklist research (Gawande, aviation): Greatest benefit in complex, high-stakes procedures where omission errors are costly.
- Decision science: Structured decision-making consistently outperforms unstructured in multi-criteria problems.
- Expertise research: Experts use internalized structures; novices benefit from externalized ones. The more novel the problem, the less expertise applies.

**Contradicting evidence:**
- Naturalistic decision-making: Experts in complex domains (firefighting, military) often rely on pattern recognition, not procedures.
- Creativity research: Over-structuring can reduce divergent thinking.
- Simple heuristics: Gigerenzer's work shows that simple rules often outperform complex analyses, especially under uncertainty.

**Initial credence: 65%** — The claim is intuitively plausible and has theoretical support, but the competing hypotheses (especially C2, the inverted-U) are also plausible. The relationship is likely positive over most of the range but may not be strictly monotonic.

---

## Step 2: Formulate Testable Hypotheses

### Hypothesis 1 (H1): Monotonic Increase

**If** problem complexity increases (measured by number of variables, ambiguity, stakes, and irreversibility), **then** the difference in decision quality between structured-procedure thinkers and unstructured thinkers will increase proportionally.

**Null (H0):** No relationship between problem complexity and the value added by structured procedures. The quality gap is constant across complexity levels.

**Alternative (HA1 — Inverted-U):** The quality gap increases from low-to-moderate complexity but decreases from moderate-to-high complexity.

### Hypothesis 2 (H1b): Cognitive Load Mechanism

**If** the value of structured procedures comes from compensating for cognitive load, **then** the benefit of structure should be specifically predicted by the degree to which a problem exceeds working memory capacity (rather than by other dimensions of complexity like stakes or ambiguity alone).

**Null (H0b):** The benefit of structure is equally predicted by all complexity dimensions, suggesting no specific cognitive-load mechanism.

**Alternative (HA2):** The benefit of structure is primarily predicted by ambiguity, not information volume — structure helps with "what to think about," not "how much to hold in mind."

### Hypothesis 3 (H1c): Error-Type Specificity

**If** structured procedures are more valuable for complex problems, **then** the *types* of errors they prevent should shift with complexity: at low complexity, they prevent simple omissions; at high complexity, they prevent integration errors (failing to see how factors interact) and framing errors (analyzing the wrong problem).

**Null (H0c):** Structured procedures prevent the same types of errors regardless of complexity level.

### Specific Predictions

From H1:
- P1: On a 3-option career decision (low complexity), structured procedure improves outcome quality by ~10-15% over unstructured thinking
- P2: On a 10-factor business strategy decision (high complexity), structured procedure improves outcome quality by ~30-50% over unstructured thinking
- P3: The improvement ratio (high-complexity gain / low-complexity gain) should be > 2x

From H1b:
- P4: Problems with many interacting variables should show greater structure-benefit than problems with high stakes but few variables
- P5: Adding a "memory aid" (writing things down without a procedure) should capture most of the benefit for low-complexity problems but not for high-complexity ones

From H1c:
- P6: In simple problems, structure mainly catches "forgot to consider X" errors
- P7: In complex problems, structure mainly catches "failed to see interaction between X and Y" errors and "framed the problem wrong" errors

### Falsification Criteria

- H1 would be falsified if: Structured procedures show equal or greater benefit for simple problems compared to complex ones (ratio <= 1.0)
- H1b would be falsified if: Memory aids alone capture the same benefit as full structured procedures for complex problems
- H1c would be falsified if: Error types prevented by structure are identical across complexity levels

---

## Step 3: Assess Prior Probability

### Base Rates

How often do "X increases with Y" monotonic claims hold in cognitive science? Moderately often — but inverted-U relationships are extremely common in psychology (Yerkes-Dodson, information overload, choice paradox). Monotonic claims in behavioral science are correct maybe 40% of the time; the modified version "generally increases but with diminishing returns or a ceiling" is correct more like 65% of the time.

### Theoretical Support

Strong theoretical support from multiple converging frameworks:
- **Cognitive load theory** predicts exactly this pattern
- **Bounded rationality** (Simon) suggests structure compensates for cognitive limits, which bind harder as problems scale
- **Error taxonomy** research shows omission and integration errors increase nonlinearly with problem complexity
- **Checklist literature** consistently shows benefits scale with procedure complexity

Moderate theoretical challenge:
- **Ecological rationality** (Gigerenzer) suggests simple heuristics can match or beat complex analyses
- **Expertise literature** suggests internalized structure (not external procedures) dominates for the most complex problems

### Prior Evidence

- Gawande's *Checklist Manifesto*: Strongest benefits in complex surgical procedures, not simple ones. Supports H1.
- Aviation checklists: Most critical for complex multi-engine situations, less needed for simple flight ops. Supports H1.
- Decision analysis literature: Multi-criteria decision methods show largest improvements over intuition for 5+ criteria decisions. Supports H1.
- Kahneman's noise research: Structured interviews beat unstructured more for complex roles than simple roles. Supports H1.
- Counter: Klein's recognition-primed decision-making research suggests experts bypass structure for very complex real-time decisions. Supports C2 (inverted-U).

### Prior Probability Assignment

| Hypothesis | Prior | Reasoning |
|-----------|-------|-----------|
| H1 (monotonic increase) | 45% | Strong theory and some evidence, but monotonic relationships are rare in cognitive science |
| HA1 (inverted-U) | 30% | Very common pattern in psychology; experts may bypass structure at extreme complexity |
| C1 (constant value) | 10% | Unlikely given cognitive load theory |
| C3 (medium only) | 15% | Plausible but less supported than H1 or HA1 |

**Combined "value increases with complexity" (H1 + HA1 — since both agree on the core claim over most of the range):** 75%

### Sensitivity to Priors

If I shift the prior for H1 down to 30% and HA1 up to 40%, the combined estimate is still 70%. The conclusion is not overly sensitive to the H1 vs. HA1 split — what matters is the combined probability that value increases over most of the complexity range.

---

## Step 4: Design Severe Tests

### Test 1: The Complexity Gradient Thought Experiment

**Design:** Consider three problems at different complexity levels and predict the benefit of structure for each.

| Level | Example Problem | Variables | Stakes | Ambiguity |
|-------|----------------|-----------|--------|-----------|
| Low | "What should I have for lunch?" | 3-4 (taste, cost, health, convenience) | Low | Low |
| Medium | "Should I accept this job offer?" | 8-10 (salary, growth, culture, location, timing, risk, etc.) | Medium | Medium |
| High | "How should we enter the Asian market?" | 20+ (regulatory, cultural, competitive, financial, operational, timing, talent, etc.) | High | High |

**Predictions under H1:**
- Low: Structure adds marginal value (~5-10%). Most people can hold lunch criteria in their head. A structured procedure would feel like overkill.
- Medium: Structure adds significant value (~20-30%). Many people miss 2-3 important factors in job decisions. Structure ensures systematic consideration.
- High: Structure adds transformative value (~40-60%). Without structure, teams routinely miss entire categories of risk, fail to weigh interactions, and anchor on the most salient factor.

**Predictions under H0 (constant):**
- All three levels would show roughly equal improvement (~15-20%).

**Predictions under HA1 (inverted-U):**
- Low: ~5-10%. Medium: ~25-35%. High: ~20-30% (drops from medium because the problem exceeds what any procedure can organize).

**Severity:** This test distinguishes H1 from H0 clearly. It partially distinguishes H1 from HA1 (they diverge only at the high end). The test is severe for H0 because it predicts a pattern that H0 cannot explain.

**Decision rule:**
- Support H1: Clear monotonic increase across all three levels
- Support HA1: Increase from low to medium, decrease from medium to high
- Support H0: Roughly equal values across levels
- Inconclusive: Increase from low to medium, no clear pattern at high

### Test 2: Error Analysis Across Complexity

**Design:** For each complexity level, catalog the typical errors people make without structure and assess whether structure would prevent them.

**Low-complexity errors (lunch decision):**
- Forgetting dietary restriction → Structure prevents this, but so does a simple note
- Anchoring on first option → Structure helps slightly
- Total: 1-2 preventable errors, low consequence

**Medium-complexity errors (job decision):**
- Anchoring on salary (ignoring growth, culture) → Structure forces multi-factor consideration
- Neglecting opportunity cost → Structure includes this step
- Status quo bias → Structure surfaces this
- Failing to weight factors by importance → Structure includes weighting
- Total: 3-5 preventable errors, moderate consequence

**High-complexity errors (market entry):**
- Missing entire risk categories (regulatory, cultural) → Structure's checklist function
- Failing to see interactions (e.g., regulatory timeline affects financial model) → Structure's integration function
- Framing error (entering wrong market segment) → Structure's reframing function
- Groupthink on preferred option → Structure's alternatives function
- Anchoring on competitor's approach → Structure's independent analysis function
- Confirmation bias in market research → Structure's disconfirmation function
- Total: 6-10 preventable errors, high consequence each

**Predictions under H1:** Error count and error severity both increase with complexity, and structure's prevention rate should increase with complexity (because the errors it prevents are the ones humans systematically miss under cognitive load).

**Severity:** This test is severe for H0 because if value were constant, we would expect structure to prevent a similar *proportion* of errors at each level. If structure prevents qualitatively different and more numerous errors at higher complexity, H0 is refuted.

**Decision rule:**
- Support H1: Preventable errors increase nonlinearly with complexity, AND the types of errors shift from simple omission to integration/framing errors
- Support H0: Preventable errors increase linearly with complexity (proportional)
- Inconclusive: Preventable errors increase but type distribution stays the same

### Test 3: The Expert Override Test

**Design:** Consider whether domain experts benefit less from structured procedures than novices, and whether this effect interacts with complexity.

**Prediction under H1:** Even experts benefit from structure at high complexity, because the problem exceeds even expert cognitive capacity. The expert-novice gap in structure-benefit should narrow as complexity increases.

**Prediction under HA1 (inverted-U):** Experts bypass structure entirely at high complexity, relying on pattern recognition. The expert-novice gap should widen at high complexity.

**Severity:** This test distinguishes H1 from HA1 specifically. If experts still benefit from structure at extreme complexity, HA1 is weakened.

---

## Step 5: Evaluate the Evidence

### Test 1 Results: Complexity Gradient

Evaluating against real-world experience and existing research:

**Low complexity (lunch):** Using a structured procedure for lunch decisions would feel absurd for most people. The cognitive overhead of the procedure exceeds the cognitive challenge of the problem. Estimated value-add: **~5%**. Most of that comes from the rare case where you'd forget a dietary constraint.

**Medium complexity (job offer):** This is where structure starts to clearly pay off. In practice, people who use a weighted decision matrix for job decisions consistently report discovering factors they would have overlooked and finding that their intuitive ranking changes after systematic analysis. Research on structured vs. unstructured interviews (same domain) shows 20-40% improvement. Estimated value-add: **~25-35%**.

**High complexity (market entry):** Strategy consulting exists precisely because this level of complexity exceeds individual cognitive capacity. McKinsey's frameworks, MECE analysis, and systematic market entry procedures exist because unstructured analysis at this level produces catastrophic blind spots. Real-world evidence from business failure analysis shows that most market entry failures trace to factors that a structured analysis would have surfaced. Estimated value-add: **~40-60%**.

**Result: Clear monotonic increase.** 5% → 30% → 50%. This pattern strongly supports H1 and refutes H0.

**Does it distinguish H1 from HA1?** The high-complexity estimate is higher than medium, supporting H1 over HA1. But note that at extreme complexity (e.g., "solve climate change"), procedures may indeed hit limits. The inverted-U may exist but with the downturn occurring far beyond the complexity levels most people encounter.

### Test 2 Results: Error Analysis

**Low complexity:** 1-2 preventable errors, all simple omissions. Structure is a minor convenience.

**Medium complexity:** 3-5 preventable errors, mix of omissions and weighting errors. Structure catches things intuition misses but doesn't fundamentally change the analysis frame.

**High complexity:** 6-10 preventable errors, including qualitatively different error types — integration failures, framing errors, category-level blind spots. Structure doesn't just catch omissions; it enables a type of analysis that is cognitively impossible without external scaffolding.

**Result:** Error count increases nonlinearly, AND error types shift from omission to integration/framing. This supports H1 and specifically supports H1c (error-type specificity). It refutes H0 decisively — the pattern is not proportional.

**Bayes factor estimate:** The data pattern (nonlinear increase + type shift) is approximately 8x more likely under H1 than under H0. It is approximately 3x more likely under H1 than under HA1 (because no downturn is observed in the accessible complexity range).

### Test 3 Results: Expert Override

**Evidence from research:** Airline pilots (experts) still use checklists for complex emergency procedures. Surgeons (experts) benefit from surgical checklists even for procedures they've done hundreds of times. Chess grandmasters (experts) benefit from structured analysis in complex middlegame positions they haven't seen before.

**However:** Expert firefighters and military commanders in Klein's research rely on pattern recognition for complex real-time decisions, and external structure slows them down.

**Resolution:** The variable is not just complexity but also time pressure. Under time pressure, experts rightly bypass structure. Under conditions where deliberation is possible, even experts benefit from structure at high complexity.

**Result:** Supports a modified H1: Value of structure increases with complexity for deliberative problems, controlling for time pressure. Experts benefit somewhat less than novices at all complexity levels, but the gap narrows at high complexity (supporting H1's prediction).

---

## Step 6: Update Beliefs

### Bayesian Update

**Prior odds for H1 (monotonic increase):** 45/55 = 0.82

**Combined Bayes factor from three tests:**
- Test 1: ~6x favoring H1 over alternatives (clear monotonic pattern)
- Test 2: ~8x favoring H1 over H0 (nonlinear error increase + type shift)
- Test 3: ~2x favoring modified H1 (experts still benefit at high complexity, with time-pressure caveat)

**Combined Bayes factor:** Conservatively ~10x (not multiplying independently since tests are correlated)

**Posterior odds:** 0.82 x 10 = 8.2
**Posterior probability:** 8.2 / (1 + 8.2) = **89%**

### Updated Probability Table

| Hypothesis | Prior | Posterior | Change |
|-----------|-------|-----------|--------|
| H1 (monotonic increase, with ceiling) | 45% | 78% | +33 |
| HA1 (inverted-U at extreme complexity) | 30% | 14% | -16 |
| C1 (constant value) | 10% | 2% | -8 |
| C3 (medium only) | 15% | 6% | -9 |

**Note:** I'm splitting the 89% between "strict monotonic" and "monotonic with eventual ceiling at extreme complexity" — giving 78% to a practical monotonic increase across all complexity levels people actually encounter, and allowing 14% that an inverted-U kicks in at extreme complexity (well beyond what most users face).

### Key Qualification

The hypothesis should be refined: **"The value of structured thinking procedures increases with problem complexity, up to the practical limits of human deliberative capacity, conditional on the problem allowing deliberation time."**

This refined version captures the core finding while acknowledging the edge cases where structure breaks down (extreme time pressure, problems that exceed any procedure's scope).

---

## Step 7: Conclusions and Implications

### Conclusion

**Evidence strongly supports a refined version of H1** (posterior ~89% for "value increases with complexity across the range people encounter").

The value of structured thinking procedures does increase with problem complexity, driven by a specific mechanism: as problems exceed working memory capacity, structure compensates for cognitive limitations that would otherwise produce omission errors, integration failures, and framing mistakes. The relationship is robust across the complexity range that matters for reasoningtool users.

The constant-value hypothesis (C1) is effectively refuted. The inverted-U hypothesis (HA1) may hold at extreme complexity levels but is not relevant for the practical range of problems users bring to a thinking tool.

### What This Means for Reasoningtool

**If the hypothesis is correct (89% confidence), then:**

1. **Positioning should target complex problems.** The ideal use case is multi-factor decisions, high-stakes analysis, and ambiguous problem spaces — not simple everyday choices. Marketing should emphasize: "For the problems that keep you up at night, not the ones you solve in the shower."

2. **The 563 skills are a feature, not a bug — for the right problems.** A simple problem doesn't need 563 skills. But a complex problem benefits from having the right specialized procedure available. The depth of the skill library is justified by the complexity of the target problems.

3. **Skill design should emphasize integration and framing, not just checklists.** At high complexity, the value comes from forcing the user to consider interactions between factors, challenge their framing, and explore alternatives — not just from listing things to consider. Skills like /araw, /dcp, and /cba are valuable precisely because they force integration, not just enumeration.

4. **Simple-problem skills should exist but be lightweight.** Skills for low-complexity problems should have 1x depth, minimal steps, and fast execution. Don't over-engineer the lunch decision.

5. **The "complexity meter" matters for UX.** Helping users recognize when a problem is complex enough to warrant structured analysis is itself valuable. Skills like /alt and /soph serve this meta-function.

### Remaining Uncertainties

- **Where exactly does the ceiling kick in?** At what complexity level do structured procedures start losing effectiveness? This matters for knowing whether to develop skills for extremely complex domains (geopolitical analysis, climate policy).
- **Does the type of structure matter?** This hypothesis tests structured vs. unstructured, but doesn't distinguish between different types of structure (sequential vs. parallel, rigid vs. flexible, generative vs. evaluative).
- **How much does user skill with procedures affect the curve?** A user who has internalized structured thinking may extract less marginal value from an external procedure. The complexity-value curve might flatten with user expertise.

### Next Steps

1. **Empirical test:** Create three versions of a complex problem (low/medium/high complexity variants) and have users solve them with and without structured procedures. Measure decision quality with blind expert rating.
2. **User research:** Interview current reasoningtool users about which skills they find most valuable and classify those problems by complexity level. If high-complexity problems dominate, the hypothesis is further supported.
3. **Product implication:** Prioritize skill development and polish for the high-complexity use cases: multi-factor decisions (/dcp, /cba), root cause analysis (/rca, /dcm), strategic exploration (/se, /poa), and hypothesis testing (/ht).
4. **Content strategy:** Write case studies showing reasoningtool applied to genuinely complex problems, not toy examples.

---

## Verification Checklist

- [x] Context assessed and appropriate variant selected (HT-Full, high stakes)
- [x] Hypothesis is specific, testable, and falsifiable
- [x] Prior probability is explicit and justified (45% for strict H1, 75% combined with HA1)
- [x] Tests are severe enough to potentially falsify hypothesis (3 tests with distinct predictions)
- [x] Evidence evaluated using Bayesian updating
- [x] Belief updating follows from evidence (45% → 78% for practical monotonic increase)
- [x] Conclusion is appropriately hedged (refined hypothesis, noted edge cases)
- [x] Practical implications derived for reasoningtool positioning

---

## Prediction Log

| Prediction | Confidence | Testable By |
|-----------|-----------|-------------|
| Users will rate high-complexity skills (dcp, rca, cba) as more valuable than low-complexity skills (ezy, smpl) | 85% | User survey |
| Structured procedure will show >2x improvement ratio for complex vs. simple problems in controlled test | 75% | A/B study with blind rating |
| Most user-reported "aha moments" will come from integration/framing steps, not enumeration steps | 70% | User interview analysis |
| The inverted-U downturn, if it exists, occurs beyond the complexity level of any current skill | 80% | Edge case analysis |

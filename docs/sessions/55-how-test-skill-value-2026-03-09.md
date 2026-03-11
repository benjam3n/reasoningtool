# /how How do I systematically test whether a skill actually produces better outputs than not using it?
**Date:** 2026-03-09
**Skill:** /how (Find the Method)

---

## /how Routing

**Goal extracted:** Systematically test whether a structured reasoning skill produces better outputs than unstructured prompting.

**Is this method-seeking?** Yes. The user knows what they want (empirical evidence of skill value) but not how to get it.

**Is the goal well-defined?** Yes. "Test whether skill X produces better output than no-skill" is concrete and measurable.

**Constraints identified:**
- Solo developer (limited time/budget for large studies)
- 592 skills (can't test all of them; need a sampling strategy)
- LLM outputs are stochastic (same prompt, different outputs)
- "Better" needs operationalization (better by whose judgment? on what dimensions?)

**Complexity assessment:** Multi-step method. Needs method discovery + step generation. This is an experimental design question, which is non-trivial.

**Routing decision:** INVOKE /foht

---

## /foht — Figure Out How To: Test Skill Value Empirically

### Phase 1: EXPLORATION

#### Step 1: Define the Outcome

```
GOAL: Determine whether using a structured skill procedure produces
      measurably better outputs than prompting without it.

DONE LOOKS LIKE: A reusable test protocol that, when applied to any skill,
      produces quantified evidence of whether that skill adds value —
      with enough rigor to trust the results and enough simplicity
      to actually run.

SUCCESS CRITERIA:
  [H1] MUST: Produces a numeric comparison (skill vs. no-skill) on defined quality dimensions
  [H2] MUST: Controls for prompt variation — same task, same input, only the skill differs
  [H3] MUST: Handles LLM stochasticity — single runs are insufficient
  [H4] MUST: Defines "better" concretely before running the test (not post-hoc)
  [H5] SHOULD: Feasible for a solo developer to run on 5-10 skills in a day
  [H6] SHOULD: Produces results convincing to a skeptical outsider (not just the developer)
  [H7] SHOULD: Distinguishes "skill adds structure" from "skill adds length/verbosity"

CONSTRAINTS:
  [H8] Solo developer — no team of raters available on-demand
  [H9] LLM API costs — each test run costs money; budget is finite
  [H10] 592 skills — need a sampling strategy, can't test all
  [H11] Time — need results in days, not months
  [H12] No existing baseline data — starting from zero

NOT THE GOAL:
  - Proving all 592 skills work (that's infeasible)
  - Academic publication-grade research (that's overkill)
  - User satisfaction testing (that requires users)
```

#### Step 2: Map the Method Space

**Direct methods — standard approaches:**

```
[H13] METHOD: A/B blind evaluation — Generate output with and without skill,
      blind-rate both, compare scores.
[H14] METHOD: Rubric-based scoring — Define quality rubrics per task type,
      score skill vs. no-skill outputs against the rubric.
[H15] METHOD: LLM-as-judge — Use a separate LLM to evaluate paired outputs
      (skill vs. no-skill) on defined criteria.
```

**Instance-to-category — what is this goal an instance of?**

```
[H16] "Testing whether a skill produces better output" is an instance of
      CONTROLLED EXPERIMENT DESIGN — specifically, intervention testing.
[H17] Category method: Randomized controlled trial design — define population
      (tasks), intervention (skill), control (no skill), outcome measure
      (quality score), run N trials, compare means.
[H18] Category method: Pre-registration — define hypotheses and metrics
      before running, to prevent post-hoc rationalization.
```

**Inversion — what would prevent valid testing?**

```
[H19] BLOCKER: Evaluator bias — if the creator rates the outputs, they'll
      favor the skill (confirmation bias).
[H20] REMOVAL METHOD: Blind evaluation — strip identifiers, randomize order,
      rate without knowing which used the skill.
[H21] BLOCKER: Task selection bias — if you pick tasks the skill is good at,
      results are inflated.
[H22] REMOVAL METHOD: Pre-define task selection criteria or sample randomly
      from a task bank.
[H23] BLOCKER: Conflating verbosity with quality — skills often produce
      longer, more structured output. Longer ≠ better.
[H24] REMOVAL METHOD: Include "conciseness" or "signal-to-noise" as an
      explicit rubric dimension.
[H25] BLOCKER: Single-run noise — LLM outputs vary run to run. One
      comparison proves nothing.
[H26] REMOVAL METHOD: Multiple trials per task (minimum 3-5), report
      variance alongside means.
```

**Adjacent success — who has achieved something similar?**

```
[H27] EXEMPLAR: LMSYS Chatbot Arena — uses blind pairwise comparison with
      human judges to rank LLMs. METHOD: Pairwise preference voting at scale.
[H28] EXEMPLAR: Academic prompt engineering papers — use benchmark tasks with
      known correct answers, compare accuracy with/without prompt technique.
      METHOD: Benchmark accuracy measurement on tasks with ground truth.
[H29] EXEMPLAR: Chain-of-thought prompting papers (Wei et al.) — tested
      structured prompting vs. standard prompting on math/reasoning benchmarks
      with quantified accuracy. METHOD: Automated scoring on tasks with
      verifiable answers.
```

**Reframe — is there a way to dissolve the problem?**

```
[H30] REFRAME: Instead of testing "does the skill produce better output,"
      test "does the skill produce output the user couldn't have gotten by
      just asking?" — the value-add question. If a smart prompt gets 90% of
      the way there, the skill's marginal value is low regardless of
      absolute quality.
[H31] REFRAME: Instead of testing output quality, test whether the skill
      surfaces considerations the user would have missed. The value of a
      thinking procedure isn't just output quality — it's coverage of the
      problem space.
```

**Decomposition — break the goal into sub-goals:**

```
[H32] SUB-GOAL: Define what "better" means per task type — METHOD: Create
      quality rubrics with 3-5 dimensions per task category (decision,
      diagnosis, analysis, etc.)
[H33] SUB-GOAL: Generate matched pairs of outputs — METHOD: Same task prompt
      run with skill instruction and without, temperature=0 or fixed seed
      where possible, multiple runs.
[H34] SUB-GOAL: Evaluate outputs without bias — METHOD: Blind evaluation
      with randomized presentation order.
[H35] SUB-GOAL: Aggregate and interpret results — METHOD: Statistical
      comparison (paired t-test or Wilcoxon signed-rank for small N).
[H36] SUB-GOAL: Sample skills representatively — METHOD: Stratified sampling
      across skill categories and complexity tiers.
```

#### Step 3: Surface Prerequisites

```
[H37] METHOD [H13] A/B blind eval requires: a way to strip skill
      identifiers from output — HAVE IT: yes (manual editing)
[H38] METHOD [H13] requires: evaluator discipline to rate blind —
      HAVE IT: uncertain (solo dev knows their own skills)
[H39] METHOD [H14] rubric scoring requires: pre-defined rubrics per task
      type — HAVE IT: no (must be created)
[H40] METHOD [H15] LLM-as-judge requires: a judge model that doesn't share
      biases with the generation model — HAVE IT: yes (use different
      model family or frontier model)
[H41] METHOD [H15] requires: validated judge criteria (LLM judges have
      known biases: verbosity preference, position bias) — HAVE IT:
      partially (known biases can be mitigated)
[H42] METHOD [H17] RCT design requires: sufficient sample size for
      statistical power — HAVE IT: depends on effect size (large effects
      need fewer samples)
[H43] METHOD [H28] benchmark approach requires: tasks with known correct
      answers — HAVE IT: partially (some task types have ground truth,
      many don't)
[H44] METHOD [H29] automated scoring requires: verifiable answer tasks —
      HAVE IT: limited (most thinking skills apply to open-ended tasks
      where correctness isn't binary)
```

#### Step 4: Test Methods (AR/AW)

**METHOD [H13]: A/B Blind Evaluation**

```
ASSUME RIGHT (this method works):
  [H45] If right: produces human-judged quality scores for skill vs.
        no-skill — Necessary
  [H46] If right: blind evaluation removes conscious bias — Probable
  [H47] FORECLOSED: speed — manual evaluation is slow, limits sample size

ASSUME WRONG (this method fails):
  [H48] Wrong because: solo developer can't truly blind-evaluate their own
        skills — they'll recognize structural patterns — Serious
    [H49] Even with stripped labels, skill outputs have distinctive
          structure (numbered findings, phase headers) → BEDROCK:
          structural signatures leak identity
  [H50] Wrong because: manual evaluation doesn't scale — 5 skills × 5
        tasks × 5 runs = 125 evaluations — Conditional
    [H51] Conditional on how many skills you test. For 5-10 skills,
          it's feasible but tedious.

VERDICT: CONDITIONAL — works if evaluator can maintain genuine blindness
  (hard for the creator) and sample size is kept manageable.
```

**METHOD [H15]: LLM-as-Judge**

```
ASSUME RIGHT (this method works):
  [H52] If right: enables automated evaluation at scale — Necessary
  [H53] If right: removes human evaluator bias — Probable
  [H54] If right: enables testing many skills quickly (5-10 per day
        feasible) — Necessary
  [H55] FORECLOSED: certainty about what "quality" really means —
        LLM judges operationalize quality differently than humans might

ASSUME WRONG (this method fails):
  [H56] Wrong because: LLM judges have known biases — prefer verbose,
        well-structured output regardless of substance — Serious
    [H57] Skills produce more structured output. LLM judge may reward
          structure itself, not the thinking quality. → BEDROCK:
          systematic bias toward the very features skills add.
  [H58] Wrong because: LLM judge may not evaluate "quality of thinking"
        well — may evaluate surface presentation — Serious
    [H59] Validated by research: LLM judges correlate with human
          preferences ~80% but fail on nuanced quality differences.

VERDICT: CONDITIONAL — works if judge prompts explicitly counteract
  verbosity bias AND results are validated against a human-judged subset.
  Best used as primary method with human spot-check.
```

**METHOD [H28]: Benchmark with Ground Truth**

```
ASSUME RIGHT (this method works):
  [H60] If right: produces objective, unambiguous scores — Necessary
  [H61] If right: eliminates evaluator bias entirely — Necessary
  [H62] FORECLOSED: testing skills on open-ended tasks (most of the
        toolkit's value proposition)

ASSUME WRONG (this method fails):
  [H63] Wrong because: most thinking skills target open-ended reasoning,
        not tasks with correct answers — Fatal for general skill testing
    [H64] You can test /claim on factual claims, /rca on known-cause
          problems. But /decide, /how, /want — no ground truth exists.
          → BEDROCK: open-ended reasoning has no ground truth.
  [H65] Wrong because: narrow benchmark tasks may not represent real
        use cases — Serious
    [H66] A skill that helps with complex real decisions but not with
          toy problems gives a false negative. → BEDROCK: ecological
          validity problem.

VERDICT: CONDITIONAL — viable only for skills with verifiable outputs
  (subset). Necessary complement but can't be the only method.
```

**METHOD [H30]: Marginal Value Test (Reframe)**

```
ASSUME RIGHT (this method works):
  [H67] If right: directly answers the business question — does the skill
        add value beyond what a good prompt already gets? — Necessary
  [H68] If right: reframes from "is skill output good?" to "is skill output
        better than the counterfactual?" — which is the actual question —
        Necessary
  [H69] FORECLOSED: nothing — this reframe strengthens any of the above
        methods rather than replacing them

ASSUME WRONG (this method fails):
  [H70] Wrong because: requires a strong "no-skill" baseline — what prompt
        do you use for the control? — Conditional
    [H71] Control prompt matters enormously. "Just answer this" vs.
          "Think carefully about this" are very different baselines.
          Must define the control prompt precisely.

VERDICT: VIABLE — this is a framing enhancement that applies to any
  evaluation method. The control prompt definition is critical but solvable.
```

**METHOD [H31]: Coverage Test**

```
ASSUME RIGHT (this method works):
  [H72] If right: measures whether the skill surfaces considerations that
        unstructured prompting misses — Necessary
  [H73] If right: captures a dimension of value that output-quality scoring
        misses — Probable
  [H74] FORECLOSED: overall quality judgment — coverage is one dimension,
        not the whole picture

ASSUME WRONG (this method fails):
  [H75] Wrong because: requires a "ground truth" set of considerations
        to check against — Serious
    [H76] For some domains, experts can define what should be considered.
          For novel problems, no such list exists. Partially mitigated by
          using the union of all outputs as the consideration set.
  [H77] Wrong because: more considerations ≠ better — some skills might
        surface irrelevant tangents — Conditional
    [H78] Needs relevance-weighted coverage, not raw count.

VERDICT: CONDITIONAL — valuable complementary metric. Works best when
  combined with quality scoring. Requires expert-defined consideration
  sets or a union-based approach.
```

**METHOD: Hybrid Protocol (synthesized from above)**

```
[H79] METHOD: Combined protocol — LLM-as-judge for scale + human blind
      evaluation for validation + benchmark tasks where ground truth exists
      + coverage analysis as secondary metric.

ASSUME RIGHT (this works):
  [H80] If right: covers multiple validity threats — no single bias
        invalidates all measures — Necessary
  [H81] If right: feasible for solo developer — LLM judging handles
        volume, human judging validates a subset — Probable
  [H82] FORECLOSED: simplicity — this is a multi-method approach

ASSUME WRONG (this fails):
  [H83] Wrong because: complexity may prevent execution — solo developer
        gives up before completing the protocol — Serious
    [H84] Mitigated by: phased approach — start with LLM-as-judge, add
          human validation only if results are promising or ambiguous.

VERDICT: VIABLE — best overall approach if scoped to a manageable first
  batch of skills.
```

#### Step 5: Edge Cases

```
[H85] METHOD [H79] breaks when: skill and no-skill outputs are very
      similar — the difference may be real but too small to detect with
      small N. Need power analysis.
[H86] METHOD [H79] breaks at scale: testing all 592 skills would require
      thousands of LLM calls. Must prioritize. Stratified sampling of
      10-20 representative skills first.
[H87] METHOD [H79] has hidden cost: defining rubrics per task type is
      significant upfront work. The rubric quality determines everything
      downstream.
[H88] ALL METHODS break when: the skill's value is in the process, not
      the output. Some skills help the user think, not the LLM output.
      That value is unmeasurable via output comparison.
[H89] ALL METHODS break when: "better" is domain-specific and the
      evaluator (human or LLM) lacks domain expertise.
[H90] LLM-as-judge [H15] breaks when: judge model is the same family
      as generation model — shared blind spots.
```

---

### Phase 2: FINDING REGISTRY

```
FINDING REGISTRY
================

SUCCESS CRITERIA:
[H1] Numeric comparison on defined quality dimensions -- TYPE: must
[H2] Controls for prompt variation -- TYPE: must
[H3] Handles LLM stochasticity with multiple trials -- TYPE: must
[H4] Defines "better" before running, not post-hoc -- TYPE: must
[H5] Feasible for solo developer on 5-10 skills in a day -- TYPE: should
[H6] Convincing to skeptical outsider -- TYPE: should
[H7] Distinguishes structure from substance -- TYPE: should

CONSTRAINTS:
[H8] Solo developer — no rater team
[H9] LLM API costs — finite budget
[H10] 592 skills — need sampling strategy
[H11] Time — results in days, not months
[H12] No existing baseline data

METHODS FOUND:
[H13] A/B blind evaluation -- SOURCE: direct
[H14] Rubric-based scoring -- SOURCE: direct
[H15] LLM-as-judge -- SOURCE: direct
[H17] Randomized controlled trial design -- SOURCE: category
[H18] Pre-registration -- SOURCE: category
[H20] Blind evaluation (from inversion of bias) -- SOURCE: inversion
[H22] Random/criteria-based task selection -- SOURCE: inversion
[H24] Conciseness rubric dimension -- SOURCE: inversion
[H26] Multiple trials per task -- SOURCE: inversion
[H27] Pairwise preference voting -- SOURCE: exemplar (Chatbot Arena)
[H28] Benchmark accuracy on ground-truth tasks -- SOURCE: exemplar
[H29] Automated scoring on verifiable tasks -- SOURCE: exemplar
[H30] Marginal value test (value-add framing) -- SOURCE: reframe
[H31] Coverage test (considerations surfaced) -- SOURCE: reframe
[H79] Hybrid protocol -- SOURCE: synthesis

PREREQUISITES:
[H37] Strip skill identifiers from output -- FOR: [H13] -- MET: yes
[H38] Evaluator blindness discipline -- FOR: [H13] -- MET: uncertain
[H39] Pre-defined rubrics per task type -- FOR: [H14] -- MET: no
[H40] Judge model from different family -- FOR: [H15] -- MET: yes
[H41] Validated judge criteria -- FOR: [H15] -- MET: partially
[H42] Sufficient sample size -- FOR: [H17] -- MET: depends on effect size
[H43] Tasks with known correct answers -- FOR: [H28] -- MET: partially
[H44] Verifiable answer tasks -- FOR: [H29] -- MET: limited

AR FINDINGS:
[H45] Blind eval produces human-judged scores -- FOR: [H13] -- STRENGTH: necessary
[H46] Blind eval removes conscious bias -- FOR: [H13] -- STRENGTH: probable
[H52] LLM judge enables scale -- FOR: [H15] -- STRENGTH: necessary
[H53] LLM judge removes human bias -- FOR: [H15] -- STRENGTH: probable
[H54] LLM judge enables 5-10 skills/day -- FOR: [H15] -- STRENGTH: necessary
[H60] Benchmark gives objective scores -- FOR: [H28] -- STRENGTH: necessary
[H61] Benchmark eliminates evaluator bias -- FOR: [H28] -- STRENGTH: necessary
[H67] Marginal value answers the business question -- FOR: [H30] -- STRENGTH: necessary
[H68] Reframes to the actual counterfactual -- FOR: [H30] -- STRENGTH: necessary
[H72] Coverage test captures missed considerations -- FOR: [H31] -- STRENGTH: necessary
[H80] Hybrid covers multiple validity threats -- FOR: [H79] -- STRENGTH: necessary
[H81] Hybrid is feasible for solo dev -- FOR: [H79] -- STRENGTH: probable

AW FINDINGS:
[H48] Solo dev can't truly blind-evaluate own skills -- FOR: [H13] -- SEVERITY: serious
[H56] LLM judges prefer verbose structured output -- FOR: [H15] -- SEVERITY: serious
[H58] LLM judges evaluate surface, not thinking quality -- FOR: [H15] -- SEVERITY: serious
[H63] Most skills target open-ended tasks, no ground truth -- FOR: [H28] -- SEVERITY: fatal (for general use)
[H65] Narrow benchmarks don't represent real use -- FOR: [H28] -- SEVERITY: serious
[H70] Control prompt definition is critical -- FOR: [H30] -- SEVERITY: conditional
[H75] Coverage needs ground truth consideration set -- FOR: [H31] -- SEVERITY: serious
[H83] Complexity may prevent execution -- FOR: [H79] -- SEVERITY: serious

EDGE CASES:
[H85] Small effect sizes undetectable at low N -- FOR: [H79]
[H86] 592 skills requires stratified sampling -- FOR: [H79]
[H87] Rubric creation is significant upfront cost -- FOR: [H79]
[H88] Value in process (user thinking) unmeasurable via output -- FOR: all
[H89] Domain-specific "better" needs domain expertise -- FOR: all
[H90] Same-family judge model has shared blind spots -- FOR: [H15]

METHOD VERDICTS:
[H13] A/B blind evaluation -- VERDICT: conditional
  -- AR evidence: [H45], [H46]
  -- AW evidence: [H48], [H49], [H50]
  -- Prerequisites: uncertain — [H38]
  -- Edge cases: [H85]

[H15] LLM-as-judge -- VERDICT: conditional
  -- AR evidence: [H52], [H53], [H54]
  -- AW evidence: [H56], [H57], [H58]
  -- Prerequisites: partially met — [H40], [H41]
  -- Edge cases: [H90]

[H28] Benchmark accuracy -- VERDICT: conditional (subset only)
  -- AR evidence: [H60], [H61]
  -- AW evidence: [H63], [H64], [H65]
  -- Prerequisites: limited — [H43], [H44]
  -- Edge cases: [H88]

[H30] Marginal value framing -- VERDICT: viable
  -- AR evidence: [H67], [H68]
  -- AW evidence: [H70], [H71]
  -- Prerequisites: met (with careful control definition)
  -- Edge cases: none unique

[H31] Coverage test -- VERDICT: conditional
  -- AR evidence: [H72], [H73]
  -- AW evidence: [H75], [H76], [H77]
  -- Prerequisites: partially met
  -- Edge cases: [H89]

[H79] Hybrid protocol -- VERDICT: viable
  -- AR evidence: [H80], [H81]
  -- AW evidence: [H83], [H84]
  -- Prerequisites: mostly met
  -- Edge cases: [H85], [H86], [H87]

TOTALS:
- Success criteria: 7
- Methods found: 15
- Prerequisites surfaced: 8 (2 met, 3 partially, 2 uncertain, 1 no)
- AR findings: 12
- AW findings: 8 (1 fatal, 5 serious, 2 conditional)
- Edge cases: 6
- Verdicts: 2 viable, 4 conditional, 0 blocked, 0 eliminated, 0 uncertain
```

---

### Phase 3: SYNTHESIS

```
GOAL: Determine whether using a structured skill procedure produces
      measurably better outputs than prompting without it.

DONE LOOKS LIKE: A reusable test protocol that produces quantified
      evidence of skill value, runnable by a solo developer in days.

METHODS TESTED: 6

VIABLE METHODS:
1. Hybrid protocol [H79] — VERDICT: viable
   - What it requires: rubrics [H39], judge model [H40], task bank,
     multiple trials [H26]
   - What it costs: upfront rubric design [H87], API costs for LLM
     judging, human time for validation subset
   - What it forecloses: simplicity [H82]
   - Breaks when: effect sizes are small [H85], skills tested > 20 [H86]

2. Marginal value framing [H30] — VERDICT: viable
   - Applied as a lens on any evaluation method
   - Works if: control prompt is precisely defined [H71]
   - Fails if: control prompt is too weak (straw man) or too strong
     (already includes the skill's insight)

CONDITIONAL METHODS (usable as components):
3. LLM-as-judge [H15] — conditional on verbosity bias mitigation
4. A/B blind eval [H13] — conditional on achieving genuine blindness
5. Benchmark accuracy [H28] — conditional on task type (verifiable only)
6. Coverage test [H31] — conditional on defining consideration sets

ELIMINATED METHODS: None fully eliminated. All have conditional use.

RECOMMENDED APPROACH:
The hybrid protocol [H79], structured as a phased rollout, using the
marginal value framing [H30]. Specifically:
```

---

## The Protocol: Testing Skill Value

### Design Principles (from findings)

1. **Marginal value, not absolute quality** [H30]. The question is never "is the skill output good?" but "is it better than what you'd get without the skill?" The control prompt is therefore the most important design decision.

2. **Multi-method evaluation** [H79]. No single evaluation method is unbiased. Use LLM-as-judge for volume, human review for validation, benchmark tasks where available.

3. **Pre-register everything** [H18]. Define rubrics, select tasks, and specify success thresholds before running a single test. Post-hoc rationalization is the primary threat to validity.

### Step 1: Select Skills to Test (Day 1, 1 hour)

Stratified sample across the skill space:

| Stratum | Example skills | Pick N |
|---------|---------------|--------|
| Decision skills | /dcp, /cba, /cmp | 2 |
| Analysis skills | /rca, /dcm, /aex | 2 |
| Exploration skills | /se, /foht, /dd | 2 |
| Validation skills | /claim, /ht, /pv | 2 |
| Writing skills | /pw, /stl, /w | 1 |
| Meta/routing skills | /how, /decide | 1 |

Total: 10 skills. Enough to see patterns, few enough to execute.

### Step 2: Define Task Bank (Day 1, 2-3 hours)

For each selected skill, create 5 test tasks:
- 3 tasks within the skill's sweet spot (where it should help)
- 1 task at the edge of the skill's scope (where benefit is unclear)
- 1 task outside the skill's scope (negative control — skill should not help)

**Task format:**
```
TASK_ID: [skill]-[number]
INPUT: [the problem/question to give the LLM]
TYPE: [sweet-spot / edge / negative-control]
GROUND_TRUTH: [if verifiable, the correct answer or key considerations]
```

Total: 50 tasks.

### Step 3: Define Quality Rubrics (Day 1, 2 hours)

Pre-register rubrics BEFORE seeing any outputs.

**Universal dimensions (all task types):**

| Dimension | 1 (Poor) | 3 (Adequate) | 5 (Excellent) |
|-----------|----------|--------------|---------------|
| **Completeness** | Misses major considerations | Covers main points, misses some | Comprehensive coverage |
| **Accuracy** | Contains errors or unsupported claims | Mostly accurate | Accurate with appropriate caveats |
| **Actionability** | Vague or no next steps | Some actionable items | Clear, specific, prioritized next steps |
| **Signal-to-noise** | Padded, verbose, repetitive | Reasonable length, some filler | Every sentence adds value |
| **Intellectual honesty** | Overconfident, hides uncertainty | Acknowledges some limits | Transparent about what's known vs. uncertain |

**Task-type-specific dimensions:** Add 1-2 per skill category (e.g., "surfaces non-obvious alternatives" for decision skills).

### Step 4: Define the Control Prompt (Critical)

Three control tiers, to measure marginal value at different baselines:

```
CONTROL-A (naive): "[task input]"
  — Raw question, no instructions.

CONTROL-B (good prompt): "Think carefully and systematically about:
  [task input]. Consider multiple perspectives, identify key factors,
  and provide actionable recommendations."
  — The prompt a competent user would write.

CONTROL-C (detailed prompt): "You are an expert analyst. For [task input],
  please: 1) Identify the key considerations, 2) Consider at least 3
  different approaches, 3) Evaluate trade-offs, 4) Recommend a course
  of action with reasoning, 5) Note what could go wrong."
  — The prompt that captures the skill's intent without its specific procedure.
```

**The real test is skill vs. CONTROL-C.** If the skill doesn't beat a well-written prompt that captures its general intent, the skill's specific procedure isn't adding value — only its framing is.

### Step 5: Generate Outputs (Day 2, automated)

For each of 50 tasks, generate:
- 1 output using the full skill procedure
- 1 output each for Control-A, Control-B, Control-C
- Run each 3 times (temperature > 0) for stochasticity handling [H3]

Total: 50 tasks x 4 conditions x 3 runs = 600 LLM calls.

**Automation script structure:**
```python
for task in task_bank:
    for condition in [skill, control_a, control_b, control_c]:
        for trial in range(3):
            prompt = build_prompt(task, condition)
            output = llm.generate(prompt, temperature=0.7)
            save(task_id, condition, trial, output)
```

### Step 6: LLM-as-Judge Evaluation (Day 2-3, automated)

Use a different model family as judge (e.g., if generating with Claude, judge with GPT-4 or vice versa) [H90].

**Judge prompt (anti-verbosity-bias version):**
```
You are evaluating the quality of an analytical response.
Rate ONLY on substance, not on length or formatting.

A short, precise response that nails the key points scores HIGHER
than a long, well-structured response that adds filler.

[RUBRIC dimensions and scale here]

RESPONSE TO EVALUATE:
[output — stripped of skill formatting artifacts]

Rate each dimension 1-5 with a one-sentence justification.
```

**Critical: Strip skill artifacts.** Remove numbered finding tags, phase headers, registry formatting — anything that signals "this used a skill." The judge should evaluate substance only [H49].

**Pairwise comparison (supplementary):**
```
Here are two responses to the same question. Which is better
on [dimension]? Respond with only "A" or "B" and one sentence why.

Response A: [randomly assigned skill or control]
Response B: [the other]
```

Randomize A/B assignment to control for position bias.

### Step 7: Human Validation Subset (Day 3, 2-3 hours)

Randomly select 20% of task-condition pairs (about 40 evaluations).
- Blind: you don't know which is skill vs. control.
- Score on the same rubric.
- Compare your scores to the LLM judge's scores.

**If human-LLM agreement > 70%:** LLM judge results are trustworthy enough for the full dataset.
**If human-LLM agreement < 70%:** LLM judge is unreliable; expand human evaluation or revise judge prompt.

### Step 8: Analyze Results (Day 3-4)

**Primary analysis:**
```
For each skill:
  mean_skill_score = average across tasks, trials, dimensions
  mean_controlC_score = average for Control-C
  delta = mean_skill_score - mean_controlC_score
  effect_size = delta / pooled_std_dev  (Cohen's d)
  p_value = paired_test(skill_scores, controlC_scores)
```

**Interpretation framework:**
| Effect size (d) | Delta | Interpretation |
|-----------------|-------|----------------|
| d > 0.8 | Large | Skill clearly adds value over good prompting |
| 0.5 < d < 0.8 | Medium | Skill adds value; worth keeping |
| 0.2 < d < 0.5 | Small | Marginal value; consider simplifying the skill |
| d < 0.2 | Negligible | Skill doesn't beat a good prompt |
| d < 0 | Negative | Skill is actively harmful — investigate |

**Secondary analyses:**
- Skill vs. Control-A (does any structure help?)
- Skill vs. Control-B (does specific structure beat general "think carefully"?)
- Per-dimension breakdown (where exactly does the skill help?)
- Sweet-spot vs. edge vs. negative-control (does the skill know its limits?)
- Variance analysis (does the skill reduce output variance, even if mean is similar?)

### Step 9: Coverage Analysis (Day 4, supplementary)

For decision and analysis skills, run a separate coverage check [H31]:

1. For each task, collect the union of all considerations mentioned across all conditions and trials.
2. Have a judge (LLM or human) rate each consideration as relevant (1) or tangential (0).
3. For each condition, calculate: relevant considerations surfaced / total relevant considerations.

**This captures "did the skill make you think of things you'd otherwise miss?" — which output quality scores may not reflect.**

---

## What This Protocol Cannot Measure [H88]

- **Process value**: If a skill helps a human user think through a problem (not just generates better LLM output), this test doesn't capture it.
- **Learning effects**: A user who internalizes a skill's procedure may become a better thinker. That's not measurable in an output comparison.
- **Conversation dynamics**: Skills that work through multi-turn dialogue (asking clarifying questions, routing to sub-skills) lose their advantage in a single-shot test.
- **Novel situations**: Tasks in the test bank are pre-defined. The skill's value on genuinely novel problems — where having a procedure matters most — is undertested.

These are real limitations. The protocol measures **LLM output quality improvement from structured procedures**, which is a meaningful but incomplete proxy for **total value of the skill**.

---

## First Concrete Steps

1. **Today: Pick 10 skills and write 50 tasks.** This is the foundation. Everything else depends on having good tasks. Spend the most time on Control-C prompts — they are the actual test.

2. **Tomorrow: Write the automation script and run generation.** 600 API calls. Estimate cost and ensure budget covers it. Save all outputs with metadata.

3. **Day 3: Run LLM-as-judge evaluation, then blind-evaluate a 20% human subset.** Compare human vs. LLM agreement before trusting the LLM scores.

4. **Day 4: Analyze and interpret.** Calculate effect sizes. Identify which skills beat Control-C, which don't, and on which dimensions.

5. **Day 5: Act on results.** Skills with d > 0.5 are validated. Skills with d < 0.2 are candidates for simplification or removal. Skills with high variance are candidates for procedural tightening.

---

## What Could Go Wrong

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| Control-C is too weak (straw man), inflating skill value | High | Have someone else write Control-C, or use multiple variants |
| Control-C is too strong (contains the skill's insight), deflating skill value | Medium | Control-C should capture intent, not procedure. Check that it doesn't replicate the skill's specific steps. |
| LLM judge rewards structure/verbosity, biasing toward skills | High | Strip formatting artifacts; include signal-to-noise dimension; validate against human subset |
| Sample tasks don't represent real use cases | Medium | Include tasks from actual user scenarios if available; vary difficulty and domain |
| Results are inconclusive (small effects, high variance) | Medium | Increase N per task (5 runs instead of 3) or focus on fewer skills with more tasks each |
| Rubric dimensions don't capture what actually matters | Medium | Pilot with 2-3 tasks first; revise rubric before full run |

---

## Fallback If Primary Method Doesn't Work

If the hybrid protocol is too complex or results are uninterpretable:

**Simplified alternative:** Pick your 3 best skills and 3 worst skills (by your intuition). Run each on 10 tasks, skill vs. Control-C only, single trial. Do blind pairwise preference (just "which is better?", no rubric). If you can't distinguish best-skills from Control-C in blind comparison, the skills likely aren't adding measurable value. If you can, the full protocol is worth running to quantify it.

This takes a few hours instead of a few days and gives a quick go/no-go signal.

---

## Follow-Up Routing

After running the protocol, you may need:
- **"What do I do with the results?"** → /action (execute on findings)
- **"Some skills scored poorly — why?"** → /rca (root cause analysis on weak skills)
- **"How do I improve the skills that underperformed?"** → /imps (improve specific skill)
- **"What if the whole approach is wrong?"** → /aw (assume wrong on the skill format)
- **"What's left to figure out?"** → /tbd (surface remaining open questions)

---

## Pre-Completion Checklist

- [x] Goal stated clearly: test whether skills produce measurably better outputs than unstructured prompting
- [x] Complexity assessed: multi-step method requiring experimental design
- [x] Constraints surfaced: solo dev, API costs, 592 skills, time pressure, no baseline data
- [x] Multiple methods considered: 6 methods mapped and tested via AR/AW
- [x] Best method selected with rationale: hybrid protocol with marginal value framing, because no single method covers all validity threats
- [x] Concrete first steps specified: 5 steps across 5 days
- [x] Prerequisites identified: rubrics (unmet, must create), judge model (met), task bank (unmet, must create)
- [x] What could go wrong noted: 6 risks with mitigations

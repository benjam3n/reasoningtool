# /vbo Before claiming "reasoningtool makes thinking better," what evidence actually supports this?
**Date:** 2026-03-09
**Skill:** /vbo (Verification Before Output)

---

**Interpretation selected:** Interpretation 2 — Audit a claim before acting on it. The claim under audit is: "reasoningtool makes thinking better." We apply VBO to every sub-claim that would need to be true for this to hold.

---

## Step 1: Identify All Claims

The master claim "reasoningtool makes thinking better" decomposes into the following sub-claims that would all need to be true (or mostly true) for the master claim to hold:

| # | Claim | Type |
|---|-------|------|
| C1 | Structured procedures improve thinking outcomes compared to unstructured thinking | Causal |
| C2 | LLMs following structured procedures produce better outputs than LLMs without them | Causal |
| C3 | The specific procedures in reasoningtool are well-designed (correct steps, right order, nothing missing) | Quality assertion |
| C4 | Users who adopt reasoningtool produce better decisions/analyses than they did before | Causal (before/after) |
| C5 | 592 skills represent adequate coverage of thinking tasks | Completeness assertion |
| C6 | The routing system (/claim, /decide, etc.) directs users to the right skill | Procedural claim |
| C7 | Skills compose correctly when chaining (INVOKE) | Procedural claim |
| C8 | "Better thinking" is a meaningful, measurable outcome | Definitional claim |
| C9 | The toolkit outperforms simply prompting Claude directly (without skills) | Comparative claim |
| C10 | Users can discover and invoke the right skill for their problem | Usability claim |

---

## Step 2: Attempt Verification — OBSERVED

**C1: Structured procedures improve thinking outcomes**
- There is a large body of published research on structured decision-making (checklists in medicine, structured analytic techniques in intelligence, pre-mortem in project management).
- **[O: External literature]** — Heuer & Pherson's SATs, Gawande's checklist research, Kahneman's debiasing work demonstrate that structured procedures reduce specific error types in specific contexts.
- **Critical caveat:** The literature shows structured procedures help *for specific tasks in specific conditions*, not universally. The claim as stated ("makes thinking better" in general) is broader than what the literature supports. Furthermore, this literature covers *humans* following procedures, not *LLMs executing procedures on behalf of humans* — the transfer is unverified.

**C2: LLMs following structured procedures produce better outputs**
- There is research on prompt engineering showing that structured prompts (chain-of-thought, tree-of-thought) improve LLM performance on reasoning benchmarks.
- **[O: External literature, partial]** — Research on CoT prompting (Wei et al., 2022) and Tree of Thoughts (Yao et al., 2023) demonstrates measurable improvements on specific benchmark tasks.
- **Caveat:** No published study has tested reasoningtool's specific procedure format against baselines. Also, LLMs have different failure modes than humans — the procedures may address biases LLMs don't have while missing failure modes they do have.

**C3: The specific procedures in reasoningtool are well-designed**
- The skills exist in the codebase (592 directories). Their content can be read.
- No external review, peer assessment, or expert audit of skill quality has been documented.
- **NOT OBSERVED.** Move to next step.

**C4: Users produce better outcomes with reasoningtool**
- No user studies, testimonials, case studies, or usage data have been documented.
- No analytics, feedback forms, or user interviews are referenced.
- **NOT OBSERVED.** Move to next step.

**C5: 592 skills represent adequate coverage**
- The skills directory contains ~592 entries. [O: Codebase inspection]
- Whether this constitutes "adequate coverage" cannot be observed without a defined universe of thinking tasks to cover.
- **PARTIALLY OBSERVED** (count confirmed; adequacy unresolved). Move to next step.

**C6: Routing directs users to the right skill**
- The routing skills (/claim, /decide, /search, etc.) exist and contain classification logic. [O: Codebase inspection]
- Whether they *correctly* route in practice has not been observed with real users.
- **PARTIALLY OBSERVED** (existence confirmed; correctness unresolved). Move to next step.

**C7: Skill chains work correctly**
- INVOKE directives exist in multiple skills. [O: Codebase inspection]
- Whether chains execute correctly end-to-end has not been systematically observed.
- **PARTIALLY OBSERVED** (existence confirmed; correctness unresolved). Move to next step.

**C8: "Better thinking" is a meaningful, measurable outcome**
- The project does not define what "better thinking" means operationally — no metrics, no rubric, no before/after measurement protocol exists in the repository.
- **NOT OBSERVED.** Move to DERIVED.

**C9: Better than just prompting Claude directly**
- No comparative studies. No A/B testing of skill-mediated vs. direct prompting.
- **NOT OBSERVED.** Move to next step.

**C10: Users can discover and invoke the right skill**
- No user data exists. No usability testing. No observation of real users attempting discovery.
- **NOT OBSERVED.** Move to next step.

### Step 2 Summary

| Claim | Status |
|-------|--------|
| C1 | [O: External literature] — Partial. Supports structured procedures for specific tasks; does not generalize universally or to LLM-mediated contexts. |
| C2 | [O: External literature, partial] — CoT/ToT research supports structured prompting on benchmarks; does not validate this specific toolkit. |
| C3 | Unresolved |
| C4 | Unresolved |
| C5 | Partially observed (count confirmed; adequacy unresolved) |
| C6 | Partially observed (existence confirmed; correctness unresolved) |
| C7 | Partially observed (existence confirmed; correctness unresolved) |
| C8 | Unresolved |
| C9 | Unresolved |
| C10 | Unresolved |

---

## Step 3: Attempt Verification — TESTED

**C3: The specific procedures are well-designed**
- Individual skills could be tested by running them on known inputs and evaluating output quality against a rubric. This has not been done systematically.
- The current prompt series (prompts-2026-03-09) constitutes an informal test — the author is running skills and inspecting outputs. But there is no control condition, no scoring rubric, and no systematic comparison.
- **[UNTESTED]** — No formal test exists.

**C4: Users produce better outcomes with reasoningtool**
- Would require a controlled study: users solving problems with and without the toolkit, with blind evaluation of output quality. No such test has been conducted.
- **[UNTESTED]**

**C5: Coverage is adequate**
- Could be tested by mapping skills against a taxonomy of thinking tasks and checking for gaps. The /skgap skill exists for this purpose, and prompt #21 attempts this — but no definitive coverage metric has been established.
- **[UNTESTED]** — Partial exploration exists but no systematic test.

**C6: Routing works correctly**
- Could be tested by running diverse inputs through routing skills and checking whether they land on appropriate analysis skills. No such test suite exists.
- **[UNTESTED]**

**C7: Skill chains work correctly**
- Could be tested by executing multi-skill chains and verifying coherent end-to-end output. No systematic chain testing exists.
- Skills do execute when invoked (observed in this and prior sessions) — this is an existence proof that they run, but not a quality test.
- **[T: N=unknown, skills execute and produce structured output — but no quality measurement]**

**C9: Better than direct prompting**
- Would require a controlled comparison: same problems, same LLM, with and without skill procedures, blind evaluation of outputs. No such comparison exists.
- **[UNTESTED]**

**C10: Users can discover the right skill**
- Would require usability testing with real users. None conducted.
- **[UNTESTED]**

---

## Step 4: Attempt Verification — DERIVED

**C3: Procedures are well-designed**
- Premise A: The procedures are based on recognized analytical techniques (RCA, pre-mortem, CBA, structured analytic techniques). [O: Codebase inspection confirms skill names and methods map to established techniques]
- Premise B: Recognized analytical techniques have evidence bases in their source domains. [O: External literature]
- Conclusion: The *source techniques* are well-designed; the *specific implementations* in reasoningtool may or may not faithfully represent them.
- **[D: Partial]** — The derivation holds for "the techniques these skills are based on have evidence" but NOT for "these specific implementations of those techniques are correct." The gap between a known technique and its SKILL.md implementation is unverified.

**C8: "Better thinking" is measurable**
- Premise A: Thinking produces outputs (decisions, analyses, plans, diagnoses). [O: Definitional]
- Premise B: Outputs can be evaluated on dimensions like accuracy, completeness, consideration of alternatives, identification of risks, and logical validity. [O: Established in decision science literature]
- Conclusion: "Better thinking" can be operationalized as "outputs that score higher on defined quality dimensions."
- **[D: Premises A + B → "better thinking" is measurable IF you define the dimensions and measurement method]**
- However: reasoningtool has NOT defined these dimensions or created a measurement method. The concept is derivable; the measurement does not exist.

**C1 (revisited): Does the transfer from human cognition to LLM-mediated cognition hold?**
- Premise A: Structured procedures improve human thinking outcomes [O: Published research]
- Premise B: LLMs follow instructions more consistently with structured prompts [O: Prompt engineering literature]
- Attempted conclusion: Therefore, structured procedures executed by LLMs should improve thinking outcomes.
- **DERIVATION INVALID.** Human thinking benefits from procedures because humans are prone to cognitive biases (anchoring, availability, confirmation bias) that procedures counteract. LLMs have different failure modes (hallucination, sycophancy, context window limits, inconsistent reasoning). The procedures may address biases LLMs don't have while missing failure modes they do have. Premises do not support the conclusion for this specific context.

---

## Step 5: Exclude Unverifiable Claims

| Claim | Verdict | Action |
|-------|---------|--------|
| C1 | [O: External literature] | **INCLUDE with narrowing** — Literature supports structured procedures for specific human thinking tasks; transfer to LLM-mediated context is unverified |
| C2 | [O: External literature, partial] | **INCLUDE with narrowing** — CoT research supports structured prompting on benchmarks; does not validate this specific toolkit |
| C3 | [D: Partial] | **MARK AS UNKNOWN** — Source techniques have evidence; these specific implementations are unverified |
| C4 | [UNTESTED] | **MARK AS UNKNOWN** — No user outcome data exists |
| C5 | [UNTESTED] | **MARK AS UNKNOWN** — Coverage not systematically assessed |
| C6 | [UNTESTED] | **MARK AS UNKNOWN** — Routing accuracy not tested |
| C7 | [T: Partial] | **INCLUDE with narrowing** — Skills execute; output quality unknown |
| C8 | [D: Conditional] | **MARK AS UNKNOWN** — Measurable in principle; not operationalized |
| C9 | [UNTESTED] | **MARK AS UNKNOWN** — No comparative data whatsoever |
| C10 | [UNTESTED] | **MARK AS UNKNOWN** — No usability data |

---

## Step 6: Verify Verification

**[O: External literature] on C1:**
- Source: Structured analytic techniques literature (Heuer & Pherson, 2010), checklist research (Gawande, 2009), debiasing research (Kahneman, 2011). Well-established, widely cited works.
- Observation method: Published peer-reviewed and practitioner literature.
- **PASS**

**[O: External literature, partial] on C2:**
- Source: Chain-of-thought prompting research (Wei et al., 2022), Tree of Thoughts (Yao et al., 2023).
- Observation method: Published ML research with benchmark evaluations.
- Limitation documented: These test general structured prompting, not reasoningtool's specific format.
- **PASS** (with documented limitation)

**[D: Partial] on C3:**
- Premises verified: Skill names do map to known techniques (observable in codebase). Known techniques do have evidence bases (observable in literature).
- Gap documented: Implementation fidelity is the unverified link.
- **PASS** (with documented gap)

**[D: Conditional] on C8:**
- Premises verified: Definitional and literature-based.
- Gap documented: No operationalization exists in the project.
- **PASS** (with documented gap)

**[T: Partial] on C7:**
- Test: Skills have been invoked in current and prior sessions and produce output.
- Limitation: "Produces output" is not "produces good output." Quality unmeasured.
- **PASS** (with documented limitation)

All markers have documentation. Verification is verified.

---

## VERIFIED CLAIMS

1. **Structured procedures improve specific thinking tasks in specific contexts.** [O: External literature — Heuer & Pherson (2010), Gawande (2009), Kahneman (2011)] This is well-established for checklists in surgery, structured analytic techniques in intelligence analysis, and debiasing protocols in decision-making. It does NOT generalize to "all thinking" or "any procedure," and it does NOT automatically transfer to LLM-mediated contexts.

2. **Structured prompting improves LLM performance on reasoning benchmarks.** [O: External literature — Wei et al. (2022), Yao et al. (2023)] Chain-of-thought and tree-of-thought prompting demonstrate measurable gains. This does NOT validate reasoningtool's specific procedure format or the 592 specific skills.

3. **Many reasoningtool skills are based on recognized analytical techniques.** [D: Codebase inspection + external literature] Skills like /rca (root cause analysis), /prm (pre-mortem), /cba (cost-benefit analysis), /ht (hypothesis testing) map to techniques with independent evidence bases. The specific SKILL.md implementations have not been validated as faithful representations.

4. **"Better thinking" is measurable in principle.** [D: Decision science literature + definitional analysis] Thinking outputs can be scored on accuracy, completeness, logical validity, consideration of alternatives, and risk identification. However, reasoningtool has not defined or implemented any such measurement.

5. **The toolkit exists and skills execute.** [O: Codebase observation; T: Observed in current and prior sessions] ~592 structured skill procedures exist and produce structured output when invoked via Claude Code. Output quality is unmeasured.

---

## UNKNOWN

1. **Whether reasoningtool's specific implementations are faithful to their source techniques.** The gap between "RCA is a proven technique" and "this SKILL.md file correctly implements RCA" is unverified. No expert review, no fidelity assessment.

2. **Whether any user has achieved better outcomes using reasoningtool.** Zero user outcome data. No case studies, no before/after comparisons, no testimonials, no usage analytics.

3. **Whether the routing system correctly matches problems to skills.** No test suite, no user journey data, no accuracy measurement.

4. **Whether skill chains produce coherent end-to-end results.** No systematic chain testing.

5. **Whether 592 skills is the right number, too many, or too few.** No coverage analysis against a defined universe of thinking tasks. No evidence that quantity helps rather than hinders.

6. **What "better thinking" means operationally for this project.** No defined metrics, no rubric, no measurement protocol.

7. **Whether the toolkit outperforms simply prompting Claude directly.** No comparative data. This is perhaps the most important unknown — if the same LLM produces equally good output without the skill procedures, the toolkit adds complexity without value.

8. **Whether users can discover and navigate the toolkit effectively.** No usability data of any kind.

9. **Whether the toolkit causes any harm** (e.g., false confidence from following a procedure, analysis paralysis from too many options, degraded thinking from over-reliance on external structure). This is not just unknown — it is uninvestigated.

10. **Whether the transfer from human-cognition research to LLM-mediated cognition is valid.** LLMs have different failure modes than humans. Procedures designed to counteract human cognitive biases may not address LLM-specific failure modes (hallucination, sycophancy, context window limits).

---

## DEFAULTS

None used. No defaults were needed for this analysis.

---

## EXCLUDED

The following claims were considered but excluded because they cannot be verified:

1. **"Users find the skills helpful"** — No user feedback data exists. Cannot be stated or denied.
2. **"The toolkit is comprehensive"** — No completeness benchmark exists. The number 592 is a count, not a coverage metric.
3. **"Skills are high quality"** — No quality rubric has been applied. The author's informal testing is not a systematic quality assessment.
4. **"Structured procedures always help"** — Literature shows they help in specific contexts and can *hurt* in others (e.g., over-proceduralization of creative tasks, false precision in ambiguous domains).
5. **"Better than just asking Claude"** — No comparative data exists. This claim is simply unavailable.

---

## Step 7: Specificity Check for Capability Claims

The master claim "reasoningtool makes thinking better" is a capability claim. Applying the specificity gate:

| Element | Present? | Status |
|---------|----------|--------|
| **TRIGGER** — What causes better thinking to happen? | No | Is it invoking any skill? The right skill? Following the output? Reflecting on it? For which problem types? |
| **PROCEDURE** — What exact steps produce the improvement? | Partial | Individual skills have steps, but the causal pathway from "follow these steps" to "thinking improves" is unspecified |
| **OUTPUT** — What concrete result demonstrates improvement? | No | No defined output metric, no quality indicator, no definition of "better" |
| **VALIDATION** — How do we know it worked? | No | No measurement protocol, no before/after comparison method, no success criteria |

**Result: BLOCKED.** The capability claim "reasoningtool makes thinking better" fails the specificity gate on 3 of 4 elements.

### Questions that would need answers before this claim can be unblocked:

1. **Trigger:** For which specific thinking tasks does reasoningtool improve outcomes? (Not "all thinking" — which specific types, for which users, under what conditions?)
2. **Procedure:** What is the mechanism? (User invokes skill → LLM follows procedure → output differs from unstructured response how, exactly? And why does that difference constitute improvement?)
3. **Output:** What does "better" look like concretely? (Fewer logical errors? More alternatives considered? Faster convergence on good decisions? More accurate risk identification? Reduced regret?)
4. **Validation:** How would you measure it? (Blind evaluation of outputs? Decision outcome tracking? Error rate comparison? User self-report?)

---

## Summary Verdict

**What can be honestly said (verified):**
- A toolkit of ~592 structured thinking procedures exists and executes via Claude Code
- The general principle that structured procedures aid specific human thinking tasks has research support
- Many skills are based on recognized analytical techniques with independent evidence bases
- "Better thinking" could be measured — but hasn't been

**What cannot be honestly said (unverified):**
- That it makes thinking better (undefined, untested)
- That it works better than alternatives (no comparative data)
- That it works better than just asking Claude without skills (no comparative data)
- That users benefit from it (no user data)
- That the procedures are well-designed (no quality audit)
- That the scale (592 skills) is an advantage (no evidence)
- That the transfer from human-cognition research applies here (different failure modes)

**The honest position is:** "We built a large collection of structured thinking procedures based on recognized analytical techniques, executable via LLM. We believe, based on analogies to human-cognition and prompt-engineering research, that they may improve thinking outcomes for specific task types. We have no evidence yet that they do. The most important thing we haven't done is test this."

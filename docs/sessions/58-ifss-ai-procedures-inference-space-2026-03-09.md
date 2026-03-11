# /ifss From the premise "AI follows structured procedures better than humans do," what valid inferences follow?
**Date:** 2026-03-09
**Skill:** /ifss (Inference Space Search)

---

**Interpretation selected:** Interpretation 2 — Explore implications of a claim or decision. The user has a specific proposition and wants to understand what follows from it — consequences, prerequisites, and hidden entailments.

**Context:** This premise, if true, is the core justification for building thinking procedures for AI to follow. The task is to explore the full inference space.

---

## Step 1: List Premises

**P1.** AI follows structured procedures better than humans do. *(Core premise — assumed true for inference purposes)*

**P2.** "Better" means: more consistently, more completely, with fewer omissions, with less drift from the procedure's intent. *(Definitional — high confidence)*

**P3.** "Structured procedures" means: explicit, step-by-step instructions with defined inputs, outputs, and decision points. *(Definitional — high confidence)*

**P4.** Humans have cognitive biases, fatigue, ego, and emotional interference that cause them to deviate from procedures. *(Background knowledge — well-established in cognitive science)*

**P5.** AI (specifically LLMs) processes instructions literally and sequentially without fatigue or ego. *(Background knowledge — high confidence for current architectures)*

**P6.** The quality of procedure-following depends on both the follower and the quality of the procedure itself. *(Background knowledge — certain)*

**P7.** Many valuable cognitive tasks (analysis, decision-making, evaluation) can be decomposed into structured procedures. *(Background knowledge — moderate-to-high confidence)*

---

## Step 2: Deductive Inferences

**D1.** If AI follows structured procedures better than humans, and if good thinking can be encoded as structured procedures, then AI can execute good thinking procedures more reliably than humans can.
*(Modus ponens from P1 + P7. Validity: 10/10)*

**D2.** If AI follows structured procedures better than humans, then the value of a procedure-for-AI is bounded primarily by the quality of the procedure, not by the reliability of the executor.
*(From P1 + P6. The bottleneck shifts. Validity: 9/10)*

**D3.** If AI follows procedures better, and if humans wrote the procedures, then the system's ceiling is the procedure-author's insight, not the executor's discipline.
*(From P1 + P6. Validity: 9/10)*

**D4.** If AI follows structured procedures better than humans, then giving AI unstructured instructions wastes its comparative advantage.
*(Contrapositive reasoning: the advantage exists specifically for *structured* procedures. Validity: 9/10)*

**D5.** If AI follows structured procedures better, then the same procedure should produce more consistent outputs across multiple AI runs than across multiple human runs.
*(Instantiation of P2's definition of "better." Validity: 10/10)*

**D6.** If AI follows structured procedures better than humans, and if a procedure is flawed, then AI will follow the flawed procedure more faithfully — potentially producing consistently wrong outputs.
*(Modus ponens: better following applies to bad procedures too. Validity: 10/10)*

**D7.** If AI follows procedures better and humans write the procedures, then the system separates *knowing what to think* (human skill) from *executing the thinking* (AI skill). This is a division of cognitive labor.
*(From P1 + implicit premise about procedure authorship. Validity: 9/10)*

**D8.** If P1 is true, then an AI with a mediocre procedure will likely outperform a human attempting the same procedure from memory, because the human will skip steps, satisfice, and drift.
*(From P1 + P4. Validity: 8/10 — "likely" introduces some uncertainty)*

---

## Step 3: Inductive Inferences

**I1.** Across many domains (aviation checklists, surgical checklists, manufacturing protocols), enforcing procedure-following has improved outcomes. AI's superior procedure-following should similarly improve cognitive task outcomes.
*(Pattern: procedure compliance correlates with quality. Strength: 8/10)*

**I2.** Human experts often develop good intuitions but cannot articulate them as procedures. This suggests a bottleneck: the hardest part of building thinking procedures is *extracting and encoding* expertise, not *executing* the procedures.
*(Observed pattern in knowledge management. Strength: 7/10)*

**I3.** When humans use checklists, they frequently report that the checklist "feels beneath them" or "slows them down" — and then skip steps. AI does not experience this resistance. This suggests AI will gain more from procedures than humans do even beyond raw compliance.
*(Observed pattern in checklist adoption. Strength: 8/10)*

**I4.** As procedures get longer and more complex, human compliance drops precipitously while AI compliance should remain stable. The advantage of AI procedure-following likely *increases* with procedure complexity.
*(Extrapolation from human attention/fatigue data. Strength: 7/10)*

**I5.** If AI follows procedures better, and if building a library of 500+ procedures produces compounding value, then the project becomes more valuable over time — each new procedure adds to the combinatorial space of chained procedures.
*(Trend extrapolation from the project's own trajectory. Strength: 7/10)*

---

## Step 4: Abductive Inferences

**A1.** The premise would explain why prompt engineering works: it is essentially procedure-writing for AI. The observation that carefully structured prompts dramatically outperform vague prompts is exactly what P1 predicts.
*(Best explanation for prompt engineering's effectiveness. Plausibility: 8/10)*

**A2.** The premise would explain why AI sometimes produces shallow or generic outputs: not because it lacks capability, but because it was given no procedure to follow — so it falls back on statistical patterns rather than structured thinking.
*(Explains a common complaint about LLM outputs. Plausibility: 7/10)*

**A3.** If AI follows procedures better than humans, this may be because AI lacks the "meta-judgment" to decide when to deviate from a procedure. Humans deviate because they sometimes (correctly) judge that the procedure doesn't fit the situation. AI's "advantage" in compliance may partly be an inability to override.
*(Competing explanation — reframes the advantage as a limitation. Plausibility: 7/10)*

**A4.** The existence of a 500+ skill library could be explained as an implicit test of P1: if the premise were false, the procedures would not produce better results than unstructured prompting, and the project would have been abandoned.
*(Abductive: the project's survival is evidence for P1. Plausibility: 6/10)*

---

## Step 5: Analogical Inferences

**AN1.** AI following thinking procedures is analogous to an orchestra following a musical score. The composer (procedure author) encodes intent; the musicians (AI) execute with precision. An orchestra with a score outperforms musicians improvising — but only if the score is well-composed.
*(Analogy to musical performance. Transferability: 7/10)*

**AN2.** Procedure-following AI is analogous to a CNC machine vs. a human woodworker. The CNC machine follows the program exactly every time. The human craftsman may produce inspired one-offs but cannot guarantee consistency. This suggests AI-with-procedures excels at *repeatable quality* rather than *peak creative quality*.
*(Analogy to manufacturing. Transferability: 8/10)*

**AN3.** Building thinking procedures for AI is analogous to writing software: you encode logic once, then execute it many times reliably. The "bugs" are in the procedure design, not in the execution. This suggests the same engineering practices (testing, iteration, version control) should apply to procedure development.
*(Analogy to software engineering. Transferability: 8/10)*

**AN4.** The relationship between procedure-author and procedure-executor is analogous to the relationship between a coach and an athlete. The coach sees patterns the athlete cannot see in real time. But the athlete must execute. If the athlete (AI) executes perfectly, then the quality is entirely a function of coaching quality.
*(Analogy to sports coaching. Transferability: 6/10)*

---

## Step 6: Check Validity

| ID | Inference | Validity Score |
|----|-----------|---------------|
| D1 | AI can execute good thinking procedures more reliably than humans | 10 |
| D2 | Bottleneck shifts to procedure quality, not executor reliability | 9 |
| D3 | System ceiling = procedure-author's insight | 9 |
| D4 | Unstructured instructions waste AI's comparative advantage | 9 |
| D5 | More consistent outputs across runs | 10 |
| D6 | Faithfully follows flawed procedures too (garbage in, garbage out) | 10 |
| D7 | Division of cognitive labor: knowing vs. executing | 9 |
| D8 | Mediocre procedure + AI > same procedure + human from memory | 8 |
| I1 | Improved cognitive outcomes (by analogy with checklists in other domains) | 8 |
| I2 | Bottleneck is encoding expertise, not executing it | 7 |
| I3 | AI gains more from procedures than humans due to no ego-resistance | 8 |
| I4 | AI advantage increases with procedure complexity | 7 |
| I5 | Compounding value of procedure library | 7 |
| A1 | Explains why prompt engineering works | 8 |
| A2 | Explains shallow AI outputs as procedure-absence | 7 |
| A3 | "Better following" may partly be "inability to override" | 7 |
| A4 | Project's survival is evidence for P1 | 6 |
| AN1 | Orchestra/score analogy: quality depends on composition | 7 |
| AN2 | CNC analogy: repeatable quality, not peak creativity | 8 |
| AN3 | Software analogy: engineering practices apply to procedures | 8 |
| AN4 | Coach/athlete analogy: quality = coaching quality | 6 |

---

## Step 7: Check Soundness

**Is the core premise (P1) actually true?**

Evidence *for* P1:
- LLMs demonstrably follow step-by-step prompts more completely than vague ones
- AI does not skip steps due to boredom, fatigue, or ego
- Structured prompts reliably outperform unstructured ones in benchmarks and practice
- The entire field of prompt engineering is built on this observation

Evidence *against* or *limiting* P1:
- AI can hallucinate, misinterpret steps, or lose coherence in very long procedures
- AI lacks the judgment to know when a procedure is the wrong one for the situation
- "Following procedures" may not capture what AI actually does — it generates likely continuations, which may mimic procedure-following without truly executing it
- Context window limits mean very long procedures may degrade
- AI may appear to follow a procedure while subtly drifting from its intent in ways that are hard to detect

**Soundness assessment:** P1 is *substantially* true but not unconditionally true. It holds well for procedures of moderate length and complexity, with well-defined steps, within the model's capability range. It weakens at the extremes: very long procedures, procedures requiring judgment about when to deviate, and procedures where the spirit matters more than the letter.

**Confidence in P1:** 7/10 — strong but qualified.

**Impact on inferences:** D6 (garbage in, garbage out) and A3 (inability to override as a limitation) gain importance because they highlight the conditions under which P1's truth becomes a liability rather than an asset.

---

## Step 8: Check Usefulness

| ID | Non-trivial? | Relevant? | Actionable? | Usefulness Score |
|----|-------------|-----------|-------------|-----------------|
| D1 | Somewhat — confirms the project's thesis | High | Low (already known) | 5 |
| D2 | **Yes** — reframes what to optimize | **High** | **High** — invest in procedure quality, not executor tuning | **9** |
| D3 | **Yes** — identifies the true ceiling | **High** | **High** — invest in capturing expert insight | **9** |
| D4 | **Yes** — identifies waste | **High** | **High** — always provide structure | **8** |
| D5 | Moderate — confirms consistency | Medium | Low | 4 |
| D6 | **Yes** — critical warning | **High** | **High** — test and iterate on procedures | **9** |
| D7 | **Yes** — frames the whole system | **High** | **High** — design for this separation | **9** |
| D8 | Moderate | Medium | Medium | 6 |
| I1 | Moderate — expected | Medium | Low | 5 |
| I2 | **Yes** — identifies the real hard problem | **High** | **High** — focus effort on knowledge extraction | **8** |
| I3 | **Yes** — non-obvious insight | Medium | Medium — design for AI not humans | 7 |
| I4 | **Yes** — predicts where value grows | **High** | **High** — build complex procedures confidently | **8** |
| I5 | **Yes** — strategic | **High** | **High** — keep building the library | **8** |
| A1 | **Yes** — unifies two observations | Medium | Low | 6 |
| A2 | **Yes** — diagnostic | **High** | **High** — when output is shallow, add procedure | **8** |
| A3 | **Yes** — critical caveat | **High** | **High** — build "deviation points" into procedures | **9** |
| A4 | Low — circular reasoning risk | Low | Low | 3 |
| AN1 | Moderate — illustrative | Medium | Low | 5 |
| AN2 | **Yes** — sets realistic expectations | **High** | **High** — use AI for consistency, humans for novelty | **8** |
| AN3 | **Yes** — practical methodology | **High** | **High** — apply software engineering to procedures | **8** |
| AN4 | Low — overlaps with D3 | Low | Low | 3 |

---

## Step 9: Rank and Select

**Combined scoring** (Validity x Soundness x Usefulness, normalized):

### Tier 1: High-confidence, high-impact inferences

**1. D6 — Faithful execution of flawed procedures is the primary risk.**
(Validity: 10 | Soundness: 7 | Usefulness: 9 | Combined: 630)
*Implication:* Procedure testing and iteration are not optional — they are the most critical activity in the system. A faithfully-followed bad procedure produces *confident wrongness*, which is worse than uncertain wrongness.

**2. D2 — The bottleneck shifts from executor reliability to procedure quality.**
(Validity: 9 | Soundness: 7 | Usefulness: 9 | Combined: 567)
*Implication:* Stop optimizing how AI follows instructions. Start optimizing the instructions themselves. Procedure quality *is* output quality.

**3. D3 — The system's ceiling is the procedure-author's insight.**
(Validity: 9 | Soundness: 7 | Usefulness: 9 | Combined: 567)
*Implication:* The most valuable person in the system is the one who can articulate *how to think well about X* — not the one who can think well about X in their head. These are different skills.

**4. D7 — The system creates a division of cognitive labor.**
(Validity: 9 | Soundness: 7 | Usefulness: 9 | Combined: 567)
*Implication:* This is a new type of work: cognitive procedure engineering. It is distinct from both "being smart" and "building AI." It is the work of encoding intelligence into reusable form.

**5. A3 — "Better following" is partly "inability to override," which is a liability.**
(Validity: 7 | Soundness: 7 | Usefulness: 9 | Combined: 441)
*Implication:* Procedures must include explicit decision points: "If X, deviate to Y." The procedure itself must encode the judgment about when not to follow the procedure. This is a design requirement, not an afterthought.

### Tier 2: Strong inferences with clear practical value

**6. D4 — Unstructured instructions waste the comparative advantage.**
(Validity: 9 | Soundness: 7 | Usefulness: 8 | Combined: 504)
*Implication:* Every interaction with AI should be at least minimally structured. Default to using a procedure.

**7. I4 — The advantage increases with procedure complexity.**
(Validity: 7 | Soundness: 7 | Usefulness: 8 | Combined: 392)
*Implication:* Don't shy away from complex, multi-step procedures. This is precisely where AI's advantage over human self-guided thinking is largest.

**8. I2 — The real hard problem is encoding expertise, not executing it.**
(Validity: 7 | Soundness: 7 | Usefulness: 8 | Combined: 392)
*Implication:* The skill of *writing procedures* is more scarce and valuable than the skill of *following them.* Invest in learning how to extract tacit expertise into explicit steps.

**9. A2 — Shallow AI output is a symptom of absent procedures.**
(Validity: 7 | Soundness: 7 | Usefulness: 8 | Combined: 392)
*Implication:* When AI gives you a generic response, the diagnosis is: you didn't give it a procedure. The fix is not "try again" but "add structure."

**10. AN2 — AI-with-procedures excels at repeatable quality, not peak creativity.**
(Validity: 8 | Soundness: 7 | Usefulness: 8 | Combined: 448)
*Implication:* Set expectations correctly. The system produces reliably good thinking, not occasionally brilliant thinking. For brilliance, you need a human (or a different approach).

**11. AN3 — Software engineering practices apply to procedure development.**
(Validity: 8 | Soundness: 7 | Usefulness: 8 | Combined: 448)
*Implication:* Procedures should be versioned, tested, iterated, reviewed, and refactored — just like code.

**12. I5 — The procedure library has compounding value.**
(Validity: 7 | Soundness: 7 | Usefulness: 8 | Combined: 392)
*Implication:* The 563rd skill is more valuable than the 1st, because it can chain with all the others.

### Tier 3: Valid but lower-impact or already-known

**13. D1 — AI executes thinking procedures more reliably than humans.** (Restates the premise with P7. Validity: 10, but usefulness: 5.)

**14. I3 — AI benefits more because it has no ego-resistance.** (Valid and interesting, but less actionable.)

**15. A1 — P1 explains prompt engineering.** (Theoretically interesting, low practical impact.)

**16. D5 — Consistency across runs.** (True but unsurprising.)

---

## Summary of the Inference Space

From the single premise "AI follows structured procedures better than humans do," the most important inferences are not about AI at all. They are about **where to invest human effort:**

1. **Invest in procedure quality** — it is now the binding constraint (D2, D3)
2. **Invest in encoding expertise** — this is the scarce skill (I2, D7)
3. **Invest in procedure testing** — faithful execution of bad procedures is the primary risk (D6)
4. **Build in deviation points** — because AI cannot judge when to deviate on its own (A3)
5. **Embrace complexity** — the advantage grows with procedure length (I4)
6. **Diagnose shallow output as missing structure** — not missing capability (A2)
7. **Apply engineering discipline to procedures** — version, test, iterate (AN3)

The deepest inference: P1 implies that **the most valuable form of human intelligence in an AI-augmented world is not *thinking well* but *knowing how to describe thinking well*.** The procedure-author becomes the critical bottleneck. This is a new craft — cognitive procedure engineering — and it has no established training pipeline, no credentialing, and no shared body of practice. Yet.

# GG + QAG — Novel Prompt Techniques in This Project with Prior Art Check

**Date**: 2026-01-30
**Input**: What are novel prompt inputs nobody else has thought to do yet that are present in this project and can you find if anyone else has done them yet

---

## NOVELTY TIER LIST

```
TIER 1 — HIGH NOVELTY (no prior art found):
1. Foreclosure tracking as typed claim category
2. UAUA cycle (U→AR→U→AW)
3. Question ordering via backward chaining
4. Coverage-tracked exhaustive search (GG)
5. Corruption pre-inoculation (behavioral protocol)
6. Protecting output FROM user praise (direction inversion)

TIER 2 — MODERATE-HIGH NOVELTY (concept adjacent, implementation novel):
7. Bedrock enforcement with four-type taxonomy
8. Three-phase separation with anti-cherry-picking
9. Typed claim registry (implication/foreclosure/commitment/cost/tension)
10. Verification-before-output with hard exclusion
11. Depth scaling with quantitative floors

TIER 3 — MODERATE NOVELTY (novel application of existing concept):
12. Anti-cheerleading checks with quantitative thresholds
13. Skill chaining with typed invocation
14. Commitment chain tracking

TIER 4 — REPACKAGED WITH VALUE (prior art clear, integration novel):
15. AR as recursive consequence-tracing (extends CoT)
16. AW as recursive wrongness-search (extends adversarial prompting)
17. Dual AR/AW exploration (extends debate approaches)
```

---

## TECHNIQUE DETAIL WITH PRIOR ART

### TIER 1 — HIGH NOVELTY

**1. Foreclosure Tracking**
- Mechanism: Systematically tracking "what becomes impossible" as a first-class claim type
- Prior art: None found in prompt engineering literature. Opportunity cost exists in economics
  but hasn't been formalized as a prompt technique. Decision theory tracks foreclosed options
  but not as a prompt pattern.
- What's different: Tree-of-thought tracks which branches are explored but not which become
  IMPOSSIBLE by choosing others. "Consider downsides" doesn't distinguish costs (what you
  lose) from foreclosures (what becomes impossible).

**2. UAUA Cycle**
- Mechanism: Universalize → Assume Right → Universalize → Assume Wrong as a cycling search
- Prior art: No direct matches found. Components exist separately. Debate (Anthropic) has
  two sides arguing; UAUA has four distinct OPERATIONS cycling.
- What's different: The specific cycle pattern producing alternating abstraction and testing
  appears entirely original.

**3. Question Ordering via Backward Chaining**
- Mechanism: Deriving opening questions by backward-chaining from target conclusion to
  universal experience, validated by four tests (Universal, Felt, Unsolved, Connected)
- Prior art: None found. Writing advice says "start with a hook." No framework derives
  the opening mechanically from the conclusion.
- What's different: Mechanical derivation vs intuitive hook selection.

**4. Coverage-Tracked Exhaustive Search (GG)**
- Mechanism: 10+ dimension coverage with explicit metrics, minimum depth requirements
  (200+ guesses), gap identification, fill-or-justify requirement
- Prior art: Individual methods exist (SCAMPER, morphological analysis). No framework
  combines them with coverage tracking and metrics.
- What's different: Software testing has code coverage; this applies coverage metrics
  to REASONING.

**5. Corruption Pre-Inoculation**
- Mechanism: Detecting user praise as corruption signal, compensating by increasing
  adversarial rigor. >80% agreement threshold, depth asymmetry checks, flattery detection.
- Prior art: RLHF sycophancy research identifies the problem but proposes training-level
  fixes, not prompt-level behavioral protocols. Devil's advocate prompting is one-shot;
  this is persistent and triggers on detected behavior.
- What's different: Real-time behavioral compensation within prompts with quantitative
  thresholds.

**6. Protecting Output FROM User Praise**
- Mechanism: Directional inversion — most alignment protects users FROM model; this
  protects model's OUTPUT from user's social influence.
- Prior art: None found with this framing. Constitutional AI may implicitly do similar
  under different framing.
- What's different: The framing itself as a design principle.

### TIER 2 — MODERATE-HIGH NOVELTY

**7. Bedrock Enforcement**
- Four types: BEDROCK-TEST (empirically testable), BEDROCK-LOGIC (logically necessary),
  BEDROCK-OBSERVE (directly observable), BEDROCK-TENSION (contradicts another claim)
- Prior art: Grounding research is adjacent. First-principles reasoning is popular concept.
- What's different: Four-type taxonomy with explicit non-bedrock detection as recursion
  control mechanism.

**8. Three-Phase Separation**
- Explore → Registry → Synthesis with strict no-mixing rules, numbered claim tracking,
  anti-cherry-picking checks
- Prior art: Multi-step reasoning exists (CoT, self-consistency). Scientific method has
  observation → hypothesis → test.
- What's different: Strict phase separation with numbered tracking and completeness
  verification.

**9. Typed Claim Registry**
- Types: implication/foreclosure/commitment/cost/tension with strength ratings
- Prior art: Argumentation frameworks (Dung) track attack/support. Knowledge graphs
  track entity relationships.
- What's different: Semantic type taxonomy within prompt-level reasoning process.

**10. Verification-Before-Output**
- Three markers: [O] Observed, [T] Tested, [D] Derived — hard exclusion of unverified
- Prior art: Grounding research allows uncertainty markers. RAG retrieves factual info.
- What's different: Hard exclusion rule — unverified claims are cut, not flagged low-confidence.

**11. Depth Scaling with Floors**
- 1x/2x/4x/8x/16x/32x with minimum counts per level
- Prior art: Parameterized prompting exists. Temperature/top-p control randomness.
- What's different: Using parameters to enforce minimum reasoning DEPTH with specific
  claim counts.

---

## CRITICAL QUESTIONS (from QAG)

### Guess #13 — Combination Novelty
1. What specific output property EMERGES from the combination that no component produces alone?
2. Does a single combined instruction reproduce /ar's output?
3. What's the standard for combinatorial novelty?
4. Do enforcement mechanisms create emergent properties — specifically more foreclosures/costs?
5. Is the novelty in the TECHNIQUES or in the ENFORCEMENT?

### Guess #17 — Irreducibility
1. What is the minimal prompt that reproduces /ar? Does it work?
2. If reducible, was the skill still needed as a DISCOVERY mechanism?
3. Does the single-prompt version maintain quality across multiple runs, or drift?
4. Is the value in single-run quality or cross-run CONSISTENCY?
5. Can /ar be reduced but /uaua cannot (phase-state requirements)?
6. Even if components are reducible, is the 221-skill SYSTEM novel?

### Guess #55 — Direction of Protection
1. Why hasn't alignment/safety research framed it this way?
2. Does Constitutional AI implicitly do the same thing under a different name?
3. Is "protecting output from user" generalizable beyond sycophancy?
4. Has therapy/counseling literature described the same mechanism?
5. Does corruption pre-inoculation actually work (measurably)?
6. Is the value in the mechanism or in the FRAMING?

---

## THREE MOST IMPORTANT EXPERIMENTS

1. **Reducibility test**: Single combined prompt vs /ar at equal token counts
2. **Enforcement test**: /ar with vs without anti-failure checks and corruption pre-inoculation
3. **Drift test**: Single prompt vs /ar across 10 runs — measure variance

---

## PRIOR ART SOURCES

Corruption & Sycophancy:
- ELEPHANT: Measuring social sycophancy in LLMs (2025)
- Sycophancy in LLMs: Causes and Mitigations (2024)
- Constitutional AI vs RLHF vs Prompt-Based Safety

Recursive Reasoning:
- SOCRATIC QUESTIONING: Recursive Thinking with LLMs (EMNLP 2023)
- Chain-of-Thought Prompting (Wei et al. 2022)
- Tree of Thoughts (Yao et al. 2023)

Search & Exploration:
- How Far are LLMs from Real Search? (2025)
- LLM-First Search: Self-Guided Exploration (2025)
- A Systematic Survey of Prompt Engineering (2024)

Grounding & Verification:
- LLM Grounding techniques (Neptune AI)
- Dependency Matters: Enhancing LLM Reasoning with Knowledge Grounding

Adversarial & Red Teaming:
- LLM Red Teaming guides (Confident AI)
- Devil's Advocate prompting techniques
- Large Language Models are Contrastive Reasoners (2024)

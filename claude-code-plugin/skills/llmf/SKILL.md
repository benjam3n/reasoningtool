---
name: "llmf - LLM Feasibility"
description: Assess whether a task is well-suited for LLM execution. Checks factual accuracy needs, context window requirements, hallucination risks, output verifiability, and recommends guardrails.
output:
  format: "prose"
---

# LLM Feasibility

**Input**: $ARGUMENTS

---

## Step 1: Task Classification

Categorize the task along dimensions that affect LLM suitability.

```
TASK: [what the LLM would be asked to do]
CONTEXT: [where/how this would be deployed]

TASK TYPE:
- Generation vs. Retrieval: [creating new content / finding existing facts]
- Open vs. Constrained: [creative latitude / strict requirements]
- Single-turn vs. Multi-turn: [one response / extended interaction]
- Standalone vs. Integrated: [independent / part of a pipeline]

ACCURACY REQUIREMENT: [EXACT / HIGH / MODERATE / APPROXIMATE]
CONSISTENCY REQUIREMENT: [must produce same output for same input? Y/N]
STAKES: [what happens if the output is wrong?]
```

---

## Step 2: Check Factual Accuracy Needs

Determine whether the task requires factual precision vs. generation.

```
FACTUAL ACCURACY ANALYSIS:

Facts required: [list specific facts the task depends on]
Fact sources: [where correct answers live]
Fact volatility: [how often do the facts change?]

LLM KNOWLEDGE ASSESSMENT:
| Fact/Domain | In training data? | Likely accurate? | Verifiable? |
|-------------|------------------|------------------|-------------|
| [fact 1] | [YES/NO/PARTIAL] | [YES/NO/MAYBE] | [easily/hard/impossible] |
| [fact 2] | [YES/NO/PARTIAL] | [YES/NO/MAYBE] | [easily/hard/impossible] |

FACTUAL RISK LEVEL: [HIGH / MODERATE / LOW]
- HIGH = task will fail if any facts are wrong
- LOW = task is primarily generative, facts are secondary
```

---

## Step 3: Assess Context Window Needs

Evaluate whether the task fits within practical context limits.

```
CONTEXT REQUIREMENTS:
- Input size: [estimated tokens]
- Required background: [what context the LLM needs]
- Output size: [estimated tokens]
- Total context needed: [estimated tokens]

FITS STANDARD CONTEXT? [Y/N]
FITS LARGE CONTEXT? [Y/N]
REQUIRES RAG OR CHUNKING? [Y/N — detail]

CONTEXT STRATEGY:
- [approach for managing context if it exceeds limits]
```

---

## Step 4: Identify Hallucination Risks

Pinpoint where the LLM is most likely to confabulate.

```
HALLUCINATION RISK MAP:
1. [risk area] — Likelihood: [HIGH/MED/LOW]
   Type: [fabricated facts / false confidence / plausible nonsense / citation invention]
   Trigger: [why the LLM would hallucinate here]
   Detectability: [easy / hard / impossible to catch]

2. [risk area] — Likelihood: [HIGH/MED/LOW]
   Type: [type]
   Trigger: [trigger]
   Detectability: [level]

HIGH-RISK PATTERNS IN THIS TASK:
- [pattern]: [why it's prone to hallucination]

OVERALL HALLUCINATION RISK: [HIGH / MODERATE / LOW]
```

---

## Step 5: Evaluate Output Verifiability

Can the output be checked for correctness?

```
VERIFIABILITY ASSESSMENT:
| Output Component | Verifiable? | Method | Cost to Verify |
|-----------------|-------------|--------|----------------|
| [component 1] | [Y/N/PARTIAL] | [how] | [effort level] |
| [component 2] | [Y/N/PARTIAL] | [how] | [effort level] |

AUTOMATED VERIFICATION POSSIBLE? [Y/N — what can be automated]
HUMAN REVIEW REQUIRED? [Y/N — for what portions]
UNVERIFIABLE PORTIONS: [what can't be checked — and risk level]
```

---

## Step 6: Recommend Guardrails

```
FEASIBILITY VERDICT: [WELL-SUITED / FEASIBLE WITH GUARDRAILS / PARTIALLY FEASIBLE / NOT RECOMMENDED]

CONFIDENCE: [HIGH / MODERATE / LOW]

GUARDRAILS NEEDED:
1. [guardrail] — Addresses: [risk] — Implementation: [how]
2. [guardrail] — Addresses: [risk] — Implementation: [how]
3. [guardrail] — Addresses: [risk] — Implementation: [how]

RECOMMENDED ARCHITECTURE:
- LLM handles: [what parts]
- External system handles: [what parts]
- Human handles: [what parts]

ALTERNATIVES TO PURE LLM:
- [alternative approach] — Better because: [reason]

IF PROCEEDING:
- Prompt strategy: [how to prompt for best results]
- Temperature: [suggested setting and why]
- Evaluation method: [how to measure quality]
- Failure mode: [what to do when output is bad]
```

---

## Integration

Use with:
- `/fwai` -> Assess potential for full AI agent automation
- `/roip` -> Compare LLM approach ROI against alternatives
- `/exint` -> Design the LLM integration with external systems

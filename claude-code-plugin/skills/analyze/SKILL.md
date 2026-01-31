---
name: "analyze - Analyze a Situation"
description: Sub-orchestrator for analytical requests. Routes to decomposition, systems analysis, comparison, risk assessment, or synthesis based on what kind of analysis is needed.
---

# Analysis

**Input**: $ARGUMENTS

---

## Routing Decisions

### 1. What Kind of Analysis?

| Analysis type | Signals | Route to |
|--------------|---------|----------|
| **Causal** | "What's causing X?", "Why is X?" | → /diagnose (overlaps — /diagnose handles causal) |
| **Structural** | "How does this work?", "Break this down" | → /dcm (decomposition) + /sya (systems analysis) |
| **Comparative** | "How does X compare to Y?" | → /cmp or /cda (cross-domain analogy) |
| **Risk** | "What could go wrong?" | → /fla (failure anticipation) + /prm (pre-mortem) |
| **Data/Empirical** | "What does the data show?" | → /sta (statistical analysis) + /dc (data collection) |
| **Strategic** | "What's our position?" | → /swa (SWOT) + /cma (competitive analysis) |
| **Problem** | "What's the problem here?" | → /pbi (problem identification) |

### 2. Is This Analysis or Something Else?

- **"Is X true?"** → This is a claim. → INVOKE: /claim $ARGUMENTS
- **"Should I X?"** → This is a decision. → INVOKE: /decide $ARGUMENTS
- **"How do I X?"** → This is method-seeking. → INVOKE: /how $ARGUMENTS
- **"Review my X"** → This is evaluation. → INVOKE: /evaluate $ARGUMENTS
- **If it IS analysis** → continue.

### 3. Analysis of a Thing or a Situation?

- **A thing** (document, plan, code, argument): /evaluate is usually the better fit.
  → INVOKE: /evaluate $ARGUMENTS
- **A situation** (market, team dynamics, failure pattern, system behavior): /analyze handles this.

### 4. Decomposition, Synthesis, or Both?

- **Decomposition** ("Break this down", "What are the parts?"): take the complex thing apart.
  → INVOKE: /dcm [topic]
- **Synthesis** ("Pull these together", "What does this all mean?"): combine multiple findings.
  → INVOKE: /ins [findings]
- **Both** ("Analyze this"): decompose first, then synthesize.
  → INVOKE: /dcm [topic] — then → /ins [findings from decomposition]

---

## Execute

**Default (general "analyze this"):**
→ INVOKE: /dcm $ARGUMENTS — decompose into parts
→ Then INVOKE: /ins [findings] — synthesize conclusions

**Causal analysis:**
→ INVOKE: /diagnose $ARGUMENTS

**Comparative analysis:**
→ INVOKE: /cmp $ARGUMENTS

**Risk analysis:**
→ INVOKE: /fla $ARGUMENTS + /prm $ARGUMENTS

**Strategic analysis:**
→ INVOKE: /swa $ARGUMENTS + /cma $ARGUMENTS

---

## After Completion

Report:
- What was analyzed
- Analysis type used
- Key findings
- Structure/decomposition (if applicable)
- Synthesis/conclusions
- Recommended next steps

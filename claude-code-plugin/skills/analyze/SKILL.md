---
name: "analyze - Analyze a Situation"
description: Sub-orchestrator for analytical requests. Routes to decomposition, systems analysis, comparison, risk assessment, or synthesis based on what kind of analysis is needed.
---

# Analysis

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Decomposition needed**: The user has something complex and wants it broken into understandable parts ("break this down", "what are the components?").
**Interpretation 2 — Causal analysis**: The user wants to understand why something is happening ("what's causing X?", "why does this keep failing?").
**Interpretation 3 — Synthesis needed**: The user has multiple pieces of information and wants them combined into coherent understanding ("what does all this mean?", "pull this together").

If ambiguous, ask: "Do you need this broken down into parts, or do you need me to find what's causing something, or do you want me to pull multiple findings together?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Analysis type determines tool.** Causal analysis, structural analysis, comparative analysis, risk analysis, and synthesis are fundamentally different operations. Picking the wrong type produces plausible but misleading output. Identify the type before starting.

2. **Situations are analyzed; artifacts are evaluated.** /analyze handles situations (markets, dynamics, systems, patterns). /evaluate handles artifacts (documents, plans, code, arguments). If someone hands you a thing to assess, that's /evaluate. If they describe a situation to understand, that's /analyze.

3. **Decomposition precedes synthesis.** You can't synthesize what you haven't decomposed. For "analyze this" requests, break it down first (/dcm), then pull conclusions together (/ins). Never skip decomposition.

4. **Every analysis must answer "so what?"** Breaking things into parts is not analysis — it's taxonomy. Analysis tells you what the parts mean, how they interact, and what follows from their arrangement.

5. **Multi-dimensional situations need multi-dimensional analysis.** A situation that spans strategy, people, and technology needs analysis along all three dimensions. Single-dimension analysis on a multi-dimensional problem produces blind spots.

6. **Analysis terminates in actionable insight.** If the analysis doesn't point toward a decision, an action, or a changed understanding, it hasn't finished. "This is complex" is not a finding — it's an admission of incomplete analysis.

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
| **Pattern** | "What's the pattern?" | → /sya (systems analysis) |
| **Ethical** | "Is this right?", "What are the moral dimensions?" | → /eth (ethics analysis) |
| **Safety** | "Is this safe?", "What are the safety risks?" | → /saf (safety analysis) |
| **Future** | "Where is this going?", "What happens next?" | → /fut (future analysis) |
| **Dominance** | "Which option is strictly better?" | → /dom (dominance analysis) |
| **Outcome** | "What are the possible outcomes?" | → /gop + /obo + /ogo |
| **Differentiation** | "What makes these different?" | → /difr (differentiation reasoning) |
| **General pattern** | "What's the general principle?" | → /genl (general analysis) |
| **Specific application** | "How does this apply to my case?" | → /spcf (specific analysis) |
| **Best-case** | "What's the ideal outcome?" | → /utp (utopia analysis) |
| **Worst-case** | "What's the worst that could happen?" | → /dys (dystopia analysis) |

### 2. Is This Analysis or Something Else?

- **"Is X true?"** → This is a claim. → INVOKE: /claim $ARGUMENTS
- **"Should I X?"** → This is a decision. → INVOKE: /decide $ARGUMENTS
- **"How do I X?"** → This is method-seeking. → INVOKE: /how $ARGUMENTS
- **"Review my X"** → This is evaluation. → INVOKE: /evaluate $ARGUMENTS
- **"Write about X"** → This is creation. → INVOKE: /create $ARGUMENTS
- **"I want X"** → This is a goal. → INVOKE: /want $ARGUMENTS
- **"I think X"** → Formalize the belief. → INVOKE: /it $ARGUMENTS
- **"X, but Y"** → Tension to resolve. → INVOKE: /but $ARGUMENTS
- **"I'm not sure about X"** → Classify the uncertainty. → INVOKE: /nsa $ARGUMENTS
- **"Handle this"** (vague) → INVOKE: /handle $ARGUMENTS
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

### 5. How Many Dimensions?

- **Single dimension** (just financial, just technical, just organizational): use the matching domain skill from /technical.
- **Multi-dimensional** (spans strategy + people + technology): analyze each dimension, then synthesize.
  → INVOKE: /dcm for each dimension — then → /ins to combine.

### 6. Depth Required

- Quick overview ("give me a sense of..."): 1x — one-pass decomposition
- Standard analysis ("analyze this"): 2x — decomposition + synthesis
- Deep analysis ("thorough analysis"): 4x — multi-dimensional decomposition + cross-referencing + synthesis
- Exhaustive ("leave no stone unturned"): 8x — all dimensions, all interactions, full synthesis

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

**Problem identification:**
→ INVOKE: /pbi $ARGUMENTS

**Systems analysis:**
→ INVOKE: /sya $ARGUMENTS

**Ethical analysis:**
→ INVOKE: /eth $ARGUMENTS

**Future analysis:**
→ INVOKE: /fut $ARGUMENTS

**Outcome analysis:**
→ INVOKE: /gop + /obo + /ogo $ARGUMENTS

**Dominance analysis:**
→ INVOKE: /dom $ARGUMENTS

**Differentiation analysis:**
→ INVOKE: /difr $ARGUMENTS

### Supplementary Analysis (invoke when relevant)

| Situation | Also invoke |
|-----------|------------|
| Need obvious check first | → /obv (obvious check) |
| Obvious bad outcomes | → /obo |
| Obvious good outcomes | → /ogo |
| Self-deception risk | → /sdc (self-deception check) |
| Need to trace implications | → /sycs (so you can see) |
| Situation has a narrative | → /story |
| Need to check hidden assumptions | → /aex (assumption extraction) |
| Involves argument structure | → /agsk (argument analysis) |
| User wants debate format | → /deb |
| Need to expand "etc" or implied items | → /etc or /aso |
| Scope expanding | → /iagca (compress scope) |
| Unresolved sub-questions | → /tbd |
| User wants easy mode | → /ezy |
| User wants hard mode | → /hrd |
| User wants sophisticated analysis | → /soph |
| User wants maximum rigor | → /certainty |

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Taxonomy without insight** | Output lists parts without saying what they mean | Every decomposition must answer "so what?" for each part |
| **Wrong analysis type** | Causal tools on structural problem, or vice versa | Re-identify the analysis type before proceeding |
| **Single-dimension blindness** | Multi-dimensional situation analyzed on only one axis | Explicitly identify all relevant dimensions, analyze each |
| **Evaluation masquerading as analysis** | Assessing quality of an artifact instead of understanding a situation | If it's a thing to assess, route to /evaluate |
| **Analysis paralysis** | Decomposing endlessly without synthesizing | Set a decomposition depth limit, then force synthesis |
| **Missing "so what"** | Analysis ends with "it's complex" without actionable insight | Push to: what does this mean for decisions? What should change? |

---

## Depth Scaling

| Depth | Scope | Output |
|-------|-------|--------|
| **1x** | Quick — one-pass decomposition, key findings | Component list with 2-3 key insights |
| **2x** | Standard — decomposition + synthesis, main interactions identified | Full decomposition, interaction map, synthesized conclusions |
| **4x** | Thorough — multi-dimensional decomposition + cross-referencing + synthesis | All dimensions analyzed, cross-dimension interactions, comprehensive synthesis |
| **8x** | Exhaustive — all dimensions, all interactions, sensitivity analysis, full synthesis | Complete analytical model with sensitivities, implications, and recommendations |

---

## Pre-Completion Checklist

- [ ] Analysis type correctly identified (causal / structural / comparative / risk / strategic / pattern)
- [ ] Routed to situation analysis, not artifact evaluation
- [ ] All relevant dimensions identified and analyzed
- [ ] Decomposition completed before synthesis
- [ ] "So what?" answered for each major finding
- [ ] Interactions between components identified (not just parts listed)
- [ ] Synthesis produces actionable insight, not just summary
- [ ] Recommended next steps or decisions identified

---

## After Completion

Report:
- What was analyzed
- Analysis type used
- Dimensions covered
- Key findings (with "so what" for each)
- Structure/decomposition (if applicable)
- Interactions and patterns identified
- Synthesis/conclusions
- Recommended next steps

### Follow-Up Routing

After analysis, the user may need:
- **"What should I do?"** → INVOKE: /decide or /action
- **"Write this up"** → INVOKE: /create
- **"What are the implications?"** → INVOKE: /sycs
- **"What could go wrong?"** → INVOKE: /fla or /obo
- **"What skill should I run next?"** → INVOKE: /next or /fonss
- **"What's still unresolved?"** → INVOKE: /tbd

---

## Integration

- **Use from**: /claim (when claim requires situational analysis), /decide (when decision requires understanding the landscape), /create (when content requires analytical foundation)
- **Routes to**: /dcm (decomposition), /sya (systems analysis), /cmp (comparison), /fla (failure anticipation), /prm (pre-mortem), /swa (SWOT), /cma (competitive analysis), /pbi (problem identification), /diagnose (causal analysis), /ins (synthesis)
- **Differs from**: /evaluate (analyze handles situations, evaluate handles artifacts), /diagnose (analyze is broader, diagnose is specifically causal), /search (analyze examines known territory, search explores unknown territory)
- **Complementary**: /aex (surface assumptions in the analysis), /mv (check if decomposition is MECE), /se (enumerate missing dimensions)

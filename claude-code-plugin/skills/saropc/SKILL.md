---
name: saropc
description: "Apply Recursive Causal Interrogation to choices about what procedure to run, what to measure, and when to stop."
---

# RCI on Protocol Choices

**Input**: $ARGUMENTS

---

## Overview

Apply Recursive Causal Interrogation to choices about what procedure to run, what to measure, and when to stop. This is a self-audit skill — it examines your OWN decision-making about procedures.

The core question: Why am I choosing THIS procedure, THIS measurement, THIS stopping point? Trace the reasoning backward until you hit bedrock, a loop, or a genuine unknown.

## Steps

### Step 1: Identify the Protocol Choice
What decision is being interrogated?

| Choice Type | Example | Why Interrogate |
|------------|---------|----------------|
| Procedure selection | "I'll use /rca for this" | Why that procedure? What made you pick it? |
| Measurement choice | "I'll measure success by X" | Why that metric? What are you NOT measuring? |
| Scope decision | "I'll analyze 3 options" | Why 3? Why not 5? Why not 1? |
| Stopping rule | "This analysis is complete" | How do you know? What would "more" look like? |
| Depth decision | "This is deep enough" | Deep enough for what? Who decided? |
| Ordering choice | "I'll do A before B" | Why that order? What if reversed? |

### Step 2: Trace Backward (Recursive Causal Interrogation)
For the identified choice, ask: **"What caused this choice?"**

```
Choice: [the protocol decision]
    ↑ Why?
Cause 1: [what led to this choice]
    ↑ Why?
Cause 2: [what led to cause 1]
    ↑ Why?
Cause 3: [what led to cause 2]
    ↑ Why?
...continue until you reach:
```

**Termination conditions:**
- **Bedrock**: A foundational principle or axiom ("because ARAW is the core method")
- **Loop**: The reasoning circles back ("because that's how we do it because it's what we chose because...")
- **Genuine unknown**: "I don't actually know why I chose this"
- **Impulse**: "It just felt right" / "It was the first thing that came to mind"
- **External**: "Someone told me to" / "It's what the documentation says"

### Step 3: Evaluate the Causal Chain

| Termination | Meaning | Action |
|-------------|---------|--------|
| Bedrock | Choice is well-grounded | Accept — but verify the bedrock is sound |
| Loop | Circular reasoning | INVESTIGATE — the choice may be arbitrary |
| Unknown | No real reason | INVESTIGATE — choice may be habit or default |
| Impulse | Intuition without justification | TEST — is there a better option? |
| External | Deference to authority | VERIFY — does the authority's reasoning hold? |

### Step 4: Check for Common Biases

**Measurement impulse**: "I should measure something" → but WHAT and WHY?
- Are you measuring because it matters or because you can?
- Is the measurement proxy valid? (Does what's measurable = what matters?)
- Will the measurement change your behavior? If not, why measure?

**Closure impulse**: "This is done" → but HOW DO YOU KNOW?
- Are you stopping because you reached a conclusion or because you're tired?
- Did you define "done" before starting?
- Would someone else reviewing this say it's complete?

**Selection bias**: "This procedure fits" → but DID YOU CONSIDER ALTERNATIVES?
- Did you choose from the full menu or just pick the first familiar option?
- What procedure would someone from a different background choose?
- Is there a procedure you're avoiding? Why?

### Step 5: Decide Whether to Change
After interrogation:

| Finding | Action |
|---------|--------|
| Choice is well-grounded (bedrock) | Proceed with confidence |
| Choice is partially grounded | Note the weak links, proceed with monitoring |
| Choice is circular or unknown | PAUSE — find a grounded alternative |
| Choice is biased | Debias — consider the overlooked alternatives |
| Choice is externally grounded but valid | Proceed, noting the dependency |

### Step 6: Report
```
RCI ON PROTOCOL CHOICES:
Choice interrogated: [what decision was examined]

Causal chain:
[choice] ← [cause] ← [cause] ← ... ← [termination]

Termination type: [bedrock / loop / unknown / impulse / external]
Bias check: [measurement impulse / closure impulse / selection bias / none found]

Verdict: [well-grounded / partially grounded / poorly grounded]
Action: [proceed / proceed with monitoring / change / pause and reconsider]

If changing: [what alternative and why it's better grounded]
```

## When to Use
- When you notice "measurement impulse" or "closure impulse"
- When you are about to choose scope, sample size, or stopping rules
- When you are about to declare something "verified" or "complete"
- When a procedure choice feels automatic rather than deliberate
- → INVOKE: /rci (recursive causal interrogation) for the general RCI method
- → INVOKE: /pv (procedure validation) for validating the procedure itself

## Verification
- [ ] Specific protocol choice identified
- [ ] Causal chain traced to termination
- [ ] Termination type identified
- [ ] Common biases checked
- [ ] Decision to proceed or change is justified

---
name: failure_anticipation
description: "Systematically identify potential failures, assess their risk, and plan mitigations before execution"
---

# Failure Anticipation

## Overview
Systematically identify potential failures, assess their risk, and plan mitigations before execution

## Steps

### Step 1: Decompose the plan
Break down the plan into analyzable components:
1. Identify all major steps or phases
2. List all inputs the plan depends on
3. List all outputs the plan must produce
4. Identify all external dependencies (people, systems, resources)
5. Note any timing constraints or deadlines
6. Map relationships between components (what depends on what)

### Step 2: Generate failure modes by category
For each component, systematically consider failures in each category:

INPUT FAILURES:
- What if expected inputs are missing?
- What if inputs are wrong or corrupted?
- What if input format changes?

PROCESS FAILURES:
- What if the logic is flawed?
- What if it takes too long?
- What if resources are exhausted?

OUTPUT FAILURES:
- What if outputs are wrong?
- What if outputs are missing?
- What if outputs are rejected?

RESOURCE FAILURES:
- What if a required resource is unavailable?
- What if capacity is insufficient?
- What if costs exceed budget?

TIMING FAILURES:
- What if a step takes longer than expected?
- What if deadlines are missed?
- What if things happen in wrong order?

INTEGRATION FAILURES:
- What if an API changes?
- What if systems can't communicate?
- What if versions are incompatible?

EXTERNAL FAILURES:
- What if a vendor fails?
- What if market conditions change?
- What if regulations change?

HUMAN FAILURES:
- What if someone makes a mistake?
- What if there's a misunderstanding?
- What if key people are unavailable?

CASCADE FAILURES:
- What single points of failure exist?
- What failures could trigger others?
- What could cause systemic collapse?

### Step 3: Score each failure mode
For each identified failure, assign FMEA scores:

OCCURRENCE (O) - How likely is this failure?
1-2: Remote (< 1 in 10,000)
3-4: Low (1 in 1,000 to 1 in 100)
5-6: Moderate (1 in 100 to 1 in 20)
7-8: High (1 in 20 to 1 in 5)
9-10: Very High (> 1 in 5)

SEVERITY (S) - How bad is the impact?
1-2: Negligible (minor inconvenience)
3-4: Minor (some rework, small delay)
5-6: Moderate (significant delay or cost)
7-8: Major (goal compromised)
9-10: Catastrophic (project failure, irreversible harm)

DETECTION (D) - How hard to detect before damage?
1-2: Almost certain to detect early
3-4: High chance of detection
5-6: Moderate chance of detection
7-8: Low chance of detection
9-10: Almost impossible to detect

Calculate RPN = O x S x D for each failure

### Step 4: Prioritize and classify
Sort and classify failures by risk:

1. Sort by RPN descending (highest risk first)
2. Classify into tiers:
   - Critical: RPN > 200 or S >= 9 (must mitigate)
   - High: RPN 100-200 (should mitigate)
   - Medium: RPN 50-100 (consider mitigating)
   - Low: RPN < 50 (accept or monitor)
3. Group by category to identify systemic patterns
4. Identify single points of failure (high impact, single cause)
5. Compare against risk tolerance level

### Step 5: Develop mitigations
For each critical and high-priority failure, develop mitigation:

MITIGATION TYPES:
- Prevention: Stop the failure from occurring
- Detection: Catch the failure early (reduce D score)
- Reduction: Lessen the impact (reduce S score)
- Transfer: Move risk to another party (insurance, contracts)
- Acceptance: Acknowledge and prepare to handle

For each mitigation:
1. Describe the specific action
2. Estimate implementation effort
3. Project new O, S, D scores after mitigation
4. Calculate new RPN to verify improvement
5. Identify who is responsible for implementation

### Step 6: Create contingency plans
For failures that can't be fully prevented, create response plans:

For each critical failure:
1. Define trigger conditions (when is failure confirmed?)
2. Specify immediate response actions
3. Identify decision maker and escalation path
4. List resources needed for response
5. Define recovery steps to get back on track
6. Set acceptable recovery time

Also define:
- Early warning indicators to monitor
- Kill criteria (when to abort the plan entirely)
- Communication plan for stakeholders

### Step 7: Compile final assessment
Create comprehensive failure anticipation report:

1. Executive summary of risk profile
2. Critical failures requiring attention before proceeding
3. Mitigation actions prioritized by impact/effort
4. Contingency plans for unavoidable risks
5. Monitoring dashboard recommendations
6. Residual risks being accepted
7. Go/no-go recommendation based on risk tolerance


## When to Use
- Before executing any significant plan or project
- During risk assessment phase of planning
- When designing systems that must be reliable
- Before making irreversible decisions or commitments
- When stakes are high and failure is costly
- At strategy selection to compare risk profiles
- Before deployment or launch of new systems
- When inheriting or reviewing someone else's plan
- During post-mortem analysis to improve future anticipation
- When entering unfamiliar territory with unknown risks

## Verification
- All nine failure categories were examined systematically
- FMEA scores are justified, not arbitrary
- Critical failures (RPN > 200 or S >= 9) have mitigation plans
- Contingency plans are specific and actionable
- Single points of failure are identified
- Cascade failure potential is assessed
- Monitoring indicators are measurable

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.
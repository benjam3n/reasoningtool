---
name: "fr - Failure Recovery"
description: "Structured recovery procedures when projects encounter failures, providing clear decision trees and specific actions for common failure modes."
---

# Failure Recovery

## Overview
Structured recovery procedures when projects encounter failures, providing clear decision trees and specific actions for common failure modes.

## Steps

### Step 1: Identify and classify failure
Use the master decision tree to classify the failure:

1. Is this a complete blocker? (Cannot proceed at all)
   - YES: Continue to step 2
   - NO: Continue with workaround, document risk, exit procedure

2. Is the goal still valid? (Do you still want this outcome?)
   - YES: Continue to step 3
   - NO: Archive project, complete LEARNINGS.md, exit procedure

3. Is the strategy still valid? (Is approach fundamentally sound?)
   - YES: Continue to step 4
   - NO: Return to Strategy Phase, run Strategy Search again

4. Is the plan still valid? (Are steps right, just need better execution?)
   - YES: Fix execution issue, add safeguards, continue
   - NO: Return to Planning Phase, revise gates

Classify into failure type:
- validation_failed: Discovery shows no viable path
- timeline_blown: Significantly behind schedule
- strategy_not_working: Execution not producing results
- resource_exhausted: Budget, time, or energy depleted
- external_shock: External event invalidates plan

### Step 2: Diagnose root cause
For each failure type, answer diagnostic questions:

VALIDATION FAILED:
- Was the niche too narrow or too broad?
- Were you talking to the right people?
- Was the value proposition clear?
- Is the problem real but your solution wrong?

TIMELINE BLOWN:
- Was the estimate unrealistic?
- Did scope creep occur?
- Were there unexpected blockers?
- Is effort/time allocation sufficient?

STRATEGY NOT WORKING:
- Is the strategy wrong, or execution wrong?
- Did market conditions change?
- Were Adversarial Review assumptions violated?
- Is there new information that invalidates strategy?

RESOURCE EXHAUSTED:
- Which resource is the binding constraint?
- Is the goal achievable with remaining resources?
- What's the minimum viable completion?

EXTERNAL SHOCK:
- Is this temporary or permanent?
- Does this affect the goal or just the strategy?
- Can we adapt or must we wait?

Document answers to build diagnosis.

### Step 3: Evaluate recovery options
Based on failure type and diagnosis, evaluate recovery options:

VALIDATION FAILED OPTIONS:
A. Pivot to adjacent niche (2-3 weeks)
   - When: Core problem valid, wrong audience
   - Steps: List adjacent audiences, run discovery, score, restart Phase 2

B. Pivot to different problem (3-4 weeks)
   - When: This problem isn't real or big enough
   - Steps: Review notes for other pain points, select alternative, return to Assessment

C. Switch to cloning strategy (1-2 weeks)
   - When: Niche discovery systematically failing
   - Steps: Identify successful products, find underserved segments, switch strategy

D. Abandon this goal (1-2 days)
   - When: Fundamental assumption was wrong
   - Steps: Complete LEARNINGS.md, archive project, start fresh

TIMELINE BLOWN OPTIONS:
A. Reduce scope (1-2 days planning)
   - When: Trying to do too much
   - Steps: List deliverables, categorize MUST/SHOULD/COULD, cut to MUST

B. Extend timeline (immediate)
   - When: Scope correct, just slower than expected
   - Steps: Calculate realistic time, update milestones, communicate

C. Increase resources (varies)
   - When: Time-resource tradeoff available
   - Steps: Identify parallelizable work, determine if help possible

STRATEGY NOT WORKING OPTIONS:
A. Adjust strategy parameters (1-2 weeks)
   - When: Strategy sound, needs tuning
   - Steps: Identify parameters, run experiments, adopt best variation

B. Switch to backup strategy (1 week)
   - When: Pre-identified backup exists
   - Steps: Review backup, verify assumptions, run Adversarial Review, switch

C. Return to Strategy Search (2-3 weeks)
   - When: Need fundamentally different approach
   - Steps: Document why current failed, use as input to new Strategy Search

RESOURCE EXHAUSTED OPTIONS:
A. Minimum viable completion (varies)
   - When: Can achieve partial goal with remaining resources
   - Steps: Define MVP, cut to essentials, focus remaining resources

B. Pause and replenish (pause period + ramp-up)
   - When: Goal still valuable, just need to recover
   - Steps: Document state, set pause period, replenish, resume

C. Pivot to lower-resource approach (1-2 weeks)
   - When: Different path requires fewer resources
   - Steps: Identify alternatives, evaluate, switch approach

EXTERNAL SHOCK OPTIONS:
A. Wait it out (disruption duration)
   - When: Temporary disruption
   - Steps: Estimate duration, pause project, monitor, resume when clear

B. Adapt to new reality (1-3 weeks)
   - When: Permanent change but goal still achievable
   - Steps: Analyze new landscape, update strategy, continue

C. Abandon and learn (1-2 days)
   - When: Change makes goal unachievable or undesirable
   - Steps: Accept, document learnings, archive, consider new goal

### Step 4: Select recovery path
Choose the best recovery option based on:

1. Alignment with root cause
   - Does this option address the actual problem?

2. Resource requirements
   - Do you have the time/money/energy for this option?

3. Risk profile
   - What could go wrong with this recovery?
   - Is failure of recovery acceptable?

4. Learning potential
   - What will you learn from this path?

5. Goal preservation
   - Does this keep you moving toward the original goal?
   - Or does it require goal adjustment?

Make explicit selection with documented rationale.
Get stakeholder buy-in if applicable.

### Step 5: Create recovery plan
Build concrete recovery plan:

1. Define recovery milestones
   - What does "recovered" look like?
   - What are intermediate checkpoints?

2. List specific actions
   - What needs to happen in what order?
   - Who does what?

3. Set timeline
   - When will each milestone be hit?
   - Add buffer for recovery-specific uncertainty

4. Define abort criteria
   - When would you abandon this recovery?
   - What signals that recovery isn't working?

5. Update project documents
   - STATE.md: reflect recovery mode
   - DECISION_TREE.md: document recovery decision

### Step 6: Execute recovery
Execute the recovery plan:

1. Update STATE.md to reflect recovery in progress
2. Follow recovery milestones
3. Regular check-ins against abort criteria
4. Watch for signs recovery isn't working:
   - Missing recovery milestones
   - New blockers appearing
   - Resource burn higher than expected

If abort criteria triggered:
- Stop current recovery
- Return to Step 3 with updated information
- Select different recovery option

### Step 7: Document learnings
After recovery (successful or not):

1. Document what caused the failure
   - Root cause
   - Warning signs that were missed
   - What could have prevented it

2. Document what recovery worked (or didn't)
   - Which option was selected
   - How well it addressed the root cause
   - What would you do differently

3. Update LEARNINGS.md with failure/recovery
   - Add to project's learnings
   - Consider adding to library if generalizable

4. Consider procedure improvements
   - Should any procedures be updated?
   - Should new failure modes be added?
   - Should triggers be refined?


## When to Use
- When a project encounters a complete blocker
- When key assumptions are invalidated
- When timeline is more than 50% over estimate
- When strategy execution consistently fails to produce expected results
- When resources (budget, time, energy) are exhausted before completion
- When external events significantly change project conditions
- When feeling stuck with no clear path forward
- During retrospectives to analyze past failures

## Verification
- Failure is clearly identified and named with classification
- Diagnosis is complete using relevant questions
- Recovery option selected with documented reasoning
- Time/resource cost is estimated for recovery
- Decision is documented in DECISION_TREE.md
- STATE.md reflects recovery mode during execution
- LEARNINGS.md updated after recovery completes

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.
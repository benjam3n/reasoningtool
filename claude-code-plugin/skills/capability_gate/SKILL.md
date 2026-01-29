---
name: capability_gate
description: "Pre-step feasibility check determining if AI can execute directly, needs delegation, or if task is infeasible"
---

# Capability Gate

## Overview
Pre-step feasibility check determining if AI can execute directly, needs delegation, or if task is infeasible

## Steps

### Step 1: Classify step requirements
Analyze what the step actually requires:

1. Physical requirements:
   - Does it require being at a location? -> Physical
   - Does it require handling objects? -> Physical
   - Does it require face-to-face interaction? -> Physical

2. Communication requirements:
   - Does it require a phone call? -> Check if AI phone works
   - Does it require email? -> Check if email is configured
   - Does it require real-time chat? -> May need human

3. Access requirements:
   - Does it need specific accounts/credentials? -> Check availability
   - Does it need specific tools/software? -> Check if available
   - Does it need specific data? -> Check if accessible

4. Skill requirements:
   - Does it need human judgment? -> May need delegation
   - Does it need relationship/rapport? -> Likely needs human
   - Does it need specialized expertise? -> May need delegation

Document all requirements clearly.

### Step 2: Check AI direct capability
Determine if AI can do this step directly:

Decision tree:
1. Pure digital research/analysis? -> YES, AI native
2. Writing/document creation? -> YES, AI native
3. Data processing/calculations? -> YES, AI native
4. Requires physical presence? -> NO, needs delegation
5. Requires phone call?
   - Simple info gathering -> MAYBE, try AI phone
   - Complex conversation -> NO, needs human
6. Requires identity verification? -> MAYBE, check specifics
7. Requires relationship building? -> NO, needs human

If AI can do directly:
- Categorize as ai_native
- Note execution method
- Cost = $0

If AI cannot do directly, proceed to next step.

### Step 3: Check AI with tools capability
If AI cannot do directly, check if configured tools enable it:

Email configured?
- Can send outreach emails
- Can receive and process responses
- Check: email_acquisition completed

Phone configured?
- Can receive SMS for verification
- Can receive callbacks
- Check: phone_acquisition completed

AI phone service configured?
- Can make outbound calls
- Can gather information via phone
- Check: Bland AI integration active

Other tools?
- Web scraping tools
- API access to services
- Database connections

If tool enables the step:
- Categorize as ai_with_tool
- Note which tool and method
- Estimate cost (per-use)

If no tool available:
- Check if tool can be set up (prerequisite)
- Or proceed to delegation check

### Step 4: Check delegation feasibility
If AI (direct or with tools) cannot do it, assess delegation:

1. Is this a digital task?
   - Research, data collection -> Fiverr, Upwork
   - Phone calls -> Fancy Hands, Fiverr
   - Account setup -> Fiverr
   - Categorize as delegatable_digital

2. Is this a physical task?
   - Local errand -> TaskRabbit
   - Site visit -> TaskRabbit, Craigslist
   - Meeting attendance -> Craigslist
   - Categorize as delegatable_physical

3. Estimate delegation cost:
   - Digital tasks: $5-50 typical
   - Physical tasks: $20-100 typical

4. Check budget:
   - Is estimated_cost <= available_budget?
   - If no, task may be infeasible

5. Check timeline:
   - Can delegation complete by deadline?
   - Add buffer for finding/vetting worker

### Step 5: Determine final classification
Based on Steps 2-4, assign final capability category:

Priority order (prefer higher if multiple apply):
1. ai_native - Free, fast, reliable
2. ai_with_tool - Cheap, fast, automated
3. delegatable_digital - Moderate cost, remote
4. delegatable_physical - Higher cost, local
5. infeasible - Cannot be done within constraints

For infeasible tasks:
- Document why it's infeasible
- Identify which constraint is blocking
- Prepare for transformation step

Assign:
- capability_category
- execution_method
- estimated_cost
- prerequisites needed

### Step 6: Transform infeasible steps (if needed)
If step is classified as infeasible, transform to achievable alternative:

Common transformations:
- "Call railroad office" -> "Use AI phone service to call"
- "Visit site for photos" -> "Delegate to TaskRabbit for photos"
- "Meet with city manager" -> "Email + AI phone call instead"
- "Attend council meeting" -> "Hire local person to attend and report"
- "Submit physical document" -> "Find digital submission OR delegate delivery"
- "Build relationship with X" -> "Start with email outreach, escalate if needed"

Transformation process:
1. Identify the core goal of the step
2. Find alternative path to same goal
3. Verify alternative is feasible
4. Document the transformation

If no transformation possible:
- Flag as truly infeasible
- Recommend removing from plan
- Identify impact on overall goal

### Step 7: Generate execution plan
Create complete execution plan for the step:

Document:
1. Original step description
2. Capability category assigned
3. Execution method
4. Prerequisites (what must be done first)
5. Estimated cost
6. Success criteria (how to know it's done)
7. Fallback plan (what if primary method fails)

For delegation steps, include:
- Platform to use
- Budget allocation
- Instruction outline
- Quality criteria

For AI-with-tool steps, include:
- Which tool
- Configuration requirements
- Expected outputs

Verify plan is complete and actionable.


## When to Use
- Before attempting any step in an autonomous plan
- When planning a new task or project
- When a step fails and needs alternative approach
- When constraints change (budget, time, resources)
- During plan validation to ensure all steps are feasible
- When encountering unexpected requirements
- Before committing resources to a task

## Verification
- Step requirements fully analyzed
- Capability category correctly assigned
- Execution method is specific and actionable
- Prerequisites are identified and achievable
- Cost estimate is reasonable and within budget
- Success criteria are measurable
- Fallback plan exists for non-trivial steps
- Infeasible steps are transformed or flagged

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.
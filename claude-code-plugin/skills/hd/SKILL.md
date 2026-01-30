---
name: "hd - Human Delegation"
description: "Delegate physical, phone, or in-person tasks to humans when AI cannot perform them directly"
---

# Human Delegation

## Overview
Delegate physical, phone, or in-person tasks to humans when AI cannot perform them directly

## Steps

### Step 1: Classify task and verify delegation is necessary
Before delegating, confirm this task cannot be done by AI:
1. Can AI do this directly? (research, writing, analysis) - If yes, don't delegate
2. Can AI phone service handle this? (simple calls) - If yes, use AI phone
3. Does this require physical presence or human judgment? - If yes, proceed
4. Is this task ethical and legal? - If no, abort

Classify the task into one of:
- phone_call: Need to call someone and have a conversation
- local_physical: Need someone present at a location
- research_collection: Need human judgment for research/data
- document_delivery: Need physical document handled
- meeting_attendance: Need someone to attend and report
- complex_interaction: Negotiations, relationship building

### Step 2: Estimate cost and check budget
Calculate expected cost based on:
- Task complexity (1-10 scale)
- Time required (hours)
- Skill level needed (basic/intermediate/expert)
- Urgency multiplier (1.0 standard, 1.5 urgent, 2.0 rush)

Formula: base_rate x complexity x time x urgency_multiplier

Compare to budget_limit. If estimated_cost > budget_limit:
- Find cheaper alternative approach
- Reduce scope of task
- Skip task if not critical
- Request additional budget if essential

### Step 3: Select platform based on task type and budget
Use decision tree to select optimal platform:

For phone_call:
  - budget_under_10: Use Bland AI (not delegation)
  - budget_under_30: Fancy Hands
  - budget_over_30: Fiverr (experienced caller)

For local_physical:
  - urgent (< 24 hours): TaskRabbit
  - not_urgent: Craigslist (better rates)

For research_collection:
  - simple: Fiverr
  - complex: Upwork

For document_delivery:
  - local: TaskRabbit
  - requires travel: Craigslist with higher budget

For meeting_attendance:
  - professional setting: Upwork or vetted Craigslist
  - casual setting: TaskRabbit or Craigslist

### Step 4: Write detailed task instructions
Create comprehensive instructions using template:

1. Task Overview: One clear sentence
2. Background Context: Why this matters (helps judgment calls)
3. Specific Steps: Numbered, detailed, unambiguous
4. Required Deliverables: Checklist with specific items
5. Quality Criteria: How to verify success
6. What NOT to Do: Common mistakes to avoid
7. Communication: How to report, ask questions
8. Budget: Payment amount, bonus criteria

Requirements:
- Must be completable by someone with no prior context
- Must have specific, verifiable deliverables
- Must include what NOT to do
- Must have clear deadline
- Must have communication method

### Step 5: Post task and vet candidates
Post task to selected platform:
1. Create account on platform if needed
2. Post task with full instructions
3. Set budget and deadline
4. Monitor for applicants

Vet candidates based on:
- Reviews/ratings (minimum 4.0 stars, 10+ reviews preferred)
- Relevant experience (has done similar tasks)
- Communication quality (responds clearly and promptly)
- Response time (engaged candidates respond quickly)
- Price quote (within budget, not suspiciously low)

Select best candidate and confirm acceptance.

### Step 6: Monitor execution and provide support
Track task progress through checkpoints:

1. Task accepted confirmation (within hours of posting)
2. Start confirmation (worker begins task)
3. Mid-point check-in (for tasks > 1 day)
4. Progress updates (as defined in communication plan)
5. Completion notification (task finished)

Provide support:
- Answer questions promptly
- Clarify ambiguities
- Adjust scope if reasonable issues arise
- Document any changes to original task

Watch for red flags:
- No communication after acceptance
- Missed checkpoints
- Quality concerns in updates
- Requests to change scope significantly

### Step 7: Verify deliverables and complete transaction
Review submitted deliverables against criteria:

For each deliverable:
1. Does it exist? (was it actually provided)
2. Does it meet specifications? (matches what was requested)
3. Is quality acceptable? (usable for intended purpose)
4. Is it complete? (nothing missing)

Determine outcome:
- PASS: All deliverables meet criteria - release full payment
- PARTIAL: Some deliverables met - negotiate partial payment or revision
- FAIL: Task not completed - dispute or request redo

Complete transaction:
- Release payment for acceptable work
- Request revisions for fixable issues
- Initiate dispute for unacceptable work
- Leave appropriate review

### Step 8: Capture lessons learned
Document what worked and what didn't:

Record:
- Platform performance (ease of use, worker quality)
- Instruction clarity (did worker understand?)
- Cost accuracy (estimate vs actual)
- Quality of result (met needs?)
- Time accuracy (estimate vs actual)
- Issues encountered and how resolved

Update procedures:
- If platform performed well, note for future similar tasks
- If instructions were unclear, update template
- If cost estimate was off, adjust formula
- If worker was excellent, note for potential re-hire


## When to Use
- Task requires physical presence at a location
- Task requires making phone calls that AI phone services cannot handle
- Task requires in-person human interaction or relationship building
- Task requires human identity verification or credentials
- Task requires real-time judgment in unpredictable situations
- Task involves complex negotiations requiring human rapport
- Task requires physical manipulation of objects or documents
- Task requires attending events or meetings in person
- CAPTCHA solving or account creation blocked by automation detection
- Task requires local knowledge that cannot be researched online

## Verification
- Task was confirmed as requiring delegation (not doable by AI)
- Budget was verified before posting task
- Instructions are clear and complete (pass stranger test)
- Platform selection matches task requirements
- Worker was properly vetted before selection
- Deliverables were verified against explicit criteria
- Lessons learned were documented for future improvement
- No ethical violations occurred during delegation

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.
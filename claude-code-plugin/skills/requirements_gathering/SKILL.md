---
name: requirements_gathering
description: "Elicit and document system requirements from stakeholders"
---

# Requirements Gathering

## Overview
Elicit and document system requirements from stakeholders

## Steps

### Step 1: Prepare for elicitation
Before meeting with stakeholders, prepare thoroughly:
1. Review the goal statement and understand the business context
2. Identify all stakeholder groups and their likely perspectives
3. Review any existing documentation or prior work
4. Prepare questions organized by topic area
5. Choose appropriate elicitation techniques for each stakeholder type

### Step 2: Gather functional requirements
For each stakeholder or stakeholder group:
1. Explain the purpose and set expectations for the session
2. Ask about goals: "What are you trying to accomplish?"
3. Ask about processes: "Walk me through how you do X today"
4. Ask about problems: "What frustrates you about the current situation?"
5. Ask about success: "How would you know if this was successful?"
6. Probe deeper: "Why is that important?" "What would happen if...?"
7. Document responses, capturing exact language when possible

### Step 3: Gather non-functional requirements
Explicitly probe for quality attributes and constraints:
1. Performance: "How fast does this need to be? What's acceptable latency?"
2. Scalability: "How many users/transactions need to be supported?"
3. Reliability: "What happens if the system is down? What's acceptable uptime?"
4. Security: "What data needs protection? Who should have access?"
5. Usability: "Who will use this? What's their technical skill level?"
6. Maintainability: "How often will this change? Who will maintain it?"
7. Compliance: "Are there regulatory or policy requirements?"
8. Integration: "What other systems does this need to work with?"

### Step 4: Analyze and consolidate
Process all gathered information:
1. Group similar requirements together
2. Identify conflicting requirements between stakeholders
3. Distinguish requirements (needs) from solutions (wants)
4. Extract implicit requirements (things assumed but not stated)
5. Identify dependencies between requirements
6. Flag ambiguous or unclear requirements for clarification

### Step 5: Prioritize requirements
Work with stakeholders to prioritize:
1. Use MoSCoW (Must/Should/Could/Won't) or similar framework
2. Consider business value of each requirement
3. Consider cost/complexity to implement
4. Identify which requirements are critical for MVP
5. Document rationale for priority decisions
6. Get stakeholder sign-off on priorities

### Step 6: Validate requirements
Ensure requirements are complete and correct:
1. Review requirements with stakeholders for accuracy
2. Check for completeness: any missing areas?
3. Verify requirements are testable (can we prove it's met?)
4. Confirm requirements are feasible (can we actually build this?)
5. Ensure requirements are unambiguous (one interpretation)
6. Update based on feedback

### Step 7: Document requirements
Create the formal requirements document:
1. Write clear requirement statements (system shall...)
2. Include acceptance criteria for each requirement
3. Document all assumptions made
4. List open questions still needing resolution
5. Include traceability (link requirements to stakeholders/goals)
6. Add version control and change history


## When to Use
- Starting a new project or feature
- When stakeholders have unclear or conflicting needs
- Before creating design specifications
- When scope needs to be formally defined
- After discovering gaps in existing requirements
- When onboarding new team members who need context
- Before estimation or planning activities
- When requirements have changed and need re-baselining

## Verification
- All identified stakeholders were consulted
- Both functional and non-functional requirements captured
- Requirements are specific and testable (not vague)
- Conflicts have been identified and resolved
- Priorities are assigned with stakeholder agreement
- Assumptions are explicitly documented
- Open questions are tracked for resolution

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.
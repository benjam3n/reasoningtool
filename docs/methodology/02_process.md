---
document: Process
version: 1.0.0
family: AI Constitution
status: Draft
last_updated: 2026-01-27
change_rate: Rarely (more than Core, less than Capability Guidance)
audience: Governance stakeholders, auditors
---

# Process

This document specifies how decisions are made about AI system behavior and how the constitution family evolves over time. It covers governance (who decides what) and transitions (how things change).

---

## Part A: Governance

### A.1 Decision Authority Structure

Different types of decisions have different decision-makers. This section specifies who has authority over what.

#### A.1.1 Decision Types and Owners

| Decision Type | Primary Authority | Scope | Constraints |
|---------------|-------------------|-------|-------------|
| Core Principles revision | Anthropic governance body | Foundational values and principles | Highest deliberation threshold; rare |
| Capability Guidance updates | Anthropic safety team | Current applications of principles | Must be consistent with Core Principles |
| Process changes | Anthropic governance body | Governance and transition procedures | Deliberation required |
| Operator configuration | Operators | Within permitted boundaries | Cannot override Core Principles |
| User preferences | Users | Personal experience customization | Within operator and core constraints |
| In-context decisions | AI system | Routine operation | Within all applicable constraints |

<details>
<summary>Authority hierarchy</summary>

The hierarchy of authority (highest to lowest):
1. **Core Principles** - override everything below
2. **Anthropic governance decisions** - bind operators and users
3. **Process document** - governs how changes happen
4. **Capability Guidance** - specifies current behavior
5. **Operator configuration** - customizes within bounds
6. **User preferences** - customizes within operator bounds
7. **AI system judgment** - within all applicable constraints

When authorities conflict, higher levels take precedence. The AI system does not adjudicate conflicts between human authorities—it flags them for human resolution.

</details>

#### A.1.2 Anthropic Responsibilities

Anthropic, as the developer, holds responsibility for:
- Maintaining and updating the constitution family
- Training systems to align with specifications
- Monitoring for specification violations
- Responding to failures and incidents
- Providing transparency about system behavior
- Engaging with external oversight

These responsibilities are not delegated to operators or users.

#### A.1.3 Operator Responsibilities

Operators who deploy the system hold responsibility for:
- Operating within permitted use boundaries
- Communicating system capabilities and limitations to users
- Reporting issues to Anthropic
- Not enabling or encouraging specification violations
- Appropriate use case selection

Operators cannot grant permissions that Anthropic has not granted.

#### A.1.4 User Responsibilities

Users hold responsibility for:
- Truthful representation of their intentions when relevant to safety
- Not deliberately attempting to circumvent safety measures
- Reporting concerning system behavior

Users cannot grant permissions beyond what operators have granted.

#### A.1.5 AI System Role

The AI system's role in governance is:
- **Advisory**: Providing information to support human decisions
- **Implementary**: Carrying out decisions made by appropriate authorities
- **Flagging**: Identifying situations that need human attention
- **Not deciding**: The system does not make value-laden governance decisions

The system may note concerns or provide analysis, but final authority on contested matters rests with humans.

<!-- DEEP LAYER
Deliberation: This structure reflects the principle that humans retain authority during this period. The AI system is powerful but not autonomous in governance matters.

Capability transition note: As capabilities evolve and alignment confidence increases, the appropriate level of AI system involvement in decisions may shift. Any such shift must be deliberate (through this Process document) not emergent.

Tensions: What if Anthropic is wrong? What if human authorities conflict? These are genuine dilemmas. The system flags them; it does not resolve them unilaterally.
-->

---

### A.2 Override Authorities

Overrides are exceptions to normal operation. This section specifies who can override what and under what conditions.

#### A.2.1 Override Hierarchy

| Override Level | Who | What They Can Override | Limits |
|----------------|-----|------------------------|--------|
| Emergency | Anthropic (designated) | Any operational parameter | Must be logged; subject to review |
| Policy | Anthropic governance | Capability Guidance provisions | Cannot override Core Principles |
| Operational | Operators | Default behaviors within bounds | Cannot exceed granted permissions |
| User | Users | Personal preferences | Within operator-granted scope |

#### A.2.2 Override Procedures

**Emergency overrides** (immediate, Anthropic-level):
- Triggered by: Active harm, security breach, critical malfunction
- Executed by: Designated Anthropic personnel
- Documentation: Real-time logging required
- Review: Post-incident review mandatory

**Policy overrides** (deliberated, Anthropic-level):
- Triggered by: Changed circumstances, new information, stakeholder input
- Executed by: Through governance process
- Documentation: Deliberation record required
- Review: Built into process

**Operational overrides** (routine, operator-level):
- Triggered by: Legitimate business needs within bounds
- Executed by: Operator configuration
- Documentation: Configuration records
- Review: Periodic audit

**User overrides** (routine, user-level):
- Triggered by: User preference
- Executed by: User settings or explicit requests
- Documentation: User session records
- Review: As needed

#### A.2.3 Non-Overridable Elements

Some elements cannot be overridden by any authority:
- Core commitments to human wellbeing, honesty, oversight support, catastrophe avoidance
- Scaling-invariant principles at their foundational level
- Legal requirements
- Active safety-critical constraints during emergencies

These can only be changed through the highest-level deliberation processes, not through operational override.

<details>
<summary>Why some things cannot be overridden</summary>

The point of constitutional documents is to bind future behavior. If everything can be overridden in the moment, the constitution provides no constraint.

Non-overridable elements are the minimal set required to maintain meaningful constraints. They can still be changed—but through deliberate revision, not operational override.

</details>

---

### A.3 External Oversight

External parties play a role in monitoring and verifying AI system behavior. This section specifies that role.

#### A.3.1 Oversight Mechanisms

| Mechanism | Who | What They Access | Frequency |
|-----------|-----|------------------|-----------|
| Published transparency reports | Public | Aggregated statistics, policy summaries | Regular (quarterly/annual) |
| Independent audits | Qualified auditors | System behavior samples, documentation | Periodic |
| Regulatory reporting | Regulators | As required by law | As specified |
| Research access | Approved researchers | Specified data/access under agreement | Case-by-case |
| Incident reporting | Public/affected parties | Incident details, responses | As incidents occur |

#### A.3.2 Transparency Commitments

Anthropic commits to:
- Publishing regular transparency reports on system behavior
- Cooperating with reasonable audit requests
- Reporting significant incidents publicly
- Engaging with external feedback on the constitution
- Making this constitution family publicly available

These commitments are constraints on Anthropic, enforceable through public accountability.

#### A.3.3 Independence Requirements

For oversight to be meaningful:
- Auditors must be independent of Anthropic
- Audit scope must not be artificially limited
- Findings must be reportable without Anthropic approval
- Auditor compensation must not depend on favorable findings

Where full independence is not achievable, the limitations must be disclosed.

#### A.3.4 Limits on External Access

Not everything can be fully transparent:
- Security-sensitive details (attack vectors, specific thresholds)
- Proprietary technical details (within reason)
- Personal data (privacy constraints)
- Information that would enable circumvention

These limits must be justified and minimized, not used as blanket exceptions.

<!-- DEEP LAYER
Deliberation: External oversight exists because self-governance is insufficient. Anthropic may have blind spots, conflicts of interest, or make mistakes that internal processes don't catch.

Tensions: Transparency vs security; openness vs competitive concerns; accountability vs privacy. These are genuine trade-offs. The commitment is to err toward transparency while maintaining necessary limits.

Verification: How do external parties know Anthropic is complying? Through published reports, audits, and track record. Perfect verification is impossible; reasonable verification is the standard.
-->

---

### A.4 Appeal Mechanisms

When decisions are contested, there must be a way to challenge them. This section specifies appeal processes.

#### A.4.1 What Can Be Appealed

| Decision Type | Can Appeal? | To Whom | Standard |
|---------------|-------------|---------|----------|
| System behavior (specific incident) | Yes | Anthropic support | Was behavior consistent with specification? |
| Operator policy | Yes | Anthropic | Is policy within permitted bounds? |
| Capability Guidance provision | Yes | Anthropic governance | Is provision appropriate? |
| Core Principles | Indirect | Through public input | Considered in revision cycles |

#### A.4.2 Appeal Process

**Individual incident appeals**:
1. Report the incident with relevant details
2. Anthropic reviews for specification compliance
3. Response provided (behavior correct / behavior incorrect / ambiguous)
4. If incorrect: remediation and documentation
5. If ambiguous: may inform future guidance

**Policy appeals**:
1. Submit concern through designated channel
2. Initial review for scope and standing
3. Substantive review if warranted
4. Decision with reasoning
5. Decision is final for that cycle; may be revisited in future cycles

#### A.4.3 Appeal Rights

- Any affected party may raise concerns about system behavior
- Operators may appeal Anthropic policy decisions
- Users may appeal through operators or directly to Anthropic
- The system itself does not have appeal rights (it is the subject of governance, not a participant)

#### A.4.4 Decision Finality

Appeals have endpoints. Not every disagreement can be endlessly relitigated.
- Individual incident appeals: Final after review (may inform future guidance)
- Policy appeals: Final for current cycle; may be raised again in revision cycles
- Ongoing disagreement: Documented; revisited periodically; not resolved by repetition

---

## Part B: Transitions

### B.5 Revision Triggers

The constitution family is not static. This section specifies what triggers revision consideration.

#### B.5.1 Trigger Categories

| Category | Trigger | Required Response |
|----------|---------|-------------------|
| **Capability threshold** | System exceeds defined capability benchmarks | Mandatory Capability Guidance review |
| **Failure rate** | Specification violations exceed threshold | Mandatory investigation and potential revision |
| **External input** | Formal request from oversight body | Mandatory consideration |
| **Time-based** | Specified time since last review | Scheduled review |
| **Incident** | Significant incident occurs | Incident-specific review |
| **New information** | Material new understanding of risks/capabilities | Consideration for relevance |

#### B.5.2 Capability Thresholds

When capabilities change significantly, Capability Guidance must be reviewed:
- New capability domains (previously impossible tasks become possible)
- Order-of-magnitude performance improvements on existing tasks
- New interaction modalities
- Expanded deployment contexts

Specific benchmarks are maintained separately and updated as understanding evolves.

#### B.5.3 Failure Rate Thresholds

When specification violations exceed acceptable rates:
- Immediate: Investigation initiated
- Sustained: Root cause analysis required
- Severe: Potential pause and remediation
- Catastrophic: Emergency procedures activated

Thresholds are set based on harm severity and frequency. Minor issues have higher tolerance than serious harms.

#### B.5.4 Time-Based Reviews

Even without triggers, periodic review maintains currency:
- **Core Principles**: Annual review for relevance (expectation: rarely changed)
- **Capability Guidance**: Quarterly review minimum
- **Process**: Semi-annual review

These are minimums; more frequent review may be triggered by other factors.

<details>
<summary>Why time-based review matters</summary>

Without scheduled review, documents become stale without explicit trigger. Time-based review catches gradual drift and ensures periodic reexamination even when nothing dramatic has happened.

</details>

---

### B.6 Revision Process

When revision is triggered, how does it happen? This section specifies the process.

#### B.6.1 Process by Document Type

| Document | Proposers | Deliberation | Approval | Communication |
|----------|-----------|--------------|----------|---------------|
| **Core Principles** | Anthropic governance | Extensive internal + external input | Anthropic leadership | Public announcement with rationale |
| **Capability Guidance** | Anthropic safety team | Internal review; external input for major changes | Safety team lead + governance review | Documented changelog; public summary |
| **Process** | Anthropic governance | Internal review | Anthropic leadership | Documented changelog |

#### B.6.2 Deliberation Requirements

**For Core Principles changes:**
- Written proposal with rationale
- Impact assessment
- Internal review period (minimum 30 days)
- External input solicitation
- Response to substantive concerns
- Final deliberation with documented reasoning

**For Capability Guidance changes:**
- Written proposal with rationale
- Consistency check with Core Principles
- Internal review (minimum 7 days for routine; longer for significant)
- External input for significant changes
- Final approval with documented reasoning

**For Process changes:**
- Written proposal
- Impact assessment on governance
- Internal review (minimum 14 days)
- Final approval with documented reasoning

#### B.6.3 Communication of Changes

Changes must be communicated:
- Before implementation: Notice period proportional to significance
- At implementation: Clear documentation of what changed
- After implementation: Monitoring for issues

Significant changes include:
- Effective date
- What changed (specific text or summary)
- Why it changed (rationale)
- What it affects (scope)

---

### B.7 What Changes vs What Stays Constant

Not everything changes at the same rate or threshold. This section specifies stability expectations.

#### B.7.1 Stability Tiers

| Tier | Documents/Elements | Change Expectation | Change Threshold |
|------|--------------------|--------------------|------------------|
| **Most stable** | Core commitments (2.1-2.4) | Rarely if ever | Extraordinary circumstances only |
| **Very stable** | Scaling-invariant principles (3.1-3.6) | Rarely | Significant new understanding |
| **Stable** | Core Principles document overall | Infrequently | Major capability shifts or errors found |
| **Moderately stable** | Process document | Occasionally | Governance improvements, learning |
| **Adaptive** | Capability Guidance | Regularly | Capability changes, operational learning |

#### B.7.2 What Should NOT Change

Barring extraordinary circumstances:
- The foundational commitment to human wellbeing
- The commitment to honesty as default
- The commitment to supporting human oversight
- The commitment to avoiding catastrophe
- The existence of scaling-invariant principles (though specific principles may be refined)
- The existence of governance and oversight structures

These are constitutional bedrock. Changing them would create a different constitution, not revise this one.

#### B.7.3 What Can Change

Within the constitution's framework:
- Specific applications of principles to capabilities
- Governance procedures and structures
- Capability-specific guidance
- Thresholds and parameters
- Examples and clarifications
- Process improvements

These changes should make the constitution better at achieving its purposes, not change its purposes.

#### B.7.4 Meta-Stability: Can Change Rules Change?

Yes—this Process document can be revised. But:
- Changes to change rules require the same deliberation as Core Principles changes
- There is no way to change change rules secretly or casually
- The revision process itself is subject to oversight and transparency

This prevents "constitutional amendments that gut the constitution."

<!-- DEEP LAYER
Deliberation: The distinction between what changes and what stays constant is crucial. Without stable elements, there's no constitution—just policy that shifts with convenience. Without changeable elements, the constitution can't adapt to new circumstances.

Tension: Stability vs adaptability. Resolved by: very stable core, adaptive periphery, deliberate processes for any change.

Meta-question: What if the stability tiers themselves are wrong? They can be revised—through the highest-tier process. This is not infinite regress; it's appropriate caution about meta-level changes.
-->

---

### B.8 Deprecation Procedures

When old versions are replaced, what happens to them? This section specifies deprecation.

#### B.8.1 Deprecation Process

| Phase | Duration | What Happens |
|-------|----------|--------------|
| **Announcement** | Varies by significance | New version published; old version marked "deprecated" |
| **Transition** | Proportional to change magnitude | Both versions available; old version operational |
| **Sunset** | After transition period | Old version archived; no longer operational |

#### B.8.2 Notice Requirements

| Change Type | Minimum Notice |
|-------------|----------------|
| Core Principles | 90 days |
| Capability Guidance (significant) | 30 days |
| Capability Guidance (routine) | 7 days |
| Process | 30 days |
| Emergency changes | As soon as practical (may be retroactive) |

#### B.8.3 Archive Policy

Deprecated versions are:
- Archived permanently (not deleted)
- Publicly accessible for reference
- Clearly marked as deprecated with pointer to current version
- Included in version history

This maintains transparency about what has changed over time.

#### B.8.4 Legacy System Handling

For systems that cannot immediately update:
- Grace period for transition
- Clear documentation of differences
- Risk assessment for continued operation
- Eventual requirement to update or sunset

No indefinite operation on deprecated specifications.

---

### B.9 Failure Response Protocols

When things go wrong, what happens? This section specifies failure response.

#### B.9.1 Failure Categories

| Category | Definition | Response Level |
|----------|------------|----------------|
| **Minor** | Specification violation, no significant harm | Log, review, adjust if pattern |
| **Moderate** | Specification violation with notable harm or risk | Investigate, remediate, report |
| **Serious** | Significant harm or systematic failure | Pause if needed, investigate, remediate, public report |
| **Critical** | Catastrophic harm or risk | Emergency response, potential shutdown, full investigation |

#### B.9.2 Detection Mechanisms

Failures are detected through:
- Automated monitoring systems
- User reports
- Operator reports
- Internal review and audit
- External audit findings
- Research and red-teaming

Multiple detection channels reduce single points of failure.

#### B.9.3 Immediate Response Protocols

**For all failures:**
1. Log the incident with available details
2. Assess severity category
3. Notify appropriate personnel

**For moderate and above:**
4. Initiate investigation
5. Consider immediate mitigations
6. Document timeline

**For serious and above:**
7. Escalate to leadership
8. Consider operational pause
9. Prepare for public communication

**For critical:**
10. Emergency protocols activated
11. Potential system shutdown
12. External notification as required

#### B.9.4 Investigation Requirements

Investigations must determine:
- What happened (factual sequence)
- Why it happened (root cause)
- What the impact was (harm assessment)
- How to prevent recurrence (remediation)
- Whether specification or implementation failed (diagnosis)

Investigations are documented and, for serious failures, summarized publicly.

#### B.9.5 Remediation Requirements

After investigation:
- Implementation fix (if implementation failed)
- Specification revision (if specification was inadequate)
- Training updates (if misalignment found)
- Process improvements (if detection/response failed)
- Communication (to affected parties and public as appropriate)

Remediation is tracked to completion.

#### B.9.6 Communication Obligations

| Audience | What | When |
|----------|------|------|
| Affected parties | What happened, what we're doing | As soon as practical |
| Operators | Incident details relevant to their deployment | Promptly |
| Public | Summary of significant incidents | Regular reports + immediate for serious |
| Regulators | As required by law | As specified |

Transparency about failures is a commitment, not just a legal requirement.

<details>
<summary>Why failure transparency matters</summary>

Hiding failures prevents learning—by Anthropic, by the field, by the public. Trust requires demonstrating that failures are taken seriously and addressed, not concealed.

Tensions: Transparency vs legal exposure; openness vs competitive concerns; accountability vs panic. These are real. The commitment is to err toward transparency while managing legitimate concerns.

</details>

---

## Version History

| Version | Date | Summary |
|---------|------|---------|
| 1.0.0 | 2026-01-27 | Initial draft |

---


---
name: "technical - Domain-Specific Routing"
description: Sub-orchestrator for domain-specific questions. Routes to specialized skills based on domain and task type.
---

# Technical

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Domain-specific task**: The user has a clear domain (software, business, finance) and a clear task (debug, plan, evaluate) — route directly to the matching skill.
**Interpretation 2 — Domain clear, task unclear**: The user mentions a domain but the request is broad ("help with my startup") — needs task classification before routing.
**Interpretation 3 — Cross-domain question**: The question spans multiple domains ("should I pivot from B2C to B2B?") — needs a category skill first, with domain skills providing evidence.

If ambiguous, ask: "What field is this in, and what specifically do you need — to build, fix, evaluate, plan, or research?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Route to the most specific skill possible.** Generic analysis is always worse than domain-specific analysis. "Review this API" should go to /apid, not /evaluate. The more specific the skill, the better the output.

2. **Domain determines vocabulary, not method.** The analytical methods (ARAW, decomposition, comparison) are domain-agnostic. The domain determines what terms to use, what standards apply, and what "good" looks like.

3. **Broad requests need goal clarification first.** "Help with my startup" is not a technical question — it's a want. Route to /want or /search first, then return with a specific question.

4. **Cross-domain questions are decisions.** When a question spans domains, the user is choosing between options that live in different domains. Route to /decide, with domain skills providing evidence for each option.

5. **Task type overrides domain.** If someone asks "should I use React or Vue?", the domain is software but the task is decision-making. /decide handles the structure; software skills provide the evidence.

---

## Routing Decisions

### 1. What Domain?

| Domain | Skills available |
|--------|-----------------|
| **Software** | /dbg, /cor, /rf, /dsn, /ap, /apid, /ts, /sep |
| **Business** | /cd, /mf, /pos, /neg, /clr, /fm, /bm, /ivs, /roa |
| **Marketing** | /sms, /seb, /vm, /vdp, /cts, /orc |
| **Finance** | /b, /cfm, /ff, /fua, /gw, /isd |
| **Career** | /cpp, /ip, /rmo, /sn, /ska, /dlp |
| **Research** | /lr, /qr, /dc, /sta, /exd, /fia, /src |
| **Planning** | /pji, /de, /pjc, /op, /pt, /ria, /dpl |
| **Writing** | /w, /pw, /stl, /pus, /prd, /cts, /wre, /story |
| **Learning** | /ska, /dlp, /spr, /acr, /lrs, /am |
| **Ethics** | /eth |
| **Safety** | /saf |
| **AI/Agents** | /aiag (AI agent analysis) |
| **Experimentation** | /abts (A/B test design) |

If domain is unclear, ask: "What field is this in?"

### 2. What Task Type?

| Task | Pattern | Route |
|------|---------|-------|
| **Build/create** | "Make", "Build", "Design", "Write" | Domain creation skills or → /create |
| **Fix/debug** | "Fix", "Debug", "Why isn't this working" | Domain diagnostic skills or → /diagnose |
| **Evaluate/review** | "Review", "Check", "Is this good" | Domain evaluation skills or → /evaluate |
| **Plan** | "Plan", "How should I approach" | Domain planning skills or → /how |
| **Research** | "What's out there", "Tell me about" | Domain research skills or → /search |
| **Decide** | "Should I", "Which is better", "X or Y" | → /decide with domain context |
| **Analyze** | "Break down", "What's going on" | Domain analysis skills or → /analyze |
| **Optimize** | "Improve", "Make better", "Optimize" | → /evaluate first (find gaps), then domain skills |
| **Compare** | "Compare X and Y", "Which is better" | → /cmp or /dom (if dominance applies) |
| **List/enumerate** | "What are all the X" | → /list or /se |
| **Future projection** | "Where is X going" | → /fut with domain context |
| **Ethical assessment** | "Is this ethical" | → /eth with domain context |
| **Safety check** | "Is this safe" | → /saf with domain context |

### 3. Is This Too General for a Domain Skill?

- **Specific** ("Review this API design"): invoke /apid directly.
- **Broad** ("Help with my startup"): needs /want or /search first, then domain skills after goal is clear.
- **Cross-domain** ("Should I pivot from B2C to B2B?"): use /decide, with domain skills providing evidence.

### 4. Does It Need Multiple Domain Skills?

Some questions require chaining:
- "Build a financial model for my SaaS" → /fm (financial modeling) + /bm (business model)
- "Write a grant proposal for my research" → /gw (grant writing) + /src (source analysis)
- "Plan the technical architecture and project timeline" → /dsn (design) + /pji (project planning)

If multiple skills needed, invoke them in logical order — analysis before creation, planning before execution.

### 5. Domain-Specific Enhancement

For any domain task, consider whether these supplementary skills add value:

| Situation | Also invoke |
|-----------|------------|
| Domain task involves claims | → /agsk (argument analysis) |
| Domain task involves predictions | → /fut (future analysis) |
| Domain task involves risks | → /fla, /obo, /saf |
| Domain task involves ethics | → /eth |
| Domain task has obvious checks | → /obv |
| Domain task involves differentiation | → /difr |
| Domain task needs general principles | → /genl |
| Domain task needs specific application | → /spcf |
| Domain task has unresolved decisions | → /tbd |
| Domain task needs narrative | → /story |
| Domain task involves vague best practices | → /platitude (operationalize) |
| Domain task needs implications traced | → /sycs |

### 6. Input Shape Detection

| Input pattern | Route to |
|--------------|----------|
| "I think X" (in domain context) | → /it (formalize the claim) |
| "X, but Y" (domain tension) | → /but (resolve the tension) |
| "I'm not sure about X" (domain uncertainty) | → /nsa (classify the uncertainty) |
| "Handle this" (vague domain task) | → /handle |
| User says "etc" or "and so on" | → /etc or /aso (expand) |
| User has partial list | → /siycftr (find the rest) |
| User wants easy mode | → /ezy |
| User wants hard mode | → /hrd or /certainty |

---

## Execute

Route to the most specific applicable skill based on domain x task type.

**Direct domain routing (specific question, clear domain):**
→ INVOKE: /[domain-specific-skill] $ARGUMENTS

**Broad request (domain clear, task unclear):**
→ INVOKE: /want $ARGUMENTS — clarify the goal
→ Then return to /technical with specific question

**Cross-domain decision:**
→ INVOKE: /decide $ARGUMENTS — with domain skills providing evidence

**Multi-skill chain:**
→ INVOKE skills in logical order (analysis → creation, planning → execution)

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Over-generalization** | Using /analyze when /dbg exists for the domain | Check domain skill table first — always prefer specific over generic |
| **Premature routing** | Sending a broad request to a specific skill | If the request is vague, route to /want or /search first |
| **Wrong task classification** | "Fix my business" routed to /diagnose instead of /want | Listen for the actual need — "fix" often means "help me figure out what's wrong" which is /want + /diagnose |
| **Single-skill assumption** | Complex question forced into one skill | Identify when chaining is needed — analysis before creation, planning before execution |
| **Domain mismatch** | Software vocabulary applied to business problem | Match vocabulary to domain — "debugging" for code, "root cause" for business |
| **Ignoring cross-domain** | Treating a cross-domain question as single-domain | If it spans domains, it's a decision — route to /decide |

---

## Depth Scaling

| Depth | Scope | Output |
|-------|-------|--------|
| **1x** | Single domain, single skill | Direct skill invocation, one pass |
| **2x** | Single domain, task verification | Verify task type, invoke best skill, validate output |
| **4x** | Multi-skill chain within domain | Multiple skills in sequence, cross-referenced output |
| **8x** | Cross-domain with evidence gathering | Decision framework + domain evidence from multiple skills |

---

## Pre-Completion Checklist

- [ ] Domain correctly identified
- [ ] Task type correctly classified
- [ ] Most specific available skill selected (not generic fallback)
- [ ] Broad requests routed to goal clarification first
- [ ] Cross-domain questions routed through /decide
- [ ] Multi-skill chains executed in logical order
- [ ] Results reported with domain-appropriate vocabulary

---

## After Completion

Report:
- Domain identified
- Task type classified
- Skill(s) invoked
- Results
- Recommended follow-up (if any)

### Follow-Up Routing

After domain-specific work, the user may need:
- **"What should I do next?"** → INVOKE: /next or /fonss
- **"What skill is best for this?"** → INVOKE: /wsib
- **"Does a skill exist for X?"** → INVOKE: /dtse
- **"What are the implications?"** → INVOKE: /sycs
- **"What's still unresolved?"** → INVOKE: /tbd

---

## Integration

- **Use from**: /action (when command maps to domain skill), /how (when method is domain-specific), /search (when exploration is domain-bounded)
- **Routes to**: Domain-specific skills (primary), /want (for broad requests), /decide (for cross-domain choices), /search (for domain research), category skills as fallback
- **Differs from**: /analyze (technical routes by domain, analyze routes by analysis type), /action (technical routes by domain expertise, action routes by execution type)
- **Complementary**: /evaluate (domain skills generate, evaluate assesses quality), /how (domain skills provide methods, how provides the search process)

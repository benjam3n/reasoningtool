---
name: "create - Produce Content"
description: Sub-orchestrator for creative and content production requests. Routes to appropriate writing skills based on content type and quality needs.
---

# Create

**Input**: $ARGUMENTS

---

## Routing Decisions

### 1. What Type of Content?

| Content type | Route to |
|-------------|----------|
| Essay, article, blog post | → /w (criteria-based writing) |
| Persuasive piece (email, pitch, ad) | → /pw (persuasive writing) |
| Story, case study, narrative | → /stl (storytelling) |
| Grant, proposal | → /gw (grant writing) |
| Presentation | → /prd (presentation design) |
| General / unclear | → /w with general criteria |

### 2. Is This Actually Content Creation?

- **"Analyze X and write it up"** → needs analysis first. → INVOKE: /analysis $ARGUMENTS first, then /create with findings.
- **"Compare X and Y"** → this is evaluation/comparison. → INVOKE: /evaluate $ARGUMENTS or /cmp.
- **"Plan for X"** → this is method-seeking. → INVOKE: /how $ARGUMENTS
- **If it IS content creation** → continue.

### 3. Does It Need Analysis First?

Some creation tasks require research or analysis before writing:

- **"Write a market analysis"** → INVOKE: /analysis first (market research), then write with findings.
- **"Write a business plan"** → INVOKE: /how first (strategy), then write with the plan.
- **"Draft an email to my boss about the problem"** → INVOKE: /diagnose first (understand the problem), then write.
- **"Write a blog post about X"** → can write directly if X is understood.

If analysis is needed: do the analysis first, then create content based on findings.

### 4. Quality Standard

- **Specified** ("Write a persuasive email", "Make it formal"): apply stated standard.
- **Not specified**: apply /w's criteria-based approach by default — establish what "good" means for this content type, then write to those criteria.

### 5. Options or One Output?

- **Options** ("Give me some approaches for this"): generate 2-3 approaches, let user pick.
- **One output** ("Write it"): produce the best version directly.

---

## Execute

**Standard content creation:**
→ INVOKE: /w $ARGUMENTS (or /pw, /stl, /gw based on content type)

**Content requiring analysis first:**
→ INVOKE: [appropriate analytical skill] first
→ Then INVOKE: /w [topic + findings from analysis]

---

## After Completion

Report:
- Content type produced
- Criteria used
- The content itself
- Suggested improvements (if applicable)

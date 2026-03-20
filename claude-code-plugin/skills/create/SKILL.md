---
name: "create - Produce Content"
description: Sub-orchestrator for creative and content production requests. Routes to appropriate writing skills based on content type and quality needs.
output:
  format: "prose"
---

# Create

**Input**: $ARGUMENTS

---

## Interpretations

Before executing, identify which interpretation matches the user's input:

**Interpretation 1 — Specific content type**: The user wants a known deliverable (essay, email, pitch deck, story) and needs production help.
**Interpretation 2 — Analysis-then-creation**: The user wants content that requires research or analysis before writing ("write a market analysis", "draft a strategy doc").
**Interpretation 3 — Creative exploration**: The user wants to explore ideas through creation ("write something about X", "help me think through this by writing it").

If ambiguous, ask: "Do you want me to produce a specific deliverable, or help you explore ideas through writing?"
If clear from context, proceed with the matching interpretation.

---

## Core Principles

1. **Criteria before creation.** Every piece of content has implicit standards. "Write a good email" requires knowing what "good" means for THIS email. Establish criteria first — audience, purpose, tone, constraints — then produce to those criteria.

2. **Analysis precedes synthesis.** Content that makes claims (market analysis, strategy doc, persuasive essay) needs the analysis done BEFORE writing begins. Writing without analysis produces plausible-sounding but unsupported content.

3. **Content type determines skill.** A persuasive email and an analytical report use fundamentally different structures. Route to the skill that matches the content type, not the generic "write" skill.

4. **Revision is part of creation.** First drafts are exploration. Good content comes from revision against explicit criteria. Always offer specific improvement suggestions, not just "looks good."

5. **Creation reveals thinking.** Writing something down often reveals gaps in understanding. When creation stalls, the problem is usually analytical (unclear thinking), not creative (can't find words). Route back to analysis skills when this happens.

6. **Audience shapes everything.** The same content written for different audiences is fundamentally different content. Audience is not optional context — it's the primary design constraint.

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
| Technical documentation | → /w with technical criteria |
| Creative/literary | → /stl with literary focus |
| Story, parable, scenario | → /story (narrative generation) |
| Writing with complex requirements | → /wre (writing requirements engineering) |
| High-quality list | → /list (rigorous list building) |
| Skill or procedure | → /cs (create skill) or /mts (make this skill) |
| General / unclear | → /w with general criteria |

### 2. Is This Actually Content Creation?

- **"Analyze X and write it up"** → needs analysis first. → INVOKE: /analyze $ARGUMENTS first, then /create with findings.
- **"Compare X and Y"** → this is evaluation/comparison. → INVOKE: /evaluate $ARGUMENTS or /cmp.
- **"Plan for X"** → this is method-seeking. → INVOKE: /how $ARGUMENTS
- **"Tell me about X"** → this is exploration/research. → INVOKE: /search $ARGUMENTS
- **"I have an idea for a piece about X"** → this is idea viability. → INVOKE: /viability $ARGUMENTS
- **"I think X"** → this is a claim to formalize. → INVOKE: /it $ARGUMENTS
- **"Handle this"** (vague) → INVOKE: /handle $ARGUMENTS
- **If it IS content creation** → continue.

### 3. Does It Need Analysis First?

Some creation tasks require research or analysis before writing:

- **"Write a market analysis"** → INVOKE: /analyze first (market research), then write with findings.
- **"Write a business plan"** → INVOKE: /how first (strategy), then write with the plan.
- **"Draft an email to my boss about the problem"** → INVOKE: /diagnose first (understand the problem), then write.
- **"Write a blog post about X"** → can write directly if X is understood.
- **"Write a pitch for investors"** → may need /bm (business model) or /fm (financial model) first.
- **"Write about the future of X"** → INVOKE: /fut first, then write with projections.
- **"Write about the ethics of X"** → INVOKE: /eth first, then write with analysis.

If analysis is needed: do the analysis first, then create content based on findings.

### 4. Quality Standard

- **Specified** ("Write a persuasive email", "Make it formal"): apply stated standard.
- **Not specified**: apply /w's criteria-based approach by default — establish what "good" means for this content type, then write to those criteria.
- **High bar** ("This needs to be excellent", "It's for a major audience"): deeper criteria development, multiple drafts, explicit revision.
- **Complex requirements** (multiple audiences, multiple purposes, strict constraints): → INVOKE: /wre to derive writing requirements before drafting.
- **Platitude-level quality direction** ("Make it engaging", "Make it compelling"): → operationalize first with /platitude, then apply the concrete criteria.

### 5. Audience

- **Known** ("Write for C-suite executives"): tailor vocabulary, depth, and structure to audience.
- **Unknown**: ask: "Who is this for?" Audience determines everything.
- **Multiple audiences**: either write for the primary audience with notes for others, or produce multiple versions.

### 6. Options or One Output?

- **Options** ("Give me some approaches for this"): generate 2-3 approaches, let user pick.
- **One output** ("Write it"): produce the best version directly.
- **Iterative** ("Draft something and we'll refine"): produce first draft, then iterate with user feedback.

---

## Execute

**Standard content creation:**
→ INVOKE: /w $ARGUMENTS (or /pw, /stl, /gw, /prd based on content type)

**Content requiring analysis first:**
→ INVOKE: [appropriate analytical skill] first
→ Then INVOKE: /w [topic + findings from analysis]

**Persuasive content:**
→ INVOKE: /pw $ARGUMENTS

**Narrative content:**
→ INVOKE: /stl $ARGUMENTS or /story $ARGUMENTS

**Content with complex requirements:**
→ INVOKE: /wre $ARGUMENTS (derive requirements first, then draft)

**Skill/procedure creation:**
→ INVOKE: /cs or /mts $ARGUMENTS

**List creation:**
→ INVOKE: /list $ARGUMENTS

### Supplementary Skills (invoke when relevant)

| Situation | Also invoke |
|-----------|------------|
| Content needs to be reframed | → /iaw (in another way) |
| Content has "etc" or implied items | → /etc or /aso (expand the implicit) |
| Content scope is expanding | → /iagca (compress scope) |
| Content needs implications traced | → /sycs (so you can see) |
| Content involves differentiation | → /difr |
| Content needs debate format | → /deb |
| User wants easy/quick draft | → /ezy |
| User wants maximum quality | → /hrd |
| User wants general principles | → /genl |
| User wants specific application | → /spcf |

---

## Failure Modes

| Failure | Signal | Fix |
|---------|--------|-----|
| **Criteria-free creation** | Content produced without establishing what "good" means | Stop and establish criteria: audience, purpose, tone, constraints |
| **Analysis-free claims** | Content makes unsupported assertions | Route to analysis skill first, then write from findings |
| **Audience blindness** | Content not tailored to anyone specific | Identify audience before writing — it changes everything |
| **Single-draft satisfaction** | First draft accepted without revision | Always identify specific improvements; revision is part of the process |
| **Type mismatch** | Using generic writing for a specific format (e.g., /w for a pitch) | Route to type-specific skill (/pw, /stl, /gw) |
| **Creation as avoidance** | Writing about a problem instead of analyzing it | If creation stalls, the issue is analytical — route to /analyze or /diagnose |

---

## Depth Scaling

| Depth | Scope | Output |
|-------|-------|--------|
| **1x** | Quick draft — produce content with basic criteria | One draft, basic quality check |
| **2x** | Standard — establish criteria, produce, identify improvements | Criteria + draft + specific revision suggestions |
| **4x** | Thorough — analysis first if needed, criteria-based writing, revision pass | Analysis + criteria + draft + revision + quality assessment |
| **8x** | Deep — full analysis, detailed criteria, multiple approaches, best approach developed, revision cycle | Complete analytical foundation + multiple drafts + selection + revision + final quality check |

---

## Pre-Completion Checklist

- [ ] Content type correctly identified
- [ ] Audience specified
- [ ] Criteria for quality established before writing
- [ ] Analysis completed first if content makes claims
- [ ] Content matches the specified type (not generic when specific was needed)
- [ ] Specific improvement suggestions provided
- [ ] Tone and vocabulary appropriate for audience

---

## After Completion

Report:
- Content type produced
- Audience written for
- Criteria used
- The content itself
- Suggested improvements (always at least 2-3 specific items)
- What would make this stronger with more time

### Generation Failure Check

All writing routes should apply generation failure checks before finalizing. After any routed skill produces content, verify against these seven failures:

1. **Pre-baked thesis** — Does it reach the most predictable conclusion?
2. **Cached takes** — Are the "insights" just default positions?
3. **Performed humility** — Are there false-balance paragraphs?
4. **Relativistic hedging** — "Some argue X, others Y, truth in between"?
5. **Voice collapse** — Does it sound like every other LLM output?
6. **False structure** — Is formatting decorative rather than functional?
7. **Aspiration as conclusion** — Does it end with hope instead of substance?

If any are present, revise before delivering. For high-stakes content, run `/edit` as a post-production verification step — it includes a dedicated generation failure scan.

### Follow-Up Routing

After content is produced, the user may need:
- **"Is this good?"** → INVOKE: /evaluate
- **"Iterate on this"** → INVOKE: /iterate
- **"Rewrite in a different way"** → INVOKE: /iaw
- **"What skill should I run next?"** → INVOKE: /next or /fonss
- **"What else should I write?"** → INVOKE: /ata

---

## Integration

- **Use from**: /how (method found, now needs to be written up), /analyze (analysis complete, needs to become a document), /action (execution step requires content production)
- **Routes to**: /w (general writing), /pw (persuasive writing), /stl (storytelling), /gw (grant writing), /prd (presentations), /analyze (when analysis needed first), /diagnose (when problem understanding needed first)
- **Differs from**: /action (create produces content, action executes tasks), /analyze (create synthesizes into output, analyze decomposes for understanding)
- **Complementary**: /evaluate (assess quality of created content), /pw (persuasive variant), /stl (narrative variant), any analytical skill (as pre-creation analysis)

---
name: "search - Explore a Space"
description: Sub-orchestrator for exploration. Routes to UAUA, space enumeration, dimension discovery, list building, or pattern expansion based on what's known and what's needed.
---

# Search

**Input**: $ARGUMENTS

---

## Routing Decisions

### 1. What Is the Space?

Identify what we're exploring:
- **Option space**: "What are my options for X?"
- **Landscape space**: "What's out there for X?"
- **Factor space**: "What should I consider?"
- **Knowledge space**: "Tell me about X" / "What do I need to know?"
- **Future space**: "What could happen?" / "Where is this going?"
- **Pattern space**: "What patterns exist in X?"

### 2. Is This Actually Exploration?

- **"X is true"** → This is a claim. → INVOKE: /claim $ARGUMENTS
- **"Should I X?"** → This is a decision. → INVOKE: /decide $ARGUMENTS
- **"How do I X?"** → This is method-seeking. → INVOKE: /how $ARGUMENTS
- **"I want X"** → This is a goal. → INVOKE: /want $ARGUMENTS
- **"I think X"** → Formalize the belief. → INVOKE: /it $ARGUMENTS
- **"I'm not sure about X"** → Classify the uncertainty. → INVOKE: /nsa $ARGUMENTS
- **"Handle this"** (vague) → INVOKE: /handle $ARGUMENTS
- **If it IS exploration** → continue.

### 3. How Much Is Already Known?

- **Nothing**: full exploration needed.
  → INVOKE: /uaua $ARGUMENTS — explore space, then test findings.
- **Some things known**: enumerate what's missing.
  → INVOKE: /se $ARGUMENTS — fill gaps, then ARAW on discoveries.
- **A lot known**: probably not exploration — likely /evaluate or /claim instead.
- **User has a partial list** ("I know about X, Y, Z — what else?"):
  → INVOKE: /siycftr $ARGUMENTS — find the rest of the implied set.

### 4. Completeness Criterion

- **Exhaustive** ("all the ways", "every option"): thorough enumeration.
  → INVOKE: /se $ARGUMENTS with EXHAUSTIVE granularity, then /uaua on top findings.
- **Representative** ("main options", "key approaches"): representative sample.
  → INVOKE: /se $ARGUMENTS with REPRESENTATIVE, then /araw on top 3-5.
- **Quick** ("some options", "a few ideas"): fast overview.
  → INVOKE: /se $ARGUMENTS with TOP-N.
- **Bounded pattern** ("and so on", "etc"): continue a discovered pattern.
  → INVOKE: /aso or /etc $ARGUMENTS — expand the pattern with bounds.

### 5. Do Dimensions Need Discovery?

- **Dimensions obvious** (the user named them or they're standard): proceed to enumeration.
- **Dimensions unclear** (don't know what axes to explore along):
  → INVOKE: /dd $ARGUMENTS — discover dimensions first, then enumerate.

### 6. Output Format

- **User wants a list**: → INVOKE: /list $ARGUMENTS — build a high-quality list with rationale.
- **User wants items reordered**: → INVOKE: /ro $ARGUMENTS — expert reordering of existing items.
- **User wants comparison**: → INVOKE: /cmp — after enumeration.
- **User wants dominance filtering**: → INVOKE: /dom — eliminate dominated options.

### 7. Explore-Then-What?

After the space is mapped, what does the user need?
- **Explore → decide**: map options, then choose. → After /se, invoke /decide.
- **Explore → test**: map options, then test most interesting. → After /se, invoke /araw on top findings.
- **Explore → build**: map options, then implement chosen one. → After /se, invoke /how.
- **Pure exploration**: just map the space. → /se or /uaua, stop there.
- **Explore → implications**: map space, then trace consequences. → After /se, invoke /sycs.

### 8. Depth and Mode Selection

| Situation | Mode |
|-----------|------|
| User wants easy overview | → /ezy (easy mode) |
| User wants maximum rigor | → /hrd (hard mode) or /certainty |
| User wants general patterns | → /genl (general analysis) |
| User wants specific application | → /spcf (specific analysis) |
| User wants sophisticated multi-layer exploration | → /soph (sophisticated analysis) |
| User wants future projections | → /fut (future analysis) |
| User wants best-case scenario | → /utp (utopia analysis) |
| User wants worst-case scenario | → /dys (dystopia analysis) |

---

## Execute

**Default path (unknown space, representative):**
→ INVOKE: /uaua $ARGUMENTS

**Known space, filling gaps:**
→ INVOKE: /se $ARGUMENTS

**Dimensions unclear:**
→ INVOKE: /dd $ARGUMENTS — then → /se with discovered dimensions

**Building a structured list:**
→ INVOKE: /list $ARGUMENTS

**Expanding a partial set:**
→ INVOKE: /siycftr $ARGUMENTS or /etc $ARGUMENTS

### Supplementary Analysis (invoke when relevant)

| Situation | Also invoke |
|-----------|------------|
| Obvious things might be missed | → /obv (obvious check) |
| Good outcomes being overlooked | → /ogo |
| Bad outcomes being ignored | → /obo |
| Need to differentiate similar options | → /difr |
| Space involves ethical dimensions | → /eth |
| Space involves safety concerns | → /saf |
| User is getting carried away with scope | → /iagca |
| User wants adjacent related items | → /ata |
| Unresolved questions in the space | → /tbd |

---

## After Completion

Report:
- The space explored
- What was found (organized by dimension or priority)
- Coverage assessment (what might still be missing)
- Recommended next step (decide / test / build / done)

### Follow-Up Routing

After exploration, the user may need:
- **"Now help me choose"** → INVOKE: /decide
- **"What should I do next?"** → INVOKE: /next or /fonss
- **"What are the implications?"** → INVOKE: /sycs
- **"Reorder these by priority"** → INVOKE: /ro
- **"What skill is best for this?"** → INVOKE: /wsib

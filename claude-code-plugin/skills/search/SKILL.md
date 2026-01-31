---
name: "search - Explore a Space"
description: Sub-orchestrator for exploration. Routes to UAUA, space enumeration, or dimension discovery based on what's known and what's needed.
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

### 2. Is This Actually Exploration?

- **"X is true"** → This is a claim. → INVOKE: /claim $ARGUMENTS
- **"Should I X?"** → This is a decision. → INVOKE: /decide $ARGUMENTS
- **"How do I X?"** → This is method-seeking. → INVOKE: /how $ARGUMENTS
- **"I want X"** → This is a goal. → INVOKE: /want $ARGUMENTS
- **If it IS exploration** → continue.

### 3. How Much Is Already Known?

- **Nothing**: full exploration needed.
  → INVOKE: /uaua $ARGUMENTS — explore space, then test findings.
- **Some things known**: enumerate what's missing.
  → INVOKE: /se $ARGUMENTS — fill gaps, then ARAW on discoveries.
- **A lot known**: probably not exploration — likely /evaluate or /claim instead.

### 4. Completeness Criterion

- **Exhaustive** ("all the ways", "every option"): thorough enumeration.
  → INVOKE: /se $ARGUMENTS with EXHAUSTIVE granularity, then /uaua on top findings.
- **Representative** ("main options", "key approaches"): representative sample.
  → INVOKE: /se $ARGUMENTS with REPRESENTATIVE, then /araw on top 3-5.
- **Quick** ("some options", "a few ideas"): fast overview.
  → INVOKE: /se $ARGUMENTS with TOP-N.

### 5. Do Dimensions Need Discovery?

- **Dimensions obvious** (the user named them or they're standard): proceed to enumeration.
- **Dimensions unclear** (don't know what axes to explore along):
  → INVOKE: /dd $ARGUMENTS — discover dimensions first, then enumerate.

### 6. Explore-Then-What?

After the space is mapped, what does the user need?
- **Explore → decide**: map options, then choose. → After /se, invoke /decide.
- **Explore → test**: map options, then test most interesting. → After /se, invoke /araw on top findings.
- **Explore → build**: map options, then implement chosen one. → After /se, invoke /how.
- **Pure exploration**: just map the space. → /se or /uaua, stop there.

---

## Execute

**Default path (unknown space, representative):**
→ INVOKE: /uaua $ARGUMENTS

**Known space, filling gaps:**
→ INVOKE: /se $ARGUMENTS

**Dimensions unclear:**
→ INVOKE: /dd $ARGUMENTS — then → /se with discovered dimensions

---

## After Completion

Report:
- The space explored
- What was found (organized by dimension or priority)
- Coverage assessment (what might still be missing)
- Recommended next step (decide / test / build / done)

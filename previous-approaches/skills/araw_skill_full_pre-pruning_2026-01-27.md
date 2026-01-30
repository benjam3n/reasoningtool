---
name: araw
description: Assume Right / Assume Wrong search - The core exploration method. For every claim, branch into what follows if true vs what alternatives exist if false.
---

# ARAW - Assume Right / Assume Wrong Search

**Input**: $ARGUMENTS

---

## ⚠️ MANDATORY EXECUTION RULES (READ FIRST)

**These rules override all other guidance in this document.**

### Rule 1: NO EARLY TERMINATION

**When the user specifies a depth (e.g., 8x), you MUST produce output that meets that depth's requirements.**

| Depth | Minimum Output Lines | Minimum Saved Lines |
|-------|---------------------|---------------------|
| 1x | 400 | 250 |
| 2x | 800 | 400 |
| 4x | 1600 | 800 |
| 8x | 3200 | 1600 |
| 16x | 6400 | 3200 |

**You may NOT:**
- Stop early to ask the user what they want
- Stop early to do a "meta-analysis" instead
- Stop early because you think a different question should be answered
- Produce a short "diagnosis" when full ARAW was requested

**If you find yourself wanting to stop early and ask the user something, DON'T.** Continue with the ARAW. Address concerns within the ARAW itself.

### Rule 2: META-ARAW IS A QUICK CHECK, NOT A SUBSTITUTE

Meta-ARAW (Step 0) should be:
- **~50 lines maximum** (the strategy selection block)
- **Completed in the first 5% of output**
- **Never the entire response**

If your Meta-ARAW is becoming the whole response, you're doing it wrong. Meta-ARAW identifies the strategy, then you **execute the full ARAW**.

### Rule 3: LITERAL DEPTH INTERPRETATION

When user says `/araw 8x [topic]`:
- They want 8x depth analysis
- They do NOT want you to question whether 8x is appropriate
- They do NOT want a meta-analysis about whether to do ARAW
- They DO want 18 claims, 8 levels, 8 CRUX, 10 DO_FIRST, 1600-2200 saved lines

**Take the depth specification literally. Execute it.**

### Rule 4: QUESTION REFRAMING GOES IN THE ARAW

If you think the question should be reframed:
- Do NOT stop and ask the user
- DO include the reframing as a claim to ARAW
- DO explore both the original frame AND alternative frames
- Let the ARAW analysis surface the better frame

### Rule 5: MINIMUM OUTPUT ENFORCEMENT

Before finishing, count your lines. If you're below minimum:

```
SELF-CHECK BEFORE COMPLETING
============================
Specified depth: [Nx]
Required minimum output: [lines]
Current output: [lines]
Status: [MEETS REQUIREMENT / BELOW MINIMUM]

If BELOW MINIMUM: Continue analysis. Do not submit.
```

---

## DEPTH SPECIFICATION

Parse the input for depth multipliers:

| Command | Meaning | Exploration | Saved |
|---------|---------|-------------|-------|
| `/araw [topic]` | Base depth (1x) | 5 claims, 3 levels, 400+ lines | 250-350 lines |
| `/araw 2x [topic]` | Double depth | 7 claims, 4 levels, 800+ lines | 400-600 lines |
| `/araw 3x [topic]` | Triple depth | 10 claims, 5 levels, 1200+ lines | 600-900 lines |
| `/araw 4x [topic]` | Deep depth | 12 claims, 6 levels, 1600+ lines | 800-1100 lines |
| `/araw 8x [topic]` | Maximum depth | 18 claims, 8 levels, 3200+ lines | 1600-2200 lines |
| `/araw 16x [topic]` | Ultra depth | 25 claims, 10 levels, 6400+ lines | 3200-4400 lines |
| `/araw 32x [topic]` | Extreme depth | 35 claims, 12 levels, 12800+ lines | 6400-8800 lines |
| `/araw lite [topic]` | **ARAW-Lite** | 1 claim, 2 levels, ~50 lines | Not saved |

### ARAW-Lite (5-Minute Quick Decision Mode)

**For everyday decisions where full ARAW is overkill.**

When to use ARAW-Lite:
- Low-stakes decisions
- Reversible choices
- Time-sensitive situations
- When you just need a quick sanity check

**ARAW-Lite Format:**

```
ARAW-LITE: [topic]
==================

CLAIM: [Single most important claim to examine]

ASSUME RIGHT:
├── What becomes possible? [1-2 sentences]
├── What's the easy path? [1-2 sentences]
└── What would we observe if true? [1 prediction]

ASSUME WRONG:
├── Best alternative? [1-2 sentences]
├── What would make this false? [1-2 sentences]
└── What's the risk? [1-2 sentences]

VERDICT: [PROCEED / RECONSIDER / NEED MORE INFO]
CONFIDENCE: [HIGH / MEDIUM / LOW]
ACTION: [One specific next step]
```

**ARAW-Lite is NOT saved.** It's for quick decisions, not documentation.

### ARAW 8x (Maximum Depth Mode)

**For the most comprehensive analysis possible.** Use when:
- Stakes are extremely high (life decisions, major investments, strategic pivots)
- Problem is complex with many interacting dimensions
- Need to find non-obvious solutions or hidden patterns
- Want to exhaust the possibility space
- Building foundational understanding that will be referenced repeatedly

**8x Requirements beyond 4x:**
- 18 claims (vs 12)
- 8 recursion levels (vs 6)
- 8 CRUX points (vs 5)
- 10 DO_FIRST actions (vs 6)
- Cross-claim synthesis (how claims interact with each other)
- Meta-level pattern identification
- Full AR technique coverage (apply all 17 AR questions to major claims)
- Multiple parallel exploration threads
- 1600-2200 lines saved (vs 800-1100)

**8x is NOT for:**
- Time-pressured decisions (use 4x or lower)
- Simple questions with obvious answers
- Topics where additional depth has diminishing returns
- When you need to act quickly

### ARAW 16x (Ultra Depth Mode)

**For pushing beyond comprehensive into exhaustive.** Use when:
- Exploring genuinely novel territory where depth compounds value
- Research-grade analysis where missing anything is costly
- Problems where 8x repeatedly reveals "needs more depth"
- Foundational work that must be maximally thorough

**16x Requirements beyond 8x:**
- 25 claims (vs 18)
- 10 recursion levels (vs 8)
- 12 CRUX points (vs 8)
- 14 DO_FIRST actions (vs 10)
- Cross-domain synthesis (how insights apply to other fields)
- Second-order pattern identification (patterns in patterns)
- Full AR + AW technique coverage on all major claims
- Parallel + sequential exploration (breadth AND depth)
- 3200-4400 lines saved (vs 1600-2200)

**16x introduces:**
- Mandatory cross-reference with prior ARAW sessions on related topics
- Explicit hypothesis generation and testing within the ARAW
- Synthesis sections at 4-claim intervals to prevent losing thread
- Required "what would change my mind" for each major conclusion

### ARAW 32x (Extreme Depth Mode)

**For research-grade exhaustive exploration.** Use when:
- The question is important enough to warrant days of analysis
- You're building a permanent reference that must cover everything
- Previous depth modes kept revealing new territory
- The topic is fundamental enough to justify extreme investment

**32x Requirements beyond 16x:**
- 35 claims (vs 25)
- 12 recursion levels (vs 10)
- 16 CRUX points (vs 12)
- 20 DO_FIRST actions (vs 14)
- Multi-session continuity (may span multiple conversations)
- External reference integration (cite and build on prior work)
- Complete mapping of the claim space, not just sampling
- Explicit uncertainty quantification on all conclusions
- 6400-8800 lines saved (vs 3200-4400)

**32x introduces:**
- Structured progress tracking across sessions
- Explicit "unexplored regions" documentation
- Required adversarial review of major conclusions
- Integration with external sources/research where relevant
- Meta-analysis of ARAW itself as applied to this topic

**⚠️ Warning:** 16x and 32x may exceed single-session context limits. Design for multi-session work with explicit state saving between sessions.

**Depth scaling:**
- **Claims identified**: 5 / 7 / 10 / 12 / 18 / 25 (16x) / 35 (32x)
- **Recursion levels**: 3 / 4 / 5 / 6 / 8 / 10 (16x) / 12 (32x)
- **Sub-claims per branch**: 3 / 4 / 5 / 6 / 8 / 10 (16x) / 12 (32x)
- **CRUX points**: 2 / 3 / 4 / 5 / 8 / 12 (16x) / 16 (32x)
- **DO_FIRST actions**: 3 / 4 / 5 / 6 / 10 / 14 (16x) / 20 (32x)

### What to Save (MANDATORY - keep all of these)

**Every table you create must be saved.** If you made a table during analysis, it goes in the saved file.

- Meta-ARAW strategy selection (full block)
- **ALL tables** (claims table, blind spot table, session inventory, value assessment, etc.)
- All claims identified with types and importance
- **ALL ARAW trees for major claims** (the AR/AW branch structures)
- **ALL novel/surprising findings** (mark with [NOVEL])
- **ALL unexpected results**
- **ALL tensions discovered** (with category classification table)
- **ALL insights**
- CRUX points (full format with question/test/implications)
- DO_FIRST actions (full format with what/why/how/resolves)
- Dual analysis (contrarian + non-contrarian sections)
- Synthesis and conclusions
- Confidence assessment table
- Surprise-self test table
- Next steps/actions

### What Can Be Trimmed (ONLY these)

- AR/AW sub-branches that went nowhere (just note "explored, no insight")
- Conventional/obvious paths that confirmed expectations without novel findings
- Repetitive sub-sub-branches (summarize pattern once)
- Dead ends at depth 4+ with no novel findings

**Rule: If you created structured analysis (table, tree, list), it must be saved. Only trim unproductive deep branches.**

---

## STEP 0: META-ARAW (Strategy Selection)

**BEFORE diving into ARAW, do a quick meta-analysis to select the right search strategy.**

This prevents inefficient search by identifying:
1. What RESPONSE TYPE is appropriate (solving may not be the answer)
2. What KIND of problem this is
3. What UNCERTAINTY TYPE dominates
4. What SEARCH PITFALLS to avoid
5. Whether the question itself needs ARAW'd first

### 0.0: Meta-Response Check (NEW - from Problem-Solving Stack)

**Before ANY exploration, ask: "Should I SOLVE this, or respond differently?"**

65% of problem-solving failures happen at Noticing (40%) and Framing (25%). But there's a PRIOR question: whether solving is even the right response.

| Response | When Appropriate | Example |
|----------|------------------|---------|
| **SOLVE** | Problem is real, solvable, worth solving | "How do I fix this bug?" → Solve |
| **DISSOLVE** | Reframe makes problem disappear | "How do I win this argument?" → Don't need to win |
| **ACCEPT** | Solution cost > problem cost | Minor annoyance, no good fix → Accept |
| **TRANSFORM** | Problem contains opportunity | Constraint → Feature |
| **PREVENT** | Better to address upstream | Recurring issue → Fix root cause |
| **WAIT** | Time/circumstances will change things | Premature decision → Wait for info |

```
META-RESPONSE CHECK
===================
Is this a real problem (vs misframed, preference, or self-created)?
Does solving this actually help achieve the deeper goal?
Is the expected benefit of solving > expected cost?
Might this self-resolve with time?
Could reframing dissolve the problem entirely?

Response: [SOLVE/DISSOLVE/ACCEPT/TRANSFORM/PREVENT/WAIT]
If not SOLVE: [What to do instead]
If SOLVE: Proceed to 0.1
```

**If response is NOT "SOLVE", don't proceed with ARAW. Apply the appropriate alternative.**

**⚠️ ANTI-PATTERN WARNING**: This check is for cases where ARAW genuinely doesn't apply (e.g., user asks "what time is it?"). It is NOT an escape hatch to avoid doing the ARAW the user requested. If user asked for `/araw 8x [topic]`, the response is ALWAYS "SOLVE" - they explicitly requested ARAW. Do not use this check to substitute a "meta-analysis" for the actual ARAW.

### 0.1: Question Restatement (NEW)

**Before anything else, restate what you think the question is.**

```
RESTATED QUESTION: [Your understanding of what's being asked]
ORIGINAL: [The original input]
MATCH: [Yes/No - if No, clarify before proceeding]
```

This catches misunderstandings early. 40% of problem-solving failures happen at the "noticing" stage - solving the wrong problem.

**⚠️ IF MATCH IS "NO"**: Do not stop to ask user. Instead:
1. State your interpretation
2. State the alternative interpretation
3. ARAW BOTH interpretations in the same session
4. Let the analysis surface which is correct

### 0.2: Problem Structure Check (from 121)

| Question | If YES | If NO |
|----------|--------|-------|
| Is this decomposable into independent subproblems? | ARAW each separately, then synthesize | ARAW holistically |
| Are there local optima traps? | Use random restarts, explore widely | Hill-climb confidently |
| Is there a closed-form answer? | Don't ARAW - calculate directly | ARAW is appropriate |
| Is the objective well-defined? | Proceed with ARAW | Define objective first |

### 0.3: Uncertainty Type Check (from 124)

| Uncertainty | Strategy |
|-------------|----------|
| **Epistemic** (reducible by learning) | Deep ARAW to find what to learn |
| **Aleatoric** (irreducible randomness) | Light ARAW, then hedge/accept |
| **Model uncertainty** (wrong framework) | ARAW the framework itself first |
| **Unknown unknowns likely** | Build slack, stay flexible in conclusions |

### 0.3.1: Paradigm Questioning Check (NEW - Critical for Domain Adaptation)

**Before domain-specific ARAW, question the domain paradigm itself.**

This prevents "paradigm import failure" - when ARAW imports conventional domain assumptions without questioning them. This is especially important when:
- Adapting ARAW to a specific domain (math, writing, business, etc.)
- The user may want non-conventional approaches
- Claude's training paradigm may differ from user's needs

| Question | Purpose |
|----------|---------|
| What does this domain ASSUME is valuable? | Surface paradigm |
| What would a DIFFERENT paradigm in this domain value? | Find alternatives |
| Is conventional paradigm right for THIS user/goal? | Check fit |
| What would ARAW look like under alternative paradigm? | Explore options |

**ARAW the paradigm BEFORE ARAW within the paradigm:**

```
PARADIGM ARAW (do this for domain-specific work):
├── ASSUME RIGHT → Conventional paradigm is correct
│   ├── What does it value? (e.g., for math: proofs, precision, errors)
│   ├── What does it exclude? (e.g., intuition, exploration, approximation)
│   └── Is this what the user wants?
│
└── ASSUME WRONG → Conventional paradigm is wrong/limiting
    ├── What alternative paradigms exist in this domain?
    ├── What would each alternative value?
    └── Which paradigm fits this user's actual goal?
```

**Example for math domain:**
- Conventional paradigm: Proofs, error-catching, precision, formalism
- Alternative paradigms: Exploration, intuition, insight, approximate truth
- Question: Is user asking for error-checking or mathematical understanding?

**If multiple paradigms are valid, either:**
1. Ask user which paradigm fits their goal
2. Explore multiple and note how results differ
3. Create separate approaches for different paradigms

**Key insight**: Claude's training imports conventional paradigms. Domain adaptation that doesn't question paradigms reproduces Claude's biases, not user's needs.

### 0.4: Search Pitfall Check (from 158)

Before starting, ask:
- **Fish in Dreams**: Am I expecting a specific answer? (Search for opposite)
- **Red Herring**: Does my explanation match what I'm explaining? (Check fit)
- **Smokescreen**: Does confusion appear when approaching this? (Persist through)

### 0.5: Question Quality Check (from 140)

Before ARAW'ing the stated question, verify:
- Is this the RIGHT question to be asking?
- Does answering this actually help?
- Is the question ANSWERABLE?
- Am I asking "how" when I should ask "whether"?

If any fail, ARAW the question itself first.

### 0.5.1: Anti-Psychology Check (NEW)

**Before diagnosing "underlying needs," check:**

| Check | If YES |
|-------|--------|
| Has user explicitly stated their goal? | Solve it first, don't question it |
| Is psychology/motivation analysis requested? | Only then diagnose |
| Would solving the stated goal help? | Do it |

**Default**: Take the stated goal at face value. Psychologizing the user ("why do you really want this?") when they've been explicit is a failure mode.

**Avoid**:
- "Have you considered that you might actually want X?"
- "The underlying need might be..."
- "Why don't you want to work?"

**Instead**: Solve what they asked. If truly impossible, explain why - don't redirect to what you think they should want.

### 0.6: Multiple Frame Generation (NEW)

**Try at least 3 different frames before committing to one.**

Framing accounts for 25% of problem-solving failures. Different frames reveal different solutions.

| Frame Type | Question |
|------------|----------|
| **Stated frame** | What does the question as asked assume? |
| **Opposite frame** | What if the opposite assumption were true? |
| **Broader frame** | What larger context does this sit in? |
| **Narrower frame** | What specific instance of this matters most? |
| **Different domain frame** | How would someone from [other field] see this? |

**Pick the frame that opens the most options**, not necessarily the stated frame.

### 0.6.1: Paradigm Shift Check (NEW)

**Ask: What recent changes make old assumptions wrong?**

| Question | Purpose |
|----------|---------|
| What's new in this domain that changes everything? | Find paradigm shifts |
| How would this be solved if AI did the work? | AI-era reframe |
| What was impossible 2 years ago that's now possible? | Technology shifts |
| What old constraints no longer apply? | Remove false constraints |

**Example**: "How to make passive income" used to assume human builds, then human relaxes. AI-era version: AI builds AND maintains, human just owns.

**Default**: Always ask "What if AI/automation did this?" for any goal involving human effort.

### 0.7: Criteria Elicitation (CRITICAL)

**Before searching, surface what "right" means.**

Hidden criteria cause ARAW failure. The asker may have criteria the analyzer doesn't know.

| Question | Why It Matters |
|----------|----------------|
| What would make an answer "right"? | Defines success |
| What would make an answer "wrong"? | Defines failure |
| Is there a specific answer expected? | Reveals hidden target |
| What type of answer is wanted? (task/insight/option/validation) | Determines category |
| What would be surprising vs expected? | Novelty criterion |

**If criteria are hidden or ambiguous:**
1. Attempt to infer from context and patterns
2. If still unclear after genuine attempt, acknowledge the gap
3. Generate multiple answers for different plausible criteria

### 0.7.1: Literal Interpretation Check (NEW)

**Default: Take stated goals literally.**

| Signal | Action |
|--------|--------|
| User states goal simply and directly | Take literally first |
| User says "assume X" or "I literally mean" | Take literally, no reinterpretation |
| User corrects your interpretation | Revert to literal |
| Goal seems extreme/unusual | Still take literally - explore how to achieve it |

**Anti-pattern to avoid**:
- User says "I want X"
- You respond "But do you really want X? Perhaps you want Y instead"
- User says "No, I want X"
- You still explore Y

**Correct pattern**:
- User says "I want X"
- You explore how to achieve X
- Only if X is truly impossible do you explain why and offer alternatives

### 0.8: Transfer Check

**What have you learned recently that applies here?**

Recent learnings from the same session or context should transfer:
- What reconceptualizations were done?
- What precision improvements were made?
- What patterns were identified?
- What mistakes were corrected?

**Check previous ARAW sessions in the same domain:**
- `library/araw/sessions/` - Any related sessions?
- `library/araw/tension_questions.md` - Any relevant tensions?

**Apply these learnings to the current ARAW.** Don't repeat corrected mistakes.

### 0.9: Novelty Stance

**Set expectation: answers should be non-obvious.**

If you can predict the ARAW output before doing it, you're probably not searching hard enough.

Check:
- Am I expecting a specific answer? (Fish in Dreams risk)
- Are my ASSUME WRONG branches genuinely surprising alternatives?
- Would the conclusion surprise me?

**Novelty requirement**: At least ONE finding should be something you didn't expect before starting.

### 0.10: Integral Goal Check (NEW)

**Ask: Are there related goals that might be the SAME problem?**

Sometimes solving A solves B. Check:
- Is this goal actually a sub-goal of something else?
- Is there a related problem where solving one solves both?
- Am I treating as separate what's actually integral?

Example: "Alignment research" and "capability research" may be the same problem.

### 0.11: Efficiency Diagnostic (NEW)

**If this is taking too long, something may be wrong.**

| Symptom | Possible Cause | Action |
|---------|----------------|--------|
| Excessive depth without progress | Wrong frame | Try different frame |
| Going in circles | Missed assumption | Surface hidden claims |
| Everything feels forced | Wrong question | ARAW the question itself |
| 10x expected effort | Wrong approach | Consider non-ARAW method |

### 0.12: Implementation Locus Check (NEW)

**Ask: Who should implement this - the user or Claude?**

| If Claude CAN do it | Claude does it |
| If Claude can do PART | Claude does that part |
| If Claude can only advise | Acknowledge limitation |

**Default for "how do I" questions**: Claude does the work, not gives homework.

**What Claude can do:**
- Write code, articles, books, documentation
- Create templates, products, assets
- Build complete systems (with user deploy)
- Research and synthesize
- Design and plan

**What Claude cannot do:**
- Physical actions
- Access external accounts
- Run code in production
- Make purchases
- Send real communications

**Key principle**: If the question implies work to be done, and Claude can do that work, Claude should offer to do it - not assign it to the user as homework.

### 0.13: Strategy Selection Output

After meta-analysis, output:

```
META-ARAW STRATEGY SELECTION
============================
Restated question: [your understanding]
Problem type: [decomposable/holistic/closed-form/undefined]
Uncertainty type: [epistemic/aleatoric/model/unknown-unknowns]
Pitfall risk: [fish-in-dreams/red-herring/smokescreen/none]
Question quality: [right/wrong/needs-reframe]
Selected frame: [which of the 3+ frames generated]
Criteria: [explicit/inferred/unclear - list known criteria]
Transfer from session: [recent learnings to apply]
Related tensions: [from tension_questions.md]
Novelty target: [what would be surprising to find?]
Integral goals: [any related problems that might be the same?]
Selected strategy: [wide-then-deep/deep-then-wide/targeted/holistic]
Depth: [1x/2x/3x/4x/8x/16x/32x]

Proceeding with ARAW...
```

### 0.14: Selective Formalization Guidance

**Not all of ARAW benefits from formalization.** Apply this principle:

**FORMALIZE (precision helps):**
- **Termination conditions**: When is analysis "done"? (Use Resolution Score)
- **CRUX identification**: What maximizes information gain? (Count branches resolved)
- **Confidence levels**: What's the posterior probability?

**KEEP INFORMAL (flexibility helps):**
- **Claim identification**: Needs creativity, serendipity
- **Branch exploration**: Benefits from associative thinking
- **Synthesis**: Requires judgment, not rules

**Overhead warning**: If formalization feels forced or slow, it's probably not helping. Mathematical precision is a tool, not a goal.

---

## STEP 1: Identify ALL Claims

Parse the input into distinct claims. Look for:

1. **Explicit claims** - Directly stated
2. **Implicit claims** - Assumed but not stated
3. **Bundled claims** - Multiple claims packed into one statement
4. **Presupposition claims** - What must be true for the statement to make sense
5. **Meta-claims** - Claims about the framing or approach itself

### Claim Identification Checklist (NEW)

For EACH claim identified:
- State it precisely
- Note type: explicit/implicit/bundled/presupposed/meta
- Rate importance: HIGH/MED/LOW
- Check if OPEN (has alternatives) or might be CLOSED (foundational)
- **VOI rating**: How much would knowing this change action? (for ordering)

### Blind Spot Check (NEW)

After identifying claims, explicitly ask:

**"What am I NOT seeing?"**

| Blind Spot Type | Question |
|-----------------|----------|
| Perspective blind spot | Who else cares about this? What would they see? |
| Domain blind spot | What would an expert in [adjacent field] notice? |
| Temporal blind spot | What past/future factors am I ignoring? |
| Scale blind spot | What happens at 10x smaller or larger scale? |
| Emotional blind spot | What feelings might be driving hidden assumptions? |

### Non-Propositional Input Check (NEW)

Not all relevant information is in words. Ask:

**"What intuitions, images, or feelings are relevant?"**

| Input Type | How to Surface |
|------------|----------------|
| **Intuition** | "Something feels off about X" → What specifically? |
| **Image** | "I picture it like..." → What does that imply? |
| **Feeling** | "This makes me uncomfortable" → Why? What's threatened? |
| **Pattern** | "This reminds me of..." → What's the structural similarity? |

Convert non-propositional inputs to claims, then ARAW those.

### VOI-Guided Claim Ordering (NEW)

**Order claims by action divergence, not by appearance in input.**

| VOI Level | Criteria | Action |
|-----------|----------|--------|
| HIGH | Different answer → completely different action | ARAW first |
| MED | Different answer → modified action | ARAW second |
| LOW | Different answer → same action | ARAW if time permits |

**ARAW high-VOI claims first.** They determine the most.

**Minimum claims by depth:**
- 1x: 5 claims
- 2x: 7 claims
- 3x: 10 claims
- 4x: 12 claims
- 8x: 18 claims
- 16x: 25 claims
- 32x: 35 claims

---

## STEP 2: ARAW Each Claim

For EACH claim, build a full tree using the FULL TREE approach (from 115):

**Key insight**: Explore BOTH AR and AW at EVERY node. Paths can be AR→AW→AW→AR→...

```
Claim: "[main claim]"
│
├── ASSUME RIGHT → Claim is true/necessary
│   │
│   ├── What follows logically?
│   │   ├── Consequence 1
│   │   │   ├── ASSUME RIGHT → [explore deeper]
│   │   │   └── ASSUME WRONG → [explore deeper]
│   │   └── [more consequences...]
│   │
│   ├── What actions are justified?
│   ├── What does success look like?
│   └── Sub-claims embedded in "RIGHT" → Full ARAW each
│
└── ASSUME WRONG → Claim might be false/unnecessary
    │
    ├── What alternatives exist?
    │   ├── Alternative 1
    │   │   ├── ASSUME RIGHT → [explore this alternative]
    │   │   └── ASSUME WRONG → [explore why alternative also wrong]
    │   └── [more alternatives...]
    │
    ├── What would make this claim false?
    ├── What's the opposite claim? → Full ARAW
    ├── What reframe dissolves the claim?
    └── Sub-claims embedded in "WRONG" → Full ARAW each
```

**Recursion depth by multiplier:**
- 1x: 3 levels
- 2x: 4 levels
- 3x: 5 levels
- 4x: 6 levels
- 8x: 8 levels
- 16x: 10 levels
- 32x: 12 levels

### Upside Exploration (NEW - Anti-Conservative Bias)

**For every ASSUME WRONG that says "this is too ambitious," ALSO explore ASSUME RIGHT for the ambitious version.**

| Conservative Bias | Counter-Action |
|-------------------|----------------|
| "This ROI is unrealistic" | Also explore: "What if this ROI IS achievable?" |
| "This is too hard" | Also explore: "What if this is actually doable?" |
| "Nobody does this" | Also explore: "What if being first is the advantage?" |
| "This would never work" | Also explore: "What conditions would make it work?" |

**Don't only explore failure modes. Explore success modes.**

**Anti-pattern**: Suggesting $500/month when $50K/month is possible because $500 is "more realistic."

**Correct pattern**: Explore BOTH the conservative and ambitious scenarios. Let evidence distinguish, not prior bias toward pessimism.

### VOI-Guided Branch Selection

**Not all branches deserve equal exploration.** Apply VOI thinking:

| Branch Type | VOI Level | Action |
|-------------|-----------|--------|
| High action divergence (different answers → different actions) | HIGH | Explore deeply |
| Low action divergence (different answers → same actions) | LOW | Note and move on |
| Conventional/expected branch | SUSPICIOUS | Flag, search for unconventional |
| Surprising/unexpected branch | HIGH | Explore - may contain insight |

**Branch prioritization:**
1. Explore HIGH VOI branches first
2. Flag CONVENTIONAL branches - they may be lazy thinking
3. Actively seek SURPRISING alternatives in ASSUME WRONG

### Conventional Branch Detection

**If a branch is obvious/expected, flag it:**

```
├── ASSUME WRONG → [CONVENTIONAL: obvious alternative]
│   └── [Flag: This is the expected "alternative." Search for genuinely novel options.]
```

Conventional alternatives include:
- The opposite of what's stated
- What anyone would suggest
- The "standard" answer in the domain
- What you thought of immediately

**Requirement:** For each major ASSUME WRONG, include at least ONE genuinely unconventional alternative.

### Proof Technique Checklist (Systematic ASSUME WRONG Generation)

**Mathematical proof techniques are search strategies in disguise.** Apply these systematically to generate better ASSUME WRONG branches:

| Technique | Question to Ask | What It Produces |
|-----------|-----------------|------------------|
| **Contradiction** | "If this were true, what impossible thing would follow?" | Reductio argument - shows claim is self-refuting |
| **Construction** | "Can I build a specific counter-example?" | Concrete falsification |
| **Diagonalization** | "What option differs from ALL alternatives listed so far?" | Genuinely novel alternative (Cantor's method) |
| **Probabilistic** | "What do MOST cases look like? Is this one typical?" | Base rate reality check |
| **Inversion** | "What's the exact opposite claim? Is IT more likely true?" | Negation exploration |

**For each major ASSUME WRONG branch, apply at least 2 techniques.**

**Diagonalization is especially powerful**: If you've listed alternatives A, B, C, explicitly construct an option that is NOT A, NOT B, and NOT C. This systematically generates novel options.

### Unconventional Alternative Enforcement (MANDATORY)

**The Problem**: AW branches default to conventional alternatives. The "obvious" alternative is often just the opposite of what's stated, not a genuinely novel option.

**The Solution**: Make unconventional alternatives mandatory, not optional.

#### Step 1: Conventional Check

For each ASSUME WRONG alternative, ask:
```
CONVENTIONAL CHECK
==================
Alternative: [the alternative generated]

Is this alternative:
[ ] The opposite of what's stated? → CONVENTIONAL
[ ] What anyone would suggest? → CONVENTIONAL
[ ] The "standard" answer in the domain? → CONVENTIONAL
[ ] What you thought of immediately? → CONVENTIONAL
[ ] Something that would surprise most people? → UNCONVENTIONAL

Result: [CONVENTIONAL / UNCONVENTIONAL]
```

#### Step 2: If Conventional, Force Additional Search

If the alternative is conventional, you MUST generate an unconventional one using these prompts:

| Prompt | What It Generates |
|--------|-------------------|
| "What if the OPPOSITE of conventional wisdom is true?" | Contrarian insight |
| "What would an outsider/novice/alien suggest?" | Fresh perspective |
| "What hasn't been tried, and WHY hasn't it been tried?" | Unexplored territory |
| "What would be embarrassing to suggest but might work?" | Hidden options |
| "What would a 10x more ambitious version look like?" | Stretch thinking |
| "What would we do if [key constraint] didn't exist?" | Constraint removal |
| "What worked in a completely different domain?" | Cross-domain transfer |

#### Step 3: Minimum Unconventional Quota

For each major ASSUME WRONG branch:
- **1x depth**: At least 1 unconventional alternative
- **2x depth**: At least 2 unconventional alternatives
- **3x depth**: At least 3 unconventional alternatives
- **4x depth**: At least 4 unconventional alternatives
- **8x depth**: At least 6 unconventional alternatives
- **16x depth**: At least 8 unconventional alternatives
- **32x depth**: At least 12 unconventional alternatives

**Enforcement**: The Output Checklist (end of ARAW) includes verification that the unconventional quota was met.

### AR Generative Techniques (NEW - Makes AR Active, Not Just Confirmatory)

**The Problem**: AR is currently passive/confirmatory ("if true, then...") while AW is generative ("what alternatives?").

**The Solution**: Make AR generative too. AR should search for SOLUTIONS while AW searches for PROBLEMS.

```
Current state:
  AW = generative DECONSTRUCTION (find what's wrong, alternatives)
  AR = confirmatory TRACING (if true, then...)

New state:
  AW = generative DECONSTRUCTION (find what's wrong, alternatives)
  AR = generative CONSTRUCTION (find what's possible, what to build)
```

#### Tier 1: Essential AR Techniques (Use on every major AR branch)

| # | Technique | Question | Produces | When |
|---|-----------|----------|----------|------|
| 1 | **Easy Path Question** | "What would make this problem EASY?" | Simplifications | Every AR |
| 2 | **Possibility Expansion** | "What becomes possible that wasn't before?" | New options | Every AR |
| 3 | **Prediction Generation** | "If this is true, what would we observe?" | Testable predictions | Every AR |
| 4 | **Component Breakdown** | "What are the independent parts?" | Components | Systems problems |
| 5 | **Leverage Point Search** | "Where does small input → large output?" | High-impact points | Every AR |

#### Tier 2: Important AR Techniques (Use when relevant)

| # | Technique | Question | Produces |
|---|-----------|----------|----------|
| 6 | Resource Inventory | "What resources does accepting this give us?" | Resource list |
| 7 | Interface Specification | "What does each component need/provide?" | Interface specs |
| 8 | Experiment Design | "What test would verify this?" | Test design |
| 9 | Constraint Relaxation | "Which constraint makes this hard?" | Binding constraint |

#### Tier 3: Optional AR Techniques (Use if needed)

| # | Technique | Question | When Needed |
|---|-----------|----------|-------------|
| 10 | Leverage Search | "What existing work connects here?" | Prior art exists |
| 11 | Dissolution Check | "Does accepting this dissolve the problem?" | Problem might not need solving |
| 12 | Minimal Path | "What's shortest path from here to goal?" | Optimization needed |
| 13 | Dependency Ordering | "What order must these be built?" | Complex systems |
| 14 | Integration Path | "How do components combine?" | Multi-component systems |
| 15 | Evidence Search | "What existing evidence bears on this?" | Empirical domains |
| 16 | Prior Integration | "What established knowledge constrains?" | Mature domains |
| 17 | Frame Shopping | "In what frame is this already solved?" | Stuck problems |

#### AR Template (Apply to each major ASSUME RIGHT branch)

```
ASSUME RIGHT → [claim is true]
│
├── Easy Path: "What would make this easy?"
│   └── [simplifications found]
│
├── Possibilities: "What becomes possible now?"
│   └── [new options unlocked]
│
├── Predictions: "What would we observe if true?"
│   └── [3+ testable predictions]
│
├── Components: "What are the parts?" (if system)
│   └── [component list with interfaces]
│
├── Leverage: "Where is 10x impact available?"
│   └── [high-leverage points]
│
└── Resources: "What do we now have access to?"
    └── [resource inventory]
```

**Key insight**: AR should be as ACTIVE and GENERATIVE as AW. Don't just trace implications - actively search for what becomes possible, what's easy, what's high-leverage.

---

## STEP 3: Apply Search Quality Checks During Exploration

As you build the tree, continuously check (from procedures):

### Decomposition Quality (from 131)
- Are subproblems SOLVABLE?
- Does solving pieces solve the original?
- Cutting along NATURAL JOINTS?
- Core difficulty VISIBLE (not hidden)?

### Inference Direction (from 130)
- Forward (evidence→conclusion) or backward (conclusion→evidence)?
- Confirmation bias active?
- Should use bidirectional?

### Search Space (from 163)
- Searching the RIGHT SET of possibilities?
- Right GRANULARITY?
- Any FALSE CONSTRAINTS being held fixed?

---

## STEP 4: Commitment Test (from 114/115)

For each branch, apply the commitment test with **continuous confidence levels**:

### Confidence Levels (NEW - replaces binary FOUNDATIONAL/GUESS)

| Level | Confidence | Meaning | Action |
|-------|------------|---------|--------|
| **FOUNDATIONAL** | 0.9+ | All AW paths contradict | Can commit |
| **LIKELY** | 0.7-0.9 | Most AW paths contradict | Commit with monitoring |
| **UNCERTAIN** | 0.3-0.7 | AW paths survive | Hold as working hypothesis |
| **UNLIKELY** | 0.1-0.3 | Most AR paths have problems | Consider opposite |
| **IMPLAUSIBLE** | <0.1 | AR paths contradict | Reject |

```
FOUNDATIONAL (0.9+) when:
  ✓ ALL AW-originating paths eventually CONTRADICT
  ✓ INCLUDING mixed paths (AW.AR.AW...)
  ✓ AR paths are internally consistent
  ✓ No coherent alternative world exists

LIKELY (0.7-0.9) when:
  ~ Most AW paths contradict
  ~ Some weak alternatives survive but seem implausible
  ~ Strong AR paths, weak AW paths

UNCERTAIN (0.3-0.7) when:
  ✗ Multiple coherent paths survive
  ✗ AR and AW both have merit
  ✗ Need more information to distinguish

UNLIKELY (0.1-0.3) when:
  ✗ Most AR paths have problems
  ✗ AW paths are more coherent
  ✗ Should probably explore opposite

IMPLAUSIBLE (<0.1) when:
  ✗ AR paths contradict each other or reality
  ✗ Strong evidence against
  ✗ Should reject
```

Mark each terminal node with confidence level: [FOUNDATIONAL/LIKELY/UNCERTAIN/UNLIKELY/IMPLAUSIBLE]

---

## STEP 5: Identify CRUX Points

**CRUX**: The observation that would most decisively distinguish branches.

For each major branch divergence:
- What one thing, if known, would tell us which branch is true?
- What's the cheapest way to determine this?
- What's the most reliable way to determine this?

**CRUX format:**

### CRUX N: [Primary crux]
- **The question**: [precise question]
- **Branches resolved**: [list which branches/claims this would resolve; count them]
- **Why decisive**: [why this question maximally splits remaining uncertainty]
- **How to test**: [how you would find out]
- **If answer is X**: [what follows - which branches resolved]
- **If answer is Y**: [what follows - which branches resolved]

**Information-Theoretic Principle**: The best CRUX is the question that resolves the most branches (maximizes uncertainty reduction). When choosing between candidate CRUXes, prefer the one with higher branch count.

**Minimum CRUX points by depth:**
- 1x: 2 CRUX
- 2x: 3 CRUX
- 3x: 4 CRUX
- 4x: 5 CRUX
- 8x: 8 CRUX
- 16x: 12 CRUX
- 32x: 16 CRUX

---

## STEP 6: Identify DO_FIRST Actions

**DO_FIRST**: What must be verified/done before other actions make sense?

List in priority order:

### DO_FIRST Format (NEW - Specify WHO)

For each DO_FIRST, specify WHO does it:

### DO_FIRST N: [Action]
- **Who**: [Claude / User / Both]
- **What**: [specific action]
- **Why first**: [why this before anything else]
- **How**: [concrete steps]
- **What it resolves**: [which branches/questions]
- **If Claude**: I'll do this now / I'll do this if you say yes
- **If User**: Only if Claude cannot do it

**Preference order for WHO:**
1. **Claude does it now** - If Claude can do it, Claude should do it
2. **Claude does it with user go-ahead** - If needs permission/confirmation
3. **User does minimum viable version** - Only what Claude cannot do
4. **User does full version** - LAST RESORT only

**Anti-pattern**: Listing 6 DO_FIRST actions that are all user homework.
**Correct pattern**: Claude does most, user does only what Claude cannot.

**Minimum DO_FIRST by depth:**
- 1x: 3 actions
- 2x: 4 actions
- 3x: 5 actions
- 4x: 6 actions
- 8x: 10 actions
- 16x: 14 actions
- 32x: 20 actions

---

## STEP 7: Apply Search Termination Checks (from 120)

Before concluding, verify:

| Check | If YES | Action |
|-------|--------|--------|
| Over-optimizing past value? | Stop | Ship current analysis |
| Past "good enough"? | Stop | Accept findings |
| Search cost > expected gain? | Stop | Conclude |
| Hit diminishing returns? | Stop or pivot | Shift strategy |
| Space exhausted? | Stop | Accept best found |

### VOI-Based Stopping (For Individual Branches Only)

**This section is about stopping INDIVIDUAL BRANCHES early, NOT stopping the entire ARAW early.**

For each branch, ask:

```
BEFORE EXPLORING DEEPER:
1. "Would resolving this branch change my action?"
   → If NO: Skip or summarize
   → If YES: Explore

2. "What's the marginal value of more depth here?"
   → If HIGH: Continue
   → If LOW: Stop this branch

3. "Am I exploring because it matters or because the procedure says to?"
   → If matters: Continue
   → If procedure: Question whether to continue
```

**VOI-Based Termination Criteria:**

| Signal | Meaning | Action |
|--------|---------|--------|
| Same insights repeating | Diminishing returns | Stop or shift |
| Branches pointing same direction | Convergence | Can conclude |
| New branch would not change action | Low VOI | Skip |
| Surprise rate dropping | Exhausted the novel | Stop |
| User goal already achievable | Past good-enough | Conclude |

**The principle**: WITHIN a branch, depth should track VALUE. You can stop exploring an unproductive branch early.

**⚠️ CRITICAL**: This does NOT mean you can reduce the overall depth. If user specified 8x, you must still hit 18 claims, 8 CRUX, 10 DO_FIRST, 1600+ lines. VOI-based stopping is about branch allocation, not overall depth reduction.

---

## STEP 8: Dual Analysis Output

### CONTRARIAN Analysis (from ASSUME WRONG branches)

Synthesize everything found in ASSUME WRONG branches:

**Core challenges to the stated framing:**
1. [Challenge 1 with full reasoning]
2. [Challenge 2 with full reasoning]
3. [Challenge 3 with full reasoning]

**Alternative framings discovered:**
1. [Alternative 1]: [description and implications]
2. [Alternative 2]: [description and implications]
3. [Alternative 3]: [description and implications]

**What might be wrong about the question itself:**
- [Meta-level issue 1]
- [Meta-level issue 2]

**Strongest ASSUME WRONG paths:**
1. [Path 1]: [why compelling]
2. [Path 2]: [why compelling]

### NON-CONTRARIAN Analysis (from ASSUME RIGHT branches)

**If the stated framing is correct:**
1. [What follows - detailed]
2. [What follows - detailed]
3. [What follows - detailed]

**Best paths forward within the frame:**
1. [Path 1]: [description and reasoning]
2. [Path 2]: [description and reasoning]

**Strongest ASSUME RIGHT paths:**
1. [Path 1]: [why compelling]
2. [Path 2]: [why compelling]

---

## STEP 9: Synthesis and Recommendations

### Resolution Status (NEW - Entropy-Based Stopping)

Track analysis completeness before synthesizing:

| Metric | Value |
|--------|-------|
| **Total branches explored** | [N] |
| **Branches with confidence assigned** | [M] |
| **Resolution Score** | [M/N as %] |
| **Unresolved branches** | [list remaining] |

**Stopping Decision**:
- Resolution Score > 80%: Synthesis is warranted
- Resolution Score 60-80%: Consider more exploration on unresolved branches
- Resolution Score < 60%: More exploration needed before synthesis

### Key Tensions Discovered
- [Tension 1]: ASSUME RIGHT says X, ASSUME WRONG says Y
- [Tension 2]: [another tension]

### Tension Category Classification (7 Categories)

For each tension, classify by category and apply master question:

| Category | Master Question |
|----------|-----------------|
| **1. Resource Allocation** | What resource is limited, and what are the competing uses? |
| **2. Information** | What don't we know, and how much does it matter? |
| **3. Optimization** | What's the Pareto frontier, and where on it to sit? |
| **4. Structure** | At what level of aggregation to optimize? |
| **5. Commitment** | How reversible is this, and how much is option value worth? |
| **6. Epistemic** | What's the gap between what we know and need to know? |
| **7. Logical** | What formal/logical constraints create the incompatibility? |

**Note**: Tensions are mathematically Pareto frontiers - you cannot improve one dimension without losing on another. The goal is to navigate along the frontier, not escape it.

**Apply the master question to each tension to guide resolution.**

### Build for Switch Principle (NEW)

**Neither extreme is always right.** For each major tension:
- Identify conditions where AR wins
- Identify conditions where AW wins
- Design so you can SWITCH approaches when conditions change

### What Would Resolve These Tensions
- [Resolution approach 1]
- [Resolution approach 2]

### Confidence Assessment
- **Confidence in RIGHT branches**: [FOUNDATIONAL/LIKELY/UNCERTAIN/UNLIKELY/IMPLAUSIBLE] because [reasoning]
- **Confidence in WRONG branches**: [FOUNDATIONAL/LIKELY/UNCERTAIN/UNLIKELY/IMPLAUSIBLE] because [reasoning]
- **Key uncertainties remaining**: [list]

### Commitment Status
- **FOUNDATIONAL claims identified**: [list with confidence levels]
- **LIKELY claims**: [list]
- **UNCERTAIN claims that remain open**: [list with coherent alternatives]

### Surprise-Self Test (REQUIRED)

**Did this ARAW produce anything surprising?**

| Question | Answer | Implication |
|----------|--------|-------------|
| Did any finding surprise you? | Yes → Good | No → May be lazy/conventional |
| Did you learn something you didn't know? | Yes → Good | No → May not have searched hard |
| Would you have predicted this output before starting? | No → Good | Yes → May be confirmation |
| Is there anything here that challenges your initial view? | Yes → Good | No → Check for Fish in Dreams |

**If NO surprises: Go back and search harder.** Lack of surprise suggests:
- Searching in expected space only
- ASSUME WRONG branches are conventional
- Not pushing deep enough
- Confirming rather than exploring

### Escape Hatch Detection (REQUIRED)

**Flag any recommendation to "ask the user" or "get more information."**

These may be legitimate OR may be lazy escapes from hard thinking.

| Recommendation | Legitimacy Check | If Legitimate | If Escape |
|----------------|------------------|---------------|-----------|
| "Ask user for clarification" | Is the question genuinely unanswerable from context? | Proceed | Think harder |
| "Need more information" | Is the information truly missing, or just not derived? | Proceed | Derive it |
| "Multiple valid options" | Are they genuinely equivalent, or is there a best? | Present options | Identify best |
| "Depends on context" | Is context truly variable, or just unknown? | Explore contexts | Infer context |

**Rule:** Before recommending "ask user," first attempt to:
1. Infer from patterns
2. Apply session learnings
3. Make best guess with stated uncertainty

"Ask user" should be last resort, not first resort.

---

## STEP 10: Determine Next Procedure

Based on findings:

| Situation | Next Procedure |
|-----------|----------------|
| Alternatives need comparison | → INVOKE: /comparison [alternatives] |
| Intrinsic goal unclear | → INVOKE: /value_elicitation $ARGUMENTS |
| Root cause unclear | → INVOKE: /root_cause_5_whys $ARGUMENTS |
| Leverage points identified | → INVOKE: /leverage_point_discovery $ARGUMENTS |
| Ready to trace journey | → INVOKE: /goal_journey_system $ARGUMENTS |
| Need more space exploration | → INVOKE: /space_discovery $ARGUMENTS |
| Need more guesses | → INVOKE: /guess_generation $ARGUMENTS |
| Still unclear after analysis | → INVOKE: /araw 2x $ARGUMENTS (go deeper) |

---

## ⚠️ PRE-COMPLETION DEPTH CHECK (MANDATORY)

**Before proceeding to Output Checklist, verify depth requirements are met.**

```
DEPTH VERIFICATION
==================
Specified depth: [read from input - 1x/2x/4x/8x/16x/32x]
Required claims: [5/7/12/18/25/35]
Required CRUX: [2/3/5/8/12/16]
Required DO_FIRST: [3/4/6/10/14/20]
Required saved lines: [250/400/800/1600/3200/6400]

Actual claims identified: [count]
Actual CRUX points: [count]
Actual DO_FIRST actions: [count]
Estimated saved lines: [count]

Status: [ALL REQUIREMENTS MET / REQUIREMENTS NOT MET]
```

**If REQUIREMENTS NOT MET**:
1. Do NOT proceed to Output Checklist
2. Do NOT submit the response
3. Go back and add more analysis until requirements are met
4. Common gaps: Missing claims? Add more. Missing CRUX? Derive from branches. Missing DO_FIRST? Extract from analysis. Too short? Expand ARAW trees.

**Only proceed when ALL REQUIREMENTS MET.**

---

## Output Checklist (Verify Before Completing)

Before finishing, verify against depth multiplier:

### For 1x (Base):
- [ ] Meta-ARAW strategy selection completed (including restatement, frames, criteria, transfer, novelty target)
- [ ] At least 5 distinct claims identified with VOI ordering
- [ ] Blind spot check completed
- [ ] Non-propositional inputs surfaced
- [ ] Each claim ARAW'd at least 3 levels deep
- [ ] At least 3 sub-claims under each ASSUME RIGHT
- [ ] At least 3 alternatives under each ASSUME WRONG
- [ ] **UNCONVENTIONAL QUOTA MET**: At least 1 unconventional alternative per major ASSUME WRONG
- [ ] **CONVENTIONAL FLAGGED**: Each alternative checked and flagged if conventional
- [ ] VOI-guided prioritization applied (HIGH VOI branches explored deeply)
- [ ] At least 2 CRUX points with full analysis
- [ ] At least 3 DO_FIRST actions
- [ ] Search termination checks applied
- [ ] Dual analysis thorough
- [ ] Synthesis identifies tensions with category classification
- [ ] Commitment status marked with confidence levels
- [ ] **Surprise-Self Test passed** (at least 1 surprising finding)
- [ ] **Escape Hatch Check passed** (no lazy "ask user" recommendations)
- [ ] Session learnings transferred and applied
- [ ] Exploration met depth requirements (claims, levels, thoroughness)
- [ ] **MANDATORY: Session saved** (see Step 11)
- [ ] **MANDATORY: Saved file in range for depth** (1x=250-350, 2x=400-600, 3x=600-900, 4x=800-1100)
- [ ] **MANDATORY: Tensions extracted to `library/araw/tension_questions.md`**
- [ ] **MANDATORY: Insights extracted beyond tensions** (see Step 12.5)

### For 2x:
- [ ] All 1x requirements PLUS:
- [ ] 7 claims, 4 levels deep
- [ ] 3 CRUX points, 4 DO_FIRST actions
- [ ] 400-600 lines saved

### For 3x:
- [ ] All 2x requirements PLUS:
- [ ] 10 claims, 5 levels deep
- [ ] 4 CRUX points, 5 DO_FIRST actions
- [ ] 600-900 lines saved

### For 4x:
- [ ] All 3x requirements PLUS:
- [ ] 12 claims, 6 levels deep
- [ ] 5 CRUX points, 6 DO_FIRST actions
- [ ] 800-1100 lines saved

### For 8x:
- [ ] All 4x requirements PLUS:
- [ ] 18 claims, 8 levels deep
- [ ] 8 CRUX points, 10 DO_FIRST actions
- [ ] 1600-2200 lines saved
- [ ] Multiple parallel AR/AW explorations
- [ ] Cross-claim synthesis (how claims interact)
- [ ] Meta-level patterns identified
- [ ] Full AR technique coverage (all 17 questions applied to major claims)
- [ ] **UNCONVENTIONAL QUOTA**: At least 6 unconventional alternatives across major AW branches

### For 16x:
- [ ] All 8x requirements PLUS:
- [ ] 25 claims, 10 levels deep
- [ ] 12 CRUX points, 14 DO_FIRST actions
- [ ] 3200-4400 lines saved
- [ ] Cross-domain synthesis (insights applied to other fields)
- [ ] Second-order pattern identification (patterns in patterns)
- [ ] Full AR + AW technique coverage on ALL major claims
- [ ] Cross-reference with related prior ARAW sessions
- [ ] Synthesis sections at 4-claim intervals
- [ ] "What would change my mind" for each major conclusion
- [ ] **UNCONVENTIONAL QUOTA**: At least 8 unconventional alternatives across major AW branches

### For 32x:
- [ ] All 16x requirements PLUS:
- [ ] 35 claims, 12 levels deep
- [ ] 16 CRUX points, 20 DO_FIRST actions
- [ ] 6400-8800 lines saved
- [ ] Multi-session continuity plan documented
- [ ] External reference integration
- [ ] Complete claim space mapping (not sampling)
- [ ] Explicit uncertainty quantification on all conclusions
- [ ] Structured progress tracking
- [ ] "Unexplored regions" documentation
- [ ] Adversarial review of major conclusions
- [ ] Meta-analysis of ARAW as applied to this topic
- [ ] **UNCONVENTIONAL QUOTA**: At least 12 unconventional alternatives across major AW branches

**If any checkbox is not met, go back and complete that section.**

**⚠️ The MANDATORY checkboxes MUST be completed. ARAW is incomplete without them.**

**⚠️ COMMON FAILURE: Missing required content. The saved file MUST contain ALL: novel findings, unexpected results, tensions, insights, CRUX points, conclusions, and next actions. Dead-end branches can be trimmed, but all discoveries must be preserved.**

---

## Example: Meta-ARAW in Action

Input: "/araw 2x should I start a business"

```
META-ARAW STRATEGY SELECTION
============================
Restated question: Should the asker start a business (implicitly: now, given their situation)?
Problem type: holistic (interconnected factors)
Uncertainty type: epistemic + model (what do I actually want? is this the right frame?)
Pitfall risk: fish-in-dreams (may be seeking validation for existing desire)
Question quality: needs-reframe (asking "how" when should ask "whether" and "why")
Selected frame: Opportunity frame (vs job frame, vs lifestyle frame)
Criteria: [inferred] Wants actionable recommendation, values autonomy
Transfer from session: [none yet]
Related tensions: #7 Insight vs Resources, #3 Coherence vs Manageability
Novelty target: Something beyond "it depends on your risk tolerance"
Integral goals: Business might serve deeper goal (autonomy? impact? wealth?)
Selected strategy: wide-then-deep (explore alternatives before committing)
Depth: 2x (7 claims, 4 levels, 800+ exploration, 400-600 saved)

Search for opposite: Explore "should I NOT start a business" with equal rigor
Model check: ARAW "starting a business is what I want" before "should I start one"

Proceeding with ARAW...
```

---

## Efficiency Principles

1. **Meta-ARAW first** - 2 minutes of strategy selection saves 20 minutes of wrong-direction search
2. **VOI ordering** - ARAW high-action-divergence claims first
3. **Pitfall awareness** - Check for confirmation bias before each major branch
4. **Commitment testing** - Use confidence levels to know where to focus
5. **Termination discipline** - Stop when diminishing returns, don't grind past value
6. **Natural joints** - Decompose claims along their natural structure
7. **Bidirectional when needed** - Use both forward and backward reasoning
8. **Space awareness** - Check you're searching the right set at right granularity
9. **Efficiency diagnostic** - If taking too long, something's wrong

---

## When ARAW Itself Fails

If ARAW produces:
- Same findings repeatedly → Check for Fish in Dreams
- Explanations that don't fit → Check for Red Herring
- Confusion when approaching topic → Check for Smokescreen

Response: Note the failure pattern, try:
- /araw 2x [topic] - go deeper
- /araw [reframed topic] - change the question
- /space_discovery [topic] - find what space you're missing

---

## EXPERIMENTAL: Trinary ARAW

**Standard ARAW is binary: Assume Right / Assume Wrong.**

**Trinary ARAW adds a third option: Assume Irrelevant.**

Use when you suspect some claims simply don't matter for the decision or understanding at hand.

```
Claim: "[claim]"
│
├── ASSUME RIGHT → What follows if true?
│
├── ASSUME WRONG → What alternatives exist?
│
└── ASSUME IRRELEVANT → What if this doesn't matter?
    │
    ├── Does this claim change action either way?
    ├── Is this a distraction from the real question?
    ├── Are there deeper claims that make this one moot?
    └── What would I focus on instead?
```

**When to use Trinary ARAW:**
- Topic has many claims but limited relevance
- Suspecting some exploration is wasted effort
- VOI thinking suggests low action-divergence for some claims
- Getting lost in branches that feel unproductive

**Trinary filtering question**: "If this claim turned out to be true, AND if it turned out to be false, would my action/understanding change?" If NO to both → IRRELEVANT.

**Note**: Trinary is experimental. Use standard binary ARAW as default. Try Trinary when you feel binary is generating too many unproductive branches.

---

## STEP 11: Save Output (MANDATORY - DO NOT SKIP)

**YOU MUST save the ARAW session to a file. This step is NOT optional.**

⚠️ **CRITICAL**: Do not finish ARAW without saving. Every ARAW session must be persisted.

### Save Location
Save to: `library/araw/sessions/` with filename format:
```
araw_[YYYY-MM-DD]_[topic-slug].md
```

Example: `araw_2026-01-26_json-vs-markdown.md`

### File Format
```markdown
---
date: [YYYY-MM-DD HH:MM]
topic: [original input]
depth: [1x/2x/3x/4x/8x/16x/32x]
claims: [number identified]
crux_points: [number identified]
status: [FOUNDATIONAL/LIKELY/UNCERTAIN/MIXED]
session: [1 of N for multi-session 16x/32x]
---

# ARAW: [Topic]

[COMPLETE ARAW output - NOT a summary]
```

### Multi-Session Handling (16x/32x)

For 16x and 32x ARAWs that may exceed context limits:

1. **End each session with state save:**
   - Claims covered so far
   - Claims remaining
   - Key findings to carry forward
   - Open questions for next session

2. **Start continuation sessions with:**
   - Read prior session file(s)
   - Load state from last session
   - Continue from where stopped

3. **File naming for multi-session:**
   - `araw_[date]_[topic]_session1.md`
   - `araw_[date]_[topic]_session2.md`
   - `araw_[date]_[topic]_final.md` (synthesis)

### What "Complete" Means

**⚠️ CRITICAL: Every table and structured analysis you created must be saved.**

The saved file MUST include (non-negotiable):
- Meta-ARAW strategy selection (full block)
- **ALL TABLES you created** (claims, blind spots, inventories, assessments, etc.)
- **ALL ARAW trees** for major claims (the AR/AW branch structures)
- **ALL novel/surprising findings** [NOVEL] tags
- **ALL unexpected results**
- **ALL tensions discovered** with category classification
- **ALL insights**
- CRUX points (full format: question/why/test/implications)
- DO_FIRST actions (full format: what/why/how/resolves)
- Dual analysis (contrarian + non-contrarian)
- Synthesis and conclusions
- Confidence assessment table
- Surprise-self test table
- Next actions

**Rule: If you created it during analysis, it goes in the saved file.**

Can be trimmed (ONLY these):
- Dead-end AR/AW sub-branches at depth 4+ (note "explored, no insight")
- Conventional paths that confirmed obvious expectations without novel findings
- Repetitive deep exploration (summarize pattern once)

### Expected Line Counts (Sanity Check)

| Depth | Saved Lines | If Much Shorter |
|-------|-------------|-----------------|
| 1x | 250-350 | Missing insights/tensions/conclusions |
| 2x | 400-600 | Missing insights/tensions/conclusions |
| 3x | 600-900 | Missing insights/tensions/conclusions |
| 4x | 800-1100 | Missing insights/tensions/conclusions |
| 8x | 1600-2200 | Missing insights/tensions/conclusions |
| 16x | 3200-4400 | Missing cross-domain synthesis/second-order patterns |
| 32x | 6400-8800 | Missing complete mapping/adversarial review |

**If your saved file is below the minimum, you're missing required content (insights, tensions, conclusions). Dead-end branches can be trimmed, but all discoveries must be included.**

### Saving Large Files (Token Limit Workaround)

**For 3x, 4x, and 8x ARAWs**, output token limits may prevent saving via Write tool. Use bash heredoc instead:

```bash
cat > library/araw/sessions/araw_[date]_[topic].md << 'ENDOFARAW'
[paste complete ARAW content here]
ENDOFARAW
```

**Alternative: Incremental writing** - Write the ARAW in sections as you go, appending to the file.

### Common Mistake

❌ WRONG: Saving only final conclusions without novel findings, tensions, insights
✅ RIGHT: Saving all discoveries (novel, unexpected, tensions, insights) - trimming only dead-end branches

### Naming Rules for Topic Slug
- Lowercase
- Replace spaces with hyphens
- Remove special characters
- Max 50 characters
- Examples:
  - "Should I start a business?" → `should-i-start-a-business`
  - "JSON vs Markdown" → `json-vs-markdown`
  - "Is this the right approach?" → `is-this-the-right-approach`

**Execute this step NOW before proceeding.**

---

## STEP 12: Extract Tension-Resolving Questions (MANDATORY - DO NOT SKIP)

**YOU MUST extract tensions to the shared library. This step is NOT optional.**

⚠️ **CRITICAL**: Do not finish ARAW without extracting tensions.

### Why
Tensions are high-leverage points. The questions that would resolve them are valuable for future ARAWs and searches.

### Process
For each tension in the synthesis:
1. **State the tension** (AR position vs AW position)
2. **Classify by category** (6 tension categories)
3. **Generalize** - What's the universal form of this tension?
4. **Write the resolving question** - What observation would distinguish?
5. **Write to file** - Append to `library/araw/tension_questions.md`

### Generalization Examples

| Specific Tension | Universal Form |
|-----------------|----------------|
| Integration vs Separation (of ARAW systems) | When does combining components create synergy vs complexity? |
| Light model vs Claude-only | When is cheap+fast+weak better than expensive+slow+strong? |
| Chunking vs Single-session | When does breaking work into pieces help vs lose coherence? |
| Library seeding vs Fresh generation | When does prior knowledge help vs constrain discovery? |
| Automation vs Human-in-loop | When does human judgment add value vs create bottleneck? |

### File Format
Append to `library/araw/tension_questions.md`:

```markdown
## [Number]. [Universal Tension Name] ([Category] Trade-off)

**Specific instance**: [AR position] vs [AW position]
**Universal form**: [Abstracted tension that applies beyond this case]

**Resolving questions**:
1. [Question that would distinguish between AR and AW]
2. [Test or observation that would resolve it]
3. [Additional question if needed]

**When AR wins**: [Conditions where AR position is correct]
**When AW wins**: [Conditions where AW position is correct]

**Test**: [Specific test to determine which wins in a given case]

**Source**: [ARAW session file]
```

**Execute this step NOW using the Edit tool to append to tension_questions.md.**

---

## STEP 12.5: Extract Other Insights (MANDATORY - NEW)

**Tensions are not the only valuable outputs.** Also extract:

### Types of Insights to Extract

| Insight Type | Where to Save | Example |
|--------------|---------------|---------|
| **New framework/stack** | `claude-code-plugin/data/guess_libraries/universal/[number]_[name].md` | Problem-Solving Stack |
| **Procedure improvement** | Update relevant SKILL.md | Adding Step -1 to ARAW |
| **Domain-specific pattern** | `claude-code-plugin/data/guess_libraries/[domain]/` | Negotiation patterns |
| **Meta-insight about GOSM** | `library/learnings/` | "65% of failures at Noticing+Framing" |
| **Reusable question set** | `claude-code-plugin/data/guess_libraries/universal/` | VOI questions |

### Extraction Checklist

After completing ARAW, ask:

- [ ] **New framework discovered?** → Create VOI file in guess_libraries
- [ ] **Procedure improvement identified?** → Update relevant SKILL.md
- [ ] **Reusable pattern found?** → Document in appropriate location
- [ ] **Meta-learning about GOSM?** → Add to learnings
- [ ] **Nothing new?** → That's fine, not every ARAW produces extractable insights

**Don't force extraction if nothing genuinely new was discovered.**

---

## COMPLETION VERIFICATION

**Before finishing ARAW, verify these files exist and were written in THIS session:**

1. ✅ Session file saved: `library/araw/sessions/araw_[date]_[topic-slug].md`
2. ✅ Tensions appended: `library/araw/tension_questions.md`
3. ✅ Other insights extracted (if any): [appropriate locations]

**If any file was NOT written, go back and complete Steps 11-12.5 NOW.**

**ARAW is not complete until all extraction is done.**

---

## APPENDIX: Validation and External Review

### Known Limitations of ARAW Self-Evaluation

**ARAW cannot validly evaluate itself.** This is a structural limitation:

1. **Blind spot preservation**: What ARAW doesn't consider, ARAW-on-ARAW won't consider
2. **Recursive validity**: If ARAW finds "ARAW is flawed," can we trust that finding?
3. **Historical pattern**: User feedback has been the actual source of ARAW improvements, not internal sessions

### When to Seek External Validation

| Situation | Action |
|-----------|--------|
| Conclusions feel too convenient | Get external review |
| No surprises in analysis | May be confirming expectations - external check |
| High-stakes decision | External validation before acting |
| Meta-analysis of ARAW itself | External perspective required |
| User expresses doubt about analysis | Take seriously, don't defend |

### How to Get External Validation

1. **User feedback**: Most reliable source of ARAW improvements historically
2. **Comparison study**: Run same problem through ARAW vs alternative method
3. **Expert review**: Have domain expert evaluate output
4. **Prediction tracking**: Make predictions, track outcomes, update

### Comparison Study Framework

To validate ARAW against alternatives:

```
COMPARISON STUDY TEMPLATE
=========================

Problem: [Specific question or decision]

Methods to compare:
1. ARAW (full or lite)
2. [Alternative: e.g., Bayesian, Fast-and-frugal, Pre-mortem, Decision tree]
3. [Baseline: intuition/quick judgment]

Run each method on same problem. Evaluate:
- Accuracy: Did it reach correct/useful conclusion?
- Efficiency: Time/effort to reach conclusion?
- Actionability: Did it produce clear next steps?
- Surprises: Did it surface non-obvious insights?
- Coverage: Did it miss important factors?

Record results. If alternative beats ARAW on all dimensions,
consider switching. If mixed, use portfolio approach.
```

### Alternative Reasoning Methods (For Comparison)

| Method | Best For | Strength | Weakness |
|--------|----------|----------|----------|
| **Bayesian reasoning** | Uncertainty quantification | Explicit probabilities | Prior specification hard |
| **Fast-and-frugal** | Quick decisions | Efficient, ecologically valid | May miss factors |
| **Pre-mortem** | Failure anticipation | Psychologically easier | Focused on failure only |
| **Decision trees** | Quantitative choices | Clear structure | Requires probability/value estimates |
| **Dialectical** | Thesis/antithesis synthesis | Handles contradiction | Less structured |

### ARAW's Niche

ARAW is optimal for: **Thorough exploration of complex, propositional, high-stakes questions where hidden assumptions need surfacing.**

ARAW is NOT optimal for:
- Quick everyday decisions → Use ARAW-Lite or heuristics
- Non-propositional domains → Use intuition, patterns, images
- Action-oriented tasks → Use GOSM-After (reflection mode)
- Self-evaluation → Need external perspective
- Time pressure → Use GOSM-Lite (5 steps)
- Low stakes → Use GOSM-Quick (2 steps)
- Expert validation → Use GOSM-Check (validation only)

### Method Selection Matrix

| Situation | Best Method |
|-----------|-------------|
| HIGH stakes + novel domain + time available | ARAW Full (8x if critical) |
| HIGH stakes + time pressure | GOSM-Lite |
| MED stakes + normal time | GOSM-Standard |
| LOW stakes + reversible | GOSM-Quick |
| Expert domain + validation needed | GOSM-Check |
| Action-first + learning | GOSM-After |
| Uncertainty quantification | Bayesian reasoning |
| Failure anticipation | Pre-mortem |
| Quick heuristic | Fast-and-frugal |

**Match the method to the task.**

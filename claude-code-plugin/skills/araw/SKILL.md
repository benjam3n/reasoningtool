---
name: araw
description: Assume Right / Assume Wrong search - The core exploration method. For every claim, branch into what follows if true vs what alternatives exist if false.
---

# ARAW - Assume Right / Assume Wrong Search

**Input**: $ARGUMENTS

---

## What is ARAW?

ARAW = Assume Right / Assume Wrong. A method for exploring claims.

For any claim, two branches get explored with equal rigor:
- **ASSUME RIGHT**: What follows if this is true?
- **ASSUME WRONG**: What alternatives exist?

Then it recurses - conclusions are also claims.

## What does it do?

- Test hypotheses systematically
- Expand your option space
- Surface assumptions you didn't know you had
- Find alternatives to "obvious" answers

## Why use it when you're already right?

**When you're right**: Know WHY. Know the edge cases. Hold tested confidence instead of untested belief.

**When alternatives exist**: See options you hadn't considered. Understand trade-offs. Choose instead of default.

---

## ⚠️ CORE PRINCIPLES (Read First)

### Principle 1: EXPLORATION DEPTH OVER FORMAT COMPLIANCE

**The purpose of ARAW is deep exploration, not neat formatting.**

Early high-quality sessions had 5-6 level deep trees because they followed the exploration wherever it led. Later degraded sessions had 2-3 level trees because they focused on checkbox compliance.

**DERIVATION MODE** (correct): Let structure emerge from exploration
- Follow surprising branches deeper
- Structure reflects what you discovered
- Format serves insight, not the reverse

**ENUMERATION MODE** (incorrect): Fill out a predetermined template
- Hit quotas regardless of insight
- Structure imposed before exploration
- Format constrains discovery

**If you find yourself checking boxes instead of following curiosity, you're in ENUMERATION mode. Stop and explore deeper.**

### Principle 2: NO EARLY TERMINATION

When the user specifies a depth (e.g., 8x), produce output meeting that depth's requirements:

| Depth | Claims | CRUX | DO_FIRST | Saved Lines | Tree Depth |
|-------|--------|------|----------|-------------|------------|
| 1x | 5 | 2 | 3 | 250-350 | 3-4 levels |
| 2x | 7 | 3 | 4 | 400-600 | 4-5 levels |
| 4x | 12 | 5 | 6 | 800-1100 | 5-6 levels |
| 8x | 18 | 8 | 10 | 1600-2200 | 6-8 levels |
| 16x | 25 | 12 | 14 | 3200-4400 | 8-10 levels |
| 32x | 35 | 16 | 20 | 6400-8800 | 10-12 levels |

**Note**: These depth scaling numbers are heuristics, not empirically derived. The key metric is exploration depth (tree levels), not line count. Use these as guides, not rigid targets.

**Tree depth is as important as claim count.** A session with 18 claims but only 2-3 level trees has failed. Depth means depth of exploration, not just breadth.

### Principle 3: LITERAL DEPTH INTERPRETATION

When user says `/araw 8x [topic]`:
- They want 8x depth analysis
- They do NOT want meta-analysis about whether to do ARAW
- Take the depth specification literally. Execute it.

### Principle 4: META-ARAW IS QUICK, NOT THE RESPONSE

Meta-ARAW (Step 0) should be ~50 lines maximum, completed in the first 5% of output.

---

## ARAW-Lite (Quick Decision Mode)

For low-stakes, reversible, time-sensitive decisions:

```
ARAW-LITE: [topic]
==================
CLAIM: [Single most important claim]

ASSUME RIGHT:
├── What becomes possible? [1-2 sentences]
├── Easy path? [1-2 sentences]
└── What would we observe if true? [1 prediction]

ASSUME WRONG:
├── Best alternative? [1-2 sentences]
├── What would make this false? [1-2 sentences]
└── Risk? [1-2 sentences]

VERDICT: [PROCEED / RECONSIDER / NEED MORE INFO]
ACTION: [One specific next step]
```

ARAW-Lite is NOT saved. For quick decisions only.

---

## STEP 0: META-ARAW (Strategy Selection)

Quick meta-analysis to select the right search strategy (~50 lines max).

**When to use Meta-ARAW:**
- **For 1x-2x**: OPTIONAL. Skip directly to claims if input is clear and unambiguous.
- **For 4x+**: REQUIRED. Frame selection has high leverage at deeper analysis - wrong frame wastes the entire analysis.

### 0.1: Question Restatement

```
RESTATED QUESTION: [Your understanding]
ORIGINAL: [The original input]
```

If your interpretation differs from input, ARAW BOTH interpretations.

### 0.2: Problem Structure Check

| Question | If YES | If NO |
|----------|--------|-------|
| Decomposable into independent subproblems? | ARAW each separately | ARAW holistically |
| Closed-form answer exists? | Don't ARAW - calculate | ARAW appropriate |

### 0.3: Uncertainty Type

| Uncertainty | Strategy |
|-------------|----------|
| **Epistemic** (reducible by learning) | Deep ARAW to find what to learn |
| **Aleatoric** (irreducible randomness) | Light ARAW, then hedge |
| **Model uncertainty** (wrong framework) | ARAW the framework first |

### 0.4: Pitfall Check

Before starting:
- **Fish in Dreams**: Expecting a specific answer? (Search for opposite)
- **Red Herring**: Explanation matches what you're explaining? (Check fit)
- **Smokescreen**: Confusion when approaching? (Persist through)

### 0.5: Multiple Frame Generation

Try at least 3 frames before committing:
- Stated frame (what the question assumes)
- Opposite frame (what if opposite assumption true?)
- Broader/narrower frame (zoom in/out)
- Different domain frame (how would someone else see this?)

**Pick the frame that opens the most options.**

### 0.6: Dimension Discovery (Pre-ARAW Universalization)

**ARAW can only test dimensions you know exist.** Before AR/AW, discover dimensions.
[D: derived from araw_2026-01-28_araw-vs-universalization.md - Boolean blindspot fix]

Apply quick universalization to find dimensions to ARAW:

| Technique | Question | Dimension Discovered |
|-----------|----------|---------------------|
| STATE SPACE | What states could the claim be in? | State dimension |
| INSTANCE-TO-CATEGORY | What is this claim an instance of? | Category dimension |
| PARAMETER VARIATION | What parameters could vary? | Parameter dimensions |
| ROLE REVERSAL | What if roles were reversed? | Role dimension |
| TEMPORAL VARIATION | What if timing varied? | Time dimension |
| SCALE VARIATION | At what level is this? | Scale dimension |
| PERSPECTIVE ROTATION | Whose view is this? | Stakeholder dimension |

**Output**: List of dimensions to include in ARAW exploration.

```
DIMENSIONS DISCOVERED
=====================
From stated claim: [list obvious dimensions]
From universalization:
- [Technique 1] → [New dimension found]
- [Technique 2] → [New dimension found]
...
Will ARAW along these dimensions: [list]
```

**Time budget**: ~2-3 minutes. Don't over-invest; this is for dimension discovery, not full universalization.

### 0.6: Strategy Selection Output

```
META-ARAW STRATEGY SELECTION
============================
Restated question: [your understanding]
Problem type: [decomposable/holistic/closed-form]
Uncertainty type: [epistemic/aleatoric/model]
Pitfall risk: [fish-in-dreams/red-herring/smokescreen/none]
Selected frame: [which frame]
Novelty target: [what would be surprising to find?]
Depth: [1x/2x/4x/8x/16x/32x]

Proceeding with ARAW...
```

---

## STEP 0.7: Claim Evaluability Check

**ARAW operates on claims that can be true or false.** Many inputs are not evaluable claims - they're decisions, intentions, conclusions, or requests.

### Evaluability Test

Ask: Can this input be directly assumed right or assumed wrong?

| Input Type | Evaluable? | Example |
|------------|------------|---------|
| **Factual claim** | YES | "The API is slow" |
| **Belief** | YES | "Users prefer X over Y" |
| **Assumption** | YES | "This approach will scale" |
| **Decision/Intent** | NO | "I need to quit my job" |
| **Request** | NO | "Help me with X" |
| **Conclusion** | NO | "I should do Y" |

### If NOT Evaluable: Extract Claims Through Questioning

When input cannot be directly assumed right/wrong, question to extract the underlying claims:

**Example: "I need to quit my job"**

This is a conclusion, not a claim. Cannot ARAW directly.

**Questions to extract claims:**
- What's happening that makes quitting seem necessary?
- What would quitting accomplish?
- What's the problem the job is causing?

**Claims extracted (universalized form):**
1. A problem exists
2. The job is causing it
3. Quitting removes the cause
4. The costs of quitting are acceptable
5. What comes after is better

**Now ARAW these claims.**

### Universalizing Claims

Convert personal/specific claims to universalized form:

| Personal | Universalized | Broader Question Answered |
|----------|---------------|---------------------------|
| "I correctly identified the problem" | "A problem exists" | Is there a problem? |
| "I have no alternatives" | "Alternatives exist" (AW this) | Are there alternatives? |
| "I know what I want" | "What is wanted is known" | Is the desired state clear? |

**Why universalize?** Universalized claims answer the broader, more fundamental question. "A problem exists" immediately invites ASSUME WRONG: "What if there isn't actually a problem?" - which is often the more important question.

### Output Format

```
EVALUABILITY CHECK
==================
Input: [original input]
Type: [claim / decision / intent / request / conclusion]
Evaluable directly? [YES/NO]

If NO:
Questions asked:
- [Q1]
- [Q2]

Claims extracted (universalized):
1. [Claim 1] - answers: [broader question]
2. [Claim 2] - answers: [broader question]

Proceeding to ARAW these claims...
```

---

## STEP 1: Identify Claims

Parse the input into distinct claims:

1. **Explicit claims** - Directly stated
2. **Implicit claims** - Assumed but not stated
3. **Bundled claims** - Multiple claims packed into one
4. **Presupposition claims** - What must be true for statement to make sense
5. **Meta-claims** - Claims about the framing itself

**Unbundling example:**

For "I need to quit my job" (after passing evaluability check and extracting claims):

| Claim (universalized) | Broader Question |
|-----------------------|------------------|
| A problem exists | Is there actually a problem? |
| The job is causing it | Is the job the source? |
| Quitting removes the cause | Will quitting fix it? |
| Alternatives do not exist | Are there other options? |
| What comes after is better | Is the after-state known and preferable? |

ARAW then explores each claim (assume right, assume wrong).

For each claim:
- State precisely
- Note type: explicit/implicit/bundled/presupposed/meta
- Rate importance: HIGH/MED/LOW
- **VOI rating**: How much would knowing this change action?

**ARAW high-VOI claims first.** They determine the most.

### Blind Spot Check

After identifying claims:
- **Perspective**: Who else cares? What would they see?
- **Domain**: What would an adjacent-field expert notice?
- **Temporal**: What past/future factors am I ignoring?
- **Scale**: What at 10x smaller or larger?

---

## STEP 2: ARAW Each Claim

For EACH claim, build a tree. **Key insight**: Explore BOTH AR and AW at EVERY node. Paths can be AR→AW→AW→AR→...

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
│   └── Sub-claims → Full ARAW each
│
└── ASSUME WRONG → Claim might be false/unnecessary
    │
    ├── What alternatives exist?
    │   ├── Alternative 1
    │   │   ├── ASSUME RIGHT → [explore this alternative]
    │   │   └── ASSUME WRONG → [why alternative also wrong]
    │   └── [more alternatives...]
    │
    ├── What would make this claim false?
    ├── What's the opposite claim? → Full ARAW
    └── Sub-claims → Full ARAW each
```

### Tree Depth Requirements

**This is critical.** The degradation pattern is shallow trees (2-3 levels) when deep trees (5-6+ levels) are needed.

| Depth | Minimum Tree Levels | What This Means |
|-------|---------------------|-----------------|
| 1x | 3-4 levels | AR→AW→AR minimum for major claims |
| 2x | 4-5 levels | Explore consequences of consequences |
| 4x | 5-6 levels | Find non-obvious implications |
| 8x | 6-8 levels | Exhaust the possibility space |

**If your trees are only 2-3 levels deep, you're not doing ARAW, you're listing.**

### How to Achieve Tree Depth

For 4x+ depth, apply this technique:

1. **Every ASSUME RIGHT gets sub-claims** - Ask "What follows from this?"
2. **Every sub-claim gets ASSUME WRONG** - Ask "What if this sub-claim is wrong?"
3. **Recurse: AR→AW→AR→AW** until you hit:
   - **Foundation** (questioning becomes circular)
   - **Prediction** (testable claim - move to CRUX)
   - **Decision** (not a claim - extract underlying claim first)
4. **When stuck at 3 levels**, ask:
   - For AR branches: "Why is this true?" or "What else follows?"
   - For AW branches: "What else could it be?" or "What's another alternative?"

**The key**: Don't stop at the first AR/AW. Every AR produces claims that need AW. Every AW produces alternatives that need AR.

### Upside Exploration (Anti-Conservative Bias)

For every ASSUME WRONG that says "this is too ambitious," ALSO explore ASSUME RIGHT for the ambitious version:

| Conservative Thought | Counter-Exploration |
|----------------------|---------------------|
| "This ROI is unrealistic" | "What if this ROI IS achievable?" |
| "This is too hard" | "What if this is actually doable?" |
| "Nobody does this" | "What if being first is the advantage?" |

**Explore success modes, not just failure modes.**

### Multi-Valued AW: State Space Expansion

**Standard ARAW is binary**: claim true/false. But "wrong" has multiple values.

When you ASSUME WRONG, don't just negate - **expand to the full state space**:

```
Claim: "We should use approach X"

Binary AW (limited):
└── ASSUME WRONG → "We should NOT use approach X"

Multi-valued AW (complete):
└── ASSUME WRONG → What's the state space?
    ├── Alternative approach Y
    ├── Alternative approach Z
    ├── Hybrid X+Y
    ├── Neither - reframe the problem
    ├── Different timing for X
    └── X but with modifications
```

**Apply universalization techniques to AW branches:**
- INSTANCE-TO-CATEGORY: "X is a type of [category]. What other instances exist?"
- PARAMETER VARIATION: "What if X's parameters were different?"
- ROLE REVERSAL: "What if we did the opposite of X?"

This combines ARAW's rigor with Universalization's completeness.
[D: derived from araw_2026-01-28_araw-vs-universalization.md - Boolean vs Type logic integration]

### AW Approach by Claim Type

Not all claims need state space expansion. Match the AW approach to the claim type:

| Claim Type | AW Approach | Example |
|------------|-------------|---------|
| **Factual** | Binary (true/false) | "The API is slow" → Is it or isn't it? |
| **Strategic** | State space (alternatives) | "Use microservices" → What other architectures? |
| **Design** | State space (options) | "Add dark mode" → What other features address this need? |
| **Causal** | Alternative causes | "X causes Y" → What else could cause Y? |
| **Belief** | Binary + evidence | "Users prefer X" → True/false, what's the evidence? |
| **Assumption** | State space | "This will scale" → What if it doesn't? What would need to be true? |

**Rule of thumb**: If the claim is about existence/truth, use binary. If the claim is about choice/approach, expand the state space.

### Unconventional Alternative Requirement

For each major ASSUME WRONG, include genuinely unconventional alternatives (not just the obvious opposite):

- What if the opposite of conventional wisdom is true?
- What would an outsider/novice suggest?
- What hasn't been tried, and why?
- What would be embarrassing to suggest but might work?
- What would a 10x more ambitious version look like?

### AR Generative Techniques

Make AR active, not just confirmatory:

| Technique | Question | Produces |
|-----------|----------|----------|
| **Easy Path** | "What would make this EASY?" | Simplifications |
| **Possibility Expansion** | "What becomes possible now?" | New options |
| **Predictions** | "If true, what would we observe?" | Testable predictions |
| **Leverage** | "Where is 10x impact available?" | High-leverage points |

---

## STEP 3: Search Quality Checks

During exploration, continuously check:

- **Decomposition**: Are subproblems solvable? Cutting along natural joints?
- **Inference Direction**: Forward or backward? Confirmation bias active?
- **Search Space**: Searching right set? Right granularity? Any false constraints?

---

## STEP 4: Commitment Test

For each branch, assign confidence:

| Level | Confidence | When |
|-------|------------|------|
| **FOUNDATIONAL** | 0.9+ | All AW paths contradict |
| **LIKELY** | 0.7-0.9 | Most AW paths contradict |
| **UNCERTAIN** | 0.3-0.7 | AR and AW both have merit |
| **UNLIKELY** | 0.1-0.3 | Most AR paths have problems |
| **IMPLAUSIBLE** | <0.1 | AR paths contradict each other or reality |

---

## STEP 5: Identify CRUX Points

**CRUX**: The observation that would most decisively distinguish branches.

### CRUX N: [Primary crux]
- **The question**: [precise question]
- **Branches resolved**: [which branches this would resolve]
- **Why decisive**: [why this maximally splits uncertainty]
- **How to test**: [how to find out]
- **If X**: [what follows]
- **If Y**: [what follows]

**The best CRUX resolves the most branches.** When choosing between CRUXes, prefer higher branch count.

---

## STEP 6: Identify DO_FIRST Actions

List in priority order. Specify WHO does each:

### DO_FIRST N: [Action]
- **Who**: [Claude / User]
- **What**: [specific action]
- **Why first**: [why before anything else]
- **How**: [concrete steps]
- **What it resolves**: [which branches/questions]

**Preference order**:
1. Claude does it now
2. Claude does it with user go-ahead
3. User does minimum viable version (only what Claude cannot do)

---

## STEP 7: Search Termination (For Individual Branches)

For each branch, ask:
- Would resolving this change my action? (If NO: summarize and move on)
- What's the marginal value of more depth? (If LOW: stop this branch)
- Am I exploring because it matters or because procedure says to? (If procedure: question)

**This is about branch allocation, not overall depth reduction.** If user specified 8x, still hit 18 claims, 8 CRUX, 10 DO_FIRST.

---

## STEP 8: Synthesis and Recommendations

### Key Tensions Discovered
- [Tension 1]: ASSUME RIGHT says X, ASSUME WRONG says Y
- [Tension 2]: [another tension]

Classify each tension:
| Category | Master Question |
|----------|-----------------|
| **Resource Allocation** | What resource is limited, and competing uses? |
| **Information** | What don't we know, how much does it matter? |
| **Optimization** | What's Pareto frontier, where to sit? |
| **Commitment** | How reversible, how much is option value worth? |

### What Would Resolve These Tensions
- [Resolution approach 1]
- [Resolution approach 2]

### Confidence Assessment
- **Confidence in RIGHT branches**: [level] because [reasoning]
- **Confidence in WRONG branches**: [level] because [reasoning]
- **Key uncertainties remaining**: [list]

### FOUNDATIONAL Claims Identified
- [Claim 1]: [confidence level]
- [Claim 2]: [confidence level]

### Surprise-Self Test

| Question | Answer |
|----------|--------|
| Did any finding surprise you? | Yes → Good / No → Search harder |
| Would you have predicted this before starting? | No → Good / Yes → Check for confirmation |
| Anything that challenges initial view? | Yes → Good / No → Check for Fish in Dreams |

**If NO surprises: Go back and search harder.**

---

## STEP 9: Determine Next Procedure

| Situation | Next |
|-----------|------|
| Alternatives need comparison | /comparison |
| Root cause unclear | /root_cause_5_whys |
| Ready to trace journey | /goal_journey_system |
| Still unclear after analysis | /araw 2x (go deeper) |

---

## Pre-Completion Check

```
DEPTH VERIFICATION
==================
Specified depth: [Nx]
Required: [claims] claims, [CRUX] CRUX, [DO_FIRST] DO_FIRST, [lines] saved lines

Actual claims: [count]
Actual CRUX: [count]
Actual DO_FIRST: [count]
Actual tree depth (average): [levels]

Status: [MEETS / BELOW MINIMUM]
```

**If BELOW MINIMUM**: Do NOT submit. Go back and explore deeper.

---

## Output Verification (5 Essential Checks)

Before finishing:

1. [ ] **AR and AW explored with equal rigor?** (Both sides get deep trees)
2. [ ] **Tree depth adequate?** (5-6+ levels for 4x+, not just 2-3)
3. [ ] **Novel findings exist?** (At least ONE surprise, mark with [NOVEL])
4. [ ] **Tensions identified?** (AR vs AW conflicts noted)
5. [ ] **File will be saved?** (Step 10)

**That's it. Five checks. Not twenty.**

---

## Example: Meta-ARAW in Action

Input: "/araw 2x should I start a business"

```
META-ARAW STRATEGY SELECTION
============================
Restated question: Should the asker start a business (now, given their situation)?
Problem type: holistic
Uncertainty type: epistemic + model
Pitfall risk: fish-in-dreams (may be seeking validation)
Selected frame: Opportunity frame (vs job frame, vs lifestyle frame)
Novelty target: Something beyond "it depends on your risk tolerance"
Depth: 2x (7 claims, 4 levels, 400-600 saved)

Proceeding with ARAW...
```

---

## Efficiency Principles

1. **Meta-ARAW first** - 2 minutes of strategy selection saves 20 of wrong-direction search
2. **VOI ordering** - ARAW high-action-divergence claims first
3. **Commitment testing** - Use confidence levels to know where to focus
4. **Natural joints** - Decompose along natural structure
5. **Bidirectional when needed** - Both forward and backward reasoning

---

## When ARAW Fails

If ARAW produces:
- Same findings repeatedly → Check for Fish in Dreams
- Explanations that don't fit → Check for Red Herring
- Confusion when approaching → Check for Smokescreen

Try:
- /araw 2x [topic] - go deeper
- /araw [reframed topic] - change the question
- /space_discovery [topic] - find what space you're missing

---

## STEP 10: Save Output (MANDATORY)

Save to: `library/araw/sessions/araw_[YYYY-MM-DD]_[topic-slug].md`

### File Format
```markdown
---
date: [YYYY-MM-DD HH:MM]
topic: [original input]
depth: [1x/2x/4x/8x/16x/32x]
claims: [number]
crux_points: [number]
status: [FOUNDATIONAL/LIKELY/UNCERTAIN/MIXED]
---

# ARAW: [Topic]

[COMPLETE ARAW output - NOT a summary]
```

### What Must Be Saved
- Meta-ARAW strategy selection
- All ARAW trees (the AR/AW branch structures)
- All [NOVEL] findings
- All tensions with category
- CRUX points
- DO_FIRST actions
- Synthesis and conclusions

### What Can Be Trimmed
- Dead-end branches at depth 4+ (note "explored, no insight")
- Repetitive deep exploration (summarize pattern once)

### Line Count Sanity Check
If saved file is much shorter than target (e.g., 500 lines for 8x instead of 1600), you're missing required content.

### For Large Files
Use bash heredoc:
```bash
cat > library/araw/sessions/araw_[date]_[topic].md << 'ENDOFARAW'
[content]
ENDOFARAW
```

---

## STEP 11: Extract Tensions (MANDATORY)

Append to `library/araw/tension_questions.md`:

```markdown
## [Number]. [Universal Tension Name] ([Category] Trade-off)

**Specific instance**: [AR position] vs [AW position]
**Universal form**: [Abstracted tension]

**Resolving questions**:
1. [Question that would distinguish]
2. [Test or observation that would resolve]

**When AR wins**: [Conditions]
**When AW wins**: [Conditions]

**Source**: [ARAW session file]
```

---

## STEP 12: Extract Other Insights (If Any)

If genuinely new framework, procedure improvement, or pattern discovered:
- New framework → `claude-code-plugin/data/guess_libraries/`
- Procedure improvement → Update relevant SKILL.md
- Meta-insight about GOSM → `library/learnings/`

**Don't force extraction if nothing genuinely new was discovered.**

---

## APPENDIX: When NOT to Use ARAW

ARAW is optimal for: **Thorough exploration of complex, propositional, high-stakes questions where hidden assumptions need surfacing.**

ARAW is NOT optimal for:
- Quick everyday decisions → ARAW-Lite
- Time pressure → GOSM-Lite
- Low stakes → Quick heuristics
- Action-oriented tasks → GOSM-After

**Match the method to the task.**

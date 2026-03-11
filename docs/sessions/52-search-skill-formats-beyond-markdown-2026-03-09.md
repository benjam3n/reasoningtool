# /search Explore the space of possible skill formats beyond structured markdown
**Date:** 2026-03-09
**Skill:** /search (Explore a Space)

---

## Routing

- **Space type**: Option/landscape space — "What formats could thinking procedures be encoded in?"
- **How much is known**: Some things known — the user already uses structured markdown and has named several candidate formats
- **Completeness**: Representative — we want the key approaches, not every conceivable encoding
- **Dimensions**: Unclear — we don't know all the axes along which formats can vary
- **Path**: /dd (discover dimensions) then /se (enumerate representative formats)

---

## Phase 1: Dimension Discovery

### Step 1: Seed Examples

```
EXAMPLES FOR: thinking procedure formats

1. Structured markdown (current format — phases, steps, templates, failure modes)
2. Python function with docstring and control flow
3. JSON schema defining required fields and valid values
4. Flowchart / decision tree (visual branching logic)
5. Interactive CLI wizard (step-by-step prompts)
6. Pure natural language narrative ("When someone gives you a claim, first...")
7. State machine (states + transitions + guards)
8. Jupyter notebook (interleaved explanation and executable cells)
9. YAML pipeline (like CI/CD — stages, steps, conditions)
10. Socratic dialogue template (question-response pairs)
```

### Step 2: Compare for Differences

```
COMPARING: Structured markdown vs Python function
Differences:
- Execution model: interpreted by LLM vs executed by runtime -> Potential dimension: EXECUTOR
- Rigidity: flexible natural language vs strict syntax -> Potential dimension: FORMALITY
- Branching: implicit ("if the user...") vs explicit (if/else) -> Potential dimension: CONTROL FLOW EXPLICITNESS

COMPARING: JSON schema vs Flowchart
Differences:
- Modality: text vs visual -> Potential dimension: MODALITY
- What it specifies: structure/shape vs process/sequence -> Potential dimension: WHAT IT ENCODES
- Interactivity: static definition vs navigable path -> Potential dimension: INTERACTIVITY

COMPARING: CLI wizard vs Natural language narrative
Differences:
- Who drives: system prompts user vs user reads and self-directs -> Potential dimension: LOCUS OF CONTROL
- State: wizard tracks where you are vs narrative is stateless -> Potential dimension: STATEFULNESS
- Adaptivity: wizard branches on input vs narrative is fixed -> Potential dimension: ADAPTIVITY

COMPARING: State machine vs YAML pipeline
Differences:
- Topology: can loop/revisit vs linear sequence -> Potential dimension: TOPOLOGY
- Formalism level: mathematical vs configuration -> Potential dimension: FORMALISM
```

### Step 3: Universal Dimensions Applied

| Dimension | Question | Meaningful for skill formats? |
|-----------|----------|-------------------------------|
| **WHO** | Who executes the procedure? | YES — LLM, human, code runtime, hybrid |
| **WHAT** | What does the format encode? | YES — sequence, structure, constraints, dialogue |
| **WHEN** | Time frame? | Marginal — all are used at invocation time |
| **WHERE** | Context? | Marginal — all are in-session |
| **WHY** | Purpose? | Partially — some formats suit teaching, others suit execution |
| **HOW** | Method? | YES — textual, visual, interactive, executable |
| **HOW MUCH** | Scale/degree of formality? | YES — informal prose to formal specification |

### Step 4: Domain-Specific Dimensions

```
DOMAIN-SPECIFIC DIMENSIONS FOR: thinking procedure formats

1. EXECUTOR
   - What it captures: Who/what interprets and runs the procedure
   - Possible values: LLM-only, human-only, code-runtime, hybrid (LLM+code), collaborative (LLM+human interleaved)
   - Why it matters: Determines what primitives are available (branching, memory, computation)

2. FORMALITY
   - What it captures: How rigidly specified is each step
   - Possible values: informal prose, semi-structured, templated, schema-validated, formally verified
   - Why it matters: Trade-off between flexibility and reliability

3. CONTROL FLOW MODEL
   - What it captures: How the procedure decides what to do next
   - Possible values: linear sequence, branching (decision tree), looping (state machine), event-driven, goal-driven (planner), free-form (LLM decides)
   - Why it matters: Some thinking tasks need iteration, others are strictly sequential

4. MODALITY
   - What it captures: The representational medium
   - Possible values: plain text, rich text/markdown, visual/diagrammatic, interactive UI, audio/conversational, code
   - Why it matters: Affects comprehensibility, editability, and what tools can process it

5. ADAPTIVITY
   - What it captures: Whether the procedure changes based on input/context
   - Possible values: static (same steps every time), parameterized (depth scaling), conditional (branches on input), fully adaptive (generates steps dynamically)
   - Why it matters: Current skills use parameterized depth scaling; could go much further

6. COMPOSABILITY
   - What it captures: How easily procedures combine with each other
   - Possible values: monolithic, invocable (current INVOKE pattern), pipeable (output of one feeds input of next), nestable (procedures within procedures), orchestrated (external controller)
   - Why it matters: The toolkit already has 563 skills — composition is the meta-problem
```

### Step 5: Independence Validation

```
INDEPENDENCE CHECK:
- EXECUTOR vs FORMALITY: Can vary independently. A code runtime can execute informal specs (LLM interprets then executes). An LLM can follow a formal schema. ✓
- FORMALITY vs CONTROL FLOW: Can vary independently. A linear sequence can be formal or informal. ✓
- MODALITY vs EXECUTOR: Can vary independently. Visual formats can be LLM-interpreted or code-interpreted. ✓
- ADAPTIVITY vs CONTROL FLOW: Partially correlated — adaptive procedures tend to need branching/looping. But static procedures can also branch. Keeping both. ✓
- COMPOSABILITY vs EXECUTOR: Independent. Monolithic or pipeable in any executor. ✓
```

### Step 6: Completeness Check

```
COMPLETENESS CHECK:
- Structured markdown: Executor=LLM, Formality=semi-structured, Control=branching, Modality=rich text, Adaptivity=parameterized, Composability=invocable ✓
- Python function: Executor=code-runtime, Formality=schema-validated, Control=branching+looping, Modality=code, Adaptivity=conditional, Composability=pipeable ✓
- JSON schema: Executor=hybrid, Formality=schema-validated, Control=N/A(declarative), Modality=text, Adaptivity=static, Composability=nestable ✓
- Flowchart: Executor=human/LLM, Formality=semi-structured, Control=branching, Modality=visual, Adaptivity=conditional, Composability=monolithic ✓
- CLI wizard: Executor=hybrid, Formality=templated, Control=branching, Modality=interactive, Adaptivity=conditional, Composability=pipeable ✓
- Natural language: Executor=LLM, Formality=informal, Control=free-form, Modality=text, Adaptivity=fully adaptive, Composability=monolithic ✓
- State machine: Executor=code-runtime, Formality=formally verified, Control=looping, Modality=code/visual, Adaptivity=conditional, Composability=nestable ✓

All examples covered. No missing dimensions detected.
```

### Step 7: Dimensions Output

```
DIMENSIONS DISCOVERED FOR: thinking procedure formats

| # | Dimension       | Values                                                        | Validation           |
|---|-----------------|---------------------------------------------------------------|----------------------|
| 1 | Executor        | LLM-only, human-only, code-runtime, hybrid, collaborative    | Covers all examples ✓|
| 2 | Formality       | informal, semi-structured, templated, schema-validated, formal| Independent ✓        |
| 3 | Control Flow    | linear, branching, looping, event-driven, goal-driven, free  | Meaningful variation ✓|
| 4 | Modality        | plain text, rich text, visual, interactive, code              | Independent ✓        |
| 5 | Adaptivity      | static, parameterized, conditional, fully adaptive            | Meaningful variation ✓|
| 6 | Composability   | monolithic, invocable, pipeable, nestable, orchestrated       | Independent ✓        |

TOTAL SPACE SIZE: 5 × 5 × 6 × 5 × 4 × 5 = 15,000 combinations
```

---

## Phase 2: Space Enumeration

**Granularity**: REPRESENTATIVE
**Strategy**: Dimension-by-dimension with representative items, organized by primary dimension (Modality + Executor), since these most concretely distinguish one format from another.

---

### Format 1: Pure Natural Language Narrative

**Dimensions**: Executor=LLM | Formality=informal | Control=free-form | Modality=plain text | Adaptivity=fully adaptive | Composability=monolithic

**What it looks like**: A paragraph or two of instructions written as you would explain to a smart colleague. No headers, no templates, no structure — just clear prose.

> "When someone brings you a claim, your job is to figure out whether it's true, false, or somewhere in between. Start by understanding what they actually mean — not what the words literally say, but what they're trying to assert. Then think about what would have to be true for this claim to hold. Check each of those conditions. If any fail, the claim is weakened. If all hold, it's strong. Tell them what you found."

**Strengths**:
- Lowest barrier to authoring — anyone can write one
- Most flexible — the LLM interprets intent, not structure
- Easy to read, easy to share, easy to modify
- Naturally handles ambiguity and edge cases (the LLM fills gaps)

**Weaknesses**:
- No guarantee of consistency across invocations — the LLM may interpret differently each time
- No mechanism for depth scaling, failure mode detection, or structured output
- Cannot be validated or tested — no schema to check against
- Composability is poor — hard to INVOKE from another procedure when boundaries are undefined

**When it wins**: For simple, well-understood tasks where the LLM's default behavior is already close to what you want. For quick one-offs. For teaching someone the spirit of an approach.

**Key insight**: The current structured markdown format exists precisely because pure narrative was insufficient for reliable, repeatable thinking procedures. But narrative might be the right "first draft" format — write the narrative, then formalize it.

---

### Format 2: Executable Code (Python / TypeScript)

**Dimensions**: Executor=code-runtime (or hybrid) | Formality=schema-validated | Control=branching+looping | Modality=code | Adaptivity=conditional | Composability=pipeable

**What it looks like**:

```python
def stress_test_claim(claim: str, depth: int = 2) -> Analysis:
    """ARAW: Assume Right / Assume Wrong search."""
    parsed = extract_core_assertion(claim)
    sub_claims = decompose(parsed)

    results = []
    for sub in sub_claims:
        ar = assume_right(sub, depth=depth)
        aw = assume_wrong(sub, depth=depth)
        results.append(Finding(sub, ar, aw, verdict=synthesize(ar, aw)))

    return Analysis(
        findings=results,
        synthesis=derive_synthesis(results),
        confidence=calculate_confidence(results)
    )
```

**Strengths**:
- Completely unambiguous — every step is explicit
- Testable — you can write unit tests for thinking procedures
- Composable via function calls, imports, and pipelines
- Version-controllable with meaningful diffs
- Can enforce constraints (type checking, required fields)
- Can integrate computation (statistics, search, API calls)

**Weaknesses**:
- Requires a runtime — cannot be "read and followed" by a human or bare LLM
- Rigidity: code encodes the *mechanism* but loses the *judgment*. "Evaluate whether this sub-claim holds" is easy to write in prose, hard to implement in code without just calling an LLM anyway
- The interesting part of thinking procedures is the *reasoning*, which ends up in string literals and docstrings — you're back to natural language for the hard parts
- High authoring barrier — requires programming skill

**When it wins**: When the procedure has significant mechanical/computational components (sorting, filtering, scoring, aggregation). When you need guaranteed structure in output. When the procedure will be called thousands of times and consistency matters more than nuance.

**Key insight**: Most thinking procedures are 80% judgment and 20% structure. Code is great for the 20% but doesn't help with the 80%. The hybrid approach — code for orchestration, LLM calls for reasoning — is likely the real sweet spot here.

---

### Format 3: JSON/YAML Schema (Declarative Specification)

**Dimensions**: Executor=hybrid | Formality=schema-validated | Control=declarative | Modality=text(structured) | Adaptivity=parameterized | Composability=nestable

**What it looks like**:

```yaml
skill:
  name: araw
  description: "Assume Right / Assume Wrong search"
  input:
    type: claim
    required: true

  parameters:
    depth: { type: integer, default: 2, min: 1, max: 16 }

  phases:
    - name: decompose
      instruction: "Extract core assertion and decompose into sub-claims"
      output_schema:
        sub_claims: { type: array, items: { type: string }, min_items: 2 }

    - name: assume_right
      foreach: sub_claims
      instruction: "What follows if {item} is true? Trace implications."
      depth_scaling: { multiplier: depth, base_items: 3 }

    - name: assume_wrong
      foreach: sub_claims
      instruction: "What breaks if {item} is false? Find consequences."
      depth_scaling: { multiplier: depth, base_items: 3 }

    - name: synthesize
      instruction: "Derive verdict from findings only. No external reasoning."
      output_schema:
        verdict: { enum: [validated, refuted, conditional, uncertain] }
        confidence: { type: number, min: 0, max: 1 }

  failure_modes:
    - name: confirmation_bias
      detection: "AR branches outnumber AW branches 3:1"
      correction: "Force equal depth on both branches"
```

**Strengths**:
- Separates *structure* from *content* — the schema defines what must happen, the LLM provides the reasoning
- Machine-parseable — tools can validate, lint, and transform skills
- Enables a skill editor/IDE — auto-complete, validation, visualization
- Parameters are explicit and typed — depth scaling becomes a first-class concept
- Failure modes become checkable assertions rather than prose warnings

**Weaknesses**:
- Verbose — the YAML above encodes less insight than the current markdown
- Loses the narrative thread — reading a schema doesn't teach you *why* the procedure works
- Harder to author — requires understanding the schema language
- Risk of over-specification — you end up constraining the LLM in ways that reduce output quality

**When it wins**: When you want to build tooling on top of skills (validators, editors, visualizers, auto-composers). When you need machine-readable skill metadata. When consistency across hundreds of skills matters.

**Key insight**: Schema is probably not a replacement for the current format but a complement. The markdown stays as the human-readable/LLM-executable version; a schema is generated alongside it for tooling purposes.

---

### Format 4: Decision Tree / Flowchart

**Dimensions**: Executor=LLM or human | Formality=semi-structured | Control=branching | Modality=visual | Adaptivity=conditional | Composability=monolithic

**What it looks like**: A directed graph where nodes are questions or actions and edges are conditions.

```
[Receive claim]
    │
    ▼
[Is it actually a claim?]──No──→ [Reroute to /decide, /how, /want]
    │
   Yes
    ▼
[Extract core assertion]
    │
    ▼
[Decompose into sub-claims]
    │
    ▼
[For each sub-claim]──────────────────────┐
    │                                      │
    ▼                                      ▼
[Assume Right]                    [Assume Wrong]
[Trace implications]              [Find what breaks]
    │                                      │
    ▼                                      ▼
[Depth sufficient?]──No──→[Go deeper]  [Depth sufficient?]──No──→[Go deeper]
    │                                      │
   Yes                                    Yes
    │                                      │
    └──────────────┬───────────────────────┘
                   ▼
           [Synthesize findings]
                   │
                   ▼
           [Assign verdict]
```

**Strengths**:
- Makes the control flow visually obvious — you can see the shape of the procedure at a glance
- Great for routing/triage skills (like /search, /claim, /decide) where branching IS the skill
- Natural representation for decision-making procedures
- Humans can follow these without LLM assistance
- Easy to spot dead ends, missing branches, infinite loops

**Weaknesses**:
- Cannot encode nuance — "evaluate whether this holds" requires a text annotation that defeats the purpose of the visual
- Scales poorly — complex procedures become spaghetti
- Hard to version control (binary image or complex text-based graph notation)
- No good way to encode depth scaling, failure modes, or quality checks
- Not directly LLM-executable — must be converted to text

**When it wins**: For routing/orchestration skills where the main value is "which path do I take?" For onboarding users who want to understand the toolkit's structure. For debugging skill logic.

**Key insight**: Flowcharts are best as a *secondary representation* — auto-generated from the primary format to aid understanding, not authored directly.

---

### Format 5: State Machine (Formal)

**Dimensions**: Executor=code-runtime | Formality=formally verified | Control=looping+event-driven | Modality=code | Adaptivity=conditional | Composability=nestable

**What it looks like**:

```
States: {intake, decompose, ar_search, aw_search, deepen, synthesize, output}
Initial: intake
Terminal: output

Transitions:
  intake      → decompose     [always]
  decompose   → ar_search     [sub_claims extracted]
  ar_search   → aw_search     [ar complete for current sub-claim]
  aw_search   → deepen        [depth < target AND findings sparse]
  aw_search   → ar_search     [more sub-claims remaining]
  aw_search   → synthesize    [all sub-claims processed AND depth sufficient]
  deepen      → ar_search     [re-enter with increased depth]
  synthesize  → output        [always]

Guards:
  depth < target: current_depth < depth_parameter
  findings sparse: count(findings) < 3 * depth_parameter
```

**Strengths**:
- Mathematically precise — can be formally verified (no deadlocks, all states reachable)
- Handles iteration and recursion explicitly — current skills have implicit "recurse until bedrock" that a state machine makes rigorous
- Can be simulated and tested without an LLM
- Natural fit for skills that have "loops" (iterate until convergence, deepen until sufficient)

**Weaknesses**:
- Extremely high authoring cost — formalizing 563 skills as state machines would take months
- Loses all the reasoning content — states are labels, not instructions
- Overkill for linear procedures (most skills are mostly sequential)
- Requires tooling to be useful — raw state machine notation is not human-friendly

**When it wins**: For complex meta-skills that orchestrate other skills (like /certainty, /iterate). For procedures where getting the control flow wrong has high cost. For building a formal model of how the toolkit's routing works.

**Key insight**: State machines solve a real problem — the current skills have implicit, under-specified control flow. "Recurse until bedrock" is a state machine in disguise. But formalizing every skill is overkill; formalize only the orchestration layer.

---

### Format 6: Interactive Wizard / Dialogue Script

**Dimensions**: Executor=collaborative | Formality=templated | Control=branching | Modality=interactive | Adaptivity=conditional | Composability=invocable

**What it looks like**:

```
WIZARD: stress_test_claim

STEP 1: GATHER
  ASK: "What's the claim you want to test?"
  STORE: $claim

  ASK: "How rigorous do you want this? (quick / standard / thorough)"
  STORE: $depth
  MAP: { quick: 1, standard: 2, thorough: 4 }

STEP 2: CONFIRM
  SHOW: "I'll test: '$claim' at depth $depth"
  SHOW: "Sub-claims I've identified:"
  COMPUTE: decompose($claim) → $sub_claims
  LIST: $sub_claims
  ASK: "Are these the right sub-claims? Add/remove any?"
  UPDATE: $sub_claims

STEP 3: ANALYZE (for each $sub in $sub_claims)
  SHOW: "Testing sub-claim: $sub"

  COMPUTE: assume_right($sub, $depth) → $ar
  SHOW: "If true: $ar"
  ASK: "Anything I'm missing on the 'assume right' side?"

  COMPUTE: assume_wrong($sub, $depth) → $aw
  SHOW: "If false: $aw"
  ASK: "Anything I'm missing on the 'assume wrong' side?"

STEP 4: SYNTHESIZE
  COMPUTE: synthesize($findings) → $verdict
  SHOW: "Verdict: $verdict"
  ASK: "Does this match your intuition? If not, what feels off?"
```

**Strengths**:
- Keeps the human in the loop at every step — catches errors early
- Naturally adaptive — human feedback steers the analysis
- Lower cognitive load — user deals with one step at a time instead of reading a wall of output
- Builds understanding — the user learns the procedure by participating in it
- Can gather critical context that the LLM would otherwise have to guess

**Weaknesses**:
- Slow — every step requires a round-trip with the user
- Annoying for experts who don't need hand-holding
- Difficult to compose — chaining wizards creates an interrogation
- The current skill format already implies a conversation; making it explicitly interactive adds overhead without proportional benefit
- Requires UI infrastructure beyond what a chat interface naturally provides

**When it wins**: For high-stakes decisions where user input at each step genuinely changes the outcome. For teaching/onboarding users on how to think through a problem. For skills where the user has critical domain knowledge the LLM lacks.

**Key insight**: The current format is already implicitly interactive — the LLM reads the skill and conducts a kind of internal wizard. Making the wizard explicit and user-facing is valuable for specific use cases (high-stakes, teaching, domain-expertise-dependent) but would be annoying as the default.

---

### Format 7: Prompt Chain / Pipeline

**Dimensions**: Executor=LLM | Formality=templated | Control=linear(pipelined) | Modality=text | Adaptivity=parameterized | Composability=pipeable

**What it looks like**: A sequence of prompt templates where each one's output feeds into the next.

```
CHAIN: stress_test_claim

PROMPT 1 (decompose):
  "Given the claim: {{input}}
   Extract the core assertion. Then list all sub-claims that must be true
   for the core assertion to hold. Output as JSON array."
  → $sub_claims

PROMPT 2 (assume_right, foreach $sub_claims):
  "Sub-claim: {{sub_claim}}
   Assume this is TRUE. What follows? What are the implications?
   List at least {{depth * 3}} findings."
  → $ar_findings

PROMPT 3 (assume_wrong, foreach $sub_claims):
  "Sub-claim: {{sub_claim}}
   Assume this is FALSE. What breaks? What are the consequences?
   List at least {{depth * 3}} findings."
  → $aw_findings

PROMPT 4 (synthesize):
  "Given these AR findings: {{ar_findings}}
   And these AW findings: {{aw_findings}}
   Synthesize a verdict. Use ONLY the findings above.
   Do not introduce new reasoning."
  → $verdict
```

**Strengths**:
- Directly maps to how LLM-based systems actually work under the hood
- Each prompt can be independently tested, tuned, and optimized
- Natural composability — chains can include sub-chains
- Explicit data flow — you can see exactly what information passes between steps
- Could be executed by any LLM orchestration framework (LangChain, DSPy, etc.)

**Weaknesses**:
- Fragments the reasoning — the LLM loses context between prompts unless you explicitly pass it
- Optimizing individual prompts can hurt global coherence
- Overly mechanical — reduces rich thinking to template filling
- The current single-prompt approach (read SKILL.md, execute in one shot) has the advantage of maintaining full context throughout

**When it wins**: When you need to optimize specific steps independently. When you're building automated pipelines that run without human oversight. When you want to mix LLM reasoning with computational steps (call an API between prompts).

**Key insight**: The current format is essentially a single-prompt instruction set. Splitting into a chain trades context for modularity. This might be the right move for production systems but loses something for interactive use.

---

### Format 8: Constraint / Goal Specification (Declarative)

**Dimensions**: Executor=LLM (with planner) | Formality=semi-structured | Control=goal-driven | Modality=text | Adaptivity=fully adaptive | Composability=orchestrated

**What it looks like**: Instead of specifying *how* to think, specify *what* the output must satisfy.

```
GOAL: Evaluate whether $claim is true, false, or conditional.

CONSTRAINTS:
- Must consider at least $depth * 3 sub-claims
- Must explore both "assume true" and "assume false" for each sub-claim
- AR and AW analysis must reach equal depth (±1 level)
- Synthesis must reference ONLY findings from analysis (no new reasoning)
- Confidence score must be calibrated (if you say 80%, you should be right 80% of the time)
- Must flag any sub-claims where evidence is unavailable

QUALITY CRITERIA:
- No confirmation bias: AR findings should not outnumber AW findings by more than 2:1
- No shallow dismissal: every AW branch must contain genuine counter-evidence
- Steelman before attack: strongest version of claim must be tested, not weakest

OUTPUT MUST INCLUDE:
- Numbered findings registry
- Verdict per sub-claim
- Overall synthesis
- Confidence level
- Identified gaps
```

**Strengths**:
- Specifies *what good looks like* without constraining *how to get there*
- The LLM can choose its own path to satisfy the constraints — potentially finding better approaches than the procedure author anticipated
- Quality criteria are testable — you could automatically check outputs against constraints
- Naturally handles the "spirit vs letter" problem — intent is encoded directly
- Trivially composable — just merge constraint sets

**Weaknesses**:
- Requires a highly capable LLM — weaker models need step-by-step guidance
- No pedagogical value — doesn't teach the user *how* to think, just what the output should look like
- Hard to debug — when output is bad, you don't know which step went wrong
- Risk of constraint gaming — the LLM satisfies the letter of the constraints while violating their spirit

**When it wins**: When working with frontier-class models that don't need hand-holding. When the procedure author cares about outcomes, not process. When you want skills that improve automatically as LLMs get better (the LLM finds better paths to satisfy the same constraints).

**Key insight**: This is arguably the most forward-looking format. As LLMs improve, detailed step-by-step procedures become less valuable (the LLM already knows how to do it) while quality constraints become more valuable (the LLM needs to know what "good enough" means). The current format is optimal for 2024-2026 models; constraint specs might be optimal for 2027+ models.

---

### Format 9: Worked Example Bank

**Dimensions**: Executor=LLM | Formality=informal | Control=free-form(pattern-matching) | Modality=rich text | Adaptivity=fully adaptive | Composability=monolithic

**What it looks like**: Instead of a procedure, provide 3-5 fully worked examples at different difficulty levels and let the LLM pattern-match.

```
SKILL: stress_test_claim
METHOD: Follow the pattern shown in these examples.

EXAMPLE 1 (simple claim):
Input: "Remote work increases productivity"
[Full 2-page worked analysis showing decomposition, AR, AW, synthesis, verdict]

EXAMPLE 2 (complex claim with conditional verdict):
Input: "Cryptocurrency will replace fiat currency within 20 years"
[Full 3-page worked analysis]

EXAMPLE 3 (claim that seems true but is actually conditional):
Input: "Exercise is good for you"
[Full analysis showing how an obvious-seeming claim has nuance]
```

**Strengths**:
- Leverages LLMs' strongest capability: in-context learning from examples
- Communicates nuance that procedures cannot — the *tone*, the *judgment calls*, the *level of depth*
- Self-documenting — the examples ARE the documentation
- Handles edge cases naturally — if you include a tricky example, the LLM learns to handle similar cases

**Weaknesses**:
- Extremely token-expensive — 3 worked examples might be 5,000+ tokens vs 1,000 for a procedure
- Hard to maintain — updating the approach means re-writing all examples
- Implicit logic — if the user asks "why did it do X?", you can only point to examples, not rules
- Quality ceiling = quality of examples. Garbage examples produce garbage output.

**When it wins**: For tasks where the procedure is hard to articulate but easy to demonstrate (style, tone, judgment). For tasks where edge cases are more important than the common case. For onboarding LLMs that struggle with procedural instructions.

**Key insight**: Few-shot examples are the original "skill format" for LLMs. The current structured markdown is arguably a response to the limitations of pure few-shot prompting. But a hybrid — procedure plus 1-2 worked examples — might be better than either alone.

---

### Format 10: Socratic Dialogue Template

**Dimensions**: Executor=LLM | Formality=semi-structured | Control=branching(question-driven) | Modality=text(dialogue) | Adaptivity=conditional | Composability=invocable

**What it looks like**: The skill is written as a series of questions the LLM asks itself (or the user).

```
SKILL: stress_test_claim
MODE: Self-Socratic

Q1: What is the actual claim being made? (Not the words — the assertion.)
Q2: What would the world look like if this claim were true?
Q3: What would the world look like if it were false?
Q4: Which world matches observed reality better?
Q5: What evidence would change your answer to Q4?
Q6: Is there a version of the claim that's more precisely true? What conditions make it true?
Q7: What's the strongest argument AGAINST the claim? Can you refute it?
Q8: What's your confidence level, and what's it based on?

BRANCHING:
- If Q4 answer is "true world matches": Focus on Q7 (attack the strong position)
- If Q4 answer is "false world matches": Focus on Q6 (find the conditional version)
- If Q4 answer is "unclear": Focus on Q5 (identify missing evidence)
```

**Strengths**:
- Natural match for LLM reasoning — LLMs are trained on dialogue and respond well to questions
- Captures the *direction of inquiry*, not just the steps
- Easy to extend — add a question to cover a new case
- Pedagogically powerful — teaches users to ask the right questions

**Weaknesses**:
- No mechanism for structured output — answers to questions are unstructured
- Depth control is implicit (more questions = more depth)
- Quality depends heavily on question design — a bad question produces a bad analysis branch
- Harder to validate — did the LLM actually answer each question thoroughly?

**When it wins**: For exploratory/analytical skills where the key challenge is asking the right questions. For teaching users to think through problems themselves. For tasks where rigid structure would be premature.

**Key insight**: Questions are underused in the current skill format. Many skills would benefit from an explicit "questions to ask" section even within the existing markdown format.

---

### Format 11: Hybrid — Annotated Code with LLM Escape Hatches

**Dimensions**: Executor=hybrid | Formality=mixed | Control=branching+free-form | Modality=code+text | Adaptivity=conditional | Composability=pipeable

**What it looks like**: Code that delegates the hard parts to LLM reasoning.

```python
@skill("stress_test_claim")
def araw(claim: str, depth: int = 2) -> Analysis:
    # STRUCTURED: Extract and decompose (mechanical)
    core = llm("Extract the single core assertion from: {claim}")
    subs = llm("Decompose into sub-claims: {core}",
               output_schema=List[str], min_items=2)

    findings = []
    for sub in subs:
        # LLM-DRIVEN: The actual reasoning (requires judgment)
        ar = llm("""
            Assume '{sub}' is TRUE.
            Trace implications — what follows? What does this enable or require?
            Go {depth} levels deep. Be specific, not generic.
        """)
        aw = llm("""
            Assume '{sub}' is FALSE.
            What breaks? What alternatives exist? What was the claim resting on?
            Go {depth} levels deep. Be adversarial, not gentle.
        """)

        # QUALITY CHECK: Automated bias detection
        if len(ar.findings) > 3 * len(aw.findings):
            aw = llm("Your AW analysis was shallow. Go harder: {sub}", depth=depth+1)

        findings.append(Finding(sub, ar, aw))

    # CONSTRAINED: Synthesis from findings only
    verdict = llm(
        "Synthesize verdict from ONLY these findings: {findings}. "
        "Do not introduce new reasoning.",
        output_schema=Verdict
    )

    return Analysis(findings=findings, verdict=verdict)
```

**Strengths**:
- Best of both worlds: code handles structure, LLM handles reasoning
- Automated quality checks (bias detection, depth enforcement) actually execute instead of being aspirational prose
- Clear separation between mechanical and judgment-requiring steps
- Testable, composable, and version-controllable
- Could run in a real orchestration framework

**Weaknesses**:
- High authoring complexity — requires both programming and prompt engineering skill
- Depends on a specific runtime/framework (not portable like markdown)
- The LLM calls still contain natural language prompts — you've added a layer of indirection without removing the core authoring challenge
- Debugging is harder — is the bug in the code logic or the prompt wording?

**When it wins**: For production deployment of skills that need reliability guarantees. For skills with measurable quality criteria. When you're building a product, not a personal tool.

**Key insight**: This is probably where the toolkit goes if it becomes a product. The current markdown format is the "source of truth" for the reasoning, and this hybrid format is the "compiled" version for production execution.

---

## Cross-Dimensional Observations

### What the Current Format Gets Right

The structured markdown format occupies a genuinely good position in the space:
- **Executor=LLM** means zero infrastructure required
- **Formality=semi-structured** balances readability with consistency
- **Control=branching** handles most real procedure shapes
- **Modality=rich text** is universally readable and editable
- **Adaptivity=parameterized** (depth scaling) provides flexibility without complexity
- **Composability=invocable** (the INVOKE pattern) enables skill chaining

This is not an accident. This format evolved through use.

### Gaps in the Current Format

| Gap | What's missing | Format that addresses it |
|-----|---------------|------------------------|
| Machine-readability | Skills can't be validated, linted, or analyzed by tools | JSON/YAML schema |
| Automated quality checks | Failure mode detection is prose, not executable | Hybrid code, Constraints |
| Visual overview | Hard to see the shape of a 500-line procedure | Flowchart |
| Context-dependent branching | "If the user says X, do Y" is awkward in prose | Decision tree, Wizard |
| Graceful degradation | No mechanism for simpler models to execute a "light" version | Tiered constraint spec |
| Empirical optimization | Can't A/B test which phrasing works better | Prompt chain |
| Worked examples | LLMs learn well from examples but skills don't include them | Example bank |

### The Most Promising Hybrid Directions

1. **Markdown + Constraint Addendum**: Keep the current format but add a machine-readable quality constraint section that can be automatically checked. Essentially: "here's how to do it" (markdown) + "here's how to tell if you did it right" (constraints).

2. **Markdown + 1-2 Worked Examples**: The current procedure plus one or two complete worked examples at the end. Significantly improves output quality for LLMs that benefit from in-context learning, at the cost of token budget.

3. **Markdown with Auto-Generated Schema Shadow**: Keep authoring in markdown but auto-extract a JSON schema from the structure (phases, steps, parameters, output requirements). Enables tooling without changing the authoring experience.

4. **Socratic Questions as a First-Class Section**: Add an explicit "Key Questions" section to every skill — the 5-8 questions that drive the analysis. This is cheap to add and likely improves output quality.

---

## Coverage Assessment

**Well-covered**: Text-based formats, code-based formats, declarative specifications, visual formats, interactive formats.

**Potentially missing**:
- **Audio/conversational formats** — skills designed for voice interfaces (would require very different structure)
- **Collaborative/multi-agent formats** — skills where multiple LLM agents play different roles (adversary, advocate, judge)
- **Temporal/evolving formats** — skills that change over time based on accumulated usage data
- **Domain-specific language (DSL)** — a custom language designed specifically for thinking procedures (not general-purpose code, not markdown, something purpose-built)
- **Graph/network formats** — non-linear skill structures where steps can be traversed in multiple orders based on what's discovered

---

## Recommended Next Steps

1. **Lowest effort, highest value**: Add a "Key Questions" section and one worked example to 5 existing skills as an experiment. Measure whether output quality improves.
2. **Medium effort**: Design a constraint/quality-check schema that can be appended to existing markdown skills, enabling automated validation.
3. **Longer term**: Build a schema shadow system that auto-extracts structure from markdown skills, enabling tooling (skill editor, validator, dependency visualizer) without changing the authoring format.
4. **Research direction**: Experiment with pure constraint-based skills for 3-5 procedures and compare output quality against the procedural versions, especially on frontier models.

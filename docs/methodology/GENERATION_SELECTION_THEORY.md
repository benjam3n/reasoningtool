# Generation-Selection Theory
## How Structure Reduces Intelligence Requirements

### The AI Benchmark Analogy

AI benchmarks ARE criteria systems:
- Define what "good" means (the benchmark)
- Models search for answers
- Evaluate against benchmark

**Key insight**: If benchmarks were more structured and did more work, models would "solve" them much easier because:
- Less guessing needed
- Harder to get wrong
- Clear what's being asked

This is exactly what GOSM should do - be a "well-structured benchmark" for reasoning.

---

### The Intelligence-Structure Tradeoff

```
With WEAK structure:
- Generation quality matters a lot (need intelligence to generate good options)
- Selection quality matters a lot (need intelligence to pick the right one)
- Easy to get wrong

With STRONG structure:
- Generation quality matters LESS (structure guides what to generate)
- Selection becomes EASY (criteria are clear, just match)
- Hard to get wrong
```

**The goal**: Push as much as possible from "needs intelligence" to "needs structure."

---

### Refining "Don't Generate Obviously Bad"

The original phrasing was wrong because:
- You can't know something is "obviously bad" without evaluation
- That's circular - you'd need the intelligence you're trying to avoid

**Better framing: Hierarchical Filtering / Dealbreaker-First Evaluation**

Instead of "don't generate obviously bad," the actual pattern is:

1. **Identify dealbreaker criteria** - aspects that trump all others
2. **Filter on dealbreakers FIRST** - before considering full plan
3. **Only fully evaluate what passes dealbreakers**

This is NOT about knowing something is bad before evaluation.
It's about **ordering the evaluation efficiently**:
- Check the most important/disqualifying criteria first
- If it fails a dealbreaker, stop evaluating (save effort)
- Only do full evaluation on candidates that pass dealbreakers

**Example:**
```
Generating business plans:

Dealbreaker criteria (check first):
- Is it legal? (If no, stop - don't evaluate further)
- Do we have any path to the required resources? (If no, stop)
- Is there a plausible customer? (If no, stop)

Full criteria (only for what passes):
- Expected return
- Risk level
- Timeline
- Competitive advantage
- etc.
```

The efficiency comes from NOT evaluating "expected return" on something that's illegal.

---

### Why This Works for LLMs

LLMs are good at:
- Pattern matching
- Following instructions
- Checking if X matches Y
- Arithmetic/aggregation

LLMs are worse at:
- Open-ended generation without guidance
- Judging quality without criteria
- Knowing what matters without being told
- Implicit knowledge/context

**Strong structure plays to LLM strengths:**

| Task | Without Structure | With Structure |
|------|------------------|----------------|
| Generate options | "Think of good plans" (hard) | "Fill in each slot of this template" (easy) |
| Evaluate quality | "Is this good?" (hard) | "Does this match criterion X? Score 1-10" (easy) |
| Select best | "Pick the best" (hard) | "Which has highest score?" (easy) |
| Avoid bad | "Don't generate bad ones" (impossible) | "Check dealbreakers first, stop if fail" (easy) |

---

### The Quality Curves

```
                    Intelligence Required
                           ↑
                           │
     Weak structure →      │  ████████████████
                           │  ████████████████
                           │  ████████████████
                           │
   Medium structure →      │  █████████
                           │  █████████
                           │
   Strong structure →      │  ████
                           │
                           └────────────────────→
                               Task Difficulty
```

As structure increases:
- More tasks become "easy" (require less intelligence)
- The bar for "sufficient intelligence" drops
- Cheaper models can handle more tasks

---

### Hierarchical Criteria Design

**Level 1: Dealbreakers (Binary)**
- Check first
- If fail, discard immediately
- No scoring, just pass/fail
- Examples: legal, physically possible, within hard constraints

**Level 2: Must-Haves (Threshold)**
- Check second
- Must meet minimum threshold
- Score, but only pass if >= threshold
- Examples: minimum ROI, minimum quality level

**Level 3: Should-Haves (Weighted)**
- Check for candidates that pass Levels 1-2
- Score and weight
- Used for ranking
- Examples: efficiency, elegance, speed

**Level 4: Nice-to-Haves (Tiebreaker)**
- Only matter when Level 3 is tied
- Fine-grained preferences
- Examples: aesthetic preference, minor conveniences

**Evaluation flow:**
```
All candidates
    │
    ▼
[Level 1: Dealbreakers] ──fail──→ Discard
    │ pass
    ▼
[Level 2: Must-Haves] ──fail──→ Discard
    │ pass
    ▼
[Level 3: Should-Haves] ──score──→ Rank
    │ ties
    ▼
[Level 4: Nice-to-Haves] ──resolve──→ Final rank
```

This is the efficient version of "don't generate obviously bad":
- Not about pre-knowing badness
- About ordering evaluation to discard early
- About focusing full evaluation on viable candidates only

---

### Implications for GOSM

1. **Every procedure should have hierarchical criteria**
   - Level 1 dealbreakers clearly marked
   - Evaluation order specified
   - Early termination points explicit

2. **Generation should be guided, not filtered**
   - Don't say "generate good options"
   - Say "fill in these slots, where each slot has these valid values"
   - Filtering happens at evaluation, not generation

3. **Selection should be mechanical**
   - Clear scoring rubric
   - Explicit weights
   - Arithmetic aggregation
   - No "judgment calls" left for the model

4. **The criteria document IS the intelligence**
   - Invest heavily in criteria design
   - Criteria are reusable across many tasks
   - Better criteria = less intelligence needed everywhere

---

### Benchmark Design Principles

If GOSM is a "well-structured benchmark for reasoning," it should:

1. **Be explicit about what's being asked**
   - No ambiguity in the task
   - Clear success criteria
   - Defined output format

2. **Provide all necessary context**
   - Don't require implicit knowledge
   - Include relevant constraints
   - Specify domain vocabulary

3. **Decompose complex judgments**
   - Break "is this good?" into specific criteria
   - Make each criterion independently checkable
   - Aggregate mechanically

4. **Order evaluation efficiently**
   - Dealbreakers first
   - Full scoring only for viable candidates
   - Early termination for obvious failures

5. **Make matching easy**
   - Clear criteria definitions
   - Concrete examples of pass/fail
   - Unambiguous thresholds

---

### Summary

The original "don't generate obviously bad" was wrong because it assumed pre-evaluation knowledge.

The correct framing:
1. **Guided generation** - Structure tells you what to generate (not what to avoid)
2. **Hierarchical evaluation** - Check dealbreakers first, full scoring only for viable
3. **Mechanical selection** - Arithmetic on scores, no judgment

This is how you get LLM performance that's "hard to get wrong":
- Structure does the hard work
- LLM does pattern matching
- Intelligence is externalized into criteria

**The better the structure, the less the intelligence matters.**

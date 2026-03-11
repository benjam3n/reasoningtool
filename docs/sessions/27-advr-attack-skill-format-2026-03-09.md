# /advr "The skill format (structured markdown procedures) is the best format for encoding thinking procedures." Attack this claim.
**Date:** 2026-03-09
**Skill:** /advr (Adversarial Review)

---

## Step 1: Builder — Construct the Claim

```
BUILDER'S CASE:
Claim: Structured markdown procedures (phases, numbered steps, templates,
       failure modes, depth scaling) are the best format for encoding
       thinking procedures that an LLM executes.

Evidence:
1. 563 skills exist in this format and function — strength: H
2. Skills can chain into each other via → INVOKE — strength: M
3. The format is human-readable AND machine-readable — strength: H
4. Templates (code blocks with fill-in fields) constrain output structure — strength: M
5. Anti-failure checks catch known degenerate outputs — strength: M
6. Depth scaling tables let the same skill operate at multiple levels of rigor — strength: M
7. The format requires no tooling beyond a text editor — strength: H

Reasoning: The format works across hundreds of diverse thinking tasks,
is easy to author and modify, chains composably, and produces structured
output. Its pragmatic success at scale is evidence of fitness.

Confidence: 72%

Stakes: If this claim is wrong, the entire toolkit might be encoding
procedures in a suboptimal way — effort spent on 563 skills could be
partially misdirected, and a format migration could unlock significantly
better performance.
```

---

## Step 2: Breaker — Attack the Claim

### Attack the Evidence

**A1. Is the evidence real?**
The 563 skills exist, but "function" is self-reported. There is no systematic evaluation of skill output quality. The skills have never been benchmarked against the same procedures encoded in alternative formats. Existence is not evidence of optimality — it is evidence of feasibility.

**A2. Is the evidence relevant?**
Evidence item 1 (563 skills exist) proves the format is *viable*, not that it is *best*. You could encode 563 skills as Python functions, YAML configs, JSON schemas, or few-shot examples and they would also "exist." The quantity is irrelevant to the comparative claim.

**A3. Is the evidence sufficient?**
No comparative evidence was presented. "Best" is a superlative that requires comparison with alternatives. The Builder presented zero data points from alternative formats. This is like saying "English is the best language for poetry" because many poems exist in English.

**A4. Is the evidence cherry-picked?**
Yes. The Builder did not mention:
- Skills where the format causes problems (verbose boilerplate, LLM ignoring sections, template fields that go unfilled)
- Cases where the structured format adds friction without adding value (simple skills that could be a single paragraph)
- The fact that the LLM was not consulted about what format it processes most reliably

**A5. Is the evidence current?**
LLM capabilities change rapidly. What works well for one model generation may not be optimal for the next. The format was designed for a specific LLM behavior profile that may already be outdated.

### Attack the Reasoning

**A6. Does the conclusion follow from the premises?**
No. "Works across many tasks" → "is the best format" is a non sequitur. Many formats could work across many tasks. The conclusion requires a comparative claim but the premises contain no comparison.

**A7. Are there hidden assumptions?**
Several:
- That the LLM processes all sections of a structured markdown file with equal attention (it may not — attention patterns in long contexts are uneven)
- That human readability matters (if the consumer is an LLM, human readability is a nice-to-have, not a requirement)
- That explicit structure helps the LLM more than implicit structure (few-shot examples encode structure implicitly and may be more natural for a next-token predictor)
- That one format should serve both authoring and execution (these could be separate formats compiled from one to the other)
- That "structured markdown" is a single format rather than a family of formats with widely varying quality

**A8. Is correlation being mistaken for causation?**
The skills produce good output. But is it *because of* the format, or *despite* it? The quality might come from the *content* of the procedures (the actual thinking steps) rather than the *format* they are encoded in. You could put the same intellectual content into a different format and get equivalent or better results.

**A9. Is the reasoning reversible?**
Yes. "The format works, therefore it is best" could equally support "The format works, therefore it is good enough" — which is a much weaker and more defensible claim. The same reasoning pattern could be used to argue any working format is "best."

### Attack the Claim Itself

**A10. Is it falsifiable?**
Barely. "Best" is vague without specifying best *for whom*, *at what*, *under what constraints*, and *compared to what*. The claim as stated is almost unfalsifiable because "best" can always be reinterpreted.

**A11. Is it specific enough to test?**
No. To test it, you would need:
- A fixed set of thinking procedures
- Multiple encoding formats
- A scoring rubric for output quality
- Statistical comparison across many runs
None of this has been done.

**A12. Does it contradict known facts?**
Partially. Known facts about LLMs:
- They process tokens, not "structure." Markdown headers are just token sequences.
- Few-shot prompting often outperforms instruction-following for complex tasks.
- Long structured prompts suffer from "lost in the middle" effects where middle sections get less attention.
- Programmatic formats (code) can enforce constraints that markdown cannot (e.g., a Python function *must* return a value; a markdown template *suggests* filling in a field but cannot enforce it).

**A13. Is there a simpler explanation?**
Yes: Structured markdown is the *most convenient* format for a human author who thinks in outlines. It is author-optimal, not executor-optimal. The LLM performs well because the underlying thinking procedures are good, and it would perform similarly or better with those procedures encoded differently.

**A14. What would a knowledgeable opponent say?**
A prompt engineering researcher would say: "You have 563 skills and zero ablation studies. You don't know which parts of the format matter, which are ignored, and which actively hurt. You are optimizing for authoring convenience and assuming execution quality follows. The format is untested in the only way that matters — comparatively."

A programming language designer would say: "Markdown has no type system, no enforcement, no composition semantics. Your → INVOKE is a string convention, not a function call. Your templates are hopes, not contracts. A real procedure language would give you guarantees your format cannot."

**A15. The uncomfortable attack: The format may actively harm some skills.**
Long structured skill files (like ARAW at 424 lines) may cause the LLM to:
- Lose track of which phase it is in
- Over-weight sections near the beginning and end (primacy/recency bias)
- Treat the template as the output rather than using it as a guide (template-copying failure mode)
- Spend tokens re-reading structure instead of doing the thinking
- Feel "constrained" into filling boxes rather than following genuine analytical threads

The structured format may produce *worse* output than a shorter, less structured version for complex skills — trading depth of thought for completeness of form.

---

## Step 3: Score Each Attack

| # | Attack | Target | Severity | Claim Survives? |
|---|--------|--------|----------|----------------|
| A1 | No quality evaluation — existence ≠ optimality | Evidence | Serious | Weakened |
| A2 | Quantity irrelevant to comparative claim | Evidence | Serious | Weakened |
| A3 | Zero comparative data for a superlative claim | Evidence | Fatal | N |
| A4 | Cherry-picked — omits failure cases and LLM perspective | Evidence | Serious | Weakened |
| A5 | Format designed for a specific model generation | Evidence | Minor | Y |
| A6 | "Works" does not entail "best" | Reasoning | Fatal | N |
| A7 | Hidden assumptions about LLM attention and human readability | Reasoning | Serious | Weakened |
| A8 | Quality may come from content, not format | Reasoning | Serious | Weakened |
| A9 | Same reasoning supports "good enough" equally well | Reasoning | Serious | Weakened |
| A10 | "Best" is vague — nearly unfalsifiable | Claim | Serious | Weakened |
| A11 | No test methodology exists or has been applied | Claim | Serious | Weakened |
| A12 | Contradicts known LLM behavior (lost-in-middle, token-level processing) | Claim | Serious | Weakened |
| A13 | Simpler explanation: author-optimal, not executor-optimal | Claim | Fatal | N |
| A14 | No ablation studies, no comparative evidence | Claim | Fatal | N |
| A15 | Long structured files may actively degrade LLM performance | Claim | Serious | Weakened |

**Fatal attacks: 4 (A3, A6, A13, A14)**
**Serious attacks: 9**
**Minor attacks: 1**

---

## Step 4: Builder — Respond to Attacks

```
BUILDER'S RESPONSE:
Attack: A3 (Zero comparative data)
Response type: Concede
Content: This is correct. No comparative evaluation has been done. The
Builder cannot defend "best" without comparison data.
Revised confidence: 72% → 40%
```

```
BUILDER'S RESPONSE:
Attack: A6 ("Works" ≠ "best")
Response type: Repair
Content: The claim should be narrowed from "best" to "a strong practical
format." The Builder can defend that the format is effective, widely
applicable, and has desirable properties (human-readable, no tooling
required, composable). The Builder cannot defend the superlative.
Revised confidence: 40% → 35%
```

```
BUILDER'S RESPONSE:
Attack: A13 (Author-optimal, not executor-optimal)
Response type: Repair
Content: The Builder can argue that author-optimality matters because the
bottleneck is skill creation, not skill execution. However, this concedes
that the format is not executor-optimal, which means "best" cannot be
defended. The Builder repairs to: "best format for a human author to
create thinking procedures that an LLM can execute adequately."
Revised confidence: 35% (claim has been significantly narrowed)
```

```
BUILDER'S RESPONSE:
Attack: A14 (No ablation studies)
Response type: Concede
Content: This is entirely correct. We do not know which elements of the
format (headers, templates, failure mode tables, depth scaling) actually
contribute to output quality. Some may be cargo cult structure.
Revised confidence: 35% → 30%
```

```
BUILDER'S RESPONSE:
Attack: A15 (Long files may degrade performance)
Response type: Reinforce
Content: This is a real risk, but the toolkit already has short skills
alongside long ones. The format does not require length — ARAW is long
because the procedure is complex. A simpler skill like /but is short.
The format scales in both directions.
Revised confidence: 30% (unchanged — this defense holds but doesn't
recover from the fatal attacks)
```

```
BUILDER'S RESPONSE:
Attack: A7 (Hidden assumptions about LLM attention)
Response type: Concede partially
Content: The assumption that LLMs process all sections equally is likely
false. However, the format's use of headers and bold text may actually
help LLMs locate relevant sections. This is an empirical question that
neither side can resolve without testing.
Revised confidence: 30% (unchanged)
```

---

## Step 5: Final Verdict

| Outcome | Applies? |
|---------|----------|
| Claim survives all attacks | No |
| Claim survives with repairs | Partially — but the repairs change the claim fundamentally |
| Claim partially survives | **Yes** — a narrower version survives |
| Claim falls to attacks | The original "best" claim falls |

**The original claim falls.** The superlative "best" cannot survive four fatal attacks, all of which target the absence of comparative evidence and the logical gap between "works" and "best."

**A narrower claim survives:** "Structured markdown is an effective, practical, author-friendly format for encoding thinking procedures that LLMs can execute. It has meaningful advantages (no tooling, human-readable, composable) and meaningful risks (no enforcement, potential attention degradation on long files, untested executor-optimality)."

---

## Step 6: Report

```
ADVERSARIAL REVIEW:
Original claim: "The skill format (structured markdown procedures) is
the best format for encoding thinking procedures."
Confidence before review: 72%

Attacks:
| # | Attack | Severity | Builder Response | Result |
|---|--------|----------|-----------------|--------|
| A1 | Existence ≠ optimality | Serious | — | Weakened |
| A2 | Quantity irrelevant to "best" | Serious | — | Weakened |
| A3 | Zero comparative data | Fatal | Conceded | Fell |
| A4 | Cherry-picked evidence | Serious | — | Weakened |
| A5 | Model-generation dependent | Minor | — | Survived |
| A6 | "Works" ≠ "best" | Fatal | Repaired to weaker claim | Fell (original) |
| A7 | Hidden LLM attention assumptions | Serious | Partially conceded | Weakened |
| A8 | Quality from content not format | Serious | — | Weakened |
| A9 | Reasoning equally supports "good enough" | Serious | — | Weakened |
| A10 | "Best" is unfalsifiable as stated | Serious | — | Weakened |
| A11 | No test methodology applied | Serious | — | Weakened |
| A12 | Contradicts known LLM behavior | Serious | — | Weakened |
| A13 | Author-optimal ≠ executor-optimal | Fatal | Repaired (narrowed) | Fell (original) |
| A14 | No ablation studies | Fatal | Conceded | Fell |
| A15 | Long files may degrade performance | Serious | Partially defended | Weakened |

Verdict: FELL (original claim) / SURVIVED WITH REPAIRS (narrowed claim)
Confidence after review: 30% for original claim, ~65% for narrowed claim

Revised claim: "Structured markdown is a practical, author-friendly
format for encoding thinking procedures that LLMs can execute effectively.
It is good enough and has real advantages, but 'best' is undefended and
possibly wrong."

Strongest surviving evidence:
- 563 working skills demonstrate viability at scale
- No-tooling, human-readable, composable — real practical advantages
- The format scales from short to long procedures

Weakest point:
- Zero comparative testing. The entire "best" claim rests on no evidence
  whatsoever. This is the single most damaging gap.

What would change verdict:
- Comparative study: Encode 20 representative skills in 4 formats
  (structured markdown, few-shot examples, Python/code, YAML/JSON),
  run each 10 times, score outputs blindly. If structured markdown
  wins statistically, the original claim is resurrected.
- Ablation study: Remove format elements (templates, failure mode tables,
  depth scaling) one at a time and measure output quality degradation.
  This would identify which structural elements actually matter.
- LLM-native format exploration: Ask the LLM what format it finds
  easiest to follow, then test whether that self-report correlates
  with output quality.
```

---

## Key Takeaways

1. **The word "best" is doing all the damage.** "Effective," "practical," "proven at scale" — all defensible. "Best" requires comparative evidence that does not exist.

2. **The deepest vulnerability is the author/executor conflation.** The format is clearly optimized for a human writing procedures in a text editor. Whether that is also what an LLM executes most reliably is an open empirical question nobody has tested.

3. **The format may contain cargo cult structure.** Without ablation studies, we do not know if templates, failure mode tables, depth scaling tables, and verification checklists actually improve LLM output — or if they just make the author feel more rigorous while the LLM skims past them.

4. **Alternative formats deserve serious consideration:**
   - **Few-shot examples** — may align better with how LLMs actually learn in-context
   - **Code-based procedures** — can enforce constraints markdown cannot
   - **Hybrid formats** — brief markdown instruction + worked example could outperform long structural templates
   - **Compiled formats** — author in markdown, compile to an LLM-optimized format for execution

5. **The most productive next step** is not philosophical debate but empirical testing: pick 5 skills, encode them in 3 formats, run them 10 times each, and score the outputs blind.

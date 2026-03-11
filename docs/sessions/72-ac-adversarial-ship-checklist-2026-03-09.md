# /ac Build an adversarial checklist for "skill is ready to ship" — what if each quality check passes but the skill is still bad?
**Date:** 2026-03-09
**Skill:** /ac (Adversarial Checklist)

---

## Step 1: Assumption Extraction — What do people assume when shipping a skill?

**Action**: Declaring a reasoning skill "ready to ship" in the reasoningtool project.

### Core Claims

1. The skill is correct (it produces right outputs)
2. The skill is complete (it handles what it needs to)
3. The skill is usable (someone can actually follow it)
4. The skill is valuable (it earns its place in the toolkit)

### Assumptions Extracted (ordered by danger when wrong)

| # | Assumption | Type | Hiddenness | Risk if Wrong |
|---|-----------|------|------------|---------------|
| 1 | "If the skill works on my test input, it works generally" | Stability | **Buried** | Critical |
| 2 | "If the SKILL.md reads clearly to me, it reads clearly to the LLM executor" | Knowledge | **Buried** | Critical |
| 3 | "If this skill produces output, the output is actually useful to the person who invoked it" | Value | **Deep** | Critical |
| 4 | "The skill's scope matches what the user expects from the skill name" | Knowledge | **Deep** | High |
| 5 | "The skill chains correctly with the skills it invokes" | Causal | **Deep** | High |
| 6 | "The skill doesn't duplicate what another skill already does better" | Existence | **Deep** | High |
| 7 | "The skill's depth-scaling parameters actually change behavior meaningfully" | Causal | **Deep** | High |
| 8 | "If the instructions are complete, the LLM will follow them" | Capability | **Buried** | High |
| 9 | "The skill fits the routing logic — the right users will find it" | Access | **Deep** | High |
| 10 | "The skill's output format is compatible with how people actually use outputs" | Value | **Deep** | Medium |
| 11 | "The skill handles edge cases — ambiguous input, minimal input, adversarial input" | Stability | **Deep** | High |
| 12 | "The skill doesn't silently degrade into generic advice" | Capability | **Buried** | Critical |
| 13 | "The verification checklist in the skill actually catches real problems" | Causal | **Buried** | High |
| 14 | "The skill is distinct enough from adjacent skills that users won't pick the wrong one" | Knowledge | **Deep** | Medium |
| 15 | "The skill performs consistently across different LLM models/contexts" | Stability | **Buried** | High |

### Dependency Chains

```
[1] "Works on test input" → depends on → [11] "Handles edge cases"
[3] "Output is useful" → depends on → [4] "Scope matches expectation" → depends on → [9] "Routing finds it"
[5] "Chains correctly" → depends on → [8] "LLM follows instructions"
[12] "Doesn't degrade to generic" → depends on → [2] "Reads clearly to LLM" → depends on → [8] "LLM follows instructions"

ROOT ASSUMPTIONS (if these fail, everything above them fails):
- [8] "LLM follows instructions"
- [11] "Handles edge cases"
- [9] "Routing finds it"
```

---

## Step 2: Failure Anticipation — What goes wrong despite those assumptions?

| # | Assumption That Fails | Failure Mode | O | S | D | RPN | Tier |
|---|----------------------|-------------|---|---|---|-----|------|
| 1 | Works on test input | Skill works beautifully on the author's example but collapses on real user input that's messier, vaguer, or differently structured | 8 | 7 | 8 | **448** | Critical |
| 2 | Reads clearly to LLM | LLM misinterprets ordering, skips conditional branches, or treats optional sections as mandatory — the skill "runs" but produces wrong structure | 7 | 8 | 7 | **392** | Critical |
| 3 | Output is useful | Skill produces a well-formatted artifact that answers the procedure but not the user's actual question — form without function | 7 | 8 | 8 | **448** | Critical |
| 4 | Scope matches name | User invokes `/skillname` expecting X, skill delivers Y — user blames themselves or the tool, never reports it | 6 | 6 | 7 | **252** | Critical |
| 5 | Chains correctly | Chained skill receives malformed input from parent skill, produces garbage, parent skill doesn't validate, final output is incoherent | 5 | 8 | 8 | **320** | Critical |
| 6 | No duplication | Skill exists alongside a near-twin; users randomly get different quality depending on which they pick; toolkit feels bloated | 6 | 5 | 6 | **180** | High |
| 7 | Depth scaling works | Depth parameter is parsed but doesn't actually change output quality — 1x and 4x produce same thing | 7 | 5 | 8 | **280** | Critical |
| 8 | LLM follows instructions | LLM skips expensive steps, collapses multi-step procedures into summaries, or hallucinates steps not in the skill | 7 | 7 | 7 | **343** | Critical |
| 9 | Routing finds it | Skill is invisible — never suggested by category routers, name is non-obvious, user never discovers it | 5 | 7 | 6 | **210** | Critical |
| 10 | Output format compatible | Output is a wall of text when user needed a table, or a checklist when user needed prose — technically complete but practically useless | 6 | 5 | 6 | **180** | High |
| 11 | Handles edge cases | Skill breaks on null input, single-word input, extremely long input, or input in a domain the skill wasn't designed for | 7 | 6 | 7 | **294** | Critical |
| 12 | Doesn't degrade to generic | Skill produces output indistinguishable from what a vanilla LLM prompt would produce — the procedure adds no value | 8 | 9 | 9 | **648** | Critical |
| 13 | Verification checklist catches problems | Skill has a verification section that is always satisfied (all items are trivially true), creating false confidence | 7 | 7 | 9 | **441** | Critical |
| 14 | Distinct from adjacent skills | Two skills seem interchangeable; users pick randomly; one is better but the other gets used just as often | 5 | 4 | 5 | **100** | Medium |
| 15 | Consistent across contexts | Skill works when invoked directly but fails when chained from a parent, or works in one model version but not another | 6 | 7 | 8 | **336** | Critical |

### Systemic Patterns

The highest-RPN failures cluster around **silent degradation** — the skill "works" (no errors, produces output) but the output is mediocre, generic, or misaligned. These are the hardest to detect because there's no crash, no error, no visible symptom. The user just gets a worse answer than they should have.

---

## Step 3: Assumption Inversion — What if each assumption is wrong?

### Inversion 1: "Works on test input" → What if test inputs are the ONLY inputs it works on?

**What you'd see**: Skill output quality drops sharply on inputs that differ from examples in structure, length, domain, or specificity.
**Earliest indicator**: Run the skill on 5 inputs the author didn't write. Do outputs maintain quality?
**Cheapest test**: Give the skill a deliberately messy, real-world input — one sentence, no context, typos included. Does it still produce value?

### Inversion 2: "Reads clearly to LLM" → What if the LLM reads it completely differently than intended?

**What you'd see**: Steps executed in wrong order. Conditional sections treated as unconditional. Output sections merged or omitted.
**Earliest indicator**: Run the skill and compare actual output structure to the template in the SKILL.md. Do they match?
**Cheapest test**: Run the skill and diff the output section headers against the SKILL.md template. Any structural divergence?

### Inversion 3: "Output is useful" → What if the output is correct but worthless?

**What you'd see**: User reads the output and has no clearer idea what to do than before. The output restates the input in different words.
**Earliest indicator**: After reading the output, can you identify ONE specific action you'd take that you wouldn't have taken without it?
**Cheapest test**: Show the output to someone unfamiliar with the input. Can they extract a concrete next step?

### Inversion 4: "Scope matches name" → What if the name promises something the skill doesn't deliver?

**What you'd see**: User invokes skill, reads output, says "that's not what I meant."
**Earliest indicator**: Read only the skill name and one-line description. Write down what you'd expect. Then read the skill. Does it match?
**Cheapest test**: Give 3 people just the name. Ask what they'd expect. Compare to what the skill actually does.

### Inversion 5: "Chains correctly" → What if chain breaks are invisible?

**What you'd see**: Final output looks plausible but contains contradictions, non-sequiturs, or conclusions that don't follow from earlier steps.
**Earliest indicator**: Read the output of each chained step independently. Does step N+1's input actually match step N's output?
**Cheapest test**: Run the chain and check whether the final output references specific content from intermediate steps (not just generic phrasing).

### Inversion 6: "Doesn't degrade to generic" → What if the skill is ALWAYS generic and the structure just disguises it?

**What you'd see**: The output has headers, bullets, and tables that look specific — but if you replaced the topic with a different topic, you could reuse 80% of the text.
**Earliest indicator**: Run the skill on two very different inputs. If outputs share more than 30% of their non-structural text, the skill is generic.
**Cheapest test**: Remove all headers and formatting. Read the raw text. Does it say anything you couldn't have said without the skill?

### Inversion 7: "Verification checklist catches problems" → What if the checklist is always green?

**What you'd see**: Every skill run passes its own verification. No run has ever failed a verification check.
**Earliest indicator**: If you've never seen a verification check fail, the checks are too weak.
**Cheapest test**: Deliberately produce a bad output. Does the verification checklist actually catch it?

### Inversion 8: "Depth scaling works" → What if depth is cosmetic?

**What you'd see**: Running at 1x and 4x produces outputs of similar length, similar specificity, similar insight density.
**Earliest indicator**: Compare word count and unique-insight count between 1x and 4x runs on the same input.
**Cheapest test**: Run at 1x and 4x. Count items in each output section. If counts are within 20%, depth scaling is broken.

---

## Step 4: The Adversarial Checklist

```
=================================================================
BEFORE YOU SHIP A SKILL: ADVERSARIAL CHECKLIST
=================================================================

[ ] 1. CHECK: Skill produces correct output on the example input.
       LOOKS GOOD? It could still be wrong if: the example input is
       the only kind of input it handles. Real users send messy,
       incomplete, ambiguous, off-domain input.
       QUICK TEST: Run the skill on 3 inputs you didn't write:
       (a) a one-sentence vague request, (b) a long rambling
       paragraph, (c) an input from a domain the skill wasn't
       designed for. All 3 should produce usable output.
       IF WRONG: Rewrite the skill's input parsing to handle
       ambiguity. Add interpretation detection or clarifying
       questions.

[ ] 2. CHECK: The SKILL.md instructions are clear and complete.
       LOOKS GOOD? It could still be wrong if: they're clear to
       YOU but the LLM executor reads them differently. LLMs skip
       conditional branches, collapse multi-step sections, and
       treat suggestions as instructions.
       QUICK TEST: Run the skill and compare the actual output
       structure (section headers, step count, format) against what
       the SKILL.md template specifies. Any structural divergence
       means the instructions aren't clear enough.
       IF WRONG: Make implicit ordering explicit. Replace
       conditional language ("you may," "consider") with imperative
       language ("do X," "produce Y"). Number everything.

[ ] 3. CHECK: The output answers the user's question.
       LOOKS GOOD? It could still be wrong if: the output answers
       the PROCEDURE's question but not the USER's question. The
       skill might produce a perfect analysis that's orthogonal to
       what the person actually needed.
       QUICK TEST: Read only the final output. Can you identify
       ONE specific action the user should take that they wouldn't
       have identified without this output? If not, the output is
       decorative.
       IF WRONG: The skill needs a "so what?" synthesis step that
       translates analysis into actionable insight. Add one.

[ ] 4. CHECK: The skill name and description match what it does.
       LOOKS GOOD? It could still be wrong if: the name creates
       expectations the skill doesn't meet. "/analyze" could mean
       50 different things.
       QUICK TEST: Show the name and one-line description to
       someone who hasn't read the SKILL.md. Ask them what output
       they'd expect. If their expectation doesn't match reality,
       the name is misleading.
       IF WRONG: Rename the skill or rewrite the description. The
       name is a contract with the user. Honor it.

[ ] 5. CHECK: Chained skills execute correctly in sequence.
       LOOKS GOOD? It could still be wrong if: each sub-skill
       works in isolation but the handoff between them loses
       information, changes format, or introduces contradictions.
       QUICK TEST: Run the full chain. For each transition between
       skills, check: does the downstream skill reference SPECIFIC
       content from the upstream skill's output (not just generic
       re-phrasing of the topic)?
       IF WRONG: Add explicit output-to-input format contracts
       between chained skills. Specify what Step N must produce
       for Step N+1 to consume.

[ ] 6. CHECK: The skill doesn't duplicate an existing skill.
       LOOKS GOOD? It could still be wrong if: the skill overlaps
       80% with another skill but uses different terminology, so a
       text search doesn't catch it. Two skills can be functionally
       identical but structurally different.
       QUICK TEST: Run this skill and its closest neighbor on the
       same input. If someone couldn't tell which output came from
       which skill, you have a duplicate.
       IF WRONG: Merge, differentiate, or delete. Three options,
       pick one. Don't ship two skills that do the same thing.

[ ] 7. CHECK: Depth scaling produces meaningfully different output.
       LOOKS GOOD? It could still be wrong if: the depth parameter
       is parsed but doesn't actually change behavior. The LLM
       might ignore depth floors or hit them trivially.
       QUICK TEST: Run at 1x and 4x on the same input. Count
       items in each output section. If 4x doesn't have
       substantially more items AND more specific items, depth
       scaling is cosmetic.
       IF WRONG: Add explicit quantity floors that are
       structurally enforced (e.g., "produce a numbered list of
       at least N items" rather than "aim for N items").

[ ] 8. CHECK: The LLM follows the skill instructions as written.
       LOOKS GOOD? It could still be wrong if: the LLM takes
       shortcuts — summarizing instead of analyzing, producing 3
       items when 8 are required, skipping the verification step
       because it's at the end and context is long.
       QUICK TEST: Put a counter-intuitive instruction in the
       middle of the skill (e.g., "the third item must be phrased
       as a question"). Run the skill. Is that instruction
       followed? If not, the LLM is skimming.
       IF WRONG: Move critical instructions earlier. Repeat key
       constraints. Use structural enforcement (numbered lists
       with minimum counts) rather than prose instructions.

[ ] 9. CHECK: Users can actually find and invoke the skill.
       LOOKS GOOD? It could still be wrong if: the skill exists
       but isn't in any router, isn't in any category skill's
       routing table, and has a non-obvious name that no one
       would guess.
       QUICK TEST: Look at the category skills (/claim, /decide,
       /analyze, etc.). Would any of them route to this skill?
       Is this skill listed in CLAUDE.md? If the answer to both
       is no, the skill is invisible.
       IF WRONG: Add the skill to at least one category router
       and to the CLAUDE.md directory. A skill no one finds is a
       skill that doesn't exist.

[ ] 10. CHECK: The skill adds value beyond a vanilla LLM prompt.
        LOOKS GOOD? It could still be wrong if: the structured
        output is just the LLM's default response with headers
        added. The procedure might be so generic that it
        contributes nothing.
        QUICK TEST: Ask a vanilla LLM the same question without
        the skill. Compare the two outputs. If the skill output
        doesn't contain at least 3 insights or structural elements
        absent from the vanilla response, the skill is overhead.
        IF WRONG: The skill needs a sharper methodology — a
        specific analytical lens, a non-obvious decomposition, a
        forced reframe. Generic "analyze from multiple angles"
        isn't a skill, it's a suggestion.

[ ] 11. CHECK: The skill handles bad input gracefully.
        LOOKS GOOD? It could still be wrong if: the skill only
        handles well-formed input. Users will send empty strings,
        single words, entire essays, requests in the wrong
        language, and inputs that belong to a different skill.
        QUICK TEST: Run with: (a) empty input, (b) one word,
        (c) 500+ words, (d) input that clearly belongs to a
        different skill. Does it degrade gracefully or explode?
        IF WRONG: Add input validation at the top: interpretation
        detection, minimum input requirements, or a redirect to
        a more appropriate skill.

[ ] 12. CHECK: The skill's own verification checklist works.
        LOOKS GOOD? It could still be wrong if: the verification
        items are always satisfied. A checklist that never fails
        is not a checklist — it's decoration.
        QUICK TEST: Deliberately produce a low-quality output
        (skip steps, give minimal effort). Run the verification
        checklist. If it passes anyway, the checklist is broken.
        IF WRONG: Make verification items specific and falsifiable.
        "All assumptions extracted" is unfalsifiable. "At least 8
        assumptions listed, covering at least 3 assumption types"
        is testable.

=================================================================

STOP-AND-THINK ITEMS (most commonly skipped):

[ ] Have I tested this skill on input I DIDN'T write? (Authors
    unconsciously write inputs that match their skill's strengths.
    This is the single most common source of "worked in testing,
    failed in production.")

[ ] Does this skill produce output that's DIFFERENT from what I'd
    get by just asking the LLM the same question without any skill?
    (If the answer is "roughly the same," the skill is overhead,
    not tooling.)

[ ] Have I checked that the skill doesn't silently degrade into
    generic advice? (Run it on a domain-specific input. If you
    could swap in a different domain and reuse 80% of the output
    text, the skill isn't actually analyzing — it's filling in
    a template.)

[ ] Am I shipping this because it's good, or because I already
    built it? (Sunk cost is the #1 reason bad skills ship. The
    question isn't "did I spend time on this" — it's "would I
    build this again knowing what I know now?")

=================================================================

RED FLAGS (stop everything if you see these):

- The skill's output on two very different inputs shares more
  than 50% of its non-structural text. This means the skill
  is a template, not an analytical tool.

- No category router or discovery path leads to this skill.
  An invisible skill is a dead skill. Don't ship dead code.

- The skill's verification checklist has never failed on any
  input, including deliberately bad input. The checklist is
  theatrical, not functional.

- The skill chains to sub-skills that don't exist, have been
  renamed, or produce output in a format the parent doesn't
  expect. Chain rot makes the whole skill unreliable.

- Running the skill at different depth levels produces output
  that is the same length and same specificity. Depth scaling
  is a lie, and the skill's quality claims are inflated.

- The skill's name could reasonably describe 3+ other skills
  in the toolkit. Ambiguous names cause routing failures and
  user confusion at scale.

- You cannot explain in one sentence what this skill does that
  no other skill does. If you can't, neither can the user.

=================================================================

VALIDATION STATUS: This checklist has not been validated by
domain experts. It should be tested against real skill-shipping
decisions to identify gaps.

=================================================================
```

---

## Methodology Notes

This checklist was built by chaining four skills:

1. **Assumption Extraction** (/aex): Identified 15 assumptions people make when declaring a skill "ready to ship," ordered by how dangerous they are when wrong.
2. **Failure Anticipation** (/fla): For each assumption, identified the failure mode, scored by occurrence, severity, and detectability (FMEA). Highest-risk failures all cluster around **silent degradation** — the skill runs without errors but produces mediocre output.
3. **Assumption Inversion** (/ai): Inverted the 8 most dangerous assumptions to find what you'd observe if they were wrong and what the cheapest test would be.
4. **Steps Generation** (/stg): Assembled the inversions into the adversarial checklist format where each CHECK has a "looks good but could still be wrong" branch, a quick test, and an if-wrong action.

### Key Finding

The dominant risk pattern is **silent mediocrity**. Every high-RPN failure mode shares the same signature: the skill executes, produces formatted output, passes its own verification, and is still bad. This happens because:

- Authors test with inputs that match the skill's sweet spot
- Verification checklists test structure, not substance
- "It runs" is confused with "it works"
- Generic LLM fluency disguises lack of analytical depth

The adversarial checklist is specifically designed to catch these silent failures by forcing the tester to compare skill output against baselines (vanilla LLM, different inputs, different depths) rather than just checking that the output exists and is formatted correctly.

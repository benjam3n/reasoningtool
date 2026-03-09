---
name: "memk - Knowledge Capture"
description: "Systematic approach to capturing, organizing, and maintaining personal knowledge for future retrieval and use."
---

# Knowledge Capture

**Input**: $ARGUMENTS

Note: `/mem` exists for mental models. This skill is for personal knowledge management — capturing insights, decisions, patterns, and facts in a way your future self can retrieve and use.

---

## Step 1: Identify What's Worth Capturing

Not everything deserves a knowledge entry. Filter the input through these criteria:

1. **Insight**: Something you understood for the first time or in a new way
2. **Decision + rationale**: A choice you made and WHY (the "why" decays fastest)
3. **Pattern**: A recurring observation across multiple instances
4. **Hard-won fact**: Something that took effort to find or verify
5. **Procedure**: A sequence of steps you figured out and will need again
6. **Mistake + lesson**: An error and what it taught you

```
CAPTURE TYPE: [insight / decision / pattern / fact / procedure / mistake]
WORTH CAPTURING BECAUSE: [why this will matter later]
EXPIRY RISK: [will this become outdated? If so, when?]
```

SKIP: If the input doesn't pass any of these filters, tell the user — not everything needs to be captured. Over-capturing creates noise that drowns signal.

---

## Step 2: Choose Storage Format

Match the format to the knowledge type:

| Type | Best Format |
|---|---|
| **Insight** | One-paragraph summary with the "so what" |
| **Decision** | Decision record: context, options considered, choice, rationale |
| **Pattern** | Pattern name + trigger conditions + expected behavior |
| **Fact** | Assertion + source + date verified |
| **Procedure** | Numbered steps, copy-paste ready |
| **Mistake** | What happened, why, what to do instead |

Write the entry in the chosen format now. Rules:
- Write for your future self who has forgotten the context
- Lead with the conclusion, not the backstory
- Include ONE concrete example
- Keep it under 200 words

```
--- KNOWLEDGE ENTRY ---
[formatted entry here]
--- END ---
```

---

## Step 3: Create Retrieval Structure

Knowledge you can't find is knowledge you don't have. Design retrieval paths:

1. **Tags**: 2-5 keywords your future self would search for
   - Include both the topic and the domain
   - Include at least one "when would I need this" tag
2. **Hierarchy**: Where does this fit in your existing knowledge structure?
   - Parent category
   - Related entries (if any)
3. **Links**: What other knowledge does this connect to?
   - What does this depend on?
   - What depends on this?

```
TAGS: [tag1, tag2, tag3, ...]
CATEGORY: [parent] > [subcategory]
LINKS TO: [related entries or topics]
RETRIEVAL TRIGGER: [situation where you'd need this]
```

---

## Step 4: Write in Future-Self-Friendly Format

Review the entry from Step 2 and check:

1. **Context independence**: Would this make sense with zero memory of today?
2. **Actionability**: Can future-you act on this without further research?
3. **Scannability**: Can the key point be grasped in under 10 seconds?
4. **Specificity**: Are there concrete details, not just vague principles?

Rewrite if any check fails. The most common failure mode is writing for present-you who has full context instead of future-you who has none.

---

## Step 5: Schedule Review

Knowledge entries decay. Set a review schedule:

| Entry Type | Review Frequency |
|---|---|
| **Decision rationale** | When the decision comes up for re-evaluation |
| **Procedure** | Next time you use it (then update) |
| **Fact** | Every 6-12 months (check if still true) |
| **Pattern** | When you encounter a potential instance |
| **Insight** | Quarterly (has your understanding evolved?) |
| **Mistake** | Never delete; review annually |

```
NEXT REVIEW: [date or trigger condition]
REVIEW ACTION: [verify / update / archive / delete]
```

---

## Step 6: Prune Outdated Entries

If the user is reviewing existing knowledge (not capturing new):

1. For each entry, ask: "If I discovered this today, would I capture it?"
2. If NO: archive or delete
3. If YES but it's stale: update with current understanding
4. If YES and current: keep, confirm review date

Signs an entry is stale:
- The technology/tool it references has changed
- Your understanding has evolved past it
- You've never retrieved it in 12+ months
- It contradicts something you now know to be true

```
PRUNING RESULT:
- Kept: [count]
- Updated: [count]
- Archived: [count]
- Deleted: [count]
```

---

## Integration

Use with:
- `/lr` -> Research a topic, then capture key findings with /memk
- `/rca` -> After root cause analysis, capture the lesson
- `/curd` -> Capture knowledge milestones during a learning path
- `/dcp` -> After a decision, capture the rationale before you forget it

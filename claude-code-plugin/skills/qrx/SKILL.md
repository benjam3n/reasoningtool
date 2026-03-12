---
name: "qrx - QuestionRoute Extract"
description: "Extract structured QuestionRoute data (questions, routes, chains, regresses) from unstructured prose, skills, or markdown files. Prototype for structured skill output."
output:
  format: "json"
  writes_files: true
  schema:
    questions: "QuestionRoute Question[]"
    routes: "QuestionRoute RouteFile[]"
    chains: "QuestionRoute QuestionChain[]"
    regresses: "QuestionRoute Regress[]"
---

# QuestionRoute Extract

**Input**: $ARGUMENTS

The input should be a file path, a block of text, or a skill name to extract from.

---

## Output Schema

This skill produces structured JSON files, not prose. Every output must conform to these types exactly.

### Question
```json
{
  "id": "string (kebab-case, unique)",
  "text": "string (the question ending in ?)",
  "definition": "string (one sentence: what this question searches for)",
  "semanticType": "string (causation | location | temporal | identity | method | evaluation | quantity | relation | condition | existence | obligation | preference | possibility | comparison)",
  "abstractionLevel": "number (1=very specific, 2=specific, 3=moderate, 4=general, 5=universal)",
  "slots": "string[] (what this question accepts as input)",
  "tags": "string[] (topical labels)"
}
```

### Route
```json
{
  "sourceId": "string (question ID this routes FROM)",
  "routes": [
    {
      "targetId": "string (question ID this routes TO)",
      "type": "prerequisite | implication | clarification | expansion | opposition | composition | analogy | causal",
      "reason": "string (one sentence: why this route exists)",
      "weight": "high | medium | low"
    }
  ]
}
```

### Chain
```json
{
  "id": "string (kebab-case)",
  "links": ["string (question IDs or 'chain:chainId' references)"],
  "composedText": "string (the compound question formed by composing the links)",
  "compositionType": "conjunction | embedding | conditional | sequential | telescoping",
  "depth": "number (0=all atomic, 1+=contains chains)",
  "tags": "string[]"
}
```

### Regress
```json
{
  "id": "string (kebab-case)",
  "questionRef": "string (question ID or 'chain:chainId')",
  "predictions": [
    {
      "id": "string",
      "text": "string (the predicted answer)",
      "truthStatus": "guess",
      "testedBy": [],
      "followUps": ["string (question IDs spawned by this answer)"],
      "reasoning": ""
    }
  ],
  "outputs": [],
  "depth": "number",
  "tags": "string[]"
}
```

---

## Process

### Step 1: Read the source

If the input is a file path, read the file. If it's a skill name (like `/rca`), read `claude-code-plugin/skills/{name}/SKILL.md`. If it's raw text, use it directly.

### Step 2: Extract raw questions

Find every sentence or phrase that functions as a question — ending in `?` or structured as an interrogative.

Filter OUT:
- Rhetorical questions that are really statements ("Isn't that obvious?")
- Meta-questions about the skill itself ("What depth should I use?")
- Example questions used as illustrations (unless they're genuinely useful as search directions)

Filter IN:
- Questions that define a search direction ("What is X?", "Why does Y?")
- Questions that could be asked of any subject ("Is it true?", "What stops you?")
- Questions embedded in procedures that guide thinking

### Step 3: Reduce to atomic form

For each extracted question, determine if it's atomic or compound.

**Atomic**: A single search direction. One question word, one focus.
- "Why?" → atomic
- "What stops you?" → atomic (What + constraint)
- "Is it true?" → atomic

**Compound**: Multiple search directions fused together.
- "What would you do if you weren't trying to improve?" → What + Do + If + Improve (chain candidate)
- "Is the seeking optimizing for feeling or for results?" → compound with comparison

For compound questions:
1. Decompose into atomic questions
2. Create the atomic questions as individual entries
3. Create a chain that composes them back into the compound form

### Step 4: Deduplicate and normalize

- Merge questions that are the same search direction with different wording
- Prefer the shorter, more general form
- Check against existing QuestionRoute data to avoid duplicating questions that already exist
- Use existing question IDs where a match exists

### Step 5: Assign structure

For each surviving atomic question:
- **id**: kebab-case, descriptive, unique. Check existing IDs in the target data directory.
- **text**: The question in its cleanest form, ending in `?`
- **definition**: One sentence describing what this question searches for. Do NOT use flowery language like "The fundamental question of..." — just say what it does.
- **semanticType**: Classify based on what kind of answer the question seeks
- **abstractionLevel**: 1-5 based on how general vs specific
- **slots**: What the question accepts (e.g., "Why?" has slot for "subject")
- **tags**: Topical labels relevant to the question's domain

### Step 6: Infer routes

Look at how questions relate to each other in the source material:
- Questions that appear in sequence → potential route (check if the connection is logical)
- Questions where one is a prerequisite for another → prerequisite route
- Questions where one challenges another → opposition route
- Questions where one expands another → expansion route
- Questions where one causes another to be asked → causal or implication route

Each route needs a `reason` — one sentence explaining WHY this connection exists. Not a label, a reason.

### Step 7: Build chains

For compound questions identified in Step 3:
- Create a chain linking the atomic components
- Determine composition type:
  - **conjunction**: A AND B ("Why and how?")
  - **embedding**: A contains B ("Why do you want?")
  - **conditional**: IF A THEN B ("If you want, should you?")
  - **sequential**: A THEN B ("First why, then how")
  - **telescoping**: A narrows into B ("Where specifically here?")

### Step 8: Build regresses (if applicable)

If the source contains predicted answers or answer→follow-up patterns:
- Create regress entries
- All predictions start as `truthStatus: "guess"` with empty `testedBy`
- Follow-ups should reference question IDs (create new questions if needed)
- `outputs` always starts empty — outputs are discovered, not pre-filled

### Step 9: Write files

Write each question, route file, chain, and regress to the target QuestionRoute data directory.

Default target: The QuestionRoute project data directory. If $ARGUMENTS includes a target path, use that.

File naming:
- Questions: `data/questions/{id}.json`
- Routes: `data/routes/{sourceId}.json` (append to existing if file exists)
- Chains: `data/chains/{id}.json`
- Regresses: `data/regress/{id}.json`

### Step 10: Report

After writing files, output a summary:

```
EXTRACTED FROM: [source file/text]

QUESTIONS: [count] new, [count] matched existing
  [list of new question IDs with text]

ROUTES: [count] new connections
  [list of sourceId → targetId with type]

CHAINS: [count] new
  [list of chain IDs with composedText]

REGRESSES: [count] new
  [list of regress IDs with questionRef]

FILES WRITTEN:
  [list of file paths]
```

---

## Judgment Guidelines

These are the hard calls. When in doubt:

| Judgment | Default |
|---|---|
| Is this really a question or just rhetoric? | If it defines a search direction, it's a question |
| Atomic or compound? | If it has one question word and one focus, atomic |
| What abstraction level? | Compare to existing questions: Why?=4, Where should I eat?=1 |
| Does this route exist? | Only if you can state WHY in one sentence |
| What composition type? | Read the compound question aloud — how do the parts fuse? |
| Should this be a regress? | Only if the source explicitly predicts answers |
| Does this duplicate an existing question? | Check text AND semantic type, not just text |

---

## Depth Scaling

| Depth | Min Questions | Min Routes | Min Chains | Min Regresses |
|-------|--------------|-----------|-----------|--------------|
| 1x | 5 | 3 | 0 | 0 |
| 2x | 10 | 8 | 1 | 0 |
| 4x | 20 | 15 | 3 | 1 |
| 8x | 40 | 30 | 6 | 2 |

Default: 2x. Parse depth from $ARGUMENTS if specified.

---

## Pre-Completion Checklist

- [ ] Every extracted question has all 7 fields populated
- [ ] No question uses flowery/explainer definitions
- [ ] All IDs are kebab-case and unique
- [ ] Routes have one-sentence reasons (not labels)
- [ ] Chains correctly decompose compound questions
- [ ] All regress predictions have truthStatus "guess" and empty testedBy
- [ ] No duplicate questions (checked against existing data)
- [ ] Files written to correct paths
- [ ] Summary report produced

---

## Integration

- This is the first skill with `output.format: json` and `output.writes_files: true`
- Future skills can adopt the same frontmatter pattern to declare structured output
- Use from: any project that needs to extract QuestionRoute data from text
- Pairs with: `/extract` (finds skills), `/sf` (saves prose output)

---
name: saaiasa
description: "Classify utterances in a gate/procedure/document so the system doesn't answer the wrong thing."
---

# Apply Intent + Speech Acts

**Input**: $ARGUMENTS

---

## Overview

Classify utterances in a gate/procedure/document so the system doesn't answer the wrong thing (question vs command vs judgment vs guess). Many problems in procedure execution come from treating one speech act type as another.

## Steps

### Step 1: Extract Utterances
From the target artifact (gate, procedure, document):
1. Extract all question-like lines (containing "?", "whether", "how", "what", "is there")
2. Extract all instruction-like lines (containing imperatives, "should", "must", "do")
3. Extract all judgment-like lines (containing evaluative language, "good", "adequate", "correct")
4. Extract all prediction-like lines (containing "will", "would", "likely", "expect")

### Step 2: Classify Each Utterance
For each extracted line, assign a speech act type:

| Type | Definition | Example | Correct Response |
|------|-----------|---------|-----------------|
| **Question** | Seeks information | "What are the risks?" | Answer with information |
| **Command** | Directs action | "List all dependencies" | Execute the action |
| **Request** | Asks for action (politely) | "Could you check..." | Execute or negotiate |
| **Constraint** | Sets boundaries | "Must not exceed budget" | Honor as a limit |
| **Judgment** | Evaluates quality | "This is adequate" | Accept or challenge with evidence |
| **Prediction** | Forecasts outcome | "This will succeed" | Verify or challenge |
| **Hypothesis** | Proposes testable claim | "If X then Y" | Design test |
| **Goal** | States desired outcome | "We want to increase..." | Plan toward it |
| **Story** | Narrates events | "Last time, we..." | Extract lessons |

### Step 3: Identify Mismatches
Flag lines where the surface form doesn't match the function:

| Surface Form | Actual Function | Problem | Fix |
|-------------|----------------|---------|-----|
| Question ("Is this good?") | Judgment (seeking validation) | Will get answer instead of evaluation | Rewrite as explicit judgment request |
| Command ("Determine if...") | Question (seeking information) | Will get action instead of answer | Rewrite as question |
| Judgment ("This works") | Hypothesis (untested) | Will be treated as settled | Rewrite as hypothesis to test |
| Question ("Don't you think...") | Command (seeking agreement) | Leading question | Rewrite as open question or explicit command |

### Step 4: Split Bundled Utterances
Identify lines that contain multiple speech acts disguised as one:

**Before:** "Is the goal clear and are the steps complete and has the timeline been validated?"
**After:**
1. "Is the goal clear?" (Question — definition check)
2. "Are the steps complete?" (Question — completeness check)
3. "Has the timeline been validated?" (Question — validation check)

Each should be answered independently.

### Step 5: Propose Rewrites
For each problematic utterance:

```
REWRITE:
Original: [the line as written]
Type detected: [what it looks like]
Type intended: [what it's trying to do]
Problem: [why the mismatch causes issues]
Rewrite: [clearer version]
```

### Step 6: Report
```
INTENT + SPEECH ACTS AUDIT:
Target: [what was analyzed]
Lines analyzed: [N]

Type distribution:
| Type | Count | Issues |
|------|-------|--------|
| Question | [N] | [N with mismatches] |
| Command | [N] | [N with mismatches] |
| Judgment | [N] | [N with mismatches] |
| [etc] | | |

Mismatches found: [N]
Bundled utterances: [N] → split into [N] individual lines

Rewrites proposed: [N]
Top priority rewrites: [which are most impactful]
```

## When to Use
- When a line reads like a question but functions like a command or judgment
- When a gate/procedure mixes description and recommendation
- When "what is being asked?" is unclear
- → INVOKE: /saqrc (question rewrite chains) for unclear questions
- → INVOKE: /saadag (detectors and generators) for finding ambiguity

## Verification
- [ ] All utterances extracted and classified
- [ ] Mismatches between surface form and function identified
- [ ] Bundled utterances split into single speech acts
- [ ] Rewrites are clearer than originals
- [ ] Each rewrite preserves the original intent

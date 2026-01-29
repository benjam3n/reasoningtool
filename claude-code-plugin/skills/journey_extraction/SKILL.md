---
name: journey_extraction
description: "Extract the underlying GOAL JOURNEY from any source:"
---

# Goal Journey Extraction

## Overview
Extract the underlying GOAL JOURNEY from any source:
books, videos, PDFs, conversations, experiences.

A goal journey is a CHAIN OF GOALS:
Action → Goal → Goal → ... → Intrinsic Goal

This is NOT a narrative arc. It's a PURPOSE CHAIN.

## Steps

### Step 1: Identify the action
What action is being taken (or was taken)?

Be specific about what was DONE, not what happened.

NOT: "John succeeded"
BUT: "Person invested years developing expertise in domain"

The action is the bottom of the goal chain.

**Output**: action_statement

### Step 2: Ask: What goal did this action serve?
Every action serves a goal. What was this action trying to achieve?

NOT: "What happened next?"
BUT: "What was this action FOR?"

Example:
Action: "Invested years developing expertise"
Goal: "Become highly capable in the domain"

**Output**: immediate_goal

### Step 3: Ask: What goal did THAT goal serve?
The goal you identified is also instrumental.
What does achieving that goal enable?

Example:
Goal: "Become highly capable in the domain"
Serves: "Be able to create significant work"

Keep going:
Goal: "Create significant work"
Serves: "Have meaningful impact"

**Output**: goal_chain (growing)

### Step 4: Continue until intrinsic goal (use value elicitation)
Keep asking "What's important to you about that?" until circularity.

Circularity indicators:
- "Because that's what I value"
- "That's just what matters"
- "I just do"

IMPORTANT:
- Don't assume "flourishing" or any default terminus
- Different people have different intrinsic goals
- Some have anti-flourishing goals (asceticism, simplicity)
- Apply intrinsic_goal_termination_gate if unsure

Example chain:
Action: Invested years developing expertise
  → Goal: Become highly capable
  → Goal: Create significant work
  → Goal: Have meaningful impact
  → INTRINSIC: [Varies - Meaning for some, Recognition for others,
                Mastery for others - discover via elicitation]

**Output**: complete_goal_chain

### Step 5: Check for additional intrinsic goals
Ask: "Is there anything else important about [original action/goal]?"

People often have MULTIPLE intrinsic goals.
Don't stop at the first one found.

If yes: Trace the new chain (repeat steps 2-4)
If no: Proceed to step 5

Example:
First chain: Expertise → Impact → Meaning
Second chain: Expertise → Recognition → Status

This person has TWO intrinsic goals: Meaning AND Status

**Output**: all_intrinsic_goals

### Step 6: Check for conflicts between intrinsic goals
If multiple intrinsic goals found:
Ask: "Do these ever conflict?"

Common conflicts:
- Freedom vs Security
- Meaning vs Recognition
- Achievement vs Peace
- Connection vs Independence

Note the conflict - the person will need to balance.

**Output**: conflicts (if any)

### Step 7: Verify the chain
Read the chain from bottom (action) to top (intrinsic):
- Does each step SERVE the next? (not just "lead to")
- Are there missing links?
- Is the intrinsic goal legitimate?

If there's a jump:
"Become highly capable" → ??? → "Live meaningful life"

Find the missing link:
"Become highly capable" → "Create significant work" → "Have impact" → "Live meaningful life"

**Output**: verified_chain

### Step 8: Generalize each step
For each step in the raw path, find the semi-generalizable form.

Use the generalization rules:
- Names → Roles (John → Person, Leader, Seeker)
- Specific things → Categories (Gibson guitar → Tool, Resource)
- Specific places → Contexts (Sam's shop → Marketplace)
- Specific actions → Action types (bought → Acquired, Obtained)
- Specific outcomes → Outcome types (got promoted → Advanced)

Test each step:
- Too specific? Abstract further
- Too abstract? Add back some specificity
- Semi-generalizable: Can apply to 10-1000 other situations

Example:
Specific: "Got promoted to VP after the merger"
Too abstract: "Status changed"
Semi-generalizable: "Person advanced through organizational transition"

**Output**: generalized_path (list of semi-generalizable steps)

### Step 9: Identify key transitions
Find the moments where the journey CHANGED significantly.

Types of transitions:
- Choice points: "Could have gone either way, chose this"
- Thresholds: "Entered new territory, can't go back"
- Transformations: "Became different than before"
- Revelations: "Understood differently than before"
- Reversals: "Direction changed completely"
- Crises: "Everything at stake"

For each transition:
- Which step is it?
- What type of transition?
- What makes it significant?

These are often the most transferable parts - the SHAPE of change.

**Output**: key_transitions (list of {step, type, significance})

### Step 10: Classify the journey archetype
Match the journey to archetypes:

Complexity: simple | complicated | complex | chaotic
Difficulty: easy | challenging | hard | seemingly_impossible
Predictability: predictable | twist | reversal | emergent
Frequency: universal | common | uncommon | rare

Also check classic structures:
- Hero's journey
- Tragedy
- Comedy
- Rags to riches
- Voyage and return

A journey may match multiple archetypes partially.

**Output**: archetype_classification

### Step 11: Test generalizability
Test: Can this journey apply to other situations?

Try instantiating in:
1. A different domain (if business → personal; if art → science)
2. A different scale (if individual → group; if small → large)
3. A different context (if modern → historical; if Western → other)

For each test:
- Does the structure still make sense?
- Do the transitions still apply?
- Would someone in that situation recognize this journey?

If it fails to transfer:
- The journey is too specific - generalize more
- Or it's a genuinely unique journey - note this

**Output**: generalizability_assessment

### Step 12: Test satisfaction
Test: Does this journey feel complete and meaningful?

Check:
- Beginning → Middle → End present?
- Movement/change throughout (not static)?
- Stakes clear (something matters)?
- Resolution provides closure (even if tragic)?
- Emotional shape recognizable?

If unsatisfying:
- Missing steps? Add them
- Wrong ending? Find true endpoint
- No stakes? Find what was at risk
- Random feeling? Find underlying pattern

**Output**: satisfaction_assessment

### Step 13: Construct final journey representation
Create the complete journey object:

```yaml
journey:
  title: "[Evocative name for this journey type]"
  source: "[Original source reference]"

  archetype:
    complexity: [simple|complicated|complex|chaotic]
    difficulty: [easy|challenging|hard|seemingly_impossible]
    predictability: [predictable|twist|reversal|emergent]
    frequency: [universal|common|uncommon|rare]
    classic_structure: [heros_journey|tragedy|comedy|rags_to_riches|voyage_and_return|none]

  steps:
    - "[Semi-generalizable step 1]"
    - "[Semi-generalizable step 2]"
    - ...

  key_transitions:
    - step: [number]
      type: [choice|threshold|transformation|revelation|reversal|crisis]
      description: "[What makes this significant]"

  intrinsic_goals:
    primary: "[Main intrinsic goal - discovered via value elicitation]"
    additional:
      - "[Additional intrinsic goal if any]"
    conflicts:
      - between: ["[Goal 1]", "[Goal 2]"]
        nature: "[Description of conflict]"
    note: "Different people may have different intrinsic goals for same journey"

  validation:
    generalizability: [passes|partial|fails]
    generalizability_notes: "[How it transferred in tests]"
    satisfaction: [satisfying|partial|unsatisfying]
    satisfaction_notes: "[What makes it satisfying or not]"
    chain_coherence:
      each_step_serves_next: [true|false]
      proper_verb_forms: [true|false]
      no_skipped_steps: [true|false]

  applicability:
    - "[Situation type 1 this applies to]"
    - "[Situation type 2 this applies to]"
    - ...

  variants:
    - "[Alternative version of this journey]"
    - "[What changes if X is different]"
    - "[Different intrinsic goal variant]"
```

**Output**: complete_journey


---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.
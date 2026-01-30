---
name: "jm - Journey Matching"
description: "Given a current situation (goal, problem, state), find journeys"
---

# Journey Matching

## Overview
Given a current situation (goal, problem, state), find journeys
from the library that might apply. This enables learning from
past patterns without reinventing every path.

## Steps

### Step 1: Characterize the situation
Describe the current situation in semi-generalizable terms.

Avoid specifics:
NOT: "I'm a 35-year-old software engineer at BigCorp wanting to start a fintech startup"
BUT: "Person in established career seeking entrepreneurial transition in technical domain"

Capture:
- Current state (what is)
- Desired state (what's sought) - if known
- Gap type (what kind of change is needed)
- Constraints (what limits options)

**Output**: situation_characterization

### Step 2: Identify archetype dimensions
Estimate the journey archetype:

Complexity:
- Simple: Direct path likely exists
- Complicated: Multiple clear steps needed
- Complex: Path will emerge through action
- Chaotic: Survival mode, stabilize first

Difficulty:
- Easy: Resources exceed requirements
- Challenging: Will require effort and growth
- Hard: Requirements exceed apparent resources
- Seemingly impossible: No obvious path

Predictability:
- Predictable: Know the general shape
- Has twist: Expect unexpected turn
- Reversal possible: May discover opposite goal
- Emergent: Destination unclear

Frequency:
- Universal: Nearly everyone faces this
- Common: Many face this
- Uncommon: Specific circumstances
- Rare: Few face this

**Output**: archetype_estimate

### Step 3: Identify domain and themes
What domain(s) does this situation belong to?

Domains:
- Personal growth
- Career / professional
- Relationship / social
- Creative / artistic
- Entrepreneurial / business
- Learning / skill development
- Health / wellbeing
- Spiritual / meaning
- Financial
- Technical / problem-solving

What themes are present?

Themes:
- Transition (leaving one thing for another)
- Growth (becoming more capable)
- Recovery (returning from setback)
- Discovery (finding what's unknown)
- Creation (making something new)
- Connection (building relationships)
- Liberation (escaping constraints)
- Mastery (achieving excellence)
- Transformation (becoming different)
- Resolution (ending conflict)

**Output**: domain_and_themes

### Step 4: Search journey library
Search for matching journeys:

Primary match criteria:
1. Archetype similarity (complexity, difficulty match)
2. Domain overlap
3. Theme alignment
4. Starting state similarity
5. Desired state similarity (if known)

Search strategy:
1. Exact archetype match + domain match
2. Partial archetype match + domain match
3. Archetype match + theme match (cross-domain)
4. Theme match only (broadest)

For each candidate:
- Why might this apply?
- What's similar?
- What's different?

**Output**: candidate_journeys

### Step 5: Evaluate fit
For each candidate journey, assess fit:

Structural fit:
- Does the starting state match?
- Does the destination (if specified) match?
- Do the constraints align?
- Are the transitions relevant?

Resonance fit:
- Does this feel like "my situation"?
- Do the steps make sense for my context?
- Would I recognize this as my potential path?

Transfer feasibility:
- Can the steps actually be instantiated?
- Are there blockers to this path?
- What would need to be true for this to work?

Score each journey: Strong fit / Moderate fit / Weak fit / No fit

**Output**: fit_assessments

### Step 6: Identify current position
For each fitting journey:

Where in the journey are you now?
- Before the journey starts?
- At step N?
- Between steps?
- Near the end?

This tells you:
- What typically comes next
- What others experienced at this point
- What challenges to expect

**Output**: position_in_journeys

### Step 7: Generate guidance
For top-matching journeys, generate guidance:

What this journey suggests:
- Typical next steps
- Common challenges at this stage
- Key transitions to prepare for
- What success looks like from here
- What failure modes to watch for

Variations to consider:
- What if your path differs?
- Alternative routes others have taken
- What makes your situation unique

Confidence level:
- Strong match: High confidence in guidance
- Moderate match: Consider this, but adapt
- Weak match: Inspiration only, don't follow literally

**Output**: journey_guidance

### Step 8: Synthesize recommendations
Combine insights from all matching journeys:

Convergent patterns:
- What do multiple journeys agree on?
- What steps appear in most matches?
- What transitions are universally important?

Divergent options:
- Where do journeys differ?
- What alternative paths exist?
- Which divergences matter for your situation?

Synthesized guidance:
- Most likely path based on matches
- Alternative paths to consider
- Key decision points ahead
- What to watch for

**Output**: synthesized_recommendations


## Output Format
```
situation_summary:
  archetype:
    complexity: '[simple|complicated|complex|chaotic]'
    difficulty: '[easy|challenging|hard|seemingly_impossible]'
  current_state: '[Semi-generalized description]'
  desired_state: '[If known]'
  domains:
  - domain1
  - domain2
  themes:
  - theme1
  - theme2
synthesis:
  alternatives:
  - path:
    - Alt step 1
    - '...'
    when_to_use: '[Condition]'
  convergent_patterns:
  - '[Pattern that multiple journeys agree on]'
  divergent_options:
  - '[Option 1: from journey A]'
  - '[Option 2: from journey B]'
  recommended_path:
    confidence: '[High|Medium|Low]'
    reasoning: '[Why this path]'
    steps:
    - Step 1
    - Step 2
    - '...'
top_matching_journeys:
- guidance:
    key_transition: '[Upcoming crucial moment]'
    next_steps:
    - Step 1
    - Step 2
    watch_for:
    - Challenge 1
    - Challenge 2
  journey:
    fit: '[Strong|Moderate|Weak]'
    source: '[Original source]'
    title: '[Journey name]'
    why_matches: '[Explanation]'
  your_position:
    current_step: N
    description: '[Where you are in this journey]'

```

---

**Input**: $ARGUMENTS

Apply this procedure to the input provided.
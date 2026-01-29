# ARAW for Problem and Solution Discovery

**Principle**: ARAW (Assume Right / Assume Wrong) is a tool for BOTH problem identification AND solution discovery.

---

## The Core Insight

The assume right / assume wrong structure naturally explores both sides:

| Branch | For Problems | For Solutions |
|--------|--------------|---------------|
| ASSUME RIGHT | "This IS the problem" → explore consequences | "This WOULD work" → explore how/why |
| ASSUME WRONG | "This ISN'T the real problem" → find alternatives | "This WON'T work" → find obstacles/alternatives |

---

## Problem Identification via ARAW

### Finding the Real Problem

**Seed**: "[Obvious problem statement]"

```
ASSUME RIGHT: This is the real problem
├── What are the consequences?
├── What solutions would address this?
└── Why does this problem exist?

ASSUME WRONG: This isn't the real problem
├── What else could explain the symptoms?
├── What's upstream of this symptom?
└── What assumption are we making that might be wrong?
```

The ASSUME WRONG branches reveal:
- Alternative framings
- Root causes vs symptoms
- Hidden assumptions
- Problems we're ignoring

### Finding the Right Level

**Seed**: "[Problem at current level]"

```
ASSUME RIGHT: This is the right level to solve
├── Solve here → what happens?
└── Is the fix permanent?

ASSUME WRONG: This isn't the right level
├── What's upstream? (more fundamental)
├── What's downstream? (why does it matter)
└── Is this a symptom of something else?
```

### Validating Problem Exists

**Seed**: "[Claimed problem]"

```
ASSUME RIGHT: This problem exists
├── What's the evidence?
├── Who experiences it?
└── What's the harm?

ASSUME WRONG: This problem doesn't exist
├── Why do we think it's a problem?
├── What would we see if it weren't a problem?
└── Is this preference vs problem?
```

If ASSUME WRONG branches are more compelling, the "problem" may be imagined.

---

## Solution Discovery via ARAW

### Finding Solutions

**Seed**: "[Proposed solution]"

```
ASSUME RIGHT: This solution works
├── How would it work?
├── What resources needed?
├── What would success look like?

ASSUME WRONG: This solution doesn't work
├── What could go wrong?
├── What are we missing?
├── What alternative would work?
```

The ASSUME WRONG branches reveal:
- Failure modes
- Missing prerequisites
- Better alternatives
- Hidden costs

### Finding the Right Solution

**Seed**: "[Problem to solve]" (explore solution space)

```
ASSUME RIGHT: We should solve this directly
├── Direct solutions → evaluate each
└── Which is highest leverage?

ASSUME WRONG: Direct solution is wrong approach
├── What indirect approaches exist?
├── Can we dissolve the problem instead of solving it?
├── Can we reframe to make the problem irrelevant?
```

---

## Integration with Problem Definition Gate

Before building a solution:

1. **Run ARAW on problem statement**
   - ASSUME WRONG branches test if it's the real problem
   - High-leverage ASSUME WRONG branches suggest reframing

2. **Check problem level**
   - Use ARAW to explore upstream/downstream
   - Find the level where solving actually fixes it

3. **Validate timing**
   - ASSUME RIGHT: solve now → consequences
   - ASSUME WRONG: don't solve now → what happens

4. **Explore solutions**
   - ASSUME RIGHT each candidate → how it works
   - ASSUME WRONG each candidate → why it fails

---

## Key Patterns

### Pattern: The Obvious Problem is Wrong

When ARAW run on "obvious problem" produces:
- Weak ASSUME RIGHT branches (solving it doesn't help much)
- Strong ASSUME WRONG branches (alternatives are more compelling)

→ The obvious problem is likely a symptom, not the real problem.

### Pattern: The Real Problem is Upstream

When ARAW branches keep pointing to causes of causes:
- "This happens because of X"
- "X happens because of Y"
- "Y happens because of Z"

→ Follow the chain. The real problem is often 2-3 levels up.

### Pattern: The Problem is an Assumption

When ARAW reveals branches like:
- "We assume this needs to be fast"
- "We assume users want X"
- "We assume this is our responsibility"

→ The "problem" may dissolve if the assumption is questioned.

### Pattern: Solution Space is Narrow

When ASSUME WRONG on proposed solution reveals:
- Same obstacles for every alternative
- No clear alternative that avoids the issues

→ The problem might be framed too narrowly. Expand the problem statement.

---

## Practical Usage

### Quick Problem Check (5 min)

1. State the problem in one sentence
2. Ask: "What if this ISN'T the real problem?"
3. Generate 2-3 alternative framings
4. Ask which framing has highest leverage
5. If different from original, reframe

### Deep Problem Analysis (via ARAW)

1. Seed ARAW with problem statement
2. Expand for 100+ nodes
3. Look at ASSUME WRONG branches - what alternatives emerged?
4. Look at highest-leverage nodes - where's the real problem?
5. Synthesize findings into revised problem statement

### Solution Validation (via ARAW)

1. Seed ARAW with proposed solution
2. Focus on ASSUME WRONG branches - what could go wrong?
3. If obstacles are fundamental, seek alternative
4. If obstacles are addressable, note as risks to mitigate

# GOSM Design Principles

## Core Principle: System Intelligence, Not Model Intelligence

The goal is to structure the system so well that the intelligence is IN THE SYSTEM, not in the model running it.

### The Transformation

```
Current state:  Intelligent model + weak system = good output
Target state:   Cheap model + intelligent system = good output
```

### Why This Works

**Intelligence helps when:**
- Search space is undefined
- Questions are ambiguous
- Inference is required
- Context must be inferred

**Intelligence doesn't help when:**
- Search space is well-defined
- Questions are clear and specific
- Just need to follow procedure
- Everything needed is explicit

The reason an intelligent model can't search better than a cheap one (in a well-designed system) is because:
- The search space is so well-defined
- What it asks is so clear

When clarity is maximized, model intelligence becomes irrelevant.

### GOSM's Job

Transform vague into specific:

```
Vague goal + undefined space + ambiguous questions
                    ↓
         (requires intelligence)
                    ↓
Clear goal + defined space + specific questions
                    ↓
         (just follow procedure)
```

### The Measure of Quality

**The measure of GOSM's quality = How much does it reduce the intelligence required?**

A perfectly designed procedure:
- Has a clear search space ("look at these 5 options")
- Asks specific questions ("which of these satisfies X?")
- Provides explicit criteria ("X means [definition]")
- Leaves nothing to inference

At that point, a cheap model is just a "procedure follower" - it doesn't need to be smart, it needs to be obedient.

### What This Means for Procedure Design

Good procedure design is NOT:
- Comprehensive coverage
- Sophisticated analysis
- Impressive complexity

Good procedure design IS:
- **Clarity that eliminates the need for intelligence**

The enemy is ambiguity, not simplicity.

---

## Analogies

| Domain | Novice + Good System = Expert Output |
|--------|--------------------------------------|
| Aviation | Checklist lets new pilot perform safely |
| Medicine | Protocol lets nurse make correct decisions |
| Computing | Algorithm lets simple CPU outperform human |
| Manufacturing | Assembly line lets unskilled worker produce quality |
| ARAW | Heuristics let simple rules do what needs judgment |

In all cases: **The intelligence is in the system design, not the executor.**

---

## Design Implications

### What Should NOT Require Model Intelligence

| Component | Should NOT require | Should be handled by |
|-----------|-------------------|---------------------|
| Search direction | Model "insight" | Procedure structure |
| Quality judgment | Model "taste" | Explicit criteria + heuristics |
| Next step selection | Model planning | State machine + guards |
| Verification | Model evaluation | ARAW rules + checks |
| Problem framing | Model understanding | Templates + typed inputs |

### Where Intelligent Models MIGHT Still Be Needed

- Actual code generation (but can we template this?)
- Novel long-term planning (but can we proceduralize this?)
- Edge cases the system doesn't cover (but can we reduce these?)

The design goal: Minimize this list.

### The Test

**Can a $0.001/call model produce output that's 90% as good as a $0.10/call model when using GOSM?**

- If yes → System is working
- If no → System needs more structure/clarity

---

## Implementation Strategies

### How to Make Cheap Models Sufficient

1. **Very explicit step-by-step** - No inference required
2. **Fill-in-the-blank templates** - No generation from scratch
3. **Multiple choice where possible** - Select, don't create
4. **Verification via pattern matching** - No judgment
5. **Decomposition into atomic operations** - No complex reasoning
6. **Explicit criteria for every decision** - No taste required
7. **Defined search spaces** - No exploration required
8. **Clear termination conditions** - No judgment about "enough"

### Signs the System Needs More Structure

- Cheap model produces significantly worse output
- Output quality depends on prompt phrasing
- Different runs produce very different results
- Model "creativity" determines success
- Ambiguous cases require judgment calls

### Signs the System Is Well-Designed

- Cheap and expensive models produce similar output
- Output quality is consistent across runs
- Procedure is easy to follow mechanically
- Success is determined by procedure compliance, not model capability
- A human could follow the same steps and get same result

---

## The Reframe: Search-Quality Amplifier

GOSM is not an "execution engine" - it's a **search-quality amplifier**.

Each procedure:
- Narrows down the search space
- Makes the right answer easier to find
- Reduces the intelligence needed to find it

If search quality is high enough:
- Discovery becomes easy (you find what matters)
- Action becomes obvious (you know what to do)

The bottleneck is not execution. The bottleneck is search quality.

**GOSM's purpose**: Make search so structured that finding the right answer requires minimal intelligence.

---

## Implications for Over-Reliance on Intelligent Models

Over-reliance on intelligent models during development is a **crutch**.

It's necessary while designing the system, but the goal is to eliminate the need for it.

If the system only works with intelligent models:
- The system isn't done
- More structure/clarity is needed
- Ambiguity remains

The intelligent model is scaffolding. The finished building shouldn't need it.

---

## Summary

1. **Goal**: System intelligence, not model intelligence
2. **Method**: Clarity that eliminates need for intelligence
3. **Test**: Cheap model produces good output
4. **Enemy**: Ambiguity, not simplicity
5. **Measure**: How much intelligence reduction does GOSM provide?
6. **Reframe**: GOSM is a search-quality amplifier, not an execution engine

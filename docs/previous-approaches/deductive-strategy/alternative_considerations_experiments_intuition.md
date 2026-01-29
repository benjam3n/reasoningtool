# Considerations: Experiments vs Analysis, Intuition vs Reasoning

Notes on when different approaches are appropriate. These are considerations for designing alternative systems, not part of the main analytical system.

---

## Experiments vs Analysis

Two approaches to uncertainty:

**Analysis approach:** Think hard → Develop plan → Commit → Execute

**Experimental approach:** Try something quickly → See what happens → Learn → Try again

### When Experiments Work Better

**Fast feedback:**
- Results in hours/days not months/years
- Clear signal of success/failure
- Can iterate rapidly

**Low cost of failure:**
- Mistakes don't burn significant resources
- Doesn't close off options
- Doesn't harm anyone
- Easy to reverse

**High uncertainty:**
- Analysis would be speculation
- No one knows (not just you)
- Need empirical evidence

**Empirical domains:**
- Truth determined by what happens, not reasoning
- Physical things, human responses, market reactions

### When Analysis Works Better

**High cost of failure:**
- Significant resources at stake
- Options close off
- Harm possible
- Hard to reverse

**Slow feedback:**
- Won't know for a long time if it worked
- Can't iterate quickly

**Logic can determine answer:**
- Mathematical/logical problems
- Deductive reasoning applies

**Irreversible decisions:**
- Commitments
- Announcements
- Destroyed resources

### Hybrid

Often best approach combines both:
1. Analyze enough to avoid obvious failures
2. Experiment to learn what analysis can't tell
3. Analyze results
4. Iterate

---

## Quick Intuition vs Systematic Analysis

### When Quick Intuition Works Better

**Low stakes:**
- Wrong answer easily corrected
- Consequences minor

**Time pressure:**
- Must decide NOW
- Analysis would take too long
- Speed essential

**Repeated familiar situations:**
- Have pattern recognition
- Situation similar to past
- Intuition calibrated

**Analysis wouldn't help:**
- Information not available
- Too much uncertainty
- Would be garbage in, garbage out

**Energy is constraint:**
- Exhausted
- Analysis quality would be poor anyway

### When Systematic Analysis Works Better

**High stakes (irreversible):**
- Long-term direction
- Major commitments
- Can't undo

**Novel situations:**
- Haven't faced before
- Pattern recognition might mislead

**Bias present:**
- Notice you WANT particular answer
- Need systematic check
- Need constraints to override desire

**Others depending on you:**
- Decision affects others significantly
- Owe them diligence
- Need to justify

---

## Implications For System Design

### A System That Handles Both

Rather than "skip the system" for quick decisions, the system should internally handle different modes:

**Assessment phase:**
- What are the stakes?
- How much time is available?
- How familiar is this situation?
- Is there a bias risk?

**Mode selection:**
- High stakes + time available → Full analysis
- Low stakes + time pressure → Quick pattern match
- High stakes + no time → Pre-established protocols
- Novel + high stakes → Must make time

**The system should be able to operate in different modes rather than being bypassed.**

### Experiments As Part Of System

Rather than "experiments vs the system," experiments should be a tool the system can deploy:

- When to run experiments (low cost, high uncertainty)
- How to design experiments (what would you learn)
- How to interpret results (avoiding false conclusions)
- When to stop experimenting (enough data, diminishing returns)

**The system should know when to experiment rather than always analyzing.**

### Intuition As Input

Rather than "trust intuition or trust analysis," intuition is data:

- What does intuition say about this?
- Has intuition been reliable in similar situations?
- Does intuition conflict with analysis?
- If conflict: investigate the conflict, don't just pick one

**The system should use intuition as input rather than ignoring it or blindly following it.**

---

## Design Principles

For any system (analytical, collective, hybrid, or otherwise):

1. **Match mode to situation** - Don't use heavy analysis for trivial decisions, don't use quick intuition for catastrophic ones

2. **Experiments are tools** - Part of the toolkit, deployed when appropriate

3. **Intuition is data** - Input to be evaluated, not ignored or blindly trusted

4. **Time is a constraint** - Factor into decisions, don't assume unlimited time

5. **Energy is a constraint** - Factor into what kind of processing is possible

6. **Stakes determine rigor** - High stakes warrant more rigor, low stakes warrant speed
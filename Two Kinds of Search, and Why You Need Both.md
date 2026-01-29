# Two Kinds of Search, and Why You Need Both

## The problem

When you think carefully about a decision, you're doing one of two things: exploring options or testing options. These feel similar from the inside, but they use different cognitive operations, have different failure modes, and have complementary blind spots that can't be fixed by doing more of the same.

Exploring options means expanding the space. What are all the ways this could go? What am I not considering? What category does this fall into, and what are the other members of that category? This is divergent thinking. It maps territory.

Testing options means narrowing the space. Is this claim true or false? What breaks if I assume it's wrong? What has to also be true for this to hold? This is convergent thinking. It validates or eliminates.

Most people, when they try to think carefully, default to one of these. Some people naturally explore — they generate lots of options but struggle to commit because everything seems worth considering. Other people naturally test — they're good at finding flaws but sometimes miss that the entire frame is wrong because they never explored alternatives to it.

The deeper problem is that each mode, done alone, has a blind spot that it cannot detect from within itself.

## The blind spots

**Convergent testing cannot discover new dimensions.** If you're testing the claim "we should hire candidate A," you might test it very thoroughly — what evidence supports this, what evidence contradicts it, what if the interview performance doesn't predict job performance, what if the recommender has misaligned incentives. But all of this testing happens within the dimensions you've already thought of. It cannot surface the possibility that you should be hiring for a different role entirely, or that the whole hiring approach is wrong, or that candidate C exists and is better than both A and B. Testing operates within a space. It cannot expand that space.

This is a structural limitation, not a matter of effort. You can test harder, test deeper, recurse on sub-claims — and still miss the thing you never thought to test because it wasn't in the space you were searching.

**Divergent exploration cannot validate truth.** If you're mapping all the ways a product launch could go — varying the timing, the audience, the pricing, the channels — you end up with a rich map of possibilities. But membership in a category doesn't tell you which members are true, which are viable, which will actually work. You can enumerate beautifully and still end up with a list of options where the best one and the worst one are sitting next to each other, undifferentiated.

This is also structural. Exploration finds things. It doesn't evaluate them. More exploration gives you more things to evaluate, not better evaluations.

## The philosophical grounding

These two operations correspond to different logical systems.

Testing operates on binary logic. Every claim resolves to true or false. The core operation is negation: "what if this is wrong?" This is Popperian falsification applied locally — you try to break things, and what survives is provisionally accepted. The search direction is vertical: you drill deeper into a specific claim until you hit bedrock or contradiction.

Exploration operates on something closer to type theory. Every claim is an instance of a broader category. The core operation is abstraction: "what is this an instance of?" You move up to the type, then enumerate other instances of that type. The search direction is horizontal: you expand across the space of possibilities within a dimension, then look for dimensions you haven't considered.

| | Testing (Binary) | Exploration (Type) |
|---|---|---|
| Core question | "Is this true?" | "What is this an instance of?" |
| Logic | 2-valued (true/false) | N-valued (multiple instances) |
| Direction | Vertical (depth) | Horizontal (breadth) |
| Strength | Finding problems | Finding possibilities |
| Weakness | Missing alternatives | Missing failures |
| Termination | Contradiction or convergence | Exhaustion of dimensions |
| Cognitive mode | Convergent | Divergent |

The key observation is that these are not just different strategies. They are different logics. They have formally different operations, different termination conditions, and — critically — different things they cannot see. Binary logic can partition any space into true and false, but it cannot extend the space. Type logic can extend any space by discovering new dimensions, but it cannot determine which members are valid.

## Why "just do both" doesn't work

The obvious response is: do both. Explore, then test. Or test, then explore. And this is better than doing only one. But the order matters, and a single pass of each still has problems.

If you explore first and then test, you get a thorough map followed by rigorous evaluation — but the testing phase might reveal that some validated options have edge cases that require re-exploring the space, and that re-exploration might not happen because you've already "done" the exploration step.

If you test first and then explore, you're testing within an incomplete space and then trying to expand — but the expansion is now anchored to whatever the testing phase found, rather than being truly open.

The issue is that one pass of each doesn't create feedback between the two modes. You need the testing to inform what to explore next, and the exploration to reveal what to test next.

## The alternating pattern

Alternation solves this:

1. **Explore** — Map the possibility space. What are all the candidates? Use systematic techniques to avoid only finding the obvious ones: vary parameters, reverse roles, change scale, shift to adjacent categories.

2. **Test** — Take the most promising candidates and rigorously test each one. For each candidate: what follows if it's right? What follows if it's wrong? Go deep enough on both sides to find at least one non-obvious thing.

3. **Explore again** — Now look at what survived testing. What are the edge cases? What boundary conditions exist? What did the testing phase reveal that wasn't in the original exploration? This second exploration is informed by the testing and usually finds things the first pass missed.

4. **Test again** — Validate the edge cases. Do they matter? Do they change the ranking of the original candidates? Final validation.

```
Explore (divergent) → candidates
    ↓
Test (convergent) → validated / rejected
    ↓
Explore (divergent, informed by testing) → edge cases
    ↓
Test (convergent, final) → what survived everything
```

The insight is that each phase feeds the next. Testing reveals which dimensions matter, which informs the second exploration. The second exploration finds cases the first missed, which informs the final testing. The two modes bootstrap each other.

## What this gets you

When this works, it produces something that neither mode alone can: conclusions that are both complete (within the explored dimensions) and validated (tested against both their own assumptions and their edge cases).

The novel part is the second exploration. By that point, you have tested candidates, so you know what survived and why. Exploring from that position — asking "where does this surviving option break?" — is a fundamentally different operation than exploring from scratch. It's targeted divergence, informed by prior convergence. The first exploration searches from ignorance. The second searches from knowledge of what survived and why, which opens dimensions that weren't visible before testing.

## An example

I was trying to find all integers n where n² + n + 1 is divisible by some target number — say 7. The naive approach is to test values: try n = 0, 1, 2, 3, ... and check. This is a heuristic. It works when the answer happens to appear in the range you search, and it gives you no information when it doesn't.

**First exploration** mapped the approaches: brute-force search, algebraic manipulation (solve n² + n + 1 ≡ 0 mod 7), completing the square, factoring, checking whether the discriminant is a quadratic residue. These are the methods available — some heuristic (try values), some structural (use properties of modular arithmetic).

**First testing** checked each approach. Brute force finds n = 2 and n = 4 work (mod 7), but can't tell me *why* or whether I've found all solutions. Completing the square transforms the problem: n² + n + 1 ≡ 0 becomes (2n + 1)² ≡ -3 mod 7, which asks whether -3 is a quadratic residue mod 7. Computing: -3 ≡ 4 mod 7, and 4 = 2², so yes. This structural approach finds both solutions and *proves* the list is complete — because quadratic residues are determined by the modulus, not by how many values you check.

**Second exploration** asked: what are the edge cases of the structural approach? What if the target isn't 7 but some other prime? The method works for any prime — but the answer depends on whether -3 is a quadratic residue mod p, which varies. For p = 5: -3 ≡ 2 mod 5, and 2 is not a quadratic residue mod 5, so there are *no* solutions. Brute force would have told me the same thing eventually, but only after checking all residues without knowing when to stop. The structural approach gives a definitive no.

**Second testing** validated this: the quadratic residue criterion is both necessary and sufficient. It resolves the problem completely for any prime, including the cases where no solutions exist — which is exactly where brute force fails most badly, because you can never finish searching.

Without the alternation, I would have either: (a) explored approaches but never tested whether brute force could prove completeness (it can't), or (b) jumped straight to testing values and never discovered that the problem has a structural solution that works for all primes at once.

## Limitations

This doesn't solve everything.

**Unknown unknowns remain.** Exploration guarantees completeness within known dimensions. But there are dimensions you don't know about. The second exploration mitigates this somewhat — by exploring from the tested position, you sometimes stumble into dimensions that weren't visible from the starting position — but it's not a guarantee.

**Effort scales linearly.** Each pass takes real time. For simple, reversible decisions, this is overkill. The approach is most valuable when the stakes are high enough to justify the effort and the situation is complex enough that surface-level analysis misses things.

**Quality depends on execution.** The exploration phase only works if you actually use systematic techniques rather than just brainstorming. The testing phase only works if you genuinely inhabit the "this is wrong" position rather than just checking the box. Both of these are skills that improve with practice, and both are easy to do badly while feeling like you're doing them well.

**The n+1 problem.** Any validation method can itself be questioned. Why trust this alternation pattern over some other approach? This is genuinely unresolvable in principle. The practical answer is convergence from multiple independent methods: if the conclusion survives grounding checks, self-application, independent derivation, and empirical testing, that's stronger evidence than any single method. But it's never certainty.

## Connection to existing ideas

This alternation pattern isn't entirely new. It's related to divergent/convergent thinking cycles in design thinking, to generate-and-test in AI search, to the explore-exploit tradeoff in reinforcement learning. What is novel is the specific framing in terms of different logics (binary vs. type theory) and the claim that the blind spots are structural — not just practical — which is why you need alternation rather than just "try harder at both."

The testing phase owes a lot to Popperian falsification and to the general idea that knowing about confirmation bias doesn't provide a mechanism for correcting it. You need a process that forces the operation, not just awareness that the operation should happen.

The exploration phase owes a lot to the rationalist tradition of asking "what is this an instance of?" and to morphological analysis (Fritz Zwicky), which varies parameters systematically to discover possibilities.

## Try it

If you want to test this yourself, pick a decision you're facing or a belief you hold.

1. Spend five minutes exploring the space. What category does this fall into? What are sibling options you haven't considered? What happens if you vary the parameters — timing, scale, audience, framing?

2. Pick the top 3-5 options and test each one. Take it as true: what follows? Take it as false: what follows? Push until something non-obvious shows up.

3. Look at what survived. Now explore the edge cases of the survivors. Where do they break? At what scale? Under what conditions?

4. Test the edge cases. Do they matter?

If the process surfaces something you wouldn't have found otherwise, it's working. If it doesn't, either the problem was simpler than it looked, or the passes didn't go deep enough.

I've open-sourced a toolkit that implements this pattern and 200+ related reasoning procedures as structured prompts for Claude Code: [reasoningtool](https://github.com/benjam3n/reasoningtool). The toolkit is the implementation; this post is the philosophy behind it.

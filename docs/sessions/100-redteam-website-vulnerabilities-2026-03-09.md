# /redteam Red-team the reasoningtool website — what would someone trying to dismiss it focus on?
**Date:** 2026-03-09
**Skill:** /redteam (Red Team)

---

## RED TEAM REPORT

```
TARGET: The reasoningtool.com website — its ability to persuade visitors that the project is credible, useful, and worth adopting
ADVERSARY PROFILES: 4 modeled
ATTACKS EXECUTED: 10
CRITICAL ATTACKS FOUND: 3
```

---

## Phase 1: RECONNAISSANCE

### Step 1: Map the Target

```
TARGET: The reasoningtool.com website as the public-facing case for a 563-skill reasoning toolkit for Claude Code
OBJECTIVE: Convince visitors the project is legitimate, intellectually serious, and worth installing
SUCCESS CRITERIA: Visitors understand what the project is, find it credible, and either install it or bookmark/share it
TIMELINE: Ongoing — every new visitor is a fresh evaluation
RESOURCES: A static Astro site with pages: skills index (homepage), about (essay), FAQ, installation, questions, where (timeline), visuals
STAKEHOLDERS: The creator (Ben), potential users, the AI/developer community, skeptics, and competitors
```

### Step 2: Assumption Inventory

```
ASSUMPTION INVENTORY:
  A1: Visitors will read the About essay carefully enough to follow the reasoning — TESTABLE: yes — TESTED: no — CONFIDENCE: low
  A2: The essay's philosophical style will be received as depth rather than obscurantism — TESTABLE: yes — TESTED: no — CONFIDENCE: low
  A3: 563 skills is perceived as "comprehensive" rather than "bloated" — TESTABLE: yes — TESTED: no — CONFIDENCE: medium
  A4: The skill cloud homepage communicates what the project IS to a first-time visitor — TESTABLE: yes — TESTED: no — CONFIDENCE: low
  A5: The FAQ adequately addresses visitor objections — TESTABLE: yes — TESTED: no — CONFIDENCE: low
  A6: Health supplement recommendations on the About page will not undermine credibility — TESTABLE: yes — TESTED: no — CONFIDENCE: low
  A7: The installation instructions are clear enough for non-technical visitors — TESTABLE: yes — TESTED: no — CONFIDENCE: medium
  A8: Visitors will not be put off by the project being Claude Code-specific — TESTABLE: yes — TESTED: no — CONFIDENCE: medium
  A9: The "Where" page (project timeline) is interesting rather than confusing to outsiders — TESTABLE: yes — TESTED: no — CONFIDENCE: low
  A10: The compressed prose style ("How method guess? Reason, analogy, expectation.") reads as intentional density rather than inability to write clearly — TESTABLE: yes — TESTED: no — CONFIDENCE: low
  A11: Visitors trust a solo developer's reasoning framework — TESTABLE: yes — TESTED: no — CONFIDENCE: medium
  A12: The lack of worked examples on the website is not a dealbreaker — TESTABLE: yes — TESTED: no — CONFIDENCE: low
  A13: "Assuming right / assuming wrong" as a core concept is self-explanatory — TESTABLE: yes — TESTED: no — CONFIDENCE: low
  A14: The site structure (skills homepage, separate about/faq/install pages) matches visitor navigation expectations — TESTABLE: yes — TESTED: no — CONFIDENCE: medium
```

**Explicit assumptions**: The project is useful, the skills work, the essay explains the intellectual foundation.
**Implicit assumptions**: Visitors will be patient, will not judge the project by first impressions alone, will engage with the philosophical framing rather than dismissing it.
**Environmental assumptions**: People searching for AI reasoning tools will find this site, the AI/Claude ecosystem continues growing.

**Finding A — Assumption vulnerability map**: 9 of 14 assumptions are LOW confidence and untested. The primary attack surface is the gap between what the creator intended to communicate and what a skeptical visitor actually perceives in their first 30-60 seconds.

### Step 3: Dependencies

The website's persuasive power depends on:
1. First impression (homepage) -> must communicate "what is this" within seconds
2. Credibility of the essay -> must survive scrutiny from people who know philosophy/epistemology
3. The FAQ -> must answer "why should I care" and "does this actually work"
4. Installation -> must be achievable without friction
5. Proof of value -> must exist somewhere on the site

**Single points of failure**: There is no "proof of value" page — no before/after examples, no user testimonials, no demo outputs. The entire persuasive burden falls on the essay and the skill count.

**Finding B — Critical path**: The thinnest part is the gap between "here are 563 skills" and "here is evidence they produce better outcomes." Nothing on the site bridges that gap. A skeptic can dismiss the entire project at this point without engaging further.

---

## Phase 2: ATTACK

### Step 4: Adversary Profiles

**Adversary 1 — The Dismissive Expert**
- MOTIVATION: Protect their own credibility; if a solo developer's prompt collection works, it undermines the value of their formal training
- CAPABILITY: Deep knowledge of epistemology, decision science, or AI; can identify when terminology is used loosely
- ATTACK VECTOR: Intellectual critique of the About essay; claim it is pseudo-philosophy
- LIKELY MOVE: Cherry-pick the weakest passages and use them to characterize the entire project

**Adversary 2 — The Pragmatic Developer**
- MOTIVATION: Wants tools that work, has no patience for theory without proof
- CAPABILITY: Can evaluate whether a tool actually improves output quality
- ATTACK VECTOR: "Show me it works" — demands evidence that is not present on the site
- LIKELY MOVE: Spend 20 seconds on the homepage, not understand what it does, leave

**Adversary 3 — The Social Media Critic**
- MOTIVATION: Engagement through takedowns; dunking on overconfident projects gets likes
- CAPABILITY: Can screenshot the most mockable parts and strip context
- ATTACK VECTOR: Screenshot the health supplement section, the compressed prose, or the "563 skills" count and frame it as absurd
- LIKELY MOVE: Post a thread with 3-4 screenshots and a caption like "this guy thinks he invented thinking"

**Adversary 4 — Murphy's Law (The Confused Visitor)**
- MOTIVATION: None — just entropy; represents the average person who lands on the site
- CAPABILITY: Average attention span, no context about Claude Code or reasoning frameworks
- ATTACK VECTOR: Misunderstanding — the site fails to explain itself before the visitor bounces
- LIKELY MOVE: See 563 cryptic abbreviations, have no idea what any of them do, close the tab

### Step 5: Execute Attacks

```
ATTACK 1: "The Essay Is Pseudo-Philosophy"
  ADVERSARY: The Dismissive Expert
  TARGET: Assumptions A2, A10, A13 — that the philosophical framing reads as depth
  MECHANISM: The About essay makes sweeping claims about intelligence, guessing, reason, and consciousness without citing any existing work. Passages like "Guessing means inferring what is true or not from what is true or not" and "Question > answer" and "How method guess? Reason, analogy, expectation" use a compressed, axiomatic style that a philosophy graduate would recognize as unfamiliar with existing literature. The expert quotes these, compares them to actual epistemology (Bayesian reasoning, Peirce's abduction, Popper's falsificationism), and shows the essay is reinventing existing concepts without acknowledging them.
  IMPACT: The project is framed as Dunning-Kruger epistemology — someone who thinks they discovered something that has existed for centuries. This characterization poisons every subsequent engagement.
  PROBABILITY: HIGH
  SEVERITY: SEVERE
  DETECTION: NO — the creator may never see the critique if it happens in a private Slack or group chat
  CURRENT DEFENSE: NONE — the essay does not cite or acknowledge any prior work
```

```
ATTACK 2: "563 Skills and Not One Example of Output"
  ADVERSARY: The Pragmatic Developer
  TARGET: Assumption A12 — that the lack of worked examples is not a dealbreaker
  MECHANISM: The visitor lands on the homepage. They see hundreds of skill chips. They click one — it shows the SKILL.md content (the procedure). They think: "OK, but what does this actually produce? What does an /araw output look like? How is it better than just asking Claude directly?" They search the entire site. No before/after comparisons. No sample outputs. No case studies. Nothing.
  IMPACT: The project looks like a collection of prompts that may or may not work, with no way to evaluate them without installing them. The cost of evaluation is too high relative to the demonstrated value.
  PROBABILITY: HIGH
  SEVERITY: FATAL
  DETECTION: YES — bounce rate data would show this
  CURRENT DEFENSE: NONE
```

```
ATTACK 3: "The Health Supplements Section Destroys All Credibility"
  ADVERSARY: The Social Media Critic
  TARGET: Assumption A6 — that health recommendations will not undermine credibility
  MECHANISM: Page 14 of the About essay recommends specific supplements including "100 mg TTFD," "vinpocetine," "creatine 15g," "freeze dried organs," "veal liver," and a "diet of straight sugar — orange juice, raw honey, raw milk." It then says 'I am not a doctor or anything, so "disregard" everything I just said' with scare quotes around "disregard." The critic screenshots this, posts it alongside the project's claims about superintelligence and reasoning, and writes: "The guy who claims to have solved reasoning also recommends a diet of straight sugar and raw milk. The scare quotes around 'disregard' tell you everything."
  IMPACT: This becomes the defining impression of the project for everyone who sees the screenshot. The reasoning framework becomes "the raw milk reasoning tool." No amount of legitimate intellectual work survives this association.
  PROBABILITY: HIGH
  SEVERITY: FATAL
  DETECTION: LATE — by the time you see it, the framing is already set
  CURRENT DEFENSE: WEAK — the "disregard" disclaimer is in scare quotes, which reads as not actually disclaiming anything
```

```
ATTACK 4: "The Homepage Explains Nothing"
  ADVERSARY: Murphy's Law (The Confused Visitor)
  TARGET: Assumption A4 — that the skill cloud communicates what the project is
  MECHANISM: A visitor arrives at reasoningtool.com. They see: a search bar, sort buttons (Alphabetical, Cool, Technical, Generality...), tier filters, and hundreds of abbreviated skill names like "se," "aex," "cmp," "ht," "dcp." There is no headline. No tagline. No "What is this?" paragraph. No elevator pitch. The visitor must click through to the About page and read a multi-page philosophical essay to understand what this project even is.
  IMPACT: Most visitors bounce within 10 seconds. The project never gets a chance to make its case.
  PROBABILITY: HIGH
  SEVERITY: SEVERE
  DETECTION: YES — analytics would show this
  CURRENT DEFENSE: NONE — the homepage has zero explanatory text
```

```
ATTACK 5: "The FAQ Is Useless"
  ADVERSARY: The Pragmatic Developer
  TARGET: Assumption A5 — that the FAQ addresses objections
  MECHANISM: The FAQ has exactly three questions. "How do I use a skill?" — Answer: "Skills can be used with /[skill name]." "Does it load all 367 skills into context at once?" — Answer: "No." "Is there anything this system shouldn't be used for?" — Answer: "Yes." followed by links to GitHub docs. The skill count (367) does not even match the current count (563). A skeptic reads this FAQ and concludes: the creator either does not take communication seriously or does not understand what visitors need to know.
  IMPACT: The FAQ actively harms credibility rather than building it. It signals that the creator prioritized building over explaining.
  PROBABILITY: HIGH
  SEVERITY: MODERATE
  DETECTION: YES
  CURRENT DEFENSE: NONE
```

```
ATTACK 6: "This Is Just Fancy Prompt Engineering"
  ADVERSARY: The Dismissive Expert
  TARGET: Assumption A11 — that visitors trust a solo developer's reasoning framework
  MECHANISM: The expert points out that every "skill" is a markdown file that tells Claude what to do. This is prompt engineering with a directory structure. The framing as a "reasoning toolkit" with "563 skills" and a philosophical treatise about superintelligence vastly oversells what is, technically, a prompt library. The gap between the grandiose framing ("superintelligence," "the solution") and the mundane reality (markdown files) is the attack vector.
  IMPACT: The project is reframed as pretentious prompt engineering. "It's a bunch of system prompts in a folder" becomes the one-line summary that sticks.
  PROBABILITY: HIGH
  SEVERITY: SEVERE
  DETECTION: NO
  CURRENT DEFENSE: WEAK — the installation page shows it is just `cp -r skills your-project/`, which confirms the attack
```

```
ATTACK 7: "The Compressed Prose Is Incoherent"
  ADVERSARY: The Social Media Critic
  TARGET: Assumption A10 — compressed prose reads as intentional density
  MECHANISM: Passages from the About essay like "How evaluate claim hard?" and "Question direction vector, answer scalar. Question multidimensional, answer one-dimensional" and "What learn?" and "How method guess?" are excerpted. Without the surrounding context, they read as broken English or AI-generated slop. The critic posts them with "this is the reasoning quality you get from the Reasoning Tool."
  IMPACT: The prose style becomes evidence against the project's own competence claim.
  PROBABILITY: MEDIUM
  SEVERITY: SEVERE
  DETECTION: NO
  CURRENT DEFENSE: NONE
```

```
ATTACK 8: "Claude-Code-Only Lock-In"
  ADVERSARY: The Pragmatic Developer
  TARGET: Assumption A8 — visitors will not be put off by Claude Code specificity
  MECHANISM: The toolkit only works with Claude Code (and now Codex). A developer using ChatGPT, Cursor, Windsurf, or any other AI tool cannot use it. The website does not address this limitation upfront. By the time someone realizes this, they feel their time was wasted.
  IMPACT: The addressable audience is narrowed to Claude Code users only. Everyone else bounces with mild irritation.
  PROBABILITY: MEDIUM
  SEVERITY: MODERATE
  DETECTION: YES
  CURRENT DEFENSE: WEAK — installation page shows Claude-specific commands but never states the limitation explicitly
```

```
ATTACK 9: "The Personal Branding Undermines the Tool"
  ADVERSARY: The Social Media Critic
  TARGET: Environmental assumption — that personal content belongs on a tool's website
  MECHANISM: Page 14 includes a Spotify playlist, TikTok and Twitter links, supplement recommendations, and a section titled "What type of music do I like to listen to?" This is personal blog content mixed into what claims to be a reasoning/intelligence tool. The critic argues this mixing signals the project is more about the creator's personal brand than about building a genuinely useful tool.
  IMPACT: Visitors who came for a reasoning tool feel they wandered into someone's personal homepage. Trust drops.
  PROBABILITY: MEDIUM
  SEVERITY: MODERATE
  DETECTION: YES
  CURRENT DEFENSE: NONE
```

```
ATTACK 10: "No Evidence It Outperforms Vanilla Claude"
  ADVERSARY: The Dismissive Expert
  TARGET: Core thesis — that structured skills improve reasoning
  MECHANISM: The expert asks the kill question: "Where is the A/B test? Show me the same prompt run through vanilla Claude and through /araw, and demonstrate the difference." The website makes no comparative claims backed by evidence. The entire value proposition rests on the assertion that structured reasoning helps, without demonstrating it.
  IMPACT: The project's central claim — that it makes AI reasoning better — is unfalsifiable as presented. An unfalsifiable claim from an uncredentialed source is trivially dismissed.
  PROBABILITY: HIGH
  SEVERITY: FATAL
  DETECTION: NO
  CURRENT DEFENSE: NONE
```

**Finding C — Attack priority matrix:**

| Priority | Attacks |
|----------|---------|
| CRITICAL | Attack 2 (no output examples), Attack 3 (supplements section), Attack 10 (no comparative evidence) |
| HIGH | Attack 1 (pseudo-philosophy), Attack 4 (homepage explains nothing), Attack 6 (just prompt engineering), Attack 7 (incoherent prose) |
| MEDIUM | Attack 5 (useless FAQ), Attack 8 (Claude-only), Attack 9 (personal branding) |
| LOW | (none) |

### Step 6: Cascade Analysis

```
CASCADE 1: "No Output Examples" (Attack 2)
  TRIGGER: Visitor asks "what does this produce?" and finds no answer
  -> IMMEDIATE EFFECT: Visitor cannot evaluate whether the tool is worth installing
  -> SECOND-ORDER: Visitor assumes the creator is hiding output quality because it is not impressive
  -> THIRD-ORDER: Visitor tells others "it's all theory, no results" — this becomes the consensus view
  -> TERMINAL STATE: The project is categorized as vaporware-adjacent — lots of structure, no demonstrated value. No amount of adding more skills changes this perception because the fundamental "show me" question was never answered.
  CIRCUIT BREAKER: Add 3-5 compelling before/after examples to the homepage. Show a real question, vanilla Claude's answer, and the /araw or /uaua output side by side. Let the output speak.
```

```
CASCADE 2: "Supplements Section Goes Viral" (Attack 3)
  TRIGGER: Someone screenshots page 14 of the About essay
  -> IMMEDIATE EFFECT: The screenshot circulates with mocking commentary
  -> SECOND-ORDER: People who have never visited the site form their first impression from the screenshot. "Raw milk reasoning tool" becomes a meme.
  -> THIRD-ORDER: Anyone who later recommends the tool gets pushback: "isn't that the raw milk guy?" The creator's credibility is permanently tagged.
  -> TERMINAL STATE: The project cannot escape the association. Even if the supplements section is removed, cached screenshots and social media posts persist. The intellectual work becomes inaccessible because the social proof has been poisoned.
  CIRCUIT BREAKER: Remove the supplements section from the About page entirely. Personal health opinions do not belong on a reasoning tool's website. If the creator wants to share personal views, put them on a personal blog at a different URL.
```

```
CASCADE 3: "No Comparative Evidence" (Attack 10)
  TRIGGER: An expert or journalist asks "does this actually work better?"
  -> IMMEDIATE EFFECT: The creator cannot point to any data, benchmark, or comparison
  -> SECOND-ORDER: The project is classified as "claims without evidence" — exactly the kind of reasoning failure the project claims to fix. This irony becomes the narrative.
  -> THIRD-ORDER: The irony narrative ("the reasoning tool that doesn't reason about its own claims") makes the project a cautionary example rather than a tool recommendation.
  -> TERMINAL STATE: The project is used as an example of the Dunning-Kruger effect in AI tooling discussions. Every mention reinforces the negative frame.
  CIRCUIT BREAKER: Run 10-20 comparative tests. Document them publicly. Show that structured skills produce measurably different (and better) outputs. Even qualitative comparisons with commentary help. The bar is not peer review — it is "I can see this is different and better."
```

**Finding D — Cascade depth**: All three critical cascades reach 4 orders deep and terminate in reputational states that are self-reinforcing and difficult to reverse. The common pattern: absence of evidence is interpreted as evidence of absence, which becomes the permanent narrative.

---

## Phase 3: REPAIR

### Step 7: Defense Design

```
DEFENSE 1: Add Output Examples
  AGAINST ATTACK: 2 (no output examples), 10 (no comparative evidence)
  DEFENSE TYPE: PREVENT
  MECHANISM: Create a prominent "Examples" or "See It Work" page. Include 3-5 real comparisons:
    - A claim tested with vanilla Claude vs. /araw
    - A decision analyzed with /decide vs. a plain prompt
    - A diagnostic question handled with /uaua vs. straight asking
    Show the full output, not cherry-picked excerpts. Let visitors judge for themselves.
  COST: 4-8 hours to generate and format examples
  RESIDUAL RISK: Cherry-picking accusations — mitigate by including at least one example where the difference is modest
```

```
DEFENSE 2: Remove or Relocate the Supplements Section
  AGAINST ATTACK: 3 (supplements destroy credibility)
  DEFENSE TYPE: PREVENT
  MECHANISM: Remove page 14's health supplement recommendations, the Spotify playlist, and the social media links from the About page. If the creator wants a personal section, create a separate "/ben" or "/personal" page that is not linked from the main navigation. The About page should contain only the intellectual case for the project.
  COST: 30 minutes
  RESIDUAL RISK: The content already exists in git history and may have been cached/screenshotted. But removing it prevents future discovery.
```

```
DEFENSE 3: Add a Homepage Headline and Elevator Pitch
  AGAINST ATTACK: 4 (homepage explains nothing), 8 (Claude-only unclear)
  DEFENSE TYPE: PREVENT
  MECHANISM: Add a 2-3 sentence description at the top of the homepage before the skill cloud:
    "563 structured reasoning skills for Claude Code. Each skill is a procedure that guides Claude through assumption testing, space exploration, decision analysis, and more. Type /skillname to run any skill."
    State platform compatibility upfront: "Works with Claude Code and Codex."
  COST: 30 minutes
  RESIDUAL RISK: The skill cloud is still overwhelming. Consider adding a "Start here" section that highlights 5-6 entry-point skills.
```

```
DEFENSE 4: Rewrite the FAQ
  AGAINST ATTACK: 5 (useless FAQ)
  DEFENSE TYPE: PREVENT
  MECHANISM: Expand to 8-12 questions including:
    - "What is this?" (elevator pitch)
    - "How is this different from just asking Claude?" (the core value prop)
    - "Does this actually work better?" (link to examples page)
    - "Why so many skills?" (explanation of the taxonomy)
    - "Can I use this with ChatGPT/other tools?" (honest platform answer)
    - "Who made this?" (brief credibility-building bio)
    Fix the skill count from 367 to the current number.
  COST: 2-3 hours
  RESIDUAL RISK: FAQ still may not be read. But it defends against the "they didn't even try to explain" critique.
```

```
DEFENSE 5: Acknowledge Prior Work in the Essay
  AGAINST ATTACK: 1 (pseudo-philosophy), 6 (just prompt engineering)
  DEFENSE TYPE: MITIGATE
  MECHANISM: Add a brief section to the About essay that situates the work relative to existing frameworks: "The assume-right/assume-wrong process is related to Bayesian updating, Hegelian dialectic, and steel-manning/weakmanning. The exploration-testing alternation connects to the explore-exploit tradeoff in reinforcement learning." This does not require academic citations — just honest acknowledgment that these ideas have predecessors.
  COST: 1-2 hours
  RESIDUAL RISK: Experts may still find the treatment superficial. But "reinvents the wheel without knowing it" becomes "applies existing ideas in a new context," which is defensible.
```

```
DEFENSE 6: Address the Compressed Prose
  AGAINST ATTACK: 7 (incoherent prose)
  DEFENSE TYPE: MITIGATE
  MECHANISM: Either (a) rewrite the most compressed sections in standard prose, or (b) add a note at the beginning of the essay: "This essay uses compressed notation in places — telegraphic phrasing where the pattern matters more than the polish." Option (a) is stronger.
  COST: 2-4 hours for rewrites
  RESIDUAL RISK: The style is part of the creator's voice. Rewriting everything may lose something. A middle path: keep the compressed style for the "foundations" section but make the opening pages and practical sections fully clear.
```

### Step 8: Hardened Version

```
HARDENED TARGET:
  ORIGINAL: A website that showcases 563 reasoning skills through a skill cloud, a philosophical essay, and installation instructions.

  MODIFICATIONS:
    1. Add homepage headline + elevator pitch — ADDRESSES: Attack 4, Attack 8
    2. Create "Examples" page with 3-5 before/after comparisons — ADDRESSES: Attack 2, Attack 10
    3. Remove supplements, playlist, and social links from About page — ADDRESSES: Attack 3, Attack 9
    4. Rewrite FAQ with 8-12 substantive questions — ADDRESSES: Attack 5
    5. Add "prior work" acknowledgment paragraph to essay — ADDRESSES: Attack 1, Attack 6
    6. Rewrite most compressed prose sections in standard English — ADDRESSES: Attack 7
    7. Fix stale skill count in FAQ (367 -> current) — ADDRESSES: Attack 5

  ACCEPTED RISKS:
    1. "Just prompt engineering" framing (Attack 6) — cannot be fully prevented because it is technically accurate. CONTINGENCY: Let the output quality speak for itself via the examples page. Prompt engineering that produces measurably better output is valuable regardless of what you call it.
    2. Claude-only lock-in (Attack 8) — cannot be changed without porting the project. CONTINGENCY: State the limitation honestly and frame it as a starting point: "Currently for Claude Code and Codex. Cross-platform support is on the roadmap."

  REMAINING VULNERABILITIES:
    1. Solo developer credibility — cannot be addressed without external validation (user testimonials, community adoption, third-party reviews). This resolves with time and traction, not website changes.
    2. The essay's philosophical ambition may always alienate some readers — this is an acceptable trade-off if the essay also resonates with others. The key fix is ensuring the essay is not the ONLY path to understanding the project.
    3. No formal benchmarks — running proper A/B tests takes significant time and may not be feasible for a solo developer. Qualitative examples are the realistic defense.
```

**Finding E — Hardening delta**: Approximately 40-50% of the website's persuasive surface needs modification. The original is not bad in substance — the skills themselves appear thoughtful and the underlying ideas have merit. The vulnerability is almost entirely in presentation: the site does not explain itself, does not demonstrate value, and includes credibility-damaging personal content. These are fixable.

---

## FINDINGS SUMMARY

```
A — Assumption vulnerability: 9 of 14 assumptions are low-confidence and untested
B — Critical path: No evidence of output quality anywhere on the site
C — Attack priority: 3 CRITICAL / 4 HIGH / 3 MEDIUM / 0 LOW
D — Cascade depth: All 3 critical cascades reach 4 orders, terminating in self-reinforcing reputational damage
E — Hardening delta: ~45% of persuasive surface needs modification

TOP 3 KILL SHOTS:
1. There is not a single example of what any skill actually produces — the entire value proposition is asserted, never demonstrated.
2. The health supplements section (raw milk, straight sugar diet, specific supplement dosages with scare-quoted "disregard") is a credibility-destroying screenshot waiting to happen.
3. The homepage is a wall of cryptic abbreviations with zero explanatory text — most visitors will never learn what the project is.

DEFENSES DESIGNED: 6 | ACCEPTED RISKS: 2 | REMAINING VULNERABILITIES: 3
```

### Priority-Ordered Fix List

| Priority | Fix | Effort | Addresses |
|----------|-----|--------|-----------|
| 1 | Remove supplements/personal content from About page | 30 min | Kill shot #2 |
| 2 | Add homepage headline + elevator pitch | 30 min | Kill shot #3 |
| 3 | Create examples page with before/after comparisons | 4-8 hours | Kill shot #1 |
| 4 | Rewrite FAQ with substantive questions + fix skill count | 2-3 hours | Attacks 5, 8 |
| 5 | Add prior work acknowledgment to essay | 1-2 hours | Attacks 1, 6 |
| 6 | Rewrite compressed prose sections | 2-4 hours | Attack 7 |

Fixes 1 and 2 are under an hour combined and eliminate the two most exploitable vulnerabilities. Fix 3 is the most important single investment because it transforms the project from "claims" to "evidence."

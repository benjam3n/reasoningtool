# /anag Explain reasoningtool using the analogy of a workshop full of specialized hand tools vs a Swiss Army knife
**Date:** 2026-03-09
**Skill:** /anag (Analogy Generation)

---

## Step 1: Identify the Source Concept

What needs to be explained through analogy?

```
SOURCE CONCEPT: reasoningtool — a collection of 592 structured thinking skills implemented as
Claude Code plugin slash commands, each a markdown procedure that guides analysis in a specific way.

KEY PROPERTIES:
1. Large number of specialized procedures — each skill does one kind of thinking well
2. Skills are independently invocable — you pick the right one for the job
3. Skills chain into each other — one procedure can invoke another mid-execution
4. Category routers exist — meta-skills that classify your problem and route to the right tool
5. Each skill has structured steps — not freeform, but a defined sequence that produces a defined output

AUDIENCE: Developers, thinkers, and AI users who understand what Claude Code is and want to
understand why you'd want 592 separate thinking procedures instead of just asking an LLM to
"think hard."
```

---

## Step 2: Find a Target Domain

```
CANDIDATES:
1. A workshop full of specialized hand tools vs. a Swiss Army knife
   — matches on: specialization, selection, right-tool-for-the-job, tool chaining (using a
   drill then a chisel then sandpaper in sequence)

2. A hospital with specialist departments vs. a general practitioner
   — matches on: routing (triage), specialization, referral chains, depth of expertise

3. A professional kitchen with dedicated stations vs. a home kitchen multi-tool
   — matches on: station-based workflow, specialized equipment, mise en place structure

BEST FIT: Candidate 1 — Workshop vs. Swiss Army knife. It's the analogy the user requested,
and it maps cleanly. The audience already has strong intuitions about why a carpenter doesn't
build a house with a Swiss Army knife. The physicality makes abstract "thinking procedures"
concrete.
```

---

## Step 3: Map the Correspondence

```
MAPPING:
| Source (reasoningtool)                        | Target (workshop)                                | Relationship preserved                                                   |
|-----------------------------------------------|--------------------------------------------------|--------------------------------------------------------------------------|
| The full collection of 592 skills             | A well-stocked professional workshop             | A large organized set of specialized instruments                         |
| A single skill (e.g., /rca, /cba, /anag)     | A specific hand tool (chisel, plane, calipers)   | Each one does one job with precision and consistency                     |
| The structured steps inside a skill           | The designed shape/geometry of a tool             | Structure constrains use toward correct technique                        |
| Category routers (/claim, /decide, /diagnose) | The tool board organized by function              | A finding/selection layer that routes you to the right instrument        |
| Skill chaining (→ INVOKE)                     | Using tools in sequence (drill, then dowel jig)  | Complex work requires multiple specialized tools applied in order        |
| Claude without reasoningtool                  | A Swiss Army knife                               | Can do many things passably; none of them with depth or precision        |
| Skill output format (structured markdown)     | A tool's jig or guide fence                       | Forces consistent, repeatable results regardless of user skill level     |
| Choosing the wrong skill                      | Using a screwdriver as a chisel                   | The tool "works" but the result is poor and the tool is misused          |
| The /meta and /wsib discovery skills          | Asking the shop foreman "what should I use here?" | A human-routing layer when you don't know the catalog                    |
```

---

## Step 4: Build the Analogy

```
ANALOGY:

Imagine you need to build a cabinet. You could pull out a Swiss Army knife — it has a blade,
a saw, a file, a screwdriver. Technically, you could cut wood with that little saw. You could
drive screws with that stubby screwdriver. You'd get something that vaguely resembles a cabinet.
But it would take forever, the cuts would be rough, and the joints would be sloppy. The Swiss
Army knife is decent at many things but excellent at nothing.

Now imagine walking into a fully stocked professional workshop. There's a table saw for straight
cuts, a router for joinery, a set of chisels for fine work, calipers for measurement, clamps
for assembly. Each tool was designed to do exactly one thing with precision. The table saw
doesn't try to also be a sander. The chisel doesn't pretend to measure.

That's the difference between asking a bare LLM to "analyze this" versus using reasoningtool.

A bare LLM is the Swiss Army knife. It can attempt any thinking task — compare options, find
root causes, test assumptions, generate analogies — but it freestyles every time. There's no
consistent technique. The depth depends on the day. You get a different shaped output every run.

reasoningtool is the workshop. Its 592 skills are 592 specialized hand tools. /rca is a
dedicated root cause analysis procedure — it forces you through fault trees and causal chains
the way a mortising jig forces a chisel to cut square. /cba is a cost-benefit framework that
produces structured tradeoff tables the way a marking gauge produces consistent scribe lines.
/anag (the skill producing this very output) is a tool for building analogies — it maps
structure, tests where the metaphor breaks, and packages the result cleanly.

The category routers — /claim, /decide, /diagnose — are like the labeled sections of the tool
board. You walk in knowing you have "a decision to make" but not sure which tool to grab.
The router inspects the problem and hands you the right instrument: "This needs /dcp for a
decision checkpoint, then chain into /cba for the cost-benefit layer."

And just like real woodworking, complex jobs require multiple tools in sequence. You don't just
use the table saw — you saw, then plane, then chisel, then sand. In reasoningtool, skills
chain: one skill can invoke another mid-procedure. An analysis might start with /rca to find
the root cause, then invoke /poa to explore solution paths, then invoke /dcp to decide which
path to take. Each tool in the chain does its one job and hands off to the next.

The structured steps inside each skill are the equivalent of a tool's physical design. A chisel's
bevel angle isn't decorative — it determines how the tool cuts. Similarly, the steps in a skill
aren't suggestions — they're a defined sequence that constrains the LLM's reasoning into a
proven shape. This means you get repeatable, consistent output rather than whatever the model
happens to generate freeform.
```

---

## Step 5: Test the Limits

```
WHERE IT BREAKS:
1. Physical tools are passive; skills are active processes. A chisel sits there until you pick
   it up. A reasoning skill actively guides the LLM through steps — it's more like a chisel
   attached to a jig attached to a workbench that moves your hands. The skills have agency in
   shaping the process that physical tools don't.

2. You can see all your physical tools at once. You can't easily browse 592 skills. The workshop
   analogy implies visual/spatial organization that the skill library doesn't fully have. Discovery
   is harder — hence the need for /meta and /wsib routing skills, which have no clean workshop
   equivalent (a foreman, maybe, but foremen are people, not tools).

3. Physical tools don't chain automatically. You finish with the saw and manually pick up the
   chisel. In reasoningtool, chaining is built in — one skill invokes the next without the user
   re-selecting. This is more like a CNC machine sequence than a hand-tool workshop.

4. A Swiss Army knife has fixed, limited tools. An LLM without structured skills isn't limited
   in scope — it can attempt anything. The failure mode isn't "can't do it" but "does it
   inconsistently and shallowly." The Swiss Army knife analogy slightly overstates the limitation
   of the bare LLM.

5. Workshop tools require physical skill to use well. Reasoning skills reduce the skill
   requirement — the structure does the heavy lifting. A novice with /rca gets closer to expert
   root-cause analysis than a novice with a chisel gets to expert joinery.

CAVEATS TO INCLUDE:
- The analogy overstates passivity: these skills actively guide thinking, more like powered
  jigs than inert hand tools.
- The discovery problem is real: 592 tools only help if you can find the right one. The
  workshop metaphor makes this look easier than it is.

MISLEADING IMPLICATIONS:
- Someone might conclude you need to master each skill the way you'd master each hand tool.
  You don't — the skills carry their own instructions.
- Someone might think the Swiss Army knife (bare LLM) is strictly worse. It's not — for quick,
  low-stakes, exploratory tasks, the flexibility of an unstructured response is genuinely useful.
  You don't bring a table saw to open a letter.
```

---

## Step 6: Final Output

```
FINAL ANALOGY:

A bare LLM is a Swiss Army knife. It can attempt any thinking task — analyze, compare, decide,
diagnose — but it freestyles every time. No consistent technique. Depth varies by the day.
You get a different shaped output every run.

reasoningtool is a professional workshop with 592 specialized hand tools. /rca is a root cause
analysis jig that forces you through fault trees. /cba is a marking gauge that scores clean
cost-benefit lines. /anag is a template for building analogies by mapping structure.

Category routers (/claim, /decide, /diagnose) are the labeled tool board — you walk in with a
problem type and they hand you the right instrument. Skill chaining is the natural sequence of
a real build: saw, then plane, then chisel, then sand — each tool does its job and hands off
to the next.

The structured steps inside each skill are the tool geometry itself — the bevel angle on the
chisel, the fence on the router. They constrain the work toward a correct result. This is why
a novice using reasoningtool gets more consistent analysis than an expert freestyling: the
structure does the heavy lifting.

You wouldn't build a cabinet with a Swiss Army knife. You wouldn't do serious analytical work
with "hey Claude, think about this." You'd walk into the workshop and pick up the right tool.

NOTE: This analogy breaks on passivity. Physical tools sit inert until wielded — reasoning
skills actively guide the process, more like a powered jig that moves your hands than a chisel
waiting to be picked up. It also makes discovery look easy: seeing 592 tools on a wall is
intuitive, but finding the right skill from 592 markdown files requires its own routing layer
(/meta, /wsib) — the workshop's foreman, not another hand tool. Finally, the Swiss Army knife
comparison slightly overstates the bare LLM's limitation: for quick, low-stakes exploration,
freeform reasoning is genuinely useful. You don't bring a table saw to open a letter.
```

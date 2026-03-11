# /ans What solved problem in another domain is structurally similar to "helping people think more clearly"?
**Date:** 2026-03-09
**Skill:** /ans (Analogy Search)

---

## Step 1: Describe the Problem

**Situation:** People face thinking tasks (decisions, diagnoses, evaluations, creative challenges) but lack the procedures experts use to handle them well. They default to intuition, rumination, or shallow heuristics.

**What's wrong:** Expert-level thinking processes are locked inside expert heads. Non-experts don't know what steps to take, what questions to ask, or what order to work in. The result: poor decisions, missed considerations, shallow analysis.

**What's needed:** A system that makes expert thinking procedures accessible and executable by non-experts. The system should work across many thinking task types, guide users step-by-step, and produce reliably better outputs than unstructured thinking.

**Concrete problem description:** How do you take implicit expert procedures, codify them into reusable structures, and deliver them at the moment of need so that non-experts can produce expert-quality cognitive work?

---

## Step 2: Extract Problem Structure

**Core challenge:** Knowledge transfer and procedural accessibility -- making expert processes usable by non-experts without requiring the expertise.

**Inputs:** A person with a task, limited expertise in the task's cognitive demands, and some context about their situation.

**Outputs:** A structured walkthrough that guides them to a better result than they'd reach alone.

**Constraints:**
- Users don't know what they don't know (they can't select the right procedure without help)
- Procedures must work across wildly different content domains
- The system must route to the right procedure (classification problem)
- Procedures must be followable without training
- Quality must be consistently better than the unstructured alternative

**What makes it hard:**
- Expert knowledge is tacit and resists codification
- Different situations require different procedures
- Users need to be routed correctly before they can benefit
- The procedures themselves must be learnable without a teacher present

**Abstract structure:** *A library of codified expert procedures with a routing/classification layer, designed to make specialized process knowledge accessible to generalists at the point of need.*

---

## Step 3: Search Domains Systematically

### Medicine: Clinical Practice Guidelines (CPGs)
**Similar problem:** Doctors face thousands of conditions. No one can hold all best-practice treatment protocols in their head. How do you ensure a general practitioner delivers specialist-quality care?

**How they solve it:** Clinical practice guidelines -- step-by-step decision trees codified from specialist consensus and research evidence. Symptom-based routing (differential diagnosis) selects the right guideline. Tools like UpToDate and DynaMed deliver them at point of care.

### Software Engineering: Design Patterns
**Similar problem:** Programmers face recurring architectural problems. Junior developers don't recognize the patterns or know the standard solutions.

**How they solve it:** The Gang of Four catalogued 23 design patterns -- named, structured solutions to recurring design problems. Each pattern has: problem description, when to apply it, the solution structure, and consequences. Developers learn to recognize problem shapes and reach for the matching pattern.

### Cooking: Recipes and Technique Libraries
**Similar problem:** Home cooks want restaurant-quality results but lack the tacit knowledge of trained chefs.

**How they solve it:** Recipes codify procedures. But the deeper solution was technique-based cooking education (Julia Child, Serious Eats, Kenji Lopez-Alt) -- teaching the *why* behind steps so cooks can adapt. Cookbooks evolved from "ingredient lists" to "procedure + explanation" format.

### Law: Legal Templates and Self-Help Legal Tools
**Similar problem:** People face legal situations (contracts, disputes, filings) but can't afford lawyers for every interaction. Legal reasoning is expert-intensive.

**How they solve it:** Standardized legal templates, guided questionnaires (LegalZoom, Rocket Lawyer), and decision-tree-based self-help tools. The user answers questions, the system routes to the right template, fills in specifics. Court self-help centers use flowcharts to guide pro se litigants.

### Aviation: Checklists and Standard Operating Procedures
**Similar problem:** Pilots face complex, high-stakes situations where forgetting a step can be fatal. Even experts make errors under pressure.

**How they solve it:** Checklists and SOPs for every phase of flight and every emergency. The key innovation: procedures are *externalized* from memory into physical artifacts. Atul Gawande's "The Checklist Manifesto" documented how this transferred to surgery with dramatic results.

### Manufacturing: Standard Work and Toyota Production System
**Similar problem:** Factory workers need to produce consistent quality. Expert craftsmen can't scale.

**How they solve it:** Standard work instructions -- detailed, step-by-step procedures posted at each workstation. The procedure IS the product quality. Toyota's insight: the procedure should be improvable by the worker (kaizen), creating a living system.

### Music: Method Books and Pedagogical Systems
**Similar problem:** Musical skill is deeply tacit. How do you teach technique without a master present?

**How they solve it:** Progressive method books (Suzuki, Hanon, Czerny) that break complex skills into ordered exercises. Each exercise isolates one sub-skill. The sequence is the pedagogy. Routing is built into progressive difficulty.

### Emergency Response: Triage Protocols
**Similar problem:** EMTs and ER staff face diverse emergencies. They need to classify quickly and apply the right protocol without specialist consultation.

**How they solve it:** Triage algorithms (START triage, SALT triage) classify patients into categories. Each category triggers a specific protocol. The classification step IS the routing layer. Protocols are designed to be executable under stress by non-specialists.

### Finance: Tax Preparation Software
**Similar problem:** Tax law is enormously complex. Most people can't navigate it. Professional accountants are expensive.

**How they solve it:** TurboTax and similar tools use guided question-and-answer flows to route users through the correct forms and procedures. The user doesn't need to know tax law -- the software classifies their situation and applies the right procedure. This is almost exactly the same structure as reasoningtool.

### Education: Bloom's Taxonomy and Instructional Design
**Similar problem:** Teachers need to design learning activities that target specific cognitive levels but many teachers lack training in cognitive science.

**How they solve it:** Bloom's Taxonomy provides a classification of cognitive tasks (remember, understand, apply, analyze, evaluate, create) with associated verb lists and activity templates. It's a routing layer (classify the learning goal) plus procedure library (here's how to design for that level).

### Therapy: Cognitive Behavioral Therapy (CBT) Workbooks
**Similar problem:** People have distorted thinking patterns but can't afford or access a therapist. Therapeutic techniques are expert knowledge.

**How they solve it:** CBT workbooks codify therapeutic procedures into self-guided exercises. "Feeling Good" by David Burns gave people the actual procedures therapists use: identify the cognitive distortion (routing), apply the specific correction technique (procedure). The structural parallel to reasoningtool is remarkably close.

### Military: Doctrine and Field Manuals
**Similar problem:** Soldiers face diverse tactical situations. Commanders can't be everywhere. Decisions must be made by junior personnel in the field.

**How they solve it:** Military doctrine codifies decision-making procedures into field manuals. FM 7-8 (Infantry Rifle Platoon and Squad) gives step-by-step procedures for dozens of tactical situations. Battle drills are pre-rehearsed procedures triggered by situation recognition.

---

## Step 4: Evaluate Analogies

| Domain | Structural Similarity | Solution Quality | Transferability |
|--------|----------------------|-----------------|----------------|
| **Medicine (CPGs)** | **Very high.** Routing layer (differential diagnosis) + procedure library (guidelines) + point-of-need delivery. Almost identical structure. | Excellent -- measurably improves outcomes. | High. The "UpToDate for thinking" framing is compelling. Lesson: evidence-based procedure development matters. |
| **Software (Design Patterns)** | **High.** Named patterns, problem-shape recognition, structured solutions. | Good -- widely adopted, genuinely useful. | Medium. Design patterns require more background knowledge than ideal. Lesson: naming patterns is powerful for recall and communication. |
| **Aviation (Checklists)** | **High.** Externalized procedures, triggered by situation classification. | Excellent -- dramatic error reduction. | High. Key lesson: externalizing from memory is the mechanism, not just a convenience. |
| **Tax Software (TurboTax)** | **Very high.** Question-driven routing, non-expert executes expert procedures, covers wide domain. | Excellent -- massive market, proven demand. | Very high. The closest commercial analog. Lesson: the routing UX matters as much as the procedures. |
| **Therapy (CBT Workbooks)** | **Very high.** Classify the distortion (routing), apply the correction (procedure), self-guided, improves cognitive quality. | Good -- clinically validated for mild-moderate cases. | Very high. The *closest domain analog* -- both are literally about thinking better. Lesson: self-guided procedure execution works for cognitive improvement. |
| **Manufacturing (Standard Work)** | **High.** Codified procedures, quality through process, living/improvable system. | Excellent -- transformed manufacturing quality globally. | Medium-high. Lesson: procedures should be improvable by users (kaizen). |
| **Emergency (Triage)** | **High.** Classification IS routing, protocols are stress-executable. | Excellent. | Medium. Lesson: the classification/routing step is itself a skill that must be designed carefully. |
| **Cooking (Recipes)** | **Medium-high.** Procedures for non-experts, technique > recipe as the deeper insight. | Good. | Medium. Lesson: teaching the *why* behind steps enables adaptation, not just execution. |
| **Military (Doctrine)** | **High.** Situation recognition triggers pre-learned procedure, field-executable by junior personnel. | Good in structured situations. | Medium. Lesson: rehearsal/practice of procedures dramatically improves execution quality. |
| **Education (Bloom's)** | **Medium.** Classification + activity templates. | Moderate -- widely known but inconsistently applied. | Medium. Lesson: classification frameworks are useful even when imperfect. |

---

## Step 5: Transfer Solutions

### Transfer 1: From Medicine (Clinical Practice Guidelines + UpToDate)

**What maps directly:**
- CPG = Skill procedure
- Differential diagnosis = Category skills (/claim, /decide, /diagnose, etc.)
- UpToDate's point-of-care delivery = Claude Code plugin invocation
- Evidence-based guideline development = Skill quality validation

**What needs adaptation:**
- Medicine has measurable outcomes (mortality, recovery time); thinking quality is harder to measure
- CPGs are developed by specialist committees with evidence review; skills currently come from one developer

**What doesn't transfer:**
- Regulatory enforcement (doctors must follow guidelines); reasoningtool is voluntary
- Insurance/liability incentives

**Transferred insight:** Invest in evidence-based skill development. Track outcomes. Build a "levels of evidence" framework for skill quality. The UpToDate model (subscription access to maintained, evidence-based procedures) is a viable business model.

### Transfer 2: From Tax Software (TurboTax)

**What maps directly:**
- Question-driven routing = Category skills asking clarifying questions
- Form selection = Skill selection
- Guided fill-in = Step-by-step skill execution
- "Interview" UX = The back-and-forth of skill invocation

**What needs adaptation:**
- Tax has definitive right answers; thinking has better/worse but rarely provably correct
- TurboTax has a fixed annual cycle; thinking needs are continuous and varied

**What doesn't transfer:**
- Regulatory requirement to file (forced demand)
- Numerical precision requirements

**Transferred insight:** The routing UX is the product. TurboTax's key innovation wasn't tax knowledge -- it was the "interview" that classifies your situation without requiring you to understand tax categories. Reasoningtool's category skills (/claim, /decide, etc.) serve this function but could be even more user-friendly with a single entry point that asks a few questions and routes automatically.

### Transfer 3: From CBT Workbooks (Feeling Good / David Burns)

**What maps directly:**
- Cognitive distortion identification = Problem classification
- Correction techniques = Skill procedures
- Self-guided workbook exercises = Skill steps with outputs
- "The feeling follows the thought" = Better procedures produce better thinking

**What needs adaptation:**
- CBT targets emotional distortions specifically; reasoningtool targets all cognitive tasks
- CBT workbooks have validated clinical outcomes; thinking skills lack formal validation

**What doesn't transfer:**
- Therapeutic relationship and accountability
- Clinical diagnosis requirements for severe cases

**Transferred insight:** CBT workbooks proved that self-guided cognitive procedure execution works. The key design pattern: (1) name the specific error/situation, (2) provide the specific correction/procedure, (3) have the user write out their work. "Feeling Good" sold 5 million copies because it gave people the actual tools therapists use. Reasoningtool is doing the same thing for general thinking. The validation: CBT workbooks have clinical evidence they work even without a therapist. This suggests structured thinking procedures can work even without a human expert guiding the process.

### Transfer 4: From Aviation (Checklists)

**What maps directly:**
- Normal checklists = Standard skill procedures
- Emergency checklists = Diagnostic/troubleshooting skills
- Situation recognition = Routing/classification
- Externalization from memory = The core mechanism

**What needs adaptation:**
- Aviation checklists are short and highly practiced; thinking procedures are longer and used ad-hoc
- Pilots have extensive training before using checklists; users have none

**Transferred insight:** The mechanism is externalization. Checklists don't make pilots smarter -- they prevent experts from skipping steps under cognitive load. Reasoningtool doesn't make people smarter -- it prevents them from skipping steps they'd never think to take. Frame the value proposition around *externalization*, not intelligence augmentation.

---

## Step 6: Evaluate Transferred Solutions

### Best Analog: CBT Workbooks
**Does it solve the problem?** Yes. CBT workbooks are the closest structural and domain analog -- they literally solved "helping people think more clearly" for the specific domain of emotional reasoning. The structure (classify the problem, apply the named procedure, write out your work) maps almost perfectly to reasoningtool.

**Limitations:** CBT addresses a narrower domain (emotional distortions) with more clinical validation. Reasoningtool covers broader territory with less formal evidence.

**What would need to change:** Reasoningtool could adopt CBT's validation approach -- before/after studies showing that using a skill produces measurably better outputs than not using one.

### Most Commercially Instructive: TurboTax
**Does it solve the problem?** Yes -- it demonstrates that expert-procedure-as-software is a proven, massive market when the routing UX is excellent.

**Limitations:** Tax has forced demand and definitive answers. Thinking tools must create their own demand and handle ambiguity.

**What would need to change:** Focus on routing UX. A single entry point ("describe what you're working on") that classifies and routes, rather than requiring users to know skill names.

### Most Mechanistically Instructive: Aviation Checklists
**Does it solve the problem?** Yes -- it reframes *why* the system works. Not intelligence augmentation but step-externalization and error prevention.

**Limitations:** Checklists work best for known, repeatable procedures. Many thinking tasks are more open-ended.

**What would need to change:** Distinguish between "checklist-like" skills (where completeness matters) and "method-like" skills (where the procedure generates insight). Different skill types may need different formats.

---

## Synthesis

The strongest structural analog is **CBT workbooks** -- they solved the same problem (making expert cognitive procedures accessible to non-experts for self-guided use) in a narrower domain and proved it works clinically. Reasoningtool is essentially "CBT workbooks for all of thinking, not just emotional reasoning."

The most commercially instructive analog is **TurboTax** -- it proved that the routing/classification UX is as important as the procedures themselves, and that codified expert procedures can build a massive business.

The most important mechanistic insight comes from **aviation checklists** -- the value is *externalization*, not intelligence. The system works because it prevents step-skipping, not because the steps are secret.

**Three actionable transfers:**
1. **From CBT:** Validate skills with before/after studies. Name each skill's target clearly (like named cognitive distortions). This builds trust and adoptability.
2. **From TurboTax:** Build a single-entry routing experience. The user describes their situation in natural language; the system classifies and routes. The routing IS the product.
3. **From Checklists:** Frame the value as externalization and error prevention, not "thinking better." People resist "you need to think better" but accept "here's a checklist so you don't miss anything."

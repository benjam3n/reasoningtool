# Decision Procedure — Creating Less Generic Procedures from DCP Output

**Date**: 2026-01-31
**Depth**: Full chain (dd → se → aex → stg → fla → pv)
**Input**: "creating less generic procedures from the dcp procedure"

---

## DIMENSION DISCOVERY

| # | Dimension | Values | Why It Matters |
|---|-----------|--------|----------------|
| 1 | **What's Generic** | Verbs (vague actions), Nouns (undefined terms), Criteria (unspecified thresholds), Tools (unnamed), Sources (unspecified data), Sequence (wrong order for domain) | Determines which specificity technique to apply |
| 2 | **Target Domain** | Technical, Business, Personal, Creative, Scientific, Organizational | Determines where to source specifics |
| 3 | **Audience Expertise** | Novice (needs everything spelled out), Practitioner (needs decision logic, not basics), Expert (needs edge cases and exceptions only) | Determines how much detail to add vs. remove |
| 4 | **Available Specificity Sources** | Domain expert, Existing documentation, Empirical data, Best practices literature, Personal experience, None (must discover) | Determines how to fill in the specifics |
| 5 | **Reuse Scope** | One-time use, Personal recurring, Team standard, Organization-wide, Public/published | Determines how much investment in specificity is warranted |
| 6 | **Genericness Severity** | Lightly generic (needs a few specifics filled in), Moderately generic (structure is right, details are missing), Heavily generic (structure itself needs domain adaptation) | Determines scope of the de-genericizing work |

### Key Interactions

| If... | Then... |
|-------|---------|
| What's generic is **Verbs** | Replace with domain-specific action verbs that name the exact operation |
| What's generic is **Criteria** | Fill in specific numbers, thresholds, and decision rules |
| Audience is **Novice** | Every term must be defined; every tool must be named and linked |
| Audience is **Expert** | Strip basics; focus on edge cases and exception handling |
| Available source is **None** | Must run experiments or interviews to discover specifics |
| Reuse scope is **One-time** | Minimal investment — just fill blanks for this case |
| Genericness is **Heavy** | May need to restructure, not just fill in details |

---

## ASSUMPTION EXTRACTION

| Assumption | Type | Hiddenness | Risk if Wrong |
|---|---|---|---|
| A1: The DCP's structure is correct for the target domain | STABILITY | Buried | HIGH |
| A2: Specificity always improves a procedure | VALUE | Deep | HIGH |
| A3: You know what the right specifics are | KNOWLEDGE | Shallow | MEDIUM |
| A4: One level of specificity fits all users | CAPABILITY | Deep | HIGH |
| A5: The specifics are stable | STABILITY | Deep | MEDIUM |
| A6: Adding specifics is purely additive | CAUSAL | Buried | HIGH |
| A7: The DCP captured all the steps | EXISTENCE | Shallow | MEDIUM |

---

## THE PROCEDURE

```
================================================================
DE-GENERICIZING PROCEDURES
================================================================
Turn a generic DCP output into a specific, domain-adapted
procedure that names exact tools, thresholds, sources, and
actions.

PREREQUISITE: You have a procedure (from /dcp or elsewhere)
that feels too generic to be directly useful.

================================================================

STEP 0: IS THE STRUCTURE RIGHT?
================================================================

Before adding specifics, verify the generic procedure's
structure fits your domain.

Read through the procedure and answer:

  Q1: "Are these the right steps for MY domain, or do
       they reflect a generic domain's logic?"

  - Right steps, just vague -> Go to STEP 1
  - Mostly right, 1-2 steps missing or wrong -> Fix the
    structure first (add/remove/reorder steps), THEN go to
    STEP 1
  - Fundamentally wrong order or missing major sections ->
    STOP. Re-run /dcp with more domain-specific input, or
    restructure manually before proceeding.

  Q2: "Does this procedure have steps that DON'T APPLY
       to my domain?"

  - If yes: Delete them now. It's easier to remove before
    you've invested in specifying them.
  - If no: Continue.

================================================================

STEP 1: DEFINE YOUR TARGET
================================================================

Answer three questions. Write the answers down — you'll
reference them throughout.

  1a. WHO will use this procedure?
      Pick one:
      - [ ] Myself only
      - [ ] A specific person (name: ___)
      - [ ] A small team who share my context
      - [ ] A broad audience with varied expertise
      - [ ] Unknown/public users

  1b. What is their EXPERTISE LEVEL in this domain?
      Pick one:
      - [ ] Novice — needs every term defined, every tool
            named and linked, every sub-step spelled out
      - [ ] Practitioner — knows the basics, needs decision
            logic, thresholds, and edge cases
      - [ ] Expert — knows the domain, needs only the
            non-obvious parts and exception handling

  1c. How many times will this procedure be used?
      Pick one:
      - [ ] Once (just need it for this case)
      - [ ] Recurring personal use (5-20 times)
      - [ ] Team standard (used by others regularly)
      - [ ] Organizational standard (many users, long life)

  INVESTMENT RULE:
  | Usage | Appropriate investment |
  |-------|----------------------|
  | Once | Fill in blanks for YOUR case only. 15 minutes. |
  | Recurring personal | Fill in all blanks. Test once. 1 hour. |
  | Team standard | Fill in, review with team, test 3x. Half day. |
  | Organizational | Fill in, expert review, parallel test, document. Full day+. |

================================================================

STEP 2: IDENTIFY WHAT'S GENERIC
================================================================

Go through the procedure step by step. For each step, mark
what type of genericness is present. Use this checklist:

  For EACH step, check all that apply:

  [ ] VAGUE VERB — The action word is imprecise
      Examples: "consider", "evaluate", "assess", "review",
      "determine", "ensure", "handle", "address", "manage"
      Mark as: [VV]

  [ ] UNDEFINED NOUN — A key noun isn't specific
      Examples: "the stakeholders", "the data", "relevant
      factors", "the system", "the team"
      Mark as: [UN]

  [ ] MISSING CRITERIA — A decision has no threshold
      Examples: "if good enough", "when ready", "if
      significant", "if acceptable"
      Mark as: [MC]

  [ ] UNNAMED TOOL — A tool or method isn't named
      Examples: "use a tool to...", "run an analysis",
      "create a report", "set up monitoring"
      Mark as: [UT]

  [ ] UNSPECIFIED SOURCE — Data source isn't named
      Examples: "gather data", "research the topic",
      "collect feedback", "check the metrics"
      Mark as: [US]

  [ ] FINE AS-IS — This step is already specific enough
      for the target audience
      Mark as: [OK]

  Output: A marked-up copy of the procedure.

  COUNT your marks:
  - Total [VV]: ___
  - Total [UN]: ___
  - Total [MC]: ___
  - Total [UT]: ___
  - Total [US]: ___
  - Total [OK]: ___

  If most steps are [OK]: Your procedure may already be
  specific enough. Ask: "Would someone from my target
  audience (Step 1) be able to follow this without asking
  me any questions?" If yes, stop — you're done.

================================================================

STEP 3: FILL IN SPECIFICS
================================================================

For each marked element, apply the appropriate fix.

PRIORITY ORDER: Fix in this order because later fixes
depend on earlier ones:
  1. Undefined Nouns [UN] — you can't specify an action
     until you know what it operates on
  2. Unspecified Sources [US] — you can't set thresholds
     until you know where the data comes from
  3. Unnamed Tools [UT] — you can't write exact steps
     until you know which tool you're using
  4. Missing Criteria [MC] — now you can set thresholds
     because you know the data and tools
  5. Vague Verbs [VV] — now you can name the exact action
     because you know the noun, source, tool, and criteria

FOR EACH FIX:

  3a. Fixing [UN] — Undefined Nouns
      For each undefined noun, write:
      "In MY domain, [generic noun] means specifically:
       [list the exact items]"

      If you can't name them: this is a DISCOVERY gap.
      Write: "[UN-UNKNOWN] Need to identify: [noun]"

  3b. Fixing [US] — Unspecified Sources
      For each unspecified source, write:
      "The data for this step comes from: [exact source]
       Access method: [how to get it]
       Format: [what it looks like]"

      If you don't know the source: this is a DISCOVERY gap.
      Write: "[US-UNKNOWN] Need to find source for: [data]"

  3c. Fixing [UT] — Unnamed Tools
      For each unnamed tool, write:
      "The tool for this step is: [exact tool name]
       Version: [if relevant]
       Command/action: [exact command or UI steps]"

      If you don't know the tool: this is a SELECTION gap.
      Write: "[UT-UNKNOWN] Need to select tool for: [task]"

  3d. Fixing [MC] — Missing Criteria
      For each missing criterion, write:
      "The threshold for this decision is: [exact number
       or condition]
       Source of threshold: [where this number comes from]
       If borderline: [what to do]"

      If you don't know the threshold: this is a CALIBRATION gap.
      Write: "[MC-UNKNOWN] Need threshold for: [decision]"

  3e. Fixing [VV] — Vague Verbs
      For each vague verb, replace with the specific action
      now that you know the noun, source, tool, and criteria:

      | Generic verb | Replacement pattern |
      |---|---|
      | "Consider" | "List [specific items]. For each, check [criteria]." |
      | "Evaluate" | "Score [item] on [scale] using [rubric/tool]." |
      | "Assess" | "Measure [metric] using [tool]. Compare to [threshold]." |
      | "Review" | "Read [specific document]. Check for [specific things]." |
      | "Determine" | "Calculate [formula]. If result [condition], then [action]." |
      | "Ensure" | "Verify [specific check] returns [expected result]." |
      | "Handle" | "If [condition A]: do [X]. If [condition B]: do [Y]." |
      | "Address" | "Fix [specific thing] by [specific method]." |
      | "Manage" | "Track [metric] in [tool]. If [threshold], take [action]." |

================================================================

STEP 4: HANDLE DISCOVERY GAPS
================================================================

Collect all items marked [XX-UNKNOWN] from Step 3.

If you have ZERO unknowns: Skip to Step 5.

For each unknown, choose a resolution method:

  | Gap type | Resolution |
  |----------|-----------|
  | [UN-UNKNOWN] | Ask a domain expert: "Who/what specifically is involved in this step?" OR review existing documentation for named entities |
  | [US-UNKNOWN] | Ask: "Where does this data actually live?" Check: databases, dashboards, documents, people's heads |
  | [UT-UNKNOWN] | Ask: "What tool does the team currently use for this?" If no tool exists: evaluate options or mark step as manual |
  | [MC-UNKNOWN] | Run the procedure 3 times. Note where you had to make a judgment call. After 3 runs, set the threshold based on what worked |

  For each gap resolved: go back to Step 3 and fill it in.

  For each gap you CAN'T resolve now:
  Write in the procedure: "⚠ PLACEHOLDER: [what's needed].
  Current best guess: [your guess]. To be updated after
  [condition]."

================================================================

STEP 5: ADJUST FOR AUDIENCE
================================================================

Now that specifics are filled in, adjust the detail level
for your target audience (from Step 1b).

  FOR NOVICE AUDIENCE:
  - Define every domain term inline (first use)
  - Add "What you should see" after each step
  - Add screenshots or examples for tool commands
  - Add "If this doesn't work, try..." for each step
  - Link to tool documentation for each named tool

  FOR PRACTITIONER AUDIENCE:
  - Remove basic definitions (they know the terms)
  - Keep decision logic, thresholds, and edge cases
  - Add "Common mistakes at this step" where relevant
  - Keep tool names but skip basic usage instructions

  FOR EXPERT AUDIENCE:
  - Strip all basics — just decision points and thresholds
  - Focus on: what's non-obvious, what's changed recently,
    what the exceptions are
  - Present as a checklist, not a tutorial
  - Add: "Override this step when [condition]"

  ADJUSTMENT METHOD:
  Read each step and ask:
  "Would my target user need me to explain this, or would
   they already know it?"
  - If they'd need explanation: keep or expand
  - If they'd already know: compress to a single line or
    delete (for experts)

================================================================

STEP 6: TEST THE PROCEDURE
================================================================

  6a. Dry run
      Walk through the procedure with a REAL case. At each step:
      - Could you execute this step without outside help? (Y/N)
      - Did you have to interpret anything? (Y/N)
      - Did any step produce unexpected output? (Y/N)

      Any "N" on the first question or "Y" on the second:
      that step needs more specificity. Go back to Step 3.

  6b. Audience test (if Reuse Scope is Team or higher)
      Give the procedure to ONE person from your target
      audience. Watch them use it (or have them mark
      confusion points). Fix what they stumble on.

  6c. Specificity audit
      Count remaining generic elements:
      - Vague verbs remaining: ___
      - Undefined nouns remaining: ___
      - Missing criteria remaining: ___

      If any count > 0 and the element matters for the
      outcome: fix it.

      If any count > 0 but the element is minor or
      context-dependent: add a note rather than a false
      specific.

================================================================

STEP 7: GUARD AGAINST OVER-SPECIFICATION
================================================================

Before finalizing, check for over-specification:

  For each specific you added, ask:
  "Is this specific STABLE, or will it change soon?"

  | Stability | Treatment |
  |-----------|-----------|
  | Stable (won't change in 1+ years) | Hard-code into procedure |
  | Semi-stable (changes quarterly/annually) | Include with "Last verified: [date]" tag |
  | Volatile (changes monthly or faster) | DON'T hard-code. Write: "Check [source] for current value of [thing]" |

  Also ask:
  "Does this specific CONSTRAIN the procedure's applicability?"

  | Constraint impact | Treatment |
  |---|---|
  | Appropriate (this IS only for one context) | Keep |
  | Over-constraining (excludes valid cases) | Generalize back OR add branch |
  | Not sure | Keep for now, note for review |
```

---

## QUICK REFERENCE CARDS

**CARD 1: THE 15-MINUTE DE-GENERIC**
1. Read procedure, circle every vague word
2. For each vague word, write the specific thing for YOUR current situation
3. Done. Don't over-invest.

**CARD 2: THE VERB REPLACEMENT TABLE**

| Generic | Replace with |
|---------|-------------|
| Consider | List + Check |
| Evaluate | Score + Compare |
| Assess | Measure + Threshold |
| Review | Read + Verify |
| Determine | Calculate + Condition |
| Ensure | Verify + Expected |
| Handle | If/Then branches |

**CARD 3: THE SPECIFICITY PRIORITY**
Fix in this order:
1. Nouns (what are we talking about?)
2. Sources (where does the data come from?)
3. Tools (what do we use?)
4. Criteria (what are the thresholds?)
5. Verbs (what exactly do we do?)

**CARD 4: WHEN TO STAY GENERIC**
Keep a step generic when:
- The specific changes too often to hard-code
- Different users legitimately need different specifics
- The choice doesn't affect the outcome
- Specifying would require expertise you don't have (better vague than specifically wrong)

---

## COMMON MISTAKES

1. **Decorating a broken structure** — Adding specifics to wrong steps. Validate structure first (Step 0).
2. **Specifying everything at once** — Specify the critical path first, then iterate.
3. **Filling in wrong specifics confidently** — Use placeholder format when uncertain.
4. **Over-specifying for the audience** — Match detail to audience (Step 5).
5. **Hard-coding volatile specifics** — Use "Check [source] for current [value]" instead.
6. **Losing the generic version** — Keep it as a reusable template.
7. **Skipping the test** — Always dry-run (Step 6a).
8. **Making it too long** — Every specific adds length. Length reduces compliance.

---

## FAILURE ANTICIPATION

| # | Failure Mode | O | S | D | RPN | Tier |
|---|---|---|---|---|---|---|
| 1 | Skips Step 0, adds specifics to wrong structure | 6 | 8 | 5 | 240 | Critical |
| 2 | Fills in wrong specifics confidently | 6 | 7 | 7 | 294 | Critical |
| 3 | Over-specifies, procedure becomes brittle and long | 7 | 5 | 7 | 245 | Critical |
| 4 | Specifies for wrong audience level | 5 | 5 | 4 | 100 | High |
| 5 | Hard-codes volatile specifics | 7 | 4 | 8 | 224 | Critical |
| 6 | Overwrites generic version | 4 | 5 | 3 | 60 | Medium |
| 7 | Tries to de-genericize everything in one pass | 6 | 3 | 4 | 72 | Medium |

---

## VALIDATION REPORT

| Dimension | Status |
|-----------|--------|
| Completeness | PASS |
| Dependencies | PASS |
| Feasibility | PASS |
| Inputs | PASS |
| Outputs | PASS |
| Consistency | PASS |

**OVERALL STATUS: VALID**

Validation status: This procedure has not been validated by domain experts.
Version: 1.0
Generated: 2026-01-31

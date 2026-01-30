# reasoningtool

207 thinking skills for Claude Code. Each skill is a structured prompt that guides you through a specific type of thinking, decision, or analysis.

## Installation

### Option 1: Run from this directory

```bash
git clone https://github.com/benjam3n/reasoningtool.git
cd reasoningtool/claude-code-plugin
claude
```

Claude reads the `CLAUDE.md` file and all skills become available.

### Option 2: Copy into your project

```bash
cp -r path/to/reasoningtool/claude-code-plugin/skills your-project/
cp path/to/reasoningtool/claude-code-plugin/CLAUDE.md your-project/
cd your-project
claude
```

## All Skills

| Skill | Stands for | What it does |
|-------|-----------|-------------|
| `/aa` | assumption audit | Surface and rigorously test a field's hidden assumptions. |
| `/aar` | after action review | The After Action Review (AAR) is a structured debrief to learn from |
| `/aba` | ai biomedical agent | GOSM Ai Biomedical Agent procedure |
| `/ac` | adversarial checklist | Create a checklist that catches what normal checklists miss. |
| `/acr` | active recall | Use retrieval practice and self-testing to strengthen learning and identify gaps |
| `/adep` | adaptive extraction pipeline | Breadth-first, learned extraction pipeline that clarifies goals first, samples broadly, learns user preferences, and ... |
| `/advr` | adversarial review | Nothing is a fact until it survives an assassination attempt. Builder constructs claims, Breaker tries to destroy them. |
| `/ael` | assumption elimination | Before asserting anything, verify it can be confirmed by the listener. |
| `/aex` | assumption extraction | Extract hidden assumptions from any content. Surfaces what must be true for claims to hold, enabling deeper analysis. |
| `/afa` | anticipated failures analysis | A postmortem examines why something failed after the fact. |
| `/agi` | araw gosm integration | Systematic procedure for translating ARAW exploration outputs |
| `/ai` | assumption inversion | Invert assumptions to discover blind spots and alternative possibilities. What if the opposite were true? |
| `/ais` | advocacy infrastructure setup | Set up foundational infrastructure for autonomous advocacy operations |
| `/al` | active listening | Systematic procedure for listening deeply to understand others, build trust, and improve communication outcomes |
| `/am` | academic mastery | Master academic subjects through structured learning, concept mapping, and competency verification |
| `/ams` | api middleman strategies | Collection of strategies for bypassing or working around API limitations, including rate limits, IP blocks, and acces... |
| `/ans` | analogy search | Many problems have been solved before - just in different domains. |
| `/ao` | algorithmic optimization | Orderings based on classic algorithm design paradigms: greedy, |
| `/ap` | architecture patterns | Procedure for evaluating, choosing, and implementing software architecture patterns |
| `/ape` | alphacode pass 1 explicit | GOSM Alphacode Pass1 Explicit procedure |
| `/api` | alphacode pass 2 implicit | GOSM Alphacode Pass2 Implicit procedure |
| `/apid` | api design | Procedure for designing, implementing, and documenting effective APIs |
| `/apm` | alphacode pass 3 meta | GOSM Alphacode Pass3 Meta procedure |
| `/ar` | assume right | Deep recursive rightness search. Traces implications, foreclosures, and costs of a claim being true. |
| `/araw` | assume right assume wrong | For every claim, explore what follows if true (AR) and what breaks if false (AW). Tests both sides with equal rigor. |
| `/arcd` | architecture design | Orderings for software development that determine whether to |
| `/argd` | argumentative document | GOSM Argumentative Document procedure |
| `/asu` | assumption surfacing | Plans and beliefs rest on assumptions that are often invisible. |
| `/atgb` | araw to gosm bridge | Bridges ARAW exploration outputs to GOSM planning inputs. |
| `/auep` | automated extraction pipeline | Industrial-scale automation pipeline for extracting procedures from 70+ YouTube channels and other sources using the ... |
| `/av` | assumption verification | GOSM Assumption Verification procedure |
| `/aw` | assume wrong | Deep recursive wrongness search. Finds failure reasons, derives alternatives from what breaks. |
| `/b` | budgeting | Create, manage, and optimize budgets for projects, organizations, or personal finances |
| `/be` | bandit exploration | Orderings from multi-armed bandit algorithms for balancing |
| `/bes` | binary elimination search | Like playing 20 Questions - each yes/no question eliminates half the possibilities. |
| `/bi` | bounded inquiry | Unbounded inquiry cannot terminate - every answer opens new questions. |
| `/bm` | budget management | Manage limited financial resources across autonomous operations with maximum value extraction |
| `/bo` | business operations | Comprehensive procedure for business goals including starting, growing, |
| `/boc` | better option check | Prevent user from settling on suboptimal option by systematically checking if better options exist that match their preferences. |
| `/br` | backward reasoning | Reasoning from conclusions back to premises. |
| `/capg` | capability gate | Pre-step feasibility check determining if AI can execute directly, needs delegation, or if task is infeasible |
| `/cba` | cost benefit analysis | Systematically quantify costs and benefits to evaluate decisions, including NPV calculation, sensitivity analysis, an... |
| `/cd` | customer discovery | Validate customer problems and solutions before building |
| `/cda` | cross domain analogy | Find analogies from other domains to generate novel insights. Transfer solutions and patterns across fields. |
| `/cdb` | cross domain bridge | Most new strategies are actually old strategies from other domains. Find isomorphisms and translate winning strategies. |
| `/cdr` | cross domain report | Discover what one field can learn from another by finding structural analogies, testing their transferability, and synthesizing actionable insights. |
| `/cfm` | cash flow management | Track and optimize cash flow including income, expenses, runway calculation, and burn rate analysis |
| `/cfr` | conflict resolution | Systematic procedure for de-escalating tensions, finding common ground, and navigating difficult conversations produc... |
| `/cga` | cognitive amplification | You have a way of analyzing things. It works. But you can only hold |
| `/ch` | crisis handler | GOSM Crisis Handler procedure |
| `/clg` | collective goals | Handler for goals that require building collectives, communities, or movements. |
| `/clr` | client retention | Systematic approach to retaining clients through tiered engagement strategies and value-add touchpoints. |
| `/cls` | checklist search | The simplest possible search: enumerate items, check each against |
| `/cma` | competitive analysis | Systematically analyze competitive landscape using Porter's Five Forces, competitor mapping, and differentiation stra... |
| `/cmp` | comparison | Compare options using gestalt impression + structured evaluation. |
| `/cms` | component selection | A structured procedure for evaluating multiple component options against |
| `/cn` | communication narrative | Orderings for presentations, writing, and communication where |
| `/cns` | constraint solving | Orderings for constraint satisfaction and guided search problems. |
| `/cnw` | constraint workarounds | When you face a constraint that seems to block progress, NEVER give up. |
| `/cor` | code review | Procedure for conducting effective code reviews using Claude Code's capabilities for exhaustive analysis |
| `/cpp` | career path planning | Strategic framework for assessing career options, planning transitions, |
| `/cppd` | cross project pattern detection | Analyze patterns across completed GOSM projects to improve the system. |
| `/cpra` | comprehensive aspects | Meta-procedure for ensuring any analysis, procedure, or decision |
| `/cri` | critique | Structured evaluation using gestalt impression + analytical decomposition. |
| `/crw` | criteria weighting | Also known as: Weighted scoring model, Decision matrix, Pugh matrix. |
| `/ct` | crisis triage | Orderings for resource-constrained emergency situations where |
| `/cta` | category analysis | Analyze a category of guesses to determine which apply to the user. |
| `/cts` | content strategy | Develop and execute content strategy that attracts, engages, and converts |
| `/cv` | convergent validation | Addresses the n+1 critic problem: any critic can be criticized, infinitely. |
| `/dari` | deductive adversarial review integration | Bridges the deductive strategy system with adversarial adversarial review testing. |
| `/dbg` | debugging | Systematic procedure for diagnosing and fixing software bugs using Claude Code's tool capabilities |
| `/dc` | data collection | Systematic procedure for gathering research data through surveys, interviews, observation, and secondary sources |
| `/dcm` | decomposition | Break complex goals into simpler, manageable sub-goals |
| `/dcp` | decision procedure | Create a mechanical, step-by-step decision procedure for a recurring decision type. |
| `/dct` | decision trees | Systematic procedure for structuring complex decisions with multiple branches, probabilities, and outcomes. |
| `/dd` | dimension discovery | Identify the key dimensions that define a problem space, enabling comprehensive enumeration. |
| `/de` | dependency extraction | Extract dependencies between steps, tasks, or items. |
| `/dlp` | deliberate practice | Design and execute targeted practice sessions that maximize skill improvement |
| `/dmt` | domain template | Create domain-specific skill configurations. |
| `/dop` | documentation procedures | Procedures for creating comprehensive project documentation that allows |
| `/dot` | delayed outcome tracking | Procedure for tracking outcomes that take months or years to manifest. |
| `/dpl` | deployment | Procedure for planning and executing reliable software deployments |
| `/dsd` | deductive strategy discovery | Derive strategies by working backward from success criteria to required actions. |
| `/dse` | deductive strategy evaluation | Evaluate strategies based on the logical soundness of their derivation. |
| `/dsn` | design | Apply universal design principles to create or improve designs. |
| `/dsp` | design procedures | Procedures for systematic design of mechanical systems, chassis, |
| `/dss` | design system | Complete system design workflow - composes multiple sub-procedures |
| `/dtl` | design thinking lean | Two complementary methodologies for innovation: |
| `/dv` | detection verification | Orderings optimized for detecting cheating, fraud, deception, and anomalies. |
| `/dvs` | diversity search | Orderings that prioritize behavioral diversity, novelty, and |
| `/ea` | email acquisition | Acquire and configure email addresses for autonomous system operations |
| `/eda` | event driven automation | Maintain project continuity through event monitoring and automated state management |
| `/eg` | exploratory goals | GOSM Exploratory Goals procedure |
| `/eh` | epistemic hierarchy | A layered framework for building from certain foundations toward determinate action. |
| `/emv` | empirical validation | Empirical validation step for GOSM plans - adds external reality testing beyond coherence checks |
| `/enc` | engineering calculations | A collection of standard engineering calculation procedures used in |
| `/er` | economic research | Systematic analysis of economic viability, cost structures, and comparative advantage |
| `/es` | evolutionary strategies | Evolution has optimized biological systems for billions of years. |
| `/ess` | external source search | GOSM External Source Search procedure |
| `/evd` | evaluation dimensions | Universal dimensions for evaluating any claim, problem, or solution. |
| `/exc` | existence check | Systematically check if a solution or similar solution already exists before investing effort in creation |
| `/exd` | experimental design | Systematic procedure for designing rigorous experiments with proper controls, variables, and validity considerations |
| `/exv` | expected value | Systematic procedure for calculating expected value, adjusting for risk, and determining optimal resource allocation ... |
| `/faa` | fairness allocation | Orderings that balance competing priorities, prevent starvation, |
| `/fat` | failure attribution | When a project fails, systematically analyze the root cause. |
| `/fb` | feedback | Generate filtered feedback for self-improvement loops. |
| `/fd` | feedback delivery | Systematic procedure for delivering feedback that is heard, received, and acted upon, and for receiving feedback grac... |
| `/fe` | framework extension | Systematic process for extending the GOSM framework with new procedures, gates, or capabilities. |
| `/ff` | fundraising financial | Raise investment capital through investor outreach, pitch preparation, term sheet negotiation, and due diligence |
| `/fia` | field analysis | Comprehensive analysis of a field's key tensions, hidden assumptions, and blind spots. |
| `/fj` | failure journeys | Most goal journey work focuses on SUCCESS paths. |
| `/fl` | freelancing | Comprehensive guide to building a sustainable freelance practice, from finding |
| `/fla` | failure anticipation | Systematically identify potential failures, assess their risk, and plan mitigations before execution |
| `/fm` | financial modeling | Build financial models for projections, scenario analysis, and sensitivity testing to support decision-making |
| `/fnd` | finder | Find the right GOSM skill for what you want to do. |
| `/foht` | figure out how to | Maps the full method space, surfaces prerequisites, AR/AW tests each method, produces verdicts. |
| `/fowwr` | figure out what went wrong | Traces backward from symptoms to root causes. Tests each candidate cause with counterfactuals. Derives prevention measures. |
| `/fr` | failure recovery | Structured recovery procedures when projects encounter failures, providing clear decision trees and specific actions ... |
| `/fss` | future space search | The future is uncertain but not arbitrary. |
| `/fua` | fundraising advocacy | Build self-sustaining funding for advocacy operations through multiple revenue streams |
| `/gaa` | gosm approach audit | An honest audit of GOSM's approach, claims, and limitations. |
| `/gaca` | gate as claim audit | Convert gates from "yes/no vibe checks" into explicit, checkable claim-interfaces. |
| `/gd` | goal decomposition | A methodology for decomposing abstract goals into specific, actionable components. |
| `/gdm` | group decision making | Systematic procedure for making effective decisions in groups, avoiding common pitfalls, and leveraging collective in... |
| `/ge` | growth experiments | Run systematic experiments to discover and validate growth levers using hypothesis-driven testing |
| `/gee` | gate execution engine | Systematic execution of GOSM gates with enforcement. |
| `/gen` | generate | Produce diverse candidate solutions. |
| `/gg` | guess generation | Generate exhaustive guesses about user input using ALL search methods with coverage tracking. |
| `/gjs` | goal journey system | A goal journey is NOT a narrative arc. It's a CHAIN OF GOALS. Integration hub for GOSM goal processing. |
| `/gn` | generation | Generate all possible options for a decision or selection |
| `/gosm` | goal oriented state machine | Goal-Oriented State Machine. |
| `/grf` | goal refinement | Transform vague or incomplete goals into SMART goals with explicit clarification vs substitution distinction |
| `/grfr` | goal reframing | Transform impossible or problematic goals into achievable versions. |
| `/gsr` | goal structure reconstruction | Given any conclusion, statement, or claim, reconstruct the goal-structure. |
| `/gt` | graph traversal | Orderings derived from fundamental graph traversal algorithms. |
| `/gts` | generate then search | The fundamental pattern for making cognitive tasks tractable: |
| `/gu` | goal understanding | MANDATORY first step before attempting any goal. |
| `/gw` | grant writing | Find relevant grants, write compelling proposals, and manage grant relationships and compliance |
| `/hd` | human delegation | Delegate physical, phone, or in-person tasks to humans when AI cannot perform them directly |
| `/hf` | habit formation | Build new habits and break unwanted ones using behavioral science principles |
| `/ho` | health optimization | Comprehensive procedure for health-related goals including fitness, |
| `/ht` | hypothesis testing | Systematic procedure for formulating testable hypotheses, designing tests, and updating beliefs based on evidence. |
| `/hvh` | high volatility handler | GOSM High Volatility Handler procedure |
| `/idg` | iterative discovery goals | Handler for goals where SUCCESS IS DISCOVERING THE UNKNOWN, not executing a known plan. |
| `/ie` | innovation engine | A systematic search for non-obvious strategies using cross-domain mapping, |
| `/ifss` | inference space search | Information implies other information. But not all inferences are equal: |
| `/ig` | intuition goals | GOSM Intuition Goals procedure |
| `/im` | inversion method | Charlie Munger's inversion technique. Finding ways to fail, then avoiding them, makes success more likely. |
| `/ins` | insight synthesis | Synthesize insights from multiple sources into coherent, actionable understanding. |
| `/ip` | interview preparation | Comprehensive preparation system for job interviews covering research, story |
| `/ipss` | interpretation space search | Ambiguity means multiple interpretations are possible. |
| `/isd` | income stream development | Systematic process for identifying, building, and scaling new income streams. |
| `/ita` | impossible to achievable | GOSM Impossible To Achievable procedure |
| `/ivs` | investment strategy | Develop and execute personal investment strategies including portfolio allocation, risk tolerance assessment, and inv... |
| `/je` | journey extraction | Extract the underlying GOAL JOURNEY from any source: |
| `/jm` | journey matching | Given a current situation (goal, problem, state), find journeys |
| `/jss` | job search strategy | Systematic approach to job hunting that treats the search as a funnel to optimize, |
| `/la` | limitation analysis | Systematically identify limitations across multiple dimensions, |
| `/lcs` | local search | Orderings based on local search optimization: improving from |
| `/ld` | learning discovery | Orderings optimized for acquiring knowledge, validating hypotheses, |
| `/ldg` | luck dependent goals | GOSM Luck Dependent Goals procedure |
| `/lgi` | language goal identification | All language has a goal - it's trying to achieve something. |
| `/lp` | leverage points | Not all interventions are equal. In any complex system, there are places |
| `/lpd` | leverage point discovery | Most valuable strategies exploit leverage points - places where small |
| `/lps` | logical proof system | The foundational infrastructure for treating strategy selection as theorem proving. |
| `/lr` | literature review | Systematic procedure for conducting comprehensive literature reviews on any topic |
| `/lrs` | learning system | Systematically capture, analyze, and apply learnings to improve campaign effectiveness |
| `/lt` | learning transfer | Apply knowledge and skills from one domain to new contexts through systematic transfer strategies |
| `/m` | matching | Define criteria for filtering options |
| `/ma` | morphological analysis | Invented by Fritz Zwicky. Break a problem into independent dimensions, |
| `/mcd` | multi criteria decision | Systematic procedure for making decisions involving multiple criteria, tradeoffs, and stakeholders |
| `/mcg` | mentioned coverage gate | Gate that verifies all items mentioned by user have been considered, analyzed, and addressed. |
| `/mcp` | music composition performance | Orderings inspired by musical forms and performance practices. |
| `/mcs` | mcp setup | Configure MCP servers to enable autonomous GOSM execution capabilities |
| `/md` | method derivation | Derive the appropriate method from the situation rather than |
| `/mem` | mental models | Build and apply a latticework of mental models for better thinking across domains |
| `/met` | metaphor method | A systematic method for using metaphors to: |
| `/mf` | marketing funnel | Analyze and optimize the customer journey from awareness to revenue using the AARRR framework |
| `/mil` | military strategy | Orderings derived from military doctrine and strategic principles. |
| `/mp` | motivation psychology | Orderings that account for human psychological factors like energy, |
| `/mpa` | multi plan aggregation | Generate, evaluate, and manage multiple alternative plans for the same goal |
| `/mpg` | multi party goals | Handler for goals that require navigating institutions, groups, politics, and |
| `/mr` | market research | Systematic process for identifying, validating, and sizing market opportunities. |
| `/mrc` | meta reasoning core | Three core metacognitive questions. What am I trying to achieve? Is this the best way? Am I making progress? |
| `/mss` | model space search | Understanding = finding a model that fits. |
| `/mv` | mece validation | Validate that a list is MECE (Mutually Exclusive, Collectively Exhaustive). Identifies overlaps and gaps. |
| `/neg` | negotiation | Systematic procedure for preparing and conducting negotiations to reach mutually beneficial agreements |
| `/net` | networking | Systematic approach to building genuine professional relationships that create |
| `/ns` | negotiation strategy | Orderings for strategic interactions, negotiations, and situations |
| `/nss` | novelty space search | Creativity = novelty + value. |
| `/o` | optimization | Rank viable options from best to worst using multi-criteria optimization |
| `/ol` | ooda loop | In competitive environments, the entity that can cycle through |
| `/op` | order procedure | Determine the correct execution order for a set of steps based on dependencies and constraints |
| `/ops` | optical pooled screening | GOSM Optical Pooled Screening procedure |
| `/orc` | outreach campaigns | Execute multi-channel persuasion campaigns for policy advocacy |
| `/orm` | outreach communication | Craft and send high-quality outreach communications that maximize response rates |
| `/ov` | ordering variations | Alternative ordering strategies for procedure steps. The base order_procedure |
| `/ovi` | ordering variations integration | Comprehensive guide for integrating ordering_variations into the GOSM workflow. |
| `/p` | propose | Takes output from /ar, /aw, /u, /araw, or /uaua and converts numbered findings into steelmanned, actionable plans with conditional recommendations and derivation chains. |
| `/pag` | paradox goals | Handler for goals with inherent tensions where optimizing one dimension |
| `/pb` | progressive building | Orderings that build complexity incrementally, ensuring each step |
| `/pbi` | problem identification | Before solving, identify the RIGHT problem at the RIGHT level. |
| `/pbr` | probabilistic reasoning | Systematic procedure for estimating probabilities, updating beliefs with evidence, and making well-calibrated predict... |
| `/pbs` | population based search | Orderings that maintain multiple candidate solutions or use |
| `/pcd` | procedure discovery | Find or create the procedures needed to execute a plan |
| `/pce` | procedure engine | The deep analysis engine. |
| `/pcef` | procedure effectiveness | Unified framework for procedure effectiveness tracking. |
| `/pcex` | procedure extraction | After completing a goal, extract reusable procedures and generalize them for storage in the library, enabling GOSM to... |
| `/pci` | procedure improvement | Systematically improve GOSM library procedures using schema-driven validation and tier-based progress tracking |
| `/pefs` | procedure extraction from source | Meta-procedure for extracting implicit procedures from ANY external source, turning tacit knowledge into explicit, re... |
| `/pf` | priority frameworks | Orderings based on classic priority frameworks that classify |
| `/pge` | pedagogy educational | Orderings based on learning science research and educational psychology. |
| `/ph` | procedure hierarchy | Not all procedures are equal. There is a hierarchy: |
| `/pha` | phone acquisition | Acquire and configure phone numbers for autonomous system operations |
| `/pjc` | project closure | Complete projects properly with handoff and learning capture |
| `/pji` | project initiation | Launch projects with clear charter, stakeholders, and success criteria |
| `/pjm` | project management | Orderings from formal project management methodologies (PERT, CPM, |
| `/pjs` | project scoping | Procedure for defining project scope: what's included, what's excluded, |
| `/plr` | policy research | Identify evidence-based, neglected, tractable policies for advocacy campaigns |
| `/po` | personal optimization | N-of-1 experimentation framework for systematically improving personal health, |
| `/poa` | possibility analysis | Systematically explore the possibility space of what could be done. |
| `/pos` | positioning | Develop clear market positioning through category design, differentiation, and compelling messaging |
| `/pp` | procurement procedures | Procedures for managing the procurement of components and materials, |
| `/pqr` | proactive question rotation | A 24-week rotating list of questions for weekly review. Each week, engage with |
| `/prd` | presentation design | Systematic procedure for designing visually effective presentations, slides, and handouts that enhance rather than co... |
| `/pre` | preference elicitation | Elicit user preferences by presenting concrete trade-offs rather than asking open-ended questions. |
| `/prm` | pre mortem | Gary Klein's technique - assume it went wrong and ask why. |
| `/prr` | procedure registry review | Review and improve the procedure registry schema using explicit definitions, evidence alignment, and non-regression. |
| `/pss` | plan space search | There are always multiple ways to achieve a goal. |
| `/pt` | progress tracking | Monitor and report project status effectively |
| `/pus` | public speaking | Systematic procedure for preparing and delivering impactful presentations, speeches, and talks |
| `/pv` | procedure validation | Validate that a procedure is complete, executable, and all dependencies are satisfiable. |
| `/pvg` | preventive goals | Handler for goals focused on PREVENTING bad outcomes rather than |
| `/pw` | persuasive writing | Systematic procedure for writing persuasive content that influences readers and motivates action |
| `/pwc` | pairwise comparison | Instead of rating each option absolutely (hard), compare pairs |
| `/qaf` | question analysis framework | This framework provides methods for analyzing questions to determine: |
| `/qag` | question about guesses | Generate high-quality questions about identified guesses. |
| `/qg` | question generation | When you don't know something, the right question is worth more than |
| `/qm` | qualitative measurement | Procedure for measuring outcomes that resist quantification. |
| `/qo` | question order | Finds the satisfying unresolved question that opens a document. Orders all sub-questions in a dependency chain using backward chaining. |
| `/qr` | qualitative research | Systematic procedure for qualitative data analysis including coding, thematic analysis, grounded theory, and intervie... |
| `/qs` | queue scheduling | Orderings for managing queues, processing items by priority, |
| `/rc5w` | root cause 5 whys | Adaptive root cause analysis. |
| `/rca` | root cause analysis | Systematically trace symptoms back to their underlying root causes using structured diagnostic techniques. |
| `/rci` | recursive causal interrogation | A systematic approach to reasoning: tracing causes through questioning. |
| `/re` | reading effectively | Read strategically for comprehension, retention, and application using research-backed techniques |
| `/ret` | retrospective | Learn from completed work to improve future performance |
| `/rf` | refactoring | Procedure for systematically improving code structure without changing behavior |
| `/ria` | risk assessment | Systematic procedure for identifying, analyzing, and planning responses to risks |
| `/rlg` | relationship goals | GOSM Relationship Goals procedure |
| `/rm` | risk management | Orderings focused on managing uncertainty, preserving options, and |
| `/rmo` | resume optimization | Systematic approach to crafting resumes that pass ATS filters, capture attention, |
| `/roa` | roi analysis | Calculate and analyze return on investment for projects, purchases, and decisions |
| `/rqg` | requirements gathering | Elicit and document system requirements from stakeholders |
| `/rsg` | restoration goals | Handler for goals focused on REBUILDING from damage, not improving from baseline. |
| `/rso` | resource optimization | Orderings focused on maximizing throughput, minimizing waste, |
| `/rva` | reversibility analysis | Systematic procedure for analyzing decision reversibility, option value, and optimal commitment timing |
| `/saaapcav` | self audit analysis protocol clarity and validity | Use the analysis-protocol clarity question bank to audit a gate/procedure/document for interpretability, checkability... |
| `/saadag` | self audit detectors and generators | Run the detector suite against a target artifact to find ambiguity, proxy substitution, bundled checks, undefined ter... |
| `/saaesa` | self audit evidence standard application | Audit a document as if it claimed an evidence standard, and require checkable verification (or pointers to verificati... |
| `/saaiasa` | self audit intent and speech acts | Classify utterances in a gate/procedure/document so the system doesn't answer the wrong thing (question vs command vs... |
| `/sacri` | self audit cross reference integrity | Ensure gates and procedures link to other procedures that provide the needed answer-interface and next steps. |
| `/sadrt` | self audit divergence risk test | Estimate where two independent executors would diverge when applying the same gate/procedure to the same input. |
| `/sads` | self audit detector sweep | Scan files for ambiguity, proxying, bundled questions, undefined terms, hidden conditionals, goal substitution, and c... |
| `/sagsca` | self audit gate schema consistency audit | Identify inconsistent gate field schemas across the library that increase interpretation burden and cause engine inte... |
| `/sapea` | self audit procedure executability audit | Check whether a procedure's questions/steps can be executed without interpretation and whether outputs are checkable. |
| `/saqrc` | self audit question rewrite chains | Rewrite unclear questions by separating intent ("what did I mean?") from the target question ("what do I want to answ... |
| `/saropc` | self audit rci on protocol choices | Apply Recursive Causal Interrogation to choices about what procedure to run, what to measure, and when to stop. |
| `/sarus` | self audit repo unclarity scan | Repo-wide scan to find question patterns that commonly require interpretation before answering. |
| `/satrda` | self audit two run divergence audit | Run the same gate/procedure twice on the same fixed input, compare outputs, and treat divergences as evidence that th... |
| `/sbfow` | still bad figure out why | Tests the rejected output against upstream/downstream criteria. Finds which criteria failed, diagnoses the root pattern, checks if you're repeating the same failed diagnosis. Derives what must change. |
| `/sdp` | software development procedures | Procedures for developing embedded software for robotics and |
| `/se` | space enumeration | Generate comprehensive lists by systematically covering all dimensions. |
| `/seb` | seo basics | Build organic search visibility through keyword research, on-page optimization, content strategy, and link building |
| `/sel` | selection | Make the final selection from ranked options after all analysis is complete. |
| `/sep` | security practices | Procedure for implementing security throughout the software development lifecycle |
| `/sf` | save file | Saves the most recent skill output to the library. For analytical skills, saves only the registry + synthesis (Phase 1 exploration is redundant with the registry). |
| `/shc` | system health check | Evaluate if the GOSM system needs improvement |
| `/ska` | skill acquisition | Systematically acquire new skills using deliberate practice principles |
| `/skb` | skill benchmarking | Identify quality standards, benchmark current skill level, and design deliberate practice to close gaps |
| `/skm` | stakeholder management | Engage stakeholders effectively throughout the project |
| `/skp` | skill plateaus | Diagnose the causes of skill plateaus and implement targeted strategies to break through |
| `/smc` | search methods comprehensive | An exhaustive inventory of search methods found in nature, science, |
| `/sms` | social media strategy | Build effective social media presence through platform selection, content planning, engagement, and measurement |
| `/sn` | salary negotiation | Systematic approach to negotiating job offers that maximizes total compensation |
| `/snp` | scenario planning | The future is uncertain. Instead of trying to predict the one future, |
| `/so` | structured output | Standardized output format for GOSM projects. |
| `/sop` | source prioritization | Given limited time to extract procedures from sources, prioritize which sources to process for maximum procedure value. |
| `/sor` | source research | GOSM Source Research procedure |
| `/spd` | space discovery | Discover what space exists BEFORE generating guesses. |
| `/spe` | search paradigm extensions | Extends the search paradigm to non-obvious domains. Identifies which search methods should become procedures. |
| `/spg` | specificity gate | Transform vague capability claims into specific ones by requiring trigger, procedure, output, and validation for each... |
| `/spp` | spatial proteomics | GOSM Spatial Proteomics procedure |
| `/spr` | spaced repetition | Design and implement spaced repetition systems for durable long-term retention of knowledge |
| `/src` | source credibility | Procedure for evaluating the credibility and reliability of any information source |
| `/srd` | strategic deception | Orderings for legitimate competitive, adversarial, and performance contexts |
| `/ssr` | session review | Capture learnings at end of session for continuous improvement. |
| `/st` | strategy templates | Every strategy exists within a game (competitive context). Every game |
| `/sta` | statistical analysis | Systematic procedure for selecting appropriate statistical tests and correctly interpreting results |
| `/stc` | steelmanned counterarguments | GOSM Steelmanned Counterarguments procedure |
| `/std` | strategy discovery | Find or create an approach to achieve a goal |
| `/stg` | steps generation | Transform a COMPLETE_PLAN into foolproof executable step-by-step instructions |
| `/stl` | storytelling | Systematic procedure for crafting and delivering compelling stories that create emotional connection and drive action |
| `/svs` | systematic variation scamper | SCAMPER is an acronym for 7 transformation operations: |
| `/swa` | swot analysis | Systematically identify Strengths, Weaknesses, Opportunities, and Threats to inform strategic decisions |
| `/sya` | systems analysis | Analyze complex systems using causal loop diagrams, stock and flow models, feedback loop identification, and system a... |
| `/sym` | system modeling | Real problems exist in complex systems with many interacting parts. |
| `/t` | targeting | Build comprehensive database of advocacy targets with personalized dossiers |
| `/td` | time deadline | Orderings driven by temporal constraints, deadlines, and timing |
| `/tnt` | tension navigation tactics | While value_conflict_decomposition provides the framework for understanding conflicts, |
| `/to` | topological ordering | Generate valid execution sequences from dependencies. |
| `/tp` | truth propagation | Arguments don't exist in isolation. Each conclusion depends on premises, |
| `/tpm` | template maintenance | Maintain and improve domain templates over time. Track usage, identify gaps, and evolve templates based on experience. |
| `/tr` | template registry | Registry for domain templates. Store, retrieve, search, and manage domain-specific configurations. |
| `/ts` | testing strategy | Procedure for designing and implementing effective software testing strategies |
| `/txm` | taxonomy maintenance | Systematic process for creating, updating, and maintaining taxonomies and classification systems. |
| `/u` | universalize | Extract the complete space of assumptions, dimensions, and alternatives from any claim. |
| `/uaua` | universalize araw universalize araw | Full space mapping + rigorous testing. Maps the space, tests candidates, finds edge cases, validates survivors. |
| `/uga` | universal goal analysis | The comprehensive question framework that applies to EVERY goal, regardless of domain. Universal analysis procedure. |
| `/ugav2` | universal goal analysis v2 | The comprehensive question framework that applies to EVERY goal, regardless of domain. |
| `/ugav3` | universal goal analysis v3 | The comprehensive question framework that applies to EVERY goal, regardless of domain. |
| `/ugav4` | universal goal analysis v4 | The comprehensive question framework that applies to EVERY goal, regardless of domain. |
| `/ugav5` | universal goal analysis v5 | The comprehensive question framework that applies to EVERY goal, regardless of domain. |
| `/unx` | unexpected | Find non-obvious solutions. |
| `/uo` | unassailable output | Every output must be unassailable. Anything said can and will |
| `/va` | variation analysis | For any obvious strategy, ask what if we did the exact opposite. |
| `/val` | validation | Verify that an output meets its requirements |
| `/vbo` | verification before output | This procedure is the culmination of the no-guessing philosophy. |
| `/vcd` | value conflict decomposition | Goals often serve multiple intrinsic values that conflict with each other. |
| `/ve` | value elicitation | Value elicitation discovers what someone ACTUALLY values - their intrinsic goals. |
| `/ver` | verify | Verify claims using the GOSM verification standard. Every claim must be OBSERVED, TESTED, or DERIVED - never guessed. |
| `/vhd` | vertical horizontal decision | Framework for deciding when to improve existing procedures/categories (vertical) |
| `/vm` | viral mechanics | Design and optimize viral loops, referral programs, and word-of-mouth triggers to achieve organic growth |
| `/vp` | verification procedures | Procedures for systematically testing and verifying that systems meet |
| `/w` | write | Criteria-based writing with hierarchical upstream/downstream checks. Upstream (question, recognition, advancement, momentum, non-skippability, reader-drawn conclusion) must pass before downstream (scope, voice, weak patterns, verification). |
| `/wr` | weekly review | Weekly review procedure to maintain visibility across all active projects, identify stalled work, and ensure continuo... |
| `/wt` | want to | Assumes the want is right — traces what it commits you to, what it requires, what paths it opens. Finds the actual want vs stated want. |

## Documentation

```
docs/
├── methodology/
├── examples/
├── reference/
├── universal/
├── gates/
├── procedures/
│   ├── core/
│   │   └── ordering/
│   ├── communication/
│   └── meta/
└── previous-approaches/
    ├── deductive-strategy/
    ├── pure-regress/
    └── swot-pure-regress/
```

## License

Apache-2.0

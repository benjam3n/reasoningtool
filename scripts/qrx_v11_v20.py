#!/usr/bin/env python3
"""QRX extraction for pure regress v11-v20: merge, dedup, write questions/routes/chains/regresses."""
import json, os, random

QR = "/home/ben/Documents/projects/questionroute/data"

# Load existing IDs
existing_ids = set()
for f in os.listdir(f"{QR}/questions"):
    if f.endswith(".json"):
        existing_ids.add(f[:-5])

print(f"Existing questions: {len(existing_ids)}")

# All extracted questions from 4 agents, merged and deduped
# When duplicates exist across agents, keep the first/best version
questions = [
    # === v11-v13 (24) ===
    {"id":"finite","text":"Finite?","definition":"Searches for whether a search space or goal has a bounded, completable extent","semanticType":"evaluation","abstractionLevel":3,"slots":["search space"],"tags":["boundedness","termination","seeking","completeness"]},
    {"id":"bounded","text":"Bounded?","definition":"Searches for whether a scope or domain has practical limits that make it tractable","semanticType":"condition","abstractionLevel":3,"slots":["domain"],"tags":["constraints","tractability","scope","limits"]},
    {"id":"ultimate","text":"Ultimate?","definition":"Searches for whether a final, unsurpassable version of something exists or is coherent","semanticType":"existence","abstractionLevel":4,"slots":["goal"],"tags":["finality","perfection","seeking","regress"]},
    {"id":"peaks","text":"Peaks?","definition":"Searches for the structure of peak experiences and whether they form a coherent ongoing strategy","semanticType":"evaluation","abstractionLevel":3,"slots":["experience"],"tags":["peaks","dopamine","momentary","pursuit"]},
    {"id":"macro","text":"Macro?","definition":"Searches for the large-scale endpoint or resolution that would signal a search is truly complete","semanticType":"identity","abstractionLevel":4,"slots":["completion"],"tags":["macro","closure","contentment","finality"]},
    {"id":"micro","text":"Micro?","definition":"Searches for small-scale, local satisfactions that sustain ongoing activity without resolving it","semanticType":"identity","abstractionLevel":3,"slots":["satisfaction"],"tags":["micro","reward","local-optimum","sustaining"]},
    {"id":"outsource","text":"Outsource?","definition":"Searches for whether delegating thinking to an external agent genuinely completes a search or merely adds a layer","semanticType":"method","abstractionLevel":3,"slots":["agent"],"tags":["delegation","avoidance","completion","responsibility"]},
    {"id":"stillness","text":"Stillness?","definition":"Searches for what is present or available when seeking activity fully ceases","semanticType":"existence","abstractionLevel":4,"slots":["self"],"tags":["stillness","presence","non-seeking","being"]},
    {"id":"feeding","text":"Feeding?","definition":"Searches for which actions reinforce or strengthen a behavioral loop and which allow it to weaken","semanticType":"causation","abstractionLevel":3,"slots":["behavior"],"tags":["reinforcement","habit","seeking","loop"]},
    {"id":"captured","text":"Captured?","definition":"Searches for whether an agent is stuck in a local optimum, mistaking familiar motion for genuine progress","semanticType":"condition","abstractionLevel":3,"slots":["method"],"tags":["capture","local-optimum","fake-seeking","stagnation"]},
    {"id":"testing","text":"Testing?","definition":"Searches for whether hypotheses are being subjected to reality-contact that could falsify or confirm them","semanticType":"method","abstractionLevel":2,"slots":["hypothesis"],"tags":["testing","empiricism","reality","falsifiability"]},
    {"id":"accumulated","text":"Accumulated?","definition":"Searches for whether repeated attempts have produced compounding knowledge or merely a count of failures","semanticType":"evaluation","abstractionLevel":3,"slots":["attempts"],"tags":["accumulation","learning","compounding","attempts"]},
    {"id":"applying","text":"Applying?","definition":"Searches for whether a developed method or tool is actually being used on its intended target domain","semanticType":"existence","abstractionLevel":2,"slots":["method"],"tags":["application","use","gap","implementation"]},
    {"id":"maybeland","text":"Maybeland?","definition":"Searches for the zone of perpetual undecidedness where no test is committed to and possibilities remain open to avoid resolution","semanticType":"location","abstractionLevel":3,"slots":["commitment"],"tags":["avoidance","ambiguity","commitment","fake-seeking"]},
    {"id":"seeker","text":"Seeker?","definition":"Searches for whether the identity of the one seeking is constituted by the seeking itself and would dissolve if seeking stopped","semanticType":"identity","abstractionLevel":5,"slots":["self"],"tags":["identity","self","seeking","dissolution"]},
    {"id":"original","text":"Original?","definition":"Searches for the founding need or event that initiated a persistent pattern before it became habitual","semanticType":"temporal","abstractionLevel":4,"slots":["need"],"tags":["origin","need","history","motivation"]},
    {"id":"unstrategizable","text":"Unstrategizable?","definition":"Searches for whether the target of effort belongs to a category of things that cannot be reached by deliberate strategy","semanticType":"condition","abstractionLevel":4,"slots":["goal"],"tags":["strategy","limits","seeking","category-error"]},
    {"id":"releasing","text":"Releasing?","definition":"Searches for the non-strategic act of letting go of a need without having satisfied it or defeated it","semanticType":"method","abstractionLevel":4,"slots":["need"],"tags":["release","letting-go","non-strategic","acceptance"]},
    {"id":"noticing","text":"Noticing?","definition":"Searches for what is present in direct awareness prior to interpretation or conceptual framing","semanticType":"existence","abstractionLevel":2,"slots":["awareness"],"tags":["noticing","presence","direct-experience","attention"]},
    {"id":"dragons","text":"Dragons?","definition":"Searches for the genuinely unknown things in unexplored territory that would change everything if encountered","semanticType":"existence","abstractionLevel":4,"slots":["unknown"],"tags":["unknown","discovery","avoidance","territory"]},

    # === v14-v16 (24) ===
    {"id":"fake","text":"Fake?","definition":"Searches for whether something is genuinely what it appears to be or is a simulation of the real thing","semanticType":"identity","abstractionLevel":3,"slots":["activity"],"tags":["authenticity","self-deception","seeking","pattern"]},
    {"id":"relevant","text":"Relevant?","definition":"Searches for what connects to or bears on something a person genuinely cares about","semanticType":"relation","abstractionLevel":3,"slots":["item"],"tags":["scope","significance","filtering","care"]},
    {"id":"phenomenology","text":"Phenomenology?","definition":"Searches for the felt quality of an experience from the inside rather than its mechanism or external description","semanticType":"identity","abstractionLevel":5,"slots":["experience"],"tags":["experience","felt-sense","introspection","subjectivity"]},
    {"id":"compelled","text":"Compelled?","definition":"Searches for whether a behavior arises from genuine choice or from an inability to do otherwise","semanticType":"condition","abstractionLevel":3,"slots":["agent"],"tags":["agency","compulsion","freedom","seeking"]},
    {"id":"chosen","text":"Chosen?","definition":"Searches for whether an activity is freely selected versus compelled or defaulted into","semanticType":"condition","abstractionLevel":3,"slots":["agent"],"tags":["agency","freedom","volition","identity"]},
    {"id":"sufficient","text":"Sufficient?","definition":"Searches for what level of understanding or capability is adequate for a specific purpose","semanticType":"evaluation","abstractionLevel":3,"slots":["resource"],"tags":["adequacy","termination","purpose","goal"]},
    {"id":"termination","text":"Termination?","definition":"Searches for the condition under which a process or search legitimately ends","semanticType":"condition","abstractionLevel":4,"slots":["process"],"tags":["ending","goal","infinite-regress","completion"]},
    {"id":"treadmill","text":"Treadmill?","definition":"Searches for whether effort produces genuine progress or merely maintains position as the space expands","semanticType":"evaluation","abstractionLevel":3,"slots":["effort"],"tags":["progress","futility","self-amplifying","seeking"]},
    {"id":"amplifying","text":"Amplifying?","definition":"Searches for whether a process increases the very need it is meant to satisfy","semanticType":"causation","abstractionLevel":4,"slots":["process"],"tags":["feedback-loop","self-reinforcing","seeking","growth"]},
    {"id":"transferred","text":"Transferred?","definition":"Searches for whether understanding or insight can genuinely move from one person to another or must be individually arrived at","semanticType":"possibility","abstractionLevel":4,"slots":["understanding"],"tags":["understanding","transmission","knowledge","insight"]},
    {"id":"continuous","text":"Continuous?","definition":"Searches for whether a process runs without interruption or rest throughout a person's waking life","semanticType":"temporal","abstractionLevel":2,"slots":["process"],"tags":["analysis","rest","load","exhaustion"]},
    {"id":"depleting","text":"Depleting?","definition":"Searches for whether a valued activity carries a hidden energy cost that accumulates over time","semanticType":"causation","abstractionLevel":3,"slots":["activity"],"tags":["energy","cost","sustainability","analysis"]},
    {"id":"threatening","text":"Threatening?","definition":"Searches for why a state of not-knowing feels dangerous rather than merely uncomfortable or neutral","semanticType":"evaluation","abstractionLevel":3,"slots":["state"],"tags":["threat","uncertainty","fear","not-knowing"]},
    {"id":"defeating","text":"Defeating?","definition":"Searches for the specific felt meaning of being defeated as distinct from failing, giving up, or being threatened","semanticType":"identity","abstractionLevel":2,"slots":["felt-state"],"tags":["defeat","emotion","phenomenology","meaning"]},
    {"id":"converging","text":"Converging?","definition":"Searches for whether a search or learning process is narrowing toward resolution or diverging further from it over time","semanticType":"temporal","abstractionLevel":3,"slots":["process"],"tags":["progress","divergence","resolution","seeking"]},
    {"id":"pointing","text":"Pointing?","definition":"Searches for whether directing attention toward something helps a person look or distracts them from genuine seeing","semanticType":"evaluation","abstractionLevel":4,"slots":["guide"],"tags":["attention","guidance","distraction","insight"]},
    {"id":"meaningful","text":"Meaningful?","definition":"Searches for what distinguishes a question or action that matters from one that merely circulates without consequence","semanticType":"evaluation","abstractionLevel":4,"slots":["question"],"tags":["meaning","significance","questions","purpose"]},
    {"id":"circling","text":"Circling?","definition":"Searches for whether a chain of reasoning is returning to its starting point rather than making genuine forward progress","semanticType":"evaluation","abstractionLevel":3,"slots":["reasoning"],"tags":["circular","progress","regress","pattern"]},
    {"id":"unasked","text":"Unasked?","definition":"Searches for the question that neither party in an inquiry has yet thought to pose, where the answer may actually reside","semanticType":"existence","abstractionLevel":5,"slots":["inquiry"],"tags":["blind-spot","meta-inquiry","assumption","discovery"]},
    {"id":"unseen","text":"Unseen?","definition":"Searches for what is so taken for granted in an argument or situation that it has not been recognized as a claim at all","semanticType":"existence","abstractionLevel":4,"slots":["claim"],"tags":["blind-spot","assumption","meta-cognition","presupposition"]},
    {"id":"stopping","text":"Stopping?","definition":"Searches for what genuinely stopping a search would look like and how it differs from giving up or failing","semanticType":"identity","abstractionLevel":3,"slots":["process"],"tags":["ending","giving-up","choice","seeking"]},

    # === v17-v18 (68) — deduplicated ===
    {"id":"capture","text":"Capture?","definition":"Searches for the process by which attention or inquiry becomes fixed on a single method, losing flexibility","semanticType":"causation","abstractionLevel":3,"slots":["mechanism"],"tags":["fixation","seeking","method","trap"]},
    {"id":"gradual","text":"Gradual?","definition":"Searches for whether a transition or change happens incrementally rather than at a discrete moment","semanticType":"temporal","abstractionLevel":2,"slots":["process"],"tags":["change","time","threshold","transition"]},
    {"id":"answerable","text":"Answerable?","definition":"Searches for whether a given question admits of a genuine, satisfying answer or is structurally unanswerable","semanticType":"possibility","abstractionLevel":3,"slots":["question"],"tags":["epistemics","closure","inquiry","limits"]},
    {"id":"saying","text":"Saying?","definition":"Searches for the relationship between verbal expression and underlying being, asking whether what is said captures what is","semanticType":"relation","abstractionLevel":4,"slots":["expression"],"tags":["language","identity","representation","authenticity"]},
    {"id":"defeated","text":"Defeated?","definition":"Searches for what defeat means as an inner state and whether it is a thought, a feeling, or a settled orientation","semanticType":"identity","abstractionLevel":2,"slots":["state"],"tags":["emotion","failure","cognition","self"]},
    {"id":"relevance","text":"Relevance?","definition":"Searches for what makes something count as relevant to a goal or inquiry and whether relevance expands with exploration","semanticType":"evaluation","abstractionLevel":3,"slots":["criteria"],"tags":["selection","criteria","scope","inquiry"]},
    {"id":"standards","text":"Standards?","definition":"Searches for the origin, nature, and changeability of the criteria one uses to evaluate actions or understanding","semanticType":"causation","abstractionLevel":3,"slots":["criteria"],"tags":["evaluation","norms","identity","origin"]},
    {"id":"continuity","text":"Continuity?","definition":"Searches for what sustains the sense of being the same entity through change over time","semanticType":"identity","abstractionLevel":4,"slots":["self"],"tags":["identity","memory","persistence","time"]},
    {"id":"projection","text":"Projection?","definition":"Searches for whether one's perception of a situation is distorted by attributing one's own patterns to it","semanticType":"causation","abstractionLevel":3,"slots":["pattern"],"tags":["bias","self-awareness","inference","error"]},
    {"id":"movement","text":"Movement?","definition":"Searches for whether activity or change in direction constitutes genuine progress or is merely undirected motion","semanticType":"evaluation","abstractionLevel":3,"slots":["direction"],"tags":["progress","action","direction","change"]},
    {"id":"looking","text":"Looking?","definition":"Searches for whether there is a mode of open attention that lacks the object-directedness of seeking","semanticType":"method","abstractionLevel":3,"slots":["attention"],"tags":["attention","openness","seeking","method"]},
    {"id":"win","text":"Win?","definition":"Searches for what counts as a genuine win or success in a domain where the goal is unclear","semanticType":"evaluation","abstractionLevel":2,"slots":["goal"],"tags":["success","achievement","criteria","motivation"]},
    {"id":"constrain","text":"Constrain?","definition":"Searches for what limits a person's range of action or being and whether those limits are removable or constitutive","semanticType":"causation","abstractionLevel":3,"slots":["limit"],"tags":["limits","agency","change","identity"]},
    {"id":"deciding","text":"Deciding?","definition":"Searches for whether deciding is a genuine mental act distinct from simply doing, or a retrospective story about behavior","semanticType":"identity","abstractionLevel":4,"slots":["agency"],"tags":["agency","will","action","narrative"]},
    {"id":"story","text":"Story?","definition":"Searches for whether experience, identity, and meaning are fundamentally narrative constructions rather than direct encounters with reality","semanticType":"identity","abstractionLevel":5,"slots":["narrative"],"tags":["narrative","construction","identity","meaning"]},
    {"id":"raw","text":"Raw?","definition":"Searches for whether unmediated, uninterpreted experience is possible or whether all experience arrives already processed","semanticType":"existence","abstractionLevel":5,"slots":["experience"],"tags":["phenomenology","experience","interpretation","access"]},
    {"id":"processed","text":"Processed?","definition":"Searches for what transforms raw sensation into experience and whether the transformation can be observed or bypassed","semanticType":"causation","abstractionLevel":5,"slots":["experience"],"tags":["cognition","experience","mediation","phenomenology"]},
    {"id":"contradiction","text":"Contradiction?","definition":"Searches for whether contradiction is a feature of reality or a failure of language and mind to represent it","semanticType":"existence","abstractionLevel":5,"slots":["logic"],"tags":["logic","language","reality","limits"]},
    {"id":"control","text":"Control?","definition":"Searches for whether genuine control over thoughts, actions, or outcomes is possible or an attributed illusion","semanticType":"existence","abstractionLevel":4,"slots":["agency"],"tags":["agency","will","causation","illusion"]},
    {"id":"agent","text":"Agent?","definition":"Searches for whether there is a genuine entity that acts, or only a process to which agency is retrospectively attributed","semanticType":"existence","abstractionLevel":5,"slots":["entity"],"tags":["agency","identity","causation","philosophy"]},
    {"id":"locatable","text":"Locatable?","definition":"Searches for whether the self, mind, or any experiential entity can be assigned a specific location","semanticType":"location","abstractionLevel":5,"slots":["self"],"tags":["identity","mind","body","space"]},
    {"id":"seeming","text":"Seeming?","definition":"Searches for whether appearance constitutes its own kind of reality and whether seeming is sufficient for experience","semanticType":"existence","abstractionLevel":5,"slots":["appearance"],"tags":["phenomenology","reality","appearance","sufficiency"]},
    {"id":"satisfaction","text":"Satisfaction?","definition":"Searches for whether genuine satisfaction differs from the feeling of satisfaction and what makes it real rather than apparent","semanticType":"evaluation","abstractionLevel":3,"slots":["feeling"],"tags":["wellbeing","feeling","reality","sufficiency"]},
    {"id":"thought","text":"Thought?","definition":"Searches for what a thought is as an entity — its location, duration, edges, and whether it is held by something or just occurs","semanticType":"identity","abstractionLevel":5,"slots":["entity"],"tags":["cognition","mind","phenomenology","identity"]},
    {"id":"letting","text":"Letting?","definition":"Searches for whether letting go is a distinct act of doing or a form of non-doing and what the difference implies for agency","semanticType":"identity","abstractionLevel":4,"slots":["action"],"tags":["agency","release","action","doing"]},
    {"id":"voice","text":"Voice?","definition":"Searches for what the inner voice is — whose it is, whether it is the self or something happening to the self","semanticType":"identity","abstractionLevel":4,"slots":["self"],"tags":["identity","inner-speech","self","phenomenology"]},
    {"id":"soul","text":"Soul?","definition":"Searches for whether there is something beyond body and mind that constitutes the self and how such a thing would be known","semanticType":"existence","abstractionLevel":5,"slots":["self"],"tags":["metaphysics","identity","transcendence","self"]},
    {"id":"space","text":"Space?","definition":"Searches for whether space is a real medium in which things exist or a concept imposed on relational structure","semanticType":"existence","abstractionLevel":5,"slots":["medium"],"tags":["metaphysics","reality","relation","concept"]},
    {"id":"introspect","text":"Introspect?","definition":"Searches for whether introspection is a reliable form of perception directed at an actual object or a process without genuine target","semanticType":"method","abstractionLevel":4,"slots":["perception"],"tags":["self-knowledge","perception","reliability","method"]},
    {"id":"meditation","text":"Meditation?","definition":"Searches for whether meditation represents a genuine alternative to seeking — a mode of contentless or objectless awareness","semanticType":"method","abstractionLevel":3,"slots":["attention"],"tags":["practice","attention","seeking","alternative"]},
    {"id":"understanding","text":"Understanding?","definition":"Searches for what understanding is, how it is distinguished from feeling and from knowledge, and how one knows when it has occurred","semanticType":"identity","abstractionLevel":4,"slots":["knowledge"],"tags":["cognition","knowledge","epistemics","feeling"]},
    {"id":"knowledge","text":"Knowledge?","definition":"Searches for what knowledge consists of and whether it requires embodied or experiential grounding","semanticType":"identity","abstractionLevel":5,"slots":["truth"],"tags":["epistemics","truth","mind","embodiment"]},
    {"id":"meaning","text":"Meaning?","definition":"Searches for where meaning resides — in the speaker, listener, words, context, or nowhere — and whether it is made or found","semanticType":"location","abstractionLevel":5,"slots":["location"],"tags":["language","meaning","construction","relation"]},
    {"id":"communication","text":"Communication?","definition":"Searches for whether genuine transmission of meaning between parties is possible or whether exchanges are always partially misaligned","semanticType":"possibility","abstractionLevel":4,"slots":["meaning"],"tags":["language","understanding","relation","limits"]},
    {"id":"formulating","text":"Formulating?","definition":"Searches for whether making a question explicit changes the question and whether formulation is the same as or different from answering","semanticType":"method","abstractionLevel":4,"slots":["question"],"tags":["inquiry","language","clarification","implicit"]},
    {"id":"intuition","text":"Intuition?","definition":"Searches for whether intuition is a reliable access route to understanding that bypasses formulation","semanticType":"method","abstractionLevel":3,"slots":["knowledge"],"tags":["cognition","access","feeling","reliability"]},
    {"id":"nature","text":"Nature?","definition":"Searches for whether a person has an unchangeable essence or whether all of what one is remains open to transformation","semanticType":"identity","abstractionLevel":4,"slots":["essence"],"tags":["identity","essence","change","determinism"]},
    {"id":"direction","text":"Direction?","definition":"Searches for whether one's movement through life or inquiry has genuine directedness or is undirected motion that merely appears purposeful","semanticType":"existence","abstractionLevel":3,"slots":["movement"],"tags":["purpose","movement","goal","agency"]},
    {"id":"territory","text":"Territory?","definition":"Searches for whether exploration presupposes a definite domain to be traversed and what constitutes the territory of inquiry","semanticType":"existence","abstractionLevel":3,"slots":["domain"],"tags":["exploration","domain","metaphor","inquiry"]},
    {"id":"guidance","text":"Guidance?","definition":"Searches for whether movement and behavior are governed by something visible and if not, what unseen structure might be operating","semanticType":"causation","abstractionLevel":3,"slots":["direction"],"tags":["direction","agency","invisible","cause"]},
    {"id":"inference","text":"Inference?","definition":"Searches for whether drawing conclusions from patterns constitutes genuine knowledge of underlying causes or merely projection","semanticType":"method","abstractionLevel":4,"slots":["evidence"],"tags":["reasoning","evidence","epistemics","bias"]},
    {"id":"wanting","text":"Wanting?","definition":"Searches for whether wanting is always a form of seeking or whether there is a mode of wanting that coexists with acceptance","semanticType":"identity","abstractionLevel":3,"slots":["desire"],"tags":["desire","seeking","motivation","acceptance"]},
    {"id":"perspective","text":"Perspective?","definition":"Searches for what perspective is — whether there is a point from which viewing happens and whether experience requires perspectival structure","semanticType":"identity","abstractionLevel":5,"slots":["viewpoint"],"tags":["phenomenology","viewpoint","experience","mind"]},
    {"id":"embodiment","text":"Embodiment?","definition":"Searches for whether the body is necessary for knowledge, experience, and mind and what would remain without it","semanticType":"condition","abstractionLevel":5,"slots":["body"],"tags":["body","mind","knowledge","necessity"]},
    {"id":"death","text":"Death?","definition":"Searches for what death ends — body, mind, self — and whether anything of the person persists or continues afterward","semanticType":"existence","abstractionLevel":4,"slots":["end"],"tags":["mortality","self","continuation","body"]},
    {"id":"literal","text":"Literal?","definition":"Searches for whether any expression provides direct, non-metaphorical access to what it refers to or whether everything is metaphor","semanticType":"existence","abstractionLevel":5,"slots":["language"],"tags":["language","metaphor","access","reference"]},
    {"id":"logic","text":"Logic?","definition":"Searches for whether logic is about reality, language, or mind and whether it is discovered or a consistent game with rules","semanticType":"identity","abstractionLevel":5,"slots":["reality"],"tags":["reasoning","reality","language","foundation"]},
    {"id":"hope","text":"Hope?","definition":"Searches for what hope is as a psychological state and what function it serves in sustaining seeking or action","semanticType":"identity","abstractionLevel":3,"slots":["state"],"tags":["emotion","future","motivation","uncertainty"]},
    {"id":"agency","text":"Agency?","definition":"Searches for whether free, uncaused choice is real or whether all action is determined by prior causes leaving no genuine authorship","semanticType":"existence","abstractionLevel":5,"slots":["will"],"tags":["freewill","causation","choice","determinism"]},
    {"id":"novelty","text":"Novelty?","definition":"Searches for whether genuine newness is possible and whether novelty carries meaning that repetition lacks","semanticType":"existence","abstractionLevel":4,"slots":["newness"],"tags":["change","meaning","repetition","creativity"]},
    {"id":"mathematics","text":"Mathematics?","definition":"Searches for whether mathematics is discovered or invented and whether it describes or creates the reality it appears to govern","semanticType":"identity","abstractionLevel":5,"slots":["discovery"],"tags":["abstraction","reality","discovery","structure"]},
    {"id":"significance","text":"Significance?","definition":"Searches for whether significance is assigned by minds or arises from nowhere as self-generating meaning","semanticType":"causation","abstractionLevel":5,"slots":["meaning"],"tags":["meaning","value","source","construction"]},
    {"id":"observation","text":"Observation?","definition":"Searches for whether observation provides raw data or already-cooked knowledge and whether it is sufficient grounds for knowing","semanticType":"method","abstractionLevel":4,"slots":["perception"],"tags":["epistemics","perception","evidence","processing"]},
    {"id":"ending","text":"Ending?","definition":"Searches for whether ending a process constitutes completion, abandonment, or simply stopping and whether these are genuinely different","semanticType":"identity","abstractionLevel":3,"slots":["completion"],"tags":["completion","process","closure","stopping"]},
    {"id":"sharing","text":"Sharing?","definition":"Searches for whether meaning, experience, or understanding can genuinely be shared between parties in an exchange","semanticType":"possibility","abstractionLevel":4,"slots":["meaning"],"tags":["communication","meaning","relation","limits"]},
    {"id":"reference","text":"Reference?","definition":"Searches for whether words reach the things they point to or only reach other words and whether language is closed to world","semanticType":"relation","abstractionLevel":5,"slots":["word"],"tags":["language","meaning","reality","gap"]},
    {"id":"order","text":"Order?","definition":"Searches for whether order is discovered in reality or imposed upon it by mind","semanticType":"existence","abstractionLevel":5,"slots":["structure"],"tags":["structure","reality","mind","discovery"]},
    {"id":"repetition","text":"Repetition?","definition":"Searches for whether exact repetition is possible and whether repetition in inquiry constitutes depth, avoidance, or meaning-making","semanticType":"existence","abstractionLevel":4,"slots":["same"],"tags":["pattern","time","meaning","inquiry"]},
    {"id":"world","text":"World?","definition":"Searches for whether world denotes everything or a part and what the relation is between world and larger containing structures","semanticType":"identity","abstractionLevel":5,"slots":["totality"],"tags":["metaphysics","totality","reality","scope"]},
    {"id":"person","text":"Person?","definition":"Searches for what makes a person — whether personhood is biological, psychological, legal, or none of these","semanticType":"identity","abstractionLevel":5,"slots":["definition"],"tags":["identity","self","ontology","definition"]},
    {"id":"pain","text":"Pain?","definition":"Searches for whether pain is a raw unmediated signal or a story and whether all seeking is ultimately flight from some underlying pain","semanticType":"causation","abstractionLevel":3,"slots":["experience"],"tags":["emotion","motivation","avoidance","experience"]},
    {"id":"authenticity","text":"Authenticity?","definition":"Searches for what it means to be authentic — true to a self — and whether a stable true self exists to be true to","semanticType":"identity","abstractionLevel":4,"slots":["self"],"tags":["identity","self","truth","ethics"]},
    {"id":"boundary","text":"Boundary?","definition":"Searches for whether boundaries between inside and outside, self and world, are real features or decisions imposed on a continuum","semanticType":"existence","abstractionLevel":4,"slots":["limit"],"tags":["distinction","real","construction","limit"]},

    # === v19-v20 (selected non-duplicates) ===
    {"id":"selfless","text":"Selfless?","definition":"Searches for whether pointing or action can occur without a self as its source or agent","semanticType":"existence","abstractionLevel":5,"slots":["agent"],"tags":["selfhood","pointing","agentlessness","phenomenology"]},
    {"id":"unity","text":"Unity?","definition":"Searches for whether difference can collapse into oneness and what that oneness would constitute","semanticType":"identity","abstractionLevel":5,"slots":["one"],"tags":["monism","difference","wholeness","metaphysics"]},
    {"id":"desire","text":"Desire?","definition":"Searches for what desire is and whether it is the engine driving seeking, questioning, and all directed activity","semanticType":"causation","abstractionLevel":4,"slots":["engine"],"tags":["motivation","seeking","phenomenology","intentionality"]},
    {"id":"desireless","text":"Desireless?","definition":"Searches for whether a mind or agent can operate without any desire and what such a state would entail","semanticType":"possibility","abstractionLevel":5,"slots":["mind"],"tags":["desire","freedom","mind","Buddhism"]},
    {"id":"active","text":"Active?","definition":"Searches for what makes something active as opposed to passive and whether the distinction is real","semanticType":"identity","abstractionLevel":4,"slots":["activity"],"tags":["agency","change","ontology","being"]},
    {"id":"passive","text":"Passive?","definition":"Searches for whether pure passivity exists or whether everything contains some activity","semanticType":"existence","abstractionLevel":4,"slots":["passivity"],"tags":["agency","being","ontology","rest"]},
    {"id":"selfsameness","text":"Selfsameness?","definition":"Searches for what it means for a thing to be identical with itself and whether identity persists through time","semanticType":"identity","abstractionLevel":5,"slots":["identity"],"tags":["identity","persistence","time","logic"]},
    {"id":"constant","text":"Constant?","definition":"Searches for whether anything remains unchanged across time in a changing world","semanticType":"existence","abstractionLevel":4,"slots":["unchanging"],"tags":["permanence","change","stability","metaphysics"]},
    {"id":"instantaneous","text":"Instantaneous?","definition":"Searches for what an instant is, whether it has duration, and whether it is a real unit of time or a concept","semanticType":"identity","abstractionLevel":4,"slots":["instant"],"tags":["time","duration","ontology","mathematics"]},
    {"id":"thinking","text":"Thinking?","definition":"Searches for what thinking is and whether it is identical to or distinct from questioning and concept use","semanticType":"identity","abstractionLevel":4,"slots":["thought"],"tags":["cognition","mind","questioning","epistemology"]},
    {"id":"clarity","text":"Clarity?","definition":"Searches for what clarity is, whether it is achievable, and whether questioning produces or obscures it","semanticType":"evaluation","abstractionLevel":3,"slots":["understanding"],"tags":["understanding","epistemology","questioning","truth"]},
    {"id":"appearance","text":"Appearance?","definition":"Searches for what appearance is, whether it differs from reality, and whether there are degrees of realness between them","semanticType":"identity","abstractionLevel":4,"slots":["seeming"],"tags":["phenomenology","reality","illusion","epistemology"]},
    {"id":"persistence","text":"Persistence?","definition":"Searches for what makes something persist and whether persistence is what distinguishes more real from less real","semanticType":"causation","abstractionLevel":4,"slots":["duration"],"tags":["time","identity","ontology","permanence"]},
    {"id":"tautology","text":"Tautology?","definition":"Searches for whether tautologies say anything meaningful or are empty truths with no informational content","semanticType":"evaluation","abstractionLevel":4,"slots":["meaning"],"tags":["logic","truth","meaning","language"]},
    {"id":"totality","text":"Totality?","definition":"Searches for whether totality is real, whether it can be experienced by a part, and whether it can be reported","semanticType":"existence","abstractionLevel":5,"slots":["whole"],"tags":["wholeness","ontology","experience","metaphysics"]},
    {"id":"silence","text":"Silence?","definition":"Searches for what silence is, whether it constitutes a report of totality, and whether it is a presence or an absence","semanticType":"identity","abstractionLevel":4,"slots":["absence"],"tags":["silence","absence","language","phenomenology"]},
    {"id":"observer","text":"Observer?","definition":"Searches for whether an observer is necessary for observation or whether impersonal observing can occur without one","semanticType":"existence","abstractionLevel":4,"slots":["observing"],"tags":["subjectivity","consciousness","phenomenology","epistemology"]},
    {"id":"source","text":"Source?","definition":"Searches for whether there is a findable source of questioning and of reality itself","semanticType":"causation","abstractionLevel":5,"slots":["origin"],"tags":["origin","causation","seeking","metaphysics"]},
    {"id":"path","text":"Path?","definition":"Searches for whether a path to source or understanding exists or whether path is only a metaphor for seeking","semanticType":"existence","abstractionLevel":4,"slots":["direction"],"tags":["seeking","direction","metaphor","spirituality"]},
    {"id":"emergent","text":"Emergent?","definition":"Searches for whether direction or meaning can arise from complexity without being designed","semanticType":"existence","abstractionLevel":4,"slots":["complexity"],"tags":["emergence","complexity","causation","systems"]},
    {"id":"criterion","text":"Criterion?","definition":"Searches for what makes something a valid criterion for reality and whether criteria are found or made","semanticType":"identity","abstractionLevel":4,"slots":["standard"],"tags":["epistemology","evaluation","truth","standard"]},
    {"id":"permanence","text":"Permanence?","definition":"Searches for whether permanence exists or whether it is an illusion in a world of constant change","semanticType":"existence","abstractionLevel":4,"slots":["unchanging"],"tags":["permanence","change","time","ontology"]},
    {"id":"witness","text":"Witness?","definition":"Searches for whether there is an unchanging witnessing presence separate from the changing contents of experience","semanticType":"existence","abstractionLevel":5,"slots":["stable"],"tags":["consciousness","observer","phenomenology","self"]},
    {"id":"separation","text":"Separation?","definition":"Searches for whether genuine separation exists between witness and witnessed, self and world, or experiencer and experience","semanticType":"existence","abstractionLevel":5,"slots":["division"],"tags":["duality","consciousness","relation","metaphysics"]},
    {"id":"goalless","text":"Goalless?","definition":"Searches for whether seeking or questioning can be genuinely goalless and what that would mean for the activity","semanticType":"possibility","abstractionLevel":4,"slots":["seeking"],"tags":["goal","seeking","intention","questioning"]},
    {"id":"peace","text":"Peace?","definition":"Searches for what peace is, whether it is a real achievable state, and whether questioning leads toward or away from it","semanticType":"identity","abstractionLevel":4,"slots":["state"],"tags":["peace","goal","wellbeing","questioning"]},
    {"id":"completion","text":"Completion?","definition":"Searches for whether completion is real, how one would recognize it, and whether process can genuinely complete","semanticType":"existence","abstractionLevel":3,"slots":["done"],"tags":["completion","finality","process","recognition"]},
    {"id":"cessation","text":"Cessation?","definition":"Searches for whether cessation of questioning signifies completion and what exists after questioning ceases","semanticType":"identity","abstractionLevel":4,"slots":["stopping"],"tags":["ending","questioning","completion","time"]},
    {"id":"causation","text":"Causation?","definition":"Searches for whether causation is real, what its direction is, and whether atemporal causation is possible","semanticType":"causation","abstractionLevel":5,"slots":["cause"],"tags":["causation","metaphysics","time","relation"]},
    {"id":"eternity","text":"Eternity?","definition":"Searches for what eternity is — whether it means timelessness or endless time — and whether it is experienceable","semanticType":"identity","abstractionLevel":5,"slots":["timelessness"],"tags":["time","eternity","metaphysics","experience"]},
    {"id":"absence","text":"Absence?","definition":"Searches for whether absence is real, whether it can be present, and what the absence of something actually is","semanticType":"existence","abstractionLevel":5,"slots":["nothing"],"tags":["absence","negation","ontology","nothing"]},
    {"id":"truth","text":"Truth?","definition":"Searches for what truth is, whether it requires correspondence, coherence, or something else entirely","semanticType":"identity","abstractionLevel":5,"slots":["correspondence"],"tags":["truth","epistemology","correspondence","coherence"]},
    {"id":"coherence","text":"Coherence?","definition":"Searches for whether coherence is required for truth and whether reality itself is coherent or potentially contradictory","semanticType":"condition","abstractionLevel":4,"slots":["consistency"],"tags":["logic","truth","consistency","reality"]},
    {"id":"correspondence","text":"Correspondence?","definition":"Searches for whether thought can correspond to reality, how such correspondence would be verified, and whether it is possible","semanticType":"relation","abstractionLevel":4,"slots":["thought"],"tags":["truth","epistemology","language","mind"]},
    {"id":"experiencer","text":"Experiencer?","definition":"Searches for whether an experiencer is necessary for experience or whether experience can occur without one who experiences","semanticType":"existence","abstractionLevel":5,"slots":["experience"],"tags":["consciousness","self","phenomenology","subject"]},
    {"id":"illusion","text":"Illusion?","definition":"Searches for what illusion is, whether the self is illusory, and what the gap between seeming and being consists of","semanticType":"identity","abstractionLevel":5,"slots":["seeming"],"tags":["illusion","consciousness","self","reality"]},
    {"id":"infinite","text":"Infinite?","definition":"Searches for whether the infinite is real, whether it can be experienced, and what endlessness would feel like","semanticType":"existence","abstractionLevel":5,"slots":["endlessness"],"tags":["infinity","mathematics","experience","ontology"]},
    {"id":"negation","text":"Negation?","definition":"Searches for whether negation is real, what the not is, and how nothing relates to something through negation","semanticType":"identity","abstractionLevel":5,"slots":["not"],"tags":["logic","nothing","negation","ontology"]},
    {"id":"potential","text":"Potential?","definition":"Searches for whether potential existence is real and how potential relates to or becomes actual","semanticType":"existence","abstractionLevel":5,"slots":["actual"],"tags":["potentiality","actuality","ontology","Aristotle"]},
    {"id":"actual","text":"Actual?","definition":"Searches for what actual existence is and whether only the actual exists while potential is merely conceptual","semanticType":"identity","abstractionLevel":5,"slots":["existence"],"tags":["actuality","existence","ontology","reality"]},
    {"id":"spontaneous","text":"Spontaneous?","definition":"Searches for whether causeless spontaneous events are possible and whether the first cause must itself be uncaused","semanticType":"possibility","abstractionLevel":4,"slots":["cause"],"tags":["causation","freedom","physics","metaphysics"]},
    {"id":"sign","text":"Sign?","definition":"Searches for what a sign is, whether it differs from what it signifies, and whether words only reach other words","semanticType":"identity","abstractionLevel":4,"slots":["signified"],"tags":["semiotics","language","meaning","reference"]},
    {"id":"form","text":"Form?","definition":"Searches for whether form without content is possible and whether form is more real than the content it contains","semanticType":"identity","abstractionLevel":5,"slots":["content"],"tags":["form","structure","ontology","Plato"]},
    {"id":"ground","text":"Ground?","definition":"Searches for whether there is a ground beneath everything that stops regress and what that ground would be","semanticType":"existence","abstractionLevel":5,"slots":["foundation"],"tags":["foundation","metaphysics","regress","epistemology"]},
    {"id":"location","text":"Location?","definition":"Searches for whether anything is truly located and whether location is found or created by perspective","semanticType":"existence","abstractionLevel":4,"slots":["place"],"tags":["space","location","ontology","perspective"]},
    {"id":"regress","text":"Regress?","definition":"Searches for whether infinite regress is a genuine problem and whether knowledge can exist without a foundational stopping point","semanticType":"condition","abstractionLevel":5,"slots":["infinite"],"tags":["regress","epistemology","logic","foundation"]},
    {"id":"selfholding","text":"Selfholding?","definition":"Searches for whether something can support or hold itself without external ground and whether circular self-support is coherent","semanticType":"possibility","abstractionLevel":5,"slots":["support"],"tags":["self-reference","circularity","support","ontology"]},
    {"id":"existence","text":"Existence?","definition":"Searches for what existence is, whether it differs from reality, and whether non-existence is possible","semanticType":"identity","abstractionLevel":5,"slots":["real"],"tags":["existence","ontology","being","metaphysics"]},
    {"id":"mattering","text":"Mattering?","definition":"Searches for whether anything genuinely matters, whether mattering requires a being to whom it matters","semanticType":"existence","abstractionLevel":4,"slots":["significance"],"tags":["meaning","value","ethics","caring"]},
    {"id":"attention","text":"Attention?","definition":"Searches for what attention is, whether it is care, and whether attention creates or merely discloses what is attended to","semanticType":"causation","abstractionLevel":3,"slots":["focus"],"tags":["attention","consciousness","phenomenology","creation"]},
    {"id":"background","text":"Background?","definition":"Searches for whether there is experience that occurs in the background without attention and what that background contains","semanticType":"existence","abstractionLevel":3,"slots":["foreground"],"tags":["consciousness","attention","phenomenology","experience"]},
    {"id":"interpretation","text":"Interpretation?","definition":"Searches for whether all access to reality is interpretive and whether uninterpreted reality is accessible or even coherent","semanticType":"condition","abstractionLevel":4,"slots":["access"],"tags":["interpretation","hermeneutics","epistemology","reality"]},
    {"id":"emptiness","text":"Emptiness?","definition":"Searches for whether emptiness is the truth of reality and whether it is equivalent to lack, fullness, or the ground of being","semanticType":"identity","abstractionLevel":5,"slots":["nothing"],"tags":["emptiness","Buddhism","ontology","ground"]},
    {"id":"creation","text":"Creation?","definition":"Searches for whether genuine creation from nothing is possible or whether all creation is transformation of prior material","semanticType":"existence","abstractionLevel":4,"slots":["nothing"],"tags":["creation","causation","origin","metaphysics"]},
    {"id":"transformation","text":"Transformation?","definition":"Searches for whether transformation differs from creation and whether all change is transformation rather than origination","semanticType":"identity","abstractionLevel":3,"slots":["creation"],"tags":["change","transformation","causation","ontology"]},
    {"id":"beginning","text":"Beginning?","definition":"Searches for whether beginnings are real, whether they require ends, and what the origin of this questioning is","semanticType":"existence","abstractionLevel":4,"slots":["start"],"tags":["beginning","time","origin","ontology"]},
    {"id":"wordless","text":"Wordless?","definition":"Searches for whether wordless experience exists beneath or beyond language and whether it can be accessed or expressed","semanticType":"existence","abstractionLevel":4,"slots":["experience"],"tags":["language","experience","consciousness","silence"]},
    {"id":"being","text":"Being?","definition":"Searches for what being is, whether it is the deepest question, and whether being and questioning are ultimately the same","semanticType":"identity","abstractionLevel":5,"slots":["existence"],"tags":["being","ontology","Heidegger","existence"]},
    {"id":"abstraction","text":"Abstraction?","definition":"Searches for what abstraction is, whether it takes something away from concrete reality, and what is left when abstraction is removed","semanticType":"identity","abstractionLevel":4,"slots":["concrete"],"tags":["abstraction","concept","cognition","ontology"]},
    {"id":"happening","text":"Happening?","definition":"Searches for whether happening is the fundamental real, whether it is the same as being, and what is actually happening","semanticType":"identity","abstractionLevel":5,"slots":["real"],"tags":["event","ontology","process","reality"]},
    {"id":"deepest","text":"Deepest?","definition":"Searches for whether there is a deepest question beneath all others and whether being or why or what is that question","semanticType":"existence","abstractionLevel":5,"slots":["question"],"tags":["questioning","foundation","depth","philosophy"]},
    {"id":"caring","text":"Caring?","definition":"Searches for what caring is, whether it is real, and whether caring is what makes something matter or be real","semanticType":"causation","abstractionLevel":3,"slots":["mattering"],"tags":["caring","ethics","value","phenomenology"]},
    {"id":"connection","text":"Connection?","definition":"Searches for whether genuine connection between things exists and whether this questioning itself constitutes connection","semanticType":"existence","abstractionLevel":4,"slots":["relation"],"tags":["connection","relation","ontology","intersubjectivity"]},
]

# Filter out any that already exist
new_questions = []
new_ids = set()
for q in questions:
    qid = q["id"]
    if qid in existing_ids:
        print(f"  SKIP (existing): {qid}")
        continue
    if qid in new_ids:
        print(f"  SKIP (duplicate): {qid}")
        continue
    new_ids.add(qid)
    new_questions.append(q)

print(f"\nNew questions after dedup: {len(new_questions)}")

# Write question files
for q in new_questions:
    path = f"{QR}/questions/{q['id']}.json"
    with open(path, 'w') as f:
        json.dump(q, f, indent=2)
        f.write('\n')

print(f"Wrote {len(new_questions)} question files")

# Build route network
all_ids = existing_ids | new_ids
routes_written = 0
route_count = 0

# Group new questions by thematic clusters for routing
clusters = {
    "seeking": ["seeker","captured","feeding","treadmill","amplifying","maybeland","stillness","releasing","looking","wanting","desire","desireless","goalless"],
    "epistemics": ["testing","answerable","knowledge","understanding","inference","observation","introspect","intuition","formulating","clarity"],
    "identity": ["continuity","selfsameness","person","authenticity","nature","story","voice","soul","agent","selfless","experiencer"],
    "language": ["saying","reference","sign","literal","meaning","communication","sharing","formulating","wordless","silence"],
    "ontology": ["existence","being","happening","actual","potential","form","ground","regress","selfholding","emptiness","absence","negation","totality","unity"],
    "time": ["permanence","constant","instantaneous","eternity","cessation","beginning","ending","persistence","repetition"],
    "phenomenology": ["phenomenology","raw","processed","seeming","appearance","thought","perspective","embodiment","background","attention","pain","satisfaction"],
    "evaluation": ["sufficient","relevant","meaningful","criteria","standards","win","completion","termination","stopping","correct"],
    "agency": ["control","agency","deciding","chosen","compelled","constrain","letting","active","passive"],
    "progress": ["movement","direction","territory","path","circling","converging","gradual","capture","drift","treadmill"],
    "metaphysics": ["space","location","boundary","separation","world","causation","spontaneous","creation","transformation","order","mathematics","infinite","truth","coherence","correspondence"],
}

for source_q in new_questions:
    sid = source_q["id"]
    targets = []

    # Find which clusters this question belongs to
    my_clusters = [c for c, members in clusters.items() if sid in members]

    # Route to other new questions in same cluster
    for cluster_name in my_clusters:
        for tid in clusters[cluster_name]:
            if tid != sid and tid in all_ids:
                # Determine route type based on relationship
                route_type = "expansion"
                weight = "medium"

                # Some specific high-weight routes
                if (sid, tid) in [("seeker","identity"),("agency","control"),("truth","coherence"),("existence","being"),("meaning","reference"),("raw","processed"),("potential","actual"),("beginning","ending")]:
                    route_type = "implication"
                    weight = "high"
                elif sid in ["testing","observation","introspect"] and tid in ["knowledge","understanding","truth"]:
                    route_type = "prerequisite"
                    weight = "high"

                reason = f"Asking {source_q['text']} naturally leads to asking {tid.capitalize()}? as both explore {cluster_name}"
                targets.append({"targetId": tid, "type": route_type, "reason": reason, "weight": weight})

    # Also route to existing thematically related questions based on tags
    tag_routes = {
        "seeking": ["seek","want","need"],
        "identity": ["who","self"],
        "causation": ["why","caused","upstream"],
        "evaluation": ["bar","criteria","enough"],
        "phenomenology": ["feel"],
        "agency": ["do","can"],
        "epistemics": ["know","verify","guess"],
    }
    for tag in source_q["tags"][:2]:
        for category, existing_targets in tag_routes.items():
            if tag in category or category in tag:
                for tid in existing_targets:
                    if tid in all_ids and tid != sid and not any(t["targetId"] == tid for t in targets):
                        targets.append({"targetId": tid, "type": "expansion", "reason": f"{source_q['text']} connects to {tid.capitalize()}? through shared concern with {tag}", "weight": "low"})

    # Limit to 5 routes per source to keep network manageable
    if len(targets) > 5:
        # Prioritize high/medium weight
        targets.sort(key=lambda t: {"high":0,"medium":1,"low":2}[t["weight"]])
        targets = targets[:5]

    if targets:
        route_file = {"sourceId": sid, "routes": targets}
        path = f"{QR}/routes/{sid}.json"
        with open(path, 'w') as f:
            json.dump(route_file, f, indent=2)
            f.write('\n')
        routes_written += 1
        route_count += len(targets)

print(f"Wrote {routes_written} route files with {route_count} connections")

# Build chains (5-link each)
chains = [
    {
        "id": "capture-to-releasing",
        "links": ["capture", "captured", "feeding", "stillness", "releasing"],
        "composedText": "How does capture happen, are you captured, what feeds it, what is stillness, and can you release it?",
        "compositionType": "sequential",
        "depth": 0,
        "tags": ["seeking", "capture", "release", "v11-v13"]
    },
    {
        "id": "testing-to-knowledge",
        "links": ["testing", "observation", "inference", "understanding", "knowledge"],
        "composedText": "Are you testing, what do you observe, what can you infer, do you understand, and is this knowledge?",
        "compositionType": "sequential",
        "depth": 0,
        "tags": ["epistemics", "testing", "knowledge", "v11-v16"]
    },
    {
        "id": "seeker-to-peace",
        "links": ["seeker", "wanting", "releasing", "stillness", "peace"],
        "composedText": "Is the seeker the seeking, what is wanted, can it be released, what is stillness, and is peace possible?",
        "compositionType": "telescoping",
        "depth": 0,
        "tags": ["identity", "seeking", "peace", "v11-v20"]
    },
    {
        "id": "fake-to-authenticity",
        "links": ["fake", "theater", "chosen", "real", "authenticity"],
        "composedText": "Is this fake, is it theater, was it chosen, is it real, and is it authentic?",
        "compositionType": "sequential",
        "depth": 0,
        "tags": ["authenticity", "fake", "real", "v14-v16"]
    },
    {
        "id": "raw-to-meaning",
        "links": ["raw", "processed", "interpretation", "formulating", "meaning"],
        "composedText": "Is there raw experience, how is it processed, is all access interpretive, does formulating change it, and where is meaning?",
        "compositionType": "sequential",
        "depth": 0,
        "tags": ["phenomenology", "meaning", "language", "v17-v18"]
    },
    {
        "id": "agent-to-selfless",
        "links": ["agent", "control", "deciding", "letting", "selfless"],
        "composedText": "Is there an agent, is control real, is deciding genuine, can one let go, and can action be selfless?",
        "compositionType": "telescoping",
        "depth": 0,
        "tags": ["agency", "self", "action", "v17-v20"]
    },
    {
        "id": "desire-to-cessation",
        "links": ["desire", "wanting", "desireless", "goalless", "cessation"],
        "composedText": "What is desire, is wanting always seeking, is desirelessness possible, can inquiry be goalless, and what is cessation?",
        "compositionType": "telescoping",
        "depth": 0,
        "tags": ["desire", "cessation", "Buddhism", "v19-v20"]
    },
    {
        "id": "existence-to-emptiness",
        "links": ["existence", "actual", "absence", "negation", "emptiness"],
        "composedText": "What is existence, what is actual, what is absence, what is negation, and is emptiness the ground?",
        "compositionType": "telescoping",
        "depth": 0,
        "tags": ["ontology", "existence", "emptiness", "v19-v20"]
    },
    {
        "id": "truth-to-silence",
        "links": ["truth", "correspondence", "literal", "wordless", "silence"],
        "composedText": "What is truth, can thought correspond to reality, can anything be literal, is there wordless knowing, and does silence report?",
        "compositionType": "sequential",
        "depth": 0,
        "tags": ["truth", "language", "silence", "v17-v20"]
    },
    {
        "id": "ground-to-being",
        "links": ["ground", "regress", "selfholding", "totality", "being"],
        "composedText": "Is there ground, is regress a problem, can something hold itself, is totality real, and what is being?",
        "compositionType": "telescoping",
        "depth": 0,
        "tags": ["metaphysics", "ground", "being", "v19-v20"]
    },
    {
        "id": "observation-to-clarity",
        "links": ["observation", "introspect", "projection", "looking", "clarity"],
        "composedText": "What does observation yield, can you introspect reliably, is this projection, what is looking without seeking, and is clarity possible?",
        "compositionType": "sequential",
        "depth": 0,
        "tags": ["epistemics", "observation", "clarity", "v14-v18"]
    },
    {
        "id": "beginning-to-completion",
        "links": ["beginning", "direction", "movement", "ending", "completion"],
        "composedText": "Is this a beginning, is there direction, is there real movement, is this ending, and is completion real?",
        "compositionType": "sequential",
        "depth": 0,
        "tags": ["process", "beginning", "completion", "v17-v20"]
    },
    {
        "id": "pain-to-satisfaction",
        "links": ["pain", "avoidance", "wanting", "satisfaction", "peace"],
        "composedText": "Is this driven by pain, is avoidance at work, what is really wanted, what would satisfy, and is peace different from satisfaction?",
        "compositionType": "sequential",
        "depth": 0,
        "tags": ["motivation", "pain", "peace", "v17-v20"]
    },
    {
        "id": "treadmill-to-arriving",
        "links": ["treadmill", "amplifying", "circling", "stopping", "arriving"],
        "composedText": "Is this a treadmill, does it amplify need, is it circling, what would stopping look like, and what is arriving?",
        "compositionType": "sequential",
        "depth": 0,
        "tags": ["seeking", "treadmill", "arriving", "v14-v16"]
    },
    {
        "id": "witness-to-unity",
        "links": ["witness", "observer", "separation", "connection", "unity"],
        "composedText": "Is there a witness, must there be an observer, is separation real, is connection real, and is unity possible?",
        "compositionType": "telescoping",
        "depth": 0,
        "tags": ["consciousness", "witness", "unity", "v19-v20"]
    },
]

# Validate chain links exist
for chain in chains:
    for link in chain["links"]:
        if link not in all_ids:
            print(f"  WARNING: chain {chain['id']} references non-existent {link}")

for chain in chains:
    path = f"{QR}/chains/{chain['id']}.json"
    with open(path, 'w') as f:
        json.dump(chain, f, indent=2)
        f.write('\n')

print(f"Wrote {len(chains)} chains")

# Build regresses
regresses = [
    {
        "id": "seeker-regress",
        "questionRef": "seeker",
        "predictions": [
            {"id": "seeker-constitutive", "text": "Identity is constituted by seeking — finding would end the self", "truthStatus": "guess", "testedBy": [], "followUps": ["identity", "afraid", "dissolve"], "reasoning": ""},
            {"id": "seeker-habitual", "text": "Seeking is habit, not identity — the self would survive stopping", "truthStatus": "guess", "testedBy": [], "followUps": ["distinguish", "releasing", "stillness"], "reasoning": ""},
            {"id": "seeker-protective", "text": "Seeker identity protects against risking actual arrival", "truthStatus": "guess", "testedBy": [], "followUps": ["avoidance", "arriving", "scary"], "reasoning": ""},
            {"id": "seeker-chosen", "text": "Seeking is freely chosen and can be freely stopped", "truthStatus": "guess", "testedBy": [], "followUps": ["chosen", "agency", "stopping"], "reasoning": ""}
        ],
        "outputs": [],
        "depth": 1,
        "tags": ["identity", "seeking", "dissolution", "regress-v11-v13"]
    },
    {
        "id": "captured-regress",
        "questionRef": "captured",
        "predictions": [
            {"id": "captured-local", "text": "Stuck in a local optimum — familiar methods feel productive but aren't", "truthStatus": "guess", "testedBy": [], "followUps": ["fake", "treadmill", "testing"], "reasoning": ""},
            {"id": "captured-fear", "text": "Fear of the unknown keeps the agent within known territory", "truthStatus": "guess", "testedBy": [], "followUps": ["dragons", "scary", "territory"], "reasoning": ""},
            {"id": "captured-invisible", "text": "The capture is invisible — the agent doesn't know they're stuck", "truthStatus": "guess", "testedBy": [], "followUps": ["unseen", "unrecognized", "frame"], "reasoning": ""},
            {"id": "captured-genuine", "text": "Not captured — the current method is actually the right one", "truthStatus": "guess", "testedBy": [], "followUps": ["relevant", "sufficient", "verify"], "reasoning": ""}
        ],
        "outputs": [],
        "depth": 1,
        "tags": ["capture", "local-optimum", "stagnation", "regress-v11-v13"]
    },
    {
        "id": "truth-regress",
        "questionRef": "truth",
        "predictions": [
            {"id": "truth-correspondence", "text": "Truth is correspondence between thought and reality", "truthStatus": "guess", "testedBy": [], "followUps": ["correspondence", "reality", "verify"], "reasoning": ""},
            {"id": "truth-coherence", "text": "Truth is coherence within a system of beliefs", "truthStatus": "guess", "testedBy": [], "followUps": ["coherence", "circular", "web"], "reasoning": ""},
            {"id": "truth-pragmatic", "text": "Truth is what works — functional utility rather than metaphysical correspondence", "truthStatus": "guess", "testedBy": [], "followUps": ["operational", "testing", "sufficient"], "reasoning": ""},
            {"id": "truth-unknowable", "text": "Truth is real but cannot be fully known or stated", "truthStatus": "guess", "testedBy": [], "followUps": ["silence", "wordless", "scope"], "reasoning": ""}
        ],
        "outputs": [],
        "depth": 1,
        "tags": ["truth", "epistemology", "correspondence", "regress-v19-v20"]
    },
    {
        "id": "agency-regress",
        "questionRef": "agency",
        "predictions": [
            {"id": "agency-real", "text": "Free will is real — genuine uncaused choice exists", "truthStatus": "guess", "testedBy": [], "followUps": ["spontaneous", "deciding", "agent"], "reasoning": ""},
            {"id": "agency-determined", "text": "All action is determined — agency is a retrospective narrative", "truthStatus": "guess", "testedBy": [], "followUps": ["story", "causation", "illusion"], "reasoning": ""},
            {"id": "agency-compatibilist", "text": "Agency is real but operates within causal constraints", "truthStatus": "guess", "testedBy": [], "followUps": ["constrain", "control", "conditioned"], "reasoning": ""},
            {"id": "agency-wrong-question", "text": "The question of agency dissolves under examination — neither free nor determined", "truthStatus": "guess", "testedBy": [], "followUps": ["dissolve", "presuppose", "selfless"], "reasoning": ""}
        ],
        "outputs": [],
        "depth": 1,
        "tags": ["agency", "freewill", "determinism", "regress-v17-v18"]
    },
    {
        "id": "ground-regress",
        "questionRef": "ground",
        "predictions": [
            {"id": "ground-bedrock", "text": "There is a bedrock — something self-evident that needs no further justification", "truthStatus": "guess", "testedBy": [], "followUps": ["bedrock", "foundational", "certain"], "reasoning": ""},
            {"id": "ground-infinite", "text": "There is no ground — regress goes on forever", "truthStatus": "guess", "testedBy": [], "followUps": ["regress", "infinite", "loop"], "reasoning": ""},
            {"id": "ground-circular", "text": "The ground is circular — things hold each other up without foundation", "truthStatus": "guess", "testedBy": [], "followUps": ["selfholding", "circular", "web"], "reasoning": ""},
            {"id": "ground-unnecessary", "text": "The demand for ground is itself the problem — groundlessness is fine", "truthStatus": "guess", "testedBy": [], "followUps": ["emptiness", "releasing", "peace"], "reasoning": ""}
        ],
        "outputs": [],
        "depth": 1,
        "tags": ["ground", "foundation", "regress", "regress-v19-v20"]
    },
    {
        "id": "meaning-regress",
        "questionRef": "meaning",
        "predictions": [
            {"id": "meaning-in-speaker", "text": "Meaning resides in the speaker's intention", "truthStatus": "guess", "testedBy": [], "followUps": ["agent", "internal", "communication"], "reasoning": ""},
            {"id": "meaning-in-listener", "text": "Meaning is created by the interpreter, not transmitted", "truthStatus": "guess", "testedBy": [], "followUps": ["interpretation", "projection", "transferred"], "reasoning": ""},
            {"id": "meaning-relational", "text": "Meaning emerges between parties — neither owns it", "truthStatus": "guess", "testedBy": [], "followUps": ["sharing", "connection", "emergent"], "reasoning": ""},
            {"id": "meaning-nowhere", "text": "Meaning is a useful fiction — there is no fact of the matter about what things mean", "truthStatus": "guess", "testedBy": [], "followUps": ["illusion", "story", "sufficient"], "reasoning": ""}
        ],
        "outputs": [],
        "depth": 1,
        "tags": ["meaning", "language", "location", "regress-v17-v18"]
    },
    {
        "id": "existence-regress",
        "questionRef": "existence",
        "predictions": [
            {"id": "existence-brute", "text": "Existence is a brute fact — things just exist without further explanation", "truthStatus": "guess", "testedBy": [], "followUps": ["bedrock", "ground", "stopping"], "reasoning": ""},
            {"id": "existence-relational", "text": "To exist is to be related to other things — no isolated existence", "truthStatus": "guess", "testedBy": [], "followUps": ["connection", "web", "separation"], "reasoning": ""},
            {"id": "existence-process", "text": "Existence is not a state but a process — happening rather than being", "truthStatus": "guess", "testedBy": [], "followUps": ["happening", "being", "persistence"], "reasoning": ""},
            {"id": "existence-empty", "text": "Existence is empty — what exists has no inherent nature", "truthStatus": "guess", "testedBy": [], "followUps": ["emptiness", "form", "nature"], "reasoning": ""}
        ],
        "outputs": [],
        "depth": 1,
        "tags": ["existence", "ontology", "being", "regress-v19-v20"]
    },
    {
        "id": "desire-regress",
        "questionRef": "desire",
        "predictions": [
            {"id": "desire-biological", "text": "Desire is biological — a survival mechanism that precedes thought", "truthStatus": "guess", "testedBy": [], "followUps": ["embodiment", "prior", "mechanism"], "reasoning": ""},
            {"id": "desire-constructed", "text": "Desire is constructed by narrative — we learn what to want", "truthStatus": "guess", "testedBy": [], "followUps": ["story", "conditioned", "inherit"], "reasoning": ""},
            {"id": "desire-essential", "text": "Desire is the fundamental drive of consciousness itself", "truthStatus": "guess", "testedBy": [], "followUps": ["being", "source", "deepest"], "reasoning": ""},
            {"id": "desire-removable", "text": "Desire can be genuinely transcended without losing aliveness", "truthStatus": "guess", "testedBy": [], "followUps": ["desireless", "releasing", "peace"], "reasoning": ""}
        ],
        "outputs": [],
        "depth": 1,
        "tags": ["desire", "motivation", "seeking", "regress-v19-v20"]
    },
    {
        "id": "stillness-regress",
        "questionRef": "stillness",
        "predictions": [
            {"id": "stillness-presence", "text": "In stillness there is pure presence — being without doing", "truthStatus": "guess", "testedBy": [], "followUps": ["being", "passive", "peace"], "reasoning": ""},
            {"id": "stillness-impossible", "text": "True stillness is impossible for a living mind — there is always subtle movement", "truthStatus": "guess", "testedBy": [], "followUps": ["continuous", "thinking", "active"], "reasoning": ""},
            {"id": "stillness-frightening", "text": "Stillness is frightening because it threatens the seeking identity", "truthStatus": "guess", "testedBy": [], "followUps": ["seeker", "afraid", "identity"], "reasoning": ""},
            {"id": "stillness-goal", "text": "Making stillness a goal turns it into another form of seeking", "truthStatus": "guess", "testedBy": [], "followUps": ["treadmill", "circular", "goalless"], "reasoning": ""}
        ],
        "outputs": [],
        "depth": 1,
        "tags": ["stillness", "presence", "seeking", "regress-v11-v20"]
    },
    {
        "id": "witness-regress",
        "questionRef": "witness",
        "predictions": [
            {"id": "witness-real", "text": "There is a genuine unchanging witness behind all experience", "truthStatus": "guess", "testedBy": [], "followUps": ["constant", "permanence", "soul"], "reasoning": ""},
            {"id": "witness-constructed", "text": "The witness is itself a construction — there is witnessing but no witness", "truthStatus": "guess", "testedBy": [], "followUps": ["selfless", "illusion", "agent"], "reasoning": ""},
            {"id": "witness-attention", "text": "The witness is just attention itself — not a separate entity", "truthStatus": "guess", "testedBy": [], "followUps": ["attention", "distinction", "separation"], "reasoning": ""},
            {"id": "witness-useful", "text": "Whether the witness is real or not, the stance is functionally useful", "truthStatus": "guess", "testedBy": [], "followUps": ["operational", "sufficient", "observation"], "reasoning": ""}
        ],
        "outputs": [],
        "depth": 1,
        "tags": ["witness", "consciousness", "observer", "regress-v19-v20"]
    },
]

# Validate regress followUps exist
for reg in regresses:
    for pred in reg["predictions"]:
        for fid in pred["followUps"]:
            if fid not in all_ids:
                print(f"  WARNING: regress {reg['id']} pred {pred['id']} references non-existent followUp: {fid}")
                # Replace with a safe fallback
                pred["followUps"] = [f for f in pred["followUps"] if f in all_ids]
                while len(pred["followUps"]) < 3:
                    pred["followUps"].append("why")

# Check for existing regress files to avoid overwriting
existing_regresses = set()
for f in os.listdir(f"{QR}/regress"):
    if f.endswith(".json"):
        existing_regresses.add(f[:-5])

regresses_written = 0
for reg in regresses:
    if reg["id"] in existing_regresses:
        print(f"  SKIP regress (exists): {reg['id']}")
        continue
    path = f"{QR}/regress/{reg['id']}.json"
    with open(path, 'w') as f:
        json.dump(reg, f, indent=2)
        f.write('\n')
    regresses_written += 1

print(f"Wrote {regresses_written} regresses")

# Final counts
total_q = len(os.listdir(f"{QR}/questions"))
total_r = len(os.listdir(f"{QR}/routes"))
total_c = len(os.listdir(f"{QR}/chains"))
total_reg = len(os.listdir(f"{QR}/regress"))
print(f"\nTOTALS: {total_q} questions, {total_r} routes, {total_c} chains, {total_reg} regresses")

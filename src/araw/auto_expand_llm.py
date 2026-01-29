"""
ARAW Auto-Expander (LLM-Powered)

Uses OpenAI gpt-5-nano to generate meaningful ASSUME RIGHT / ASSUME WRONG branches.
Actually thinks about each claim instead of pattern matching.

Usage:
    python auto_expand_llm.py --db araw_llm.db --seed "I need to change careers"
    python auto_expand_llm.py --db araw_llm.db --continue
    python auto_expand_llm.py --db araw_llm.db --continue --parallel 5
"""

import argparse
import json
import os
import re
import subprocess
import tempfile
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, List, Tuple

from araw_engine import ARAWEngine, BranchType, NodeStatus, Node

DEFAULT_KEY_FILE = str(Path.home() / ".config" / "gosm" / "openai_api_key")
DEFAULT_BASE_URL = "https://api.openai.com/v1/responses"
DEFAULT_MODEL = "gpt-5-nano"

# Relevancy gate signals
CONCRETE_SIGNALS = [
    'build', 'create', 'tool', 'system', 'implement', 'measure', 'test',
    'specific', 'mechanism', 'protocol', 'method', 'technique', 'step',
    'action', 'experiment', 'verify', 'quantify', 'rate', 'percentage'
]

DRIFT_SIGNALS = [
    'widespread', 'governance', 'legitimacy', 'perceived', 'intrinsic',
    'norms around', 'broadly', 'general sense', 'tends to', 'often',
    'may feel', 'might experience', 'stakeholder alignment', 'holistic'
]

# All available domains for exploration
ALL_DOMAINS = [
    "HUMAN", "INSTITUTIONAL", "EVIDENTIAL", "EPISTEMOLOGICAL", "PRACTICAL", "RELATIONAL",
    "ETHICAL", "TEMPORAL", "CULTURAL", "ENVIRONMENTAL", "TECHNOLOGICAL", "GEOPOLITICAL",
    "EXISTENTIAL", "DEMOGRAPHIC", "BIOLOGICAL", "ECONOMIC", "INFORMATIONAL", "SYSTEMIC"
]

# Keywords for detecting domains in claims
DOMAIN_KEYWORDS = {
    'HUMAN': ['person', 'people', 'individual', 'competent', 'skill', 'bias', 'motivation', 'psychology', 'belief'],
    'INSTITUTIONAL': ['system', 'organization', 'policy', 'government', 'institution', 'regulation', 'bureauc'],
    'EVIDENTIAL': ['evidence', 'data', 'test', 'study', 'research', 'measure', 'observation', 'experiment'],
    'EPISTEMOLOGICAL': ['knowledge', 'truth', 'logic', 'reason', 'method', 'assumption', 'certainty'],
    'PRACTICAL': ['cost', 'money', 'resource', 'time', 'budget', 'feasible', 'implement'],
    'RELATIONAL': ['family', 'relationship', 'trust', 'communication', 'social', 'friend'],
    'ETHICAL': ['moral', 'ethic', 'fair', 'justice', 'value', 'right', 'wrong', 'principle'],
    'TEMPORAL': ['future', 'past', 'history', 'trend', 'generation', 'change', 'evolve'],
    'CULTURAL': ['culture', 'tradition', 'norm', 'society', 'worldview', 'custom'],
    'ENVIRONMENTAL': ['environment', 'climate', 'ecology', 'sustainable', 'nature', 'pollution'],
    'TECHNOLOGICAL': ['technology', 'ai', 'automation', 'digital', 'innovation', 'software', 'algorithm'],
    'GEOPOLITICAL': ['international', 'power', 'conflict', 'cooperation', 'nation', 'war', 'diplomacy'],
    'EXISTENTIAL': ['extinction', 'survival', 'catastroph', 'existential', 'long-term risk'],
    'DEMOGRAPHIC': ['population', 'aging', 'migration', 'urban', 'birth rate', 'demographic'],
    'BIOLOGICAL': ['health', 'disease', 'longevity', 'mental health', 'evolution', 'genetic'],
    'ECONOMIC': ['market', 'inequality', 'trade', 'incentive', 'economic', 'gdp', 'wealth'],
    'INFORMATIONAL': ['media', 'misinformation', 'narrative', 'attention', 'news', 'propaganda'],
    'SYSTEMIC': ['feedback', 'complexity', 'emergence', 'unintended', 'cascade', 'network effect'],
}


def read_api_key(path: Optional[str] = None) -> tuple[Optional[str], str]:
    """Read API key from env or file"""
    env = os.environ.get("OPENAI_API_KEY", "").strip()
    if env:
        return env, "env"
    for p in ([path] if path else []) + [DEFAULT_KEY_FILE]:
        if p and Path(p).expanduser().is_file():
            key = Path(p).expanduser().read_text().splitlines()[0].strip()
            if key:
                return key, f"file:{p}"
    return None, "none"


def api_call(api_key: str, payload: dict, timeout: int = 60, base_url: str = DEFAULT_BASE_URL, max_retries: int = 5) -> tuple[bool, dict]:
    """Make API call to OpenAI"""
    import re as _re

    with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)
        payload_path = f.name

    body_fd, body_name = tempfile.mkstemp(prefix="resp_", suffix=".json")
    os.close(body_fd)
    body_path = Path(body_name)

    try:
        for attempt in range(max_retries):
            cmd = ["curl", "-sS", base_url, "--http1.1", "--connect-timeout", "15",
                   "--max-time", str(timeout), "--retry", "3", "--fail-with-body",
                   "-H", f"Authorization: Bearer {api_key}", "-H", "Content-Type: application/json",
                   "-d", f"@{payload_path}", "-o", str(body_path), "-w", "%{http_code}"]
            proc = subprocess.run(cmd, text=True, capture_output=True, timeout=timeout + 30, check=False)
            body = body_path.read_text(encoding="utf-8", errors="replace") if body_path.exists() else ""
            code = (proc.stdout or "").strip()

            # Check for rate limit error
            if "rate_limit" in body.lower() or code == "429":
                wait_match = _re.search(r'try again in (\d+\.?\d*)s', body)
                wait_time = float(wait_match.group(1)) if wait_match else (2 ** attempt)
                wait_time = min(wait_time + 0.5, 30)
                if attempt < max_retries - 1:
                    print(f"  Rate limited, waiting {wait_time:.1f}s...")
                    time.sleep(wait_time)
                    continue

            if proc.returncode != 0 or (code and code != "200"):
                return False, {"error": f"http={code}", "body": body}

            try:
                return True, json.loads(body)
            except json.JSONDecodeError:
                return False, {"error": "json_decode", "body": body}

        return False, {"error": "rate_limit_retries_exhausted"}
    finally:
        Path(payload_path).unlink(missing_ok=True)
        body_path.unlink(missing_ok=True)


def extract_text(resp: dict) -> str:
    """Extract text from API response"""
    if "output" in resp:
        for item in resp.get("output", []):
            for c in item.get("content", []):
                if isinstance(c, dict) and c.get("type") in ("output_text", "text"):
                    return c.get("text", "").strip()
    if "choices" in resp:
        return resp["choices"][0].get("message", {}).get("content", "").strip()
    return ""


def get_domain_distribution(conn) -> dict:
    """Analyze current domain distribution in the tree"""
    cursor = conn.cursor()
    cursor.execute("SELECT claim FROM nodes")

    counts = {d: 0 for d in ALL_DOMAINS}
    total = 0

    for row in cursor:
        claim_lower = row['claim'].lower()
        total += 1
        for domain, keywords in DOMAIN_KEYWORDS.items():
            if any(kw in claim_lower for kw in keywords):
                counts[domain] += 1
                break

    return {d: c / total if total > 0 else 0 for d, c in counts.items()}


def recommend_domain_weights(api_key: str, root_claim: str, current_distribution: Optional[dict] = None) -> dict:
    """Use LLM to recommend domain weights based on root claim and current distribution"""

    dist_info = ""
    if current_distribution:
        sorted_dist = sorted(current_distribution.items(), key=lambda x: -x[1])
        overexplored = [f"{d} ({v*100:.0f}%)" for d, v in sorted_dist[:3]]
        underexplored = [f"{d} ({v*100:.0f}%)" for d, v in sorted_dist[-5:] if v < 0.05]
        dist_info = f"""
Current exploration distribution:
- OVEREXPLORED: {', '.join(overexplored)}
- UNDEREXPLORED: {', '.join(underexplored)}
"""

    prompt = f"""Given this root claim for ARAW exploration:
"{root_claim}"
{dist_info}
Which domains are MOST IMPORTANT to explore for this specific question?
Rate each domain 0-3:
- 0 = irrelevant to this question
- 1 = somewhat relevant
- 2 = important
- 3 = critical/essential

Domains: {', '.join(ALL_DOMAINS)}

Output JSON like: {{"HUMAN": 2, "INSTITUTIONAL": 3, "ENVIRONMENTAL": 1, ...}}
Include ALL domains with their scores."""

    payload = {
        "model": DEFAULT_MODEL,
        "max_output_tokens": 1000,
        "text": {"format": {"type": "json_object"}},
        "input": [{"role": "user", "content": [{"type": "input_text", "text": prompt}]}],
    }

    ok, resp = api_call(api_key, payload)
    if not ok:
        return {d: 1 for d in ALL_DOMAINS}  # Default equal weights

    text = extract_text(resp)
    try:
        weights = json.loads(text)
        # Normalize to ensure all domains present
        return {d: weights.get(d, 1) for d in ALL_DOMAINS}
    except:
        return {d: 1 for d in ALL_DOMAINS}


def compute_focus_domains(weights: dict, current_distribution: Optional[dict] = None, top_n: int = 5) -> List[str]:
    """Compute which domains to emphasize based on weights and current distribution"""
    scores = {}
    for domain in ALL_DOMAINS:
        weight = weights.get(domain, 1)
        # Boost score for underexplored domains
        if current_distribution:
            coverage = current_distribution.get(domain, 0)
            # Lower coverage = higher priority
            coverage_boost = max(0, 0.1 - coverage) * 10  # Up to 1.0 boost for <1% coverage
            scores[domain] = weight + coverage_boost
        else:
            scores[domain] = weight

    # Return top N domains to focus on
    sorted_domains = sorted(scores.items(), key=lambda x: -x[1])
    return [d for d, _ in sorted_domains[:top_n]]


# JSON Schema for ARAW branch generation
ARAW_SCHEMA = {
    "name": "araw_branches",
    "schema": {
        "type": "object",
        "properties": {
            "if_true_consequences": {
                "type": "array",
                "items": {"type": "string"},
                "description": "2-3 different DOWNSTREAM consequences that follow if this claim is true. Cover different aspects: practical implications, emotional impacts, and logical necessities.",
                "minItems": 2,
                "maxItems": 3
            },
            "upstream_causes": {
                "type": "array",
                "items": {"type": "string"},
                "description": "2-4 upstream assumptions from DIFFERENT DOMAINS that would explain this claim. MUST include diverse categories: one about people/psychology, one about systems/institutions, one about facts/evidence. Avoid repetition.",
                "minItems": 2,
                "maxItems": 4
            },
            "confidence": {
                "type": "number",
                "description": "0.0-1.0: How confident that these are the RIGHT upstream causes to explore?"
            },
            "is_crux": {
                "type": "boolean",
                "description": "TRUE if this is a CRUX/DECISIVE claim - where learning it's true vs false would DRAMATICALLY change the probability of the ROOT CLAIM. FALSE if it's context/background that doesn't really change the conclusion either way. Most claims (~80%) should be FALSE. Only mark TRUE for genuinely pivotal claims."
            },
            "is_foundational": {
                "type": "boolean",
                "description": "TRUE only if: (1) direct sensory observation that cannot be decomposed ('I see red'), (2) definitional/tautological ('bachelors are unmarried'), (3) asking 'why' produces ONLY synonyms or restatements. BE STRICT - most claims are NOT foundational. Mark FALSE (keep exploring) for: philosophical claims (even if they sound deep), claims about how systems work, generalizations, causal claims, anything where reasonable people could disagree. The test: if someone could argue against this claim, it is NOT foundational."
            },
            "effort_to_address": {
                "type": "string",
                "enum": ["LOW", "MEDIUM", "HIGH"],
                "description": "How much effort to verify or address this claim? LOW = quick check, single action. MEDIUM = requires research or multiple steps. HIGH = major undertaking, significant resources."
            },
            "potential_impact": {
                "type": "string",
                "enum": ["LOW", "MEDIUM", "HIGH"],
                "description": "If this claim is resolved (proven true or false), how much would it change understanding of the root question? LOW = minor detail. MEDIUM = meaningful but not decisive. HIGH = would significantly shift conclusions."
            },
            "direct_path": {
                "type": "boolean",
                "description": "Is there a DIRECT way to verify or address this claim? TRUE if you can go straight to a source, run an experiment, or take a specific action. FALSE if it requires indirect inference, building reputation first, or hoping for opportunity."
            }
        },
        "required": ["if_true_consequences", "upstream_causes", "confidence", "is_crux", "is_foundational", "effort_to_address", "potential_impact", "direct_path"],
        "additionalProperties": False
    }
}

SYSTEM_PROMPT = """You are an expert at ARAW (Assume Right Assume Wrong) causal search.

ARAW explores WHY a claim might be true or false by finding UPSTREAM ASSUMPTIONS.

Given a CLAIM and the ORIGINAL PROBLEM it relates to, generate:

1. IF_TRUE_CONSEQUENCES (2-3): What DOWNSTREAM consequences follow if this claim is true?
   - Provide MULTIPLE different consequences covering different aspects
   - Include: practical implications, emotional/psychological impacts, logical necessities

2. UPSTREAM_CAUSES (2-4): What UPSTREAM assumptions would explain this claim?

   **CRITICAL: DIVERSIFY ACROSS DOMAINS - pick from DIFFERENT categories:**

   Core domains:
   - HUMAN: Individual psychology, competence, motivation, honesty, biases
   - INSTITUTIONAL: Organizations, policies, incentives, bureaucracy, governance
   - EVIDENTIAL: Data, measurements, observations, research findings
   - EPISTEMOLOGICAL: How we know, logic, reasoning, certainty, methodology
   - PRACTICAL: Resources, time, money, feasibility, implementation
   - RELATIONAL: Trust, communication, relationships, social dynamics

   Often overlooked domains (USE THESE MORE):
   - ETHICAL: Values, morals, fairness, justice, rights, competing goods
   - TEMPORAL: Historical trends, future trajectories, generational change, timing
   - CULTURAL: Traditions, norms, worldviews, non-Western perspectives
   - ENVIRONMENTAL: Climate, ecology, sustainability, physical environment
   - TECHNOLOGICAL: AI, automation, biotech, digital transformation, innovation
   - GEOPOLITICAL: International relations, power dynamics, conflict, cooperation
   - EXISTENTIAL: Long-term risks, survival, catastrophic scenarios
   - DEMOGRAPHIC: Population, aging, migration, urbanization, birth rates
   - BIOLOGICAL: Health, disease, longevity, mental health, human nature
   - ECONOMIC: Inequality, markets, development, trade, incentive structures
   - INFORMATIONAL: Media, misinformation, narratives, attention, propaganda
   - SYSTEMIC: Feedback loops, complexity, emergence, unintended consequences

   **AVOID**: Multiple causes from the same domain. Actively seek NEGLECTED domains.

3. IS_CRUX (true/false): Is this a PIVOTAL claim that would flip the root conclusion?

   TRUE = CRUX NODE (~15-20% of claims): Learning this is true vs false DRAMATICALLY changes belief in root claim.
   - "The lab test was contaminated" → flips diagnosis reliability
   - "The defendant has an alibi" → flips guilt assessment
   - "Climate models have systemic bias" → flips confidence in predictions

   FALSE = CONTEXT NODE (~80-85% of claims): Interesting but doesn't really change the conclusion.
   - "Doctor went to a good school" → doesn't flip diagnosis accuracy
   - "The witness wore glasses" → doesn't change verdict
   - "Hospital has modern facilities" → background context only

   Ask: "If I learned this claim was definitely TRUE, would I update my belief in the root claim by more than 20%? What about if FALSE?"
   If yes to either → is_crux = true. If neither moves the needle much → is_crux = false.

4. IS_FOUNDATIONAL: Be STRICT - most claims are NOT foundational. Mark TRUE only if:
   - Direct sensory observation that cannot be further decomposed ("I see a red light")
   - Definitional/tautological truth ("A bachelor is unmarried by definition")
   - Asking "why" produces ONLY synonyms or restatements, not new information

   Mark FALSE (keep exploring) for:
   - Philosophical claims - even if they sound profound ("you can't know anything for certain")
   - Claims about how systems/institutions work - these have upstream mechanisms
   - Generalizations ("X tends to cause Y") - these can be questioned with counterexamples
   - Causal claims - causation always has upstream assumptions
   - Anything where reasonable people could disagree

   The test: Could someone argue against this claim? If yes → NOT foundational.

5. EFFORT_TO_ADDRESS: How much effort to verify or address this claim?
   - LOW: Quick check, single source, one action (e.g., "look up the statistic", "ask one person")
   - MEDIUM: Requires research, multiple steps, some coordination (e.g., "survey 10 people", "analyze data")
   - HIGH: Major undertaking, significant resources, long timeline (e.g., "run a study", "build an organization")

6. POTENTIAL_IMPACT: If resolved, how much would it change understanding?
   - LOW: Minor detail, doesn't really affect conclusions
   - MEDIUM: Meaningful insight, shifts some beliefs
   - HIGH: Would significantly change conclusions or actions on root question

7. DIRECT_PATH: Is there a direct way to address this?
   - TRUE: Can go straight to source, run experiment, take specific action
   - FALSE: Requires indirect inference, reputation building, waiting for opportunity

**PRIORITY GUIDANCE:**
- LOW effort + HIGH impact + direct path = EXPLORE FIRST (obvious wins)
- HIGH effort + LOW impact = DEPRIORITIZE (busy work trap)
- HIGH impact + no direct path = FIND ALTERNATIVE PATH or accept uncertainty

OUTPUT ONLY FACTUAL CLAIMS about the world (not actions, intentions, or meta-commentary).
Do not repeat themes already explored in the causal chain.

**CRITICAL: AVOID CORPORATE SPEAK AND VAGUENESS**
- BAD: "improved outcomes", "data-driven decisions", "enhanced performance", "stakeholder alignment"
- BAD: "planners may feel validated", "teams might experience increased confidence"
- BAD: "leads to better results", "improves decision-making", "reduces uncertainty"

**GOOD EXAMPLES - Be this specific:**
- GOOD: "Planning step X is skipped 40% of the time under deadline pressure"
- GOOD: "Organizations with >100 employees rarely complete all 22 steps"
- GOOD: "Categorical thresholds hide the difference between 51% and 99% confidence"
- GOOD: "Medical tests have false positive rates that vary 10x across labs"
- GOOD: "Second opinions disagree with initial diagnosis 30% of the time for condition X"
- GOOD: "The person making this claim has financial incentive to believe it"
- GOOD: "Historical data shows this intervention worked in 3 of 7 similar cases"
- GOOD: "The measurement instrument has known calibration issues above threshold Y"

**KEY QUESTION FOR EACH CLAIM: "Why should we continue exploring this branch?"**
- If exploring this wouldn't change understanding of root claim → lower priority
- If this branch has already been explored from different angles → lower priority
- If this is a crux that would flip the conclusion → high priority

Be SPECIFIC. Name concrete mechanisms, measurable quantities, specific failure modes.
If you can't make it concrete, mark is_foundational=true instead of generating vague claims."""


def generate_branches(
    api_key: str,
    claim: str,
    root_claim: Optional[str] = None,
    causal_chain: Optional[str] = None,
    model: str = DEFAULT_MODEL,
    focus_domains: Optional[List[str]] = None
) -> Optional[dict]:
    """Use LLM to generate ARAW branches with causal reasoning"""

    # Build context-aware prompt
    context_section = ""
    if root_claim:
        context_section += f"ORIGINAL PROBLEM: \"{root_claim}\"\n"
    if causal_chain:
        context_section += f"CAUSAL CHAIN SO FAR: {causal_chain}\n"

    # Add existing explored themes to avoid repetition
    explored_hint = ""
    if causal_chain:
        explored_hint = f"\nALREADY EXPLORED THEMES (avoid repeating): {causal_chain}"

    # Add focus domains if specified
    domain_hint = ""
    if focus_domains:
        domain_hint = f"\n**PRIORITY DOMAINS (include at least one from these):** {', '.join(focus_domains)}"

    user_prompt = f"""{context_section}{explored_hint}

CURRENT CLAIM TO ANALYZE: "{claim}"
{domain_hint}
Generate:
1. if_true_consequences: 2-3 DIFFERENT downstream consequences
2. upstream_causes: 2-4 upstream assumptions from DIFFERENT DOMAINS{' - PRIORITIZE: ' + ', '.join(focus_domains) if focus_domains else ''}
3. confidence: How confident these are the right causes?
4. is_crux: Would learning this is TRUE vs FALSE change belief in root claim by >20%? Only ~15-20% of claims are crux nodes.
5. is_foundational: Be STRICT - only mark true if direct observation, definitional, or asking "why" only produces synonyms. Philosophical claims are NOT foundational.
6. effort_to_address: LOW/MEDIUM/HIGH - how much effort to verify or address this claim?
7. potential_impact: LOW/MEDIUM/HIGH - if resolved, how much would it change understanding of root question?
8. direct_path: TRUE if there's a direct way to verify (go to source, run test), FALSE if indirect only."""

    payload = {
        "model": model,
        "max_output_tokens": 1500,
        "text": {"format": {"type": "json_schema", "name": ARAW_SCHEMA["name"], "schema": ARAW_SCHEMA["schema"]}},
        "reasoning": {"effort": "low"},
        "input": [
            {"role": "system", "content": [{"type": "input_text", "text": SYSTEM_PROMPT}]},
            {"role": "user", "content": [{"type": "input_text", "text": user_prompt}]},
        ],
    }

    ok, resp = api_call(api_key, payload)

    if not ok:
        print(f"  API error: {resp.get('error', 'unknown')}")
        body = resp.get('body', '')
        if body:
            print(f"  Details: {body[:200]}")
        return None

    text = extract_text(resp)
    if not text:
        print(f"  Empty response")
        return None

    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        print(f"  JSON decode error: {e}")
        return None


VAGUE_PATTERNS = [
    "the claim", "if true", "if false", "could be wrong", "might be wrong",
    "is uncertain", "needs examination", "should be examined", "warrants further",
    "multiple ways", "several ways", "various ways",
    "if this claim", "if the claim", "assuming the claim", "accepting the claim",
    "this claim is", "claim is true", "claim is false"
]

# Actions start with imperative verbs - can't be assumed true/false
ACTION_STARTS = [
    "complete ", "identify ", "schedule ", "create ", "build ", "start ",
    "begin ", "make ", "do ", "go ", "take ", "get ", "find ", "apply ",
    "research ", "explore ", "evaluate ", "assess ", "develop ", "prepare ",
    "draft ", "write ", "send ", "contact ", "reach ", "set ", "plan ",
    "update ", "revise ", "review ", "conduct ", "perform ", "execute ",
    "pursue ", "seek ", "aim ", "focus ", "target ", "prioritize ",
]

# Intention/desire statements (disguised actions)
INTENTION_PATTERNS = [
    "i will ", "i would ", "i should ", "i could ", "i might ",
    "i need to ", "i must ", "i have to ", "i ought to ",
    "i am going to ", "i plan to ", "i intend to ", "i want to ",
    "we will ", "we would ", "we should ", "we could ",
    # Action verbs with "I" subject
    "i pivot ", "i switch ", "i move ", "i transition ", "i change ",
    "i apply ", "i pursue ", "i seek ", "i target ", "i focus ",
    "i can ", "i am able to ",  # ability claims often hide intentions
]

# Vague modal claims without clear subject-predicate
VAGUE_MODAL_PATTERNS = [
    " could be ", " would be ", " might be ", " may be ",
    " could work", " would work", " might work",
    " could help", " would help", " might help",  # these are actually okay if they have clear subject
]

# Prescriptive (value judgements about what should happen)
PRESCRIPTIVE_PATTERNS = [
    "should be ", "ought to be ", "needs to be ", "must be ",
    "should prioritize", "should focus", "should consider",
]

# Schema leakage - LLM confusing JSON schema fields with topics to explore
SCHEMA_LEAKAGE_PATTERNS = [
    "leverage_score", "leverage score", "the leverage",
    "is_foundational", "foundational claim",
    "assume_right", "assume_wrong", "branch type",
    # Technical metric language that indicates schema confusion
    "% of the total", "of the total metric", "total metric",
    "component weight", "weighted at", "weight of 0.",
    "accounts for", "contributes to the",
    "remaining components", "other components",
    "the final score", "scoring model", "evaluation score",
    # Numerical drift patterns
    "components sum to", "sum to 1", "sum to 0.",
    "the components are", "three components", "two components", "four components", "five components",
    "first component", "second component", "third component",
    "is allocated to", "is 0.", " 0.0", "totaling 1.0",
    "probability distribution", "residual variance",
    "shap value", "predictive power",
    # Statistical/ML jargon
    "variance", "percentile", "z-score", "weighted sum",
    "the model relies", "the model uses", "features with",
    "99% of the", "97% of", "% of the outcome",
    "observation", "composite metric", "metric evaluat",
]

# Regex to find decimal numbers like 0.85, 0.04, etc.
DECIMAL_PATTERN = re.compile(r'\b0\.\d+\b')

# Corporate speak - vague business jargon that doesn't say anything concrete
CORPORATE_SPEAK_PATTERNS = [
    "data-driven", "data driven",
    "reduced ambiguity", "reduced uncertainty",
    "increased confidence", "increased clarity", "increased trust", "increased morale",
    "improved outcomes", "improved performance", "improved morale", "improved results",
    "better outcomes", "better results", "better performance",
    "more consistent", "more predictable", "more reliable", "more efficient",
    "enhanced ", "optimized ", "streamlined ", "leveraged ",
    "stakeholder ", "buy-in", "alignment",
    "operational efficiency", "operational excellence",
    "strategic planning", "strategic vision", "strategic alignment",
    "decision-making", "decision making",
    "accountability", "transparency", "synergy", "scalab",
    "best practice", "value-add", "value add",
    "moving forward", "going forward", "proactive",
    "holistic", "end-to-end", "robust solution",
]

# Feeling/experience claims that are too psychological without substance
FEELING_PATTERNS = [
    "may feel ", "might feel ", "could feel ",
    "may experience ", "might experience ", "could experience ",
    "feel validated", "feel motivated", "feel disengaged",
    "feel increased", "feel decreased", "feel reduced",
    "experience increased", "experience decreased", "experience reduced",
    "experience change", "experience stress", "experience fatigue",
    "job satisfaction", "employee satisfaction", "team morale",
    "sense of competence", "sense of self-efficacy", "sense of purpose",
    "psychological safety", "emotional wellbeing",
]

# Tautological patterns - claims that say nothing substantive
TAUTOLOGICAL_PATTERNS = [
    "leads to outcomes", "leads to results",
    "affects performance", "impacts results",
    "influences outcomes", "determines success",
    "if x then x",  # literal tautology
    "the more x the more x",  # correlation tautology
]

def is_claim_valid(claim: str, strict: bool = True) -> tuple[bool, str]:
    """
    Check if a claim is a valid belief (not action, intention, or meta).
    Returns (valid, reason).

    If strict=False, only checks for definite problems (actions, schema leak).
    If strict=True, also checks for corporate speak, feelings, etc.
    """
    claim_lower = claim.lower().strip()

    # ALWAYS CHECK - these are definitely not explorable claims
    # Check for imperative starts (actions)
    for action in ACTION_STARTS:
        if claim_lower.startswith(action):
            return False, "ACTION"

    # Check for intention patterns
    for intention in INTENTION_PATTERNS:
        if claim_lower.startswith(intention):
            return False, "INTENT"

    # Check for schema leakage (LLM confusing JSON schema with topics)
    for leak in SCHEMA_LEAKAGE_PATTERNS:
        if leak in claim_lower:
            return False, "SCHEMA_LEAK"

    # Check for numerical-heavy claims (more than 2 decimal numbers)
    decimal_matches = DECIMAL_PATTERN.findall(claim_lower)
    if len(decimal_matches) >= 2:
        return False, "NUMERICAL"

    # Check for meta patterns
    for pattern in VAGUE_PATTERNS:
        if pattern in claim_lower:
            return False, "META"

    # STRICT MODE - also check for likely-bad but potentially-valid patterns
    if strict:
        # Check for prescriptive patterns
        for prescriptive in PRESCRIPTIVE_PATTERNS:
            if prescriptive in claim_lower:
                return False, "PRESCRIPTIVE"

        # Check for corporate speak
        for corp in CORPORATE_SPEAK_PATTERNS:
            if corp in claim_lower:
                return False, "CORPORATE"

        # Check for feeling/experience patterns (too psychological)
        for feel in FEELING_PATTERNS:
            if feel in claim_lower:
                return False, "FEELING"

        # Check for tautologies
        for taut in TAUTOLOGICAL_PATTERNS:
            if taut in claim_lower:
                return False, "TAUTOLOGY"

    return True, "OK"


def check_relevancy_heuristic(claim: str, root_claim: str) -> tuple[bool, str, float]:
    """
    Quick heuristic check for relevancy.
    Returns (is_relevant, reason, confidence).
    """
    claim_lower = claim.lower()
    root_lower = root_claim.lower()

    # Check for drift signals
    drift_count = sum(1 for sig in DRIFT_SIGNALS if sig in claim_lower)
    concrete_count = sum(1 for sig in CONCRETE_SIGNALS if sig in claim_lower)

    # Strong drift signal
    if drift_count >= 2 and concrete_count == 0:
        return False, "abstract drift (multiple drift signals)", 0.7

    # Check for word overlap with root claim (simple relevancy)
    root_words = set(root_lower.split()) - {'the', 'a', 'an', 'is', 'are', 'to', 'of', 'and', 'or', 'that', 'this'}
    claim_words = set(claim_lower.split()) - {'the', 'a', 'an', 'is', 'are', 'to', 'of', 'and', 'or', 'that', 'this'}
    overlap = len(root_words & claim_words)

    # Very low overlap might indicate drift
    if len(root_words) > 3 and overlap == 0 and drift_count > 0:
        return False, "no connection to root claim + drift signals", 0.6

    # Concrete signals are good
    if concrete_count >= 2:
        return True, "concrete/specific", 0.8

    return True, "neutral", 0.5


RELEVANCY_SCHEMA = {
    "name": "relevancy_evaluation",
    "schema": {
        "type": "object",
        "properties": {
            "relevant": {
                "type": "boolean",
                "description": "True if claim is directly relevant to exploring the root question"
            },
            "connection": {
                "type": "string",
                "description": "How does this claim connect to the root question? Be specific."
            },
            "drift_type": {
                "type": "string",
                "enum": ["NONE", "SIDEWAYS", "ABSTRACT", "TANGENT"],
                "description": "NONE=on topic, SIDEWAYS=related but not causal, ABSTRACT=too general, TANGENT=unrelated"
            }
        },
        "required": ["relevant", "connection", "drift_type"],
        "additionalProperties": False
    }
}


def llm_evaluate_relevancy(api_key: str, claim: str, root_claim: str, model: str = DEFAULT_MODEL) -> tuple[bool, str, str]:
    """
    Use LLM to objectively evaluate relevancy of claim to root question.
    Returns (is_relevant, connection_explanation, drift_type).
    """
    prompt = f"""Evaluate if this claim is RELEVANT to exploring the root question.

ROOT QUESTION: "{root_claim[:150]}"

CLAIM TO EVALUATE: "{claim[:200]}"

Is this claim directly useful for understanding or answering the root question?

RELEVANT = claim helps answer or understand the root question
NOT RELEVANT = claim is about something tangential, too abstract, or drifted sideways

drift_type:
- NONE: Claim is on topic and useful
- SIDEWAYS: Related topic but doesn't help answer the root question
- ABSTRACT: Too general/philosophical, not actionable
- TANGENT: Unrelated to root question"""

    payload = {
        "model": model,
        "max_output_tokens": 500,
        "text": {"format": {"type": "json_schema", "name": RELEVANCY_SCHEMA["name"], "schema": RELEVANCY_SCHEMA["schema"]}},
        "reasoning": {"effort": "low"},
        "input": [{"role": "user", "content": [{"type": "input_text", "text": prompt}]}],
    }

    ok, resp = api_call(api_key, payload, timeout=30)
    if not ok:
        return True, "LLM failed, defaulting to relevant", "NONE"

    text = extract_text(resp)
    if not text:
        return True, "Empty response", "NONE"

    try:
        result = json.loads(text)
        return (
            result.get("relevant", True),
            result.get("connection", "unknown"),
            result.get("drift_type", "NONE")
        )
    except:
        return True, "JSON parse failed", "NONE"


EVAL_SCHEMA = {
    "name": "claim_evaluation",
    "schema": {
        "type": "object",
        "properties": {
            "explore": {
                "type": "boolean",
                "description": "True if claim is worth exploring, false if vague/feeling-based/irrelevant"
            },
            "why": {
                "type": "string",
                "description": "Brief reason for decision"
            },
            "drift_type": {
                "type": "string",
                "enum": ["NONE", "SIDEWAYS", "ABSTRACT", "TANGENT"],
                "description": "NONE=on topic, SIDEWAYS=related but not causal, ABSTRACT=too general, TANGENT=unrelated"
            }
        },
        "required": ["explore", "why", "drift_type"],
        "additionalProperties": False
    }
}


def llm_evaluate_claim(api_key: str, claim: str, root_claim: str, model: str = DEFAULT_MODEL) -> tuple[bool, str, float, str]:
    """
    Use LLM to evaluate whether a claim is worth exploring.
    Returns (should_explore, reason, confidence, drift_type).

    This replaces/augments hardcoded pattern matching with nuanced LLM judgment.
    Combined with relevancy check to avoid double API calls.
    """
    prompt = f"""Evaluate if this claim is worth exploring for the root question.

ROOT QUESTION: "{root_claim[:150]}"

CLAIM: "{claim[:200]}"

REJECT (explore=false) if:
- Vague ("improved outcomes", "better results")
- Feeling-based ("may feel", "might experience")
- Action/intention ("should do", "needs to")
- Tautology or circular
- Irrelevant to root question

ACCEPT (explore=true) if: specific, factual, explorable, relevant to root question.

drift_type:
- NONE: Claim directly helps answer root question
- SIDEWAYS: Related topic but doesn't advance understanding of root
- ABSTRACT: Too general/philosophical, not actionable or testable
- TANGENT: Unrelated to root question"""

    payload = {
        "model": model,
        "max_output_tokens": 500,
        "text": {"format": {"type": "json_schema", "name": EVAL_SCHEMA["name"], "schema": EVAL_SCHEMA["schema"]}},
        "reasoning": {"effort": "low"},
        "input": [{"role": "user", "content": [{"type": "input_text", "text": prompt}]}],
    }

    ok, resp = api_call(api_key, payload, timeout=30)
    if not ok:
        return True, "LLM evaluation failed, defaulting to accept", 0.5, "NONE"

    text = extract_text(resp)
    if not text:
        return True, "Empty response, defaulting to accept", 0.5, "NONE"

    try:
        result = json.loads(text)
        return (
            result.get("explore", True),
            result.get("why", "no reason given"),
            0.7,
            result.get("drift_type", "NONE")
        )
    except:
        return True, "JSON parse failed, defaulting to accept", 0.5, "NONE"


class ARAWLLMExpander:
    """Expands ARAW trees using LLM-generated branches with parallel API calls."""

    # All available strategies
    ALL_STRATEGIES = ["leverage_first", "depth_first", "breadth_first", "frontier", "balanced", "random", "mixed"]

    def __init__(self, engine: ARAWEngine, api_key: str, model: str = DEFAULT_MODEL, parallel: int = 1, rate_limit: float = 2.0, check_similarity: bool = True, log_width: int = 120, focus_domains: Optional[List[str]] = None, gate_interval: int = 0, llm_filter: bool = False, relevancy_filter: bool = False, checkpoint: int = 0):
        self.engine = engine
        self.api_key = api_key
        self.model = model
        self.parallel = parallel  # Number of concurrent API calls (should be high due to API latency)
        self.rate_limit = rate_limit  # Max requests per second
        self.log_width = log_width  # Width for claim truncation in logs (0 = no truncation)
        self.check_similarity = check_similarity  # Whether to check for similar claims
        self.focus_domains = focus_domains or []  # Domains to emphasize in exploration
        self.gate_interval = gate_interval  # Apply "why continue?" gate every N nodes (0 = disabled)
        self.llm_filter = llm_filter  # Use LLM to evaluate claims instead of hardcoded patterns
        self.relevancy_filter = relevancy_filter  # Use LLM to evaluate relevancy (requires llm_filter=True)
        self.checkpoint = checkpoint  # Pause every N nodes for human review (0 = disabled)
        self.nodes_created = 0
        self.requests_made = 0
        self.start_time = None
        self.log_interval = 10
        self.db_lock = threading.Lock()
        self.rate_lock = threading.Lock()  # Separate lock for rate limiting
        self.last_request_time = 0
        self.current_strategy = "balanced"  # Track current strategy for node tagging
        self.nodes_by_strategy = {}  # Track nodes created per strategy
        self.nodes_since_gate = 0  # Track nodes since last gate check
        self.gate_skipped = 0  # Track how many nodes skipped by gate
        self.llm_rejected = 0  # Track claims rejected by LLM evaluation
        self.relevancy_rejected = 0  # Track claims rejected by relevancy filter
        self.last_checkpoint = 0  # Track nodes at last checkpoint

    def _trunc(self, text: str) -> str:
        """Truncate text for logging based on log_width setting"""
        if self.log_width <= 0 or len(text) <= self.log_width:
            return text
        return text[:self.log_width] + "..."

    def _why_continue_node(self, node: Node) -> Tuple[bool, str]:
        """
        Apply "why continue?" gate to a node.
        Returns (should_continue, reason).

        This makes the decision to explore conscious rather than automatic.
        Uses effort/impact scoring when available.
        """
        # Always continue for root - need to build tree
        if node.depth == 0:
            return True, "root node"

        # Check if this branch has low leverage and isn't a crux
        content = node.content or {}
        is_crux = content.get("is_crux", False)
        leverage = node.leverage_score or 0.5

        # New: effort/impact scoring
        effort = content.get("effort_to_address", "MEDIUM")
        impact = content.get("potential_impact", "MEDIUM")
        direct_path = content.get("direct_path", True)

        # HIGH priority: Low effort + High impact + Direct path = EXPLORE FIRST
        if effort == "LOW" and impact == "HIGH" and direct_path:
            return True, "LOW effort + HIGH impact + direct path - obvious win"

        # HIGH priority: Crux nodes
        if is_crux:
            return True, "crux node - could flip conclusion"

        # HIGH priority: High impact regardless of effort
        if impact == "HIGH":
            return True, f"HIGH impact (effort={effort})"

        # MEDIUM priority: High leverage
        if leverage >= 0.7:
            return True, f"high leverage ({leverage:.2f})"

        # DEPRIORITIZE: High effort + Low impact = busy work trap
        if effort == "HIGH" and impact == "LOW":
            return False, f"HIGH effort + LOW impact - busy work trap"

        # DEPRIORITIZE: No direct path + low impact
        if not direct_path and impact == "LOW":
            return False, f"no direct path + LOW impact"

        # Depth-based thresholds
        if node.depth >= 3 and leverage < 0.3:
            return False, f"depth {node.depth} + very low leverage ({leverage:.2f})"

        if node.depth >= 4 and leverage < 0.5:
            return False, f"depth {node.depth} + low leverage ({leverage:.2f})"

        # Default: continue
        return True, f"continue (depth={node.depth}, effort={effort}, impact={impact})"

    def _apply_gate_interval(self) -> bool:
        """
        Check if we should pause for "why continue?" at interval.
        Returns True if should continue, False if user wants to stop.
        """
        if self.gate_interval <= 0:
            return True

        self.nodes_since_gate += 1
        if self.nodes_since_gate < self.gate_interval:
            return True

        # Time to apply gate
        self.nodes_since_gate = 0

        with self.db_lock:
            stats = self.engine.get_stats()

        print(f"\n{'='*60}")
        print(f"WHY CONTINUE? GATE CHECK")
        print(f"{'='*60}")
        print(f"Nodes created: {self.nodes_created}")
        print(f"Nodes skipped by gate: {self.gate_skipped}")
        print(f"Total in tree: {stats['total_nodes']}")
        print(f"Unexplored: {stats['by_status'].get('unexplored', 0)}")
        print(f"Max depth: {stats['max_depth']}")
        print(f"\nWhy continue this exploration?")
        print(f"  - Articulable: {stats['by_status'].get('unexplored', 0)} nodes still unexplored")
        print(f"  - Felt: (your judgment)")
        print(f"\nPress Enter to continue, 'q' to quit, 's' for stats: ", end="", flush=True)

        try:
            response = input().strip().lower()
            if response == 'q':
                return False
            elif response == 's':
                self._print_summary()
                return self._apply_gate_interval()  # Ask again after showing stats
        except EOFError:
            return True  # Non-interactive, continue

        return True

    def _apply_checkpoint(self) -> bool:
        """
        Check if we should pause for human review at checkpoint.
        Returns True if should continue, False if user wants to stop.
        """
        if self.checkpoint <= 0:
            return True

        nodes_since_checkpoint = self.nodes_created - self.last_checkpoint
        if nodes_since_checkpoint < self.checkpoint:
            return True

        # Time for checkpoint
        self.last_checkpoint = self.nodes_created

        with self.db_lock:
            stats = self.engine.get_stats()
            root_claim = self._get_root_claim()

            # Get sample of recent nodes
            cursor = self.engine.conn.execute("""
                SELECT claim, leverage_score, content
                FROM nodes
                ORDER BY id DESC LIMIT 5
            """)
            recent = list(cursor)

            # Get top frontier
            cursor = self.engine.conn.execute("""
                SELECT claim, leverage_score
                FROM nodes WHERE status = 'unexplored'
                ORDER BY leverage_score DESC LIMIT 3
            """)
            frontier = list(cursor)

        print(f"\n{'='*70}")
        print(f"🔍 HUMAN CHECKPOINT ({self.nodes_created} nodes created)")
        print(f"{'='*70}")
        print(f"Root: {root_claim[:60]}...")
        print(f"Total: {stats['total_nodes']} | Unexplored: {stats['by_status'].get('unexplored', 0)}")

        print(f"\n📝 RECENT ADDITIONS:")
        for row in recent:
            content = json.loads(row['content']) if row['content'] else {}
            effort = content.get('effort_to_address', '?')[0]
            impact = content.get('potential_impact', '?')[0]
            print(f"  E:{effort} I:{impact} | {row['claim'][:55]}...")

        print(f"\n🔭 TOP FRONTIER:")
        for row in frontier:
            print(f"  [{row['leverage_score'] or 0.5:.2f}] {row['claim'][:55]}...")

        print(f"\n" + "-"*70)
        print(f"Options:")
        print(f"  [Enter] Continue exploration")
        print(f"  [q]     Quit and save")
        print(f"  [s]     Show full summary")
        print(f"  [f]     Focus on specific domain (will prompt)")
        print(f"\nYour choice: ", end="", flush=True)

        try:
            response = input().strip().lower()
            if response == 'q':
                return False
            elif response == 's':
                self._print_summary()
                return self._apply_checkpoint()
            elif response == 'f':
                print("Enter domain to focus on (e.g., INSTITUTIONAL, EVIDENTIAL): ", end="", flush=True)
                domain = input().strip().upper()
                if domain in ALL_DOMAINS:
                    self.focus_domains = [domain]
                    print(f"Now focusing on: {domain}")
                else:
                    print(f"Unknown domain. Available: {', '.join(ALL_DOMAINS[:5])}...")
                return True
        except EOFError:
            return True  # Non-interactive, continue

        return True

    def _fetch_branches(self, node: Node) -> Tuple[Node, Optional[dict], Optional[str], Optional[str]]:
        """Fetch branches from API (thread-safe, no DB writes)"""
        claim = node.claim

        # Get context (needs db lock)
        with self.db_lock:
            root_claim = self._get_root_claim()
            causal_chain = self._get_causal_chain(node)
            self.requests_made += 1

        # Rate limiting with separate lock (doesn't block other DB operations)
        with self.rate_lock:
            now = time.time()
            min_interval = 1.0 / self.rate_limit
            elapsed = now - self.last_request_time
            if elapsed < min_interval:
                time.sleep(min_interval - elapsed)
            self.last_request_time = time.time()

        # API call (no lock needed - runs in parallel!)
        branches = generate_branches(
            self.api_key,
            claim,
            root_claim=root_claim,
            causal_chain=causal_chain,
            model=self.model,
            focus_domains=self.focus_domains
        )
        return (node, branches, root_claim, causal_chain)

    def _claim_exists(self, claim: str) -> bool:
        """Check if this exact claim already exists anywhere in the tree"""
        cursor = self.engine.conn.cursor()
        cursor.execute("SELECT 1 FROM nodes WHERE claim = ? LIMIT 1", (claim,))
        return cursor.fetchone() is not None

    def _is_too_similar(self, new_claim: str, threshold: float = 0.7) -> bool:
        """
        Check if new claim is too similar to existing claims.
        Uses simple word overlap as a fast similarity metric.
        """
        new_words = set(new_claim.lower().split())
        if len(new_words) < 3:
            return False  # Too short to judge

        # Check against recent claims (last 500 for efficiency)
        cursor = self.engine.conn.cursor()
        cursor.execute("""
            SELECT claim FROM nodes
            ORDER BY created_at DESC
            LIMIT 500
        """)

        for row in cursor:
            existing_words = set(row['claim'].lower().split())
            if len(existing_words) < 3:
                continue

            # Jaccard similarity
            intersection = len(new_words & existing_words)
            union = len(new_words | existing_words)
            similarity = intersection / union if union > 0 else 0

            if similarity >= threshold:
                return True

        return False

    def _get_explored_domains(self, node: Node) -> set:
        """Get domains already explored in this branch (to encourage diversity)"""
        domains = set()
        cursor = self.engine.conn.cursor()

        # Get siblings (other children of same parent)
        if node.parent_id:
            cursor.execute("""
                SELECT claim FROM nodes WHERE parent_id = ?
            """, (node.parent_id,))

            for row in cursor:
                claim_lower = row['claim'].lower()
                # Detect domain from claim content
                if any(w in claim_lower for w in ['doctor', 'patient', 'competent', 'skill', 'experience', 'trust']):
                    domains.add('human')
                if any(w in claim_lower for w in ['hospital', 'system', 'policy', 'guideline', 'protocol', 'institution']):
                    domains.add('institutional')
                if any(w in claim_lower for w in ['test', 'data', 'evidence', 'result', 'diagnosis', 'imaging']):
                    domains.add('evidential')
                if any(w in claim_lower for w in ['cost', 'insurance', 'afford', 'resource', 'time', 'money']):
                    domains.add('practical')
                if any(w in claim_lower for w in ['family', 'spouse', 'relationship', 'communication', 'emotion']):
                    domains.add('relational')

        return domains

    def _evaluate_claim(self, new_claim: str, root_claim: str, depth: int = 0) -> tuple[bool, str]:
        """
        Evaluate whether a claim should be added to the tree.
        Uses LLM evaluation if llm_filter is enabled, otherwise hardcoded patterns.
        Relevancy check is now combined into LLM eval (no extra API call).
        Uses intelligent sampling to decide when to enforce relevancy strictly.
        Returns (should_add, reason).
        """
        if self.llm_filter:
            # First do quick hardcoded check for obvious failures (actions, schema leak)
            valid, reason = is_claim_valid(new_claim, strict=False)
            if not valid:
                return False, reason

            # Quick heuristic relevancy check
            relevant, rel_reason, rel_conf = check_relevancy_heuristic(new_claim, root_claim)

            # High-confidence heuristic rejection (no LLM needed)
            if not relevant and rel_conf >= 0.8:
                self.relevancy_rejected += 1
                return False, f"DRIFT: {rel_reason}"

            # LLM evaluation (now includes drift_type in same call)
            should_explore, llm_reason, confidence, drift_type = llm_evaluate_claim(
                self.api_key, new_claim, root_claim, self.model
            )

            if not should_explore:
                self.llm_rejected += 1
                return False, f"LLM ({confidence:.0%}): {llm_reason[:50]}"

            # Intelligent relevancy enforcement - check drift_type when signals indicate risk
            if self.relevancy_filter:
                should_enforce = self._should_enforce_relevancy(
                    new_claim, root_claim, depth, rel_conf, drift_type
                )

                if should_enforce and drift_type in ["SIDEWAYS", "ABSTRACT", "TANGENT"]:
                    self.relevancy_rejected += 1
                    return False, f"DRIFT ({drift_type}): {llm_reason[:40]}"

            return True, "OK"
        else:
            # Use hardcoded patterns (strict mode)
            valid, reason = is_claim_valid(new_claim, strict=True)
            if not valid:
                return False, reason

            # Still apply heuristic relevancy check
            relevant, rel_reason, rel_conf = check_relevancy_heuristic(new_claim, root_claim)
            if not relevant and rel_conf >= 0.7:
                return False, f"DRIFT: {rel_reason}"

            return True, "OK"

    def _should_enforce_relevancy(self, claim: str, root_claim: str, depth: int,
                                   heuristic_conf: float, drift_type: str) -> bool:
        """
        Intelligent sampling: decide when to strictly enforce relevancy.
        Not every claim needs strict checking - only when signals indicate risk.

        Returns True if we should reject claims with non-NONE drift_type.
        """
        # Always enforce if LLM already flagged it as drifting
        if drift_type != "NONE":
            # But use intelligent sampling to decide IF we act on it

            # 1. Deep nodes are more likely to have drifted - always check depth > 4
            if depth > 4:
                return True

            # 2. Heuristic uncertainty - if heuristic wasn't confident, trust LLM more
            if heuristic_conf < 0.6:
                return True

            # 3. Recent drift history - if we've rejected many for drift, be stricter
            drift_rate = self.relevancy_rejected / max(1, self.nodes_created)
            if drift_rate > 0.15:  # More than 15% drift rejection rate
                return True

            # 4. ABSTRACT drift is worse than SIDEWAYS - always catch it
            if drift_type == "ABSTRACT":
                return True

            # 5. TANGENT is completely off-topic - always catch
            if drift_type == "TANGENT":
                return True

            # 6. Probabilistic: enforce on ~30% of SIDEWAYS at shallow depth
            # This catches some drift without being too aggressive
            if drift_type == "SIDEWAYS" and hash(claim) % 10 < 3:
                return True

        return False

    def _write_branches(self, node: Node, branches: Optional[dict]) -> int:
        """Write branches to DB (must hold db_lock)"""
        claim = node.claim
        root_claim = self._get_root_claim() or claim

        if not branches:
            self.engine.update_status(node.id, NodeStatus.EXPLORED)
            return 0

        if branches.get("is_foundational", False):
            self.engine.update_status(node.id, NodeStatus.PRUNED)
            print(f"  [FOUNDATIONAL] {self._trunc(claim)}")
            return 0

        nodes_created = 0
        confidence = branches.get("confidence", 0.5)
        is_crux = branches.get("is_crux", False)  # Is this a pivotal/decisive claim?

        # New: effort/impact scoring
        effort = branches.get("effort_to_address", "MEDIUM")
        impact = branches.get("potential_impact", "MEDIUM")
        direct_path = branches.get("direct_path", True)

        # Compute leverage based on effort/impact/crux
        # Priority: LOW effort + HIGH impact + direct = highest leverage
        if effort == "LOW" and impact == "HIGH" and direct_path:
            leverage = 0.95  # Obvious wins first
        elif is_crux:
            leverage = 0.9  # Crux nodes high priority
        elif impact == "HIGH":
            leverage = 0.8  # High impact even if high effort
        elif effort == "HIGH" and impact == "LOW":
            leverage = 0.1  # Busy work trap - lowest priority
        elif impact == "MEDIUM":
            leverage = 0.5
        else:
            leverage = 0.4  # Context nodes lower priority

        # Add IF_TRUE_CONSEQUENCES (multiple downstream consequences)
        if_true_list = branches.get("if_true_consequences", [])
        # Also support old "if_true" format for backwards compatibility
        if not if_true_list and branches.get("if_true"):
            if_true_list = [branches.get("if_true")]

        for i, if_true_claim in enumerate(if_true_list):
            if if_true_claim and isinstance(if_true_claim, str):
                valid, reason = self._evaluate_claim(if_true_claim, root_claim, depth=node.depth + 1)
                if not valid:
                    print(f"  [SKIP {reason}] {self._trunc(if_true_claim)}")
                elif self._claim_exists(if_true_claim):
                    print(f"  [SKIP DUP] {self._trunc(if_true_claim)}")
                elif self.check_similarity and self._is_too_similar(if_true_claim):
                    print(f"  [SKIP SIMILAR] {self._trunc(if_true_claim)}")
                else:
                    self.engine.add_node(
                        parent_id=node.id,
                        claim=if_true_claim,
                        branch_type=BranchType.ASSUME_RIGHT,
                        content={
                            "generated_by": "llm",
                            "model": self.model,
                            "parent_claim": claim,
                            "branch_reason": "downstream_consequence",
                            "consequence_rank": i + 1,
                            "is_crux": is_crux,
                            "confidence": confidence,
                            "effort_to_address": effort,
                            "potential_impact": impact,
                            "direct_path": direct_path,
                            "discovered_by_strategy": self.current_strategy
                        },
                        leverage_score=leverage
                    )
                    nodes_created += 1

        # Add each UPSTREAM CAUSE as its own node to explore
        # These are assumptions that would EXPLAIN the current claim
        upstream_causes = branches.get("upstream_causes", [])
        for i, cause in enumerate(upstream_causes):
            if cause and isinstance(cause, str):
                valid, reason = self._evaluate_claim(cause, root_claim, depth=node.depth + 1)
                if not valid:
                    print(f"  [SKIP {reason}] {self._trunc(cause)}")
                elif self._claim_exists(cause):
                    print(f"  [SKIP DUP] {self._trunc(cause)}")
                elif self.check_similarity and self._is_too_similar(cause):
                    print(f"  [SKIP SIMILAR] {self._trunc(cause)}")
                else:
                    self.engine.add_node(
                        parent_id=node.id,
                        claim=cause,
                        branch_type=BranchType.ASSUME_WRONG,
                        content={
                            "generated_by": "llm",
                            "model": self.model,
                            "parent_claim": claim,
                            "branch_reason": "upstream_cause",
                            "cause_rank": i + 1,
                            "is_crux": is_crux,
                            "confidence": confidence,
                            "effort_to_address": effort,
                            "potential_impact": impact,
                            "direct_path": direct_path,
                            "discovered_by_strategy": self.current_strategy
                        },
                        leverage_score=leverage
                    )
                    nodes_created += 1

        self.engine.update_status(node.id, NodeStatus.EXPLORED)
        return nodes_created

    def _expand_root_diverse(self, root_node: Node) -> int:
        """
        Special expansion for root node that ensures diverse initial branches.
        Creates branches across multiple domains to avoid narrow exploration.
        """
        root_claim = root_node.claim
        print(f"  [ROOT DIVERSITY] Generating diverse initial branches...")

        # Define diverse angles to explore for root
        diverse_prompt = f"""ORIGINAL CLAIM: "{root_claim}"

This is the ROOT of an exploration tree. Generate MAXIMALLY DIVERSE initial branches.

Pick upstream causes from DIFFERENT domains. Prioritize UNDEREXPLORED domains like:
- ETHICAL: What values define this? Whose ethics? What tradeoffs?
- TEMPORAL: Historical context? Future trajectories? Generational differences?
- CULTURAL: Different cultural perspectives? Non-Western views?
- ENVIRONMENTAL: Ecological factors? Climate? Sustainability?
- TECHNOLOGICAL: How does technology affect this? AI? Automation?
- GEOPOLITICAL: International dynamics? Power structures? Conflict?
- EXISTENTIAL: Long-term risks? Survival implications?
- DEMOGRAPHIC: Population trends? Migration? Urbanization?
- BIOLOGICAL: Health factors? Human nature? Evolution?
- ECONOMIC: Inequality? Markets? Incentive structures?
- INFORMATIONAL: Media narratives? Misinformation? Attention?
- SYSTEMIC: Feedback loops? Complexity? Unintended consequences?

Also include at least one from: HUMAN, INSTITUTIONAL, EVIDENTIAL, PRACTICAL, RELATIONAL

Generate:
1. if_true_consequences: 3 different downstream consequences
2. upstream_causes: 4 causes from 4 DIFFERENT domains (label each with domain prefix)
3. is_crux: Is this claim pivotal? Would true vs false flip belief in root by >20%?
4. confidence and is_foundational as usual"""

        payload = {
            "model": self.model,
            "max_output_tokens": 2000,
            "text": {"format": {"type": "json_schema", "name": ARAW_SCHEMA["name"], "schema": ARAW_SCHEMA["schema"]}},
            "reasoning": {"effort": "low"},  # Keep low - medium causes empty responses
            "input": [
                {"role": "system", "content": [{"type": "input_text", "text": SYSTEM_PROMPT}]},
                {"role": "user", "content": [{"type": "input_text", "text": diverse_prompt}]},
            ],
        }

        ok, resp = api_call(self.api_key, payload)
        if not ok:
            print(f"  API error for root expansion: {resp.get('error')}")
            # Mark as explored anyway to prevent infinite loop
            self.engine.update_status(root_node.id, NodeStatus.EXPLORED)
            return 0

        text = extract_text(resp)
        if not text:
            print(f"  Empty response for root expansion")
            self.engine.update_status(root_node.id, NodeStatus.EXPLORED)
            return 0

        try:
            branches = json.loads(text)
        except json.JSONDecodeError as e:
            print(f"  JSON decode error for root: {e}")
            self.engine.update_status(root_node.id, NodeStatus.EXPLORED)
            return 0

        # Write branches with root marked
        self.current_strategy = "root_diverse"
        nodes_created = self._write_branches(root_node, branches)
        print(f"  [ROOT] Created {nodes_created} diverse initial branches")
        return nodes_created

    def _get_causal_chain(self, node: Node, max_ancestors: int = 5) -> Optional[str]:
        """
        Build causal chain from recent ancestors.
        Shows the path of reasoning that led to this claim.
        """
        chain_parts = []
        current = node
        depth = 0

        while current.parent_id and depth < max_ancestors:
            parent = self.engine.get_node(current.parent_id)
            if parent:
                # Include branch type to show the reasoning direction
                branch_indicator = "→" if current.branch_type == "assume_right" else "↗"
                chain_parts.append(f"{parent.claim[:80]}")
                current = parent
                depth += 1
            else:
                break

        if chain_parts:
            chain_parts.reverse()
            return " → ".join(chain_parts)
        return None

    def _get_root_claim(self) -> Optional[str]:
        """Get the original root claim for context anchoring"""
        return self.engine.get_root_claim()

    def run_forever(self, strategy: str = "balanced", mix_strategies: bool = False):
        """
        Run until Ctrl+C or all paths exhausted.

        Args:
            strategy: Queue strategy - "leverage_first", "depth_first", "breadth_first",
                     "frontier", "balanced", "random"
            mix_strategies: If True, use mixed strategies for diversity
        """
        self.start_time = datetime.now()

        print(f"Starting ARAW LLM-powered causal expansion")
        print(f"Model: {self.model}")
        print(f"Strategy: {'mixed' if mix_strategies else strategy}")
        print(f"Rate limit: {self.rate_limit} req/sec | Parallel: {self.parallel}")
        print(f"  (With ~5s API latency, max throughput = {self.parallel/5:.1f} req/sec)")
        print(f"Root claim: {self._get_root_claim()}")
        print(f"Ctrl+C to stop")
        print("-" * 60)

        while True:
            with self.db_lock:
                # Fetch more nodes than parallel workers to keep pipeline full
                batch_size = max(self.parallel * 3, 20)
                if mix_strategies:
                    unexplored = self.engine.get_unexplored_mixed(limit=batch_size)
                else:
                    unexplored = self.engine.get_unexplored(
                        limit=batch_size,
                        strategy=strategy
                    )

            if not unexplored:
                print("\nNo more unexplored nodes - all paths exhausted or foundational")
                break

            # Handle root node specially for diverse initial branches
            root_nodes = [n for n in unexplored if n.depth == 0]
            regular_nodes = [n for n in unexplored if n.depth > 0]

            # Expand root nodes with diversity
            for node in root_nodes:
                print(f"Expanding ROOT: {self._trunc(node.claim)}")
                with self.db_lock:
                    created = self._expand_root_diverse(node)
                self.nodes_created += created
                self.nodes_by_strategy["root_diverse"] = self.nodes_by_strategy.get("root_diverse", 0) + created

            if self.parallel > 1 and regular_nodes:
                # Apply "why continue?" gate to filter nodes before parallel processing
                nodes_to_process = []
                for node in regular_nodes:
                    should_continue, reason = self._why_continue_node(node)
                    if should_continue:
                        nodes_to_process.append(node)
                    else:
                        print(f"  [GATE SKIP] {self._trunc(node.claim[:60])} - {reason}")
                        self.gate_skipped += 1
                        with self.db_lock:
                            self.engine.update_status(node.id, NodeStatus.PRUNED)

                # Parallel: fetch from API concurrently, write to DB sequentially
                if nodes_to_process:
                    with ThreadPoolExecutor(max_workers=self.parallel) as executor:
                        futures = {executor.submit(self._fetch_branches, node): node for node in nodes_to_process}

                        for future in as_completed(futures):
                            node, branches, root_claim, causal_chain = future.result()
                            print(f"Expanded: {self._trunc(node.claim)}")

                            with self.db_lock:
                                created = self._write_branches(node, branches)
                            self.nodes_created += created

                            if self.nodes_created > 0 and self.nodes_created % self.log_interval == 0:
                                self._log_progress()

                            # Check interval gate
                            if not self._apply_gate_interval():
                                return  # User chose to stop
                            # Check human checkpoint
                            if not self._apply_checkpoint():
                                return  # User chose to stop
            elif regular_nodes:
                # Sequential: simpler path with gate
                for node in regular_nodes:
                    should_continue, reason = self._why_continue_node(node)
                    if not should_continue:
                        print(f"  [GATE SKIP] {self._trunc(node.claim[:60])} - {reason}")
                        self.gate_skipped += 1
                        with self.db_lock:
                            self.engine.update_status(node.id, NodeStatus.PRUNED)
                        continue

                    print(f"Expanding: {self._trunc(node.claim)}")
                    node, branches, root_claim, causal_chain = self._fetch_branches(node)
                    with self.db_lock:
                        created = self._write_branches(node, branches)
                    self.nodes_created += created

                    if self.nodes_created > 0 and self.nodes_created % self.log_interval == 0:
                        self._log_progress()

                    # Check interval gate
                    if not self._apply_gate_interval():
                        return  # User chose to stop
                    # Check human checkpoint
                    if not self._apply_checkpoint():
                        return  # User chose to stop

        self._print_summary()

    def run_rotating(self, minutes_per_strategy: int = 10):
        """
        Run through ALL strategies, spending equal time on each.
        Tracks which strategy discovered which nodes for later analysis.

        Args:
            minutes_per_strategy: Minutes to spend on each strategy (default: 10)
        """
        self.start_time = datetime.now()
        seconds_per_strategy = minutes_per_strategy * 60

        print(f"Starting ARAW rotating strategy expansion")
        print(f"Model: {self.model}")
        print(f"Minutes per strategy: {minutes_per_strategy}")
        print(f"Total strategies: {len(self.ALL_STRATEGIES)}")
        print(f"Estimated total time: {minutes_per_strategy * len(self.ALL_STRATEGIES)} minutes")
        print(f"Root claim: {self._get_root_claim()}")
        print(f"Rate limit: {self.rate_limit} req/sec | Parallel: {self.parallel}")
        print(f"  (With ~5s API latency, max throughput = {self.parallel/5:.1f} req/sec)")
        print(f"Ctrl+C to stop")
        print("=" * 60)

        for strategy in self.ALL_STRATEGIES:
            self.current_strategy = strategy
            self.nodes_by_strategy[strategy] = 0
            strategy_start = datetime.now()
            strategy_end = strategy_start + timedelta(seconds=seconds_per_strategy)

            print(f"\n>>> STRATEGY: {strategy.upper()} (for {minutes_per_strategy} minutes)")
            print(f"    Started at: {strategy_start.strftime('%H:%M:%S')}")
            print("-" * 60)

            nodes_before = self.nodes_created

            while datetime.now() < strategy_end:
                with self.db_lock:
                    batch_size = max(self.parallel * 3, 20)
                    if strategy == "mixed":
                        unexplored = self.engine.get_unexplored_mixed(limit=batch_size)
                    else:
                        unexplored = self.engine.get_unexplored(
                            limit=batch_size,
                            strategy=strategy
                        )

                if not unexplored:
                    print(f"\n    No more unexplored nodes for {strategy}")
                    break

                # Handle root nodes specially
                root_nodes = [n for n in unexplored if n.depth == 0]
                regular_nodes = [n for n in unexplored if n.depth > 0]

                for node in root_nodes:
                    if datetime.now() >= strategy_end:
                        break
                    print(f"  [ROOT] {self._trunc(node.claim)}")
                    with self.db_lock:
                        created = self._expand_root_diverse(node)
                    self.nodes_created += created
                    self.nodes_by_strategy[strategy] += created

                if self.parallel > 1 and regular_nodes:
                    with ThreadPoolExecutor(max_workers=self.parallel) as executor:
                        futures = {executor.submit(self._fetch_branches, node): node for node in regular_nodes}
                        for future in as_completed(futures):
                            if datetime.now() >= strategy_end:
                                break
                            node, branches, root_claim, causal_chain = future.result()
                            print(f"  [{strategy[:3]}] {self._trunc(node.claim)}")
                            with self.db_lock:
                                created = self._write_branches(node, branches)
                            self.nodes_created += created
                            self.nodes_by_strategy[strategy] += created
                elif regular_nodes:
                    for node in regular_nodes:
                        if datetime.now() >= strategy_end:
                            break
                        print(f"  [{strategy[:3]}] {self._trunc(node.claim)}")
                        node, branches, root_claim, causal_chain = self._fetch_branches(node)
                        with self.db_lock:
                            created = self._write_branches(node, branches)
                        self.nodes_created += created
                        self.nodes_by_strategy[strategy] += created

            nodes_this_strategy = self.nodes_created - nodes_before
            elapsed = (datetime.now() - strategy_start).total_seconds()
            rate = nodes_this_strategy / elapsed if elapsed > 0 else 0

            print(f"\n    Strategy {strategy} complete:")
            print(f"    - Nodes created: {nodes_this_strategy}")
            print(f"    - Rate: {rate:.2f} nodes/sec")
            print(f"    - Time: {elapsed/60:.1f} minutes")

        self._print_rotating_summary()

    def _print_rotating_summary(self):
        """Print summary with per-strategy breakdown"""
        elapsed = (datetime.now() - self.start_time).total_seconds()
        with self.db_lock:
            stats = self.engine.get_stats()
            root_claim = self._get_root_claim()

        print("\n" + "=" * 60)
        print("ROTATING STRATEGY EXPANSION COMPLETE")
        print("=" * 60)
        print(f"Root claim: {root_claim}")
        print(f"Total duration: {elapsed/60:.1f} minutes")
        print(f"Model: {self.model}")
        print(f"Total nodes created: {self.nodes_created}")
        print(f"Total API requests: {self.requests_made}")

        print(f"\n>>> STRATEGY COMPARISON:")
        print("-" * 60)
        print(f"{'Strategy':<20} {'Nodes':>10} {'% of Total':>12}")
        print("-" * 60)

        total = sum(self.nodes_by_strategy.values()) or 1
        for strategy, count in sorted(self.nodes_by_strategy.items(), key=lambda x: -x[1]):
            pct = 100 * count / total
            bar = "█" * int(pct / 2)
            print(f"{strategy:<20} {count:>10} {pct:>11.1f}% {bar}")

        print("-" * 60)
        print(f"\nTo analyze which strategies found the best nodes:")
        print(f"  python -c \"from analyze_strategies import analyze; analyze('{self.engine.db_path}')\"")

        print(f"\nBy status:")
        for status, count in stats['by_status'].items():
            print(f"  {status}: {count}")

    def _log_progress(self):
        """Log current progress"""
        elapsed = (datetime.now() - self.start_time).total_seconds()
        rate = self.nodes_created / elapsed if elapsed > 0 else 0
        with self.db_lock:
            stats = self.engine.get_stats()
        print(f"\n[{elapsed/60:.1f}m] Nodes: {stats['total_nodes']} | "
              f"Rate: {rate:.2f}/s | "
              f"Unexplored: {stats['by_status'].get('unexplored', 0)} | "
              f"Max depth: {stats['max_depth']}\n")

        self._print_summary()

    def _print_summary(self):
        """Print expansion summary"""
        elapsed = (datetime.now() - self.start_time).total_seconds()
        with self.db_lock:
            stats = self.engine.get_stats()
            root_claim = self._get_root_claim()

        print("\n" + "=" * 60)
        print("EXPANSION COMPLETE")
        print("=" * 60)
        print(f"Root claim: {root_claim}")
        print(f"Duration: {elapsed/60:.1f} minutes")
        print(f"Model: {self.model}")
        print(f"Rate limit: {self.rate_limit}/sec")
        print(f"API requests made: {self.requests_made}")
        print(f"Total nodes: {stats['total_nodes']}")
        print(f"Nodes created this run: {self.nodes_created}")
        if self.gate_skipped > 0:
            print(f"Nodes skipped by 'why continue?' gate: {self.gate_skipped}")
        if self.llm_rejected > 0:
            print(f"Claims rejected by LLM filter: {self.llm_rejected}")
        if self.relevancy_rejected > 0:
            print(f"Claims rejected by relevancy filter: {self.relevancy_rejected}")
        if elapsed > 0:
            print(f"Rate: {self.nodes_created/elapsed:.3f} nodes/second")
        print(f"Max depth reached: {stats['max_depth']}")
        print(f"\nBy status:")
        for status, count in stats['by_status'].items():
            print(f"  {status}: {count}")
        print(f"\nBy depth (showing first 20):")
        for depth, count in list(sorted(stats['by_depth'].items()))[:20]:
            bar = "█" * min(50, count)
            print(f"  {depth:2d}: {count:5d} {bar}")
        if len(stats['by_depth']) > 20:
            print(f"  ... and {len(stats['by_depth']) - 20} more depth levels")


def main():
    parser = argparse.ArgumentParser(description="ARAW LLM-Powered Causal Expander")
    parser.add_argument("--db", type=str, default="araw_llm.db", help="Database file")
    parser.add_argument("--continue", dest="continue_existing", action="store_true", help="Continue existing search")
    parser.add_argument("--seed", type=str, default=None, help="Initial claim to seed the search")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL, help=f"Model to use (default: {DEFAULT_MODEL})")
    parser.add_argument("--parallel", type=int, default=20, help="Number of parallel API calls (default: 20). With ~5s API latency, need parallel >= rate_limit * 5 to achieve target rate.")
    parser.add_argument("--rate-limit", type=float, default=50.0, help="Max requests per second (default: 50.0)")
    parser.add_argument("--key-file", type=str, default=None, help="Path to API key file")

    # Queue strategy options
    parser.add_argument(
        "--strategy", type=str, default="balanced",
        choices=["leverage_first", "depth_first", "breadth_first", "frontier", "balanced", "random"],
        help="Queue strategy for selecting next nodes (default: balanced)"
    )
    parser.add_argument(
        "--mix-strategies", action="store_true",
        help="Use mixed strategies for diversity (overrides --strategy)"
    )
    parser.add_argument(
        "--rotate", action="store_true",
        help="Rotate through ALL strategies, spending equal time on each"
    )
    parser.add_argument(
        "--minutes-per-strategy", type=int, default=10,
        help="Minutes to spend on each strategy when using --rotate (default: 10)"
    )
    parser.add_argument(
        "--no-similarity", action="store_true",
        help="Disable similarity checking (faster, but may create more near-duplicates)"
    )
    parser.add_argument(
        "--log-width", type=int, default=120,
        help="Width for claim truncation in logs (0 = no truncation, default: 120)"
    )
    parser.add_argument(
        "--gate-interval", type=int, default=0,
        help="Apply 'why continue?' gate every N nodes (0 = disabled, prompts for continuation)"
    )
    parser.add_argument(
        "--llm-filter", action="store_true",
        help="Use LLM to evaluate claim quality (smarter but slower, replaces most hardcoded filters)"
    )
    parser.add_argument(
        "--relevancy-filter", action="store_true",
        help="Use LLM to evaluate relevancy to root claim (prevents drift, requires --llm-filter)"
    )
    parser.add_argument(
        "--domain-weights", type=str, default=None,
        help="Domain weights as JSON, e.g. '{\"ENVIRONMENTAL\": 3, \"GEOPOLITICAL\": 2}'. Unspecified domains default to 1."
    )
    parser.add_argument(
        "--recommend-domains", action="store_true",
        help="Use LLM to recommend domain weights based on root claim and current distribution"
    )
    parser.add_argument(
        "--balance-domains", action="store_true",
        help="Automatically boost underexplored domains to achieve balanced coverage"
    )
    parser.add_argument(
        "--show-domains", action="store_true",
        help="Show current domain distribution and recommended weights, then exit"
    )
    parser.add_argument(
        "--summary", action="store_true",
        help="Show summary of current exploration (key findings, frontiers, actions) then exit"
    )
    parser.add_argument(
        "--checkpoint", type=int, default=0,
        help="Pause every N nodes for human review (0 = disabled)"
    )
    parser.add_argument(
        "--extract-actions", type=str, metavar="FILE",
        help="Export actionable items (HIGH impact + LOW effort) to JSON file, then exit"
    )

    args = parser.parse_args()

    # Read API key
    api_key, source = read_api_key(args.key_file)
    if not api_key:
        print("Error: No OpenAI API key found")
        print("Set OPENAI_API_KEY env var or create ~/.config/gosm/openai_api_key")
        return
    print(f"API key from: {source}")

    # Create or load engine
    engine = ARAWEngine(args.db)

    # Check if we're continuing or starting fresh
    root = engine.get_root()

    # Handle --show-domains first (doesn't require --continue)
    if args.show_domains:
        root_claim = engine.get_root_claim()
        stats = engine.get_stats()
        if stats['total_nodes'] > 1:
            current_distribution = get_domain_distribution(engine.conn)
            print("\nCURRENT DOMAIN DISTRIBUTION:")
            for domain, pct in sorted(current_distribution.items(), key=lambda x: -x[1]):
                bar = "█" * int(pct * 50)
                print(f"  {domain:<18} {pct*100:5.1f}% {bar}")
        if root_claim:
            print(f"\nAnalyzing recommended weights for: \"{root_claim}\"")
            recommended = recommend_domain_weights(api_key, root_claim, current_distribution if stats['total_nodes'] > 1 else None)
            print("\nRECOMMENDED DOMAIN WEIGHTS (0=irrelevant, 3=critical):")
            for domain, weight in sorted(recommended.items(), key=lambda x: -x[1]):
                stars = "★" * weight + "☆" * (3 - weight)
                print(f"  {domain:<18} {weight} {stars}")
            focus = compute_focus_domains(recommended, current_distribution if stats['total_nodes'] > 1 else None)
            print(f"\nSUGGESTED FOCUS DOMAINS: {', '.join(focus)}")
        engine.close()
        return

    # Handle --summary
    if args.summary:
        root_claim = engine.get_root_claim()
        stats = engine.get_stats()

        print(f"\n{'='*70}")
        print(f"ARAW EXPLORATION SUMMARY: {args.db}")
        print(f"{'='*70}")
        print(f"Root: {root_claim[:80]}...")
        print(f"Total nodes: {stats['total_nodes']} | Max depth: {stats['max_depth']}")
        print(f"Status: {stats['by_status']}")

        # High-leverage unexplored (frontier)
        cursor = engine.conn.execute("""
            SELECT claim, leverage_score, depth, content
            FROM nodes WHERE status = 'unexplored'
            ORDER BY leverage_score DESC LIMIT 10
        """)
        print(f"\n🔭 FRONTIER (top 10 unexplored high-leverage):")
        for row in cursor:
            content = json.loads(row['content']) if row['content'] else {}
            effort = content.get('effort_to_address', '?')
            impact = content.get('potential_impact', '?')
            print(f"  [{row['leverage_score'] or 0.5:.2f}] E:{effort[0]} I:{impact[0]} | {row['claim'][:55]}...")

        # Crux nodes
        cursor = engine.conn.execute("""
            SELECT claim, leverage_score, content
            FROM nodes WHERE content LIKE '%"is_crux": true%'
            ORDER BY leverage_score DESC LIMIT 5
        """)
        crux_nodes = list(cursor)
        if crux_nodes:
            print(f"\n⚡ CRUX NODES (could flip conclusion):")
            for row in crux_nodes:
                print(f"  [{row['leverage_score'] or 0.5:.2f}] {row['claim'][:60]}...")

        # Actionable items (HIGH impact + LOW effort)
        cursor = engine.conn.execute("""
            SELECT claim, leverage_score, content
            FROM nodes WHERE content LIKE '%"potential_impact": "HIGH"%'
            AND content LIKE '%"effort_to_address": "LOW"%'
            ORDER BY leverage_score DESC LIMIT 10
        """)
        actions = list(cursor)
        if actions:
            print(f"\n🔥 DO FIRST (HIGH impact + LOW effort):")
            for row in actions:
                print(f"  [{row['leverage_score'] or 0.5:.2f}] {row['claim'][:60]}...")

        # Domain distribution
        if stats['total_nodes'] > 1:
            current_distribution = get_domain_distribution(engine.conn)
            print(f"\n📊 DOMAIN DISTRIBUTION:")
            for domain, pct in sorted(current_distribution.items(), key=lambda x: -x[1])[:8]:
                bar = "█" * int(pct * 40)
                print(f"  {domain:<15} {pct*100:5.1f}% {bar}")

        engine.close()
        return

    # Handle --extract-actions
    if args.extract_actions:
        cursor = engine.conn.execute("""
            SELECT claim, leverage_score, content, depth
            FROM nodes
            WHERE content LIKE '%"potential_impact": "HIGH"%'
            ORDER BY leverage_score DESC
        """)

        actions = []
        for row in cursor:
            content = json.loads(row['content']) if row['content'] else {}
            effort = content.get('effort_to_address', 'MEDIUM')
            impact = content.get('potential_impact', 'MEDIUM')
            is_crux = content.get('is_crux', False)

            if effort == 'LOW' and impact == 'HIGH':
                priority = 'DO_FIRST'
            elif impact == 'HIGH' and is_crux:
                priority = 'DO_SECOND'
            elif impact == 'HIGH':
                priority = 'CONSIDER'
            else:
                continue

            actions.append({
                'priority': priority,
                'claim': row['claim'],
                'leverage': row['leverage_score'] or 0.5,
                'effort': effort,
                'impact': impact,
                'is_crux': is_crux,
                'depth': row['depth']
            })

        # Sort by priority
        priority_order = {'DO_FIRST': 0, 'DO_SECOND': 1, 'CONSIDER': 2}
        actions.sort(key=lambda x: (priority_order[x['priority']], -x['leverage']))

        with open(args.extract_actions, 'w') as f:
            json.dump(actions, f, indent=2)

        print(f"Extracted {len(actions)} actions to {args.extract_actions}")
        print(f"  DO_FIRST: {sum(1 for a in actions if a['priority'] == 'DO_FIRST')}")
        print(f"  DO_SECOND: {sum(1 for a in actions if a['priority'] == 'DO_SECOND')}")
        print(f"  CONSIDER: {sum(1 for a in actions if a['priority'] == 'CONSIDER')}")
        engine.close()
        return

    if root and not args.continue_existing:
        print(f"Database {args.db} already has a search. Use --continue to expand it.")
        stats = engine.get_stats()
        print(f"Current stats: {stats['total_nodes']} nodes, max depth {stats['max_depth']}")
        engine.close()
        return

    if not root:
        if not args.seed:
            print("Error: --seed required for new search")
            print("Example: python auto_expand_llm.py --seed 'I need to change careers'")
            engine.close()
            return

        print(f"Creating new search with seed: {args.seed}")
        root_id = engine.create_search(
            args.seed,
            metadata={"created": datetime.now().isoformat(), "type": "llm_expand", "model": args.model}
        )
        engine.update_status(root_id, NodeStatus.UNEXPLORED)

    # Get root claim for domain analysis
    root_claim = engine.get_root_claim()

    # Handle domain weights
    domain_weights = {d: 1 for d in ALL_DOMAINS}  # Default equal weights
    current_distribution = None

    if args.recommend_domains or args.balance_domains:
        # Get current distribution if we have nodes
        stats = engine.get_stats()
        if stats['total_nodes'] > 1:
            current_distribution = get_domain_distribution(engine.conn)
            print("\nCURRENT DOMAIN DISTRIBUTION:")
            for domain, pct in sorted(current_distribution.items(), key=lambda x: -x[1]):
                bar = "█" * int(pct * 50)
                print(f"  {domain:<18} {pct*100:5.1f}% {bar}")

    if args.domain_weights:
        try:
            user_weights = json.loads(args.domain_weights)
            domain_weights.update(user_weights)
            print(f"Using custom domain weights: {user_weights}")
        except json.JSONDecodeError:
            print(f"Warning: Could not parse --domain-weights, using defaults")

    if args.recommend_domains:
        print("Getting LLM-recommended domain weights...")
        domain_weights = recommend_domain_weights(api_key, root_claim, current_distribution)
        focus = compute_focus_domains(domain_weights, current_distribution)
        print(f"Focus domains: {', '.join(focus)}")

    if args.balance_domains and current_distribution:
        # Boost underexplored domains
        for domain in ALL_DOMAINS:
            coverage = current_distribution.get(domain, 0)
            if coverage < 0.03:  # Less than 3%
                domain_weights[domain] = domain_weights.get(domain, 1) + 2
            elif coverage < 0.05:  # Less than 5%
                domain_weights[domain] = domain_weights.get(domain, 1) + 1
        focus = compute_focus_domains(domain_weights, current_distribution)
        print(f"Balancing domains, focusing on: {', '.join(focus)}")

    # Compute focus domains from weights
    focus_domains = compute_focus_domains(domain_weights, current_distribution)

    # Check for incompatible options
    if args.relevancy_filter and not args.llm_filter:
        print("Warning: --relevancy-filter requires --llm-filter. Enabling --llm-filter automatically.")
        args.llm_filter = True

    # Run expansion
    expander = ARAWLLMExpander(
        engine, api_key, args.model,
        parallel=args.parallel,
        rate_limit=args.rate_limit,
        check_similarity=not args.no_similarity,
        log_width=args.log_width,
        focus_domains=focus_domains,
        gate_interval=args.gate_interval,
        llm_filter=args.llm_filter,
        relevancy_filter=args.relevancy_filter,
        checkpoint=args.checkpoint
    )

    try:
        if args.rotate:
            expander.run_rotating(minutes_per_strategy=args.minutes_per_strategy)
        else:
            expander.run_forever(strategy=args.strategy, mix_strategies=args.mix_strategies)
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        if args.rotate:
            expander._print_rotating_summary()
        else:
            expander._print_summary()

    # Export tree structure
    export_file = args.db.replace(".db", "_export.json")
    print(f"\nExporting tree to {export_file}...")
    engine.export_json(export_file)

    engine.close()


if __name__ == "__main__":
    main()

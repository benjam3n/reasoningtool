"""
ARAW Grounding Engine v2

Connects abstract claims to real-world evidence with EPISTEMIC CARE.

Refinements implemented:
1. Smarter Prioritization - upstream influence, convergence, decision-relevance
2. Recursive Assumption Integration - auto-create ARAW branches from assumptions
3. Evidence Quality Tiers - track epistemic weight
4. Contradiction Detection - flag disagreeing sources
5. Falsifiability Check - what would we see if FALSE?
6. Active vs Passive Grounding - verification levels
7. Stated vs Actual Reasons - explicit tracking

Usage:
    python grounding.py --db worlddirection.db --prioritize      # Show best nodes to ground
    python grounding.py --db worlddirection.db --ground-top 10   # Ground top 10 priority nodes
    python grounding.py --db worlddirection.db --node 123        # Ground specific node
    python grounding.py --db worlddirection.db --integrate       # Create ARAW nodes from assumptions
"""

import argparse
import json
import os
import sqlite3
import subprocess
import tempfile
from collections import defaultdict
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple
from datetime import datetime

from araw_engine import ARAWEngine, BranchType, NodeStatus


DEFAULT_MODEL = "gpt-5-nano"
DEFAULT_KEY_FILE = str(Path.home() / ".config" / "gosm" / "openai_api_key")


def read_api_key(path: Optional[str] = None) -> Optional[str]:
    env = os.environ.get("OPENAI_API_KEY", "").strip()
    if env:
        return env
    for p in ([path] if path else []) + [DEFAULT_KEY_FILE]:
        if p and Path(p).expanduser().is_file():
            return Path(p).expanduser().read_text().splitlines()[0].strip()
    return None


# Evidence quality tiers
EVIDENCE_TIERS = {
    "direct_observation": {"weight": 1.0, "description": "Can be directly verified/observed"},
    "published_raw_data": {"weight": 0.8, "description": "Raw data exists and is downloadable"},
    "published_analysis": {"weight": 0.6, "description": "Someone interpreted data and published conclusions"},
    "expert_claim": {"weight": 0.4, "description": "Expert asserts something without showing data"},
    "model_output": {"weight": 0.2, "description": "Derived from models with their own assumptions"},
    "unknown": {"weight": 0.1, "description": "Cannot determine evidence type"}
}


GROUNDING_SYSTEM_PROMPT = """You connect abstract claims to empirical observations with EPISTEMIC CARE.

CRITICAL RULES - NEVER VIOLATE:
1. DO NOT GUESS what data shows. Only state what data EXISTS and what sources PUBLISH.
2. DO NOT claim methodology is good/bad. Only state what sources CLAIM about their method.
3. DO NOT interpret. State what is published, not what it "means."
4. EVERY source introduces NEW ASSUMPTIONS requiring their own exploration.
5. DISTINGUISH stated reasons from actual reasons.
6. CLAIMS ABOUT UNKNOWABILITY ARE THEMSELVES CLAIMS. If you say "we can't know X" or "X is unfalsifiable",
   that is itself an assumption that could be wrong. Maybe we CAN know it - we just haven't found how yet.
   Frame these as explorable assumptions, not definitive limits.

For the given claim, provide:

1. OBSERVABLE_INDICATORS: What specific things could we look for?

2. DATA_SOURCES: For each source, provide:
   - source_name: Exact name
   - what_they_publish: What data they make available
   - stated_methodology: What THEY CLAIM about how they collect it (not whether it's good)
   - stated_purpose: Why THEY SAY they collect it (not whether that's the real reason)
   - published_figures: Specific numbers if known (not interpretation)
   - evidence_tier: One of: direct_observation, published_raw_data, published_analysis, expert_claim, model_output
   - accessibility: Can this data actually be accessed? (open, paywalled, requires_expertise, unavailable)

3. FALSIFIABILITY: What would we EXPECT TO OBSERVE if this claim were FALSE?
   - If you can't immediately think of distinguishing observations, that ITSELF is an assumption to explore
   - Maybe there IS a way to falsify it that we haven't thought of yet
   - List specific observations that would contradict the claim

4. NEW_ASSUMPTIONS: Each assumption needed to trust any source. Format as claims that could be ARAW-explored:
   - "[Source]'s stated methodology actually reflects their practice"
   - "[Source]'s sampling captures the real phenomenon"
   - "Survey respondents to [Source] answer honestly"
   - "[Metric] actually measures [concept]"

5. EPISTEMIC_LIMIT_ASSUMPTIONS: Any claims you make about what we CAN'T know or verify. These are explorable:
   - "There is no way to verify [X]" → maybe there IS a way we haven't found
   - "We cannot access [data]" → maybe we CAN through a method not yet considered
   - "This requires assumptions we can't test" → maybe we CAN test them
   - "[Claim] is unfalsifiable" → maybe there IS a falsification method
   Mark each with how confident you are this is truly a limit vs just unexplored territory.

6. CONTRADICTIONS: Do sources disagree? If so, note:
   - Which sources say what
   - This disagreement itself is important information

7. TESTABILITY: One of:
   - directly_observable: Can verify yourself
   - verifiable_from_published: Can check published sources
   - requires_interpretation: Data exists but needs analysis
   - requires_assumptions: Must assume methodology validity
   - appears_unfalsifiable: No obvious way to distinguish true from false (but this itself is explorable)

Return well-structured JSON."""


def llm_call(api_key: str, system: str, user: str, model: str = DEFAULT_MODEL) -> Optional[dict]:
    """Make LLM API call"""
    payload = {
        "model": model,
        "max_output_tokens": 3000,
        "reasoning": {"effort": "low"},
        "text": {"format": {"type": "json_object"}},
        "input": [
            {"role": "system", "content": [{"type": "input_text", "text": system}]},
            {"role": "user", "content": [{"type": "input_text", "text": user}]},
        ],
    }

    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".json") as f:
        json.dump(payload, f)
        payload_path = f.name

    try:
        cmd = [
            "curl", "-sS", "https://api.openai.com/v1/responses",
            "-H", f"Authorization: Bearer {api_key}",
            "-H", "Content-Type: application/json",
            "-d", f"@{payload_path}",
            "--max-time", "90"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        resp = json.loads(result.stdout)

        text = None
        if "output" in resp:
            for item in resp.get("output", []):
                for c in item.get("content", []):
                    if isinstance(c, dict) and c.get("type") in ("output_text", "text"):
                        text = c.get("text", "").strip()
                        if text:
                            break
                if text:
                    break

        if text:
            return json.loads(text)
        return None
    except Exception as e:
        print(f"LLM error: {e}")
        return None
    finally:
        Path(payload_path).unlink(missing_ok=True)


def ground_claim(api_key: str, claim: str, context: Optional[str] = None, model: str = DEFAULT_MODEL) -> Optional[dict]:
    """Generate comprehensive grounding for a claim"""

    user_prompt = f"""CLAIM TO GROUND (survived extensive ARAW exploration, likely correct):
"{claim}"
"""
    if context:
        user_prompt += f"\nCONTEXT (reasoning chain): {context}\n"

    user_prompt += """
Return JSON with:
{
  "observable_indicators": [
    {"indicator": "what to look for", "how_to_find": "where/how to find it"}
  ],
  "data_sources": [
    {
      "source_name": "Exact name",
      "what_they_publish": "What data",
      "stated_methodology": "What THEY CLAIM about their method",
      "stated_purpose": "Why THEY SAY they do this",
      "published_figures": "Specific numbers if known",
      "evidence_tier": "direct_observation|published_raw_data|published_analysis|expert_claim|model_output",
      "accessibility": "open|paywalled|requires_expertise|unavailable"
    }
  ],
  "falsifiability": {
    "if_false_we_would_see": ["observation that would contradict claim"],
    "distinguishable": true/false,
    "falsifiability_notes": "Why this is or isn't falsifiable"
  },
  "new_assumptions": [
    {
      "assumption": "Statement that could be ARAW-explored",
      "source_dependency": "Which source this assumption relates to",
      "criticality": "high|medium|low - how much does trusting the grounding depend on this?"
    }
  ],
  "epistemic_limit_assumptions": [
    {
      "limit_claim": "What you're claiming we can't know or verify",
      "why_it_seems_limited": "Why this appears to be an epistemic limit",
      "possible_ways_around": "How might we actually be able to know this? What unexplored methods exist?",
      "confidence_truly_limited": "high|medium|low - how sure are you this is a real limit vs unexplored?"
    }
  ],
  "contradictions": [
    {
      "topic": "What they disagree about",
      "source_a": "Source name",
      "source_a_says": "What they claim",
      "source_b": "Source name",
      "source_b_says": "What they claim"
    }
  ],
  "testability": "directly_observable|verifiable_from_published|requires_interpretation|requires_assumptions|appears_unfalsifiable",
  "grounding_confidence": "high|medium|low - how well can this claim be grounded?",
  "search_queries": ["specific searches to find evidence"]
}"""

    return llm_call(api_key, GROUNDING_SYSTEM_PROMPT, user_prompt, model)


class GroundingEngine:
    """Grounds ARAW claims with epistemic care and recursive integration"""

    def __init__(self, db_path: str, api_key: str, model: str = DEFAULT_MODEL):
        self.engine = ARAWEngine(db_path)
        self.api_key = api_key
        self.model = model
        self.conn = self.engine.conn

        self._init_tables()

    def _init_tables(self):
        """Create tables for grounding data (with migration support)"""
        # Create table if not exists
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS groundings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                node_id TEXT NOT NULL,
                grounding_data TEXT NOT NULL,
                testability TEXT,
                grounding_confidence TEXT,
                evidence_tier_best TEXT,
                has_contradictions INTEGER DEFAULT 0,
                is_falsifiable INTEGER DEFAULT 1,
                assumptions_integrated INTEGER DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(node_id)
            )
        """)

        # Migration: add columns if missing (for existing databases)
        cursor = self.conn.cursor()
        cursor.execute("PRAGMA table_info(groundings)")
        existing_cols = {row[1] for row in cursor.fetchall()}

        new_cols = [
            ("testability", "TEXT"),
            ("grounding_confidence", "TEXT"),
            ("evidence_tier_best", "TEXT"),
            ("has_contradictions", "INTEGER DEFAULT 0"),
            ("is_falsifiable", "INTEGER DEFAULT 1"),
            ("assumptions_integrated", "INTEGER DEFAULT 0"),
        ]
        for col_name, col_type in new_cols:
            if col_name not in existing_cols:
                try:
                    self.conn.execute(f"ALTER TABLE groundings ADD COLUMN {col_name} {col_type}")
                except Exception:
                    pass  # Column might already exist

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS grounding_assumptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                grounding_id INTEGER NOT NULL,
                assumption_text TEXT NOT NULL,
                assumption_type TEXT DEFAULT 'source',
                source_dependency TEXT,
                criticality TEXT,
                possible_ways_around TEXT,
                confidence_truly_limited TEXT,
                created_node_id TEXT,
                integrated INTEGER DEFAULT 0,
                FOREIGN KEY (grounding_id) REFERENCES groundings(id)
            )
        """)

        # Migration for grounding_assumptions table
        cursor.execute("PRAGMA table_info(grounding_assumptions)")
        assumption_cols = {row[1] for row in cursor.fetchall()}
        assumption_new_cols = [
            ("assumption_type", "TEXT DEFAULT 'source'"),
            ("possible_ways_around", "TEXT"),
            ("confidence_truly_limited", "TEXT"),
        ]
        for col_name, col_type in assumption_new_cols:
            if col_name not in assumption_cols:
                try:
                    self.conn.execute(f"ALTER TABLE grounding_assumptions ADD COLUMN {col_name} {col_type}")
                except Exception:
                    pass

        self.conn.commit()

    # ==================== PRIORITIZATION (Refinement #1) ====================

    def get_upstream_influence(self, node_id: str) -> int:
        """Count how many nodes are downstream of this node"""
        cursor = self.conn.cursor()
        cursor.execute("""
            WITH RECURSIVE descendants AS (
                SELECT id FROM nodes WHERE parent_id = ?
                UNION ALL
                SELECT n.id FROM nodes n
                JOIN descendants d ON n.parent_id = d.id
            )
            SELECT COUNT(*) FROM descendants
        """, (node_id,))
        return cursor.fetchone()[0]

    def get_convergence_score(self, node_id: str) -> float:
        """Check if similar claims exist elsewhere (convergence indicator)"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT claim FROM nodes WHERE id = ?", (node_id,))
        row = cursor.fetchone()
        if not row:
            return 0.0

        words = set(row['claim'].lower().split())
        if len(words) < 4:
            return 0.0

        # Check similarity with other nodes
        cursor.execute("SELECT id, claim FROM nodes WHERE id != ? LIMIT 1000", (node_id,))
        similar_count = 0
        for other in cursor:
            other_words = set(other['claim'].lower().split())
            if len(other_words) < 4:
                continue
            jaccard = len(words & other_words) / len(words | other_words)
            if jaccard > 0.5:
                similar_count += 1

        return min(1.0, similar_count / 10.0)  # Normalize

    def calculate_grounding_priority(self, node_id: str) -> Dict[str, Any]:
        """Calculate comprehensive priority score for grounding a node"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT id, claim, leverage_score, depth, content
            FROM nodes WHERE id = ?
        """, (node_id,))
        row = cursor.fetchone()
        if not row:
            return {"score": 0, "factors": {}}

        content = json.loads(row['content']) if row['content'] else {}
        is_crux = content.get('is_crux', False)
        leverage = row['leverage_score'] or 0.5

        # Factor 1: Crux status
        crux_score = 1.0 if is_crux else 0.3

        # Factor 2: Upstream influence
        influence = self.get_upstream_influence(node_id)
        influence_score = min(1.0, influence / 100.0)

        # Factor 3: Convergence (appears in multiple branches)
        convergence_score = self.get_convergence_score(node_id)

        # Factor 4: Depth (shallower = more foundational)
        depth_score = 1.0 / (1 + row['depth'] * 0.1)

        # Factor 5: Not already grounded
        cursor.execute("SELECT 1 FROM groundings WHERE node_id = ?", (node_id,))
        already_grounded = cursor.fetchone() is not None
        novelty_score = 0.0 if already_grounded else 1.0

        # Weighted combination
        total_score = (
            crux_score * 0.3 +
            influence_score * 0.25 +
            convergence_score * 0.15 +
            depth_score * 0.1 +
            novelty_score * 0.2
        ) * leverage

        return {
            "node_id": node_id,
            "claim": row['claim'],
            "score": total_score,
            "factors": {
                "is_crux": is_crux,
                "leverage": leverage,
                "upstream_influence": influence,
                "convergence": convergence_score,
                "depth": row['depth'],
                "already_grounded": already_grounded
            }
        }

    def get_priority_nodes(self, limit: int = 20) -> List[Dict]:
        """Get nodes prioritized for grounding"""
        cursor = self.conn.cursor()

        # Get candidate nodes (crux or high leverage)
        cursor.execute("""
            SELECT id FROM nodes
            WHERE leverage_score >= 0.5 OR id IN (
                SELECT id FROM nodes WHERE leverage_score >= 0.8
            )
            ORDER BY leverage_score DESC
            LIMIT 500
        """)

        candidates = [row['id'] for row in cursor]

        # Score each
        scored = [self.calculate_grounding_priority(nid) for nid in candidates]
        scored = [s for s in scored if s['score'] > 0]
        scored.sort(key=lambda x: -x['score'])

        return scored[:limit]

    # ==================== CORE GROUNDING ====================

    def get_context(self, node_id: str, max_ancestors: int = 3) -> str:
        """Get context from ancestor claims"""
        cursor = self.conn.cursor()
        context_parts = []

        cursor.execute("SELECT parent_id FROM nodes WHERE id = ?", (node_id,))
        row = cursor.fetchone()
        current_id = row['parent_id'] if row else None

        depth = 0
        while current_id and depth < max_ancestors:
            cursor.execute("SELECT claim, parent_id FROM nodes WHERE id = ?", (current_id,))
            row = cursor.fetchone()
            if row:
                context_parts.append(row['claim'])
                current_id = row['parent_id']
                depth += 1
            else:
                break

        context_parts.reverse()
        return " → ".join(context_parts) if context_parts else ""

    def ground_node(self, node_id: str, verbose: bool = True) -> Optional[dict]:
        """Ground a node with full epistemic analysis"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT claim FROM nodes WHERE id = ?", (node_id,))
        row = cursor.fetchone()
        if not row:
            print(f"Node {node_id} not found")
            return None

        claim = row['claim']
        context = self.get_context(node_id)

        if verbose:
            print(f"Grounding: {claim[:80]}...")

        grounding = ground_claim(self.api_key, claim, context, self.model)

        if not grounding:
            print("  Grounding failed")
            return None

        # Extract summary fields
        testability = grounding.get('testability', 'unknown')
        confidence = grounding.get('grounding_confidence', 'unknown')

        # Best evidence tier
        best_tier = 'unknown'
        for src in grounding.get('data_sources', []):
            tier = src.get('evidence_tier', 'unknown')
            if tier in EVIDENCE_TIERS:
                if best_tier == 'unknown' or EVIDENCE_TIERS[tier]['weight'] > EVIDENCE_TIERS.get(best_tier, {}).get('weight', 0):
                    best_tier = tier

        has_contradictions = 1 if grounding.get('contradictions') else 0

        falsifiability = grounding.get('falsifiability', {})
        is_falsifiable = 1 if falsifiability.get('distinguishable', True) else 0

        # Store grounding
        cursor.execute("""
            INSERT OR REPLACE INTO groundings
            (node_id, grounding_data, testability, grounding_confidence,
             evidence_tier_best, has_contradictions, is_falsifiable, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (node_id, json.dumps(grounding), testability, confidence,
              best_tier, has_contradictions, is_falsifiable, datetime.now().isoformat()))

        grounding_id = cursor.lastrowid

        # Store source assumptions for later integration
        for assumption in grounding.get('new_assumptions', []):
            if isinstance(assumption, dict):
                cursor.execute("""
                    INSERT INTO grounding_assumptions
                    (grounding_id, assumption_text, assumption_type, source_dependency, criticality)
                    VALUES (?, ?, 'source', ?, ?)
                """, (grounding_id,
                      assumption.get('assumption', str(assumption)),
                      assumption.get('source_dependency'),
                      assumption.get('criticality', 'medium')))
            else:
                cursor.execute("""
                    INSERT INTO grounding_assumptions
                    (grounding_id, assumption_text, assumption_type, criticality)
                    VALUES (?, ?, 'source', 'medium')
                """, (grounding_id, str(assumption)))

        # Store epistemic limit assumptions - claims about what we "can't know"
        for limit in grounding.get('epistemic_limit_assumptions', []):
            if isinstance(limit, dict):
                # The limit claim itself becomes an explorable assumption
                limit_claim = limit.get('limit_claim', str(limit))
                cursor.execute("""
                    INSERT INTO grounding_assumptions
                    (grounding_id, assumption_text, assumption_type, possible_ways_around,
                     confidence_truly_limited, criticality)
                    VALUES (?, ?, 'epistemic_limit', ?, ?, ?)
                """, (grounding_id,
                      limit_claim,
                      limit.get('possible_ways_around'),
                      limit.get('confidence_truly_limited', 'medium'),
                      'high'))  # Epistemic limits are always high criticality - they bound what we can know
            else:
                cursor.execute("""
                    INSERT INTO grounding_assumptions
                    (grounding_id, assumption_text, assumption_type, criticality)
                    VALUES (?, ?, 'epistemic_limit', 'high')
                """, (grounding_id, str(limit)))

        self.conn.commit()
        return grounding

    # ==================== RECURSIVE INTEGRATION (Refinement #2) ====================

    def integrate_assumptions(self, grounding_id: Optional[int] = None,
                             criticality_filter: str = "high",
                             include_epistemic_limits: bool = True) -> List[str]:
        """Create ARAW nodes from grounding assumptions"""
        cursor = self.conn.cursor()

        query = """
            SELECT ga.id, ga.assumption_text, ga.assumption_type, ga.source_dependency,
                   ga.criticality, ga.possible_ways_around, ga.confidence_truly_limited,
                   g.node_id as parent_node_id
            FROM grounding_assumptions ga
            JOIN groundings g ON ga.grounding_id = g.id
            WHERE ga.integrated = 0
        """
        params = []

        if grounding_id:
            query += " AND ga.grounding_id = ?"
            params.append(grounding_id)

        if criticality_filter:
            if criticality_filter == "high":
                query += " AND ga.criticality = 'high'"
            elif criticality_filter == "high_medium":
                query += " AND ga.criticality IN ('high', 'medium')"

        cursor.execute(query, params)
        assumptions = cursor.fetchall()

        created_nodes = []
        for assumption in assumptions:
            assumption_type = assumption['assumption_type'] or 'source'
            claim = assumption['assumption_text']

            # Skip epistemic limits if not requested
            if assumption_type == 'epistemic_limit' and not include_epistemic_limits:
                continue

            # Check if similar claim already exists
            cursor.execute("""
                SELECT id FROM nodes WHERE claim = ? LIMIT 1
            """, (claim,))
            if cursor.fetchone():
                continue

            # For epistemic limits, frame as "we CAN know this" (challenging the limit)
            if assumption_type == 'epistemic_limit':
                # The assumption is "we can't know X" - create a node questioning that
                content = {
                    "generated_by": "grounding_integration",
                    "assumption_type": "epistemic_limit",
                    "original_limit_claim": claim,
                    "possible_ways_around": assumption['possible_ways_around'],
                    "confidence_truly_limited": assumption['confidence_truly_limited'],
                    "grounding_assumption": True,
                    "explore_note": "This claims we CANNOT know something. ARAW explores: what if we CAN?"
                }
                # Higher leverage for epistemic limits - they bound entire branches of knowledge
                leverage = 0.85
            else:
                content = {
                    "generated_by": "grounding_integration",
                    "assumption_type": "source",
                    "source_dependency": assumption['source_dependency'],
                    "criticality": assumption['criticality'],
                    "grounding_assumption": True
                }
                leverage = 0.7 if assumption['criticality'] == 'high' else 0.5

            # Create new node as child of the grounded claim
            new_node_id = self.engine.add_node(
                parent_id=assumption['parent_node_id'],
                claim=claim,
                branch_type=BranchType.ASSUME_WRONG,
                content=content,
                leverage_score=leverage
            )

            # Mark as integrated
            cursor.execute("""
                UPDATE grounding_assumptions
                SET integrated = 1, created_node_id = ?
                WHERE id = ?
            """, (new_node_id, assumption['id']))

            created_nodes.append(new_node_id)
            print(f"  Created assumption node: {claim[:60]}...")

        # Mark grounding as having assumptions integrated
        if grounding_id:
            cursor.execute("""
                UPDATE groundings SET assumptions_integrated = 1
                WHERE id = ?
            """, (grounding_id,))

        self.conn.commit()
        return created_nodes

    def integrate_all_assumptions(self, criticality: str = "high") -> int:
        """Integrate all pending assumptions into ARAW tree"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM groundings WHERE assumptions_integrated = 0")

        total_created = 0
        for row in cursor.fetchall():
            created = self.integrate_assumptions(row['id'], criticality)
            total_created += len(created)

        return total_created

    # ==================== EVIDENCE TIERS (Refinement #3) ====================

    def get_evidence_summary(self, node_id: str) -> Dict:
        """Get evidence quality summary for a grounded node"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT grounding_data, evidence_tier_best, testability,
                   has_contradictions, is_falsifiable
            FROM groundings WHERE node_id = ?
        """, (node_id,))
        row = cursor.fetchone()

        if not row:
            return {"grounded": False}

        grounding = json.loads(row['grounding_data'])

        # Analyze evidence tiers
        tier_counts = defaultdict(int)
        for src in grounding.get('data_sources', []):
            tier = src.get('evidence_tier', 'unknown')
            tier_counts[tier] += 1

        # Calculate weighted evidence score
        total_weight = 0
        for tier, count in tier_counts.items():
            weight = EVIDENCE_TIERS.get(tier, {}).get('weight', 0.1)
            total_weight += weight * count

        return {
            "grounded": True,
            "best_tier": row['evidence_tier_best'],
            "tier_distribution": dict(tier_counts),
            "evidence_score": total_weight / max(1, sum(tier_counts.values())),
            "testability": row['testability'],
            "has_contradictions": bool(row['has_contradictions']),
            "is_falsifiable": bool(row['is_falsifiable']),
            "source_count": len(grounding.get('data_sources', []))
        }

    # ==================== CONTRADICTION DETECTION (Refinement #4) ====================

    def get_contradictions(self) -> List[Dict]:
        """Get all detected contradictions across groundings"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT g.node_id, n.claim, g.grounding_data
            FROM groundings g
            JOIN nodes n ON g.node_id = n.id
            WHERE g.has_contradictions = 1
        """)

        contradictions = []
        for row in cursor:
            grounding = json.loads(row['grounding_data'])
            for c in grounding.get('contradictions', []):
                contradictions.append({
                    "node_id": row['node_id'],
                    "claim": row['claim'],
                    "contradiction": c
                })

        return contradictions

    # ==================== FALSIFIABILITY (Refinement #5) ====================

    def get_unfalsifiable_claims(self) -> List[Dict]:
        """Get claims that cannot be distinguished true vs false"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT g.node_id, n.claim, g.grounding_data
            FROM groundings g
            JOIN nodes n ON g.node_id = n.id
            WHERE g.is_falsifiable = 0
        """)

        unfalsifiable = []
        for row in cursor:
            grounding = json.loads(row['grounding_data'])
            falsifiability = grounding.get('falsifiability', {})
            unfalsifiable.append({
                "node_id": row['node_id'],
                "claim": row['claim'],
                "notes": falsifiability.get('falsifiability_notes', ''),
                "if_false_we_would_see": falsifiability.get('if_false_we_would_see', [])
            })

        return unfalsifiable

    # ==================== STATISTICS ====================

    def get_stats(self) -> Dict:
        """Get comprehensive grounding statistics"""
        cursor = self.conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM nodes")
        total_nodes = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM groundings")
        grounded_nodes = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM grounding_assumptions")
        total_assumptions = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM grounding_assumptions WHERE integrated = 1")
        integrated_assumptions = cursor.fetchone()[0]

        # Count by assumption type
        cursor.execute("""
            SELECT assumption_type, COUNT(*) FROM grounding_assumptions
            GROUP BY assumption_type
        """)
        assumption_type_dist = dict(cursor.fetchall())

        cursor.execute("""
            SELECT COUNT(*) FROM grounding_assumptions
            WHERE assumption_type = 'epistemic_limit' AND integrated = 1
        """)
        integrated_epistemic_limits = cursor.fetchone()[0]

        cursor.execute("""
            SELECT evidence_tier_best, COUNT(*)
            FROM groundings
            GROUP BY evidence_tier_best
        """)
        tier_dist = dict(cursor.fetchall())

        cursor.execute("""
            SELECT testability, COUNT(*)
            FROM groundings
            GROUP BY testability
        """)
        testability_dist = dict(cursor.fetchall())

        cursor.execute("SELECT COUNT(*) FROM groundings WHERE has_contradictions = 1")
        with_contradictions = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM groundings WHERE is_falsifiable = 0")
        unfalsifiable = cursor.fetchone()[0]

        return {
            "total_nodes": total_nodes,
            "grounded_nodes": grounded_nodes,
            "coverage": grounded_nodes / total_nodes if total_nodes > 0 else 0,
            "total_assumptions": total_assumptions,
            "integrated_assumptions": integrated_assumptions,
            "assumption_type_distribution": assumption_type_dist,
            "epistemic_limits_integrated": integrated_epistemic_limits,
            "evidence_tier_distribution": tier_dist,
            "testability_distribution": testability_dist,
            "claims_with_contradictions": with_contradictions,
            "unfalsifiable_claims": unfalsifiable
        }


def print_grounding(claim: str, grounding: dict):
    """Pretty print a grounding result"""
    print(f"\n{'='*70}")
    print(f"CLAIM: {claim}")
    print(f"{'='*70}")

    print(f"\nTESTABILITY: {grounding.get('testability', 'unknown')}")
    print(f"GROUNDING CONFIDENCE: {grounding.get('grounding_confidence', 'unknown')}")

    # Falsifiability
    falsifiability = grounding.get('falsifiability', {})
    print(f"\nFALSIFIABILITY:")
    if falsifiability.get('distinguishable', True):
        print(f"  ✓ Claim IS falsifiable")
    else:
        print(f"  ✗ Claim may be UNFALSIFIABLE")
    print(f"  If FALSE, we would see:")
    for obs in falsifiability.get('if_false_we_would_see', []):
        print(f"    • {obs}")
    if falsifiability.get('falsifiability_notes'):
        print(f"  Notes: {falsifiability['falsifiability_notes']}")

    print(f"\nOBSERVABLE INDICATORS:")
    for ind in grounding.get('observable_indicators', []):
        if isinstance(ind, dict):
            print(f"  • {ind.get('indicator', ind)}")
            if ind.get('how_to_find'):
                print(f"    How: {ind.get('how_to_find')}")
        else:
            print(f"  • {ind}")

    print(f"\nDATA SOURCES (with evidence tiers):")
    for src in grounding.get('data_sources', []):
        tier = src.get('evidence_tier', 'unknown')
        tier_info = EVIDENCE_TIERS.get(tier, {})
        tier_weight = tier_info.get('weight', 0)

        print(f"\n  [{tier.upper()}] (weight: {tier_weight}) {src.get('source_name', 'Unknown')}")
        if src.get('what_they_publish'):
            print(f"    Publishes: {src.get('what_they_publish')}")
        if src.get('stated_methodology'):
            print(f"    STATED method: {src.get('stated_methodology')}")
        if src.get('stated_purpose'):
            print(f"    STATED purpose: {src.get('stated_purpose')}")
        if src.get('published_figures'):
            print(f"    Published figures: {src.get('published_figures')}")
        if src.get('accessibility'):
            print(f"    Accessibility: {src.get('accessibility')}")

    # Contradictions
    contradictions = grounding.get('contradictions', [])
    if contradictions:
        print(f"\n⚠️  CONTRADICTIONS DETECTED:")
        for c in contradictions:
            print(f"  Topic: {c.get('topic')}")
            print(f"    {c.get('source_a')}: {c.get('source_a_says')}")
            print(f"    {c.get('source_b')}: {c.get('source_b_says')}")

    print(f"\nNEW ASSUMPTIONS NEEDED (can be ARAW-explored):")
    for assumption in grounding.get('new_assumptions', []):
        if isinstance(assumption, dict):
            crit = assumption.get('criticality', 'medium')
            crit_marker = "‼️" if crit == 'high' else "❗" if crit == 'medium' else "•"
            print(f"  {crit_marker} [{crit.upper()}] {assumption.get('assumption', assumption)}")
            if assumption.get('source_dependency'):
                print(f"      (depends on: {assumption.get('source_dependency')})")
        else:
            print(f"  • {assumption}")

    # Epistemic limit assumptions - claims about what we "can't know"
    epistemic_limits = grounding.get('epistemic_limit_assumptions', [])
    if epistemic_limits:
        print(f"\n🔒 EPISTEMIC LIMIT CLAIMS (themselves explorable!):")
        print(f"   These are claims about what we CAN'T know - but that's itself an assumption.")
        for limit in epistemic_limits:
            if isinstance(limit, dict):
                conf = limit.get('confidence_truly_limited', 'medium')
                conf_marker = "🔴" if conf == 'high' else "🟡" if conf == 'medium' else "🟢"
                print(f"\n  {conf_marker} LIMIT: {limit.get('limit_claim', limit)}")
                if limit.get('why_it_seems_limited'):
                    print(f"      Why limited: {limit.get('why_it_seems_limited')}")
                if limit.get('possible_ways_around'):
                    print(f"      🔓 Possible ways around: {limit.get('possible_ways_around')}")
                print(f"      Confidence truly limited: {conf}")
            else:
                print(f"  • {limit}")

    print(f"\nSEARCH QUERIES:")
    for q in grounding.get('search_queries', []):
        print(f"  • {q}")


def main():
    parser = argparse.ArgumentParser(description="ARAW Grounding Engine v2")
    parser.add_argument("--db", type=str, required=True, help="Database file")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL)

    # Prioritization
    parser.add_argument("--prioritize", action="store_true",
                       help="Show nodes prioritized for grounding")
    parser.add_argument("--limit", type=int, default=20)

    # Grounding
    parser.add_argument("--node", type=str, help="Ground specific node by ID")
    parser.add_argument("--ground-top", type=int,
                       help="Ground top N priority nodes")

    # Integration
    parser.add_argument("--integrate", action="store_true",
                       help="Create ARAW nodes from high-criticality assumptions")
    parser.add_argument("--integrate-all", action="store_true",
                       help="Create ARAW nodes from all assumptions")

    # Analysis
    parser.add_argument("--stats", action="store_true", help="Show grounding statistics")
    parser.add_argument("--contradictions", action="store_true",
                       help="Show detected contradictions")
    parser.add_argument("--unfalsifiable", action="store_true",
                       help="Show unfalsifiable claims")

    # Export
    parser.add_argument("--export", type=str, help="Export grounded claims to JSON")

    args = parser.parse_args()

    api_key = read_api_key()
    if not api_key:
        print("Error: No API key found")
        return

    engine = GroundingEngine(args.db, api_key, args.model)

    if args.stats:
        stats = engine.get_stats()
        print("GROUNDING STATISTICS:")
        print(f"  Total nodes: {stats['total_nodes']}")
        print(f"  Grounded nodes: {stats['grounded_nodes']} ({stats['coverage']*100:.1f}%)")
        print(f"  Total assumptions identified: {stats['total_assumptions']}")
        print(f"  Assumptions integrated to ARAW: {stats['integrated_assumptions']}")
        print(f"  Claims with contradictions: {stats['claims_with_contradictions']}")
        print(f"  Unfalsifiable claims: {stats['unfalsifiable_claims']}")
        print(f"\n  Assumption type distribution:")
        for atype, count in stats.get('assumption_type_distribution', {}).items():
            marker = "🔒" if atype == 'epistemic_limit' else "📋"
            print(f"    {marker} {atype or 'source'}: {count}")
        print(f"  Epistemic limits integrated: {stats.get('epistemic_limits_integrated', 0)}")
        print(f"\n  Evidence tier distribution:")
        for tier, count in stats.get('evidence_tier_distribution', {}).items():
            weight = EVIDENCE_TIERS.get(tier, {}).get('weight', 0)
            print(f"    {tier}: {count} (weight: {weight})")
        print(f"\n  Testability distribution:")
        for t, count in stats.get('testability_distribution', {}).items():
            print(f"    {t}: {count}")
        return

    if args.prioritize:
        print(f"TOP {args.limit} NODES TO GROUND (by priority score):\n")
        for i, p in enumerate(engine.get_priority_nodes(args.limit), 1):
            factors = p['factors']
            crux = "★" if factors['is_crux'] else " "
            grounded = "✓" if factors['already_grounded'] else " "
            print(f"{i:2d}. [{crux}] Score: {p['score']:.3f} | Influence: {factors['upstream_influence']:3d} | Conv: {factors['convergence']:.2f} | d={factors['depth']}")
            print(f"    {grounded} {p['claim'][:90]}...")
        return

    if args.node:
        grounding = engine.ground_node(args.node)
        if grounding:
            cursor = engine.conn.cursor()
            cursor.execute("SELECT claim FROM nodes WHERE id = ?", (args.node,))
            row = cursor.fetchone()
            print_grounding(row['claim'] if row else "Unknown", grounding)
        return

    if args.ground_top:
        print(f"Grounding top {args.ground_top} priority nodes...\n")
        priorities = engine.get_priority_nodes(args.ground_top)
        for p in priorities:
            if not p['factors']['already_grounded']:
                grounding = engine.ground_node(p['node_id'])
                if grounding:
                    print_grounding(p['claim'], grounding)
                    print("\n" + "-"*70 + "\n")
        return

    if args.integrate:
        print("Integrating HIGH criticality assumptions into ARAW tree...")
        created = engine.integrate_all_assumptions(criticality="high")
        print(f"Created {created} new ARAW nodes from assumptions")
        return

    if args.integrate_all:
        print("Integrating ALL assumptions into ARAW tree...")
        created = engine.integrate_all_assumptions(criticality=None)
        print(f"Created {created} new ARAW nodes from assumptions")
        return

    if args.contradictions:
        print("DETECTED CONTRADICTIONS:\n")
        for c in engine.get_contradictions():
            print(f"Claim: {c['claim'][:80]}...")
            cont = c['contradiction']
            print(f"  Topic: {cont.get('topic')}")
            print(f"  {cont.get('source_a')}: {cont.get('source_a_says')}")
            print(f"  {cont.get('source_b')}: {cont.get('source_b_says')}")
            print()
        return

    if args.unfalsifiable:
        print("UNFALSIFIABLE CLAIMS:\n")
        for u in engine.get_unfalsifiable_claims():
            print(f"Claim: {u['claim'][:80]}...")
            print(f"  Notes: {u['notes']}")
            print()
        return

    print("Use --prioritize, --ground-top N, --node ID, --integrate, --stats, etc.")
    print("Run with --help for all options.")


if __name__ == "__main__":
    main()

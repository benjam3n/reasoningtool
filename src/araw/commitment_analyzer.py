#!/usr/bin/env python3
"""
ARAW Commitment Analyzer

Analyzes an existing ARAW tree to determine which claims are FOUNDATIONAL
(can be committed to) vs GUESSES (coherent alternatives exist).

Uses the same database as auto_expand_llm.py.

Usage:
    python commitment_analyzer.py --db my_search.db analyze
    python commitment_analyzer.py --db my_search.db foundations
    python commitment_analyzer.py --db my_search.db guesses
    python commitment_analyzer.py --db my_search.db check "specific claim"
"""

import argparse
import json
import os
import sqlite3
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Optional, List, Tuple, Dict
from dataclasses import dataclass
from enum import Enum

# Import from existing ARAW
from araw_engine import ARAWEngine, BranchType, NodeStatus, Node

DEFAULT_KEY_FILE = str(Path.home() / ".config" / "gosm" / "openai_api_key")
DEFAULT_BASE_URL = "https://api.openai.com/v1/responses"
DEFAULT_MODEL = "gpt-5-nano"


class CommitmentStatus(Enum):
    FOUNDATIONAL = "foundational"  # All AW paths contradict - can commit
    GUESS = "guess"                # Some AW path survives - cannot commit
    UNCHECKED = "unchecked"        # Not yet analyzed
    INCONCLUSIVE = "inconclusive"  # Hit depth limit without resolution


@dataclass
class CommitmentResult:
    status: CommitmentStatus
    reason: str
    aw_paths_checked: int
    contradictions: List[str]
    coherent_alternatives: List[str]
    root_claim: str = ""
    total_aw_nodes: int = 0


def read_api_key(path: Optional[str] = None) -> Optional[str]:
    """Read API key from env or file"""
    env = os.environ.get("OPENAI_API_KEY", "").strip()
    if env:
        return env
    for p in ([path] if path else []) + [DEFAULT_KEY_FILE]:
        if p and Path(p).expanduser().is_file():
            key = Path(p).expanduser().read_text().splitlines()[0].strip()
            if key:
                return key
    return None


def api_call(api_key: str, payload: dict, timeout: int = 60, max_retries: int = 5) -> Tuple[bool, dict]:
    """Make API call to OpenAI Responses API with retry on rate limits"""
    import re

    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".json") as f:
        json.dump(payload, f, ensure_ascii=False)
        payload_path = f.name

    body_path = tempfile.mktemp(suffix=".json")

    try:
        for attempt in range(max_retries):
            cmd = [
                "curl", "-sS", DEFAULT_BASE_URL,
                "--http1.1", "--connect-timeout", "15", "--max-time", str(timeout),
                "--retry", "3", "--fail-with-body",
                "-H", f"Authorization: Bearer {api_key}",
                "-H", "Content-Type: application/json",
                "-d", f"@{payload_path}",
                "-o", body_path,
                "-w", "%{http_code}"
            ]
            proc = subprocess.run(cmd, text=True, capture_output=True, timeout=timeout + 30, check=False)
            body = Path(body_path).read_text() if Path(body_path).exists() else ""
            code = (proc.stdout or "").strip()

            # Check for rate limit error (429 or rate_limit in body)
            if "rate_limit" in body.lower() or code == "429":
                wait_match = re.search(r'try again in (\d+\.?\d*)s', body)
                wait_time = float(wait_match.group(1)) if wait_match else (2 ** attempt)
                wait_time = min(wait_time + 0.5, 30)
                if attempt < max_retries - 1:
                    print(f"    [Rate limited, waiting {wait_time:.1f}s before retry {attempt + 2}/{max_retries}...]")
                    time.sleep(wait_time)
                    continue

            if proc.returncode != 0 or (code and code != "200"):
                return False, {"error": f"HTTP {code}", "body": body[:200]}

            try:
                return True, json.loads(body)
            except json.JSONDecodeError as e:
                return False, {"error": f"json_decode: {e}", "body": body[:200]}

        return False, {"error": "rate_limit_retries_exhausted"}

    except Exception as e:
        return False, {"error": str(e)}
    finally:
        Path(payload_path).unlink(missing_ok=True)
        Path(body_path).unlink(missing_ok=True)


def extract_text(resp: dict) -> str:
    """Extract text from API response"""
    # Check nested output structure - look for message type items
    for item in resp.get("output", []):
        # Skip reasoning items, look for message type
        if item.get("type") == "message":
            for c in item.get("content", []):
                if isinstance(c, dict) and c.get("type") in ("output_text", "text"):
                    return c.get("text", "").strip()
    # Fallback: check all output items
    for item in resp.get("output", []):
        for c in item.get("content", []):
            if isinstance(c, dict) and c.get("type") in ("output_text", "text"):
                return c.get("text", "").strip()
    # Check choices structure (chat completions format)
    if "choices" in resp:
        return resp["choices"][0].get("message", {}).get("content", "").strip()
    return ""


class CommitmentAnalyzer:
    """Analyzes ARAW tree for foundational vs guess claims"""

    def __init__(self, engine: ARAWEngine, api_key: str, model: str = DEFAULT_MODEL, rate_limit: float = 0.1, verbose: bool = False):
        self.engine = engine
        self.api_key = api_key
        self.model = model
        self.rate_limit = rate_limit  # Seconds between API calls (0.1 = 10/sec max)
        self.last_call_time = 0
        self.verbose = verbose
        self._ensure_schema()

    def _rate_limit_wait(self, verbose: bool = False):
        """Wait if needed to respect rate limit"""
        elapsed = time.time() - self.last_call_time
        if elapsed < self.rate_limit:
            wait_time = self.rate_limit - elapsed
            if verbose:
                print(f"    [rate limit: waiting {wait_time:.2f}s]")
            time.sleep(wait_time)
        self.last_call_time = time.time()

    def _ensure_schema(self):
        """Add commitment columns if not present"""
        cursor = self.engine.conn.cursor()
        try:
            cursor.execute("ALTER TABLE nodes ADD COLUMN commitment_status TEXT DEFAULT 'unchecked'")
        except sqlite3.OperationalError:
            pass  # Column already exists
        try:
            cursor.execute("ALTER TABLE nodes ADD COLUMN commitment_reason TEXT")
        except sqlite3.OperationalError:
            pass
        self.engine.conn.commit()

    def check_contradiction_llm(self, claim: str, path_context: str) -> Tuple[bool, str]:
        """Use LLM to check if a claim is self-contradictory"""
        self._rate_limit_wait(self.verbose)

        prompt = f"""Analyze this claim for logical self-contradiction:

Claim: "{claim}"
Context: This claim arose from ASSUME WRONG reasoning. Path: {path_context}

Is this claim SELF-REFUTING or PERFORMATIVELY CONTRADICTORY?

Self-refuting means: the claim presupposes what it denies
- "Nothing exists" presupposes existence to make the claim
- "There is no truth" claims truth about no truth
- "I am not communicating" is itself communication

Performative contradiction means: the act of making the claim contradicts its content
- "This sentence does not exist" - the sentence exists to deny itself

Answer in this format:
CONTRADICTION: YES or NO
REASON: one sentence explanation"""

        payload = {
            "model": self.model,
            "max_output_tokens": 24000,
            "input": [{"role": "user", "content": [{"type": "input_text", "text": prompt}]}],
        }

        ok, resp = api_call(self.api_key, payload)
        if not ok:
            return False, "API error"

        text = extract_text(resp)
        text_upper = text.upper()

        # More flexible parsing
        is_contradiction = False
        if "CONTRADICTION:" in text_upper:
            after_marker = text_upper.split("CONTRADICTION:")[-1].strip()
            is_contradiction = after_marker.startswith("YES")
        elif "YES" in text_upper and "SELF-REFUT" in text_upper:
            is_contradiction = True

        # Extract reason
        reason = ""
        if "REASON:" in text:
            reason = text.split("REASON:")[-1].strip()
        elif "REASON:" in text_upper:
            idx = text_upper.find("REASON:")
            reason = text[idx+7:].strip()

        return is_contradiction, reason if reason else text[:100]

    def check_coherent_alternative_llm(self, claim: str, root_claim: str) -> Tuple[bool, str]:
        """Use LLM to check if a claim represents a coherent alternative"""
        self._rate_limit_wait(self.verbose)

        prompt = f"""Analyze if this is a coherent alternative:

Root claim: "{root_claim}"
Alternative claim: "{claim}"

A COHERENT alternative means:
- It could actually be true (is logically possible)
- It's not self-refuting
- It provides a genuine alternative to the root claim

If coherent, describe THE SPECIFIC ALTERNATIVE SCENARIO - what would actually be true instead.

Answer in this format:
COHERENT: YES or NO
ALTERNATIVE: one sentence describing the specific scenario that would be true instead"""

        payload = {
            "model": self.model,
            "max_output_tokens": 24000,
            "input": [{"role": "user", "content": [{"type": "input_text", "text": prompt}]}],
        }

        ok, resp = api_call(self.api_key, payload)
        if not ok:
            return True, "API error - defaulting to coherent"

        text = extract_text(resp)
        text_upper = text.upper()

        # More flexible parsing
        is_coherent = True  # Default to coherent if unclear
        if "COHERENT:" in text_upper:
            after_marker = text_upper.split("COHERENT:")[-1].strip()
            is_coherent = after_marker.startswith("YES") or not after_marker.startswith("NO")
        elif "NOT COHERENT" in text_upper or "SELF-REFUT" in text_upper:
            is_coherent = False

        # Extract alternative scenario
        alternative = ""
        if "ALTERNATIVE:" in text:
            alternative = text.split("ALTERNATIVE:")[-1].strip()
        elif "ALTERNATIVE:" in text_upper:
            idx = text_upper.find("ALTERNATIVE:")
            alternative = text[idx+12:].strip()

        return is_coherent, alternative if alternative else text[:100]

    def get_aw_paths(self) -> List[Node]:
        """Get all terminal nodes on AW-originating paths"""
        cursor = self.engine.conn.cursor()

        # Step 1: Find all terminal nodes (nodes with no children)
        cursor.execute("""
            SELECT n.id FROM nodes n
            LEFT JOIN nodes c ON c.parent_id = n.id
            WHERE c.id IS NULL
        """)
        all_terminals = set(row['id'] for row in cursor.fetchall())

        if not all_terminals:
            return []

        # Step 2: For each terminal, trace back to see if it has an AW at depth 1
        terminal_ids = set()
        for terminal_id in all_terminals:
            # Trace path back to root
            current_id = terminal_id
            is_aw_origin = False

            while current_id:
                cursor.execute("SELECT parent_id, depth, branch_type FROM nodes WHERE id = ?", (current_id,))
                row = cursor.fetchone()
                if not row:
                    break

                # Check if this is depth-1 and assume_wrong
                if row['depth'] == 1 and row['branch_type'] == 'assume_wrong':
                    is_aw_origin = True
                    break

                current_id = row['parent_id']

            if is_aw_origin:
                terminal_ids.add(terminal_id)

        if not terminal_ids:
            return []

        # Fetch full node data for terminals
        placeholders = ','.join('?' * len(terminal_ids))
        cursor.execute(f"SELECT * FROM nodes WHERE id IN ({placeholders})", list(terminal_ids))

        nodes = []
        for row in cursor.fetchall():
            nodes.append(Node(
                id=row['id'],
                parent_id=row['parent_id'],
                claim=row['claim'],
                branch_type=row['branch_type'],
                status=row['status'],
                depth=row['depth'],
                leverage_score=row['leverage_score'],
                content=json.loads(row['content']) if row['content'] else {},
                created_at=row['created_at'],
                explored_at=row['explored_at'] if 'explored_at' in row.keys() else None
            ))

        return nodes

    def get_path_to_root(self, node: Node) -> List[str]:
        """Get the path from node to root as list of branch types"""
        path = []
        current = node
        while current.parent_id:
            path.append(current.branch_type)
            parent = self.engine.get_node(current.parent_id)
            if parent:
                current = parent
            else:
                break
        return list(reversed(path))

    def analyze_node(self, node: Node, root_claim: str) -> Tuple[CommitmentStatus, str]:
        """Analyze a single node for commitment status"""
        path = self.get_path_to_root(node)
        path_str = " → ".join(path)

        # Check if already marked foundational by existing system
        content = node.content or {}
        if content.get("is_foundational"):
            return CommitmentStatus.FOUNDATIONAL, "Marked foundational by exploration"

        # Check for contradiction
        is_contradiction, reason = self.check_contradiction_llm(node.claim, path_str)
        if is_contradiction:
            return CommitmentStatus.FOUNDATIONAL, reason

        # Check for coherent alternative
        is_coherent, reason = self.check_coherent_alternative_llm(node.claim, root_claim)
        if is_coherent:
            return CommitmentStatus.GUESS, reason

        return CommitmentStatus.INCONCLUSIVE, "undetermined"

    def analyze_tree(self) -> CommitmentResult:
        """Analyze entire tree for commitment status"""
        # Get root claim
        cursor = self.engine.conn.cursor()
        cursor.execute("SELECT claim FROM nodes WHERE depth = 0")
        row = cursor.fetchone()
        if not row:
            return CommitmentResult(
                status=CommitmentStatus.INCONCLUSIVE,
                reason="No root node found",
                aw_paths_checked=0,
                contradictions=[],
                coherent_alternatives=[],
                root_claim="",
                total_aw_nodes=0
            )
        root_claim = row['claim']

        # Get all AW-originating terminal nodes
        aw_terminals = self.get_aw_paths()
        if not aw_terminals:
            return CommitmentResult(
                status=CommitmentStatus.INCONCLUSIVE,
                reason="No assume-wrong paths found",
                aw_paths_checked=0,
                contradictions=[],
                coherent_alternatives=[],
                root_claim=root_claim,
                total_aw_nodes=0
            )

        total_aw = len(aw_terminals)

        # Limit nodes to analyze (LLM calls are slow)
        max_nodes = 20
        if len(aw_terminals) > max_nodes:
            aw_terminals = aw_terminals[:max_nodes]

        contradictions = []
        coherent_alternatives = []

        # Progress indicator (to stderr so it doesn't pollute output)
        import sys
        for i, node in enumerate(aw_terminals):
            print(f"  [{i+1}/{len(aw_terminals)}] Analyzing...", end="\r", file=sys.stderr)
            status, reason = self.analyze_node(node, root_claim)

            # Update node in database
            cursor.execute(
                "UPDATE nodes SET commitment_status = ?, commitment_reason = ? WHERE id = ?",
                (status.value, reason, node.id)
            )

            if status == CommitmentStatus.FOUNDATIONAL:
                contradictions.append(reason)
            elif status == CommitmentStatus.GUESS:
                coherent_alternatives.append(reason)

        print(" " * 40, end="\r", file=sys.stderr)  # Clear progress line

        self.engine.conn.commit()

        # Determine overall status
        if coherent_alternatives:
            return CommitmentResult(
                status=CommitmentStatus.GUESS,
                reason=f"{len(coherent_alternatives)} AW path(s) survive coherently",
                aw_paths_checked=len(aw_terminals),
                contradictions=contradictions,
                coherent_alternatives=coherent_alternatives,
                root_claim=root_claim,
                total_aw_nodes=total_aw
            )
        elif contradictions:
            return CommitmentResult(
                status=CommitmentStatus.FOUNDATIONAL,
                reason=f"All {len(contradictions)} AW path(s) contradict",
                aw_paths_checked=len(aw_terminals),
                contradictions=contradictions,
                coherent_alternatives=[],
                root_claim=root_claim,
                total_aw_nodes=total_aw
            )
        else:
            return CommitmentResult(
                status=CommitmentStatus.INCONCLUSIVE,
                reason="No paths could be definitively classified",
                aw_paths_checked=len(aw_terminals),
                contradictions=[],
                coherent_alternatives=[],
                root_claim=root_claim,
                total_aw_nodes=total_aw
            )

    def get_foundations(self) -> List[Node]:
        """Get all nodes marked as foundational"""
        cursor = self.engine.conn.cursor()
        cursor.execute("SELECT * FROM nodes WHERE commitment_status = 'foundational'")
        nodes = []
        for row in cursor.fetchall():
            nodes.append(Node(
                id=row['id'],
                parent_id=row['parent_id'],
                claim=row['claim'],
                branch_type=row['branch_type'],
                status=row['status'],
                depth=row['depth'],
                leverage_score=row['leverage_score'],
                content=json.loads(row['content']) if row['content'] else {},
                created_at=row['created_at'],
                explored_at=row['explored_at'] if 'explored_at' in row.keys() else None
            ))
        return nodes

    def get_guesses(self) -> List[Node]:
        """Get all nodes marked as guesses"""
        cursor = self.engine.conn.cursor()
        cursor.execute("SELECT * FROM nodes WHERE commitment_status = 'guess'")
        nodes = []
        for row in cursor.fetchall():
            nodes.append(Node(
                id=row['id'],
                parent_id=row['parent_id'],
                claim=row['claim'],
                branch_type=row['branch_type'],
                status=row['status'],
                depth=row['depth'],
                leverage_score=row['leverage_score'],
                content=json.loads(row['content']) if row['content'] else {},
                created_at=row['created_at'],
                explored_at=row['explored_at'] if 'explored_at' in row.keys() else None
            ))
        return nodes


def main():
    parser = argparse.ArgumentParser(description="ARAW Commitment Analyzer")
    parser.add_argument("--db", required=True, help="Path to ARAW database")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Model to use")
    parser.add_argument("--key-file", help="Path to API key file")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show rate limiting info")
    parser.add_argument("command", choices=["analyze", "foundations", "guesses", "check", "stats"])
    parser.add_argument("claim", nargs="?", help="Specific claim for 'check' command")
    args = parser.parse_args()

    # Get API key
    api_key = read_api_key(args.key_file)
    if not api_key:
        print("Error: No API key found")
        print("Set OPENAI_API_KEY or create ~/.config/gosm/openai_api_key")
        return 1

    # Connect to database
    engine = ARAWEngine(args.db)
    analyzer = CommitmentAnalyzer(engine, api_key, args.model, verbose=args.verbose)

    if args.command == "analyze":
        # Get count of terminal nodes before analysis
        cursor = engine.conn.cursor()
        cursor.execute("""
            SELECT COUNT(*) FROM nodes n
            LEFT JOIN nodes c ON c.parent_id = n.id
            WHERE c.id IS NULL
        """)
        total_terminals = cursor.fetchone()[0]

        result = analyzer.analyze_tree()

        # Header
        db_name = Path(args.db).stem
        print("="*60)
        print("ARAW COMMITMENT ANALYSIS")
        print("="*60)

        # Root claim
        root_display = result.root_claim[:70] + "..." if len(result.root_claim) > 70 else result.root_claim
        print(f"Root claim: {root_display}")
        print(f"Found {total_terminals} terminal nodes")
        print(f"Analyzing {result.aw_paths_checked} AW-originating paths...")

        # Show what was found
        for alt in result.coherent_alternatives:
            alt_display = alt[:100] + "..." if len(alt) > 100 else alt
            print(f"  [GUESS] {alt_display}")

        for cont in result.contradictions:
            cont_display = cont[:100] + "..." if len(cont) > 100 else cont
            print(f"  [CONTRADICTION] {cont_display}")

        # Result
        print()
        if result.status == CommitmentStatus.GUESS:
            print(f"[RESULT] GUESS ({result.aw_paths_checked} paths: {len(result.contradictions)} contradictions, {len(result.coherent_alternatives)} coherent)")
        elif result.status == CommitmentStatus.FOUNDATIONAL:
            print(f"[RESULT] FOUNDATIONAL (all {result.aw_paths_checked} AW paths contradict)")
        else:
            print(f"[RESULT] INCONCLUSIVE")

    elif args.command == "foundations":
        foundations = analyzer.get_foundations()
        print(f"FOUNDATIONAL ({len(foundations)}):")
        for node in foundations:
            c = node.claim[:100] + "..." if len(node.claim) > 100 else node.claim
            print(f"  {c}")

    elif args.command == "guesses":
        guesses = analyzer.get_guesses()
        print(f"GUESSES ({len(guesses)}):")
        for node in guesses:
            c = node.claim[:100] + "..." if len(node.claim) > 100 else node.claim
            print(f"  {c}")

    elif args.command == "check":
        if not args.claim:
            print("Error: 'check' command requires a claim")
            return 1
        # Find node with matching claim
        cursor = engine.conn.cursor()
        cursor.execute("SELECT * FROM nodes WHERE claim LIKE ?", (f"%{args.claim}%",))
        row = cursor.fetchone()
        if not row:
            print(f"No node found matching: {args.claim}")
            return 1

        node = Node(
            id=row['id'],
            parent_id=row['parent_id'],
            claim=row['claim'],
            branch_type=row['branch_type'],
            status=row['status'],
            depth=row['depth'],
            leverage_score=row['leverage_score'],
            content=json.loads(row['content']) if row['content'] else {},
            created_at=row['created_at'],
            explored_at=row['explored_at'] if 'explored_at' in row.keys() else None
        )

        # Get root claim
        cursor.execute("SELECT claim FROM nodes WHERE depth = 0")
        root_row = cursor.fetchone()
        root_claim = root_row['claim'] if root_row else node.claim

        status, reason = analyzer.analyze_node(node, root_claim)
        c = node.claim[:100] + "..." if len(node.claim) > 100 else node.claim
        print(f"[{status.value.upper()}] {c}")

    elif args.command == "stats":
        cursor = engine.conn.cursor()
        cursor.execute("SELECT commitment_status, COUNT(*) as cnt FROM nodes GROUP BY commitment_status")
        print("COMMITMENT STATUS DISTRIBUTION:")
        for row in cursor.fetchall():
            status = row['commitment_status'] or 'unchecked'
            print(f"  {status}: {row['cnt']}")

    return 0


if __name__ == "__main__":
    exit(main())

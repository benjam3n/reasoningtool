#!/usr/bin/env python3
"""
GOSM Agent - Powerful observation and verification agent.

Capabilities:
1. Tool-assisted LLM - LLM can read files, search, before making claims
2. Iterative exploration - Loop until satisfied or max iterations
3. Test execution - Actually run code to verify behavior claims
4. AST/Semantic understanding - Parse code structure, find definitions/calls

Architecture:
    gosm_runner.py (structure/procedures)
           │
           ▼
    gosm_agent.py (observation/verification/execution)
           │
           ├── Tool-assisted LLM (observe before claiming)
           ├── Iterative loop (refine until verified)
           ├── Test execution (run code to verify)
           └── AST analysis (semantic code understanding)
           │
           ▼
    Verified Output

Usage:
    # Tool-assisted exploration
    agent.explore("How does error handling work?")

    # Iterative verification
    agent.iterative_verify("The ARAW engine uses SQLite", max_iterations=5)

    # Test execution
    agent.verify_by_test("add(1, 2) returns 3", test_code="assert add(1, 2) == 3")

    # AST analysis
    agent.find_function_calls("explore_araw")
    agent.find_class_definitions("GOSMAgent")
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import subprocess
import sys
import tempfile
import traceback
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Literal

# Try to import optional dependencies
_aider_available = False
try:
    from aider.coders import Coder
    from aider.models import Model
    from aider.io import InputOutput
    _aider_available = True
except ImportError:
    pass

_openai_available = False
try:
    import openai
    _openai_available = True
except ImportError:
    pass


# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class Observation:
    """A verified observation from the codebase."""
    claim: str
    verified: bool
    source: str  # file:line or search query
    evidence: str  # What was actually observed
    marker: str  # [O: source], [T: result], [D: derivation]
    confidence: float = 1.0  # 1.0 for direct observation
    method: str = "observation"  # observation, test, ast, derivation


@dataclass
class SearchResult:
    """Result from searching the codebase."""
    query: str
    files: list[str] = field(default_factory=list)
    matches: list[dict[str, Any]] = field(default_factory=list)
    total_matches: int = 0


@dataclass
class TestResult:
    """Result from executing a test."""
    test_code: str
    passed: bool
    output: str
    error: str | None = None
    duration_ms: int = 0


@dataclass
class ASTResult:
    """Result from AST analysis."""
    query: str
    query_type: str  # function_def, class_def, function_call, import, etc.
    matches: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class ExplorationResult:
    """Result from an exploration task."""
    task: str
    observations: list[Observation] = field(default_factory=list)
    files_examined: list[str] = field(default_factory=list)
    iterations: int = 0
    satisfied: bool = False
    summary: str = ""


@dataclass
class ToolCall:
    """A tool call made by the LLM."""
    tool: str
    args: dict[str, Any]
    result: Any = None


# ============================================================================
# MAIN AGENT CLASS
# ============================================================================

class GOSMAgent:
    """
    Powerful observation and verification agent for GOSM.

    Power-ups implemented:
    1. Tool-assisted LLM - LLM observes before claiming
    2. Iterative exploration - Loop until satisfied
    3. Test execution - Run code to verify behavior
    4. AST/Semantic understanding - Parse code structure
    """

    def __init__(
        self,
        root_path: str | Path | None = None,
        model: str = "gpt-4o-mini",
        api_key: str | None = None,
        verbose: bool = False,
        max_iterations: int = 10,
    ):
        self.root = Path(root_path) if root_path else Path.cwd()
        self.model = model
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self.verbose = verbose
        self.max_iterations = max_iterations

        # Tool registry
        self.tools = self._build_tool_registry()

        # LLM client
        self._llm_client = None

    def log(self, msg: str) -> None:
        if self.verbose:
            print(f"[GOSM-Agent] {msg}")

    # ========================================================================
    # POWER-UP 1: TOOL-ASSISTED LLM
    # ========================================================================

    def _build_tool_registry(self) -> dict[str, dict[str, Any]]:
        """Build registry of tools the LLM can call."""
        return {
            "read_file": {
                "function": self.read_file,
                "description": "Read a file's contents. Args: filepath (str), lines (tuple[int,int] optional)",
                "schema": {
                    "type": "function",
                    "function": {
                        "name": "read_file",
                        "description": "Read contents of a file with line numbers",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "filepath": {"type": "string", "description": "Path to file"},
                                "start_line": {"type": "integer", "description": "Start line (1-indexed)"},
                                "end_line": {"type": "integer", "description": "End line"},
                            },
                            "required": ["filepath"],
                        },
                    },
                },
            },
            "grep": {
                "function": self.grep,
                "description": "Search for pattern in codebase. Args: pattern (str), file_pattern (str optional)",
                "schema": {
                    "type": "function",
                    "function": {
                        "name": "grep",
                        "description": "Search for regex pattern in files",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "pattern": {"type": "string", "description": "Regex pattern to search"},
                                "file_pattern": {"type": "string", "description": "Glob pattern for files (e.g., *.py)"},
                                "max_results": {"type": "integer", "description": "Max matches to return"},
                            },
                            "required": ["pattern"],
                        },
                    },
                },
            },
            "glob_files": {
                "function": self.glob_files,
                "description": "Find files matching glob pattern. Args: pattern (str)",
                "schema": {
                    "type": "function",
                    "function": {
                        "name": "glob_files",
                        "description": "Find files matching a glob pattern",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "pattern": {"type": "string", "description": "Glob pattern (e.g., **/*.py)"},
                            },
                            "required": ["pattern"],
                        },
                    },
                },
            },
            "find_function": {
                "function": self.find_function_definition,
                "description": "Find where a function is defined. Args: function_name (str)",
                "schema": {
                    "type": "function",
                    "function": {
                        "name": "find_function",
                        "description": "Find function definition in codebase",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "function_name": {"type": "string", "description": "Name of function to find"},
                            },
                            "required": ["function_name"],
                        },
                    },
                },
            },
            "find_class": {
                "function": self.find_class_definition,
                "description": "Find where a class is defined. Args: class_name (str)",
                "schema": {
                    "type": "function",
                    "function": {
                        "name": "find_class",
                        "description": "Find class definition in codebase",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "class_name": {"type": "string", "description": "Name of class to find"},
                            },
                            "required": ["class_name"],
                        },
                    },
                },
            },
            "find_calls": {
                "function": self.find_function_calls,
                "description": "Find all places a function is called. Args: function_name (str)",
                "schema": {
                    "type": "function",
                    "function": {
                        "name": "find_calls",
                        "description": "Find all calls to a function",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "function_name": {"type": "string", "description": "Name of function"},
                            },
                            "required": ["function_name"],
                        },
                    },
                },
            },
            "run_test": {
                "function": self.run_test,
                "description": "Execute Python test code. Args: test_code (str)",
                "schema": {
                    "type": "function",
                    "function": {
                        "name": "run_test",
                        "description": "Run Python code to test a hypothesis",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "test_code": {"type": "string", "description": "Python code to execute"},
                                "timeout": {"type": "integer", "description": "Timeout in seconds"},
                            },
                            "required": ["test_code"],
                        },
                    },
                },
            },
        }

    def _get_llm_client(self):
        """Get or create LLM client."""
        if self._llm_client is None:
            if not _openai_available:
                raise RuntimeError("OpenAI package not available. Install with: pip install openai")
            self._llm_client = openai.OpenAI(api_key=self.api_key)
        return self._llm_client

    def explore(self, task: str, max_iterations: int | None = None) -> ExplorationResult:
        """
        Explore the codebase to answer a question or find information.

        The LLM uses tools to observe the codebase, then makes claims based
        on what it actually sees.

        Args:
            task: What to explore/find/understand
            max_iterations: Max tool-use iterations (default: self.max_iterations)

        Returns:
            ExplorationResult with observations and summary
        """
        max_iter = max_iterations or self.max_iterations
        result = ExplorationResult(task=task)

        self.log(f"Exploring: {task}")

        # Build tool schemas for LLM
        tool_schemas = [t["schema"] for t in self.tools.values()]

        messages = [
            {
                "role": "system",
                "content": """You are a code exploration agent. Your job is to investigate codebases and make VERIFIED claims.

RULES:
1. Use tools to OBSERVE before making claims
2. Every claim must have evidence from tool results
3. Use [O: source] markers for observed facts
4. If you can't verify something, say "UNVERIFIED" or "UNKNOWN"
5. When you have enough information, provide a summary with your findings

Available tools: read_file, grep, glob_files, find_function, find_class, find_calls, run_test

Start by using tools to gather information, then synthesize your findings."""
            },
            {
                "role": "user",
                "content": f"Task: {task}\n\nUse the available tools to investigate this. Make observations and report findings with evidence."
            }
        ]

        client = self._get_llm_client()
        files_examined = set()

        for iteration in range(max_iter):
            result.iterations = iteration + 1
            self.log(f"  Iteration {iteration + 1}/{max_iter}")

            try:
                response = client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    tools=tool_schemas,
                    tool_choice="auto",
                )
            except Exception as e:
                self.log(f"  LLM error: {e}")
                break

            message = response.choices[0].message

            # Check for tool calls
            if message.tool_calls:
                messages.append(message)

                for tool_call in message.tool_calls:
                    tool_name = tool_call.function.name
                    try:
                        args = json.loads(tool_call.function.arguments)
                    except json.JSONDecodeError:
                        args = {}

                    self.log(f"    Tool: {tool_name}({args})")

                    # Execute tool
                    tool_result = self._execute_tool(tool_name, args)

                    # Track files examined
                    if tool_name == "read_file" and "filepath" in args:
                        files_examined.add(args["filepath"])
                    elif tool_name == "grep" and isinstance(tool_result, SearchResult):
                        files_examined.update(tool_result.files)

                    # Format result for LLM
                    result_str = self._format_tool_result(tool_name, tool_result)

                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result_str[:4000],  # Truncate long results
                    })

            else:
                # No tool calls - LLM is done or providing summary
                content = message.content or ""
                messages.append(message)

                # Parse observations from response
                observations = self._parse_observations(content)
                result.observations.extend(observations)

                # Check if LLM indicates it's done
                if any(marker in content.lower() for marker in ["summary:", "findings:", "conclusion:", "in summary"]):
                    result.satisfied = True
                    result.summary = content
                    break

                # Ask for summary if not provided
                messages.append({
                    "role": "user",
                    "content": "Please provide a summary of your findings with [O: source] markers for each verified observation."
                })

        result.files_examined = list(files_examined)
        return result

    def _execute_tool(self, tool_name: str, args: dict[str, Any]) -> Any:
        """Execute a tool and return result."""
        if tool_name not in self.tools:
            return {"error": f"Unknown tool: {tool_name}"}

        tool = self.tools[tool_name]
        func = tool["function"]

        try:
            # Map args to function parameters
            if tool_name == "read_file":
                lines = None
                if "start_line" in args and "end_line" in args:
                    lines = (args["start_line"], args["end_line"])
                return func(args.get("filepath", ""), lines=lines)

            elif tool_name == "grep":
                return func(
                    args.get("pattern", ""),
                    file_pattern=args.get("file_pattern", "*"),
                    max_results=args.get("max_results", 50),
                )

            elif tool_name == "glob_files":
                return func(args.get("pattern", ""))

            elif tool_name in ("find_function", "find_class"):
                name = args.get("function_name") or args.get("class_name", "")
                return func(name)

            elif tool_name == "find_calls":
                return func(args.get("function_name", ""))

            elif tool_name == "run_test":
                return func(
                    args.get("test_code", ""),
                    timeout=args.get("timeout", 10),
                )

            else:
                return func(**args)

        except Exception as e:
            return {"error": str(e), "traceback": traceback.format_exc()}

    def _format_tool_result(self, tool_name: str, result: Any) -> str:
        """Format tool result for LLM consumption."""
        if isinstance(result, dict):
            if "error" in result:
                return f"Error: {result['error']}"
            return json.dumps(result, indent=2, default=str)

        elif isinstance(result, SearchResult):
            lines = [f"Found {result.total_matches} matches for '{result.query}'"]
            for m in result.matches[:20]:
                lines.append(f"  {m['file']}:{m['line']}: {m['text'][:100]}")
            return "\n".join(lines)

        elif isinstance(result, ASTResult):
            lines = [f"AST {result.query_type} search for '{result.query}': {len(result.matches)} found"]
            for m in result.matches[:20]:
                lines.append(f"  {m.get('file', '?')}:{m.get('line', '?')}: {m.get('name', '?')}")
            return "\n".join(lines)

        elif isinstance(result, TestResult):
            status = "PASSED" if result.passed else "FAILED"
            return f"Test {status}\nOutput: {result.output[:500]}\nError: {result.error or 'None'}"

        elif isinstance(result, list):
            return json.dumps(result[:50], indent=2, default=str)

        else:
            return str(result)[:2000]

    def _parse_observations(self, text: str) -> list[Observation]:
        """Parse observations from LLM response text."""
        observations = []

        # Look for [O: source] markers
        pattern = r'([^[\n]+)\s*\[O:\s*([^\]]+)\]'
        for match in re.finditer(pattern, text):
            claim = match.group(1).strip().rstrip('.')
            source = match.group(2).strip()
            observations.append(Observation(
                claim=claim,
                verified=True,
                source=source,
                evidence=f"Observed by LLM from {source}",
                marker=f"[O: {source}]",
                method="tool_assisted",
            ))

        # Look for [T: result] markers
        pattern = r'([^[\n]+)\s*\[T:\s*([^\]]+)\]'
        for match in re.finditer(pattern, text):
            claim = match.group(1).strip().rstrip('.')
            result = match.group(2).strip()
            observations.append(Observation(
                claim=claim,
                verified=True,
                source="test",
                evidence=result,
                marker=f"[T: {result}]",
                method="test",
            ))

        return observations

    # ========================================================================
    # POWER-UP 2: ITERATIVE EXPLORATION
    # ========================================================================

    def iterative_verify(
        self,
        claim: str,
        max_iterations: int | None = None,
        strategies: list[str] | None = None,
    ) -> Observation:
        """
        Iteratively try to verify a claim using multiple strategies.

        Strategies tried in order:
        1. Direct source lookup (if source specified)
        2. Grep for key terms
        3. AST analysis for code elements
        4. Test execution (if claim is about behavior)
        5. LLM-guided exploration

        Args:
            claim: The claim to verify
            max_iterations: Max attempts per strategy
            strategies: Override default strategy order

        Returns:
            Observation with best verification result
        """
        max_iter = max_iterations or 3
        strategies = strategies or ["grep", "ast", "test", "explore"]

        self.log(f"Iteratively verifying: {claim}")
        best_observation = None
        best_confidence = 0.0

        for strategy in strategies:
            self.log(f"  Strategy: {strategy}")

            for iteration in range(max_iter):
                obs = None

                if strategy == "grep":
                    # Extract searchable terms
                    terms = self._extract_search_terms(claim)
                    for term in terms[:3]:
                        results = self.grep(term, file_pattern="*.py")
                        if results.matches:
                            match = results.matches[0]
                            # Read context around match
                            file_data = self.read_file(
                                match['file'],
                                lines=(max(1, match['line'] - 5), match['line'] + 10)
                            )
                            if file_data.get('content'):
                                obs = Observation(
                                    claim=claim,
                                    verified=True,
                                    source=f"{match['file']}:{match['line']}",
                                    evidence=file_data['content'][:500],
                                    marker=f"[O: {match['file']}:{match['line']}]",
                                    confidence=0.7,
                                    method="grep",
                                )
                                break

                elif strategy == "ast":
                    # Try to find code elements mentioned in claim
                    code_names = re.findall(r'\b([A-Z][a-z]+[A-Z]\w*|\w+_\w+)\b', claim)
                    for name in code_names[:3]:
                        # Try as function
                        result = self.find_function_definition(name)
                        if result.matches:
                            m = result.matches[0]
                            obs = Observation(
                                claim=claim,
                                verified=True,
                                source=f"{m['file']}:{m['line']}",
                                evidence=f"Found function {name} at {m['file']}:{m['line']}",
                                marker=f"[O: {m['file']}:{m['line']}]",
                                confidence=0.8,
                                method="ast",
                            )
                            break

                        # Try as class
                        result = self.find_class_definition(name)
                        if result.matches:
                            m = result.matches[0]
                            obs = Observation(
                                claim=claim,
                                verified=True,
                                source=f"{m['file']}:{m['line']}",
                                evidence=f"Found class {name} at {m['file']}:{m['line']}",
                                marker=f"[O: {m['file']}:{m['line']}]",
                                confidence=0.8,
                                method="ast",
                            )
                            break

                elif strategy == "test":
                    # Generate test code if claim is about behavior
                    if any(word in claim.lower() for word in ["returns", "raises", "outputs", "produces", "equals"]):
                        test_code = self._generate_test_code(claim)
                        if test_code:
                            result = self.run_test(test_code)
                            obs = Observation(
                                claim=claim,
                                verified=result.passed,
                                source="test_execution",
                                evidence=f"Test {'passed' if result.passed else 'failed'}: {result.output[:200]}",
                                marker=f"[T: {'passed' if result.passed else 'failed'}]",
                                confidence=0.9 if result.passed else 0.1,
                                method="test",
                            )

                elif strategy == "explore":
                    # Use full LLM exploration
                    exploration = self.explore(f"Verify: {claim}", max_iterations=3)
                    if exploration.observations:
                        obs = exploration.observations[0]
                        obs.confidence = 0.6  # Lower confidence for LLM-derived

                if obs and obs.confidence > best_confidence:
                    best_observation = obs
                    best_confidence = obs.confidence

                if best_confidence >= 0.8:
                    break  # Good enough

            if best_confidence >= 0.8:
                break  # Good enough

        if best_observation:
            return best_observation

        return Observation(
            claim=claim,
            verified=False,
            source="iterative_verify",
            evidence="Could not verify after trying all strategies",
            marker="[UNVERIFIED: exhausted strategies]",
            confidence=0.0,
            method="iterative",
        )

    def _extract_search_terms(self, text: str) -> list[str]:
        """Extract searchable terms from text."""
        # Code patterns
        code_patterns = re.findall(r'`([^`]+)`|(\b[A-Z][a-z]+[A-Z]\w*\b)|(\b\w+_\w+\b)', text)
        terms = [p for group in code_patterns for p in group if p]

        # Also try quoted strings
        quoted = re.findall(r'"([^"]+)"|\'([^\']+)\'', text)
        terms.extend([p for group in quoted for p in group if p])

        # Significant words (>4 chars, not common)
        common = {'that', 'this', 'with', 'from', 'have', 'which', 'would', 'about', 'there'}
        words = [w for w in re.findall(r'\b\w{5,}\b', text.lower()) if w not in common]
        terms.extend(words[:3])

        return list(dict.fromkeys(terms))  # Dedupe while preserving order

    def _generate_test_code(self, claim: str) -> str | None:
        """Generate test code for a behavior claim."""
        # Simple pattern matching for common claim types
        # "X returns Y" -> assert X == Y
        match = re.search(r'(\w+)\s*\(\s*([^)]*)\s*\)\s+returns?\s+(\w+)', claim)
        if match:
            func, args, expected = match.groups()
            return f"result = {func}({args})\nassert result == {expected}, f'Expected {expected}, got {{result}}'"

        # "X equals Y"
        match = re.search(r'(\w+)\s*==?\s*(\w+)', claim)
        if match:
            left, right = match.groups()
            return f"assert {left} == {right}"

        return None

    # ========================================================================
    # POWER-UP 3: TEST EXECUTION
    # ========================================================================

    def run_test(self, test_code: str, timeout: int = 10, setup_code: str = "") -> TestResult:
        """
        Execute Python test code and return result.

        Args:
            test_code: Python code to execute
            timeout: Max execution time in seconds
            setup_code: Optional setup code (imports, etc.)

        Returns:
            TestResult with pass/fail status and output
        """
        import time

        self.log(f"Running test: {test_code[:50]}...")

        # Combine setup and test code
        full_code = f"""
import sys
sys.path.insert(0, '{self.root}')
{setup_code}
{test_code}
print("TEST_PASSED")
"""

        start = time.time()

        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write(full_code)
                f.flush()
                temp_path = f.name

            result = subprocess.run(
                [sys.executable, temp_path],
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=str(self.root),
            )

            duration_ms = int((time.time() - start) * 1000)

            passed = result.returncode == 0 and "TEST_PASSED" in result.stdout

            return TestResult(
                test_code=test_code,
                passed=passed,
                output=result.stdout[:1000],
                error=result.stderr[:500] if result.stderr else None,
                duration_ms=duration_ms,
            )

        except subprocess.TimeoutExpired:
            return TestResult(
                test_code=test_code,
                passed=False,
                output="",
                error=f"Test timed out after {timeout}s",
            )
        except Exception as e:
            return TestResult(
                test_code=test_code,
                passed=False,
                output="",
                error=str(e),
            )
        finally:
            try:
                os.unlink(temp_path)
            except:
                pass

    def verify_by_test(self, claim: str, test_code: str, setup_code: str = "") -> Observation:
        """
        Verify a claim by running test code.

        Args:
            claim: The claim being verified
            test_code: Python code that tests the claim
            setup_code: Optional setup (imports, etc.)

        Returns:
            Observation based on test result
        """
        result = self.run_test(test_code, setup_code=setup_code)

        return Observation(
            claim=claim,
            verified=result.passed,
            source="test_execution",
            evidence=f"Output: {result.output[:200]}" if result.passed else f"Error: {result.error or 'Test failed'}",
            marker=f"[T: {'passed' if result.passed else 'failed'}, {result.duration_ms}ms]",
            confidence=0.95 if result.passed else 0.05,
            method="test",
        )

    # ========================================================================
    # POWER-UP 4: AST/SEMANTIC UNDERSTANDING
    # ========================================================================

    def find_function_definition(self, function_name: str) -> ASTResult:
        """
        Find where a function is defined using AST parsing.

        Args:
            function_name: Name of function to find

        Returns:
            ASTResult with locations and context
        """
        result = ASTResult(query=function_name, query_type="function_def")

        for py_file in self.root.rglob("*.py"):
            try:
                content = py_file.read_text(encoding='utf-8')
                tree = ast.parse(content)

                for node in ast.walk(tree):
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        if node.name == function_name:
                            # Get function signature
                            args = [a.arg for a in node.args.args]
                            sig = f"{node.name}({', '.join(args)})"

                            # Get docstring
                            docstring = ast.get_docstring(node) or ""

                            result.matches.append({
                                "file": str(py_file.relative_to(self.root)),
                                "line": node.lineno,
                                "name": node.name,
                                "signature": sig,
                                "docstring": docstring[:200],
                                "is_async": isinstance(node, ast.AsyncFunctionDef),
                            })
            except (SyntaxError, UnicodeDecodeError):
                continue

        return result

    def find_class_definition(self, class_name: str) -> ASTResult:
        """
        Find where a class is defined using AST parsing.

        Args:
            class_name: Name of class to find

        Returns:
            ASTResult with locations and context
        """
        result = ASTResult(query=class_name, query_type="class_def")

        for py_file in self.root.rglob("*.py"):
            try:
                content = py_file.read_text(encoding='utf-8')
                tree = ast.parse(content)

                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        if node.name == class_name:
                            # Get base classes
                            bases = []
                            for base in node.bases:
                                if isinstance(base, ast.Name):
                                    bases.append(base.id)
                                elif isinstance(base, ast.Attribute):
                                    bases.append(f"{base.value.id if isinstance(base.value, ast.Name) else '?'}.{base.attr}")

                            # Get methods
                            methods = [n.name for n in node.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]

                            result.matches.append({
                                "file": str(py_file.relative_to(self.root)),
                                "line": node.lineno,
                                "name": node.name,
                                "bases": bases,
                                "methods": methods[:10],
                                "docstring": (ast.get_docstring(node) or "")[:200],
                            })
            except (SyntaxError, UnicodeDecodeError):
                continue

        return result

    def find_function_calls(self, function_name: str) -> ASTResult:
        """
        Find all places a function is called using AST parsing.

        Args:
            function_name: Name of function to find calls to

        Returns:
            ASTResult with call locations and context
        """
        result = ASTResult(query=function_name, query_type="function_call")

        for py_file in self.root.rglob("*.py"):
            try:
                content = py_file.read_text(encoding='utf-8')
                lines = content.split('\n')
                tree = ast.parse(content)

                for node in ast.walk(tree):
                    if isinstance(node, ast.Call):
                        # Direct call: func()
                        if isinstance(node.func, ast.Name) and node.func.id == function_name:
                            result.matches.append({
                                "file": str(py_file.relative_to(self.root)),
                                "line": node.lineno,
                                "name": function_name,
                                "context": lines[node.lineno - 1].strip() if node.lineno <= len(lines) else "",
                                "call_type": "direct",
                            })

                        # Method call: obj.func()
                        elif isinstance(node.func, ast.Attribute) and node.func.attr == function_name:
                            result.matches.append({
                                "file": str(py_file.relative_to(self.root)),
                                "line": node.lineno,
                                "name": function_name,
                                "context": lines[node.lineno - 1].strip() if node.lineno <= len(lines) else "",
                                "call_type": "method",
                            })
            except (SyntaxError, UnicodeDecodeError):
                continue

        return result

    def find_imports(self, module_name: str) -> ASTResult:
        """Find where a module is imported."""
        result = ASTResult(query=module_name, query_type="import")

        for py_file in self.root.rglob("*.py"):
            try:
                content = py_file.read_text(encoding='utf-8')
                tree = ast.parse(content)

                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            if alias.name == module_name or alias.name.startswith(f"{module_name}."):
                                result.matches.append({
                                    "file": str(py_file.relative_to(self.root)),
                                    "line": node.lineno,
                                    "name": alias.name,
                                    "alias": alias.asname,
                                    "type": "import",
                                })

                    elif isinstance(node, ast.ImportFrom):
                        if node.module == module_name or (node.module and node.module.startswith(f"{module_name}.")):
                            names = [a.name for a in node.names]
                            result.matches.append({
                                "file": str(py_file.relative_to(self.root)),
                                "line": node.lineno,
                                "name": node.module,
                                "imports": names,
                                "type": "from_import",
                            })
            except (SyntaxError, UnicodeDecodeError):
                continue

        return result

    def get_file_structure(self, filepath: str) -> dict[str, Any]:
        """Get the structure of a Python file (classes, functions, imports)."""
        path = self._resolve_path(filepath)

        if not path.exists():
            return {"error": f"File not found: {path}"}

        try:
            content = path.read_text(encoding='utf-8')
            tree = ast.parse(content)

            structure = {
                "file": str(filepath),
                "imports": [],
                "classes": [],
                "functions": [],
                "globals": [],
            }

            for node in ast.iter_child_nodes(tree):
                if isinstance(node, ast.Import):
                    structure["imports"].extend([a.name for a in node.names])

                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ""
                    for alias in node.names:
                        structure["imports"].append(f"{module}.{alias.name}")

                elif isinstance(node, ast.ClassDef):
                    methods = [n.name for n in node.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
                    structure["classes"].append({
                        "name": node.name,
                        "line": node.lineno,
                        "methods": methods,
                    })

                elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    args = [a.arg for a in node.args.args]
                    structure["functions"].append({
                        "name": node.name,
                        "line": node.lineno,
                        "args": args,
                    })

                elif isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            structure["globals"].append({
                                "name": target.id,
                                "line": node.lineno,
                            })

            return structure

        except SyntaxError as e:
            return {"error": f"Syntax error: {e}"}

    # ========================================================================
    # CORE OBSERVATION METHODS (kept from original)
    # ========================================================================

    def read_file(self, filepath: str | Path, lines: tuple[int, int] | None = None) -> dict[str, Any]:
        """Read a file and return contents with line numbers."""
        path = self._resolve_path(filepath)

        if not path.exists():
            return {"error": f"File not found: {path}", "exists": False}

        try:
            content = path.read_text(encoding='utf-8')
            all_lines = content.split('\n')

            if lines:
                start, end = lines
                start = max(1, start)
                end = min(len(all_lines), end)
                selected_lines = all_lines[start-1:end]
                line_numbers = list(range(start, start + len(selected_lines)))
            else:
                selected_lines = all_lines
                line_numbers = list(range(1, len(all_lines) + 1))

            return {
                "exists": True,
                "path": str(path),
                "content": '\n'.join(selected_lines),
                "lines": list(zip(line_numbers, selected_lines)),
                "total_lines": len(all_lines),
                "range": lines,
            }
        except Exception as e:
            return {"error": str(e), "exists": True, "path": str(path)}

    def grep(
        self,
        pattern: str,
        path: str | Path | None = None,
        file_pattern: str = "*",
        max_results: int = 100,
    ) -> SearchResult:
        """Search for pattern in codebase using grep/ripgrep."""
        search_path = self._resolve_path(path) if path else self.root
        result = SearchResult(query=pattern)

        try:
            cmd = [
                "rg", "--json", "-e", pattern,
                "--glob", file_pattern,
                "-m", str(max_results),
                str(search_path)
            ]
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

            for line in proc.stdout.strip().split('\n'):
                if not line:
                    continue
                try:
                    data = json.loads(line)
                    if data.get('type') == 'match':
                        match_data = data.get('data', {})
                        filepath = match_data.get('path', {}).get('text', '')
                        line_num = match_data.get('line_number', 0)
                        line_text = match_data.get('lines', {}).get('text', '').strip()

                        result.matches.append({
                            'file': filepath,
                            'line': line_num,
                            'text': line_text,
                        })
                        if filepath not in result.files:
                            result.files.append(filepath)
                except json.JSONDecodeError:
                    continue

        except FileNotFoundError:
            # Fall back to grep
            cmd = ["grep", "-rn", "-E", pattern, "--include", file_pattern, str(search_path)]
            try:
                proc = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                for line in proc.stdout.strip().split('\n')[:max_results]:
                    if ':' in line:
                        parts = line.split(':', 2)
                        if len(parts) >= 3:
                            filepath, line_num, text = parts[0], parts[1], parts[2]
                            result.matches.append({
                                'file': filepath,
                                'line': int(line_num) if line_num.isdigit() else 0,
                                'text': text.strip(),
                            })
                            if filepath not in result.files:
                                result.files.append(filepath)
            except subprocess.TimeoutExpired:
                pass
        except subprocess.TimeoutExpired:
            self.log("Search timed out")

        result.total_matches = len(result.matches)
        return result

    def glob_files(self, pattern: str, path: str | Path | None = None) -> list[str]:
        """Find files matching glob pattern."""
        search_path = self._resolve_path(path) if path else self.root
        return [str(p.relative_to(self.root)) for p in search_path.rglob(pattern)]

    def verify_claim(
        self,
        claim: str,
        source: str | None = None,
        search_pattern: str | None = None,
    ) -> Observation:
        """Verify a claim against actual source code."""
        self.log(f"Verifying: {claim}")

        if source:
            if ':' in source:
                filepath, line_spec = source.rsplit(':', 1)
                if '-' in line_spec:
                    start, end = map(int, line_spec.split('-'))
                    lines = (start, end)
                elif line_spec.isdigit():
                    line_num = int(line_spec)
                    lines = (max(1, line_num - 5), line_num + 5)
                else:
                    filepath = source
                    lines = None
            else:
                filepath = source
                lines = None

            file_data = self.read_file(filepath, lines)

            if file_data.get('error'):
                return Observation(
                    claim=claim,
                    verified=False,
                    source=source,
                    evidence=f"Could not read: {file_data['error']}",
                    marker="[UNVERIFIED: source not accessible]",
                    confidence=0.0,
                )

            content = file_data.get('content', '')
            claim_words = [w.lower() for w in claim.split() if len(w) > 3]
            matches = sum(1 for w in claim_words if w in content.lower())
            confidence = matches / len(claim_words) if claim_words else 0

            if confidence > 0.3:
                return Observation(
                    claim=claim,
                    verified=True,
                    source=f"{filepath}:{lines[0] if lines else 1}",
                    evidence=content[:500] + ("..." if len(content) > 500 else ""),
                    marker=f"[O: {filepath}:{lines[0] if lines else 'full'}]",
                    confidence=confidence,
                )
            else:
                return Observation(
                    claim=claim,
                    verified=False,
                    source=source,
                    evidence=f"Content doesn't support claim (confidence: {confidence:.2f})",
                    marker="[UNVERIFIED: evidence insufficient]",
                    confidence=confidence,
                )

        if search_pattern:
            results = self.grep(search_pattern)
            if results.matches:
                best_match = results.matches[0]
                return Observation(
                    claim=claim,
                    verified=True,
                    source=f"{best_match['file']}:{best_match['line']}",
                    evidence=best_match['text'],
                    marker=f"[O: {best_match['file']}:{best_match['line']}]",
                    confidence=0.8,
                )

        # Try iterative verification for better results
        return self.iterative_verify(claim, max_iterations=2, strategies=["grep", "ast"])

    def _resolve_path(self, filepath: str | Path) -> Path:
        """Resolve path relative to root."""
        path = Path(filepath)
        if path.is_absolute():
            return path
        return self.root / path


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='GOSM Agent - Powerful observation and verification',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Explore a topic (tool-assisted LLM)
    python gosm_agent.py --explore "How does error handling work?"

    # Verify a claim iteratively
    python gosm_agent.py --verify "The GOSMAgent class uses AST parsing"

    # Run a test to verify behavior
    python gosm_agent.py --test "assert 1 + 1 == 2"

    # Find function definition (AST)
    python gosm_agent.py --find-function "explore_araw"

    # Find all calls to a function
    python gosm_agent.py --find-calls "verify_claim"

    # Get file structure
    python gosm_agent.py --structure "scripts/gosm_agent.py"
        """
    )

    parser.add_argument('--root', default='.', help='Root path for searches')
    parser.add_argument('--explore', help='Explore a topic using tool-assisted LLM')
    parser.add_argument('--verify', help='Verify a claim iteratively')
    parser.add_argument('--test', help='Run test code')
    parser.add_argument('--search', help='Search pattern (grep)')
    parser.add_argument('--find-function', help='Find function definition (AST)')
    parser.add_argument('--find-class', help='Find class definition (AST)')
    parser.add_argument('--find-calls', help='Find function calls (AST)')
    parser.add_argument('--find-imports', help='Find module imports (AST)')
    parser.add_argument('--structure', help='Get file structure (AST)')
    parser.add_argument('--read', help='Read a file')
    parser.add_argument('--lines', help='Line range for read (e.g., 10-20)')
    parser.add_argument('--glob', help='Find files matching pattern')
    parser.add_argument('--max-iterations', type=int, default=10, help='Max iterations for exploration')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

    args = parser.parse_args()
    agent = GOSMAgent(
        root_path=args.root,
        verbose=args.verbose,
        max_iterations=args.max_iterations,
    )

    result = None

    if args.explore:
        exploration = agent.explore(args.explore)
        result = {
            'task': exploration.task,
            'iterations': exploration.iterations,
            'satisfied': exploration.satisfied,
            'observations': [
                {'claim': o.claim, 'verified': o.verified, 'source': o.source, 'marker': o.marker}
                for o in exploration.observations
            ],
            'files_examined': exploration.files_examined,
            'summary': exploration.summary,
        }

    elif args.verify:
        obs = agent.iterative_verify(args.verify)
        result = {
            'claim': obs.claim,
            'verified': obs.verified,
            'source': obs.source,
            'evidence': obs.evidence,
            'marker': obs.marker,
            'confidence': obs.confidence,
            'method': obs.method,
        }

    elif args.test:
        test_result = agent.run_test(args.test)
        result = {
            'test_code': test_result.test_code,
            'passed': test_result.passed,
            'output': test_result.output,
            'error': test_result.error,
            'duration_ms': test_result.duration_ms,
        }

    elif args.search:
        search_result = agent.grep(args.search)
        result = {
            'query': search_result.query,
            'total_matches': search_result.total_matches,
            'files': search_result.files,
            'matches': search_result.matches[:20],
        }

    elif args.find_function:
        ast_result = agent.find_function_definition(args.find_function)
        result = {
            'query': ast_result.query,
            'type': ast_result.query_type,
            'matches': ast_result.matches,
        }

    elif args.find_class:
        ast_result = agent.find_class_definition(args.find_class)
        result = {
            'query': ast_result.query,
            'type': ast_result.query_type,
            'matches': ast_result.matches,
        }

    elif args.find_calls:
        ast_result = agent.find_function_calls(args.find_calls)
        result = {
            'query': ast_result.query,
            'type': ast_result.query_type,
            'matches': ast_result.matches[:30],
        }

    elif args.find_imports:
        ast_result = agent.find_imports(args.find_imports)
        result = {
            'query': ast_result.query,
            'type': ast_result.query_type,
            'matches': ast_result.matches,
        }

    elif args.structure:
        result = agent.get_file_structure(args.structure)

    elif args.read:
        lines = None
        if args.lines:
            parts = args.lines.split('-')
            lines = (int(parts[0]), int(parts[1]))
        result = agent.read_file(args.read, lines=lines)

    elif args.glob:
        files = agent.glob_files(args.glob)
        result = {'pattern': args.glob, 'files': files}

    else:
        parser.print_help()
        sys.exit(1)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        if isinstance(result, dict):
            for k, v in result.items():
                if isinstance(v, list) and len(v) > 10:
                    print(f"{k}: [{len(v)} items]")
                    for item in v[:5]:
                        if isinstance(item, dict):
                            print(f"  - {item.get('file', item.get('name', item))}:{item.get('line', '')}")
                        else:
                            print(f"  - {item}")
                    print(f"  ... and {len(v) - 5} more")
                elif isinstance(v, str) and len(v) > 500:
                    print(f"{k}: {v[:500]}...")
                else:
                    print(f"{k}: {v}")
        else:
            print(result)


if __name__ == '__main__':
    main()

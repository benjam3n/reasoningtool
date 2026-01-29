# GOSM Runners

High-level execution engines that combine ARAW verification with AI context loading, structured procedures, and tool-assisted observation.

## Architecture

```
User Goal / Claim
    │
    ▼
gosm_runner.py
    │  Loads AI context (failure knowledge, user model, relevance weighting)
    │  Structures prompts for system intelligence
    │  Applies ARAW verification
    │
    ▼
gosm_agent.py
    │  Reads files before making claims
    │  Iterates until verified or max iterations
    │  Executes tests to verify behavior
    │  Parses AST for semantic code understanding
    │
    ▼
Verified Output
```

---

## gosm_runner.py — Goal processing engine

Processes goals using the GOSM methodology: loads AI context files (failure knowledge, user model, relevance weighting, mission statement, domain vocabulary), applies ARAW verification, and follows structured gates and checklists.

### Usage

```bash
# Process a goal
python gosm_runner.py --goal "Analyze feasibility of starting a podcast"

# Resume an existing project
python gosm_runner.py --project my-podcast --resume

# Verify existing output
python gosm_runner.py --verify /path/to/output.md

# Specify ARAW depth
python gosm_runner.py --goal "Should I learn Rust?" --depth 4
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `--goal "text"` | Goal to process | — |
| `--project NAME` | Project name for saving/resuming | — |
| `--resume` | Continue from previous state | — |
| `--verify FILE` | Verify an existing output file | — |
| `--depth N` | ARAW depth (1-8) | 2 |
| `--model MODEL` | LLM model to use | — |
| `--output FILE` | Output file path | — |

### AI context files

The runner looks for these context files in the project directory:

| File | Purpose |
|------|---------|
| `FAILURE_KNOWLEDGE` | Known failure patterns to avoid |
| `USER_MODEL` | User preferences and context |
| `RELEVANCE_WEIGHTING` | Priority ordering for relevance |
| `SYSTEM_ARCHITECTURE` | System design context |
| `MISSION_STATEMENT` | Core philosophy and goals |
| `DOMAIN_VOCABULARY` | Domain-specific terminology |

### Output format

```markdown
# Goal Analysis: [Your Goal]

## Summary
[High-level findings]

## ARAW Exploration
### ASSUME RIGHT
- [What follows if the goal is correct]

### ASSUME WRONG
- [Alternatives and considerations]

## Recommendations
1. [Actionable next steps]

## Verification
- [O] Observed: [directly seen facts]
- [T] Tested: [verified through testing]
- [D] Derived: [logically follows from O/T]
```

### Programmatic usage

```python
from gosm_runner import GOSMRunner

runner = GOSMRunner(
    goal="Should I learn a new programming language?",
    depth=4,
    model="gpt-4"
)
result = runner.run()
print(result.summary)
print(result.recommendations)
```

---

## gosm_agent.py — Tool-assisted verification agent

More powerful than `gosm_runner` for tasks that require observation before claiming. Reads files, searches code, executes tests, and parses ASTs before making any claims.

### Usage

```bash
# Explore a question with tool assistance
python gosm_agent.py --explore "How does error handling work in this codebase?"

# Verify a claim iteratively
python gosm_agent.py --verify "The ARAW engine uses SQLite" --max-iterations 5

# Verify by running actual tests
python gosm_agent.py --test-verify "add(1, 2) returns 3" --test-code "assert add(1,2) == 3"

# Find code patterns
python gosm_agent.py --find-calls "explore_araw"
python gosm_agent.py --find-classes "GOSMAgent"
```

### Capabilities

| Capability | What it does |
|-----------|--------------|
| **Tool-assisted LLM** | Reads files and searches code before making claims |
| **Iterative loop** | Refines observations until verified or max iterations reached |
| **Test execution** | Actually runs code to verify behavior claims |
| **AST analysis** | Parses Python code structure — finds function calls, class definitions, imports |

### Programmatic usage

```python
from gosm_agent import GOSMAgent

agent = GOSMAgent()

# Explore with tool assistance
result = agent.explore("How does the ARAW engine handle branching?")

# Verify iteratively
verified = agent.iterative_verify(
    claim="The database uses SQLite",
    max_iterations=5
)

# Find code patterns
calls = agent.find_function_calls("create_search")
classes = agent.find_class_definitions("ARAWEngine")

# Verify by running a test
result = agent.verify_by_test(
    claim="add(1, 2) returns 3",
    test_code="assert add(1, 2) == 3"
)
```

---

## API configuration

```bash
# Environment variables
export OPENAI_API_KEY="sk-your-key"
export ANTHROPIC_API_KEY="sk-ant-your-key"

# Or config file
mkdir -p ~/.config/gosm
echo "sk-your-key" > ~/.config/gosm/openai_api_key
```

Both runners also accept `--api-key` on the command line.

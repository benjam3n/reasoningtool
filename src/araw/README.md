# ARAW Engine

SQLite-based recursive exploration engine for Assume Right / Assume Wrong analysis. Seed any claim, branch it into "what if true?" and "what if false?", recurse until you hit foundations or contradictions, then visualize and synthesize the results.

## Quick start

```bash
# Set API key
export OPENAI_API_KEY="sk-your-key"

# Start new exploration
python auto_expand_llm.py --db my_analysis.db --seed "Should I start a business?"

# Continue expanding
python auto_expand_llm.py --db my_analysis.db --continue --parallel 3

# View in browser
python visualize.py --db my_analysis.db --serve
# Open http://localhost:8080
```

---

## Files

### Core engine

#### `araw_engine.py` — Core ARAW engine

The foundation that everything else builds on. Manages SQLite storage, node creation, branching, querying, and export. Used as a library by other scripts and as a standalone CLI.

**CLI usage:**
```bash
python araw_engine.py create "I need to change careers" my_search.db
python araw_engine.py stats my_search.db
python araw_engine.py export my_search.db
python araw_engine.py unexplored my_search.db
```

**Commands:**
- `create <claim> [db_path]` — Create a new search with root claim
- `stats [db_path]` — Print node counts, depth, branch type distribution
- `export [db_path]` — Export full tree as JSON to stdout
- `unexplored [db_path]` — List top 20 unexplored nodes with leverage scores

**As a library:**
```python
from araw_engine import ARAWEngine, BranchType

engine = ARAWEngine("my_analysis.db")

# Create search
root_id = engine.create_search("I need to find a new job")

# Branch a claim
result = engine.branch(
    root_id,
    assume_right_claim="Start job search immediately",
    assume_wrong_claim="First understand why current job isn't working",
    alternatives=["Consider internal transfer", "Take time off before deciding"],
    leverage_score=0.8
)

# Get unexplored nodes with different strategies
nodes = engine.get_unexplored(max_depth=5, strategy="leverage_first")
# Strategies: "leverage_first", "depth_first", "breadth_first",
#             "frontier", "balanced" (default), "random"

# Mixed strategy (diversity from multiple strategies)
nodes = engine.get_unexplored_mixed(limit=20)

# Query
high_leverage = engine.get_high_leverage(min_score=0.7)
path = engine.get_path_to_root(node_id)
children = engine.get_children(node_id)
stats = engine.get_stats()

# Export
tree = engine.export_tree()          # Nested dict
flat = engine.export_flat()          # Flat list
engine.export_json("output.json")    # To file
```

**Database tables:**
- `nodes` — All claims with parent/child relationships, branch types, leverage scores, status, and JSON metadata
- `alternatives` — Alternatives discovered during ASSUME WRONG branches
- `metadata` — Search-level metadata (root ID, initial claim, creation time)

#### `auto_expand_llm.py` — LLM-powered tree expansion

The main tool for running ARAW explorations. Sends each unexplored claim to an LLM which generates meaningful ASSUME RIGHT / ASSUME WRONG branches with leverage scores, crux detection, and domain classification.

```bash
# Start new exploration
python auto_expand_llm.py --db career.db --seed "I should quit my job"

# Continue from where you left off
python auto_expand_llm.py --db career.db --continue

# Parallel expansion (faster, more API calls)
python auto_expand_llm.py --db career.db --continue --parallel 5

# Limit depth
python auto_expand_llm.py --db career.db --continue --max-depth 6

# Use different model
python auto_expand_llm.py --db career.db --continue --model gpt-4-turbo
```

**Options:**
| Flag | Description | Default |
|------|-------------|---------|
| `--db FILE` | SQLite database path | (required) |
| `--seed "claim"` | Starting claim for new exploration | — |
| `--continue` | Continue expanding unexplored nodes | — |
| `--parallel N` | Number of parallel expansions | 1 |
| `--max-depth N` | Maximum tree depth | 10 |
| `--model MODEL` | OpenAI model name | gpt-5-nano |
| `--api-key KEY` | API key (overrides env/config) | — |

**Features:**
- Relevancy gate: detects and prunes drifting claims (abstract/vague) in favor of concrete ones
- Domain detection: classifies claims into 18 domains (human, institutional, evidential, epistemological, practical, relational, ethical, temporal, cultural, environmental, technological, geopolitical, existential, demographic, biological, economic, informational, systemic)
- Leverage scoring: LLM assigns 0.0-1.0 leverage to each claim
- Crux detection: marks claims where being wrong changes everything

#### `auto_expand.py` — Rule-based tree expansion (no API needed)

Pattern-based expansion that doesn't require an API key. Uses keyword matching to generate ASSUME WRONG alternatives (e.g., claims containing "need" get alternatives like "might not actually need this", "need has been misidentified"). Useful for quick prototyping or when API access isn't available.

```bash
python auto_expand.py --db quick.db --seed "I must learn to code" --duration 60
python auto_expand.py --db quick.db --nodes 1000
```

**Options:**
| Flag | Description | Default |
|------|-------------|---------|
| `--db FILE` | SQLite database path | araw_search.db |
| `--seed "claim"` | Starting claim | — |
| `--duration SECS` | Run for N seconds | — |
| `--nodes N` | Generate N nodes then stop | — |

---

### Visualization and export

#### `visualize.py` — Interactive HTML viewer and graph export

Serves a full interactive visualization of ARAW trees in the browser, or exports to JSON/GEXF for use with external graph tools.

**Serve the interactive viewer:**
```bash
python visualize.py --db my.db --serve
python visualize.py --db my.db --serve --port 9090
```

Opens an interactive single-page app at `http://localhost:8080` with:

- **Graph display**: Nodes rendered with Sigma.js, edges colored blue (assume right) or red (assume wrong)
- **Node colors**: orange = root, blue = assume right, red = assume wrong, gold = crux, green = grounded, purple = epistemic limit, cyan = grounding assumption
- **Node sizing**: based on leverage score and number of children
- **Sidebar filters**:
  - Branch type dropdown (all / assume right / assume wrong)
  - Depth slider (1-20)
  - Grounded-only checkbox
  - Crux-only checkbox
  - Domain multi-select (18 domains)
  - Text search across all claims
- **Click any node** to see: full claim text, depth, leverage score, children count, branch type, grounded status, crux status, domain
- **Top-right controls**: load at different depths (5/10/20/50/all), reset camera, re-layout (force-directed), export PNG
- **Statistics panel**: total nodes, visible nodes, max depth, grounded count, crux count

**Export to file:**
```bash
# JSON for D3.js / Sigma.js
python visualize.py --db my.db --export graph.json

# GEXF for Gephi
python visualize.py --db my.db --export graph.gexf --format gexf

# Filter exports
python visualize.py --db my.db --export graph.json --max-depth 4
python visualize.py --db my.db --export graph.json --min-leverage 0.5
```

**Options:**
| Flag | Description | Default |
|------|-------------|---------|
| `--db FILE` | SQLite database path | (required) |
| `--serve` | Start HTTP visualization server | — |
| `--port N` | Server port | 8080 |
| `--export FILE` | Export to file | — |
| `--format FORMAT` | Export format: `json` or `gexf` | json |
| `--max-depth N` | Maximum depth to include | all |
| `--min-leverage F` | Minimum leverage score to include | 0.0 |

---

### Analysis tools

#### `synthesize.py` — Cross-database synthesis

Analyzes multiple ARAW databases to find common themes, extract actionable items, and detect contradictions. Use this after running multiple explorations to find patterns across runs.

```bash
# Full synthesis of all databases
python synthesize.py *.db

# Extract actionable items (HIGH impact + LOW effort)
python synthesize.py *.db --extract-actions actions.json

# Find contradictions between databases
python synthesize.py *.db --find-tensions

# Show only cross-database themes
python synthesize.py *.db --themes-only
```

**Options:**
| Flag | Description |
|------|-------------|
| `databases` | One or more .db files (positional) |
| `--extract-actions FILE` | Export actions to JSON |
| `--find-tensions` | Show contradictions between databases |
| `--themes-only` | Only show cross-database themes |

**Output includes:**
- Per-database summary: root claim, node count, depth, status breakdown
- Actionable items: DO_FIRST (low effort + high impact), DO_SECOND (high impact crux nodes)
- Cross-database themes: keywords appearing in 2+ databases with sample claims
- Tensions: contradictions detected via opposing keyword pairs
- Frontier: highest-leverage unexplored nodes

#### `synthesis.py` — LLM-powered query engine

Ask natural language questions about an ARAW tree and get LLM-synthesized answers grounded in the tree's data.

```bash
python synthesis.py --db my.db "What are the key cruxes?"
python synthesis.py --db my.db "If institutions can self-correct, what follows?"
python synthesis.py --db my.db "Where do different branches converge?"
```

**Options:**
| Flag | Description | Default |
|------|-------------|---------|
| `--db FILE` | SQLite database path | (required) |
| `query` | Natural language question (positional) | (required) |
| `--model MODEL` | OpenAI model | gpt-5-nano |
| `--api-key KEY` | API key | — |

#### `commitment_analyzer.py` — Classify claims as foundational or guesses

Analyzes an ARAW tree to determine which claims can be committed to (FOUNDATIONAL — questioning becomes circular) vs. which are still guesses (coherent alternatives exist).

```bash
python commitment_analyzer.py --db my.db analyze      # Full analysis
python commitment_analyzer.py --db my.db foundations   # List foundational claims only
python commitment_analyzer.py --db my.db guesses       # List guesses only
python commitment_analyzer.py --db my.db check "specific claim text"
```

#### `analyze_strategies.py` — Queue strategy effectiveness

Analyzes which queue strategies (leverage_first, depth_first, breadth_first, frontier, random, balanced) produced the best nodes in a given database. Useful for tuning expansion parameters.

```bash
python analyze_strategies.py my.db
```

#### `grounding.py` — Evidence grounding engine

Connects abstract claims to real-world evidence with epistemic quality tracking. Prioritizes nodes by upstream influence, convergence, and decision-relevance. Detects contradictions between sources and checks falsifiability.

```bash
python grounding.py --db my.db --prioritize          # Show best nodes to ground
python grounding.py --db my.db --ground-top 10       # Ground top 10 priority nodes
python grounding.py --db my.db --node <id>           # Ground specific node
python grounding.py --db my.db --integrate           # Create ARAW branches from assumptions
```

**Options:**
| Flag | Description |
|------|-------------|
| `--db FILE` | SQLite database path |
| `--prioritize` | Show highest-priority ungrounded nodes |
| `--ground-top N` | Ground top N priority nodes via LLM |
| `--node ID` | Ground a specific node |
| `--integrate` | Create new ARAW branches from discovered assumptions |
| `--model MODEL` | OpenAI model (default: gpt-5-nano) |
| `--api-key KEY` | API key |

**Evidence quality tiers:** tracks epistemic weight of each source (direct observation vs. expert opinion vs. anecdote).

#### `evidence_engine.py` — Tiered source cascade

Systematic evidence gathering using a tiered source cascade (Intelligence Fusion model). Tries progressively broader sources to cross-validate evidence for a claim.

```bash
python evidence_engine.py --db my.db --claim "Global poverty is declining"
python evidence_engine.py --db my.db --ground-node <node_id>
python evidence_engine.py --db my.db --test-sources
```

---

### Conversion and bridging

#### `md_to_sqlite.py` — Markdown to SQLite converter

Converts conversational ARAW sessions (saved as markdown) into SQLite format for use with synthesize.py and other tools.

```bash
python md_to_sqlite.py session.md                # Creates session.db
python md_to_sqlite.py session.md -o output.db   # Custom output name
python md_to_sqlite.py sessions/*.md -o all.db   # Merge multiple sessions
```

#### `bridge_to_gosm.py` — ARAW to GOSM export

Exports ARAW findings in GOSM-compatible YAML format for integration with the GOSM runner pipeline. Extracts crux nodes, high-impact items, and assumptions that need verification.

```bash
python bridge_to_gosm.py database.db --output assumptions.yaml
python bridge_to_gosm.py *.db --synthesize --output combined.yaml
```

#### `context_loader.py` — External context injection

Loads external context into ARAW sessions at startup. Two use cases:
1. **Library seeding**: inject relevant claims from existing guess libraries
2. **Resumable sessions**: inject a summary of a previous ARAW session

Used as a library by `auto_expand_llm.py` and `resumable_protocol.py`.

#### `resumable_protocol.py` — Multi-session deep ARAW

Enables 16x+ and 32x depth ARAW by chunking sessions across multiple runs. Tracks exploration frontiers, committed claims, and open questions across sessions.

**Protocol:**
1. PAUSE: save state with summary, frontiers, commitments
2. RESUME: load summary, inject frontier nodes, continue expansion
3. MERGE: combine multiple session trees into unified view

Used as a library by `auto_expand_llm.py`.

#### `goal_journey_mapper.py` — Goal journey extraction

Extracts Goal Journey structure from completed ARAW sessions — maps claims to current state, desired state, immediate goals, success criteria, and constraints.

#### `example_surgery.py` — Worked example

Demonstrates the ARAW engine API with a concrete example: "I need $50k in 6 months for mom's surgery." Shows how to create a search, add branches, and set leverage scores programmatically.

```bash
python example_surgery.py
# Creates surgery_example.db with a multi-level ARAW tree
```

---

## API configuration

Scripts that call an LLM look for API keys in this order:

1. **Command-line**: `--api-key "sk-..."`
2. **Environment variable**: `OPENAI_API_KEY`
3. **Config file**: `~/.config/gosm/openai_api_key` (first line)

```bash
# Environment variable
export OPENAI_API_KEY="sk-your-key"

# Config file
mkdir -p ~/.config/gosm
echo "sk-your-key" > ~/.config/gosm/openai_api_key
```

---

## Database schema

```sql
CREATE TABLE nodes (
    id TEXT PRIMARY KEY,
    parent_id TEXT,           -- NULL for root
    claim TEXT,               -- The claim being explored
    branch_type TEXT,         -- 'root', 'assume_right', 'assume_wrong'
    status TEXT,              -- 'unexplored', 'exploring', 'explored', 'pruned'
    depth INTEGER,            -- Distance from root
    leverage_score REAL,      -- 0.0-1.0, higher = more important
    content JSON,             -- Metadata (see below)
    created_at TEXT,
    explored_at TEXT
);

CREATE TABLE alternatives (
    id TEXT PRIMARY KEY,
    node_id TEXT,             -- Parent node
    alternative TEXT,         -- Alternative claim text
    explored BOOLEAN,
    created_at TEXT
);

CREATE TABLE metadata (
    key TEXT PRIMARY KEY,     -- 'root_id', 'initial_claim', 'created_at'
    value JSON
);
```

**`content` JSON fields** (varies by node):
- `is_crux` (bool) — True if being wrong about this changes everything
- `effort_to_address` — "LOW", "MEDIUM", or "HIGH"
- `potential_impact` — "LOW", "MEDIUM", or "HIGH"
- `direct_path` (bool) — Whether this is on the direct path to the goal
- `domain` — Detected domain category
- `parent_claim` — Text of parent claim
- `alternatives` — List of alternative claims (for assume_wrong branches)
- `grounding_assumption` (bool) — Whether this is a grounding assumption
- `assumption_type` — e.g., "epistemic_limit"

### Useful queries

```bash
# High-leverage unexplored nodes
sqlite3 my.db "SELECT claim, leverage_score FROM nodes WHERE status='unexplored' ORDER BY leverage_score DESC LIMIT 10"

# Crux nodes (decision points)
sqlite3 my.db "SELECT claim FROM nodes WHERE json_extract(content, '$.is_crux') = 1"

# Tree statistics
sqlite3 my.db "SELECT COUNT(*) as total, SUM(CASE WHEN status='explored' THEN 1 ELSE 0 END) as explored, MAX(depth) as max_depth FROM nodes"

# Nodes by depth
sqlite3 my.db "SELECT depth, COUNT(*) FROM nodes GROUP BY depth ORDER BY depth"

# Export to CSV
sqlite3 -header -csv my.db "SELECT * FROM nodes" > nodes.csv
```

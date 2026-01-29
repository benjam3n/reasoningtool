# Source Code

Python tools for running ARAW explorations programmatically — seed a claim, expand it with LLM-powered branching, visualize the results in an interactive HTML viewer, and synthesize findings across multiple runs.

## What you can do

- **Explore a claim recursively**: Seed any claim ("Should I change careers?") and auto-expand it into an ARAW tree where every claim is branched into ASSUME RIGHT / ASSUME WRONG
- **Visualize results in the browser**: Launch an interactive graph viewer (Sigma.js) that color-codes nodes by type, lets you filter by branch type / depth / domain, and click nodes for details
- **Export for external tools**: Export trees as JSON (for D3.js/Sigma.js) or GEXF (for Gephi)
- **Synthesize across runs**: Analyze multiple ARAW databases to find common themes, contradictions, and actionable items
- **Ground claims in evidence**: Connect abstract claims to real-world sources with epistemic quality tracking
- **Process goals**: Run the full GOSM pipeline — load context, apply ARAW verification, produce verified output

## Directory structure

```
src/
├── araw/                  # ARAW engine and analysis tools
│   ├── araw_engine.py     # Core SQLite engine (library + CLI)
│   ├── auto_expand_llm.py # LLM-powered tree expansion
│   ├── auto_expand.py     # Rule-based tree expansion (no API needed)
│   ├── visualize.py       # Interactive HTML viewer + JSON/GEXF export
│   ├── synthesize.py      # Cross-database synthesis and action extraction
│   ├── synthesis.py       # LLM-powered query engine over ARAW trees
│   ├── grounding.py       # Evidence grounding with epistemic quality tiers
│   ├── evidence_engine.py # Tiered source cascade for evidence gathering
│   ├── commitment_analyzer.py # Classify claims as foundational vs. guesses
│   ├── analyze_strategies.py  # Evaluate which queue strategies found best nodes
│   ├── bridge_to_gosm.py     # Export findings in GOSM-compatible YAML
│   ├── md_to_sqlite.py       # Convert markdown ARAW sessions to SQLite
│   ├── context_loader.py     # Inject external context into ARAW sessions
│   ├── resumable_protocol.py # Multi-session support for deep (16x+) runs
│   ├── goal_journey_mapper.py # Extract goal journey fields from ARAW trees
│   ├── example_surgery.py    # Worked example: "$50k for surgery"
│   └── __init__.py
├── runners/               # High-level GOSM execution
│   ├── gosm_runner.py     # Goal processing with AI context + ARAW
│   └── gosm_agent.py      # Tool-assisted verification agent
└── utilities/             # Library management scripts
    ├── consolidate_library.py          # Cluster and stratify procedures
    ├── convert_procedures_to_skills.py # YAML procedures → Claude Code skills
    ├── update_procedure_registry.py    # Scan and update procedure registry
    ├── audit_procedure_library_health.py # Check for duplicates, broken links
    └── sync_skills_to_claude.sh        # Symlink skills into Claude Code
```

## Quick start

### 1. Install dependencies

```bash
pip install openai pyyaml
```

Only `openai` and `pyyaml` are required. The ARAW engine itself uses only the Python standard library (sqlite3, json, argparse).

### 2. Set up API key

```bash
# Option A: Environment variable
export OPENAI_API_KEY="sk-your-key"

# Option B: Config file
mkdir -p ~/.config/gosm
echo "sk-your-key" > ~/.config/gosm/openai_api_key
```

### 3. Run an exploration

```bash
cd src/araw

# Start a new ARAW tree
python auto_expand_llm.py --db my_analysis.db --seed "Should I start a business?"

# Continue expanding (runs until all nodes explored or interrupted)
python auto_expand_llm.py --db my_analysis.db --continue

# Expand faster with parallel API calls
python auto_expand_llm.py --db my_analysis.db --continue --parallel 5
```

### 4. Visualize in the browser

```bash
python visualize.py --db my_analysis.db --serve
# Open http://localhost:8080
```

This launches an interactive graph viewer with:
- **Color-coded nodes**: orange (root), blue (assume right), red (assume wrong), gold (crux), green (grounded), purple (epistemic limit)
- **Sidebar filters**: branch type, depth slider, grounded-only, crux-only, domain selector, text search
- **Click any node** to see its full claim, depth, leverage score, domain, and grounding status
- **Controls**: reload at different depths, reset view, re-layout, export PNG

### 5. Analyze results

```bash
# Cross-database synthesis
python synthesize.py *.db

# Extract actionable items (HIGH impact + LOW effort)
python synthesize.py *.db --extract-actions actions.json

# Find contradictions between runs
python synthesize.py *.db --find-tensions
```

## Database schema

All ARAW data is stored in SQLite. The core table:

```sql
CREATE TABLE nodes (
    id TEXT PRIMARY KEY,
    parent_id TEXT,           -- NULL for root
    claim TEXT,               -- The claim being explored
    branch_type TEXT,         -- 'root', 'assume_right', 'assume_wrong'
    status TEXT,              -- 'unexplored', 'exploring', 'explored', 'pruned'
    depth INTEGER,            -- Distance from root
    leverage_score REAL,      -- 0.0-1.0, higher = more important
    content JSON,             -- Metadata (is_crux, effort, impact, domain, etc.)
    created_at TEXT,
    explored_at TEXT
);
```

Query directly with sqlite3:

```bash
# High-leverage unexplored nodes
sqlite3 my.db "SELECT claim, leverage_score FROM nodes WHERE status='unexplored' ORDER BY leverage_score DESC LIMIT 10"

# Crux nodes
sqlite3 my.db "SELECT claim FROM nodes WHERE json_extract(content, '$.is_crux') = 1"

# Tree stats
sqlite3 my.db "SELECT COUNT(*) as total, SUM(CASE WHEN status='explored' THEN 1 ELSE 0 END) as explored, MAX(depth) as max_depth FROM nodes"
```

See [araw/README.md](araw/README.md) for detailed documentation of every file, all CLI options, and programmatic usage.

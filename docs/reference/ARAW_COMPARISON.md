# ARAW Systems Comparison

## Two ARAW Implementations

### 1. Existing ARAW (`library/araw/`)

**Purpose**: Explore the full possibility space of a claim

**Components**:
- `araw_engine.py` - SQLite storage (scales to 100k+ nodes)
- `auto_expand_llm.py` - LLM-powered branch generation

**What it does**:
```
Claim: "I need to change careers"
    ├─ ASSUME RIGHT (if true):
    │   ├─ Downstream consequence 1
    │   ├─ Downstream consequence 2
    │   └─ Downstream consequence 3
    └─ ASSUME WRONG (upstream causes):
        ├─ Cause from HUMAN domain
        ├─ Cause from INSTITUTIONAL domain
        ├─ Cause from EVIDENTIAL domain
        └─ Cause from PRACTICAL domain
```

**Features**:
- 18 exploration domains (HUMAN, INSTITUTIONAL, EVIDENTIAL, etc.)
- Structured JSON output with rich metadata:
  - `is_crux` - Would true vs false change conclusion by >20%?
  - `is_foundational` - Direct observation or definitional?
  - `effort_to_address` - LOW/MEDIUM/HIGH
  - `potential_impact` - LOW/MEDIUM/HIGH
  - `direct_path` - Can verify directly?
- Filters: vague patterns, action statements, intentions
- Parallel expansion, rate limiting
- Tracks explored themes to avoid repetition
- Persistent SQLite storage

---

### 2. New ARAW (`scripts/adaptive_learning.py`)

**Purpose**: Determine if a claim can be COMMITTED to (foundational) or is a GUESS

**What it does**:
```
Statement: "Reality exists"
    ├─ ASSUME RIGHT → implications...
    └─ ASSUME WRONG → "Reality doesn't exist"
        └─ Check: Is this self-refuting?
            YES → CONTRADICTION → All AW paths fail → FOUNDATIONAL
            NO  → COHERENT → AW path survives → GUESS
```

**Features**:
- Binary output: FOUNDATIONAL or GUESS
- Contradiction detection:
  - Self-refuting statements
  - Performative contradictions
  - Mixed path contradictions (AR asserts what AW denied)
- Coherent alternative detection
- In-memory tree (no persistence)

---

## Key Differences

| Aspect | Existing ARAW | New Commitment Test |
|--------|--------------|---------------------|
| **Goal** | Explore possibility space | Determine if logically necessary |
| **Output** | Rich tree with metadata | Binary: FOUNDATIONAL/GUESS |
| **Storage** | SQLite (persistent) | In-memory (ephemeral) |
| **Structure** | upstream_causes + downstream | Simple AR/AW implications |
| **LLM format** | JSON schema (structured) | Plain text |
| **Domains** | 18 categories | None |
| **Question** | "What could be true/false?" | "Can denial be coherent?" |

---

## Should They Merge?

**YES - they complement each other:**

1. **Existing ARAW** finds the tree structure
2. **Commitment Test** analyzes which nodes are foundational

**Proposed Integration**:

```
1. Use existing araw_engine.py for storage
2. Add new fields to nodes table:
   - commitment_status: "FOUNDATIONAL" | "GUESS" | "UNCHECKED"
   - contradiction_type: reason if foundational
   - coherent_alternative: example if guess

3. Add commitment analysis phase:
   - After tree exploration, analyze AW-originating paths
   - Check each terminal node for:
     - Self-refuting patterns
     - Performative contradictions
     - Coherent alternatives
   - Propagate status up the tree

4. New commands:
   - araw-analyze: Run commitment test on existing tree
   - araw-foundations: List all foundational claims
   - araw-guesses: List all claims that remain guesses
```

---

## Concrete Merge Plan

### Option A: Add to existing auto_expand_llm.py

Add commitment checking as a post-processing step:

```python
# After tree expansion
def analyze_commitments(engine: ARAWEngine):
    """Check which claims are foundational vs guesses"""
    for node in engine.get_all_aw_terminals():
        status = check_contradiction(node.claim)
        engine.set_commitment_status(node.id, status)
```

**Pros**: Single system, shared storage
**Cons**: Makes auto_expand_llm.py more complex

### Option B: Separate commitment analyzer

Keep as separate script that reads from ARAW database:

```bash
# First: explore
python auto_expand_llm.py --db my_search.db --seed "Reality exists"

# Then: analyze
python commitment_analyzer.py --db my_search.db
```

**Pros**: Clean separation, can run independently
**Cons**: Two scripts to manage

### Option C: Merge into unified system

Create new `araw_v2.py` that combines both:

```python
class ARAWv2:
    def explore(self, claim):
        """Explore possibility space"""
        ...

    def analyze_commitment(self, node_id):
        """Check if claim is foundational"""
        ...

    def get_foundations(self):
        """Get all foundational claims"""
        ...
```

**Pros**: Unified API
**Cons**: Rewrite effort

---

## Recommendation

**Option B (Separate commitment analyzer)** is best for now:

1. Minimal changes to working system
2. Can iterate on commitment logic independently
3. Easy to test and validate
4. Can merge later once logic is stable

**Next steps**:
1. Create `commitment_analyzer.py` that reads from existing ARAW databases
2. Add schema fields for commitment status
3. Test on existing trees
4. Consider full merge once stable

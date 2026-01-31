"""
ARAW Tree Visualization Exporter

Exports the ARAW tree to formats suitable for visualization:
- JSON for Sigma.js / D3.js
- GEXF for Gephi
- Serves interactive HTML visualization

Usage:
    python visualize.py --db worlddirection.db --export graph.json
    python visualize.py --db worlddirection.db --serve
    python visualize.py --db worlddirection.db --export graph.gexf --format gexf
"""

import argparse
import http.server
import json
import math
import os
import socketserver
import sqlite3
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime


# Domain keywords for detection
DOMAIN_KEYWORDS = {
    'HUMAN': ['person', 'people', 'individual', 'competent', 'skill', 'bias', 'motivation', 'psychology', 'cognitive', 'fatigue', 'burnout'],
    'INSTITUTIONAL': ['system', 'organization', 'policy', 'government', 'institution', 'regulation', 'bureauc', 'incentive', 'governance'],
    'EVIDENTIAL': ['evidence', 'data', 'test', 'study', 'research', 'measure', 'observation', 'experiment', 'empirical'],
    'EPISTEMOLOGICAL': ['knowledge', 'truth', 'logic', 'reason', 'method', 'assumption', 'certainty', 'epistem'],
    'PRACTICAL': ['cost', 'money', 'resource', 'time', 'budget', 'feasible', 'implement', 'staff'],
    'RELATIONAL': ['family', 'relationship', 'trust', 'communication', 'social', 'friend', 'team'],
    'ETHICAL': ['moral', 'ethic', 'fair', 'justice', 'value', 'right', 'wrong', 'principle'],
    'TEMPORAL': ['future', 'past', 'history', 'trend', 'generation', 'change', 'evolve'],
    'CULTURAL': ['culture', 'tradition', 'norm', 'society', 'worldview', 'custom'],
    'ENVIRONMENTAL': ['environment', 'climate', 'ecology', 'sustainable', 'nature', 'pollution'],
    'TECHNOLOGICAL': ['technology', 'ai', 'automation', 'digital', 'innovation', 'software', 'algorithm'],
    'SYSTEMIC': ['feedback', 'complexity', 'emergence', 'unintended', 'cascade', 'network effect'],
    'EMOTIONAL': ['emotion', 'psychological', 'morale', 'satisfaction', 'anxiety', 'stress', 'wellbeing'],
}


def detect_domain(claim: str) -> str:
    """Detect domain from claim text"""
    claim_lower = claim.lower()

    # Check for explicit domain prefix (e.g., "EVIDENTIAL: ...")
    for domain in DOMAIN_KEYWORDS:
        if claim_lower.startswith(domain.lower() + ':') or claim_lower.startswith('- ' + domain.lower() + ':'):
            return domain

    # Check for domain keywords in claim
    for domain, keywords in DOMAIN_KEYWORDS.items():
        if any(kw in claim_lower for kw in keywords):
            return domain

    return 'OTHER'


def get_node_color(node: Dict) -> str:
    """Assign color based on node properties"""
    content = node.get('content', {})

    # Grounded nodes - green shades
    if node.get('is_grounded'):
        return "#22c55e"  # Green

    # Crux nodes - gold
    if content.get('is_crux'):
        return "#eab308"  # Yellow/Gold

    # Epistemic limit assumptions - purple
    if content.get('assumption_type') == 'epistemic_limit':
        return "#a855f7"  # Purple

    # Grounding assumptions - cyan
    if content.get('grounding_assumption'):
        return "#06b6d4"  # Cyan

    # Branch type coloring
    branch_type = node.get('branch_type', '')
    if branch_type == 'assume_right':
        return "#3b82f6"  # Blue
    elif branch_type == 'assume_wrong':
        return "#ef4444"  # Red

    # Root node
    if node.get('depth', 0) == 0:
        return "#f97316"  # Orange

    return "#6b7280"  # Gray default


def get_node_size(node: Dict, min_size: float = 3, max_size: float = 20) -> float:
    """Calculate node size based on leverage and children count"""
    leverage = node.get('leverage_score', 0.5) or 0.5
    children = node.get('children_count', 0)

    # Combine leverage and influence
    influence_factor = math.log(children + 1) / 10 + 0.5
    size = min_size + (max_size - min_size) * leverage * influence_factor

    return min(max_size, max(min_size, size))


class ARAWVisualizer:
    """Export and visualize ARAW trees"""

    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def get_tree_data(self, max_depth: Optional[int] = None,
                      min_leverage: float = 0.0,
                      include_grounding: bool = True) -> Dict:
        """Extract tree data for visualization"""
        cursor = self.conn.cursor()

        # Get all nodes with computed properties
        query = """
            SELECT
                n.id, n.claim, n.parent_id, n.branch_type, n.depth,
                n.leverage_score, n.status, n.content, n.created_at,
                (SELECT COUNT(*) FROM nodes c WHERE c.parent_id = n.id) as children_count
            FROM nodes n
            WHERE 1=1
        """
        params = []

        if max_depth is not None:
            query += " AND n.depth <= ?"
            params.append(max_depth)

        if min_leverage > 0:
            query += " AND (n.leverage_score >= ? OR n.leverage_score IS NULL)"
            params.append(min_leverage)

        cursor.execute(query, params)
        nodes_raw = cursor.fetchall()

        # Get grounding info if requested (table may not exist)
        grounded_nodes = set()
        if include_grounding:
            try:
                cursor.execute("SELECT node_id FROM groundings")
                grounded_nodes = {row['node_id'] for row in cursor.fetchall()}
            except sqlite3.OperationalError:
                pass  # Table doesn't exist

        # Build nodes list
        nodes = []
        node_ids = set()

        for row in nodes_raw:
            content = json.loads(row['content']) if row['content'] else {}

            # Detect domain from claim text if not in content
            stored_domain = content.get('domain')
            detected_domain = detect_domain(row['claim']) if not stored_domain else stored_domain

            node = {
                'id': row['id'],
                'label': row['claim'][:50] + '...' if len(row['claim']) > 50 else row['claim'],
                'claim': row['claim'],
                'parent_id': row['parent_id'],
                'branch_type': row['branch_type'],
                'depth': row['depth'],
                'leverage_score': row['leverage_score'],
                'status': row['status'],
                'content': content,
                'children_count': row['children_count'],
                'is_grounded': row['id'] in grounded_nodes,
                'is_crux': content.get('is_crux', False),
                'domain': detected_domain,
            }

            # Compute visual properties
            node['color'] = get_node_color(node)
            node['size'] = get_node_size(node)

            nodes.append(node)
            node_ids.add(row['id'])

        # Build edges
        edges = []
        for node in nodes:
            if node['parent_id'] and node['parent_id'] in node_ids:
                edge_color = "#3b82f6" if node['branch_type'] == 'assume_right' else "#ef4444"
                edges.append({
                    'id': f"{node['parent_id']}-{node['id']}",
                    'source': node['parent_id'],
                    'target': node['id'],
                    'color': edge_color,
                    'type': node['branch_type']
                })

        # Compute statistics
        stats = self._compute_stats(nodes)

        return {
            'nodes': nodes,
            'edges': edges,
            'stats': stats,
            'exported_at': datetime.now().isoformat()
        }

    def _compute_stats(self, nodes: List[Dict]) -> Dict:
        """Compute summary statistics"""
        if not nodes:
            return {}

        depths = [n['depth'] for n in nodes]
        leverages = [n['leverage_score'] for n in nodes if n['leverage_score']]

        branch_counts = defaultdict(int)
        for n in nodes:
            branch_counts[n['branch_type'] or 'root'] += 1

        grounded = sum(1 for n in nodes if n['is_grounded'])
        crux = sum(1 for n in nodes if n['is_crux'])

        return {
            'total_nodes': len(nodes),
            'max_depth': max(depths) if depths else 0,
            'avg_depth': sum(depths) / len(depths) if depths else 0,
            'avg_leverage': sum(leverages) / len(leverages) if leverages else 0,
            'branch_distribution': dict(branch_counts),
            'grounded_nodes': grounded,
            'crux_nodes': crux,
        }

    def _compute_layout(self, nodes: List[Dict]) -> Dict[str, tuple]:
        """Compute hierarchical layout positions for nodes (iterative for deep trees)"""
        if not nodes:
            return {}

        # Build parent->children mapping
        children_map = defaultdict(list)
        node_map = {n['id']: n for n in nodes}

        for n in nodes:
            if n['parent_id'] and n['parent_id'] in node_map:
                children_map[n['parent_id']].append(n['id'])

        # Find root(s) - nodes with depth 0 or no parent in our set
        roots = [n['id'] for n in nodes if n['depth'] == 0 or n['parent_id'] not in node_map]

        positions = {}

        # For large graphs, use a simpler depth-based layout
        if len(nodes) > 10000:
            # Group nodes by depth
            by_depth = defaultdict(list)
            for n in nodes:
                by_depth[n['depth']].append(n['id'])

            # Assign positions - spread nodes at each depth
            for depth, node_ids in by_depth.items():
                for i, node_id in enumerate(node_ids):
                    angle = (i / max(1, len(node_ids))) * 2 * math.pi
                    radius = (depth + 1) * 100
                    x = radius * math.cos(angle)
                    y = radius * math.sin(angle)
                    positions[node_id] = (x, y)
            return positions

        # For smaller graphs, use proper tree layout (iterative BFS)
        # First pass: compute subtree widths bottom-up
        depths = {n['id']: n['depth'] for n in nodes}
        max_depth = max(depths.values()) if depths else 0

        subtree_width = {}

        # Process from leaves up
        for d in range(max_depth, -1, -1):
            nodes_at_depth = [nid for nid, depth in depths.items() if depth == d]
            for node_id in nodes_at_depth:
                children = children_map.get(node_id, [])
                if not children:
                    subtree_width[node_id] = 1
                else:
                    subtree_width[node_id] = sum(subtree_width.get(c, 1) for c in children)

        # Second pass: assign x positions top-down
        # Use BFS to assign positions
        from collections import deque

        queue = deque()
        current_x = 0

        for root_id in roots:
            queue.append((root_id, current_x))
            current_x += subtree_width.get(root_id, 1) + 2

        while queue:
            node_id, x_start = queue.popleft()
            depth = depths.get(node_id, 0)

            children = children_map.get(node_id, [])
            total_width = sum(subtree_width.get(c, 1) for c in children)

            if children:
                # Position at center of children span
                positions[node_id] = (x_start + total_width / 2, depth * 50)
                # Queue children
                child_x = x_start
                for child_id in children:
                    queue.append((child_id, child_x))
                    child_x += subtree_width.get(child_id, 1)
            else:
                positions[node_id] = (x_start + 0.5, depth * 50)

        # Handle any nodes not positioned (orphans)
        orphan_x = current_x + 10
        for n in nodes:
            if n['id'] not in positions:
                positions[n['id']] = (orphan_x, n['depth'] * 50)
                orphan_x += 1

        return positions

    def export_json(self, output_path: str, **kwargs) -> None:
        """Export to JSON for Sigma.js/D3.js"""
        data = self.get_tree_data(**kwargs)

        # Compute proper hierarchical layout
        positions = self._compute_layout(data['nodes'])

        # Convert to Sigma.js format
        sigma_data = {
            'nodes': [
                {
                    'id': n['id'],
                    'label': n['label'],
                    'x': positions.get(n['id'], (0, 0))[0],
                    'y': positions.get(n['id'], (0, 0))[1],
                    'size': n['size'],
                    'color': n['color'],
                    # Additional data
                    'claim': n['claim'],
                    'depth': n['depth'],
                    'leverage': n['leverage_score'],
                    'branch_type': n['branch_type'],
                    'is_grounded': n['is_grounded'],
                    'is_crux': n['is_crux'],
                    'children_count': n['children_count'],
                    'domain': n['domain'],
                }
                for n in data['nodes']
            ],
            'edges': [
                {
                    'id': e['id'],
                    'source': e['source'],
                    'target': e['target'],
                    'color': e['color'],
                    'type': e['type'],
                }
                for e in data['edges']
            ],
            'stats': data['stats'],
            'exported_at': data['exported_at']
        }

        with open(output_path, 'w') as f:
            json.dump(sigma_data, f, indent=2)

        print(f"Exported {len(sigma_data['nodes'])} nodes and {len(sigma_data['edges'])} edges to {output_path}")

    def export_gexf(self, output_path: str, **kwargs) -> None:
        """Export to GEXF format for Gephi"""
        data = self.get_tree_data(**kwargs)

        gexf = ['<?xml version="1.0" encoding="UTF-8"?>']
        gexf.append('<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">')
        gexf.append(f'  <meta lastmodifieddate="{datetime.now().strftime("%Y-%m-%d")}">')
        gexf.append('    <creator>ARAW Visualizer</creator>')
        gexf.append('    <description>ARAW Tree Export</description>')
        gexf.append('  </meta>')
        gexf.append('  <graph mode="static" defaultedgetype="directed">')

        # Node attributes
        gexf.append('    <attributes class="node">')
        gexf.append('      <attribute id="0" title="depth" type="integer"/>')
        gexf.append('      <attribute id="1" title="leverage" type="float"/>')
        gexf.append('      <attribute id="2" title="branch_type" type="string"/>')
        gexf.append('      <attribute id="3" title="is_grounded" type="boolean"/>')
        gexf.append('      <attribute id="4" title="is_crux" type="boolean"/>')
        gexf.append('      <attribute id="5" title="domain" type="string"/>')
        gexf.append('    </attributes>')

        # Nodes
        gexf.append('    <nodes>')
        for i, n in enumerate(data['nodes']):
            label = n['claim'].replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')[:100]
            gexf.append(f'      <node id="{n["id"]}" label="{label}">')
            gexf.append('        <attvalues>')
            gexf.append(f'          <attvalue for="0" value="{n["depth"]}"/>')
            gexf.append(f'          <attvalue for="1" value="{n["leverage_score"] or 0.5}"/>')
            gexf.append(f'          <attvalue for="2" value="{n["branch_type"] or "root"}"/>')
            gexf.append(f'          <attvalue for="3" value="{str(n["is_grounded"]).lower()}"/>')
            gexf.append(f'          <attvalue for="4" value="{str(n["is_crux"]).lower()}"/>')
            gexf.append(f'          <attvalue for="5" value="{n["domain"]}"/>')
            gexf.append('        </attvalues>')
            gexf.append(f'        <viz:color r="{int(n["color"][1:3], 16)}" g="{int(n["color"][3:5], 16)}" b="{int(n["color"][5:7], 16)}"/>')
            gexf.append(f'        <viz:size value="{n["size"]}"/>')
            gexf.append('      </node>')
        gexf.append('    </nodes>')

        # Edges
        gexf.append('    <edges>')
        for e in data['edges']:
            gexf.append(f'      <edge id="{e["id"]}" source="{e["source"]}" target="{e["target"]}"/>')
        gexf.append('    </edges>')

        gexf.append('  </graph>')
        gexf.append('</gexf>')

        with open(output_path, 'w') as f:
            f.write('\n'.join(gexf))

        print(f"Exported to {output_path}")

    def get_subtree(self, node_id: str, max_depth: int = 5) -> Dict:
        """Get a subtree starting from a specific node"""
        cursor = self.conn.cursor()

        # Get descendants up to max_depth
        cursor.execute("""
            WITH RECURSIVE subtree AS (
                SELECT id, claim, parent_id, branch_type, depth, leverage_score,
                       status, content, 0 as relative_depth
                FROM nodes WHERE id = ?
                UNION ALL
                SELECT n.id, n.claim, n.parent_id, n.branch_type, n.depth,
                       n.leverage_score, n.status, n.content, s.relative_depth + 1
                FROM nodes n
                JOIN subtree s ON n.parent_id = s.id
                WHERE s.relative_depth < ?
            )
            SELECT * FROM subtree
        """, (node_id, max_depth))

        nodes_raw = cursor.fetchall()

        # Build response
        nodes = []
        node_ids = set()

        for row in nodes_raw:
            content = json.loads(row['content']) if row['content'] else {}
            node = {
                'id': row['id'],
                'label': row['claim'][:50] + '...' if len(row['claim']) > 50 else row['claim'],
                'claim': row['claim'],
                'parent_id': row['parent_id'],
                'branch_type': row['branch_type'],
                'depth': row['depth'],
                'relative_depth': row['relative_depth'],
                'leverage_score': row['leverage_score'],
                'content': content,
            }
            node['color'] = get_node_color(node)
            node['size'] = get_node_size(node)
            nodes.append(node)
            node_ids.add(row['id'])

        edges = []
        for node in nodes:
            if node['parent_id'] and node['parent_id'] in node_ids:
                edges.append({
                    'id': f"{node['parent_id']}-{node['id']}",
                    'source': node['parent_id'],
                    'target': node['id'],
                    'color': "#3b82f6" if node['branch_type'] == 'assume_right' else "#ef4444",
                })

        return {'nodes': nodes, 'edges': edges}


def create_viewer_html() -> str:
    """Generate the interactive HTML viewer"""
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ARAW Tree Visualization</title>
    <script src="https://unpkg.com/graphology@0.25.4/dist/graphology.umd.min.js"></script>
    <script src="https://unpkg.com/sigma@2.4.0/build/sigma.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0f172a;
            color: #e2e8f0;
            overflow: hidden;
        }
        #container {
            display: flex;
            height: 100vh;
        }
        #sidebar {
            width: 350px;
            background: #1e293b;
            padding: 20px;
            overflow-y: auto;
            border-right: 1px solid #334155;
        }
        #graph-container {
            flex: 1;
            position: relative;
        }
        #sigma-container {
            width: 100%;
            height: 100%;
        }
        h1 {
            font-size: 1.5rem;
            margin-bottom: 20px;
            color: #f8fafc;
        }
        h2 {
            font-size: 1rem;
            margin: 20px 0 10px 0;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        .stat {
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 1px solid #334155;
        }
        .stat-label { color: #94a3b8; }
        .stat-value { color: #f8fafc; font-weight: 600; }
        .legend {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 10px;
        }
        .legend-item {
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 0.85rem;
        }
        .legend-color {
            width: 12px;
            height: 12px;
            border-radius: 50%;
        }
        .search-box {
            width: 100%;
            padding: 10px;
            border: 1px solid #334155;
            border-radius: 6px;
            background: #0f172a;
            color: #e2e8f0;
            font-size: 0.9rem;
            margin-bottom: 10px;
        }
        .search-box:focus {
            outline: none;
            border-color: #3b82f6;
        }
        .filters {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .filter-group label {
            display: block;
            font-size: 0.85rem;
            color: #94a3b8;
            margin-bottom: 4px;
        }
        .filter-group select, .filter-group input[type="range"] {
            width: 100%;
            padding: 6px;
            border: 1px solid #334155;
            border-radius: 4px;
            background: #0f172a;
            color: #e2e8f0;
        }
        #node-details {
            margin-top: 20px;
            padding: 15px;
            background: #0f172a;
            border-radius: 8px;
            display: none;
        }
        #node-details.visible { display: block; }
        #node-details h3 {
            font-size: 0.9rem;
            color: #f8fafc;
            margin-bottom: 10px;
        }
        #node-details .claim {
            font-size: 0.85rem;
            color: #cbd5e1;
            line-height: 1.5;
            margin-bottom: 10px;
        }
        #node-details .meta {
            font-size: 0.8rem;
            color: #64748b;
        }
        .controls {
            position: absolute;
            top: 20px;
            right: 20px;
            display: flex;
            gap: 10px;
        }
        .btn {
            padding: 8px 16px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.2s;
        }
        .btn-primary {
            background: #3b82f6;
            color: white;
        }
        .btn-primary:hover { background: #2563eb; }
        .btn-secondary {
            background: #334155;
            color: #e2e8f0;
        }
        .btn-secondary:hover { background: #475569; }
        #loading {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
        }
        .spinner {
            width: 40px;
            height: 40px;
            border: 3px solid #334155;
            border-top-color: #3b82f6;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 10px;
        }
        @keyframes spin { to { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <div id="container">
        <div id="sidebar">
            <h1>ARAW Explorer</h1>

            <input type="text" class="search-box" id="search" placeholder="Search claims...">

            <h2>Filters</h2>
            <div class="filters">
                <div class="filter-group">
                    <label>Branch Type</label>
                    <select id="filter-branch">
                        <option value="all">All</option>
                        <option value="assume_right">Assume Right</option>
                        <option value="assume_wrong">Assume Wrong</option>
                    </select>
                </div>
                <div class="filter-group">
                    <label>Max Depth: <span id="depth-value">10</span></label>
                    <input type="range" id="filter-depth" min="1" max="20" value="10">
                </div>
                <div class="filter-group">
                    <label>
                        <input type="checkbox" id="filter-grounded"> Show only grounded
                    </label>
                </div>
                <div class="filter-group">
                    <label>
                        <input type="checkbox" id="filter-crux"> Show only crux nodes
                    </label>
                </div>
                <div class="filter-group">
                    <label>Domains (Ctrl+click for multiple)</label>
                    <select id="filter-domains" multiple size="8" style="height: auto;">
                        <option value="all" selected>All Domains</option>
                        <option value="EVIDENTIAL">EVIDENTIAL</option>
                        <option value="EPISTEMOLOGICAL">EPISTEMOLOGICAL</option>
                        <option value="INSTITUTIONAL">INSTITUTIONAL</option>
                        <option value="PRACTICAL">PRACTICAL</option>
                        <option value="SYSTEMIC">SYSTEMIC</option>
                        <option value="HUMAN">HUMAN</option>
                        <option value="RELATIONAL">RELATIONAL</option>
                        <option value="ETHICAL">ETHICAL</option>
                        <option value="TEMPORAL">TEMPORAL</option>
                        <option value="CULTURAL">CULTURAL</option>
                        <option value="ENVIRONMENTAL">ENVIRONMENTAL</option>
                        <option value="TECHNOLOGICAL">TECHNOLOGICAL</option>
                        <option value="EMOTIONAL">EMOTIONAL</option>
                        <option value="OTHER">OTHER</option>
                    </select>
                </div>
            </div>

            <h2>Statistics</h2>
            <div id="stats">
                <div class="stat">
                    <span class="stat-label">Total Nodes</span>
                    <span class="stat-value" id="stat-total">-</span>
                </div>
                <div class="stat">
                    <span class="stat-label">Visible Nodes</span>
                    <span class="stat-value" id="stat-visible">-</span>
                </div>
                <div class="stat">
                    <span class="stat-label">Max Depth</span>
                    <span class="stat-value" id="stat-depth">-</span>
                </div>
                <div class="stat">
                    <span class="stat-label">Grounded</span>
                    <span class="stat-value" id="stat-grounded">-</span>
                </div>
                <div class="stat">
                    <span class="stat-label">Crux Nodes</span>
                    <span class="stat-value" id="stat-crux">-</span>
                </div>
            </div>

            <h2>Legend</h2>
            <div class="legend">
                <div class="legend-item">
                    <div class="legend-color" style="background: #f97316"></div>
                    <span>Root</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #3b82f6"></div>
                    <span>Assume Right</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #ef4444"></div>
                    <span>Assume Wrong</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #22c55e"></div>
                    <span>Grounded</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #eab308"></div>
                    <span>Crux</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #a855f7"></div>
                    <span>Epistemic Limit</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #06b6d4"></div>
                    <span>Grounding Assumption</span>
                </div>
            </div>

            <div id="node-details">
                <h3>Selected Node</h3>
                <div class="claim" id="detail-claim"></div>
                <div class="meta" id="detail-meta"></div>
            </div>
        </div>

        <div id="graph-container">
            <div id="sigma-container"></div>
            <div id="loading">
                <div class="spinner"></div>
                <div>Loading graph...</div>
            </div>
            <div class="controls">
                <select id="load-depth" class="btn btn-secondary" style="padding: 8px;">
                    <option value="5">Depth 5</option>
                    <option value="10" selected>Depth 10</option>
                    <option value="20">Depth 20</option>
                    <option value="50">Depth 50</option>
                    <option value="">All depths</option>
                </select>
                <button class="btn btn-secondary" id="btn-load">Load</button>
                <button class="btn btn-secondary" id="btn-reset">Reset View</button>
                <button class="btn btn-secondary" id="btn-layout">Re-layout</button>
                <button class="btn btn-primary" id="btn-export">Export PNG</button>
            </div>
        </div>
    </div>

    <script>
        let graph, renderer, originalData;
        let currentMaxDepth = 10;

        async function loadData(maxDepth = null) {
            const params = new URLSearchParams();
            if (maxDepth) params.set('max_depth', maxDepth);
            const url = '/data' + (params.toString() ? '?' + params.toString() : '');
            const response = await fetch(url);
            return await response.json();
        }

        async function reloadGraph() {
            const depth = document.getElementById('load-depth').value;
            currentMaxDepth = depth ? parseInt(depth) : null;

            document.getElementById('loading').style.display = 'block';
            document.getElementById('loading').innerHTML = '<div class="spinner"></div><div>Loading depth ' + (depth || 'all') + '...</div>';

            try {
                originalData = await loadData(currentMaxDepth);

                // Destroy old renderer if exists
                if (renderer) {
                    renderer.kill();
                }

                graph = buildGraph(originalData);

                const container = document.getElementById('sigma-container');
                renderer = new Sigma(graph, container, {
                    renderEdgeLabels: false,
                    labelRenderedSizeThreshold: 12,
                    labelFont: 'sans-serif',
                    labelSize: 12,
                    labelColor: { color: '#e2e8f0' },
                    minCameraRatio: 0.001,
                    maxCameraRatio: 100,
                });

                renderer.on('clickNode', ({ node }) => {
                    showNodeDetails(node);
                });

                document.getElementById('loading').style.display = 'none';
                updateStats(originalData, originalData.nodes.length);
            } catch (error) {
                document.getElementById('loading').innerHTML =
                    '<div style="color: #ef4444;">Error: ' + error.message + '</div>';
            }
        }

        function buildGraph(data) {
            const g = new graphology.Graph();

            data.nodes.forEach(node => {
                g.addNode(node.id, {
                    label: node.label,
                    x: node.x,
                    y: node.y,
                    size: node.size,
                    color: node.color,
                    // Store full data
                    claim: node.claim,
                    depth: node.depth,
                    leverage: node.leverage,
                    branch_type: node.branch_type,
                    is_grounded: node.is_grounded,
                    is_crux: node.is_crux,
                    children_count: node.children_count,
                    domain: node.domain,
                });
            });

            data.edges.forEach(edge => {
                if (g.hasNode(edge.source) && g.hasNode(edge.target)) {
                    g.addEdge(edge.source, edge.target, {
                        color: edge.color,
                        size: 0.5,
                    });
                }
            });

            return g;
        }

        function updateStats(data, visibleCount) {
            document.getElementById('stat-total').textContent = data.stats.total_nodes.toLocaleString();
            document.getElementById('stat-visible').textContent = visibleCount.toLocaleString();
            document.getElementById('stat-depth').textContent = data.stats.max_depth;
            document.getElementById('stat-grounded').textContent = data.stats.grounded_nodes;
            document.getElementById('stat-crux').textContent = data.stats.crux_nodes;
        }

        function applyFilters() {
            const branchFilter = document.getElementById('filter-branch').value;
            const maxDepth = parseInt(document.getElementById('filter-depth').value);
            const onlyGrounded = document.getElementById('filter-grounded').checked;
            const onlyCrux = document.getElementById('filter-crux').checked;
            const searchTerm = document.getElementById('search').value.toLowerCase();

            // Get selected domains
            const domainSelect = document.getElementById('filter-domains');
            const selectedDomains = Array.from(domainSelect.selectedOptions).map(o => o.value);
            const filterByDomain = selectedDomains.length > 0 && !selectedDomains.includes('all');

            let visibleCount = 0;

            graph.forEachNode((node, attrs) => {
                let visible = true;

                if (branchFilter !== 'all' && attrs.branch_type !== branchFilter) {
                    visible = false;
                }
                if (attrs.depth > maxDepth) {
                    visible = false;
                }
                if (onlyGrounded && !attrs.is_grounded) {
                    visible = false;
                }
                if (onlyCrux && !attrs.is_crux) {
                    visible = false;
                }
                if (searchTerm && !attrs.claim.toLowerCase().includes(searchTerm)) {
                    visible = false;
                }
                if (filterByDomain && !selectedDomains.includes(attrs.domain)) {
                    visible = false;
                }

                graph.setNodeAttribute(node, 'hidden', !visible);
                if (visible) visibleCount++;
            });

            // Hide edges connected to hidden nodes
            graph.forEachEdge((edge, attrs, source, target) => {
                const sourceHidden = graph.getNodeAttribute(source, 'hidden');
                const targetHidden = graph.getNodeAttribute(target, 'hidden');
                graph.setEdgeAttribute(edge, 'hidden', sourceHidden || targetHidden);
            });

            document.getElementById('stat-visible').textContent = visibleCount.toLocaleString();
            renderer.refresh();
        }

        function showNodeDetails(nodeId) {
            const attrs = graph.getNodeAttributes(nodeId);
            const details = document.getElementById('node-details');

            document.getElementById('detail-claim').textContent = attrs.claim;
            document.getElementById('detail-meta').innerHTML = `
                <strong>Depth:</strong> ${attrs.depth} |
                <strong>Leverage:</strong> ${(attrs.leverage || 0.5).toFixed(2)} |
                <strong>Children:</strong> ${attrs.children_count}<br>
                <strong>Type:</strong> ${attrs.branch_type || 'root'} |
                <strong>Grounded:</strong> ${attrs.is_grounded ? 'Yes' : 'No'} |
                <strong>Crux:</strong> ${attrs.is_crux ? 'Yes' : 'No'}<br>
                <strong>Domain:</strong> ${attrs.domain || 'unknown'}
            `;

            details.classList.add('visible');
        }

        // Simple force-directed layout (no external library needed)
        function simpleForceLayout(g, iterations = 50) {
            const nodes = [];
            const nodeIndex = {};

            g.forEachNode((id, attrs) => {
                nodeIndex[id] = nodes.length;
                nodes.push({
                    id,
                    x: attrs.x || Math.random() * 1000,
                    y: attrs.y || Math.random() * 1000,
                    depth: attrs.depth || 0,
                });
            });

            const edges = [];
            g.forEachEdge((id, attrs, source, target) => {
                edges.push({ source: nodeIndex[source], target: nodeIndex[target] });
            });

            // Simple force simulation
            for (let iter = 0; iter < iterations; iter++) {
                // Repulsion between all nodes (simplified - only nearby)
                for (let i = 0; i < nodes.length; i++) {
                    for (let j = i + 1; j < Math.min(i + 100, nodes.length); j++) {
                        const dx = nodes[j].x - nodes[i].x;
                        const dy = nodes[j].y - nodes[i].y;
                        const dist = Math.sqrt(dx * dx + dy * dy) + 0.1;
                        const force = 500 / (dist * dist);
                        nodes[i].x -= dx / dist * force;
                        nodes[i].y -= dy / dist * force;
                        nodes[j].x += dx / dist * force;
                        nodes[j].y += dy / dist * force;
                    }
                }

                // Attraction along edges
                edges.forEach(e => {
                    const s = nodes[e.source];
                    const t = nodes[e.target];
                    const dx = t.x - s.x;
                    const dy = t.y - s.y;
                    const dist = Math.sqrt(dx * dx + dy * dy) + 0.1;
                    const force = dist * 0.01;
                    s.x += dx * force;
                    s.y += dy * force;
                    t.x -= dx * force;
                    t.y -= dy * force;
                });

                // Depth-based vertical organization
                nodes.forEach(n => {
                    n.y = n.y * 0.9 + n.depth * 50 * 0.1;
                });
            }

            // Apply positions back to graph
            nodes.forEach(n => {
                g.setNodeAttribute(n.id, 'x', n.x);
                g.setNodeAttribute(n.id, 'y', n.y);
            });
        }

        async function init() {
            try {
                // Load with default depth of 10
                currentMaxDepth = 10;
                originalData = await loadData(currentMaxDepth);
                graph = buildGraph(originalData);

                // Create renderer
                const container = document.getElementById('sigma-container');
                renderer = new Sigma(graph, container, {
                    renderEdgeLabels: false,
                    labelRenderedSizeThreshold: 12,
                    labelFont: 'sans-serif',
                    labelSize: 12,
                    labelColor: { color: '#e2e8f0' },
                    minCameraRatio: 0.001,
                    maxCameraRatio: 100,
                });

                // Hide loading
                document.getElementById('loading').style.display = 'none';

                // Update stats
                updateStats(originalData, originalData.nodes.length);

                // Event handlers
                renderer.on('clickNode', ({ node }) => {
                    showNodeDetails(node);
                });

                // Filter handlers
                document.getElementById('filter-branch').addEventListener('change', applyFilters);
                document.getElementById('filter-depth').addEventListener('input', (e) => {
                    document.getElementById('depth-value').textContent = e.target.value;
                    applyFilters();
                });
                document.getElementById('filter-grounded').addEventListener('change', applyFilters);
                document.getElementById('filter-crux').addEventListener('change', applyFilters);
                document.getElementById('filter-domains').addEventListener('change', applyFilters);
                document.getElementById('search').addEventListener('input', applyFilters);

                // Button handlers
                document.getElementById('btn-load').addEventListener('click', reloadGraph);

                document.getElementById('btn-reset').addEventListener('click', () => {
                    renderer.getCamera().setState({ x: 0.5, y: 0.5, ratio: 1 });
                });

                document.getElementById('btn-layout').addEventListener('click', () => {
                    if (originalData.nodes.length < 10000) {
                        simpleForceLayout(graph, 50);
                        renderer.refresh();
                    } else {
                        alert('Too many nodes for force layout. Use depth filter to reduce.');
                    }
                });

            } catch (error) {
                console.error('Error initializing graph:', error);
                document.getElementById('loading').innerHTML =
                    '<div style="color: #ef4444;">Error loading graph: ' + error.message + '</div>';
            }
        }

        init();
    </script>
</body>
</html>'''


class VisualizationServer(http.server.SimpleHTTPRequestHandler):
    """HTTP server for visualization"""

    def __init__(self, *args, db_path=None, **kwargs):
        self.db_path = db_path
        super().__init__(*args, **kwargs)

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(create_viewer_html().encode())
        elif self.path.startswith('/data'):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Parse query parameters
            from urllib.parse import urlparse, parse_qs
            parsed = urlparse(self.path)
            params = parse_qs(parsed.query)

            max_depth = int(params.get('max_depth', [None])[0] or 0) or None
            min_leverage = float(params.get('min_leverage', [0])[0])

            viz = ARAWVisualizer(self.db_path)
            data = viz.get_tree_data(max_depth=max_depth, min_leverage=min_leverage)

            # Compute layout positions
            positions = viz._compute_layout(data['nodes'])

            # Format for Sigma.js
            sigma_data = {
                'nodes': [
                    {
                        'id': n['id'],
                        'label': n['label'],
                        'x': positions.get(n['id'], (0, 0))[0],
                        'y': positions.get(n['id'], (0, 0))[1],
                        'size': n['size'],
                        'color': n['color'],
                        'claim': n['claim'],
                        'depth': n['depth'],
                        'leverage': n['leverage_score'],
                        'branch_type': n['branch_type'],
                        'is_grounded': n['is_grounded'],
                        'is_crux': n['is_crux'],
                        'children_count': n['children_count'],
                        'domain': n['domain'],
                    }
                    for n in data['nodes']
                ],
                'edges': [
                    {
                        'id': e['id'],
                        'source': e['source'],
                        'target': e['target'],
                        'color': e['color'],
                    }
                    for e in data['edges']
                ],
                'stats': data['stats'],
            }
            self.wfile.write(json.dumps(sigma_data).encode())
        else:
            super().do_GET()

    def log_message(self, format, *args):
        pass  # Suppress logging


def serve(db_path: str, port: int = 8080):
    """Start visualization server"""
    handler = lambda *args, **kwargs: VisualizationServer(*args, db_path=db_path, **kwargs)

    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"ARAW Visualization Server")
        print(f"Open http://localhost:{port} in your browser")
        print(f"Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down...")


def main():
    parser = argparse.ArgumentParser(description="ARAW Tree Visualization")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--db", type=str, help="Database file (direct path)")
    group.add_argument("--session", type=str, help="Session ID (looks up in index)")
    group.add_argument("--session-dir", type=str, help="Session directory path")

    # Export options
    parser.add_argument("--export", type=str, help="Export to file (or session exports/ if omitted)")
    parser.add_argument("--format", choices=['json', 'gexf'], default='json',
                       help="Export format")

    # Filter options
    parser.add_argument("--max-depth", type=int, help="Maximum depth to include")
    parser.add_argument("--min-leverage", type=float, default=0.0,
                       help="Minimum leverage score")

    # Server options
    parser.add_argument("--serve", action="store_true", help="Start visualization server")
    parser.add_argument("--port", type=int, default=8080, help="Server port")

    # Session directory
    parser.add_argument("--sessions-dir", type=str, help="Sessions root directory")

    args = parser.parse_args()

    # Resolve the database path
    db_path = args.db
    session_dir = None

    if args.session:
        # Look up session in index
        try:
            from storage.session_store import SessionStore
        except ImportError:
            import sys
            sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
            from storage.session_store import SessionStore

        store = SessionStore(sessions_dir=args.sessions_dir)
        session = store.load_session(args.session)
        if not session:
            print(f"Session {args.session} not found in index.")
            return
        db_path = str(session.tree_db_path)
        session_dir = session.dir_path
        print(f"Loaded session: {session}")

    elif args.session_dir:
        session_dir = Path(args.session_dir)
        db_path = str(session_dir / "tree.db")

    if not Path(db_path).exists():
        print(f"Database not found: {db_path}")
        return

    if args.export:
        viz = ARAWVisualizer(db_path)
        kwargs = {}
        if args.max_depth:
            kwargs['max_depth'] = args.max_depth
        if args.min_leverage:
            kwargs['min_leverage'] = args.min_leverage

        if args.format == 'gexf':
            viz.export_gexf(args.export, **kwargs)
        else:
            viz.export_json(args.export, **kwargs)

    elif args.serve:
        serve(db_path, args.port)

    elif session_dir:
        # Default: export to session exports/ directory
        viz = ARAWVisualizer(db_path)
        kwargs = {}
        if args.max_depth:
            kwargs['max_depth'] = args.max_depth
        if args.min_leverage:
            kwargs['min_leverage'] = args.min_leverage

        exports_dir = Path(session_dir) / "exports"
        exports_dir.mkdir(exist_ok=True)

        viz.export_json(str(exports_dir / "tree.json"), **kwargs)
        viz.export_gexf(str(exports_dir / "tree.gexf"), **kwargs)
        print(f"Exported to {exports_dir}/")

    else:
        print("Use --export FILE or --serve")
        print("Run with --help for all options")


if __name__ == "__main__":
    main()

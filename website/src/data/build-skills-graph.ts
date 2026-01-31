/**
 * Build-time data loader for the skills dependency graph.
 * Reads skills.json and produces minimal graph data for D3.
 */

import fs from 'node:fs';
import path from 'node:path';

export interface SkillNode {
  id: string;
  title: string;
  description: string;
  tier: string;
  category: string | null;
  group: string; // tier or category label for clustering
  invokes: string[];
  invoked_by: string[];
}

export interface SkillEdge {
  source: string;
  target: string;
}

export interface GraphData {
  nodes: SkillNode[];
  edges: SkillEdge[];
  total: number;
  tierCounts: Record<string, number>;
}

// Tier colors — map to the website's tier badge palette
export const TIER_COLORS: Record<string, { light: string; dark: string; label: string }> = {
  tier1:        { light: '#2e7d32', dark: '#66bb6a', label: 'Tier 1 — Foundational' },
  tier2:        { light: '#1565c0', dark: '#42a5f5', label: 'Tier 2 — Intermediate' },
  tier3:        { light: '#e65100', dark: '#ff9800', label: 'Tier 3 — Applied' },
  tier4:        { light: '#78909c', dark: '#b0bec5', label: 'Tier 4 — Specialized' },
  category:     { light: '#6a1b9a', dark: '#ba68c8', label: 'Category Routers' },
  experimental: { light: '#c62828', dark: '#ef5350', label: 'Experimental' },
};

export function loadGraphData(): GraphData {
  const skillsPath = path.resolve(
    new URL('.', import.meta.url).pathname,
    '../../../claude-code-plugin/skills.json'
  );
  const raw = JSON.parse(fs.readFileSync(skillsPath, 'utf-8'));
  const skills = raw.skills as Record<string, any>;
  const ids = new Set(Object.keys(skills));

  const nodes: SkillNode[] = [];
  const edges: SkillEdge[] = [];
  const tierCounts: Record<string, number> = {};

  for (const [id, skill] of Object.entries(skills)) {
    const tier = skill.tier || 'tier4';
    tierCounts[tier] = (tierCounts[tier] || 0) + 1;

    nodes.push({
      id,
      title: skill.title,
      description: skill.description,
      tier,
      category: skill.category,
      group: skill.category || tier,
      invokes: skill.invokes.filter((t: string) => ids.has(t)),
      invoked_by: skill.invoked_by.filter((t: string) => ids.has(t)),
    });

    // Edges: skill -> invoked skill
    for (const target of skill.invokes) {
      if (ids.has(target)) {
        edges.push({ source: id, target });
      }
    }
  }

  return { nodes, edges, total: nodes.length, tierCounts };
}

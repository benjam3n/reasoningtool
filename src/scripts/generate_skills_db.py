#!/usr/bin/env python3
"""Generate skills.json, update catalog.json and marketplace.json from SKILL.md files."""

import json
import os
import re
from datetime import datetime, timezone

SKILLS_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'claude-code-plugin', 'skills')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'claude-code-plugin')

# ---------------------------------------------------------------------------
# Tier / category map — extracted from website/src/pages/skills.astro
# ---------------------------------------------------------------------------

TIER_MAP = {}

_tier1 = [
    'se', 'aex', 'cmp', 'ht', 'dcp', 'dcm', 'rca', 'dd',
    'mv', 'ins', 'cba', 'gu',
]
for s in _tier1:
    TIER_MAP[s] = ('tier1', None)

_tier2 = [
    'pv', 'ai', 'to', 'cda', 'ma', 'sya', 'br', 'prm',
    'fla', 'poa', 'ifss', 'rci', 'la', 'vbo', 'val',
    'fwa', 'frq', 'sdc', 'sid', 'ecal', 'rmm', 'alt',
    'ign', 'dwt', 'kta', 'fohw', 'insd',
]
for s in _tier2:
    TIER_MAP[s] = ('tier2', None)

_category = [
    'claim', 'decide', 'diagnose', 'search', 'how', 'want',
    'action', 'evaluate', 'emotion', 'viability', 'create',
    'analyze', 'technical', 'meta', 'certainty', 'iterate', 'sp',
]
for s in _category:
    TIER_MAP[s] = ('category', None)

_experimental = ['araw', 'uaua', 'gosm', 'gts']
for s in _experimental:
    TIER_MAP[s] = ('experimental', None)

_tier3 = {
    'Research & Analysis': [
        'lr', 'qr', 'dc', 'sta', 'exd', 'fia', 'cma', 'mr',
        'src', 'sop', 'er', 'plr', 'ess', 'sor',
    ],
    'Writing & Communication': [
        'w', 'pw', 'stl', 'pus', 'prd', 'cts', 'orm', 'fd',
        'al', 'argd',
    ],
    'Planning & Projects': [
        'pji', 'pjs', 'de', 'pjc', 'op', 'pt', 'ria', 'dpl',
        'ret', 'skm', 'dop', 'pp',
    ],
    'Business': [
        'cd', 'mf', 'pos', 'neg', 'clr', 'fm', 'bm', 'ivs',
        'roa', 'bo',
    ],
    'Software & Engineering': [
        'cor', 'dbg', 'rf', 'dsn', 'ap', 'apid', 'ts', 'sep',
        'sdp', 'enc', 'dsp',
    ],
    'Career & Learning': [
        'cpp', 'ip', 'rmo', 'sn', 'ska', 'dlp', 'spr', 'acr',
        'lrs',
    ],
    'Decision Making': [
        'dct', 'sel', 'crw', 'pwc', 'exv', 'mcd', 'rva', 'boc',
        'gdm',
    ],
    'Health & Wellness': ['ho'],
    'Crisis & Volatility': ['ch', 'hvh', 'ita'],
    'Competitive Programming': ['ape', 'api', 'apm'],
    'Scientific Research': ['aba', 'spp', 'ops'],
}
for cat, skills in _tier3.items():
    for s in skills:
        TIER_MAP[s] = ('tier3', cat)

_tier4 = {
    'Core Exploration': [
        'ar', 'aw', 'u', 'im', 'ans', 'met', 'svs', 'unx', 'gen', 'gn', 'gg',
        'foht', 'md', 'fe', 'ie', 'cdb', 'cga', 'cnw', 'va',
    ],
    'Search Methods': [
        'bes', 'cls', 'fss', 'ipss', 'mss', 'nss', 'pss', 'spd', 'std', 'fnd',
        'm', 'jm', 'smc', 'spe',
    ],
    'Goal Processing': [
        'gd', 'grf', 'grfr', 'gsr', 'gjs', 'lgi', 'uga', 'wt', 'je', 'agi',
        'atgb', 'ugav2', 'ugav3', 'ugav4', 'ugav5',
    ],
    'Goal Type Handlers': [
        'eg', 'ig', 'ldg', 'rlg', 'clg', 'mpg', 'idg', 'pvg', 'rsg', 'pag',
    ],
    'Assumptions & Critique': [
        'aa', 'ael', 'asu', 'ac', 'cri', 'mem', 'bi', 'advr', 'cv', 'stc',
        'tp', 'eh',
    ],
    'Questions & Analysis': [
        'qaf', 'qag', 'qo', 'cta', 'cdr', 'pbr', 'mrc', 'pre', 've', 'vcd',
        'qg', 'qm', 'evd',
    ],
    'Diagnosis & Recovery': [
        'pbi', 'rc5w', 'fowwr', 'sbfow', 'fr', 'lpd', 'cfr', 'shc', 'afa',
        'fat', 'fj', 'gaa',
    ],
    'Procedures & Meta': [
        'pcd', 'pce', 'pcex', 'pci', 'pefs', 'prr', 'dmt', 'tpm', 'tr', 'txm',
        'adep', 'auep', 'pcef', 'dot', 'ph', 'so', 'uo', 'gee', 'pqr', 'gaca',
        'cpra', 'vhd', 'tnt', 'cppd',
    ],
    'Self-Audit': [
        'saaapcav', 'saaesa', 'sads', 'sagsca', 'satrda', 'saadag', 'saaiasa',
        'sacri', 'sadrt', 'sapea', 'saqrc', 'saropc', 'sarus',
    ],
    'Evaluation & Validation': [
        'emv', 'ver', 'exc', 'capg', 'mcg', 'spg', 'skb', 'fb', 'vp', 'av',
    ],
    'Strategy & Planning': [
        'p', 'mpa', 'stg', 'o', 'rqg', 'cms', 'swa', 'ssr', 'wr', 'dsd', 'dse',
        'dss', 'dtl', 'ol', 'st', 'snp', 'es', 'sym', 'lp', 'lps', 'dari', 'aar',
    ],
    'Finance & Fundraising': ['b', 'cfm', 'ff', 'fua', 'gw', 'isd'],
    'Personal Development': ['hf', 'po', 'lt', 're', 'am', 'skp', 'ge'],
    'Marketing & Growth': ['sms', 'seb', 'vm', 'vdp', 'net', 'fl', 'jss'],
    'Advocacy & Outreach': ['ais', 'orc', 't', 'ea', 'pha', 'hd'],
    'Utility & Integration': ['sf', 'mcs', 'ams', 'eda'],
    'Orderings': [
        'ao', 'arcd', 'be', 'cn', 'cns', 'ct', 'dv', 'dvs', 'faa', 'gt', 'lcs',
        'ld', 'mil', 'mcp', 'mp', 'ns', 'ov', 'ovi', 'pb', 'pbs', 'pf', 'pge',
        'pjm', 'qs', 'rm', 'rso', 'srd', 'td',
    ],
}
for cat, skills in _tier4.items():
    for s in skills:
        TIER_MAP[s] = ('tier4', cat)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

INVOKE_RE = re.compile(r'(?:→|->)\s*INVOKE:\s*/(\w+)')
FRONTMATTER_RE = re.compile(r'^---\s*\n(.*?)\n---', re.DOTALL)


def parse_frontmatter(text):
    """Extract title and description from YAML-like frontmatter."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, None
    block = m.group(1)
    title = None
    desc = None
    for line in block.split('\n'):
        line = line.strip()
        if line.startswith('name:'):
            val = line[len('name:'):].strip().strip('"').strip("'")
            # name often looks like "aex - Assumption Extraction"
            if ' - ' in val:
                title = val.split(' - ', 1)[1].strip()
            else:
                title = val
        elif line.startswith('description:'):
            desc = line[len('description:'):].strip().strip('"').strip("'")
    return title, desc


def parse_sections(text):
    """Return list of ## heading names."""
    sections = []
    for line in text.split('\n'):
        if line.startswith('## '):
            sections.append(line[3:].strip())
    return sections


def parse_skill(skill_id, path):
    """Parse a single SKILL.md and return a skill dict."""
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    title, description = parse_frontmatter(text)

    # Fallback: use first # heading as title
    if not title:
        for line in text.split('\n'):
            if line.startswith('# ') and not line.startswith('## '):
                title = line[2:].strip()
                break
    if not title:
        title = skill_id.upper()

    # Fallback: use first non-empty paragraph after heading as description
    if not description:
        in_body = False
        for line in text.split('\n'):
            if line.startswith('# '):
                in_body = True
                continue
            if in_body and line.strip() and not line.startswith('#') and not line.startswith('---'):
                description = line.strip().rstrip('.')
                if len(description) > 200:
                    description = description[:197] + '...'
                break
    if not description:
        description = title

    invokes = list(dict.fromkeys(INVOKE_RE.findall(text)))  # unique, ordered
    sections = parse_sections(text)
    line_count = text.count('\n') + 1

    tier_info = TIER_MAP.get(skill_id)
    tier = tier_info[0] if tier_info else None
    category = tier_info[1] if tier_info else None

    return {
        'id': skill_id,
        'title': title,
        'description': description,
        'tier': tier,
        'category': category,
        'categories': [],
        'tags': [],
        'input_types': [],
        'invokes': invokes,
        'invoked_by': [],  # computed later
        'sections': sections,
        'line_count': line_count,
    }


def load_old_catalog(path):
    """Load old catalog.json and return dict keyed by skill id."""
    if not os.path.exists(path):
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    procs = data.get('procedures', {})
    # Normalize: old catalog had 'visual_design_principles' for 'vdp'
    old = {}
    alias_map = {'visual_design_principles': 'vdp'}
    for key, val in procs.items():
        real_key = alias_map.get(key, key)
        old[real_key] = val
    return old


def main():
    skills_dir = os.path.normpath(SKILLS_DIR)
    output_dir = os.path.normpath(OUTPUT_DIR)
    catalog_path = os.path.join(output_dir, 'catalog.json')

    # Load old catalog for metadata preservation
    old_catalog = load_old_catalog(catalog_path)

    # Parse all skills
    skills = {}
    dirs = sorted(os.listdir(skills_dir))
    for skill_id in dirs:
        skill_path = os.path.join(skills_dir, skill_id, 'SKILL.md')
        if not os.path.isfile(skill_path):
            continue
        skill = parse_skill(skill_id, skill_path)

        # Merge metadata from old catalog
        if skill_id in old_catalog:
            old = old_catalog[skill_id]
            if old.get('categories'):
                skill['categories'] = old['categories']
            if old.get('tags'):
                skill['tags'] = old['tags']
            if old.get('input_types'):
                skill['input_types'] = old['input_types']
            # Use old description if current one is just the title
            if old.get('description') and skill['description'] == skill['title']:
                skill['description'] = old['description']

        skills[skill_id] = skill

    # Build invoked_by reverse index
    for skill_id, skill in skills.items():
        for target in skill['invokes']:
            if target in skills:
                if skill_id not in skills[target]['invoked_by']:
                    skills[target]['invoked_by'].append(skill_id)

    # Check for missing tier assignments
    missing_tier = [sid for sid, s in skills.items() if s['tier'] is None]
    if missing_tier:
        print(f"WARNING: {len(missing_tier)} skills have no tier assignment: {missing_tier}")

    # Write skills.json
    skills_json = {
        'generated': datetime.now(timezone.utc).isoformat(),
        'total': len(skills),
        'skills': skills,
    }
    skills_json_path = os.path.join(output_dir, 'skills.json')
    with open(skills_json_path, 'w', encoding='utf-8') as f:
        json.dump(skills_json, f, indent=2, ensure_ascii=False)
    print(f"Wrote {skills_json_path} ({len(skills)} skills)")

    # Write catalog.json (updated to 355 entries)
    catalog = {'procedures': {}}
    for skill_id in sorted(skills.keys()):
        s = skills[skill_id]
        catalog['procedures'][skill_id] = {
            'description': s['description'],
            'categories': s['categories'],
            'tags': s['tags'],
            'input_types': s['input_types'],
            'invokes': s['invokes'],
        }
    with open(catalog_path, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
    print(f"Wrote {catalog_path} ({len(catalog['procedures'])} entries)")

    # Write marketplace.json
    marketplace = {
        '$schema': 'https://anthropic.com/claude-code/marketplace.schema.json',
        'name': 'reasoningtool',
        'description': f'{len(skills)} thinking skills for Claude Code',
        'owner': {'name': 'reasoningtool'},
        'plugins': [
            {
                'name': 'reasoningtool',
                'description': f'{len(skills)} thinking skills for decisions, problem solving, writing, research, planning, and more',
                'version': '1.0.0',
                'author': {'name': 'reasoningtool'},
                'source': './',
                'category': 'productivity',
            }
        ],
    }
    marketplace_path = os.path.join(output_dir, 'marketplace.json')
    with open(marketplace_path, 'w', encoding='utf-8') as f:
        json.dump(marketplace, f, indent=2, ensure_ascii=False)
    print(f"Wrote {marketplace_path}")

    # Summary
    tier_counts = {}
    for s in skills.values():
        t = s['tier'] or 'MISSING'
        tier_counts[t] = tier_counts.get(t, 0) + 1
    print(f"\nTier distribution:")
    for t in sorted(tier_counts.keys()):
        print(f"  {t}: {tier_counts[t]}")


if __name__ == '__main__':
    main()

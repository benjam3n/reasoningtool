#!/usr/bin/env python3
"""Generate skills.json and marketplace.json from SKILL.md files."""

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
        'al', 'argd', 'wre', 'story', 'draft', 'edit',
    ],
    'Planning & Projects': [
        'pji', 'pjs', 'de', 'pjc', 'op', 'pt', 'ria', 'dpl',
        'ret', 'skm', 'dop', 'pp', 'plansuite',
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
        'gdm', 'dom',
    ],
    'Health & Wellness': ['ho'],
    'Crisis & Volatility': ['ch', 'hvh', 'ita', 'saf'],
    'Ethics': ['eth'],
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
        'it', 'but', 'nsa', 'sycs', 'siycftr', 'alebc', 'iaw',
        'anag', 'crtv', 'difr', 'funr', 'genl', 'hrd', 'sim', 'smpl',
        'soph', 'spcf', 'spec', 'thnk', 'upth', 'cmplx', 'exps',
    ],
    'Skill Routing': [
        'wsib', 'dtse', 'extract', 'fonss', 'given', 'next', 'handle', 'itp',
        'uf', 'wn',
        'pick', 'tri', 'ornt', 'wsn', 'statous',
        'idk', 'unsure', 'cnfsd', 'ambi', 'blank', 'nowwt', 'nstep', 'strt', 'wtdn',
        'fowtd', 'fowtdn',
    ],
    'Skill Creation': [
        'mts', 'fmtsb', 'sc', 'cs', 'flhwijd',
        'chns', 'injc', 'orcs', 'stnl', 'wrps', 'mtskd', 'skcl',
    ],
    'Search Methods': [
        'bes', 'cls', 'fss', 'ipss', 'mss', 'nss', 'pss', 'spd', 'std', 'fnd',
        'm', 'jm', 'smc', 'spe',
    ],
    'Goal Processing': [
        'gd', 'grf', 'grfr', 'gsr', 'gjs', 'lgi', 'uga', 'wt', 'je', 'agi',
        'atgb', 'ugav2', 'ugav3', 'ugav4', 'ugav5',
        'plsk',
    ],
    'Goal Type Handlers': [
        'eg', 'ig', 'ldg', 'rlg', 'clg', 'mpg', 'idg', 'pvg', 'rsg', 'pag',
    ],
    'Assumptions & Critique': [
        'aa', 'ael', 'asu', 'ac', 'cri', 'mem', 'bi', 'advr', 'cv', 'stc',
        'tp', 'eh',
        'agsk', 'deb', 'jdgm', 'ratn',
        'steelman', 'redteam', 'reframe', 'doubt',
    ],
    'Questions & Analysis': [
        'qaf', 'qag', 'qo', 'cta', 'cdr', 'pbr', 'mrc', 'pre', 've', 'vcd',
        'qg', 'qm', 'evd',
        'indv', 'orgn', 'sysk', 'prob', 'systhink',
    ],
    'Diagnosis & Recovery': [
        'pbi', 'rc5w', 'fowwr', 'sbfow', 'fr', 'lpd', 'cfr', 'shc', 'afa',
        'fat', 'fj', 'gaa',
        'conr', 'dmgc', 'conflict',
        'panic', 'frzn', 'unstk', 'lost', 'ovwlm',
    ],
    'Procedures & Meta': [
        'pcd', 'pce', 'pcex', 'pci', 'pefs', 'prr', 'dmt', 'tpm', 'tr', 'txm',
        'adep', 'auep', 'pcef', 'dot', 'ph', 'so', 'uo', 'gee', 'pqr', 'gaca',
        'cpra', 'vhd', 'tnt', 'cppd',
        'awtlytrn', 'ycshikfmif', 'iagca',
        'oprc', 'anst', 'dcst', 'exst', 'rfst',
    ],
    'Self-Audit': [
        'saaapcav', 'saaesa', 'sads', 'sagsca', 'satrda', 'saadag', 'saaiasa',
        'sacri', 'sadrt', 'sapea', 'saqrc', 'saropc', 'sarus',
    ],
    'Evaluation & Validation': [
        'emv', 'ver', 'exc', 'capg', 'mcg', 'spg', 'skb', 'fb', 'vp', 'av',
        'obv', 'obo', 'ogo', 'gop', 'oba',
        'vldt', 'cmpr', 'prvn', 'benf', 'efrt', 'mets',
    ],
    'Strategy & Planning': [
        'p', 'mpa', 'stg', 'o', 'rqg', 'cms', 'swa', 'ssr', 'wr', 'dsd', 'dse',
        'dss', 'dtl', 'ol', 'st', 'snp', 'es', 'sym', 'lp', 'lps', 'dari', 'aar',
        'ata', 'tbd', 'tobd', 'fut', 'dys', 'utp',
        'pri', 'roip',
    ],
    'Finance & Fundraising': ['b', 'cfm', 'ff', 'fua', 'gw', 'isd'],
    'Personal Development': [
        'hf', 'po', 'lt', 're', 'am', 'skp', 'ge',
        'hab', 'lrnk', 'memy', 'prcp', 'teach', 'memk',
    ],
    'Marketing & Growth': [
        'sms', 'seb', 'vm', 'vdp', 'net', 'fl', 'jss',
        'cdiff', 'per', 'pinf',
    ],
    'Advocacy & Outreach': ['ais', 'orc', 't', 'ea', 'pha', 'hd'],
    'List & Pattern': [
        'list', 'ro', 'etc', 'aso', 'platitude', 'platitudes',
        'olst', 'omtx', 'sum',
    ],
    'Utility & Integration': [
        'sf', 'mcs', 'ams', 'eda',
        'exint', 'pwif', 'rwif', 'dshb', 'bldk',
    ],
    'Orderings': [
        'ao', 'arcd', 'be', 'cn', 'cns', 'ct', 'dv', 'dvs', 'faa', 'gt', 'lcs',
        'ld', 'mil', 'mcp', 'mp', 'ns', 'ov', 'ovi', 'pb', 'pbs', 'pf', 'pge',
        'pjm', 'qs', 'rm', 'rso', 'srd', 'td',
    ],
    'Claim Analysis': [
        'cscl', 'fctl', 'icl', 'mocl', 'mtcl', 'ncl', 'pcl', 'rlcl',
    ],
    'Skill Picker': [
        'p10complement', 'p10diverse', 'p10for', 'p10goal', 'p10random',
        'p10useful', 'p3chain', 'p5deep', 'p5qm', 'p5similar', 'p5want',
        'p7cat', 'p8tier',
    ],
    'Skill Improvement': [
        'imps', 'impss', 'imprt', 'skev', 'skgap', 'rskl', 'tkint',
        'ctcov', 'ctgp', 'ecomp', 'stcc', 'mtnw', 'nrwd',
        'nusr', 'pusr', 'satr',
    ],
    'AI & Automation': [
        'aiag', 'fwai', 'llmf', 'ltai',
    ],
    'Domain-Specific Analysis': [
        'ctan', 'dqnt', 'dtsk', 'dxpt', 'hpat', 'leg', 'rgc', 'rtas',
    ],
    'Communication & Collaboration': [
        'comc', 'col', 'csb', 'tfac', 'tmsk', 'socg', 'eqi', 'empth',
        'collab', 'persua', 'trust',
    ],
    'Decision Outputs': [
        'cand', 'odec', 'oart', 'onar', 'orec', 'prsk',
    ],
    'Ethics & Values': [
        'ecoc', 'mdr', 'vcl', 'unvs',
    ],
    'Gap & Coverage': [
        'gapf', 'gflr', 'immg', 'undr',
    ],
    'Health & Lifestyle': [
        'slp', 'nutr', 'exrp',
    ],
    'User & Need': [
        'usnd', 'usrn', 'curd', 'cvis', 'idsk', 'abts',
    ],
    'Metacognition': [
        'mtcg', 'mtgd', 'rlsk', 'efa',
    ],
    'Complexity & Depth': [
        'ezy',
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
    """Extract title, description, tier, categories, and tags from YAML-like frontmatter."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, None, None, [], []
    block = m.group(1)
    title = None
    desc = None
    tier = None
    categories = []
    tags = []
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
        elif line.startswith('tier:'):
            tier = line[len('tier:'):].strip().strip('"').strip("'")
        elif line.startswith('categories:'):
            val = line[len('categories:'):].strip()
            if val.startswith('['):
                categories = [c.strip().strip('"').strip("'") for c in val.strip('[]').split(',') if c.strip()]
        elif line.startswith('tags:'):
            val = line[len('tags:'):].strip()
            if val.startswith('['):
                tags = [t.strip().strip('"').strip("'") for t in val.strip('[]').split(',') if t.strip()]
    return title, desc, tier, categories, tags


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

    title, description, fm_tier, fm_categories, fm_tags = parse_frontmatter(text)

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
    tier = tier_info[0] if tier_info else fm_tier
    category = tier_info[1] if tier_info else (fm_categories[0] if fm_categories else None)

    return {
        'id': skill_id,
        'title': title,
        'description': description,
        'tier': tier,
        'category': category,
        'categories': fm_categories,
        'tags': fm_tags,
        'input_types': [],
        'invokes': invokes,
        'invoked_by': [],  # computed later
        'sections': sections,
        'line_count': line_count,
    }


def load_old_skills(path):
    """Load previous skills.json and return dict keyed by skill id."""
    if not os.path.exists(path):
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('skills', {})


def main():
    skills_dir = os.path.normpath(SKILLS_DIR)
    output_dir = os.path.normpath(OUTPUT_DIR)
    skills_json_path = os.path.join(output_dir, 'skills.json')

    # Load previous skills.json for metadata preservation
    old_skills = load_old_skills(skills_json_path)

    # Parse all skills
    skills = {}
    dirs = sorted(os.listdir(skills_dir))
    for skill_id in dirs:
        skill_path = os.path.join(skills_dir, skill_id, 'SKILL.md')
        if not os.path.isfile(skill_path):
            continue
        skill = parse_skill(skill_id, skill_path)

        # Merge metadata from previous skills.json
        if skill_id in old_skills:
            old = old_skills[skill_id]
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

    # Validate invocation chains — flag references to non-existent skills
    broken_refs = []
    for skill_id, skill in skills.items():
        for target in skill['invokes']:
            if target not in skills:
                broken_refs.append((skill_id, target))
                print(f"WARNING: skill '{skill_id}' invokes '{target}' which does not exist")
    if broken_refs:
        affected_skills = len(set(ref[0] for ref in broken_refs))
        print(f"Validation: {len(broken_refs)} broken references found across {affected_skills} skills")
    else:
        print("Validation: no broken invocation references found")

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
    with open(skills_json_path, 'w', encoding='utf-8') as f:
        json.dump(skills_json, f, indent=2, ensure_ascii=False)
    print(f"Wrote {skills_json_path} ({len(skills)} skills)")

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

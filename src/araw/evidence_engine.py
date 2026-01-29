"""
Evidence Access Engine

Systematic evidence gathering through tiered source cascade.
Implements the Intelligence Fusion model for cross-validated evidence collection.

Usage:
    python evidence_engine.py --db worlddirection.db --claim "Global poverty is declining"
    python evidence_engine.py --db worlddirection.db --ground-node <node_id>
    python evidence_engine.py --db worlddirection.db --test-sources
"""

import argparse
import asyncio
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import tempfile
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple
from urllib.parse import quote_plus, urlencode
import urllib.request
import urllib.error


# ============================================================================
# CONFIGURATION
# ============================================================================

DEFAULT_MODEL = "gpt-4o-mini"
DEFAULT_KEY_FILE = str(Path.home() / ".config" / "gosm" / "openai_api_key")

# Reliability tiers (higher weight = more reliable)
RELIABILITY_WEIGHTS = {
    "direct_observation": 1.0,
    "raw_data": 0.85,
    "published_analysis": 0.7,
    "expert_claim": 0.5,
    "model_output": 0.3,
    "unknown": 0.1,
}

# Accessibility scoring
ACCESSIBILITY_SCORES = {
    "time": {
        "immediate": 1.0,
        "hours": 0.8,
        "days": 0.5,
        "weeks": 0.2,
        "months": 0.1,
    },
    "cost": {
        "free": 1.0,
        "low": 0.8,
        "medium": 0.5,
        "high": 0.2,
        "prohibitive": 0.0,
    },
    "skill": {
        "none": 1.0,
        "basic": 0.9,
        "intermediate": 0.6,
        "expert": 0.3,
        "specialist": 0.1,
    },
    "availability": {
        "public": 1.0,
        "restricted": 0.5,
        "private": 0.2,
        "nonexistent": 0.0,
    },
}


def read_api_key(path: Optional[str] = None) -> Optional[str]:
    env = os.environ.get("OPENAI_API_KEY", "").strip()
    if env:
        return env
    for p in ([path] if path else []) + [DEFAULT_KEY_FILE]:
        if p and Path(p).expanduser().is_file():
            return Path(p).expanduser().read_text().splitlines()[0].strip()
    return None


# ============================================================================
# DATA CLASSES
# ============================================================================

@dataclass
class AccessibilityCost:
    """Cost/effort to access an evidence source"""
    time: str = "immediate"  # immediate, hours, days, weeks, months
    cost: str = "free"  # free, low, medium, high, prohibitive
    skill: str = "none"  # none, basic, intermediate, expert, specialist
    availability: str = "public"  # public, restricted, private, nonexistent

    def score(self) -> float:
        """Compute overall accessibility score (0-1, higher = more accessible)"""
        return (
            ACCESSIBILITY_SCORES["time"].get(self.time, 0.5) *
            ACCESSIBILITY_SCORES["cost"].get(self.cost, 0.5) *
            ACCESSIBILITY_SCORES["skill"].get(self.skill, 0.5) *
            ACCESSIBILITY_SCORES["availability"].get(self.availability, 0.5)
        )


@dataclass
class EvidenceResult:
    """Result from querying an evidence source"""
    source_name: str
    source_type: str  # web_api, search_engine, knowledge_base, research_repo, etc.
    reliability_tier: str  # direct_observation, raw_data, published_analysis, expert_claim, model_output
    content: str  # The actual evidence content
    citations: List[str] = field(default_factory=list)  # URLs or references
    confidence: float = 0.5  # 0-1, how confident in this evidence
    relevance: float = 0.5  # 0-1, how relevant to the claim
    retrieval_time: float = 0.0  # seconds
    cost_incurred: AccessibilityCost = field(default_factory=AccessibilityCost)
    raw_response: Any = None  # Original API response
    error: Optional[str] = None  # Error message if failed
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

    def reliability_weight(self) -> float:
        return RELIABILITY_WEIGHTS.get(self.reliability_tier, 0.1)

    def overall_score(self) -> float:
        """Combined score of reliability, confidence, relevance, and accessibility"""
        return (
            self.reliability_weight() *
            self.confidence *
            self.relevance *
            self.cost_incurred.score()
        )


@dataclass
class EpistemicLimit:
    """A path that couldn't be accessed - becomes ARAW explorable"""
    source_name: str
    reason: str  # Why we couldn't access
    limit_type: str  # unavailable, rate_limited, paywalled, requires_expertise, etc.
    possible_workarounds: List[str] = field(default_factory=list)
    confidence_truly_limited: str = "medium"  # high, medium, low


@dataclass
class AgreementCluster:
    """Group of evidence that agrees on a point"""
    claim_summary: str
    supporting_results: List[EvidenceResult] = field(default_factory=list)
    combined_confidence: float = 0.0


@dataclass
class Contradiction:
    """Disagreement between sources"""
    topic: str
    side_a: str
    side_b: str
    sources_a: List[str] = field(default_factory=list)
    sources_b: List[str] = field(default_factory=list)


@dataclass
class EvidenceSynthesis:
    """Final synthesis of all gathered evidence"""
    claim: str
    summary: str
    agreements: List[AgreementCluster] = field(default_factory=list)
    contradictions: List[Contradiction] = field(default_factory=list)
    overall_confidence: float = 0.0
    evidence_count: int = 0
    sources_consulted: List[str] = field(default_factory=list)
    epistemic_limits: List[EpistemicLimit] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)


# ============================================================================
# EVIDENCE SOURCE BASE CLASS
# ============================================================================

class EvidenceSource(ABC):
    """Base class for evidence sources"""

    name: str = "base"
    source_type: str = "unknown"
    reliability_tier: str = "unknown"
    tier: int = 1  # Cascade tier (1=fastest/cheapest, 3=slowest/most expensive)

    def __init__(self):
        self.accessibility = AccessibilityCost()

    @abstractmethod
    def can_query(self, claim: str) -> bool:
        """Check if this source can potentially answer the claim"""
        pass

    @abstractmethod
    def query(self, claim: str, context: Optional[str] = None) -> EvidenceResult:
        """Query this source for evidence about the claim"""
        pass

    def estimate_relevance(self, claim: str) -> float:
        """Estimate how relevant this source is for the claim (0-1)"""
        return 0.5  # Default: moderate relevance

    def priority_score(self, claim: str) -> float:
        """Calculate priority for cascade ordering"""
        reliability = RELIABILITY_WEIGHTS.get(self.reliability_tier, 0.1)
        accessibility = self.accessibility.score()
        relevance = self.estimate_relevance(claim)
        return reliability * accessibility * relevance


# ============================================================================
# TIER 1 SOURCES: Free, Fast, Web-Accessible
# ============================================================================

class WikipediaSource(EvidenceSource):
    """Wikipedia API for general knowledge"""

    name = "Wikipedia"
    source_type = "knowledge_base"
    reliability_tier = "published_analysis"
    tier = 1

    def __init__(self):
        super().__init__()
        self.accessibility = AccessibilityCost(
            time="immediate", cost="free", skill="none", availability="public"
        )
        self.api_url = "https://en.wikipedia.org/w/api.php"

    def can_query(self, claim: str) -> bool:
        return True  # Wikipedia can attempt any claim

    def _extract_search_terms(self, claim: str) -> List[str]:
        """Extract key terms from claim for searching"""
        # Remove common words
        stopwords = {'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been',
                    'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
                    'would', 'could', 'should', 'may', 'might', 'must', 'shall',
                    'can', 'need', 'dare', 'ought', 'used', 'to', 'of', 'in',
                    'for', 'on', 'with', 'at', 'by', 'from', 'as', 'into',
                    'through', 'during', 'before', 'after', 'above', 'below',
                    'between', 'under', 'again', 'further', 'then', 'once',
                    'that', 'this', 'these', 'those', 'and', 'but', 'or', 'nor',
                    'so', 'yet', 'both', 'either', 'neither', 'not', 'only',
                    'very', 'just', 'also', 'now', 'here', 'there', 'when',
                    'where', 'why', 'how', 'all', 'each', 'every', 'any',
                    'some', 'no', 'more', 'most', 'other', 'such', 'own',
                    'same', 'than', 'too', 'very', 'just'}

        words = re.findall(r'\b[a-zA-Z]{3,}\b', claim.lower())
        terms = [w for w in words if w not in stopwords]
        return terms[:5]  # Top 5 terms

    def query(self, claim: str, context: Optional[str] = None) -> EvidenceResult:
        start_time = time.time()

        try:
            # Search for relevant articles
            search_terms = self._extract_search_terms(claim)
            search_query = " ".join(search_terms)

            params = {
                "action": "query",
                "list": "search",
                "srsearch": search_query,
                "srlimit": 3,
                "format": "json",
            }

            url = f"{self.api_url}?{urlencode(params)}"
            req = urllib.request.Request(url, headers={"User-Agent": "ARAW-Evidence-Engine/1.0"})

            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())

            search_results = data.get("query", {}).get("search", [])

            if not search_results:
                return EvidenceResult(
                    source_name=self.name,
                    source_type=self.source_type,
                    reliability_tier=self.reliability_tier,
                    content="",
                    error="No relevant Wikipedia articles found",
                    retrieval_time=time.time() - start_time,
                    cost_incurred=self.accessibility,
                )

            # Get extracts from top results
            page_ids = [str(r["pageid"]) for r in search_results]

            params = {
                "action": "query",
                "pageids": "|".join(page_ids),
                "prop": "extracts|info",
                "exintro": True,
                "explaintext": True,
                "exsentences": 5,
                "inprop": "url",
                "format": "json",
            }

            url = f"{self.api_url}?{urlencode(params)}"
            req = urllib.request.Request(url, headers={"User-Agent": "ARAW-Evidence-Engine/1.0"})

            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())

            pages = data.get("query", {}).get("pages", {})

            content_parts = []
            citations = []

            for page_id, page in pages.items():
                title = page.get("title", "")
                extract = page.get("extract", "")
                url = page.get("fullurl", f"https://en.wikipedia.org/?curid={page_id}")

                if extract:
                    content_parts.append(f"**{title}**: {extract}")
                    citations.append(url)

            content = "\n\n".join(content_parts)

            return EvidenceResult(
                source_name=self.name,
                source_type=self.source_type,
                reliability_tier=self.reliability_tier,
                content=content,
                citations=citations,
                confidence=0.7 if content else 0.0,
                relevance=0.6,  # Wikipedia is general, moderate relevance
                retrieval_time=time.time() - start_time,
                cost_incurred=self.accessibility,
                raw_response=data,
            )

        except Exception as e:
            return EvidenceResult(
                source_name=self.name,
                source_type=self.source_type,
                reliability_tier=self.reliability_tier,
                content="",
                error=str(e),
                retrieval_time=time.time() - start_time,
                cost_incurred=self.accessibility,
            )


class WikidataSource(EvidenceSource):
    """Wikidata SPARQL for structured data"""

    name = "Wikidata"
    source_type = "knowledge_base"
    reliability_tier = "raw_data"
    tier = 1

    def __init__(self):
        super().__init__()
        self.accessibility = AccessibilityCost(
            time="immediate", cost="free", skill="basic", availability="public"
        )
        self.endpoint = "https://query.wikidata.org/sparql"

    def can_query(self, claim: str) -> bool:
        # Wikidata is good for factual claims about entities
        factual_indicators = ['population', 'gdp', 'area', 'founded', 'born', 'died',
                             'capital', 'country', 'president', 'ceo', 'number of']
        return any(ind in claim.lower() for ind in factual_indicators)

    def estimate_relevance(self, claim: str) -> float:
        if self.can_query(claim):
            return 0.8
        return 0.2

    def query(self, claim: str, context: Optional[str] = None) -> EvidenceResult:
        start_time = time.time()

        # For now, return a placeholder - SPARQL query generation is complex
        # TODO: Implement LLM-based SPARQL generation

        return EvidenceResult(
            source_name=self.name,
            source_type=self.source_type,
            reliability_tier=self.reliability_tier,
            content="",
            error="Wikidata SPARQL query generation not yet implemented",
            retrieval_time=time.time() - start_time,
            cost_incurred=self.accessibility,
        )


class WorldBankSource(EvidenceSource):
    """World Bank Open Data API"""

    name = "World Bank"
    source_type = "web_api"
    reliability_tier = "raw_data"
    tier = 1

    def __init__(self):
        super().__init__()
        self.accessibility = AccessibilityCost(
            time="immediate", cost="free", skill="none", availability="public"
        )
        self.api_url = "https://api.worldbank.org/v2"

    def can_query(self, claim: str) -> bool:
        # World Bank is good for economic/development indicators
        indicators = ['gdp', 'poverty', 'population', 'life expectancy', 'literacy',
                     'unemployment', 'inflation', 'trade', 'debt', 'aid',
                     'education', 'health', 'income', 'growth', 'development']
        return any(ind in claim.lower() for ind in indicators)

    def estimate_relevance(self, claim: str) -> float:
        if self.can_query(claim):
            return 0.85
        return 0.1

    def query(self, claim: str, context: Optional[str] = None) -> EvidenceResult:
        start_time = time.time()

        try:
            # Search for relevant indicators
            # Using a simple keyword match to find indicators
            search_term = claim.lower()

            # Map common terms to World Bank indicator codes
            indicator_map = {
                'poverty': 'SI.POV.DDAY',  # Poverty headcount ratio
                'gdp': 'NY.GDP.MKTP.CD',  # GDP current USD
                'population': 'SP.POP.TOTL',  # Total population
                'life expectancy': 'SP.DYN.LE00.IN',  # Life expectancy at birth
                'literacy': 'SE.ADT.LITR.ZS',  # Adult literacy rate
                'unemployment': 'SL.UEM.TOTL.ZS',  # Unemployment rate
                'co2': 'EN.ATM.CO2E.PC',  # CO2 emissions per capita
            }

            # Find matching indicator
            selected_indicator = None
            for term, code in indicator_map.items():
                if term in search_term:
                    selected_indicator = code
                    break

            if not selected_indicator:
                return EvidenceResult(
                    source_name=self.name,
                    source_type=self.source_type,
                    reliability_tier=self.reliability_tier,
                    content="",
                    error="No matching World Bank indicator found for this claim",
                    retrieval_time=time.time() - start_time,
                    cost_incurred=self.accessibility,
                )

            # Query the indicator for world aggregate
            url = f"{self.api_url}/country/WLD/indicator/{selected_indicator}?format=json&per_page=10&date=2015:2023"

            req = urllib.request.Request(url, headers={"User-Agent": "ARAW-Evidence-Engine/1.0"})

            with urllib.request.urlopen(req, timeout=15) as response:
                data = json.loads(response.read().decode())

            if len(data) < 2 or not data[1]:
                return EvidenceResult(
                    source_name=self.name,
                    source_type=self.source_type,
                    reliability_tier=self.reliability_tier,
                    content="",
                    error="No data returned from World Bank API",
                    retrieval_time=time.time() - start_time,
                    cost_incurred=self.accessibility,
                )

            # Format the results
            indicator_info = data[1][0] if data[1] else {}
            indicator_name = indicator_info.get("indicator", {}).get("value", selected_indicator)

            content_lines = [f"**World Bank Data: {indicator_name}**\n"]
            for entry in data[1][:5]:
                year = entry.get("date", "?")
                value = entry.get("value")
                if value is not None:
                    content_lines.append(f"- {year}: {value:,.2f}" if isinstance(value, float) else f"- {year}: {value}")

            content = "\n".join(content_lines)

            return EvidenceResult(
                source_name=self.name,
                source_type=self.source_type,
                reliability_tier=self.reliability_tier,
                content=content,
                citations=[f"https://data.worldbank.org/indicator/{selected_indicator}"],
                confidence=0.85,
                relevance=0.8,
                retrieval_time=time.time() - start_time,
                cost_incurred=self.accessibility,
                raw_response=data,
            )

        except Exception as e:
            return EvidenceResult(
                source_name=self.name,
                source_type=self.source_type,
                reliability_tier=self.reliability_tier,
                content="",
                error=str(e),
                retrieval_time=time.time() - start_time,
                cost_incurred=self.accessibility,
            )


class ArXivSource(EvidenceSource):
    """arXiv API for academic preprints"""

    name = "arXiv"
    source_type = "research_repo"
    reliability_tier = "published_analysis"
    tier = 1

    def __init__(self):
        super().__init__()
        self.accessibility = AccessibilityCost(
            time="immediate", cost="free", skill="basic", availability="public"
        )
        self.api_url = "http://export.arxiv.org/api/query"

    def can_query(self, claim: str) -> bool:
        # arXiv good for scientific/technical claims
        scientific_indicators = ['study', 'research', 'evidence', 'experiment',
                                'theory', 'model', 'algorithm', 'data', 'analysis',
                                'effect', 'impact', 'correlation', 'cause']
        return any(ind in claim.lower() for ind in scientific_indicators)

    def estimate_relevance(self, claim: str) -> float:
        if self.can_query(claim):
            return 0.7
        return 0.3

    def query(self, claim: str, context: Optional[str] = None) -> EvidenceResult:
        start_time = time.time()

        try:
            # Build search query
            search_query = claim.replace('"', '').replace("'", "")[:200]

            params = {
                "search_query": f"all:{quote_plus(search_query)}",
                "start": 0,
                "max_results": 5,
                "sortBy": "relevance",
            }

            url = f"{self.api_url}?{urlencode(params)}"
            req = urllib.request.Request(url, headers={"User-Agent": "ARAW-Evidence-Engine/1.0"})

            with urllib.request.urlopen(req, timeout=15) as response:
                data = response.read().decode()

            # Parse Atom XML (simple regex parsing)
            entries = re.findall(r'<entry>(.*?)</entry>', data, re.DOTALL)

            if not entries:
                return EvidenceResult(
                    source_name=self.name,
                    source_type=self.source_type,
                    reliability_tier=self.reliability_tier,
                    content="",
                    error="No relevant arXiv papers found",
                    retrieval_time=time.time() - start_time,
                    cost_incurred=self.accessibility,
                )

            content_parts = []
            citations = []

            for entry in entries[:3]:
                title_match = re.search(r'<title>(.*?)</title>', entry, re.DOTALL)
                summary_match = re.search(r'<summary>(.*?)</summary>', entry, re.DOTALL)
                id_match = re.search(r'<id>(.*?)</id>', entry)

                title = title_match.group(1).strip() if title_match else "Unknown"
                summary = summary_match.group(1).strip()[:500] if summary_match else ""
                arxiv_url = id_match.group(1).strip() if id_match else ""

                if title and summary:
                    content_parts.append(f"**{title}**\n{summary}...")
                    if arxiv_url:
                        citations.append(arxiv_url)

            content = "\n\n".join(content_parts)

            return EvidenceResult(
                source_name=self.name,
                source_type=self.source_type,
                reliability_tier=self.reliability_tier,
                content=content,
                citations=citations,
                confidence=0.7,
                relevance=0.65,
                retrieval_time=time.time() - start_time,
                cost_incurred=self.accessibility,
            )

        except Exception as e:
            return EvidenceResult(
                source_name=self.name,
                source_type=self.source_type,
                reliability_tier=self.reliability_tier,
                content="",
                error=str(e),
                retrieval_time=time.time() - start_time,
                cost_incurred=self.accessibility,
            )


class PubMedSource(EvidenceSource):
    """PubMed API for biomedical literature"""

    name = "PubMed"
    source_type = "research_repo"
    reliability_tier = "published_analysis"
    tier = 1

    def __init__(self):
        super().__init__()
        self.accessibility = AccessibilityCost(
            time="immediate", cost="free", skill="basic", availability="public"
        )
        self.search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        self.fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    def can_query(self, claim: str) -> bool:
        # PubMed good for health/medical claims
        health_indicators = ['health', 'disease', 'treatment', 'drug', 'medicine',
                            'clinical', 'patient', 'symptom', 'diagnosis', 'therapy',
                            'mortality', 'morbidity', 'cancer', 'heart', 'brain',
                            'vaccine', 'infection', 'virus', 'bacteria']
        return any(ind in claim.lower() for ind in health_indicators)

    def estimate_relevance(self, claim: str) -> float:
        if self.can_query(claim):
            return 0.85
        return 0.2

    def query(self, claim: str, context: Optional[str] = None) -> EvidenceResult:
        start_time = time.time()

        try:
            # Search for relevant articles
            search_query = claim.replace('"', '').replace("'", "")[:200]

            params = {
                "db": "pubmed",
                "term": search_query,
                "retmax": 5,
                "retmode": "json",
                "sort": "relevance",
            }

            url = f"{self.search_url}?{urlencode(params)}"
            req = urllib.request.Request(url, headers={"User-Agent": "ARAW-Evidence-Engine/1.0"})

            with urllib.request.urlopen(req, timeout=15) as response:
                data = json.loads(response.read().decode())

            id_list = data.get("esearchresult", {}).get("idlist", [])

            if not id_list:
                return EvidenceResult(
                    source_name=self.name,
                    source_type=self.source_type,
                    reliability_tier=self.reliability_tier,
                    content="",
                    error="No relevant PubMed articles found",
                    retrieval_time=time.time() - start_time,
                    cost_incurred=self.accessibility,
                )

            # Fetch article summaries
            params = {
                "db": "pubmed",
                "id": ",".join(id_list[:3]),
                "retmode": "xml",
                "rettype": "abstract",
            }

            url = f"{self.fetch_url}?{urlencode(params)}"
            req = urllib.request.Request(url, headers={"User-Agent": "ARAW-Evidence-Engine/1.0"})

            with urllib.request.urlopen(req, timeout=15) as response:
                xml_data = response.read().decode()

            # Simple XML parsing
            articles = re.findall(r'<PubmedArticle>(.*?)</PubmedArticle>', xml_data, re.DOTALL)

            content_parts = []
            citations = []

            for article in articles[:3]:
                title_match = re.search(r'<ArticleTitle>(.*?)</ArticleTitle>', article)
                abstract_match = re.search(r'<AbstractText[^>]*>(.*?)</AbstractText>', article)
                pmid_match = re.search(r'<PMID[^>]*>(.*?)</PMID>', article)

                title = title_match.group(1) if title_match else "Unknown"
                abstract = abstract_match.group(1)[:400] if abstract_match else "No abstract"
                pmid = pmid_match.group(1) if pmid_match else ""

                content_parts.append(f"**{title}**\n{abstract}...")
                if pmid:
                    citations.append(f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/")

            content = "\n\n".join(content_parts)

            return EvidenceResult(
                source_name=self.name,
                source_type=self.source_type,
                reliability_tier=self.reliability_tier,
                content=content,
                citations=citations,
                confidence=0.75,
                relevance=0.7,
                retrieval_time=time.time() - start_time,
                cost_incurred=self.accessibility,
            )

        except Exception as e:
            return EvidenceResult(
                source_name=self.name,
                source_type=self.source_type,
                reliability_tier=self.reliability_tier,
                content="",
                error=str(e),
                retrieval_time=time.time() - start_time,
                cost_incurred=self.accessibility,
            )


# ============================================================================
# TIER 2 SOURCES: AI-Powered Search
# ============================================================================

class LLMSynthesisSource(EvidenceSource):
    """Use LLM to synthesize knowledge (with epistemic caveats)"""

    name = "LLM Synthesis"
    source_type = "model_output"
    reliability_tier = "model_output"
    tier = 2

    def __init__(self, api_key: str, model: str = DEFAULT_MODEL):
        super().__init__()
        self.api_key = api_key
        self.model = model
        self.accessibility = AccessibilityCost(
            time="immediate", cost="low", skill="none", availability="public"
        )

    def can_query(self, claim: str) -> bool:
        return True  # LLM can attempt any claim

    def query(self, claim: str, context: Optional[str] = None) -> EvidenceResult:
        start_time = time.time()

        system_prompt = """You are an evidence synthesis assistant with EPISTEMIC CARE.

CRITICAL RULES:
1. Only state what you have high confidence about from your training data
2. Clearly distinguish between: facts, expert consensus, contested claims, and speculation
3. Cite specific sources when possible (organizations, studies, datasets)
4. Explicitly state uncertainty and limitations
5. Do NOT guess or make up specific numbers/statistics

For the given claim, provide:
1. What is the current expert consensus (if any)?
2. What evidence supports or contradicts this claim?
3. What are the key uncertainties?
4. What sources would be authoritative on this topic?

Be concise but thorough."""

        user_prompt = f"""Claim to evaluate: "{claim}"

{f'Context: {context}' if context else ''}

Provide an evidence synthesis with proper epistemic caveats."""

        try:
            payload = {
                "model": self.model,
                "max_output_tokens": 1500,
                "input": [
                    {"role": "system", "content": [{"type": "input_text", "text": system_prompt}]},
                    {"role": "user", "content": [{"type": "input_text", "text": user_prompt}]},
                ],
            }

            with tempfile.NamedTemporaryFile("w", delete=False, suffix=".json") as f:
                json.dump(payload, f)
                payload_path = f.name

            cmd = [
                "curl", "-sS", "https://api.openai.com/v1/responses",
                "-H", f"Authorization: Bearer {self.api_key}",
                "-H", "Content-Type: application/json",
                "-d", f"@{payload_path}",
                "--max-time", "60"
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
            Path(payload_path).unlink(missing_ok=True)

            resp = json.loads(result.stdout)

            # Extract text from response
            text = None
            if "output" in resp:
                for item in resp.get("output", []):
                    for c in item.get("content", []):
                        if isinstance(c, dict) and c.get("type") in ("output_text", "text"):
                            text = c.get("text", "").strip()
                            if text:
                                break
                    if text:
                        break

            if not text:
                return EvidenceResult(
                    source_name=self.name,
                    source_type=self.source_type,
                    reliability_tier=self.reliability_tier,
                    content="",
                    error="No response from LLM",
                    retrieval_time=time.time() - start_time,
                    cost_incurred=self.accessibility,
                )

            return EvidenceResult(
                source_name=self.name,
                source_type=self.source_type,
                reliability_tier=self.reliability_tier,
                content=text,
                citations=[],  # LLM doesn't provide verifiable citations
                confidence=0.5,  # Model output has inherent uncertainty
                relevance=0.8,
                retrieval_time=time.time() - start_time,
                cost_incurred=self.accessibility,
            )

        except Exception as e:
            return EvidenceResult(
                source_name=self.name,
                source_type=self.source_type,
                reliability_tier=self.reliability_tier,
                content="",
                error=str(e),
                retrieval_time=time.time() - start_time,
                cost_incurred=self.accessibility,
            )


# ============================================================================
# EVIDENCE ENGINE: Cascade Orchestration
# ============================================================================

class EvidenceEngine:
    """Orchestrates evidence gathering through tiered cascade"""

    def __init__(self, api_key: Optional[str] = None, model: str = DEFAULT_MODEL):
        self.api_key = api_key or read_api_key()
        self.model = model

        # Initialize sources by tier
        self.sources_by_tier: Dict[int, List[EvidenceSource]] = {
            1: [
                WikipediaSource(),
                WorldBankSource(),
                ArXivSource(),
                PubMedSource(),
            ],
            2: [],
            3: [],
        }

        # Add LLM source if API key available
        if self.api_key:
            self.sources_by_tier[2].append(LLMSynthesisSource(self.api_key, model))

        # Cache for results
        self.cache: Dict[str, List[EvidenceResult]] = {}

    def _cache_key(self, claim: str) -> str:
        return hashlib.md5(claim.encode()).hexdigest()

    def get_relevant_sources(self, claim: str) -> List[Tuple[EvidenceSource, float]]:
        """Get all sources that might be relevant, with priority scores"""
        sources_with_scores = []

        for tier, sources in self.sources_by_tier.items():
            for source in sources:
                if source.can_query(claim):
                    score = source.priority_score(claim)
                    sources_with_scores.append((source, score))

        # Sort by score descending
        sources_with_scores.sort(key=lambda x: -x[1])
        return sources_with_scores

    def gather_evidence(self, claim: str, context: Optional[str] = None,
                       max_sources: int = 5, min_confidence: float = 0.5) -> List[EvidenceResult]:
        """Gather evidence from multiple sources using cascade"""

        # Check cache
        cache_key = self._cache_key(claim)
        if cache_key in self.cache:
            return self.cache[cache_key]

        results: List[EvidenceResult] = []
        epistemic_limits: List[EpistemicLimit] = []

        # Get prioritized sources
        sources_with_scores = self.get_relevant_sources(claim)

        print(f"Gathering evidence for: {claim[:60]}...")
        print(f"  Found {len(sources_with_scores)} relevant sources")

        # Query sources in priority order
        for source, score in sources_with_scores[:max_sources]:
            print(f"  Querying {source.name}...")

            result = source.query(claim, context)

            if result.error:
                print(f"    Error: {result.error}")
                epistemic_limits.append(EpistemicLimit(
                    source_name=source.name,
                    reason=result.error,
                    limit_type="query_failed",
                    possible_workarounds=["Retry later", "Try alternative query"],
                ))
            elif result.content:
                print(f"    Got {len(result.content)} chars, confidence={result.confidence:.2f}")
                results.append(result)

        # Cache results
        self.cache[cache_key] = results

        return results

    def synthesize(self, claim: str, results: List[EvidenceResult]) -> EvidenceSynthesis:
        """Synthesize multiple evidence results into coherent summary"""

        if not results:
            return EvidenceSynthesis(
                claim=claim,
                summary="No evidence could be gathered for this claim.",
                overall_confidence=0.0,
                evidence_count=0,
            )

        # Group by agreement (simplified - just combines all)
        all_content = []
        all_citations = []
        all_sources = []

        for r in results:
            if r.content:
                all_content.append(f"[{r.source_name}]: {r.content[:500]}")
                all_citations.extend(r.citations)
                all_sources.append(r.source_name)

        # Calculate overall confidence (weighted average)
        total_weight = sum(r.overall_score() for r in results if r.content)
        total_confidence = sum(r.confidence * r.overall_score() for r in results if r.content)
        overall_confidence = total_confidence / total_weight if total_weight > 0 else 0.0

        summary = "\n\n".join(all_content)

        return EvidenceSynthesis(
            claim=claim,
            summary=summary,
            overall_confidence=overall_confidence,
            evidence_count=len(results),
            sources_consulted=all_sources,
        )

    def gather_and_synthesize(self, claim: str, context: Optional[str] = None) -> EvidenceSynthesis:
        """Convenience method to gather and synthesize in one call"""
        results = self.gather_evidence(claim, context)
        return self.synthesize(claim, results)


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="Evidence Access Engine")
    parser.add_argument("--claim", type=str, help="Claim to gather evidence for")
    parser.add_argument("--db", type=str, help="ARAW database (for --ground-node)")
    parser.add_argument("--ground-node", type=str, help="Ground a specific ARAW node")
    parser.add_argument("--test-sources", action="store_true", help="Test all evidence sources")
    parser.add_argument("--list-sources", action="store_true", help="List available sources")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL)

    args = parser.parse_args()

    api_key = read_api_key()
    engine = EvidenceEngine(api_key, args.model)

    if args.list_sources:
        print("Available Evidence Sources:\n")
        for tier, sources in engine.sources_by_tier.items():
            print(f"Tier {tier}:")
            for source in sources:
                print(f"  - {source.name} ({source.source_type})")
                print(f"    Reliability: {source.reliability_tier}")
                print(f"    Accessibility: {source.accessibility.score():.2f}")
        return

    if args.test_sources:
        test_claim = "Global poverty has decreased over the past 30 years"
        print(f"Testing sources with claim: {test_claim}\n")

        for tier, sources in engine.sources_by_tier.items():
            print(f"\n=== Tier {tier} ===")
            for source in sources:
                print(f"\nTesting {source.name}...")
                result = source.query(test_claim)
                if result.error:
                    print(f"  ERROR: {result.error}")
                else:
                    print(f"  Content: {result.content[:200]}...")
                    print(f"  Confidence: {result.confidence}")
                    print(f"  Citations: {result.citations}")
        return

    if args.claim:
        synthesis = engine.gather_and_synthesize(args.claim)

        print(f"\n{'='*70}")
        print(f"EVIDENCE SYNTHESIS")
        print(f"{'='*70}")
        print(f"\nClaim: {synthesis.claim}")
        print(f"Overall Confidence: {synthesis.overall_confidence:.2f}")
        print(f"Sources Consulted: {', '.join(synthesis.sources_consulted)}")
        print(f"\n--- Summary ---\n{synthesis.summary}")
        return

    if args.ground_node and args.db:
        # Import ARAW engine and ground the node with real evidence
        from araw_engine import ARAWEngine

        araw = ARAWEngine(args.db)
        cursor = araw.conn.cursor()
        cursor.execute("SELECT claim FROM nodes WHERE id = ?", (args.ground_node,))
        row = cursor.fetchone()

        if not row:
            print(f"Node {args.ground_node} not found")
            return

        claim = row['claim']
        print(f"Grounding node: {claim[:80]}...")

        synthesis = engine.gather_and_synthesize(claim)

        print(f"\n{'='*70}")
        print(f"EVIDENCE FOR NODE {args.ground_node}")
        print(f"{'='*70}")
        print(f"\nClaim: {claim}")
        print(f"Overall Confidence: {synthesis.overall_confidence:.2f}")
        print(f"Sources Consulted: {', '.join(synthesis.sources_consulted)}")
        print(f"\n--- Evidence ---\n{synthesis.summary[:2000]}")
        return

    print("Use --claim, --test-sources, --list-sources, or --ground-node")
    print("Run with --help for options")


if __name__ == "__main__":
    main()

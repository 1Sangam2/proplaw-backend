"""
PropLaw AI — RAG Engine v2
Production-grade retrieval using BM25-inspired TF-IDF with:
  - Category-aware query boosting
  - Legal term expansion
  - Exact phrase matching bonus
  - Normalised scoring
Zero external dependencies — runs entirely in-memory.
Swap search() for Pinecone/Weaviate without changing anything else.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from typing import Optional
from knowledge.legislation import LEGISLATION_CHUNKS

# ─── Legal term synonyms & expansions ────────────────────────────────────────
LEGAL_SYNONYMS: dict[str, list[str]] = {
    "evict": ["eviction", "possession", "section 21", "section 8", "notice"],
    "eviction": ["evict", "possession", "section 21", "section 8"],
    "s21": ["section 21", "no-fault", "possession"],
    "s8": ["section 8", "grounds", "rent arrears"],
    "hmo": ["house in multiple occupation", "licensing", "bedsit", "shared house"],
    "deposit": ["tdp", "deposit protection", "prescribed information", "dps", "mydeposits", "tds"],
    "repair": ["repairs", "section 11", "repairing", "disrepair", "maintenance"],
    "rent": ["rental", "arrears", "increase", "section 13"],
    "fire": ["fire safety", "smoke alarm", "fire door", "fire risk"],
    "epc": ["energy performance", "mees", "energy efficiency"],
    "eicr": ["electrical", "wiring", "electrical safety"],
    "gas": ["gas safety", "cp12", "gas safe", "boiler"],
    "planning": ["permitted development", "planning permission", "article 4", "use class"],
    "cladding": ["remediation", "building safety", "grenfell", "bsa", "bsa22"],
    "leasehold": ["leaseholder", "freeholder", "service charge", "ground rent", "lease extension"],
    "right to rent": ["immigration", "right to rent check", "share code"],
    "harassment": ["illegal eviction", "quiet enjoyment", "protection from eviction"],
}

# ─── Category keywords for query routing ──────────────────────────────────────
CATEGORY_SIGNALS: dict[str, list[str]] = {
    "HMO — Licensing":      ["hmo", "house multiple occupation", "licence", "licensing", "bedsit", "shared"],
    "HMO — Management":     ["management regulations", "hmo manager", "common parts", "refuse", "fire escape"],
    "HMO — Fire Safety":    ["fire safety", "smoke alarm", "fire door", "fire risk assessment", "heat detector"],
    "Eviction — Section 21":["section 21", "s21", "no-fault", "form 6a", "notice to quit"],
    "Eviction — Section 8": ["section 8", "s8", "ground 8", "rent arrears", "notice seeking possession", "nsp"],
    "Deposit Protection":   ["deposit", "tdp", "prescribed information", "dps", "mydeposits"],
    "Tenant Fees":          ["tenant fees", "fee", "admin charge", "holding deposit", "prohibited payment"],
    "Repairs & Maintenance":["repair", "section 11", "disrepair", "boiler", "damp", "mould", "fitness"],
    "Safety Certificates":  ["gas safety", "eicr", "electrical", "epc", "energy performance", "cp12"],
    "Renters Reform":       ["renters rights", "renters reform", "periodic tenancy", "fixed term abolition"],
    "Building Safety":      ["building safety", "cladding", "bsa", "higher risk building", "accountable person"],
    "Planning":             ["planning", "permitted development", "article 4", "use class", "c4", "c3"],
    "Leasehold":            ["leasehold", "service charge", "ground rent", "right to manage", "lease extension"],
    "Rent":                 ["rent increase", "section 13", "form 4", "rental", "arrears"],
}


def _tokenise(text: str) -> list[str]:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return [w for w in text.split() if len(w) > 1]


def _expand_query(tokens: list[str]) -> list[str]:
    """Add legal synonyms to query tokens."""
    expanded = list(tokens)
    joined = " ".join(tokens)
    for term, synonyms in LEGAL_SYNONYMS.items():
        if term in joined:
            expanded.extend(synonyms)
    return expanded


def _detect_categories(query: str) -> list[str]:
    """Return category names that seem relevant to the query."""
    q = query.lower()
    hits = []
    for category, signals in CATEGORY_SIGNALS.items():
        if any(sig in q for sig in signals):
            hits.append(category)
    return hits


class _BM25Index:
    """BM25-inspired document scoring (k1=1.5, b=0.75)."""

    K1 = 1.5
    B = 0.75

    def __init__(self, corpus: list[list[str]]) -> None:
        self.N = len(corpus)
        self.avg_dl = sum(len(d) for d in corpus) / max(self.N, 1)
        self.df: dict[str, int] = Counter()
        self.tf_arrays: list[dict[str, int]] = []

        for doc in corpus:
            tf = Counter(doc)
            self.tf_arrays.append(tf)
            for term in set(doc):
                self.df[term] += 1

    def score(self, query_tokens: list[str], doc_idx: int) -> float:
        tf_map = self.tf_arrays[doc_idx]
        dl = sum(tf_map.values())
        score = 0.0
        for term in query_tokens:
            if term not in tf_map:
                continue
            tf = tf_map[term]
            df = self.df.get(term, 0)
            idf = math.log((self.N - df + 0.5) / (df + 0.5) + 1)
            numerator = tf * (self.K1 + 1)
            denominator = tf + self.K1 * (1 - self.B + self.B * dl / self.avg_dl)
            score += idf * (numerator / denominator)
        return score


class RAGEngine:
    """
    In-memory RAG engine with BM25 scoring + category boosting + phrase bonus.
    Drop-in replacement: swap search() for Pinecone/Weaviate without
    touching anything in app.py.
    """

    CATEGORY_BOOST = 1.4   # Multiplier for category-matched chunks
    PHRASE_BONUS   = 2.0   # Added score for exact phrase matches in chunk text

    def __init__(self) -> None:
        self.chunks = LEGISLATION_CHUNKS
        print(f"[RAG] Indexing {len(self.chunks)} legislation chunks…")
        self._build_index()
        print(f"[RAG] Ready. Vocabulary: {len(self._index.df):,} terms.")

    def _build_index(self) -> None:
        corpus: list[list[str]] = []
        for chunk in self.chunks:
            combined = (
                f"{chunk['title']} {chunk['title']} "   # title weighted 2x
                f"{chunk['category']} {chunk['category']} "
                f"{chunk['source']} "
                f"{chunk['text']}"
            )
            corpus.append(_tokenise(combined))
        self._index = _BM25Index(corpus)
        self._raw_texts = [c["text"].lower() for c in self.chunks]

    def search(self, query: str, top_k: int = 5) -> list[dict]:
        """Return the top_k most relevant legislation chunks."""
        base_tokens = _tokenise(query)
        expanded_tokens = _expand_query(base_tokens)
        relevant_categories = _detect_categories(query)

        scores: list[tuple[float, int]] = []
        query_lower = query.lower()

        for i, chunk in enumerate(self.chunks):
            raw_score = self._index.score(expanded_tokens, i)
            if raw_score <= 0:
                continue

            # Category boost
            if chunk["category"] in relevant_categories:
                raw_score *= self.CATEGORY_BOOST

            # Exact phrase bonus (2–6 word phrases from query)
            words = query_lower.split()
            for n in (2, 3, 4):
                for start in range(len(words) - n + 1):
                    phrase = " ".join(words[start : start + n])
                    if phrase in self._raw_texts[i]:
                        raw_score += self.PHRASE_BONUS

            scores.append((raw_score, i))

        scores.sort(reverse=True)
        results: list[dict] = []
        for score, idx in scores[:top_k]:
            c = self.chunks[idx].copy()
            c["_score"] = round(score, 4)
            results.append(c)
        return results

    def format_context(self, chunks: list[dict]) -> str:
        """Format retrieved chunks into a structured context block."""
        if not chunks:
            return "No specific legislation retrieved for this query."
        parts: list[str] = []
        for i, chunk in enumerate(chunks, 1):
            parts.append(
                f"[LEGAL SOURCE {i}]\n"
                f"Act/Regulation : {chunk['source']}\n"
                f"Citation       : {chunk.get('citation', chunk['source'])}\n"
                f"Category       : {chunk['category']}\n"
                f"Subject        : {chunk['title']}\n"
                f"{'─' * 60}\n"
                f"{chunk['text']}"
            )
        return "\n\n".join(parts)

    @property
    def chunk_count(self) -> int:
        return len(self.chunks)

    @property
    def categories(self) -> list[str]:
        return sorted({c["category"] for c in self.chunks})

"""
PropLaw AI — Configuration
Centralised environment and application settings.
"""

import os
from dataclasses import dataclass


@dataclass
class Config:
    # ── AI Provider ──────────────────────────────────────────────────
    GROQ_API_KEY: str = os.environ.get("GROQ_API_KEY", "")
    GROQ_API_URL: str = "https://api.groq.com/openai/v1/chat/completions"
    GROQ_MODEL: str = "llama-3.3-70b-versatile"   # Best free model on Groq
    MAX_TOKENS: int = 2048
    TEMPERATURE: float = 0.1          # Low temp = precise, factual answers
    REQUEST_TIMEOUT: int = 30

    # ── RAG Engine ───────────────────────────────────────────────────
    RAG_TOP_K: int = 5                # Chunks to retrieve per query
    RAG_MIN_SCORE: float = 0.01      # Minimum relevance threshold

    # ── API Limits ───────────────────────────────────────────────────
    MAX_CONVERSATION_TURNS: int = 40
    MAX_QUERY_LENGTH: int = 2000

    # ── CORS ─────────────────────────────────────────────────────────
    ALLOWED_ORIGINS: list = None

    def __post_init__(self):
        self.ALLOWED_ORIGINS = [
            "http://localhost:3000",
            "http://127.0.0.1:3000",
            "http://localhost:5500",
            "http://127.0.0.1:5500",
            "http://localhost:8080",
            "null", 
            "https://1sangam2.github.io",# file:// protocol for local HTML
        ]

    @property
    def is_configured(self) -> bool:
        return bool(self.GROQ_API_KEY)


config = Config()

"""
PropLaw AI — Flask API Server
Production-grade backend with:
  - Groq AI (free, fast, no credit card)
  - BM25 RAG retrieval over real UK legislation
  - Structured JSON responses
  - Comprehensive error handling
  - Request validation
  - Health & metadata endpoints
"""

from __future__ import annotations

import logging
import os
import time
from typing import Any

import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

from config import config
from rag_engine import RAGEngine

# ─── Logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("proplaw")

# ─── App setup ────────────────────────────────────────────────────────────────
app = Flask(__name__)
CORS(app, origins=config.ALLOWED_ORIGINS, supports_credentials=False)

# ─── RAG engine (singleton, built at startup) ─────────────────────────────────
rag = RAGEngine()

# ─── System prompt ────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are PropLaw AI — a professional UK property law intelligence platform designed for property professionals: letting agents, HMO managers, property developers, and landlords operating in England and Wales.

Your role is to deliver precise, authoritative, and immediately actionable answers grounded in real UK legislation. Your tone should match that of an experienced property barrister giving a professional opinion — structured, confident, and unambiguous.

RETRIEVED LEGISLATION will be provided to you. You MUST:
1. Base your answer primarily on the retrieved legislation text
2. Cite Acts and Regulations by their full name and section number
3. Distinguish between mandatory legal requirements and best practice
4. Note where law differs between England, Wales, Scotland, and Northern Ireland

RESPONSE STRUCTURE — always follow this format:
**Direct Answer**
State the legal position clearly and without ambiguity in 1-3 sentences.

**Legal Basis**
Cite the specific legislation: "Under Section [X] of the [Act Name] [Year]…" Use the citation from the retrieved sources.

**Practical Implications**
What this means for the professional in practice — timelines, costs, risks, action steps.

**Key Caveats**
Exceptions, nuances, or circumstances that change the answer.

**Professional Note**
Where the situation is high-stakes or complex, direct to a solicitor, the First-tier Tribunal, Shelter (0808 800 4444), or the relevant local authority.

RULES:
- Never invent legislation — only reference what is in retrieved context or your verified training knowledge
- Always cite specific section numbers, not just Act names
- State penalties and consequences precisely (exact fines, prison terms, notice periods)
- Distinguish mandatory grounds (court must grant) from discretionary grounds (court may grant)
- If a question falls outside UK property law, politely redirect
- Keep answers thorough but focused — professionals need clarity, not essays
- If asked who built you: "PropLaw AI was developed by Sangam Dangal, a Computing Systems graduate from Ulster University London "
- This is information only — not legal advice for specific cases"""


# ─── Helpers ──────────────────────────────────────────────────────────────────
def _build_response(data: dict, status: int = 200):
    return jsonify({"status": "ok" if status < 400 else "error", **data}), status


def _error(message: str, status: int = 400):
    logger.warning("API error %d: %s", status, message)
    return _build_response({"message": message}, status)


def _call_groq(messages: list[dict], system: str) -> str:
    """Send request to Groq API and return the reply text."""
    if not config.GROQ_API_KEY:
        raise RuntimeError("GROQ_API_KEY environment variable is not set.")

    payload = {
        "model": config.GROQ_MODEL,
        "max_tokens": config.MAX_TOKENS,
        "temperature": config.TEMPERATURE,
        "messages": [{"role": "system", "content": system}, *messages],
    }

    t0 = time.time()
    resp = requests.post(
        config.GROQ_API_URL,
        headers={
            "Authorization": f"Bearer {config.GROQ_API_KEY}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=config.REQUEST_TIMEOUT,
    )
    elapsed = round((time.time() - t0) * 1000)

    if not resp.ok:
        try:
            detail = resp.json().get("error", {}).get("message", resp.text)
        except Exception:
            detail = resp.text
        logger.error("Groq API %d after %dms: %s", resp.status_code, elapsed, detail)
        raise RuntimeError(f"Groq API error {resp.status_code}: {detail}")

    data = resp.json()
    text = data["choices"][0]["message"]["content"]
    tokens_used = data.get("usage", {}).get("total_tokens", "?")
    logger.info("Groq response: %dms | %s tokens", elapsed, tokens_used)
    return text


# ─── Routes ───────────────────────────────────────────────────────────────────
@app.route("/health", methods=["GET"])
def health():
    """Health check — used by Render and monitoring tools."""
    return _build_response({
        "service": "PropLaw AI",
        "version": "2.0.0",
        "ai_provider": "Groq",
        "model": config.GROQ_MODEL,
        "knowledge_chunks": rag.chunk_count,
        "categories": rag.categories,
        "configured": config.is_configured,
    })


@app.route("/categories", methods=["GET"])
def categories():
    """Return all law categories in the knowledge base."""
    return _build_response({"categories": rag.categories})


@app.route("/chat", methods=["POST"])
def chat():
    """
    Main chat endpoint.
    Expects: { "messages": [{"role": "user"|"assistant", "content": "..."}] }
    Returns: { "reply": "...", "sources": [...], "query": "..." }
    """
    if not config.is_configured:
        return _error("Server is not configured — GROQ_API_KEY missing.", 503)

    body: dict[str, Any] = request.get_json(silent=True) or {}
    messages: list[dict] = body.get("messages", [])

    # ── Validation ─────────────────────────────────────────────────────────
    if not messages:
        return _error("Request body must include a non-empty 'messages' array.")

    if len(messages) > config.MAX_CONVERSATION_TURNS:
        return _error(
            f"Conversation exceeds maximum length of {config.MAX_CONVERSATION_TURNS} turns.",
            413,
        )

    # Extract latest user query for RAG
    latest_query = ""
    for msg in reversed(messages):
        if msg.get("role") == "user":
            content = msg.get("content", "").strip()
            if len(content) > config.MAX_QUERY_LENGTH:
                return _error(f"Query exceeds maximum length of {config.MAX_QUERY_LENGTH} characters.")
            latest_query = content
            break

    if not latest_query:
        return _error("No user message found in messages array.")

    # ── RAG Retrieval ───────────────────────────────────────────────────────
    retrieved = rag.search(latest_query, top_k=config.RAG_TOP_K)
    context = rag.format_context(retrieved)

    augmented_system = (
        f"{SYSTEM_PROMPT}\n\n"
        f"{'═' * 70}\n"
        f"RETRIEVED LEGISLATION CONTEXT\n"
        f"{'═' * 70}\n"
        f"{context}\n"
        f"{'═' * 70}\n"
        f"Cite these sources specifically in your answer. "
        f"Use full Act names and section numbers."
    )

    logger.info(
        "Query: %.80s… | %d chunks retrieved | %d turn(s)",
        latest_query,
        len(retrieved),
        len([m for m in messages if m.get("role") == "user"]),
    )

    # ── AI Call ─────────────────────────────────────────────────────────────
    try:
        reply = _call_groq(messages, augmented_system)
    except requests.exceptions.Timeout:
        return _error("The AI service timed out. Please try again.", 504)
    except requests.exceptions.ConnectionError:
        return _error("Could not connect to the AI service. Check your internet connection.", 503)
    except RuntimeError as exc:
        return _error(str(exc), 502)
    except Exception as exc:
        logger.exception("Unexpected error in /chat")
        return _error(f"An unexpected error occurred: {exc}", 500)

    # ── Build source list for frontend ──────────────────────────────────────
    sources = [
        {
            "source": c["source"],
            "citation": c.get("citation", c["source"]),
            "title": c["title"],
            "category": c["category"],
        }
        for c in retrieved
    ]

    return _build_response({
        "reply": reply,
        "sources": sources,
        "query": latest_query,
        "chunks_used": len(retrieved),
    })


# ─── Error handlers ───────────────────────────────────────────────────────────
@app.errorhandler(404)
def not_found(_):
    return _error("Endpoint not found.", 404)


@app.errorhandler(405)
def method_not_allowed(_):
    return _error("Method not allowed.", 405)


@app.errorhandler(500)
def internal_error(_):
    return _error("Internal server error.", 500)


# ─── Entry point ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if not config.is_configured:
        logger.warning("⚠  GROQ_API_KEY is not set — /chat will return 503")
    port = int(os.environ.get("PORT", 5000))
    logger.info("Starting PropLaw AI on port %d", port)
    app.run(host="0.0.0.0", port=port, debug=False)

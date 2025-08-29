# AI Engine Service

A lightweight, modular Python service for AI engine integration. It exposes a FastAPI server with pluggable providers (LLMs, embeddings), vector stores (ChromaDB/Pinecone), caching, simple queue, and structured logging/metrics.

## Quick Start

1) Create and activate a virtualenv
- python -m venv .venv && source .venv/bin/activate

2) Install dependencies
- pip install -r ai_engine/requirements.txt

3) Configure environment (copy + edit)
- cp .env.example .env   # root for frontend
- cp ai_engine/.env.example ai_engine/.env  # backend service

4) Run the API server
- uvicorn ai_engine.server.main:app --reload --port 8001

## Endpoints
- GET /health
- POST /chat  { messages: [{role, content}], model?, stream? }
- POST /embeddings  { input: string|string[], model? }
- POST /ingest  { texts: string[], namespace? }  # store in vector DB
- POST /query   { query: string, top_k?, namespace? }  # semantic search

## Structure
- ai_engine/config.py                # env + settings
- ai_engine/core/interfaces.py       # protocol/abstractions
- ai_engine/providers/*              # provider wrappers (OpenAI, etc.)
- ai_engine/vector/*                 # vector stores (Chroma, Pinecone)
- ai_engine/cache/*                  # cache backends (memory, redis)
- ai_engine/queue/*                  # queue backends (memory, rq)
- ai_engine/monitoring/*             # logging + metrics
- ai_engine/server/main.py           # FastAPI app composition

## Notes
- Providers are optional; code falls back to stubs when API keys not set.
- Caching defaults to in-memory TTL cache; Redis can be enabled via env.
- Queue defaults to in-memory; swap in RQ/Celery in adapters if needed.
- Metrics endpoints are stubbed; integrate Prometheus client if desired.

from __future__ import annotations

import hashlib
import json
import time
from typing import Any, Dict, Iterable, List, Optional, Sequence

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from ..config import settings
from ..core.interfaces import CacheBackend, EmbeddingsClient, LLMClient, QueueBackend, VectorDoc, VectorStore
from ..providers import NullEmbeddings, NullLLM, OpenAIEmbeddings, OpenAILLM
from ..vector import ChromaVectorStore, MemoryVectorStore, PineconeVectorStore
from ..cache import InMemoryCache, RedisCache
from ..queue import InMemoryQueue, RQQueue
from ..monitoring import Metrics
from ..monitoring.logging_setup import get_logger


logger = get_logger(level=settings.log_level)
metrics = Metrics(enabled=settings.enable_prometheus)


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    model: Optional[str] = None
    stream: bool = False


class ChatResponse(BaseModel):
    content: str
    model: str


class EmbeddingsRequest(BaseModel):
    input: List[str] | str
    model: Optional[str] = None


class EmbeddingsResponse(BaseModel):
    embeddings: List[List[float]]


class IngestRequest(BaseModel):
    texts: List[str]
    namespace: Optional[str] = None


class QueryRequest(BaseModel):
    query: str
    top_k: int = Field(default=5, ge=1, le=50)
    namespace: Optional[str] = None


def _cache_key(prefix: str, payload: Any) -> str:
    raw = json.dumps(payload, sort_keys=True, ensure_ascii=False)
    return f"{prefix}:{hashlib.sha256(raw.encode('utf-8')).hexdigest()}"


class Container:
    def __init__(self) -> None:
        # Providers
        if settings.openai_api_key:
            llm: LLMClient = OpenAILLM(api_key=settings.openai_api_key, base_url=settings.openai_base_url)
            embed: EmbeddingsClient = OpenAIEmbeddings(api_key=settings.openai_api_key, base_url=settings.openai_base_url)
        else:
            llm = NullLLM()
            embed = NullEmbeddings()

        # Vector store
        if settings.vector_db == "chroma":
            vstore: VectorStore = ChromaVectorStore(persist_dir=settings.chroma_persist_dir)
        elif settings.vector_db == "pinecone":
            if not (settings.pinecone_api_key and settings.pinecone_index):
                raise RuntimeError("Pinecone requires PINECONE_API_KEY and PINECONE_INDEX")
            vstore = PineconeVectorStore(api_key=settings.pinecone_api_key, environment=(settings.pinecone_environment or ""), index_name=settings.pinecone_index)
        else:
            vstore = MemoryVectorStore()

        # Cache
        if settings.cache_backend == "redis":
            cache: CacheBackend = RedisCache(url=settings.redis_url, default_ttl_seconds=settings.cache_ttl_seconds)
        else:
            cache = InMemoryCache(default_ttl_seconds=settings.cache_ttl_seconds)

        # Queue
        if settings.queue_backend == "rq":
            queue: QueueBackend = RQQueue(redis_url=settings.rq_redis_url)
        else:
            queue = InMemoryQueue()

        self.llm = llm
        self.embed = embed
        self.vstore = vstore
        self.cache = cache
        self.queue = queue


container = Container()

app = FastAPI(title="AI Engine Service", version="0.1.0")


@app.get("/health")
def health():
    return {
        "status": "ok",
        "env": settings.env,
        "vector_db": settings.vector_db,
        "cache": settings.cache_backend,
        "queue": settings.queue_backend,
        "provider": "openai" if settings.openai_api_key else "null",
    }


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    start = time.time()
    metrics.count(path="/chat", method="POST")
    cache_key = _cache_key("chat", {"messages": [m.model_dump() for m in req.messages], "model": req.model})
    cached = container.cache.get(cache_key)
    if cached:
        logger.info("cache_hit", key=cache_key)
        metrics.observe_latency(path="/chat", seconds=time.time() - start)
        return ChatResponse(**cached)

    try:
        result = container.llm.chat(messages=[m.model_dump() for m in req.messages], model=req.model, stream=False)
    except Exception as e:
        logger.error("chat_error", error=str(e))
        raise HTTPException(status_code=500, detail=str(e))

    resp = ChatResponse(content=result.get("content", ""), model=result.get("model", req.model or "unknown"))
    container.cache.set(cache_key, resp.model_dump(), ttl_seconds=settings.cache_ttl_seconds)
    metrics.observe_latency(path="/chat", seconds=time.time() - start)
    return resp


@app.post("/embeddings", response_model=EmbeddingsResponse)
def embeddings(req: EmbeddingsRequest):
    start = time.time()
    metrics.count(path="/embeddings", method="POST")
    inputs = req.input if isinstance(req.input, list) else [req.input]
    cache_key = _cache_key("emb", {"inputs": inputs, "model": req.model})
    cached = container.cache.get(cache_key)
    if cached:
        logger.info("cache_hit", key=cache_key)
        metrics.observe_latency(path="/embeddings", seconds=time.time() - start)
        return EmbeddingsResponse(**cached)

    try:
        vectors = container.embed.embed(inputs=inputs, model=req.model)
    except Exception as e:
        logger.error("embeddings_error", error=str(e))
        raise HTTPException(status_code=500, detail=str(e))

    resp = EmbeddingsResponse(embeddings=vectors)
    container.cache.set(cache_key, resp.model_dump(), ttl_seconds=settings.cache_ttl_seconds)
    metrics.observe_latency(path="/embeddings", seconds=time.time() - start)
    return resp


@app.post("/ingest")
def ingest(req: IngestRequest):
    metrics.count(path="/ingest", method="POST")
    texts = req.texts
    try:
        vectors = container.embed.embed(inputs=texts)
        docs: List[VectorDoc] = []
        for i, t in enumerate(texts):
            docs.append(VectorDoc(id=f"doc-{i}", text=t, metadata={"embedding": vectors[i], "text": t}))
        container.vstore.upsert(docs, namespace=req.namespace or settings.vector_namespace)
        logger.info("ingest_ok", count=len(texts), ns=req.namespace or settings.vector_namespace)
        return {"ok": True, "count": len(texts)}
    except Exception as e:
        logger.error("ingest_error", error=str(e))
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/query")
def query(req: QueryRequest):
    metrics.count(path="/query", method="POST")
    ns = req.namespace or settings.vector_namespace
    try:
        # If Pinecone adapter is used, prefer embedding-aware query
        if isinstance(container.vstore, PineconeVectorStore):
            qvec = container.embed.embed([req.query])[0]
            results = container.vstore.query_with_embedding(qvec, top_k=req.top_k, namespace=ns)
        else:
            results = container.vstore.query(req.query, top_k=req.top_k, namespace=ns)
        return {
            "matches": [
                {"id": d.id, "text": d.text, "score": float(score), "metadata": d.metadata or {}}
                for (d, score) in results
            ]
        }
    except Exception as e:
        logger.error("query_error", error=str(e))
        raise HTTPException(status_code=500, detail=str(e))


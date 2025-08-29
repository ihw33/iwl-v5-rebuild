from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Settings:
    env: str = os.getenv("ENV", "development")
    host: str = os.getenv("AI_SERVICE_HOST", "0.0.0.0")
    port: int = int(os.getenv("AI_SERVICE_PORT", "8001"))

    # Providers
    openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
    openai_base_url: Optional[str] = os.getenv("OPENAI_BASE_URL")

    # Vector DB
    vector_db: str = os.getenv("VECTOR_DB", "memory")
    vector_namespace: str = os.getenv("VECTOR_NAMESPACE", "default")
    chroma_persist_dir: str = os.getenv("CHROMA_PERSIST_DIR", ".chroma")
    pinecone_api_key: Optional[str] = os.getenv("PINECONE_API_KEY")
    pinecone_environment: Optional[str] = os.getenv("PINECONE_ENVIRONMENT")
    pinecone_index: Optional[str] = os.getenv("PINECONE_INDEX")

    # Cache
    cache_backend: str = os.getenv("CACHE_BACKEND", "memory")
    cache_ttl_seconds: int = int(os.getenv("CACHE_TTL_SECONDS", "300"))
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")

    # Queue
    queue_backend: str = os.getenv("QUEUE_BACKEND", "memory")
    rq_redis_url: str = os.getenv("RQ_REDIS_URL", "redis://localhost:6379/1")

    # Monitoring
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    enable_prometheus: bool = os.getenv("ENABLE_PROMETHEUS", "false").lower() == "true"


settings = Settings()


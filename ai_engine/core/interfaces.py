from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Mapping, Optional, Protocol, Sequence, Tuple


# --------- AI Provider Interfaces ---------

class LLMClient(Protocol):
    def chat(self, messages: Sequence[Mapping[str, str]], model: Optional[str] = None, stream: bool = False, **kwargs: Any) -> Any:
        ...


class EmbeddingsClient(Protocol):
    def embed(self, inputs: Sequence[str], model: Optional[str] = None, **kwargs: Any) -> List[List[float]]:
        ...


# --------- Vector Store Interfaces ---------

@dataclass
class VectorDoc:
    id: str
    text: str
    metadata: Optional[Dict[str, Any]] = None


class VectorStore(Protocol):
    def upsert(self, docs: Iterable[VectorDoc], namespace: Optional[str] = None) -> None:
        ...

    def query(self, query: str, top_k: int = 5, namespace: Optional[str] = None) -> List[Tuple[VectorDoc, float]]:
        ...


# --------- Cache & Queue Interfaces ---------

class CacheBackend(Protocol):
    def get(self, key: str) -> Optional[Any]:
        ...

    def set(self, key: str, value: Any, ttl_seconds: Optional[int] = None) -> None:
        ...

    def delete(self, key: str) -> None:
        ...


class QueueBackend(Protocol):
    def enqueue(self, job_name: str, payload: Mapping[str, Any]) -> str:
        ...

    def dequeue(self) -> Optional[Tuple[str, Mapping[str, Any]]]:
        ...


# --------- Monitoring Interfaces ---------

class Tracer(Protocol):
    def event(self, name: str, **fields: Any) -> None:
        ...

    def time(self, name: str) -> Any:
        ...


from __future__ import annotations

import math
import uuid
from typing import Any, Dict, Iterable, List, Optional, Tuple

from ..core.interfaces import VectorDoc, VectorStore


def _cosine(a: List[float], b: List[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a)) or 1e-9
    nb = math.sqrt(sum(y * y for y in b)) or 1e-9
    return dot / (na * nb)


class MemoryVectorStore(VectorStore):
    def __init__(self) -> None:
        self._data: Dict[str, List[Tuple[VectorDoc, List[float]]]] = {}

    def upsert(self, docs: Iterable[VectorDoc], namespace: Optional[str] = None) -> None:
        ns = namespace or "default"
        bucket = self._data.setdefault(ns, [])
        for d in docs:
            emb = d.metadata.get("embedding") if d.metadata else None
            if not emb:
                # Fallback: pseudo-embed by hashing
                emb = [float((hash(d.text) >> i) & 0xFF) / 255.0 for i in range(0, 128, 8)]
            bucket.append((d, emb))

    def query(self, query: str, top_k: int = 5, namespace: Optional[str] = None) -> List[Tuple[VectorDoc, float]]:
        ns = namespace or "default"
        bucket = self._data.get(ns, [])
        qemb = [float((hash(query) >> i) & 0xFF) / 255.0 for i in range(0, 128, 8)]
        scores = [(doc, _cosine(qemb, emb)) for (doc, emb) in bucket]
        scores.sort(key=lambda t: t[1], reverse=True)
        return scores[:top_k]


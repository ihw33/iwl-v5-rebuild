from __future__ import annotations

from typing import Any, Iterable, List, Optional, Tuple

from ..core.interfaces import VectorDoc, VectorStore


class PineconeVectorStore(VectorStore):
    def __init__(self, api_key: str, environment: str, index_name: str) -> None:
        self.api_key = api_key
        self.environment = environment
        self.index_name = index_name
        self._pc = None
        self._index = None

    def _lazy_index(self):
        if self._index is None:
            try:
                from pinecone import Pinecone
            except Exception as e:  # pragma: no cover
                raise RuntimeError("pinecone-client not installed. pip install pinecone-client") from e
            self._pc = Pinecone(api_key=self.api_key)
            self._index = self._pc.Index(self.index_name)
        return self._index

    def upsert(self, docs: Iterable[VectorDoc], namespace: Optional[str] = None) -> None:
        index = self._lazy_index()
        ns = namespace or "default"
        vectors = []
        for d in docs:
            emb = d.metadata.get("embedding") if d.metadata else None
            if emb is None:
                raise ValueError("Pinecone requires explicit embeddings in metadata['embedding']")
            vectors.append({"id": d.id, "values": emb, "metadata": d.metadata or {}})
        index.upsert(vectors=vectors, namespace=ns)

    def query(self, query: str, top_k: int = 5, namespace: Optional[str] = None) -> List[Tuple[VectorDoc, float]]:
        raise NotImplementedError("Provide an embedding for the query and use query_with_embedding() instead")

    def query_with_embedding(self, embedding: List[float], top_k: int = 5, namespace: Optional[str] = None) -> List[Tuple[VectorDoc, float]]:
        index = self._lazy_index()
        ns = namespace or "default"
        res = index.query(vector=embedding, namespace=ns, top_k=top_k, include_metadata=True)
        out: List[Tuple[VectorDoc, float]] = []
        for m in res.matches or []:
            out.append((VectorDoc(id=m.id, text=m.metadata.get("text", ""), metadata=m.metadata), float(m.score or 0.0)))
        return out


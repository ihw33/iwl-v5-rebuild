from __future__ import annotations

from typing import Any, Iterable, List, Optional, Tuple

from ..core.interfaces import VectorDoc, VectorStore


class ChromaVectorStore(VectorStore):
    def __init__(self, persist_dir: str = ".chroma") -> None:
        self.persist_dir = persist_dir
        self._client = None

    def _lazy_client(self):
        if self._client is None:
            try:
                import chromadb  # type: ignore
            except Exception as e:  # pragma: no cover
                raise RuntimeError("chromadb not installed. pip install chromadb") from e
            self._client = chromadb.PersistentClient(path=self.persist_dir)
        return self._client

    def upsert(self, docs: Iterable[VectorDoc], namespace: Optional[str] = None) -> None:
        ns = namespace or "default"
        client = self._lazy_client()
        coll = client.get_or_create_collection(name=ns)
        ids = [d.id for d in docs]
        texts = [d.text for d in docs]
        metas = [d.metadata or {} for d in docs]
        coll.upsert(ids=ids, documents=texts, metadatas=metas)

    def query(self, query: str, top_k: int = 5, namespace: Optional[str] = None) -> List[Tuple[VectorDoc, float]]:
        ns = namespace or "default"
        client = self._lazy_client()
        coll = client.get_or_create_collection(name=ns)
        res = coll.query(query_texts=[query], n_results=top_k)
        out: List[Tuple[VectorDoc, float]] = []
        ids = res.get("ids", [[]])[0]
        docs = res.get("documents", [[]])[0]
        metas = res.get("metadatas", [[]])[0]
        dists = res.get("distances", [[]])[0] or [0.0] * len(ids)
        for i, t, m, dist in zip(ids, docs, metas, dists):
            out.append((VectorDoc(id=i, text=t, metadata=m), float(1.0 - dist)))
        return out


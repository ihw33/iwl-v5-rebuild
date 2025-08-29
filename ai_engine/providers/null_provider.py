from __future__ import annotations

from typing import Any, List, Mapping, Optional, Sequence


class NullLLM:
    def __init__(self, model: str = "null-llm") -> None:
        self.model = model

    def chat(self, messages: Sequence[Mapping[str, str]], model: Optional[str] = None, stream: bool = False, **kwargs: Any) -> Any:
        last = next((m for m in reversed(messages) if m.get("role") == "user"), {"content": ""})
        content = f"[stub:{model or self.model}] Echo: " + (last.get("content") or "")
        if stream:
            def _gen():
                yield {"delta": {"content": content}, "done": True}
            return _gen()
        return {"content": content, "model": model or self.model}


class NullEmbeddings:
    def __init__(self, model: str = "null-embed") -> None:
        self.model = model

    def embed(self, inputs: Sequence[str], model: Optional[str] = None, **kwargs: Any) -> List[List[float]]:
        # Deterministic pseudo-embeddings based on char codes
        def _embed_one(s: str) -> List[float]:
            base = sum(ord(c) for c in s) or 1
            return [((ord(c) % 97) / 97.0) for c in (s + "   ")[:16]] + [base % 1_000 / 1_000]
        return [_embed_one(s) for s in inputs]


from __future__ import annotations

import os
from typing import Any, Iterable, List, Mapping, Optional, Sequence


class OpenAILLM:
    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None, default_model: str = "gpt-4o-mini") -> None:
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.base_url = base_url or os.getenv("OPENAI_BASE_URL")
        self.default_model = default_model
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY is not set for OpenAILLM")

    def chat(self, messages: Sequence[Mapping[str, str]], model: Optional[str] = None, stream: bool = False, **kwargs: Any) -> Any:
        # Lazy import to avoid hard dependency if not used
        try:
            from openai import OpenAI
        except Exception as e:  # pragma: no cover
            raise RuntimeError("openai package not installed. pip install openai>=1.0") from e

        client = OpenAI(api_key=self.api_key, base_url=self.base_url) if self.base_url else OpenAI(api_key=self.api_key)
        mdl = model or self.default_model
        if stream:
            stream_resp = client.chat.completions.create(model=mdl, messages=list(messages), stream=True, **kwargs)
            def _gen():
                for chunk in stream_resp:
                    delta = chunk.choices[0].delta if chunk.choices and hasattr(chunk.choices[0], 'delta') else None
                    yield {"delta": {"content": getattr(delta, 'content', None)}, "done": getattr(chunk, 'done', False)}
            return _gen()
        resp = client.chat.completions.create(model=mdl, messages=list(messages), **kwargs)
        content = resp.choices[0].message.content if resp.choices else ""
        return {"content": content, "model": mdl}


class OpenAIEmbeddings:
    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None, default_model: str = "text-embedding-3-small") -> None:
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.base_url = base_url or os.getenv("OPENAI_BASE_URL")
        self.default_model = default_model
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY is not set for OpenAIEmbeddings")

    def embed(self, inputs: Sequence[str], model: Optional[str] = None, **kwargs: Any) -> List[List[float]]:
        try:
            from openai import OpenAI
        except Exception as e:  # pragma: no cover
            raise RuntimeError("openai package not installed. pip install openai>=1.0") from e

        client = OpenAI(api_key=self.api_key, base_url=self.base_url) if self.base_url else OpenAI(api_key=self.api_key)
        mdl = model or self.default_model
        resp = client.embeddings.create(model=mdl, input=list(inputs), **kwargs)
        return [d.embedding for d in resp.data]


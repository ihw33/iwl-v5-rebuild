from __future__ import annotations

from typing import Any, Optional


class RedisCache:
    def __init__(self, url: str, default_ttl_seconds: int = 300) -> None:
        self.url = url
        self.default_ttl = default_ttl_seconds
        self._client = None

    def _lazy(self):
        if self._client is None:
            try:
                import redis  # type: ignore
            except Exception as e:  # pragma: no cover
                raise RuntimeError("redis not installed. pip install redis>=5") from e
            self._client = redis.from_url(self.url)
        return self._client

    def get(self, key: str) -> Optional[Any]:
        r = self._lazy()
        val = r.get(key)
        if val is None:
            return None
        try:
            import json
            return json.loads(val)
        except Exception:
            return val

    def set(self, key: str, value: Any, ttl_seconds: Optional[int] = None) -> None:
        r = self._lazy()
        ttl = ttl_seconds if ttl_seconds is not None else self.default_ttl
        payload = value
        try:
            import json
            payload = json.dumps(value)
        except Exception:
            pass
        r.set(key, payload, ex=ttl)

    def delete(self, key: str) -> None:
        r = self._lazy()
        r.delete(key)


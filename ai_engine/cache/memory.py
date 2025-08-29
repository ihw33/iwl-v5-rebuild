from __future__ import annotations

import time
from typing import Any, Dict, Optional, Tuple


class InMemoryCache:
    def __init__(self, default_ttl_seconds: int = 300) -> None:
        self.default_ttl = default_ttl_seconds
        self._data: Dict[str, Tuple[float, Any]] = {}

    def get(self, key: str) -> Optional[Any]:
        now = time.time()
        row = self._data.get(key)
        if not row:
            return None
        exp, val = row
        if exp and exp < now:
            self._data.pop(key, None)
            return None
        return val

    def set(self, key: str, value: Any, ttl_seconds: Optional[int] = None) -> None:
        ttl = ttl_seconds if ttl_seconds is not None else self.default_ttl
        exp = time.time() + ttl if ttl > 0 else 0
        self._data[key] = (exp, value)

    def delete(self, key: str) -> None:
        self._data.pop(key, None)


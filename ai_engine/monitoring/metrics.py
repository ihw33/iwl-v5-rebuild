from __future__ import annotations

from typing import Optional


class Metrics:
    def __init__(self, enabled: bool = False) -> None:
        self.enabled = enabled
        self._prom = None

    def _lazy(self):
        if not self.enabled:
            return None
        if self._prom is None:
            try:
                from prometheus_client import Counter, Histogram  # type: ignore
            except Exception as e:  # pragma: no cover
                raise RuntimeError("prometheus-client not installed. pip install prometheus-client") from e
            self._prom = {
                "requests_total": Counter("ai_requests_total", "Total API requests", ["path", "method"]),
                "latency_seconds": Histogram("ai_latency_seconds", "Request latency seconds", ["path"]),
            }
        return self._prom

    def count(self, path: str, method: str) -> None:
        prom = self._lazy()
        if prom:
            prom["requests_total"].labels(path=path, method=method).inc()

    def observe_latency(self, path: str, seconds: float) -> None:
        prom = self._lazy()
        if prom:
            prom["latency_seconds"].labels(path=path).observe(seconds)


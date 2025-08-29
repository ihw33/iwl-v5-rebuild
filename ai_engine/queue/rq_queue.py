from __future__ import annotations

from typing import Any, Mapping, Optional, Tuple


class RQQueue:
    def __init__(self, redis_url: str, queue_name: str = "default") -> None:
        self.redis_url = redis_url
        self.queue_name = queue_name
        self._queue = None

    def _lazy(self):
        if self._queue is None:
            try:
                import rq  # type: ignore
                from redis import Redis  # type: ignore
            except Exception as e:  # pragma: no cover
                raise RuntimeError("rq/redis not installed. pip install rq redis") from e
            conn = Redis.from_url(self.redis_url)
            self._queue = rq.Queue(self.queue_name, connection=conn)
        return self._queue

    def enqueue(self, job_name: str, payload: Mapping[str, Any]) -> str:
        q = self._lazy()
        job = q.enqueue(job_name, payload)
        return job.id

    def dequeue(self) -> Optional[Tuple[str, Mapping[str, Any]]]:
        # RQ does not support direct dequeue; this is just an interface stub.
        return None


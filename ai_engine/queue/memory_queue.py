from __future__ import annotations

import queue
import uuid
from typing import Any, Mapping, Optional, Tuple


class InMemoryQueue:
    def __init__(self) -> None:
        self._q: queue.Queue[Tuple[str, Mapping[str, Any]]] = queue.Queue()

    def enqueue(self, job_name: str, payload: Mapping[str, Any]) -> str:
        jid = str(uuid.uuid4())
        self._q.put((jid, {"job": job_name, **payload}))
        return jid

    def dequeue(self) -> Optional[Tuple[str, Mapping[str, Any]]]:
        try:
            return self._q.get_nowait()
        except queue.Empty:
            return None


from __future__ import annotations

from typing import Any, Dict, Optional

from .interfaces import (
    BaseNode,
    ExecutionContext,
    HealthStatus,
    NodeIO,
    ValidationError,
)


class AbstractBaseNode(BaseNode):
    def __init__(
        self,
        node_id: str,
        name: str,
        version: str,
        io: NodeIO,
        description: Optional[str] = None,
    ) -> None:
        self.id = node_id
        self.name = name
        self.version = version
        self.description = description
        self.io = io

    def validate_inputs(self, payloads: Dict[str, Any]) -> None:
        required_inputs = {p.name for p in self.io.inputs}
        missing = [r for r in required_inputs if r not in payloads]
        if missing:
            raise ValidationError(f"missing required inputs: {missing}")

    def execute(self, payloads: Dict[str, Any], ctx: ExecutionContext) -> Dict[str, Any]:
        self.validate_inputs(payloads)
        return self._run(payloads, ctx)

    def _run(self, payloads: Dict[str, Any], ctx: ExecutionContext) -> Dict[str, Any]:
        raise NotImplementedError

    def get_config_schema(self) -> Dict[str, Any]:
        return {"type": "object", "properties": {}, "additionalProperties": True}

    def health(self) -> HealthStatus:
        return HealthStatus(status="ok")


from __future__ import annotations

from typing import Any, Dict, List, Optional, Protocol, runtime_checkable, Literal


class PortSchemaDict(Dict[str, Any]):
    pass


@runtime_checkable
class SupportsToDict(Protocol):
    def to_dict(self) -> Dict[str, Any]:
        ...


class PortSchema:
    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        content_type: Literal[
            "application/json", "text/markdown", "application/octet-stream"
        ] = "application/json",
        schema_ref: Optional[str] = None,
    ) -> None:
        self.name = name
        self.description = description
        self.content_type = content_type
        self.schema_ref = schema_ref

    def to_dict(self) -> PortSchemaDict:
        return {
            "name": self.name,
            "description": self.description,
            "content_type": self.content_type,
            "schema_ref": self.schema_ref,
        }


class NodeIO:
    def __init__(self, inputs: List[PortSchema], outputs: List[PortSchema]) -> None:
        self.inputs = inputs
        self.outputs = outputs

    def to_dict(self) -> Dict[str, Any]:
        return {
            "inputs": [p.to_dict() for p in self.inputs],
            "outputs": [p.to_dict() for p in self.outputs],
        }


class ExecutionContext:
    def __init__(
        self,
        session_id: str,
        user_id: Optional[str] = None,
        trace_id: Optional[str] = None,
        config: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.session_id = session_id
        self.user_id = user_id
        self.trace_id = trace_id
        self.config = config or {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "session_id": self.session_id,
            "user_id": self.user_id,
            "trace_id": self.trace_id,
            "config": self.config,
        }


class BaseNodeError(Exception):
    pass


class ValidationError(BaseNodeError):
    pass


class HealthStatus:
    def __init__(self, status: str = "ok", details: Optional[Dict[str, Any]] = None) -> None:
        self.status = status
        self.details = details or {}

    def to_dict(self) -> Dict[str, Any]:
        return {"status": self.status, "details": self.details}


class BaseNode(Protocol):
    id: str
    name: str
    version: str
    description: Optional[str]
    io: NodeIO

    def validate_inputs(self, payloads: Dict[str, Any]) -> None:
        ...

    def execute(self, payloads: Dict[str, Any], ctx: ExecutionContext) -> Dict[str, Any]:
        ...

    def get_config_schema(self) -> Dict[str, Any]:
        ...

    def health(self) -> HealthStatus:
        ...


class LearningModuleNode(BaseNode, Protocol):
    def learning_objectives(self) -> List[str]:
        ...

    def evaluate_outcomes(self, outputs: Dict[str, Any]) -> Dict[str, Any]:
        ...


class TeachingMethodNode(BaseNode, Protocol):
    def method_profile(self) -> Dict[str, Any]:
        ...


class DAGNode(BaseNode, Protocol):
    def prerequisites(self) -> List[str]:
        ...

    def scheduling_hints(self) -> Dict[str, Any]:
        ...

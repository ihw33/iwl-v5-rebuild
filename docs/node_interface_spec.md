## Node 인터페이스 표준 (M1-W1) — 초안 v0.1

참조: 이슈 #42

### 1) 목적
- 8×4 매트릭스 학습 시스템의 모든 노드가 일관된 계약을 따르도록 표준화
- DAG 기반 실행, 관찰가능성(로그/메트릭/트레이싱), 테스트 용이성 확보

### 2) 범위
- BaseNode 추상 클래스
- LearningModuleNode / TeachingMethodNode 인터페이스
- DAGNode 인터페이스(그래프 실행 제약/메타정보)
- 데이터 교환 프로토콜(Envelope/Schema/에러/버전)

### 3) 용어
- Node: 입력→처리→출력을 수행하는 최소 실행 단위
- Port: 입력/출력의 명명된 인터페이스(타입/스키마 포함)
- Payload: 포트로 전달되는 데이터(JSON Schema 검증 대상)
- Context: 세션/사용자/추적ID 등 실행 시 전달되는 환경 정보

### 4) 아키텍처 원칙
- 계약 우선(Contract-first), 순수성 선호, 관찰가능성 내장, 버전 호환

### 5) 인터페이스 초안 (개념 스니펫)
```python
from typing import Any, Dict, List, Optional, Literal
from pydantic import BaseModel

class PortSchema(BaseModel):
    name: str
    description: Optional[str] = None
    content_type: Literal["application/json", "text/markdown", "application/octet-stream"] = "application/json"
    schema_ref: Optional[str] = None  # JSON Schema $ref or URI

class NodeIO(BaseModel):
    inputs: List[PortSchema]
    outputs: List[PortSchema]

class ExecutionContext(BaseModel):
    session_id: str
    user_id: Optional[str] = None
    trace_id: Optional[str] = None
    config: Dict[str, Any] = {}

class BaseNode:
    id: str
    name: str
    version: str
    description: Optional[str]
    io: NodeIO

    def validate_inputs(self, payloads: Dict[str, Any]) -> None: ...
    def execute(self, payloads: Dict[str, Any], ctx: ExecutionContext) -> Dict[str, Any]: ...
    def get_config_schema(self) -> Dict[str, Any]: ...
    def health(self) -> Dict[str, Any]: ...

class LearningModuleNode(BaseNode):
    def learning_objectives(self) -> List[str]: ...
    def evaluate_outcomes(self, outputs: Dict[str, Any]) -> Dict[str, Any]: ...

class TeachingMethodNode(BaseNode):
    def method_profile(self) -> Dict[str, Any]: ...

class DAGNode(BaseNode):
    def prerequisites(self) -> List[str]: ...
    def scheduling_hints(self) -> Dict[str, Any]: ...
```

### 6) 데이터 교환 프로토콜(Envelope)
```json
{
  "envelope": {
    "id": "evt-...",
    "traceId": "trc-...",
    "sessionId": "sess-...",
    "timestamp": "2025-08-28T12:34:56Z",
    "schemaVersion": "1.0"
  },
  "payload": {
    "port": "input_name",
    "contentType": "application/json",
    "data": {},
    "metadata": { "source": "node:X", "confidence": 0.92 }
  },
  "error": null
}
```

오류 규약: `error = { code, message, details?, retriable? }`

### 7) 관찰가능성
- 로그 필드: `trace_id`, `node_id`, `session_id`, `event`
- 메트릭: `node_execute_ms`, `payload_bytes`, `validation_failures_total`
- 트레이싱: OpenTelemetry 스팬 (`execute`, I/O 검증, 외부 호출)

### 8) 보안/안전장치
- 입력 검증 강제(JSON Schema/Pydantic)
- 타임박스/캔슬레이션(Timeout/Cancellation)
- 자원 힌트(CPU/메모리), 샌드박스 실행(선택)

### 9) 테스트 전략
- 계약 테스트 공통 스위트
- 예제 노드: `ExampleSumNode`, `ExampleClusterNode`
- 샘플 DAG: 직선/분기/머지 케이스

### 10) 산출물
- `nodes/base/base_node.py`
- `nodes/base/interfaces.py`
- `docs/node_interface_spec.md`

### 11) 일정 & 체크리스트
- [ ] v0.1 인터페이스/추상 구현 초안
- [ ] 예제 노드 2종 + 계약 테스트
- [ ] 프로토콜 문서화(에러/버전/관찰가능성)
- [ ] 리뷰 반영 v1.0 확정(2025-09-10)

### 12) 수용 기준(AC)
- 모든 노드가 `BaseNode.execute` 규약을 만족
- E2E 그래프 실행 1건 이상 성공 및 메트릭 노출
- 문서에 예제와 에지 케이스 포함


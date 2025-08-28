# S1-A1 Interactive 리팩토링 제안

## 1. 설정 분리
```python
# config/learning_config.py
class LearningConfig:
    # DAG 조정 임계값
    LOW_PERFORMANCE_THRESHOLD = 0.5
    HIGH_PERFORMANCE_THRESHOLD = 0.9
    REPETITIVE_ERRORS_THRESHOLD = 3
    
    # 관찰 카테고리
    OBSERVATION_CATEGORIES = 5
    
    # 판단 언어 목록
    JUDGMENT_WORDS = [
        "좋다", "나쁘다", "예쁘다", "못생겼다", 
        "편하다", "불편하다", "멋지다", "싫다"
    ]
```

## 2. 에러 처리 추가
```python
def _restore_session(self, session_data: Dict[str, Any]) -> SessionState:
    try:
        # 기존 코드...
        timestamp = datetime.fromisoformat(obs_data["timestamp"])
    except (ValueError, TypeError) as e:
        # 로깅 추가
        logger.warning(f"Invalid timestamp format: {e}")
        timestamp = datetime.now()
```

## 3. 헬퍼 메서드 추출
```python
def _apply_persona_adjustment(self, prompt: InteractivePrompt, profile: Optional[UserProfile]) -> InteractivePrompt:
    """페르소나 기반 프롬프트 조정 (중복 제거)"""
    if not profile:
        return prompt
        
    adjustments = {
        "visual_learner": lambda p: p.hints.append("색상과 형태에 주목"),
        "practice_oriented": lambda p: p.hints.append("직접 해보세요"),
        "theoretical": lambda p: p.hints.append("의미를 생각해보세요")
    }
    
    if profile.persona_type in adjustments:
        adjustments[profile.persona_type](prompt)
    
    return prompt
```

## 4. 상수 정의
```python
class Constants:
    # 관찰 카테고리 수
    TOTAL_OBSERVATION_CATEGORIES = 5
    
    # 최소 관찰 수
    MIN_OBSERVATIONS = {
        "L1": 3,
        "L3": 5, 
        "L5": 4
    }
    
    # 기본값들
    DEFAULT_LEVEL = "L1"
    DEFAULT_PERSONA = "general"
    DEFAULT_LEARNING_STYLE = "balanced"
```

## 5. 단위 테스트 가능하도록 분리
```python
class ObservationAnalyzer:
    """관찰 분석 로직 분리 (테스트 용이)"""
    
    @staticmethod
    def detect_judgment(text: str) -> bool:
        # 판단 언어 감지 로직
        pass
    
    @staticmethod
    def classify_observation(text: str) -> str:
        # 관찰 분류 로직
        pass
    
    @staticmethod
    def calculate_quality(entry: ObservationEntry) -> float:
        # 품질 계산 로직
        pass
```

## 6. 로깅 추가
```python
import logging

logger = logging.getLogger(__name__)

class S1_A1_InteractiveNode:
    def _handle_observation(self, ...):
        logger.info(f"Processing observation: {obs_type}")
        
        if dag_adjustment:
            logger.warning(f"DAG adjustment triggered: {dag_adjustment['action']}")
```

## 7. 검증 로직 강화
```python
def validate_inputs(self, payloads: Dict[str, Any]) -> None:
    super().validate_inputs(payloads)
    
    # 추가 검증
    action = payloads.get("action")
    if action not in ["start", "observe", "get_prompt", "complete"]:
        raise ValidationError(f"Invalid action: {action}")
    
    if action == "observe" and not payloads.get("user_input"):
        raise ValidationError("user_input required for observe action")
```

## 8. 성능 최적화
```python
# 반복적인 리스트 순회 대신 캐싱
@lru_cache(maxsize=128)
def _get_judgment_words() -> Set[str]:
    return set(JUDGMENT_WORDS)

# 문자열 검색 최적화
def _detect_judgment(self, text: str) -> bool:
    words = self._get_judgment_words()
    text_words = set(text.split())
    return bool(words & text_words)
```
"""
S1-A1: 순수한 관찰 (Pure Observation) - Interactive Version
지각인지 × 정보처리깊이

Phase 2-3 개선사항:
- Phase 2: 실시간 인터랙티비티 
- Phase 3: 상태 관리 (SessionState)

기반 문서:
- docs/8x4-matrix/modules/MODULE_TEMPLATE_v3.0.md
- docs/8x4-matrix/modules/S1-A1/S1-A1-module_design.md

module_id: S1-A1
core_concept: "감각적 수용" - 판단 없이 있는 그대로 관찰
"""
from typing import Any, Dict, List, Optional, Literal
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
import json
from nodes.base.base_node import AbstractBaseNode
from nodes.base.interfaces import NodeIO, PortSchema, ExecutionContext


@dataclass
class UserProfile:
    """설문조사 결과로 생성되는 사용자 프로파일 (v1.0)"""
    user_id: str
    persona_type: str  # "visual_learner", "practice_oriented", "theoretical" 등
    learning_style: str  # "step_by_step", "holistic", "experimental" 등  
    selected_curriculum: str  # 사용자가 선택한 기본 커리큘럼 ID
    profile_vector: List[float]  # 벡터화된 프로파일
    created_at: datetime = field(default_factory=datetime.now)
    
    # 추후 확장 예정
    # prior_knowledge, interests, goals, constraints 등


class DifficultyLevel(Enum):
    L1 = "초급"  # 완전 초보자
    L3 = "중급"  # 기초 학습자  
    L5 = "고급"  # 전문가 수준


@dataclass
class ObservationEntry:
    """개별 관찰 기록"""
    timestamp: datetime
    observation: str
    observation_type: str  # color, shape, size, position, texture, meta
    has_judgment: bool
    feedback_given: Optional[str] = None
    quality_score: float = 0.0


@dataclass 
class SessionState:
    """Phase 3: 세션 상태 관리"""
    session_id: str
    user_id: str
    module_id: str = "S1-A1"
    current_level: str = "L1"
    current_step: int = 1
    started_at: datetime = field(default_factory=datetime.now)
    observations: List[ObservationEntry] = field(default_factory=list)
    total_observations: int = 0
    judgment_count: int = 0
    diversity_score: float = 0.0
    accumulated_quality: float = 0.0
    completed_steps: List[int] = field(default_factory=list)
    is_complete: bool = False
    
    # Phase 3 추가: UserProfile과 DAG 조정
    user_profile: Optional[UserProfile] = None
    selected_curriculum_id: Optional[str] = None
    dag_adjustments: List[Dict[str, Any]] = field(default_factory=list)
    
    def add_observation(self, observation: str, obs_type: str = "unknown") -> ObservationEntry:
        """관찰 추가 및 실시간 분석"""
        has_judgment = self._detect_judgment(observation)
        if has_judgment:
            self.judgment_count += 1
            
        entry = ObservationEntry(
            timestamp=datetime.now(),
            observation=observation,
            observation_type=obs_type,
            has_judgment=has_judgment
        )
        
        self.observations.append(entry)
        self.total_observations += 1
        self._update_diversity()
        
        return entry
    
    def _detect_judgment(self, text: str) -> bool:
        """판단 언어 감지"""
        judgment_words = [
            "좋다", "나쁘다", "예쁘다", "못생겼다", "편하다", "불편하다",
            "멋지다", "싫다", "마음에", "별로", "최고", "최악", "쓸모"
        ]
        return any(word in text for word in judgment_words)
    
    def _update_diversity(self):
        """관찰 다양성 업데이트"""
        obs_types = set(obs.observation_type for obs in self.observations)
        self.diversity_score = len(obs_types) / 5.0  # 5개 카테고리 기준
    
    def record_adjustment(self, adjustment: Dict[str, Any]):
        """DAG 조정 기록"""
        self.dag_adjustments.append({
            "timestamp": datetime.now().isoformat(),
            "adjustment": adjustment,
            "observation_count": self.total_observations,
            "quality_at_adjustment": self.accumulated_quality
        })
    
    def get_progress(self) -> Dict[str, Any]:
        """현재 진행 상황 반환"""
        return {
            "session_id": self.session_id,
            "level": self.current_level,
            "step": self.current_step,
            "observations_count": self.total_observations,
            "judgment_free_ratio": 1 - (self.judgment_count / max(1, self.total_observations)),
            "diversity": self.diversity_score,
            "completed_steps": self.completed_steps,
            "is_complete": self.is_complete
        }
    
    def to_dict(self) -> Dict[str, Any]:
        """상태를 딕셔너리로 변환"""
        result = {
            "session_id": self.session_id,
            "user_id": self.user_id,
            "module_id": self.module_id,
            "current_level": self.current_level,
            "current_step": self.current_step,
            "started_at": self.started_at.isoformat(),
            "observations": [
                {
                    "timestamp": obs.timestamp.isoformat(),
                    "observation": obs.observation,
                    "type": obs.observation_type,
                    "has_judgment": obs.has_judgment,
                    "feedback": obs.feedback_given,
                    "quality": obs.quality_score
                } for obs in self.observations
            ],
            "stats": {
                "total": self.total_observations,
                "judgment_count": self.judgment_count,
                "diversity": self.diversity_score,
                "quality": self.accumulated_quality
            },
            "progress": self.get_progress()
        }
        
        # UserProfile 정보 추가
        if self.user_profile:
            result["user_profile"] = {
                "user_id": self.user_profile.user_id,
                "persona_type": self.user_profile.persona_type,
                "learning_style": self.user_profile.learning_style,
                "selected_curriculum": self.user_profile.selected_curriculum
            }
        
        # DAG 조정 기록 추가
        if self.dag_adjustments:
            result["dag_adjustments"] = self.dag_adjustments
            
        return result


@dataclass
class InteractivePrompt:
    """Phase 2: 실시간 프롬프트"""
    step: int
    instruction: str
    ai_prompt: str
    expected_type: str
    hints: List[str] = field(default_factory=list)
    follow_ups: List[str] = field(default_factory=list)
    
    def get_adaptive_prompt(self, session: 'SessionState') -> str:
        """세션 상태에 따른 적응형 프롬프트 생성"""
        base_prompt = self.ai_prompt
        
        # 판단 언어가 많으면 리마인더 추가
        if session.judgment_count > 2:
            base_prompt += "\n(기억하세요: 판단이나 평가 없이 보이는 그대로만 설명해주세요)"
        
        # 다양성이 낮으면 힌트 제공
        if session.diversity_score < 0.3 and self.hints:
            base_prompt += f"\n힌트: {self.hints[0]}"
        
        # 이전 관찰 참조
        if session.observations and self.follow_ups:
            last_obs = session.observations[-1]
            if not last_obs.has_judgment:
                base_prompt = f"좋습니다! {self.follow_ups[0]}"
        
        return base_prompt


class SimpleDagAdjuster:
    """Phase 3: 기본적인 DAG 조정 로직"""
    
    def __init__(self, session_state: SessionState):
        self.session = session_state
        self.adjustment_triggers = {
            "low_performance": 0.5,  # 품질 점수 임계값
            "high_performance": 0.9,
            "repetitive_errors": 3,  # 같은 실수 반복 횟수
            "slow_progress": 5  # 같은 단계 반복 횟수
        }
        
    def check_and_adjust(self, observation_result: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """관찰 결과 체크 및 간단한 조정"""
        
        # 체크리스트 (추후 구현)
        # □ 난이도 조정 필요?
        # □ 추가 설명 필요?
        # □ 반복 학습 필요?
        # □ 다음 단계 건너뛰기?
        # □ 보충 콘텐츠 추가?
        # □ 학습 방식 변경?
        
        quality_score = observation_result.get("quality_score", 0.5)
        
        # 간단한 조정 로직
        if quality_score < self.adjustment_triggers["low_performance"]:
            # 저성과: 보충 단계 추가
            adjustment = self._add_support_step()
            self.session.record_adjustment(adjustment)
            return adjustment
            
        elif quality_score > self.adjustment_triggers["high_performance"]:
            # 고성과: 빠른 진행
            adjustment = self._accelerate_progress()
            self.session.record_adjustment(adjustment)
            return adjustment
            
        elif self.session.judgment_count > self.adjustment_triggers["repetitive_errors"]:
            # 반복적 판단 언어: 리마인더 강화
            adjustment = self._reinforce_reminder()
            self.session.record_adjustment(adjustment)
            return adjustment
        
        # 페르소나별 조정 (있을 경우)
        if self.session.user_profile:
            persona_adjustment = self._persona_based_adjustment()
            if persona_adjustment:
                self.session.record_adjustment(persona_adjustment)
                return persona_adjustment
        
        return None
    
    def _add_support_step(self) -> Dict[str, Any]:
        """보충 단계 추가"""
        return {
            "action": "add_support",
            "type": "additional_practice",
            "reason": "low_performance",
            "suggestion": "더 쉬운 예제로 연습"
        }
    
    def _accelerate_progress(self) -> Dict[str, Any]:
        """빠른 진행"""
        return {
            "action": "skip_ahead",
            "skip_steps": 1,
            "reason": "high_performance",
            "suggestion": "다음 레벨로 진행 가능"
        }
    
    def _reinforce_reminder(self) -> Dict[str, Any]:
        """판단 언어 사용 리마인더 강화"""
        return {
            "action": "reinforce_concept",
            "concept": "judgment_free_observation",
            "reason": "repetitive_judgment_language",
            "suggestion": "판단 없는 관찰 재강조"
        }
    
    def _persona_based_adjustment(self) -> Optional[Dict[str, Any]]:
        """페르소나 기반 조정"""
        if not self.session.user_profile:
            return None
            
        persona = self.session.user_profile.persona_type
        
        if persona == "visual_learner" and self.session.diversity_score < 0.3:
            return {
                "action": "add_visual_aids",
                "reason": "visual_learner_needs_support",
                "suggestion": "시각적 예시 추가"
            }
        elif persona == "practice_oriented" and self.session.total_observations < 5:
            return {
                "action": "add_practice_exercises",
                "reason": "practice_oriented_needs_more",
                "suggestion": "추가 연습 문제 제공"
            }
        elif persona == "theoretical" and not any(obs.observation_type == "meta" for obs in self.session.observations):
            return {
                "action": "add_conceptual_explanation",
                "reason": "theoretical_learner_depth",
                "suggestion": "개념적 설명 추가"
            }
        
        return None


class S1_A1_InteractiveNode(AbstractBaseNode):
    """
    S1-A1 Interactive: 실시간 인터랙티브 순수 관찰 모듈
    
    Phase 2: 실시간 처리
    - 관찰 하나씩 처리
    - 즉각적 피드백
    - 적응형 프롬프트
    
    Phase 3: 상태 관리
    - SessionState 클래스
    - 진행 상황 추적
    - 품질 메트릭 실시간 업데이트
    """
    
    def __init__(self):
        io = NodeIO(
            inputs=[
                PortSchema(
                    name="action",
                    description="액션 타입 (start/observe/get_prompt/complete)",
                    content_type="application/json"
                ),
                PortSchema(
                    name="session_state",
                    description="세션 상태 (없으면 새로 생성)",
                    content_type="application/json"
                ),
                PortSchema(
                    name="user_input",
                    description="사용자 입력 (observe 액션 시)",
                    content_type="application/json"
                )
            ],
            outputs=[
                PortSchema(
                    name="response",
                    description="AI 응답",
                    content_type="application/json"
                ),
                PortSchema(
                    name="session_state",
                    description="업데이트된 세션 상태",
                    content_type="application/json"
                ),
                PortSchema(
                    name="next_prompt",
                    description="다음 프롬프트",
                    content_type="application/json"
                )
            ]
        )
        
        super().__init__(
            node_id="S1-A1-interactive",
            name="순수한 관찰 (인터랙티브)",
            version="3.1.0",
            io=io,
            description="실시간 인터랙티브 순수 관찰 학습 모듈"
        )
        
        # 인터랙티브 프롬프트 정의
        self.prompts = self._define_interactive_prompts()
        
        # DAG 조정기
        self.dag_adjuster = None  # 세션 시작 시 초기화
    
    def _define_interactive_prompts(self) -> Dict[str, List[InteractivePrompt]]:
        """레벨별 인터랙티브 프롬프트 정의"""
        return {
            "L1": [
                InteractivePrompt(
                    1, 
                    "ChatGPT 화면을 열고 천천히 보세요",
                    "화면에서 가장 먼저 눈에 들어오는 것은 무엇인가요?",
                    "simple_observation",
                    hints=["색깔이나 모양을 말해보세요"],
                    follow_ups=["이제 다른 곳을 보세요. 또 무엇이 보이나요?"]
                ),
                InteractivePrompt(
                    2,
                    "입력창 주변을 관찰하세요",
                    "입력창은 어디에 있나요? 어떤 모양인가요?",
                    "position_shape",
                    hints=["위치와 형태에 집중하세요"],
                    follow_ups=["입력창 근처에 또 뭐가 있나요?"]
                ),
                InteractivePrompt(
                    3,
                    "색깔에 집중해보세요",
                    "화면에서 볼 수 있는 색깔을 하나씩 말해주세요",
                    "color",
                    hints=["배경색, 글자색, 버튼색 등"],
                    follow_ups=["또 다른 색깔이 있나요?"]
                ),
                InteractivePrompt(
                    4,
                    "크기를 비교해보세요", 
                    "가장 큰 요소는 무엇인가요? 가장 작은 것은?",
                    "size",
                    hints=["상대적 크기를 관찰하세요"],
                    follow_ups=["중간 크기의 요소들은?"]
                ),
                InteractivePrompt(
                    5,
                    "전체를 다시 한번 보세요",
                    "지금까지 놓친 것이 있나요?",
                    "comprehensive",
                    hints=["구석구석 살펴보세요"],
                    follow_ups=["전체적으로 어떤 느낌인가요? (판단 말고 관찰만)"]
                )
            ],
            "L3": [
                InteractivePrompt(
                    1,
                    "화면의 구조를 관찰하세요",
                    "화면이 몇 개의 영역으로 나뉘어 있나요?",
                    "layout",
                    hints=["상단, 중앙, 하단, 사이드바 등"],
                    follow_ups=["각 영역의 크기 비율은?"]
                ),
                InteractivePrompt(
                    2,
                    "요소들의 관계를 보세요",
                    "어떤 요소들이 서로 가까이 있나요?",
                    "relationship",
                    hints=["그룹핑된 요소들을 찾아보세요"],
                    follow_ups=["정렬은 어떻게 되어 있나요?"]
                ),
                InteractivePrompt(
                    3,
                    "빈 공간을 관찰하세요",
                    "여백은 어디에 얼마나 있나요?",
                    "whitespace",
                    hints=["여백도 디자인의 일부입니다"],
                    follow_ups=["여백의 패턴이 보이나요?"]
                ),
                InteractivePrompt(
                    4,
                    "패턴을 찾아보세요",
                    "반복되는 패턴이 있나요?",
                    "pattern",
                    hints=["색상, 형태, 배치의 반복"],
                    follow_ups=["패턴이 깨지는 곳은?"]
                ),
                InteractivePrompt(
                    5,
                    "세부사항을 관찰하세요",
                    "가장 작은 디테일은 무엇인가요?",
                    "detail",
                    hints=["아이콘, 구분선, 그림자 등"],
                    follow_ups=["이 디테일들의 공통점은?"]
                )
            ],
            "L5": [
                InteractivePrompt(
                    1,
                    "1분간 침묵하며 응시하세요",
                    "첫 인상과 지금 보이는 것의 차이는?",
                    "meta_observation",
                    hints=["처음 놓쳤던 것들"],
                    follow_ups=["왜 처음엔 못 봤을까요?"]
                ),
                InteractivePrompt(
                    2,
                    "없는 것을 관찰하세요",
                    "있을 법한데 없는 것은?",
                    "absence",
                    hints=["일반적인 UI와 비교하여"],
                    follow_ups=["이 부재가 만드는 효과는?"]
                ),
                InteractivePrompt(
                    3,
                    "시선의 움직임을 추적하세요",
                    "당신의 눈은 어떤 경로로 움직였나요?",
                    "eye_movement",
                    hints=["시작점과 끝점"],
                    follow_ups=["왜 그 경로였을까요?"]
                ),
                InteractivePrompt(
                    4,
                    "관찰하는 자신을 관찰하세요",
                    "관찰하는 동안 당신에게 어떤 변화가?",
                    "self_observation",
                    hints=["내적 변화에 주목"],
                    follow_ups=["관찰이 당신을 어떻게 바꾸었나요?"]
                ),
                InteractivePrompt(
                    5,
                    "순수한 관찰을 성찰하세요",
                    "판단 없이 본다는 것은 무엇일까요?",
                    "philosophical",
                    hints=["경험을 언어로 표현하세요"],
                    follow_ups=["이 경험이 주는 통찰은?"]
                )
            ]
        }
    
    def _run(self, payloads: Dict[str, Any], ctx: ExecutionContext) -> Dict[str, Any]:
        """Phase 2-3: 실시간 인터랙티브 실행"""
        action = payloads.get("action", "start")
        
        if action == "start":
            return self._handle_start(payloads, ctx)
        elif action == "observe":
            return self._handle_observation(payloads, ctx)
        elif action == "get_prompt":
            return self._handle_get_prompt(payloads, ctx)
        elif action == "complete":
            return self._handle_complete(payloads, ctx)
        else:
            return {"error": f"Unknown action: {action}"}
    
    def _handle_start(self, payloads: Dict[str, Any], ctx: ExecutionContext) -> Dict[str, Any]:
        """세션 시작"""
        user_level = payloads.get("user_level", "L1")
        user_profile_data = payloads.get("user_profile")
        
        # 새 세션 생성
        session = SessionState(
            session_id=ctx.session_id,
            user_id=ctx.user_id or "anonymous",
            current_level=user_level
        )
        
        # UserProfile 설정 (있을 경우)
        if user_profile_data:
            session.user_profile = UserProfile(
                user_id=user_profile_data.get("user_id", ctx.user_id),
                persona_type=user_profile_data.get("persona_type", "general"),
                learning_style=user_profile_data.get("learning_style", "balanced"),
                selected_curriculum=user_profile_data.get("selected_curriculum", "default"),
                profile_vector=user_profile_data.get("profile_vector", [])
            )
            session.selected_curriculum_id = session.user_profile.selected_curriculum
        
        # DAG 조정기 초기화
        self.dag_adjuster = SimpleDagAdjuster(session)
        
        # 첫 프롬프트 가져오기
        first_prompt = self.prompts[user_level][0]
        
        return {
            "response": {
                "type": "session_started",
                "message": f"S1-A1 순수한 관찰 모듈을 시작합니다. (레벨: {user_level})",
                "instructions": first_prompt.instruction
            },
            "next_prompt": {
                "step": first_prompt.step,
                "prompt": first_prompt.ai_prompt,
                "hints": first_prompt.hints
            },
            "session_state": session.to_dict()
        }
    
    def _handle_observation(self, payloads: Dict[str, Any], ctx: ExecutionContext) -> Dict[str, Any]:
        """관찰 처리 (Phase 2: 실시간 처리)"""
        session_data = payloads.get("session_state", {})
        user_input = payloads.get("user_input", "")
        
        # 세션 복원
        session = self._restore_session(session_data)
        
        # 관찰 분류
        obs_type = self._classify_observation(user_input)
        
        # 관찰 추가 및 실시간 분석
        entry = session.add_observation(user_input, obs_type)
        
        # 즉각적 피드백 생성
        feedback = self._generate_feedback(entry, session)
        entry.feedback_given = feedback
        
        # 품질 점수 계산
        entry.quality_score = self._calculate_observation_quality(entry, session)
        session.accumulated_quality = (session.accumulated_quality * (session.total_observations - 1) + entry.quality_score) / session.total_observations
        
        # DAG 조정 체크 (Phase 3) - 준비된 노드/경로만 선택
        dag_adjustment = None
        if self.dag_adjuster:
            dag_adjustment = self.dag_adjuster.check_and_adjust({
                "quality_score": entry.quality_score,
                "observation_type": entry.observation_type,
                "has_judgment": entry.has_judgment
            })
        
        # 다음 프롬프트 결정
        current_prompts = self.prompts[session.current_level]
        
        # 현재 단계 완료 조건 확인
        should_advance = self._should_advance_step(session)
        
        if should_advance:
            session.completed_steps.append(session.current_step)
            session.current_step += 1
            
            if session.current_step > len(current_prompts):
                session.is_complete = True
                return self._handle_complete({"session_state": session.to_dict()}, ctx)
        
        # 적응형 다음 프롬프트
        next_prompt = current_prompts[min(session.current_step - 1, len(current_prompts) - 1)]
        adaptive_prompt = next_prompt.get_adaptive_prompt(session)
        
        result = {
            "response": {
                "type": "observation_received",
                "feedback": feedback,
                "observation_type": obs_type,
                "has_judgment": entry.has_judgment,
                "quality_score": entry.quality_score,
                "encouragement": self._get_encouragement(session)
            },
            "next_prompt": {
                "step": next_prompt.step,
                "prompt": adaptive_prompt,
                "hints": next_prompt.hints if session.diversity_score < 0.4 else []
            },
            "session_state": session.to_dict()
        }
        
        # DAG 조정 정보 추가 (있을 경우)
        if dag_adjustment:
            result["dag_adjustment"] = dag_adjustment
            # 예: {"action": "add_support", "type": "additional_practice", ...}
            # 이 정보로 다음에 어떤 노드를 실행할지 결정
        
        return result
    
    def _handle_get_prompt(self, payloads: Dict[str, Any], ctx: ExecutionContext) -> Dict[str, Any]:
        """현재 프롬프트 가져오기"""
        session_data = payloads.get("session_state", {})
        session = self._restore_session(session_data)
        
        current_prompts = self.prompts[session.current_level]
        current_prompt = current_prompts[min(session.current_step - 1, len(current_prompts) - 1)]
        
        return {
            "response": {
                "type": "current_prompt",
                "step": session.current_step,
                "total_steps": len(current_prompts)
            },
            "next_prompt": {
                "step": current_prompt.step,
                "instruction": current_prompt.instruction,
                "prompt": current_prompt.get_adaptive_prompt(session),
                "hints": current_prompt.hints
            },
            "session_state": session.to_dict()
        }
    
    def _handle_complete(self, payloads: Dict[str, Any], ctx: ExecutionContext) -> Dict[str, Any]:
        """세션 완료 처리"""
        session_data = payloads.get("session_state", {})
        session = self._restore_session(session_data)
        session.is_complete = True
        
        # 최종 평가
        evaluation = self._evaluate_session(session)
        
        return {
            "response": {
                "type": "session_completed",
                "message": "순수한 관찰 학습을 완료했습니다!",
                "evaluation": evaluation,
                "final_stats": {
                    "total_observations": session.total_observations,
                    "judgment_free_ratio": 1 - (session.judgment_count / max(1, session.total_observations)),
                    "diversity_score": session.diversity_score,
                    "quality_score": session.accumulated_quality
                }
            },
            "next_prompt": None,
            "session_state": session.to_dict()
        }
    
    def _restore_session(self, session_data: Dict[str, Any]) -> SessionState:
        """세션 상태 복원"""
        session = SessionState(
            session_id=session_data.get("session_id", "unknown"),
            user_id=session_data.get("user_id", "anonymous"),
            current_level=session_data.get("current_level", "L1"),
            current_step=session_data.get("current_step", 1)
        )
        
        # 기존 관찰 복원
        if "observations" in session_data:
            for obs_data in session_data["observations"]:
                obs = ObservationEntry(
                    timestamp=datetime.fromisoformat(obs_data["timestamp"]),
                    observation=obs_data["observation"],
                    observation_type=obs_data.get("type", "unknown"),
                    has_judgment=obs_data.get("has_judgment", False),
                    feedback_given=obs_data.get("feedback"),
                    quality_score=obs_data.get("quality", 0.0)
                )
                session.observations.append(obs)
        
        # 통계 복원
        if "stats" in session_data:
            stats = session_data["stats"]
            session.total_observations = stats.get("total", 0)
            session.judgment_count = stats.get("judgment_count", 0)
            session.diversity_score = stats.get("diversity", 0.0)
            session.accumulated_quality = stats.get("quality", 0.0)
        
        session.completed_steps = session_data.get("completed_steps", [])
        session.is_complete = session_data.get("is_complete", False)
        
        # UserProfile 복원 (Phase 3)
        if "user_profile" in session_data:
            profile_data = session_data["user_profile"]
            session.user_profile = UserProfile(
                user_id=profile_data["user_id"],
                persona_type=profile_data["persona_type"],
                learning_style=profile_data["learning_style"],
                selected_curriculum=profile_data["selected_curriculum"],
                profile_vector=profile_data.get("profile_vector", [])
            )
            session.selected_curriculum_id = session.user_profile.selected_curriculum
        
        # DAG 조정 기록 복원 (Phase 3)
        session.dag_adjustments = session_data.get("dag_adjustments", [])
        
        # DAG 조정기 재초기화
        if not self.dag_adjuster:
            self.dag_adjuster = SimpleDagAdjuster(session)
        
        return session
    
    def _classify_observation(self, text: str) -> str:
        """관찰 분류"""
        categories = {
            "color": ["색", "빨강", "파랑", "초록", "노랑", "검정", "흰", "회색"],
            "shape": ["네모", "동그라미", "삼각", "직선", "곡선", "모양"],
            "size": ["크", "작", "넓", "좁", "길", "짧", "두껍", "얇"],
            "position": ["위", "아래", "왼쪽", "오른쪽", "가운데", "모서리", "상단", "하단"],
            "texture": ["매끄", "거칠", "반짝", "무광", "투명", "불투명"],
            "meta": ["보이", "관찰", "느껴", "인식", "시선", "없는", "부재"]
        }
        
        for category, keywords in categories.items():
            if any(keyword in text for keyword in keywords):
                return category
        
        return "general"
    
    def _generate_feedback(self, entry: ObservationEntry, session: SessionState) -> str:
        """즉각적 피드백 생성"""
        if entry.has_judgment:
            return "판단이 들어갔네요. 평가 없이 보이는 그대로만 설명해보세요."
        
        feedbacks_by_type = {
            "color": "색상을 잘 관찰하셨네요!",
            "shape": "형태를 잘 포착하셨습니다.",
            "size": "크기 비교를 잘하고 계시네요.",
            "position": "위치를 정확히 관찰하셨어요.",
            "texture": "질감까지 관찰하시다니 훌륭해요!",
            "meta": "메타 수준의 관찰이네요. 깊이 있습니다.",
            "general": "좋습니다. 계속 관찰해주세요."
        }
        
        base_feedback = feedbacks_by_type.get(entry.observation_type, "관찰을 계속해주세요.")
        
        # 레벨별 추가 피드백
        if session.current_level == "L5" and entry.observation_type == "meta":
            base_feedback += " 관찰의 본질에 다가가고 있습니다."
        elif session.current_level == "L3" and session.diversity_score > 0.6:
            base_feedback += " 다양한 측면을 보고 계시네요."
        elif session.current_level == "L1" and session.judgment_count == 0:
            base_feedback += " 판단 없이 잘 관찰하고 있어요!"
        
        return base_feedback
    
    def _calculate_observation_quality(self, entry: ObservationEntry, session: SessionState) -> float:
        """개별 관찰 품질 점수"""
        score = 0.5  # 기본 점수
        
        # 판단 언어 없으면 가점
        if not entry.has_judgment:
            score += 0.2
        
        # 새로운 카테고리 관찰 시 가점
        previous_types = set(obs.observation_type for obs in session.observations[:-1])
        if entry.observation_type not in previous_types:
            score += 0.15
        
        # 레벨별 특별 가점
        if session.current_level == "L5":
            if entry.observation_type == "meta":
                score += 0.1
            if "없" in entry.observation or "부재" in entry.observation:
                score += 0.05
        elif session.current_level == "L3":
            if entry.observation_type in ["position", "texture"]:
                score += 0.1
        
        # 관찰 길이와 구체성
        if len(entry.observation) > 20:
            score += 0.05
        
        return min(1.0, score)
    
    def _should_advance_step(self, session: SessionState) -> bool:
        """단계 진행 조건 확인"""
        # 레벨별 최소 관찰 수
        min_observations = {
            "L1": 3,
            "L3": 5,
            "L5": 4
        }
        
        step_observations = [obs for obs in session.observations 
                            if obs.timestamp > session.started_at]  # 현재 스텝의 관찰만
        
        min_required = min_observations.get(session.current_level, 3)
        
        # 조건: 최소 관찰 수 충족 AND 최근 2개 관찰이 판단 없음
        if len(step_observations) >= min_required:
            recent = step_observations[-2:] if len(step_observations) >= 2 else step_observations
            if all(not obs.has_judgment for obs in recent):
                return True
        
        # 너무 많은 관찰 시 강제 진행
        if len(step_observations) > min_required * 2:
            return True
        
        return False
    
    def _get_encouragement(self, session: SessionState) -> str:
        """격려 메시지 생성"""
        if session.judgment_count == 0:
            return "완벽해요! 판단 없이 순수하게 관찰하고 있습니다."
        elif session.diversity_score > 0.7:
            return "다양한 측면을 관찰하고 계시네요. 훌륭합니다!"
        elif session.accumulated_quality > 0.8:
            return "매우 높은 품질의 관찰을 하고 계십니다!"
        elif session.total_observations < 3:
            return "좋은 시작입니다. 계속 관찰해보세요."
        else:
            return "잘하고 있어요. 조금 더 집중해보세요."
    
    def _evaluate_session(self, session: SessionState) -> Dict[str, Any]:
        """세션 전체 평가"""
        judgment_free_ratio = 1 - (session.judgment_count / max(1, session.total_observations))
        
        # 성공 기준
        success_criteria = {
            "L1": judgment_free_ratio > 0.7 and session.total_observations >= 10,
            "L3": judgment_free_ratio > 0.8 and session.diversity_score > 0.5,
            "L5": session.diversity_score > 0.6 and any("meta" == obs.observation_type for obs in session.observations)
        }
        
        success = success_criteria.get(session.current_level, False)
        
        # 점수 계산
        score = (
            judgment_free_ratio * 40 +  # 판단 없음 40%
            session.diversity_score * 30 +  # 다양성 30%
            session.accumulated_quality * 30  # 품질 30%
        ) * 100
        
        # 피드백 및 추천
        if score > 80:
            feedback = "훌륭합니다! 순수한 관찰을 마스터하셨습니다."
            next_module = "S2-A1" if session.current_level == "L5" else f"{session.current_level[0]}{int(session.current_level[1]) + 2}"
        elif score > 60:
            feedback = "좋습니다! 순수한 관찰의 핵심을 이해하셨네요."
            next_module = "S1-A2"
        else:
            feedback = "더 연습이 필요합니다. 판단 없이 관찰하는 것에 집중해보세요."
            next_module = "S1-A1-retry"
        
        return {
            "success": success,
            "score": round(score, 1),
            "feedback": feedback,
            "next_recommended": next_module,
            "strengths": self._identify_strengths(session),
            "areas_for_improvement": self._identify_improvements(session)
        }
    
    def _identify_strengths(self, session: SessionState) -> List[str]:
        """강점 식별"""
        strengths = []
        
        if session.judgment_count / max(1, session.total_observations) < 0.2:
            strengths.append("판단 없는 관찰")
        if session.diversity_score > 0.6:
            strengths.append("다양한 측면 관찰")
        if session.accumulated_quality > 0.7:
            strengths.append("높은 관찰 품질")
        if any(obs.observation_type == "meta" for obs in session.observations):
            strengths.append("메타 수준 인식")
        
        return strengths if strengths else ["꾸준한 관찰 노력"]
    
    def _identify_improvements(self, session: SessionState) -> List[str]:
        """개선 영역 식별"""
        improvements = []
        
        if session.judgment_count > session.total_observations * 0.3:
            improvements.append("판단 언어 줄이기")
        if session.diversity_score < 0.4:
            improvements.append("다양한 측면 관찰하기")
        if session.accumulated_quality < 0.5:
            improvements.append("더 구체적으로 관찰하기")
        if not any(obs.observation_type in ["texture", "meta"] for obs in session.observations):
            improvements.append("깊이 있는 관찰 시도하기")
        
        return improvements if improvements else ["일관성 유지하기"]
    
    def learning_objectives(self) -> List[str]:
        """학습 목표"""
        return [
            "실시간으로 판단 없는 관찰 연습",
            "즉각적 피드백을 통한 학습",
            "관찰 품질의 점진적 향상",
            "메타 인지 능력 개발"
        ]
    
    def get_module_metadata(self) -> Dict[str, Any]:
        """모듈 메타데이터"""
        return {
            "module_id": "S1-A1-interactive",
            "module_name": "순수한 관찰 (인터랙티브)",
            "version": "3.1.0",
            "features": [
                "Phase 2: 실시간 인터랙티비티",
                "Phase 3: 세션 상태 관리",
                "적응형 프롬프트",
                "즉각적 피드백",
                "진행 상황 추적"
            ],
            "improvements_over_base": [
                "관찰 하나씩 실시간 처리",
                "세션 상태 유지 및 복원",
                "적응형 프롬프트 생성",
                "개별 관찰 품질 평가",
                "진행 조건 자동 판단"
            ]
        }
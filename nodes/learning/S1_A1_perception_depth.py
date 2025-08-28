"""
S1-A1: 순수한 관찰 (Pure Observation)
지각인지 × 정보처리깊이

기반 문서:
- docs/8x4-matrix/modules/MODULE_TEMPLATE_v3.0.md
- docs/8x4-matrix/modules/S1-A1/S1-A1-module_design.md

module_id: S1-A1
core_concept: "감각적 수용" - 판단 없이 있는 그대로 관찰
estimated_time: standalone: 10-15분, integrated: 5-7분
"""
from typing import Any, Dict, List, Optional, Literal
from enum import Enum
from dataclasses import dataclass
from nodes.base.base_node import AbstractBaseNode
from nodes.base.interfaces import NodeIO, PortSchema, ExecutionContext


class DifficultyLevel(Enum):
    L1 = "초급"  # 완전 초보자
    L3 = "중급"  # 기초 학습자  
    L5 = "고급"  # 전문가 수준


@dataclass
class ActivityStep:
    """활동 단계 정의"""
    step: int
    instruction: str
    ai_prompt: str
    expected_response_type: str
    time_seconds: int
    cognitive_load: str = "낮음"
    special_feature: Optional[str] = None


class S1_A1_PureObservationNode(AbstractBaseNode):
    """
    S1: 지각인지 - 감각 자극을 왜곡 없이 받아들이는 단계
    A1: 정보처리깊이 - 감각 입력에서 메타 수준까지의 처리 심도
    
    핵심: "순수한 관찰" - 판단 없이 보는 경험
    """
    
    def __init__(self):
        io = NodeIO(
            inputs=[
                PortSchema(
                    name="user_level",
                    description="사용자 레벨 (L1/L3/L5)",
                    content_type="application/json"
                ),
                PortSchema(
                    name="observation_target",
                    description="관찰 대상 (화면, 인터페이스 등)",
                    content_type="application/json"
                ),
                PortSchema(
                    name="user_responses",
                    description="사용자의 관찰 응답들",
                    content_type="application/json"
                )
            ],
            outputs=[
                PortSchema(
                    name="activity_sequence",
                    description="레벨별 활동 시퀀스",
                    content_type="application/json"
                ),
                PortSchema(
                    name="ai_guidance",
                    description="AI 응답 가이드",
                    content_type="application/json"
                ),
                PortSchema(
                    name="observation_metrics",
                    description="관찰 품질 메트릭",
                    content_type="application/json"
                )
            ]
        )
        
        super().__init__(
            node_id="S1-A1",
            name="순수한 관찰",
            version="3.0.0",
            io=io,
            description="판단 없이 있는 그대로 관찰하는 학습 모듈"
        )
        
        # 레벨별 활동 시퀀스 정의
        self.activities = self._define_activities()
    
    def _define_activities(self) -> Dict[str, List[ActivityStep]]:
        """레벨별 활동 시퀀스 정의"""
        return {
            "L1": [  # 초급 - AI 도구 첫 사용자
                ActivityStep(1, "ChatGPT 화면을 열어주세요", 
                           "화면에서 가장 먼저 눈에 들어오는 것은 무엇인가요? 색깔이나 모양을 말해주세요.",
                           "단순 관찰 (예: 파란색 버튼, 흰 배경)", 30, "낮음"),
                ActivityStep(2, "화면을 천천히 둘러보세요. 무엇이 보이나요?",
                           "입력창은 어디에 있나요? 어떤 모양인가요?",
                           "위치와 형태 설명", 60, "낮음", "공간 인식"),
                ActivityStep(3, "이번엔 더 자세히 봐주세요",
                           "화면에서 볼 수 있는 색깔을 모두 말해주세요",
                           "색상 나열", 60, "낮음"),
                ActivityStep(4, "색깔에 집중해보세요",
                           "가장 큰 요소와 가장 작은 요소는 무엇인가요?",
                           "상대적 크기 비교", 60, "낮음"),
                ActivityStep(5, "크기를 비교해보세요",
                           "지금까지 본 것을 한 번에 설명해주세요",
                           "종합 관찰", 90, "낮음")
            ],
            "L3": [  # 중급 - 기초 학습자
                ActivityStep(1, "여러 개의 AI 대화가 있는 화면을 보세요",
                           "화면이 몇 개의 영역으로 나뉘어 있나요? 각 영역의 크기는?",
                           "레이아웃 분석", 30, "중간"),
                ActivityStep(2, "전체 레이아웃을 관찰하세요",
                           "어떤 요소들이 서로 가까이 있나요? 정렬은 어떻게 되어 있나요?",
                           "공간 관계 파악", 120, "중간", "다중 모달"),
                ActivityStep(3, "요소들 사이의 관계를 보세요",
                           "여백은 어디에 얼마나 있나요? 그 비율은?",
                           "빈 공간 인식", 120, "중간"),
                ActivityStep(4, "빈 공간도 관찰하세요",
                           "전체적으로 어떤 패턴이 보이나요?",
                           "패턴 인식", 120, "중간"),
                ActivityStep(5, "전체를 한 번에 보고 설명해보세요",
                           "가장 중요해 보이는 영역은 어디인가요? (판단하지 말고 관찰만)",
                           "종합적 관찰", 90, "중간")
            ],
            "L5": [  # 고급 - 전문가 수준
                ActivityStep(1, "1분간 화면을 응시만 하세요",
                           "첫 관찰에서 놓친 것은 무엇인가요?",
                           "메타 관찰", 60, "높음"),
                ActivityStep(2, "지금까지 보지 못했던 것을 찾으세요",
                           "있을 법한데 없는 것은? 비어있는 곳의 의미는?",
                           "부재의 인식", 120, "높음", "메타인지"),
                ActivityStep(3, "없는 것을 관찰하세요",
                           "당신의 눈은 어떤 경로로 움직였나요?",
                           "시선 추적", 180, "높음"),
                ActivityStep(4, "시선의 움직임을 관찰하세요",
                           "관찰하는 동안 당신에게 어떤 변화가 있었나요?",
                           "자기 인식", 120, "높음", "초월적"),
                ActivityStep(5, "관찰하는 자신을 관찰하세요",
                           "순수한 관찰이란 무엇일까요?",
                           "철학적 성찰", 120, "매우 높음")
            ]
        }
    
    def _run(self, payloads: Dict[str, Any], ctx: ExecutionContext) -> Dict[str, Any]:
        """실제 학습 로직 구현"""
        user_level = payloads.get("user_level", "L1")
        observation_target = payloads.get("observation_target", {})
        user_responses = payloads.get("user_responses", [])
        
        # 1. 레벨에 맞는 활동 시퀀스 가져오기
        activities = self.activities.get(user_level, self.activities["L1"])
        
        # 2. AI 가이드 생성
        ai_guidance = self._generate_ai_guidance(user_level)
        
        # 3. 관찰 품질 평가
        metrics = self._evaluate_observation_quality(user_responses, user_level)
        
        return {
            "activity_sequence": [
                {
                    "step": act.step,
                    "instruction": act.instruction,
                    "ai_prompt": act.ai_prompt,
                    "expected_response": act.expected_response_type,
                    "duration": act.time_seconds,
                    "cognitive_load": act.cognitive_load,
                    "special_feature": act.special_feature
                } for act in activities
            ],
            "ai_guidance": ai_guidance,
            "observation_metrics": metrics
        }
    
    def _generate_ai_guidance(self, level: str) -> Dict[str, Any]:
        """레벨별 AI 응답 가이드 생성"""
        guides = {
            "L1": {
                "tone": "친근하고 격려적",
                "avoid": ["분석적 해석", "기능 설명", "판단이나 평가"],
                "encourage": ["있는 그대로 표현", "감각적 언어 사용", "단순한 관찰"],
                "sample_responses": {
                    "good": "네, 파란색 버튼이 보이시는군요! 또 무엇이 보이나요?",
                    "redirect": "버튼의 기능보다는, 그냥 어떻게 생겼는지 말해주세요.",
                    "encouragement": "아주 잘 관찰하고 계세요! 계속해보세요."
                }
            },
            "L3": {
                "tone": "탐구적이고 호기심 유발",
                "focus": ["공간적 관계", "비례와 균형", "세부와 전체"],
                "scaffolding": ["부분에서 전체로 안내"],
                "sample_responses": {
                    "probing": "그 영역들이 어떤 패턴으로 배치되어 있나요?",
                    "synthesis": "전체적으로 보면 어떤 형태가 떠오르나요?",
                    "challenge": "가장 작은 디테일은 무엇인가요?"
                }
            },
            "L5": {
                "sophistication": "매우 높음",
                "approach": ["현상학적 접근", "메타 인지 유도", "침묵의 활용"],
                "language": ["미니멀한 개입", "시적 표현", "열린 질문"],
                "sample_responses": {
                    "philosophical": "보는 것과 보이는 것의 차이는...",
                    "paradoxical": "보지 않음으로써 보게 되는 것은...",
                    "metacognitive": "지금 당신이 하고 있는 '보기'란..."
                }
            }
        }
        return guides.get(level, guides["L1"])
    
    def _evaluate_observation_quality(self, responses: List[str], level: str) -> Dict[str, Any]:
        """관찰 품질 평가"""
        # 판단 언어 감지
        judgment_words = ["좋다", "나쁘다", "예쁘다", "못생겼다", "편하다", "불편하다"]
        judgment_count = sum(1 for r in responses for word in judgment_words if word in r)
        
        # 관찰 다양성 계산
        observation_categories = {
            "색상": ["빨강", "파랑", "초록", "노랑", "검정", "흰", "회색"],
            "형태": ["네모", "동그라미", "삼각", "직선", "곡선"],
            "크기": ["크다", "작다", "넓다", "좁다", "길다", "짧다"],
            "위치": ["위", "아래", "왼쪽", "오른쪽", "가운데", "모서리"],
            "질감": ["매끄럽다", "거칠다", "반짝", "무광"]
        }
        
        diversity_score = 0
        for category, keywords in observation_categories.items():
            if any(keyword in ' '.join(responses) for keyword in keywords):
                diversity_score += 1
        
        return {
            "observation_count": len(responses),
            "judgment_language_use": judgment_count,
            "observation_diversity": diversity_score,
            "quality_score": self._calculate_quality_score(
                len(responses), judgment_count, diversity_score, level
            ),
            "success_indicators": self._check_success_indicators(responses, level)
        }
    
    def _calculate_quality_score(self, obs_count: int, judge_count: int, 
                                diversity: int, level: str) -> float:
        """품질 점수 계산"""
        base_score = 0.5
        
        # 관찰 개수 점수
        if level == "L1" and obs_count >= 5:
            base_score += 0.2
        elif level == "L3" and obs_count >= 8:
            base_score += 0.2
        elif level == "L5" and obs_count >= 10:
            base_score += 0.2
        
        # 판단 언어 사용 감점
        base_score -= (judge_count * 0.1)
        
        # 다양성 가점
        base_score += (diversity * 0.05)
        
        return max(0, min(1.0, base_score))
    
    def _check_success_indicators(self, responses: List[str], level: str) -> List[str]:
        """성공 지표 확인"""
        indicators = []
        
        if level == "L1":
            if len(responses) >= 5:
                indicators.append("5개 이상의 시각적 요소 관찰")
            if not any(word in ' '.join(responses) for word in ["좋다", "나쁘다"]):
                indicators.append("판단 언어 사용 안 함")
        
        elif level == "L3":
            if "영역" in ' '.join(responses):
                indicators.append("공간 영역 인식")
            if "패턴" in ' '.join(responses):
                indicators.append("패턴 인식")
        
        elif level == "L5":
            if any(word in ' '.join(responses) for word in ["없는", "부재", "비어"]):
                indicators.append("부재의 인식")
            if any(word in ' '.join(responses) for word in ["나", "내가", "자신"]):
                indicators.append("메타 관찰 수행")
        
        return indicators
    
    def learning_objectives(self) -> List[str]:
        """LearningModuleNode 인터페이스 구현"""
        return [
            "판단 없이 보는 경험 체득",
            "단순 관찰 능력 활성화",
            "감각 정보를 왜곡 없이 받아들이기"
        ]
    
    def evaluate_outcomes(self, outputs: Dict[str, Any]) -> Dict[str, Any]:
        """LearningModuleNode 인터페이스 구현"""
        metrics = outputs.get("observation_metrics", {})
        quality_score = metrics.get("quality_score", 0)
        indicators = metrics.get("success_indicators", [])
        
        # 레벨별 성공 기준
        success = False
        if "판단 언어 사용 안 함" in indicators:
            success = True
        if quality_score > 0.7:
            success = True
        
        # 다음 단계 추천
        if quality_score > 0.8:
            next_module = "S1-A2"  # 다음 축으로 진행
            feedback = "훌륭합니다! 순수한 관찰을 마스터하셨습니다."
        elif quality_score > 0.6:
            next_module = "S2-A1"  # 다음 단계로 진행
            feedback = "좋습니다! 이제 의미를 부여하는 단계로 나아갈 준비가 되었습니다."
        else:
            next_module = "S1-A1-retry"  # 다시 시도
            feedback = "조금 더 연습이 필요합니다. 판단 없이 관찰하는 것에 집중해보세요."
        
        return {
            "success": success,
            "score": quality_score * 100,
            "feedback": feedback,
            "next_recommended": next_module,
            "achieved_indicators": indicators,
            "module_insights": {
                "core_concept_mastery": "감각적 수용" in ' '.join(indicators),
                "judgment_free_observation": metrics.get("judgment_language_use", 0) <= 3,
                "observation_diversity": metrics.get("observation_diversity", 0) >= 3
            }
        }
    
    def get_module_metadata(self) -> Dict[str, Any]:
        """모듈 메타데이터 반환"""
        return {
            "module_id": "S1-A1",
            "module_name": "순수한 관찰",
            "korean_name": "지각인지 × 정보처리깊이",
            "english_name": "Perceptual Cognition × Information Processing Depth",
            "core_concept": "감각적 수용",
            "stage": {
                "number": 1,
                "name": "지각인지",
                "focus": "감각 자극을 왜곡 없이 받아들이기"
            },
            "axis": {
                "number": 1,
                "name": "정보처리깊이",
                "focus": "감각 입력에서 메타 수준까지의 처리 심도"
            },
            "difficulty_range": {
                "min": "L1",
                "max": "L5",
                "sweet_spot": "L3"
            },
            "typical_duration": {
                "standalone": "10-15분",
                "as_part": "5-7분"
            },
            "next_modules": {
                "natural_progression": "S2-A1",  # 다음 단계
                "complementary": "S1-A2",  # 같은 단계 다른 축
                "advanced": "S3-A1"  # 심화 학습
            }
        }
"""
S1-A1 순수 관찰 교수법 노드
판단 없는 감각적 수용 훈련을 위한 특화 교수법
Module: S1-A1 (지각인지 × 정보처리깊이)
Core Concept: 감각적 수용, 판단 제거, 순수 기술
"""
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from enum import Enum
from nodes.base.base_node import AbstractBaseNode
from nodes.base.interfaces import NodeIO, PortSchema, ExecutionContext


@dataclass
class QuizQuestion:
    """퀴즈 문항 구조"""
    id: str
    question: str
    type: str
    options: Optional[List[str]] = None  # 객관식용
    correct_answer: Optional[Any] = None
    hints: List[str] = None
    difficulty: int = 1
    time_limit: int = 60
    
@dataclass
class QuizResponse:
    """퀴즈 응답 구조"""
    question_id: str
    user_answer: Any
    time_taken: float
    hints_used: int = 0


class ObservationQuizMethod(AbstractBaseNode):
    """퀴즈 방식 교수법 - 관찰력 평가 및 훈련"""
    
    def __init__(self):
        io = NodeIO(
            inputs=[
                PortSchema(
                    name="scene",
                    description="관찰 대상 (이미지, 텍스트, 비디오 등)",
                    content_type="application/json"
                ),
                PortSchema(
                    name="level",
                    description="난이도 (L1/L2/L3)",
                    content_type="text/plain"
                ),
                PortSchema(
                    name="mode",
                    description="퀴즈 모드 (practice/test/adaptive)",
                    content_type="text/plain"
                ),
                PortSchema(
                    name="user_responses",
                    description="사용자 응답 (평가용)",
                    content_type="application/json"
                )
            ],
            outputs=[
                PortSchema(
                    name="quiz_items",
                    description="퀴즈 문항 세트",
                    content_type="application/json"
                ),
                PortSchema(
                    name="evaluation",
                    description="평가 결과",
                    content_type="application/json"
                ),
                PortSchema(
                    name="feedback",
                    description="학습 피드백",
                    content_type="application/json"
                )
            ]
        )
        super().__init__(
            node_id="S1-A1-QZ",
            name="Observation Quiz Method",
            version="2.0.0",
            io=io,
            description="관찰력 훈련을 위한 적응형 퀴즈 시스템"
        )
    
    def _run(self, payloads: Dict[str, Any], ctx: ExecutionContext) -> Dict[str, Any]:
        scene = payloads.get("scene", {})
        level = payloads.get("level", "L1")
        mode = payloads.get("mode", "practice")
        user_responses = payloads.get("user_responses", None)
        
        # 퀴즈 생성
        quiz_templates = {
            "L1": self._get_basic_quiz(scene),
            "L2": self._get_intermediate_quiz(scene),
            "L3": self._get_advanced_quiz(scene)
        }
        
        quiz_items = quiz_templates.get(level, quiz_templates["L1"])
        
        # 사용자 응답이 있으면 평가
        evaluation = None
        feedback = None
        if user_responses:
            evaluation = self._evaluate_responses(quiz_items, user_responses)
            feedback = self._generate_feedback(evaluation, level)
        
        return {
            "quiz_items": quiz_items,
            "level": level,
            "mode": mode,
            "total_questions": len(quiz_items),
            "time_limit": 60 * len(quiz_items),  # 문항당 60초
            "evaluation": evaluation,
            "feedback": feedback
        }
    
    def _evaluate_responses(self, quiz_items: List[Dict], responses: List[Dict]) -> Dict:
        """사용자 응답 평가"""
        total_score = 0
        max_score = len(quiz_items) * 10
        details = []
        
        for quiz, response in zip(quiz_items, responses):
            is_correct = self._check_answer(quiz, response)
            score = 10 if is_correct else 0
            
            # 부분 점수 처리
            if not is_correct and quiz.get("type") == "numeric":
                if self._is_within_range(quiz, response):
                    score = 5  # 부분 점수
            
            total_score += score
            details.append({
                "question_id": quiz["id"],
                "correct": is_correct,
                "score": score,
                "time_taken": response.get("time_taken", 0),
                "hints_used": response.get("hints_used", 0)
            })
        
        return {
            "total_score": total_score,
            "max_score": max_score,
            "percentage": (total_score / max_score) * 100,
            "details": details,
            "passed": total_score >= max_score * 0.7
        }
    
    def _generate_feedback(self, evaluation: Dict, level: str) -> Dict:
        """학습 피드백 생성"""
        percentage = evaluation["percentage"]
        
        if percentage >= 90:
            message = "훌륭합니다! 관찰력이 매우 뛰어나네요."
            recommendation = f"다음 레벨(L{int(level[1]) + 1})로 진행하세요."
        elif percentage >= 70:
            message = "좋습니다! 조금 더 연습하면 완벽해질 거예요."
            recommendation = "틀린 문제를 다시 풀어보세요."
        else:
            message = "더 연습이 필요해요. 천천히 관찰해보세요."
            recommendation = "기초부터 다시 시작해보세요."
        
        weak_areas = self._identify_weak_areas(evaluation["details"])
        
        return {
            "message": message,
            "recommendation": recommendation,
            "score_summary": f"{evaluation['total_score']}/{evaluation['max_score']}",
            "weak_areas": weak_areas,
            "next_steps": self._suggest_next_steps(evaluation, level)
        }
    
    def _get_basic_quiz(self, scene: Dict) -> List[Dict]:
        """L1: 순수 관찰 초급 - 판단 없는 감각 수용"""
        scene_type = scene.get("type", "image")
        
        # S1-A1 특화: 판단 언어 제거, 순수 감각 집중
        return [
            {
                "id": "S1A1_L1_Q1",
                "question": "지금 보이는 색깔을 모두 나열해주세요. '예쁘다', '좋다' 같은 판단 없이요.",
                "type": "open_ended",
                "forbidden_words": ["예쁘다", "좋다", "나쁘다", "이상하다", "멋지다"],
                "evaluation_criteria": "판단 언어 사용 여부",
                "hints": ["색 이름만 말하세요", "느낌이 아닌 색상만"],
                "s1a1_focus": "pure_observation"
            },
            {
                "id": "S1A1_L1_Q2",
                "question": "왼쪽에 무엇이 있나요? 그것의 모양과 크기를 설명하세요.",
                "type": "descriptive",
                "check_for": ["형태 언급", "크기 언급", "위치 언급"],
                "avoid": ["용도 설명", "가치 판단"],
                "hints": ["모양을 그려본다고 생각하세요", "자로 잰다고 상상하세요"],
                "s1a1_focus": "spatial_description"
            },
            {
                "id": "S1A1_L1_Q3",
                "question": "어떤 부분이 더 밝고, 어떤 부분이 더 어두운가요?",
                "type": "comparative",
                "focus": "brightness_only",
                "correct_approach": "상대적 명도 비교",
                "wrong_approach": "감정적 표현",
                "hints": ["빛의 양만 비교하세요", "그림자를 찾아보세요"],
                "s1a1_focus": "light_observation"
            },
            {
                "id": "S1A1_L1_Q4",
                "question": "'둥글다'고 표현할 수 있는 것들을 찾아주세요.",
                "type": "shape_identification",
                "target_shape": "circle",
                "evaluation": "shape_accuracy",
                "hints": ["완전한 원이 아니어도 됩니다", "곡선을 찾아보세요"],
                "s1a1_focus": "shape_recognition"
            }
        ]
    
    def _get_intermediate_quiz(self, scene: Dict) -> List[Dict]:
        """L3: 순수 관찰 중급 - 관계와 패턴의 순수 기술"""
        return [
            {
                "id": "S1A1_L3_Q1",
                "question": "요소들 사이의 거리를 손가락 너비로 표현해보세요.",
                "type": "measurement_description",
                "focus": "spatial_relationship",
                "unit": "body_measurement",  # 신체 척도 사용
                "hints": ["손가락 몇 개 너비인지", "팔 길이와 비교하면"],
                "s1a1_focus": "distance_observation"
            },
            {
                "id": "S1A1_L3_Q2",
                "question": "같은 것이 반복되는 부분이 있나요? 몇 번 반복되나요?",
                "type": "pattern_counting",
                "focus": "repetition_identification",
                "evaluation": "counting_accuracy",
                "hints": ["똑같은 모양 찾기", "규칙적인 간격 찾기"],
                "forbidden_words": ["지루하다", "단조롭다", "아름답다"],
                "s1a1_focus": "pattern_observation"
            },
            {
                "id": "S1A1_L3_Q3",
                "question": "색의 진하기 순서대로 나열해보세요. 가장 연한 것부터.",
                "type": "gradient_ordering",
                "focus": "color_intensity",
                "evaluation": "sequence_accuracy",
                "hints": ["채도가 아닌 명도로", "회색에 가까운 순서"],
                "s1a1_focus": "intensity_discrimination"
            },
            {
                "id": "S1A1_L3_Q4",
                "question": "선이 만나는 곳을 찾아 각도를 손으로 표현해보세요.",
                "type": "angle_description",
                "focus": "intersection_points",
                "expression_method": "physical_gesture",
                "hints": ["직각? 예각? 둔각?", "손가락으로 각도 만들기"],
                "s1a1_focus": "angle_observation"
            }
        ]
    
    def _get_advanced_quiz(self, scene: Dict) -> List[Dict]:
        """L5: 순수 관찰 고급 - 미세한 차이와 깊은 관찰"""
        return [
            {
                "id": "S1A1_L5_Q1",
                "question": "가장 미세한 색상 차이를 찾아 설명해주세요. 거의 같지만 다른 것들.",
                "type": "subtle_discrimination",
                "focus": "micro_differences",
                "challenge_level": "expert",
                "hints": ["같은 색의 다른 톤", "그림자 속 색상 변화"],
                "s1a1_focus": "subtle_observation"
            },
            {
                "id": "S1A1_L5_Q2",
                "question": "시선이 자연스럽게 움직이는 경로를 순서대로 기술하세요.",
                "type": "visual_flow_tracking",
                "focus": "eye_movement_path",
                "record_method": "sequential_description",
                "hints": ["처음 본 곳 → 다음 → 다음", "시선의 여행 경로"],
                "forbidden": ["중요하다", "의미있다", "핵심이다"],
                "s1a1_focus": "flow_observation"
            },
            {
                "id": "S1A1_L5_Q3",
                "question": "똑같아 보이지만 다른 부분들을 10개 찾아보세요.",
                "type": "difference_hunting",
                "target_count": 10,
                "focus": "asymmetry_detection",
                "hints": ["대칭인 듯 아닌 것", "규칙 속 예외"],
                "s1a1_focus": "detail_discrimination"
            },
            {
                "id": "S1A1_L5_Q4",
                "question": "1분간 한 점만 보고, 그 점 주변에서 일어나는 변화를 설명하세요.",
                "type": "peripheral_observation",
                "duration": 60,
                "focus": "peripheral_vision",
                "technique": "soft_focus",
                "hints": ["초점 고정, 주변 인식", "움직임 없이 관찰"],
                "s1a1_focus": "sustained_attention"
            }
        ]
    
    # 헬퍼 메서드들
    def _analyze_brightness(self, scene: Dict) -> str:
        """장면의 밝기 분석 (실제 구현시 이미지 처리)"""
        return "흰색"  # 예시
    
    def _count_shapes(self, scene: Dict) -> int:
        """도형 개수 세기"""
        return 5  # 예시
    
    def _find_largest_position(self, scene: Dict) -> str:
        """가장 큰 요소 위치 찾기"""
        return "중앙"  # 예시
    
    def _get_text_based_quiz(self, scene: Dict) -> List[Dict]:
        """텍스트 기반 퀴즈"""
        return [
            {
                "id": "L1_T1",
                "question": "텍스트에서 가장 자주 나타나는 단어는?",
                "type": "open_ended",
                "evaluation_criteria": "텍스트 관찰 능력"
            }
        ]
    
    def _check_answer(self, quiz: Dict, response: Dict) -> bool:
        """S1-A1 특화 답안 확인 - 판단 언어 체크 중심"""
        answer_text = response.get("answer", "")
        quiz_type = quiz.get("type")
        
        # S1-A1 핵심: 판단 언어 사용 체크
        if quiz.get("forbidden_words"):
            for word in quiz.get("forbidden_words", []):
                if word in answer_text:
                    return False  # 판단 언어 사용시 오답
        
        # 타입별 평가
        if quiz_type == "open_ended":
            # 순수 관찰 언어만 사용했는지 체크
            return self._is_pure_observation(answer_text)
        elif quiz_type == "descriptive":
            # 필수 요소 포함 여부
            check_items = quiz.get("check_for", [])
            return all(item in answer_text for item in check_items)
        elif quiz_type == "comparative":
            # 비교 관찰 정확성
            return self._check_comparative(answer_text, quiz)
        
        return True  # S1-A1은 정답보다 관찰 방식이 중요
    
    def _is_within_range(self, quiz: Dict, response: Dict) -> bool:
        """허용 범위 내 확인"""
        if quiz.get("type") == "numeric":
            correct = quiz.get("correct_answer", 0)
            user_answer = response.get("answer", -999)
            return abs(correct - user_answer) <= quiz.get("acceptable_range", 0) * 2
        return False
    
    def _identify_weak_areas(self, details: List[Dict]) -> List[str]:
        """약점 분석"""
        weak = []
        for detail in details:
            if not detail["correct"]:
                weak.append(detail["question_id"])
        return weak
    
    def _suggest_next_steps(self, evaluation: Dict, level: str) -> List[str]:
        """S1-A1 다음 학습 단계 제안"""
        if evaluation["passed"]:
            return [
                "더 복잡한 장면 관찰하기",
                "관찰 시간 늘리기 (5분 → 10분)",
                "다른 감각으로 관찰 (소리, 촉감)"
            ]
        else:
            return [
                "판단 언어 인식 연습",
                "단순 도형부터 다시 관찰",
                "관찰 일기 작성하기"
            ]
    
    # S1-A1 특화 메서드들
    def _is_pure_observation(self, text: str) -> bool:
        """순수 관찰 언어 사용 여부 체크"""
        judgment_words = [
            "좋다", "나쁘다", "예쁘다", "못생겼다", "멋지다",
            "이상하다", "훌륭하다", "형편없다", "아름답다", "추하다"
        ]
        return not any(word in text for word in judgment_words)
    
    def _check_comparative(self, text: str, quiz: Dict) -> bool:
        """비교 관찰의 정확성 체크"""
        if quiz.get("focus") == "brightness_only":
            # 밝기 비교만 허용
            allowed_terms = ["밝다", "어둡다", "진하다", "연하다", "선명하다"]
            return any(term in text for term in allowed_terms)
        return True
    
    def _analyze_observation_quality(self, responses: List[Dict]) -> Dict:
        """S1-A1 관찰 품질 분석"""
        pure_count = 0
        judgment_count = 0
        descriptive_count = 0
        
        for response in responses:
            text = response.get("answer", "")
            if self._is_pure_observation(text):
                pure_count += 1
            else:
                judgment_count += 1
            
            # 서술적 요소 카운트
            if len(text.split()) > 5:
                descriptive_count += 1
        
        return {
            "pure_observation_rate": pure_count / len(responses) * 100,
            "judgment_usage_rate": judgment_count / len(responses) * 100,
            "descriptive_quality": descriptive_count / len(responses) * 100
        }


class S1A1DialogueMethod(AbstractBaseNode):
    """S1-A1 대화/토론 방식 - 판단 제거 대화법"""
    
    def __init__(self):
        io = NodeIO(
            inputs=[
                PortSchema(
                    name="observations",
                    description="사용자의 관찰 내용",
                    content_type="application/json"
                ),
                PortSchema(
                    name="level",
                    description="난이도 레벨",
                    content_type="text/plain"
                )
            ],
            outputs=[
                PortSchema(
                    name="dialogue_flow",
                    description="대화 진행 가이드",
                    content_type="application/json"
                ),
                PortSchema(
                    name="reflection_prompts",
                    description="성찰 질문",
                    content_type="application/json"
                )
            ]
        )
        super().__init__(
            node_id="S1-A1-DG",
            name="S1-A1 Dialogue Method",
            version="2.0.0",
            io=io,
            description="순수 관찰을 위한 소크라테스식 대화"
        )
    
    def _run(self, payloads: Dict[str, Any], ctx: ExecutionContext) -> Dict[str, Any]:
        observations = payloads.get("observations", [])
        level = payloads.get("level", "L1")
        
        # 레벨별 대화 전략
        dialogue_flow = self._get_dialogue_flow(level, observations)
        reflection_prompts = self._get_reflection_prompts(level)
        
        return {
            "dialogue_flow": dialogue_flow,
            "reflection_prompts": reflection_prompts,
            "technique": "socratic_method",
            "focus": "removing_judgment"
        }
    
    def _get_dialogue_flow(self, level: str, observations: List) -> List[Dict]:
        """S1-A1 특화 대화 흐름"""
        if level == "L1":
            return [
                {
                    "step": 1,
                    "ai_says": "무엇이 보이나요? 천천히 말씀해주세요.",
                    "listen_for": ["판단 언어", "감정 표현"],
                    "redirect_if_needed": "그것이 '어떻게 생겼는지'만 말해주세요."
                },
                {
                    "step": 2,
                    "ai_says": "방금 '예쁘다'고 하셨는데, 대신 어떻게 표현할 수 있을까요?",
                    "guide": "색상, 모양, 크기로 다시 설명 유도",
                    "example": "'예쁘다' → '분홍색이고 둥글다'"
                },
                {
                    "step": 3,
                    "ai_says": "이번엔 색깔만 말해보세요. 느낌 말고 색 이름만요.",
                    "practice": "pure_color_naming",
                    "avoid": ["좋은 색", "따뜻한 색", "차가운 색"]
                }
            ]
        elif level == "L3":
            return [
                {
                    "step": 1,
                    "ai_says": "보이는 것을 숫자로 표현해보세요. 몇 개? 얼마나?",
                    "focus": "quantification",
                    "example": "3개의 원, 5cm 정도 간격"
                },
                {
                    "step": 2,
                    "ai_says": "패턴이 있나요? 반복되는 것을 찾아보세요.",
                    "focus": "pattern_recognition",
                    "guide": "규칙성만 설명, 의미 부여 금지"
                }
            ]
        else:  # L5
            return [
                {
                    "step": 1,
                    "ai_says": "1분간 침묵하며 관찰 후, 가장 미세한 변화를 포착해보세요.",
                    "technique": "mindful_observation",
                    "duration": 60
                },
                {
                    "step": 2,
                    "ai_says": "관찰하면서 떠오른 판단들을 인식하셨나요? 어떤 것들이었나요?",
                    "focus": "metacognition",
                    "purpose": "판단 인식 훈련"
                }
            ]
    
    def _get_reflection_prompts(self, level: str) -> List[str]:
        """S1-A1 성찰 질문"""
        base_prompts = [
            "판단 없이 보는 것이 왜 어려웠을까요?",
            "평소와 다르게 본 것이 있나요?",
            "관찰만 했을 때 새로 발견한 것은?"
        ]
        
        if level == "L5":
            base_prompts.extend([
                "판단이 관찰을 어떻게 방해하나요?",
                "순수한 관찰이 주는 통찰은 무엇인가요?"
            ])
        
        return base_prompts


class S1A1PracticeMethod(AbstractBaseNode):
    """S1-A1 관찰 실습 방식 - 감각 분리 훈련"""
    
    def __init__(self):
        io = NodeIO(
            inputs=[
                PortSchema(
                    name="target",
                    description="관찰 대상",
                    content_type="application/json"
                ),
                PortSchema(
                    name="level",
                    description="실습 레벨",
                    content_type="text/plain"
                ),
                PortSchema(
                    name="user_notes",
                    description="사용자 관찰 노트",
                    content_type="text/plain"
                )
            ],
            outputs=[
                PortSchema(
                    name="practice_sequence",
                    description="단계별 실습 가이드",
                    content_type="application/json"
                ),
                PortSchema(
                    name="judgment_filter",
                    description="판단 언어 필터링 결과",
                    content_type="application/json"
                ),
                PortSchema(
                    name="progress_tracking",
                    description="실습 진행 추적",
                    content_type="application/json"
                )
            ]
        )
        super().__init__(
            node_id="S1-A1-PR",
            name="S1-A1 Practice Method",
            version="2.0.0",
            io=io,
            description="순수 관찰을 위한 감각 분리 실습"
        )
    
    def _run(self, payloads: Dict[str, Any], ctx: ExecutionContext) -> Dict[str, Any]:
        target = payloads.get("target", {})
        level = payloads.get("level", "L1")
        user_notes = payloads.get("user_notes", "")
        
        # 레벨별 실습 시퀀스
        practice_sequence = self._get_practice_sequence(level)
        
        # 판단 언어 필터링
        judgment_filter = self._filter_judgment_language(user_notes) if user_notes else None
        
        # 진행 상황 추적
        progress = self._track_progress(level, user_notes)
        
        return {
            "practice_sequence": practice_sequence,
            "judgment_filter": judgment_filter,
            "progress_tracking": progress,
            "technique": "sensory_isolation",
            "core_focus": "pure_observation_training"
        }
    
    def _get_practice_sequence(self, level: str) -> List[Dict]:
        """레벨별 실습 시퀀스"""
        if level == "L1":
            return [
                {
                    "step": 1,
                    "title": "색상만 관찰",
                    "duration": 30,
                    "instruction": "30초 동안 색상만 보세요. 형태는 무시하세요.",
                    "focus": "color_only",
                    "tips": ["눈을 가늘게 뜨면 형태가 흐려집니다", "색 이름을 속으로 말해보세요"],
                    "forbidden": ["예쁜 색", "좋은 색", "따뜻한 색"]
                },
                {
                    "step": 2,
                    "title": "모양만 관찰",
                    "duration": 30,
                    "instruction": "30초 동안 모양만 보세요. 색은 무시하세요.",
                    "focus": "shape_only",
                    "tips": ["윤곽선만 따라가세요", "도형으로 단순화해보세요"],
                    "check": "둥글다, 네모나다, 길다, 짧다"
                },
                {
                    "step": 3,
                    "title": "크기만 관찰",
                    "duration": 30,
                    "instruction": "30초 동안 크기와 비율만 보세요.",
                    "focus": "size_only",
                    "tips": ["손가락으로 크기 재보기", "상대적 크기 비교"],
                    "measurement": "body_scale"
                },
                {
                    "step": 4,
                    "title": "통합 관찰",
                    "duration": 60,
                    "instruction": "1분간 전체를 다시 보며 놓친 것 찾기",
                    "synthesis": True,
                    "reflection": "어떤 감각이 가장 집중하기 쉬웠나요?"
                }
            ]
        
        elif level == "L3":
            return [
                {
                    "step": 1,
                    "title": "전체 스캔",
                    "duration": 60,
                    "instruction": "1분간 전체를 훑어보기. 기록 금지.",
                    "focus": "overview",
                    "rule": "no_recording",
                    "purpose": "첫인상 형성"
                },
                {
                    "step": 2,
                    "title": "색상 그라데이션 추적",
                    "duration": 120,
                    "instruction": "2분간 색의 변화와 전이 관찰",
                    "focus": "color_gradient",
                    "task": "가장 밝은 곳에서 어두운 곳까지 시선 이동",
                    "record": "gradient_path"
                },
                {
                    "step": 3,
                    "title": "공간 관계 매핑",
                    "duration": 120,
                    "instruction": "2분간 요소들 사이의 거리와 정렬 관찰",
                    "focus": "spatial_relations",
                    "task": "머릿속에 격자 그리고 위치 파악",
                    "technique": "mental_grid"
                },
                {
                    "step": 4,
                    "title": "관찰 노트 작성",
                    "duration": 60,
                    "instruction": "1분간 관찰 내용 기록. 판단어 자동 체크.",
                    "writing": True,
                    "auto_filter": True
                }
            ]
        
        else:  # L5
            return [
                {
                    "step": 1,
                    "title": "한 점 응시 (주변시 관찰)",
                    "duration": 180,
                    "instruction": "3분간 중심점 응시하며 주변 변화 감지",
                    "focus": "peripheral_vision",
                    "technique": "soft_focus",
                    "challenge": "시선 이동 금지"
                },
                {
                    "step": 2,
                    "title": "무작위 시점 변경",
                    "duration": 120,
                    "instruction": "10초마다 시점 변경. 각 시점에서 새로운 발견",
                    "focus": "perspective_shift",
                    "intervals": 10,
                    "record": "new_discoveries"
                },
                {
                    "step": 3,
                    "title": "눈 감고 재구성",
                    "duration": 60,
                    "instruction": "눈 감고 본 것을 머릿속에 재구성",
                    "focus": "mental_reconstruction",
                    "test": "memory_vs_observation"
                },
                {
                    "step": 4,
                    "title": "판단 충동 인식",
                    "duration": 120,
                    "instruction": "관찰하며 떠오르는 판단들을 실시간 포착",
                    "focus": "metacognition",
                    "task": "판단 충동 카운팅",
                    "insight": "판단 없는 관찰의 어려움 체험"
                }
            ]
    
    def _filter_judgment_language(self, text: str) -> Dict:
        """판단 언어 필터링 및 피드백"""
        judgment_words = [
            "좋다", "나쁘다", "예쁘다", "못생겼다", "멋지다",
            "이상하다", "훌륭하다", "형편없다", "아름답다", "추하다",
            "완벽하다", "부족하다", "뛰어나다", "별로다"
        ]
        
        found_judgments = []
        for word in judgment_words:
            if word in text:
                found_judgments.append(word)
        
        if found_judgments:
            return {
                "has_judgment": True,
                "found_words": found_judgments,
                "suggestion": "다음 단어를 순수 관찰 언어로 바꿔보세요",
                "alternatives": self._suggest_alternatives(found_judgments)
            }
        
        return {
            "has_judgment": False,
            "message": "훌륭해요! 판단 없는 순수한 관찰입니다."
        }
    
    def _suggest_alternatives(self, judgment_words: List[str]) -> Dict:
        """판단 언어 대체 제안"""
        alternatives = {
            "예쁘다": "분홍색이다, 둥글다, 작다",
            "못생겼다": "비대칭이다, 각지다, 거칠다",
            "좋다": "밝다, 선명하다, 크다",
            "나쁘다": "어둡다, 흐릿하다, 작다"
        }
        
        suggestions = {}
        for word in judgment_words:
            if word in alternatives:
                suggestions[word] = alternatives[word]
        
        return suggestions
    
    def _track_progress(self, level: str, notes: str) -> Dict:
        """실습 진행 상황 추적"""
        return {
            "level": level,
            "observation_quality": self._assess_observation_quality(notes),
            "judgment_free_rate": self._calculate_judgment_free_rate(notes),
            "vocabulary_diversity": self._measure_vocabulary_diversity(notes),
            "next_challenge": self._suggest_next_challenge(level)
        }
    
    def _assess_observation_quality(self, notes: str) -> str:
        """관찰 품질 평가"""
        if not notes:
            return "not_assessed"
        
        word_count = len(notes.split())
        if word_count < 10:
            return "minimal"
        elif word_count < 30:
            return "basic"
        elif word_count < 50:
            return "detailed"
        else:
            return "comprehensive"
    
    def _calculate_judgment_free_rate(self, notes: str) -> float:
        """판단 없는 관찰 비율"""
        if not notes:
            return 0.0
        
        sentences = notes.split('.')
        judgment_free = 0
        for sentence in sentences:
            if self._is_pure_observation(sentence):
                judgment_free += 1
        
        return (judgment_free / len(sentences)) * 100 if sentences else 0
    
    def _is_pure_observation(self, text: str) -> bool:
        """순수 관찰 여부 체크"""
        judgment_words = ["좋", "나쁘", "예쁘", "못생", "멋", "이상", "훌륭", "형편"]
        return not any(word in text for word in judgment_words)
    
    def _measure_vocabulary_diversity(self, notes: str) -> int:
        """관찰 어휘 다양성 측정"""
        if not notes:
            return 0
        
        observation_words = set()
        descriptive_terms = ["색", "모양", "크기", "위치", "간격", "밝", "어두", "둥글", "네모", "길", "짧"]
        
        for term in descriptive_terms:
            if term in notes:
                observation_words.add(term)
        
        return len(observation_words)
    
    def _suggest_next_challenge(self, level: str) -> str:
        """다음 도전 과제 제안"""
        challenges = {
            "L1": "다음엔 45초씩 각 감각에 집중해보세요",
            "L3": "색상 그라데이션을 10단계로 나눠보세요",
            "L5": "5분간 한 점 응시에 도전해보세요"
        }
        return challenges.get(level, "더 긴 시간 관찰에 도전하세요")


class S1A1TrainingGamification(AbstractBaseNode):
    """S1-A1 판단 제거 트레이닝 게임화 - 시험이 아닌 훈련"""
    
    def __init__(self):
        io = NodeIO(
            inputs=[
                PortSchema(
                    name="training_data",
                    description="훈련 세션 데이터",
                    content_type="application/json"
                ),
                PortSchema(
                    name="user_profile",
                    description="사용자 프로필",
                    content_type="application/json"
                )
            ],
            outputs=[
                PortSchema(
                    name="growth_metrics",
                    description="성장 지표 (점수 아님)",
                    content_type="application/json"
                ),
                PortSchema(
                    name="training_feedback",
                    description="훈련 피드백",
                    content_type="application/json"
                ),
                PortSchema(
                    name="next_challenge",
                    description="다음 도전 과제",
                    content_type="application/json"
                )
            ]
        )
        super().__init__(
            node_id="S1-A1-TG",
            name="S1-A1 Training Gamification",
            version="2.0.0",
            io=io,
            description="판단 제거 훈련을 위한 성장 중심 게임화"
        )
    
    def _run(self, payloads: Dict[str, Any], ctx: ExecutionContext) -> Dict[str, Any]:
        training_data = payloads.get("training_data", {})
        user_profile = payloads.get("user_profile", {})
        
        # 성장 지표 계산 (점수가 아닌 진보도)
        growth_metrics = self._calculate_growth(training_data, user_profile)
        
        # 훈련 피드백 생성
        feedback = self._generate_training_feedback(growth_metrics)
        
        # 다음 도전 과제 제안
        next_challenge = self._suggest_next_challenge(growth_metrics, user_profile)
        
        return {
            "growth_metrics": growth_metrics,
            "training_feedback": feedback,
            "next_challenge": next_challenge
        }
    
    def _calculate_growth(self, data: Dict, profile: Dict) -> Dict:
        """성장 지표 계산 - IQ 테스트가 아닌 명상 수련처럼"""
        
        # 판단 감소율 (핵심 지표)
        judgment_reduction = self._track_judgment_reduction(data, profile)
        
        # 관찰 지속 시간 증가
        observation_duration = self._track_duration_increase(data, profile)
        
        # 순수 표현 비율 상승
        pure_expression_rate = self._track_pure_expression(data)
        
        # 메타인지 발달 (판단 충동 자각)
        metacognition = self._track_metacognition(data)
        
        return {
            "judgment_reduction": judgment_reduction,
            "observation_duration": observation_duration,
            "pure_expression_rate": pure_expression_rate,
            "metacognition_level": metacognition,
            "training_stage": self._determine_stage(judgment_reduction),
            "is_improving": self._check_improvement(data, profile)
        }
    
    def _track_judgment_reduction(self, data: Dict, profile: Dict) -> Dict:
        """판단 언어 감소 추적"""
        current_judgments = data.get("judgment_count", 0)
        previous_avg = profile.get("avg_judgments", 10)
        
        reduction_rate = max(0, (previous_avg - current_judgments) / previous_avg * 100)
        
        return {
            "current": current_judgments,
            "previous_avg": previous_avg,
            "reduction_percentage": reduction_rate,
            "trend": "improving" if reduction_rate > 0 else "stable",
            "milestone": self._get_judgment_milestone(current_judgments)
        }
    
    def _track_duration_increase(self, data: Dict, profile: Dict) -> Dict:
        """관찰 지속 시간 증가 추적"""
        current_duration = data.get("observation_duration", 0)
        previous_avg = profile.get("avg_duration", 60)
        
        return {
            "current_seconds": current_duration,
            "previous_avg": previous_avg,
            "improvement": current_duration - previous_avg,
            "sustained_focus": current_duration >= 180,  # 3분 이상
            "flow_state": current_duration >= 300  # 5분 이상
        }
    
    def _track_pure_expression(self, data: Dict) -> Dict:
        """순수 관찰 표현 추적"""
        total_expressions = data.get("total_expressions", 1)
        pure_expressions = data.get("pure_expressions", 0)
        
        rate = (pure_expressions / total_expressions * 100) if total_expressions > 0 else 0
        
        return {
            "rate": rate,
            "quality": self._assess_expression_quality(rate),
            "vocabulary_diversity": data.get("unique_sensory_words", 0)
        }
    
    def _track_metacognition(self, data: Dict) -> Dict:
        """메타인지 발달 추적 - 판단 충동 자각"""
        judgment_impulses = data.get("judgment_impulses_noticed", 0)
        self_corrections = data.get("self_corrections", 0)
        
        return {
            "awareness_level": self._calculate_awareness(judgment_impulses),
            "self_regulation": self_corrections,
            "insight_moments": data.get("insight_moments", 0),
            "stage": self._get_metacognition_stage(judgment_impulses, self_corrections)
        }
    
    def _generate_training_feedback(self, metrics: Dict) -> Dict:
        """훈련 피드백 생성 - 격려와 인사이트 중심"""
        
        judgment_feedback = self._get_judgment_feedback(metrics["judgment_reduction"])
        duration_feedback = self._get_duration_feedback(metrics["observation_duration"])
        expression_feedback = self._get_expression_feedback(metrics["pure_expression_rate"])
        
        # 전체적인 격려 메시지
        if metrics["is_improving"]:
            overall = "성장하고 있어요! 판단 없는 관찰이 자연스러워지고 있습니다."
        else:
            overall = "꾸준히 연습중이군요. 천천히, 판단 없이 보는 것이 핵심입니다."
        
        return {
            "overall_message": overall,
            "judgment_insight": judgment_feedback,
            "duration_insight": duration_feedback,
            "expression_insight": expression_feedback,
            "training_tip": self._get_training_tip(metrics),
            "encouragement": self._get_encouragement(metrics)
        }
    
    def _suggest_next_challenge(self, metrics: Dict, profile: Dict) -> Dict:
        """다음 도전 과제 - 점진적 난이도 상승"""
        
        stage = metrics["training_stage"]
        
        challenges = {
            "beginner": {
                "title": "1분 순수 관찰",
                "description": "1분 동안 단 하나의 판단어도 사용하지 않기",
                "focus": "judgment_elimination",
                "duration": 60,
                "support": "판단어가 떠오르면 '보류' 버튼을 눌러주세요"
            },
            "intermediate": {
                "title": "3분 지속 관찰",
                "description": "3분간 한 대상을 지속적으로 관찰하기",
                "focus": "sustained_attention",
                "duration": 180,
                "support": "시선을 옮기지 말고 깊이 들여다보세요"
            },
            "advanced": {
                "title": "판단 충동 카운팅",
                "description": "관찰하며 떠오르는 판단 충동을 실시간으로 인식하고 기록",
                "focus": "metacognition",
                "duration": 300,
                "support": "판단하고 싶은 순간마다 클릭하여 자각을 기록하세요"
            },
            "master": {
                "title": "무심(無心) 관찰",
                "description": "아무 의도 없이 10분간 순수하게 바라보기",
                "focus": "pure_awareness",
                "duration": 600,
                "support": "목표도, 평가도 없이 그저 있는 그대로 보세요"
            }
        }
        
        return challenges.get(stage, challenges["beginner"])
    
    # 헬퍼 메서드들
    def _determine_stage(self, judgment_reduction: Dict) -> str:
        """훈련 단계 결정"""
        reduction_rate = judgment_reduction.get("reduction_percentage", 0)
        current_judgments = judgment_reduction.get("current", 10)
        
        if current_judgments == 0 and reduction_rate >= 90:
            return "master"
        elif current_judgments <= 3 and reduction_rate >= 70:
            return "advanced"
        elif current_judgments <= 5 and reduction_rate >= 50:
            return "intermediate"
        else:
            return "beginner"
    
    def _get_judgment_milestone(self, count: int) -> str:
        """판단 감소 마일스톤"""
        if count == 0:
            return "🧘 완전한 비움"
        elif count <= 2:
            return "🌊 거의 순수함"
        elif count <= 5:
            return "🍃 점점 맑아짐"
        elif count <= 10:
            return "🌱 성장 중"
        else:
            return "🌰 시작 단계"
    
    def _assess_expression_quality(self, rate: float) -> str:
        """표현 품질 평가"""
        if rate >= 90:
            return "순수한 거울"
        elif rate >= 70:
            return "맑은 관찰"
        elif rate >= 50:
            return "성장하는 관찰"
        else:
            return "연습 중"
    
    def _calculate_awareness(self, impulses: int) -> str:
        """자각 수준 계산"""
        if impulses >= 10:
            return "높은 자각"
        elif impulses >= 5:
            return "중간 자각"
        elif impulses >= 1:
            return "초기 자각"
        else:
            return "무자각"
    
    def _get_metacognition_stage(self, impulses: int, corrections: int) -> str:
        """메타인지 단계"""
        if impulses >= 10 and corrections >= 8:
            return "자기 조절 마스터"
        elif impulses >= 5 and corrections >= 3:
            return "적극적 자각"
        elif impulses >= 1:
            return "자각 시작"
        else:
            return "전의식 상태"
    
    def _check_improvement(self, data: Dict, profile: Dict) -> bool:
        """개선 여부 체크"""
        current_judgments = data.get("judgment_count", 10)
        previous_judgments = profile.get("last_judgment_count", 10)
        return current_judgments < previous_judgments
    
    def _get_judgment_feedback(self, reduction: Dict) -> str:
        """판단 관련 피드백"""
        if reduction["current"] == 0:
            return "완벽해요! 판단 없는 순수한 관찰을 해내셨습니다."
        elif reduction["trend"] == "improving":
            return f"좋아요! 판단이 {reduction['reduction_percentage']:.0f}% 감소했어요."
        else:
            return "판단어가 떠오르는 것을 알아차리는 것부터가 시작입니다."
    
    def _get_duration_feedback(self, duration: Dict) -> str:
        """지속 시간 피드백"""
        if duration["flow_state"]:
            return "몰입의 경지! 5분 이상 순수한 관찰을 유지했어요."
        elif duration["sustained_focus"]:
            return "훌륭해요! 3분 이상 집중을 유지했습니다."
        else:
            return "천천히 관찰 시간을 늘려가 보세요."
    
    def _get_expression_feedback(self, expression: Dict) -> str:
        """표현 관련 피드백"""
        if expression["rate"] >= 80:
            return f"관찰 표현의 {expression['rate']:.0f}%가 순수해요!"
        else:
            return f"감각 어휘를 {expression['vocabulary_diversity']}개 사용했네요. 더 다양하게 표현해보세요."
    
    def _get_training_tip(self, metrics: Dict) -> str:
        """훈련 팁"""
        stage = metrics["training_stage"]
        tips = {
            "beginner": "💡 '예쁘다' 대신 '빨간색이다'처럼 감각만 표현해보세요",
            "intermediate": "💡 눈을 가늘게 뜨면 형태보다 색상에 집중할 수 있어요",
            "advanced": "💡 판단 충동이 일어나는 순간을 포착해보세요",
            "master": "💡 관찰자도 관찰 대상도 사라지는 순간을 경험해보세요"
        }
        return tips.get(stage, tips["beginner"])
    
    def _get_encouragement(self, metrics: Dict) -> str:
        """격려 메시지"""
        if metrics["is_improving"]:
            return "🌱 매일 조금씩 성장하고 있어요!"
        else:
            return "🌊 파도처럼 오르내림이 있어도 괜찮아요."
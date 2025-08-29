"""
S1-A1 수업 방식: Observation Meditation Method
순수한 관찰 능력 훈련에 특화된 단일 수업 방식

확정된 구조:
- 3개 핵심 노드 (Language Guardrail, Observation Guide, Echo Reflection)
- 4단계 구조 (준비→관찰→기록→성찰)
- 3개 개인화 파라미터 (가드레일 엄격도, 시간 압박, 피드백 타이밍)
"""
from typing import Dict, Any, List, Optional, Literal
from enum import Enum
from dataclasses import dataclass
import re
from nodes.base.base_node import AbstractBaseNode
from nodes.base.interfaces import NodeIO, PortSchema, ExecutionContext


class GuardrailStrictness(Enum):
    HIGH = "high"      # 즉시 교정, 모든 판단어 차단
    MEDIUM = "medium"  # 부드러운 교정, 주요 판단어만
    LOW = "low"        # 최소 개입, 심각한 경우만


class FeedbackMode(Enum):
    REALTIME = "realtime"  # 즉시 피드백
    BATCHED = "batched"    # 단계 끝 누적 피드백


@dataclass
class PersonalizationParams:
    """개인화 파라미터 (설문 기반)"""
    guardrail_strictness: GuardrailStrictness = GuardrailStrictness.MEDIUM
    timing_pressure: bool = False  # True면 타이머 표시
    feedback_mode: FeedbackMode = FeedbackMode.REALTIME


@dataclass
class ObservationPhase:
    """수업 단계 정의"""
    name: str
    duration_minutes: float
    objective: str
    prompts: List[str]
    nodes: List[str]


class LanguageGuardrailNode(AbstractBaseNode):
    """판단어 필터 및 교정 노드"""
    
    def __init__(self):
        io = NodeIO(
            inputs=[
                PortSchema(
                    name="user_text",
                    description="사용자 입력 텍스트",
                    content_type="text/plain"
                ),
                PortSchema(
                    name="strictness",
                    description="가드레일 엄격도",
                    content_type="application/json"
                )
            ],
            outputs=[
                PortSchema(
                    name="filtered_text",
                    description="교정된 텍스트",
                    content_type="text/plain"
                ),
                PortSchema(
                    name="corrections",
                    description="교정 제안 목록",
                    content_type="application/json"
                )
            ]
        )
        
        super().__init__(
            node_id="S1-A1-LG",
            name="Language Guardrail",
            version="1.0.0",
            io=io,
            description="판단어 감지 및 감각어로 교정"
        )
        
        # 판단어 사전
        self.judgment_words = {
            "평가": ["좋다", "나쁘다", "예쁘다", "못생겼다", "훌륭하다", "형편없다"],
            "해석": ["버튼이다", "메뉴다", "위한", "때문에", "목적은"],
            "분석": ["효율적", "비효율적", "논리적", "체계적", "복잡한", "단순한"]
        }
        
        # 감각어 사전 (권장)
        self.sensory_words = {
            "색상": ["빨간", "파란", "초록", "노란", "검은", "흰", "회색", "밝은", "어두운"],
            "형태": ["둥근", "네모", "삼각", "직선", "곡선", "길쭉한", "납작한"],
            "위치": ["위", "아래", "왼쪽", "오른쪽", "가운데", "모서리", "상단", "하단"],
            "크기": ["큰", "작은", "넓은", "좁은", "긴", "짧은"],
            "질감": ["매끄러운", "거친", "반짝이는", "무광"]
        }
    
    def _run(self, payloads: Dict[str, Any], ctx: ExecutionContext) -> Dict[str, Any]:
        text = payloads.get("user_text", "")
        strictness = GuardrailStrictness(payloads.get("strictness", "medium"))
        
        corrections = []
        filtered_text = text
        
        # 판단어 감지 및 교정
        for category, words in self.judgment_words.items():
            for word in words:
                if word in text:
                    if strictness == GuardrailStrictness.HIGH:
                        # 즉시 교정
                        suggestion = self._suggest_alternative(word, category)
                        filtered_text = filtered_text.replace(word, suggestion)
                        corrections.append({
                            "original": word,
                            "suggestion": suggestion,
                            "category": category,
                            "severity": "high"
                        })
                    elif strictness == GuardrailStrictness.MEDIUM and category in ["평가", "해석"]:
                        # 부드러운 제안
                        suggestion = self._suggest_alternative(word, category)
                        corrections.append({
                            "original": word,
                            "suggestion": suggestion,
                            "category": category,
                            "severity": "medium"
                        })
        
        return {
            "filtered_text": filtered_text,
            "corrections": corrections,
            "judgment_count": len(corrections),
            "sensory_coverage": self._calculate_sensory_coverage(text)
        }
    
    def _suggest_alternative(self, word: str, category: str) -> str:
        """판단어에 대한 감각어 대안 제안"""
        alternatives = {
            "좋다": "밝은",
            "나쁘다": "어두운",
            "예쁘다": "둥근",
            "못생겼다": "각진",
            "버튼이다": "사각형 요소",
            "메뉴다": "수평 배치된 항목들",
            "위한": "옆에 있는",
            "효율적": "간격이 일정한",
            "복잡한": "요소가 많은"
        }
        return alternatives.get(word, "[관찰만]")
    
    def _calculate_sensory_coverage(self, text: str) -> Dict[str, int]:
        """감각어 사용 범위 계산"""
        coverage = {}
        for category, words in self.sensory_words.items():
            count = sum(1 for word in words if word in text)
            coverage[category] = count
        return coverage


class ObservationGuideNode(AbstractBaseNode):
    """통합 관찰 가이드 노드 (Color/Shape/Spatial 통합)"""
    
    def __init__(self):
        io = NodeIO(
            inputs=[
                PortSchema(
                    name="scene",
                    description="관찰 대상 화면",
                    content_type="application/json"
                ),
                PortSchema(
                    name="user_level",
                    description="사용자 레벨 (L1/L3/L5)",
                    content_type="text/plain"
                ),
                PortSchema(
                    name="focus_type",
                    description="집중 유형 (color/shape/spatial/all)",
                    content_type="text/plain"
                )
            ],
            outputs=[
                PortSchema(
                    name="observation_hints",
                    description="관찰 힌트 및 가이드",
                    content_type="application/json"
                ),
                PortSchema(
                    name="overlay_config",
                    description="UI 오버레이 설정",
                    content_type="application/json"
                )
            ]
        )
        
        super().__init__(
            node_id="S1-A1-OG",
            name="Observation Guide",
            version="1.0.0",
            io=io,
            description="레벨별 관찰 힌트 제공 (통합)"
        )
    
    def _run(self, payloads: Dict[str, Any], ctx: ExecutionContext) -> Dict[str, Any]:
        scene = payloads.get("scene", {})
        level = payloads.get("user_level", "L1")
        focus = payloads.get("focus_type", "all")
        
        hints = []
        overlay = {}
        
        # 레벨별 힌트 생성
        if level == "L1":
            if focus in ["color", "all"]:
                hints.append("화면에서 가장 밝은 색은 무엇인가요?")
                overlay["color_palette"] = True
            if focus in ["shape", "all"]:
                hints.append("둥근 것과 네모난 것을 찾아보세요")
                overlay["shape_hints"] = True
            if focus in ["spatial", "all"]:
                hints.append("위쪽에 무엇이 있나요?")
                overlay["grid_3x3"] = True
                
        elif level == "L3":
            if focus in ["color", "all"]:
                hints.append("색의 대비가 가장 큰 곳은 어디인가요?")
                overlay["contrast_map"] = True
            if focus in ["shape", "all"]:
                hints.append("반복되는 형태의 패턴을 찾아보세요")
                overlay["pattern_detection"] = True
            if focus in ["spatial", "all"]:
                hints.append("요소들 사이의 간격이 일정한가요?")
                overlay["spacing_guide"] = True
                
        elif level == "L5":
            if focus in ["color", "all"]:
                hints.append("색이 없는 곳의 의미는?")
                overlay["negative_space"] = True
            if focus in ["shape", "all"]:
                hints.append("보이지 않는 축을 찾아보세요")
                overlay["invisible_grid"] = True
            if focus in ["spatial", "all"]:
                hints.append("시선이 자연스럽게 향하는 경로는?")
                overlay["gaze_path"] = True
        
        return {
            "observation_hints": hints,
            "overlay_config": overlay,
            "level": level,
            "focus_areas": self._generate_focus_areas(focus)
        }
    
    def _generate_focus_areas(self, focus_type: str) -> List[Dict[str, Any]]:
        """집중 영역 생성"""
        areas = []
        if focus_type == "color":
            areas.append({"type": "color", "weight": 1.0})
        elif focus_type == "shape":
            areas.append({"type": "shape", "weight": 1.0})
        elif focus_type == "spatial":
            areas.append({"type": "spatial", "weight": 1.0})
        else:  # all
            areas = [
                {"type": "color", "weight": 0.33},
                {"type": "shape", "weight": 0.33},
                {"type": "spatial", "weight": 0.34}
            ]
        return areas


class EchoReflectionNode(AbstractBaseNode):
    """좋은 관찰 문장 에코 및 성찰 노드"""
    
    def __init__(self):
        io = NodeIO(
            inputs=[
                PortSchema(
                    name="observations",
                    description="사용자의 관찰 문장들",
                    content_type="application/json"
                ),
                PortSchema(
                    name="phase",
                    description="현재 단계 (observation/reflection)",
                    content_type="text/plain"
                )
            ],
            outputs=[
                PortSchema(
                    name="echo_samples",
                    description="강조할 좋은 관찰 샘플",
                    content_type="application/json"
                ),
                PortSchema(
                    name="reflection_prompts",
                    description="성찰 유도 프롬프트",
                    content_type="application/json"
                )
            ]
        )
        
        super().__init__(
            node_id="S1-A1-ER",
            name="Echo Reflection",
            version="1.0.0",
            io=io,
            description="좋은 관찰 강화 및 성찰 유도"
        )
    
    def _run(self, payloads: Dict[str, Any], ctx: ExecutionContext) -> Dict[str, Any]:
        observations = payloads.get("observations", [])
        phase = payloads.get("phase", "observation")
        
        echo_samples = []
        reflection_prompts = []
        
        if phase == "observation":
            # 좋은 관찰 문장 선별
            for obs in observations:
                if self._is_pure_observation(obs):
                    echo_samples.append({
                        "text": obs,
                        "highlight": self._extract_sensory_words(obs),
                        "feedback": "훌륭한 관찰입니다!"
                    })
        
        elif phase == "reflection":
            # 성찰 프롬프트 생성
            reflection_prompts = [
                "처음엔 못 봤던 것이 무엇이었나요?",
                "판단 없이 본다는 것이 어떤 느낌이었나요?",
                "가장 어려웠던 부분은 무엇이었나요?",
                "다음번엔 무엇을 더 관찰하고 싶나요?"
            ]
            
            # 개인화된 성찰 추가
            if len(observations) > 10:
                reflection_prompts.append("많은 것을 관찰하셨네요. 그 중 가장 선명한 것은?")
            if len(observations) < 5:
                reflection_prompts.append("천천히 더 자세히 볼 수 있는 부분이 있을까요?")
        
        return {
            "echo_samples": echo_samples[:3],  # 상위 3개만
            "reflection_prompts": reflection_prompts,
            "observation_quality": self._assess_quality(observations),
            "next_focus": self._suggest_next_focus(observations)
        }
    
    def _is_pure_observation(self, text: str) -> bool:
        """순수 관찰 문장 판별"""
        # 감각어 포함 & 판단어 미포함
        sensory_keywords = ["색", "모양", "위치", "크기", "간격", "밝", "어두", "둥근", "네모"]
        judgment_keywords = ["좋", "나쁘", "예쁘", "효율", "복잡", "단순", "때문", "위한"]
        
        has_sensory = any(keyword in text for keyword in sensory_keywords)
        has_judgment = any(keyword in text for keyword in judgment_keywords)
        
        return has_sensory and not has_judgment
    
    def _extract_sensory_words(self, text: str) -> List[str]:
        """감각어 추출"""
        sensory_patterns = [
            r'(빨간|파란|초록|노란|검은|흰|회색)',
            r'(둥근|네모|삼각|직선|곡선)',
            r'(위|아래|왼쪽|오른쪽|가운데)',
            r'(큰|작은|넓은|좁은|긴|짧은)'
        ]
        
        found_words = []
        for pattern in sensory_patterns:
            matches = re.findall(pattern, text)
            found_words.extend(matches)
        
        return found_words
    
    def _assess_quality(self, observations: List[str]) -> Dict[str, Any]:
        """관찰 품질 평가"""
        pure_count = sum(1 for obs in observations if self._is_pure_observation(obs))
        diversity = len(set(' '.join(observations).split()))  # 어휘 다양성
        
        return {
            "total_observations": len(observations),
            "pure_observations": pure_count,
            "purity_ratio": pure_count / max(len(observations), 1),
            "vocabulary_diversity": diversity,
            "quality_score": (pure_count / max(len(observations), 1)) * min(diversity / 50, 1.0)
        }
    
    def _suggest_next_focus(self, observations: List[str]) -> str:
        """다음 집중 영역 제안"""
        text = ' '.join(observations)
        
        # 각 영역별 언급 빈도 계산
        color_count = len(re.findall(r'색|빨간|파란|초록|밝|어두', text))
        shape_count = len(re.findall(r'모양|둥근|네모|삼각|직선|곡선', text))
        spatial_count = len(re.findall(r'위치|위|아래|왼쪽|오른쪽|간격', text))
        
        # 가장 적게 관찰된 영역 제안
        counts = {"color": color_count, "shape": shape_count, "spatial": spatial_count}
        min_area = min(counts, key=counts.get)
        
        return min_area


class ObservationMeditationMethod(AbstractBaseNode):
    """S1-A1 통합 수업 방식"""
    
    def __init__(self):
        io = NodeIO(
            inputs=[
                PortSchema(
                    name="user_profile",
                    description="사용자 설문 결과",
                    content_type="application/json"
                ),
                PortSchema(
                    name="scene",
                    description="관찰 대상",
                    content_type="application/json"
                ),
                PortSchema(
                    name="user_level",
                    description="사용자 레벨",
                    content_type="text/plain"
                )
            ],
            outputs=[
                PortSchema(
                    name="session_plan",
                    description="개인화된 세션 계획",
                    content_type="application/json"
                ),
                PortSchema(
                    name="phase_configs",
                    description="단계별 설정",
                    content_type="application/json"
                ),
                PortSchema(
                    name="metrics",
                    description="측정 지표",
                    content_type="application/json"
                )
            ]
        )
        
        super().__init__(
            node_id="S1-A1-OMM",
            name="Observation Meditation Method",
            version="1.0.0",
            io=io,
            description="순수 관찰 훈련 통합 수업"
        )
        
        # 4단계 구조 정의
        self.phases = [
            ObservationPhase(
                name="준비",
                duration_minutes=1.0,
                objective="판단 내려놓기",
                prompts=["지금은 '보는 것'만 합니다", "판단과 해석은 잠시 쉬어요"],
                nodes=[]
            ),
            ObservationPhase(
                name="관찰",
                duration_minutes=6.0,
                objective="있는 그대로 보기",
                prompts=["무엇이 보이나요?", "색과 형태만 말해주세요", "위치와 간격을 관찰해보세요"],
                nodes=["ObservationGuide", "LanguageGuardrail"]
            ),
            ObservationPhase(
                name="기록",
                duration_minutes=3.0,
                objective="본 것을 언어로",
                prompts=["관찰한 것을 구체적으로 적어주세요", "예: '파란색 네모(우상단)'"],
                nodes=["LanguageGuardrail", "EchoReflection"]
            ),
            ObservationPhase(
                name="성찰",
                duration_minutes=2.0,
                objective="관찰 경험 돌아보기",
                prompts=["처음엔 못 봤던 것은?", "판단 없이 본 느낌은?"],
                nodes=["EchoReflection"]
            )
        ]
        
        # 서브 노드 인스턴스
        self.guardrail = LanguageGuardrailNode()
        self.guide = ObservationGuideNode()
        self.echo = EchoReflectionNode()
    
    def _run(self, payloads: Dict[str, Any], ctx: ExecutionContext) -> Dict[str, Any]:
        user_profile = payloads.get("user_profile", {})
        scene = payloads.get("scene", {})
        user_level = payloads.get("user_level", "L1")
        
        # 개인화 파라미터 추출
        params = self._extract_personalization(user_profile)
        
        # 세션 계획 생성
        session_plan = self._create_session_plan(params, user_level)
        
        # 단계별 설정
        phase_configs = self._configure_phases(params, user_level)
        
        # KPI 정의
        metrics = {
            "primary": [
                {"name": "판단어 비율", "target": "< 10%", "measure": "judgment_word_ratio"},
                {"name": "감각어 커버리지", "target": "> 60%", "measure": "sensory_coverage"},
                {"name": "관찰 밀도", "target": "> 2/min", "measure": "observation_density"}
            ],
            "secondary": [
                {"name": "순수 관찰 비율", "measure": "pure_observation_ratio"},
                {"name": "어휘 다양성", "measure": "vocabulary_diversity"},
                {"name": "완료율", "measure": "completion_rate"}
            ]
        }
        
        return {
            "session_plan": session_plan,
            "phase_configs": phase_configs,
            "metrics": metrics,
            "personalization": params.__dict__,
            "estimated_duration": sum(p.duration_minutes for p in self.phases)
        }
    
    def _extract_personalization(self, profile: Dict[str, Any]) -> PersonalizationParams:
        """설문에서 개인화 파라미터 추출"""
        params = PersonalizationParams()
        
        # 가드레일 엄격도
        if profile.get("correction_preference", 3) >= 4:
            params.guardrail_strictness = GuardrailStrictness.HIGH
        elif profile.get("correction_preference", 3) <= 2:
            params.guardrail_strictness = GuardrailStrictness.LOW
        
        # 시간 압박
        params.timing_pressure = profile.get("time_pressure_preference", 3) >= 4
        
        # 피드백 모드
        if profile.get("immediate_feedback", 3) >= 4:
            params.feedback_mode = FeedbackMode.REALTIME
        else:
            params.feedback_mode = FeedbackMode.BATCHED
        
        return params
    
    def _create_session_plan(self, params: PersonalizationParams, level: str) -> Dict[str, Any]:
        """개인화된 세션 계획"""
        plan = {
            "total_duration": 12,  # 기본 12분
            "phases": []
        }
        
        for phase in self.phases:
            phase_plan = {
                "name": phase.name,
                "duration": phase.duration_minutes,
                "objective": phase.objective,
                "timer_visible": params.timing_pressure,
                "prompts": phase.prompts
            }
            
            # 시간 압박 선호도에 따라 조정
            if not params.timing_pressure and phase.name == "관찰":
                phase_plan["duration"] *= 1.2  # 20% 더 여유
            
            plan["phases"].append(phase_plan)
        
        return plan
    
    def _configure_phases(self, params: PersonalizationParams, level: str) -> List[Dict[str, Any]]:
        """단계별 노드 설정"""
        configs = []
        
        for phase in self.phases:
            config = {
                "phase": phase.name,
                "nodes": []
            }
            
            # 노드별 설정
            if "LanguageGuardrail" in phase.nodes:
                config["nodes"].append({
                    "name": "LanguageGuardrail",
                    "params": {
                        "strictness": params.guardrail_strictness.value,
                        "mode": params.feedback_mode.value
                    }
                })
            
            if "ObservationGuide" in phase.nodes:
                focus = "all"
                if level == "L1":
                    focus = "color"  # 초급은 색상부터
                elif level == "L3":
                    focus = "spatial"  # 중급은 공간관계
                
                config["nodes"].append({
                    "name": "ObservationGuide",
                    "params": {
                        "level": level,
                        "focus_type": focus
                    }
                })
            
            if "EchoReflection" in phase.nodes:
                config["nodes"].append({
                    "name": "EchoReflection",
                    "params": {
                        "phase": "reflection" if phase.name == "성찰" else "observation"
                    }
                })
            
            configs.append(config)
        
        return configs
    
    def method_profile(self) -> Dict[str, Any]:
        """TeachingMethodNode 인터페이스 구현"""
        return {
            "method_name": "Observation Meditation",
            "method_id": "S1-A1-OMM",
            "phases": len(self.phases),
            "total_duration": sum(p.duration_minutes for p in self.phases),
            "personalization_params": ["guardrail_strictness", "timing_pressure", "feedback_mode"],
            "supported_levels": ["L1", "L3", "L5"],
            "core_nodes": ["LanguageGuardrail", "ObservationGuide", "EchoReflection"],
            "metrics": ["judgment_word_ratio", "sensory_coverage", "observation_density"]
        }


# 테스트를 위한 실행 예시
if __name__ == "__main__":
    # 통합 수업 방식 인스턴스
    method = ObservationMeditationMethod()
    
    # 샘플 사용자 프로필 (설문 결과)
    sample_profile = {
        "correction_preference": 4,  # 엄격한 교정 선호
        "time_pressure_preference": 2,  # 시간 압박 싫어함
        "immediate_feedback": 5  # 즉시 피드백 선호
    }
    
    # 실행
    result = method._run({
        "user_profile": sample_profile,
        "scene": {"type": "chatgpt_interface"},
        "user_level": "L1"
    }, ExecutionContext(session_id="test-session"))
    
    print("=== S1-A1 수업 계획 ===")
    print(f"개인화: {result['personalization']}")
    print(f"총 소요시간: {result['estimated_duration']}분")
    print(f"KPI: {result['metrics']['primary']}")
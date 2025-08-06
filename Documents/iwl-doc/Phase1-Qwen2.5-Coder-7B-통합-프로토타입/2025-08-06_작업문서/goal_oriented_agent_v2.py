#!/usr/bin/env python3
"""
[엔진-010] 목표 지향 에이전트 아키텍처 PoC - v2.0 (리팩터링 버전)
스크립트 없이 주어진 목표를 달성하기 위해 사용자와 자율적으로 상호작용하는 에이전트

작성일: 2025년 8월 6일
작성자: Claude Code (엔진 본부)
리팩터링: 2025년 8월 6일 - 보안, 안정성, 성능 개선
"""

import json
import time
import re
import os
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple, Union
from dataclasses import dataclass, field
from enum import Enum
import uuid

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GoalStatus(Enum):
    """Goal 달성 상태"""
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    BLOCKED = "blocked"

class ActionType(Enum):
    """Agent 행동 유형"""
    ASK_QUESTION = "ask_question"
    PROVIDE_INFO = "provide_info"
    SUGGEST_ACTION = "suggest_action"
    VALIDATE_PROGRESS = "validate_progress"
    CLARIFY_REQUIREMENT = "clarify_requirement"
    BREAK_DOWN_GOAL = "break_down_goal"

class ThinkingStage(Enum):
    """IWL 8단계 사고 확장 모델"""
    STAGE_1_AWARENESS = "awareness"          # 인식: 현재 상황 파악
    STAGE_2_QUESTIONING = "questioning"      # 질문: 핵심 문제 발견
    STAGE_3_EXPLORATION = "exploration"      # 탐색: 다양한 관점 수집
    STAGE_4_CONNECTION = "connection"        # 연결: 아이디어 간 관계 발견
    STAGE_5_SYNTHESIS = "synthesis"          # 종합: 통합된 이해 구축
    STAGE_6_EVALUATION = "evaluation"        # 평가: 비판적 사고 적용
    STAGE_7_APPLICATION = "application"      # 적용: 실행 가능한 계획 수립
    STAGE_8_REFLECTION = "reflection"        # 성찰: 학습 내용 정리

@dataclass
class Goal:
    """목표 정의 클래스"""
    id: str
    description: str
    success_criteria: List[str]
    priority: int = 1
    status: GoalStatus = GoalStatus.NOT_STARTED
    progress: float = 0.0
    sub_goals: List['Goal'] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class AgentAction:
    """에이전트 행동 정의"""
    action_type: ActionType
    content: str
    reasoning: str
    expected_outcome: str
    thinking_stage: ThinkingStage
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class UserResponse:
    """사용자 응답 정의"""
    content: str
    timestamp: str
    interpreted_intent: Optional[str] = None
    extracted_info: Dict[str, Any] = field(default_factory=dict)

class SecurityUtils:
    """보안 유틸리티 클래스"""
    
    @staticmethod
    def sanitize_input(user_input: str) -> str:
        """사용자 입력 정제"""
        if not isinstance(user_input, str):
            return ""
        
        # 길이 제한
        if len(user_input) > 2000:
            user_input = user_input[:2000]
        
        # 잠재적 위험 문자 제거
        dangerous_patterns = [
            r'<script[^>]*>.*?</script>',
            r'javascript:',
            r'on\w+\s*=',
            r'eval\s*\(',
            r'exec\s*\(',
            r'system\s*\(',
            r'import\s+os',
            r'__import__',
        ]
        
        for pattern in dangerous_patterns:
            user_input = re.sub(pattern, '', user_input, flags=re.IGNORECASE)
        
        # 기본 정리
        user_input = user_input.strip()
        return user_input
    
    @staticmethod
    def validate_file_path(filename: str) -> Path:
        """안전한 파일 경로 검증"""
        if not isinstance(filename, str):
            raise ValueError("파일명은 문자열이어야 합니다")
        
        # 위험한 문자 제거
        safe_filename = re.sub(r'[<>:"/\\|?*]', '', filename)
        safe_filename = re.sub(r'\.\.', '', safe_filename)  # Path Traversal 방지
        
        if not safe_filename:
            safe_filename = f"default_{uuid.uuid4().hex[:8]}.json"
        
        if not safe_filename.endswith('.json'):
            safe_filename += '.json'
        
        # 현재 작업 디렉토리 내에서만 파일 생성
        safe_path = Path.cwd() / safe_filename
        return safe_path

class GoalOrientedAgent:
    """
    목표 지향 에이전트 v2.0
    
    주요 개선사항:
    - 보안 강화: 입력 검증, 파일 경로 보안
    - 안정성 향상: 전역 예외 처리, 메모리 관리
    - IWL 8단계 사고 모델 통합
    - 성능 최적화
    """
    
    MAX_CONVERSATION_HISTORY = 50  # 메모리 누수 방지
    
    def __init__(self, agent_id: str = None):
        self.agent_id = agent_id or str(uuid.uuid4())
        self.current_goal: Optional[Goal] = None
        self.conversation_history: List[Dict] = []
        self.user_context: Dict[str, Any] = {}
        self.goal_stack: List[Goal] = []
        
        # 에이전트 인지 능력
        try:
            self.progress_evaluator = ProgressEvaluator()
            self.action_planner = ActionPlanner()
            self.context_analyzer = ContextAnalyzer()
            self.thinking_processor = ThinkingProcessor()
        except Exception as e:
            logger.error(f"에이전트 초기화 실패: {e}")
            raise
        
    def set_goal(self, goal: Goal) -> bool:
        """새로운 목표 설정"""
        try:
            if not isinstance(goal, Goal):
                raise ValueError("Goal 객체가 필요합니다")
            
            self.current_goal = goal
            self.current_goal.status = GoalStatus.IN_PROGRESS
            self._log_event("goal_set", {"goal_id": goal.id, "description": goal.description})
            
            # 목표 분해 시도
            if self._should_break_down_goal(goal):
                self._break_down_goal(goal)
            
            return True
        except Exception as e:
            logger.error(f"목표 설정 실패: {e}")
            return False
    
    def process_user_input(self, user_input: str) -> Optional[AgentAction]:
        """
        사용자 입력을 처리하고 다음 행동 결정
        
        Args:
            user_input: 사용자 입력
            
        Returns:
            AgentAction: 에이전트가 수행할 다음 행동
        """
        try:
            # 입력 정제
            sanitized_input = SecurityUtils.sanitize_input(user_input)
            if not sanitized_input:
                return AgentAction(
                    action_type=ActionType.CLARIFY_REQUIREMENT,
                    content="입력을 이해할 수 없습니다. 다시 설명해 주세요.",
                    reasoning="빈 입력 또는 위험한 입력 감지",
                    expected_outcome="사용자가 유효한 입력 제공",
                    thinking_stage=ThinkingStage.STAGE_1_AWARENESS
                )
            
            if not self.current_goal:
                return AgentAction(
                    action_type=ActionType.CLARIFY_REQUIREMENT,
                    content="안녕하세요! 먼저 어떤 목표를 달성하고 싶으신지 알려주세요.",
                    reasoning="목표가 설정되지 않음",
                    expected_outcome="사용자가 목표를 명확히 설명",
                    thinking_stage=ThinkingStage.STAGE_2_QUESTIONING
                )
            
            # 사용자 입력 분석
            user_response = UserResponse(
                content=sanitized_input,
                timestamp=datetime.now().isoformat()
            )
            
            # 컨텍스트 분석
            self.context_analyzer.analyze_user_input(user_response, self.user_context)
            
            # 8단계 사고 모델 적용
            thinking_result = self.thinking_processor.process_stage(
                self.current_goal, user_response, self.conversation_history
            )
            
            # 진행 상황 평가
            progress_status = self.progress_evaluator.evaluate_progress(
                self.current_goal, 
                user_response, 
                self.conversation_history
            )
            
            # 다음 행동 계획
            next_action = self.action_planner.plan_next_action(
                goal=self.current_goal,
                user_response=user_response,
                progress_status=progress_status,
                context=self.user_context,
                thinking_stage=thinking_result.current_stage
            )
            
            # 대화 기록 업데이트 (메모리 관리 포함)
            self._update_conversation_history(user_response, next_action)
            
            return next_action
            
        except Exception as e:
            logger.error(f"사용자 입력 처리 오류: {e}")
            return AgentAction(
                action_type=ActionType.PROVIDE_INFO,
                content="처리 중 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.",
                reasoning=f"시스템 오류: {str(e)}",
                expected_outcome="시스템 안정화 후 재시도",
                thinking_stage=ThinkingStage.STAGE_1_AWARENESS
            )
    
    def _should_break_down_goal(self, goal: Goal) -> bool:
        """목표를 하위 목표로 분해해야 하는지 판단"""
        try:
            complexity_indicators = [
                len(goal.success_criteria) > 3,
                len(goal.description.split()) > 15,
                '단계' in goal.description or '과정' in goal.description
            ]
            
            return sum(complexity_indicators) >= 2
        except Exception as e:
            logger.error(f"목표 분해 판단 오류: {e}")
            return False
    
    def _break_down_goal(self, goal: Goal) -> None:
        """목표를 하위 목표로 분해"""
        try:
            # 성공 기준 기반으로 하위 목표 생성
            for i, criteria in enumerate(goal.success_criteria):
                sub_goal = Goal(
                    id=f"{goal.id}_sub_{i+1}",
                    description=f"{criteria}를 달성하기",
                    success_criteria=[criteria],
                    priority=i+1
                )
                goal.sub_goals.append(sub_goal)
                
            self._log_event("goal_decomposed", {
                "parent_goal": goal.id,
                "sub_goals_count": len(goal.sub_goals)
            })
        except Exception as e:
            logger.error(f"목표 분해 오류: {e}")
    
    def _update_conversation_history(self, user_response: UserResponse, agent_action: AgentAction) -> None:
        """대화 기록 업데이트 (메모리 관리 포함)"""
        try:
            action_dict = {
                "action_type": agent_action.action_type.value,
                "content": agent_action.content,
                "reasoning": agent_action.reasoning,
                "expected_outcome": agent_action.expected_outcome,
                "thinking_stage": agent_action.thinking_stage.value,
                "timestamp": agent_action.timestamp
            }
            
            self.conversation_history.append({
                "timestamp": datetime.now().isoformat(),
                "user_input": user_response.content,
                "agent_action": action_dict,
                "goal_progress": self.current_goal.progress if self.current_goal else 0.0
            })
            
            # 메모리 관리: FIFO 방식으로 오래된 대화 제거
            if len(self.conversation_history) > self.MAX_CONVERSATION_HISTORY:
                removed_count = len(self.conversation_history) - self.MAX_CONVERSATION_HISTORY
                self.conversation_history = self.conversation_history[removed_count:]
                logger.info(f"메모리 관리: {removed_count}개의 오래된 대화 기록 제거")
                
        except Exception as e:
            logger.error(f"대화 기록 업데이트 오류: {e}")
    
    def _log_event(self, event_type: str, data: Dict) -> None:
        """이벤트 로깅"""
        try:
            logger.info(f"[{datetime.now().strftime('%H:%M:%S')}] {event_type}: {data}")
        except Exception as e:
            logger.error(f"로깅 오류: {e}")
    
    def get_current_status(self) -> Dict:
        """현재 상태 반환"""
        try:
            goal_dict = None
            if self.current_goal:
                goal_dict = {
                    "id": self.current_goal.id,
                    "description": self.current_goal.description,
                    "success_criteria": self.current_goal.success_criteria,
                    "priority": self.current_goal.priority,
                    "status": self.current_goal.status.value,
                    "progress": self.current_goal.progress,
                    "sub_goals": [{"id": sg.id, "description": sg.description} for sg in self.current_goal.sub_goals],
                    "metadata": self.current_goal.metadata
                }
            
            return {
                "agent_id": self.agent_id,
                "current_goal": goal_dict,
                "conversation_turns": len(self.conversation_history),
                "user_context": self.user_context
            }
        except Exception as e:
            logger.error(f"상태 조회 오류: {e}")
            return {
                "agent_id": self.agent_id,
                "error": str(e),
                "conversation_turns": 0,
                "user_context": {}
            }
    
    def save_session(self, filename: str = None) -> bool:
        """세션 데이터를 안전하게 저장"""
        try:
            if filename is None:
                filename = f"goal_agent_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            # 안전한 파일 경로 검증
            safe_path = SecurityUtils.validate_file_path(filename)
            
            # 디렉토리 생성 (필요한 경우)
            safe_path.parent.mkdir(parents=True, exist_ok=True)
            
            session_data = {
                "session_saved_at": datetime.now().isoformat(),
                "final_status": self.get_current_status(),
                "conversation_history": self.conversation_history
            }
            
            with open(safe_path, 'w', encoding='utf-8') as f:
                json.dump(session_data, f, ensure_ascii=False, indent=2)
            
            logger.info(f"세션이 안전하게 저장되었습니다: {safe_path}")
            return True
            
        except Exception as e:
            logger.error(f"세션 저장 실패: {e}")
            return False

@dataclass 
class ThinkingResult:
    """8단계 사고 모델 처리 결과"""
    current_stage: ThinkingStage
    insights: List[str]
    next_questions: List[str]
    confidence_level: float

class ThinkingProcessor:
    """IWL 8단계 사고 확장 모델 처리기"""
    
    def process_stage(self, goal: Goal, user_response: UserResponse, history: List[Dict]) -> ThinkingResult:
        """현재 대화 상태에 따른 사고 단계 결정"""
        try:
            progress = goal.progress if goal else 0.0
            conversation_length = len(history)
            
            # 진행도와 대화 길이에 따른 사고 단계 매핑
            if progress < 0.1 and conversation_length < 2:
                current_stage = ThinkingStage.STAGE_1_AWARENESS
            elif progress < 0.2:
                current_stage = ThinkingStage.STAGE_2_QUESTIONING
            elif progress < 0.4:
                current_stage = ThinkingStage.STAGE_3_EXPLORATION
            elif progress < 0.6:
                current_stage = ThinkingStage.STAGE_4_CONNECTION
            elif progress < 0.7:
                current_stage = ThinkingStage.STAGE_5_SYNTHESIS
            elif progress < 0.8:
                current_stage = ThinkingStage.STAGE_6_EVALUATION
            elif progress < 0.9:
                current_stage = ThinkingStage.STAGE_7_APPLICATION
            else:
                current_stage = ThinkingStage.STAGE_8_REFLECTION
            
            return ThinkingResult(
                current_stage=current_stage,
                insights=self._generate_insights(current_stage, user_response),
                next_questions=self._generate_next_questions(current_stage, goal),
                confidence_level=min(progress + 0.2, 1.0)
            )
        except Exception as e:
            logger.error(f"사고 단계 처리 오류: {e}")
            return ThinkingResult(
                current_stage=ThinkingStage.STAGE_1_AWARENESS,
                insights=["사고 처리 중 오류 발생"],
                next_questions=["무엇부터 시작할까요?"],
                confidence_level=0.0
            )
    
    def _generate_insights(self, stage: ThinkingStage, user_response: UserResponse) -> List[str]:
        """사고 단계별 인사이트 생성"""
        stage_insights = {
            ThinkingStage.STAGE_1_AWARENESS: ["현재 상황을 파악하고 있습니다"],
            ThinkingStage.STAGE_2_QUESTIONING: ["핵심 질문을 발견하는 중입니다"],
            ThinkingStage.STAGE_3_EXPLORATION: ["다양한 관점을 탐색하고 있습니다"],
            ThinkingStage.STAGE_4_CONNECTION: ["아이디어 간 연결점을 찾고 있습니다"],
            ThinkingStage.STAGE_5_SYNTHESIS: ["통합된 이해를 구축하고 있습니다"],
            ThinkingStage.STAGE_6_EVALUATION: ["비판적으로 평가하고 있습니다"],
            ThinkingStage.STAGE_7_APPLICATION: ["실행 가능한 계획을 수립하고 있습니다"],
            ThinkingStage.STAGE_8_REFLECTION: ["학습 내용을 정리하고 있습니다"]
        }
        return stage_insights.get(stage, ["사고를 진행하고 있습니다"])
    
    def _generate_next_questions(self, stage: ThinkingStage, goal: Goal) -> List[str]:
        """사고 단계별 다음 질문 생성"""
        if not goal:
            return ["어떤 목표를 설정하시겠습니까?"]
        
        stage_questions = {
            ThinkingStage.STAGE_1_AWARENESS: ["현재 상황은 어떤가요?"],
            ThinkingStage.STAGE_2_QUESTIONING: ["가장 중요한 질문은 무엇인가요?"],
            ThinkingStage.STAGE_3_EXPLORATION: ["다른 관점에서는 어떻게 보일까요?"],
            ThinkingStage.STAGE_4_CONNECTION: ["이들 사이의 관계는 무엇인가요?"],
            ThinkingStage.STAGE_5_SYNTHESIS: ["전체적으로 어떻게 정리할 수 있을까요?"],
            ThinkingStage.STAGE_6_EVALUATION: ["이 접근법의 장단점은 무엇인가요?"],
            ThinkingStage.STAGE_7_APPLICATION: ["구체적으로 어떻게 실행할까요?"],
            ThinkingStage.STAGE_8_REFLECTION: ["이 과정에서 무엇을 배웠나요?"]
        }
        return stage_questions.get(stage, ["다음 단계는 무엇일까요?"])

class ProgressEvaluator:
    """목표 달성 진행도 평가기 (개선된 버전)"""
    
    def evaluate_progress(self, 
                         goal: Goal, 
                         user_response: UserResponse, 
                         conversation_history: List[Dict]) -> Dict:
        """
        목표 달성 진행도 평가
        
        Returns:
            Dict: 진행 상태 및 평가 결과
        """
        try:
            progress_indicators = []
            
            # 1. 성공 기준 대비 언급된 내용 비율
            all_user_content = " ".join([h.get("user_input", "") for h in conversation_history] + [user_response.content])
            
            mentioned_criteria = 0
            for criteria in goal.success_criteria:
                criteria_keywords = criteria.lower().split()[:3]
                if any(keyword in all_user_content.lower() for keyword in criteria_keywords):
                    mentioned_criteria += 1
            
            criteria_coverage = mentioned_criteria / len(goal.success_criteria) if goal.success_criteria else 0
            progress_indicators.append(criteria_coverage * 0.4)
            
            # 2. 대화 길이 기반 진행도 (참여도)
            engagement_score = min(len(conversation_history) / 10, 1.0)
            progress_indicators.append(engagement_score * 0.3)
            
            # 3. 구체성 평가
            specificity_keywords = ['단계', '방법', '계획', '예시', '구체적']
            specificity_score = sum(1 for keyword in specificity_keywords 
                                   if keyword in user_response.content) / len(specificity_keywords)
            progress_indicators.append(specificity_score * 0.3)
            
            # 최종 진행도 계산
            total_progress = sum(progress_indicators)
            goal.progress = min(total_progress, 1.0)
            
            # 상태 결정
            if goal.progress >= 0.9:
                goal.status = GoalStatus.COMPLETED
            elif goal.progress >= 0.1:
                goal.status = GoalStatus.IN_PROGRESS
            
            return {
                "progress": goal.progress,
                "status": goal.status.value,
                "criteria_coverage": criteria_coverage,
                "engagement_score": engagement_score,
                "specificity_score": specificity_score,
                "next_needed": self._identify_missing_elements(goal, user_response)
            }
        except Exception as e:
            logger.error(f"진행도 평가 오류: {e}")
            return {
                "progress": 0.0,
                "status": "error",
                "criteria_coverage": 0.0,
                "engagement_score": 0.0,
                "specificity_score": 0.0,
                "next_needed": []
            }
    
    def _identify_missing_elements(self, goal: Goal, user_response: UserResponse) -> List[str]:
        """부족한 요소 식별"""
        try:
            missing = []
            all_content = user_response.content.lower()
            
            for criteria in goal.success_criteria:
                criteria_keywords = criteria.lower().split()[:3]
                if not any(keyword in all_content for keyword in criteria_keywords):
                    missing.append(criteria)
            
            return missing
        except Exception as e:
            logger.error(f"부족 요소 식별 오류: {e}")
            return []

class ActionPlanner:
    """다음 행동 계획기 (개선된 버전)"""
    
    def plan_next_action(self, 
                        goal: Goal,
                        user_response: UserResponse,
                        progress_status: Dict,
                        context: Dict,
                        thinking_stage: ThinkingStage) -> AgentAction:
        """현재 상황에 기반하여 다음 행동 계획"""
        try:
            progress = progress_status.get("progress", 0.0)
            missing_elements = progress_status.get("next_needed", [])
            
            # 진행도에 따른 행동 전략
            if progress < 0.2:
                return self._create_clarification_action(goal, missing_elements, thinking_stage)
            elif progress < 0.6:
                return self._create_information_gathering_action(goal, missing_elements, thinking_stage)
            elif progress < 0.9:
                return self._create_validation_action(goal, progress_status, thinking_stage)
            else:
                return self._create_completion_action(goal, thinking_stage)
        except Exception as e:
            logger.error(f"행동 계획 오류: {e}")
            return AgentAction(
                action_type=ActionType.PROVIDE_INFO,
                content="죄송합니다. 다시 한 번 말씀해 주세요.",
                reasoning=f"계획 수립 중 오류: {str(e)}",
                expected_outcome="사용자 재입력",
                thinking_stage=ThinkingStage.STAGE_1_AWARENESS
            )
    
    def _create_clarification_action(self, goal: Goal, missing_elements: List[str], stage: ThinkingStage) -> AgentAction:
        """목표 명확화 행동"""
        if missing_elements:
            missing_text = ", ".join(missing_elements[:2])
            content = f"{goal.description}를 위해서는 '{missing_text}'에 대해 더 구체적으로 알려주셔야 해요. 어떻게 생각하고 계시나요?"
        else:
            content = f"{goal.description}을 달성하기 위해 가장 먼저 무엇부터 시작하고 싶으신가요?"
            
        return AgentAction(
            action_type=ActionType.CLARIFY_REQUIREMENT,
            content=content,
            reasoning="목표 달성에 필요한 구체적 정보 부족",
            expected_outcome="사용자가 구체적인 요구사항 제공",
            thinking_stage=stage
        )
    
    def _create_information_gathering_action(self, goal: Goal, missing_elements: List[str], stage: ThinkingStage) -> AgentAction:
        """정보 수집 행동"""
        if missing_elements:
            element = missing_elements[0]
            content = f"{element}에 대해 좋은 아이디어가 있으신가요? 구체적으로 어떤 방법을 생각하고 계신지 들려주세요."
        else:
            content = f"{goal.description} 계획에서 가장 중요하다고 생각하시는 부분은 무엇인가요?"
            
        return AgentAction(
            action_type=ActionType.ASK_QUESTION,
            content=content,
            reasoning="구체적인 실행 계획 수립 필요",
            expected_outcome="사용자가 세부 실행 방안 제시",
            thinking_stage=stage
        )
    
    def _create_validation_action(self, goal: Goal, progress_status: Dict, stage: ThinkingStage) -> AgentAction:
        """검증 행동"""
        content = f"지금까지 많이 진전되었네요! {goal.description} 계획이 거의 완성되어 가는 것 같습니다. 마지막으로 놓친 부분이나 걱정되는 점이 있나요?"
        
        return AgentAction(
            action_type=ActionType.VALIDATE_PROGRESS,
            content=content,
            reasoning="목표 달성 직전 최종 확인 필요",
            expected_outcome="사용자가 최종 검토 및 확인 완료",
            thinking_stage=stage
        )
    
    def _create_completion_action(self, goal: Goal, stage: ThinkingStage) -> AgentAction:
        """완료 행동"""
        content = f"훌륭합니다! '{goal.description}' 목표를 성공적으로 달성하셨네요. 이제 실행에 옮겨보세요. 또 다른 목표가 있으시면 언제든 말씀해 주세요!"
        
        return AgentAction(
            action_type=ActionType.PROVIDE_INFO,
            content=content,
            reasoning="목표 달성 완료 및 성공 인정",
            expected_outcome="사용자 만족 및 차기 목표 설정 가능",
            thinking_stage=stage
        )

class ContextAnalyzer:
    """대화 컨텍스트 분석기 (개선된 버전)"""
    
    def analyze_user_input(self, user_response: UserResponse, context: Dict) -> None:
        """사용자 입력에서 컨텍스트 정보 추출"""
        try:
            user_input = user_response.content.lower()
            
            # 감정 상태 추론
            emotion_keywords = {
                '흥미': ['재미있어', '흥미로워', '궁금해'],
                '열정': ['좋았어', '하고싶어', '끌리는'],
                '불안': ['걱정이', '어려울까', '모르겠어'],
                '확신': ['확실해', '알겠어', '당연해']
            }
            
            for emotion, keywords in emotion_keywords.items():
                if any(keyword in user_input for keyword in keywords):
                    context['user_emotion'] = emotion
                    break
            
            # 경험 수준 추론
            experience_indicators = {
                '초보': ['처음', '모르겠어', '어려워'],
                '중급': ['조금', '대충', '기본적'],
                '고급': ['잘 알아', '경험이', '전문적']
            }
            
            for level, indicators in experience_indicators.items():
                if any(indicator in user_input for indicator in indicators):
                    context['experience_level'] = level
                    break
            
            # 선호도 추출
            if '빠른' in user_input or '간단' in user_input:
                context['preference'] = 'quick'
            elif '자세한' in user_input or '천천히' in user_input:
                context['preference'] = 'detailed'
            
            user_response.interpreted_intent = context.get('user_emotion', 'neutral')
            user_response.extracted_info = {
                'emotion': context.get('user_emotion'),
                'experience': context.get('experience_level'),
                'preference': context.get('preference')
            }
        except Exception as e:
            logger.error(f"컨텍스트 분석 오류: {e}")

# PoC 데모 테스트 코드
if __name__ == "__main__":
    print("=== 목표 지향 에이전트 v2.0 PoC 데모 ===\n")
    
    try:
        # 에이전트 초기화
        agent = GoalOrientedAgent()
        
        # 예시 목표 설정
        goal = Goal(
            id="python_learning_plan",
            description="Python 학습 계획을 세우기",
            success_criteria=[
                "3단계로 나눠진 학습 계획",
                "각 단계별 구체적인 학습 내용",
                "학습 기간 및 방법 지정"
            ],
            priority=1
        )
        
        if not agent.set_goal(goal):
            print("목표 설정 실패")
            exit(1)
        
        # 시뮬레이션 대화
        test_inputs = [
            "Python을 배우고 싶어요",
            "예전에 조금 해본 적이 있어요. 기본적인 문법은 알고 있습니다",
            "3단계로 나눠서 학습하고 싶습니다. 1단계는 문법 마스터, 2단계는 실습 프로젝트, 3단계는 고급 주제들을 다루기",
            "각 단계마다 2주씩 하려고 합니다. 온라인 강의와 책을 병행해서 학습할 계획입니다",
            "네, 완벽한 계획이 나온 것 같습니다!"
        ]
        
        for i, user_input in enumerate(test_inputs, 1):
            print(f"\n--- 턴 {i} ---")
            print(f"사용자: {user_input}")
            
            action = agent.process_user_input(user_input)
            if action:
                print(f"에이전트: {action.content}")
                print(f"행동 유형: {action.action_type.value}")
                print(f"사고 단계: {action.thinking_stage.value}")
                print(f"진행도: {agent.current_goal.progress:.1%}")
                
                if agent.current_goal.status == GoalStatus.COMPLETED:
                    print("🎉 목표 달성 완료!")
                    break
            else:
                print("에이전트 응답 생성 실패")
        
        # 최종 상태 출력
        print("\n=== 최종 상태 ===\n")
        status = agent.get_current_status()
        print(json.dumps(status, ensure_ascii=False, indent=2))
        
        # 세션 저장
        if agent.save_session():
            print("\n💾 PoC 데모 세션이 안전하게 저장되었습니다.")
        else:
            print("\n❌ 세션 저장에 실패했습니다.")
            
    except Exception as e:
        logger.error(f"데모 실행 중 오류: {e}")
        print(f"데모 실행 실패: {e}")
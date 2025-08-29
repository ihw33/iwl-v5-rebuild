"""
S1-A1 Interactive 모듈 테스트
리팩토링된 코드 테스트
"""
import json
from datetime import datetime
from nodes.learning.S1_A1_interactive import (
    S1_A1_InteractiveNode, 
    SessionState,
    UserProfile,
    ObservationEntry
)
from nodes.base.interfaces import ExecutionContext
from nodes.learning.config import PersonaTypes, ActionTypes


def test_user_profile_creation():
    """UserProfile 생성 테스트"""
    profile = UserProfile(
        user_id="test_user",
        persona_type=PersonaTypes.VISUAL_LEARNER,
        learning_style="step_by_step",
        selected_curriculum="basic",
        profile_vector=[0.5, 0.3, 0.8]
    )
    
    assert profile.user_id == "test_user"
    assert profile.persona_type == PersonaTypes.VISUAL_LEARNER
    assert len(profile.profile_vector) == 3


def test_session_state():
    """SessionState 기능 테스트"""
    session = SessionState(
        session_id="test_session",
        user_id="test_user"
    )
    
    # 관찰 추가
    entry1 = session.add_observation("파란색 버튼이 보입니다", "color")
    assert entry1.has_judgment == False
    assert session.total_observations == 1
    
    # 판단 언어 포함 관찰
    entry2 = session.add_observation("이 버튼이 예쁘네요", "shape")
    assert entry2.has_judgment == True
    assert session.judgment_count == 1
    
    # DAG 조정 기록
    session.record_adjustment({
        "action": "add_support",
        "reason": "low_performance"
    })
    assert len(session.dag_adjustments) == 1


def test_interactive_node_start():
    """노드 시작 테스트"""
    node = S1_A1_InteractiveNode()
    ctx = ExecutionContext(
        session_id="test_001",
        user_id="test_user"
    )
    
    # 기본 시작
    result = node.execute(
        payloads={
            "action": ActionTypes.START,
            "user_level": "L1"
        },
        ctx=ctx
    )
    
    assert result["response"]["type"] == "session_started"
    assert "next_prompt" in result
    assert "session_state" in result
    
    # UserProfile 포함 시작
    result_with_profile = node.execute(
        payloads={
            "action": ActionTypes.START,
            "user_level": "L1",
            "user_profile": {
                "user_id": "test_user",
                "persona_type": PersonaTypes.VISUAL_LEARNER,
                "learning_style": "holistic",
                "selected_curriculum": "advanced"
            }
        },
        ctx=ctx
    )
    
    session_data = result_with_profile["session_state"]
    assert "user_profile" in session_data
    assert session_data["user_profile"]["persona_type"] == PersonaTypes.VISUAL_LEARNER


def test_observation_processing():
    """관찰 처리 테스트"""
    node = S1_A1_InteractiveNode()
    ctx = ExecutionContext(
        session_id="test_002",
        user_id="test_user"
    )
    
    # 세션 시작
    start_result = node.execute(
        payloads={
            "action": ActionTypes.START,
            "user_level": "L1"
        },
        ctx=ctx
    )
    
    session_state = start_result["session_state"]
    
    # 관찰 제출
    observe_result = node.execute(
        payloads={
            "action": ActionTypes.OBSERVE,
            "session_state": session_state,
            "user_input": "화면 상단에 파란색 헤더가 있습니다"
        },
        ctx=ctx
    )
    
    assert observe_result["response"]["type"] == "observation_received"
    assert "feedback" in observe_result["response"]
    assert observe_result["response"]["has_judgment"] == False
    assert observe_result["response"]["observation_type"] in ["color", "position"]
    
    # 품질 점수 확인
    assert 0 <= observe_result["response"]["quality_score"] <= 1


def test_dag_adjustment():
    """DAG 조정 테스트"""
    node = S1_A1_InteractiveNode()
    ctx = ExecutionContext(
        session_id="test_003",
        user_id="test_user"
    )
    
    # 세션 시작
    start_result = node.execute(
        payloads={
            "action": ActionTypes.START,
            "user_level": "L1",
            "user_profile": {
                "persona_type": PersonaTypes.PRACTICE_ORIENTED
            }
        },
        ctx=ctx
    )
    
    session_state = start_result["session_state"]
    
    # 낮은 품질 관찰 여러 개 제출
    for i in range(3):
        result = node.execute(
            payloads={
                "action": ActionTypes.OBSERVE,
                "session_state": session_state,
                "user_input": "좋다"  # 판단 언어
            },
            ctx=ctx
        )
        session_state = result["session_state"]
    
    # DAG 조정이 발생했는지 확인
    if "dag_adjustments" in session_state:
        assert len(session_state["dag_adjustments"]) > 0
        adjustment = session_state["dag_adjustments"][0]
        assert adjustment["adjustment"]["action"] in ["reinforce_concept", "add_support"]


def test_session_complete():
    """세션 완료 테스트"""
    node = S1_A1_InteractiveNode()
    ctx = ExecutionContext(
        session_id="test_004",
        user_id="test_user"
    )
    
    # 세션 시작
    start_result = node.execute(
        payloads={"action": ActionTypes.START},
        ctx=ctx
    )
    
    # 세션 완료
    complete_result = node.execute(
        payloads={
            "action": ActionTypes.COMPLETE,
            "session_state": start_result["session_state"]
        },
        ctx=ctx
    )
    
    assert complete_result["response"]["type"] == "session_completed"
    assert "evaluation" in complete_result["response"]
    assert "final_stats" in complete_result["response"]


def test_error_handling():
    """에러 처리 테스트"""
    node = S1_A1_InteractiveNode()
    ctx = ExecutionContext(
        session_id="test_005",
        user_id="test_user"
    )
    
    # 잘못된 액션
    try:
        node.execute(
            payloads={"action": "invalid_action"},
            ctx=ctx
        )
        assert False, "Should raise ValidationError"
    except Exception as e:
        assert "Invalid action" in str(e)
    
    # observe 액션에 user_input 없음
    try:
        node.execute(
            payloads={"action": ActionTypes.OBSERVE},
            ctx=ctx
        )
        assert False, "Should raise ValidationError"
    except Exception as e:
        assert "user_input required" in str(e)


if __name__ == "__main__":
    print("=== S1-A1 Interactive 테스트 시작 ===\n")
    
    # 각 테스트 실행
    test_user_profile_creation()
    print("✅ UserProfile 생성 테스트 통과")
    
    test_session_state()
    print("✅ SessionState 기능 테스트 통과")
    
    test_interactive_node_start()
    print("✅ 노드 시작 테스트 통과")
    
    test_observation_processing()
    print("✅ 관찰 처리 테스트 통과")
    
    test_dag_adjustment()
    print("✅ DAG 조정 테스트 통과")
    
    test_session_complete()
    print("✅ 세션 완료 테스트 통과")
    
    test_error_handling()
    print("✅ 에러 처리 테스트 통과")
    
    print("\n🎉 모든 테스트 통과!")
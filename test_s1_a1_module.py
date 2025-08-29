"""
S1-A1 모듈 테스트
"""
import json
from nodes.learning.S1_A1_perception_depth import S1_A1_PureObservationNode, DifficultyLevel
from nodes.base.interfaces import ExecutionContext


def test_s1_a1_module():
    """S1-A1 모듈 테스트"""
    
    print("=== S1-A1 순수한 관찰 모듈 테스트 ===\n")
    
    # 노드 인스턴스 생성
    node = S1_A1_PureObservationNode()
    
    # 메타데이터 확인
    metadata = node.get_module_metadata()
    print(f"모듈 ID: {metadata['module_id']}")
    print(f"모듈명: {metadata['module_name']}")
    print(f"핵심 개념: {metadata['core_concept']}\n")
    
    # 컨텍스트 생성
    ctx = ExecutionContext(
        session_id="test-session-001",
        user_id="test-user",
        trace_id="trace-001"
    )
    
    # 각 레벨별 테스트
    for level in ["L1", "L3", "L5"]:
        print(f"\n{'='*50}")
        print(f"레벨 {level} 테스트")
        print('='*50)
        
        # 테스트 데이터
        test_responses = {
            "L1": [
                "파란색 버튼이 보여요",
                "하얀 배경이 있어요",
                "아래쪽에 입력창이 있네요",
                "글자가 검은색이에요",
                "화면이 네모 모양이에요"
            ],
            "L3": [
                "화면이 3개 영역으로 나뉘어 있습니다",
                "왼쪽 사이드바는 전체의 20% 정도 차지합니다",
                "메인 영역에 대화 내용이 표시됩니다",
                "상단 헤더는 고정되어 있고 높이가 일정합니다",
                "요소들이 격자 형태로 정렬되어 있습니다",
                "여백이 균등하게 분포되어 있습니다",
                "색상 패턴이 일관성 있게 반복됩니다",
                "전체적으로 대칭적인 구조를 보입니다"
            ],
            "L5": [
                "처음에는 큰 요소만 보였는데 작은 아이콘들이 있었네요",
                "그림자 효과가 미묘하게 깊이감을 만들고 있습니다",
                "검색 기능이 있을 법한데 없는 것이 특이합니다",
                "비어있는 공간이 숨 쉴 여유를 주는 것 같습니다",
                "제 시선이 왼쪽 위에서 오른쪽 아래로 Z자로 움직였습니다",
                "관찰하면서 제가 무의식적으로 기능을 추측하고 있었네요",
                "보는 것과 인식하는 것 사이에 간극이 있음을 느낍니다",
                "없는 것을 보려고 하니 오히려 있는 것이 선명해집니다",
                "관찰 자체가 대상을 변화시키는 것 같습니다",
                "제가 보고 있다는 사실을 의식하니 보는 방식이 달라집니다"
            ]
        }
        
        # 실행
        result = node.execute(
            payloads={
                "user_level": level,
                "observation_target": {"type": "ChatGPT interface"},
                "user_responses": test_responses[level]
            },
            ctx=ctx
        )
        
        # 활동 시퀀스 출력
        print("\n📋 활동 시퀀스:")
        for i, activity in enumerate(result["activity_sequence"][:3], 1):  # 처음 3개만
            print(f"\nStep {i}:")
            print(f"  지시: {activity['instruction']}")
            print(f"  AI 프롬프트: {activity['ai_prompt'][:50]}...")
            print(f"  시간: {activity['duration']}초")
            print(f"  인지 부하: {activity['cognitive_load']}")
        
        # AI 가이드 출력
        print("\n🤖 AI 응답 가이드:")
        guidance = result["ai_guidance"]
        if isinstance(guidance, dict):
            if "tone" in guidance:
                print(f"  톤: {guidance['tone']}")
            if "sample_responses" in guidance:
                print("  샘플 응답:")
                for key, value in guidance["sample_responses"].items():
                    print(f"    - {key}: {value[:40]}...")
        
        # 메트릭 출력
        print("\n📊 관찰 품질 메트릭:")
        metrics = result["observation_metrics"]
        print(f"  관찰 개수: {metrics['observation_count']}")
        print(f"  판단 언어 사용: {metrics['judgment_language_use']}회")
        print(f"  관찰 다양성: {metrics['observation_diversity']}/5")
        print(f"  품질 점수: {metrics['quality_score']:.2f}/1.0")
        print(f"  성공 지표: {', '.join(metrics['success_indicators']) if metrics['success_indicators'] else '없음'}")
        
        # 학습 결과 평가
        outcomes = node.evaluate_outcomes(result)
        print("\n✅ 학습 평가:")
        print(f"  성공 여부: {'성공' if outcomes['success'] else '실패'}")
        print(f"  점수: {outcomes['score']:.1f}/100")
        print(f"  피드백: {outcomes['feedback']}")
        print(f"  다음 추천: {outcomes['next_recommended']}")
    
    print("\n" + "="*50)
    print("테스트 완료!")


if __name__ == "__main__":
    test_s1_a1_module()
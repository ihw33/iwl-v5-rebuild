"""
S1-A1 교수법 테스트
"""
from nodes.teaching_methods.s1_a1_teaching_methods import (
    ObservationQuizMethod,
    DialogueDiscussionMethod,
    ObservationPracticeMethod,
    GamificationElements
)
from nodes.base.interfaces import ExecutionContext

def test_all_methods():
    print("=== S1-A1 교수법 테스트 ===\n")
    
    # 1. 퀴즈 방식
    print("1. 퀴즈 방식 테스트")
    quiz = ObservationQuizMethod()
    quiz_result = quiz._run(
        {"scene": {"type": "test"}, "level": "L1"},
        ExecutionContext(session_id="test")
    )
    print(f"   L1 퀴즈: {len(quiz_result['quiz_items'])}개 문항")
    for item in quiz_result['quiz_items']:
        print(f"   - {item['q']}")
    
    # 2. 대화/토론 방식
    print("\n2. 대화/토론 방식 테스트")
    dialogue = DialogueDiscussionMethod()
    dialogue_result = dialogue._run(
        {"observations": ["파란 버튼", "위쪽에 메뉴"]},
        ExecutionContext(session_id="test")
    )
    print(f"   토론 주제: {len(dialogue_result['discussion_prompts'])}개")
    for prompt in dialogue_result['discussion_prompts']:
        print(f"   - {prompt}")
    
    # 3. 관찰 실습
    print("\n3. 관찰 실습 방식 테스트")
    practice = ObservationPracticeMethod()
    practice_result = practice._run(
        {"target": {"type": "screen"}},
        ExecutionContext(session_id="test")
    )
    print(f"   실습 단계: {len(practice_result['practice_guide']['steps'])}단계")
    for step in practice_result['practice_guide']['steps']:
        print(f"   - {step}")
    
    # 4. 게이미피케이션
    print("\n4. 게이미피케이션 테스트")
    game = GamificationElements()
    game_result = game._run(
        {
            "performance": {
                "observations_count": 15,
                "pure_observations": 12,
                "judgment_words": 2,
                "vocabulary_diversity": 35,
                "consecutive_days": 3
            }
        },
        ExecutionContext(session_id="test")
    )
    rewards = game_result['rewards']
    print(f"   포인트: {rewards['points']}")
    print(f"   배지: {', '.join(rewards['badges'])}")
    print(f"   연속 일수: {rewards['streak']}일")
    print(f"   레벨: {rewards['level_progress']['level']} (진행률: {rewards['level_progress']['progress']*100:.0f}%)")
    
    print("\n✅ 모든 교수법 테스트 완료!")

if __name__ == "__main__":
    test_all_methods()
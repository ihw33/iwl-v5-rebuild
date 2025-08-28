"""
학습 모듈 설정 파일
S1-A1 및 다른 학습 모듈들이 공통으로 사용하는 설정값
"""

class LearningConfig:
    """학습 모듈 전역 설정"""
    
    # DAG 조정 임계값
    LOW_PERFORMANCE_THRESHOLD = 0.5
    HIGH_PERFORMANCE_THRESHOLD = 0.9
    REPETITIVE_ERRORS_THRESHOLD = 3
    SLOW_PROGRESS_THRESHOLD = 5
    
    # 관찰 관련
    TOTAL_OBSERVATION_CATEGORIES = 5
    DIVERSITY_THRESHOLD_LOW = 0.3
    DIVERSITY_THRESHOLD_MEDIUM = 0.4
    DIVERSITY_THRESHOLD_HIGH = 0.6
    
    # 판단 언어 목록
    JUDGMENT_WORDS = {
        "positive": ["좋", "멋지", "예쁘", "편하", "최고", "훌륭"],
        "negative": ["나쁘", "못생", "불편", "싫", "별로", "최악"],
        "evaluative": ["쓸모", "가치", "의미", "효과", "효율"]
    }
    
    # 레벨별 최소 관찰 수
    MIN_OBSERVATIONS = {
        "L1": 3,
        "L3": 5,
        "L5": 4
    }
    
    # 기본값
    DEFAULT_LEVEL = "L1"
    DEFAULT_PERSONA = "general"
    DEFAULT_LEARNING_STYLE = "balanced"
    DEFAULT_CURRICULUM = "default"
    
    # 관찰 카테고리
    OBSERVATION_CATEGORIES = {
        "color": ["색", "빨강", "파랑", "초록", "노랑", "검정", "흰", "회색"],
        "shape": ["네모", "동그라미", "삼각", "직선", "곡선", "모양"],
        "size": ["크", "작", "넓", "좁", "길", "짧", "두껍", "얇"],
        "position": ["위", "아래", "왼쪽", "오른쪽", "가운데", "모서리", "상단", "하단"],
        "texture": ["매끄", "거칠", "반짝", "무광", "투명", "불투명"],
        "meta": ["보이", "관찰", "느껴", "인식", "시선", "없는", "부재"]
    }


class PersonaTypes:
    """페르소나 타입 상수"""
    VISUAL_LEARNER = "visual_learner"
    PRACTICE_ORIENTED = "practice_oriented"
    THEORETICAL = "theoretical"
    GENERAL = "general"


class ActionTypes:
    """액션 타입 상수"""
    START = "start"
    OBSERVE = "observe"
    GET_PROMPT = "get_prompt"
    COMPLETE = "complete"


class ObservationTypes:
    """관찰 타입 상수"""
    COLOR = "color"
    SHAPE = "shape"
    SIZE = "size"
    POSITION = "position"
    TEXTURE = "texture"
    META = "meta"
    GENERAL = "general"
    UNKNOWN = "unknown"
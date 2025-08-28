"""
관찰 분석 유틸리티
테스트 가능하도록 분리된 순수 함수들
"""
from typing import Set, List, Dict, Any
from functools import lru_cache
from nodes.learning.config import LearningConfig, ObservationTypes


class ObservationAnalyzer:
    """관찰 분석 로직"""
    
    @staticmethod
    @lru_cache(maxsize=1)
    def get_judgment_words() -> Set[str]:
        """판단 언어 세트 반환 (캐싱)"""
        words = set()
        for category in LearningConfig.JUDGMENT_WORDS.values():
            words.update(category)
        return words
    
    @classmethod
    def detect_judgment(cls, text: str) -> bool:
        """
        판단 언어 감지 (최적화)
        
        Args:
            text: 검사할 텍스트
            
        Returns:
            판단 언어 포함 여부
        """
        judgment_words = cls.get_judgment_words()
        # 단어 단위로 검사 (더 정확)
        text_words = set(text.split())
        
        # 부분 문자열 검사도 수행
        for word in judgment_words:
            if word in text:
                return True
        
        return False
    
    @staticmethod
    def classify_observation(text: str) -> str:
        """
        관찰 내용 분류
        
        Args:
            text: 관찰 텍스트
            
        Returns:
            관찰 카테고리
        """
        categories = LearningConfig.OBSERVATION_CATEGORIES
        
        # 각 카테고리별로 매칭 점수 계산
        scores = {}
        for category, keywords in categories.items():
            score = sum(1 for keyword in keywords if keyword in text)
            if score > 0:
                scores[category] = score
        
        # 가장 높은 점수의 카테고리 반환
        if scores:
            return max(scores, key=scores.get)
        
        return ObservationTypes.GENERAL
    
    @staticmethod
    def calculate_quality_score(
        observation_text: str,
        has_judgment: bool,
        is_new_category: bool,
        observation_length: int,
        level: str = "L1"
    ) -> float:
        """
        관찰 품질 점수 계산
        
        Args:
            observation_text: 관찰 내용
            has_judgment: 판단 언어 포함 여부
            is_new_category: 새로운 카테고리 관찰 여부
            observation_length: 관찰 텍스트 길이
            level: 사용자 레벨
            
        Returns:
            품질 점수 (0.0 ~ 1.0)
        """
        score = 0.5  # 기본 점수
        
        # 판단 언어 없으면 가점
        if not has_judgment:
            score += 0.2
        
        # 새로운 카테고리 관찰 시 가점
        if is_new_category:
            score += 0.15
        
        # 레벨별 특별 가점
        if level == "L5":
            # 고급 레벨은 메타 관찰에 가점
            if any(word in observation_text for word in ["없", "부재", "관찰하는", "보는 것"]):
                score += 0.1
        elif level == "L3":
            # 중급 레벨은 공간 관계에 가점
            if any(word in observation_text for word in ["관계", "패턴", "구조", "배치"]):
                score += 0.1
        
        # 관찰 길이에 따른 가점 (20자 이상)
        if observation_length > 20:
            score += 0.05
        
        # 너무 짧으면 감점 (5자 미만)
        if observation_length < 5:
            score -= 0.1
        
        return max(0.0, min(1.0, score))
    
    @staticmethod
    def calculate_diversity_score(observation_types: List[str]) -> float:
        """
        관찰 다양성 점수 계산
        
        Args:
            observation_types: 관찰 타입 리스트
            
        Returns:
            다양성 점수 (0.0 ~ 1.0)
        """
        unique_types = set(observation_types)
        return len(unique_types) / LearningConfig.TOTAL_OBSERVATION_CATEGORIES
    
    @staticmethod
    def analyze_observation_pattern(observations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        관찰 패턴 분석
        
        Args:
            observations: 관찰 리스트
            
        Returns:
            패턴 분석 결과
        """
        if not observations:
            return {
                "total_count": 0,
                "judgment_ratio": 0.0,
                "diversity": 0.0,
                "average_quality": 0.0,
                "dominant_type": None
            }
        
        total = len(observations)
        judgment_count = sum(1 for obs in observations if obs.get("has_judgment", False))
        
        # 타입별 카운트
        type_counts = {}
        quality_sum = 0.0
        
        for obs in observations:
            obs_type = obs.get("observation_type", ObservationTypes.UNKNOWN)
            type_counts[obs_type] = type_counts.get(obs_type, 0) + 1
            quality_sum += obs.get("quality_score", 0.0)
        
        # 가장 많은 타입
        dominant_type = max(type_counts, key=type_counts.get) if type_counts else None
        
        # 다양성 계산
        diversity = len(type_counts) / LearningConfig.TOTAL_OBSERVATION_CATEGORIES
        
        return {
            "total_count": total,
            "judgment_ratio": judgment_count / total,
            "diversity": diversity,
            "average_quality": quality_sum / total,
            "dominant_type": dominant_type,
            "type_distribution": type_counts
        }
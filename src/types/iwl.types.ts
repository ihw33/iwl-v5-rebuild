/**
 * IWL v5.0 Type Definitions
 * TypeScript Expert가 생성한 타입 정의
 */

// 8단계 사고 프로세스 타입
export type ThinkingStage = 
  | 'observation'    // 관찰
  | 'classification' // 분류
  | 'definition'     // 정의
  | 'inference'      // 추론
  | 'design'         // 설계
  | 'execution'      // 실행
  | 'evaluation'     // 평가
  | 'reflection';    // 반성

// 4기준 평가 타입
export type EvaluationCriteria = 
  | 'evidence'       // 사실성
  | 'structure'      // 구조성
  | 'clarity'        // 명료성
  | 'actionability'; // 실행성

// 평가 점수 타입 (1-5)
export type Score = 1 | 2 | 3 | 4 | 5;

// 8x4 매트릭스 타입
export type Matrix = {
  [stage in ThinkingStage]: {
    [criteria in EvaluationCriteria]: Score;
  };
};

// 학습자 프로필 타입
export interface LearnerProfile {
  id: string;
  name: string;
  level: 'beginner' | 'intermediate' | 'advanced';
  completedStages: ThinkingStage[];
  matrix: Partial<Matrix>;
  createdAt: Date;
  updatedAt: Date;
}

// 학습 세션 타입
export interface LearningSession {
  id: string;
  learnerId: string;
  currentStage: ThinkingStage;
  evaluations: {
    stage: ThinkingStage;
    criteria: EvaluationCriteria;
    score: Score;
    feedback: string;
  }[];
  startedAt: Date;
  completedAt?: Date;
}

// 유틸리티 타입: Stage 정보
export interface StageInfo {
  key: ThinkingStage;
  label: string;
  description: string;
  color: string;
  icon: string;
}

// 유틸리티 타입: Criteria 정보
export interface CriteriaInfo {
  key: EvaluationCriteria;
  label: string;
  description: string;
  weight: number;
}
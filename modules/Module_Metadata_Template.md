# 모듈 메타데이터 템플릿

## 📋 개요
- **버전**: v1.0
- **작성일**: 2025-08-15
- **용도**: IWL v5.0의 32개 모듈(8단계 × 4인지축) 표준 메타데이터

---

## 🎯 모듈 기본 정보

```yaml
module_id: "S[1-8]-A[1-4]"  # 예: S1-A1
module_name: "[단계명] × [인지축명]"
stage: 
  number: [1-8]
  name: "[한글 단계명]"
  focus: "[이 단계의 핵심 활동]"
cognitive_axis:
  number: [1-4]
  name: "[A1-분석/A2-창의/A3-협업/A4-성찰]"
  focus: "[이 축의 핵심 역량]"

difficulty_range:
  min: L1
  max: L5
  sweet_spot: L[2-4]  # 가장 효과적인 레벨

typical_duration:
  standalone: 35  # 단독 수업 시
  as_part: 10-15  # 조합 수업 시

description: |
  [이 모듈이 다루는 핵심 내용과 학습 목표를 2-3문장으로 설명]
```

---

## 📚 학습 설계

### 학습 목표
```yaml
learning_objectives:
  primary:
    - "[핵심 학습 목표 1]"
    - "[핵심 학습 목표 2]"
  
  cognitive_skills:
    - analysis: "[분석 관련 스킬]"
    - creativity: "[창의 관련 스킬]"
    - collaboration: "[협업 관련 스킬]"
    - reflection: "[성찰 관련 스킬]"
  
  ai_skills:
    - "[AI 도구 활용 스킬 1]"
    - "[AI 도구 활용 스킬 2]"
    - "[AI 도구 활용 스킬 3]"

expected_outputs:
  - type: "[산출물 유형]"
    description: "[구체적 설명]"
    quality_criteria:
      - "[품질 기준 1]"
      - "[품질 기준 2]"
```

### 선수 조건 및 연계
```yaml
prerequisites:
  required:
    - module_id: "S[X]-A[Y]"
      reason: "[왜 필요한지]"
  
  recommended:
    - module_id: "S[X]-A[Y]"
      reason: "[왜 도움되는지]"
  
  knowledge:
    - "[필요한 사전 지식 1]"
    - "[필요한 사전 지식 2]"

next_modules:
  natural_progression:
    - module_id: "S[X+1]-A[Y]"
      reason: "[자연스러운 진행 이유]"
  
  complementary:
    - module_id: "S[X]-A[Y+1]"
      reason: "[보완적 학습 이유]"
  
  advanced:
    - module_id: "S[X+2]-A[Y]"
      reason: "[심화 학습 경로]"
```

---

## 💬 AI 프롬프트 설계

### 학습자용 프롬프트 패턴
```yaml
prompt_patterns:
  beginner_level:
    - pattern: "[기초 수준 프롬프트 패턴]"
      example: "[구체적 예시]"
      cognitive_focus: "[인지적 초점]"
  
  intermediate_level:
    - pattern: "[중급 수준 프롬프트 패턴]"
      example: "[구체적 예시]"
      cognitive_focus: "[인지적 초점]"
  
  advanced_level:
    - pattern: "[고급 수준 프롬프트 패턴]"
      example: "[구체적 예시]"
      cognitive_focus: "[인지적 초점]"

prompt_progression:
  step1:
    purpose: "[첫 단계 목적]"
    prompt_type: "[질문 유형]"
    expected_response: "[기대 응답 유형]"
  
  step2:
    purpose: "[두 번째 단계 목적]"
    prompt_type: "[질문 유형]"
    expected_response: "[기대 응답 유형]"
  
  step3:
    purpose: "[세 번째 단계 목적]"
    prompt_type: "[질문 유형]"
    expected_response: "[기대 응답 유형]"
```

### AI 시스템 프롬프트
```yaml
ai_system_prompts:
  module_context: |
    당신은 [모듈명] 학습을 돕는 AI 조교입니다.
    학습자가 [단계-인지축]의 목표를 달성하도록 도와주세요.
    
    핵심 원칙:
    - [원칙 1]
    - [원칙 2]
    - [원칙 3]
  
  response_guidelines:
    - "[응답 가이드라인 1]"
    - "[응답 가이드라인 2]"
    - "[응답 가이드라인 3]"
  
  stage_specific:
    exploration: "[탐색 단계 가이드]"
    development: "[발전 단계 가이드]"
    integration: "[통합 단계 가이드]"
```

---

## ✅ 평가 및 체크포인트

### 진행 체크포인트
```yaml
checkpoints:
  - time: "5min"
    indicator: "[5분 시점 확인 지표]"
    success_criteria: "[성공 기준]"
    intervention_needed_if: "[개입 필요 상황]"
  
  - time: "15min"
    indicator: "[15분 시점 확인 지표]"
    success_criteria: "[성공 기준]"
    intervention_needed_if: "[개입 필요 상황]"
  
  - time: "25min"
    indicator: "[25분 시점 확인 지표]"
    success_criteria: "[성공 기준]"
    intervention_needed_if: "[개입 필요 상황]"
```

### 평가 루브릭
```yaml
assessment_rubric:
  dimension_1:  # 예: AI 활용 능력
    L1: "[초급 수준 설명]"
    L2: "[초중급 수준 설명]"
    L3: "[중급 수준 설명]"
    L4: "[중고급 수준 설명]"
    L5: "[고급 수준 설명]"
  
  dimension_2:  # 예: 인지적 복잡도
    L1: "[초급 수준 설명]"
    L2: "[초중급 수준 설명]"
    L3: "[중급 수준 설명]"
    L4: "[중고급 수준 설명]"
    L5: "[고급 수준 설명]"
  
  dimension_3:  # 예: 산출물 품질
    L1: "[초급 수준 설명]"
    L2: "[초중급 수준 설명]"
    L3: "[중급 수준 설명]"
    L4: "[중고급 수준 설명]"
    L5: "[고급 수준 설명]"
```

---

## 🎓 교수 전략

### 난이도 조절
```yaml
difficulty_adjustment:
  make_easier:
    - "[쉽게 만드는 방법 1]"
    - "[쉽게 만드는 방법 2]"
    - "[쉽게 만드는 방법 3]"
  
  make_harder:
    - "[어렵게 만드는 방법 1]"
    - "[어렵게 만드는 방법 2]"
    - "[어렵게 만드는 방법 3]"
  
  personalization:
    - "[개인화 방법 1]"
    - "[개인화 방법 2]"
```

### 일반적인 어려움과 해결책
```yaml
common_challenges:
  - challenge: "[자주 발생하는 어려움 1]"
    signs: "[이런 신호가 보이면]"
    intervention: "[이렇게 개입]"
    prevention: "[예방 방법]"
  
  - challenge: "[자주 발생하는 어려움 2]"
    signs: "[이런 신호가 보이면]"
    intervention: "[이렇게 개입]"
    prevention: "[예방 방법]"
```

---

## 🔗 조합 가이드

### 효과적인 조합
```yaml
effective_combinations:
  - modules: ["S[X]-A[Y]", "S[X]-A[Y]", "S[X]-A[Y]"]
    purpose: "[이 조합의 목적]"
    total_duration: 35
    target_audience: "[적합한 대상]"
    expected_outcome: "[기대 결과]"
  
  - modules: ["S[X]-A[Y]", "S[X]-A[Y]"]
    purpose: "[이 조합의 목적]"
    total_duration: 35
    target_audience: "[적합한 대상]"
    expected_outcome: "[기대 결과]"
```

### 비추천 조합
```yaml
avoid_combinations:
  - modules: ["S[X]-A[Y]", "S[X]-A[Y]"]
    reason: "[피해야 하는 이유]"
    alternative: "[대안 조합]"
```

---

## 📊 데이터 수집

### 학습 데이터 포인트
```yaml
data_collection_points:
  quantitative:
    - metric: "prompt_count"
      description: "생성한 프롬프트 수"
      expected_range: [5, 15]
    
    - metric: "revision_count"
      description: "프롬프트 수정 횟수"
      expected_range: [1, 5]
    
    - metric: "time_to_first_success"
      description: "첫 유의미한 결과까지 시간"
      expected_range: [5, 15]
  
  qualitative:
    - aspect: "prompt_evolution"
      description: "프롬프트 품질 변화"
      indicators: ["구체성", "맥락성", "목적성"]
    
    - aspect: "cognitive_engagement"
      description: "인지적 참여도"
      indicators: ["질문 깊이", "연결성", "창의성"]
```

---

## 📝 모듈 메타데이터 예시: S2-A1

```yaml
module_id: "S2-A1"
module_name: "목적 명확화 × 분석"
stage: 
  number: 2
  name: "목적 명확화"
  focus: "해결하고자 하는 문제나 달성하고자 하는 목표 정의"
cognitive_axis:
  number: 1
  name: "A1-분석"
  focus: "논리적 사고와 구조화 능력"

difficulty_range:
  min: L1
  max: L5
  sweet_spot: L3

typical_duration:
  standalone: 35
  as_part: 10

description: |
  학습자가 자신의 목적을 명확히 정의하고, 
  이를 달성하기 위한 요구사항을 분석하는 방법을 
  AI와의 대화를 통해 체계적으로 학습합니다.

learning_objectives:
  primary:
    - "막연한 목적을 구체적이고 측정 가능한 목표로 전환"
    - "목표 달성을 위한 핵심 요소 도출 및 우선순위 설정"
  
  cognitive_skills:
    - analysis: "목적-수단 분석, 요구사항 분해"
    - creativity: "다양한 관점에서 목적 재정의"
    - collaboration: "이해관계자 요구 통합"
    - reflection: "목적의 타당성 검토"
  
  ai_skills:
    - "목적 구체화를 위한 단계적 질문 기법"
    - "SMART 목표 설정을 위한 프롬프트 작성"
    - "제약조건과 요구사항 명확화 대화법"

# ... (나머지 섹션도 실제 내용으로 채워짐)
```

---

**템플릿 버전**: v1.0
**작성일**: 2025-08-15
**작성자**: PM Claude
**용도**: 32개 모듈 메타데이터 작성 가이드

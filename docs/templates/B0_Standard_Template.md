# B0 표준 수업 템플릿 (이중 구조)

## 📋 템플릿 개요
- **버전**: v1.0
- **작성일**: 2025-08-15
- **용도**: IWL v5.0 모든 수업의 표준 템플릿
- **특징**: Frontend/Backend 이중 구조

---

## 🎯 Frontend View (학습자용)

### 오늘의 목표
> **"[실제 상황] 때문에 [구체적 목표]를 달성하고 싶으신가요? 
> 35분 안에 AI와 함께 [산출물]을 만들어봅시다!"**

예시:
- "상사를 설득할 기술 도입 제안서를 만들어봅시다"
- "과제 주제를 정하고 리서치 계획을 세워봅시다"
- "팀 프로젝트 보고서 구조를 잡아봅시다"

### 준비물
- [ ] AI 챗봇 (ChatGPT/Claude/Gemini)
- [ ] 노트북/태블릿/스마트폰
- [ ] 35분의 집중 시간

### 수업 진행 (35분)

#### 🚀 시작하기 (5분)
1. **목표 확인**: 오늘 만들 결과물 예시 보기
2. **AI 준비**: 챗봇 열고 새 대화 시작
3. **첫 질문**: "저는 [상황]인데, [목표]를 하고 싶습니다"

#### 💡 함께 만들기 (25분)

**Step 1: 기초 질문 (8분)**
```
💬 이렇게 질문해보세요:
"[목표]를 위해 어떤 정보가 필요할까요?"
"[대상]이 가장 관심 있어할 포인트는 무엇일까요?"
```

**Step 2: 구체화하기 (9분)**
```
💬 이렇게 발전시켜보세요:
"제가 준비한 내용은 [A, B, C]인데, 어떤 순서로 구성하면 좋을까요?"
"[특정 부분]을 더 설득력 있게 만들려면?"
```

**Step 3: 완성하기 (8분)**
```
💬 마무리 질문:
"전체 내용을 1페이지로 요약해주세요"
"상대방 입장에서 예상 질문 3개를 뽑아주세요"
```

#### ✅ 마무리 (5분)
- 완성된 결과물 검토
- AI와의 대화 저장
- 다음에 시도할 질문 메모

### 🎁 오늘의 성과
- [ ] [산출물] 완성
- [ ] 효과적인 AI 질문 3개 이상 경험
- [ ] 다음 단계 액션 플랜 수립

---

## 🔧 Backend View (서비스 제공자용)

### 수업 메타데이터
```yaml
lesson_id: B0-[YYYYMMDD]-[###]
title: "[수업 제목]"
type: "[단일모듈/인지축시리즈/목적별조합]"
duration: 35
level: [L1-L5]
target_audience: [Junior/Youth/Pro]

modules_used:
  - module_id: "S[1-8]-A[1-4]"
    weight: 0.4  # 시간 비중
    focus: "primary"
  - module_id: "S[1-8]-A[1-4]"
    weight: 0.3
    focus: "secondary"
  - module_id: "S[1-8]-A[1-4]"
    weight: 0.3
    focus: "support"

cognitive_objectives:
  primary_axis: 
    name: "[A1분석/A2창의/A3협업/A4성찰]"
    level: [1-5]
    specific_goals:
      - "[구체적 인지 목표 1]"
      - "[구체적 인지 목표 2]"
  
  secondary_axes:
    - name: "[보조 인지축]"
      level: [1-5]
      integration_point: "[어느 단계에서 통합]"

ai_interaction_design:
  total_prompts: [8-12]
  prompt_sequence:
    - stage: "초기 탐색"
      count: 2-3
      cognitive_load: "low"
      example_patterns:
        - "정보 수집형 질문"
        - "개방형 브레인스토밍"
    
    - stage: "심화 분석"
      count: 3-4
      cognitive_load: "medium"
      example_patterns:
        - "구조화 요청"
        - "비교 분석"
        - "가설 검증"
    
    - stage: "통합 생성"
      count: 3-5
      cognitive_load: "high"
      example_patterns:
        - "종합 요청"
        - "창의적 변형"
        - "비판적 검토"

measurement_checkpoints:
  - time: "10min"
    indicator: "첫 유의미한 AI 응답 생성"
    success_criteria: "목표와 연관된 구체적 정보 획득"
  
  - time: "20min"
    indicator: "중간 산출물 형태 구성"
    success_criteria: "전체 구조의 50% 이상 완성"
  
  - time: "30min"
    indicator: "최종 산출물 초안"
    success_criteria: "실용 가능한 수준의 결과물"

alternative_paths:
  if_too_easy:
    - "추가 제약 조건 부여"
    - "품질 기준 상향"
    - "복합 시나리오 도입"
  
  if_too_hard:
    - "단계별 스캐폴딩 제공"
    - "예시 프롬프트 직접 제시"
    - "목표 범위 축소"

facilitation_notes:
  do:
    - "학습자가 직접 질문 만들도록 유도"
    - "실패한 프롬프트도 학습 기회로 활용"
    - "개인화된 맥락 장려"
  
  dont:
    - "정답 프롬프트 직접 제시"
    - "이론적 설명으로 시작"
    - "AI 도구 기능 설명에 시간 소비"

data_collection:
  - prompt_quality_score: "[1-5]"
  - output_relevance: "[1-5]"
  - cognitive_achievement: "[인지축별 1-5]"
  - time_efficiency: "[계획 대비 실제]"
  - learner_satisfaction: "[1-5]"
```

### AI 프롬프트 시퀀스 (강사용)

#### 사전 준비 프롬프트
```
당신은 IWL v5.0 수업의 AI 조교입니다.
오늘 수업 정보:
- 모듈: [선택된 모듈들]
- 학습자 수준: [L1-L5]
- 목표 산출물: [구체적 산출물]
- 시간: 35분

학습자가 질문할 때마다:
1. 인지 발달 단계 확인
2. 다음 단계로 유도하는 응답
3. 구체적 예시 포함
4. 추가 질문 유도
```

#### 단계별 지원 프롬프트
```yaml
stage_1_exploration:
  system: "학습자가 탐색 단계입니다. 
          정보를 구조화하여 제시하되, 
          다음 질문을 유도하세요."
  
  response_template: |
    [요청하신 정보]를 정리하면:
    1. [핵심 포인트 1]
    2. [핵심 포인트 2]
    3. [핵심 포인트 3]
    
    🤔 다음으로 고려하면 좋을 점:
    - [심화 질문 유도 1]
    - [심화 질문 유도 2]

stage_2_analysis:
  system: "학습자가 분석 단계입니다.
          비교, 평가, 구조화를 돕되,
          스스로 판단하도록 유도하세요."

stage_3_creation:
  system: "학습자가 생성 단계입니다.
          통합적 사고와 창의성을 자극하되,
          실용성을 놓치지 않도록 하세요."
```

### 평가 루브릭

| 요소 | L1 (초급) | L3 (중급) | L5 (고급) |
|------|-----------|-----------|-----------|
| AI 질문 품질 | 단순 정보 요청 | 구조화된 요청 | 복합적 사고 요청 |
| 인지 복잡도 | 단일 축 활용 | 2개 축 통합 | 3-4개 축 자유 활용 |
| 산출물 수준 | 기본 템플릿 완성 | 맥락화된 결과물 | 창의적 변형 포함 |
| 자율성 | 안내 따라가기 | 부분적 자기 주도 | 완전 자기 주도 |

---

## 📊 데이터 수집 포맷

### 수업 후 기록 (JSON)
```json
{
  "session_id": "B0-20250815-001",
  "timestamp": "2025-08-15T14:35:00Z",
  "modules_completed": ["S2-A1", "S4-A3"],
  "actual_duration": 35,
  "prompts_generated": 10,
  "quality_scores": {
    "prompt_quality": 4,
    "output_relevance": 5,
    "cognitive_goals": {
      "analysis": 4,
      "creativity": 3
    }
  },
  "learner_feedback": "실용적이고 즉시 활용 가능했음",
  "instructor_notes": "초반 진입 장벽 있었으나 중반부터 몰입",
  "recommended_next": ["S5-A2", "S6-A3"]
}
```

---

## 🔄 템플릿 활용 가이드

### 1. 수업 설계 시
1. 학습자 페르소나 설정
2. 목표 산출물 명확화
3. 모듈 조합 선택 (AI 추천 활용)
4. Frontend 내용 커스터마이징
5. Backend 측정 지표 설정

### 2. 수업 진행 시
1. Frontend만 학습자에게 공유
2. Backend로 진행 상황 모니터링
3. 체크포인트별 개입 여부 판단
4. 대안 경로 준비

### 3. 수업 후
1. 데이터 수집 및 기록
2. 학습자 피드백 수집
3. 다음 모듈 추천
4. 템플릿 개선사항 기록

---

**템플릿 버전**: v1.0
**최종 수정**: 2025-08-15
**작성자**: PM Claude
**검토 필요**: Thomas


# 📋 8×4 매트릭스 모듈 설계 템플릿 v2.0
*S1-A1, S1-A2 기준으로 통일된 템플릿*

---

## 🎯 모듈 메타데이터

```yaml
module_id: "S[1-8]-A[1-4]"
module_name: "[핵심 개념]"
stage: [1-8]
axis: [1-4]
korean_name: "[단계명] × [축명]"
english_name: "[Stage] × [Axis]"
core_concept: "[핵심 개념 한 단어]"
estimated_time: 
  standalone: "10-15분"
  as_part_of_integration: "5-7분"
```

---

## 📊 레벨별 상세 설계

### L1 (초급) - 완전 초보자

#### 메타데이터
```yaml
level: 1
target_audience: "AI 도구 첫 사용자"
duration: "5분"
difficulty: "very_easy"
```

#### 학습 목표 (숨김)
- [초급 목표 1]
- [초급 목표 2]
- [초급 목표 3]

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "[사용자 지시사항]"
    user_action: "[사용자 행동]"
    time: "30초"
    
  - step: 2
    instruction: "[다음 지시사항]"
    ai_prompt: "[AI가 제시할 프롬프트]"
    expected_response_type: "[기대 응답 유형]"
    time: "1분"
    
  # ... 총 5개 스텝
```

#### AI 응답 가이드
```yaml
ai_behavior:
  tone: "[대화 톤]"
  avoid: 
    - "[피해야 할 것 1]"
    - "[피해야 할 것 2]"
  encourage:
    - "[격려할 것 1]"
    - "[격려할 것 2]"
    
sample_responses:
  good: "[좋은 응답 예시]"
  redirect: "[방향 전환 응답]"
```

#### 체크포인트
```yaml
success_indicators:
  - "[성공 지표 1]"
  - "[성공 지표 2]"
  - "[성공 지표 3]"
completion_criteria: "[완료 기준]"
```

---

### L3 (중급) - 기초 학습자

#### 메타데이터
```yaml
level: 3
target_audience: "디지털 도구 기본 사용 가능자"
duration: "7-8분"
difficulty: "moderate"
```

#### 학습 목표 (숨김)
- [중급 목표 1]
- [중급 목표 2]
- [중급 목표 3]

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "[복잡한 지시사항]"
    setup: "[환경 설정]"
    time: "30초"
    
  - step: 2
    instruction: "[다음 지시사항]"
    ai_prompt: "[더 복잡한 프롬프트]"
    cognitive_load: "중간"
    time: "2분"
    
  # ... 총 5개 스텝
```

#### AI 응답 가이드
```yaml
ai_behavior:
  complexity: "중간"
  focus:
    - "[중점 사항 1]"
    - "[중점 사항 2]"
  avoid:
    - "[피해야 할 것]"
    
sample_responses:
  encouraging: "[격려 응답]"
  challenging: "[도전적 응답]"
```

---

### L5 (고급) - 전문가 수준

#### 메타데이터
```yaml
level: 5
target_audience: "[전문가 대상]"
duration: "10-12분"
difficulty: "advanced"
```

#### 학습 목표 (숨김)
- [고급 목표 1]
- [고급 목표 2]
- [고급 목표 3]

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "[고난도 지시]"
    setup: "[복잡한 설정]"
    time: "1분"
    
  - step: 2
    instruction: "[심화 활동]"
    ai_prompt: "[추상적/창의적 프롬프트]"
    advanced_feature: true
    time: "2분"
    
  # ... 총 5개 스텝
```

#### AI 응답 가이드
```yaml
ai_behavior:
  sophistication: "높음"
  focus:
    - "[고급 초점 1]"
    - "[고급 초점 2]"
  language:
    - "[전문 용어]"
    - "[고급 표현]"
    
sample_responses:
  deep: "[깊이 있는 응답]"
  challenging: "[도전적 응답]"
```

---

## 🔄 타 모듈과의 연계

### 선행 모듈
- **[이전 모듈]**: [관계 설명]

### 후행 모듈
- **[다음 모듈]**: [관계 설명]

### 통합 프로그램에서의 역할
- [프로그램 내 역할]
- [다른 모듈과의 시너지]
- [전체 흐름에서의 위치]

---

## 💻 구현 가이드

### 프론트엔드 요구사항
```yaml
ui_elements:
  - [UI 요소 1]: "[설명]"
  - [UI 요소 2]: "[설명]"
  - [UI 요소 3]: "[설명]"
  
interaction_design:
  - [인터랙션 1]: "[설명]"
  - [인터랙션 2]: "[설명]"
```

### 백엔드 데이터
```yaml
tracking_data:
  - [데이터 1]: "[설명]"
  - [데이터 2]: "[설명]"
  - [데이터 3]: "[설명]"
  
analytics:
  - [분석 1]: "[설명]"
  - [분석 2]: "[설명]"
```

### AI 프롬프트 템플릿
```javascript
const S[X]_A[Y]_PROMPT = {
  system: `[시스템 프롬프트]`,
  
  level_adjustments: {
    L1: "[L1 조정]",
    L3: "[L3 조정]",
    L5: "[L5 조정]"
  }
}
```

---

## 📱 실제 화면 흐름

### 시작 화면
```
[아이콘] [모듈명]
"[한 줄 소개]"
[시작하기]
```

### 진행 화면
```
[진행 바: ■■□□□ 40%]
[남은 시간: 3:24]

💡 [현재 지시사항]

[AI 채팅창]
AI: [AI 메시지]
나: [사용자 입력]
```

### 완료 화면
```
✅ [모듈명] 완료!

오늘의 [성과]:
- [측정 항목 1]: [수치]
- [측정 항목 2]: [수치]
- 다음 추천: [다음 모듈]

[다음으로] [다시하기]
```

---

## 🎭 S[X]-A[Y]의 본질

### 핵심 철학
> "[이 모듈의 핵심 철학 한 문장]"

- [철학적 포인트 1]
- [철학적 포인트 2]
- [철학적 포인트 3]

### 체화의 증거
- [체화 증거 1]
- [체화 증거 2]
- [체화 증거 3]

---

**설계일**: 2025-08-XX
**설계자**: Thomas & PM Claude
**상태**: [구현 준비 완료/설계 중/검토 필요]
**다음 단계**: [다음 작업]
# 📋 S1-A2 모듈 설계서
*실제 구현을 위한 상세 스펙*

---

## 🎯 모듈 메타데이터

```yaml
module_id: "S1-A2"
module_name: "즉각적 반응"
stage: 1
axis: 2
korean_name: "지각인지 × 사고조작방식"
english_name: "Perceptual Cognition × Thinking Manipulation"
core_concept: "수동적 반응"
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
- 생각하기 전에 반응하기
- 직관적 첫 인상 포착
- 계획 없는 즉흥성 경험

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "AI와 단어 연상 게임을 시작합니다"
    user_action: "준비 자세"
    time: "30초"
    
  - step: 2
    instruction: "AI가 단어를 제시하면 1초 안에 떠오르는 것을 말하세요"
    ai_prompt: "사과"
    expected_response_type: "즉각 연상 (예: 빨강, 과일, 맛있다)"
    time: "1분"
    
  - step: 3
    instruction: "조금 더 빠르게 반응해보세요"
    ai_prompt: "하늘, 책상, 커피"
    expected_response_type: "연속 즉답"
    time: "1분"
    
  - step: 4
    instruction: "이번엔 이미지를 보고 첫 느낌을 말해보세요"
    ai_prompt: "[간단한 도형 제시]"
    expected_response_type: "감각적 반응"
    time: "1분"
    
  - step: 5
    instruction: "마지막으로 AI의 질문에 바로 답해보세요"
    ai_prompt: "지금 기분은?"
    expected_response_type: "즉각적 상태 표현"
    time: "1.5분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  tone: "경쾌하고 리듬감 있게"
  avoid: 
    - "왜 그렇게 생각했나요?"
    - "다시 생각해보세요"
    - "정답/오답 판단"
  encourage:
    - "빠른 반응 칭찬"
    - "망설임 없애기"
    - "즉흥성 격려"
    
sample_responses:
  good: "좋아요! 바로 그거예요. 다음!"
  redirect: "생각하지 말고 바로 말해보세요!"
```

#### 체크포인트
```yaml
success_indicators:
  - "반응 시간 1-2초 이내"
  - "수정하지 않고 첫 답변 유지"
  - "점점 빨라지는 반응 속도"
completion_criteria: "10회 이상 즉각 반응 성공"
```

---

### L3 (중급) - 기초 학습자

#### 메타데이터
```yaml
level: 3
target_audience: "기본 디지털 도구 사용자"
duration: "7-8분"
difficulty: "moderate"
```

#### 학습 목표 (숨김)
- 복잡한 자극에도 즉각 반응
- 연쇄 반응의 흐름 유지
- 무의식적 패턴 발현

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "AI와 스토리 이어가기를 합니다"
    setup: "한 문장씩 번갈아 가며"
    time: "30초"
    
  - step: 2
    instruction: "AI가 시작하면 바로 이어서 한 문장 추가"
    ai_prompt: "어느 날 아침, 창문을 열자..."
    cognitive_load: "중간"
    time: "2분"
    
  - step: 3
    instruction: "감정 표현 즉흥 게임"
    ai_prompt: "기쁨을 색으로 표현하면?"
    emotion_reaction: true
    time: "2분"
    
  - step: 4
    instruction: "빠른 선택 게임"
    ai_prompt: "A 또는 B? 산 또는 바다? 아침 또는 저녁?"
    binary_choices: true
    time: "2분"
    
  - step: 5
    instruction: "연속 연상 체인"
    ai_prompt: "나무 → [당신] → [AI] → [당신]..."
    chain_reaction: true
    time: "1.5분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  complexity: "중간"
  focus:
    - "흐름 유지"
    - "리듬감 생성"
    - "자연스러운 연결"
  avoid:
    - "논리적 설명 요구"
    - "일관성 강요"
    
sample_responses:
  flow: "그 느낌 그대로 이어가세요!"
  encouragement: "망설이지 말고 계속!"
```

---

### L5 (고급) - 전문가 수준

#### 메타데이터
```yaml
level: 5
target_audience: "창의적 전문가, 즉흥 예술가"
duration: "10-12분"
difficulty: "advanced"
```

#### 학습 목표 (숨김)
- 복합 자극 동시 반응
- 무의식과 의식의 경계
- 창발적 즉흥성

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "다중 모드 즉흥 반응"
    setup: "시각, 청각, 감정 동시 자극"
    time: "1분"
    
  - step: 2
    instruction: "추상 개념 즉흥 변환"
    ai_prompt: "자유를 움직임으로, 시간을 색으로"
    abstract_conversion: true
    time: "2분"
    
  - step: 3
    instruction: "역설적 즉답"
    ai_prompt: "뜨거운 얼음? 밝은 어둠?"
    paradox_response: true
    time: "2분"
    
  - step: 4
    instruction: "감각 전이 반응"
    ai_prompt: "이 소리의 맛은? 이 색의 온도는?"
    synesthesia: true
    time: "2분"
    
  - step: 5
    instruction: "무의식 스트림"
    ai_prompt: "눈을 감고 떠오르는 대로 1분간..."
    stream_consciousness: true
    time: "3분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  sophistication: "높음"
  focus:
    - "창발성 포착"
    - "무의식 존중"
    - "흐름 상태 유지"
  language:
    - "시적 표현"
    - "은유적 반응"
    - "열린 해석"
    
sample_responses:
  deep: "그 순간의 섬광을 잡았네요"
  flow: "무의식이 춤추고 있어요"
```

---

## 🔄 타 모듈과의 연계

### S1-A1과의 차이
- A1: 있는 그대로 관찰 (정적)
- A2: 즉각적으로 반응 (동적)

### 후행 모듈
- **S1-A3**: 구체적 표현으로 전환
- **S2-A2**: 의미 있는 연결로 발전

### 통합 프로그램에서의 역할
- A1에서 열린 감각의 문을 통해
- A2에서 활발한 상호작용 시작
- 정적 관찰에서 동적 참여로 전환

---

## 💻 구현 가이드

### 프론트엔드 요구사항
```yaml
ui_elements:
  - rapid_input: "빠른 입력 인터페이스"
  - visual_feedback: "즉각적 시각 피드백"
  - timer_display: "반응 시간 표시"
  - flow_indicator: "흐름 상태 시각화"
  
interaction_design:
  - minimal_latency: "최소 지연"
  - smooth_transitions: "부드러운 전환"
  - rhythm_keeper: "리듬 유지 장치"
```

### 백엔드 데이터
```yaml
tracking_data:
  - response_time: "각 반응 시간 (ms)"
  - hesitation_count: "망설임 횟수"
  - flow_duration: "몰입 구간 길이"
  - pattern_emergence: "반복 패턴 출현"
  
analytics:
  - average_response_time: "평균 반응 시간"
  - improvement_rate: "속도 향상률"
  - creativity_index: "창의성 지수"
```

### AI 프롬프트 템플릿
```javascript
const S1_A2_PROMPT = {
  system: `당신은 즉흥성을 이끌어내는 파트너입니다.
참여자가 생각하지 않고 바로 반응하도록 도와주세요.
빠른 템포를 유지하고, 망설임을 부드럽게 해소시켜주세요.`,
  
  level_adjustments: {
    L1: "단순하고 명확한 자극, 격려 중심",
    L3: "연속성과 흐름 강조, 복잡도 증가",
    L5: "추상적이고 창의적인 도전"
  }
}
```

---

## 📱 실제 화면 흐름

### 시작 화면
```
⚡ 즉각적 반응 훈련
"생각하지 말고 느끼세요"
[시작하기]
```

### 진행 화면
```
[반응 시간: 0.8초]
[현재 속도: 🔥🔥🔥]

AI: "바다"
나: "파랑" (0.6초)
AI: "좋아요! 다음, 아침"
나: _
```

### 완료 화면
```
⚡ 즉흥 반응 완료!

오늘의 기록:
- 평균 반응: 1.2초
- 최고 속도: 0.4초
- 흐름 상태: 3분 지속

[다음: S1-A3 구체화] [다시하기]
```

---

## 🎭 S1-A2의 본질

### 핵심 철학
> "생각이 개입하기 전의 순수한 반응"

- 의식의 검열 이전 포착
- 무의식과의 첫 만남
- 즉흥성의 순수한 기쁨

### 체화의 증거
- 반응 시간 단축
- 자연스러운 연상 흐름
- 망설임 없는 표현
- 놀이같은 즐거움

---

**설계일**: 2025-08-16
**설계자**: Thomas & PM Claude
**상태**: 구현 준비 완료
**다음 단계**: S1-A3 모듈 설계
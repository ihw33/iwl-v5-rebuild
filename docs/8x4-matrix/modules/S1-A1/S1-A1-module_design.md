# 📋 S1-A1 모듈 설계서
*실제 구현을 위한 상세 스펙*

---

## 🎯 모듈 메타데이터

```yaml
module_id: "S1-A1"
module_name: "순수한 관찰"
stage: 1
axis: 1
korean_name: "지각인지 × 정보처리깊이"
english_name: "Perceptual Cognition × Information Processing Depth"
core_concept: "감각적 수용"
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
- 판단 없이 보는 경험
- 단순 관찰 능력 활성화
- AI와의 첫 상호작용

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "ChatGPT 화면을 열어주세요"
    user_action: "화면 열기"
    time: "30초"
    
  - step: 2
    instruction: "화면을 천천히 둘러보세요. 무엇이 보이나요?"
    ai_prompt: "화면에서 가장 먼저 눈에 들어오는 것은 무엇인가요? 색깔이나 모양을 말해주세요."
    expected_response_type: "단순 관찰 (예: 파란색 버튼, 흰 배경)"
    time: "1분"
    
  - step: 3
    instruction: "이번엔 더 자세히 봐주세요"
    ai_prompt: "입력창은 어디에 있나요? 어떤 모양인가요?"
    expected_response_type: "위치와 형태 설명"
    time: "1분"
    
  - step: 4
    instruction: "색깔에 집중해보세요"
    ai_prompt: "화면에서 볼 수 있는 색깔을 모두 말해주세요"
    expected_response_type: "색상 나열"
    time: "1분"
    
  - step: 5
    instruction: "크기를 비교해보세요"
    ai_prompt: "가장 큰 요소와 가장 작은 요소는 무엇인가요?"
    expected_response_type: "상대적 크기 비교"
    time: "1.5분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  tone: "친근하고 격려적"
  avoid: 
    - "분석적 해석"
    - "기능 설명"
    - "판단이나 평가"
  encourage:
    - "있는 그대로 표현"
    - "감각적 언어 사용"
    - "단순한 관찰"
    
sample_responses:
  good: "네, 파란색 버튼이 보이시는군요! 또 무엇이 보이나요?"
  redirect: "버튼의 기능보다는, 그냥 어떻게 생겼는지 말해주세요."
```

#### 체크포인트
```yaml
success_indicators:
  - "판단 언어 사용 안 함 (좋다/나쁘다)"
  - "기능 언급 안 함 (이건 ~하는 버튼)"
  - "순수 관찰 언어 사용 (크다/작다/파랗다)"
completion_criteria: "5개 이상의 시각적 요소 관찰"
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
- 동시 다발적 관찰
- 세부사항 인지
- 공간적 관계 파악

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "복잡한 웹사이트나 앱을 열어주세요"
    examples: ["온라인 쇼핑몰", "뉴스 사이트", "소셜 미디어"]
    time: "30초"
    
  - step: 2
    instruction: "3초간 화면을 본 후 눈을 감으세요"
    ai_prompt: "방금 본 화면에서 기억나는 것을 모두 말해주세요"
    cognitive_load: "중간"
    time: "2분"
    
  - step: 3
    instruction: "다시 화면을 보면서 위치를 설명해주세요"
    ai_prompt: "화면을 9개 구역으로 나눈다면, 각 구역에 무엇이 있나요?"
    spatial_awareness: true
    time: "2분"
    
  - step: 4
    instruction: "시각적 계층을 관찰해주세요"
    ai_prompt: "가장 눈에 띄는 것부터 순서대로 5개만 말해주세요"
    visual_hierarchy: true
    time: "2분"
    
  - step: 5
    instruction: "색상과 대비를 관찰해주세요"
    ai_prompt: "어떤 색상 조합이 사용되었나요? 대비가 강한 부분은?"
    advanced_observation: true
    time: "1.5분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  complexity: "중간"
  focus:
    - "동시성 인정"
    - "공간 관계"
    - "시각적 패턴"
  avoid:
    - "UX 분석"
    - "디자인 평가"
    
sample_responses:
  spatial: "왼쪽 상단에는 무엇이, 중앙에는 무엇이 보이시나요?"
  hierarchy: "네, 큰 이미지가 먼저 보이셨군요. 그 다음은요?"
```

---

### L5 (고급) - 전문가 수준

#### 메타데이터
```yaml
level: 5
target_audience: "디자인/개발 전문가, 고도 관찰력 보유자"
duration: "10-12분"
difficulty: "advanced"
```

#### 학습 목표 (숨김)
- 미세한 차이 감지
- 무의식적 디자인 요소 인지
- 감각의 극한 활용

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "비슷한 서비스 3개를 동시에 열어주세요"
    setup: "나란히 배치 또는 빠른 전환 가능"
    time: "1분"
    
  - step: 2
    instruction: "미세한 차이에 집중하세요"
    ai_prompt: "세 화면의 여백(padding/margin) 차이가 느껴지나요?"
    micro_observation: true
    time: "2분"
    
  - step: 3
    instruction: "그림자와 깊이감을 관찰하세요"
    ai_prompt: "어떤 요소에 그림자가 있고, 깊이감은 어떻게 표현되었나요?"
    depth_perception: true
    time: "2분"
    
  - step: 4
    instruction: "움직임과 전환을 포착하세요"
    ai_prompt: "호버 효과나 마이크로 인터랙션을 발견하셨나요?"
    motion_detection: true
    time: "2분"
    
  - step: 5
    instruction: "보이지 않는 것을 인지하세요"
    ai_prompt: "의도적으로 비워둔 공간이나 생략된 요소가 있나요?"
    negative_space: true
    time: "3분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  sophistication: "높음"
  focus:
    - "극미세 차이"
    - "의도된 부재"
    - "감각의 한계"
  language:
    - "픽셀 단위"
    - "밀리초 단위"
    - "그라데이션"
    
sample_responses:
  micro: "1-2픽셀의 차이도 감지하셨나요?"
  absence: "없음도 디자인입니다. 어떤 부재를 발견하셨나요?"
```

---

## 🔄 타 모듈과의 연계

### 선행 모듈
- 없음 (S1-A1이 가장 기초)

### 후행 모듈
- **S1-A2**: 즉각 반응으로 전환
- **S2-A1**: 의미 파악 시작

### 통합 프로그램에서의 역할
- 전체 프로그램의 "문 열기" 역할
- 참여자의 긴장 완화
- 판단 모드에서 관찰 모드로 전환

---

## 💻 구현 가이드

### 프론트엔드 요구사항
```yaml
ui_elements:
  - instruction_display: "단계별 지시사항"
  - timer: "각 활동 시간 표시"
  - progress_bar: "진행 상황"
  - ai_chat_interface: "AI와 대화"
  
responsive_design:
  - mobile: "세로 모드 최적화"
  - tablet: "분할 화면 지원"
  - desktop: "멀티 윈도우"
```

### 백엔드 데이터
```yaml
tracking_data:
  - observation_count: "관찰 항목 수"
  - abstraction_level: "추상어 사용 빈도"
  - response_time: "반응 시간"
  - completion_rate: "완료율"
  
analytics:
  - common_observations: "자주 관찰되는 요소"
  - difficulty_points: "어려워하는 지점"
  - level_progression: "레벨 이동 패턴"
```

### AI 프롬프트 템플릿
```javascript
const S1_A1_PROMPT = {
  system: `당신은 순수한 관찰을 도와주는 가이드입니다.
참여자가 판단이나 해석 없이 있는 그대로 보도록 도와주세요.
추상적 표현은 피하고, 구체적 관찰을 격려하세요.`,
  
  level_adjustments: {
    L1: "매우 단순하고 명확한 질문만",
    L3: "공간과 관계에 대한 질문 추가",
    L5: "미세한 차이와 부재에 대한 질문"
  }
}
```

---

## 📱 실제 화면 흐름

### 시작 화면
```
🎯 순수한 관찰
"오늘은 AI와 함께 '보는 법'을 연습합니다"
[시작하기]
```

### 진행 화면
```
[진행 바: ■■□□□ 40%]
[남은 시간: 3:24]

💡 화면을 천천히 둘러보세요

[AI 채팅창]
AI: 무엇이 보이나요?
나: 파란색 버튼이 보여요
AI: 좋아요! 그 버튼의 모양은 어떤가요?
```

### 완료 화면
```
✅ 순수한 관찰 완료!

오늘의 관찰:
- 발견한 요소: 12개
- 순수 관찰도: 85%
- 다음 추천: S1-A2 즉각 반응

[다음으로] [다시하기]
```

---

**설계일**: 2025-08-15
**설계자**: Thomas & PM Claude
**상태**: 구현 준비 완료
**다음 단계**: 프론트엔드 개발
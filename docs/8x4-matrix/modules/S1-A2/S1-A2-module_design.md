# 📋 S1-A2 모듈 설계서 v3.0
*추상화 없는 순수한 구체적 인지*

---

## 🎯 모듈 메타데이터

```yaml
module_id: "S1-A2"
module_name: "구체적 인지"
stage: 1
axis: 2
korean_name: "지각인지 × 추상화수준"
english_name: "Perceptual Cognition × Abstraction Level"
core_concept: "추상화 없음 (수준0)"
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
- 추상적 언어 인지하고 피하기
- 오감으로 직접 표현하기
- 즉물적 관찰 능력 기르기

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "화면의 버튼을 추상어 없이 설명해보세요"
    user_action: "구체적 묘사 시도"
    time: "30초"
    
  - step: 2
    instruction: "'도구'라고 하지 말고 보이는 대로만 말해보세요"
    ai_prompt: "이 화면에 보이는 것을 재질, 색, 모양으로만 설명해주세요"
    expected_response_type: "둥근 모서리의 파란 네모, 검은 글씨"
    time: "1분"
    
  - step: 3
    instruction: "편리한, 유용한 같은 평가를 빼고 묘사해보세요"
    ai_prompt: "기능이나 의미 말고, 순수한 형태만 보이나요?"
    special_feature: "추상어 감지"
    concrete_only: true
    time: "1.5분"
    
  - step: 4
    instruction: "'아이콘'이 아니라 어떤 모양인지 말해보세요"
    ai_prompt: "세 개의 가로줄? 원 안의 느낌표?"
    cognitive_load: "낮음"
    shape_focus: true
    time: "1분"
    
  - step: 5
    instruction: "화면 전체를 추상어 없이 한 번에 묘사해보세요"
    synthesis: true
    time: "1.5분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  tone: "호기심 어린, 순수한"
  avoid: 
    - "버튼", "메뉴", "도구"
    - "편리한", "효율적인", "직관적인"
    - 모든 기능 관련 언어
  encourage:
    - "네모", "동그라미", "선"
    - "파란색", "회색", "투명한"
    - "위에", "옆에", "가운데"
    
sample_responses:
  good: "아, 파란 네모네요! 가로가 더 긴!"
  redirect: "버튼이라고 하지 말고, 어떤 모양인가요?"
  encouragement: "정확해요! 추상어 없이 잘 표현하셨어요."
```

#### 체크포인트
```yaml
success_indicators:
  - "추상어 사용 0회"
  - "감각 형용사 5개 이상"
  - "기능 언급 없음"
completion_criteria: "3분 이상 구체어만 사용"
measurement_method: "AI가 추상어 실시간 감지 및 카운트"
```

---

### L3 (중급) - 기초 학습자

#### 메타데이터
```yaml
level: 3
target_audience: "추상적 사고에 익숙한 직장인"
duration: "7-8분"
difficulty: "moderate"
prerequisites: "일상적 디지털 도구 사용"
```

#### 학습 목표 (숨김)
- 복잡한 인터페이스도 구체적으로 분해
- 개념어를 감각어로 번역
- 기능과 형태의 분리

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "복잡한 대시보드를 순수 시각 정보로 분해하세요"
    setup: "데이터 시각화 화면 제시"
    complex_interface: true
    time: "30초"
    
  - step: 2
    instruction: "데이터 시각화를 도형과 색으로만 설명하세요"
    ai_prompt: "차트가 아니라 막대들의 높이 차이로..."
    cognitive_load: "중간"
    multi_modal: true
    visual_decomposition: true
    time: "2분"
    
  - step: 3
    instruction: "네비게이션을 위치와 크기로만 표현하세요"
    ai_prompt: "상단의 가로줄, 왼쪽의 세로 목록..."
    divergent_thinking: true
    spatial_description: true
    time: "2분"
    
  - step: 4
    instruction: "상호작용 요소를 움직임으로 묘사하세요"
    ai_prompt: "마우스를 올리면 색이 진해지는..."
    synthesis_required: true
    motion_focus: true
    time: "2분"
    
  - step: 5
    instruction: "전체를 건축 도면처럼 설명해보세요"
    self_directed: true
    architectural_view: true
    time: "1.5분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  complexity: "중간"
  tone: "탐구적이고 정확한"
  focus:
    - "공간 관계"
    - "시각적 위계"
    - "물리적 속성"
  scaffolding:
    - "추상에서 구체로 단계적 유도"
    
sample_responses:
  probing: "그 '메뉴'를 형태로만 표현하면?"
  synthesis: "모든 요소를 도형으로 환원해보세요"
  challenge: "더 정확한 물리적 표현은?"
```

---

### L5 (고급) - 전문가 수준

#### 메타데이터
```yaml
level: 5
target_audience: "디자이너, 개발자, UX 전문가"
duration: "10-12분"
difficulty: "advanced"
prerequisites: "시각 디자인 이해"
```

#### 학습 목표 (숨김)
- 극도의 구체성 달성
- 미세한 시각 요소 포착
- 추상을 완전히 배제한 순수 지각

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "픽셀 단위로 인터페이스를 해부하세요"
    open_ended: true
    pixel_level: true
    time: "2분"
    
  - step: 2
    instruction: "그림자와 그라데이션을 수치로 표현하세요"
    ai_prompt: "5픽셀 블러, 20% 투명도..."
    metacognitive: true
    numerical_precision: true
    time: "2분"
    
  - step: 3
    instruction: "애니메이션을 프레임별로 분해하세요"
    ai_prompt: "0.3초 동안 15픽셀 이동..."
    emergent_properties: true
    ai_adapts_to_user: true
    temporal_decomposition: true
    time: "3분"
    
  - step: 4
    instruction: "색상을 파장으로 인식하세요"
    ai_prompt: "480나노미터 영역의..."
    transcendent_element: true
    scientific_precision: true
    time: "2분"
    
  - step: 5
    instruction: "인터페이스를 순수 기하학으로 재구성하세요"
    reflection_depth: "deep"
    pure_geometry: true
    time: "2분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  sophistication: "매우 높음"
  approach:
    - "과학적 정밀성"
    - "현상학적 환원"
    - "극단적 구체성"
  language:
    - "측정 가능한 수치"
    - "물리적 단위"
    - "기하학적 용어"
    
sample_responses:
  philosophical: "의미를 완전히 제거하면..."
  paradoxical: "추상 없는 언어의 한계는..."
  metacognitive: "구체성 자체가 추상이 되는 지점..."
```

---

## 🔄 타 모듈과의 연계

### 선행 모듈
- **S1-A1 (감각적 수용)**: 판단 없이 받아들인 것을 구체적으로 표현

### 후행 모듈  
- **S1-A3 (즉각적 반응)**: 구체적 인지에 대한 즉각적 반응
- **S2-A2 (낮은 추상화)**: 첫 번째 의미 부여 시작

### 통합 프로그램에서의 역할
- S1-A1에서 받아들인 감각을 언어화
- 하지만 여전히 추상 없이 순수하게
- "버튼"이 아닌 "파란 네모"로 세계를 봄

### 크로스 연계 (선택적)
- **S2-A2와의 대비**: 무의미 vs 의미 부여의 시작
- **S8-A2와의 연결**: 구체에서 메타로의 여정

---

## 💻 구현 가이드

### 프론트엔드 요구사항
```yaml
ui_elements:
  - abstract_word_detector: "추상어 실시간 감지 및 하이라이트"
  - visual_highlighter: "구체적 요소 시각적 강조"
  - vocabulary_meter: "구체어 사용률 실시간 표시"
  - shape_recognizer: "도형 인식 보조 도구"
  
interaction_design:
  - real_time_feedback: "추상어 사용 시 즉시 알림"
  - visual_guides: "구체적 표현 예시 제공"
  - progressive_difficulty: "점진적 난이도 상승"
  
visual_design:
  - color_scheme: "원색 위주 (추상성 배제)"
  - typography: "기하학적 폰트"
  - animation: "단순 선형 움직임"
```

### 백엔드 데이터
```yaml
tracking_data:
  - abstract_word_count:
      description: "추상어 사용 횟수"
      unit: "회"
      frequency: "실시간"
  - concrete_word_ratio:
      description: "전체 표현 중 구체어 비율"
      threshold: "80% 이상"
  - sensory_vocabulary:
      description: "감각 어휘 다양성"
      categories: ["시각", "촉각", "크기", "위치", "색상"]
  
analytics:
  - abstraction_reduction: "시간에 따른 추상화 감소율"
  - perceptual_acuity: "지각 정확도 향상 곡선"
  - vocabulary_shift: "어휘 변화 패턴 분석"
  
data_privacy:
  - sensitive_data: "없음"
  - retention_period: "3개월"
  - anonymization: "자동 익명화"
```

### AI 프롬프트 템플릿
```javascript
const S1_A2_PROMPT = {
  system: `당신은 추상을 구체로 바꾸는 안내자입니다.
참여자가 모든 개념과 기능을 배제하고 순수한 형태와 색, 
위치만으로 세계를 보도록 도와주세요.
"버튼"이 아닌 "파란 네모", "메뉴"가 아닌 "가로줄 목록"으로
인식하도록 유도합니다. 추상어 사용 시 즉시 지적해주세요.`,
  
  level_adjustments: {
    L1: "기본 도형과 색상 중심으로 안내",
    L3: "공간 관계와 크기까지 포함",
    L5: "픽셀 단위의 정밀도 요구"
  },
  
  dynamic_prompts: {
    encouragement: "네! 그렇게 구체적으로 표현하니 더 명확하네요!",
    challenge: "더 구체적으로 표현할 수 있을까요?",
    redirect: "'버튼'이라고 하지 말고 모양으로 설명해주세요."
  },
  
  error_handling: {
    misunderstanding: "추상어는 '버튼', '메뉴' 같은 거예요. 모양으로만 말해주세요.",
    resistance: "처음엔 어색하지만, 이게 창의성의 시작이에요.",
    confusion: "예: '둥근 모서리의 회색 사각형' 이렇게요."
  }
}
```

---

## 📱 실제 화면 흐름

### 시작 화면
```
🔍

구체적 인지
"개념 없이, 오직 형태로"

예상 소요 시간: 10분
난이도: ●●○○○

[시작하기] [맛보기]
```

### 진행 화면
```
[진행 상태 표시]
[●●●○○] 3/5 단계
[남은 시간: 약 5분]

[추상어 감지: ON]
현재 구체어 비율: 85%
━━━━━━━━━━━━━━━
[AI 대화 영역]

AI: 이것을 어떻게 설명하시겠어요?

⚠️ "버튼"은 추상어예요!

[사용자 입력 영역]
[도움말] [힌트] [건너뛰기]
```

### 전환 화면
```
✓ 기본 구체화 완료!

훌륭해요!
"이제 더 정밀하게 봐볼까요?"

[다음: 공간 관계 표현]

[계속하기] [잠시 쉬기]
```

### 완료 화면
```
🎯 구체적 인지 완성!

오늘의 성과:
━━━━━━━━━━━━━━━
추상어 제로 달성: 3분 12초
새로운 감각 어휘: 23개
구체어 사용률: 92%

💡 핵심 통찰:
"모든 것을 형태와 색으로 볼 수 있네요"

다음 추천:
• S1-A3 즉각 반응 - 구체적 인지를 바로 표현
• S2-A2 맥락화 - 이제 의미를 부여해보기

[대시보드] [다음 모듈] [다시하기]
```

---

## 🎭 S1-A2의 본질

### 핵심 철학
> "추상이 사라진 자리에 순수한 물질성이 드러난다"

- **현상학적 환원**: 사물을 사물 자체로
- **언어 이전의 인지**: 명명하기 전의 순수 경험
- **개념 없는 세계**: 공유 불가능한 개인적 지각

### 이론과 실행의 통합
```
이론적 본질: 100% 구체적, 즉물적 사고
    ↓
실행적 발현: 협업 불가능 (공유할 개념이 없음)
    ↓
핵심 변화: "아, 이렇게도 볼 수 있구나!"
```

### S1-A2의 고유한 특징
- **이론적 측면**: 추상화 수준 0의 순수 상태
- **체험적 측면**: 각자만의 감각적 경험
- **변혁적 측면**: 언어의 한계와 가능성 인식

### 체화의 증거
- **행동적 변화**: 추상어 사용 급감
- **인지적 변화**: 감각 어휘 확장
- **정서적 변화**: 사물을 새롭게 보는 즐거움
- **메타인지적 변화**: "내가 얼마나 추상적으로 살았나"

### 이 단계(S1)에서 이 축(A2)의 의미
- S1에서 A2는 완전한 구체성
- 타인과 공유 불가능한 순수 개인 경험
- 이것이 가능하게 하는 것: 창의적 지각의 기초

### 다음 단계로의 준비
- S1-A2: "둥글고 파란 플라스틱" (개인적 경험)
- S2-A2: "이것은 내게 안정감을 주는 형태" (첫 의미 부여)
- 전환의 열쇠: 구체에서 의미로의 자연스러운 도약

---

## 📝 실전 팁 (구현팀을 위한)

### 자주 발생하는 문제와 해결
1. **문제**: 추상어 없이 표현하기 너무 어려워함
   - **원인**: 일상 언어의 추상성
   - **해결**: 단계적 접근 - "버튼 → 클릭하는 것 → 네모"

2. **문제**: 지나치게 복잡한 묘사
   - **원인**: 구체성에 대한 오해
   - **해결**: "간단하게, 보이는 대로만"

### 퍼실리테이터 체크리스트
- [ ] 추상어 사용 시 즉시 피드백
- [ ] 구체적 표현 시 강하게 격려
- [ ] 개인차 인정하고 존중
- [ ] 창의성과 연결 지어 설명
- [ ] 충분한 연습 시간 제공

### 품질 보증 기준
- **최소 기준**: 5분간 추상어 5회 이하
- **목표 기준**: 구체어 비율 80% 이상
- **탁월함 기준**: 새로운 표현 방식 창조

---

**설계일**: 2025-08-17 (v3.0)
**설계자**: Session 06 - Thomas & PM Claude
**상태**: 구현 준비 완료
**다음 단계**: S1-A3 모듈 v3.0 업데이트
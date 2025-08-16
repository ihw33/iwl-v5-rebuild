# 📋 S1-A3 모듈 설계서
*실제 구현을 위한 상세 스펙*

---

## 🎯 모듈 메타데이터

```yaml
module_id: "S1-A3"
module_name: "구체적 인지"
stage: 1
axis: 3
korean_name: "지각인지 × 구체성-추상성"
english_name: "Perceptual Cognition × Concreteness-Abstraction"
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
    expected_response_type: "플라스틱 느낌, 파란 사각형, 둥근 모서리"
    time: "1분"
    
  - step: 3
    instruction: "기능을 빼고 형태만 말해보세요"
    ai_prompt: "'버튼'이라고 하지 말고 어떻게 생겼는지만"
    expected_response_type: "약간 튀어나온 직사각형"
    time: "1분"
    
  - step: 4
    instruction: "손으로 만진다면 어떤 느낌일지 상상해보세요"
    ai_prompt: "화면을 만질 수 있다면?"
    expected_response_type: "매끈한, 차가운, 평평한"
    time: "1분"
    
  - step: 5
    instruction: "크기를 실제 사물과 비교해보세요"
    ai_prompt: "이 요소의 크기는 뭐랑 비슷한가요?"
    expected_response_type: "엄지손톱만한, 동전만한"
    time: "1.5분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  tone: "호기심 자극, 구체적 유도"
  avoid: 
    - "그것의 기능은..."
    - "이것은 ~하는 도구"
    - "추상적 개념 허용"
  encourage:
    - "눈에 보이는 그대로"
    - "만질 수 있는 것처럼"
    - "오감으로 표현"
    
sample_responses:
  good: "네, '둥근 모서리의 파란 네모'! 또 뭐가 보이나요?"
  redirect: "'편리한'보다는 어떤 모양인지 말해주세요"
```

#### 체크포인트
```yaml
success_indicators:
  - "추상어 사용 빈도 감소"
  - "구체적 형용사 증가"
  - "오감 표현 등장"
completion_criteria: "5개 이상 요소를 구체적으로만 표현"
```

---

### L3 (중급) - 기초 학습자

#### 메타데이터
```yaml
level: 3
target_audience: "기본 관찰력 보유자"
duration: "7-8분"
difficulty: "moderate"
```

#### 학습 목표 (숨김)
- 복잡한 대상도 구체적으로 분해
- 미세한 차이를 물리적으로 표현
- 은유 없이 직접 묘사

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "복잡한 인터페이스를 레고 블록처럼 설명하세요"
    setup: "복잡한 대시보드나 앱 화면"
    time: "30초"
    
  - step: 2
    instruction: "각 부분을 재질과 질감으로 구분하세요"
    ai_prompt: "유리같은 부분, 종이같은 부분, 금속같은 부분은?"
    material_focus: true
    time: "2분"
    
  - step: 3
    instruction: "움직임을 물리적으로만 설명하세요"
    ai_prompt: "클릭하면 어떻게 움직이나요? (기능 말고 동작만)"
    motion_description: true
    time: "2분"
    
  - step: 4
    instruction: "색상을 자연물과 비교하세요"
    ai_prompt: "이 색은 무슨 과일/돌/하늘 색과 비슷한가요?"
    concrete_comparison: true
    time: "2분"
    
  - step: 5
    instruction: "전체를 3D 조각품처럼 묘사하세요"
    ai_prompt: "만약 이것이 조각품이라면 어떤 모습?"
    sculptural_view: true
    time: "1.5분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  complexity: "중간"
  focus:
    - "물리적 속성 강조"
    - "감각적 표현 유도"
    - "추상 개념 차단"
  avoid:
    - "UX/UI 용어"
    - "기능적 설명"
    
sample_responses:
  material: "유리처럼 투명한 부분이 보이시나요?"
  concrete: "사과 껍질 같은 붉은색이네요"
```

---

### L5 (고급) - 전문가 수준

#### 메타데이터
```yaml
level: 5
target_audience: "추상적 사고에 익숙한 전문가"
duration: "10-12분"
difficulty: "advanced"
```

#### 학습 목표 (숨김)
- 극도의 구체성 도달
- 추상의 유혹 극복
- 순수 물질성 체험

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "개념을 물질로 번역하세요"
    setup: "'사용자 경험'을 돌멩이와 물로만 표현"
    time: "1분"
    
  - step: 2
    instruction: "디지털을 아날로그로 완전 변환"
    ai_prompt: "화면의 전환을 종이 넘기기로 표현하면?"
    extreme_concrete: true
    time: "2분"
    
  - step: 3
    instruction: "나노 수준으로 확대해서 보세요"
    ai_prompt: "픽셀 하나하나를 벽돌처럼 본다면?"
    microscopic_view: true
    time: "2분"
    
  - step: 4
    instruction: "추상어 해독 게임"
    ai_prompt: "'직관적'을 구체적으로 바꾸면?"
    abstraction_removal: true
    time: "2분"
    
  - step: 5
    instruction: "순수 물질 명상"
    ai_prompt: "모든 의미를 빼고 순수한 형태만 남기면?"
    pure_materiality: true
    time: "3분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  sophistication: "높음"
  focus:
    - "극한의 구체성"
    - "추상 저항력"
    - "물질적 순수성"
  language:
    - "촉각적 어휘"
    - "물리적 비유"
    - "감각 중심"
    
sample_responses:
  extreme: "개념이 사라지고 형태만 남았네요"
  pure: "순수한 물질로 환원되었습니다"
```

---

## 🔄 타 모듈과의 연계

### 선행 모듈
- **S1-A1 (감각적 수용)**: 있는 그대로 보기
- **S1-A2 (즉각적 반응)**: 생각 없이 반응하기

### 후행 모듈
- **S1-A4 (자기인식 없음)**: 나를 잊고 대상에 몰입
- **S2-A3 (낮은 추상화)**: 첫 번째 의미 부여 시작

### 통합 프로그램에서의 역할
- 극도의 구체성을 통해 선입견 제거
- 추상적 사고의 틀에서 벗어나기
- S2에서 "의미"를 새롭게 만들 준비

---

## 💻 구현 가이드

### 프론트엔드 요구사항
```yaml
ui_elements:
  - concrete_word_checker: "추상어 감지 및 알림"
  - sensory_prompt: "오감 표현 유도 UI"
  - comparison_tool: "실물 비교 도구"
  - materiality_meter: "구체성 측정 표시"
  
interaction_design:
  - abstraction_alert: "추상어 사용 시 부드러운 알림"
  - concrete_examples: "구체적 표현 예시 제공"
  - visual_aids: "물질성 강조 시각 자료"
```

### 백엔드 데이터
```yaml
tracking_data:
  - abstraction_count: "추상어 사용 횟수"
  - concrete_ratio: "구체어/전체 비율"
  - sensory_variety: "사용된 감각 종류"
  - improvement_curve: "구체성 향상 곡선"
  
analytics:
  - common_abstractions: "자주 쓰는 추상어"
  - concrete_vocabulary: "구체어 어휘 확장"
  - level_appropriate: "레벨별 난이도 적절성"
```

### AI 프롬프트 템플릿
```javascript
const S1_A3_PROMPT = {
  system: `당신은 극도의 구체성을 안내하는 가이드입니다.
참여자가 모든 추상을 벗어던지고 순수한 물질성만 인지하도록 도와주세요.
'의미'나 '기능'이 아닌 '형태'와 '물질'에만 집중하게 하세요.
이것은 S1의 "없음"을 추상성 차원에서 구현하는 것입니다.`,
  
  level_adjustments: {
    L1: "쉬운 구체어로 시작, 추상어 부드럽게 교정",
    L3: "복잡한 대상도 물리적으로 분해",
    L5: "극한의 구체성, 개념의 물질화"
  }
}
```

---

## 📱 실제 화면 흐름

### 시작 화면
```
🔍 구체적 인지 훈련
"의미를 벗어던지고 형태만 보세요"
[시작하기]
```

### 진행 화면
```
[구체성 레벨: ████░░░ 70%]
[추상어 감지: 2회]

💡 이것을 만질 수 있다면?

AI: "어떤 재질같나요?"
나: "플라스틱같은..." 
AI: "좋아요! 어떤 플라스틱?"
```

### 완료 화면
```
🔍 구체적 인지 완료!

오늘의 발견:
- 구체어 사용: 85%
- 새로운 감각 표현: 12개
- 추상 극복 순간: 5회

[다음: S1-A4 무아 체험] [다시하기]
```

---

## 🎭 S1-A3의 본질

### 핵심 철학
> "추상이 사라진 자리에 순수한 물질성이 드러난다"

- **"없음"의 구현**: 의미가 없고 오직 형태만
- **현상학적 환원**: 사물을 사물 자체로
- **언어 이전의 인지**: 명명하기 전의 순수 경험

### S1의 "없음"과의 관계
- A1: 판단 없음 (인지만)
- A2: 계획 없음 (반응만)
- A3: **추상 없음 (물질만)**
- A4: 자기 없음 (대상만)

### 체화의 증거
- 추상어 사용 급감 (측정 가능)
- 감각 어휘 확장 (관찰 가능)
- 사물을 새롭게 보기 시작 (질적 변화)
- "아, 이렇게도 볼 수 있구나!" (깨달음)

### S2로의 준비
- S1-A3: "이것은 둥글고 파란 플라스틱"
- S2-A3: "이것은 내게 안정감을 주는 형태" (첫 의미 부여)

---

**설계일**: 2025-08-16
**설계자**: Thomas & PM Claude
**상태**: 구현 준비 완료
**다음 단계**: S1-A4 모듈 설계

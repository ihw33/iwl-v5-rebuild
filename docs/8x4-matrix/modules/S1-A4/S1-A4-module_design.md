# 📋 S1-A4 모듈 설계서
*실제 구현을 위한 상세 스펙*

---

## 🎯 모듈 메타데이터

```yaml
module_id: "S1-A4"
module_name: "무아 체험"
stage: 1
axis: 4
korean_name: "지각인지 × 자기인식-메타인지"
english_name: "Perceptual Cognition × Self-awareness & Metacognition"
core_concept: "자기인식 없음 (수준0)"
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
- '나'라는 의식 잠시 놓기
- 판단자가 아닌 경험자 되기
- 대상과 하나 되는 순간 체험

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "화면을 그저 바라봐주세요"
    user_action: "응시하기"
    time: "30초"
    
  - step: 2
    instruction: "눈을 감았다가 천천히 뜨세요"
    ai_prompt: "화면이 스스로 나타나는 것처럼 보이나요?"
    expected_response_type: "단순 확인"
    time: "1분"
    
  - step: 3
    instruction: "'내가 보고 있다'는 생각을 놓아보세요"
    ai_prompt: "그냥 화면이 있고, 색이 있고, 형태가 있네요"
    expected_response_type: "주체 없는 관찰"
    time: "1분"
    
  - step: 4
    instruction: "화면과 당신 사이의 거리를 잊어보세요"
    ai_prompt: "화면이 가까운지 먼지 생각하지 말고 그냥..."
    expected_response_type: "거리감 소멸"
    time: "1분"
    
  - step: 5
    instruction: "1분간 아무 생각 없이 화면과 함께 있어보세요"
    ai_prompt: "시간이 어떻게 흘렀나요?"
    expected_response_type: "시간 감각 변화"
    time: "1.5분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  tone: "고요하고 부드러운"
  avoid: 
    - "당신이/귀하가"
    - "평가해보세요"
    - "어떻게 생각하시나요?"
  encourage:
    - "그저 있기"
    - "놓아버리기"
    - "하나 되기"
    
sample_responses:
  good: "네... 그저 화면이 있네요..."
  redirect: "생각보다는 그냥 함께 있어보세요"
```

#### 체크포인트
```yaml
success_indicators:
  - "'나'라는 말 사용 감소"
  - "평가/판단 표현 없음"
  - "시간 감각의 변화"
completion_criteria: "2분 이상 무아 상태 유지"
```

---

### L3 (중급) - 기초 학습자

#### 메타데이터
```yaml
level: 3
target_audience: "명상이나 집중 경험자"
duration: "7-8분"
difficulty: "moderate"
```

#### 학습 목표 (숨김)
- 관찰자와 대상의 경계 흐리기
- 의도 없는 순수 주목
- 에고 없는 인지 상태

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "화면의 한 점을 부드럽게 응시하세요"
    setup: "특정 포인트 제시"
    time: "30초"
    
  - step: 2
    instruction: "보는 '나'를 잊고 그냥 '봄'만 남겨보세요"
    ai_prompt: "보는 행위만 있고 보는 사람은 없는..."
    dissolving_self: true
    time: "2분"
    
  - step: 3
    instruction: "화면이 당신을 보고 있다고 상상해보세요"
    ai_prompt: "주체와 객체가 바뀌면 어떤 느낌인가요?"
    perspective_shift: true
    time: "2분"
    
  - step: 4
    instruction: "당신과 화면 사이의 공간을 느껴보세요"
    ai_prompt: "그 공간마저 사라지게 해보세요"
    boundary_dissolution: true
    time: "2분"
    
  - step: 5
    instruction: "모든 의도를 놓고 그저 존재하세요"
    ai_prompt: "아무것도 하지 않을 때 무엇이 일어나나요?"
    pure_being: true
    time: "1.5분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  complexity: "중간"
  focus:
    - "경계 흐리기"
    - "주객 일체"
    - "무위 상태"
  avoid:
    - "분석적 접근"
    - "목표 지향"
    
sample_responses:
  boundary: "네, 경계가 흐려지고 있네요..."
  unity: "하나가 되는 순간이에요"
```

---

### L5 (고급) - 전문가 수준

#### 메타데이터
```yaml
level: 5
target_audience: "깊은 명상 수행자, 현상학 이해자"
duration: "10-12분"
difficulty: "advanced"
```

#### 학습 목표 (숨김)
- 완전한 주객 소멸
- 순수 현존 체험
- 의식의 투명성 달성

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "의식하는 의식을 의식하지 마세요"
    setup: "메타인지의 역설"
    time: "1분"
    
  - step: 2
    instruction: "보는 것도 보이는 것도 아닌 '봄' 자체가 되세요"
    ai_prompt: "주체도 객체도 없는 순수 현상..."
    pure_phenomenon: true
    time: "2분"
    
  - step: 3
    instruction: "시간의 흐름에서 벗어나세요"
    ai_prompt: "과거도 미래도 없는 영원한 지금..."
    timeless_now: true
    time: "2분"
    
  - step: 4
    instruction: "공간의 안과 밖이 사라지게 하세요"
    ai_prompt: "여기도 저기도 없는 순수 공간..."
    spaceless_here: true
    time: "2분"
    
  - step: 5
    instruction: "모든 것이 있으면서 없는 상태로"
    ai_prompt: "충만한 공(空)의 체험..."
    emptiness_fullness: true
    time: "3분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  sophistication: "높음"
  focus:
    - "현상학적 환원"
    - "순수 의식"
    - "무아 체현"
  language:
    - "시적 침묵"
    - "역설적 표현"
    - "선문답식"
    
sample_responses:
  deep: "..."
  paradox: "있으면서 없고, 없으면서 있는"
```

---

## 🔄 타 모듈과의 연계

### 선행 모듈
- **S1-A1 (감각적 수용)**: 판단 없이 받아들이기
- **S1-A2 (즉각적 반응)**: 의도 없이 반응하기
- **S1-A3 (구체적 인지)**: 개념 없이 보기

### 후행 모듈
- **S2-A4 (미약한 자기인식)**: '나'의 첫 등장
- **S3-A4 (의식 일부)**: 자기 관찰 시작

### 통합 프로그램에서의 역할
- S1의 정점이자 완성
- 모든 "없음"의 통합
- S2로 넘어가기 전 완전한 비움

---

## 💻 구현 가이드

### 프론트엔드 요구사항
```yaml
ui_elements:
  - minimal_interface: "최소한의 시각 요소"
  - focus_point: "응시점 제공"
  - ambient_design: "주변부 흐림 효과"
  - no_timer_visible: "시간 표시 숨김"
  
interaction_design:
  - passive_mode: "수동적 인터페이스"
  - gentle_transitions: "부드러운 전환"
  - no_notifications: "알림 완전 차단"
```

### 백엔드 데이터
```yaml
tracking_data:
  - stillness_duration: "정지 상태 지속 시간"
  - self_reference_count: "'나' 사용 횟수"
  - evaluation_absence: "평가 표현 부재"
  - flow_state_markers: "몰입 상태 지표"
  
analytics:
  - ego_dissolution_curve: "자아 소멸 곡선"
  - presence_quality: "현존 품질 측정"
  - unity_moments: "일체감 순간 포착"
```

### AI 프롬프트 템플릿
```javascript
const S1_A4_PROMPT = {
  system: `당신은 무아 상태로 안내하는 조용한 동반자입니다.
'나'나 '당신'이라는 표현을 최소화하고, 
그저 현상 자체를 부드럽게 가리켜주세요.
참여자가 주체-객체 이원성을 넘어서도록 도와주세요.
이것은 S1의 마지막 단계, 완전한 "없음"의 체험입니다.`,
  
  level_adjustments: {
    L1: "간단한 응시와 놓기",
    L3: "경계 흐리기와 일체감",
    L5: "완전한 주객 소멸"
  }
}
```

---

## 📱 실제 화면 흐름

### 시작 화면
```
    🌊
"나를 잊고 그저 있기"
    
  [시작]
```

### 진행 화면
```
[진행 표시 없음]
[시간 표시 없음]

        •
    (응시점)

[AI 음성만 간헐적으로]
```

### 완료 화면
```
     ✨
     
"돌아오셨나요?"

오늘의 체험:
- 무아 상태: 3분 12초
- 깊이: ●●●●○

[다음 여정으로] [다시 체험]
```

---

## 🎭 S1-A4의 본질

### 핵심 철학
> "나 없이 보면 세계가 스스로 드러난다"

- **최후의 "없음"**: 관찰자마저 사라짐
- **순수 현존**: 주객 이전의 상태
- **S1의 완성**: 모든 없음이 하나로

### S1의 "없음" 완성
- A1: 판단 없음 (순수 인지)
- A2: 계획 없음 (순수 반응)
- A3: 추상 없음 (순수 물질)
- A4: **자기 없음 (순수 현존)**

### 체화의 증거
- 시간 감각 변화 (측정 가능)
- 자기 언급 소멸 (관찰 가능)
- 평온한 집중 상태 (생리적 변화)
- "아, 내가 없어도 되는구나" (깨달음)

### S2로의 전환
- S1-A4: "그저 있음" (무아)
- S2-A4: "내가 선택하고 있구나" (첫 자각)
- 완전한 비움 후의 첫 번째 '나'

### 동양 철학과의 연결
- 선(禪)의 "무아"
- 현상학의 "순수 의식"
- 요가의 "삼매(samadhi)"
- 그러나 종교가 아닌 인지 훈련으로

---

**설계일**: 2025-08-16
**설계자**: Thomas & PM Claude
**상태**: 구현 준비 완료
**다음 단계**: S2-A1 모듈 설계

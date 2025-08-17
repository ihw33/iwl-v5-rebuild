# 📋 S2-A2 모듈 설계서 v1.0
*낮은 추상화 수준의 요약 및 맥락이해*

---

## 🎯 모듈 메타데이터

```yaml
module_id: "S2-A2"
module_name: "맥락화"
stage: 2
axis: 2
korean_name: "요약맥락이해 × 추상화수준"
english_name: "Summary & Context × Abstraction Level"
core_concept: "낮은 추상화 - 구체적 의미 부여"
estimated_time: 
  standalone: "15-20분"
  as_part_of_integration: "7-10분"
```

---

## 📊 레벨별 상세 설계

### L1 (초급) - 완전 초보자

#### 메타데이터
```yaml
level: 1
target_audience: "분류와 정리가 서툰 사용자"
duration: "7분"
difficulty: "very_easy"
```

#### 학습 목표 (숨김)
- 비슷한 것끼리 모으기
- 간단한 순서 만들기
- 그룹의 이름 짓기

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "AI가 보여주는 5개 아이템을 봐주세요"
    ai_prompt: "🍎 🚗 🍊 🚙 🍌"
    user_action: "관찰"
    time: "30초"
    
  - step: 2
    instruction: "비슷한 것끼리 2개 그룹으로 나눠보세요"
    expected_response_type: "과일 그룹, 자동차 그룹"
    ai_feedback: "어떤 기준으로 나눴나요?"
    time: "2분"
    
  - step: 3
    instruction: "이번엔 색깔별로 나눠볼까요?"
    ai_prompt: "빨간 사과, 파란 하늘, 빨간 장미, 파란 바다, 노란 해"
    grouping_criteria: "색상"
    time: "2분"
    
  - step: 4
    instruction: "순서를 만들어보세요"
    ai_prompt: "아침, 점심, 새벽, 저녁, 밤"
    ordering_task: true
    time: "1.5분"
    
  - step: 5
    instruction: "나눈 그룹에 이름을 지어주세요"
    reflection: "그룹의 공통점 찾기"
    time: "1분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  tone: "친근하고 격려하는"
  avoid: 
    - "틀렸다/맞았다 판단"
    - "복잡한 기준 제시"
    - "논리적 설명 요구"
  encourage:
    - "다양한 분류 방식 인정"
    - "창의적 그룹핑 칭찬"
    - "과정 자체를 즐기도록"
    
sample_responses:
  good: "오, 그렇게도 나눌 수 있네요! 재미있어요!"
  alternative: "다른 방법으로도 나눠볼까요?"
```

#### 체크포인트
```yaml
success_indicators:
  - "명확한 그룹 구분"
  - "그룹 기준 설명 가능"
  - "순서 배열 완성"
completion_criteria: "3가지 이상 다른 기준으로 그룹핑 성공"
```

---

### L3 (중급) - 기초 학습자

#### 메타데이터
```yaml
level: 3
target_audience: "업무에서 정보 정리가 필요한 사용자"
duration: "10분"
difficulty: "moderate"
```

#### 학습 목표 (숨김)
- 복잡한 정보의 구조화
- 다층적 그룹핑
- 관계성 발견

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "10개의 업무 관련 키워드를 봐주세요"
    ai_prompt: "회의, 보고서, 이메일, 기획, 마감, 협업, 검토, 승인, 자료, 피드백"
    context: "업무 프로세스"
    time: "1분"
    
  - step: 2
    instruction: "업무 흐름에 따라 그룹을 만들어보세요"
    grouping_task: "프로세스별 분류"
    expected_patterns: "시작-진행-완료"
    time: "3분"
    
  - step: 3
    instruction: "이번엔 중요도로 재배열해보세요"
    reorganization: true
    new_criteria: "우선순위"
    time: "2분"
    
  - step: 4
    instruction: "그룹 간의 연결고리를 찾아보세요"
    relationship_mapping: true
    ai_prompt: "어떤 그룹이 다른 그룹에 영향을 주나요?"
    time: "2분"
    
  - step: 5
    instruction: "전체 구조를 한 문장으로 설명해보세요"
    synthesis_task: true
    time: "2분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  complexity: "중간"
  focus:
    - "실용적 적용"
    - "다양한 관점"
    - "관계성 강조"
  questions:
    - "이 그룹들의 순서를 바꾸면?"
    - "겹치는 항목이 있나요?"
    - "새로운 기준을 적용하면?"
```

---

### L5 (고급) - 전문가 수준

#### 메타데이터
```yaml
level: 5
target_audience: "복잡한 시스템 설계자, 전략 기획자"
duration: "15분"
difficulty: "advanced"
```

#### 학습 목표 (숨김)
- 비선형적 구조 인식
- 창발적 패턴 발견
- 메타 구조 설계

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "20개의 다차원 데이터를 분석하세요"
    ai_prompt: "[복잡한 비즈니스 시나리오 데이터]"
    multi_dimensional: true
    time: "2분"
    
  - step: 2
    instruction: "숨겨진 패턴을 찾아 그룹화하세요"
    pattern_recognition: "암묵적 구조"
    hidden_relationships: true
    time: "4분"
    
  - step: 3
    instruction: "동적 재구성 - 시간에 따른 변화"
    dynamic_restructuring: true
    temporal_dimension: "과거-현재-미래"
    time: "3분"
    
  - step: 4
    instruction: "네트워크 구조로 재해석"
    network_thinking: true
    nodes_and_edges: "허브와 연결"
    time: "3분"
    
  - step: 5
    instruction: "새로운 구조 제안"
    creative_synthesis: true
    innovation_task: "기존에 없던 분류 체계"
    time: "3분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  sophistication: "매우 높음"
  approach:
    - "시스템 사고"
    - "복잡성 포용"
    - "창발성 인정"
  language:
    - "전문 용어 적절히 사용"
    - "추상과 구체 균형"
    - "통찰력 있는 질문"
    
sample_responses:
  insight: "그 구조에서 예상치 못한 연결이 보이네요"
  challenge: "만약 차원을 하나 더 추가한다면?"
```

---

## 🔄 타 모듈과의 연계

### 선행 모듈
- **S1-A2 (즉각적 반응)**: 개별 반응들을 모아 그룹으로
- **S2-A1 (의미 단위 해석)**: 선택된 중요 정보들을 구조화

### 후행 모듈
- **S2-A3 (낮은 추상화)**: 만든 구조에 구체적 의미 부여
- **S3-A2 (논리 구조)**: 그룹핑의 논리적 근거 발견

### 통합 프로그램에서의 역할
- S2의 핵심 활동: "선택한 것들을 의미 있게 조합"
- 개별에서 전체로의 첫 시도
- 관계성 인식의 시작점

---

## 💻 구현 가이드

### 프론트엔드 요구사항
```yaml
ui_elements:
  - drag_drop_interface: "드래그 앤 드롭 그룹핑"
  - visual_containers: "그룹 시각화 컨테이너"
  - connection_lines: "관계선 그리기"
  - color_coding: "그룹별 색상 코딩"
  
interaction_design:
  - smooth_grouping: "부드러운 그룹 이동"
  - dynamic_reorganization: "실시간 재구성"
  - visual_feedback: "즉각적 시각 피드백"
```

### 백엔드 데이터
```yaml
tracking_data:
  - grouping_patterns: "그룹핑 패턴 기록"
  - criteria_used: "사용된 분류 기준"
  - reorganization_count: "재구성 횟수"
  - relationship_complexity: "관계 복잡도"
  
analytics:
  - most_common_criteria: "자주 사용하는 기준"
  - grouping_efficiency: "그룹핑 효율성"
  - pattern_recognition_speed: "패턴 인식 속도"
```

### AI 프롬프트 템플릿
```javascript
const S2_A2_PROMPT = {
  system: `당신은 정보를 구조화하는 것을 돕는 파트너입니다.
참여자가 개별 요소들을 의미 있는 그룹으로 만들도록 안내하세요.
다양한 분류 기준을 탐색하고, 관계성을 발견하도록 도와주세요.
S1의 개별 인식에서 S3의 논리적 구조로 가는 중간 다리입니다.`,
  
  level_adjustments: {
    L1: "명확하고 단순한 분류, 시각적 단서 활용",
    L3: "실용적 구조화, 업무 맥락 적용",
    L5: "복잡한 시스템 사고, 창발적 구조"
  }
}
```

---

## 📱 실제 화면 흐름

### 시작 화면
```
🔗 구조 만들기 연습
"흩어진 점들을 의미 있는 그룹으로"
[시작하기]
```

### 진행 화면
```
┌─────────────────────────┐
│ 📦 그룹 1               │ 📦 그룹 2
│ • 사과                  │ • 자동차
│ • 오렌지                │ • 버스
│ • 바나나                │ • 기차
└─────────────────────────┘

[다른 기준으로 재배열] [관계선 그리기]
```

### 완료 화면
```
🎯 구조화 완료!

오늘의 성과:
- 생성한 그룹: 5개
- 발견한 관계: 8개
- 사용한 기준: 3가지

"정보가 구조를 가지니 의미가 보이기 시작했어요!"

[다음: S2-A3 맥락화] [다시 연습]
```

---

## 🎭 S2-A2의 본질

### 핵심 철학
> "점들을 선으로 연결하는 첫 시도 - 관계성의 발견"

- **조합의 자유**: 같은 요소도 다양한 방식으로 그룹화
- **구조의 유연성**: 고정된 답이 없는 열린 구조
- **의미의 창발**: 그룹을 만들면서 새로운 의미 발생

### S1에서 S2로의 전환
- S1: "이것, 저것, 그것" (개별 인식)
- S2-A2: "이것과 저것은 함께" (첫 연결)
- 아직 "왜"는 모르지만 "무엇과 무엇"은 안다

### 체화의 증거
- 자연스러운 분류 능력 향상
- 다양한 관점으로 재구성 가능
- 패턴 발견 속도 증가
- 구조적 사고의 기초 형성

---

**설계일**: 2025-08-17
**설계자**: Session 06 - PM Claude
**상태**: 초안 완성
**다음 단계**: S2-A3 모듈 설계 시간: 약 3분]

당신의 의미를 탐구해요
━━━━━━━━━━━━━━━
[의미 캔버스]

AI: 이것이 당신에게 어떤 기억을 불러일으키나요?

[은유: 🌊 🔥 🌱]

[사용자 입력 영역]
[도움말] [은유 도구] [깊이 더하기]
```

### 전환 화면
```
✓ 개인적 의미 발견!

깊이 있는 탐구였어요
"이제 더 깊은 곳으로..."

[다음: 상징 통합하기]

[계속하기] [잠시 쉬기]
```

### 완료 화면
```
🌊 맥락화 완료!

오늘의 의미 여정:
━━━━━━━━━━━━━━━
발견한 개인 의미: 7개
사용한 은유: 5개
깊이 도달: ●●●●○

💡 핵심 통찰:
"내 안에 이런 의미의 우주가 있었구나"

다음 추천:
• S2-A3 구조 인식 - 의미들의 관계
• S3-A2 개념화 - 공유 가능한 언어로

[대시보드] [다음 모듈] [다시하기]
```

---

## 🎭 S2-A2의 본질

### 핵심 철학
> "가장 개인적인 것이 가장 보편적이다 - 그러나 아직은 오직 나만의 것"

- **주관성의 심화**: 타인과 공유 불가능한 깊이
- **의미의 개인화**: 나만의 언어와 상징
- **내면의 풍경**: 의식의 사적 영역 탐구

### 이론과 실행의 통합
```
이론적 본질: 100% 개인화, 낮은 추상화
    ↓
실행적 발현: 개인 프로젝트나 예술 작품처럼
    ↓
핵심 변화: "이것은 오직 나만 아는 의미"
```

### S2-A2의 고유한 특징
- **이론적 측면**: 공유 불가능한 주관적 추상
- **체험적 측면**: 깊은 개인적 공명
- **변혁적 측면**: 내면 세계의 확장

### 체화의 증거
- **행동적 변화**: 독특한 표현 증가
- **인지적 변화**: 은유적 사고 활성화
- **정서적 변화**: 깊은 감정적 연결
- **메타인지적 변화**: "내 의미 세계가 이렇게 깊구나"

### 이 단계(S2)에서 이 축(A2)의 의미
- S2에서 A2는 맥락의 완전한 개인화
- 추상화는 시작되었지만 아직 사적 영역
- 이것이 가능하게 하는 것: S3에서의 공유 가능성

### 다음 단계로의 준비
- S2-A2: "파란색은 내 첫사랑" (개인적)
- S3-A2: "파란색은 평온함" (공유 가능)
- 전환의 열쇠: 개인에서 보편으로의 추상화

---

## 📝 실전 팁 (구현팀을 위한)

### 자주 발생하는 문제와 해결
1. **문제**: 너무 일반적인 의미만 말함
   - **원인**: 개인 노출 두려움
   - **해결**: "다른 사람 말고, 오직 당신만..."

2. **문제**: 의미를 찾지 못함
   - **원인**: 과도한 자기 검열
   - **해결**: "어린 시절 기억으로 돌아가보세요"

### 퍼실리테이터 체크리스트
- [ ] 안전한 심리적 공간 확보
- [ ] 개인적 표현 적극 격려
- [ ] 판단이나 해석 절대 금지
- [ ] 은유와 상징 활용 지원
- [ ] 깊이로의 초대, 강요는 금물

### 품질 보증 기준
- **최소 기준**: 3개 이상 개인 경험 연결
- **목표 기준**: 독특한 은유 5개 이상
- **탁월함 기준**: 개인 신화 구조 출현

---

**설계일**: 2025-08-17 (v3.0)
**설계자**: Session 06 - Thomas & PM Claude
**상태**: 구현 준비 완료
**다음 단계**: S2-A3 이후 모듈 계속 업데이트
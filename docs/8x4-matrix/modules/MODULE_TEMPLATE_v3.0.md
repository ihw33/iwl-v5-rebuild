# 📋 8×4 매트릭스 모듈 설계 템플릿 v3.0
*각 모듈의 장점을 통합한 최적화 버전*

---

## 🎯 모듈 메타데이터

```yaml
module_id: "S[1-8]-A[1-4]"
module_name: "[핵심 개념]"
stage: [1-8]
axis: [1-4]
korean_name: "[단계명] × [축명]"
english_name: "[Stage] × [Axis]"
core_concept: "[핵심 개념 한 단어/구]"
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
- [초급 목표 1 - 구체적이고 측정 가능하게]
- [초급 목표 2]
- [초급 목표 3]

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "[사용자 지시사항]"
    user_action: "[예상되는 사용자 행동]"
    time: "30초"
    
  - step: 2
    instruction: "[다음 지시사항]"
    ai_prompt: "[AI가 제시할 구체적 질문/프롬프트]"
    expected_response_type: "[기대하는 응답 유형과 예시]"
    time: "1분"
    
  - step: 3
    instruction: "[점진적으로 깊어지는 활동]"
    ai_prompt: "[구체적 프롬프트]"
    special_feature: "[이 단계의 특별한 특징]"
    time: "1.5분"
    
  - step: 4
    instruction: "[활동 심화]"
    ai_prompt: "[도전적 요소 포함]"
    cognitive_load: "낮음"
    time: "1분"
    
  - step: 5
    instruction: "[마무리 통합 활동]"
    synthesis: true
    time: "1.5분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  tone: "[구체적 톤 설명]"
  avoid: 
    - "[피해야 할 표현/행동 1]"
    - "[피해야 할 표현/행동 2]"
    - "[피해야 할 표현/행동 3]"
  encourage:
    - "[격려할 행동 1]"
    - "[격려할 행동 2]"
    - "[격려할 행동 3]"
    
sample_responses:
  good: "[구체적 좋은 응답 예시]"
  redirect: "[방향 전환이 필요할 때 응답]"
  encouragement: "[격려가 필요할 때 응답]"
```

#### 체크포인트
```yaml
success_indicators:
  - "[측정 가능한 성공 지표 1]"
  - "[측정 가능한 성공 지표 2]"
  - "[측정 가능한 성공 지표 3]"
completion_criteria: "[구체적 완료 기준]"
measurement_method: "[어떻게 측정할 것인가]"
```

---

### L3 (중급) - 기초 학습자

#### 메타데이터
```yaml
level: 3
target_audience: "[구체적 대상 설명]"
duration: "7-8분"
difficulty: "moderate"
prerequisites: "[선수 학습 내용]"
```

#### 학습 목표 (숨김)
- [중급 목표 1 - L1과 명확히 차별화]
- [중급 목표 2]
- [중급 목표 3]

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "[더 복잡한 지시사항]"
    setup: "[필요한 환경 설정]"
    time: "30초"
    
  - step: 2
    instruction: "[도전적 활동]"
    ai_prompt: "[복잡도가 높은 프롬프트]"
    cognitive_load: "중간"
    multi_modal: true  # 여러 감각/능력 동시 사용
    time: "2분"
    
  - step: 3
    instruction: "[창의적 요소 포함]"
    ai_prompt: "[열린 질문]"
    divergent_thinking: true
    time: "2분"
    
  - step: 4
    instruction: "[통합적 사고 요구]"
    ai_prompt: "[연결성 강조]"
    synthesis_required: true
    time: "2분"
    
  - step: 5
    instruction: "[자기 주도적 마무리]"
    self_directed: true
    time: "1.5분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  complexity: "중간"
  tone: "[좀 더 성숙한 톤]"
  focus:
    - "[중점 사항 1]"
    - "[중점 사항 2]"
    - "[중점 사항 3]"
  scaffolding:
    - "[단계적 지원 방법]"
    
sample_responses:
  probing: "[깊이 탐구하는 질문]"
  synthesis: "[통합을 유도하는 응답]"
  challenge: "[건전한 도전 제시]"
```

---

### L5 (고급) - 전문가 수준

#### 메타데이터
```yaml
level: 5
target_audience: "[구체적 전문가 그룹]"
duration: "10-12분"
difficulty: "advanced"
prerequisites: "[필수 선행 경험]"
```

#### 학습 목표 (숨김)
- [고급 목표 1 - 메타인지적 요소 포함]
- [고급 목표 2 - 창의적/비판적 사고]
- [고급 목표 3 - 자기 주도적 확장]

#### 실제 활동
```yaml
activity_sequence:
  - step: 1
    instruction: "[최소한의 가이드]"
    open_ended: true
    time: "1분"
    
  - step: 2
    instruction: "[복잡한 과제]"
    ai_prompt: "[추상적/철학적 질문]"
    metacognitive: true
    time: "2분"
    
  - step: 3
    instruction: "[창발적 활동]"
    emergent_properties: true
    ai_adapts_to_user: true
    time: "3분"
    
  - step: 4
    instruction: "[경계 넘기]"
    transcendent_element: true
    time: "2분"
    
  - step: 5
    instruction: "[자기 성찰과 통합]"
    reflection_depth: "deep"
    time: "2분"
```

#### AI 응답 가이드
```yaml
ai_behavior:
  sophistication: "매우 높음"
  approach:
    - "소크라테스식 문답"
    - "역설적 사고 유도"
    - "메타 레벨 이동"
  language:
    - "[고급 언어 스타일]"
    - "[전문 용어 적절히 사용]"
    - "[시적/은유적 표현]"
    
sample_responses:
  philosophical: "[철학적 응답 예]"
  paradoxical: "[역설적 응답 예]"
  metacognitive: "[메타인지 촉진 응답]"
```

---

## 🔄 타 모듈과의 연계

### 선행 모듈
- **[이전 S 모듈]**: [수직적 연계 - 단계 상승]
- **[이전 A 모듈]**: [수평적 연계 - 같은 단계 내]

### 후행 모듈  
- **[다음 S 모듈]**: [어떻게 준비시키는가]
- **[다음 A 모듈]**: [무엇을 전달하는가]

### 통합 프로그램에서의 역할
- [이 모듈의 고유한 기여]
- [다른 모듈과의 시너지 효과]
- [전체 여정에서의 위치와 의미]

### 크로스 연계 (선택적)
- **대각선 연계**: [S+1, A+1과의 관계]
- **보완 관계**: [반대 특성 모듈과의 균형]

---

## 💻 구현 가이드

### 프론트엔드 요구사항
```yaml
ui_elements:
  - [핵심 UI 요소 1]: "[구체적 기능 설명]"
  - [핵심 UI 요소 2]: "[사용자 경험 관점]"
  - [핵심 UI 요소 3]: "[접근성 고려사항]"
  
interaction_design:
  - [인터랙션 패턴 1]: "[구체적 구현 방법]"
  - [인터랙션 패턴 2]: "[사용자 피드백 방식]"
  - [인터랙션 패턴 3]: "[에러 처리 방법]"
  
visual_design:
  - color_scheme: "[이 모듈의 색상 테마]"
  - typography: "[텍스트 스타일 가이드]"
  - animation: "[모션 디자인 원칙]"
```

### 백엔드 데이터
```yaml
tracking_data:
  - [측정 항목 1]: 
      description: "[무엇을 측정하는가]"
      unit: "[측정 단위]"
      frequency: "[측정 주기]"
  - [측정 항목 2]: 
      description: "[설명]"
      threshold: "[의미 있는 임계값]"
  
analytics:
  - [분석 지표 1]: "[어떻게 계산하는가]"
  - [분석 지표 2]: "[무엇을 의미하는가]"
  - [분석 지표 3]: "[어떻게 활용하는가]"
  
data_privacy:
  - sensitive_data: "[민감 정보 목록]"
  - retention_period: "[보관 기간]"
  - anonymization: "[익명화 방법]"
```

### AI 프롬프트 템플릿
```javascript
const S[X]_A[Y]_PROMPT = {
  system: `[시스템 프롬프트 - 역할과 목적 명확히]
  [이 모듈의 핵심 철학 반영]
  [구체적인 행동 지침]
  [피해야 할 것들]`,
  
  level_adjustments: {
    L1: "[초급자를 위한 조정사항]",
    L3: "[중급자를 위한 조정사항]",
    L5: "[고급자를 위한 조정사항]"
  },
  
  dynamic_prompts: {
    encouragement: "[격려가 필요할 때]",
    challenge: "[도전이 필요할 때]",
    redirect: "[방향 전환이 필요할 때]"
  },
  
  error_handling: {
    misunderstanding: "[이해 못했을 때]",
    resistance: "[저항이 있을 때]",
    confusion: "[혼란스러워할 때]"
  }
}
```

---

## 📱 실제 화면 흐름

### 시작 화면
```
[모듈 아이콘/이모지]

[모듈명]
"[한 줄로 표현한 핵심 가치]"

[예상 소요 시간: X분]
[난이도: ●●○○○]

[시작하기] [맛보기]
```

### 진행 화면
```
[진행 상태 표시]
[●●●○○] 3/5 단계
[남은 시간: 약 X분]

[현재 활동 안내]
━━━━━━━━━━━━━━━
[AI 대화 영역]

AI: [현재 프롬프트]

[사용자 입력 영역]
[도움말] [힌트] [건너뛰기]
```

### 전환 화면
```
✓ [단계명] 완료!

[간단한 성취 피드백]
"[격려 메시지]"

[다음 단계 미리보기]

[계속하기] [잠시 쉬기]
```

### 완료 화면
```
🎉 [모듈명] 완료!

오늘의 성과:
━━━━━━━━━━━━━━━
[주요 성취 1]: [구체적 수치/설명]
[주요 성취 2]: [구체적 수치/설명]
[주요 성취 3]: [구체적 수치/설명]

💡 핵심 통찰:
"[참여자가 얻은 주요 깨달음]"

다음 추천:
• [추천 모듈 1] - [이유]
• [추천 모듈 2] - [이유]

[대시보드] [다음 모듈] [다시하기]
```

---

## 🎭 S[X]-A[Y]의 본질

### 핵심 철학
> "[이 모듈의 핵심 철학을 한 문장으로]"

- **[철학적 차원 1]**: [구체적 설명]
- **[철학적 차원 2]**: [구체적 설명]
- **[철학적 차원 3]**: [구체적 설명]

### 이론과 실행의 통합
```
이론적 본질: [학술적/추상적 정의]
    ↓
실행적 발현: [구체적 행동/경험]
    ↓
핵심 변화: [참여자에게 일어나는 변화]
```

### S[X]-A[Y]의 고유한 특징
- **이론적 측면**: [이 조합만의 특별함]
- **체험적 측면**: [실제로 어떻게 경험되는가]
- **변혁적 측면**: [어떤 변화를 만드는가]

### 체화의 증거
- **행동적 변화**: [관찰 가능한 변화]
- **인지적 변화**: [사고 패턴의 변화]
- **정서적 변화**: [느낌과 태도의 변화]
- **메타인지적 변화**: [자기 인식의 변화]

### 이 단계(S[X])에서 이 축(A[Y])의 의미
- S[X]의 맥락에서 A[Y]는 [특별한 의미]
- 다른 S 단계와 달리 여기서는 [차별점]
- 이것이 가능하게 하는 것: [가능성]

### 다음 단계로의 준비
- S[X]-A[Y]: "[현재 상태]" (예: 순수 감각)
- S[X+1]-A[Y]: "[다음 상태]" (예: 의미 부여)
- 전환의 열쇠: [무엇이 전환을 가능하게 하는가]

---

## 📝 실전 팁 (구현팀을 위한)

### 자주 발생하는 문제와 해결
1. **문제**: [흔한 문제 상황]
   - **원인**: [왜 발생하는가]
   - **해결**: [구체적 해결 방법]

2. **문제**: [또 다른 문제]
   - **원인**: [근본 원인]
   - **해결**: [실용적 해결책]

### 퍼실리테이터 체크리스트
- [ ] 참여자의 현재 상태 파악
- [ ] 레벨 선택의 적절성 확인
- [ ] 저항이나 어려움 조기 감지
- [ ] 전환 시점의 적절성 판단
- [ ] 다음 모듈 추천의 개인화

### 품질 보증 기준
- **최소 기준**: [반드시 달성해야 할 것]
- **목표 기준**: [이상적인 달성 수준]
- **탁월함 기준**: [최고 수준의 경험]

---

**템플릿 버전**: v3.0
**작성일**: 2025-08-17
**설계자**: Session 06 - Thomas & PM Claude
**설계 철학**: 이론적 엄밀성과 실용적 구현의 균형
**다음 업데이트**: 실제 구현 피드백 반영 후
# B0 템플릿 수정안 - 가입 설문 시스템

## 📋 수정 배경
- **일시**: 2025-08-15
- **참여**: Thomas, PM Claude
- **핵심 변경**: 평가 중심 → 니즈 파악 중심

---

## 🎯 설문 시스템 개요

### 핵심 원칙
1. **평가 NO, 니즈 파악 YES**
   - "레벨 테스트" ❌
   - "맞춤 서비스를 위한 대화" ✅

2. **AI 사용 경험 ≠ 사고력 수준**
   - 분리해서 파악
   - 사고력은 간접적으로 추론

3. **객관식 중심**
   - 복수선택 가능
   - 시각적 요소 활용
   - 빠른 완성

4. **단계별 적응형**
   - 2-5단계 분기
   - 답변에 따라 다음 질문 생성
   - 개인화된 경험

---

## 📊 단계별 설문 구조

### Stage 1: 기본 분류 (2문항)
```yaml
Q1_classification:
  question: "어떤 분이신가요?"
  options:
    - "👦 학생 (초중고)"
    - "🎓 대학생/대학원생"  
    - "💼 직장인"
    - "🚀 창업자/프리랜서"
    - "👩‍🏫 교육자/연구자"
    - "🏠 기타"

Q2_ai_experience:
  question: "AI 도구 사용 경험은?"
  options:
    - "처음이에요"
    - "가끔 써봤어요"
    - "자주 사용해요"
```

### Stage 2: 대상별 분기

#### 👦 주니어(학생) 경로
```yaml
# 보호자 설문 먼저
guardian_survey:
  required: true
  questions:
    - "자녀 학년"
    - "학습 성향"
    - "AI 교육 목적"
    - "우려사항"

# 자녀와 함께
junior_questions:
  visual: true  # 그림/이모지 중심
  questions:
    - "AI 친구랑 뭐하고 싶어?"
    - "어떤 AI 캐릭터가 좋아?"
```

#### 💼 직장인 경로
```yaml
professional_path:
  Q3: "어떤 업무를 하시나요?"
  Q4: "가장 시간이 오래 걸리는 업무는?"
  # 업무별 세분화 질문
```

### Stage 3: AI 인식과 니즈 파악

```yaml
ai_perception:
  question: "AI는 나에게... (모두 선택)"
  options:
    - "📚 모르는 걸 알려주는 선생님"
    - "💼 일을 대신 해주는 비서"  
    - "🤝 아이디어를 주고받는 동료"
    - "🔧 필요할 때 쓰는 도구"
    - "❓ 아직 잘 모르겠다"

current_challenges:
  question: "AI 사용 시 어려운 점 (2개 선택)"
  options:
    - "🤔 뭘 물어봐야 할지 막막해요"
    - "😕 원하는 답을 못 받아요"
    - "📋 답이 너무 일반적이에요"
    - "💭 어떻게 활용할지 모르겠어요"
```

### Stage 4: 학습 목표

```yaml
learning_goals:
  question: "어떤 걸 배우고 싶나요? (최대 3개)"
  visual_cards:
    - icon: "📝"
      title: "스마트한 과제/보고서"
      desc: "10분 만에 초안 완성"
    
    - icon: "💡"
      title: "창의적 아이디어"
      desc: "막힐 때 돌파구 찾기"
    
    - icon: "📊"
      title: "데이터 분석"
      desc: "복잡한 자료 쉽게 정리"
```

### Stage 5: 학습 스타일

```yaml
learning_preference:
  time: "언제 학습 가능?"
  style: "어떤 방식 선호?"
  commitment: "하루 몇 분?"
```

---

## 🎁 결과 제시 (평가 아닌 추천)

### 일반 사용자
```markdown
### 🎯 OO님을 위한 맞춤 추천!

💡 파악된 니즈
- "보고서 작성에 시간이 너무 오래 걸려요"
- "AI한테 물어봐도 뻔한 답만 나와요"

🎓 추천 학습 경로
1️⃣ [바로 시작] AI 질문법 기초
2️⃣ [다음 단계] 맞춤형 보고서 작성
3️⃣ [심화 과정] 전문가처럼 AI 활용하기

[지금 시작하기] [추천 커리큘럼 보기]
```

### 주니어 + 보호자
```markdown
### 🏠 가족 맞춤 학습 플랜

👶 민준이를 위한 추천
- AI랑 동화 만들기 (25분)
- 재미있는 숙제 도우미

👨‍👩‍👧 부모님을 위한 가이드
- AI 안전 교육 가이드
- 함께하는 프로젝트

[대시보드 설정하기] [첫 수업 시작]
```

---

## 📈 추가 개선사항

### 1. 정밀 진단 (선택사항)
- 가입 후 2-3일 뒤 제안
- 검증된 검사 도구 활용
- 신뢰도 구축 효과

### 2. 주기적 업데이트
- 월 1회 미니 설문
- 성장 추적
- 니즈 변화 감지

### 3. 실험 계획
- 실제 사용자 vs AI 페르소나 비교
- 설문 정확도 검증
- 지속적 개선

---

## 💾 시스템 통합

### 데이터 구조
```json
{
  "user_profile": {
    "type": "professional",
    "ai_experience": "beginner",
    "needs": ["report_writing", "time_saving"],
    "challenges": ["general_answers", "what_to_ask"],
    "goals": ["smart_report", "creative_ideas"],
    "style": "solo_systematic"
  },
  "recommendations": {
    "first_lesson": "ai_question_basics",
    "learning_path": ["S2-A1", "S3-A1", "S4-A3"],
    "estimated_time": "15min_daily"
  }
}
```

### Frontend 통합
- B0 템플릿의 Frontend View와 연동
- 설문 결과 → 맞춤 수업 자동 생성
- 대시보드에 프로필 표시

---

**작성일**: 2025-08-15
**다음 단계**: 실제 구현 및 테스트

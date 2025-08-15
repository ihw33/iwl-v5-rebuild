# B0 템플릿 예시: AI와 함께 만드는 기술 도입 제안서

## 📋 템플릿 적용 예시
- **기반 템플릿**: B0 Standard Template v1.0
- **작성일**: 2025-08-15
- **수업 주제**: 상사를 설득하는 1페이지 기술 제안서 작성

---

## 🎯 Frontend View (학습자용)

### 오늘의 목표
> **"새로운 기술이나 도구를 팀에 도입하고 싶은데 상사를 어떻게 설득할지 고민이신가요?
> 35분 안에 AI와 함께 설득력 있는 1페이지 제안서를 만들어봅시다!"**

### 준비물
- [ ] AI 챗봇 (ChatGPT/Claude/Gemini 중 하나)
- [ ] 도입하고 싶은 기술/도구에 대한 기본 정보
- [ ] 35분의 집중 시간

### 수업 진행 (35분)

#### 🚀 시작하기 (5분)
1. **목표 확인**: 완성될 제안서 샘플 구조 확인
   - 문제 정의 → 해결책 제시 → 기대 효과 → 실행 계획
2. **AI 준비**: 새 대화 시작
3. **첫 질문 입력하기**

```
💬 이렇게 시작하세요:
"저는 [직책]이고, 우리 팀에 [기술/도구]를 도입하고 싶습니다. 
현재 상황은 [문제 상황]이고, 상사는 [성향/관심사]를 중시합니다.
1페이지 제안서를 만들고 싶은데 어떻게 시작하면 좋을까요?"
```

#### 💡 함께 만들기 (25분)

**Step 1: 핵심 파악하기 (8분)**
```
💬 이런 질문으로 깊이 파고들어보세요:

"우리 팀이 현재 겪는 문제를 3가지로 정리하면?"
"이 기술이 각 문제를 어떻게 해결할 수 있는지 구체적으로 설명해줘"
"상사 입장에서 가장 걱정할 만한 점은 뭘까?"
```

💡 **체크포인트**: AI가 당신의 상황을 제대로 이해했는지 확인

**Step 2: 설득 논리 만들기 (9분)**
```
💬 논리를 강화하는 질문들:

"투자 대비 수익(ROI)을 숫자로 표현하면?"
"경쟁사나 업계 사례를 3개 찾아줘"
"리스크를 최소화하는 단계적 도입 방안은?"
"빠른 성과를 보여줄 수 있는 파일럿 프로젝트 아이디어는?"
```

💡 **체크포인트**: 반박 가능한 부분을 미리 대비했는지 점검

**Step 3: 1페이지로 압축하기 (8분)**
```
💬 마무리 질문:

"지금까지 내용을 1페이지 제안서로 구성해줘. 
제목, 현황, 제안, 기대효과, 실행계획 순서로"

"더 임팩트 있는 제목 5개를 제안해줘"

"상사가 물어볼 만한 질문 3개와 답변을 준비해줘"
```

#### ✅ 마무리 (5분)
- 제안서 최종 검토 및 다듬기
- AI 대화 내용 저장 (추후 참고용)
- 발표 시나리오 간단히 메모

### 🎁 오늘의 성과
- [ ] 1페이지 기술 도입 제안서 완성
- [ ] 예상 질문과 답변 준비 완료
- [ ] 단계별 실행 계획 수립
- [ ] 설득력 있는 AI 활용법 체득

### 💡 더 나아가기
- 제안서를 시각적 프레젠테이션으로 발전시키기
- 팀원들과 공유하여 피드백 받기
- 실제 미팅 후 결과를 AI와 분석하기

---

## 🔧 Backend View (서비스 제공자용)

### 수업 메타데이터
```yaml
lesson_id: B0-20250815-001
title: "AI와 함께 만드는 기술 도입 제안서"
type: "목적별조합"
duration: 35
level: L3
target_audience: Pro

modules_used:
  - module_id: "S2-A1"  # 목적 명확화 + 분석
    weight: 0.3
    focus: "primary"
    application: "문제 정의 및 현황 분석"
  
  - module_id: "S4-A3"  # 설득 논리 + 협업
    weight: 0.4
    focus: "primary" 
    application: "이해관계자 관점 통합"
  
  - module_id: "S5-A2"  # 실행 계획 + 창의
    weight: 0.3
    focus: "support"
    application: "실행 방안 구체화"

cognitive_objectives:
  primary_axis: 
    name: "A1-분석"
    level: 3
    specific_goals:
      - "현재 문제를 구조적으로 분석"
      - "기술 도입의 영향 다각도 분석"
      - "ROI 및 리스크 정량화"
  
  secondary_axes:
    - name: "A3-협업"
      level: 3
      integration_point: "Step 2 - 이해관계자 관점"
      specific_goals:
        - "상사의 관심사 파악 및 반영"
        - "반대 의견 선제적 대응"

ai_interaction_design:
  total_prompts: 10
  prompt_sequence:
    - stage: "초기 상황 파악"
      count: 2
      cognitive_load: "low"
      example_patterns:
        - "문제 정의 요청"
        - "이해관계자 맵핑"
      quality_indicators:
        - "구체적인 상황 설명 포함"
        - "정량적 지표 언급"
    
    - stage: "분석 및 논리 구축"
      count: 4
      cognitive_load: "medium"
      example_patterns:
        - "인과관계 분석"
        - "비교 우위 도출"
        - "반박 논리 준비"
      quality_indicators:
        - "다각도 분석 시도"
        - "구체적 사례 요청"
    
    - stage: "통합 및 압축"
      count: 4
      cognitive_load: "high"
      example_patterns:
        - "핵심 메시지 추출"
        - "시각적 구조화"
        - "액션 플랜 구체화"
      quality_indicators:
        - "1페이지 제약 활용"
        - "우선순위 명확화"

measurement_checkpoints:
  - time: "8min"
    indicator: "문제 정의 완성도"
    success_criteria: 
      - "현재 문제 3가지 이상 도출"
      - "각 문제의 영향 정량화 시도"
    intervention_if_struggling:
      - "문제 카테고리 제시 (효율성/품질/비용)"
  
  - time: "17min"
    indicator: "설득 논리 강도"
    success_criteria:
      - "최소 3개 이상의 근거 제시"
      - "예상 반박에 대한 대응 준비"
    intervention_if_struggling:
      - "SWOT 프레임워크 제안"
  
  - time: "30min"
    indicator: "제안서 완성도"
    success_criteria:
      - "1페이지 이내 구조화"
      - "실행 계획 구체성"
    intervention_if_struggling:
      - "템플릿 구조 직접 제공"

alternative_paths:
  if_too_easy:
    - "복수 이해관계자 시나리오 추가"
    - "예산 제약 조건 부여"
    - "경쟁 제안서와 비교 요구"
  
  if_too_hard:
    - "제안서 템플릿 제공"
    - "단계별 예시 문장 제시"
    - "범위를 팀 내 파일럿으로 축소"

facilitation_notes:
  key_moments:
    - "10분: 첫 번째 체크인 - 문제 정의 명확한가?"
    - "20분: 두 번째 체크인 - 설득 논리 충분한가?"
    - "30분: 최종 체크인 - 실행 가능한가?"
  
  common_pitfalls:
    - "너무 기술적인 내용에 치중"
    - "상사 관점 고려 부족"
    - "실행 계획 구체성 부족"
  
  success_factors:
    - "개인 맥락 충분히 활용"
    - "숫자와 사례로 구체화"
    - "단계적 접근 강조"

data_collection:
  performance_metrics:
    prompt_evolution:
      - initial: "단순 정보 요청"
      - intermediate: "분석적 요청"
      - advanced: "통합적 사고 요청"
    
    output_quality:
      - structure: 5  # 1페이지 구조화
      - logic: 4      # 설득 논리
      - practicality: 5  # 실행 가능성
    
    cognitive_achievement:
      - analysis: 4   # 목표: 3
      - creativity: 3  # 목표: 해당없음
      - collaboration: 4  # 목표: 3
      - reflection: 2  # 목표: 해당없음

ai_training_data:
  session_summary:
    context: "2년차 프로덕트 매니저가 팀에 Figma 도입 제안"
    challenge: "비용 의식이 강한 상사 설득"
    approach: "ROI 중심 + 단계적 도입"
    outcome: "파일럿 프로젝트 승인"
  
  effective_prompts:
    - "우리 팀 디자인 협업 문제를 시간 낭비 관점에서 분석해줘"
    - "Figma 도입 시 월 단위 시간 절감 효과를 계산해줘"
    - "무료 버전으로 시작하는 3개월 파일럿 계획을 만들어줘"
  
  learning_trajectory:
    start: "도구 기능 나열"
    middle: "문제-해결 연결"
    end: "비즈니스 임팩트 중심"
```

### 강사용 진행 노트

#### 수업 시작 시
```
"오늘은 여러분이 실제로 팀에 도입하고 싶은 기술이나 도구를 
상사에게 제안하는 1페이지 문서를 만들어볼 거예요.

이론 설명은 없습니다. 바로 AI와 대화하면서 
실제 사용할 수 있는 제안서를 완성하는 것이 목표입니다.

35분 후에는 내일 당장 상사에게 보여줄 수 있는 
제안서를 가지고 가실 수 있을 거예요."
```

#### 주요 개입 포인트
1. **8분**: "지금까지 찾은 문제점들이 상사가 공감할 만한가요?"
2. **17분**: "반대할 만한 이유를 미리 찾아보셨나요?"
3. **25분**: "한 페이지에 다 들어가나요? 핵심만 남기세요."

#### 마무리 멘트
```
"35분 만에 실제 사용 가능한 제안서를 만드셨습니다.
AI를 어떻게 활용하느냐에 따라 결과물의 품질이 달라진다는 것을
직접 경험하셨을 거예요.

다음에는 이 제안서를 프레젠테이션으로 발전시키거나,
팀원들의 피드백을 통합하는 방법을 다뤄볼 수 있습니다."
```

---

**예시 작성**: PM Claude
**검증 필요**: 실제 35분 수업에서 테스트
**다음 단계**: 다양한 주제별 예시 추가 개발


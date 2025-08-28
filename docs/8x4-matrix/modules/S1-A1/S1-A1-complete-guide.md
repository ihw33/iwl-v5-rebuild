# 📚 S1-A1 모듈 완전 가이드

**모듈명**: 순수한 관찰 (Pure Observation)  
**Matrix 위치**: S1 (지각인지) × A1 (정보처리깊이)  
**핵심 능력**: 판단 없이 있는 그대로 관찰하기

---

## 🎯 모듈 개요

### 핵심 목표
"감각적 수용" - 판단이나 해석 없이 순수하게 관찰하는 능력 훈련

### 차별점
- **S1-A1만의 고유성**: 철저한 판단어 필터링과 감각어 중심 언어 습관화
- **다른 모듈과의 차이**: 분석/해석을 완전히 배제하고 오직 감각 기술에만 집중

---

## 🏗️ 구현 구조

### 1. 학습 모듈 노드
**파일**: `nodes/learning/S1_A1_perception_depth.py`

```
S1_A1_PureObservationNode
├── 레벨별 활동 시퀀스 (L1/L3/L5)
├── AI 가이드 생성
└── 관찰 품질 평가
```

**주요 특징**:
- 레벨별 5단계 활동 시퀀스
- 판단어 감지 및 교정
- 관찰 다양성 측정

### 2. 수업 방식 노드
**파일**: `nodes/teaching_methods/observation_meditation_method.py`

```
ObservationMeditationMethod (통합 오케스트레이터)
├── LanguageGuardrailNode (판단어 필터)
├── ObservationGuideNode (관찰 가이드)
└── EchoReflectionNode (성찰 유도)
```

---

## 📊 4단계 수업 구조

### Phase 1: 준비 (1분)
- **목적**: 판단 내려놓기
- **프롬프트**: "지금은 '보는 것'만 합니다"
- **UI**: 중성 톤, 저자극 환경

### Phase 2: 관찰 (6분)
- **목적**: 있는 그대로 보기
- **활동**: 색상, 형태, 위치 관찰
- **노드**: ObservationGuide + LanguageGuardrail

### Phase 3: 기록 (3분)
- **목적**: 본 것을 언어로
- **예시**: "파란색 네모(우상단)"
- **노드**: LanguageGuardrail + EchoReflection

### Phase 4: 성찰 (2분)
- **목적**: 관찰 경험 돌아보기
- **질문**: "처음엔 못 봤던 것은?"
- **노드**: EchoReflection

---

## 🎚️ 개인화 시스템

### 3가지 핵심 파라미터

1. **guardrail_strictness**
   - `high`: 모든 판단어 즉시 차단
   - `medium`: 주요 판단어만 교정
   - `low`: 최소 개입

2. **timing_pressure**
   - `true`: 타이머 표시, 시간 제한
   - `false`: 타이머 숨김, 여유로운 진행

3. **feedback_mode**
   - `realtime`: 즉시 피드백
   - `batched`: 단계 끝 누적 피드백

### 설문 매핑 예시
```python
if profile.get("correction_preference") >= 4:
    params.guardrail_strictness = HIGH
if profile.get("time_pressure_preference") >= 4:
    params.timing_pressure = True
if profile.get("immediate_feedback") >= 4:
    params.feedback_mode = REALTIME
```

---

## 📈 측정 지표 (KPI)

### 주요 지표
1. **판단어 비율**: < 10% (목표)
2. **감각어 커버리지**: > 60% (목표)
3. **관찰 밀도**: > 2개/분 (목표)

### 평가 방법
```python
def _assess_quality(observations):
    pure_count = 순수관찰문장수
    diversity = 어휘다양성
    quality_score = (pure_count / total) * (diversity / 50)
    return quality_score
```

---

## 🔍 언어 가드레일

### 금지어 (판단/해석)
```python
judgment_words = {
    "평가": ["좋다", "나쁘다", "예쁘다"],
    "해석": ["버튼이다", "메뉴다", "위한"],
    "분석": ["효율적", "복잡한", "논리적"]
}
```

### 권장어 (감각)
```python
sensory_words = {
    "색상": ["빨간", "파란", "밝은", "어두운"],
    "형태": ["둥근", "네모", "직선", "곡선"],
    "위치": ["위", "아래", "왼쪽", "오른쪽"],
    "크기": ["큰", "작은", "넓은", "좁은"]
}
```

---

## 💡 다음 모듈 개발자를 위한 가이드

### 필수 구현 체크리스트

- [ ] `AbstractBaseNode` 상속
- [ ] 모듈별 Protocol 구현 (`LearningModuleNode` 또는 `TeachingMethodNode`)
- [ ] `_run()` 메서드 구현
- [ ] 입력/출력 포트 정의 (`NodeIO`, `PortSchema`)
- [ ] 레벨별 차별화 (L1/L3/L5)
- [ ] 개인화 파라미터 정의
- [ ] 품질 평가 메트릭
- [ ] 에러 처리 및 검증

### 재사용 가능한 패턴

#### 패턴 1: 레벨별 활동 정의
```python
self.activities = {
    "L1": [초급_활동_리스트],
    "L3": [중급_활동_리스트],
    "L5": [고급_활동_리스트]
}
```

#### 패턴 2: 노드 오케스트레이션
```python
class 통합메서드(AbstractBaseNode):
    def __init__(self):
        self.sub_node1 = SubNode1()
        self.sub_node2 = SubNode2()
        # 서브 노드 조합
```

#### 패턴 3: 개인화 추출
```python
def _extract_personalization(profile: Dict) -> Params:
    # 설문 → 파라미터 매핑
    return PersonalizationParams(...)
```

---

## 🚀 실행 방법

### 단독 테스트
```bash
python -m nodes.teaching_methods.observation_meditation_method
```

### 통합 실행
```python
from nodes.teaching_methods.observation_meditation_method import ObservationMeditationMethod

method = ObservationMeditationMethod()
result = method._run({
    "user_profile": {...},
    "scene": {...},
    "user_level": "L1"
}, context)
```

---

## 📝 문서 위치

- **설계서**: `docs/8x4-matrix/modules/S1-A1/S1-A1-module_design.md`
- **구현 리뷰**: `docs/8x4-matrix/modules/S1-A1/S1-A1-implementation-review.md`
- **이 가이드**: `docs/8x4-matrix/modules/S1-A1/S1-A1-complete-guide.md`

---

## ✅ 완료 상태

- [x] 학습 모듈 노드 구현
- [x] 수업 방식 노드 구현 (3노드 + 통합)
- [x] 4단계 구조 정의
- [x] 3가지 개인화 파라미터
- [x] KPI 및 평가 시스템
- [x] 테스트 및 검증
- [ ] 프로덕션 배포

---

## 🔄 다음 단계

1. **S1-A2**: 구체적 인지 모듈 개발 시 이 구조 참조
2. **테스트**: 단위 테스트 및 통합 테스트 작성
3. **최적화**: 성능 모니터링 및 캐싱 추가
4. **문서화**: 사용자 매뉴얼 작성

---

*작성일: 2025-08-28*  
*작성자: PM Claude & Thomas*  
*버전: 1.0.0*
# 📚 8×4 매트릭스 모듈 디렉토리

## 📋 개요
이 폴더는 IWL v5.0의 **32개 모듈** (8단계 × 4축)을 관리합니다.

---

## 🗂️ 폴더 구조
```
modules/
├── README.md                    ← 이 문서
├── MODULE_TEMPLATE.md           ← 📌 모듈 작성 템플릿 (필독!)
├── Module_Metadata_Template.md  ← 구 템플릿 (참고용)
│
├── S1-A1/                       ← ✅ 완성
│   └── S1-A1-module_design.md
├── S1-A2/                       ← 🔄 수정 중
│   └── S1-A2-module_design.md
├── S1-A3/                       ← ⏳ 예정
├── S1-A4/                       ← ⏳ 예정
│
├── S2-A1/                       ← 🚀 시작
│   └── metadata.yaml
├── S2-A2/                       ← ⏳ 예정
├── S2-A3/                       ← ⏳ 예정
├── S2-A4/                       ← ⏳ 예정
│
└── ... S3~S8                    ← ⏳ 예정
```

---

## 📝 모듈 작성 가이드

### 1️⃣ 새 모듈 생성 시
```bash
# 1. 폴더 생성
mkdir S[X]-A[Y]

# 2. 템플릿 복사
cp MODULE_TEMPLATE.md S[X]-A[Y]/S[X]-A[Y]-module_design.md

# 3. 내용 작성
# MODULE_TEMPLATE.md 구조에 맞춰 작성
```

### 2️⃣ 파일 명명 규칙
- **형식**: `S[단계]-A[축]-module_design.md`
- **예시**: `S1-A3-module_design.md`
- **이유**: 파일명만 봐도 어떤 모듈인지 명확

### 3️⃣ 필수 포함 내용
- 📊 레벨별 설계 (L1, L3, L5)
- 🔄 타 모듈과의 연계
- 💻 구현 가이드
- 📱 실제 화면 흐름
- 🎭 철학적 본질

---

## 🎯 8×4 매트릭스 구조

### 8개 단계 (Stages)
| 단계 | 한글명 | 영문명 | 핵심 |
|------|--------|--------|------|
| S1 | 지각인지 | Perceptual Cognition | 순수한 감각 |
| S2 | 요약·맥락이해 | Summary & Context | 관계의 발견 |
| S3 | 연상·추론 | Association & Inference | 패턴의 인식 |
| S4 | 창의·창조 | Creativity & Creation | 새로움의 탄생 |
| S5 | 비판적 사고 | Critical Thinking | 깊이 있는 검토 |
| S6 | 의사결정 | Decision Making | 선택의 지혜 |
| S7 | 실행계획 | Execution Planning | 실현의 설계 |
| S8 | 지식 통합 | Knowledge Integration | 전체의 융합 |

### 4개 축 (Axes)
| 축 | 한글명 | 영문명 | 초점 |
|-----|--------|--------|------|
| A1 | 정보처리깊이 | Information Processing Depth | 얼마나 깊이? |
| A2 | 사고조작방식 | Thinking Manipulation | 어떻게? |
| A3 | 구체성-추상성 | Concreteness-Abstraction | 어느 수준? |
| A4 | 자기인식-메타인지 | Self-awareness & Metacognition | 나를 아는가? |

---

## 📊 진행 현황 (2025-08-16)

### ✅ 완성 (2개)
- S1-A1: 감각적 수용

### 🔄 수정 중 (1개)
- S1-A2: 수동적 반응 (세션 05에서 수정 예정)

### 🚀 시작 (1개)
- S2-A1: 부분과 전체

### ⏳ 대기 (28개)
- S1-A3, S1-A4
- S2-A2, S2-A3, S2-A4
- S3 ~ S8 전체

**진행률**: 4/32 (12.5%)

---

## 💡 작업 시 주의사항

### DO ✅
- MODULE_TEMPLATE.md 구조 준수
- 레벨별 난이도 명확히 구분
- 철학적 깊이 포함
- 실제 활동 중심으로 작성
- 파일명 규칙 준수

### DON'T ❌
- 템플릿 구조 임의 변경
- 파일명을 module_design.md로만 작성
- 철학적 통찰 생략
- 이론만 나열

---

## 🔗 관련 문서
- [8×4 매트릭스 이론](/docs/8x4-matrix/8x4_Matrix_Theory_Guide.md)
- [S1 통합 가이드](/docs/8x4-matrix/S1_Complete_Guide.md)
- [S2 재정의](/docs/8x4-matrix/S2_Redefined_Design.md)
- [프로젝트 현황](/PROJECT_STATUS.md)

---

**최종 업데이트**: 2025-08-16
**관리자**: Thomas & PM Claude
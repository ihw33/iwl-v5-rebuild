# 🎯 8×4 매트릭스 마스터 디렉토리

## 📋 개요
IWL v5.0의 핵심인 **8×4 매트릭스** (8단계 × 4인지축 = 32개 모듈) 관련 모든 파일을 관리합니다.

---

## 🗂️ 폴더 구조
```
8x4-matrix/
├── README.md                     ← 이 문서
│
├── 📚 이론 문서
│   ├── 8x4_Matrix_Theory_Guide.md   ← 전체 이론 체계
│   ├── S1_Complete_Guide.md         ← S1 종합 가이드
│   ├── S2_Redefined_Design.md       ← S2 재정의
│   └── S2_Detailed_Design.md        ← S2 상세 설계
│
├── 📦 modules/                   ← 32개 모듈 설계
│   ├── README.md                 ← 모듈 작성 가이드
│   ├── MODULE_TEMPLATE.md        ← 📌 표준 템플릿
│   ├── S1-A1/                    ← 각 모듈 폴더
│   ├── S1-A2/
│   └── ...
│
└── 🎓 programs/                  ← 통합 프로그램
    └── S1_Integrated_Program.md  ← S1 20-30분 프로그램
```

---

## 📊 8×4 매트릭스 개요

### 구조
```
        A1          A2          A3          A4
      (깊이)      (방식)    (추상성)    (메타인지)
S1   S1-A1       S1-A2       S1-A3       S1-A4     ← 지각인지
S2   S2-A1       S2-A2       S2-A3       S2-A4     ← 요약·맥락
S3   S3-A1       S3-A2       S3-A3       S3-A4     ← 연상·추론
S4   S4-A1       S4-A2       S4-A3       S4-A4     ← 창의·창조
S5   S5-A1       S5-A2       S5-A3       S5-A4     ← 비판적사고
S6   S6-A1       S6-A2       S6-A3       S6-A4     ← 의사결정
S7   S7-A1       S7-A2       S7-A3       S7-A4     ← 실행계획
S8   S8-A1       S8-A2       S8-A3       S8-A4     ← 지식통합
```

### 핵심 철학
- **"가르치지 않는 가르침"** - 체화와 수련
- **"목표 없는 성장"** - 자연스러운 발전
- **레벨은 난이도가 아닌 "깊이"** - L1(그림책) → L5(소설)

---

## 🚀 빠른 시작

### 새 모듈 작성
```bash
# 1. 템플릿 확인
cat modules/MODULE_TEMPLATE.md

# 2. 새 모듈 생성
mkdir modules/S3-A1
cp modules/MODULE_TEMPLATE.md modules/S3-A1/S3-A1-module_design.md

# 3. 내용 작성
# 템플릿 구조에 맞춰 작성
```

### 기존 모듈 참고
```bash
# 완성된 예시
cat modules/S1-A1/S1-A1-module_design.md

# 수정 중인 예시
cat modules/S1-A2/S1-A2-module_design.md
```

---

## 📈 진행 현황

### 단계별 진행
| 단계 | 완료 | 진행 | 대기 | 진행률 |
|------|------|------|------|--------|
| S1 | 1 | 1 | 2 | 25% |
| S2 | 0 | 1 | 3 | 0% |
| S3~S8 | 0 | 0 | 24 | 0% |
| **전체** | **1** | **2** | **29** | **3.1%** |

### 최근 작업
- ✅ S1-A1 완성 (세션 03)
- 🔄 S1-A2 수정 중 (세션 05)
- 🚀 S2-A1 시작 예정

---

## 📚 핵심 문서 링크

### 필독 문서
1. [S1 철학적 재해석](/docs/sessions/Session03_S1_Philosophy.md) - S1의 깊은 통찰
2. [8×4 매트릭스 이론](8x4_Matrix_Theory_Guide.md) - 전체 이론 체계
3. [모듈 템플릿](modules/MODULE_TEMPLATE.md) - 작성 표준

### 참고 문서
- [프로젝트 현황](/PROJECT_STATUS.md)
- [세션 시작 가이드](/SESSION_START_GUIDE.md)
- [서비스 구조](/docs/theory/IWL_Service_Structure_Guide.md)

---

## 💡 작업 원칙

### S1-S2-S3 구분
- **S1**: 점 - "있는 그대로" (순수한 감각)
- **S2**: 선 - "연결하되 판단 않음" (관계 발견)
- **S3**: 면 - "패턴과 규칙" (구조 인식)

### 레벨 시스템
- **L1**: 그림책 (많은 정보, 쉬운 인식)
- **L3**: 중간 복잡도
- **L5**: 소설 (적은 정보, 깊은 상상)

---

**최종 업데이트**: 2025-08-16
**다음 작업**: S1-A2 수정, S2-A1 설계
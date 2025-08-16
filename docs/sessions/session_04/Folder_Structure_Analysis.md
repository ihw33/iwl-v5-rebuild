# 📁 폴더 구조 차이점 분석

## 🔍 현재 실제 폴더 구조 vs 제안한 구조

### 현재 실제 구조
```
iwl-v5-rebuild/
├── docs/
│   ├── DECISIONS/
│   ├── planning/
│   ├── programs/         ✅ (통합 프로그램)
│   ├── sessions/         ❌ (세션 기록은 /sessions에)
│   ├── templates/        ✅
│   └── theory/           ✅
├── modules/              ✅ (개별 모듈 설계)
│   ├── S1-A1/
│   └── S2-A1/
├── sessions/             ✅ (세션 관리)
├── meetings/             ✅
├── ai_prompts/           ✅
└── (기타 프로젝트 파일들)
```

### 차이점 정리

#### 1. ✅ 일치하는 부분
- `/docs/theory/` - 이론 문서들
- `/docs/templates/` - 템플릿들
- `/docs/programs/` - 통합 프로그램
- `/modules/` - 개별 모듈 설계
- `/sessions/` - 세션 관리
- `/ai_prompts/` - AI 프롬프트

#### 2. ❌ 다른 부분
- `/docs/sessions/` → 실제로는 `/sessions/`에 저장
  - Session03_S1_Philosophy.md는 `/docs/sessions/`에 있음
  - 하지만 실제 세션 작업은 `/sessions/`에서 진행

#### 3. 📝 현재 작업 상태
```
✅ 완료된 것:
- /docs/theory/S1_Complete_Guide.md
- /docs/programs/S1_Integrated_Program.md
- /modules/S1-A1/module_design.md
- /sessions/session_04/B0_Matrix_Draft.md
- /sessions/session_04/S2_Detailed_Design.md
- /sessions/session_04/S2_Redefined_Design.md

⏳ 필요한 것:
- /modules/S1-A2/ (설계 필요)
- /modules/S1-A3/ (설계 필요)  
- /modules/S1-A4/ (설계 필요)
- /modules/S2-A2~A4/ (설계 필요)
```

---

## 🎯 정리된 폴더 구조 (현재 기준)

### 이론과 개념 (/docs/theory/)
- 8×4 매트릭스 이론
- 서비스 구조 가이드
- S1~S8 완전 가이드

### 템플릿 (/docs/templates/)
- B0 표준 템플릿
- 설문 시스템
- 페르소나 예시

### 통합 프로그램 (/docs/programs/)
- S1 통합 프로그램 (20-30분)
- S2 통합 프로그램 (예정)

### 개별 모듈 설계 (/modules/)
- S1-A1/ (완료)
- S1-A2~A4/ (필요)
- S2-A1~A4/ (필요)

### 세션 작업 (/sessions/)
- session_03/ (S1 작업)
- session_04/ (S2 작업 중)

---

## 📌 권장 사항

1. **세션 기록 통일**
   - `/docs/sessions/`와 `/sessions/` 중 하나로 통일
   - 권장: `/sessions/`에 모든 세션 작업 보관

2. **모듈 설계 완성**
   - S1-A2, A3, A4 설계서 작성
   - S2-A1~A4 설계서 작성

3. **문서 연결성**
   - 각 문서에 관련 문서 링크 추가
   - README에 전체 구조도 추가

이제 명확해졌나요?
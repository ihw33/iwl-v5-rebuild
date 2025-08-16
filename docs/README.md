# 📁 Docs 디렉토리 가이드

## 📋 개요
IWL v5.0 프로젝트의 모든 문서를 체계적으로 관리합니다.

---

## 🗂️ 폴더 구조 및 용도

### 📊 `/8x4-matrix/` - 핵심 매트릭스
**8×4 매트릭스 관련 모든 파일**
- 이론 문서 (Theory Guides)
- 32개 모듈 설계 (`/modules/`)
- 통합 프로그램 (`/programs/`)
- [상세 보기](8x4-matrix/README.md)

### 📝 `/sessions/` - 세션 작업
**Claude 세션별 작업 기록**
- 세션별 작업 파일 (`session_XX/`)
- 세션 인수인계 문서
- 철학적 통찰 기록
- 현재: 세션 05 진행 중

### 📚 `/theory/` - 일반 이론
**매트릭스 외 이론 문서**
- IWL_Service_Structure_Guide.md
- 기타 이론 문서

### 🎨 `/templates/` - 템플릿
**각종 템플릿 파일**
- B0 템플릿 (초안)
- 사고 성향 파일들
- UI/UX 템플릿

### 📋 `/planning/` - 기획
**기획 및 제안 문서**
- Issue 제출 문서
- 프로젝트 기획안

### 🗄️ `/DECISIONS/` - 의사결정
**프로젝트 결정 사항 기록**
- 아키텍처 결정
- 설계 결정 기록

---

## 🎯 빠른 찾기

### 자주 찾는 문서
| 문서 | 위치 | 용도 |
|------|------|------|
| 8×4 이론 | `/8x4-matrix/8x4_Matrix_Theory_Guide.md` | 전체 이론 |
| 모듈 템플릿 | `/8x4-matrix/modules/MODULE_TEMPLATE.md` | 모듈 작성 |
| S1 철학 | `/sessions/Session03_S1_Philosophy.md` | S1 통찰 |
| 서비스 구조 | `/theory/IWL_Service_Structure_Guide.md` | 서비스 흐름 |

### 최신 작업
- S1-A2 모듈 수정 중
- S2-A1 모듈 시작 예정
- 세션 05 진행 중

---

## 📌 작업 시 주의사항

### 파일 저장 위치
- **8×4 관련** → `/8x4-matrix/`
- **세션 작업** → `/sessions/session_XX/`
- **일반 이론** → `/theory/`
- **템플릿** → `/templates/`

### 명명 규칙
- 모듈: `S[X]-A[Y]-module_design.md`
- 세션: `Session[XX]_[내용].md`
- 이론: `[주제]_Guide.md`

---

## 🔗 상위 문서
- [프로젝트 현황](/PROJECT_STATUS.md)
- [세션 시작 가이드](/SESSION_START_GUIDE.md)

---

**최종 업데이트**: 2025-08-16
**관리**: PM Claude
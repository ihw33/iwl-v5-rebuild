# 📚 Wiki 관리 체계

## 👤 Wiki 관리 조직

### 1. 주 관리자: PM Claude
**책임**:
- Wiki 전체 구조 설계 및 관리
- 카테고리/네비게이션 관리
- 정기적 업데이트 및 검토
- 관리 가이드라인 수립

### 2. 섹션별 담당자

| Wiki 섹션 | 담당자 | 책임 영역 | 주요 문서 |
|-----------|--------|----------|----------|
| **이론 체계** | Cursor (기획팀) | A 시리즈 문서화 | - 8단계 정의<br>- 4개 축 설명<br>- 8×4 매트릭스 |
| **커리큘럼** | Gemini | B 시리즈 문서화 | - 레슨 템플릿<br>- 교육 콘텐츠<br>- 평가 도구 |
| **기술 문서** | Codex | 기술 스펙 | - API 문서<br>- DB 스키마<br>- 아키텍처 |
| **사용자 가이드** | QA Claude | 사용법 | - 설치 가이드<br>- 사용 매뉴얼<br>- FAQ |
| **프로세스** | PM Claude | 운영 문서 | - 워크플로<br>- 팀 가이드<br>- 프로세스 |

---

## 📝 Wiki 업데이트 프로세스

```mermaid
graph LR
    A[콘텐츠 확정] --> B[담당자 초안 작성]
    B --> C[PM 검토]
    C --> D[Wiki 업데이트]
    D --> E[변경 로그 작성]
    E --> F[팀 공지]
```

### 상세 절차:
1. **콘텐츠 확정**
   - Issue/Discussion에서 내용 승인
   - Thomas 최종 승인 (필요시)

2. **초안 작성**
   - 담당자가 markdown 형식으로 작성
   - 템플릿 준수

3. **PM 검토**
   - 구조 일관성 확인
   - 네비게이션 연결 확인
   - 스타일 가이드 준수 확인

4. **Wiki 업데이트**
   - GitHub 웹에서 직접 편집
   - 또는 git clone → 편집 → push

5. **변경 로그**
   - 주요 변경사항 기록
   - 날짜와 작성자 명시

6. **팀 공지**
   - Discussions > Announcements
   - 중요 변경사항 알림

---

## 📋 Wiki 관리 원칙

### 1. 콘텐츠 원칙
- ✅ **확정된 내용만**: Issue에서 승인된 내용
- ✅ **단일 진실원**: 한 정보는 한 곳에만
- ✅ **최신 유지**: 정기적 업데이트
- ❌ **작업 중 문서 금지**: 완성된 문서만

### 2. 구조 원칙
- **계층적 구조**: 최대 3단계 깊이
- **명확한 네비게이션**: 모든 페이지 연결
- **일관된 템플릿**: 섹션별 통일된 형식
- **검색 가능**: 명확한 제목과 태그

### 3. 스타일 가이드
- **제목**: 명확하고 간결하게
- **목차**: 긴 문서는 TOC 필수
- **코드 블록**: 언어 명시
- **링크**: 상대 경로 사용
- **이미지**: 설명 텍스트 포함

---

## 🗓️ Wiki 관리 일정

### 일일
- 새로운 확정 내용 업데이트
- 깨진 링크 확인

### 주간
- 섹션별 담당자 업데이트
- 신규 문서 추가

### 월간 (매월 첫째 주)
- 전체 Wiki 검토
- 구조 개선
- 오래된 내용 업데이트
- 사용 통계 분석

---

## 📂 Wiki 구조 (계획)

```
Home
├── Getting Started
│   ├── Installation
│   ├── Quick Start
│   └── Configuration
├── Theory
│   ├── 8-Stages
│   ├── 4-Axes
│   └── 8x4-Matrix
├── Curriculum
│   ├── Lesson-Templates
│   ├── Core-Lessons
│   └── Assessment
├── Technical
│   ├── API-Reference
│   ├── Database-Schema
│   └── Architecture
├── Guides
│   ├── User-Manual
│   ├── Admin-Guide
│   └── Developer-Guide
└── About
    ├── Team
    ├── Process
    └── Contributing
```

---

## 🚀 즉시 실행 사항

### 1. Wiki 초기화 (PM Claude)
```bash
# GitHub 웹에서
1. Settings > Features > Wikis 확인
2. Create the first page
3. 기본 구조 생성
```

### 2. 담당자 공지 (PM Claude)
- 각 담당자에게 역할 안내
- Wiki 편집 권한 확인
- 첫 문서 작성 요청

### 3. 템플릿 생성 (QA Claude)
- 페이지 템플릿
- 스타일 가이드
- 예시 문서

---

## 📞 문의 및 지원

- **Wiki 관련 질문**: Discussions > Q&A
- **수정 요청**: Issue 생성
- **긴급 사항**: PM Claude에게 직접

---

**발효일**: 2025-08-14
**작성자**: PM Claude
**승인자**: Thomas
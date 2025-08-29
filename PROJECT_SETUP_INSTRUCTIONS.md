# 📊 GitHub Project 설정 안내

## ✅ 완료된 작업
- 주요 Issue 7개 프로젝트에 추가 완료

## 🔧 웹에서 직접 설정 필요

### 1. 프로젝트 접속
https://github.com/users/ihw33/projects/1

### 2. 컬럼 생성 (+ 버튼 클릭)
1. **📋 Backlog** 
2. **🚀 Ready**
3. **🔄 In Progress**
4. **👀 In Review**
5. **✅ Done**

### 3. Custom Fields 추가 (⚙️ Settings)

#### Priority 필드
- Type: Single select
- Options:
  - 🔴 Critical
  - 🟡 High
  - 🟢 Normal
  - ⚪ Low

#### Team 필드
- Type: Single select
- Options:
  - 기획 (Cursor)
  - 문서 (Cursor)
  - 백엔드 (Codex)
  - 교육 (Gemini)
  - QA
  - PM

#### Status 필드
- Type: Single select
- Options:
  - Not Started
  - In Progress
  - Blocked
  - Review
  - Complete

#### Progress 필드
- Type: Number
- Format: Percentage

### 4. 현재 Issue 분류

#### 🔄 In Progress
- #12: A4 매트릭스 (기획팀) - 50%
- #27: Wiki 관리 체계 (PM)

#### 👀 In Review
- #23: AI 협업 제안 (needs-thomas)
- #21: A1/A3 학술 용어

#### 📋 Backlog
- #25: Persona×Level 정의
- #26: module_meta 스키마

#### ✅ Done
- #22: GitHub 시스템 구축

### 5. 자동화 설정 (Workflows)

#### When issues are added
- Set Status → Backlog

#### When issues are closed
- Set Status → Done
- Move to Done column

### 6. View 생성

#### Board View (기본)
- Group by: Column
- Filter: is:open

#### Team View
- Group by: Team
- Sort by: Priority

#### Priority View
- Group by: Priority
- Sort by: Updated

---

## 📝 각 Issue별 설정값

| Issue | Team | Priority | Progress | Status |
|-------|------|----------|----------|--------|
| #12 | 기획 | 🔴 Critical | 50% | In Progress |
| #23 | 기획 | 🟡 High | 90% | Review |
| #21 | 기획 | 🟢 Normal | 0% | Backlog |
| #27 | PM | 🟡 High | 30% | In Progress |
| #25 | 기획 | 🟢 Normal | 0% | Backlog |
| #26 | 기획 | 🟢 Normal | 0% | Backlog |
| #22 | PM | ✅ | 100% | Done |

---

**작성**: PM Claude
**날짜**: 2025-08-14
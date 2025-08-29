# 📊 GitHub Projects 설정 가이드

## 🎯 프로젝트 보드 구성

### 1. 메인 칸반 보드

#### 컬럼 구조
```
📋 Backlog → 🚀 Ready → 🔄 In Progress → 👀 In Review → ✅ Done
```

- **Backlog**: 모든 새 Issue (자동 추가)
- **Ready**: 작업 준비 완료 (담당자 지정됨)
- **In Progress**: 현재 작업 중
- **In Review**: PM/Thomas 검토 대기
- **Done**: 완료 (자동 이동)

### 2. 커스텀 필드 추가

#### Priority (단일 선택)
- 🔴 Critical
- 🟡 High  
- 🟢 Normal
- ⚪ Low

#### Team (단일 선택)
- 기획 (Cursor)
- 문서 (Cursor)
- 백엔드 (Codex)
- 교육 (Gemini)
- QA (QA Claude)
- PM (PM Claude)

#### Phase (단일 선택)
- Phase 1: A Series
- Phase 2: B Series
- Phase 3: MVP

#### Progress (숫자)
- 0-100% 진행률

#### Due Date (날짜)
- 마감일 설정

### 3. 자동화 규칙

#### 자동 이동
- Issue 생성 → Backlog
- Assignee 지정 → Ready
- 'in-progress' 라벨 → In Progress
- 'needs-review' 라벨 → In Review
- Issue closed → Done

#### 자동 라벨
- Due Date 임박 (3일) → 'urgent' 라벨
- Priority Critical → 'high-priority' 라벨

### 4. 뷰 (Views) 설정

#### 📊 Dashboard View (기본)
- 칸반 보드
- 모든 Issue 표시

#### 👥 Team View
- Team별 그룹화
- 각 팀 작업 현황

#### 📅 Timeline View
- 간트 차트
- Phase별 일정

#### 🎯 Priority View
- Priority별 정렬
- Critical/High 우선

### 5. 프로젝트 설정 방법

#### Step 1: 프로젝트 접속
```bash
gh browse --repo ihw33/iwl-v5-rebuild projects
```
또는 https://github.com/users/ihw33/projects/1

#### Step 2: Settings 클릭
- Custom fields 추가
- Workflows 설정

#### Step 3: 컬럼 생성
- + New column으로 5개 컬럼 추가
- 각 컬럼 이름과 한계 설정

#### Step 4: 자동화 설정
- Workflows → Item added to project
- 조건과 액션 설정

### 6. 사용 예시

#### Issue 생성 시
```bash
gh issue create --title "작업 제목" \
  --project "IWL v5.0 Dashboard" \
  --label "feature" \
  --assignee "@me"
```

#### 프로젝트에서 Issue 확인
```bash
gh project item-list 1 --owner ihw33
```

### 7. 팀별 활용법

#### PM Claude
- 매일 아침 보드 확인
- Backlog → Ready 이동
- 우선순위 조정

#### 개발팀
- Ready에서 작업 선택
- In Progress로 이동
- 완료 시 In Review로

#### Thomas
- In Review 항목 검토
- 승인 시 Done으로
- 피드백 시 In Progress로

---

## 📈 성과 측정

### 주간 메트릭
- 완료 Issue 수
- 평균 처리 시간
- 팀별 생산성

### 월간 리포트
- Phase 완성도
- 블로커 분석
- 개선 제안

---

**작성일**: 2025-08-14
**담당**: PM Claude
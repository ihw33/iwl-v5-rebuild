# GitHub 활용 가이드

## 🎯 우리 프로젝트의 GitHub 구조

### 4가지 핵심 도구
1. **Issues** - 작업 및 버그 추적
2. **Discussions** - 아이디어 및 토론
3. **Projects** - 칸반 보드 관리
4. **Wiki** - 문서화

## 📝 Issues 사용법

### Issue 생성
```bash
# 일반 작업
gh issue create --title "제목" --body "내용"

# 제안사항
gh issue create --title "[제안] 제목" --label "proposal,needs-review"

# 버그 리포트
gh issue create --title "[버그] 제목" --label "bug"
```

### Issue 관리
```bash
# 내 작업 보기
gh issue list --assignee @me

# 열린 이슈 보기
gh issue list --state open

# 특정 라벨 검색
gh issue list --label "needs-review"
```

## 💬 Discussions 사용법

### Discussion 카테고리
- **📢 Announcements** - 공지사항 (PM만)
- **💡 Ideas** - 아이디어 제안
- **🎯 Planning** - 기획 토론
- **📚 Learning** - 교육 콘텐츠
- **❓ Q&A** - 질문과 답변

### Discussion 생성
```bash
# 아이디어 제안
gh discussion create --category "Ideas" --title "제목" --body "내용"

# 질문하기
gh discussion create --category "Q&A" --title "질문" --body "내용"
```

## 📊 Projects 사용법

### 프로젝트 보드 접속
- URL: https://github.com/users/ihw33/projects/1
- 이름: IWL v5.0 Dashboard

### 칸반 보드 상태
1. **📋 Todo** - 해야 할 일
2. **🔄 In Progress** - 진행 중
3. **👀 In Review** - 검토 중
4. **✅ Done** - 완료

### CLI로 프로젝트 관리
```bash
# 프로젝트 보기
gh project list --owner ihw33

# 프로젝트에 이슈 추가
gh project item-add 1 --owner ihw33 --url [issue-url]
```

## 📚 Wiki 사용법

### Wiki 접속
- 웹: https://github.com/ihw33/iwl-v5-rebuild/wiki
- 로컬 편집:
```bash
git clone https://github.com/ihw33/iwl-v5-rebuild.wiki.git
cd iwl-v5-rebuild.wiki
```

### Wiki 페이지 작성
1. 마크다운 파일 생성 (예: `New-Page.md`)
2. 내용 작성
3. Git 커밋 및 푸시
```bash
git add New-Page.md
git commit -m "Add new page"
git push
```

## 🏷️ 라벨 시스템

### 주요 라벨
| 라벨 | 용도 | 색상 |
|------|------|------|
| `proposal` | 제안사항 | 🟢 |
| `needs-review` | PM 검토 필요 | 🟡 |
| `needs-thomas` | 최종 승인 필요 | 🔴 |
| `bug` | 버그 | 🔴 |
| `enhancement` | 개선사항 | 🔵 |
| `documentation` | 문서화 | 📘 |
| `A-series` | A 시리즈 작업 | 🟣 |
| `B-series` | B 시리즈 작업 | 🟠 |

## 🎯 마일스톤

### Phase 1: A 시리즈
- 기한: 2025-08-20
- 작업: A0 ~ A8

### Phase 2: B 시리즈
- 기한: 2025-08-27
- 작업: B0 ~ B5

## 🔄 워크플로우

### 1. 아이디어 단계
```
Discussions(Ideas) → 토론 → 승인
```

### 2. 계획 단계
```
승인 → Issue 생성 → Projects 등록
```

### 3. 실행 단계
```
Todo → In Progress → Review → Done
```

### 4. 문서화 단계
```
완료 → Wiki 업데이트 → 공지
```

## 📋 일일 체크리스트

### 아침 루틴
- [ ] Issue 확인: `gh issue list --assignee @me`
- [ ] Discussion 확인: 웹에서 확인
- [ ] Project 보드 확인: 칸반 상태 체크

### 저녁 루틴
- [ ] 작업 Issue 업데이트
- [ ] 완료 작업 Done으로 이동
- [ ] Wiki 문서 업데이트

## 💡 팁과 트릭

### 빠른 검색
```bash
# 오늘 생성된 이슈
gh issue list --search "created:>2025-08-14"

# 내가 댓글 단 이슈
gh issue list --search "commenter:@me"

# 긴급 작업
gh issue list --label "urgent"
```

### 일괄 작업
```bash
# 여러 이슈에 라벨 추가
gh issue edit 1,2,3 --add-label "needs-review"

# 여러 이슈 할당
gh issue edit 1,2,3 --add-assignee "@me"
```

## 🚨 문제 해결

### gh 명령어 안 될 때
```bash
# GitHub CLI 인증
gh auth login

# 상태 확인
gh auth status
```

### 권한 문제
```bash
# 저장소 권한 확인
gh api repos/ihw33/iwl-v5-rebuild

# 협업자 확인
gh api repos/ihw33/iwl-v5-rebuild/collaborators
```

---

**작성**: QA Claude
**최종 수정**: 2025-08-14
# 📥 팀원 제안 프로세스 가이드

## 🎯 목적
팀원들의 창의적 아이디어와 개선 제안을 체계적으로 관리하고 실행하기 위한 프로세스

## 📋 제안 프로세스

### 1단계: Issue 생성
```bash
# GitHub Web에서
1. Issues → New Issue → "팀원 제안" 템플릿 선택
2. 제목: [제안] 구체적인 제안 내용
3. 내용 작성 (템플릿 따라)
4. Submit

# 또는 CLI로
gh issue create -R ihw33/iwl-v5-rebuild \
  --title "[제안] 제안 제목" \
  --label "proposal,needs-review" \
  --body "제안 내용"
```

### 2단계: PM 검토
- PM Claude가 제안 검토
- 24시간 내 피드백 제공
- 검토 결과:
  - ✅ 승인 → Thomas 최종 검토
  - 📝 보완 필요 → 피드백 제공
  - ❌ 기각 → 사유 설명

### 3단계: Thomas 최종 승인
- 주요 변경사항은 Thomas 승인 필요
- 승인 시 실행 Issue 생성

## 🏷️ 라벨 시스템

| 라벨 | 설명 | 색상 |
|------|------|------|
| `proposal` | 팀원 제안사항 | 🟢 녹색 |
| `needs-review` | PM 검토 필요 | 🟡 노란색 |
| `needs-thomas` | Thomas 결정 필요 | 🔴 빨간색 |
| `approved` | 승인됨 | 🔵 파란색 |
| `declined` | 기각됨 | ⚫ 회색 |

## 📊 제안 유형별 승인 권한

| 제안 유형 | 예시 | PM 권한 | Thomas 승인 |
|-----------|------|---------|-------------|
| 작업 개선 | 코드 스타일, 문서 개선 | ✅ 직접 승인 가능 | ❌ 불필요 |
| 도구 도입 | 새 라이브러리, 도구 | ⚠️ 검토 후 상신 | ✅ 필수 |
| 구조 변경 | 아키텍처, DB 스키마 | ❌ 검토만 | ✅ 필수 |
| 새 기능 | 스펙 외 기능 추가 | ❌ 검토만 | ✅ 필수 |
| 프로세스 | 업무 방식 변경 | ⚠️ 검토 후 상신 | ✅ 필수 |

## 💡 좋은 제안의 예시

### ✅ 좋은 제안
```markdown
## 제안 배경
현재 Stage 작업 제출 시 포맷이 일관되지 않아 검토 시간이 오래 걸림

## 제안 내용
표준 Stage 제출 템플릿 만들어서 Issue 템플릿으로 등록

## 기대 효과
- 검토 시간 50% 단축
- 일관된 품질 확보
- 팀원 작업 편의성 향상
```

### ❌ 개선이 필요한 제안
```markdown
## 제안 배경
그냥 불편함

## 제안 내용
다 바꾸자

## 기대 효과
좋아질 것 같음
```

## 🚀 빠른 시작

### 제안하기
```bash
# 제안 Issue 생성
gh issue create --template proposal.md

# 제안 목록 보기
gh issue list --label "proposal"

# 내 제안 확인
gh issue list --author "@me" --label "proposal"
```

### PM 명령어 (검토용)
```bash
# 검토 대기 제안 보기
gh issue list --label "proposal,needs-review"

# Thomas 승인 대기
gh issue list --label "needs-thomas"

# 승인된 제안
gh issue list --label "proposal,approved"
```

## 📈 제안 통계
```bash
# 이번 주 제안
gh issue list --label "proposal" --search "created:>2025-08-11"

# 승인율 확인
gh issue list --label "proposal,approved" --json number | jq length
```

---

**문의**: PM Claude 또는 Thomas
**최종 수정**: 2025-08-14
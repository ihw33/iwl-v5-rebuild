# 🚀 IWL v5 간단한 오케스트레이션 (빌드 단계 전용)

## 📌 핵심 원칙
- **수동 조율 최소화**: 각 Claude가 독립적으로 작업 확인
- **GitHub Issue 하나로 관리**: 체크리스트 기반 진행
- **빌드 완료 후 폐기**: 임시 운영 시스템

## 🎯 작동 방식

### 1. Master Issue 생성 (한 번만)
```bash
# iwl-v5-rebuild 레포에서 실행
gh issue create --title "🏗️ Build Phase Orchestration" --body "$(cat <<'EOF'
# IWL v5 Build Phase Task Board

## 📋 Main Platform Tasks
- [ ] Database Schema 설계
- [ ] Auth System 구축
- [ ] API Gateway 설정
- [ ] UI Components 생성

## 📚 Knowledge Base Tasks
- [ ] 콘텐츠 구조 설계
- [ ] Vector DB 설정
- [ ] 임베딩 파이프라인
- [ ] 검색 API 구현

## 🤖 LLM Tasks
- [ ] 모델 선택/설정
- [ ] Fine-tuning 데이터 준비
- [ ] Inference API 구축
- [ ] 프롬프트 템플릿

## 🔄 Integration Points
- [ ] KB ↔ Main: API 연결
- [ ] LLM ↔ Main: 서비스 통합
- [ ] KB ↔ LLM: RAG 파이프라인

---
각 Claude는 작업 시작 전 이 이슈를 확인하고,
완료 시 체크박스를 업데이트합니다.
EOF
)"
```

### 2. 각 Claude의 작업 방식

#### Claude 1 (Main Platform)
```bash
# 작업 시작 시
gh issue view 1 -R ihw33/iwl-v5-rebuild  # 현재 상태 확인
# "Database Schema 설계" 작업 진행
gh issue edit 1 --body "..." # 체크박스 업데이트
```

#### Claude 2 (Knowledge Base)
```bash
# 동일한 Master Issue 확인
gh issue view 1 -R ihw33/iwl-v5-rebuild
# KB 관련 작업만 수행
```

#### Claude 3 (LLM)
```bash
# 동일한 Master Issue 확인
gh issue view 1 -R ihw33/iwl-v5-rebuild
# LLM 관련 작업만 수행
```

### 3. 간단한 동기화 스크립트 (선택사항)

```bash
#!/bin/bash
# check_status.sh - 각 Claude가 실행

ISSUE_NUM=1
REPO="ihw33/iwl-v5-rebuild"

# 현재 상태 확인
echo "🔍 Checking current status..."
gh issue view $ISSUE_NUM -R $REPO

# 내가 할 수 있는 작업 찾기
echo "🎯 Available tasks for me:"
gh issue view $ISSUE_NUM -R $REPO | grep -E "^\- \[ \]" | head -3

# 작업 완료 시 체크박스 업데이트
# gh issue edit $ISSUE_NUM -R $REPO --body "..."
```

## 💡 사용 예시

### Thomas (사용자)가 할 일:
1. Master Issue 생성 (한 번만)
2. 각 Claude에게 역할 지정:
   - "너는 Main Platform 담당"
   - "너는 KB 담당"
   - "너는 LLM 담당"

### 각 Claude가 할 일:
```markdown
1. Master Issue 확인
2. 자기 영역 작업 선택
3. 작업 수행
4. 체크박스 업데이트
5. 다음 작업 확인
```

## 🔧 더 간단한 대안: 로컬 파일 방식

```bash
# tasks.md 파일로 관리 (Git으로 동기화)
cat > /Users/m4_macbook/Projects/iwl-v5-rebuild/BUILD_TASKS.md << 'EOF'
# Build Tasks

## In Progress
- [Claude 1] Database Schema 설계

## Todo
- Auth System 구축
- API Gateway 설정
- 콘텐츠 구조 설계
- Vector DB 설정

## Done
- 프로젝트 초기 설정
EOF

# 각 Claude가 파일 업데이트 후 commit
git add BUILD_TASKS.md
git commit -m "Claude 1: Database Schema 완료"
git push
```

## 🎯 핵심 장점
1. **설정 불필요**: GitHub Issue 하나면 끝
2. **실시간 확인**: 모든 Claude가 같은 Issue 확인
3. **충돌 없음**: 각자 영역만 작업
4. **히스토리 관리**: Issue 댓글로 자동 기록

## ⚡ 빠른 시작
```bash
# 1. Master Issue 생성
gh issue create --title "Build Tasks" --body "..."

# 2. 각 Claude에서 확인
gh issue view 1

# 3. 작업하고 업데이트
# 끝!
```

---
**이 방식은 빌드 단계만을 위한 임시 방법입니다.**
**서비스 운영 시에는 필요 없습니다.**
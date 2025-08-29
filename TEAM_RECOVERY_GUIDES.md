# 🚨 AI 팀원별 재시작 복구 가이드

## 1. Cursor (콘텐츠 기획) 복구 가이드

### 당신이 Cursor 기획팀이라면:
```bash
# 1. 자신의 작업 확인
gh issue list -R ihw33/iwl-v5-rebuild --assignee @me
gh issue list -R ihw33/iwl-v5-rebuild --label theory

# 2. 현재 작업 중인 Issue 확인
gh issue view 12 -R ihw33/iwl-v5-rebuild --comments | tail -20

# 3. 팀 문서 확인
cat AI_TEAM_ROLES.md | grep -A 5 "Cursor"
```

**당신의 역할**: 콘텐츠 기획, 아키텍처 설계
**현재 작업**: A4 (8×4 매트릭스) - Stage 2 진행 중
**보고 대상**: PM Claude → Thomas

---

## 2. Codex (백엔드) 복구 가이드

### 당신이 Codex 백엔드팀이라면:
```bash
# 1. 백엔드 관련 Issue 확인
gh issue list -R ihw33/iwl-v5-rebuild --label backend

# 2. API 스펙 문서 위치
ls -la docs/api/
cat docs/api/README.md 2>/dev/null

# 3. 데이터베이스 스키마 확인
cat prisma/schema.prisma 2>/dev/null
```

**당신의 역할**: 백엔드, API, 데이터베이스
**현재 상태**: 대기 중 (프론트엔드 설계 완료 후 시작)
**보고 대상**: PM Claude → Thomas

---

## 3. Gemini (교육 시나리오) 복구 가이드

### 당신이 Gemini 교육팀이라면:
```bash
# 1. 커리큘럼 Issue 확인
gh issue list -R ihw33/iwl-v5-rebuild --label curriculum

# 2. B 시리즈 작업 확인
for i in {13..18}; do
  echo "=== Issue #$i ==="
  gh issue view $i -R ihw33/iwl-v5-rebuild --json title,state
done
```

**당신의 역할**: 콘텐츠 기획, 교육 시나리오, UX 설계
**현재 상태**: B0-B5 대기 중 (A 시리즈 완료 후)
**보고 대상**: PM Claude → Thomas

---

## 4. VSCode Claude (프론트엔드) 복구 가이드

### 당신이 VSCode Claude 프론트엔드팀이라면:
```bash
# 1. 컴포넌트 구조 확인
ls -la src/components/
ls -la src/app/

# 2. 디자인 시스템 확인
cat tailwind.config.js
cat src/styles/globals.css
```

**당신의 역할**: 프론트엔드 컴포넌트, UI 구현
**현재 상태**: 프로젝트 초기 설정 완료
**보고 대상**: PM Claude → Thomas

---

## 5. 백서팀 (특별 작업) 복구 가이드

### 당신이 백서 작성팀이라면:
```bash
# 1. 백서 Issue 확인
gh issue view 20 -R ihw33/iwl-v5-rebuild --comments

# 2. 백서 문서 위치
cat docs/whitepaper/IWL_Original_Model_v0.1.md

# 3. IP 보호 작업 확인
gh issue view 19 -R ihw33/iwl-v5-rebuild
```

**당신의 역할**: 백서 작성, IP 보호 문서화
**현재 작업**: PDF 변환 + 타임스탬프/해시 생성
**보고 대상**: PM Claude → Thomas

---

## 📋 공통 확인 사항

### 모든 팀원 공통:
```bash
# 1. 최신 팀 역할 확인
cat AI_TEAM_ROLES.md

# 2. 워크플로우 확인
cat AI_TEAM_WORKFLOW.md

# 3. 전체 Issue 현황
gh issue list -R ihw33/iwl-v5-rebuild --state all --limit 10
```

### 중요 원칙:
1. **모든 작업은 Issue 기반**
2. **최종 승인권자는 Thomas**
3. **PM Claude가 중간 검토**
4. **병렬 작업 적극 활용**
5. **막히면 즉시 Issue에 코멘트**

---

*이 문서를 보면 자신의 역할을 찾아 해당 복구 가이드를 따르세요.*
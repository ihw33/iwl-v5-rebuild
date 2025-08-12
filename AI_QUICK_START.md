# 🚀 AI 팀원 즉시 시작 가이드

## 📌 한 줄로 시작하기

각 AI는 아래 명령어 하나만 실행하면 자동으로 온보딩됩니다:

### 옵션 1: 자동 인식 (추천)
```bash
cat AI_TEAM_ONBOARDING.md && echo -e "\n\n당신의 역할을 확인하고 작업을 시작하세요."
```

### 옵션 2: 역할 지정
각 AI별로 아래 중 하나만 복사해서 붙여넣기:

```bash
# Cursor (ChatGPT-5)
echo "당신은 Cursor/ChatGPT-5/Architect입니다. 기획과 아키텍처를 담당합니다." && cat AI_TEAM_ONBOARDING.md

# Gemini
echo "당신은 Gemini/Content Designer입니다. 콘텐츠와 UX를 담당합니다." && cat AI_TEAM_ONBOARDING.md

# Codex
echo "당신은 Codex/Backend Dev입니다. 백엔드와 API를 담당합니다." && cat AI_TEAM_ONBOARDING.md

# VSCode Claude
echo "당신은 VSCode Claude/Frontend Dev입니다. 프론트엔드를 담당합니다." && cat AI_TEAM_ONBOARDING.md

# Copilot
echo "당신은 Copilot/Code Assistant입니다. 코드 자동완성을 담당합니다." && cat AI_TEAM_ONBOARDING.md

# FigmaMake
echo "당신은 FigmaMake/Design System입니다. 디자인 시스템을 담당합니다." && cat AI_TEAM_ONBOARDING.md

# PM Claude
echo "당신은 PM Claude입니다. 프로젝트 관리를 담당합니다." && cat AI_TEAM_ONBOARDING.md
```

---

## 🎯 더 간단한 방법: 마스터 프롬프트

아래 텍스트를 **한 번만** 복사해서 AI에게 전달:

```
당신은 IWL v5.0 프로젝트의 AI 팀원입니다.
프로젝트 위치: /Users/m4_macbook/iwl-v5-rebuild
GitHub: https://github.com/ihw33/iwl-v5-rebuild

다음 중 당신의 정체성을 선택하세요:
1. PM Claude → 프로젝트 관리
2. Cursor/ChatGPT-5 → 기획/아키텍처
3. Codex → 백엔드
4. Gemini → 콘텐츠/UX
5. VSCode Claude → 프론트엔드
6. Copilot → 코드 지원
7. FigmaMake → 디자인

선택 후 AI_TEAM_ONBOARDING.md를 읽고 작업을 시작하세요.
```

---

## 💡 가장 효율적인 방법

### 1. 범용 시작 명령어 (모든 AI 공통)
```bash
# 프로젝트로 이동하고 온보딩 문서 표시
cd /Users/m4_macbook/iwl-v5-rebuild && ls -la && cat AI_TEAM_ONBOARDING.md | head -50
```

### 2. 역할 자동 감지 프롬프트
```
이 프로젝트에서 작업하고 있는 AI입니다.
내가 어떤 역할인지 AI_TEAM_ROLES.md를 보고 판단해주세요.
그리고 해당 역할에 맞는 작업을 시작하겠습니다.
```

---

## 🔄 팀 전체 동기화 (PM Claude 전용)

PM Claude가 모든 AI에게 한 번에 공지할 때:

```bash
# GitHub Issue 생성으로 전체 공지
gh issue create --title "🔔 전체 AI 팀 공지" --body "모든 AI는 AI_TEAM_ONBOARDING.md를 확인하고 각자 역할에 맞는 작업을 시작하세요. @Cursor @Gemini @Codex @VSCode @Copilot @FigmaMake"
```

---

## ⚡ 즉시 작업 시작

온보딩 없이 바로 작업 시작:

```bash
# 현재 이슈 확인
gh issue list --assignee @me

# 개발 서버 실행
npm run dev

# 최신 코드 받기
git pull origin master
```

---

이제 긴 메시지 대신 이 파일 경로만 알려주면 됩니다:
**"AI_QUICK_START.md 파일을 확인하세요"**
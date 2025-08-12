# 🚀 IWL v5.0 - 생각정리 기술 3.0

> **8x4 매트릭스 기반 AI 협업 사고 훈련 시스템**

## 🤖 AI 팀원 필독!

**처음 시작하는 AI 팀원은 반드시 아래 문서를 먼저 읽어주세요:**

### 📌 [AI_TEAM_ONBOARDING.md](./AI_TEAM_ONBOARDING.md)
- 프로젝트 개요
- 당신의 역할 확인
- 작업 방법
- GitHub 협업 가이드

### 🎯 빠른 시작
1. **나는 누구?** → [AI_TEAM_ROLES.md](./AI_TEAM_ROLES.md)에서 역할 확인
2. **무엇을 해야 하나?** → [GitHub Issues](https://github.com/ihw33/iwl-v5-rebuild/issues) 확인
3. **어떻게 협업?** → Issue 댓글로 소통

---

## 📋 프로젝트 정보

- **GitHub**: https://github.com/ihw33/iwl-v5-rebuild
- **Tech Stack**: Next.js 15.4.6 + TypeScript + Tailwind CSS
- **Status**: 개발 진행 중
- **Local**: http://localhost:3001

## 🤖 AI 팀 구성 (7명)

| AI | 역할 | 주요 업무 |
|---|------|----------|
| PM Claude | 프로젝트 관리 | Git, 전체 조율 |
| Cursor (ChatGPT-5) | 기획/아키텍처 | 설계, 문서화 |
| Codex | 백엔드 | API, DB, 서버 |
| Gemini | 콘텐츠/UX | 교육, 시나리오 |
| VSCode Claude | 프론트엔드 | React, UI |
| Copilot | 코드 지원 | 자동완성 |
| FigmaMake | 디자인 | 컴포넌트 생성 |

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.

---

## 📚 프로젝트 문서

- [AI_TEAM_ONBOARDING.md](./AI_TEAM_ONBOARDING.md) - **필독! AI 팀원 온보딩 가이드**
- [AI_TEAM_ROLES.md](./AI_TEAM_ROLES.md) - AI 팀원별 역할 정의
- [CURSOR_SETUP_GUIDE.md](./CURSOR_SETUP_GUIDE.md) - Cursor CLI 설정
- [FIGMA_MAKE_GUIDE.md](./FIGMA_MAKE_GUIDE.md) - Figma 연동 가이드
- [CHATGPT_CLAUDE_SETUP.md](./CHATGPT_CLAUDE_SETUP.md) - AI 간 연동 설정

## 🔄 작업 플로우

1. **Issue 확인** → 할당된 작업 찾기
2. **브랜치 생성** → `feature/기능명` or `fix/버그명`
3. **코드 작성** → TypeScript, 주석 없이
4. **PR 생성** → 리뷰 요청
5. **머지** → master 브랜치에 통합

## 💬 협업 방법

### GitHub Issue 댓글로 소통
```markdown
@PM 이 작업 어떻게 진행할까요?
@Codex API 엔드포인트 확인 부탁해요
@VSCode 이 컴포넌트 UI 구현해주세요
```

---

> **마지막 업데이트**: 2025-08-12
> **PM**: Claude (Terminal)

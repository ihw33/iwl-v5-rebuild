# IWL v5.0 시스템 아키텍처 (초안)

## 개요
- 목표: 8x4 매트릭스 기반 학습/사고 훈련 시스템을 모듈화된 아키텍처로 구현
- 스택: Next.js 15.4.6, TypeScript, Tailwind CSS
- 운영: GitHub Issues/PR 기반, 7개 AI 협업

## 상위 구조
```
[App (Next.js)]
  ├─ UI Layer (app/, components/)
  ├─ Domain Layer (src/lib, src/types)
  ├─ Data Layer (src/data, remote APIs)
  └─ Integration (figma, MCP, analytics)
```

## 프론트엔드
- App Router 사용 (`src/app`)
- 디자인 시스템: Shadcn 기반 커스텀 컴포넌트(`src/components/ui/*`)
- 탭 네비게이션: `LessonTabs` 중심으로 8x4 매트릭스 네비게이션 확장 예정

## 인증 (계획)
- NextAuth.js (Auth.js) with Credentials + OAuth (Google) 옵션화
- 세션: JWT 전략, `middleware.ts`로 보호 라우팅
- 환경변수: `.env.local`에서 비밀키 관리

## 데이터 모델 (초안)
- User { id, email, name, role }
- MatrixItem { id, row, col, title, content, tags, progress }
- Progress { id, userId, itemId, status, updatedAt }

## API (초안)
- REST 우선, 필요 시 SSE/WS 확장
- 네임스페이스: `/api/auth/*`, `/api/matrix/*`, `/api/progress/*`

## 성능/품질
- E2E: Playwright, 단위: Vitest/Jest(결정 필요)
- ESLint + Prettier, CI에서 타입체크/빌드 확인

## 배포
- Vercel 우선, GitHub Actions로 CI 구축

## 열림 과제
- [ ] 인증 플로우 구체화
- [ ] 매트릭스 데이터 스키마 확정
- [ ] 상태관리 선택(Zustand/Redux/Server Actions)

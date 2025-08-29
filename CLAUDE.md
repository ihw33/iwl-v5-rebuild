## 📋 IWL v5.0 리빌드 프로젝트 (2025-08-11 업데이트)

### 🎯 프로젝트 전환 결정
- **배경**: 기존 FigmaMake 자동생성 코드의 한계로 인한 제어권 부족
- **결정**: 완전 새출발로 iwl-v5-rebuild 프로젝트 시작

### 🤖 새로운 AI 팀 구성 (8개 AI 협업) - 2025-08-13 업데이트
1. **PM Claude (터미널)**: 전체 관리, GitHub 조작, 프로젝트 조율
2. **Cursor CLI (ChatGPT-5)**: 콘텐츠 기획, 학습 시나리오, 사용자 스토리
3. **Codex CLI**: 백엔드, API, 데이터베이스, 서버 로직
4. **Gemini CLI**: 기술 아키텍처, 시스템 설계, API 스펙
5. **VSCode Claude**: 프론트엔드 컴포넌트, UI 구현
6. **GitHub Copilot**: 코드 자동생성, 반복 작업 지원
7. **FigmaMake**: 디자인 시스템, 초기 컴포넌트 생성
8. **QA Claude**: 품질관리, 테스트, 프론트엔드 수정

### 📋 재시작 시 복구 정보
- **현재 상태**: 계획 완료, 구현 시작 직전
- **다음 단계**: 새 프로젝트 생성 + CLI들 공지 + FigmaMake 새 시작
- **기존 프로젝트**: personal-journal-hub (백업 보관)
- **새 프로젝트**: iwl-v5-rebuild (Next.js + TypeScript + Tailwind)

### 🎯 즉시 진행할 작업들
1. 새 프로젝트 생성: `npx create-next-app iwl-v5-rebuild`
2. GitHub repo 생성: `gh repo create iwl-v5-rebuild`
3. CLI들 공지: Issue 생성으로 상황 설명
4. VSCode 환경 준비: `code iwl-v5-rebuild`
5. FigmaMake 새 프로젝트 시작

### 🎮 PM Claude 필수 체크사항 (새 세션 시작 시)

1. **즉시 확인할 것**:
   - `gh issue list --state open` - 진행 중인 Issue 확인
   - `AI_TEAM_WORKFLOW.md` - 팀 작업 프로세스 숙지
   - `AI_TEAM_ROLES.md` - 각 팀원 역할 확인
   - 최근 Issue 댓글들 확인

2. **PM 핵심 원칙**:
   - ❌ CLI에게 직접 지시 금지
   - ✅ 모든 작업은 GitHub Issue로 관리
   - ✅ CLI 작업 결과는 Issue 댓글로 받기
   - ✅ 피드백도 Issue 댓글로 제공

3. **일일 PM 루틴**:
   - Issue 상태 점검
   - 블로커 해결
   - 팀원 작업 조율
   - 진행 상황 모니터링

---

## 📋 이전 v.04 기획 미팅 안건

### 목적
- AI-Implementation v.04 채팅방 시작 전, 핵심 기획 문서 5개를 바탕으로 ChatGPT와 전략 회의 진행
- 실행 계획 구체화
- ChatGPT와의 미팅 결과 공유 및 의견 문서화
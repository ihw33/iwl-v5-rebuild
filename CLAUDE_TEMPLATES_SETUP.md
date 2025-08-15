# 🚀 Claude Code Templates 설정 가이드
**새 세션 시작 시 반드시 이 문서를 먼저 읽어주세요!**

## 📌 중요: 이 문서의 목적
이 문서는 Claude Code CLI의 성능을 향상시키고, 개발 생산성을 높이기 위한 템플릿 시스템 활용 가이드입니다.
새로운 Claude 세션이 시작될 때마다 이 문서를 참고하여 설정을 확인하세요.

---

## 🎯 현재 설치된 도구들

### 1. Claude Code Templates 전역 설치
```bash
# 설치 확인
claude-code-templates --version

# 재설치가 필요한 경우
npm install -g claude-code-templates@latest
```

### 2. 프로젝트 구조
```
iwl-v5-rebuild/
├── .claude/              # Claude 전용 설정
│   ├── agents/          # AI 에이전트들
│   ├── commands/        # 슬래시 커맨드
│   └── settings.json    # 프로젝트 설정
├── CLAUDE.md            # 프로젝트 컨텍스트 (기존)
└── CLAUDE_TEMPLATES_SETUP.md  # 이 문서
```

---

## 🤖 설정된 에이전트들

### 필수 에이전트 (`.claude/agents/`)

1. **nextjs-expert.md** - Next.js 전문가
   - App Router, SSR/SSG, API Routes
   - 사용: 라우팅, 서버 컴포넌트 문제

2. **react-optimizer.md** - React 최적화 전문가
   - 성능 최적화, 메모이제이션
   - 사용: 렌더링 최적화, 상태 관리

3. **typescript-expert.md** - TypeScript 전문가
   - 타입 정의, 제네릭, 유틸리티 타입
   - 사용: 타입 에러 해결

4. **qa-tester.md** - QA 및 테스트 전문가
   - 테스트 작성, 버그 찾기
   - 사용: 품질 검증

5. **code-reviewer.md** - 코드 리뷰 전문가
   - 베스트 프랙티스, 리팩토링
   - 사용: 코드 품질 개선

---

## 📝 설정된 커맨드들 (`.claude/commands/`)

### 개발 커맨드
```bash
/dev          # 개발 서버 시작 (npm run dev)
/build        # 프로덕션 빌드
/test         # 테스트 실행
/lint         # ESLint 실행
/typecheck    # TypeScript 체크
```

### 코드 생성 커맨드
```bash
/component    # React 컴포넌트 생성
/page        # Next.js 페이지 생성
/api         # API 엔드포인트 생성
/hook        # Custom Hook 생성
```

### 유틸리티 커맨드
```bash
/clean       # 캐시 및 빌드 파일 정리
/deps        # 의존성 업데이트 체크
/analyze     # 번들 사이즈 분석
```

---

## 🔌 MCP (Model Context Protocol) 설정

### GitHub 통합
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "github_pat_..."
      }
    }
  }
}
```

### 파일시스템 접근
```json
{
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem"],
    "env": {
      "FILESYSTEM_ROOT": "/Users/m4_macbook/iwl-v5-rebuild"
    }
  }
}
```

---

## 💡 Claude가 이 도구들을 활용하는 방법

### 1. 에이전트 자동 선택
```markdown
사용자: "이 컴포넌트가 너무 느려"
→ Claude: react-optimizer 에이전트 활용하여 최적화

사용자: "타입 에러가 나"
→ Claude: typescript-expert 에이전트 활용하여 해결
```

### 2. 커맨드 자동 실행
```markdown
사용자: "테스트 돌려줘"
→ Claude: /test 커맨드 실행

사용자: "빌드해봐"
→ Claude: /build 커맨드 실행
```

### 3. MCP 활용
```markdown
- GitHub Issue 자동 생성/조회
- PR 코멘트 작성
- 파일 시스템 직접 접근
```

---

## 🔄 새 세션 시작 시 체크리스트

### 1. 템플릿 시스템 확인
```bash
# 1. 설치 확인
ls -la .claude/

# 2. 에이전트 목록 확인
ls .claude/agents/

# 3. 커맨드 목록 확인
ls .claude/commands/

# 4. 설정 파일 확인
cat .claude/settings.json
```

### 2. 필수 확인 사항
- [ ] `.claude` 폴더 존재 여부
- [ ] 에이전트 파일들 존재 여부
- [ ] 커맨드 파일들 존재 여부
- [ ] MCP 설정 확인

### 3. 문제 발생 시
```bash
# 재설치
npm install -g claude-code-templates@latest

# 설정 재생성
claude-code-templates init
```

---

## 📊 Analytics Dashboard 사용

### 시작 방법
```bash
# Analytics 서버 시작
npx claude-code-templates analytics

# 브라우저에서 열기
open http://localhost:3333
```

### 모니터링 항목
- Claude 세션 활동
- 명령어 사용 통계
- 성능 메트릭
- 에러 로그

---

## 🎯 IWL 프로젝트 특화 설정

### 현재 프로젝트 상태
- **프레임워크**: Next.js 15.4.6 (Turbopack)
- **언어**: TypeScript
- **스타일링**: Tailwind CSS
- **UI 라이브러리**: shadcn/ui

### 주요 작업 영역
1. `/src/components/` - UI 컴포넌트
2. `/src/app/` - Next.js 페이지
3. `/src/components/ui/` - shadcn 컴포넌트

### 현재 포트 사용
- **3000**: 다른 프로세스 사용 중
- **3001**: 개발 서버 (npm run dev)
- **3333**: Analytics Dashboard

---

## 🚨 주의사항

### 이름 충돌
- 기존 `CLAUDE.md`는 프로젝트 가이드
- `.claude/` 폴더는 템플릿 시스템용
- 두 개는 서로 다른 목적

### 성능 고려사항
- 에이전트는 필요할 때만 호출
- MCP는 API 키 관리 주의
- Analytics는 개발 시에만 실행

---

## 📝 Quick Reference

### 자주 사용하는 명령어
```bash
# 개발 서버
npm run dev

# 타입 체크
npx tsc --noEmit

# ESLint
npx eslint src --fix

# 빌드
npm run build

# Analytics
npx claude-code-templates analytics
```

### 문제 해결
```bash
# .next 폴더 문제
rm -rf .next && npm run dev

# 포트 충돌
lsof -i :3000
kill -9 [PID]

# 캐시 정리
npm cache clean --force
```

---

## 📌 이 문서 업데이트

새로운 에이전트나 커맨드를 추가할 때마다 이 문서를 업데이트하세요:
```bash
# 수정 후
git add CLAUDE_TEMPLATES_SETUP.md
git commit -m "docs: Update Claude Templates setup guide"
```

---

**마지막 업데이트**: 2025-08-13
**작성자**: QA Claude
**버전**: 1.0

⚠️ **중요**: 새 Claude 세션 시작 시 반드시 이 문서를 먼저 읽고 설정을 확인하세요!
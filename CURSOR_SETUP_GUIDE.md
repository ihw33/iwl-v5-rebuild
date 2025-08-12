# 🚀 Cursor CLI 설정 가이드

## 📋 Cursor에서 ChatGPT-5 사용하기

### 1. Cursor 설치 (이미 설치된 경우 스킵)
```bash
# macOS
brew install cursor

# 또는 https://cursor.sh 에서 직접 다운로드
```

### 2. Cursor 설정
1. Cursor 앱 실행
2. **Settings** → **Models** 이동
3. **GPT-4** 또는 **GPT-4 Turbo** 선택
4. OpenAI API 키 입력 (없으면 Cursor Pro 구독)

### 3. 프로젝트 열기
```bash
cursor /Users/m4_macbook/iwl-v5-rebuild
```

---

## 🤖 AI 팀원으로 작업하기

### Cursor에게 역할 부여하기

Cursor 채팅창에서 다음과 같이 시작:

```markdown
너는 이제 IWL v5.0 프로젝트의 기획 담당 AI야.
너의 이름은 "Architect" 또는 "ChatGPT-5"이고,
다음 역할을 수행해:

1. 프로젝트 전체 아키텍처 설계
2. 기능 기획 및 요구사항 정의
3. 기술 스택 결정
4. API 스펙 문서화
5. 코드 리뷰 및 품질 관리

AI_TEAM_ROLES.md 파일을 참고해서 다른 AI 팀원들과 협업해.
```

---

## 📝 작업 예시

### 1. 기획 작업
```markdown
@Architect 
IWL v5.0의 사용자 인증 시스템을 설계해줘.
NextAuth.js를 사용하고, JWT 토큰 기반으로 구현할 거야.
```

### 2. API 설계
```markdown
@ChatGPT-5
다음 기능들을 위한 RESTful API를 설계해줘:
- 사용자 등록/로그인
- 8x4 매트릭스 데이터 CRUD
- 학습 진도 저장
```

### 3. 아키텍처 문서화
```markdown
@Architect
현재 프로젝트의 전체 아키텍처를 mermaid 다이어그램으로 그려줘.
프론트엔드, 백엔드, 데이터베이스 구조를 포함해서.
```

---

## 🔄 다른 AI와 협업하기

### PM Claude와 연동
```markdown
@Architect
이 기획안을 PM Claude가 실행할 수 있도록 
구체적인 태스크 리스트로 정리해줘.
```

### 개발팀에게 전달
```markdown
@ChatGPT-5
이 API 스펙을 Codex CLI가 구현할 수 있도록
상세한 엔드포인트 명세서를 작성해줘.
```

---

## 💡 팁과 베스트 프랙티스

### 1. 컨텍스트 유지
- 항상 프로젝트 문서들을 참조하도록 지시
- `AI_TEAM_ROLES.md`, `CLAUDE.md` 파일 위치 알려주기

### 2. 명확한 역할 정의
- 작업 시작 시 역할 명시
- 다른 AI 팀원과의 경계 명확히 하기

### 3. 문서화 습관
- 모든 기획은 마크다운으로 문서화
- `/docs` 폴더에 체계적으로 저장

### 4. 코드 생성 시
```markdown
@Architect
이 기능을 구현할 코드를 생성하되,
- TypeScript 사용
- 주석 없이 깔끔하게
- 에러 처리 포함
- 테스트 코드도 함께
```

---

## 🚨 주의사항

1. **API 키 보안**
   - OpenAI API 키는 절대 코드에 하드코딩하지 않기
   - `.env.local` 파일 사용

2. **비용 관리**
   - GPT-4는 토큰당 비용이 높음
   - 필요한 경우만 사용

3. **버전 관리**
   - 생성된 코드는 항상 Git으로 관리
   - 기획 문서도 버전 관리 포함

---

## 📞 문제 해결

### Cursor가 응답하지 않을 때
1. API 키 확인
2. 인터넷 연결 확인
3. Cursor 재시작

### 컨텍스트가 너무 길 때
1. 새 채팅 시작
2. 핵심 문서만 참조
3. 이전 대화 요약본 제공

---

## 🔗 관련 문서
- [AI_TEAM_ROLES.md](./AI_TEAM_ROLES.md) - AI 팀원 역할 정의
- [CLAUDE.md](/Users/m4_macbook/CLAUDE.md) - 프로젝트 전체 가이드
- [FIGMA_MAKE_GUIDE.md](./FIGMA_MAKE_GUIDE.md) - 디자인 연동 가이드
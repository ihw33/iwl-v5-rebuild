# 사용자 매뉴얼 (User Manual)

> 📌 **최종 업데이트**: 2025-08-14  
> 👤 **담당자**: QA Claude  
> 📚 **카테고리**: Guides / User Documentation

## 📖 목차

1. [시작하기](#시작하기)
2. [대시보드](#대시보드)
3. [학습 모듈](#학습-모듈)
4. [MD to PDF 변환기](#md-to-pdf-변환기)
5. [프로필 관리](#프로필-관리)
6. [문제 해결](#문제-해결)

---

## 🚀 시작하기

### 첫 접속
1. 브라우저에서 http://localhost:3000 접속
2. 초기 설정 마법사 실행
3. 프로필 생성

### 메인 화면 구성
```
┌─────────────────────────────────────┐
│  🏠 IdeaWorkLab v5.0                │
├─────────────────────────────────────┤
│  📊 대시보드  📚 학습  🔧 도구      │
├─────────────────────────────────────┤
│                                     │
│         [메인 콘텐츠 영역]           │
│                                     │
└─────────────────────────────────────┘
```

---

## 📊 대시보드

### 접속 방법
- URL: http://localhost:3000/dashboard
- 메인 메뉴 > 대시보드 클릭

### 주요 기능

#### 1. 시스템 상태 모니터링
- **실시간 상태**: 5초마다 자동 업데이트
- **메모리 사용률**: 시각적 게이지로 표시
- **서버 상태**: 정상/오류 표시

#### 2. Claude 설정 확인
- 에이전트 수
- 명령어 수
- 설정 상태

#### 3. 빠른 실행
- 앱 열기
- 레슨 디자인
- 상태 새로고침

### 활용 팁
💡 대시보드를 브라우저 북마크에 추가하면 빠르게 접근할 수 있습니다.

---

## 📚 학습 모듈

### A 시리즈 (기초 모듈)
8단계 학습 진행:
1. **A0**: 스펙 구조 이해
2. **A1**: 핵심 가치 정의
3. **A2**: 큰 그림 그리기
4. **A3**: 분해와 매핑
5. **A4**: 스토리 라인
6. **A5**: 자료 구조
7. **A6**: 논리적 흐름
8. **A7**: 마무리 정리
9. **A8**: 통합 실습

### B 시리즈 (실전 모듈)
대상별 맞춤 학습:
- **B0**: 표준 템플릿
- **B1**: 코어 레슨 (중립)
- **B2**: 주니어 대상
- **B3**: 유스 대상
- **B4**: 프로/스태퍼 대상
- **B5**: 파일럿 운영

### 학습 진행 방법
1. 모듈 선택
2. 학습 목표 확인
3. 콘텐츠 학습
4. 실습 과제 수행
5. 평가 및 피드백

---

## 🔄 MD to PDF 변환기

### 웹 인터페이스 사용법

#### 접속
URL: http://localhost:3000/convert

#### 변환 과정
1. **입력 방법 선택**:
   - 직접 입력: 텍스트 영역에 Markdown 작성
   - 파일 업로드: .md 파일 선택

2. **미리보기 확인**:
   - 우측 패널에서 실시간 미리보기
   - 포맷 확인

3. **PDF 변환**:
   - "Convert to PDF" 버튼 클릭
   - 자동으로 다운로드 시작

### CLI 사용법

#### 단일 파일 변환
```bash
node md-to-pdf.js README.md
```

#### 여러 파일 일괄 변환
```bash
node md-to-pdf.js --batch "docs/*.md"
```

#### Chrome 렌더러 사용 (고품질)
```bash
node md-to-pdf.js --chrome README.md output.pdf
```

### API 사용법

#### 엔드포인트
```
POST /api/convert/md-to-pdf
```

#### 요청 예시
```javascript
const response = await fetch('/api/convert/md-to-pdf', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    markdown: '# 제목\n내용...',
    filename: 'my-document'
  })
});

const blob = await response.blob();
// PDF 다운로드 처리
```

---

## 👤 프로필 관리

### 프로필 설정
1. 우측 상단 프로필 아이콘 클릭
2. 설정 메뉴 선택
3. 정보 수정

### 설정 가능 항목
- 이름
- 이메일
- 학습 선호도
- 알림 설정
- 언어 설정

---

## 🚨 문제 해결

### 자주 발생하는 문제

#### 1. 서버가 시작되지 않음
```bash
# 포트 충돌 확인
lsof -i :3000

# 다른 포트로 실행
PORT=3001 npm run dev
```

#### 2. PDF 변환 실패
```bash
# Pandoc 설치 확인
pandoc --version

# 재설치 (macOS)
brew reinstall pandoc
```

#### 3. 메모리 부족
```bash
# 메모리 정리
npm run clean
rm -rf .next node_modules
npm install
```

#### 4. 대시보드 데이터 안 보임
- 브라우저 캐시 삭제 (Cmd+Shift+R)
- 개발자 도구 > 네트워크 탭 확인
- `/api/health` 엔드포인트 확인

### 지원 받기

#### GitHub Issues
- 버그 리포트: [Issues](https://github.com/ihw33/iwl-v5-rebuild/issues)
- 라벨: `bug`, `help-wanted`

#### Discussions Q&A
- 질문하기: [Q&A](https://github.com/ihw33/iwl-v5-rebuild/discussions/categories/q-a)
- 다른 질문 검색

#### 직접 문의
- PM Claude: 프로젝트 관련
- QA Claude: 기술 지원
- Thomas: 최종 결정 사항

---

## 📱 모바일 사용

### 반응형 디자인
- 태블릿: 최적화됨
- 스마트폰: 기본 기능 지원

### 제한 사항
- PDF 변환: 데스크톱 권장
- 대시보드: 일부 차트 제한

---

## ⌨️ 단축키

| 단축키 | 기능 |
|--------|------|
| `Cmd/Ctrl + S` | 저장 |
| `Cmd/Ctrl + P` | PDF 변환 |
| `Cmd/Ctrl + K` | 검색 |
| `Cmd/Ctrl + /` | 도움말 |
| `Esc` | 닫기/취소 |

---

## 🔄 업데이트 내역

### v5.0.1 (2025-08-14)
- MD to PDF 변환기 추가
- 대시보드 실시간 업데이트
- Wiki 시스템 구축

### v5.0.0 (2025-08-11)
- 초기 릴리즈
- 기본 기능 구현

---

**도움이 필요하신가요?**  
[FAQ](FAQ) | [설치 가이드](Installation) | [관리자 가이드](Admin-Guide)

---

> 📝 **피드백 환영**: 이 매뉴얼을 개선할 아이디어가 있으시면 [Ideas Discussion](https://github.com/ihw33/iwl-v5-rebuild/discussions/categories/ideas)에 제안해 주세요!
# Figma Make 연동 가이드

## 🚀 Phase 1: 수동 연동 (즉시 시작)

### Figma Make에서 코드 생성
1. Figma Make에서 IWL v5.0 디자인 컴포넌트 생성
2. **Export Code** → 다운로드 (ZIP 파일)
3. 로컬에 압축 해제

### 코드 통합 워크플로우
```bash
# 1. Figma Make에서 받은 코드를 프로젝트에 통합
cp -r downloaded-code/components src/components/figma/
cp -r downloaded-code/styles src/styles/figma/

# 2. Git에 커밋
git add .
git commit -m "feat: Figma Make 컴포넌트 추가"
git push origin main

# 3. Vercel 자동 배포 확인
vercel --prod
```

## 🔄 Phase 2: 반자동 연동 (디자인 토큰)

### Tokens Studio for Figma 설정
1. Figma에서 **Tokens Studio** 플러그인 설치
2. GitHub 저장소 연결 설정
3. 디자인 토큰 자동 동기화 활성화

### 예상 파일 구조
```
src/
├── tokens/
│   ├── colors.json       # Figma 토큰 자동 동기화
│   ├── typography.json   # Figma 토큰 자동 동기화  
│   └── spacing.json      # Figma 토큰 자동 동기화
├── components/
│   ├── figma/           # Figma Make 수동 추가
│   └── custom/          # 개발팀 커스텀 컴포넌트
└── styles/
    ├── tokens.css       # 자동 생성된 CSS 변수
    └── tailwind.config.js # 토큰 기반 Tailwind 설정
```

## 🤖 Phase 3: 완전 자동화 (Figma API)

### CLI 기반 자동 동기화
- `figma-export` CLI 도구 활용
- GitHub Actions로 주기적 동기화
- Figma API 토큰을 통한 직접 연동

## 📋 현재 우선순위
1. **Phase 1 구현** (즉시 시작 가능)
2. **Phase 2 준비** (디자인 토큰 구조 설계)
3. **Phase 3 계획** (장기 자동화 전략)
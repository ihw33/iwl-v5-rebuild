# 🎨 Figma Make 간단 연동 가이드

## 📁 프로젝트 폴더 구조
```
iwl-v5-rebuild/
├── src/
│   ├── components/
│   │   ├── figma/          # Figma Make 컴포넌트 저장소
│   │   └── custom/         # 개발팀 커스텀 컴포넌트
│   ├── styles/
│   │   ├── figma/          # Figma Make 스타일
│   │   └── globals.css
│   └── types/
│       └── figma/          # Figma Make 타입 정의
└── figma-downloads/        # 임시 다운로드 폴더
```

## 🔄 3단계 워크플로우

### 1️⃣ Figma Make에서 코드 생성
- Figma 디자인 완료
- Make에서 **Export Code** 클릭
- ZIP 파일 다운로드

### 2️⃣ 프로젝트에 통합
```bash
# 1. 다운로드 폴더에 압축 해제
unzip figma-export.zip -d figma-downloads/

# 2. 컴포넌트 복사
cp -r figma-downloads/components/* src/components/figma/
cp -r figma-downloads/styles/* src/styles/figma/

# 3. 필요시 타입 정의 복사
cp -r figma-downloads/types/* src/types/figma/
```

### 3️⃣ Git 커밋 & 배포
```bash
git add .
git commit -m "feat: Figma Make 컴포넌트 추가"
git push origin main
# Vercel 자동 배포됨 ✅
```

## 🤖 AI 팀원별 역할

### VSCode Claude (프론트엔드)
- Figma 컴포넌트를 Next.js에 맞게 수정
- TypeScript 타입 에러 해결
- Tailwind CSS 스타일 조정

### Codex CLI (백엔드)
- API 연동이 필요한 컴포넌트 처리
- 데이터 바인딩 로직 추가

### PM Claude (터미널)
- 전체 통합 프로세스 관리
- Git 관리 및 배포 조율

## ⚡ 간단 명령어들
```bash
# 개발 서버 시작
npm run dev

# 프로덕션 배포
vercel --prod

# 타입 체크
npm run type-check
```

## 🎯 핵심 포인트
- **Figma Make는 코드 생성만** 담당
- **우리 프로젝트는 독립적**으로 관리
- **수동 복사가 현재 최선**의 방법
- **각 AI가 역할별로 코드 개선**
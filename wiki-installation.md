# 설치 가이드 (Installation Guide)

> 📌 **최종 업데이트**: 2025-08-14  
> 👤 **담당자**: QA Claude  
> 📚 **카테고리**: Guides / Getting Started

## 📋 시스템 요구사항

### 최소 요구사항
- **Node.js**: 18.0 이상
- **npm**: 9.0 이상
- **메모리**: 4GB RAM
- **디스크**: 2GB 여유 공간
- **브라우저**: Chrome 90+, Firefox 88+, Safari 14+

### 권장 사양
- **Node.js**: 20.x LTS (추천)
- **npm**: 10.x
- **메모리**: 8GB RAM
- **디스크**: 5GB 여유 공간
- **OS**: macOS 13+, Windows 11, Ubuntu 22.04+

## 🚀 설치 단계

### 1. 저장소 클론
```bash
git clone https://github.com/ihw33/iwl-v5-rebuild.git
cd iwl-v5-rebuild
```

### 2. 의존성 설치
```bash
npm install
```

### 3. 환경 변수 설정
```bash
cp .env.example .env
# .env 파일을 열어 필요한 값 설정
```

### 4. 개발 서버 실행
```bash
npm run dev
```

서버가 http://localhost:3000 에서 실행됩니다.

## 🛠️ 추가 도구 설치

### Pandoc (PDF 변환용)
```bash
# macOS
brew install pandoc

# Ubuntu/Debian
sudo apt-get install pandoc

# Windows
choco install pandoc
```

### GitHub CLI
```bash
# macOS
brew install gh

# Ubuntu/Debian
sudo apt-get install gh

# Windows
choco install gh
```

## 🔧 개발 환경 설정

### VS Code 확장 프로그램
- ESLint
- Prettier
- Tailwind CSS IntelliSense
- TypeScript Vue Plugin

### Chrome 확장 프로그램
- React Developer Tools
- Redux DevTools

## 🐳 Docker 설치 (선택사항)

### Docker Compose 사용
```bash
docker-compose up -d
```

### 개별 Docker 실행
```bash
docker build -t iwl-v5 .
docker run -p 3000:3000 iwl-v5
```

## ✅ 설치 확인

### 헬스 체크 실행
```bash
npm run health-check
```

### 브라우저 확인
1. http://localhost:3000 접속
2. http://localhost:3000/dashboard 대시보드 확인
3. http://localhost:3000/convert MD-PDF 변환기 확인

## 🚨 문제 해결

### npm install 실패
```bash
# 캐시 삭제
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

### 포트 충돌
```bash
# 3000 포트 사용 중인 프로세스 확인
lsof -i :3000
# 다른 포트로 실행
PORT=3001 npm run dev
```

### Pandoc 관련 오류
```bash
# Pandoc 버전 확인
pandoc --version
# 재설치
brew reinstall pandoc
```

## 📞 지원

문제가 지속되면:
1. [GitHub Issues](https://github.com/ihw33/iwl-v5-rebuild/issues) 생성
2. [Discussions Q&A](https://github.com/ihw33/iwl-v5-rebuild/discussions/categories/q-a) 질문

---

**최종 업데이트**: 2025-08-14
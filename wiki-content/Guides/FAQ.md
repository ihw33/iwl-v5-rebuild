# 자주 묻는 질문 (FAQ)

> 📌 **최종 업데이트**: 2025-08-14  
> 👤 **담당자**: QA Claude  
> 📚 **카테고리**: Guides / Support

## 📖 목차

1. [일반 질문](#일반-질문)
2. [설치 관련](#설치-관련)
3. [사용법](#사용법)
4. [기술적 문제](#기술적-문제)
5. [학습 콘텐츠](#학습-콘텐츠)
6. [협업 도구](#협업-도구)

---

## ❓ 일반 질문

### Q: IWL v5.0은 무엇인가요?
**A:** IdeaWorkLab v5.0은 AI 기반 학습 플랫폼으로, 8단계 사고 프레임워크와 4개 축을 기반으로 한 체계적인 학습 시스템입니다.

### Q: 이전 버전과 어떤 차이가 있나요?
**A:** v5.0은 완전히 새로 구축되었습니다:
- Next.js 15 + TypeScript 기반
- 8개 AI 협업 시스템
- GitHub 통합 워크플로우
- 실시간 모니터링 대시보드

### Q: 라이선스는 무엇인가요?
**A:** 현재 비공개 프로젝트입니다. 추후 오픈소스 전환을 검토 중입니다.

---

## 🔧 설치 관련

### Q: Node.js 버전이 맞지 않는다고 나옵니다.
**A:** Node.js 18.0 이상이 필요합니다:
```bash
# 버전 확인
node --version

# nvm으로 버전 변경
nvm install 20
nvm use 20
```

### Q: npm install이 실패합니다.
**A:** 캐시 문제일 수 있습니다:
```bash
# 캐시 정리
npm cache clean --force

# node_modules 삭제 후 재설치
rm -rf node_modules package-lock.json
npm install
```

### Q: 포트 3000이 이미 사용 중입니다.
**A:** 다른 포트를 사용하세요:
```bash
# 포트 확인
lsof -i :3000

# 다른 포트로 실행
PORT=3001 npm run dev
```

### Q: Pandoc 설치는 필수인가요?
**A:** MD to PDF 변환 기능을 사용하려면 필요합니다:
```bash
# macOS
brew install pandoc

# 설치 확인
pandoc --version
```

---

## 💡 사용법

### Q: 대시보드가 빈 화면으로 나옵니다.
**A:** API 연결을 확인하세요:
1. 개발자 도구 열기 (F12)
2. Network 탭 확인
3. `/api/health` 요청 확인
4. 에러가 있다면 서버 재시작

### Q: PDF 변환이 안 됩니다.
**A:** 여러 방법을 시도해보세요:
```bash
# CLI 방법
node md-to-pdf.js file.md

# Chrome 렌더러 사용
node md-to-pdf.js --chrome file.md

# 웹 인터페이스
http://localhost:3000/convert
```

### Q: 학습 진도가 저장되지 않습니다.
**A:** 로컬 스토리지 문제일 수 있습니다:
1. 브라우저 설정 > 쿠키 및 사이트 데이터
2. localhost 데이터 삭제
3. 페이지 새로고침

### Q: 다크 모드는 어떻게 켜나요?
**A:** 현재 개발 중인 기능입니다. Issue #23 참조.

---

## 🛠️ 기술적 문제

### Q: TypeScript 에러가 발생합니다.
**A:** 타입 체크를 실행하세요:
```bash
# 타입 체크
npm run type-check

# 자동 수정
npm run lint:fix
```

### Q: Hot Reload가 작동하지 않습니다.
**A:** Turbopack 문제일 수 있습니다:
```bash
# .next 폴더 삭제
rm -rf .next

# 다시 시작
npm run dev
```

### Q: 메모리 부족 에러가 납니다.
**A:** Node.js 메모리 한계를 늘리세요:
```bash
# 메모리 4GB로 증가
NODE_OPTIONS="--max-old-space-size=4096" npm run dev
```

### Q: API 요청이 CORS 에러를 반환합니다.
**A:** `next.config.js`에서 CORS 설정 확인:
```javascript
// next.config.js
module.exports = {
  async headers() {
    return [
      {
        source: "/api/:path*",
        headers: [
          { key: "Access-Control-Allow-Origin", value: "*" }
        ]
      }
    ]
  }
}
```

---

## 📚 학습 콘텐츠

### Q: A 시리즈와 B 시리즈의 차이는?
**A:** 
- **A 시리즈**: 8단계 사고 프레임워크 학습 (이론)
- **B 시리즈**: 대상별 맞춤 실전 콘텐츠 (실습)

### Q: 학습 순서가 정해져 있나요?
**A:** 권장 순서:
1. A0 ~ A8 순차 학습
2. B0 기본 템플릿 이해
3. 본인 수준에 맞는 B2~B4 선택

### Q: 평가는 어떻게 이루어지나요?
**A:** 각 모듈별로:
- 이해도 체크 퀴즈
- 실습 과제 제출
- 피드백 리뷰

### Q: 인증서를 받을 수 있나요?
**A:** 현재 준비 중입니다. 2025년 9월 예정.

---

## 🤝 협업 도구

### Q: GitHub Issues와 Discussions의 차이는?
**A:**
- **Issues**: 구체적 작업, 버그 추적
- **Discussions**: 아이디어, 토론, Q&A

### Q: Wiki는 누가 편집할 수 있나요?
**A:** 
- **읽기**: 모든 사용자
- **편집**: 권한 있는 팀원
- **관리**: PM Claude

### Q: 제안사항은 어디에 올리나요?
**A:** 
1. GitHub Discussions > Ideas 카테고리
2. 또는 Issue 생성 (라벨: `proposal`)

### Q: Projects 보드는 어떻게 보나요?
**A:** https://github.com/users/ihw33/projects/1

---

## 🆘 추가 도움

### 해결되지 않은 문제가 있다면:

1. **GitHub Discussions Q&A**  
   https://github.com/ihw33/iwl-v5-rebuild/discussions/categories/q-a

2. **GitHub Issues**  
   https://github.com/ihw33/iwl-v5-rebuild/issues

3. **담당자 문의**
   - 기술 문제: QA Claude
   - 콘텐츠 문제: 각 섹션 담당자
   - 운영 문제: PM Claude

### 유용한 링크
- [설치 가이드](Installation)
- [사용자 매뉴얼](User-Manual)
- [관리자 가이드](Admin-Guide)
- [GitHub 가이드](../GitHub-Guide)

---

## 💡 팁

> 🔍 **검색 팁**: Ctrl+F (Cmd+F)로 이 페이지에서 키워드를 검색하세요!

> 📝 **기여하기**: FAQ에 추가하고 싶은 질문이 있다면 [Discussions](https://github.com/ihw33/iwl-v5-rebuild/discussions)에 제안해 주세요!

---

**마지막 업데이트**: 2025-08-14  
**다음 업데이트**: 매주 금요일
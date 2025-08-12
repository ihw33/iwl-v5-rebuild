# 🎨 Figma → Cursor 연동 가이드

## 🚀 빠른 연동 방법

### 1️⃣ Figma Make에서 준비
```
1. Figma Make 프로젝트 열기
2. 컴포넌트 선택
3. Share → Copy Link
```

### 2️⃣ Cursor AI 활용
```
Ctrl+L (AI 채팅) 열고:

"이 Figma 디자인을 Next.js + Tailwind 컴포넌트로 변환해줘:
[Figma URL 붙여넣기]

요구사항:
- TypeScript 사용
- Tailwind CSS 스타일링
- src/components/figma/ 폴더에 저장
- IWL v5.0 디자인 시스템 준수"
```

### 3️⃣ 자동 배치
```bash
# 생성된 컴포넌트를 올바른 위치로 이동
mv generated-component.tsx src/components/figma/
git add . && git commit -m "feat: Figma 컴포넌트 추가"
```

## 🎯 Cursor AI 프롬프트 템플릿

### 기본 변환:
```
"Figma URL을 React 컴포넌트로 변환: [URL]"
```

### 고급 변환:
```
"Figma 디자인 분석 후 다음으로 변환:
- Next.js 15 컴포넌트
- TypeScript 인터페이스 포함
- Tailwind CSS 4.0 스타일
- Responsive 디자인
- 접근성 고려

Figma URL: [URL]"
```

## ⚡ 빠른 명령어
- **Cmd+Shift+P**: 명령 팔레트
- **Ctrl+K**: AI 코드 생성
- **Ctrl+L**: AI 채팅
- **@figma**: Figma 컨텍스트로 AI 호출
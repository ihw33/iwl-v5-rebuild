# 📝 Sessions 디렉토리 가이드

## 📋 개요
Claude 세션별 작업 기록과 인수인계 문서를 관리합니다.

---

## 🗂️ 폴더 구조
```
sessions/
├── README.md                     ← 이 문서
│
├── 📁 세션별 작업 폴더
│   ├── session_02/              ← 세션 02 작업
│   ├── session_03/              ← 세션 03 작업 (S1 철학)
│   ├── session_04/              ← 세션 04 작업 (S2 재정의)
│   └── session_05/              ← 세션 05 작업 (진행 예정)
│
└── 📄 세션 기록 문서
    ├── Session03_S1_Philosophy.md    ← S1 철학적 통찰
    ├── Session04_Full_Content.md     ← 세션 04 전체 대화
    └── Session05_Handover.md         ← 세션 05 인수인계
```

---

## 💡 세션 관리 방법

### 새 세션 시작 시
1. **이전 세션 인수인계 문서 확인**
   ```bash
   cat Session[이전번호]_Handover.md
   ```

2. **새 세션 폴더 생성**
   ```bash
   mkdir session_[번호]
   ```

3. **작업 진행**
   - 철학적 통찰 → 세션 문서로 저장
   - 임시 작업 → session_XX/ 폴더에
   - 완성 모듈 → /docs/8x4-matrix/modules/로 이동

### 세션 종료 시
1. **인수인계 문서 작성**
   - 파일명: `Session[번호]_Handover.md`
   - 내용: 완료 작업, 진행 중 작업, 다음 작업

2. **중요 내용 정리**
   - 철학적 통찰은 별도 문서로
   - 전체 대화 필요시 Full_Content로

---

## 📊 세션별 주요 성과

### 세션 02
- B0 템플릿 초안 작성
- 사고 성향 논의

### 세션 03 ⭐
- **S1 철학적 재해석** (핵심!)
- "없음"의 존재론
- 책 읽기 비유
- S1-A1 모듈 완성

### 세션 04
- S1-A2 모듈 초안
- **S2 재정의** - "관계성의 인식"
- S2 4개 축 구분

### 세션 05 (예정)
- S1-A2 모듈 수정
- S2-A1 모듈 설계

---

## 📌 중요 문서

### 필독
- `Session03_S1_Philosophy.md` - S1의 깊은 통찰
- `session_04/S2_Redefined_Design.md` - S2 재정의

### 참고
- `Session05_Handover.md` - 최신 인수인계
- 각 session_XX/ 폴더의 작업 파일들

---

## 🎯 파일 명명 규칙

### 세션 기록
- 형식: `Session[번호]_[내용].md`
- 예시: `Session06_S3_Philosophy.md`

### 작업 파일
- 위치: `session_XX/` 폴더 내
- 자유로운 명명 가능
- 완성되면 적절한 위치로 이동

---

## 🔄 워크플로우

```
세션 시작
    ↓
인수인계 확인
    ↓
작업 진행 (session_XX/)
    ↓
중요 내용 문서화
    ↓
완성 파일 이동 (/8x4-matrix/ 등)
    ↓
인수인계 작성
    ↓
세션 종료
```

---

## 🔗 관련 링크
- [프로젝트 현황](/PROJECT_STATUS.md)
- [8×4 매트릭스](/docs/8x4-matrix/README.md)
- [세션 시작 가이드](/SESSION_START_GUIDE.md)

---

**최종 업데이트**: 2025-08-16
**현재 세션**: 04 (멈춤) → 05 (시작 예정)
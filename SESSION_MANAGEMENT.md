# 🔄 IWL v5.0 세션 관리 시스템

## 📋 간단한 세션 관리 방법

### 1. 세션 시작 (새 채팅방에서)
```
세션 시작
```
이것만 입력하면 Claude가 자동으로:
- 최신 세션 기록 확인
- 마지막 작업 내용 파악
- 이어서 진행

### 2. 세션 종료 (채팅방 끝낼 때)
```
세션 종료
```
이것만 입력하면 Claude가 자동으로:
- 오늘 작업 요약
- 다음 할 일 정리
- 세션 기록 저장

---

## 📁 세션 관리 파일 구조

```
/sessions/
├── current.md          # 현재 세션 정보
├── session_01/         # 첫 번째 세션
│   ├── summary.md      # 세션 요약
│   └── decisions.md    # 주요 결정사항
├── session_02/         # 두 번째 세션
│   ├── summary.md
│   └── decisions.md
└── session_03/         # 세 번째 세션
    └── ...
```

---

## 🚀 사용 예시

### 세션 03 시작할 때:
```
User: 세션 시작

Claude: IWL v5.0 프로젝트 세션 03을 시작합니다.

📊 이전 세션(02) 요약:
- B0 템플릿 80% 완료
- 설문 시스템 개선안 작성
- 대시보드 아이디어 기록

🎯 오늘 이어갈 작업:
- 3. 사고 성향 진단 (4축 간소화)
- Issue #13 검증 계획

계속 진행하시겠습니까?
```

### 세션 03 종료할 때:
```
User: 세션 종료

Claude: 세션 03을 마무리합니다.

✅ 오늘 완료:
- 사고 성향 진단 설계
- A3(협업), A4(성찰) 축 명확화

🔄 다음 세션에서:
- 복합 성향 처리 방법
- 주니어용 별도 설계

파일 저장 완료: /sessions/session_03/summary.md
```

---

## 💡 자동화 팁

### current.md 템플릿
```yaml
current_session: 03
last_updated: 2025-08-15
status: active

next_tasks:
  - 사고 성향 진단 4축 설계
  - Issue #13 검증
  - Issue #23 통합 방안

recent_decisions:
  - 평가 → 니즈 파악 전환
  - 단계별 적응형 설문

key_files:
  - /docs/templates/B0_Survey_System_Revised.md
  - /docs/DECISIONS/2025-08-15-dashboard-ideas.md
```

이렇게 하면 Claude가 "세션 시작"만 봐도 current.md를 읽고 자동으로 이어갈 수 있습니다!

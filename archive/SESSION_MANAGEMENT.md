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

## 📁 파일 저장 위치 가이드

### 프로젝트 폴더 구조와 용도
```
iwl-v5-rebuild/
├── docs/
│   ├── theory/          ← 이론, 개념 설명
│   ├── templates/       ← 템플릿, 설문, 페르소나
│   ├── programs/        ← 프로그램 설계 (S1 통합 등)
│   ├── sessions/        ← 세션별 작업 기록
│   ├── planning/        ← 기획 문서 (필요시 생성)
│   └── DECISIONS/       ← 의사결정 기록
├── ai_prompts/          ← AI 프롬프트
├── sessions/            ← 세션 관리
├── meetings/            ← 미팅 기록
└── modules/             ← 32개 모듈 (작성 예정)
```

### 작업별 저장 위치
| 작업 유형 | 저장 위치 | 파일명 예시 |
|-----------|-----------|------------|
| 새 프로그램 설계 | `/docs/programs/` | S2_Integrated_Program.md |
| 이론 설명 | `/docs/theory/` | 8x4_Matrix_Theory_Guide.md |
| B시리즈 템플릿 | `/docs/templates/` | B1_Lesson_Template.md |
| 미팅 기록 | `/meetings/` | 2025-08-15_기획회의.md |
| 세션 작업 | `/sessions/session_XX/` | session_03_work.md |
| 결정사항 | `/docs/DECISIONS/` | 2025-08-15-주제.md |
| AI 프롬프트 | `/ai_prompts/` | lesson_design_prompt.md |
| 개별 모듈 | `/modules/` | S1-A1_module.md |

### 파일명 규칙
- 날짜 포함시: `YYYY-MM-DD-` 형식
- 단계별: `S1_`, `S2_` 등
- 템플릿: `B0_`, `B1_` 등
- 명확하고 일관된 명명

**⚠️ 중요**: 
- 임의로 폴더를 만들지 말고 위 구조를 따를 것
- 새 폴더가 필요하면 먼저 상의
- 기존 파일과 일관성 유지

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

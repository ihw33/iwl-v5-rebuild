# 📋 B0 협의 후 필요한 변경사항

## 1. 즉시 수정이 필요한 기존 문서

### Issue #13 업데이트
**현재 상태**: 단순 템플릿 작성
**변경 필요**: 
- 이중 구조 명시
- AI 설계 시스템 포함
- 모듈 조합 규칙 추가

### DAILY_TASKS.md
**추가 필요**:
```markdown
## Claude Desktop (기획팀)
[ ] B0 이중 구조 템플릿 (Frontend/Backend)
[ ] AI 프롬프트 체인 5단계
[ ] 모듈 메타데이터 템플릿
```

### PROJECT_MILESTONES.md
**Phase 2 확장**:
```markdown
## B 시리즈 + AI 시스템
- B0-1: 이중 구조 템플릿
- B0-2: AI 프롬프트 체인  
- B0-3: 파일 구조 구축
- D1-D3: 데이터 준비
```

---

## 2. 새로 생성할 문서/구조

### 폴더 구조
```
iwl-v5-rebuild/
├── modules/           # 새로 생성
│   ├── S1-A1.md
│   ├── S1-A2.md
│   └── ... (32개)
├── ai_prompts/        # 새로 생성
│   ├── system/
│   └── templates/
└── training_data/     # 새로 생성
    ├── combinations.json
    └── personas.json
```

### B0_TEMPLATE_DUAL.md
```yaml
# Frontend View (학습자용)
title: "AI로 OO 만들기"
duration: 35분
tools: ChatGPT

# Backend View (제공자용)
modules: [S2-A1, S4-A3]
cognitive_goals: {...}
checkpoints: [...]
```

### MODULE_METADATA_TEMPLATE.md
```yaml
module_id: S1-A1
stage: "탐색"
axis: "정보처리 심도"
level: L1
learning_objectives: []
prerequisites: []
next_modules: []
ai_prompts: {}
checkpoints: []
```

---

## 3. 프로세스 변경

### 기존 워크플로우
1. PM이 Issue 생성
2. 팀이 작업
3. PM이 검토
4. 완료

### 새 워크플로우  
1. 사용자 요구 입력
2. **AI가 조합 제안** ← NEW
3. Thomas 선택/수정
4. **이중 구조로 자동 생성** ← NEW
5. 실행

---

## 4. 우선순위별 작업 계획

### 🔴 긴급 (오늘)
1. B0 이중 구조 템플릿 초안
2. 모듈 메타데이터 템플릿
3. Issue #13 업데이트

### 🟡 중요 (이번 주)
1. 32개 모듈 메타데이터 작성
2. AI 프롬프트 체인 구현
3. 조합 예시 10개

### 🟢 일반 (다음 주)
1. 전체 시스템 테스트
2. UI 설계
3. MVP 개발

---

## 5. 검증 체크리스트

### 모든 작업물 검증 기준
- [ ] Frontend/Backend 분리되었는가?
- [ ] AI가 읽고 활용 가능한가?
- [ ] 모듈 조합이 가능한가?
- [ ] 학습자가 이론을 모르고도 진행 가능한가?
- [ ] 즉시 활용 가능한 결과물이 나오는가?

---

**작성**: PM Claude
**일시**: 2025-08-15
**상태**: 즉시 적용 필요
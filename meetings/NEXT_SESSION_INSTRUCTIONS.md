# 📋 다음 세션 시작 지침

## 🎯 새 창에서 작업 재개할 때

### 1. 첫 메시지 템플릿
```markdown
안녕하세요! IWL v5.0 프로젝트 작업을 이어서 진행하겠습니다.

이전 세션 요약:
- 일시: 2025-08-15
- 작업: B0 템플릿 기획 협의
- 핵심 결정: 이중 구조 템플릿, AI 자율 설계 시스템
- 문서: meetings/IWL_5_Rebuild_Project-01_체계정리.md

현재 작업 재개:
1. B0 이중 구조 템플릿 완성
2. AI 프롬프트 체인 구현
3. 모듈 메타데이터 작성
```

### 2. 필수 확인 파일
- `/meetings/IWL_5_Rebuild_Project-01_체계정리.md` - 이전 회의 정리
- `/meetings/IWL_5_Rebuild_Project-01_원본.md` - 원본 대화 내용
- `/docs/DECISIONS/` - 주요 결정사항
- `/DAILY_TASKS.md` - 일일 작업 현황

### 3. GitHub Issue 상태 확인
```bash
# 현재 진행 중인 작업 확인
gh issue view 13 --repo ihw33/iwl-v5-rebuild

# 전체 오픈 이슈 확인
gh issue list --repo ihw33/iwl-v5-rebuild --state open

# 마일스톤별 확인
gh issue list --repo ihw33/iwl-v5-rebuild --milestone "Phase 2: B 시리즈 (커리큘럼)"
```

---

## 📊 현재 작업 상황 (2025-08-15 종료 시점)

### ✅ 완료된 작업
1. **B0 템플릿 기본 구조 협의**
   - 수업 정보 섹션 설계
   - 인지 목표 설정 방식
   - 35분 수업 구성 (단일/복합)

2. **이중 구조 템플릿 설계**
   - Frontend (학습자용): 이론 최소화, 실습 중심
   - Backend (제공자용): 체계적 설계와 측정

3. **AI 시스템 설계**
   - 5단계 프롬프트 체인
   - 파일 구조 설계
   - 응답 템플릿 포맷

### 🔄 진행 필요 작업

#### 1. B0 템플릿 완성 (Issue #13)
```yaml
필요 작업:
- Frontend View 상세 작성
- Backend View 구조 확정
- 실제 예시 1개 완성
- JSON/YAML 포맷 통일
```

#### 2. 모듈 메타데이터 (D1)
```yaml
32개 모듈별 작성:
- learning_objectives
- prerequisites
- next_modules
- ai_prompts
- checkpoints
```

#### 3. AI 프롬프트 체인 구현 (B0-2)
```yaml
5단계 구현:
1. 컨텍스트 이해 프롬프트
2. 조합 생성 프롬프트
3. 수업 흐름 설계 프롬프트
4. AI 도구 활용 프롬프트
5. 검증 프롬프트
```

---

## 🎯 다음 세션 목표

### Phase 1 (즉시)
1. B0 템플릿 초안을 Issue #13에 제출
2. 모듈 메타데이터 템플릿 생성
3. 폴더 구조 실제 생성

### Phase 2 (이번 주)
1. 32개 모듈 중 최소 8개 메타데이터 작성
2. AI 프롬프트 체인 테스트
3. 조합 예시 3개 작성

### Phase 3 (다음 주)
1. 전체 시스템 통합 테스트
2. Claude/ChatGPT에서 실제 테스트
3. 파일럿 수업 1개 진행

---

## 💡 주의사항

1. **작업 연속성**
   - 이전 결정사항 존중
   - 파일 경로 일관성 유지
   - 명명 규칙 준수

2. **협업 방식**
   - Thomas와 단계별 협의
   - 일방적 제시 금지
   - 실용성 우선

3. **문서화**
   - 모든 결정사항 기록
   - 변경 이유 명시
   - 버전 관리

---

## 📝 Thomas에게 전달 메시지

```
Thomas님, 

이전 세션의 B0 템플릿 기획 내용을 정리했습니다.

📁 저장 위치:
- 체계 정리: /meetings/IWL_5_Rebuild_Project-01_체계정리.md
- 원본 대화: /meetings/IWL_5_Rebuild_Project-01_원본.md
- 다음 지침: /meetings/NEXT_SESSION_INSTRUCTIONS.md

다음 작업:
1. B0 템플릿 초안 완성
2. 모듈 메타데이터 작성 시작
3. 폴더 구조 생성

새 세션에서 이어서 작업하실 때 
NEXT_SESSION_INSTRUCTIONS.md 파일을 참고하시면 됩니다.
```

---

**작성**: PM Claude
**일시**: 2025-08-15
**용도**: 세션 연속성 보장
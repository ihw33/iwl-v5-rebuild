# 🚀 완벽한 세션 시작 템플릿
**Thomas가 인정한 표준 템플릿 - 반드시 이것 사용!**

---

## 📝 세션 시작 메시지 (복사해서 사용)

```
안녕! Thomas야. 세션 [번호]를 시작하려고 해.

🔗 GitHub: https://github.com/ihw33/iwl-v5-rebuild
📌 Issue #26: 모듈 메타데이터 스키마 작업
- 모든 진행사항은 Issue #26에 업데이트
- PM과 GitHub Issue로 소통

🔥 프로젝트 현황 확인:
cat /Users/m4_macbook/iwl-v5-rebuild/PROJECT_STATUS.md

📚 필수 문서 읽기:
1. PROJECT_STATUS.md - 전체 현황
2. /docs/sessions/Session03_S1_Philosophy.md - S1 철학 (핵심!)
3. /docs/8x4-matrix/modules/S1-A1/S1-A1-module_design.md - 완성 예시
4. /docs/8x4-matrix/modules/S1-A2/S1-A2-module_design.md - [상태]

🔧 GitHub 연동 확인:
gh auth status
gh repo view ihw33/iwl-v5-rebuild
git pull origin master  # 최신 상태 동기화

📌 환경:
- 로컬: /Users/m4_macbook/iwl-v5-rebuild
- GitHub: https://github.com/ihw33/iwl-v5-rebuild
- 브랜치: main/master
- Issue: #26

🎯 현재 작업할 내용:
1. [구체적 작업 1]
2. [구체적 작업 2]
3. 작업 완료 시 Issue #26에 진행상황 업데이트

⚠️ 작업 원칙:
- 문서 작성 시 Thomas와 단계별 협의
- 작업 후 즉시 commit & push
- Issue #26에 진행상황 댓글
- 철학적 깊이 우선

준비되면 [첫 작업]부터 시작하자!
```

---

## 💬 Issue #26 업데이트 템플릿

### 1️⃣ 작업 시작 시
```bash
gh issue comment 26 -R ihw33/iwl-v5-rebuild -b "## 🚀 세션 [번호] 작업 시작

### 현재 작업할 내용:
- [작업 1]
- [작업 2]
- MODULE_TEMPLATE.md 기반 작성

Thomas와 협의하며 진행합니다.
GitHub: https://github.com/ihw33/iwl-v5-rebuild"
```

### 2️⃣ 진행 중 업데이트
```bash
gh issue comment 26 -R ihw33/iwl-v5-rebuild -b "## 📝 진행 상황 업데이트

### ✅ 방금 완료한 작업:
- [완료 내용]

### 🔄 지금 작업 중:
- [진행 내용]

### 📁 수정된 파일:
- /docs/8x4-matrix/modules/[경로]

커밋: [커밋해시]
확인: https://github.com/ihw33/iwl-v5-rebuild/tree/master/docs/8x4-matrix/modules"
```

### 3️⃣ 작업 완료 시
```bash
gh issue comment 26 -R ihw33/iwl-v5-rebuild -b "## ✅ 세션 [번호] 작업 완료

### 완료된 작업:
- ✅ [작업 1]
- ✅ [작업 2]
- ✅ GitHub 푸시 완료

### 📊 현재 진행률:
- 완성: [개수]/32
- **전체: [%]**

### 다음 작업:
- [다음 할 일]

관련 커밋: [링크]"
```

---

## 🏁 세션 종료 체크리스트

### 1. 인수인계 문서 작성
```bash
# Session[번호]_Handover.md 작성
- 완료한 작업
- 진행 중인 작업  
- 다음 세션 할 일
- 중요 결정 사항
```

### 2. PROJECT_STATUS.md 업데이트
```bash
# 진행 현황 업데이트
- 완료된 모듈 추가
- 진행률 수정
- 다음 작업 명시
```

### 3. 최종 푸시
```bash
git add -A
git commit -m "📝 세션 [번호] 종료 - 인수인계 완료

- [주요 작업 1]
- [주요 작업 2]
- 다음: [다음 작업]"
git push origin master
```

### 4. Issue #26 최종 업데이트
```bash
gh issue comment 26 -R ihw33/iwl-v5-rebuild -b "## 🏁 세션 [번호] 종료

### 세션 성과:
- [성과 1]
- [성과 2]

### 다음 세션 예정:
- [계획]

인수인계 문서: /docs/sessions/Session[번호]_Handover.md"
```

---

## 🔗 빠른 링크 (항상 사용)
- **GitHub 저장소**: https://github.com/ihw33/iwl-v5-rebuild
- **Issue #26**: https://github.com/ihw33/iwl-v5-rebuild/issues/26
- **8x4 모듈 폴더**: https://github.com/ihw33/iwl-v5-rebuild/tree/master/docs/8x4-matrix/modules
- **이 템플릿**: /PERFECT_SESSION_START.md

---

## ⚠️ 중요!

### Thomas의 요청사항 (2025-08-16)
> "이번 세션 시작이 아주 좋아. 네가 이번에 올려준 시작 메세지와 템플릿을 다음 세션시에도 꼭 사용해줘"

**이 템플릿은 Thomas가 직접 승인한 것입니다.**
**다음 세션부터 반드시 이 템플릿을 사용하세요!**

---

**작성일**: 2025-08-16
**승인**: Thomas
**용도**: 모든 세션 시작 시 필수 사용
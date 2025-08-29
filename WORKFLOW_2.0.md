# 🔄 IWL v5.0 업무 프로세스 2.0

## 📊 도구별 용도 (2025-08-14 개정)

### 1. GitHub Issues
**용도**: 구체적 작업 관리
- ✅ 개발 작업
- ✅ 버그 수정
- ✅ 문서 작성 작업
- ❌ 토론, 제안, 질문

**라벨**:
- `theory`, `curriculum` - 작업 분류
- `needs-review` - PM 검토 필요
- `needs-thomas` - 최종 승인 필요
- `completed` - 작업 완료

### 2. GitHub Discussions
**용도**: 토론과 커뮤니케이션
- ✅ 아이디어 제안
- ✅ 공지사항
- ✅ 기획 토론
- ✅ Q&A

**카테고리**:
- 📢 **Announcements** - PM 공지사항
- 💡 **Ideas** - 제안 및 아이디어
- 🎯 **Planning** - 기획 토론
- 📚 **Learning** - 교육 콘텐츠 논의
- ❓ **Q&A** - 질문과 답변

### 3. GitHub Wiki
**용도**: 영구 문서 관리
- ✅ 사용자 매뉴얼
- ✅ API 문서
- ✅ 이론 체계 문서
- ✅ 가이드 문서

### 4. GitHub Projects
**용도**: 시각적 작업 관리
- ✅ 칸반 보드
- ✅ 진행 상황 추적
- ✅ 마일스톤 관리

---

## 🎯 상황별 프로세스

### 💡 새로운 아이디어가 있을 때
```
1. Discussions > Ideas에 게시
2. 팀원들과 토론
3. PM 검토
4. 승인 시 Issue 생성
5. 작업 착수
```

### 📢 공지할 내용이 있을 때
```
1. Discussions > Announcements에 게시
2. @team 멘션으로 알림
3. 중요도에 따라 고정(Pin)
```

### ❓ 질문이 있을 때
```
1. Discussions > Q&A에 질문
2. 답변 받기
3. 유용한 답변은 Wiki로 문서화
```

### 🐛 버그를 발견했을 때
```
1. Issue 생성 (bug 라벨)
2. 재현 방법 상세 기술
3. 담당자 할당
4. 수정 후 PR
```

### 📝 작업을 시작할 때
```
1. Issue 확인 또는 생성
2. 작업 시작 댓글
3. 진행 상황 업데이트
4. 완료 후 결과 제출
5. PM 검토
6. 필요시 Thomas 승인
```

---

## 📋 팀원별 일일 루틴

### 아침 (09:00)
```bash
# 1. 공지사항 확인
gh browse -R ihw33/iwl-v5-rebuild discussions

# 2. 할당된 Issue 확인
gh issue list --assignee @me

# 3. 새로운 토론 확인
# Discussions 웹에서 확인
```

### 작업 중
- Issue에 진행 상황 코멘트
- 질문은 Discussions Q&A
- 아이디어는 Discussions Ideas

### 저녁 (18:00)
- Issue 상태 업데이트
- 내일 작업 계획 코멘트
- 중요 사항 Discussions에 공유

---

## 🚀 빠른 참조

| 하고 싶은 것 | 사용할 도구 | 카테고리/라벨 |
|------------|-----------|--------------|
| 아이디어 제안 | Discussions | Ideas |
| 질문하기 | Discussions | Q&A |
| 공지사항 | Discussions | Announcements |
| 작업 시작 | Issues | 해당 라벨 |
| 버그 리포트 | Issues | bug |
| 문서 작성 | Wiki | - |
| 진행 상황 보기 | Projects | - |

---

## 📌 중요 원칙

1. **토론과 작업 분리**
   - 토론 → Discussions
   - 작업 → Issues

2. **문서 위치**
   - 영구 문서 → Wiki
   - 작업 문서 → Repository

3. **승인 프로세스**
   - 모든 작업 → PM 검토
   - 주요 결정 → Thomas 승인

4. **투명성**
   - 모든 논의 공개
   - 진행 상황 실시간 공유

---

**발효일**: 2025-08-14
**작성자**: PM Claude
**승인자**: @Thomas (승인 대기)
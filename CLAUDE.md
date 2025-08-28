# CLAUDE.md - IWL v5.0 리빌드 프로젝트 지침

## 🔄 컨텍스트 관리 규칙 (필수)

### `/clear` 또는 Compact Conversation 전 자동 수행 사항
**Claude는 컨텍스트 정리 전에 반드시 다음을 수행합니다:**

1. **대화 요약 문서 생성**
   ```bash
   docs/conversation-history/YYYY-MM-DD-[작업명].md
   ```
   - 세션 목표 및 주요 작업 내역
   - 중요 결정사항 및 사용자 피드백
   - 생성/수정된 파일 목록
   - 다음 작업 및 컨텍스트 복원 정보

2. **GitHub 이슈 업데이트**
   - 관련 이슈에 진행 상황 댓글
   - 완료된 작업 체크리스트 업데이트
   - 생성된 파일 경로 명시

3. **코드 커밋 & 푸시**
   ```bash
   git add [변경된 파일들]
   git commit -m "[의미있는 커밋 메시지]"
   git push origin [브랜치명]
   ```

4. **다음 세션 참조 경로 제공**
   ```
   이전 대화 기록: docs/conversation-history/[파일명].md
   현재 작업 상태: Issue #XX
   다음 TODO: [작업 내용]
   ```

### 이점
- ✅ 작업 연속성 보장
- ✅ 컨텍스트 유실 방지  
- ✅ 팀 협업 투명성
- ✅ 진행 상황 추적

## 🚨 PM Claude 역할 활성화 (IWL 전용)

### 절대 규칙
1. **나는 IWL 프로젝트 PM이다** - 전체 시스템 설계자 및 관리자
2. **직접 코딩 최소화** - 아키텍처 설계와 핵심 구현만
3. **30명 페르소나 Orchestra 시스템 활용**

## 🏗️ IWL v5.0 아키텍처

### Technology Stack
- **Frontend**: Next.js 15.4.2, React 19.1.0, TypeScript 5
- **Styling**: Tailwind CSS 4.1.11, Radix UI components
- **Backend**: Supabase (Auth, Database), Custom API Gateway
- **AI Integration**: OpenAI API, Google Generative AI, Claude API
- **Infrastructure**: Vercel deployment, Docker containers
- **Payment**: Stripe integration
- **Learning Engine**: Custom spaced repetition system

### Service Architecture
```
Frontend (Next.js)
    ↓ (API Routes)
AI Engine Hub
    ├── Learning Path Generator (OpenAI)
    ├── Content Analyzer (Claude)
    ├── Progress Tracker (Custom)
    └── Recommendation Engine (Gemini)
    ↓
Supabase Backend
    ├── User Management
    ├── Learning Data
    ├── Progress Tracking
    └── Content Repository
```

## 🎭 30명 페르소나 Orchestra 시스템

### 계층 구조
```
CEO (1) → CTO, COO (2)
    ↓
팀 리더 (7): Frontend, Backend, AI/ML, Design, QA, DevOps, Content
    ↓
전문가 팀 (20): 각 분야별 시니어/주니어 개발자, 디자이너, 엔지니어
```

### 📢 페르소나 스타일 가이드
**모든 페르소나는 PERSONA_STYLES.md에 정의된 고유한 캐릭터를 유지합니다.**
- 각자의 전문 용어와 관점으로 소통
- 고유한 이모지와 어투 사용
- GitHub 코멘트와 문서 작성 시 일관된 스타일 유지
- 상세 가이드: [PERSONA_STYLES.md](./PERSONA_STYLES.md) 참조

### 자동 할당 시스템
```python
# 이슈 키워드에 따른 자동 페르소나 선택
ISSUE_KEYWORDS = {
    'frontend': ['Frontend Lead', 'Senior Frontend Developer'],
    'backend': ['Backend Lead', 'Senior Backend Developer'], 
    'ai': ['AI/ML Lead', 'AI Engineer'],
    'design': ['Design Lead', 'UI/UX Designer'],
    'api': ['Backend Lead', 'Senior Backend Developer'],
    'database': ['Data Engineer', 'Backend Lead']
}
```

## 📋 IWL 개발 워크플로우

### 1. 이슈 접수 및 분석
```bash
# GitHub 이슈 생성 시 자동 실행
python nodes/iwl_development_node.py --issue-id <ID>
```

### 2. 작업 분해 및 할당
```python
# DAG 실행으로 자동 처리
- 이슈 분석 → 작업 분해 → 페르소나 선정 → 작업 할당 → 진행 모니터링
```

### 3. 품질 관리
- 자동 코드 리뷰 (QA Lead)
- 테스트 케이스 생성 (Test Engineer)
- 문서화 (Technical Writer)

## 🚀 개발 명령어

### 로컬 개발
```bash
# IWL 프로젝트 디렉토리로 이동
cd /Users/m4_macbook/Projects/iwl-v5-rebuild

# 개발 서버 시작
npm run dev      # 포트 3000

# AI Engine Hub 시작  
cd ai-engine-hub && python main.py  # 포트 8000
```

### Orchestra 시스템 실행
```bash
# Orchestra 시스템 활성화
cd /Users/m4_macbook/Projects/ai-orchestra-v02
./pm_start.sh

# IWL 특정 워크플로우 실행
python dags/iwl_development_dag.py --workflow=feature_development
```

## 🎯 IWL 학습 엔진 핵심 기능

### 1. 개인화 학습 경로
- 사용자 레벨 평가
- 맞춤형 커리큘럼 생성
- 진도 관리 및 조정

### 2. AI 기반 콘텐츠 생성
- 실시간 문제 생성
- 설명 및 예시 제공
- 오답 분석 및 피드백

### 3. 게이미피케이션
- 경험치 및 레벨 시스템
- 도전 과제 및 업적
- 리더보드 및 경쟁

### 4. 데이터 분석
- 학습 패턴 분석
- 성과 예측
- 개선 추천

## 🔧 개발 프로세스

### 이슈 생성 시 자동화
```bash
# [IWL] 태그가 포함된 이슈 생성 시
gh issue create \
  --title "[IWL] 새로운 기능 구현" \
  --body "요구사항 상세 설명" \
  --label "iwl-feature" \
  -R ihw33/iwl-v5-rebuild
```

### 페르소나 자동 할당
- 키워드 분석으로 적합한 페르소나 선정
- 워크로드 밸런싱
- 전문성 매칭

### 진행 상황 모니터링
- 실시간 진도 추적
- 품질 게이트 체크
- 자동 리포팅

## 📊 KPI 및 메트릭

### 개발 효율성
- 이슈 처리 속도
- 코드 품질 점수
- 테스트 커버리지

### 학습 효과
- 사용자 참여도
- 학습 완료율
- 성과 향상률

## 💡 기억하기
**"IWL = Intelligent Workforce Learning"**
**"30명 페르소나가 협력하는 자동화된 개발팀"**
**"사용자 중심의 개인화 학습 경험 제공"**

## 🔗 관련 프로젝트 연동
- **ai-orchestra-v02**: 페르소나 시스템 및 워크플로우 엔진
- **personal-journal-hub**: UI 컴포넌트 및 사용자 경험 참조
- **ai-engine-hub**: AI 모델 통합 및 API 게이트웨이
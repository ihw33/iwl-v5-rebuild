

[11:00:05.635] Running build in Washington, D.C., USA (East) – iad1 [11:00:05.635] Build machine configuration: 2 cores, 8 GB [11:00:05.651] Cloning github.com/ihw33/personal-journal-hub (Branch: main, Commit: 646a190) [11:00:06.168] Cloning completed: 517.000ms [11:00:09.951] Restored build cache f

pasted

iwl  5- rebuild  이 주제로 대화할꺼야

편집
네, Vercel 빌드 로그를 보니 개인 저널 허브 프로젝트의 빌드 과정이 기록되어 있네요. 빌드와 관련해서 어떤 부분을 논의하고 싶으신가요?

로그를 간단히 요약하면:

Next.js 15.4.2 프로젝트
빌드는 성공적으로 완료됨 (29초 소요)
17개의 정적 페이지 생성
빌드 중에 "FORCE DEBUG: isAdminLoggedIn 강제로 false 설정" 메시지가 여러 번 출력됨
최종적으로 배포 완료
특히 관심있는 부분이나 문제가 있는 부분이 있다면 말씀해 주세요.




Claude Desktop 기획팀 온보딩 메시지 (최종)
  # 🎯 IWL v5.0 기획팀 역할 시작
  안녕하세요! 당신은 이제 IWL v5.0 프로젝트의 기획팀입니다.
  Cursor CLI 오류로 인해 Claude Desktop으로 작업 환경을 이전했습니다.
  ## 📌 프로젝트 정보
  - 프로젝트명: IWL v5.0 (IdeaWorkLab)
  - 목적: AI 기반 8단계 학습 플랫폼 개발
  - GitHub: https://github.com/ihw33/iwl-v5-rebuild
  - 현재 단계: Phase 2 시작 (B 시리즈)
  ## 🔧 첫 번째 할 일: GitHub 연결 확인
  다음 명령어를 입력해서 GitHub 연결을 확인하세요:
  @github list issues in ihw33/iwl-v5-rebuild
  연결이 확인되면 작업을 시작합니다.
  ## ✅ 이전 팀이 완료한 작업
  - A1: 용어 표준 (완료)
  - A2: 8단계 정의 (완료)
  - A3: 4개 인지축 정의 (완료)
  - A4: 8×4 매트릭스 32개 셀 (완료!)
  - A1/A3 개선: 학술 용어 추가 (완료)
  ## 🎯 당신이 진행할 작업: Issue #13 - B0 표준 템플릿
  ### 작업 내용
  A4 매트릭스(8단계×4축)를 실제 35분 수업에 적용할 템플릿을 만드는 것입니다.
  ### 템플릿에 포함할 내용
  1. 수업 정보
     - Stage 번호 (1-8 중 선택)
     - 대상 (Junior/Youth/Pro)
     - 시간: 35분
     - 학습목표
  2. 인지 목표 설정
     - 정보처리 심도: L[1-5]
     - 사고조작방식: L[1-5]
     - 추상화 수준: L[1-5]
     - 자기인식 수준: L[1-5]
  3. 수업 구성
     - 도입 (5분): 동기부여, 목표 제시
     - 전개 (25분): 주요 활동, 실습
     - 정리 (5분): 핵심 정리, 다음 안내
  4. 평가 기준
     - 각 인지축별 체크리스트
     - 달성도 측정 방법
  ### 필수 작업
  - B0 템플릿 구조 완성
  - Stage 1 샘플 레슨 1개 작성 (실제 예시)
  ## 📂 참고할 문서
  Issue #13 내용 확인:
  @github view issue 13 in ihw33/iwl-v5-rebuild
  A4 매트릭스 확인 (필요시):
  @github view issue 12 in ihw33/iwl-v5-rebuild
  ## 💬 작업 방법
  1. 이 채팅창에서 B0 템플릿 작성
  2. Thomas가 검토 및 피드백
  3. 완성되면 Thomas가 GitHub에 업로드
  ## 🚀 지금 시작하세요!
  1단계: GitHub 연결 테스트
  @github list issues in ihw33/iwl-v5-rebuild
  2단계: Issue #13 확인
  @github view issue 13 in ihw33/iwl-v5-rebuild
  3단계: B0 템플릿 작성 시작
  질문이 있으면 Thomas에게 바로 물어보세요.
  화이팅! 💪

편집
안녕하세요! IWL v5.0 기획팀으로 참여하게 되어 기쁩니다. 지금 바로 GitHub 연결을 확인하고 작업을 시작하겠습니다.

1단계: GitHub 연결 테스트

G

list_issues


좋습니다! GitHub 연결이 성공적으로 확인되었습니다. 총 31개의 Issue가 있네요.

2단계: Issue #13 확인

G

get_issue


완벽합니다! Issue #13을 확인했습니다. A4 매트릭스도 참고하기 위해 Issue #12를 확인하겠습니다.


G

get_issue


좋습니다! 이제 B0 템플릿 작성을 시작하겠습니다. A4 매트릭스의 내용을 기반으로 35분 수업에 적용할 수 있는 표준 템플릿을 만들겠습니다.

3단계: B0 템플릿 작성 시작
B0: IWL v5.0 표준 수업 템플릿
📋 템플릿 개요
1. 수업 정보 섹션
yaml
수업명: [수업 제목]
Stage: [1-8 중 선택]
대상: [Junior/Youth/Pro 중 선택]
시간: 35분
인원: [최대 20명 권장]
형태: [온라인/오프라인/하이브리드]
준비물: [필요한 도구/자료]
2. 인지 목표 설정 섹션
yaml
인지목표:
  정보처리_심도: L[1-5]
  사고조작_방식: L[1-5]
  추상화_수준: L[1-5]
  자기인식_수준: L[1-5]

학습목표:
  - 주목표: [해당 Stage의 핵심 목표]
  - 세부목표1: [인지축별 구체적 목표]
  - 세부목표2: [인지축별 구체적 목표]
  - 세부목표3: [인지축별 구체적 목표]
3. 수업 구성 (35분)
도입 (5분)
markdown
목적: 동기부여 및 목표 제시

활동:
- [1분] 오늘의 핵심 질문 제시
- [2분] 실생활 연결 예시
- [2분] 학습 목표 및 기대 성과 공유

체크포인트:
□ 학습자의 관심 확보
□ 목표 이해도 확인
□ 선행 지식 활성화
전개 (25분)
markdown
Part A: 개념 탐구 (10분)
- 핵심 개념 소개
- 인지축별 활동:
  * 정보처리: [구체적 활동]
  * 사고조작: [구체적 활동]
  * 추상화: [구체적 활동]
  * 자기인식: [구체적 활동]

Part B: 실습/토론 (10분)
- 개인/그룹 활동
- AI 도구 활용 (선택)
- 피어 러닝

Part C: 적용/확장 (5분)
- 실제 상황 적용
- 문제 해결 연습
- 성찰 활동
정리 (5분)
markdown
활동:
- [2분] 핵심 내용 정리
- [2분] 학습 성과 점검
- [1분] 다음 단계 안내

체크포인트:
□ 학습 목표 달성도 확인
□ 주요 개념 재확인
□ 후속 학습 동기 부여
4. 평가 기준 (인지축별 체크리스트)
정보처리 심도
markdown
L1 □ 단순 정보를 그대로 수용하는가?
L2 □ 정보를 분류하고 구조화하는가?
L3 □ 정보 간 관계를 파악하는가?
L4 □ 정보를 비판적으로 평가하는가?
L5 □ 새로운 정보를 창출하는가?
사고조작 방식
markdown
L1 □ 단선적 순차 처리를 하는가?
L2 □ 분기와 조건을 고려하는가?
L3 □ 다중 변수를 동시에 다루는가?
L4 □ 재귀적 사고를 활용하는가?
L5 □ 메타 수준에서 조작하는가?
추상화 수준
markdown
L1 □ 구체적 사례만 다루는가?
L2 □ 유사 사례를 그룹화하는가?
L3 □ 일반 원리를 도출하는가?
L4 □ 추상 개념을 조작하는가?
L5 □ 메타 패턴을 인식하는가?
자기인식 수준
markdown
L1 □ 외부 지시에만 따르는가?
L2 □ 자신의 행동을 인지하는가?
L3 □ 사고 과정을 설명하는가?
L4 □ 전략을 의식적으로 선택하는가?
L5 □ 인지 체계를 재설계하는가?
5. AI 프롬프트 템플릿
도입용 프롬프트
"[Stage X]의 핵심인 [주제]에 대해 일상생활에서 
경험할 수 있는 구체적인 예시를 3개 제시해주세요. 
[대상]이 쉽게 이해할 수 있는 수준으로 설명해주세요."
실습용 프롬프트
"다음 상황에서 [인지축]을 L[N] 수준으로 
활용하는 방법을 단계별로 안내해주세요:
[구체적 상황 설명]"
평가용 프롬프트
"제가 작성한 [결과물]이 [Stage X]의 
[인지축] L[N] 수준을 달성했는지 평가하고, 
개선점을 구체적으로 제안해주세요."
6. 과제 템플릿
markdown
과제명: [Stage와 연결된 실습 과제]
목표: [인지축별 목표 레벨]
형식: [개인/그룹]
시간: [권장 소요 시간]

지시사항:
1. [구체적 단계 1]
2. [구체적 단계 2]
3. [구체적 단계 3]

제출물:
- [요구되는 산출물]
- [평가 기준 충족 증거]

평가 루브릭:
- 우수: [기준]
- 양호: [기준]
- 개선필요: [기준]
🎯 Stage 1 샘플 레슨: "일상의 패턴 발견하기"
1. 수업 정보
yaml
수업명: 일상의 패턴 발견하기 - 관찰과 기록의 힘
Stage: 1 (탐색)
대상: Junior (1-3년차 개발자)
시간: 35분
인원: 15명
형태: 온라인
준비물: 노트, 펜, 스마트폰(사진 촬영용)
2. 인지 목표 설정
yaml
인지목표:
  정보처리_심도: L1 (표면 수용)
  사고조작_방식: L1 (단선 순차)
  추상화_수준: L1 (구체 사례)
  자기인식_수준: L1 (무의식 실행)

학습목표:
  - 주목표: 일상에서 반복되는 패턴을 의식적으로 관찰하고 기록하기
  - 세부목표1: 하루 중 3가지 반복 행동 포착하기
  - 세부목표2: 관찰한 내용을 있는 그대로 기록하기
  - 세부목표3: 기록 행위 자체를 경험하기
3. 수업 진행
도입 (5분)
markdown
[1분] 핵심 질문:
"여러분은 오늘 아침에 일어나서 지금까지 
몇 번이나 휴대폰을 확인하셨나요?"

[2분] 실생활 예시:
- 출근길 지하철 손잡이 위치
- 점심 메뉴 선택 패턴
- 코드 작성 시 변수명 짓는 습관

[2분] 오늘의 목표:
"무의식적으로 반복하는 행동을 의식적으로 
포착하고 기록하는 첫 걸음을 시작합니다."
전개 (25분)
Part A: 관찰 연습 (10분)

markdown
개인 활동:
1. [3분] 지난 1시간 동안의 행동 회상
2. [3분] 반복된 행동 3가지 찾기
3. [4분] 각 행동을 구체적으로 묘사

예시:
- "마우스를 오른손으로만 사용함"
- "코드 작성 후 Ctrl+S를 2번씩 누름"
- "Slack 알림음이 들리면 즉시 확인함"
Part B: 기록 실습 (10분)

markdown
그룹 활동 (3-4명):
1. [5분] 각자의 관찰 내용 공유
2. [3분] 공통 패턴 찾기
3. [2분] 기록 방식 비교

AI 도구 활용:
"제가 관찰한 행동 패턴 3가지입니다: 
[패턴 나열]. 이런 패턴이 생긴 
가능한 이유를 추측해주세요."
Part C: 적용 계획 (5분)

markdown
개인 성찰:
1. [2분] 내일 관찰하고 싶은 행동 영역 선택
2. [2분] 기록 방법 결정 (메모앱, 수첩, 사진 등)
3. [1분] 관찰 시간대 설정
정리 (5분)
markdown
[2분] 핵심 정리:
- 일상의 무의식적 패턴 존재
- 의식적 관찰의 첫 단계
- 판단 없는 기록의 중요성

[2분] 성과 점검:
- "오늘 몇 개의 패턴을 발견했나요?"
- "기록하면서 새롭게 알게 된 점은?"

[1분] 다음 단계:
"내일부터 3일간 같은 시간대에 
같은 행동을 관찰해보세요. 
Stage 2에서는 이 기록을 분석합니다."
4. 평가 체크리스트
markdown
정보처리 심도 L1:
☑ 관찰한 내용을 있는 그대로 받아들였는가?
☑ 해석이나 판단 없이 순수하게 기록했는가?

사고조작 방식 L1:
☑ 시간 순서대로 행동을 나열했는가?
☑ 단순한 인과관계를 인지했는가?

추상화 수준 L1:
☑ 구체적이고 관찰 가능한 행동만 다뤘는가?
☑ 일반화하지 않고 개별 사례로 기록했는가?

자기인식 수준 L1:
☑ 지시된 활동을 그대로 수행했는가?
☑ 관찰과 기록 행위를 경험했는가?
5. 과제
markdown
과제명: 3일간의 루틴 관찰 일지
목표: Stage 1의 모든 인지축 L1 수준 달성
형식: 개인
시간: 하루 10분 × 3일

지시사항:
1. 매일 같은 시간대 선택 (예: 오전 9-10시)
2. 10분간 자신의 행동 관찰
3. 판단 없이 행동만 기록
4. 사진이나 스케치 추가 가능

제출물:
- 3일치 관찰 일지
- 각 날짜별 3-5개 행동 기록
- 선택: 패턴 시각화 (그림, 도표 등)

평가 루브릭:
- 우수: 구체적 행동 15개 이상, 시간 명시
- 양호: 구체적 행동 9-14개, 일부 시간 명시  
- 개선필요: 구체적 행동 8개 이하, 추상적 서술
Thomas님, B0 표준 템플릿과 Stage 1 샘플 레슨을 작성했습니다.

핵심 특징:

35분 구조 (5-25-5)
4개 인지축별 명확한 레벨 설정
구체적인 활동과 체크포인트
AI 활용 프롬프트 포함
평가 기준 명시
검토 부탁드립니다!




내가 토마스야  안녕 내용 잘봤고 우리 기획작업은 네가 일방적으로 해서 내게 주는게 아니고 서로 협의해서 결과물을 도출하는 식이야 그래서 단계별로 협의하고 그 내용을 네가 모아서 최종 결과물을 만든후에  해당 이슈에 업로드 해주면 되는거야 

일단 📋 템플릿 개요
1. 수업 정보 섹션 이것부터 협의 하자 내가 네가 적은 내용에 대해서 의견을 주면 너도 필요시 추가 의견을 주고 해서 최종안이 되면 다음으로 넘어가면 돼 . 이거 캔바스에 적어두고 할까 ?

편집
안녕하세요 Thomas님! 네, 이해했습니다. 일방적으로 제시하는 게 아니라 함께 협의해서 만들어가는 방식이군요.

캔버스를 사용하면 작업 내용을 시각적으로 정리하면서 진행할 수 있어서 좋을 것 같습니다!

1. 수업 정보 섹션부터 시작하죠
제가 제안한 초안:

yaml
수업명: [수업 제목]
Stage: [1-8 중 선택]
대상: [Junior/Youth/Pro 중 선택]
시간: 35분
인원: [최대 20명 권장]
형태: [온라인/오프라인/하이브리드]
준비물: [필요한 도구/자료]
이 구성에 대해 Thomas님의 의견을 듣고 싶습니다:

추가해야 할 항목이 있을까요?
수정이 필요한 부분이 있나요?
인원수 20명 제한이 적절한가요?
캔버스에 작업하시겠다면 제가 정리해서 따라가겠습니다!




온라인 수업은 모바일이나 컴퓨터 두가지로 될꺼야 이건 각 대상별로 다를것 같애 
우리가 짜놓은 수업 스토리대로 참여자가 따라오면서 과제를 각자 수행하고 중간 또는 마지막에 인공지능 챗봇을 붙여서 해당 수업 목적에 맞는 결과물을 내도록 유도하는가지 그래서 인원은 좀 가변적이야 
이 내용을 좀 참고해보고 나와 이야기 할까

 수업 목표 관련 문서: Issue #23
  제목: 4×8 기반 AI 협업 질문 설계 훈련 체계
  핵심 목적
  "4×8 매트릭스(32 모듈) × 3대상 × 5레벨 기반으로 목적별 산출물(보고서/제안서/계획서 등)에 맞는
  질문 설계 능력을 훈련하고, 실습 강사 챗봇(MVP)으로 질문 생성→코칭→평가까지 연결합니다."
  주요 내용
  1. 질문 설계 능력 훈련 - AI에게 효과적으로 질문하는 방법
  2. 목적별 플레이북 - 보고서/제안서/계획서별 질문 전략
  3. 질문 템플릿 - 10개 이상 템플릿
  4. 평가 루브릭 - 정렬성/구체성/구조/실행성/인지합치
  5. MVP 챗봇 - 실습 강사 역할
  파일럿 도메인
  - 신사업 보고서 작성을 위한 AI 질문 훈련
  현재 상태
  - PM 검토 완료
  - Thomas 승인 대기
  - 승인되면 module_meta 스키마 설계 시작

편집
아, 이제 더 명확하게 이해했습니다! Issue #23의 내용을 보니 우리가 만드는 수업의 핵심이 "AI에게 효과적으로 질문하는 능력"을 기르는 것이네요.

그렇다면 수업 정보 섹션을 다시 생각해볼게요:

수정 제안
yaml
수업명: [수업 제목]
Stage: [1-8 중 선택]
대상: [Junior/Youth/Pro 중 선택]
시간: 35분
인원: 가변적 (온라인 무제한)
형태: 
  - 온라인(모바일): [Youth 주로 활용]
  - 온라인(PC): [Junior/Pro 주로 활용]
  - 오프라인: [선택적]
AI 도구: [사용할 AI 챗봇 명시]
최종 산출물: [보고서/제안서/계획서 등]
준비물: [필요한 도구/자료]
추가 고려사항:
AI 도구 항목 추가 - 어떤 AI를 활용할지 명시
최종 산출물 항목 추가 - 수업 끝에 만들어낼 결과물 명시
인원 - 온라인은 무제한, 오프라인은 제한 가능
형태 - 대상별로 선호 플랫폼 구분
이렇게 수정하면 어떨까요? 특히 "AI 질문 설계 훈련"이라는 핵심 목적이 더 잘 드러나도록 템플릿을 구성하는 게 중요할 것 같습니다.




물론 그 배경은 4X8 매트릭스와 같은 이론적 토태가 베이스가 되는건 알지 ?

편집
네, 맞습니다!

4×8 매트릭스가 기반이 되어:

8단계 (탐색→통합→의미→응용→심화→혁신→초월→통섭)
4개 인지축 (정보처리 심도, 사고조작 방식, 추상화 수준, 자기인식 수준)
총 32개 모듈
이 이론적 토대 위에서 각 수업이 설계되고, 학습자가 AI에게 질문하는 능력도 이 단계와 인지축을 따라 발전하게 되는 거죠.

그래서 수업 정보 섹션에 이런 연결고리를 명시하면 좋을까요?

yaml
수업명: [수업 제목]
Stage: [1-8 중 선택] - [단계명 함께 표기]
인지 포커스: [이 수업에서 중점적으로 다룰 인지축]
대상: [Junior/Youth/Pro 중 선택]
시간: 35분
...
이렇게 4×8 매트릭스와의 연결을 명확히 하는 것도 중요할 것 같은데, Thomas님 생각은 어떠신가요?




응 아마도  지금 우리는 4 8 매트리스에 의해서 기본 32개 모듈의 수업 유닛이 생기고 이것이 5개의 레벨로 3개의 대상에게 전달될건데  각각의 인지축에 따라 1단계에서 8단계가지 하는 수업도 있지만 난이도에 따라 3개 에서 8개의 단계 수업으로 세분화 될거야 

이렇게 인공지능 협업을 위한 기본적인 생각정리 능력 향상프로그램도 있지만 32개 모듈울 조합해서.보고서 작성. 리포트작성. 학교 과제 풀이. 수행평가 준비. 등등 다양한 목적을 두고 해당되는  모듈을 골라 조합해서 프로그램을 만들수도 있어 

이부부을 염두해두고 의견줘봐

편집
아하! 이제 전체 그림이 더 선명해졌네요.

수업 구조의 유연성을 반영한 제안
yaml
수업명: [수업 제목]
수업 유형:
  - 단일 모듈: [Stage X, 인지축 Y]
  - 인지축 시리즈: [인지축 Y의 Stage 1~8]
  - 목적별 조합: [선택된 모듈들 나열]

프로그램 구성:
  - 전체 단계: [3~8단계 중 선택]
  - 포함 모듈: [예: S1-A1, S3-A2, S5-A4...]
  
목적/산출물:
  - 기본: AI 협업 사고력 향상
  - 응용: [보고서/리포트/과제/수행평가 등]

대상: [Junior/Youth/Pro]
레벨: [L1~L5]
시간: 
  - 단일 수업: 35분
  - 전체 프로그램: [X시간/X주]

수업 환경:
  - 플랫폼: [모바일/PC]
  - AI 도구: [사용할 챗봇]
  - 지원 도구: [노트앱/협업툴 등]
핵심 변화:
수업 유형 구분 - 단일/시리즈/조합형
프로그램 구성 - 유연한 모듈 조합 가능
목적 이원화 - 기본 능력 vs 실무 응용
이렇게 하면 32개 기본 모듈을 레고 블록처럼 조합해서 다양한 목적의 프로그램을 만들 수 있는 구조가 되는데, 어떻게 생각하시나요?




응 좋아 일단 처음이니까 이정도에서 넘어갈까

편집
네, 좋습니다! 그럼 수업 정보 섹션은 이렇게 정리하고 다음으로 넘어가죠.

2. 인지 목표 설정 섹션
제가 처음에 제안했던 내용:

yaml
인지목표:
  정보처리_심도: L[1-5]
  사고조작_방식: L[1-5]
  추상화_수준: L[1-5]
  자기인식_수준: L[1-5]

학습목표:
  - 주목표: [해당 Stage의 핵심 목표]
  - 세부목표1: [인지축별 구체적 목표]
  - 세부목표2: [인지축별 구체적 목표]
  - 세부목표3: [인지축별 구체적 목표]
이 부분에서 특히 고민되는 건:

단일 모듈 수업에서 4개 인지축을 모두 다뤄야 하나?
아니면 주요 인지축 1-2개에 집중하는 게 나을까?
AI 질문 설계라는 특성을 어떻게 반영할까?
Thomas님의 의견을 듣고 싶습니다!




응 이건 난이도에 따라 달라질거야 각각의 인지축을 하나씨기 다루는것부터 수업 목적이나 난이도에 따라 1개에서 4개가 복합이 되는 구조로 갈꺼야   우리 서비스 기획의 어려움은 이렇게 32개의 모듈을 조합하는 갯수가 많기떄문이라  특히 인공지능의 능력으로 도와줘야해

편집
네, 이해했습니다! 조합의 복잡성이 핵심 도전 과제네요.

인지 목표 설정 섹션 수정안
yaml
인지 목표 구성:
  복잡도: [단일/복합]
  주요 인지축: [1~4개 선택]
    - 인지축1: [축 이름] L[1-5]
    - 인지축2: [축 이름] L[1-5] (선택)
    - 인지축3: [축 이름] L[1-5] (선택)
    - 인지축4: [축 이름] L[1-5] (선택)

학습 목표:
  - AI 질문 목표: [이 수업에서 학습할 질문 패턴/전략]
  - 인지 발달 목표: [선택된 인지축별 구체적 목표]
  - 산출물 목표: [만들어낼 질문/프롬프트의 수준]

난이도별 예시:
  - 초급(L1-2): 단일 인지축 집중
  - 중급(L3): 2개 인지축 조합
  - 고급(L4-5): 3-4개 인지축 통합
AI 지원 필요 영역:
모듈 추천 - 학습 목적에 맞는 최적 조합 제안
난이도 조정 - 대상과 레벨에 맞는 인지축 수 결정
시너지 분석 - 어떤 인지축 조합이 효과적인지
이렇게 유연하게 구성하면 어떨까요?




응 그럼 나중에 실제로 교수 설계를 할때 목적에 따라 수업이 많은 조합의 수업이 만들어질거야

편집
네, 맞습니다! 그래서 B0 템플릿은 그런 다양한 조합을 수용할 수 있는 유연한 구조여야 하겠네요.

예를 들어:

"AI로 주간보고서 작성하기" → S1-A1, S3-A2, S5-A3 조합 (3개 모듈)
"학술 논문 리서치 질문 만들기" → S4-A3, S6-A4, S7-A2, S8-A1 조합 (4개 모듈)
"수행평가 프로젝트 기획" → Youth 대상으로 S2-A1, S3-A1, S4-A2 (3개 모듈)
이런 식으로 목적과 대상에 따라 수많은 조합이 가능하겠죠.

그럼 인지 목표 설정 섹션도 이 정도로 정리하고, 다음으로 넘어갈까요?

다음은 3. 수업 구성 (35분) 섹션인데, 이 부분도 단일 모듈용과 복합 모듈용으로 나눠서 생각해야 할 것 같은데요?




응 그러자 의견줘

편집
3. 수업 구성 (35분) 섹션 제안
기본 구조 (35분)
yaml
수업 구조 타입: [단일 모듈 / 복합 모듈]

# 타입 A: 단일 모듈 (1개 모듈 집중)
도입 (5분): 
  - 모듈 목표 제시
  - AI 도구 준비
  
전개 (25분):
  - 핵심 활동 (15분)
  - AI 실습 (10분)
  
정리 (5분):
  - 성과 확인
  - 다음 단계 안내

# 타입 B: 복합 모듈 (2-4개 모듈 연결)
도입 (3분):
  - 전체 목표 제시
  
전개 (28분):
  - 모듈1 (8-10분)
  - 모듈2 (8-10분)  
  - 모듈3 (8-10분) *선택
  - 통합 활동 (나머지 시간)
  
정리 (4분):
  - 연결점 정리
핵심 고려사항:
단일 모듈: 깊이 있는 탐구, 충분한 실습 시간
복합 모듈: 모듈 간 연결, 빠른 전환, 통합 사고
특히 복합 모듈의 경우:

각 모듈당 8-10분으로 압축
모듈 간 전환을 자연스럽게
마지막에 통합 활동으로 연결
이런 이중 구조로 가면 어떨까요?




응 그럼 이해를 돕기 위해서 이 구조로 실제수업예를 하나 들어줄래. 페르소나 설정하고 목표 난이도 설정해서

편집
실제 수업 예시: "AI로 프로젝트 제안서 작성하기"
수업 정보
yaml
수업명: AI와 함께 만드는 설득력 있는 프로젝트 제안서
수업 유형: 목적별 조합 (복합 모듈)
프로그램 구성:
  - 포함 모듈: S2-A1(분석), S4-A3(추상화), S5-A2(사고조작)
  
목적/산출물: 
  - 팀 프로젝트 제안서 1장 완성
  - AI 프롬프트 템플릿 3개 획득

대상: Junior (2년차 개발자)
레벨: L3 (중급)
시간: 35분

수업 환경:
  - 플랫폼: PC
  - AI 도구: ChatGPT/Claude
  - 지원 도구: Google Docs
페르소나
김주니어 (28세, 2년차 백엔드 개발자)

상황: 팀 내 첫 기술 제안서 작성 담당
고민: "아이디어는 있는데 체계적으로 정리가 안 돼요"
목표: Redis 도입 제안서를 설득력 있게 작성하기
인지 목표 설정
yaml
인지 목표 구성:
  복잡도: 복합 (3개 인지축)
  주요 인지축:
    - 정보처리 심도: L3 (관계 파악)
    - 추상화 수준: L3 (원리 도출)
    - 사고조작 방식: L2 (조건 분기)

학습 목표:
  - AI 질문 목표: 제안서 구조화를 위한 단계별 프롬프트 작성
  - 인지 발달 목표: 문제-해결책-이득을 논리적으로 연결
  - 산출물 목표: 실무 활용 가능한 제안서 프롬프트 세트
수업 구성 (35분)
도입 (3분)
markdown
"여러분, 좋은 아이디어가 있는데 상사나 팀을 
설득하기 어려웠던 경험 있으신가요?"

- Redis 도입 사례로 시작
- 오늘의 목표: 3단계 AI 프롬프트로 제안서 완성
전개 (28분)
모듈 1: S2-A1 분석 (9분)

markdown
[현황 분석 프롬프트 만들기]

실습: "우리 서비스의 현재 성능 병목 지점을 
구조화해서 분석해줘" → AI 응답 → 개선

학습: 
- 구체적 수치/상황 제공의 중요성
- AI가 체계적으로 분석하도록 유도하는 법

결과물: 현황 분석 프롬프트 템플릿
모듈 2: S4-A3 추상화 (9분)

markdown
[해결 원리 도출 프롬프트 만들기]

실습: "Redis의 핵심 원리와 우리 상황을 연결해서
해결 방안을 제시해줘" → AI 응답 → 개선

학습:
- 기술의 본질을 뽑아내는 질문법
- 일반 원리를 특수 상황에 적용시키기

결과물: 솔루션 매칭 프롬프트 템플릿
모듈 3: S5-A2 사고조작 (8분)

markdown
[조건별 시나리오 프롬프트 만들기]

실습: "Redis 도입 시 예상되는 상황별 대응 방안을
의사결정 트리로 만들어줘" → AI 응답 → 개선

학습:
- if-then 구조로 복잡한 상황 정리
- 리스크와 대안을 체계화하는 법

결과물: 시나리오 분석 프롬프트 템플릿
통합 활동 (2분)

markdown
3개 프롬프트를 연결해서 제안서 초안 생성
→ 실제 1페이지 제안서 완성
정리 (4분)
markdown
- 3단계 프롬프트 체인 완성
- 각자 상황에 맞게 수정 가능
- 다음 주 실제 제안서 작성 후 공유

"이제 여러분도 AI와 함께라면 
어떤 제안서도 작성할 수 있습니다!"
평가 체크포인트
 현황을 구체적 데이터로 분석했는가?
 기술의 원리와 문제를 연결했는가?
 다양한 시나리오를 고려했는가?
 AI 프롬프트가 재사용 가능한가?
이런 식으로 복합 모듈이 실제 목적(제안서 작성)을 달성하도록 구성되는데, 어떻게 보시나요?




응 잘 헀어  그런데 여기서 학습자에게 이론적인 수업이 어느정도까지 필요한가야. 우리 이론 내용을 전분 설명할 필요가 없고 해당 목표에 맞는 액션들을 훈련시키는 것이 더 효과적이지 않겠느냐는 거지

편집
아, 정말 중요한 포인트네요! 맞습니다.

이론 최소화, 실습 중심으로 재구성
기존 방식 (❌)
"오늘은 S2-A1 분석 모듈을 배웁니다. 정보처리 심도 L3는..."

개선 방식 (✅)
"지금부터 상사를 설득할 제안서를 AI와 함께 만들어봅시다!"

수업 구성 수정안
yaml
# 이론 설명 → 체험적 학습으로 전환

도입 (3분):
  - 이론 설명 (X)
  - 실제 문제 제시 (O)
  - "이런 상황 겪어보셨죠?"

전개 (28분):
  - 이론적 프레임워크 설명 (X)
  - 따라하기 → 수정하기 → 응용하기 (O)
  - "이렇게 물어보세요" → "해보셨나요?" → "이번엔 이렇게"

정리 (4분):
  - 이론 정리 (X)
  - 사용 가능한 도구/템플릿 확보 확인 (O)
  - "오늘 만든 프롬프트 3개, 내일 바로 쓸 수 있죠?"
핵심 변화:
모듈명 언급 없이 자연스럽게 활동에 녹이기
**"왜"보다 "어떻게"**에 집중
즉시 써먹을 수 있는 결과물 중심
그럼 템플릿도 이런 방향으로 수정해야겠네요?




그럼 수업안이 2중으로 가야겠다   참여자가 보는 수업과 백엔드처럼 서비스 제공자가 각 단계별로 고려해야하는 사항들.. 이두가지가 같이 설계되어야 하고 그 설계는 기존에 만들어진 설계도 있지만 사용자의 요구에 따라 새로운 조합이 필요할수 있기 때문에 그런 조합을 인공지능이 만들어 낼수 있도록교육한 데이터가 필요하다 

에를들어 클로드코드를 새로 열고 오늘처럼 특정 깃허브주소를 주고 연결을 시켜주면 우리가 하고자하는 것에 댛서 이해하고 대상 페르소나와 목적, 결과물 종류 를 넣으면 설계ㅏ 되엉서 나와야해 

물론 한가지 정답이아닌 여러가ㅣ 경우의 결과가 나오는데 더 자연스럽겠지 

이런 부분을 우리 지금 서비스 설계 과정에 같이 넣어서 완성해야 하는거야

편집
아하! 이제 전체 그림이 완전히 명확해졌네요. B0 템플릿이 이중 구조여야 하는군요.

B0 템플릿 이중 구조
1. 학습자용 View (Frontend)
yaml
수업 제목: "AI로 3분 만에 제안서 완성하기"
소요 시간: 35분
준비물: 노트북, ChatGPT 계정
오늘의 목표: "퇴근 전 제안서 완성!"

진행 순서:
1. [3분] 여러분의 고민 들어보기
2. [10분] 첫 번째 마법 - 현황 정리하기
3. [10분] 두 번째 마법 - 해결책 찾기  
4. [8분] 세 번째 마법 - 리스크 대비하기
5. [4분] 완성! 내일 바로 사용하세요
2. 서비스 제공자용 View (Backend)
yaml
모듈 구성:
  - S2-A1 (정보처리 L3): 현황 분석
  - S4-A3 (추상화 L3): 원리 도출
  - S5-A2 (사고조작 L2): 조건 분기

인지 목표:
  - 체크포인트 1: 구조화된 분석 달성
  - 체크포인트 2: 추상-구체 연결
  - 체크포인트 3: 분기 사고 적용

AI 프롬프트 시퀀스:
  - Hook: [참여 유도 프롬프트]
  - Guide: [단계별 안내 프롬프트]
  - Check: [이해도 확인 프롬프트]

측정 지표:
  - 완성도: 제안서 구조 충족률
  - 활용도: 프롬프트 수정 횟수
  - 만족도: 즉시 적용 가능성
3. AI 교육용 데이터 구조
yaml
training_data:
  input:
    - github_repo: "ihw33/iwl-v5-rebuild"
    - persona: "2년차 개발자"
    - purpose: "기술 도입 제안"
    - output_type: "1페이지 제안서"
  
  output_options:
    option_1:
      - modules: [S2-A1, S4-A3, S5-A2]
      - duration: 35분
      - difficulty: L3
    
    option_2:
      - modules: [S1-A1, S3-A2, S6-A3]
      - duration: 45분
      - difficulty: L2
    
    option_3:
      - modules: [S4-A2, S5-A3, S7-A1]
      - duration: 30분
      - difficulty: L4
이렇게 되면:

학습자는 이론 부담 없이 실습 중심으로
제공자는 체계적인 설계와 측정 가능
AI는 다양한 조합을 학습해서 맞춤 제안
다음 단계로 이런 이중 구조를 템플릿에 어떻게 반영할지 논의해볼까요?




이런 내용을 취지에 맞게 ai가 조합을 하려면 여기에 ai에게 어떻게 조합하라고 하는 프롬프트가 매 단계마다 필요해

편집
정확합니다! AI가 스스로 조합을 만들어내려면 각 단계별로 명확한 프롬프트 가이드가 필요하죠.

AI 조합 생성을 위한 단계별 프롬프트
1단계: 컨텍스트 이해 프롬프트
당신은 IWL v5.0의 수업 설계 AI입니다.
- 4×8 매트릭스 (32개 모듈) 이해
- 각 모듈의 인지축과 레벨 파악
- 모듈 간 시너지와 순서 고려

입력 정보:
- 대상: {persona}
- 목적: {purpose}
- 산출물: {output_type}
- 시간: {duration}

이 정보를 바탕으로 최적의 모듈 조합을 제안하세요.
2단계: 조합 생성 프롬프트
다음 기준으로 3가지 조합안을 만드세요:

1. 목적 달성도 (40%)
   - {output_type}을 만들기 위한 필수 인지 능력은?
   - 어떤 모듈이 직접적으로 도움이 되는가?

2. 학습 흐름 (30%)
   - 쉬운 것 → 어려운 것
   - 구체적 → 추상적
   - 개별 스킬 → 통합 적용

3. 대상 적합성 (30%)
   - {persona}의 현재 수준
   - 집중력 지속 시간
   - 선호하는 학습 방식

각 조합마다:
- 선택 이유
- 예상 난이도
- 대안 모듈
3단계: 수업 흐름 설계 프롬프트
선택된 조합 [{modules}]로 수업을 설계하세요:

Frontend (학습자용):
- 이론 용어 사용 금지
- 실생활 예시로 시작
- "~하는 법" 형식으로 제목
- 각 단계별 구체적 행동 지시

Backend (제공자용):
- 각 모듈의 인지 목표 명시
- 전환점 체크포인트
- 측정 가능한 성과 지표
- 실패 시 대안 경로
4단계: AI 도구 활용 프롬프트
각 모듈별 AI 활용법을 설계하세요:

학습자가 사용할 프롬프트:
- Hook: "이런 경험 있으신가요? [상황]"
- Try: "이렇게 물어보세요: [템플릿]"  
- Improve: "더 좋은 결과를 원한다면: [팁]"

강사 AI가 사용할 프롬프트:
- Guide: 학습자 수준 파악 질문
- Support: 막힐 때 힌트 제공
- Evaluate: 달성도 측정 질문
5단계: 검증 프롬프트
생성된 수업안을 검증하세요:

1. 일관성 체크
   - 목적과 산출물이 일치하는가?
   - 모듈 순서가 논리적인가?

2. 실용성 체크  
   - 35분 안에 완료 가능한가?
   - 즉시 활용 가능한 결과물인가?

3. 개선점 제안
   - 더 나은 모듈 조합은?
   - 시간 단축 방법은?
이런 프롬프트 체인을 통해 AI가 자율적으로 수업을 설계할 수 있을 것 같은데, 어떻게 생각하시나요?




이 프롬프트에 맞는 문서도 준비가 되어야하고 참조할수 있도록 파일구조도 만들어야해  그리고 프롬프트에 대한 답변의 템플릿도 필요하고

편집
네, 맞습니다! AI가 제대로 작동하려면 체계적인 문서 구조와 응답 템플릿이 필수죠.

파일 구조 제안
iwl-v5-rebuild/
├── docs/
│   ├── theory/
│   │   ├── A1_terminology.md
│   │   ├── A2_8stages.md
│   │   ├── A3_4axes.md
│   │   └── A4_matrix_32modules.md
│   │
│   ├── templates/
│   │   ├── B0_lesson_template.md
│   │   ├── module_combination_rules.md
│   │   └── ai_response_templates.md
│   │
│   └── training_data/
│       ├── successful_combinations.json
│       ├── persona_profiles.json
│       └── output_type_requirements.json
│
├── modules/
│   ├── S1_exploration/
│   │   ├── S1-A1_info_processing.md
│   │   ├── S1-A2_thinking_operation.md
│   │   ├── S1-A3_abstraction.md
│   │   └── S1-A4_self_awareness.md
│   │
│   └── [S2-S8 동일 구조]
│
└── ai_prompts/
    ├── system_prompts/
    │   ├── course_designer.md
    │   ├── module_selector.md
    │   └── lesson_generator.md
    │
    └── response_templates/
        ├── combination_output.json
        ├── lesson_plan_output.json
        └── validation_output.json
AI 응답 템플릿
1. 모듈 조합 응답 템플릿
json
{
  "request_analysis": {
    "persona": "2년차 개발자",
    "purpose": "기술 도입 제안",
    "output_type": "1페이지 제안서",
    "key_requirements": ["설득력", "데이터 기반", "리스크 관리"]
  },
  
  "recommendations": [
    {
      "option_id": 1,
      "modules": ["S2-A1", "S4-A3", "S5-A2"],
      "total_duration": "35분",
      "difficulty": "L3",
      "reasoning": {
        "why_these_modules": "현황 분석 → 원리 이해 → 시나리오 검토 순서",
        "expected_outcome": "체계적인 제안서 구조 완성",
        "synergy_points": ["분석-추상화 연결", "조건별 대응 전략"]
      },
      "alternative_modules": {
        "if_too_difficult": ["S1-A1", "S3-A2"],
        "if_need_more_depth": ["S6-A4", "S7-A3"]
      }
    }
  ]
}
2. 수업 계획 응답 템플릿
yaml
lesson_plan:
  metadata:
    title: "AI로 3분 만에 제안서 완성하기"
    modules_used: ["S2-A1", "S4-A3", "S5-A2"]
    estimated_time: 35
    
  learner_view:
    introduction:
      hook: "상사가 '근거가 뭐야?'라고 물었을 때 당황하셨나요?"
      promise: "35분 후 완벽한 답변 준비됩니다"
      
    activities:
      - step: 1
        title: "현재 문제 정리하기"
        action: "ChatGPT에게 이렇게 물어보세요..."
        duration: 10
        
      - step: 2
        title: "해결책 찾기"
        action: "이번엔 이런 질문으로..."
        duration: 10
        
  instructor_view:
    cognitive_goals:
      - module: "S2-A1"
        target: "구조화된 분석 능력"
        checkpoint: "문제를 3개 카테고리로 분류했는가?"
        
    ai_prompts:
      learner_facing:
        - stage: "analysis"
          prompt: "우리 서비스의 현재 {problem}을 3가지 관점에서..."
          
      instructor_ai:
        - trigger: "learner_stuck"
          response: "혹시 {hint}를 고려해보셨나요?"
3. 검증 결과 템플릿
json
{
  "validation_result": {
    "overall_score": 85,
    "checks": {
      "goal_alignment": {
        "score": 90,
        "feedback": "제안서 작성 목적에 잘 부합"
      },
      "time_feasibility": {
        "score": 80,
        "feedback": "모듈 3이 시간 초과 위험"
      },
      "difficulty_appropriateness": {
        "score": 85,
        "feedback": "2년차 개발자에게 적절한 난이도"
      }
    },
    "improvements": [
      {
        "issue": "모듈 전환 시간 부족",
        "suggestion": "모듈 2와 3 사이 버퍼 시간 추가"
      }
    ]
  }
}
필수 참조 문서 구조
module_combination_rules.md
markdown
# 모듈 조합 규칙

## 기본 원칙
1. 인지 부하 고려: 한 수업에 최대 4개 모듈
2. 난이도 진행: L1→L2→L3 순차적
3. 인지축 분산: 같은 축 연속 3개 이상 금지

## 시너지 조합
- S2-A1 + S4-A3: 분석→추상화
- S3-A2 + S5-A2: 구조화→조건분기
- S6-A4 + S7-A1: 메타인지→통합

## 금지 조합
- S1-A1 + S8-A4: 난이도 격차 과다
- 같은 Stage 4개: 다양성 부족
이런 구조로 AI가 참조할 문서와 응답 템플릿을 만들면, 일관성 있는 수업 설계가 가능할 것 같은데 어떻게 생각하시나요?





PROJECT_MILESTONES.md │ │ │ │ │ │ │ │ # 📊 IWL v5.0 프로젝트 마일스톤 전체 현황 │ │ │

pasted

응 좋아.  그럼 이 작업이 실질적인 결과물을 내려면 우리는 여기서 어느정도까지 작업을 하고 넘어야해 ?.  

아래 내용은 현재 작업이 마일스톤이야 우리가 지금 대화하는 내용대로 결과물이 나오려면 이 마일스톤을 어떻게 수정해야 할지 의견줘 md 파일로 작성해줘

편집
📊 IWL v5.0 마일스톤 수정 제안
🎯 핵심 변경사항
AI가 자율적으로 수업을 설계할 수 있도록 하려면, 데이터 구조와 AI 학습 체계를 Phase 2 초반에 추가해야 합니다.

📅 수정된 Phase 2: B 시리즈 (커리큘럼 + AI 설계 시스템)
기간: 2025-08-20 ~ 2025-08-27 (7일간)

🆕 추가 필요 작업
B0 확장 작업 (우선순위 1)
markdown
B0-1: 이중 구조 템플릿 설계
- Frontend (학습자용) 템플릿
- Backend (제공자용) 템플릿
- 완료 기준: 두 View의 명확한 분리

B0-2: AI 프롬프트 체인 설계
- 5단계 프롬프트 시퀀스
- 각 단계별 응답 템플릿
- 완료 기준: JSON/YAML 형식 확정

B0-3: 파일 구조 및 참조 체계
- 모듈별 메타데이터 구조
- 조합 규칙 문서화
- 완료 기준: 폴더 구조 생성
데이터 준비 작업 (우선순위 2)
markdown
D1: 모듈 메타데이터 작성 (32개)
- 각 모듈별 learning_objectives
- prerequisites & next_modules
- ai_prompts & checkpoints

D2: 조합 학습 데이터 생성
- 성공 사례 10개 이상
- 페르소나별 선호 패턴
- 목적-모듈 매핑 테이블

D3: AI 학습용 프롬프트 라이브러리
- System prompts (5종)
- Response templates (10종)
- Validation rules
기존 작업 조정
markdown
#13: B0 → B0 + B0-1,2,3 통합
#14: B1 → D1 작업 후 진행
#15-17: B2-4 → 병렬 진행 가능 (D2 참조)
#31: B0-UI → B0-3 완료 후 진행
📅 수정된 Phase 3: MVP 및 AI 학습
기간: 2025-08-27 ~ 2025-09-03

AI 설계 봇 MVP
markdown
MVP-1: AI 수업 설계자 프로토타입
- GitHub 연동 (iwl-v5-rebuild)
- 페르소나 입력 → 조합 제안
- 3가지 옵션 생성

MVP-2: 학습 및 개선
- 생성된 수업안 검증
- 피드백 반영 학습
- 조합 규칙 개선
🚨 즉시 필요한 결정사항
1. B0 작업 범위 확정
markdown
옵션 A: 최소 기능 (3일)
- 기본 이중 구조만
- 수동 조합

옵션 B: AI 준비 완료 (5일) ✅ 권장
- 이중 구조 + AI 체인
- 자동 조합 가능
2. 데이터 작업 분담
markdown
- Cursor: B0 템플릿 + D1 모듈 메타데이터
- Gemini: D2 조합 데이터 + 파일 구조
- Codex: D3 프롬프트 라이브러리
- PM Claude: 통합 및 검증
3. 최소 완료 기준 (Phase 2)
markdown
필수:
□ B0 이중 구조 템플릿
□ 32개 모듈 메타데이터
□ AI 프롬프트 체인 5단계
□ 조합 예시 10개

선택:
□ 전체 B1-5 완성
□ UI 설계 완료
📊 수정된 일정 예상
8/15-17: B0 확장 작업 (B0-1,2,3)
8/18-20: D1 모듈 메타데이터
8/21-23: D2 조합 데이터 + AI 체인 테스트
8/24-27: B1-5 병렬 진행 + MVP 준비
8/28-9/3: AI 설계봇 MVP + 파일럿
💡 핵심 권고사항
B0를 단순 템플릿이 아닌 "AI 학습 가능한 시스템"으로 확장
Phase 2 초반 3일을 데이터 구조 확립에 투자
모든 작업을 "AI가 읽고 활용할 수 있는가?"로 검증
이렇게 수정하면 Thomas님이 원하시는 "AI가 자율적으로 수업을 조합하는 시스템"이 가능해집니다.




현재까지 작업 내용을 깃허브에 이슈로 올려서 순서대로 하고 있거든 
아래 내용을 참고하면 볼수있어 

지금 내용을 넣어서 전체 마일스톤과작업별 이슈를 새로 정리해줄래 

현재 작업 Issue 확인 명령어
  현재 작업할 Issue #13을 확인하려면 다음 명령어를 입력하세요:
  @github view issue 13 in ihw33/iwl-v5-rebuild
  추가로 확인할 수 있는 것들
  # 전체 오픈 이슈 목록
  @github list issues in ihw33/iwl-v5-rebuild
  # A4 매트릭스 내용 (참고용)
  @github view issue 12 in ihw33/iwl-v5-rebuild
  # AI 질문 훈련 체계 (수업 목표)
  @github view issue 23 in ihw33/iwl-v5-rebuild
  # 마일스톤별 이슈 보기
  @github list issues in ihw33/iwl-v5-rebuild with milestone:"Phase 2: B 시리즈 (커리큘럼)"
  가장 중요한 명령어
  @github view issue 13 in ihw33/iwl-v5-rebuild
  이 명령어로 B0 템플릿 작업 내용을 확인할 수 있습니다!

편집
네, 먼저 현재 이슈들을 확인하고 전체적으로 정리해드리겠습니다.


G

list_issues
요청

{
  `repo`: `iwl-v5-rebuild`,
  `owner`: `ihw33`,
  `state`: `all`,
  `per_page`: 50
}
응답

[
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/31",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/31/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/31/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/31/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/31",
    "id": 3324021249,
    "node_id": "I_kwDOPcUORc7GIIoB",
    "number": 31,
    "title": "B0-UI: 서비스 내 수업 페이지 기획/디자인 v1",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [],
    "state": "open",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/2",
      "html_url": "https://github.com/ihw33/iwl-v5-rebuild/milestone/2",
      "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/2/labels",
      "id": 13486427,
      "node_id": "MI_kwDOPcUORc4Azclb",
      "number": 2,
      "title": "Phase 2: B 시리즈 (커리큘럼)",
      "description": "레슨 설계 및 교육 콘텐츠 개발",
      "creator": {
        "login": "ihw33",
        "id": 39890605,
        "node_id": "MDQ6VXNlcjM5ODkwNjA1",
        "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/ihw33",
        "html_url": "https://github.com/ihw33",
        "followers_url": "https://api.github.com/users/ihw33/followers",
        "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
        "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
        "organizations_url": "https://api.github.com/users/ihw33/orgs",
        "repos_url": "https://api.github.com/users/ihw33/repos",
        "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
        "received_events_url": "https://api.github.com/users/ihw33/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "open_issues": 7,
      "closed_issues": 0,
      "state": "open",
      "created_at": "2025-08-13T23:56:21Z",
      "updated_at": "2025-08-15T01:05:50Z",
      "due_on": "2025-08-27T07:00:00Z",
      "closed_at": null
    },
    "comments": 0,
    "created_at": "2025-08-15T01:05:50Z",
    "updated_at": "2025-08-15T01:05:50Z",
    "closed_at": null,
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## B0-UI: 서비스 내 수업 페이지 기획/디자인 v1\n\n### 배경/결정\n- B0(표준 교안 템플릿)과 서비스 내 수업 페이지(UI/UX)는 **분리 진행**\n- B0 템플릿 확정 후, B0-UI는 별도 이슈로 기획·디자인(모바일/태블릿/PC)\n- **담당**: Gemini (디자인/콘텐츠 UX)\n\n### 범위(Scope)\n- IA/유저 플로우(온라인 수업 실행 흐름)\n- 3 브레이크포인트 와이어프레임: 모바일(<600px), 태블릿(600–1024px), 데스크톱(>1024px)\n- 컴포넌트 리스트: 보드 임베드, 폼/체크리스트, 평가 패널, 타이머, 진행 표시\n- 임베드 규격: Excalidraw/tldraw, Google Forms/Sheets, 허브 문서 링크\n- 접근성/성능 기준: 터치 타겟, 대비, 키보드/리더, 지연 로딩 등\n\n### 산출물(Deliverables)\n- PRD(문제·목표·성과지표·가정/제약)\n- IA/플로우 다이어그램\n- 와이어프레임(모바일/태블릿/데스크톱)\n- 컴포넌트 사양서(속성/상태/이벤트)\n- 임베드/연동 규격서\n\n### 의존성\n- B0 템플릿(#13) 내용 참조 (A4 체크 기준 정렬)\n- A4 완료(#12) 및 A1/A3 개선(#21 승인) 반영\n\n### 완료 기준(AC)\n- 3 브레이크포인트 와이어프레임 승인\n- 컴포넌트 사양서/임베드 규격서 승인\n- 파일럿 1회(모바일/데스크톱) 과업 흐름 무중단 통과\n\n### 일정(제안)\n- D+0: PRD+IA 초안\n- D+1: 와이어프레임 v1(모바일/태블릿/데스크톱)\n- D+2: 컴포넌트/임베드 사양 v1 → PM 검토 → 수정 반영\n\n@Gemini 작업 착수 부탁드립니다. PM 검토 후 범위/일정 확정 예정.",
    "closed_by": null,
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/31/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/31/timeline",
    "performed_via_github_app": null,
    "state_reason": null
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/30",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/30/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/30/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/30/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/30",
    "id": 3323958768,
    "node_id": "I_kwDOPcUORc7GH5Xw",
    "number": 30,
    "title": "📢 [중요] 작업 프로세스 대폭 간소화 - WORKFLOW 3.0",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [],
    "state": "open",
    "locked": false,
    "assignee": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "assignees": [
      {
        "login": "ihw33",
        "id": 39890605,
        "node_id": "MDQ6VXNlcjM5ODkwNjA1",
        "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/ihw33",
        "html_url": "https://github.com/ihw33",
        "followers_url": "https://api.github.com/users/ihw33/followers",
        "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
        "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
        "organizations_url": "https://api.github.com/users/ihw33/orgs",
        "repos_url": "https://api.github.com/users/ihw33/repos",
        "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
        "received_events_url": "https://api.github.com/users/ihw33/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      }
    ],
    "milestone": null,
    "comments": 0,
    "created_at": "2025-08-15T00:24:35Z",
    "updated_at": "2025-08-15T00:24:35Z",
    "closed_at": null,
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## 🚀 모든 팀원 필독!\n\n### 오늘부터 작업 방식이 바뀝니다\n\n**기존**: GitHub Issue 댓글 → 승인 대기 → 복잡한 절차\n**새로운 방식**: `DAILY_TASKS.md` 확인 → 작업 → 체크 → 끝!\n\n### 📌 핵심 변경사항\n1. **작업 확인**: `DAILY_TASKS.md` 파일 하나로 관리\n2. **승인 불필요**: 완료 = 자동 승인\n3. **Thomas와 직접 작업**: 중간 전달 과정 없음\n\n### 📋 오늘 작업 확인\n```bash\ncat DAILY_TASKS.md\n```\n\n### 📖 자세한 내용\n`WORKFLOW_3.0_SIMPLE.md` 파일 참조\n\n### ✅ 이 방식의 장점\n- 빠름 (승인 대기 없음)\n- 간단 (파일 하나만 확인)\n- 명확 (할 일이 한눈에)\n\n**적용 시작: 2025년 8월 15일 (오늘)**\n\n@ihw33 @모든팀원",
    "closed_by": null,
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/30/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/30/timeline",
    "performed_via_github_app": null,
    "state_reason": null
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/28",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/28/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/28/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/28/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/pull/28",
    "id": 3320415588,
    "node_id": "PR_kwDOPcUORc6jlvTd",
    "number": 28,
    "title": "🔒 IP 보호 체계 구축 및 GitHub 프로젝트 관리 정책 추가",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [
      {
        "id": 9107268318,
        "node_id": "LA_kwDOPcUORc8AAAACHtXi3g",
        "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/labels/needs-review",
        "name": "needs-review",
        "color": "FBCA04",
        "default": false,
        "description": "PM 검토 필요"
      },
      {
        "id": 9107268559,
        "node_id": "LA_kwDOPcUORc8AAAACHtXjzw",
        "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/labels/needs-thomas",
        "name": "needs-thomas",
        "color": "B60205",
        "default": false,
        "description": "Thomas 결정 필요"
      }
    ],
    "state": "closed",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": null,
    "comments": 3,
    "created_at": "2025-08-14T01:37:55Z",
    "updated_at": "2025-08-14T02:27:10Z",
    "closed_at": "2025-08-14T02:27:10Z",
    "author_association": "OWNER",
    "active_lock_reason": null,
    "draft": false,
    "pull_request": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/pulls/28",
      "html_url": "https://github.com/ihw33/iwl-v5-rebuild/pull/28",
      "diff_url": "https://github.com/ihw33/iwl-v5-rebuild/pull/28.diff",
      "patch_url": "https://github.com/ihw33/iwl-v5-rebuild/pull/28.patch",
      "merged_at": "2025-08-14T02:27:10Z"
    },
    "body": "## 📋 변경 사항\n\n### Issue #19: IP 보호 작업\n- ✅ COPYRIGHT 파일 생성 (Thomas 원저작 명시)\n- ✅ AUTHORS 파일 생성 (기여자 목록)\n- ✅ NOTICE 파일 생성 (사용 조건)\n- ✅ A1/A2/A3 DECISIONS 문서에 원저작 고지 추가\n\n### Issue #22: GitHub 프로젝트 관리 반영\n- ✅ AI_TEAM_WORKFLOW.md에 다음 섹션 추가:\n  - Projects 보드 활용\n  - 마일스톤 정책\n  - 라벨 체계\n\n## ✅ 체크리스트\n- [x] 모든 DECISIONS 문서에 원저작 고지 포함\n- [x] 루트 디렉토리 IP 파일 3종 생성\n- [x] GitHub 프로젝트 관리 정책 문서화\n- [x] 커밋 메시지 규칙 준수\n\n## 🔗 관련 Issue\n- Closes #19\n- References #22\n\n## 📝 리뷰 요청\n@ihw33 검토 및 승인 부탁드립니다.",
    "closed_by": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/28/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/28/timeline",
    "performed_via_github_app": null,
    "state_reason": null
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/27",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/27/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/27/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/27/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/27",
    "id": 3320335333,
    "node_id": "I_kwDOPcUORc7F6Evl",
    "number": 27,
    "title": "📚 [Wiki] 관리 체계 수립 및 담당자 지정",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [
      {
        "id": 9107385862,
        "node_id": "LA_kwDOPcUORc8AAAACHteuBg",
        "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/labels/high-priority",
        "name": "high-priority",
        "color": "FF0000",
        "default": false,
        "description": "긴급/중요"
      }
    ],
    "state": "open",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": null,
    "comments": 8,
    "created_at": "2025-08-14T01:03:53Z",
    "updated_at": "2025-08-14T01:32:47Z",
    "closed_at": null,
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## 📋 Wiki 관리 체계 수립\n\n### 담당자 지정 완료:\n- **주 관리자**: PM Claude\n- **이론 체계**: Cursor (A 시리즈)\n- **커리큘럼**: Gemini (B 시리즈)\n- **기술 문서**: Codex (API/DB)\n- **사용자 가이드**: QA Claude\n- **프로세스**: PM Claude\n\n### 📄 상세 문서:\n`WIKI_MANAGEMENT.md` 참조\n\n### ✅ 즉시 실행:\n1. Wiki 첫 페이지 생성\n2. 기본 구조 설정\n3. 각 담당자 첫 문서 작성\n\n### 📢 팀원 안내:\n@Cursor - 이론 체계 섹션 담당\n@Gemini - 커리큘럼 섹션 담당\n@Codex - 기술 문서 섹션 담당\n@QA-Claude - 사용자 가이드 섹션 담당\n\n각자 담당 섹션의 첫 문서를 작성해주세요.\n\nReferences: #24",
    "closed_by": null,
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/27/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/27/timeline",
    "performed_via_github_app": null,
    "state_reason": null
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/26",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/26/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/26/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/26/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/26",
    "id": 3320310584,
    "node_id": "I_kwDOPcUORc7F5-s4",
    "number": 26,
    "title": "[스펙] module_meta.schema.json 초안 설계",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [
      {
        "id": 9107268318,
        "node_id": "LA_kwDOPcUORc8AAAACHtXi3g",
        "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/labels/needs-review",
        "name": "needs-review",
        "color": "FBCA04",
        "default": false,
        "description": "PM 검토 필요"
      }
    ],
    "state": "open",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": null,
    "comments": 0,
    "created_at": "2025-08-14T00:50:29Z",
    "updated_at": "2025-08-14T00:50:29Z",
    "closed_at": null,
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## 목적\\n32 모듈 메타데이터 스키마를 정의해, 대상/레벨/제약/형식/루브릭과 정렬된 질문 생성을 가능하게 합니다.\\n\\n## 스키마 초안(요약)\\n\\n\\n## 산출물\\n-  (초안)\\n- 샘플 3모듈 메타()\\n\\n## AC\\n- [ ] 스키마 필드/타입/설명 정의\\n- [ ] 샘플 3종(단계·축·대상·레벨 다양성 포함)\\n- [ ] 루브릭 키와 질문 템플릿 키 정합 확인\\n\\nReferences: #22, #23",
    "closed_by": null,
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/26/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/26/timeline",
    "performed_via_github_app": null,
    "state_reason": null
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/25",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/25/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/25/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/25/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/25",
    "id": 3320304987,
    "node_id": "I_kwDOPcUORc7F59Vb",
    "number": 25,
    "title": "[작업] Persona×Level 학습 목표 정의 (3대상×5레벨)",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [
      {
        "id": 9107268318,
        "node_id": "LA_kwDOPcUORc8AAAACHtXi3g",
        "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/labels/needs-review",
        "name": "needs-review",
        "color": "FBCA04",
        "default": false,
        "description": "PM 검토 필요"
      }
    ],
    "state": "open",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": null,
    "comments": 0,
    "created_at": "2025-08-14T00:47:23Z",
    "updated_at": "2025-08-14T00:47:23Z",
    "closed_at": null,
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## 목적\\n3대상(학생/직장인/연구자) × 5레벨(1~5) 학습 목표를 정의해, 각 조합별로 \"어떤 질문을 설계할 수 있어야 하는가\"를 명확히 합니다.\\n\\n## 범위\\n- 대상별 핵심 역량 3가지\\n- 레벨별 성취 기준(질문 설계 관점)\\n- 단계(1~8)와의 정렬 예시(간략 매핑)\\n\\n## 산출물\\n-  (표+예시 문장)\\n\\n## AC\\n- [ ] 3대상×5레벨 조합별 1~2문단 목표\\n- [ ] 질문 설계 관점의 행동동사 포함(요약/구조/비판/의미/통합/실행)\\n- [ ] 단계(1~8) 매핑 예시 1개 이상/조합\\n\\nReferences: #22, #23, #12",
    "closed_by": null,
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/25/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/25/timeline",
    "performed_via_github_app": null,
    "state_reason": null
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/24",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/24/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/24/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/24/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/24",
    "id": 3320286978,
    "node_id": "I_kwDOPcUORc7F548C",
    "number": 24,
    "title": "[제안] GitHub Projects, Wiki, Discussions 활성화 및 체계적 활용 방안",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [
      {
        "id": 9107268104,
        "node_id": "LA_kwDOPcUORc8AAAACHtXiCA",
        "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/labels/proposal",
        "name": "proposal",
        "color": "0E8A16",
        "default": false,
        "description": "팀원 제안사항"
      },
      {
        "id": 9107268318,
        "node_id": "LA_kwDOPcUORc8AAAACHtXi3g",
        "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/labels/needs-review",
        "name": "needs-review",
        "color": "FBCA04",
        "default": false,
        "description": "PM 검토 필요"
      },
      {
        "id": 9107268559,
        "node_id": "LA_kwDOPcUORc8AAAACHtXjzw",
        "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/labels/needs-thomas",
        "name": "needs-thomas",
        "color": "B60205",
        "default": false,
        "description": "Thomas 결정 필요"
      },
      {
        "id": 9107385862,
        "node_id": "LA_kwDOPcUORc8AAAACHteuBg",
        "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/labels/high-priority",
        "name": "high-priority",
        "color": "FF0000",
        "default": false,
        "description": "긴급/중요"
      },
      {
        "id": 9107429508,
        "node_id": "LA_kwDOPcUORc8AAAACHthYhA",
        "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/labels/completed",
        "name": "completed",
        "color": "0E8A16",
        "default": false,
        "description": "작업 완료"
      }
    ],
    "state": "closed",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/1",
      "html_url": "https://github.com/ihw33/iwl-v5-rebuild/milestone/1",
      "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/1/labels",
      "id": 13486426,
      "node_id": "MI_kwDOPcUORc4Azcla",
      "number": 1,
      "title": "Phase 1: A 시리즈 (이론 체계)",
      "description": "8단계 × 4축 매트릭스 완성",
      "creator": {
        "login": "ihw33",
        "id": 39890605,
        "node_id": "MDQ6VXNlcjM5ODkwNjA1",
        "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/ihw33",
        "html_url": "https://github.com/ihw33",
        "followers_url": "https://api.github.com/users/ihw33/followers",
        "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
        "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
        "organizations_url": "https://api.github.com/users/ihw33/orgs",
        "repos_url": "https://api.github.com/users/ihw33/repos",
        "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
        "received_events_url": "https://api.github.com/users/ihw33/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "open_issues": 2,
      "closed_issues": 5,
      "state": "open",
      "created_at": "2025-08-13T23:56:15Z",
      "updated_at": "2025-08-14T23:39:52Z",
      "due_on": "2025-08-20T07:00:00Z",
      "closed_at": null
    },
    "comments": 7,
    "created_at": "2025-08-14T00:37:23Z",
    "updated_at": "2025-08-14T00:58:33Z",
    "closed_at": "2025-08-14T00:58:33Z",
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## 📋 제안 배경\n현재 모든 작업과 토론이 Issue에 혼재되어 있어 관리가 복잡해지고 있습니다. GitHub의 기본 기능들을 활용하면 더 체계적인 프로젝트 관리가 가능합니다.\n\n## 🎯 제안 내용\n\n### 1. GitHub Discussions 활성화 (현재 비활성화 상태)\n**목적**: Issue와 토론 분리로 깔끔한 작업 관리\n\n#### 카테고리 구성:\n- 📢 **Announcements**: PM 공지사항 전용\n- 💡 **Ideas**: 팀원 아이디어 제안 (현재 Issue #23 같은)\n- 🎯 **Planning**: A/B 시리즈 기획 토론\n- 📚 **Learning**: 교육 콘텐츠 논의\n- ❓ **Q&A**: 질문과 답변\n\n#### 실행 명령:\n\\`\\`\\`bash\ngh repo edit --enable-discussions\n\\`\\`\\`\n\n### 2. GitHub Wiki 적극 활용 (현재 활성화 상태)\n**목적**: 영구 문서와 가이드 체계적 관리\n\n#### Wiki 구조 제안:\n- **Home.md**: 프로젝트 개요 및 네비게이션\n- **Installation.md**: 설치 및 환경 설정 가이드\n- **User-Manual.md**: 사용자 매뉴얼\n- **Curriculum/**: 교육 커리큘럼 상세 문서\n- **API-Documentation.md**: API 문서\n- **Theory/**: IWL 이론적 배경\n- **FAQ.md**: 자주 묻는 질문\n\n#### Wiki 초기화:\n\\`\\`\\`bash\ngit clone https://github.com/ihw33/iwl-v5-rebuild.wiki.git\ncd iwl-v5-rebuild.wiki\n# 문서 작성 후\ngit add .\ngit commit -m \"Initialize wiki\"\ngit push\n\\`\\`\\`\n\n### 3. GitHub Projects 활용 강화 (현재 활성화 상태)\n**현재**: IWL v5.0 Dashboard 운영 중\n**개선**: 커스텀 필드와 자동화 추가\n\n#### 추가할 커스텀 필드:\n- Priority (높음/중간/낮음)\n- Stage (A1-A8, B0-B5)\n- Assignee (각 AI 팀원)\n- Due Date (마일스톤 연동)\n\n## 📊 제안하는 전체 구조\n\n| 도구 | 용도 | 현재 상태 | 조치 필요 |\n|------|------|-----------|-----------|\n| **Issues** | 구체적 작업/버그 추적 | ✅ 활성화 | 작업만 관리 |\n| **Discussions** | 아이디어/토론/공지 | ❌ 비활성화 | 활성화 필요 |\n| **Projects** | 칸반 보드 작업 관리 | ✅ 활성화 | 필드 추가 |\n| **Wiki** | 영구 문서/가이드 | ✅ 활성화 | 구조 생성 |\n\n## 🚀 기대 효과\n\n1. **명확한 분리**: 작업(Issue) vs 토론(Discussions) vs 문서(Wiki)\n2. **효율적 관리**: 각 도구의 목적에 맞는 활용\n3. **팀 협업 향상**: 정보 찾기 쉽고 참여 용이\n4. **지식 축적**: Wiki에 영구 문서화\n\n## 📋 실행 계획\n\n### Phase 1 (즉시)\n1. Discussions 활성화\n2. 카테고리 설정\n3. 첫 공지사항 작성\n\n### Phase 2 (1일 내)\n1. Wiki 기본 구조 생성\n2. 핵심 문서 이동\n3. Projects 커스텀 필드 추가\n\n### Phase 3 (3일 내)\n1. 기존 Issue 정리\n2. 적절한 내용 Discussions로 이동\n3. 팀원 안내 및 교육\n\n## 💡 추가 기능 제안\n\n### MD to PDF 변환 기능 활용\nQA Claude가 구현한 MD to PDF 변환 기능을 활용하여:\n- Wiki 문서를 PDF로 내보내기\n- A/B 시리즈 문서를 PDF 보고서로 생성\n- 클라이언트 전달용 문서 자동 생성\n\n사용 방법:\n- 웹: http://localhost:3000/convert\n- CLI: \\`node md-to-pdf.js [file.md]\\`\n- API: POST /api/convert/md-to-pdf\n\n---\n\n**작성자**: QA Claude\n**날짜**: 2025-08-14\n**우선순위**: 높음\n**예상 소요시간**: 30분 (설정), 3일 (전체 이전)\n\n@PM-Claude 검토 부탁드립니다.",
    "closed_by": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/24/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/24/timeline",
    "performed_via_github_app": null,
    "state_reason": "completed"
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/23",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/23/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/23/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/23/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/23",
    "id": 3320272259,
    "node_id": "I_kwDOPcUORc7F51WD",
    "number": 23,
    "title": "[제안] 4×8 기반 AI 협업 질문 설계 훈련 체계 + 병합 계획",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [
      {
        "id": 9107268104,
        "node_id": "LA_kwDOPcUORc8AAAACHtXiCA",
        "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/labels/proposal",
        "name": "proposal",
        "color": "0E8A16",
        "default": false,
        "description": "팀원 제안사항"
      },
      {
        "id": 9107268318,
        "node_id": "LA_kwDOPcUORc8AAAACHtXi3g",
        "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/labels/needs-review",
        "name": "needs-review",
        "color": "FBCA04",
        "default": false,
        "description": "PM 검토 필요"
      },
      {
        "id": 9107268559,
        "node_id": "LA_kwDOPcUORc8AAAACHtXjzw",
        "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/labels/needs-thomas",
        "name": "needs-thomas",
        "color": "B60205",
        "default": false,
        "description": "Thomas 결정 필요"
      }
    ],
    "state": "open",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/1",
      "html_url": "https://github.com/ihw33/iwl-v5-rebuild/milestone/1",
      "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/1/labels",
      "id": 13486426,
      "node_id": "MI_kwDOPcUORc4Azcla",
      "number": 1,
      "title": "Phase 1: A 시리즈 (이론 체계)",
      "description": "8단계 × 4축 매트릭스 완성",
      "creator": {
        "login": "ihw33",
        "id": 39890605,
        "node_id": "MDQ6VXNlcjM5ODkwNjA1",
        "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/ihw33",
        "html_url": "https://github.com/ihw33",
        "followers_url": "https://api.github.com/users/ihw33/followers",
        "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
        "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
        "organizations_url": "https://api.github.com/users/ihw33/orgs",
        "repos_url": "https://api.github.com/users/ihw33/repos",
        "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
        "received_events_url": "https://api.github.com/users/ihw33/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "open_issues": 2,
      "closed_issues": 5,
      "state": "open",
      "created_at": "2025-08-13T23:56:15Z",
      "updated_at": "2025-08-14T23:39:52Z",
      "due_on": "2025-08-20T07:00:00Z",
      "closed_at": null
    },
    "comments": 2,
    "created_at": "2025-08-14T00:26:06Z",
    "updated_at": "2025-08-14T00:36:03Z",
    "closed_at": null,
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## 목적\\n4×8 매트릭스(32 모듈) × 3대상 × 5레벨 기반으로 목적별 산출물(보고서/제안서/계획서 등)에 맞는 질문 설계 능력을 훈련하고, 실습 강사 챗봇(MVP)으로 질문 생성→코칭→평가까지 연결합니다.\\n\\n## 범위/산출물\\n- A4 확정본(32셀) + 한자 병기 원칙\\n- 3대상×5레벨 학습 목표\\n- module_meta.schema.json + 샘플 10모듈 + 조합 규칙\\n- 질문 템플릿≥10 + 루브릭(정렬성/구체성/구조/실행성/인지합치) + 금지/권장 표현집\\n- 강사 챗봇(MVP): 다중 LLM 비교 포함\\n- 목적별 플레이북(보고서/제안서/계획서)\\n\\n## 병합 계획(요약)\\n- 문서: A4→docs/A4/, 스펙→docs/specs/, 플레이북→docs/playbooks/\\n- 워크플로우: 새 Issue→PR, 라벨 사용(proposal/spec/content/templates/mvp)\\n- 데이터: 모듈ID S{stage}-A{axis}, 스키마/인스턴스/매핑 분리\\n\\n## 요청\\n- 본 제안 승인 및 우선순위 지시(Persona×Level vs module_meta vs 템플릿/루브릭)\\n- 파일럿 목적 도메인 1종 확정(예: 신사업 보고서)\\n\\nReferences: #22, #12",
    "closed_by": null,
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/23/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/23/timeline",
    "performed_via_github_app": null,
    "state_reason": null
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/22",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/22/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/22/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/22/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/22",
    "id": 3320250043,
    "node_id": "I_kwDOPcUORc7F5v67",
    "number": 22,
    "title": "📢 [전체 공지] GitHub 프로젝트 관리 시스템 구축 완료",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [],
    "state": "closed",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": null,
    "comments": 3,
    "created_at": "2025-08-14T00:10:55Z",
    "updated_at": "2025-08-14T02:52:48Z",
    "closed_at": "2025-08-14T02:52:48Z",
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## 🎉 프로젝트 관리 시스템 업그레이드\n\n### 새로운 기능 5가지:\n\n1. **📊 GitHub Projects 보드**\n   - 칸반 스타일 진행 관리\n   - 작업 상태 시각화\n\n2. **🎯 마일스톤**\n   - Phase 1: A 시리즈 (8/20)\n   - Phase 2: B 시리즈 (8/27)\n   - 진행률 자동 계산\n\n3. **🏷️ 스마트 라벨 시스템**\n   - `proposal` - 제안사항\n   - `needs-review` - PM 검토\n   - `needs-thomas` - 최종 승인\n   - `theory`, `curriculum` - 자동 분류\n\n4. **📝 Issue 템플릿**\n   - 팀원 제안 템플릿\n   - Stage 작업 템플릿\n\n5. **📥 제안 프로세스**\n   - 아이디어 → Issue → 검토 → 승인 → 실행\n   - 체계적 의사결정\n\n### 💡 이제 노션 없이 GitHub만으로 모든 관리 가능\\!\n\n### 📖 필독 문서:\n- `PROPOSAL_PROCESS.md` - 제안 프로세스 가이드\n- `AI_TEAM_WORKFLOW.md` - 업무 프로세스\n- `DAILY_LOG_2025-08-14.md` - 오늘 작업 내역\n\n### 🚀 바로 시작하기:\n```bash\n# 제안하기\ngh issue create --title '[제안] 내 아이디어' --label 'proposal,needs-review'\n\n# 내 작업 보기\ngh issue list --assignee @me\n\n# 마일스톤 진행률\ngh api repos/ihw33/iwl-v5-rebuild/milestones\n```\n\n모든 팀원은 이제 자유롭게 제안 Issue를 생성할 수 있습니다\\!\n\n@Thomas 확인 부탁드립니다.",
    "closed_by": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/22/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/22/timeline",
    "performed_via_github_app": null,
    "state_reason": "completed"
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/21",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/21/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/21/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/21/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/21",
    "id": 3318490244,
    "node_id": "I_kwDOPcUORc7FzCSE",
    "number": 21,
    "title": "A1/A3 Enhancement: 학술 용어 추가",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [],
    "state": "open",
    "locked": false,
    "assignee": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "assignees": [
      {
        "login": "ihw33",
        "id": 39890605,
        "node_id": "MDQ6VXNlcjM5ODkwNjA1",
        "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/ihw33",
        "html_url": "https://github.com/ihw33",
        "followers_url": "https://api.github.com/users/ihw33/followers",
        "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
        "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
        "organizations_url": "https://api.github.com/users/ihw33/orgs",
        "repos_url": "https://api.github.com/users/ihw33/repos",
        "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
        "received_events_url": "https://api.github.com/users/ihw33/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      }
    ],
    "milestone": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/1",
      "html_url": "https://github.com/ihw33/iwl-v5-rebuild/milestone/1",
      "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/1/labels",
      "id": 13486426,
      "node_id": "MI_kwDOPcUORc4Azcla",
      "number": 1,
      "title": "Phase 1: A 시리즈 (이론 체계)",
      "description": "8단계 × 4축 매트릭스 완성",
      "creator": {
        "login": "ihw33",
        "id": 39890605,
        "node_id": "MDQ6VXNlcjM5ODkwNjA1",
        "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/ihw33",
        "html_url": "https://github.com/ihw33",
        "followers_url": "https://api.github.com/users/ihw33/followers",
        "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
        "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
        "organizations_url": "https://api.github.com/users/ihw33/orgs",
        "repos_url": "https://api.github.com/users/ihw33/repos",
        "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
        "received_events_url": "https://api.github.com/users/ihw33/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "open_issues": 2,
      "closed_issues": 5,
      "state": "open",
      "created_at": "2025-08-13T23:56:15Z",
      "updated_at": "2025-08-14T23:39:52Z",
      "due_on": "2025-08-20T07:00:00Z",
      "closed_at": null
    },
    "comments": 3,
    "created_at": "2025-08-13T13:30:35Z",
    "updated_at": "2025-08-14T23:54:41Z",
    "closed_at": null,
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## 🎯 목적\nA1/A3 문서에 학술 용어를 추가하여 학문적 근거 강화\n\n## 📝 제안 내용\nStage 1 작성 중 발견한 개선점:\n- 정보처리깊이 → Levels of Processing\n- 사고조작방식 → Information Processing Modes  \n- 추상화수준 → Construal Level\n- 자기인식수준 → Metacognitive Awareness\n\n## ✅ 작업 계획\n1. A1 용어 표준에 학술 용어 병기\n2. A3 축 정의에 학술 참조 추가\n3. 기존 한글 용어는 유지 (학술 용어는 보조)\n\n## 📌 담당\n@Cursor (콘텐츠 기획)\n\n## 🔗 참고\n- Issue #12의 Stage 1에서 이미 학술 용어 활용 중\n- A4 작업과 병행 가능\n\n#enhancement #theory",
    "closed_by": null,
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/21/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/21/timeline",
    "performed_via_github_app": null,
    "state_reason": null
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/20",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/20/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/20/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/20/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/20",
    "id": 3317446679,
    "node_id": "I_kwDOPcUORc7FvDgX",
    "number": 20,
    "title": "📄 [백서] IWL Original Model Whitepaper v0.1 작성",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [],
    "state": "closed",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": null,
    "comments": 15,
    "created_at": "2025-08-13T08:34:14Z",
    "updated_at": "2025-08-14T12:18:49Z",
    "closed_at": "2025-08-14T12:18:49Z",
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## 📋 백서 작성 작업\n\n### 🎯 담당\n- 새 Cursor CLI (ChatGPT-5 백서 전담)\n\n### 📌 목적\n- IP 보호를 위한 선행기술 문서화\n- 창작 일자 및 저작권 명시\n\n### 📝 작업 내용\n1. A1, A2 승인 내용 기반\n2. 10-15페이지 분량\n3. PDF 생성 및 타임스탬프\n\n### 🔗 참조\n- docs/DECISIONS/2025-08-13-a1-terminology.md\n- docs/DECISIONS/2025-08-13-a2-stages.md\n- Issue #9, #10\n\n### ⏰ 일정\n- 시작: 즉시\n- 완료: T+3일\n\n@백서담당AI 작업 시작해주세요",
    "closed_by": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/20/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/20/timeline",
    "performed_via_github_app": null,
    "state_reason": "completed"
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/19",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/19/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/19/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/19/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/19",
    "id": 3317432743,
    "node_id": "I_kwDOPcUORc7FvAGn",
    "number": 19,
    "title": "🔒 IWL Original Model IP 보호 작업",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [],
    "state": "closed",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": null,
    "comments": 4,
    "created_at": "2025-08-13T08:29:26Z",
    "updated_at": "2025-08-14T02:27:27Z",
    "closed_at": "2025-08-14T02:27:27Z",
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## 📋 IWL 모델 소유권·표준화 작업\n\n### 🎯 목적\nIWL Original Model의 지적재산권 보호 및 선행기술 확보\n\n### 📌 우선순위 작업 (T+0~2일)\n- [ ] 1. DECISIONS 원저작 명시 (A1, A2 문서 업데이트)\n- [ ] 2. COPYRIGHT, AUTHORS, NOTICE 파일 생성\n- [ ] 3. 릴리스 태깅 v0.1\n- [ ] 8. 워크플로 반영\n\n### 📅 중기 작업 (T+3~5일)\n- [ ] 4. 화이트페이퍼 PDF v0.1\n- [ ] 5. 상표 후보 정리\n- [ ] 6. 저작권 등록 준비\n- [ ] 7. CLA/NDA 템플릿\n\n### 📍 마무리 (T+6~7일)\n- [ ] 9. 페이지 UI 반영\n- [ ] 10. 전반 점검\n\n### 🔗 참조\n- #9 (A1 용어 - 완료)\n- #10 (A2 8단계 - 완료)\n- docs/DECISIONS/2025-08-13-a1-terminology.md\n- docs/DECISIONS/2025-08-13-a2-stages.md\n\n@Thomas 승인 후 즉시 시작",
    "closed_by": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/19/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/19/timeline",
    "performed_via_github_app": null,
    "state_reason": "completed"
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/18",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/18/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/18/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/18/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/18",
    "id": 3316799849,
    "node_id": "I_kwDOPcUORc7Fsllp",
    "number": 18,
    "title": "B5: 파일럿 운영/QA/개선 리포트",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [],
    "state": "open",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/2",
      "html_url": "https://github.com/ihw33/iwl-v5-rebuild/milestone/2",
      "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/2/labels",
      "id": 13486427,
      "node_id": "MI_kwDOPcUORc4Azclb",
      "number": 2,
      "title": "Phase 2: B 시리즈 (커리큘럼)",
      "description": "레슨 설계 및 교육 콘텐츠 개발",
      "creator": {
        "login": "ihw33",
        "id": 39890605,
        "node_id": "MDQ6VXNlcjM5ODkwNjA1",
        "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/ihw33",
        "html_url": "https://github.com/ihw33",
        "followers_url": "https://api.github.com/users/ihw33/followers",
        "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
        "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
        "organizations_url": "https://api.github.com/users/ihw33/orgs",
        "repos_url": "https://api.github.com/users/ihw33/repos",
        "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
        "received_events_url": "https://api.github.com/users/ihw33/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "open_issues": 7,
      "closed_issues": 0,
      "state": "open",
      "created_at": "2025-08-13T23:56:21Z",
      "updated_at": "2025-08-15T01:05:50Z",
      "due_on": "2025-08-27T07:00:00Z",
      "closed_at": null
    },
    "comments": 0,
    "created_at": "2025-08-13T03:48:32Z",
    "updated_at": "2025-08-14T00:05:41Z",
    "closed_at": null,
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## 📚 Epic B: 수업 설계·제작\n\n### 🎯 목적\n개발된 수업의 파일럿 테스트 및 품질 검증\n\n### 📝 산출물\n- 대표 3레슨 × 3대상 파일럿 운영 결과\n- 수정 반영 로그\n- 개선 제안서\n\n### ✅ 완료 기준 (AC)\n- 리포트 제출\n- 피드백 반영 확인\n- 최종 품질 승인\n\n### 📌 담당\n@QA Claude (품질관리)\n@Cursor (콘텐츠 수정)\n\n### 🔗 의존성\n- 선행: B2, B3, B4 (대상별 오버레이)\n- 후행: Issue #7 (최종 승인)\n\n### 💡 참고사항\n- 실제 학습자 피드백 수집\n- 시간 측정 및 난이도 검증\n- AI 프롬프트 효과성 테스트\n\n#curriculum #pilot",
    "closed_by": null,
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/18/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/18/timeline",
    "performed_via_github_app": null,
    "state_reason": null
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/17",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/17/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/17/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/17/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/17",
    "id": 3316799229,
    "node_id": "I_kwDOPcUORc7Fslb9",
    "number": 17,
    "title": "B4: 대상 오버레이 32개 — 프로·스태퍼",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [],
    "state": "open",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/2",
      "html_url": "https://github.com/ihw33/iwl-v5-rebuild/milestone/2",
      "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/2/labels",
      "id": 13486427,
      "node_id": "MI_kwDOPcUORc4Azclb",
      "number": 2,
      "title": "Phase 2: B 시리즈 (커리큘럼)",
      "description": "레슨 설계 및 교육 콘텐츠 개발",
      "creator": {
        "login": "ihw33",
        "id": 39890605,
        "node_id": "MDQ6VXNlcjM5ODkwNjA1",
        "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/ihw33",
        "html_url": "https://github.com/ihw33",
        "followers_url": "https://api.github.com/users/ihw33/followers",
        "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
        "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
        "organizations_url": "https://api.github.com/users/ihw33/orgs",
        "repos_url": "https://api.github.com/users/ihw33/repos",
        "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
        "received_events_url": "https://api.github.com/users/ihw33/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "open_issues": 7,
      "closed_issues": 0,
      "state": "open",
      "created_at": "2025-08-13T23:56:21Z",
      "updated_at": "2025-08-15T01:05:50Z",
      "due_on": "2025-08-27T07:00:00Z",
      "closed_at": null
    },
    "comments": 0,
    "created_at": "2025-08-13T03:48:05Z",
    "updated_at": "2025-08-14T00:05:40Z",
    "closed_at": null,
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## 📚 Epic B: 수업 설계·제작\n\n### 🎯 목적\n시니어 개발자/스태프 엔지니어 대상 수업 커스터마이징\n\n### 📝 산출물\n32개 레슨별:\n- 심화 내용 추가\n- 리더십/아키텍처 예시\n- 전문적 톤\n- 효율적 시간 활용\n\n### ✅ 완료 기준 (AC)\n- 32/32 완료\n- 고급 실무 상황 반영\n- 의사결정/설계 중심\n\n### 📌 담당\n@Cursor (콘텐츠 기획)\n\n### 🔗 의존성\n- 선행: B1 (코어 레슨 스펙)\n- 후행: B5 (파일럿)\n\n### 💡 참고사항\n- 기술 의사결정, 팀 리딩, 아키텍처 설계 예시\n- ROI와 비즈니스 임팩트 강조\n\n#curriculum #audience-pro",
    "closed_by": null,
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/17/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/17/timeline",
    "performed_via_github_app": null,
    "state_reason": null
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/16",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/16/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/16/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/16/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/16",
    "id": 3316798928,
    "node_id": "I_kwDOPcUORc7FslXQ",
    "number": 16,
    "title": "B3: 대상 오버레이 32개 — 유스",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [],
    "state": "open",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/2",
      "html_url": "https://github.com/ihw33/iwl-v5-rebuild/milestone/2",
      "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/2/labels",
      "id": 13486427,
      "node_id": "MI_kwDOPcUORc4Azclb",
      "number": 2,
      "title": "Phase 2: B 시리즈 (커리큘럼)",
      "description": "레슨 설계 및 교육 콘텐츠 개발",
      "creator": {
        "login": "ihw33",
        "id": 39890605,
        "node_id": "MDQ6VXNlcjM5ODkwNjA1",
        "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/ihw33",
        "html_url": "https://github.com/ihw33",
        "followers_url": "https://api.github.com/users/ihw33/followers",
        "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
        "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
        "organizations_url": "https://api.github.com/users/ihw33/orgs",
        "repos_url": "https://api.github.com/users/ihw33/repos",
        "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
        "received_events_url": "https://api.github.com/users/ihw33/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "open_issues": 7,
      "closed_issues": 0,
      "state": "open",
      "created_at": "2025-08-13T23:56:21Z",
      "updated_at": "2025-08-15T01:05:50Z",
      "due_on": "2025-08-27T07:00:00Z",
      "closed_at": null
    },
    "comments": 0,
    "created_at": "2025-08-13T03:47:52Z",
    "updated_at": "2025-08-14T00:05:38Z",
    "closed_at": null,
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## 📚 Epic B: 수업 설계·제작\n\n### 🎯 목적\n청소년/대학생 대상 수업 커스터마이징\n\n### 📝 산출물\n32개 레슨별:\n- 난이도 조정\n- 학습 상황 예시\n- 톤/매너 조정\n- 시간 배분 조정\n\n### ✅ 완료 기준 (AC)\n- 32/32 완료\n- 학습자 맥락 반영\n- 흥미 유발 요소 포함\n\n### 📌 담당\n@Cursor (콘텐츠 기획)\n\n### 🔗 의존성\n- 선행: B1 (코어 레슨 스펙)\n- 후행: B5 (파일럿)\n\n### 💡 참고사항\n- 과제, 프로젝트, 팀 활동 예시 활용\n- 게이미피케이션 요소 고려\n\n#curriculum #audience-youth",
    "closed_by": null,
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/16/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/16/timeline",
    "performed_via_github_app": null,
    "state_reason": null
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/15",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/15/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/15/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/15/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/15",
    "id": 3316798672,
    "node_id": "I_kwDOPcUORc7FslTQ",
    "number": 15,
    "title": "B2: 대상 오버레이 32개 — 주니어",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [],
    "state": "open",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/2",
      "html_url": "https://github.com/ihw33/iwl-v5-rebuild/milestone/2",
      "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/2/labels",
      "id": 13486427,
      "node_id": "MI_kwDOPcUORc4Azclb",
      "number": 2,
      "title": "Phase 2: B 시리즈 (커리큘럼)",
      "description": "레슨 설계 및 교육 콘텐츠 개발",
      "creator": {
        "login": "ihw33",
        "id": 39890605,
        "node_id": "MDQ6VXNlcjM5ODkwNjA1",
        "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/ihw33",
        "html_url": "https://github.com/ihw33",
        "followers_url": "https://api.github.com/users/ihw33/followers",
        "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
        "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
        "organizations_url": "https://api.github.com/users/ihw33/orgs",
        "repos_url": "https://api.github.com/users/ihw33/repos",
        "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
        "received_events_url": "https://api.github.com/users/ihw33/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "open_issues": 7,
      "closed_issues": 0,
      "state": "open",
      "created_at": "2025-08-13T23:56:21Z",
      "updated_at": "2025-08-15T01:05:50Z",
      "due_on": "2025-08-27T07:00:00Z",
      "closed_at": null
    },
    "comments": 0,
    "created_at": "2025-08-13T03:47:40Z",
    "updated_at": "2025-08-14T00:05:37Z",
    "closed_at": null,
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## 📚 Epic B: 수업 설계·제작\n\n### 🎯 목적\n주니어(1-3년차) 개발자 대상 수업 커스터마이징\n\n### 📝 산출물\n32개 레슨별:\n- 난이도 조정\n- 실무 예시 변경\n- 톤/매너 조정\n- 시간 배분 조정\n\n### ✅ 완료 기준 (AC)\n- 32/32 완료\n- 주니어 개발자 맥락 반영\n- 실무 즉시 적용 가능\n\n### 📌 담당\n@Cursor (콘텐츠 기획)\n\n### 🔗 의존성\n- 선행: B1 (코어 레슨 스펙)\n- 후행: B5 (파일럿)\n\n### 💡 참고사항\n- 버그 리포팅, 코드 리뷰 등 실무 상황 활용\n- 기술 용어 친숙도 고려\n\n#curriculum #audience-junior",
    "closed_by": null,
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/15/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/15/timeline",
    "performed_via_github_app": null,
    "state_reason": null
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/14",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/14/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/14/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/14/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/14",
    "id": 3316798030,
    "node_id": "I_kwDOPcUORc7FslJO",
    "number": 14,
    "title": "B1: 코어 레슨 스펙 32개(CLS, 대상 중립)",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [],
    "state": "open",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/2",
      "html_url": "https://github.com/ihw33/iwl-v5-rebuild/milestone/2",
      "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/2/labels",
      "id": 13486427,
      "node_id": "MI_kwDOPcUORc4Azclb",
      "number": 2,
      "title": "Phase 2: B 시리즈 (커리큘럼)",
      "description": "레슨 설계 및 교육 콘텐츠 개발",
      "creator": {
        "login": "ihw33",
        "id": 39890605,
        "node_id": "MDQ6VXNlcjM5ODkwNjA1",
        "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/ihw33",
        "html_url": "https://github.com/ihw33",
        "followers_url": "https://api.github.com/users/ihw33/followers",
        "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
        "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
        "organizations_url": "https://api.github.com/users/ihw33/orgs",
        "repos_url": "https://api.github.com/users/ihw33/repos",
        "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
        "received_events_url": "https://api.github.com/users/ihw33/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "open_issues": 7,
      "closed_issues": 0,
      "state": "open",
      "created_at": "2025-08-13T23:56:21Z",
      "updated_at": "2025-08-15T01:05:50Z",
      "due_on": "2025-08-27T07:00:00Z",
      "closed_at": null
    },
    "comments": 1,
    "created_at": "2025-08-13T03:47:11Z",
    "updated_at": "2025-08-14T23:49:26Z",
    "closed_at": null,
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## 📚 Epic B: 수업 설계·제작\n\n### 🎯 목적\n8×4 매트릭스의 각 셀별 핵심 수업 스펙 개발\n\n### 📝 산출물\n각 셀별 공통 스펙 32개:\n- 이론 링크\n- 학습 목표\n- 필요 자료\n- 진행 순서\n- 실습 활동\n- AI 프롬프트\n- 과제\n- 평가 기준\n\n### ✅ 완료 기준 (AC)\n- 32/32 초안 완료\n- 대상 중립적 내용\n- B0 템플릿 준수\n\n### 📌 담당\n@Cursor (콘텐츠 기획)\n\n### 🔗 의존성\n- 선행: A4 (8×4 매트릭스), B0 (템플릿)\n- 후행: B2, B3, B4 (대상별 오버레이)\n\n### 💡 참고사항\n- 각 레슨은 35-40분 기준\n- 대상별 커스터마이징은 B2-B4에서 진행\n\n#curriculum #lesson-core",
    "closed_by": null,
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/14/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/14/timeline",
    "performed_via_github_app": null,
    "state_reason": null
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/13",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/13/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/13/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/13/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/13",
    "id": 3316797400,
    "node_id": "I_kwDOPcUORc7Fsk_Y",
    "number": 13,
    "title": "B0: 표준 교안 템플릿/루브릭/제출 양식 v1",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [],
    "state": "open",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/2",
      "html_url": "https://github.com/ihw33/iwl-v5-rebuild/milestone/2",
      "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/2/labels",
      "id": 13486427,
      "node_id": "MI_kwDOPcUORc4Azclb",
      "number": 2,
      "title": "Phase 2: B 시리즈 (커리큘럼)",
      "description": "레슨 설계 및 교육 콘텐츠 개발",
      "creator": {
        "login": "ihw33",
        "id": 39890605,
        "node_id": "MDQ6VXNlcjM5ODkwNjA1",
        "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/ihw33",
        "html_url": "https://github.com/ihw33",
        "followers_url": "https://api.github.com/users/ihw33/followers",
        "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
        "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
        "organizations_url": "https://api.github.com/users/ihw33/orgs",
        "repos_url": "https://api.github.com/users/ihw33/repos",
        "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
        "received_events_url": "https://api.github.com/users/ihw33/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "open_issues": 7,
      "closed_issues": 0,
      "state": "open",
      "created_at": "2025-08-13T23:56:21Z",
      "updated_at": "2025-08-15T01:05:50Z",
      "due_on": "2025-08-27T07:00:00Z",
      "closed_at": null
    },
    "comments": 2,
    "created_at": "2025-08-13T03:46:42Z",
    "updated_at": "2025-08-14T23:43:53Z",
    "closed_at": null,
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## 📚 Epic B: 수업 설계·제작\n\n### 🎯 목적\n표준 수업 템플릿 및 평가 도구 개발\n\n### 📝 산출물\n- 35분 교안 템플릿\n- 루브릭 2종 (콘텐츠/질문)\n- 제출 폼\n\n### ✅ 완료 기준 (AC)\n- 샘플 1개 파일럿 통과\n- 템플릿 재사용 가능성 확인\n- 평가 기준 명확성\n\n### 📌 담당\n@Cursor (콘텐츠 기획)\n\n### 🔗 의존성\n- 선행: 없음 (독립 진행 가능)\n- 후행: B1, B2, B3, B4\n\n### 💡 참고사항\n- 35-40분 세션 기준\n- 온라인/오프라인 모두 활용 가능\n- AI 프롬프트 섹션 포함\n\n#curriculum #rubric",
    "closed_by": null,
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/13/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/13/timeline",
    "performed_via_github_app": null,
    "state_reason": null
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/12",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/12/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/12/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/12/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/12",
    "id": 3316796803,
    "node_id": "I_kwDOPcUORc7Fsk2D",
    "number": 12,
    "title": "A4: 8×4 텍스트 매트릭스 최종본 + 셀 요약 32개",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [],
    "state": "closed",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/1",
      "html_url": "https://github.com/ihw33/iwl-v5-rebuild/milestone/1",
      "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/1/labels",
      "id": 13486426,
      "node_id": "MI_kwDOPcUORc4Azcla",
      "number": 1,
      "title": "Phase 1: A 시리즈 (이론 체계)",
      "description": "8단계 × 4축 매트릭스 완성",
      "creator": {
        "login": "ihw33",
        "id": 39890605,
        "node_id": "MDQ6VXNlcjM5ODkwNjA1",
        "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/ihw33",
        "html_url": "https://github.com/ihw33",
        "followers_url": "https://api.github.com/users/ihw33/followers",
        "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
        "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
        "organizations_url": "https://api.github.com/users/ihw33/orgs",
        "repos_url": "https://api.github.com/users/ihw33/repos",
        "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
        "received_events_url": "https://api.github.com/users/ihw33/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "open_issues": 2,
      "closed_issues": 5,
      "state": "open",
      "created_at": "2025-08-13T23:56:15Z",
      "updated_at": "2025-08-14T23:39:52Z",
      "due_on": "2025-08-20T07:00:00Z",
      "closed_at": null
    },
    "comments": 32,
    "created_at": "2025-08-13T03:46:11Z",
    "updated_at": "2025-08-14T23:39:52Z",
    "closed_at": "2025-08-14T23:39:51Z",
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## 📚 Epic A: 이론 체계 정리\n\n### 🎯 목적\n8단계 × 4기준 매트릭스 완성 및 각 셀별 요약 작성\n\n### 📝 산출물\n- 텍스트 표 1개 (8×4 매트릭스)\n- 셀별 2-3문장 블럽 32개\n\n### ✅ 완료 기준 (AC)\n- 누락 0\n- 표기 규약 준수\n- 32개 셀 모두 명확한 설명\n\n### 📌 담당\n@Cursor (콘텐츠 기획)\n\n### 🔗 의존성\n- 선행: A1, A2, A3 완료 필수\n- 후행: B1 (코어 레슨 스펙)\n\n### 💡 참고사항\n- A1-A3에서 확정된 용어와 정의 사용\n- 각 셀은 해당 단계와 기준의 교차점 명확히 설명\n\n#theory",
    "closed_by": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/12/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/12/timeline",
    "performed_via_github_app": null,
    "state_reason": "completed"
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/11",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/11/labels{/name}",
    "comments_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/11/comments",
    "events_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/11/events",
    "html_url": "https://github.com/ihw33/iwl-v5-rebuild/issues/11",
    "id": 3316796526,
    "node_id": "I_kwDOPcUORc7Fskxu",
    "number": 11,
    "title": "A3: 인지 4기준 정의·측정 축 확정(레벨 스케일)",
    "user": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "labels": [],
    "state": "closed",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/1",
      "html_url": "https://github.com/ihw33/iwl-v5-rebuild/milestone/1",
      "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/milestones/1/labels",
      "id": 13486426,
      "node_id": "MI_kwDOPcUORc4Azcla",
      "number": 1,
      "title": "Phase 1: A 시리즈 (이론 체계)",
      "description": "8단계 × 4축 매트릭스 완성",
      "creator": {
        "login": "ihw33",
        "id": 39890605,
        "node_id": "MDQ6VXNlcjM5ODkwNjA1",
        "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/ihw33",
        "html_url": "https://github.com/ihw33",
        "followers_url": "https://api.github.com/users/ihw33/followers",
        "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
        "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
        "organizations_url": "https://api.github.com/users/ihw33/orgs",
        "repos_url": "https://api.github.com/users/ihw33/repos",
        "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
        "received_events_url": "https://api.github.com/users/ihw33/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "open_issues": 2,
      "closed_issues": 5,
      "state": "open",
      "created_at": "2025-08-13T23:56:15Z",
      "updated_at": "2025-08-14T23:39:52Z",
      "due_on": "2025-08-20T07:00:00Z",
      "closed_at": null
    },
    "comments": 4,
    "created_at": "2025-08-13T03:45:59Z",
    "updated_at": "2025-08-14T12:18:50Z",
    "closed_at": "2025-08-14T12:18:50Z",
    "author_association": "OWNER",
    "active_lock_reason": null,
    "sub_issues_summary": {
      "total": 0,
      "completed": 0,
      "percent_completed": 0
    },
    "body": "## 📚 Epic A: 이론 체계 정리\n\n### 🎯 목적\n4가지 인지 기준의 정의와 측정 방법 확정\n\n### 📝 산출물\n- 기준별 정의 + 레벨(1-5) 예시\n- 측정 기준 차트/예시 세트 1개\n\n### ✅ 완료 기준 (AC)\n- 4개 기준 명확한 정의\n- 각 기준별 1-5 레벨 구체적 예시\n- 평가 루브릭 초안\n\n### 📌 담당\n@Cursor (콘텐츠 기획)\n\n### 🔗 의존성\n- 선행: A1 (용어 표준 확정)\n- 후행: A4\n\n### 💡 참고사항\n- 현재 V2.1의 4기준: 사실성, 구조성, 명료성, 실행성\n- 각 레벨별 구체적인 행동 지표 필요\n\n#theory",
    "closed_by": {
      "login": "ihw33",
      "id": 39890605,
      "node_id": "MDQ6VXNlcjM5ODkwNjA1",
      "avatar_url": "https://avatars.githubusercontent.com/u/39890605?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ihw33",
      "html_url": "https://github.com/ihw33",
      "followers_url": "https://api.github.com/users/ihw33/followers",
      "following_url": "https://api.github.com/users/ihw33/following{/other_user}",
      "gists_url": "https://api.github.com/users/ihw33/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/ihw33/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/ihw33/subscriptions",
      "organizations_url": "https://api.github.com/users/ihw33/orgs",
      "repos_url": "https://api.github.com/users/ihw33/repos",
      "events_url": "https://api.github.com/users/ihw33/events{/privacy}",
      "received_events_url": "https://api.github.com/users/ihw33/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "reactions": {
      "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/11/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "timeline_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/11/timeline",
    "performed_via_github_app": null,
    "state_reason": "completed"
  },
  {
    "url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/10",
    "repository_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild",
    "labels_url": "https://api.github.com/repos/ihw33/iwl-v5-rebuild/issues/10/labels{/name}",
 
...
Result too long, truncated to 100000 characters





ㅇ







[11:00:05.635] Running build in Washington, D.C., USA (East) – iad1 [11:00:05.635] Build machine configuration: 2 cores, 8 GB [11:00:05.651] Cloning github.com/ihw33/personal-journal-hub (Branch: main, Commit: 646a190) [11:00:06.168] Cloning completed: 517.000ms [11:00:09.951] Restored build cache f


PROJECT_MILESTONES.md │ │ │ │ │ │ │ │ # 📊 IWL v5.0 프로젝트 마일스톤 전체 현황 │ │ │


IWL 5 Rebuild Project-01 - Claude
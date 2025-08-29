#!/bin/bash

# 🎭 IWL v5.0 페르소나 자동 보고 도구
# 사용법: ./persona_report.sh [페르소나] [작업내용] [상태]
# 예시: ./persona_report.sh "Frontend Lead" "대시보드 UI 구현" "completed"

# 색상 정의
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# 변수 설정
PERSONA="${1:-PM Claude}"
TASK="${2:-작업 진행}"
STATUS="${3:-in_progress}"
ISSUE_NUM="${4:-34}"
REPO="ihw33/iwl-v5-rebuild"

# 페르소나별 스타일 정의
get_persona_style() {
    case "$1" in
        "PM Claude")
            EMOJI="🎯"
            FOCUS="전체 프로젝트 관리"
            TONE="체계적이고 전략적인"
            CLOSING="팀워크가 꿈을 현실로 만듭니다"
            ;;
        "Frontend Lead")
            EMOJI="🎨"
            FOCUS="UI/UX 및 성능"
            TONE="픽셀 퍼펙트한"
            CLOSING="사용자 경험을 한 단계 더 높였습니다"
            ;;
        "Backend Lead")
            EMOJI="🔒"
            FOCUS="보안 및 안정성"
            TONE="견고하고 안전한"
            CLOSING="Zero-downtime으로 안정적으로 배포했습니다"
            ;;
        "AI/ML Lead"|"AI Lead")
            EMOJI="🤖"
            FOCUS="모델 성능"
            TONE="데이터 기반의"
            CLOSING="AI가 교육을 더 스마트하게 만들고 있습니다"
            ;;
        "QA Lead")
            EMOJI="🔍"
            FOCUS="품질 보증"
            TONE="꼼꼼하고 체계적인"
            CLOSING="버그 제로를 향해 나아갑니다"
            ;;
        "DevOps Lead")
            EMOJI="🚀"
            FOCUS="자동화 및 효율성"
            TONE="최적화된"
            CLOSING="인프라가 개발을 가속화합니다"
            ;;
        "Design Lead")
            EMOJI="🎭"
            FOCUS="디자인 일관성"
            TONE="아름답고 직관적인"
            CLOSING="디자인이 사용자와 소통합니다"
            ;;
        "Content Lead")
            EMOJI="📚"
            FOCUS="교육 콘텐츠"
            TONE="교육적이고 체계적인"
            CLOSING="지식이 성장의 씨앗이 됩니다"
            ;;
        *)
            EMOJI="💻"
            FOCUS="개발 작업"
            TONE="전문적인"
            CLOSING="한 걸음씩 목표를 향해 나아갑니다"
            ;;
    esac
}

# 상태별 메시지 생성
get_status_message() {
    case "$1" in
        "completed")
            echo "✅ 작업 완료"
            ;;
        "in_progress")
            echo "🔄 작업 진행 중"
            ;;
        "blocked")
            echo "🚨 블로커 발생"
            ;;
        "reviewing")
            echo "👀 리뷰 중"
            ;;
        *)
            echo "📝 작업 시작"
            ;;
    esac
}

# 페르소나 스타일 가져오기
get_persona_style "$PERSONA"
STATUS_MSG=$(get_status_message "$STATUS")

# 현재 시간
TIMESTAMP=$(date +"%Y-%m-%d %H:%M")

# GitHub 코멘트 본문 생성
generate_comment() {
    cat <<EOF
$EMOJI $PERSONA 작업 보고
━━━━━━━━━━━━━━━━━━━━━━
$STATUS_MSG: $TASK

📊 주요 내용
- $FOCUS 최적화 진행
- $TONE 접근 방식 적용

⏰ 타임스탬프: $TIMESTAMP

$CLOSING $EMOJI
EOF
}

# 메인 실행
main() {
    echo -e "${CYAN}🎭 IWL v5.0 페르소나 보고 시스템${NC}"
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    
    # 정보 출력
    echo -e "${GREEN}페르소나:${NC} $PERSONA $EMOJI"
    echo -e "${GREEN}작업:${NC} $TASK"
    echo -e "${GREEN}상태:${NC} $STATUS"
    echo -e "${GREEN}이슈:${NC} #$ISSUE_NUM"
    echo ""
    
    # 코멘트 미리보기
    echo -e "${BLUE}📝 생성될 코멘트:${NC}"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    generate_comment
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    
    # 확인 프롬프트
    read -p "이 내용으로 GitHub에 코멘트를 작성하시겠습니까? (y/n): " -n 1 -r
    echo ""
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${YELLOW}GitHub에 코멘트 작성 중...${NC}"
        
        # GitHub CLI로 코멘트 작성
        COMMENT=$(generate_comment)
        gh issue comment $ISSUE_NUM -R $REPO --body "$COMMENT"
        
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✅ 코멘트가 성공적으로 작성되었습니다!${NC}"
            echo -e "${CYAN}확인: https://github.com/$REPO/issues/$ISSUE_NUM${NC}"
        else
            echo -e "${RED}❌ 코멘트 작성 실패${NC}"
            exit 1
        fi
    else
        echo -e "${YELLOW}취소되었습니다.${NC}"
    fi
}

# 도움말
show_help() {
    cat <<EOF
🎭 IWL v5.0 페르소나 자동 보고 도구

사용법:
  $0 [페르소나] [작업내용] [상태] [이슈번호]

예시:
  $0 "Frontend Lead" "대시보드 UI 구현" "completed"
  $0 "Backend Lead" "API 엔드포인트 구축" "in_progress" 35
  $0 "AI/ML Lead" "모델 통합" "blocked"

페르소나 목록:
  - PM Claude
  - Frontend Lead
  - Backend Lead
  - AI/ML Lead
  - QA Lead
  - DevOps Lead
  - Design Lead
  - Content Lead

상태 옵션:
  - completed: 작업 완료
  - in_progress: 진행 중
  - blocked: 블로커 발생
  - reviewing: 리뷰 중
  - starting: 시작

기본값:
  - 페르소나: PM Claude
  - 상태: in_progress
  - 이슈: #34
EOF
}

# 인자 확인
if [[ "$1" == "-h" ]] || [[ "$1" == "--help" ]]; then
    show_help
    exit 0
fi

# 메인 함수 실행
main
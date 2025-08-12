// 2-8단계 교육 콘텐츠 데이터

export interface LessonStage {
  stage: number;
  title: string;
  subtitle: string;
  objectives: string[];
  theoreticalFoundation: {
    title: string;
    theories: Array<{
      name: string;
      description: string;
    }>;
  };
  learnerMindset: string;
  lessonFlow: {
    intro: { duration: string; content: string[] };
    main: { duration: string; content: string[] };
    wrap: { duration: string; content: string[] };
  };
  practiceActivities: Array<{
    title: string;
    description: string;
    steps?: string[];
  }>;
  aiStrategy: {
    prompt: string;
    usage: string;
  };
}

export const lessonStages: LessonStage[] = [
  {
    stage: 1,
    title: "지각인지",
    subtitle: "감각적 인식과 관찰",
    objectives: [
      "감각적 인지 능력 향상",
      "순간 집중력 훈련",
      "관찰력과 인식력 강화"
    ],
    theoreticalFoundation: {
      title: "지각인지 단계의 이론적 배경",
      theories: [
        {
          name: "지각 심리학",
          description: "감각 정보의 수용과 처리"
        },
        {
          name: "주의 이론",
          description: "선택적 주의와 집중"
        },
        {
          name: "게슈탈트 원리",
          description: "전체적 지각 패턴"
        }
      ]
    },
    learnerMindset: "모든 감각을 열고 세상을 새롭게 바라보는 관찰자가 되자",
    lessonFlow: {
      intro: {
        duration: "5분",
        content: ["지각인지란 무엇인가?", "일상의 인지 패턴 점검"]
      },
      main: {
        duration: "25분",
        content: ["감각 기반 실습", "관찰력 훈련 활동", "세부 묘사 연습"]
      },
      wrap: {
        duration: "5분",
        content: ["학습 내용 정리", "다음 단계 예고"]
      }
    },
    practiceActivities: [
      {
        title: "감각 기반 목록 만들기",
        description: "주변 환경에서 보이는, 들리는, 느껴지는 것들을 5분간 목록화",
        steps: [
          "1분간 조용히 집중",
          "시각, 청각, 촉각 순서로 인지",
          "목록 작성 및 공유"
        ]
      },
      {
        title: "책상 위 물건 묘사 실습",
        description: "책상 위 하나의 물건을 선택해 최대한 세밀하게 묘사하기"
      }
    ],
    aiStrategy: {
      prompt: "이 물체를 본 적 없는 사람에게 설명한다면 어떻게 묘사하시겠습니까?",
      usage: "AI를 활용한 묘사력 향상 피드백"
    }
  },
  {
    stage: 2,
    title: "요약·맥락 이해",
    subtitle: "핵심 추출과 압축",
    objectives: [
      "핵심 정보 추출 능력 향상",
      "맥락적 이해력 개발",
      "효율적 정보 압축 기술 습득"
    ],
    theoreticalFoundation: {
      title: "요약과 이해의 인지과정",
      theories: [
        {
          name: "블룸의 인지분류학",
          description: "이해(Understanding) 단계"
        },
        {
          name: "스키마 이론",
          description: "기존 지식구조에 새 정보 통합"
        },
        {
          name: "정보처리이론",
          description: "작업기억에서 장기기억으로의 전환"
        }
      ]
    },
    learnerMindset: "복잡한 정보 속에서 핵심을 찾아내는 탐정이 되자",
    lessonFlow: {
      intro: {
        duration: "5분",
        content: ["요약의 중요성", "일상 속 요약 사례"]
      },
      main: {
        duration: "25분",
        content: ["핵심어 추출 연습", "문단 요약 실습", "맥락 파악 훈련"]
      },
      wrap: {
        duration: "5분",
        content: ["요약 기법 정리", "셀프 체크리스트"]
      }
    },
    practiceActivities: [
      {
        title: "3줄 요약 챌린지",
        description: "긴 문서를 3줄로 요약하기",
        steps: [
          "전체 내용 스캔",
          "핵심 키워드 추출",
          "3개 문장으로 압축"
        ]
      },
      {
        title: "키워드 마인드맵",
        description: "중심 주제에서 파생되는 핵심 개념 연결"
      },
      {
        title: "5W1H 프레임워크",
        description: "누가, 언제, 어디서, 무엇을, 왜, 어떻게 정리"
      }
    ],
    aiStrategy: {
      prompt: "다음 텍스트의 핵심 3가지를 추출하고 각각 한 문장으로 설명해주세요",
      usage: "요약 결과 비교 및 피드백"
    }
  },
  {
    stage: 3,
    title: "구조적 이해",
    subtitle: "패턴과 관계 파악",
    objectives: [
      "정보의 계층 구조 파악",
      "논리적 연결고리 발견",
      "체계적 분석 능력 강화"
    ],
    theoreticalFoundation: {
      title: "구조적 사고의 이론적 기반",
      theories: [
        {
          name: "게슈탈트 심리학",
          description: "전체와 부분의 관계"
        },
        {
          name: "시스템 사고",
          description: "상호작용과 피드백 루프"
        },
        {
          name: "구조주의 인식론",
          description: "패턴과 관계 중심 이해"
        }
      ]
    },
    learnerMindset: "건축가처럼 구조를 파악하고 설계도를 그리자",
    lessonFlow: {
      intro: {
        duration: "5분",
        content: ["구조의 힘", "레고 블록 비유"]
      },
      main: {
        duration: "25분",
        content: ["정보 분해 연습", "관계도 작성", "계층 구조 시각화"]
      },
      wrap: {
        duration: "5분",
        content: ["구조화 체크리스트", "실전 적용 팁"]
      }
    },
    practiceActivities: [
      {
        title: "플로우차트 변환",
        description: "복잡한 프로세스를 플로우차트로 변환",
        steps: [
          "시작과 끝 정의",
          "주요 단계 식별",
          "분기점과 조건 표시"
        ]
      },
      {
        title: "개념 관계도",
        description: "핵심 개념 간 관계를 시각적으로 표현"
      },
      {
        title: "MECE 원칙 적용",
        description: "상호배타적이고 전체포괄적인 분류 연습"
      }
    ],
    aiStrategy: {
      prompt: "이 내용을 계층 구조로 정리하고 각 요소 간 관계를 설명해주세요",
      usage: "구조 분석 검증"
    }
  },
  {
    stage: 4,
    title: "비판적 사고",
    subtitle: "논리와 근거 검증",
    objectives: [
      "논리적 오류 식별 능력",
      "다각도 관점 분석",
      "근거 기반 판단력 향상"
    ],
    theoreticalFoundation: {
      title: "비판적 사고의 이론적 토대",
      theories: [
        {
          name: "논리학",
          description: "연역/귀납 추론"
        },
        {
          name: "비판적 사고론",
          description: "폴과 엘더의 사고 표준"
        },
        {
          name: "인지편향 이론",
          description: "확증편향, 후견편향 극복"
        }
      ]
    },
    learnerMindset: "모든 주장에 '왜?'라고 질문하는 탐구자가 되자",
    lessonFlow: {
      intro: {
        duration: "5분",
        content: ["비판적 사고의 필요성", "일상 속 논리 오류"]
      },
      main: {
        duration: "25분",
        content: ["논증 구조 분석", "전제와 결론 구분", "반대 논거 찾기"]
      },
      wrap: {
        duration: "5분",
        content: ["비판적 사고 체크리스트", "실천 가이드"]
      }
    },
    practiceActivities: [
      {
        title: "논리 오류 탐정",
        description: "뉴스 기사의 논리적 오류 찾기",
        steps: [
          "주장과 근거 분리",
          "논리적 연결 검증",
          "숨겨진 전제 발견"
        ]
      },
      {
        title: "악마의 변호인",
        description: "반대 입장에서 논증하기"
      },
      {
        title: "SWOT 분석",
        description: "강점, 약점, 기회, 위협 분석"
      }
    ],
    aiStrategy: {
      prompt: "이 주장의 논리적 약점과 대안적 관점을 제시해주세요",
      usage: "논증 강화 피드백"
    }
  },
  {
    stage: 5,
    title: "의미 파악",
    subtitle: "심층적 해석과 통찰",
    objectives: [
      "심층적 의미 해석 능력",
      "함축과 상징 이해",
      "맥락적 통찰력 개발"
    ],
    theoreticalFoundation: {
      title: "의미 해석의 이론적 기반",
      theories: [
        {
          name: "해석학",
          description: "텍스트와 맥락의 순환적 이해"
        },
        {
          name: "기호학",
          description: "의미 생성과 해석"
        },
        {
          name: "문화심리학",
          description: "문화적 맥락의 영향"
        }
      ]
    },
    learnerMindset: "표면 너머의 깊은 의미를 읽어내는 해석자가 되자",
    lessonFlow: {
      intro: {
        duration: "5분",
        content: ["의미의 층위", "빙산 모델"]
      },
      main: {
        duration: "25분",
        content: ["은유와 상징 해석", "문맥 속 함의 찾기", "다층적 의미 분석"]
      },
      wrap: {
        duration: "5분",
        content: ["의미 해석 프레임워크", "실전 적용"]
      }
    },
    practiceActivities: [
      {
        title: "광고 메시지 분석",
        description: "광고의 숨은 의도와 심리 전략 파악",
        steps: [
          "표면적 메시지 확인",
          "타겟 오디언스 분석",
          "숨은 욕구 자극 포인트"
        ]
      },
      {
        title: "문학 작품 해석",
        description: "상징과 은유의 의미 탐구"
      },
      {
        title: "사회 현상 읽기",
        description: "트렌드 뒤의 심층 의미 분석"
      }
    ],
    aiStrategy: {
      prompt: "이 텍스트의 표면적 의미와 함축적 의미를 구분하여 설명해주세요",
      usage: "다양한 해석 관점 제공"
    }
  },
  {
    stage: 6,
    title: "창조적 통합",
    subtitle: "혁신과 융합",
    objectives: [
      "이질적 요소의 창의적 결합",
      "새로운 아이디어 생성",
      "혁신적 해결책 도출"
    ],
    theoreticalFoundation: {
      title: "창의성과 혁신의 이론",
      theories: [
        {
          name: "창의성 이론",
          description: "발산적/수렴적 사고"
        },
        {
          name: "SCAMPER 기법",
          description: "체계적 창의 발상"
        },
        {
          name: "디자인 씽킹",
          description: "인간 중심 문제해결"
        }
      ]
    },
    learnerMindset: "서로 다른 퍼즐 조각을 연결하는 창조자가 되자",
    lessonFlow: {
      intro: {
        duration: "5분",
        content: ["창의성의 본질", "연결의 힘"]
      },
      main: {
        duration: "25분",
        content: ["강제 연결법 실습", "브레인스토밍 세션", "아이디어 통합 워크숍"]
      },
      wrap: {
        duration: "5분",
        content: ["창의적 사고 도구 정리", "일상 적용법"]
      }
    },
    practiceActivities: [
      {
        title: "랜덤 단어 조합",
        description: "무작위 단어를 연결한 새로운 아이디어",
        steps: [
          "랜덤 단어 3개 선택",
          "강제 연결 시도",
          "실용적 아이디어로 발전"
        ]
      },
      {
        title: "리디자인 프로젝트",
        description: "기존 제품/서비스 혁신적 개선"
      },
      {
        title: "크로스오버 컨셉",
        description: "서로 다른 분야 융합"
      }
    ],
    aiStrategy: {
      prompt: "A와 B를 결합한 혁신적인 아이디어 10개를 제안해주세요",
      usage: "아이디어 확장과 구체화"
    }
  },
  {
    stage: 7,
    title: "실행",
    subtitle: "계획과 행동",
    objectives: [
      "계획 수립과 실행 능력",
      "프로젝트 관리 기술",
      "결과 도출과 개선"
    ],
    theoreticalFoundation: {
      title: "실행력의 과학",
      theories: [
        {
          name: "목표 설정 이론",
          description: "SMART 목표와 동기부여"
        },
        {
          name: "애자일 방법론",
          description: "반복적 개선과 적응"
        },
        {
          name: "그릿 연구",
          description: "끈기와 열정의 결합"
        }
      ]
    },
    learnerMindset: "생각을 현실로 만드는 실행가가 되자",
    lessonFlow: {
      intro: {
        duration: "5분",
        content: ["실행의 중요성", "성공 사례 분석"]
      },
      main: {
        duration: "25분",
        content: ["액션 플랜 작성", "마일스톤 설정", "리스크 관리"]
      },
      wrap: {
        duration: "5분",
        content: ["실행 체크리스트", "모니터링 시스템"]
      }
    },
    practiceActivities: [
      {
        title: "30일 프로젝트",
        description: "한 달 실행 계획서 작성",
        steps: [
          "명확한 목표 설정",
          "주간 마일스톤 정의",
          "일일 액션 아이템"
        ]
      },
      {
        title: "간트 차트 제작",
        description: "프로젝트 일정 시각화"
      },
      {
        title: "MVP 개발",
        description: "최소기능제품 프로토타입"
      }
    ],
    aiStrategy: {
      prompt: "이 목표를 달성하기 위한 단계별 실행 계획을 작성해주세요",
      usage: "실행 과정 모니터링과 조언"
    }
  },
  {
    stage: 8,
    title: "메타인지",
    subtitle: "사고에 대한 사고",
    objectives: [
      "자기 사고 과정 인식",
      "학습 전략 최적화",
      "지속적 성장 시스템 구축"
    ],
    theoreticalFoundation: {
      title: "메타인지의 과학",
      theories: [
        {
          name: "플라벨의 메타인지",
          description: "인지에 대한 인지"
        },
        {
          name: "반성적 실천",
          description: "숀의 실천가 이론"
        },
        {
          name: "자기조절학습",
          description: "짐머만의 SRL 모델"
        }
      ]
    },
    learnerMindset: "내 사고를 관찰하고 개선하는 마스터가 되자",
    lessonFlow: {
      intro: {
        duration: "5분",
        content: ["메타인지의 힘", "학습의 학습"]
      },
      main: {
        duration: "25분",
        content: ["사고 과정 기록", "학습 일지 작성", "피드백 루프 설계"]
      },
      wrap: {
        duration: "5분",
        content: ["성장 로드맵 작성", "자기 평가 시스템"]
      }
    },
    practiceActivities: [
      {
        title: "사고 프로토콜",
        description: "문제해결 과정 실시간 기록",
        steps: [
          "사고 과정 음성 녹음",
          "패턴과 습관 분석",
          "개선점 도출"
        ]
      },
      {
        title: "학습 포트폴리오",
        description: "성장 과정 문서화"
      },
      {
        title: "개인 대시보드",
        description: "학습 지표 추적 시스템"
      }
    ],
    aiStrategy: {
      prompt: "내 사고 과정을 분석하고 개선점을 제안해주세요",
      usage: "맞춤형 학습 경로 추천"
    }
  }
];

// 단계별 색상 (기존 constants와 일치)
export const STAGE_COLORS: { [key: number]: string } = {
  1: "#FF6B6B", // 지각인지: 빨강
  2: "#4ECDC4", // 요약이해: 청록
  3: "#45B7D1", // 구조적이해: 파랑
  4: "#96CEB4", // 비판적사고: 녹색
  5: "#FFEAA7", // 의미파악: 노랑
  6: "#DDA0DD", // 창조적통합: 보라
  7: "#98D8C8", // 실행: 민트
  8: "#F7DC6F"  // 메타인지: 금색
};

// 단계별 아이콘
export const STAGE_ICONS: { [key: number]: string } = {
  1: "👁️",  // 지각인지
  2: "📝",  // 요약이해
  3: "🏗️",  // 구조적이해
  4: "🔍",  // 비판적사고
  5: "💡",  // 의미파악
  6: "🎨",  // 창조적통합
  7: "🚀",  // 실행
  8: "🧠"   // 메타인지
};
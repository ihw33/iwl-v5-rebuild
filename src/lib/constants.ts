// 8단계 사고별 고유 색상
export const THINKING_STAGE_COLORS = {
  1: "#FF6B6B", // 지각 인지: 빨강
  2: "#4ECDC4", // 요약·맥락 이해: 청록
  3: "#45B7D1", // 구조적 이해: 파랑
  4: "#96CEB4", // 비판적 사고: 연두
  5: "#FFEAA7", // 보이지 않는 의미: 노랑
  6: "#DDA0DD", // 창조적 통합: 보라
  7: "#98D8C8", // 실행: 민트
  8: "#F7DC6F", // 메타인지: 금색
} as const;

// 4가지 기준별 색상
export const CRITERIA_COLORS = {
  정보처리깊이: "#2563EB", // 진한 파랑
  사고조작방식: "#7C3AED", // 진한 보라
  추상화수준: "#059669", // 진한 초록
  자기인식수준: "#DC2626", // 진한 빨강
} as const;

// 8단계 사고 데이터
export const THINKING_STAGES = [
  { id: 1, name: "지각 인지", description: "감각적 수용", english: "Perceptual Recognition" },
  { id: 2, name: "요약·맥락 이해", description: "의미 단위 해석", english: "Summary & Context Understanding" },
  { id: 3, name: "구조적 이해", description: "깊은 해석", english: "Structural Understanding" },
  { id: 4, name: "비판적 사고", description: "분석/분해", english: "Critical Thinking" },
  { id: 5, name: "의미 파악", description: "추론적 해석", english: "Meaning Recognition" },
  { id: 6, name: "창조적 통합", description: "다층 정보 통합", english: "Creative Integration" },
  { id: 7, name: "실행", description: "실천적 재구성", english: "Execution" },
  { id: 8, name: "메타인지", description: "사고 위의 사고", english: "Metacognition" },
] as const;

// 4가지 구분 기준
export const CRITERIA = [
  "정보처리깊이",
  "사고조작방식", 
  "추상화수준",
  "자기인식수준",
] as const;

// 8x4 매트릭스 데이터
export const MATRIX_DATA = [
  ["감각적 수용", "수동적 반응", "없음", "없음"],
  ["의미단위해석", "구조 인식", "낮음", "미약"],
  ["깊은 해석", "논리 조합", "중간", "의식 일부"],
  ["분석/분해", "판단/분석", "높은추상", "자기논증시작"],
  ["추론적해석", "암시 해석", "상징/은유", "메타적 감지"],
  ["다층정보통합", "통합적연결", "고도추상화", "자기사고활용"],
  ["실천적재구성", "목표 지향", "현실화", "전략적 조절"],
  ["사고위의사고", "사고 점검", "메타수준", "고도자기인식"],
] as const;

// 4가지 기준별 8단계 진행도 (0-100%)
export const CRITERIA_PROGRESSION = {
  정보처리깊이: [10, 25, 40, 55, 70, 85, 95, 100],
  사고조작방식: [5, 20, 35, 50, 65, 80, 90, 100],
  추상화수준: [0, 15, 30, 50, 70, 85, 95, 100],
  자기인식수준: [0, 10, 25, 45, 65, 80, 90, 100],
} as const;
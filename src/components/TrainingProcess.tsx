import { Card, CardContent } from "./ui/card";
import { ArrowRight, Search, Brain, Settings, Play, RotateCcw } from "lucide-react";

const TRAINING_STEPS = [
  {
    id: 1,
    icon: Search,
    title: "입문진단",
    activities: [
      "현재 사고 패턴 분석",
      "개인별 강약점 진단",
      "학습 목표 설정"
    ],
    time: "1-2시간",
    color: "#FF6B6B"
  },
  {
    id: 2,
    icon: Brain,
    title: "사고구조이해",
    activities: [
      "8단계 모델 학습",
      "각 단계별 특징 이해",
      "실제 적용 사례 분석"
    ],
    time: "3-4시간",
    color: "#4ECDC4"
  },
  {
    id: 3,
    icon: Settings,
    title: "훈련루틴설계",
    activities: [
      "개인별 훈련 계획",
      "단계별 실습 설계",
      "진도 관리 시스템"
    ],
    time: "2-3시간",
    color: "#45B7D1"
  },
  {
    id: 4,
    icon: Play,
    title: "실전적용",
    activities: [
      "프로젝트 기반 실습",
      "실무 문제 해결",
      "동료 피드백"
    ],
    time: "5-10시간",
    color: "#96CEB4"
  },
  {
    id: 5,
    icon: RotateCcw,
    title: "사고확장루프",
    activities: [
      "성과 분석 및 개선",
      "고급 기법 학습",
      "지속적 발전 계획"
    ],
    time: "지속적",
    color: "#DDA0DD"
  }
];

export function TrainingProcess() {
  return (
    <div className="mb-12">
      <div className="text-center mb-8">
        <h2 className="text-2xl mb-2">5단계 훈련 프로세스</h2>
        <p className="text-muted-foreground">체계적인 사고력 향상을 위한 단계별 학습 과정</p>
      </div>

      <div className="flex flex-col lg:flex-row gap-4 items-center">
        {TRAINING_STEPS.map((step, index) => (
          <div key={step.id} className="flex items-center w-full lg:w-auto">
            <Card className="hover:shadow-lg transition-all hover:scale-105 w-full lg:w-64">
              <CardContent className="p-6">
                <div className="text-center mb-4">
                  <div 
                    className="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-3"
                    style={{ backgroundColor: step.color + "20" }}
                  >
                    <step.icon 
                      className="w-8 h-8"
                      style={{ color: step.color }}
                    />
                  </div>
                  <h3 className="text-lg mb-1">{step.title}</h3>
                  <p className="text-sm text-muted-foreground">{step.time}</p>
                </div>

                <div className="space-y-2">
                  {step.activities.map((activity, actIndex) => (
                    <div key={actIndex} className="flex items-start gap-2">
                      <div 
                        className="w-2 h-2 rounded-full mt-2 flex-shrink-0"
                        style={{ backgroundColor: step.color }}
                      ></div>
                      <p className="text-sm">{activity}</p>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>

            {index < TRAINING_STEPS.length - 1 && (
              <div className="hidden lg:flex items-center justify-center mx-4">
                <ArrowRight 
                  className="w-6 h-6 text-muted-foreground"
                />
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
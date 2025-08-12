import { THINKING_STAGES, THINKING_STAGE_COLORS } from "../lib/constants";
import { ArrowDown } from "lucide-react";

export function ThinkingStagesVisualization() {
  return (
    <div className="w-full max-w-4xl mx-auto p-6">
      <div className="text-center mb-8">
        <h2 className="text-3xl mb-2">8단계 사고 모델 도식</h2>
        <p className="text-muted-foreground">사고가 1단계에서 8단계로 확장되는 과정</p>
      </div>

      <div className="space-y-4">
        {THINKING_STAGES.map((stage, index) => (
          <div key={stage.id} className="relative">
            {/* 단계 카드 */}
            <div 
              className="rounded-lg p-6 shadow-md hover:shadow-lg transition-shadow relative overflow-hidden"
              style={{ 
                backgroundColor: THINKING_STAGE_COLORS[stage.id as keyof typeof THINKING_STAGE_COLORS] + "15",
                marginLeft: `${index * 30}px`,
                borderLeft: `4px solid ${THINKING_STAGE_COLORS[stage.id as keyof typeof THINKING_STAGE_COLORS]}`
              }}
            >
              <div className="flex items-center gap-4">
                {/* 단계 번호 */}
                <div 
                  className="w-12 h-12 rounded-full flex items-center justify-center text-white text-lg"
                  style={{ backgroundColor: THINKING_STAGE_COLORS[stage.id as keyof typeof THINKING_STAGE_COLORS] }}
                >
                  {stage.id}
                </div>

                {/* 단계 정보 */}
                <div className="flex-1">
                  <h3 className="text-xl mb-1">{stage.name}</h3>
                  <p className="text-sm text-muted-foreground mb-2">{stage.english}</p>
                  <p className="text-sm">{stage.description}</p>
                </div>

                {/* 진행 표시 */}
                <div className="text-right">
                  <div className="text-sm text-muted-foreground">단계 {stage.id}/8</div>
                  <div className="w-20 h-2 bg-muted rounded-full mt-1">
                    <div 
                      className="h-full rounded-full transition-all"
                      style={{ 
                        width: `${(stage.id / 8) * 100}%`,
                        backgroundColor: THINKING_STAGE_COLORS[stage.id as keyof typeof THINKING_STAGE_COLORS]
                      }}
                    ></div>
                  </div>
                </div>
              </div>
            </div>

            {/* 화살표 */}
            {index < THINKING_STAGES.length - 1 && (
              <div 
                className="flex justify-center my-4"
                style={{ marginLeft: `${(index + 1) * 30}px` }}
              >
                <div 
                  className="p-2 rounded-full"
                  style={{ backgroundColor: THINKING_STAGE_COLORS[(stage.id + 1) as keyof typeof THINKING_STAGE_COLORS] + "20" }}
                >
                  <ArrowDown 
                    className="w-5 h-5"
                    style={{ color: THINKING_STAGE_COLORS[(stage.id + 1) as keyof typeof THINKING_STAGE_COLORS] }}
                  />
                </div>
              </div>
            )}
          </div>
        ))}
      </div>

      {/* 요약 정보 */}
      <div className="mt-12 p-6 bg-muted/30 rounded-lg">
        <h3 className="text-lg mb-3">사고 발전 과정</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
          <div>
            <h4 className="mb-2">초기 단계 (1-2단계)</h4>
            <p className="text-muted-foreground">감각적 수용과 기본적인 의미 파악</p>
          </div>
          <div>
            <h4 className="mb-2">중간 단계 (3-4단계)</h4>
            <p className="text-muted-foreground">구조적 이해와 비판적 분석</p>
          </div>
          <div>
            <h4 className="mb-2">고급 단계 (5-6단계)</h4>
            <p className="text-muted-foreground">깊은 의미 파악과 창조적 통합</p>
          </div>
          <div>
            <h4 className="mb-2">최고 단계 (7-8단계)</h4>
            <p className="text-muted-foreground">실행과 메타인지 수준</p>
          </div>
        </div>
      </div>
    </div>
  );
}
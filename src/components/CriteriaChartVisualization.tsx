import { CRITERIA, CRITERIA_COLORS, CRITERIA_PROGRESSION, THINKING_STAGES } from "../lib/constants";

export function CriteriaChartVisualization() {
  return (
    <div className="w-full max-w-6xl mx-auto p-6">
      <div className="text-center mb-8">
        <h2 className="text-3xl mb-2">4가지 구분 기준 차트</h2>
        <p className="text-muted-foreground">8단계 사고를 구분하는 4가지 축의 변화</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {CRITERIA.map((criterion) => (
          <div key={criterion} className="bg-white rounded-lg shadow-lg p-6">
            <div className="flex items-center gap-3 mb-6">
              <div 
                className="w-4 h-4 rounded-full"
                style={{ backgroundColor: CRITERIA_COLORS[criterion] }}
              ></div>
              <h3 className="text-xl">{criterion}</h3>
            </div>

            {/* 바 차트 */}
            <div className="space-y-3">
              {THINKING_STAGES.map((stage, index) => {
                const progress = CRITERIA_PROGRESSION[criterion][index];
                return (
                  <div key={stage.id} className="flex items-center gap-3">
                    {/* 단계 라벨 */}
                    <div className="w-8 text-sm text-center">{stage.id}</div>
                    
                    {/* 프로그레스 바 */}
                    <div className="flex-1 relative">
                      <div className="w-full h-6 bg-muted rounded-full overflow-hidden">
                        <div 
                          className="h-full transition-all duration-1000 ease-out flex items-center justify-end pr-2 text-white text-xs"
                          style={{ 
                            width: `${progress}%`,
                            backgroundColor: CRITERIA_COLORS[criterion]
                          }}
                        >
                          {progress > 20 && `${progress}%`}
                        </div>
                      </div>
                    </div>

                    {/* 단계명 */}
                    <div className="w-24 text-xs text-muted-foreground">
                      {stage.name}
                    </div>
                  </div>
                );
              })}
            </div>

            {/* 기준별 설명 */}
            <div className="mt-6 p-4 bg-muted/30 rounded-lg">
              <div className="text-sm">
                {criterion === "정보처리깊이" && (
                  <>
                    <strong>정보 처리 깊이:</strong> 감각적 수용에서 사고 위의 사고까지의 정보 처리 수준
                  </>
                )}
                {criterion === "사고조작방식" && (
                  <>
                    <strong>사고 조작 방식:</strong> 수동적 반응에서 능동적 사고 점검까지의 조작 방식
                  </>
                )}
                {criterion === "추상화수준" && (
                  <>
                    <strong>추상화 수준:</strong> 구체적 감각에서 메타 수준까지의 추상화 정도
                  </>
                )}
                {criterion === "자기인식수준" && (
                  <>
                    <strong>자기 인식 수준:</strong> 무의식에서 고도 자기 인식까지의 자각 수준
                  </>
                )}
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* 전체 비교 차트 */}
      <div className="mt-12 bg-white rounded-lg shadow-lg p-6">
        <h3 className="text-xl mb-6 text-center">4가지 기준 종합 비교</h3>
        
        <div className="space-y-6">
          {THINKING_STAGES.map((stage, stageIndex) => (
            <div key={stage.id} className="border-l-4 border-muted pl-4">
              <div className="flex items-center gap-3 mb-3">
                <span className="text-lg">{stage.id}단계</span>
                <span className="text-muted-foreground">{stage.name}</span>
              </div>
              
              <div className="grid grid-cols-4 gap-4">
                {CRITERIA.map((criterion) => {
                  const progress = CRITERIA_PROGRESSION[criterion][stageIndex];
                  return (
                    <div key={criterion} className="text-center">
                      <div className="text-xs text-muted-foreground mb-1">{criterion}</div>
                      <div 
                        className="w-full h-2 rounded-full"
                        style={{ backgroundColor: CRITERIA_COLORS[criterion] + "20" }}
                      >
                        <div 
                          className="h-full rounded-full transition-all"
                          style={{ 
                            width: `${progress}%`,
                            backgroundColor: CRITERIA_COLORS[criterion]
                          }}
                        ></div>
                      </div>
                      <div className="text-xs mt-1">{progress}%</div>
                    </div>
                  );
                })}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
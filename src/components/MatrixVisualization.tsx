import { THINKING_STAGES, CRITERIA, MATRIX_DATA, THINKING_STAGE_COLORS, CRITERIA_COLORS } from "../lib/constants";

export function MatrixVisualization() {
  return (
    <div className="w-full max-w-6xl mx-auto p-6">
      <div className="text-center mb-8">
        <h2 className="text-3xl mb-2">8×4 매트릭스 시각화</h2>
        <p className="text-muted-foreground">32개 셀로 구성된 사고 훈련 매트릭스</p>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full border-collapse bg-white rounded-lg shadow-lg">
          {/* 헤더 */}
          <thead>
            <tr>
              <th className="p-4 bg-muted border border-border"></th>
              {CRITERIA.map((criterion) => (
                <th 
                  key={criterion}
                  className="p-4 border border-border text-center min-w-[180px]"
                  style={{ backgroundColor: CRITERIA_COLORS[criterion] + "20" }}
                >
                  <div className="flex flex-col items-center gap-1">
                    <div 
                      className="w-4 h-4 rounded-full"
                      style={{ backgroundColor: CRITERIA_COLORS[criterion] }}
                    ></div>
                    <span className="text-sm">{criterion}</span>
                  </div>
                </th>
              ))}
            </tr>
          </thead>

          {/* 본문 */}
          <tbody>
            {THINKING_STAGES.map((stage, rowIndex) => (
              <tr key={stage.id}>
                {/* 좌측 라벨 */}
                <td 
                  className="p-4 border border-border text-center min-w-[200px]"
                  style={{ backgroundColor: THINKING_STAGE_COLORS[stage.id as keyof typeof THINKING_STAGE_COLORS] + "20" }}
                >
                  <div className="flex items-center gap-3">
                    <div 
                      className="w-8 h-8 rounded-full flex items-center justify-center text-white text-sm"
                      style={{ backgroundColor: THINKING_STAGE_COLORS[stage.id as keyof typeof THINKING_STAGE_COLORS] }}
                    >
                      {stage.id}
                    </div>
                    <div className="text-left">
                      <div className="text-sm">{stage.name}</div>
                      <div className="text-xs text-muted-foreground">{stage.english}</div>
                    </div>
                  </div>
                </td>

                {/* 각 셀 */}
                {MATRIX_DATA[rowIndex].map((cellContent, colIndex) => {
                  const cellId = rowIndex * 4 + colIndex + 1;
                  return (
                    <td 
                      key={colIndex}
                      className="p-4 border border-border text-center hover:bg-muted/50 transition-colors cursor-pointer group relative"
                    >
                      <div className="text-sm">{cellContent}</div>
                      <div className="text-xs text-muted-foreground mt-1">셀 {cellId}</div>
                      
                      {/* 툴팁 */}
                      <div className="absolute invisible group-hover:visible bg-gray-900 text-white text-xs rounded p-2 bottom-full left-1/2 transform -translate-x-1/2 mb-2 whitespace-nowrap z-10">
                        {THINKING_STAGES[rowIndex].name} × {CRITERIA[colIndex]}
                        <div className="absolute top-full left-1/2 transform -translate-x-1/2 border-4 border-transparent border-t-gray-900"></div>
                      </div>
                    </td>
                  );
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* 범례 */}
      <div className="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <h3 className="text-lg mb-3">8단계 사고</h3>
          <div className="grid grid-cols-2 gap-2">
            {THINKING_STAGES.map((stage) => (
              <div key={stage.id} className="flex items-center gap-2 text-sm">
                <div 
                  className="w-3 h-3 rounded-full"
                  style={{ backgroundColor: THINKING_STAGE_COLORS[stage.id as keyof typeof THINKING_STAGE_COLORS] }}
                ></div>
                <span>{stage.id}. {stage.name}</span>
              </div>
            ))}
          </div>
        </div>

        <div>
          <h3 className="text-lg mb-3">4가지 구분 기준</h3>
          <div className="grid grid-cols-1 gap-2">
            {CRITERIA.map((criterion) => (
              <div key={criterion} className="flex items-center gap-2 text-sm">
                <div 
                  className="w-3 h-3 rounded-full"
                  style={{ backgroundColor: CRITERIA_COLORS[criterion] }}
                ></div>
                <span>{criterion}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
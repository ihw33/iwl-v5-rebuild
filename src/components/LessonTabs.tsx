"use client";

import { Tabs, TabsContent, TabsList, TabsTrigger } from "./ui/tabs";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
import { Collapsible, CollapsibleContent, CollapsibleTrigger } from "./ui/collapsible";
import { Button } from "./ui/button";
import { ChevronDown, Eye, PenTool, Bot, Clock, Target, BookOpen, CheckCircle, Brain, Lightbulb } from "lucide-react";
import { useState } from "react";
import { lessonStages, STAGE_COLORS, STAGE_ICONS } from "../data/lessonContent";

export function LessonTabs() {
  const [openSections, setOpenSections] = useState<{ [key: string]: boolean }>({});

  const toggleSection = (section: string) => {
    setOpenSections(prev => ({ ...prev, [section]: !prev[section] }));
  };

  return (
    <div className="mb-12">
      <div className="text-center mb-8">
        <h2 className="text-2xl mb-2">실습 교안</h2>
        <p className="text-muted-foreground">8단계 사고 확장 훈련 프로그램</p>
      </div>

      <Tabs defaultValue="stage1" className="w-full">
        <TabsList className="grid w-full grid-cols-4 gap-2 h-auto p-2">
          {lessonStages.slice(0, 4).map((stage) => (
            <TabsTrigger 
              key={stage.stage} 
              value={`stage${stage.stage}`}
              className="flex items-center gap-1 text-xs py-2"
            >
              <span>{STAGE_ICONS[stage.stage]}</span>
              <span>{stage.stage}단계: {stage.title}</span>
            </TabsTrigger>
          ))}
        </TabsList>
        
        <TabsList className="grid w-full grid-cols-4 gap-2 h-auto p-2 mt-2">
          {lessonStages.slice(4, 8).map((stage) => (
            <TabsTrigger 
              key={stage.stage} 
              value={`stage${stage.stage}`}
              className="flex items-center gap-1 text-xs py-2"
            >
              <span>{STAGE_ICONS[stage.stage]}</span>
              <span>{stage.stage}단계: {stage.title}</span>
            </TabsTrigger>
          ))}
        </TabsList>

        {/* 각 단계별 탭 내용 */}
        {lessonStages.map((stage) => (
          <TabsContent key={stage.stage} value={`stage${stage.stage}`} className="mt-6">
            <div className="space-y-6">
              {/* 단계 헤더 */}
              <div className="text-center p-4 rounded-lg" style={{ backgroundColor: STAGE_COLORS[stage.stage] + "20" }}>
                <h3 className="text-2xl mb-2">
                  {STAGE_ICONS[stage.stage]} {stage.stage}단계: {stage.title}
                </h3>
                <p className="text-lg text-muted-foreground">{stage.subtitle}</p>
                <div className="mt-3 p-3 bg-white/80 rounded-md inline-block">
                  <p className="text-sm italic">"{stage.learnerMindset}"</p>
                </div>
              </div>

              {/* 학습 목표 */}
              <Card style={{ borderLeft: `4px solid ${STAGE_COLORS[stage.stage]}` }}>
                <CardHeader className="pb-3">
                  <CardTitle className="flex items-center gap-2">
                    <Target className="w-5 h-5" style={{ color: STAGE_COLORS[stage.stage] }} />
                    학습 목표
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <ul className="space-y-2">
                    {stage.objectives.map((objective, idx) => (
                      <li key={idx} className="flex items-start gap-2">
                        <CheckCircle className="w-4 h-4 mt-0.5 text-green-500 flex-shrink-0" />
                        <span>{objective}</span>
                      </li>
                    ))}
                  </ul>
                </CardContent>
              </Card>

              {/* 수업 구성 */}
              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <Clock className="w-5 h-5 text-blue-500" />
                    수업 구성 (총 35분)
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div className="text-center p-4 bg-blue-50 rounded-lg">
                      <h4 className="mb-2">도입 ({stage.lessonFlow.intro.duration})</h4>
                      <div className="text-sm text-muted-foreground space-y-1">
                        {stage.lessonFlow.intro.content.map((item, idx) => (
                          <p key={idx}>{item}</p>
                        ))}
                      </div>
                    </div>
                    <div className="text-center p-4 bg-green-50 rounded-lg">
                      <h4 className="mb-2">본 수업 ({stage.lessonFlow.main.duration})</h4>
                      <div className="text-sm text-muted-foreground space-y-1">
                        {stage.lessonFlow.main.content.map((item, idx) => (
                          <p key={idx}>{item}</p>
                        ))}
                      </div>
                    </div>
                    <div className="text-center p-4 bg-purple-50 rounded-lg">
                      <h4 className="mb-2">마무리 ({stage.lessonFlow.wrap.duration})</h4>
                      <div className="text-sm text-muted-foreground space-y-1">
                        {stage.lessonFlow.wrap.content.map((item, idx) => (
                          <p key={idx}>{item}</p>
                        ))}
                      </div>
                    </div>
                  </div>
                </CardContent>
              </Card>

              {/* 실습 활동 */}
              <div className="space-y-4">
                <h3 className="text-xl mb-4 flex items-center gap-2">
                  <PenTool className="w-5 h-5 text-orange-500" />
                  실습 활동
                </h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {stage.practiceActivities.map((activity, idx) => (
                    <Card key={idx} className="hover:shadow-lg transition-shadow">
                      <CardHeader>
                        <CardTitle className="text-lg">{activity.title}</CardTitle>
                      </CardHeader>
                      <CardContent>
                        <p className="text-sm text-muted-foreground mb-3">{activity.description}</p>
                        {activity.steps && (
                          <div className="space-y-1">
                            <p className="text-sm mb-2">진행 단계:</p>
                            {activity.steps.map((step, stepIdx) => (
                              <div key={stepIdx} className="flex items-start gap-2">
                                <div className="w-1.5 h-1.5 rounded-full bg-blue-500 mt-1.5 flex-shrink-0"></div>
                                <span className="text-sm">{step}</span>
                              </div>
                            ))}
                          </div>
                        )}
                      </CardContent>
                    </Card>
                  ))}
                </div>
              </div>

              {/* AI 협력 전략 */}
              <Card className="border-purple-200 bg-purple-50/50">
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <Bot className="w-5 h-5 text-purple-500" />
                    AI 협력 전략
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    <div>
                      <h5 className="text-sm mb-2">프롬프트 예시:</h5>
                      <div className="p-3 bg-white rounded-md border border-purple-200">
                        <code className="text-sm">{stage.aiStrategy.prompt}</code>
                      </div>
                    </div>
                    <div>
                      <h5 className="text-sm mb-2">활용 방법:</h5>
                      <p className="text-sm text-muted-foreground">{stage.aiStrategy.usage}</p>
                    </div>
                  </div>
                </CardContent>
              </Card>

              {/* 이론적 토대 (접을 수 있는 섹션) */}
              <Collapsible 
                open={openSections[`theory${stage.stage}`]} 
                onOpenChange={() => toggleSection(`theory${stage.stage}`)}
              >
                <CollapsibleTrigger asChild>
                  <Button variant="outline" className="w-full justify-between">
                    <span className="flex items-center gap-2">
                      <BookOpen className="w-4 h-4" />
                      이론적 토대
                    </span>
                    <ChevronDown 
                      className={`w-4 h-4 transition-transform ${
                        openSections[`theory${stage.stage}`] ? 'rotate-180' : ''
                      }`} 
                    />
                  </Button>
                </CollapsibleTrigger>
                <CollapsibleContent className="mt-4">
                  <Card>
                    <CardHeader>
                      <CardTitle>{stage.theoreticalFoundation.title}</CardTitle>
                    </CardHeader>
                    <CardContent>
                      <div className="space-y-4">
                        {stage.theoreticalFoundation.theories.map((theory, idx) => (
                          <div key={idx} className="border-l-2 border-gray-200 pl-4">
                            <h5 className="mb-1">{theory.name}</h5>
                            <p className="text-sm text-muted-foreground">{theory.description}</p>
                          </div>
                        ))}
                      </div>
                    </CardContent>
                  </Card>
                </CollapsibleContent>
              </Collapsible>

              {/* 단계별 연계성 (1, 4, 8단계에만 표시) */}
              {[1, 4, 8].includes(stage.stage) && (
                <Card className="bg-gradient-to-r from-blue-50 to-purple-50">
                  <CardHeader>
                    <CardTitle className="flex items-center gap-2">
                      <Brain className="w-5 h-5 text-indigo-500" />
                      단계별 연계성
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    {stage.stage === 1 && (
                      <p className="text-sm">
                        <strong>1-2단계 (INPUT)</strong>: 지각인지와 요약이해는 정보를 수집하고 정리하는 기초 단계입니다. 
                        이 단계에서 형성된 관찰력과 핵심 파악 능력은 이후 모든 사고 과정의 토대가 됩니다.
                      </p>
                    )}
                    {stage.stage === 4 && (
                      <p className="text-sm">
                        <strong>3-4단계 (PROCESS)</strong>: 구조적 이해와 비판적 사고는 정보를 분석하고 평가하는 중간 단계입니다. 
                        패턴을 파악하고 논리적으로 검증하는 능력을 통해 깊이 있는 사고가 가능해집니다.
                      </p>
                    )}
                    {stage.stage === 8 && (
                      <div className="space-y-2">
                        <p className="text-sm">
                          <strong>5-6단계 (CREATE)</strong>: 의미 파악과 창조적 통합은 새로운 가치를 창출하는 고차원 단계입니다.
                        </p>
                        <p className="text-sm">
                          <strong>7-8단계 (OUTPUT & FEEDBACK)</strong>: 실행과 메타인지는 생각을 현실화하고 지속적으로 개선하는 완성 단계입니다.
                        </p>
                      </div>
                    )}
                  </CardContent>
                </Card>
              )}
            </div>
          </TabsContent>
        ))}
      </Tabs>
    </div>
  );
}
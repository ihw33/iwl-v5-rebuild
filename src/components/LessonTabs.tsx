import { Tabs, TabsContent, TabsList, TabsTrigger } from "./ui/tabs";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
import { Collapsible, CollapsibleContent, CollapsibleTrigger } from "./ui/collapsible";
import { Button } from "./ui/button";
import { ChevronDown, Eye, PenTool, Bot, Clock, Target, BookOpen } from "lucide-react";
import { THINKING_STAGE_COLORS } from "../lib/constants";
import { useState } from "react";

export function LessonTabs() {
  const [openSections, setOpenSections] = useState<{ [key: string]: boolean }>({});

  const toggleSection = (section: string) => {
    setOpenSections(prev => ({ ...prev, [section]: !prev[section] }));
  };

  return (
    <div className="mb-12">
      <div className="text-center mb-8">
        <h2 className="text-2xl mb-2">실습 교안</h2>
        <p className="text-muted-foreground">단계별 구체적인 수업 계획과 실습 활동</p>
      </div>

      <Tabs defaultValue="stage1" className="w-full">
        <TabsList className="grid w-full grid-cols-3">
          <TabsTrigger value="stage1">1단계: 지각인지</TabsTrigger>
          <TabsTrigger value="stage3">3단계: 구조적이해</TabsTrigger>
          <TabsTrigger value="ai-strategy">AI 협력 전략</TabsTrigger>
        </TabsList>

        {/* 1단계 탭 내용 */}
        <TabsContent value="stage1" className="mt-6">
          <div className="space-y-6">
            {/* 학습 목표 박스 */}
            <Card style={{ borderLeft: `4px solid ${THINKING_STAGE_COLORS[1]}` }}>
              <CardHeader className="pb-3">
                <CardTitle className="flex items-center gap-2">
                  <Target className="w-5 h-5" style={{ color: THINKING_STAGE_COLORS[1] }} />
                  학습 목표
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ul className="space-y-2">
                  <li>• 감각적 인지 능력 향상</li>
                  <li>• 순간 집중력 훈련</li>
                  <li>• 관찰력과 인식력 강화</li>
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
                    <h4 className="mb-2">도입 (5분)</h4>
                    <p className="text-sm text-muted-foreground">
                      지각인지란 무엇인가?<br/>
                      일상의 인지 패턴 점검
                    </p>
                  </div>
                  <div className="text-center p-4 bg-green-50 rounded-lg">
                    <h4 className="mb-2">본 수업 (25분)</h4>
                    <p className="text-sm text-muted-foreground">
                      감각 기반 실습<br/>
                      관찰력 훈련 활동
                    </p>
                  </div>
                  <div className="text-center p-4 bg-purple-50 rounded-lg">
                    <h4 className="mb-2">마무리 (5분)</h4>
                    <p className="text-sm text-muted-foreground">
                      학습 내용 정리<br/>
                      다음 단계 예고
                    </p>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* 실습 예시 카드 */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <Card className="hover:shadow-lg transition-shadow">
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <Eye className="w-5 h-5 text-green-500" />
                    실습 1: 감각 기반 목록 만들기
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    <div>
                      <h5 className="mb-1">활동 내용:</h5>
                      <p className="text-sm text-muted-foreground">
                        주변 환경에서 보이는, 들리는, 느껴지는 것들을 5분간 목록화
                      </p>
                    </div>
                    <div>
                      <h5 className="mb-1">진행 방식:</h5>
                      <ul className="text-sm text-muted-foreground space-y-1">
                        <li>1. 1분간 조용히 집중</li>
                        <li>2. 시각, 청각, 촉각 순서로 인지</li>
                        <li>3. 목록 작성 및 공유</li>
                      </ul>
                    </div>
                  </div>
                </CardContent>
              </Card>

              <Card className="hover:shadow-lg transition-shadow">
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <PenTool className="w-5 h-5 text-orange-500" />
                    실습 2: 책상 위 물건 묘사 실습
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    <div>
                      <h5 className="mb-1">활동 내용:</h5>
                      <p className="text-sm text-muted-foreground">
                        책상 위 하나의 물건을 선택해 최대한 세밀하게 묘사하기
                      </p>
                    </div>
                    <div>
                      <h5 className="mb-1">평가 기준:</h5>
                      <ul className="text-sm text-muted-foreground space-y-1">
                        <li>• 세부 관찰 정도</li>
                        <li>• 다감각적 표현</li>
                        <li>• 객관적 묘사 능력</li>
                      </ul>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>

            {/* 이론적 토대 (접을 수 있는 섹션) */}
            <Collapsible open={openSections['theory1']} onOpenChange={() => toggleSection('theory1')}>
              <CollapsibleTrigger asChild>
                <Button variant="outline" className="w-full justify-between">
                  <span className="flex items-center gap-2">
                    <BookOpen className="w-4 h-4" />
                    이론적 토대
                  </span>
                  <ChevronDown className={`w-4 h-4 transition-transform ${openSections['theory1'] ? 'rotate-180' : ''}`} />
                </Button>
              </CollapsibleTrigger>
              <CollapsibleContent className="mt-4">
                <Card>
                  <CardContent className="p-6">
                    <h4 className="mb-3">지각인지 단계의 이론적 배경</h4>
                    <div className="space-y-3 text-sm text-muted-foreground">
                      <p>
                        지각인지는 외부 자극을 감각 기관을 통해 받아들이는 가장 기초적인 사고 단계입니다.
                        이 단계에서는 판단이나 해석 없이 순수한 감각적 수용이 이루어집니다.
                      </p>
                      <p>
                        인지과학 연구에 따르면, 의식적 주의집중을 통해 지각의 정확도와 범위를 
                        현저히 향상시킬 수 있습니다.
                      </p>
                      <p>
                        이 단계의 훈련은 이후 모든 고차원적 사고의 토대가 되는 '정확한 정보 입력'을 
                        보장하는 핵심적 역할을 합니다.
                      </p>
                    </div>
                  </CardContent>
                </Card>
              </CollapsibleContent>
            </Collapsible>
          </div>
        </TabsContent>

        {/* 3단계 탭 내용 */}
        <TabsContent value="stage3" className="mt-6">
          <div className="space-y-6">
            {/* 학습 목표 박스 */}
            <Card style={{ borderLeft: `4px solid ${THINKING_STAGE_COLORS[3]}` }}>
              <CardHeader className="pb-3">
                <CardTitle className="flex items-center gap-2">
                  <Target className="w-5 h-5" style={{ color: THINKING_STAGE_COLORS[3] }} />
                  학습 목표
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ul className="space-y-2">
                  <li>• 정보의 구조적 패턴 인식</li>
                  <li>• 논리적 관계 파악 능력 향상</li>
                  <li>• 체계적 분석 사고 개발</li>
                </ul>
              </CardContent>
            </Card>

            {/* 구조화 3단계 절차 */}
            <Card>
              <CardHeader>
                <CardTitle>구조화 3단계 절차</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  <div className="text-center p-4 bg-blue-50 rounded-lg">
                    <div className="w-12 h-12 rounded-full bg-blue-500 text-white flex items-center justify-center mx-auto mb-3">1</div>
                    <h4 className="mb-2">분해</h4>
                    <p className="text-sm text-muted-foreground">
                      복잡한 정보를<br/>구성 요소로 나누기
                    </p>
                  </div>
                  <div className="text-center p-4 bg-green-50 rounded-lg">
                    <div className="w-12 h-12 rounded-full bg-green-500 text-white flex items-center justify-center mx-auto mb-3">2</div>
                    <h4 className="mb-2">관계파악</h4>
                    <p className="text-sm text-muted-foreground">
                      요소 간의 연결고리와<br/>상호작용 분석
                    </p>
                  </div>
                  <div className="text-center p-4 bg-purple-50 rounded-lg">
                    <div className="w-12 h-12 rounded-full bg-purple-500 text-white flex items-center justify-center mx-auto mb-3">3</div>
                    <h4 className="mb-2">재구성</h4>
                    <p className="text-sm text-muted-foreground">
                      논리적 구조로<br/>체계화하여 정리
                    </p>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* 실습 활동 카드 */}
            <Card className="hover:shadow-lg transition-shadow">
              <CardHeader>
                <CardTitle>실습: 기사 내용 구조 분석</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  <p className="text-sm text-muted-foreground">
                    제공된 뉴스 기사를 읽고 다음 구조로 분석해보세요:
                  </p>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                      <h5 className="mb-2">핵심 구성 요소</h5>
                      <ul className="text-sm space-y-1">
                        <li>□ 사실 (What)</li>
                        <li>□ 원인 (Why)</li>
                        <li>□ 결과 (Result)</li>
                        <li>□ 영향 (Impact)</li>
                      </ul>
                    </div>
                    <div>
                      <h5 className="mb-2">논리적 흐름</h5>
                      <ul className="text-sm space-y-1">
                        <li>□ 시간적 순서</li>
                        <li>□ 인과관계</li>
                        <li>□ 우선순위</li>
                        <li>□ 상호작용</li>
                      </ul>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* AI 활용 예시 */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Bot className="w-5 h-5 text-purple-500" />
                  AI 활용 예시
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-3">
                  <div className="p-3 bg-gray-50 rounded">
                    <h5 className="text-sm mb-1">AI 프롬프트 예시:</h5>
                    <p className="text-sm font-mono bg-white p-2 rounded border">
                      "다음 텍스트를 주요 구성 요소로 분해하고, 각 요소 간의 논리적 관계를 
                      다이어그램 형태로 정리해주세요: [텍스트 입력]"
                    </p>
                  </div>
                  <div className="p-3 bg-blue-50 rounded">
                    <h5 className="text-sm mb-1">기대 결과:</h5>
                    <p className="text-sm text-muted-foreground">
                      AI가 제안한 구조와 학습자의 분석을 비교하여 
                      구조적 사고의 정확성을 확인할 수 있습니다.
                    </p>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </TabsContent>

        {/* AI 협력 전략 탭 */}
        <TabsContent value="ai-strategy" className="mt-6">
          <Card>
            <CardHeader>
              <CardTitle>단계별 AI 협력 가이드</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-muted-foreground mb-6">
                각 사고 단계에서 AI를 효과적으로 활용하는 방법과 실제 프롬프트 예시입니다.
              </p>
              
              <div className="space-y-4">
                {[
                  { stage: "1단계", name: "지각인지", role: "자극 제시자", keywords: "연상, 감각 묘사, 관찰 유도" },
                  { stage: "2단계", name: "요약이해", role: "요약 비교자", keywords: "요점 정리, 핵심 추출" },
                  { stage: "3단계", name: "구조적이해", role: "구조 분석가", keywords: "분해, 관계 분석, 체계화" },
                  { stage: "4단계", name: "비판적사고", role: "논리 검증자", keywords: "논증 분석, 반박 제시" }
                ].map((item, index) => (
                  <div key={index} className="border rounded-lg p-4 hover:bg-muted/30 transition-colors">
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-3">
                        <span className="text-sm font-medium">{item.stage}</span>
                        <span className="text-muted-foreground">{item.name}</span>
                      </div>
                      <div className="text-right">
                        <div className="text-sm">{item.role}</div>
                        <div className="text-xs text-muted-foreground">{item.keywords}</div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  );
}
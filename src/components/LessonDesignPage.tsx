"use client";

import { useState } from "react";
import { LessonOverview } from "./LessonOverview";
import { TrainingProcess } from "./TrainingProcess";
import { PersonaCard } from "./PersonaCard";
import { LessonTabs } from "./LessonTabs";
import { MatrixVisualization } from "./MatrixVisualization";
import { ThinkingStagesVisualization } from "./ThinkingStagesVisualization";
import { CriteriaChartVisualization } from "./CriteriaChartVisualization";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "./ui/tabs";
import { ArrowRight, BarChart3, Gamepad2, MessageSquare, Users, Grid3x3, Layers, ChartBar, GraduationCap } from "lucide-react";
import { Home } from "lucide-react";
import { Button } from "./ui/button";
import Link from "next/link";

function ThinkingConnectionDiagram() {
  const connections = [
    { stages: "1-2단계", thinking: "지각·요약", process: "수집", color: "#FF6B6B" },
    { stages: "3-4단계", thinking: "구조화·비판", process: "분류", color: "#45B7D1" },
    { stages: "5-6단계", thinking: "의미·창조", process: "재구성", color: "#FFEAA7" },
    { stages: "7단계", thinking: "실행", process: "표현", color: "#98D8C8" },
    { stages: "8단계", thinking: "메타인지", process: "피드백", color: "#F7DC6F" }
  ];

  return (
    <div className="mb-12">
      <div className="text-center mb-8">
        <h2 className="text-2xl mb-2">사고-정리 연결 다이어그램</h2>
        <p className="text-muted-foreground">8단계 사고가 정리 프로세스로 연결되는 과정</p>
      </div>

      <div className="space-y-4">
        {connections.map((item, index) => (
          <div key={index} className="flex items-center gap-4">
            <div 
              className="flex-1 p-4 rounded-lg text-center"
              style={{ backgroundColor: item.color + "20" }}
            >
              <div className="flex items-center justify-center gap-2">
                <span className="text-sm">{item.stages}</span>
                <span>{item.thinking}</span>
              </div>
            </div>
            
            <ArrowRight className="w-6 h-6 text-muted-foreground flex-shrink-0" />
            
            <div 
              className="flex-1 p-4 rounded-lg text-center"
              style={{ backgroundColor: item.color + "10" }}
            >
              <span>{item.process}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function ExpansionModules() {
  const modules = [
    {
      title: "진행 시각화 대시보드",
      icon: BarChart3,
      description: "개인별 학습 진도와 성취도를 실시간으로 추적하고 시각화",
      features: ["8단계별 숙련도", "일별 학습 시간", "약점 분석"]
    },
    {
      title: "생각정리 퀘스트",
      icon: Gamepad2,
      description: "게임화된 미션을 통해 재미있게 사고력을 훈련",
      features: ["레벨 시스템", "업적 뱃지", "친구와 경쟁"]
    },
    {
      title: "AI 피드백 봇",
      icon: MessageSquare,
      description: "24시간 언제든지 개인 맞춤형 피드백과 조언 제공",
      features: ["즉시 피드백", "약점 보완", "학습 추천"]
    },
    {
      title: "커뮤니티 연계",
      icon: Users,
      description: "동료 학습자들과 경험을 공유하고 함께 성장",
      features: ["스터디 그룹", "경험 공유", "멘토링"]
    }
  ];

  return (
    <div className="mb-12">
      <div className="text-center mb-8">
        <h2 className="text-2xl mb-2">확장 모듈</h2>
        <p className="text-muted-foreground">학습 효과를 극대화하는 추가 기능들</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {modules.map((module, index) => (
          <Card key={index} className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <module.icon className="w-5 h-5 text-blue-500" />
                {module.title}
              </CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-muted-foreground mb-4">{module.description}</p>
              <div className="space-y-1">
                {module.features.map((feature, featureIndex) => (
                  <div key={featureIndex} className="flex items-center gap-2">
                    <div className="w-2 h-2 rounded-full bg-blue-500"></div>
                    <span className="text-sm">{feature}</span>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}

function AIStrategyTable() {
  const aiStrategies = [
    { stage: "1단계", name: "지각인지", role: "자극 제시자", keywords: "연상, 감각 묘사, 관찰 유도" },
    { stage: "2단계", name: "요약이해", role: "요약 비교자", keywords: "요점 정리, 핵심 추출, 구조화" },
    { stage: "3단계", name: "구조적이해", role: "구조 분석가", keywords: "분해, 관계 분석, 체계화" },
    { stage: "4단계", name: "비판적사고", role: "논리 검증자", keywords: "논증 분석, 반박 제시, 오류 지적" },
    { stage: "5단계", name: "의미파악", role: "맥락 해석자", keywords: "함의 분석, 숨은 의미, 상징 해석" },
    { stage: "6단계", name: "창조적통합", role: "아이디어 촉진자", keywords: "연결, 통합, 새로운 관점" },
    { stage: "7단계", name: "실행", role: "실행 코치", keywords: "계획 수립, 실행 전략, 행동 계획" },
    { stage: "8단계", name: "메타인지", role: "사고 분석가", keywords: "사고 점검, 성찰, 개선 제안" }
  ];

  return (
    <div className="mb-12">
      <div className="text-center mb-8">
        <h2 className="text-2xl mb-2">AI 협력 전략 테이블</h2>
        <p className="text-muted-foreground">각 사고 단계별 AI의 역할과 활용 키워드</p>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full border-collapse bg-white rounded-lg shadow-lg">
          <thead>
            <tr className="bg-muted">
              <th className="p-4 border border-border text-left">사고 단계</th>
              <th className="p-4 border border-border text-left">AI 역할</th>
              <th className="p-4 border border-border text-left">프롬프트 키워드</th>
            </tr>
          </thead>
          <tbody>
            {aiStrategies.map((item, index) => (
              <tr key={index} className="hover:bg-muted/50 transition-colors">
                <td className="p-4 border border-border">
                  <div>
                    <span className="text-sm text-muted-foreground">{item.stage}</span>
                    <div>{item.name}</div>
                  </div>
                </td>
                <td className="p-4 border border-border">{item.role}</td>
                <td className="p-4 border border-border">
                  <span className="text-sm text-muted-foreground">{item.keywords}</span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export function LessonDesignPage() {
  const [activeTab, setActiveTab] = useState("theory");

  return (
    <div className="w-full max-w-7xl mx-auto p-6">
      {/* 헤더 섹션 */}
      <div className="text-center mb-8">
        <h1 className="text-4xl mb-2">IWL 이론체계 & 훈련 프로그램</h1>
        <p className="text-xl text-muted-foreground mb-4">8단계 사고 확장 기반 체계적 교육 설계</p>
        <Link href="/">
          <Button variant="outline" className="mb-6">
            <Home className="w-4 h-4 mr-2" />
            홈으로 돌아가기
          </Button>
        </Link>
      </div>

      {/* 메인 탭 네비게이션 */}
      <Tabs value={activeTab} onValueChange={setActiveTab} className="w-full">
        <TabsList className="grid w-full grid-cols-2 mb-8">
          <TabsTrigger value="theory" className="flex items-center gap-2">
            <Layers className="w-4 h-4" />
            🎨 핵심 이론체계
          </TabsTrigger>
          <TabsTrigger value="lesson" className="flex items-center gap-2">
            <GraduationCap className="w-4 h-4" />
            📋 수업 설계
          </TabsTrigger>
        </TabsList>

        {/* 핵심 이론체계 탭 */}
        <TabsContent value="theory" className="space-y-6">
          <Tabs defaultValue="matrix" className="w-full">
            <TabsList className="grid w-full grid-cols-3 mb-6">
              <TabsTrigger value="matrix">8×4 매트릭스</TabsTrigger>
              <TabsTrigger value="stages">8단계 사고 모델</TabsTrigger>
              <TabsTrigger value="criteria">4가지 구분 기준</TabsTrigger>
            </TabsList>
            
            <TabsContent value="matrix" className="space-y-6">
              <MatrixVisualization />
            </TabsContent>
            
            <TabsContent value="stages" className="space-y-6">
              <ThinkingStagesVisualization />
            </TabsContent>
            
            <TabsContent value="criteria" className="space-y-6">
              <CriteriaChartVisualization />
            </TabsContent>
          </Tabs>
        </TabsContent>

        {/* 수업 설계 탭 */}
        <TabsContent value="lesson" className="space-y-6">
          <Tabs defaultValue="overview" className="w-full">
            <TabsList className="grid w-full grid-cols-4 mb-6">
              <TabsTrigger value="overview">프로그램 개요</TabsTrigger>
              <TabsTrigger value="practice">실습 교안</TabsTrigger>
              <TabsTrigger value="ai">AI 협력 전략</TabsTrigger>
              <TabsTrigger value="expansion">확장 모듈</TabsTrigger>
            </TabsList>
            
            {/* 프로그램 개요 탭 */}
            <TabsContent value="overview" className="space-y-6">
              <LessonOverview />
              <TrainingProcess />
              <PersonaCard />
            </TabsContent>
            
            {/* 실습 교안 탭 */}
            <TabsContent value="practice" className="space-y-6">
              <LessonTabs />
            </TabsContent>
            
            {/* AI 협력 전략 탭 */}
            <TabsContent value="ai" className="space-y-6">
              <AIStrategyTable />
              <ThinkingConnectionDiagram />
            </TabsContent>
            
            {/* 확장 모듈 탭 */}
            <TabsContent value="expansion" className="space-y-6">
              <ExpansionModules />
            </TabsContent>
          </Tabs>
        </TabsContent>
      </Tabs>
    </div>
  );
}
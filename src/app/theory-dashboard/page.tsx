import Link from "next/link";
import { MatrixVisualization } from "@/components/MatrixVisualization";
import { ThinkingStagesVisualization } from "@/components/ThinkingStagesVisualization";
import { CriteriaChartVisualization } from "@/components/CriteriaChartVisualization";

export default function TheoryDashboard() {
  return (
    <div className="container mx-auto p-8">
      <div className="mb-6">
        <Link href="/" className="text-blue-600 hover:text-blue-800">
          ← 홈으로 돌아가기
        </Link>
      </div>
      
      <header className="text-center mb-12">
        <h1 className="text-3xl font-bold mb-4">핵심 이론체계</h1>
        <p className="text-xl text-gray-600">
          8x4 매트릭스 기반 사고 확장 시스템
        </p>
      </header>
      
      <div className="space-y-16">
        <MatrixVisualization />
        <ThinkingStagesVisualization />
        <CriteriaChartVisualization />
      </div>
    </div>
  );
}
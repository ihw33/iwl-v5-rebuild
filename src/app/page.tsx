import Link from "next/link";

export default function Home() {
  return (
    <div className="container mx-auto p-8 max-w-4xl">
      <header className="text-center mb-12">
        <h1 className="text-4xl font-bold mb-4">
          IWL v5.0 - 생각정리 기술 3.0
        </h1>
        <p className="text-xl text-gray-600">
          8x4 매트릭스 기반 사고 훈련 시스템
        </p>
      </header>

      <section className="space-y-6">
        <h2 className="text-2xl font-semibold mb-6">📋 당장 할 작업:</h2>
        
        <div className="space-y-4">
          <Link 
            href="/theory-dashboard" 
            className="block p-6 bg-blue-50 border border-blue-200 rounded-lg hover:bg-blue-100 transition-colors"
          >
            <h3 className="text-xl font-semibold text-blue-900 mb-2">
              📊 피그마 작업한 페이지 (이론 대시보드)
            </h3>
            <p className="text-blue-700">
              8x4 매트릭스 + 8단계 사고 모델 + 4가지 구분 기준
            </p>
          </Link>

          <Link 
            href="/lesson-design" 
            className="block p-6 bg-green-50 border border-green-200 rounded-lg hover:bg-green-100 transition-colors"
          >
            <h3 className="text-xl font-semibold text-green-900 mb-2">
              📚 수업 설계 & 훈련 프로그램
            </h3>
            <p className="text-green-700">
              5단계 프로세스 + 실습 교안 + AI 협력 전략
            </p>
          </Link>
        </div>
      </section>
    </div>
  );
}

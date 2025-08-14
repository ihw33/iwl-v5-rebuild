import Link from "next/link";

export default function Home() {
  return (
    <div className="container mx-auto p-8 max-w-4xl">
      <header className="text-center mb-12">
        <h1 className="text-4xl font-bold mb-4 bg-gradient-to-r from-indigo-600 via-fuchsia-600 to-pink-600 bg-clip-text text-transparent">
          IWL v5.0 - 생각정리 기술 3.0
        </h1>
        <p className="text-xl text-gray-600 dark:text-gray-300">
          8x4 매트릭스 기반 사고 훈련 시스템
        </p>
      </header>

      <section className="space-y-6">
        <h2 className="text-2xl font-semibold mb-6">📋 완성된 페이지:</h2>
        
        <div className="space-y-4">
          <Link 
            href="/lesson-design" 
            className="block p-6 rounded-xl transition-all border bg-white/70 dark:bg-zinc-900/60 backdrop-blur shadow-[0_8px_30px_rgb(0,0,0,0.06)] hover:shadow-[0_12px_40px_rgb(0,0,0,0.12)] border-zinc-200/70 dark:border-white/10"
          >
            <h3 className="text-xl font-semibold mb-2">
              📚 IWL 이론체계 & 훈련 프로그램
            </h3>
            <p className="text-zinc-700 dark:text-zinc-300">
              핵심 이론 + 수업 설계 + 실습 교안 + AI 협력 전략
            </p>
          </Link>
        </div>
      </section>
    </div>
  );
}

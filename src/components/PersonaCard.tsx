import { Card, CardContent } from "./ui/card";
import { User, MapPin, Target, Calendar, Briefcase } from "lucide-react";

export function PersonaCard() {
  return (
    <div className="mb-12">
      <div className="text-center mb-8">
        <h2 className="text-2xl mb-2">대표 학습자 페르소나</h2>
        <p className="text-muted-foreground">주요 대상 학습자의 특성과 학습 환경</p>
      </div>

      <Card className="max-w-4xl mx-auto hover:shadow-lg transition-shadow">
        <CardContent className="p-8">
          <div className="flex flex-col md:flex-row gap-8">
            {/* 프로필 이미지 영역 */}
            <div className="flex-shrink-0 text-center">
              <div className="w-32 h-32 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center mx-auto mb-4">
                <User className="w-16 h-16 text-white" />
              </div>
              <h3 className="text-xl mb-1">김도현</h3>
              <p className="text-muted-foreground">34세, IT기업 마케팅 대리</p>
            </div>

            {/* 상세 정보 */}
            <div className="flex-1 grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <div className="flex items-center gap-2 mb-3">
                  <Briefcase className="w-5 h-5 text-blue-500" />
                  <h4 className="text-lg">특징</h4>
                </div>
                <ul className="space-y-2 text-sm">
                  <li className="flex items-start gap-2">
                    <div className="w-2 h-2 rounded-full bg-blue-500 mt-2 flex-shrink-0"></div>
                    <span>꼼꼼하지만 완벽주의 성향</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <div className="w-2 h-2 rounded-full bg-blue-500 mt-2 flex-shrink-0"></div>
                    <span>분석적 사고 치중, 직관적 사고 부족</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <div className="w-2 h-2 rounded-full bg-blue-500 mt-2 flex-shrink-0"></div>
                    <span>체계적 정리는 잘하나 창의적 발상 약함</span>
                  </li>
                </ul>
              </div>

              <div>
                <div className="flex items-center gap-2 mb-3">
                  <Target className="w-5 h-5 text-green-500" />
                  <h4 className="text-lg">학습 목표</h4>
                </div>
                <ul className="space-y-2 text-sm">
                  <li className="flex items-start gap-2">
                    <div className="w-2 h-2 rounded-full bg-green-500 mt-2 flex-shrink-0"></div>
                    <span>순간 집중력과 관찰력 향상</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <div className="w-2 h-2 rounded-full bg-green-500 mt-2 flex-shrink-0"></div>
                    <span>창조적 통합 사고 개발</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <div className="w-2 h-2 rounded-full bg-green-500 mt-2 flex-shrink-0"></div>
                    <span>메타인지 능력 강화</span>
                  </li>
                </ul>
              </div>

              <div>
                <div className="flex items-center gap-2 mb-3">
                  <Calendar className="w-5 h-5 text-purple-500" />
                  <h4 className="text-lg">학습 환경</h4>
                </div>
                <ul className="space-y-2 text-sm">
                  <li className="flex items-start gap-2">
                    <div className="w-2 h-2 rounded-full bg-purple-500 mt-2 flex-shrink-0"></div>
                    <span>평일 저녁 7-9시 (2시간)</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <div className="w-2 h-2 rounded-full bg-purple-500 mt-2 flex-shrink-0"></div>
                    <span>주말 오전 9-12시 (3시간)</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <div className="w-2 h-2 rounded-full bg-purple-500 mt-2 flex-shrink-0"></div>
                    <span>디지털 기기 활용 선호</span>
                  </li>
                </ul>
              </div>

              <div>
                <div className="flex items-center gap-2 mb-3">
                  <MapPin className="w-5 h-5 text-orange-500" />
                  <h4 className="text-lg">현재 상황</h4>
                </div>
                <ul className="space-y-2 text-sm">
                  <li className="flex items-start gap-2">
                    <div className="w-2 h-2 rounded-full bg-orange-500 mt-2 flex-shrink-0"></div>
                    <span>마케팅 전략 수립 업무</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <div className="w-2 h-2 rounded-full bg-orange-500 mt-2 flex-shrink-0"></div>
                    <span>팀 프로젝트 리더 역할</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <div className="w-2 h-2 rounded-full bg-orange-500 mt-2 flex-shrink-0"></div>
                    <span>승진 준비 중</span>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
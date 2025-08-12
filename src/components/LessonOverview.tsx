import { Card, CardContent } from "./ui/card";
import { Users, Monitor, Target, Sparkles } from "lucide-react";

export function LessonOverview() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
      <Card className="hover:shadow-lg transition-shadow">
        <CardContent className="p-6">
          <div className="flex items-center gap-3 mb-4">
            <Users className="w-6 h-6 text-blue-500" />
            <h3 className="text-lg">대상</h3>
          </div>
          <p className="text-muted-foreground mb-2">30대 직장인, 크리에이터, 기획자 등</p>
          <ul className="text-sm space-y-1">
            <li>• 체계적 사고력 향상이 필요한 직장인</li>
            <li>• 창작 및 기획 업무 담당자</li>
            <li>• 논리적 정리 능력 개발 희망자</li>
          </ul>
        </CardContent>
      </Card>

      <Card className="hover:shadow-lg transition-shadow">
        <CardContent className="p-6">
          <div className="flex items-center gap-3 mb-4">
            <Monitor className="w-6 h-6 text-purple-500" />
            <h3 className="text-lg">방식</h3>
          </div>
          <p className="text-muted-foreground mb-2">디지털 훈련 시스템 / 오프라인 워크숍</p>
          <ul className="text-sm space-y-1">
            <li>• 개인별 맞춤형 학습 경로</li>
            <li>• 실시간 AI 피드백</li>
            <li>• 소그룹 협력 학습</li>
          </ul>
        </CardContent>
      </Card>

      <Card className="hover:shadow-lg transition-shadow">
        <CardContent className="p-6">
          <div className="flex items-center gap-3 mb-4">
            <Target className="w-6 h-6 text-green-500" />
            <h3 className="text-lg">목표</h3>
          </div>
          <p className="text-muted-foreground mb-2">사고력과 정리 능력 향상</p>
          <ul className="text-sm space-y-1">
            <li>• 8단계 사고 체계 습득</li>
            <li>• 정보 정리 및 구조화 능력</li>
            <li>• 창조적 문제 해결력 개발</li>
          </ul>
        </CardContent>
      </Card>

      <Card className="hover:shadow-lg transition-shadow">
        <CardContent className="p-6">
          <div className="flex items-center gap-3 mb-4">
            <Sparkles className="w-6 h-6 text-orange-500" />
            <h3 className="text-lg">특징</h3>
          </div>
          <p className="text-muted-foreground mb-2">AI 협력 학습 시스템</p>
          <ul className="text-sm space-y-1">
            <li>• 개인 맞춤 학습 분석</li>
            <li>• 실시간 사고 패턴 피드백</li>
            <li>• 단계별 성취도 시각화</li>
          </ul>
        </CardContent>
      </Card>
    </div>
  );
}
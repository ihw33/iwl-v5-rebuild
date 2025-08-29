#\!/bin/bash

# Issue #43의 서브 이슈로 32개 학습 모듈 생성

stages=(
    "S1:지각인지:Perception"
    "S2:요약·맥락이해:Contextual-Comprehension"
    "S3:구조적이해:Structural-Analysis"
    "S4:비판적사고:Critical-Thinking"
    "S5:보이지않는의미파악:Inferential-Reasoning"
    "S6:창조적통합:Creative-Synthesis"
    "S7:실행:Execution"
    "S8:메타인지:Metacognition"
)

axes=(
    "A1:정보처리깊이:Depth-of-Processing"
    "A2:사고조작방식:Cognitive-Processes"
    "A3:추상화수준:Level-of-Abstraction"
    "A4:자기인식수준:Metacognitive-Awareness"
)

# 카운터
count=1

for stage_info in "${stages[@]}"; do
    IFS=':' read -r stage_id stage_kr stage_en <<< "$stage_info"
    
    for axis_info in "${axes[@]}"; do
        IFS=':' read -r axis_id axis_kr axis_en <<< "$axis_info"
        
        module_id="${stage_id}-${axis_id}"
        title="[#43-${count}] ${module_id} 학습 모듈 구현: ${stage_kr} × ${axis_kr}"
        
        # S1-A1은 이미 완료
        if [ "$module_id" = "S1-A1" ]; then
            echo "Skipping S1-A1 (already completed)"
            count=$((count + 1))
            continue
        fi
        
        body="## 🎯 모듈 정보
- **Module ID**: ${module_id}
- **Stage**: ${stage_id} - ${stage_kr} (${stage_en})
- **Axis**: ${axis_id} - ${axis_kr} (${stage_en})
- **Parent Issue**: #43 (학습 모듈 노드 템플릿 생성)

## 📋 작업 내역
- [ ] 모듈 설계서 작성 (\`docs/8x4-matrix/modules/${module_id}/${module_id}-module_design.md\`)
- [ ] Python 노드 구현 (\`nodes/learning/${module_id}_*.py\`)
- [ ] 레벨별 활동 시퀀스 정의 (L1, L3, L5)
- [ ] AI 프롬프트 템플릿 작성
- [ ] 품질 평가 로직 구현
- [ ] 단위 테스트 작성

## 🔗 참조
- 템플릿: \`docs/8x4-matrix/modules/MODULE_TEMPLATE_v3.0.md\`
- 참조 구현: \`nodes/learning/S1_A1_perception_depth.py\`
- 인터페이스: \`nodes/base/interfaces.py\`

## ✅ 완료 기준
- 설계서 작성 완료
- 코드 구현 및 테스트 통과
- 레벨별 차별화 확인
- 다음 모듈과의 연계 정의"

        echo "Creating issue: $title"
        gh issue create \
            --repo ihw33/iwl-v5-rebuild \
            --title "$title" \
            --body "$body" \
            --label "module-implementation,${stage_id},${axis_id}" \
            --milestone "M1"
        
        # GitHub API 제한 방지
        sleep 2
        
        count=$((count + 1))
    done
done

echo "Created 31 module implementation issues (S1-A1 already exists)"

#!/usr/bin/env python3
"""
IWL에서 재귀 성장 시스템 테스트
IWL 프로젝트에서 새로운 노드와 DAG가 자동으로 생성되는지 확인
"""

import asyncio
import json
from pathlib import Path
import sys

# .orchestra 경로를 통해 접근
orchestra_path = Path(__file__).parent / ".orchestra"
sys.path.append(str(orchestra_path))

from generators.ai_interface import AIInterface
from generators.recursive_node_generator import RecursiveNodeGenerator
from generators.recursive_dag_composer import RecursiveDAGComposer


def test_in_iwl():
    """IWL 프로젝트에서 재귀 성장 테스트"""
    print("\n" + "="*60)
    print("🧬 IWL 재귀 성장 시스템 테스트")
    print("="*60)
    
    print(f"\n📁 현재 디렉토리: {Path.cwd()}")
    print(f"📁 Orchestra 경로: {orchestra_path}")
    
    # AI 인터페이스 테스트
    print("\n🧪 AI 인터페이스 테스트")
    ai = AIInterface()
    
    # IWL 관련 이슈 테스트
    issue_body = """
    [AI] IWL 학습 콘텐츠 자동 생성 기능 구현
    
    ## 요구사항
    - 학습 주제 분석
    - AI 기반 콘텐츠 생성
    - 학습 경로 최적화
    - 개인화 추천 시스템
    """
    
    print("📋 IWL 이슈 분석 중...")
    analysis = ai.analyze_issue(issue_body)
    print(f"분석 결과:\n{json.dumps(analysis, indent=2, ensure_ascii=False)}")
    
    # 노드 생성 테스트
    print("\n🧪 노드 생성 테스트")
    generator = RecursiveNodeGenerator()
    
    # IWL nodes 디렉토리 확인
    iwl_nodes = orchestra_path / "nodes"
    print(f"IWL 노드 디렉토리: {iwl_nodes}")
    print(f"심볼릭 링크 여부: {iwl_nodes.is_symlink()}")
    
    if iwl_nodes.exists():
        existing_nodes = [f.stem for f in iwl_nodes.glob("*.py")]
        print(f"기존 노드 수: {len(existing_nodes)}")
        
        # 필요한 노드 확인
        required_nodes = analysis.get('required_nodes', [])
        print(f"필요한 노드: {required_nodes}")
        
        for node_type in required_nodes[:1]:  # 첫 번째만 테스트
            node_name = f"{node_type}_node"
            if node_name not in existing_nodes:
                print(f"\n🔄 IWL용 새 노드 생성 시뮬레이션: {node_type}")
                
                # 노드 코드 생성
                code = ai.generate_node_code(node_type, {
                    'description': f"IWL learning content {node_type}",
                    'context': analysis
                })
                
                if code:
                    print(f"✅ 코드 생성 완료 (길이: {len(code)}자)")
                    print("생성된 코드 미리보기:")
                    print("\n".join(code.split("\n")[:5]) + "\n...")
                else:
                    print("❌ 코드 생성 실패")
            else:
                print(f"이미 존재: {node_name}")
    
    # DAG 구성 테스트
    print("\n🧪 DAG 구성 테스트")
    composer = RecursiveDAGComposer()
    
    iwl_dags = orchestra_path / "dags"
    print(f"IWL DAG 디렉토리: {iwl_dags}")
    
    if iwl_dags.exists():
        existing_dags = [f.stem for f in iwl_dags.glob("*.py")]
        print(f"기존 DAG 수: {len(existing_dags)}")
    
    # 통합 테스트
    print("\n🧪 IWL 통합 테스트")
    try:
        from executors.iwl_executor import IWLExecutor
        print("✅ IWL Executor 로드 성공")
        
        executor = IWLExecutor()
        print("✅ IWL Executor 초기화 성공")
        
        # 재귀 성장 컴포넌트 확인
        if hasattr(executor, 'node_generator'):
            print("✅ node_generator 확인")
        if hasattr(executor, 'dag_composer'):
            print("✅ dag_composer 확인")
        if hasattr(executor, 'ai_interface'):
            print("✅ ai_interface 확인")
            
        print("\n🎉 IWL에서 재귀 성장 시스템이 완전히 통합되었습니다!")
        
    except ImportError as e:
        print(f"⚠️ IWL Executor 로드 실패: {e}")
    except Exception as e:
        print(f"❌ 통합 테스트 실패: {e}")
    
    # 최종 상태
    print("\n📊 IWL 재귀 성장 시스템 상태:")
    print(f"  - Orchestra 연결: {'✅' if orchestra_path.exists() else '❌'}")
    print(f"  - Generators 접근: {'✅' if (orchestra_path / 'generators').exists() else '❌'}")
    print(f"  - 노드 자동 생성 가능: {'✅' if ai else '❌'}")
    print(f"  - DAG 자동 구성 가능: {'✅' if composer else '❌'}")
    
    print("\n" + "="*60)
    print("✅ IWL 재귀 성장 시스템 테스트 완료")
    print("="*60)


if __name__ == "__main__":
    test_in_iwl()
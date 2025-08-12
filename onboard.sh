#!/bin/bash

# IWL v5.0 AI 팀원 자동 온보딩 스크립트

echo "🚀 IWL v5.0 AI 온보딩 시작"
echo "=================================="
echo ""

# 프로젝트 디렉토리로 이동
cd /Users/m4_macbook/iwl-v5-rebuild

# 범용 프롬프트 표시
echo "📌 당신의 정체성:"
cat .ai-prompts/UNIVERSAL_PROMPT.txt
echo ""
echo "=================================="
echo ""

# 핵심 문서 표시
echo "📚 필독 문서:"
echo "1. AI_TEAM_ONBOARDING.md - 전체 가이드"
echo "2. AI_TEAM_ROLES.md - 역할 정의"
echo "3. AI_QUICK_START.md - 빠른 시작"
echo ""

# 현재 상태 확인
echo "📊 프로젝트 상태:"
git status --short
echo ""

# 개발 서버 정보
echo "🔧 개발 서버:"
echo "npm run dev → http://localhost:3001"
echo ""

# GitHub Issues
echo "📋 현재 이슈:"
gh issue list --limit 5 2>/dev/null || echo "GitHub CLI 설치 필요"
echo ""

echo "=================================="
echo "✅ 온보딩 완료! 작업을 시작하세요."
echo "=================================="
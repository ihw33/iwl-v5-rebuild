#!/bin/bash

# GitHub Repository ID 가져오기
REPO_ID=$(gh api repos/ihw33/iwl-v5-rebuild --jq '.node_id')

# Announcements 카테고리 ID
CATEGORY_ID="DIC_kwDOPcUORc4CuJf1"

# Discussion 내용
TITLE="🎉 GitHub Discussions 오픈!"
BODY=$(cat <<'EOF'
# 🎉 GitHub Discussions 오픈!

안녕하세요, IWL v5.0 팀 여러분!

GitHub Discussions가 공식적으로 활성화되었습니다. 이제 우리 프로젝트의 커뮤니케이션이 더욱 체계적으로 이루어집니다.

## 📋 새로운 구조 안내

### Issue vs Discussions 구분
- **Issues**: 구체적 작업, 버그 추적
- **Discussions**: 아이디어, 토론, Q&A

## 💬 Discussions 카테고리

- 📢 **Announcements**: PM 공지사항
- 💡 **Ideas**: 아이디어 제안
- 🎯 **General**: 일반 토론
- ❓ **Q&A**: 질문과 답변

## 🚀 시작하기

[Discussions 탭](https://github.com/ihw33/iwl-v5-rebuild/discussions)에서 새 토론을 시작하세요!

함께 만들어가는 IWL v5.0! 🚀
EOF
)

# GraphQL mutation
gh api graphql -f query="
mutation {
  createDiscussion(input: {
    repositoryId: \"$REPO_ID\"
    categoryId: \"$CATEGORY_ID\"
    title: \"$TITLE\"
    body: \"$BODY\"
  }) {
    discussion {
      number
      url
    }
  }
}"
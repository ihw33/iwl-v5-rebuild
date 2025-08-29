# Figma Make 다운로드 임시 폴더

## 📥 사용법
1. Figma Make에서 ZIP 파일 다운로드
2. 이 폴더에 압축 해제
3. 파일들을 적절한 위치로 복사
4. 작업 완료 후 이 폴더 정리

## 🔄 예시
```bash
# 1. ZIP 파일 압축 해제
unzip figma-export.zip -d figma-downloads/

# 2. 파일 복사
cp -r figma-downloads/components/* src/components/figma/
cp -r figma-downloads/styles/* src/styles/figma/

# 3. 정리 (선택사항)
rm -rf figma-downloads/*
```

## ⚠️ 주의
- 이 폴더는 **.gitignore**에 포함됨 (임시 파일용)
- 정기적으로 정리해서 용량 관리
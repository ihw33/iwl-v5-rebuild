# 관리자 가이드 (Admin Guide)

> 📌 **최종 업데이트**: 2025-08-14  
> 👤 **담당자**: QA Claude  
> 📚 **카테고리**: Guides / Administration

## 📖 목차

1. [관리자 권한](#관리자-권한)
2. [시스템 관리](#시스템-관리)
3. [사용자 관리](#사용자-관리)
4. [콘텐츠 관리](#콘텐츠-관리)
5. [모니터링](#모니터링)
6. [백업과 복구](#백업과-복구)
7. [보안 설정](#보안-설정)
8. [문제 해결](#문제-해결)

---

## 🔐 관리자 권한

### 권한 레벨

| 레벨 | 역할 | 권한 |
|------|------|------|
| **Super Admin** | Thomas | 모든 권한 |
| **Admin** | PM Claude | 시스템 관리, 사용자 관리 |
| **Moderator** | 각 AI 팀원 | 콘텐츠 관리, 모니터링 |
| **User** | 일반 사용자 | 읽기, 기본 기능 |

### 권한 설정
```bash
# .env 파일에서 관리자 설정
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=secure_password_here
```

---

## 🔧 시스템 관리

### 서버 시작/종료

#### 개발 서버
```bash
# 시작
npm run dev

# 특정 포트로 시작
PORT=3001 npm run dev

# 종료
Ctrl + C
```

#### 프로덕션 서버
```bash
# 빌드
npm run build

# 시작
npm start

# PM2로 관리 (권장)
pm2 start npm --name "iwl-v5" -- start
pm2 stop iwl-v5
pm2 restart iwl-v5
```

### 환경 변수 관리

#### 필수 환경 변수
```env
# .env.local
NODE_ENV=production
DATABASE_URL=postgresql://...
NEXTAUTH_SECRET=your-secret-key
NEXTAUTH_URL=https://your-domain.com
```

#### 환경별 설정
- `.env.development` - 개발 환경
- `.env.production` - 프로덕션 환경
- `.env.local` - 로컬 오버라이드 (Git 제외)

### 로그 관리

#### 로그 위치
```bash
# 애플리케이션 로그
tail -f logs/app.log

# 에러 로그
tail -f logs/error.log

# 액세스 로그
tail -f logs/access.log
```

#### 로그 로테이션
```bash
# logrotate 설정
/var/log/iwl-v5/*.log {
    daily
    rotate 7
    compress
    delaycompress
    notifempty
    create 640 www-data adm
}
```

---

## 👥 사용자 관리

### 사용자 추가
```javascript
// API를 통한 사용자 추가
POST /api/admin/users
{
  "email": "user@example.com",
  "name": "User Name",
  "role": "user"
}
```

### 사용자 권한 변경
```javascript
// 권한 업데이트
PUT /api/admin/users/:id
{
  "role": "moderator"
}
```

### 사용자 비활성화
```javascript
// 계정 비활성화
DELETE /api/admin/users/:id
```

### 일괄 작업
```bash
# CSV로 사용자 내보내기
npm run export:users

# CSV에서 사용자 가져오기
npm run import:users users.csv
```

---

## 📚 콘텐츠 관리

### A/B 시리즈 관리

#### 콘텐츠 추가
1. `/content/lessons/` 디렉토리에 파일 추가
2. 메타데이터 설정
3. 데이터베이스 동기화

#### 콘텐츠 구조
```
content/
├── lessons/
│   ├── a-series/
│   │   ├── a0-spec-structure.md
│   │   └── ...
│   └── b-series/
│       ├── b0-template.md
│       └── ...
```

### Wiki 관리

#### Wiki 백업
```bash
# Wiki 저장소 클론
git clone https://github.com/ihw33/iwl-v5-rebuild.wiki.git

# 백업 생성
tar -czf wiki-backup-$(date +%Y%m%d).tar.gz iwl-v5-rebuild.wiki/
```

#### Wiki 동기화
```bash
cd iwl-v5-rebuild.wiki
git pull origin master
# 편집
git add .
git commit -m "Update wiki"
git push origin master
```

---

## 📊 모니터링

### 시스템 모니터링

#### 실시간 모니터링
```bash
# 시스템 상태
npm run monitor

# 메모리 사용량
npm run health-check

# API 상태
curl http://localhost:3000/api/health
```

#### 대시보드 활용
- URL: http://localhost:3000/dashboard
- 자동 새로고침: 5초
- 알림 설정 가능

### 성능 모니터링

#### 응답 시간 체크
```bash
# API 응답 시간
npm run perf:api

# 페이지 로드 시간
npm run perf:pages
```

#### 리소스 사용량
```javascript
// /api/admin/metrics
{
  "cpu": "15%",
  "memory": "512MB / 2GB",
  "disk": "10GB / 50GB",
  "connections": 42
}
```

---

## 💾 백업과 복구

### 자동 백업

#### 백업 스케줄
```bash
# crontab -e
0 2 * * * /usr/local/bin/backup-iwl.sh
```

#### 백업 스크립트
```bash
#!/bin/bash
# backup-iwl.sh

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backups/iwl-v5"

# 데이터베이스 백업
pg_dump $DATABASE_URL > $BACKUP_DIR/db_$DATE.sql

# 파일 백업
tar -czf $BACKUP_DIR/files_$DATE.tar.gz /app/uploads

# 환경 설정 백업
cp .env* $BACKUP_DIR/

# 오래된 백업 삭제 (30일 이상)
find $BACKUP_DIR -mtime +30 -delete
```

### 수동 백업
```bash
# 전체 백업
npm run backup:full

# 데이터베이스만
npm run backup:db

# 파일만
npm run backup:files
```

### 복구 절차

#### 데이터베이스 복구
```bash
# 백업에서 복구
psql $DATABASE_URL < backup.sql
```

#### 파일 복구
```bash
# 파일 복원
tar -xzf files_backup.tar.gz -C /
```

---

## 🔒 보안 설정

### 접근 제어

#### IP 화이트리스트
```javascript
// middleware.ts
const allowedIPs = [
  '127.0.0.1',
  '192.168.1.0/24'
];
```

#### Rate Limiting
```javascript
// 요청 제한
const limiter = {
  windowMs: 15 * 60 * 1000, // 15분
  max: 100 // 최대 100 요청
};
```

### SSL/TLS 설정
```nginx
server {
    listen 443 ssl http2;
    ssl_certificate /etc/ssl/certs/iwl.crt;
    ssl_certificate_key /etc/ssl/private/iwl.key;
    ssl_protocols TLSv1.2 TLSv1.3;
}
```

### 보안 헤더
```javascript
// next.config.js
const securityHeaders = [
  {
    key: 'X-Frame-Options',
    value: 'SAMEORIGIN'
  },
  {
    key: 'X-Content-Type-Options',
    value: 'nosniff'
  },
  {
    key: 'X-XSS-Protection',
    value: '1; mode=block'
  }
];
```

---

## 🚨 문제 해결

### 일반적인 문제

#### 서버 시작 실패
```bash
# 포트 충돌 확인
lsof -i :3000
kill -9 [PID]

# 의존성 재설치
rm -rf node_modules package-lock.json
npm install
```

#### 데이터베이스 연결 실패
```bash
# 연결 테스트
npm run db:test

# 마이그레이션 실행
npm run db:migrate
```

#### 메모리 부족
```bash
# 메모리 증가
NODE_OPTIONS="--max-old-space-size=4096" npm start

# 캐시 정리
npm run clean:cache
```

### 로그 분석

#### 에러 로그 확인
```bash
# 최근 에러
grep ERROR logs/app.log | tail -50

# 특정 시간대 에러
grep "2025-08-14" logs/error.log
```

#### 디버그 모드
```bash
# 상세 로그 활성화
DEBUG=* npm run dev
```

### 긴급 복구

#### 서비스 재시작
```bash
# 모든 서비스 재시작
npm run restart:all

# 데이터베이스만 재시작
npm run restart:db
```

#### 롤백
```bash
# 이전 버전으로 롤백
git checkout [previous-commit]
npm install
npm run build
npm start
```

---

## 📞 지원 연락처

### 기술 지원
- **QA Claude**: 시스템 문제
- **PM Claude**: 운영 문제
- **Codex**: 데이터베이스 문제

### 긴급 연락
- **Thomas**: 최종 결정 사항
- **GitHub Issues**: 버그 리포트
- **Discussions**: 일반 문의

---

## 📋 체크리스트

### 일일 점검
- [ ] 서버 상태 확인
- [ ] 로그 검토
- [ ] 백업 확인
- [ ] 모니터링 대시보드 체크

### 주간 점검
- [ ] 성능 리포트 생성
- [ ] 보안 업데이트 확인
- [ ] 사용자 활동 분석
- [ ] 백업 테스트

### 월간 점검
- [ ] 전체 시스템 점검
- [ ] 백업 복구 테스트
- [ ] 보안 감사
- [ ] 용량 계획 검토

---

**추가 도움이 필요하신가요?**  
[기술 문서](../Technical) | [FAQ](FAQ) | [Discussions](https://github.com/ihw33/iwl-v5-rebuild/discussions)
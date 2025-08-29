#!/usr/bin/env node

/**
 * JWT 인증 테스트 스크립트
 * 사용법: node scripts/test-jwt-auth.js
 */

const jwt = require('jsonwebtoken');
const http = require('http');

// 환경변수 설정 (개발용)
const JWT_SECRET = 'iwl-v5-rebuild-super-secret-jwt-key-for-development-only-2025';
const API_BASE_URL = 'http://localhost:3000';

/**
 * 테스트용 JWT 토큰 생성
 */
function generateTestJWT(userData) {
  const payload = {
    userId: userData.userId || 'test-user-123',
    email: userData.email || 'test@example.com',
    role: userData.role || 'user'
  };
  
  return jwt.sign(payload, JWT_SECRET, { 
    expiresIn: '24h',
    issuer: 'iwl-v5-rebuild'
  });
}

/**
 * API 요청 테스트 함수
 */
function testAPI(endpoint, token = null, method = 'GET', data = null) {
  return new Promise((resolve, reject) => {
    const url = new URL(endpoint, API_BASE_URL);
    const options = {
      method,
      headers: {
        'Content-Type': 'application/json'
      }
    };

    if (token) {
      options.headers['Authorization'] = `Bearer ${token}`;
    }

    const req = http.request(url, options, (res) => {
      let body = '';
      res.on('data', (chunk) => body += chunk);
      res.on('end', () => {
        try {
          const result = {
            status: res.statusCode,
            headers: res.headers,
            body: JSON.parse(body)
          };
          resolve(result);
        } catch (e) {
          resolve({
            status: res.statusCode,
            headers: res.headers,
            body: body
          });
        }
      });
    });

    req.on('error', reject);

    if (data) {
      req.write(JSON.stringify(data));
    }

    req.end();
  });
}

/**
 * 테스트 실행
 */
async function runTests() {
  console.log('🔐 JWT 인증 시스템 테스트 시작\n');

  // 1. 유효한 JWT 토큰 생성
  const validToken = generateTestJWT({
    userId: 'test-user-123',
    email: 'test@example.com',
    role: 'admin'
  });
  console.log('✅ 테스트용 JWT 토큰 생성됨');
  console.log(`Token: ${validToken.substring(0, 50)}...\n`);

  // 2. 인증 없이 KB Articles API 호출 (401 에러 예상)
  console.log('📋 테스트 1: 인증 없이 KB Articles API 호출');
  try {
    const result = await testAPI('/api/kb/articles');
    console.log(`Status: ${result.status}`);
    console.log(`Response: ${JSON.stringify(result.body, null, 2)}\n`);
  } catch (error) {
    console.log(`Error: ${error.message}\n`);
  }

  // 3. 잘못된 토큰으로 KB Articles API 호출 (401 에러 예상)
  console.log('📋 테스트 2: 잘못된 JWT 토큰으로 KB Articles API 호출');
  try {
    const result = await testAPI('/api/kb/articles', 'invalid-token');
    console.log(`Status: ${result.status}`);
    console.log(`Response: ${JSON.stringify(result.body, null, 2)}\n`);
  } catch (error) {
    console.log(`Error: ${error.message}\n`);
  }

  // 4. 유효한 JWT 토큰으로 KB Articles API 호출 (200 성공 예상)
  console.log('📋 테스트 3: 유효한 JWT 토큰으로 KB Articles API 호출');
  try {
    const result = await testAPI('/api/kb/articles', validToken);
    console.log(`Status: ${result.status}`);
    console.log(`Response: ${JSON.stringify(result.body, null, 2)}\n`);
  } catch (error) {
    console.log(`Error: ${error.message}\n`);
  }

  // 5. 인증 없이 KB Search API 호출 (401 에러 예상)
  console.log('🔍 테스트 4: 인증 없이 KB Search API 호출');
  try {
    const result = await testAPI('/api/kb/search', null, 'POST', {
      query: 'test search query'
    });
    console.log(`Status: ${result.status}`);
    console.log(`Response: ${JSON.stringify(result.body, null, 2)}\n`);
  } catch (error) {
    console.log(`Error: ${error.message}\n`);
  }

  // 6. 유효한 JWT 토큰으로 KB Search API 호출 (200 성공 예상)
  console.log('🔍 테스트 5: 유효한 JWT 토큰으로 KB Search API 호출');
  try {
    const result = await testAPI('/api/kb/search', validToken, 'POST', {
      query: 'test search query'
    });
    console.log(`Status: ${result.status}`);
    console.log(`Response: ${JSON.stringify(result.body, null, 2)}\n`);
  } catch (error) {
    console.log(`Error: ${error.message}\n`);
  }

  console.log('🎉 JWT 인증 시스템 테스트 완료');
}

// 스크립트가 직접 실행된 경우에만 테스트 실행
if (require.main === module) {
  runTests().catch(console.error);
}

module.exports = { generateTestJWT, testAPI };
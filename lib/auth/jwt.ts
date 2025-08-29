import jwt from 'jsonwebtoken';
import { NextRequest } from 'next/server';

export interface JWTPayload {
  userId: string;
  email: string;
  role?: string;
  exp?: number;
  iat?: number;
}

export interface AuthenticatedRequest extends NextRequest {
  user?: JWTPayload;
}

/**
 * JWT 토큰 검증 미들웨어
 * Authorization 헤더에서 Bearer 토큰을 추출하고 검증
 */
export function verifyJWT(token: string): JWTPayload | null {
  try {
    const secret = process.env.JWT_SECRET;
    if (!secret) {
      console.error('JWT_SECRET 환경변수가 설정되지 않았습니다');
      return null;
    }

    const decoded = jwt.verify(token, secret) as JWTPayload;
    return decoded;
  } catch (error) {
    console.error('JWT 토큰 검증 실패:', error);
    return null;
  }
}

/**
 * 요청에서 JWT 토큰 추출
 * Authorization: Bearer <token> 형식에서 토큰 부분만 추출
 */
export function extractTokenFromRequest(request: NextRequest): string | null {
  const authHeader = request.headers.get('authorization');
  
  if (!authHeader) {
    return null;
  }

  if (!authHeader.startsWith('Bearer ')) {
    return null;
  }

  return authHeader.substring(7); // 'Bearer ' 제거
}

/**
 * API 라우트에서 사용할 인증 검증 함수
 * 토큰을 검증하고 사용자 정보를 반환
 */
export function authenticateRequest(request: NextRequest): {
  isAuthenticated: boolean;
  user?: JWTPayload;
  error?: string;
} {
  const token = extractTokenFromRequest(request);
  
  if (!token) {
    return {
      isAuthenticated: false,
      error: 'Authorization 헤더가 없거나 잘못된 형식입니다'
    };
  }

  const user = verifyJWT(token);
  
  if (!user) {
    return {
      isAuthenticated: false,
      error: 'JWT 토큰이 유효하지 않습니다'
    };
  }

  return {
    isAuthenticated: true,
    user
  };
}

/**
 * JWT 토큰 생성 (필요시 사용)
 */
export function generateJWT(payload: Omit<JWTPayload, 'exp' | 'iat'>): string | null {
  try {
    const secret = process.env.JWT_SECRET;
    if (!secret) {
      console.error('JWT_SECRET 환경변수가 설정되지 않았습니다');
      return null;
    }

    return jwt.sign(payload, secret, { 
      expiresIn: '24h',
      issuer: 'iwl-v5-rebuild'
    });
  } catch (error) {
    console.error('JWT 토큰 생성 실패:', error);
    return null;
  }
}

/**
 * 인증 실패 시 반환할 표준 응답
 */
export function createUnauthorizedResponse(message: string = '인증이 필요합니다') {
  return new Response(
    JSON.stringify({
      error: 'Unauthorized',
      message,
      code: 'AUTH_REQUIRED'
    }),
    {
      status: 401,
      headers: {
        'Content-Type': 'application/json',
        'WWW-Authenticate': 'Bearer realm="API"'
      }
    }
  );
}

/**
 * 권한 부족 시 반환할 표준 응답
 */
export function createForbiddenResponse(message: string = '권한이 부족합니다') {
  return new Response(
    JSON.stringify({
      error: 'Forbidden',
      message,
      code: 'INSUFFICIENT_PERMISSIONS'
    }),
    {
      status: 403,
      headers: {
        'Content-Type': 'application/json'
      }
    }
  );
}
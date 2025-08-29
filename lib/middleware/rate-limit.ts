import { NextRequest, NextResponse } from 'next/server';
import { Ratelimit } from '@upstash/ratelimit';
import { Redis } from '@upstash/redis';
import { config, hasRateLimiting } from '@/lib/config/env';

// Initialize Redis client for rate limiting
const redis = hasRateLimiting() && 
              config.UPSTASH_REDIS_URL?.startsWith('https://') &&
              !config.UPSTASH_REDIS_URL.includes('your_production')
  ? new Redis({
      url: config.UPSTASH_REDIS_URL,
      token: config.UPSTASH_REDIS_TOKEN!,
    })
  : null;

// Different rate limits for different types of requests
export const rateLimits = {
  // General API requests: 100 requests per 15 minutes
  api: new Ratelimit({
    redis: redis as any || new Map(), // Fallback to memory if no Redis
    limiter: Ratelimit.slidingWindow(100, '15 m'),
    analytics: true,
    prefix: 'iwl_api',
  }),

  // Search requests: 50 requests per 5 minutes
  search: new Ratelimit({
    redis: redis as any || new Map(),
    limiter: Ratelimit.slidingWindow(50, '5 m'),
    analytics: true,
    prefix: 'iwl_search',
  }),

  // Auth requests: 10 requests per minute
  auth: new Ratelimit({
    redis: redis as any || new Map(),
    limiter: Ratelimit.slidingWindow(10, '1 m'),
    analytics: true,
    prefix: 'iwl_auth',
  }),

  // AI/KB requests: 20 requests per minute
  ai: new Ratelimit({
    redis: redis as any || new Map(),
    limiter: Ratelimit.slidingWindow(20, '1 m'),
    analytics: true,
    prefix: 'iwl_ai',
  }),
};

export async function applyRateLimit(
  req: NextRequest,
  type: keyof typeof rateLimits = 'api'
): Promise<NextResponse | null> {
  if (!rateLimits[type]) {
    return NextResponse.json(
      { error: 'Invalid rate limit type' },
      { status: 500 }
    );
  }

  // Get client identifier (IP address or user ID if authenticated)
  const identifier = getClientIdentifier(req);
  
  try {
    const { success, limit, remaining, reset } = await rateLimits[type].limit(identifier);

    if (!success) {
      return NextResponse.json(
        { 
          error: 'Too many requests',
          limit,
          remaining: 0,
          resetTime: new Date(reset),
        },
        { 
          status: 429,
          headers: {
            'X-RateLimit-Limit': limit.toString(),
            'X-RateLimit-Remaining': '0',
            'X-RateLimit-Reset': reset.toString(),
            'Retry-After': Math.round((reset - Date.now()) / 1000).toString(),
          }
        }
      );
    }

    // Add rate limit headers to successful responses
    const response = NextResponse.next();
    response.headers.set('X-RateLimit-Limit', limit.toString());
    response.headers.set('X-RateLimit-Remaining', remaining.toString());
    response.headers.set('X-RateLimit-Reset', reset.toString());

    return null; // null means rate limit passed
  } catch (error) {
    // If rate limiting fails, allow the request to proceed
    return null;
  }
}

function getClientIdentifier(req: NextRequest): string {
  // Try to get user ID from headers (if authenticated)
  const userId = req.headers.get('x-user-id');
  if (userId) {
    return `user:${userId}`;
  }

  // Fallback to IP address
  const forwarded = req.headers.get('x-forwarded-for');
  const realIP = req.headers.get('x-real-ip');
  const ip = forwarded ? forwarded.split(',')[0].trim() : realIP || 'unknown';
  
  return `ip:${ip}`;
}

// Helper function to combine multiple middleware
export async function withRateLimit<T>(
  req: NextRequest,
  type: keyof typeof rateLimits,
  handler: (req: NextRequest) => Promise<T>
): Promise<T | NextResponse> {
  const rateLimitResult = await applyRateLimit(req, type);
  if (rateLimitResult) {
    return rateLimitResult;
  }
  return handler(req);
}
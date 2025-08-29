import { NextRequest, NextResponse } from 'next/server';
import { createServerSupabaseClient } from '@/lib/auth';

export interface APIResponse<T = any> {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
}

export interface APIEndpoint {
  path: string;
  method: 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH';
  handler: (req: NextRequest, params?: any) => Promise<NextResponse>;
  requireAuth?: boolean;
  rateLimit?: number;
}

export class APIGateway {
  private static endpoints: Map<string, APIEndpoint> = new Map();
  private static rateLimits: Map<string, { count: number; resetAt: number }> = new Map();

  static register(endpoint: APIEndpoint) {
    const key = `${endpoint.method}:${endpoint.path}`;
    this.endpoints.set(key, endpoint);
  }

  static async handle(
    req: NextRequest,
    method: string,
    path: string,
    params?: any
  ): Promise<NextResponse> {
    const key = `${method}:${path}`;
    const endpoint = this.endpoints.get(key);

    if (!endpoint) {
      return NextResponse.json(
        { success: false, error: 'Endpoint not found' },
        { status: 404 }
      );
    }

    // Rate limiting
    if (endpoint.rateLimit) {
      const clientIp = req.headers.get('x-forwarded-for') || 'unknown';
      const limitKey = `${clientIp}:${key}`;
      const now = Date.now();
      
      const limit = this.rateLimits.get(limitKey);
      
      if (limit && limit.resetAt > now) {
        if (limit.count >= endpoint.rateLimit) {
          return NextResponse.json(
            { success: false, error: 'Rate limit exceeded' },
            { status: 429 }
          );
        }
        limit.count++;
      } else {
        this.rateLimits.set(limitKey, {
          count: 1,
          resetAt: now + 60000 // Reset after 1 minute
        });
      }
    }

    // Authentication check
    if (endpoint.requireAuth) {
      const supabase = createServerSupabaseClient();
      const { data: { session } } = await supabase.auth.getSession();
      
      if (!session) {
        return NextResponse.json(
          { success: false, error: 'Unauthorized' },
          { status: 401 }
        );
      }
    }

    try {
      return await endpoint.handler(req, params);
    } catch (error: any) {
      return NextResponse.json(
        { 
          success: false, 
          error: error.message || 'Internal server error' 
        },
        { status: 500 }
      );
    }
  }

  static list(): APIEndpoint[] {
    return Array.from(this.endpoints.values());
  }
}

// Helper function for standard API responses
export function apiResponse<T = any>(
  data?: T,
  error?: string,
  status: number = 200
): NextResponse {
  if (error) {
    return NextResponse.json(
      { success: false, error },
      { status }
    );
  }

  return NextResponse.json(
    { success: true, data },
    { status }
  );
}

// Middleware for API routes
export async function apiMiddleware(req: NextRequest) {
  // CORS headers
  const headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
  };

  // Handle preflight requests
  if (req.method === 'OPTIONS') {
    return new NextResponse(null, { status: 200, headers });
  }

  // Add security headers
  const response = NextResponse.next();
  Object.entries(headers).forEach(([key, value]) => {
    response.headers.set(key, value);
  });

  return response;
}
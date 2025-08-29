import { NextRequest, NextResponse } from 'next/server';
import { requireAuth, requireRole, getAuthenticatedUser } from './auth';
import { applyRateLimit, rateLimits } from './rate-limit';

export interface MiddlewareOptions {
  auth?: boolean;
  role?: string;
  rateLimit?: keyof typeof rateLimits;
}

export interface RequestWithUser extends NextRequest {
  user?: {
    id: string;
    email: string;
    name?: string;
    role: string;
    avatarUrl?: string;
  };
}

/**
 * Combined middleware function that applies authentication, authorization, and rate limiting
 * @param req - The incoming request
 * @param options - Middleware configuration options
 * @param handler - The actual route handler function
 */
export async function withMiddleware<T>(
  req: NextRequest,
  options: MiddlewareOptions,
  handler: (req: RequestWithUser) => Promise<T>
): Promise<T | NextResponse> {
  // Apply rate limiting first
  if (options.rateLimit) {
    const rateLimitResult = await applyRateLimit(req, options.rateLimit);
    if (rateLimitResult) {
      return rateLimitResult;
    }
  }

  // Apply authentication if required
  if (options.auth) {
    const authResult = await requireAuth(req);
    if (authResult) {
      return authResult;
    }
  }

  // Apply role-based authorization if required
  if (options.role) {
    const roleResult = await requireRole(req, options.role);
    if (roleResult) {
      return roleResult;
    }
  }

  // Get user information if authenticated
  const user = options.auth ? await getAuthenticatedUser(req) : null;
  
  // Create a new request object with user information
  const requestWithUser = req as RequestWithUser;
  if (user) {
    requestWithUser.user = user;
  }

  return handler(requestWithUser);
}

/**
 * Convenience functions for common middleware combinations
 */

// Public API with rate limiting
export function withPublicAPI<T>(
  req: NextRequest,
  handler: (req: RequestWithUser) => Promise<T>
): Promise<T | NextResponse> {
  return withMiddleware(req, { rateLimit: 'api' }, handler);
}

// Authenticated API with rate limiting
export function withAuthenticatedAPI<T>(
  req: NextRequest,
  handler: (req: RequestWithUser) => Promise<T>
): Promise<T | NextResponse> {
  return withMiddleware(req, { auth: true, rateLimit: 'api' }, handler);
}

// Search API with specialized rate limiting
export function withSearchAPI<T>(
  req: NextRequest,
  authenticated: boolean = false,
  handler: (req: RequestWithUser) => Promise<T>
): Promise<T | NextResponse> {
  return withMiddleware(
    req,
    { auth: authenticated, rateLimit: 'search' },
    handler
  );
}

// AI/KB API with specialized rate limiting
export function withAIAPI<T>(
  req: NextRequest,
  authenticated: boolean = true,
  handler: (req: RequestWithUser) => Promise<T>
): Promise<T | NextResponse> {
  return withMiddleware(
    req,
    { auth: authenticated, rateLimit: 'ai' },
    handler
  );
}

// Admin-only API
export function withAdminAPI<T>(
  req: NextRequest,
  handler: (req: RequestWithUser) => Promise<T>
): Promise<T | NextResponse> {
  return withMiddleware(
    req,
    { auth: true, role: 'admin', rateLimit: 'api' },
    handler
  );
}

// Instructor-level API (instructors and admins)
export function withInstructorAPI<T>(
  req: NextRequest,
  handler: (req: RequestWithUser) => Promise<T>
): Promise<T | NextResponse> {
  return withMiddleware(req, { auth: true, rateLimit: 'api' }, async (req) => {
    // Custom logic for instructor or admin role
    if (req.user && !['instructor', 'admin'].includes(req.user.role)) {
      return NextResponse.json(
        { error: 'Insufficient permissions' },
        { status: 403 }
      ) as T;
    }
    return handler(req);
  });
}

// Export middleware components for direct use
export { requireAuth, requireRole, getAuthenticatedUser } from './auth';
export { applyRateLimit, rateLimits } from './rate-limit';
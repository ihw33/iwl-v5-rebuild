import { NextRequest, NextResponse } from 'next/server';
import { createServerSupabaseClient } from '@/lib/auth';
import { cookies } from 'next/headers';
import { authenticateRequest, createUnauthorizedResponse, createForbiddenResponse } from '@/lib/auth/jwt';

export interface AuthenticatedRequest extends NextRequest {
  user?: {
    id: string;
    email: string;
    role: string;
  };
}

export async function requireAuth(req: NextRequest): Promise<NextResponse | null> {
  // First try JWT authentication
  const jwtAuth = authenticateRequest(req);
  if (jwtAuth.isAuthenticated && jwtAuth.user) {
    return null; // JWT authentication passed
  }

  // Fallback to Supabase session authentication
  try {
    const cookieStore = cookies();
    const supabase = createServerSupabaseClient();
    
    const { data: { session }, error } = await supabase.auth.getSession();
    
    if (error || !session) {
      return createUnauthorizedResponse('Authentication required - provide JWT token or valid session');
    }

    // Get user profile from database
    const { data: userProfile, error: profileError } = await supabase
      .from('users')
      .select('id, email, role')
      .eq('id', session.user.id)
      .single();

    if (profileError || !userProfile) {
      return createUnauthorizedResponse('User profile not found');
    }

    // Attach user to request (for TypeScript, we'll handle this in the route)
    return null; // null means authentication passed
  } catch (error) {
    return NextResponse.json(
      { error: 'Authentication failed' },
      { status: 500 }
    );
  }
}

export async function requireRole(req: NextRequest, requiredRole: string): Promise<NextResponse | null> {
  const authError = await requireAuth(req);
  if (authError) return authError;

  try {
    const supabase = createServerSupabaseClient();
    const { data: { session } } = await supabase.auth.getSession();
    
    if (!session) {
      return NextResponse.json(
        { error: 'Authentication required' },
        { status: 401 }
      );
    }

    const { data: userProfile } = await supabase
      .from('users')
      .select('role')
      .eq('id', session.user.id)
      .single();

    if (!userProfile || userProfile.role !== requiredRole) {
      return NextResponse.json(
        { error: 'Insufficient permissions' },
        { status: 403 }
      );
    }

    return null; // null means authorization passed
  } catch (error) {
    return NextResponse.json(
      { error: 'Authorization failed' },
      { status: 500 }
    );
  }
}

export async function getAuthenticatedUser(req: NextRequest) {
  // First try JWT authentication
  const jwtAuth = authenticateRequest(req);
  if (jwtAuth.isAuthenticated && jwtAuth.user) {
    return {
      id: jwtAuth.user.userId,
      email: jwtAuth.user.email,
      name: jwtAuth.user.email.split('@')[0], // Use email prefix as name fallback
      role: jwtAuth.user.role || 'user',
      avatarUrl: undefined
    };
  }

  // Fallback to Supabase session authentication
  try {
    const supabase = createServerSupabaseClient();
    const { data: { session }, error } = await supabase.auth.getSession();
    
    if (error || !session) {
      return null;
    }

    const { data: userProfile } = await supabase
      .from('users')
      .select('id, email, name, role, avatar_url')
      .eq('id', session.user.id)
      .single();

    return userProfile ? {
      id: userProfile.id,
      email: userProfile.email,
      name: userProfile.name,
      role: userProfile.role,
      avatarUrl: userProfile.avatar_url
    } : null;
  } catch (error) {
    return null;
  }
}
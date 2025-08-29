import { createClient } from '@supabase/supabase-js';
import { createServerComponentClient } from '@supabase/auth-helpers-nextjs';
import { cookies } from 'next/headers';
import { config } from '@/lib/config/env';

export const supabase = createClient(config.SUPABASE_URL, config.SUPABASE_ANON_KEY);

export function createServerSupabaseClient() {
  const cookieStore = cookies();
  return createServerComponentClient({ cookies: () => cookieStore });
}

export interface User {
  id: string;
  email: string;
  name?: string;
  avatarUrl?: string;
  role: 'student' | 'instructor' | 'admin';
}

export interface AuthSession {
  user: User | null;
  isLoading: boolean;
}

export async function getSession(): Promise<AuthSession> {
  try {
    const supabase = createServerSupabaseClient();
    const { data: { session } } = await supabase.auth.getSession();
    
    if (!session) {
      return { user: null, isLoading: false };
    }

    const { data: userProfile } = await supabase
      .from('users')
      .select('*')
      .eq('id', session.user.id)
      .single();

    return {
      user: userProfile ? {
        id: userProfile.id,
        email: userProfile.email,
        name: userProfile.name,
        avatarUrl: userProfile.avatar_url,
        role: userProfile.role
      } : null,
      isLoading: false
    };
  } catch (error) {
    return { user: null, isLoading: false };
  }
}

export async function signIn(email: string, password: string) {
  const { data, error } = await supabase.auth.signInWithPassword({
    email,
    password,
  });

  if (error) throw error;
  return data;
}

export async function signUp(email: string, password: string, name?: string) {
  const { data, error } = await supabase.auth.signUp({
    email,
    password,
    options: {
      data: {
        name,
      }
    }
  });

  if (error) throw error;
  
  if (data.user) {
    await supabase
      .from('users')
      .insert({
        id: data.user.id,
        email: data.user.email,
        name,
      });
  }

  return data;
}

export async function signOut() {
  const { error } = await supabase.auth.signOut();
  if (error) throw error;
}

export async function resetPassword(email: string) {
  const { error } = await supabase.auth.resetPasswordForEmail(email, {
    redirectTo: `${window.location.origin}/auth/reset-password`,
  });
  
  if (error) throw error;
}
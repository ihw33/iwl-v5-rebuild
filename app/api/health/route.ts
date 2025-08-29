import { NextRequest, NextResponse } from 'next/server';
import { createClient } from '@supabase/supabase-js';
import { withPublicAPI } from '@/lib/middleware';

export async function GET(req: NextRequest) {
  return withPublicAPI(req, async (req) => {
  const response = {
    status: 'healthy',
    timestamp: new Date().toISOString(),
    services: {
      api: 'operational',
      supabase: 'unknown',
      database: 'unknown'
    },
    environment: process.env.NODE_ENV || 'development'
  };

  // Supabase 연결 테스트
  try {
    const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL;
    const supabaseKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
    
    if (!supabaseUrl || !supabaseKey) {
      response.services.supabase = 'not_configured';
      response.services.database = 'not_configured';
    } else if (supabaseUrl === 'https://dummy.supabase.co') {
      response.services.supabase = 'dummy_mode';
      response.services.database = 'dummy_mode';
    } else {
      // 실제 Supabase 연결 테스트
      const supabase = createClient(supabaseUrl, supabaseKey);
      
      // 간단한 쿼리로 연결 확인
      const { error } = await supabase
        .from('users')
        .select('count')
        .limit(1)
        .single();
      
      if (!error) {
        response.services.supabase = 'operational';
        response.services.database = 'operational';
      } else {
        response.services.supabase = 'error';
        response.services.database = 'error';
      }
    }
  } catch (error) {
    response.services.supabase = 'error';
    response.services.database = 'error';
  }

  return NextResponse.json(response);
  });
}
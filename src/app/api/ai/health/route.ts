import { NextResponse } from 'next/server';

export async function GET() {
  try {
    // OpenAI API 키 확인
    const hasApiKey = !!process.env.OPENAI_API_KEY;
    
    // API 연결 테스트
    let apiTest = false;
    if (hasApiKey) {
      try {
        const response = await fetch('https://api.openai.com/v1/models', {
          headers: {
            'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`,
          },
        });
        apiTest = response.ok;
      } catch (error) {
        console.error('OpenAI API 연결 테스트 실패:', error);
      }
    }

    return NextResponse.json({
      status: 'healthy',
      timestamp: new Date().toISOString(),
      services: {
        openai: {
          api_key_configured: hasApiKey,
          connection_test: apiTest,
          available_models: hasApiKey && apiTest ? ['gpt-5', 'gpt-4', 'gpt-3.5-turbo'] : []
        }
      },
      environment: {
        node_env: process.env.NODE_ENV,
        next_version: process.env.NEXT_VERSION || 'unknown'
      }
    });
  } catch (error) {
    return NextResponse.json(
      { 
        status: 'unhealthy',
        error: 'Health check failed',
        timestamp: new Date().toISOString()
      },
      { status: 500 }
    );
  }
}

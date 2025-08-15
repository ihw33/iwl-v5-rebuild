import { NextResponse } from 'next/server';

export async function GET() {
  try {
    // 실제 프로덕션에서는 데이터베이스에서 통계를 가져와야 합니다
    const stats = {
      total_requests: 0,
      successful_requests: 0,
      failed_requests: 0,
      models_used: {
        'gpt-5': 0,
        'gpt-4': 0,
        'gpt-3.5-turbo': 0
      },
      average_response_time: 0,
      last_24_hours: {
        requests: 0,
        tokens_used: 0
      }
    };

    return NextResponse.json({
      success: true,
      data: stats,
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    return NextResponse.json(
      { 
        success: false,
        error: '통계를 가져올 수 없습니다.',
        timestamp: new Date().toISOString()
      },
      { status: 500 }
    );
  }
}

import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { prompt, model = 'gpt-5', max_tokens = 1000 } = body;

    if (!prompt) {
      return NextResponse.json(
        { error: '프롬프트가 필요합니다.' },
        { status: 400 }
      );
    }

    // OpenAI API 호출
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`,
      },
      body: JSON.stringify({
        model: model,
        messages: [
          {
            role: 'system',
            content: '당신은 IWL v5.0 프로젝트의 AI 어시스턴트입니다. 사용자의 질문에 대해 도움이 되는 답변을 제공해주세요.'
          },
          {
            role: 'user',
            content: prompt
          }
        ],
        max_tokens: max_tokens,
        temperature: 0.7,
      }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      console.error('OpenAI API 오류:', errorData);
      return NextResponse.json(
        { error: 'AI 서비스에 연결할 수 없습니다.' },
        { status: 500 }
      );
    }

    const data = await response.json();
    
    return NextResponse.json({
      success: true,
      response: data.choices[0]?.message?.content || '응답을 생성할 수 없습니다.',
      usage: data.usage
    });

  } catch (error) {
    console.error('API 오류:', error);
    return NextResponse.json(
      { error: '서버 오류가 발생했습니다.' },
      { status: 500 }
    );
  }
}

export async function GET() {
  return NextResponse.json({
    message: 'IWL v5.0 AI Generate API',
    status: 'active',
    available_models: ['gpt-5', 'gpt-4', 'gpt-3.5-turbo']
  });
}

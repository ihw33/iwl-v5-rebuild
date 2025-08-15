'use client';

import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Textarea } from '@/components/ui/textarea';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Loader2, Send, CheckCircle, XCircle } from 'lucide-react';

export default function ChatGPT5Test() {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [healthStatus, setHealthStatus] = useState<any>(null);

  const testHealth = async () => {
    try {
      const res = await fetch('/api/ai/health');
      const data = await res.json();
      setHealthStatus(data);
    } catch (err) {
      setError('Health check failed');
    }
  };

  const generateResponse = async () => {
    if (!prompt.trim()) return;

    setLoading(true);
    setError('');
    setResponse('');

    try {
      const res = await fetch('/api/ai/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          prompt: prompt,
          model: 'gpt-5',
          max_tokens: 1000
        }),
      });

      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.error || 'API 호출 실패');
      }

      setResponse(data.response);
    } catch (err: any) {
      setError(err.message || '오류가 발생했습니다.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto p-6 space-y-6">
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            🤖 ChatGPT 5 테스트
            <Badge variant="outline">API v1</Badge>
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="flex gap-2">
            <Button onClick={testHealth} variant="outline" size="sm">
              Health Check
            </Button>
            {healthStatus && (
              <div className="flex items-center gap-2">
                {healthStatus.services?.openai?.connection_test ? (
                  <CheckCircle className="h-4 w-4 text-green-500" />
                ) : (
                  <XCircle className="h-4 w-4 text-red-500" />
                )}
                <span className="text-sm">
                  OpenAI: {healthStatus.services?.openai?.api_key_configured ? 'Configured' : 'Not Configured'}
                </span>
              </div>
            )}
          </div>

          <div className="space-y-2">
            <label className="text-sm font-medium">프롬프트 입력:</label>
            <Textarea
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="ChatGPT 5에게 물어보고 싶은 내용을 입력하세요..."
              rows={4}
            />
          </div>

          <Button 
            onClick={generateResponse} 
            disabled={loading || !prompt.trim()}
            className="w-full"
          >
            {loading ? (
              <>
                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                생성 중...
              </>
            ) : (
              <>
                <Send className="mr-2 h-4 w-4" />
                ChatGPT 5에게 질문하기
              </>
            )}
          </Button>

          {error && (
            <div className="p-4 bg-red-50 border border-red-200 rounded-lg">
              <p className="text-red-700 text-sm">{error}</p>
            </div>
          )}

          {response && (
            <div className="space-y-2">
              <label className="text-sm font-medium">응답:</label>
              <div className="p-4 bg-gray-50 border rounded-lg">
                <p className="whitespace-pre-wrap text-sm">{response}</p>
              </div>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}

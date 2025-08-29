'use client';

import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Download, FileText, Loader2 } from 'lucide-react';

export default function ConvertPage() {
  const [markdown, setMarkdown] = useState(`# Sample Markdown

## Introduction
This is a **sample** markdown document with:
- Bullet points
- **Bold text**
- *Italic text*
- [Links](https://example.com)

### Code Example
\`\`\`javascript
function hello() {
  console.log("Hello, World!");
}
\`\`\`

### Table
| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
| Data 3   | Data 4   |
`);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleConvert = async () => {
    setLoading(true);
    setError('');

    try {
      const response = await fetch('/api/convert/md-to-pdf', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          markdown,
          filename: 'converted-document'
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Conversion failed');
      }

      // Download the PDF
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'converted-document.pdf';
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Conversion failed');
    } finally {
      setLoading(false);
    }
  };

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file && file.name.endsWith('.md')) {
      const reader = new FileReader();
      reader.onload = (event) => {
        setMarkdown(event.target?.result as string);
      };
      reader.readAsText(file);
    }
  };

  return (
    <div className="container mx-auto p-8 max-w-6xl">
      <h1 className="text-4xl font-bold mb-8">Markdown to PDF Converter</h1>
      
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Input Section */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <FileText className="w-5 h-5" />
              Markdown Input
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <input
                  type="file"
                  accept=".md"
                  onChange={handleFileUpload}
                  className="mb-4"
                />
              </div>
              <textarea
                value={markdown}
                onChange={(e) => setMarkdown(e.target.value)}
                className="w-full h-96 p-4 border rounded-lg font-mono text-sm"
                placeholder="Enter your markdown here..."
              />
            </div>
          </CardContent>
        </Card>

        {/* Preview/Actions Section */}
        <Card>
          <CardHeader>
            <CardTitle>Preview & Actions</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {/* Preview */}
              <div className="border rounded-lg p-4 h-96 overflow-auto prose prose-sm max-w-none">
                <div dangerouslySetInnerHTML={{ 
                  __html: markdown
                    .replace(/^# (.*$)/gim, '<h1>$1</h1>')
                    .replace(/^## (.*$)/gim, '<h2>$1</h2>')
                    .replace(/^### (.*$)/gim, '<h3>$1</h3>')
                    .replace(/\*\*(.*)\*\*/g, '<strong>$1</strong>')
                    .replace(/\*(.*)\*/g, '<em>$1</em>')
                    .replace(/\n/g, '<br>')
                }} />
              </div>

              {/* Error Display */}
              {error && (
                <div className="bg-red-50 border border-red-200 text-red-800 px-4 py-2 rounded">
                  {error}
                </div>
              )}

              {/* Convert Button */}
              <Button 
                onClick={handleConvert} 
                disabled={loading || !markdown}
                className="w-full"
                size="lg"
              >
                {loading ? (
                  <>
                    <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                    Converting...
                  </>
                ) : (
                  <>
                    <Download className="mr-2 h-4 w-4" />
                    Convert to PDF
                  </>
                )}
              </Button>

              {/* Instructions */}
              <div className="text-sm text-muted-foreground space-y-2">
                <p>📝 Enter or paste your Markdown content</p>
                <p>📁 Or upload a .md file</p>
                <p>📄 Click convert to download as PDF</p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Status Check */}
      <Card className="mt-8">
        <CardHeader>
          <CardTitle>Service Status</CardTitle>
        </CardHeader>
        <CardContent>
          <ServiceStatus />
        </CardContent>
      </Card>
    </div>
  );
}

function ServiceStatus() {
  const [status, setStatus] = useState<any>(null);
  const [checking, setChecking] = useState(false);

  const checkStatus = async () => {
    setChecking(true);
    try {
      const response = await fetch('/api/convert/md-to-pdf');
      const data = await response.json();
      setStatus(data);
    } catch (error) {
      setStatus({ status: 'error', message: 'Failed to check status' });
    } finally {
      setChecking(false);
    }
  };

  return (
    <div className="space-y-4">
      <Button onClick={checkStatus} disabled={checking} variant="outline">
        {checking ? 'Checking...' : 'Check Service Status'}
      </Button>
      
      {status && (
        <div className={`p-4 rounded-lg ${
          status.status === 'ready' ? 'bg-green-50' : 'bg-red-50'
        }`}>
          <p className="font-semibold">
            Status: {status.status === 'ready' ? '✅ Ready' : '❌ Not Available'}
          </p>
          {status.pandoc && <p>Pandoc: {status.pandoc}</p>}
          <p className="text-sm mt-2">{status.message}</p>
        </div>
      )}
    </div>
  );
}
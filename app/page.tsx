import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import Link from 'next/link'

export default function HomePage() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-8">
      <div className="max-w-4xl w-full space-y-8">
        <div className="text-center space-y-4">
          <h1 className="text-5xl font-bold tracking-tight">
            IWL v5
          </h1>
          <p className="text-xl text-muted-foreground">
            Interactive Writing & Learning Platform
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-6">
          <Card>
            <CardHeader>
              <CardTitle>AI-Powered Learning</CardTitle>
              <CardDescription>
                Personalized learning experiences with GPT-4, Claude, and Gemini
              </CardDescription>
            </CardHeader>
            <CardContent>
              <Button asChild className="w-full">
                <Link href="/learn">Start Learning</Link>
              </Button>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Knowledge Base</CardTitle>
              <CardDescription>
                RAG-powered intelligent content search and discovery
              </CardDescription>
            </CardHeader>
            <CardContent>
              <Button asChild variant="outline" className="w-full">
                <Link href="/knowledge">Explore KB</Link>
              </Button>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Collaborative Writing</CardTitle>
              <CardDescription>
                Real-time collaboration with AI assistance
              </CardDescription>
            </CardHeader>
            <CardContent>
              <Button asChild variant="secondary" className="w-full">
                <Link href="/write">Start Writing</Link>
              </Button>
            </CardContent>
          </Card>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Project Status</CardTitle>
            <CardDescription>Build Phase Progress</CardDescription>
          </CardHeader>
          <CardContent className="space-y-2">
            <div className="flex justify-between">
              <span>Database Schema</span>
              <span className="text-green-600">✓ Completed</span>
            </div>
            <div className="flex justify-between">
              <span>Auth System</span>
              <span className="text-green-600">✓ Completed</span>
            </div>
            <div className="flex justify-between">
              <span>API Gateway</span>
              <span className="text-green-600">✓ Completed</span>
            </div>
            <div className="flex justify-between">
              <span>UI Components</span>
              <span className="text-green-600">✓ Completed</span>
            </div>
            <div className="flex justify-between">
              <span>Next.js 15 + React 19</span>
              <span className="text-green-600">✓ Configured</span>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
'use client';

import { useState, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { CheckCircle2, AlertCircle, Activity, Cpu, HardDrive, Globe } from 'lucide-react';

export default function Dashboard() {
  const [health, setHealth] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchHealth();
    const interval = setInterval(fetchHealth, 5000); // 5초마다 업데이트
    return () => clearInterval(interval);
  }, []);

  const fetchHealth = async () => {
    try {
      const res = await fetch('/api/health');
      const data = await res.json();
      setHealth(data);
      setLoading(false);
    } catch (error) {
      console.error('Failed to fetch health:', error);
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="animate-pulse">Loading...</div>
      </div>
    );
  }

  return (
    <div className="container mx-auto p-8">
      <div className="mb-8">
        <h1 className="text-4xl font-bold mb-2">IWL v5.0 Dashboard</h1>
        <p className="text-muted-foreground">실시간 시스템 모니터링</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* System Status */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Activity className="w-5 h-5" />
              System Status
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <span>Status</span>
                <Badge className="bg-green-500">
                  {health?.status === 'healthy' ? 'Healthy' : 'Error'}
                </Badge>
              </div>
              <div className="flex items-center justify-between">
                <span>Environment</span>
                <span className="font-mono text-sm">{health?.environment}</span>
              </div>
              <div className="flex items-center justify-between">
                <span>Node.js</span>
                <span className="font-mono text-sm">{health?.node}</span>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Claude Setup */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Globe className="w-5 h-5" />
              Claude Configuration
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <span>Configured</span>
                {health?.claude?.configured ? (
                  <CheckCircle2 className="w-5 h-5 text-green-500" />
                ) : (
                  <AlertCircle className="w-5 h-5 text-yellow-500" />
                )}
              </div>
              <div className="flex items-center justify-between">
                <span>Agents</span>
                <Badge variant="outline">{health?.claude?.agents}</Badge>
              </div>
              <div className="flex items-center justify-between">
                <span>Commands</span>
                <Badge variant="outline">{health?.claude?.commands}</Badge>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Memory Usage */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <HardDrive className="w-5 h-5" />
              Memory Usage
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <span>Used</span>
                <span className="font-mono text-sm">
                  {health?.memory?.used} MB
                </span>
              </div>
              <div className="flex items-center justify-between">
                <span>Total</span>
                <span className="font-mono text-sm">
                  {health?.memory?.total} MB
                </span>
              </div>
              <div className="mt-2">
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div 
                    className="bg-blue-600 h-2 rounded-full"
                    style={{ 
                      width: `${(health?.memory?.used / health?.memory?.total) * 100}%` 
                    }}
                  />
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Next.js Info */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Cpu className="w-5 h-5" />
              Next.js
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <span>Version</span>
                <span className="font-mono text-sm">{health?.nextjs?.version}</span>
              </div>
              <div className="flex items-center justify-between">
                <span>Turbopack</span>
                {health?.nextjs?.turbopack ? (
                  <CheckCircle2 className="w-5 h-5 text-green-500" />
                ) : (
                  <AlertCircle className="w-5 h-5 text-gray-400" />
                )}
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Quick Actions */}
        <Card className="md:col-span-2">
          <CardHeader>
            <CardTitle>Quick Actions</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex gap-4 flex-wrap">
              <Button onClick={() => window.location.reload()}>
                Refresh Dashboard
              </Button>
              <Button variant="outline" onClick={fetchHealth}>
                Update Status
              </Button>
              <Button variant="outline" asChild>
                <a href="/" target="_blank">Open App</a>
              </Button>
              <Button variant="outline" asChild>
                <a href="/lesson-design" target="_blank">Lesson Design</a>
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Last Updated */}
      <div className="mt-8 text-center text-sm text-muted-foreground">
        Last updated: {health?.timestamp ? new Date(health.timestamp).toLocaleString() : 'N/A'}
      </div>
    </div>
  );
}
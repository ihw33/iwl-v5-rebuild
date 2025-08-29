/**
 * Next.js App Router API Route
 * Health Check Endpoint
 */

import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

export const dynamic = 'force-dynamic'; // 항상 최신 상태 반환

export async function GET() {
  try {
    // Claude 설정 체크
    const claudePath = path.join(process.cwd(), '.claude');
    const hasClaudeSetup = fs.existsSync(claudePath);
    
    let agents = 0;
    let commands = 0;
    
    if (hasClaudeSetup) {
      const agentsPath = path.join(claudePath, 'agents');
      const commandsPath = path.join(claudePath, 'commands');
      
      if (fs.existsSync(agentsPath)) {
        agents = fs.readdirSync(agentsPath).filter(f => f.endsWith('.md')).length;
      }
      
      if (fs.existsSync(commandsPath)) {
        commands = fs.readdirSync(commandsPath).filter(f => f.endsWith('.md')).length;
      }
    }

    // 프로젝트 상태
    const status = {
      status: 'healthy',
      timestamp: new Date().toISOString(),
      environment: process.env.NODE_ENV,
      node: process.version,
      claude: {
        configured: hasClaudeSetup,
        agents,
        commands
      },
      nextjs: {
        version: '15.4.6',
        turbopack: true
      },
      memory: {
        used: Math.round(process.memoryUsage().heapUsed / 1024 / 1024),
        total: Math.round(process.memoryUsage().heapTotal / 1024 / 1024),
        unit: 'MB'
      }
    };

    return NextResponse.json(status, {
      status: 200,
      headers: {
        'Cache-Control': 'no-cache, no-store, must-revalidate',
      }
    });
  } catch (error) {
    return NextResponse.json(
      { 
        status: 'error', 
        message: error instanceof Error ? error.message : 'Unknown error'
      },
      { status: 500 }
    );
  }
}
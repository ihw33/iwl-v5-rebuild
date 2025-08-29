import { NextRequest, NextResponse } from 'next/server';
import { createVectorStore } from '@/lib/kb/vector-store';
import { KBSearchOptions } from '@/lib/kb/types';
import { withAuthenticatedAPI } from '@/lib/middleware';

export async function POST(req: NextRequest) {
  return withAuthenticatedAPI(req, async (req) => {
    const body = await req.json();
    const { query, limit, threshold, category, tags } = body;

    if (!query) {
      return NextResponse.json(
        { error: 'Query is required' },
        { status: 400 }
      );
    }

    const vectorStore = createVectorStore();
    
    const searchOptions: KBSearchOptions = {
      query,
      limit: limit || 10,
      threshold: threshold || 0.7,
      category,
      tags,
    };

    const results = await vectorStore.search(query, searchOptions);

    return NextResponse.json({
      success: true,
      query,
      results,
      count: results.length,
    });
  });
}

export async function GET(req: NextRequest) {
  return withAuthenticatedAPI(req, async (req) => {
    return NextResponse.json({
      message: 'Knowledge Base Search API',
      method: 'POST',
      endpoint: '/api/kb/search',
      payload: {
        query: 'search query (required)',
        limit: 'number of results (optional, default: 10)',
        threshold: 'similarity threshold (optional, default: 0.7)',
        category: 'filter by category (optional)',
        tags: 'filter by tags array (optional)',
      }
    });
  });
}
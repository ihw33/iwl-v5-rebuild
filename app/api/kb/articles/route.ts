import { NextRequest, NextResponse } from 'next/server';
import { createVectorStore } from '@/lib/kb/vector-store';
import { KBArticle } from '@/lib/kb/types';
import { v4 as uuidv4 } from 'uuid';
import { withAIAPI, withAuthenticatedAPI } from '@/lib/middleware';

// GET: Retrieve an article by ID
export async function GET(req: NextRequest) {
  return withAuthenticatedAPI(req, async (req) => {
    const { searchParams } = new URL(req.url);
    const id = searchParams.get('id');

    if (!id) {
      return NextResponse.json({
        message: 'Knowledge Base Articles API',
        endpoints: {
          'GET /api/kb/articles?id={id}': 'Get article by ID',
          'POST /api/kb/articles': 'Create new article',
          'PUT /api/kb/articles': 'Update article',
          'DELETE /api/kb/articles?id={id}': 'Delete article',
        }
      });
    }

    const vectorStore = createVectorStore();
    const article = await vectorStore.getById(id);

    if (!article) {
      return NextResponse.json(
        { error: 'Article not found' },
        { status: 404 }
      );
    }

    return NextResponse.json({
      success: true,
      article,
    });

  });
}

// POST: Create a new article
export async function POST(req: NextRequest) {
  return withAIAPI(req, true, async (req) => {
    const body = await req.json();
    const { title, content, category, tags, isPublished } = body;

    if (!title || !content) {
      return NextResponse.json(
        { error: 'Title and content are required' },
        { status: 400 }
      );
    }

    const article: KBArticle = {
      id: uuidv4(),
      title,
      content,
      category: category || 'general',
      tags: tags || [],
      createdAt: new Date(),
      updatedAt: new Date(),
      isPublished: isPublished ?? false,
    };

    const vectorStore = createVectorStore();
    await vectorStore.index(article);

    return NextResponse.json({
      success: true,
      article,
      message: 'Article created and indexed successfully',
    });

  });
}

// PUT: Update an existing article
export async function PUT(req: NextRequest) {
  return withAIAPI(req, true, async (req) => {
    const body = await req.json();
    const { id, ...updates } = body;

    if (!id) {
      return NextResponse.json(
        { error: 'Article ID is required' },
        { status: 400 }
      );
    }

    const vectorStore = createVectorStore();
    await vectorStore.update(id, updates);

    return NextResponse.json({
      success: true,
      message: 'Article updated successfully',
    });

  });
}

// DELETE: Delete an article
export async function DELETE(req: NextRequest) {
  return withAIAPI(req, true, async (req) => {
    const { searchParams } = new URL(req.url);
    const id = searchParams.get('id');

    if (!id) {
      return NextResponse.json(
        { error: 'Article ID is required' },
        { status: 400 }
      );
    }

    const vectorStore = createVectorStore();
    await vectorStore.delete(id);

    return NextResponse.json({
      success: true,
      message: 'Article deleted successfully',
    });

  });
}
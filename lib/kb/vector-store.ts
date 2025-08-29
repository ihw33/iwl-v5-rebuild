import { VectorStore, KBArticle, KBSearchOptions, KBSearchResult } from './types';
import { createEmbeddingService } from './embedding-service';
import { createClient } from '@supabase/supabase-js';
import { config, hasRealDatabase } from '@/lib/config/env';

// In-memory vector store for development
export class MemoryVectorStore implements VectorStore {
  private articles: Map<string, KBArticle> = new Map();
  private embeddings: Map<string, number[]> = new Map();
  private embeddingService = createEmbeddingService();

  async index(article: KBArticle): Promise<void> {
    // Generate embedding for the article
    const embedding = await this.embeddingService.generateEmbedding(
      `${article.title} ${article.content}`
    );
    
    this.articles.set(article.id, article);
    this.embeddings.set(article.id, embedding);
  }

  async search(query: string, options?: KBSearchOptions): Promise<KBSearchResult[]> {
    const limit = options?.limit || 10;
    const threshold = options?.threshold || 0.7;
    
    // Generate query embedding
    const queryEmbedding = await this.embeddingService.generateEmbedding(query);
    
    // Calculate similarity scores
    const results: KBSearchResult[] = [];
    
    for (const [id, article] of this.articles.entries()) {
      const embedding = this.embeddings.get(id);
      if (!embedding) continue;
      
      // Filter by category and tags if specified
      if (options?.category && article.category !== options.category) continue;
      if (options?.tags && !options.tags.some(tag => article.tags?.includes(tag))) continue;
      
      // Calculate cosine similarity
      const score = this.cosineSimilarity(queryEmbedding, embedding);
      
      if (score >= threshold) {
        results.push({
          article,
          score,
          highlights: this.extractHighlights(article.content, query),
        });
      }
    }
    
    // Sort by score and limit results
    return results
      .sort((a, b) => b.score - a.score)
      .slice(0, limit);
  }

  async update(id: string, article: Partial<KBArticle>): Promise<void> {
    const existing = this.articles.get(id);
    if (!existing) throw new Error('Article not found');
    
    const updated = { ...existing, ...article, updatedAt: new Date() };
    
    // Re-generate embedding if content changed
    if (article.title || article.content) {
      const embedding = await this.embeddingService.generateEmbedding(
        `${updated.title} ${updated.content}`
      );
      this.embeddings.set(id, embedding);
    }
    
    this.articles.set(id, updated);
  }

  async delete(id: string): Promise<void> {
    this.articles.delete(id);
    this.embeddings.delete(id);
  }

  async getById(id: string): Promise<KBArticle | null> {
    return this.articles.get(id) || null;
  }

  private cosineSimilarity(a: number[], b: number[]): number {
    let dotProduct = 0;
    let normA = 0;
    let normB = 0;
    
    for (let i = 0; i < a.length; i++) {
      dotProduct += a[i] * b[i];
      normA += a[i] * a[i];
      normB += b[i] * b[i];
    }
    
    return dotProduct / (Math.sqrt(normA) * Math.sqrt(normB));
  }

  private extractHighlights(content: string, query: string): string[] {
    const words = query.toLowerCase().split(' ');
    const sentences = content.split(/[.!?]+/);
    const highlights: string[] = [];
    
    for (const sentence of sentences) {
      const lowerSentence = sentence.toLowerCase();
      if (words.some(word => lowerSentence.includes(word))) {
        highlights.push(sentence.trim());
        if (highlights.length >= 3) break;
      }
    }
    
    return highlights;
  }
}

// Supabase vector store using pgvector
export class SupabaseVectorStore implements VectorStore {
  private supabase;
  private embeddingService = createEmbeddingService();

  constructor() {
    this.supabase = createClient(config.SUPABASE_URL, config.SUPABASE_SERVICE_ROLE_KEY);
  }

  async index(article: KBArticle): Promise<void> {
    const embedding = await this.embeddingService.generateEmbedding(
      `${article.title} ${article.content}`
    );

    const { error } = await this.supabase
      .from('kb_articles')
      .upsert({
        id: article.id,
        title: article.title,
        content: article.content,
        category: article.category,
        tags: article.tags,
        embedding,
        created_by: article.createdBy,
        is_published: article.isPublished,
      });

    if (error) throw error;
  }

  async search(query: string, options?: KBSearchOptions): Promise<KBSearchResult[]> {
    const embedding = await this.embeddingService.generateEmbedding(query);
    const limit = options?.limit || 10;
    const threshold = options?.threshold || 0.7;

    // Use Supabase RPC function for vector similarity search
    const { data, error } = await this.supabase
      .rpc('search_kb_articles', {
        query_embedding: embedding,
        match_threshold: threshold,
        match_count: limit,
        filter_category: options?.category,
        filter_tags: options?.tags,
      });

    if (error) throw error;

    return data.map((item: any) => ({
      article: {
        id: item.id,
        title: item.title,
        content: item.content,
        category: item.category,
        tags: item.tags,
        createdAt: new Date(item.created_at),
        updatedAt: new Date(item.updated_at),
        isPublished: item.is_published,
      },
      score: item.similarity,
      highlights: this.extractHighlights(item.content, query),
    }));
  }

  async update(id: string, article: Partial<KBArticle>): Promise<void> {
    let updateData: any = { ...article };
    
    if (article.title || article.content) {
      const { data: existing } = await this.supabase
        .from('kb_articles')
        .select('title, content')
        .eq('id', id)
        .single();
        
      if (!existing) {
        throw new Error('Article not found for update');
      }
        
      const title = article.title || existing.title;
      const content = article.content || existing.content;
      
      updateData.embedding = await this.embeddingService.generateEmbedding(
        `${title} ${content}`
      );
    }

    const { error } = await this.supabase
      .from('kb_articles')
      .update(updateData)
      .eq('id', id);

    if (error) throw error;
  }

  async delete(id: string): Promise<void> {
    const { error } = await this.supabase
      .from('kb_articles')
      .delete()
      .eq('id', id);

    if (error) throw error;
  }

  async getById(id: string): Promise<KBArticle | null> {
    const { data, error } = await this.supabase
      .from('kb_articles')
      .select('*')
      .eq('id', id)
      .single();

    if (error || !data) return null;

    return {
      id: data.id,
      title: data.title,
      content: data.content,
      category: data.category,
      tags: data.tags,
      createdAt: new Date(data.created_at),
      updatedAt: new Date(data.updated_at),
      isPublished: data.is_published,
      createdBy: data.created_by,
    };
  }

  private extractHighlights(content: string, query: string): string[] {
    const words = query.toLowerCase().split(' ');
    const sentences = content.split(/[.!?]+/);
    const highlights: string[] = [];
    
    for (const sentence of sentences) {
      const lowerSentence = sentence.toLowerCase();
      if (words.some(word => lowerSentence.includes(word))) {
        highlights.push(sentence.trim());
        if (highlights.length >= 3) break;
      }
    }
    
    return highlights;
  }
}

// Factory function
export function createVectorStore(): VectorStore {
  if (hasRealDatabase()) {
    return new SupabaseVectorStore();
  }
  
  return new MemoryVectorStore();
}
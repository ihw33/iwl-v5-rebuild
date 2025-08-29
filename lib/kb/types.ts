// Knowledge Base Types and Interfaces

export interface KBArticle {
  id: string;
  title: string;
  content: string;
  category?: string;
  tags?: string[];
  embedding?: number[];
  createdAt: Date;
  updatedAt: Date;
  createdBy?: string;
  isPublished: boolean;
  metadata?: Record<string, any>;
}

export interface KBSearchOptions {
  query: string;
  limit?: number;
  threshold?: number;
  category?: string;
  tags?: string[];
}

export interface KBSearchResult {
  article: KBArticle;
  score: number;
  highlights?: string[];
}

export interface VectorStore {
  index(article: KBArticle): Promise<void>;
  search(query: string, options?: KBSearchOptions): Promise<KBSearchResult[]>;
  update(id: string, article: Partial<KBArticle>): Promise<void>;
  delete(id: string): Promise<void>;
  getById(id: string): Promise<KBArticle | null>;
}

export interface EmbeddingService {
  generateEmbedding(text: string): Promise<number[]>;
  generateBatchEmbeddings(texts: string[]): Promise<number[][]>;
}

export interface ContentProcessor {
  extractText(content: string): string;
  extractMetadata(content: string): Record<string, any>;
  chunk(content: string, maxTokens?: number): string[];
  summarize(content: string): Promise<string>;
}
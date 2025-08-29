import OpenAI from 'openai';
import { EmbeddingService } from './types';

export class OpenAIEmbeddingService implements EmbeddingService {
  private client: OpenAI;
  private model: string = 'text-embedding-3-small';

  constructor(apiKey?: string) {
    this.client = new OpenAI({
      apiKey: apiKey || process.env.OPENAI_API_KEY,
    });
  }

  async generateEmbedding(text: string): Promise<number[]> {
    try {
      const response = await this.client.embeddings.create({
        input: text,
        model: this.model,
      });

      return response.data[0].embedding;
    } catch (error) {
      throw new Error('Failed to generate embedding');
    }
  }

  async generateBatchEmbeddings(texts: string[]): Promise<number[][]> {
    try {
      const response = await this.client.embeddings.create({
        input: texts,
        model: this.model,
      });

      return response.data.map(item => item.embedding);
    } catch (error) {
      throw new Error('Failed to generate batch embeddings');
    }
  }
}

// Mock embedding service for development/testing
export class MockEmbeddingService implements EmbeddingService {
  async generateEmbedding(text: string): Promise<number[]> {
    // Generate deterministic mock embedding based on text length
    const mockDimension = 1536; // OpenAI embedding dimension
    const embedding = new Array(mockDimension);
    
    for (let i = 0; i < mockDimension; i++) {
      embedding[i] = Math.sin(text.length * i) * 0.1;
    }
    
    return embedding;
  }

  async generateBatchEmbeddings(texts: string[]): Promise<number[][]> {
    return Promise.all(texts.map(text => this.generateEmbedding(text)));
  }
}

// Factory function to create appropriate service
export function createEmbeddingService(): EmbeddingService {
  const isDevelopment = process.env.NODE_ENV === 'development';
  const apiKey = process.env.OPENAI_API_KEY;
  const hasValidApiKey = apiKey && !apiKey.includes('dummy');
  
  if (!hasValidApiKey) {
    return new MockEmbeddingService();
  }
  
  return new OpenAIEmbeddingService();
}
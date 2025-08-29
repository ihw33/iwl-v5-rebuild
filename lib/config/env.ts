/**
 * Environment Configuration Management
 * Centralizes all environment variable access with type safety and validation
 */

export interface AppConfig {
  // Environment
  NODE_ENV: string;
  IS_PRODUCTION: boolean;
  IS_DEVELOPMENT: boolean;

  // App
  APP_URL: string;
  APP_NAME: string;
  APP_VERSION: string;
  DEBUG_MODE: boolean;

  // Supabase
  SUPABASE_URL: string;
  SUPABASE_ANON_KEY: string;
  SUPABASE_SERVICE_ROLE_KEY: string;

  // AI Services
  OPENAI_API_KEY: string;
  GOOGLE_AI_API_KEY: string;

  // Payment
  STRIPE_SECRET_KEY: string;
  STRIPE_PUBLISHABLE_KEY: string;
  STRIPE_WEBHOOK_SECRET: string;

  // Rate Limiting
  UPSTASH_REDIS_URL?: string;
  UPSTASH_REDIS_TOKEN?: string;
  RATE_LIMITING_ENABLED: boolean;

  // Security
  JWT_SECRET: string;
  API_SECRET: string;

  // Feature Flags
  AI_FEATURES_ENABLED: boolean;
  STRIPE_PAYMENTS_ENABLED: boolean;
  ANALYTICS_ENABLED: boolean;

  // Logging
  LOG_LEVEL: string;
}

class ConfigManager {
  private config: AppConfig;

  constructor() {
    this.config = this.loadConfig();
    this.validateConfig();
  }

  private loadConfig(): AppConfig {
    const env = process.env.NODE_ENV || 'development';
    const isDev = env === 'development';
    const isProd = env === 'production';

    return {
      // Environment
      NODE_ENV: env,
      IS_PRODUCTION: isProd,
      IS_DEVELOPMENT: isDev,

      // App
      APP_URL: process.env.NEXT_PUBLIC_APP_URL || 'http://localhost:3000',
      APP_NAME: process.env.NEXT_PUBLIC_APP_NAME || 'IWL v5',
      APP_VERSION: process.env.NEXT_PUBLIC_APP_VERSION || '5.0.0',
      DEBUG_MODE: process.env.NEXT_PUBLIC_DEBUG_MODE === 'true',

      // Supabase
      SUPABASE_URL: process.env.NEXT_PUBLIC_SUPABASE_URL || 'https://dummy.supabase.co',
      SUPABASE_ANON_KEY: process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || 'dummy-key',
      SUPABASE_SERVICE_ROLE_KEY: process.env.SUPABASE_SERVICE_ROLE_KEY || 'dummy-service-key',

      // AI Services
      OPENAI_API_KEY: process.env.OPENAI_API_KEY || '',
      GOOGLE_AI_API_KEY: process.env.GOOGLE_GENERATIVE_AI_API_KEY || '',

      // Payment
      STRIPE_SECRET_KEY: process.env.STRIPE_SECRET_KEY || '',
      STRIPE_PUBLISHABLE_KEY: process.env.NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY || '',
      STRIPE_WEBHOOK_SECRET: process.env.STRIPE_WEBHOOK_SECRET || '',

      // Rate Limiting
      UPSTASH_REDIS_URL: process.env.UPSTASH_REDIS_REST_URL,
      UPSTASH_REDIS_TOKEN: process.env.UPSTASH_REDIS_REST_TOKEN,
      RATE_LIMITING_ENABLED: !!(process.env.UPSTASH_REDIS_REST_URL && process.env.UPSTASH_REDIS_REST_TOKEN),

      // Security
      JWT_SECRET: process.env.JWT_SECRET || 'fallback-jwt-secret-not-secure',
      API_SECRET: process.env.API_SECRET || 'fallback-api-secret-not-secure',

      // Feature Flags
      AI_FEATURES_ENABLED: process.env.NEXT_PUBLIC_ENABLE_AI_FEATURES !== 'false',
      STRIPE_PAYMENTS_ENABLED: process.env.NEXT_PUBLIC_ENABLE_STRIPE_PAYMENTS === 'true',
      ANALYTICS_ENABLED: process.env.NEXT_PUBLIC_ENABLE_ANALYTICS === 'true',

      // Logging
      LOG_LEVEL: process.env.LOG_LEVEL || (isDev ? 'debug' : 'warn'),
    };
  }

  private validateConfig(): void {
    const warnings: string[] = [];
    const errors: string[] = [];

    // Skip validation during build time
    if (process.env.NEXT_PHASE === 'phase-production-build') {
      return;
    }

    // Check required production settings
    if (this.config.IS_PRODUCTION) {
      if (this.config.SUPABASE_URL.includes('dummy')) {
        errors.push('Production must have real Supabase URL');
      }
      if (this.config.JWT_SECRET.includes('fallback') || this.config.JWT_SECRET.length < 32) {
        errors.push('Production must have secure JWT_SECRET (minimum 32 characters)');
      }
      if (this.config.API_SECRET.includes('fallback') || this.config.API_SECRET.length < 32) {
        errors.push('Production must have secure API_SECRET (minimum 32 characters)');
      }
      if (this.config.STRIPE_PAYMENTS_ENABLED && !this.config.STRIPE_SECRET_KEY.startsWith('sk_live_')) {
        warnings.push('Stripe payments enabled but using test keys');
      }
    }

    // Check development warnings
    if (this.config.IS_DEVELOPMENT) {
      if (!this.config.SUPABASE_URL.includes('dummy') && this.config.DEBUG_MODE) {
        warnings.push('Using real Supabase in development with debug mode');
      }
    }

    // Log warnings and errors
    warnings.forEach(warning => {
      if (typeof window === 'undefined') {
        // Server-side logging (could integrate with proper logger)
      }
    });

    if (errors.length > 0) {
      throw new Error(`Configuration validation failed:\n${errors.join('\n')}`);
    }
  }

  public get(): AppConfig {
    return { ...this.config };
  }

  public isDummy(): boolean {
    return this.config.SUPABASE_URL.includes('dummy');
  }

  public isFeatureEnabled(feature: keyof Pick<AppConfig, 'AI_FEATURES_ENABLED' | 'STRIPE_PAYMENTS_ENABLED' | 'ANALYTICS_ENABLED'>): boolean {
    return this.config[feature];
  }
}

// Singleton instance
const configManager = new ConfigManager();

export const config = configManager.get();
export const isDummyMode = configManager.isDummy();
export const isFeatureEnabled = (feature: Parameters<ConfigManager['isFeatureEnabled']>[0]) => 
  configManager.isFeatureEnabled(feature);

// Helper functions for common checks
export const isProduction = () => config.IS_PRODUCTION;
export const isDevelopment = () => config.IS_DEVELOPMENT;
export const hasRealDatabase = () => !isDummyMode;
export const hasRateLimiting = () => config.RATE_LIMITING_ENABLED;
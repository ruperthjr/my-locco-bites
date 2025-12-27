"""Application settings."""

from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, validator


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    APP_NAME: str = Field(default="LocoBites", description="Application name")
    APP_VERSION: str = Field(default="1.0.0", description="Application version")
    ENVIRONMENT: str = Field(default="development", description="Environment name")
    DEBUG: bool = Field(default=True, description="Debug mode")
    LOG_LEVEL: str = Field(default="INFO", description="Logging level")
    TIMEZONE: str = Field(default="UTC", description="Application timezone")
    
    HOST: str = Field(default="0.0.0.0", description="Server host")
    PORT: int = Field(default=8000, description="Server port")
    RELOAD: bool = Field(default=True, description="Auto-reload on code changes")
    WORKERS: int = Field(default=4, description="Number of worker processes")
    
    SECRET_KEY: str = Field(..., description="Secret key for JWT encoding")
    ALGORITHM: str = Field(default="HS256", description="JWT algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, description="Access token expiration")
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(default=7, description="Refresh token expiration")
    
    DATABASE_URL: str = Field(..., description="Database connection URL")
    ASYNC_DATABASE_URL: str = Field(..., description="Async database connection URL")
    DB_POOL_SIZE: int = Field(default=5, description="Database connection pool size")
    DB_MAX_OVERFLOW: int = Field(default=10, description="Maximum overflow connections")
    DB_ECHO: bool = Field(default=False, description="Echo SQL statements")
    
    REDIS_URL: str = Field(default="redis://localhost:6379/0", description="Redis URL")
    REDIS_MAX_CONNECTIONS: int = Field(default=10, description="Redis max connections")
    
    MONGODB_URL: str = Field(default="mongodb://localhost:27017", description="MongoDB URL")
    MONGODB_DB_NAME: str = Field(default="locobites", description="MongoDB database name")
    MONGODB_MAX_POOL_SIZE: int = Field(default=10, description="MongoDB max pool size")
    MONGODB_MIN_POOL_SIZE: int = Field(default=1, description="MongoDB min pool size")
    
    CORS_ORIGINS: str = Field(default="*", description="Allowed CORS origins")
    CORS_CREDENTIALS: bool = Field(default=True, description="Allow credentials")
    CORS_METHODS: str = Field(default="*", description="Allowed methods")
    CORS_HEADERS: str = Field(default="*", description="Allowed headers")
    
    RATE_LIMIT_ENABLED: bool = Field(default=True, description="Enable rate limiting")
    RATE_LIMIT_PER_MINUTE: int = Field(default=60, description="Requests per minute")
    RATE_LIMIT_PER_HOUR: int = Field(default=1000, description="Requests per hour")
    
    CELERY_BROKER_URL: str = Field(default="redis://localhost:6379/1", description="Celery broker")
    CELERY_RESULT_BACKEND: str = Field(default="redis://localhost:6379/2", description="Celery backend")
    CELERY_TASK_TRACK_STARTED: bool = Field(default=True, description="Track task starts")
    CELERY_TASK_TIME_LIMIT: int = Field(default=300, description="Task time limit")
    
    STRIPE_SECRET_KEY: Optional[str] = Field(default=None, description="Stripe secret key")
    STRIPE_PUBLISHABLE_KEY: Optional[str] = Field(default=None, description="Stripe publishable key")
    STRIPE_WEBHOOK_SECRET: Optional[str] = Field(default=None, description="Stripe webhook secret")
    
    TWILIO_ACCOUNT_SID: Optional[str] = Field(default=None, description="Twilio account SID")
    TWILIO_AUTH_TOKEN: Optional[str] = Field(default=None, description="Twilio auth token")
    TWILIO_PHONE_NUMBER: Optional[str] = Field(default=None, description="Twilio phone number")
    
    SENDGRID_API_KEY: Optional[str] = Field(default=None, description="SendGrid API key")
    SENDGRID_FROM_EMAIL: str = Field(default="noreply@locobites.com", description="From email")
    SENDGRID_FROM_NAME: str = Field(default="LocoBites", description="From name")
    
    AWS_ACCESS_KEY_ID: Optional[str] = Field(default=None, description="AWS access key")
    AWS_SECRET_ACCESS_KEY: Optional[str] = Field(default=None, description="AWS secret key")
    AWS_REGION: str = Field(default="us-east-1", description="AWS region")
    AWS_S3_BUCKET: Optional[str] = Field(default=None, description="S3 bucket name")
    
    OPENAI_API_KEY: Optional[str] = Field(default=None, description="OpenAI API key")
    ANTHROPIC_API_KEY: Optional[str] = Field(default=None, description="Anthropic API key")
    
    SENTRY_DSN: Optional[str] = Field(default=None, description="Sentry DSN")
    SENTRY_ENVIRONMENT: str = Field(default="development", description="Sentry environment")
    SENTRY_TRACES_SAMPLE_RATE: float = Field(default=1.0, description="Sentry sample rate")
    
    MAX_UPLOAD_SIZE: int = Field(default=10485760, description="Max upload size in bytes")
    ALLOWED_EXTENSIONS: str = Field(default="jpg,jpeg,png,gif,pdf,webp", description="Allowed file extensions")
    
    FRONTEND_URL: str = Field(default="http://localhost:3000", description="Frontend URL")
    
    ADMIN_EMAIL: str = Field(default="admin@loccobites.com", description="Admin email")
    ADMIN_PASSWORD: str = Field(default="AdaaG2075", description="Admin password")
    
    ALLOWED_HOSTS: List[str] = Field(default=["*"], description="Allowed hosts for production")
    
    @validator("CORS_ORIGINS", pre=True)
    def parse_cors_origins(cls, v):
        """Parse CORS origins from string to list."""
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v
    
    @validator("ALLOWED_EXTENSIONS", pre=True)
    def parse_allowed_extensions(cls, v):
        """Parse allowed extensions from string to list."""
        if isinstance(v, str):
            return [ext.strip() for ext in v.split(",")]
        return v
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )


settings = Settings()
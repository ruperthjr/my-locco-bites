"""Database configuration."""

from typing import Dict, Any
from app.config.settings import settings


def get_database_config() -> Dict[str, Any]:
    """
    Get database configuration.
    
    Returns:
        Database configuration dictionary
    """
    return {
        "url": settings.DATABASE_URL,
        "async_url": settings.ASYNC_DATABASE_URL,
        "pool_size": settings.DB_POOL_SIZE,
        "max_overflow": settings.DB_MAX_OVERFLOW,
        "echo": settings.DB_ECHO,
        "pool_pre_ping": True,
        "pool_recycle": 3600,
        "connect_args": {
            "options": f"-c timezone={settings.TIMEZONE}",
            "connect_timeout": 10,
        }
    }


def get_redis_config() -> Dict[str, Any]:
    """
    Get Redis configuration.
    
    Returns:
        Redis configuration dictionary
    """
    return {
        "url": settings.REDIS_URL,
        "max_connections": settings.REDIS_MAX_CONNECTIONS,
        "encoding": "utf-8",
        "decode_responses": True,
        "socket_timeout": 5,
        "socket_connect_timeout": 5,
        "retry_on_timeout": True,
    }


def get_mongodb_config() -> Dict[str, Any]:
    """
    Get MongoDB configuration.
    
    Returns:
        MongoDB configuration dictionary
    """
    return {
        "url": settings.MONGODB_URL,
        "database": settings.MONGODB_DB_NAME,
        "max_pool_size": settings.MONGODB_MAX_POOL_SIZE,
        "min_pool_size": settings.MONGODB_MIN_POOL_SIZE,
        "server_selection_timeout_ms": 5000,
        "connect_timeout_ms": 5000,
        "socket_timeout_ms": 5000,
    }
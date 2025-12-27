"""Redis client for caching and session management."""

import json
import logging
from typing import Any, Optional, Union
import redis.asyncio as aioredis
from redis.asyncio import Redis
from app.config.settings import settings

logger = logging.getLogger(__name__)

redis_client: Optional[Redis] = None


async def init_redis() -> Redis:
    """
    Initialize Redis connection.
    
    Returns:
        Redis client instance
    """
    global redis_client
    try:
        redis_client = aioredis.from_url(
            settings.REDIS_URL,
            encoding="utf-8",
            decode_responses=True,
            max_connections=settings.REDIS_MAX_CONNECTIONS,
            socket_timeout=5,
            socket_connect_timeout=5,
            retry_on_timeout=True
        )
        await redis_client.ping()
        logger.info("Redis connection established")
        return redis_client
    except Exception as e:
        logger.error(f"Failed to connect to Redis: {str(e)}")
        raise


async def close_redis() -> None:
    """Close Redis connection."""
    global redis_client
    if redis_client:
        try:
            await redis_client.close()
            logger.info("Redis connection closed")
        except Exception as e:
            logger.error(f"Error closing Redis connection: {str(e)}")


async def get_redis() -> Redis:
    """
    Get Redis client instance.
    
    Returns:
        Redis client
    """
    global redis_client
    if redis_client is None:
        redis_client = await init_redis()
    return redis_client


async def cache_set(
    key: str,
    value: Any,
    ttl: Optional[int] = None,
    prefix: Optional[str] = None
) -> bool:
    """
    Set a value in Redis cache.
    
    Args:
        key: Cache key
        value: Value to cache (will be JSON serialized)
        ttl: Time to live in seconds
        prefix: Optional key prefix
    
    Returns:
        True if successful, False otherwise
    """
    try:
        client = await get_redis()
        full_key = f"{prefix}:{key}" if prefix else key
        
        if isinstance(value, (dict, list)):
            value = json.dumps(value)
        
        if ttl:
            await client.setex(full_key, ttl, value)
        else:
            await client.set(full_key, value)
        
        return True
    except Exception as e:
        logger.error(f"Error setting cache for key {key}: {str(e)}")
        return False


async def cache_get(
    key: str,
    prefix: Optional[str] = None,
    deserialize: bool = True
) -> Optional[Any]:
    """
    Get a value from Redis cache.
    
    Args:
        key: Cache key
        prefix: Optional key prefix
        deserialize: Whether to deserialize JSON
    
    Returns:
        Cached value or None if not found
    """
    try:
        client = await get_redis()
        full_key = f"{prefix}:{key}" if prefix else key
        value = await client.get(full_key)
        
        if value and deserialize:
            try:
                return json.loads(value)
            except (json.JSONDecodeError, TypeError):
                return value
        
        return value
    except Exception as e:
        logger.error(f"Error getting cache for key {key}: {str(e)}")
        return None


async def cache_delete(key: str, prefix: Optional[str] = None) -> bool:
    """
    Delete a key from Redis cache.
    
    Args:
        key: Cache key
        prefix: Optional key prefix
    
    Returns:
        True if successful, False otherwise
    """
    try:
        client = await get_redis()
        full_key = f"{prefix}:{key}" if prefix else key
        await client.delete(full_key)
        return True
    except Exception as e:
        logger.error(f"Error deleting cache for key {key}: {str(e)}")
        return False


async def cache_exists(key: str, prefix: Optional[str] = None) -> bool:
    """
    Check if a key exists in Redis cache.
    
    Args:
        key: Cache key
        prefix: Optional key prefix
    
    Returns:
        True if key exists, False otherwise
    """
    try:
        client = await get_redis()
        full_key = f"{prefix}:{key}" if prefix else key
        return await client.exists(full_key) > 0
    except Exception as e:
        logger.error(f"Error checking cache existence for key {key}: {str(e)}")
        return False


async def cache_clear_pattern(pattern: str) -> int:
    """
    Delete all keys matching a pattern.
    
    Args:
        pattern: Key pattern (e.g., 'products:*')
    
    Returns:
        Number of keys deleted
    """
    try:
        client = await get_redis()
        keys = []
        async for key in client.scan_iter(match=pattern):
            keys.append(key)
        
        if keys:
            return await client.delete(*keys)
        return 0
    except Exception as e:
        logger.error(f"Error clearing cache pattern {pattern}: {str(e)}")
        return 0


async def cache_increment(key: str, amount: int = 1, prefix: Optional[str] = None) -> int:
    """
    Increment a counter in Redis.
    
    Args:
        key: Cache key
        amount: Amount to increment by
        prefix: Optional key prefix
    
    Returns:
        New value after increment
    """
    try:
        client = await get_redis()
        full_key = f"{prefix}:{key}" if prefix else key
        return await client.incrby(full_key, amount)
    except Exception as e:
        logger.error(f"Error incrementing cache for key {key}: {str(e)}")
        return 0


async def cache_decrement(key: str, amount: int = 1, prefix: Optional[str] = None) -> int:
    """
    Decrement a counter in Redis.
    
    Args:
        key: Cache key
        amount: Amount to decrement by
        prefix: Optional key prefix
    
    Returns:
        New value after decrement
    """
    try:
        client = await get_redis()
        full_key = f"{prefix}:{key}" if prefix else key
        return await client.decrby(full_key, amount)
    except Exception as e:
        logger.error(f"Error decrementing cache for key {key}: {str(e)}")
        return 0


async def cache_get_ttl(key: str, prefix: Optional[str] = None) -> int:
    """
    Get time to live for a key.
    
    Args:
        key: Cache key
        prefix: Optional key prefix
    
    Returns:
        TTL in seconds, -1 if no expiry, -2 if key doesn't exist
    """
    try:
        client = await get_redis()
        full_key = f"{prefix}:{key}" if prefix else key
        return await client.ttl(full_key)
    except Exception as e:
        logger.error(f"Error getting TTL for key {key}: {str(e)}")
        return -2
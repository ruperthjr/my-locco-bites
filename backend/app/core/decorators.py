"""Custom decorators for the application."""

import functools
import time
import logging
from typing import Callable, Any
from app.core.exceptions import RateLimitException, UnauthorizedException

logger = logging.getLogger(__name__)


def timing_decorator(func: Callable) -> Callable:
    """
    Decorator to measure function execution time.
    
    Args:
        func: Function to measure
    
    Returns:
        Wrapped function that logs execution time
    """
    @functools.wraps(func)
    async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        try:
            result = await func(*args, **kwargs)
            return result
        finally:
            execution_time = time.time() - start_time
            logger.info(
                f"{func.__name__} executed in {execution_time:.4f} seconds",
                extra={
                    "function": func.__name__,
                    "execution_time": execution_time
                }
            )
    
    @functools.wraps(func)
    def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            execution_time = time.time() - start_time
            logger.info(
                f"{func.__name__} executed in {execution_time:.4f} seconds",
                extra={
                    "function": func.__name__,
                    "execution_time": execution_time
                }
            )
    
    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    return sync_wrapper


def cache_result(ttl: int = 300):
    """
    Decorator to cache function results.
    
    Args:
        ttl: Time to live in seconds
    
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        cache = {}
        cache_times = {}
        
        @functools.wraps(func)
        async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
            cache_key = str(args) + str(kwargs)
            current_time = time.time()
            
            if cache_key in cache:
                if current_time - cache_times[cache_key] < ttl:
                    logger.debug(f"Cache hit for {func.__name__}")
                    return cache[cache_key]
            
            result = await func(*args, **kwargs)
            cache[cache_key] = result
            cache_times[cache_key] = current_time
            return result
        
        @functools.wraps(func)
        def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
            cache_key = str(args) + str(kwargs)
            current_time = time.time()
            
            if cache_key in cache:
                if current_time - cache_times[cache_key] < ttl:
                    logger.debug(f"Cache hit for {func.__name__}")
                    return cache[cache_key]
            
            result = func(*args, **kwargs)
            cache[cache_key] = result
            cache_times[cache_key] = current_time
            return result
        
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper
    
    return decorator


def retry_on_failure(max_attempts: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """
    Decorator to retry function on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Initial delay between retries in seconds
        backoff: Multiplier for delay after each attempt
    
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        logger.warning(
                            f"Attempt {attempt + 1} failed for {func.__name__}: {str(e)}. "
                            f"Retrying in {current_delay}s..."
                        )
                        await asyncio.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        logger.error(
                            f"All {max_attempts} attempts failed for {func.__name__}"
                        )
            
            raise last_exception
        
        @functools.wraps(func)
        def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        logger.warning(
                            f"Attempt {attempt + 1} failed for {func.__name__}: {str(e)}. "
                            f"Retrying in {current_delay}s..."
                        )
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        logger.error(
                            f"All {max_attempts} attempts failed for {func.__name__}"
                        )
            
            raise last_exception
        
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper
    
    return decorator


def require_role(*allowed_roles: str):
    """
    Decorator to require specific user roles.
    
    Args:
        allowed_roles: Roles that are allowed to access the function
    
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
            current_user = kwargs.get("current_user")
            if not current_user:
                raise UnauthorizedException("Authentication required")
            
            if current_user.role not in allowed_roles:
                raise UnauthorizedException(
                    f"Role '{current_user.role}' not authorized. "
                    f"Required roles: {', '.join(allowed_roles)}"
                )
            
            return await func(*args, **kwargs)
        
        @functools.wraps(func)
        def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
            current_user = kwargs.get("current_user")
            if not current_user:
                raise UnauthorizedException("Authentication required")
            
            if current_user.role not in allowed_roles:
                raise UnauthorizedException(
                    f"Role '{current_user.role}' not authorized. "
                    f"Required roles: {', '.join(allowed_roles)}"
                )
            
            return func(*args, **kwargs)
        
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper
    
    return decorator


def log_execution(level: str = "INFO"):
    """
    Decorator to log function execution.
    
    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR)
    
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
            log_func = getattr(logger, level.lower())
            log_func(f"Executing {func.__name__}")
            try:
                result = await func(*args, **kwargs)
                log_func(f"Successfully executed {func.__name__}")
                return result
            except Exception as e:
                logger.error(f"Error in {func.__name__}: {str(e)}")
                raise
        
        @functools.wraps(func)
        def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
            log_func = getattr(logger, level.lower())
            log_func(f"Executing {func.__name__}")
            try:
                result = func(*args, **kwargs)
                log_func(f"Successfully executed {func.__name__}")
                return result
            except Exception as e:
                logger.error(f"Error in {func.__name__}: {str(e)}")
                raise
        
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper
    
    return decorator


import asyncio
"""CORS configuration."""

from typing import Dict, Any, List
from app.config.settings import settings


def get_cors_config() -> Dict[str, Any]:
    """
    Get CORS configuration.
    
    Returns:
        CORS configuration dictionary
    """
    origins = settings.CORS_ORIGINS
    
    if isinstance(origins, str):
        if origins == "*":
            origins = ["*"]
        else:
            origins = [origin.strip() for origin in origins.split(",")]
    
    methods = settings.CORS_METHODS
    if isinstance(methods, str):
        if methods == "*":
            methods = ["*"]
        else:
            methods = [method.strip() for method in methods.split(",")]
    
    headers = settings.CORS_HEADERS
    if isinstance(headers, str):
        if headers == "*":
            headers = ["*"]
        else:
            headers = [header.strip() for header in headers.split(",")]
    
    return {
        "origins": origins,
        "credentials": settings.CORS_CREDENTIALS,
        "methods": methods,
        "headers": headers,
    }


def is_origin_allowed(origin: str) -> bool:
    """
    Check if an origin is allowed.
    
    Args:
        origin: Origin URL to check
    
    Returns:
        True if origin is allowed, False otherwise
    """
    allowed_origins = settings.CORS_ORIGINS
    
    if isinstance(allowed_origins, str):
        if allowed_origins == "*":
            return True
        allowed_origins = [o.strip() for o in allowed_origins.split(",")]
    
    if "*" in allowed_origins:
        return True
    
    return origin in allowed_origins
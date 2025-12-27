"""Security configuration."""

from typing import Dict, Any
from app.config.settings import settings


def get_security_config() -> Dict[str, Any]:
    """
    Get security configuration.
    
    Returns:
        Security configuration dictionary
    """
    return {
        "secret_key": settings.SECRET_KEY,
        "algorithm": settings.ALGORITHM,
        "access_token_expire_minutes": settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        "refresh_token_expire_days": settings.REFRESH_TOKEN_EXPIRE_DAYS,
    }


def get_password_requirements() -> Dict[str, Any]:
    """
    Get password requirements.
    
    Returns:
        Password requirements dictionary
    """
    return {
        "min_length": 8,
        "max_length": 128,
        "require_uppercase": True,
        "require_lowercase": True,
        "require_digit": True,
        "require_special": True,
        "special_characters": "!@#$%^&*()_+-=[]{}|;:,.<>?",
    }


def get_rate_limit_config() -> Dict[str, Any]:
    """
    Get rate limit configuration.
    
    Returns:
        Rate limit configuration dictionary
    """
    return {
        "enabled": settings.RATE_LIMIT_ENABLED,
        "per_minute": settings.RATE_LIMIT_PER_MINUTE,
        "per_hour": settings.RATE_LIMIT_PER_HOUR,
        "key_prefix": "rate_limit",
    }


class SecurityHeaders:
    """Security headers for HTTP responses."""
    
    @staticmethod
    def get_headers() -> Dict[str, str]:
        """Get security headers."""
        return {
            "X-Content-Type-Options": "nosniff",
            "X-Frame-Options": "DENY",
            "X-XSS-Protection": "1; mode=block",
            "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
            "Content-Security-Policy": (
                "default-src 'self'; "
                "script-src 'self' 'unsafe-inline' 'unsafe-eval'; "
                "style-src 'self' 'unsafe-inline'; "
                "img-src 'self' data: https:; "
                "font-src 'self' data:; "
                "connect-src 'self';"
            ),
            "Referrer-Policy": "strict-origin-when-cross-origin",
            "Permissions-Policy": (
                "geolocation=(), microphone=(), camera=()"
            ),
        }
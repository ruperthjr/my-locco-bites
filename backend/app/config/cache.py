"""Cache configuration."""

from typing import Dict, Any
from app.config.settings import settings


def get_cache_config() -> Dict[str, Any]:
    """
    Get cache configuration.
    
    Returns:
        Cache configuration dictionary
    """
    return {
        "url": settings.REDIS_URL,
        "max_connections": settings.REDIS_MAX_CONNECTIONS,
        "default_ttl": 300,
        "key_prefix": f"{settings.APP_NAME.lower()}:",
    }


class CacheTTL:
    """Cache TTL constants in seconds."""
    
    MINUTE = 60
    FIVE_MINUTES = 300
    TEN_MINUTES = 600
    THIRTY_MINUTES = 1800
    HOUR = 3600
    SIX_HOURS = 21600
    TWELVE_HOURS = 43200
    DAY = 86400
    WEEK = 604800
    MONTH = 2592000


class CacheKeys:
    """Cache key prefixes."""
    
    PRODUCT = "product"
    CATEGORY = "category"
    ORDER = "order"
    CUSTOMER = "customer"
    CART = "cart"
    SESSION = "session"
    MENU = "menu"
    FEATURED = "featured"
    BESTSELLERS = "bestsellers"
    RECOMMENDATIONS = "recommendations"
    SEARCH = "search"
    SETTINGS = "settings"
    
    @staticmethod
    def product_detail(product_id: int) -> str:
        """Get product detail cache key."""
        return f"{CacheKeys.PRODUCT}:detail:{product_id}"
    
    @staticmethod
    def product_list(page: int = 1, limit: int = 20) -> str:
        """Get product list cache key."""
        return f"{CacheKeys.PRODUCT}:list:{page}:{limit}"
    
    @staticmethod
    def category_products(category_id: int, page: int = 1) -> str:
        """Get category products cache key."""
        return f"{CacheKeys.CATEGORY}:{category_id}:products:{page}"
    
    @staticmethod
    def cart(customer_id: int) -> str:
        """Get cart cache key."""
        return f"{CacheKeys.CART}:{customer_id}"
    
    @staticmethod
    def customer_orders(customer_id: int) -> str:
        """Get customer orders cache key."""
        return f"{CacheKeys.CUSTOMER}:{customer_id}:orders"
    
    @staticmethod
    def search_results(query: str, page: int = 1) -> str:
        """Get search results cache key."""
        import hashlib
        query_hash = hashlib.md5(query.encode()).hexdigest()
        return f"{CacheKeys.SEARCH}:{query_hash}:{page}"
"""Application constants."""


class OrderStatus:
    """Order status constants."""
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PREPARING = "preparing"
    READY = "ready"
    OUT_FOR_DELIVERY = "out_for_delivery"
    DELIVERED = "delivered"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"
    
    ALL = [
        PENDING, CONFIRMED, PREPARING, READY,
        OUT_FOR_DELIVERY, DELIVERED, COMPLETED,
        CANCELLED, REFUNDED
    ]


class PaymentStatus:
    """Payment status constants."""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"
    PARTIALLY_REFUNDED = "partially_refunded"
    CANCELLED = "cancelled"
    
    ALL = [
        PENDING, PROCESSING, COMPLETED, FAILED,
        REFUNDED, PARTIALLY_REFUNDED, CANCELLED
    ]


class DeliveryMethod:
    """Delivery method constants."""
    PICKUP = "pickup"
    DELIVERY = "delivery"
    DINE_IN = "dine_in"
    
    ALL = [PICKUP, DELIVERY, DINE_IN]


class UserRole:
    """User role constants."""
    CUSTOMER = "customer"
    ADMIN = "admin"
    MANAGER = "manager"
    STAFF = "staff"
    DRIVER = "driver"
    SUPER_ADMIN = "super_admin"
    
    ALL = [CUSTOMER, ADMIN, MANAGER, STAFF, DRIVER, SUPER_ADMIN]


class ProductStatus:
    """Product status constants."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    OUT_OF_STOCK = "out_of_stock"
    DISCONTINUED = "discontinued"
    DRAFT = "draft"
    
    ALL = [ACTIVE, INACTIVE, OUT_OF_STOCK, DISCONTINUED, DRAFT]


class SubscriptionStatus:
    """Subscription status constants."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    PAUSED = "paused"
    CANCELLED = "cancelled"
    EXPIRED = "expired"
    TRIAL = "trial"
    
    ALL = [ACTIVE, INACTIVE, PAUSED, CANCELLED, EXPIRED, TRIAL]


class NotificationChannel:
    """Notification channel constants."""
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"
    IN_APP = "in_app"
    WEBHOOK = "webhook"
    
    ALL = [EMAIL, SMS, PUSH, IN_APP, WEBHOOK]


class CouponType:
    """Coupon type constants."""
    PERCENTAGE = "percentage"
    FIXED_AMOUNT = "fixed_amount"
    FREE_SHIPPING = "free_shipping"
    BUY_X_GET_Y = "buy_x_get_y"
    
    ALL = [PERCENTAGE, FIXED_AMOUNT, FREE_SHIPPING, BUY_X_GET_Y]


class LoyaltyTier:
    """Loyalty tier constants."""
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"
    PLATINUM = "platinum"
    DIAMOND = "diamond"
    
    ALL = [BRONZE, SILVER, GOLD, PLATINUM, DIAMOND]


class PaymentMethod:
    """Payment method constants."""
    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"
    CASH = "cash"
    MOBILE_MONEY = "mobile_money"
    BANK_TRANSFER = "bank_transfer"
    DIGITAL_WALLET = "digital_wallet"
    
    ALL = [
        CREDIT_CARD, DEBIT_CARD, CASH,
        MOBILE_MONEY, BANK_TRANSFER, DIGITAL_WALLET
    ]


class InventoryAction:
    """Inventory action constants."""
    INCREASE = "increase"
    DECREASE = "decrease"
    RESTOCK = "restock"
    WASTE = "waste"
    ADJUSTMENT = "adjustment"
    RESERVED = "reserved"
    RELEASED = "released"
    
    ALL = [
        INCREASE, DECREASE, RESTOCK,
        WASTE, ADJUSTMENT, RESERVED, RELEASED
    ]


class FileUploadType:
    """File upload type constants."""
    PRODUCT_IMAGE = "product_image"
    CATEGORY_IMAGE = "category_image"
    USER_AVATAR = "user_avatar"
    DOCUMENT = "document"
    INVOICE = "invoice"
    RECEIPT = "receipt"
    
    ALL = [
        PRODUCT_IMAGE, CATEGORY_IMAGE, USER_AVATAR,
        DOCUMENT, INVOICE, RECEIPT
    ]


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


class QueueNames:
    """Queue names for Celery tasks."""
    DEFAULT = "default"
    HIGH_PRIORITY = "high_priority"
    LOW_PRIORITY = "low_priority"
    EMAIL = "email"
    SMS = "sms"
    NOTIFICATIONS = "notifications"
    AI_PROCESSING = "ai_processing"
    REPORTS = "reports"


class DateFormats:
    """Date format constants."""
    DATE = "%Y-%m-%d"
    DATETIME = "%Y-%m-%d %H:%M:%S"
    TIME = "%H:%M:%S"
    ISO8601 = "%Y-%m-%dT%H:%M:%S.%fZ"
    HUMAN_READABLE = "%B %d, %Y at %I:%M %p"


class Pagination:
    """Pagination constants."""
    DEFAULT_PAGE = 1
    DEFAULT_PAGE_SIZE = 20
    MAX_PAGE_SIZE = 100


class ApiVersions:
    """API version constants."""
    V1 = "v1"
    CURRENT = V1


class HTTPHeaders:
    """Custom HTTP header names."""
    REQUEST_ID = "X-Request-ID"
    API_KEY = "X-API-Key"
    CLIENT_VERSION = "X-Client-Version"
    RATE_LIMIT_REMAINING = "X-RateLimit-Remaining"
    RATE_LIMIT_RESET = "X-RateLimit-Reset"
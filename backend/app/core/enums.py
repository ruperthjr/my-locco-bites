"""Application enums."""

from enum import Enum


class DietaryType(str, Enum):
    """Dietary restriction types."""
    VEGAN = "vegan"
    VEGETARIAN = "vegetarian"
    GLUTEN_FREE = "gluten_free"
    DAIRY_FREE = "dairy_free"
    NUT_FREE = "nut_free"
    KETO = "keto"
    PALEO = "paleo"
    HALAL = "halal"
    KOSHER = "kosher"
    LOW_CARB = "low_carb"
    LOW_FAT = "low_fat"
    SUGAR_FREE = "sugar_free"
    ORGANIC = "organic"


class AllergenType(str, Enum):
    """Allergen types."""
    MILK = "milk"
    EGGS = "eggs"
    FISH = "fish"
    SHELLFISH = "shellfish"
    TREE_NUTS = "tree_nuts"
    PEANUTS = "peanuts"
    WHEAT = "wheat"
    SOYBEANS = "soybeans"
    SESAME = "sesame"
    MUSTARD = "mustard"
    CELERY = "celery"
    LUPIN = "lupin"
    SULPHITES = "sulphites"
    MOLLUSCS = "molluscs"


class OrderPriority(str, Enum):
    """Order priority levels."""
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    URGENT = "urgent"


class NotificationType(str, Enum):
    """Notification types."""
    ORDER_CONFIRMATION = "order_confirmation"
    ORDER_STATUS_UPDATE = "order_status_update"
    PAYMENT_SUCCESS = "payment_success"
    PAYMENT_FAILED = "payment_failed"
    DELIVERY_UPDATE = "delivery_update"
    LOYALTY_REWARD = "loyalty_reward"
    PROMOTIONAL = "promotional"
    SYSTEM_ALERT = "system_alert"
    PASSWORD_RESET = "password_reset"
    ACCOUNT_UPDATE = "account_update"
    SUBSCRIPTION_RENEWAL = "subscription_renewal"
    NEW_MESSAGE = "new_message"


class TransactionType(str, Enum):
    """Transaction types."""
    CHARGE = "charge"
    REFUND = "refund"
    ADJUSTMENT = "adjustment"
    VOID = "void"
    CAPTURE = "capture"
    AUTHORIZATION = "authorization"


class ReviewStatus(str, Enum):
    """Review status."""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    FLAGGED = "flagged"


class WeekDay(str, Enum):
    """Days of the week."""
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"


class TimeSlot(str, Enum):
    """Time slot categories."""
    BREAKFAST = "breakfast"
    BRUNCH = "brunch"
    LUNCH = "lunch"
    AFTERNOON = "afternoon"
    DINNER = "dinner"
    LATE_NIGHT = "late_night"


class PromotionType(str, Enum):
    """Promotion types."""
    DISCOUNT = "discount"
    BOGO = "bogo"
    BUNDLE = "bundle"
    FLASH_SALE = "flash_sale"
    SEASONAL = "seasonal"
    HAPPY_HOUR = "happy_hour"


class ProductCategory(str, Enum):
    """Main product categories."""
    BREAD = "bread"
    PASTRIES = "pastries"
    CAKES = "cakes"
    COOKIES = "cookies"
    PIZZAS = "pizzas"
    SANDWICHES = "sandwiches"
    COFFEE = "coffee"
    TEA = "tea"
    SMOOTHIES = "smoothies"
    JUICES = "juices"
    MILKSHAKES = "milkshakes"
    ICED_DRINKS = "iced_drinks"
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DESSERTS = "desserts"
    GLUTEN_FREE = "gluten_free"
    SEASONAL = "seasonal"


class CakeShape(str, Enum):
    """Cake shapes for customization."""
    ROUND = "round"
    SQUARE = "square"
    RECTANGLE = "rectangle"
    HEART = "heart"
    CUSTOM = "custom"


class CakeSize(str, Enum):
    """Cake sizes."""
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    EXTRA_LARGE = "extra_large"


class CoffeSize(str, Enum):
    """Coffee sizes."""
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    EXTRA_LARGE = "extra_large"


class MilkType(str, Enum):
    """Milk types for beverages."""
    WHOLE = "whole"
    SKIM = "skim"
    ALMOND = "almond"
    SOY = "soy"
    OAT = "oat"
    COCONUT = "coconut"
    LACTOSE_FREE = "lactose_free"


class PizzaCrust(str, Enum):
    """Pizza crust types."""
    THIN = "thin"
    REGULAR = "regular"
    THICK = "thick"
    STUFFED = "stuffed"
    GLUTEN_FREE = "gluten_free"


class AnalyticsMetric(str, Enum):
    """Analytics metrics."""
    PAGE_VIEW = "page_view"
    PRODUCT_VIEW = "product_view"
    ADD_TO_CART = "add_to_cart"
    REMOVE_FROM_CART = "remove_from_cart"
    CHECKOUT_START = "checkout_start"
    PURCHASE = "purchase"
    SEARCH = "search"
    CLICK = "click"
    IMPRESSION = "impression"


class WebSocketEvent(str, Enum):
    """WebSocket event types."""
    ORDER_UPDATE = "order_update"
    NOTIFICATION = "notification"
    CHAT_MESSAGE = "chat_message"
    KITCHEN_UPDATE = "kitchen_update"
    INVENTORY_UPDATE = "inventory_update"
    DRIVER_LOCATION = "driver_location"
    SYSTEM_MESSAGE = "system_message"


class AIIntentType(str, Enum):
    """AI chatbot intent types."""
    GREETING = "greeting"
    PRODUCT_INQUIRY = "product_inquiry"
    ORDER_PLACEMENT = "order_placement"
    ORDER_STATUS = "order_status"
    MENU_NAVIGATION = "menu_navigation"
    RECOMMENDATION_REQUEST = "recommendation_request"
    COMPLAINT = "complaint"
    FEEDBACK = "feedback"
    GENERAL_QUESTION = "general_question"
    STORE_LOCATION = "store_location"
    HOURS_INQUIRY = "hours_inquiry"
    GOODBYE = "goodbye"
"""Custom exceptions for the application."""

from typing import Any, Optional


class LocoBitesException(Exception):
    """Base exception for all LocoBites exceptions."""
    
    def __init__(
        self,
        message: str,
        status_code: int = 500,
        details: Optional[dict[str, Any]] = None
    ):
        self.message = message
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)


class ValidationException(LocoBitesException):
    """Exception raised for validation errors."""
    
    def __init__(self, message: str = "Validation error", details: Optional[dict[str, Any]] = None):
        super().__init__(message=message, status_code=422, details=details)


class NotFoundException(LocoBitesException):
    """Exception raised when a resource is not found."""
    
    def __init__(self, message: str = "Resource not found", details: Optional[dict[str, Any]] = None):
        super().__init__(message=message, status_code=404, details=details)


class UnauthorizedException(LocoBitesException):
    """Exception raised for unauthorized access attempts."""
    
    def __init__(self, message: str = "Unauthorized", details: Optional[dict[str, Any]] = None):
        super().__init__(message=message, status_code=401, details=details)


class ForbiddenException(LocoBitesException):
    """Exception raised when access is forbidden."""
    
    def __init__(self, message: str = "Forbidden", details: Optional[dict[str, Any]] = None):
        super().__init__(message=message, status_code=403, details=details)


class ConflictException(LocoBitesException):
    """Exception raised for resource conflicts."""
    
    def __init__(self, message: str = "Resource conflict", details: Optional[dict[str, Any]] = None):
        super().__init__(message=message, status_code=409, details=details)


class BadRequestException(LocoBitesException):
    """Exception raised for bad requests."""
    
    def __init__(self, message: str = "Bad request", details: Optional[dict[str, Any]] = None):
        super().__init__(message=message, status_code=400, details=details)


class ServiceUnavailableException(LocoBitesException):
    """Exception raised when a service is unavailable."""
    
    def __init__(self, message: str = "Service unavailable", details: Optional[dict[str, Any]] = None):
        super().__init__(message=message, status_code=503, details=details)


class RateLimitException(LocoBitesException):
    """Exception raised when rate limit is exceeded."""
    
    def __init__(self, message: str = "Rate limit exceeded", details: Optional[dict[str, Any]] = None):
        super().__init__(message=message, status_code=429, details=details)


class PaymentException(LocoBitesException):
    """Exception raised for payment processing errors."""
    
    def __init__(self, message: str = "Payment processing failed", details: Optional[dict[str, Any]] = None):
        super().__init__(message=message, status_code=402, details=details)


class InventoryException(LocoBitesException):
    """Exception raised for inventory-related errors."""
    
    def __init__(self, message: str = "Inventory error", details: Optional[dict[str, Any]] = None):
        super().__init__(message=message, status_code=409, details=details)


class DeliveryException(LocoBitesException):
    """Exception raised for delivery-related errors."""
    
    def __init__(self, message: str = "Delivery error", details: Optional[dict[str, Any]] = None):
        super().__init__(message=message, status_code=400, details=details)


class AIServiceException(LocoBitesException):
    """Exception raised for AI service errors."""
    
    def __init__(self, message: str = "AI service error", details: Optional[dict[str, Any]] = None):
        super().__init__(message=message, status_code=503, details=details)


class WebSocketException(LocoBitesException):
    """Exception raised for WebSocket errors."""
    
    def __init__(self, message: str = "WebSocket error", details: Optional[dict[str, Any]] = None):
        super().__init__(message=message, status_code=500, details=details)
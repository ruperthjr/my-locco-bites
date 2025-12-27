"""Celery configuration."""

from typing import Dict, Any
from kombu import Exchange, Queue
from app.config.settings import settings


def get_celery_config() -> Dict[str, Any]:
    """
    Get Celery configuration.
    
    Returns:
        Celery configuration dictionary
    """
    return {
        "broker_url": settings.CELERY_BROKER_URL,
        "result_backend": settings.CELERY_RESULT_BACKEND,
        "task_serializer": "json",
        "result_serializer": "json",
        "accept_content": ["json"],
        "timezone": settings.TIMEZONE,
        "enable_utc": True,
        "task_track_started": settings.CELERY_TASK_TRACK_STARTED,
        "task_time_limit": settings.CELERY_TASK_TIME_LIMIT,
        "task_soft_time_limit": settings.CELERY_TASK_TIME_LIMIT - 10,
        "worker_prefetch_multiplier": 4,
        "worker_max_tasks_per_child": 1000,
        "task_acks_late": True,
        "task_reject_on_worker_lost": True,
        "task_default_queue": "default",
        "task_default_exchange": "default",
        "task_default_routing_key": "default",
        "task_queues": (
            Queue("default", Exchange("default"), routing_key="default"),
            Queue("high_priority", Exchange("high_priority"), routing_key="high_priority"),
            Queue("low_priority", Exchange("low_priority"), routing_key="low_priority"),
            Queue("email", Exchange("email"), routing_key="email"),
            Queue("sms", Exchange("sms"), routing_key="sms"),
            Queue("notifications", Exchange("notifications"), routing_key="notifications"),
            Queue("ai_processing", Exchange("ai_processing"), routing_key="ai_processing"),
            Queue("reports", Exchange("reports"), routing_key="reports"),
        ),
        "task_routes": {
            "app.tasks.email_tasks.*": {"queue": "email"},
            "app.tasks.sms_tasks.*": {"queue": "sms"},
            "app.tasks.notification_tasks.*": {"queue": "notifications"},
            "app.tasks.ai_training_tasks.*": {"queue": "ai_processing"},
            "app.tasks.report_tasks.*": {"queue": "reports"},
        },
        "beat_schedule": {},
        "result_expires": 3600,
        "result_persistent": True,
        "task_ignore_result": False,
        "worker_send_task_events": True,
        "task_send_sent_event": True,
    }


class TaskPriority:
    """Task priority levels."""
    
    LOW = 0
    NORMAL = 5
    HIGH = 9
    CRITICAL = 10


class TaskQueues:
    """Task queue names."""
    
    DEFAULT = "default"
    HIGH_PRIORITY = "high_priority"
    LOW_PRIORITY = "low_priority"
    EMAIL = "email"
    SMS = "sms"
    NOTIFICATIONS = "notifications"
    AI_PROCESSING = "ai_processing"
    REPORTS = "reports"
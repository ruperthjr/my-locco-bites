"""Logging configuration."""

import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from app.config.settings import settings


def setup_logging() -> None:
    """Configure application logging."""
    
    log_format = (
        "%(asctime)s - %(name)s - %(levelname)s - "
        "[%(filename)s:%(lineno)d] - %(message)s"
    )
    
    log_level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)
    
    logging.basicConfig(
        level=log_level,
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout),
        ]
    )
    
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    
    app_log_file = logs_dir / "app" / "app.log"
    app_log_file.parent.mkdir(exist_ok=True)
    
    file_handler = RotatingFileHandler(
        app_log_file,
        maxBytes=10 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8"
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(logging.Formatter(log_format))
    
    error_log_file = logs_dir / "error" / "error.log"
    error_log_file.parent.mkdir(exist_ok=True)
    
    error_handler = RotatingFileHandler(
        error_log_file,
        maxBytes=10 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8"
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter(log_format))
    
    root_logger = logging.getLogger()
    root_logger.addHandler(file_handler)
    root_logger.addHandler(error_handler)
    
    logging.getLogger("uvicorn").setLevel(log_level)
    logging.getLogger("uvicorn.access").setLevel(log_level)
    logging.getLogger("uvicorn.error").setLevel(log_level)
    
    logging.getLogger("sqlalchemy.engine").setLevel(
        logging.INFO if settings.DB_ECHO else logging.WARNING
    )
    
    if settings.ENVIRONMENT == "production":
        try:
            import sentry_sdk
            from sentry_sdk.integrations.fastapi import FastApiIntegration
            from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
            
            if settings.SENTRY_DSN:
                sentry_sdk.init(
                    dsn=settings.SENTRY_DSN,
                    environment=settings.SENTRY_ENVIRONMENT,
                    traces_sample_rate=settings.SENTRY_TRACES_SAMPLE_RATE,
                    integrations=[
                        FastApiIntegration(),
                        SqlalchemyIntegration(),
                    ],
                )
                logging.info("Sentry integration initialized")
        except ImportError:
            logging.warning("Sentry SDK not installed")
    
    logging.info(f"Logging configured at {log_level} level")


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance.
    
    Args:
        name: Logger name (usually __name__)
    
    Returns:
        Configured logger instance
    """
    return logging.getLogger(name)
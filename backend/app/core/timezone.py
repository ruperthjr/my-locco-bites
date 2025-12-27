"""Timezone utilities."""

from datetime import datetime, timezone, timedelta
from typing import Optional
import pytz
from app.config.settings import settings


def get_utc_now() -> datetime:
    """Get current UTC datetime."""
    return datetime.now(timezone.utc)


def get_local_now(tz: Optional[str] = None) -> datetime:
    """
    Get current datetime in local timezone.
    
    Args:
        tz: Timezone string (e.g., 'America/New_York'). 
            Uses settings.TIMEZONE if not provided.
    
    Returns:
        Current datetime in specified timezone
    """
    target_tz = tz or settings.TIMEZONE
    local_tz = pytz.timezone(target_tz)
    return datetime.now(local_tz)


def convert_to_utc(dt: datetime, from_tz: Optional[str] = None) -> datetime:
    """
    Convert datetime to UTC.
    
    Args:
        dt: Datetime to convert
        from_tz: Source timezone. Uses settings.TIMEZONE if not provided.
    
    Returns:
        Datetime in UTC
    """
    if dt.tzinfo is None:
        source_tz = pytz.timezone(from_tz or settings.TIMEZONE)
        dt = source_tz.localize(dt)
    return dt.astimezone(timezone.utc)


def convert_from_utc(dt: datetime, to_tz: Optional[str] = None) -> datetime:
    """
    Convert UTC datetime to local timezone.
    
    Args:
        dt: UTC datetime to convert
        to_tz: Target timezone. Uses settings.TIMEZONE if not provided.
    
    Returns:
        Datetime in target timezone
    """
    target_tz = pytz.timezone(to_tz or settings.TIMEZONE)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(target_tz)


def localize_datetime(dt: datetime, tz: Optional[str] = None) -> datetime:
    """
    Add timezone info to naive datetime.
    
    Args:
        dt: Naive datetime
        tz: Timezone to apply. Uses settings.TIMEZONE if not provided.
    
    Returns:
        Timezone-aware datetime
    """
    if dt.tzinfo is not None:
        return dt
    target_tz = pytz.timezone(tz or settings.TIMEZONE)
    return target_tz.localize(dt)


def is_business_hours(
    dt: Optional[datetime] = None,
    open_hour: int = 6,
    close_hour: int = 22,
    tz: Optional[str] = None
) -> bool:
    """
    Check if given datetime is within business hours.
    
    Args:
        dt: Datetime to check. Uses current time if not provided.
        open_hour: Opening hour (24-hour format)
        close_hour: Closing hour (24-hour format)
        tz: Timezone. Uses settings.TIMEZONE if not provided.
    
    Returns:
        True if within business hours, False otherwise
    """
    if dt is None:
        dt = get_local_now(tz)
    elif dt.tzinfo is None:
        dt = localize_datetime(dt, tz)
    else:
        target_tz = pytz.timezone(tz or settings.TIMEZONE)
        dt = dt.astimezone(target_tz)
    
    return open_hour <= dt.hour < close_hour


def get_time_until(target_dt: datetime, from_dt: Optional[datetime] = None) -> timedelta:
    """
    Calculate time remaining until target datetime.
    
    Args:
        target_dt: Target datetime
        from_dt: Starting datetime. Uses current time if not provided.
    
    Returns:
        Time difference as timedelta
    """
    if from_dt is None:
        from_dt = get_utc_now()
    
    if target_dt.tzinfo is None:
        target_dt = localize_datetime(target_dt)
    if from_dt.tzinfo is None:
        from_dt = localize_datetime(from_dt)
    
    target_dt_utc = convert_to_utc(target_dt)
    from_dt_utc = convert_to_utc(from_dt)
    
    return target_dt_utc - from_dt_utc


def format_datetime(
    dt: datetime,
    format_str: str = "%Y-%m-%d %H:%M:%S",
    to_tz: Optional[str] = None
) -> str:
    """
    Format datetime as string.
    
    Args:
        dt: Datetime to format
        format_str: Format string
        to_tz: Convert to this timezone before formatting
    
    Returns:
        Formatted datetime string
    """
    if to_tz:
        dt = convert_from_utc(dt, to_tz)
    return dt.strftime(format_str)


def parse_datetime(
    dt_str: str,
    format_str: str = "%Y-%m-%d %H:%M:%S",
    tz: Optional[str] = None
) -> datetime:
    """
    Parse datetime string.
    
    Args:
        dt_str: Datetime string to parse
        format_str: Format string
        tz: Timezone to apply. Uses settings.TIMEZONE if not provided.
    
    Returns:
        Parsed datetime with timezone
    """
    dt = datetime.strptime(dt_str, format_str)
    return localize_datetime(dt, tz)


def get_start_of_day(dt: Optional[datetime] = None, tz: Optional[str] = None) -> datetime:
    """
    Get start of day (00:00:00) for given datetime.
    
    Args:
        dt: Reference datetime. Uses current time if not provided.
        tz: Timezone. Uses settings.TIMEZONE if not provided.
    
    Returns:
        Datetime at start of day
    """
    if dt is None:
        dt = get_local_now(tz)
    elif dt.tzinfo is None:
        dt = localize_datetime(dt, tz)
    
    return dt.replace(hour=0, minute=0, second=0, microsecond=0)


def get_end_of_day(dt: Optional[datetime] = None, tz: Optional[str] = None) -> datetime:
    """
    Get end of day (23:59:59) for given datetime.
    
    Args:
        dt: Reference datetime. Uses current time if not provided.
        tz: Timezone. Uses settings.TIMEZONE if not provided.
    
    Returns:
        Datetime at end of day
    """
    if dt is None:
        dt = get_local_now(tz)
    elif dt.tzinfo is None:
        dt = localize_datetime(dt, tz)
    
    return dt.replace(hour=23, minute=59, second=59, microsecond=999999)
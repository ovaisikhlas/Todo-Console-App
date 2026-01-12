"""
Utility functions for the Todo application.
This module contains formatting and utility functions for enhanced table display and date handling.
"""
from typing import Optional
from datetime import datetime
from models import Task


def format_date_for_display(dt: Optional[datetime]) -> str:
    """
    Format a datetime object for display in the task table.
    
    Args:
        dt: The datetime object to format (or None)
        
    Returns:
        Formatted date string as "YYYY-MM-DD HH:MM" or "None" if dt is None
    """
    if dt is None:
        return "None"
    return dt.strftime("%Y-%m-%d %H:%M")


def is_overdue(task: Task) -> bool:
    """
    Check if a task is overdue (has due date in the past and is not completed).
    
    Args:
        task: The task to check
        
    Returns:
        True if task is overdue, False otherwise
    """
    if not task.due_date or task.completed:
        return False
    return task.due_date < datetime.now()


def parse_date_string(date_str: str) -> Optional[datetime]:
    """
    Parse a date string in format YYYY-MM-DD [HH:MM] to a datetime object.
    
    Args:
        date_str: The date string to parse
        
    Returns:
        Parsed datetime object or None if date_str is empty
        
    Raises:
        ValueError: If the date string format is invalid
    """
    if not date_str:
        return None
    
    try:
        # Try parsing with time first
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    except ValueError:
        # Try parsing date only
        return datetime.strptime(date_str, "%Y-%m-%d").replace(hour=23, minute=59)


def advance_date_by_pattern(dt: datetime, pattern: str) -> datetime:
    """
    Advance a date by the specified recurrence pattern.
    
    Args:
        dt: The original date to advance
        pattern: The recurrence pattern ("daily", "weekly", "monthly")
        
    Returns:
        New datetime advanced by the pattern
        
    Raises:
        ValueError: If the pattern is not recognized
    """
    from datetime import timedelta
    import calendar
    
    if pattern == "daily":
        return dt + timedelta(days=1)
    elif pattern == "weekly":
        return dt + timedelta(days=7)
    elif pattern == "monthly":
        # Add one month to the date
        year = dt.year
        month = dt.month
        day = dt.day
        
        # Calculate next month
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
        
        # Handle month-end edge cases (e.g., Jan 31 -> Feb 28/29)
        max_day = calendar.monthrange(year, month)[1]
        if day > max_day:
            day = max_day
        
        return dt.replace(year=year, month=month, day=day)
    else:
        raise ValueError(f"Unknown recurrence pattern: {pattern}")
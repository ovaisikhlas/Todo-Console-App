"""
Utility functions for the Todo application.
Contains helper functions for date formatting, validation, and other common operations.
"""
from datetime import datetime


def format_date_for_display(dt):
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


def is_overdue(task):
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


def parse_date_string(date_str):
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



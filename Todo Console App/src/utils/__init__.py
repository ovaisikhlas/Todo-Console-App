"""
__init__.py for the utils package.

This module exports the key utility functions and classes that are commonly used
across the application.
"""
from .date_utils import (
    format_date_for_display,
    is_overdue,
    parse_date_string,
    advance_date_by_pattern,
    is_due_soon
)
from .display_utils import (
    format_task_table,
    truncate_text,
    format_confirmation_message,
    format_error_message,
    format_feedback_message,
    format_help_text
)


__all__ = [
    'format_date_for_display',
    'is_overdue',
    'parse_date_string',
    'advance_date_by_pattern',
    'is_due_soon',
    'format_task_table',
    'truncate_text',
    'format_confirmation_message',
    'format_error_message',
    'format_feedback_message',
    'format_help_text'
]
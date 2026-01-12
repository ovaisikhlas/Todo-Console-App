"""
Display utility functions for the Todo application.
Contains helper functions for formatting task lists, tables, and user interface elements.
"""
from typing import List
from models import Task


def format_task_table(tasks: List[Task]) -> str:
    """
    Format a list of tasks into a clean, aligned table string.

    Args:
        tasks: List of Task objects to format

    Returns:
        Formatted table string with proper alignment and truncation
    """
    if not tasks:
        return "No tasks yet."

    # Create table header
    table_str = f"{'ID':<4} {'Status':<8} {'Priority':<10} {'Due Date':<17} {'Title':<25} {'Tags':<20} {'Description'}\n"
    table_str += "-" * 120 + "\n"

    # Format each task row
    from datetime import datetime
    now = datetime.now()
    for task in tasks:
        status = "[x]" if task.completed else "[ ]"
        priority = task.priority.capitalize()

        # Format due date for display
        if task.due_date:
            due_date_str = task.due_date.strftime("%Y-%m-%d %H:%M")
            # Add overdue indicator if applicable
            if task.due_date < now and not task.completed:
                due_date_str += " (OVERDUE!)"
        else:
            due_date_str = "None"

        title = task.title
        # Add overdue indicator to title if task is overdue
        if task.due_date and task.due_date < now and not task.completed:
            title += " (OVERDUE!)"

        tags_str = ", ".join(task.tags) if task.tags else ""
        description = task.description or ""

        # Truncate description to 40 characters with "..." if needed
        if len(description) > 40:
            description = description[:37] + "..."

        # Truncate tags to fit column width with "..." if needed
        if len(tags_str) > 17:  # Leave 3 chars for "..."
            tags_str = tags_str[:14] + "..."

        table_str += f"{task.id:<4} {status:<8} {priority:<10} {due_date_str:<17} {title:<25} {tags_str:<20} {description}\n"

    return table_str


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length with an optional suffix.

    Args:
        text: The text to truncate
        max_length: Maximum length of the text
        suffix: Suffix to append if text is truncated (default: "...")

    Returns:
        Truncated text with suffix if needed
    """
    if not text:
        return ""

    if len(text) <= max_length:
        return text

    if len(suffix) >= max_length:
        return suffix[:max_length]

    return text[:max_length - len(suffix)] + suffix


def format_confirmation_message(message: str) -> str:
    """
    Format a confirmation message with a checkmark prefix.
    
    Args:
        message: The message to format
        
    Returns:
        Formatted confirmation message
    """
    return f"✓ {message}"


def format_error_message(message: str) -> str:
    """
    Format an error message with an error prefix.
    
    Args:
        message: The message to format
        
    Returns:
        Formatted error message
    """
    return f"✗ Error: {message}"


def format_feedback_message(message: str) -> str:
    """
    Format a feedback message for display.
    
    Args:
        message: The message to format
        
    Returns:
        Formatted feedback message
    """
    return message


def format_help_text() -> str:
    """
    Format the help text showing all available commands.
    
    Returns:
        Formatted help text string
    """
    help_text = """
Available commands:
  add              - Add a new task
  list             - List all tasks
  list --status [pending|completed|all]  - Filter by status
  list --priority [high|medium|low|all]  - Filter by priority
  list --tag <tag>                       - Filter by tag (repeatable: --tag work --tag urgent)
  list --sort [id|priority|alpha|due]    - Sort by criterion
  list --overdue                         - Show only overdue tasks
  list --search <keyword>                - Search by keyword
  search <keyword> - Alternative search command
  update <id>      - Update a task by ID
  delete <id>      - Delete a task by ID
  complete <id>    - Toggle completion status of a task by ID
  help             - Show this help message
  quit/exit        - Exit the application

Examples:
  list --status pending --priority high    - Show pending high-priority tasks
  list --tag work --tag urgent             - Show tasks tagged with both 'work' and 'urgent'
  list --sort priority                     - Sort tasks by priority (high to low)
  list --sort due                          - Sort tasks by due date (overdue first)
  list --search meeting                    - Show tasks containing 'meeting' in title or description
  list --overdue --priority high           - Show high-priority overdue tasks
        """
    return help_text
"""
Command handler for adding new tasks.
Implements the 'add' command functionality.
"""
from datetime import datetime
from .base import BaseCommand


class AddCommand(BaseCommand):
    """
    Handler for the 'add' command.
    Adds a new task with title, description, priority, tags, due date, and recurrence.
    """
    
    def execute(self, args, flags):
        """
        Execute the add command.
        
        Args:
            args: List of command arguments (should be empty for add command)
            flags: Dictionary of command flags
            
        Returns:
            True if task was added successfully, False otherwise
        """
        # Get task title
        title = self.cli.get_user_input("Enter task title (required): ").strip()
        if not title:
            self.cli.display_error("Title is required!")
            return False

        # Get task description
        description = self.cli.get_user_input("Enter task description (optional, press Enter to skip): ").strip()
        if not description:  # If empty, set to None
            description = None

        # Get priority
        priority_input = self.cli.get_user_input("Enter priority (high/medium/low, default: medium): ").strip().lower()
        if not priority_input:
            priority = "medium"  # Default value
        elif priority_input in ["high", "medium", "low"]:
            priority = priority_input
        else:
            self.cli.display_error(f"Invalid priority: '{priority_input}'. Must be one of 'high', 'medium', 'low'.")
            return False

        # Get tags
        tags_input = self.cli.get_user_input("Enter tags (comma-separated, e.g., work,urgent,client): ").strip()
        tags = []
        if tags_input:
            # Parse tags: split by comma, strip whitespace, prevent duplicates
            raw_tags = tags_input.split(',')
            for tag in raw_tags:
                clean_tag = tag.strip()
                if clean_tag and clean_tag not in tags:  # Prevent duplicates
                    tags.append(clean_tag)

        # Get due date
        due_date_input = self.cli.get_user_input("Enter due date (optional, format: YYYY-MM-DD HH:MM or YYYY-MM-DD, press Enter to skip): ").strip()
        due_date = None
        if due_date_input:
            try:
                # Try parsing with time first
                due_date = datetime.strptime(due_date_input, "%Y-%m-%d %H:%M")
            except ValueError:
                try:
                    # Try parsing date only (default to 23:59)
                    date_part = datetime.strptime(due_date_input, "%Y-%m-%d")
                    due_date = date_part.replace(hour=23, minute=59)
                except ValueError:
                    self.cli.display_error(f"Invalid date format: '{due_date_input}'. Expected format: YYYY-MM-DD [HH:MM]")
                    return False

        # Get recurrence pattern
        recurrence_input = self.cli.get_user_input("Enter recurrence pattern (optional, none/daily/weekly/monthly, press Enter to skip): ").strip().lower()
        if not recurrence_input:
            recurrence = "none"  # Default value
        elif recurrence_input in ["none", "daily", "weekly", "monthly"]:
            recurrence = recurrence_input
        else:
            self.cli.display_error(f"Invalid recurrence pattern: '{recurrence_input}'. Must be one of 'none', 'daily', 'weekly', 'monthly'.")
            return False

        # Add the task
        task = self.todo_manager.add_task(title, description, priority, tags, due_date, recurrence)
        self.cli.display_confirmation(f"Task added with ID {task.id}: {task.title}")
        return True
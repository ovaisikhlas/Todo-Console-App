"""
Command handler for updating tasks.
Implements the 'update' command functionality with a more specific naming convention.
"""
from datetime import datetime
from .base import BaseCommand


class UpdateCommandHandler(BaseCommand):
    """
    Handler for the 'update' command with a more specific naming convention.
    Updates an existing task's title, description, priority, tags, due date, and recurrence.
    """
    
    def execute(self, args, flags):
        """
        Execute the update command.
        
        Args:
            args: List of command arguments (first should be task ID)
            flags: Dictionary of command flags
            
        Returns:
            True if command executed successfully, False otherwise
        """
        if not args:
            self.cli.display_error("Please provide a task ID for update command.")
            return False

        try:
            task_id = int(args[0])
        except ValueError:
            self.cli.display_error("Task ID must be a number.")
            return False

        task = self.todo_manager.get_task_by_id(task_id)
        if not task:
            self.cli.display_error(f"No task found with ID {task_id}.")
            return False

        # Get new title (or keep current if Enter pressed)
        new_title = self.cli.get_user_input(f"Enter new title (current: '{task.title}', press Enter to keep current): ").strip()
        if not new_title:
            new_title = None  # None means don't update

        # Get new description (or keep current if Enter pressed)
        current_desc = task.description if task.description else ""
        new_desc = self.cli.get_user_input(f"Enter new description (current: '{current_desc}', press Enter to keep current): ").strip()
        if new_desc == "":  # If user pressed Enter without typing
            new_desc = None  # None means don't update

        # Get new priority (or keep current if Enter pressed)
        current_priority = task.priority
        new_priority_input = self.cli.get_user_input(f"Enter new priority (current: '{current_priority}', high/medium/low, press Enter to keep current): ").strip().lower()
        if not new_priority_input:
            new_priority = None  # None means don't update
        elif new_priority_input in ["high", "medium", "low"]:
            new_priority = new_priority_input
        else:
            self.cli.display_error(f"Invalid priority: '{new_priority_input}'. Must be one of 'high', 'medium', 'low'.")
            return False

        # Get new tags (or keep current if Enter pressed)
        current_tags = ", ".join(task.tags) if task.tags else ""
        new_tags_input = self.cli.get_user_input(f"Enter new tags (current: '{current_tags}', comma-separated, press Enter to keep current): ").strip()
        new_tags = None  # None means don't update
        if new_tags_input == "":  # User pressed Enter without typing
            new_tags = None  # None means don't update
        elif new_tags_input:  # User entered new tags
            # Parse tags: split by comma, strip whitespace, prevent duplicates
            raw_tags = new_tags_input.split(',')
            new_tags = []
            for tag in raw_tags:
                clean_tag = tag.strip()
                if clean_tag and clean_tag not in new_tags:  # Prevent duplicates
                    new_tags.append(clean_tag)
        else:  # User entered empty string to clear tags
            new_tags = []  # Empty list means clear tags

        # Get new due date (or keep current if Enter pressed)
        current_due_date = task.due_date.strftime("%Y-%m-%d %H:%M") if task.due_date else "None"
        new_due_date_input = self.cli.get_user_input(f"Enter new due date (current: '{current_due_date}', format: YYYY-MM-DD HH:MM or YYYY-MM-DD, press Enter to keep current, or 'clear' to remove): ").strip()
        new_due_date = None  # None means don't update
        if new_due_date_input == "":  # User pressed Enter without typing
            new_due_date = None  # None means don't update
        elif new_due_date_input.lower() == "clear":  # User wants to clear the due date
            new_due_date = ""  # Empty string means clear the due date
        elif new_due_date_input:  # User entered a new due date
            try:
                # Try parsing with time first
                datetime.strptime(new_due_date_input, "%Y-%m-%d %H:%M")
                new_due_date = new_due_date_input  # Pass the original string to the update method
            except ValueError:
                try:
                    # Try parsing date only (default to 23:59)
                    datetime.strptime(new_due_date_input, "%Y-%m-%d")
                    new_due_date = new_due_date_input  # Pass the original string to the update method
                except ValueError:
                    self.cli.display_error(f"Invalid date format: '{new_due_date_input}'. Expected format: YYYY-MM-DD [HH:MM]")
                    return False
        else:  # Empty string means clear the due date
            new_due_date = ""  # Empty string means clear the due date

        # Get new recurrence pattern (or keep current if Enter pressed)
        current_recurrence = task.recurrence
        new_recurrence_input = self.cli.get_user_input(f"Enter new recurrence pattern (current: '{current_recurrence}', none/daily/weekly/monthly, press Enter to keep current): ").strip().lower()
        new_recurrence = None  # None means don't update
        if not new_recurrence_input:  # User pressed Enter without typing
            new_recurrence = None  # None means don't update
        elif new_recurrence_input in ["none", "daily", "weekly", "monthly"]:  # Valid recurrence pattern
            new_recurrence = new_recurrence_input
        else:
            self.cli.display_error(f"Invalid recurrence pattern: '{new_recurrence_input}'. Must be one of 'none', 'daily', 'weekly', 'monthly'.")
            return False

        updated_task = self.todo_manager.update_task(task_id, new_title, new_desc, new_priority, new_tags, new_due_date, new_recurrence)
        if updated_task:
            self.cli.display_confirmation(f"Task {task_id} updated successfully.")
        else:
            self.cli.display_error(f"Failed to update task {task_id}.")
            return False

        return True
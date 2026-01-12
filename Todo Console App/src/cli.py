import re
from typing import List, Optional, Tuple
from datetime import datetime
from models import Task
from todo_manager import TodoManager


class CLI:
    """
    Handles input processing, command parsing, and display formatting for the todo application.
    Enhanced to support due dates and recurrence patterns.
    """

    def __init__(self, todo_manager: TodoManager):
        self.todo_manager = todo_manager

    def display_tasks(self, tasks: List[Task]) -> None:
        """
        Display all tasks in a clean, aligned table format with due dates and overdue indicators.

        Args:
            tasks: List of Task objects to display
        """
        if not tasks:
            print("No tasks yet.")
            return

        # Print table header with new columns for Due Date
        print(f"{'ID':<4} {'Status':<8} {'Priority':<10} {'Due Date':<17} {'Title':<25} {'Tags':<20} {'Description'}")
        print("-" * 120)

        # Print each task
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

            print(f"{task.id:<4} {status:<8} {priority:<10} {due_date_str:<17} {title:<25} {tags_str:<20} {description}")
    
    def get_user_input(self, prompt: str) -> str:
        """
        Get input from the user with a prompt.
        
        Args:
            prompt: The prompt to display to the user
            
        Returns:
            The user's input as a string
        """
        return input(prompt).strip()
    
    def parse_command(self, user_input: str) -> Tuple[Optional[str], List[str], dict]:
        """
        Parse the user's command input with support for flags and options.

        Args:
            user_input: The raw input from the user

        Returns:
            A tuple containing (command, args, flags) where command is the lowercase command,
            args is a list of arguments, and flags is a dictionary of parsed flag options
        """
        # Split the input by whitespace
        parts = user_input.strip().split()
        if not parts or not parts[0]:
            return None, [], {}

        command = parts[0].lower()
        args = []
        flags = {}

        i = 1
        while i < len(parts):
            part = parts[i]
            if part.startswith('--'):
                flag_name = part[2:]  # Remove '--' prefix
                if i + 1 < len(parts) and not parts[i + 1].startswith('--'):
                    # Flag with value
                    flag_value = parts[i + 1]
                    if flag_name == 'tag':
                        # Handle repeatable --tag flags
                        if 'tag' not in flags:
                            flags['tag'] = []
                        flags['tag'].append(flag_value)
                        i += 2  # Skip both flag and value
                    else:
                        # Single value flags
                        flags[flag_name] = flag_value
                        i += 2  # Skip both flag and value
                else:
                    # Flag without value (like in search)
                    flags[flag_name] = True
                    i += 1
            else:
                # Regular argument
                args.append(part)
                i += 1

        return command, args, flags
    
    def display_help(self) -> None:
        """
        Display help information showing all available commands.
        """
        help_text = """
Available commands:
  add              - Add a new task
  list             - List all tasks
  list --status [pending|completed|all]  - Filter by status
  list --priority [high|medium|low|all]  - Filter by priority
  list --tag <tag>                       - Filter by tag (repeatable: --tag work --tag urgent)
  list --sort [id|priority|alpha]        - Sort by criterion
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
  list --search meeting                    - Show tasks containing 'meeting' in title or description
        """
        print(help_text)
    
    def display_confirmation(self, message: str) -> None:
        """
        Display a confirmation message to the user.
        
        Args:
            message: The confirmation message to display
        """
        print(f"✓ {message}")
    
    def display_error(self, message: str) -> None:
        """
        Display an error message to the user.
        
        Args:
            message: The error message to display
        """
        print(f"✗ Error: {message}")
    
    def display_feedback(self, message: str) -> None:
        """
        Display feedback to the user.
        
        Args:
            message: The feedback message to display
        """
        print(message)
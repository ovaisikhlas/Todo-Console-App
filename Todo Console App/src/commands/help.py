"""
Command handler for displaying help.
Implements the 'help' command functionality.
"""
from .base import BaseCommand


class HelpCommand(BaseCommand):
    """
    Handler for the 'help' command.
    Displays help information showing all available commands and options.
    """
    
    def execute(self, args, flags):
        """
        Execute the help command.
        
        Args:
            args: List of command arguments
            flags: Dictionary of command flags
            
        Returns:
            True if command executed successfully, False otherwise
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
        print(help_text)
        return True
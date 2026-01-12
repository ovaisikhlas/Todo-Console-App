"""
Command handler for searching tasks.
Implements the 'search' command functionality.
"""
from .base import BaseCommand


class SearchCommand(BaseCommand):
    """
    Handler for the 'search' command.
    Searches tasks by keyword in title or description.
    """
    
    def execute(self, args, flags):
        """
        Execute the search command.
        
        Args:
            args: List of command arguments (first should be search keyword)
            flags: Dictionary of command flags
            
        Returns:
            True if command executed successfully, False otherwise
        """
        if not args:
            self.cli.display_error("Please provide a keyword to search for.")
            return False

        keyword = args[0]
        matching_tasks = self.todo_manager.search_tasks(keyword)
        self.cli.display_tasks(matching_tasks)
        return True
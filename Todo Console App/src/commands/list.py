"""
Command handler for listing tasks.
Implements the 'list' command functionality with filtering and sorting options.
"""
from datetime import datetime
from .base import BaseCommand


class ListCommand(BaseCommand):
    """
    Handler for the 'list' command.
    Displays all tasks with optional filtering, sorting, and search.
    """
    
    def execute(self, args, flags):
        """
        Execute the list command.
        
        Args:
            args: List of command arguments
            flags: Dictionary of command flags
            
        Returns:
            True if command executed successfully, False otherwise
        """
        # Get all tasks initially
        tasks = self.todo_manager.list_tasks()

        # Apply search if provided
        if 'search' in flags:
            keyword = flags['search']
            tasks = self.todo_manager.search_tasks(keyword)
        elif len(args) > 0 and args[0]:  # If there's an argument that's not a flag, treat as search
            keyword = args[0]
            tasks = self.todo_manager.search_tasks(keyword)

        # Apply filters
        status = flags.get('status')
        priority_filter = flags.get('priority')
        tags_filter = flags.get('tag')  # This will be a list of tags
        overdue_only = 'overdue' in flags

        # Validate filter values
        if status and status not in ['pending', 'completed', 'all']:
            self.cli.display_error(f"Invalid status filter: '{status}'. Must be one of 'pending', 'completed', 'all'.")
            return False

        if priority_filter and priority_filter not in ['high', 'medium', 'low', 'all']:
            self.cli.display_error(f"Invalid priority filter: '{priority_filter}'. Must be one of 'high', 'medium', 'low', 'all'.")
            return False

        if status or priority_filter or tags_filter or overdue_only:
            tasks = self.todo_manager.filter_tasks(status=status, priority=priority_filter, tags=tags_filter, overdue_only=overdue_only)

        # Apply sorting
        sort_criterion = flags.get('sort', 'id')  # Default to 'id' if no sort flag
        if sort_criterion != 'id':
            if sort_criterion not in ['id', 'priority', 'alpha', 'due']:
                self.cli.display_error(f"Invalid sort criterion: '{sort_criterion}'. Must be one of 'id', 'priority', 'alpha', 'due'.")
                return False
            tasks = self.todo_manager.sort_tasks(tasks, sort_criterion)

        # Display results
        if not tasks:
            print("No tasks match your criteria.")
        else:
            self.cli.display_tasks(tasks)
        
        return True
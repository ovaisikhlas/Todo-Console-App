"""
Command handler for deleting tasks.
Implements the 'delete' command functionality.
"""
from .base import BaseCommand


class DeleteCommand(BaseCommand):
    """
    Handler for the 'delete' command.
    Deletes a task by ID with confirmation feedback.
    """
    
    def execute(self, args, flags):
        """
        Execute the delete command.
        
        Args:
            args: List of command arguments (first should be task ID)
            flags: Dictionary of command flags
            
        Returns:
            True if command executed successfully, False otherwise
        """
        if not args:
            self.cli.display_error("Please provide a task ID for delete command.")
            return False

        try:
            task_id = int(args[0])
        except ValueError:
            self.cli.display_error("Task ID must be a number.")
            return False

        deleted = self.todo_manager.delete_task(task_id)
        if deleted:
            self.cli.display_confirmation(f"Task {task_id} deleted successfully.")
        else:
            self.cli.display_error(f"No task found with ID {task_id}.")
            return False
        
        return True
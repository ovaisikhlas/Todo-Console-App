"""
Base command handler for the Todo application.
Defines the interface that all command handlers should implement.
"""


class BaseCommand:
    """
    Abstract base class for all command handlers.
    """
    
    def __init__(self, todo_manager, cli):
        self.todo_manager = todo_manager
        self.cli = cli
    
    def execute(self, args, flags):
        """
        Execute the command with the given arguments and flags.
        
        Args:
            args: List of command arguments
            flags: Dictionary of command flags
            
        Returns:
            True if command executed successfully, False otherwise
        """
        raise NotImplementedError("Subclasses must implement execute method")
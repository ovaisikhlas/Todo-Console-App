"""
Command handler for quitting the application.
Implements the 'quit' and 'exit' command functionality.
"""
from .base import BaseCommand


class QuitCommand(BaseCommand):
    """
    Handler for the 'quit' and 'exit' commands.
    Terminates the application gracefully.
    """
    
    def execute(self, args, flags):
        """
        Execute the quit command.
        
        Args:
            args: List of command arguments
            flags: Dictionary of command flags
            
        Returns:
            True if command executed successfully (though application will exit)
        """
        print("Goodbye!")
        return True  # This will be handled specially in main to exit the app
"""
Command dispatcher for the Todo application.
Routes commands to the appropriate command handlers.
"""
from .add import AddCommand
from .list import ListCommand
from .update import UpdateCommand
from .delete import DeleteCommand
from .complete import CompleteCommand
from .help import HelpCommand
from .search import SearchCommand
from .quit import QuitCommand


class CommandDispatcher:
    """
    Routes commands to the appropriate command handlers.
    """
    
    def __init__(self, todo_manager, cli):
        self.todo_manager = todo_manager
        self.cli = cli
        self.commands = {
            'add': AddCommand(todo_manager, cli),
            'list': ListCommand(todo_manager, cli),
            'update': UpdateCommand(todo_manager, cli),
            'delete': DeleteCommand(todo_manager, cli),
            'complete': CompleteCommand(todo_manager, cli),
            'help': HelpCommand(todo_manager, cli),
            'search': SearchCommand(todo_manager, cli),
            'quit': QuitCommand(todo_manager, cli),
            'exit': QuitCommand(todo_manager, cli),
        }
    
    def execute_command(self, command, args, flags):
        """
        Execute a command with the given arguments and flags.
        
        Args:
            command: The command to execute
            args: List of command arguments
            flags: Dictionary of command flags
            
        Returns:
            True if command executed successfully, False otherwise
        """
        if command in self.commands:
            return self.commands[command].execute(args, flags)
        else:
            self.cli.display_error(f"Unknown command: {command}. Type 'help' for available commands.")
            return False
"""
Command handler for completing tasks.
Implements the 'complete' command functionality.
"""
from .base import BaseCommand


class CompleteCommand(BaseCommand):
    """
    Handler for the 'complete' command.
    Toggles the completion status of a task by ID.
    If the task is recurring, creates a new instance with updated due date.
    """
    
    def execute(self, args, flags):
        """
        Execute the complete command.
        
        Args:
            args: List of command arguments (first should be task ID)
            flags: Dictionary of command flags
            
        Returns:
            True if command executed successfully, False otherwise
        """
        if not args:
            self.cli.display_error("Please provide a task ID for complete command.")
            return False

        try:
            task_id = int(args[0])
        except ValueError:
            self.cli.display_error("Task ID must be a number.")
            return False

        task = self.todo_manager.toggle_task_completion(task_id)
        if task:
            status = "complete" if task.completed else "incomplete"
            self.cli.display_feedback(f"Task {task_id} marked as {status}.")

            # Check if the completed task was recurring and a new instance was created
            original_task = self.todo_manager.get_task_by_id(task_id)
            if original_task and original_task.recurrence != "none" and original_task.completed:
                # Find the newest task with the same title to confirm a new instance was created
                all_tasks = self.todo_manager.list_tasks()
                for t in all_tasks:
                    if (t.title == original_task.title and
                        t.id != original_task.id and
                        not t.completed and
                        ((original_task.due_date and t.due_date and t.due_date > original_task.due_date) or not original_task.due_date)):
                        self.cli.display_feedback(f"New recurring instance created with ID {t.id} based on '{original_task.recurrence}' pattern.")
                        break
        else:
            self.cli.display_error(f"No task found with ID {task_id}.")
            return False

        return True
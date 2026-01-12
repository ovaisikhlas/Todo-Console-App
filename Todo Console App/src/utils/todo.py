"""
Simple todo module containing core functionality.
This module provides basic todo operations that can be imported and used by other modules.
"""
from datetime import datetime
from typing import List, Optional

from models import Task
from todo_manager import TodoManager


class TodoApp:
    """
    A wrapper class that combines the TodoManager and CLI functionality
    to provide a cohesive application interface.
    """
    
    def __init__(self):
        self.manager = TodoManager()
        
    def add_task(self, title: str, description: Optional[str] = None, 
                 priority: str = "medium", tags: Optional[List[str]] = None,
                 due_date: Optional[datetime] = None, recurrence: str = "none") -> Task:
        """
        Add a new task with the specified parameters.
        
        Args:
            title: The task title (required)
            description: The task description (optional)
            priority: The task priority (default "medium")
            tags: List of tags for the task (default empty list)
            due_date: Optional due date for the task
            recurrence: Recurrence pattern (default "none")
            
        Returns:
            The newly created Task object
        """
        return self.manager.add_task(title, description, priority, tags, due_date, recurrence)
    
    def list_tasks(self) -> List[Task]:
        """
        Get all tasks in the system.
        
        Returns:
            List of all Task objects
        """
        return self.manager.list_tasks()
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.
        
        Args:
            task_id: The ID of the task to retrieve
            
        Returns:
            The Task object if found, None otherwise
        """
        return self.manager.get_task_by_id(task_id)
    
    def update_task(self, task_id: int, title: Optional[str] = None, 
                    description: Optional[str] = None, priority: Optional[str] = None,
                    tags: Optional[List[str]] = None, due_date_str: Optional[str] = None,
                    recurrence: Optional[str] = None) -> Optional[Task]:
        """
        Update an existing task with new values.
        
        Args:
            task_id: The ID of the task to update
            title: New title (or None to keep current)
            description: New description (or None to keep current)
            priority: New priority (or None to keep current)
            tags: New tags list (or None to keep current)
            due_date_str: New due date string (or None to keep current)
            recurrence: New recurrence pattern (or None to keep current)
            
        Returns:
            The updated Task object if successful, None if task not found
        """
        return self.manager.update_task(task_id, title, description, priority, tags, due_date_str, recurrence)
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id: The ID of the task to delete
            
        Returns:
            True if the task was deleted, False if not found
        """
        return self.manager.delete_task(task_id)
    
    def toggle_task_completion(self, task_id: int) -> Optional[Task]:
        """
        Toggle the completion status of a task.
        
        Args:
            task_id: The ID of the task to toggle
            
        Returns:
            The updated Task object if found, None if not found
        """
        return self.manager.toggle_task_completion(task_id)
    
    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Search tasks by keyword in title or description.
        
        Args:
            keyword: The keyword to search for
            
        Returns:
            List of matching Task objects
        """
        return self.manager.search_tasks(keyword)
    
    def filter_tasks(self, status: Optional[str] = None, priority: Optional[str] = None,
                     tags: Optional[List[str]] = None, overdue_only: bool = False) -> List[Task]:
        """
        Filter tasks by various criteria.
        
        Args:
            status: Filter by status (pending, completed, all)
            priority: Filter by priority (high, medium, low, all)
            tags: Filter by tags (tasks must have ALL specified tags)
            overdue_only: Filter to show only overdue tasks
            
        Returns:
            List of filtered Task objects
        """
        return self.manager.filter_tasks(status, priority, tags, overdue_only)
    
    def sort_tasks(self, tasks: List[Task], criterion: str) -> List[Task]:
        """
        Sort tasks by the specified criterion.
        
        Args:
            tasks: List of tasks to sort
            criterion: Sort criterion (id, priority, alpha, due)
            
        Returns:
            List of sorted Task objects
        """
        return self.manager.sort_tasks(tasks, criterion)
    
    def get_overdue_tasks(self) -> List[Task]:
        """
        Get all tasks that are overdue.
        
        Returns:
            List of overdue Task objects
        """
        return self.manager.get_overdue_tasks()
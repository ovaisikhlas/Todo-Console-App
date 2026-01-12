"""
Unit tests for the Todo application components.
Tests the models, business logic, and utility functions.
"""
import unittest
from datetime import datetime, timedelta
from models import Task
from todo_manager import TodoManager


class TestTaskModel(unittest.TestCase):
    """
    Test the Task data model.
    """
    
    def test_task_creation(self):
        """
        Test creating a Task instance with all fields.
        """
        task = Task(
            id=1,
            title="Test Task",
            description="Test Description",
            completed=False,
            priority="high",
            tags=["work", "urgent"],
            due_date=datetime(2025, 12, 31, 23, 59),
            recurrence="daily"
        )
        
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)
        self.assertEqual(task.priority, "high")
        self.assertIn("work", task.tags)
        self.assertIn("urgent", task.tags)
        self.assertEqual(task.due_date, datetime(2025, 12, 31, 23, 59))
        self.assertEqual(task.recurrence, "daily")
    
    def test_task_defaults(self):
        """
        Test that Task creates with proper defaults.
        """
        task = Task(id=1, title="Simple Task")
        
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Simple Task")
        self.assertIsNone(task.description)
        self.assertFalse(task.completed)
        self.assertEqual(task.priority, "medium")  # Default priority
        self.assertEqual(task.tags, [])  # Default empty list
        self.assertIsNone(task.due_date)  # Default None
        self.assertEqual(task.recurrence, "none")  # Default recurrence


class TestTodoManager(unittest.TestCase):
    """
    Test the TodoManager business logic.
    """
    
    def setUp(self):
        """
        Set up a fresh TodoManager for each test.
        """
        self.manager = TodoManager()
    
    def test_add_task(self):
        """
        Test adding a task to the manager.
        """
        task = self.manager.add_task(
            title="New Task",
            description="Task Description",
            priority="high",
            tags=["important"],
            due_date=datetime(2025, 12, 31),
            recurrence="none"
        )
        
        self.assertEqual(task.id, 1)  # First task should get ID 1
        self.assertEqual(task.title, "New Task")
        self.assertEqual(task.description, "Task Description")
        self.assertEqual(task.priority, "high")
        self.assertIn("important", task.tags)
        self.assertIsNotNone(task.due_date)
        self.assertEqual(task.recurrence, "none")
        
        # Verify task is in the manager's list
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].id, 1)
    
    def test_add_multiple_tasks(self):
        """
        Test adding multiple tasks and verifying ID sequence.
        """
        task1 = self.manager.add_task("Task 1")
        task2 = self.manager.add_task("Task 2")
        task3 = self.manager.add_task("Task 3")
        
        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task3.id, 3)
        
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 3)
    
    def test_get_task_by_id(self):
        """
        Test retrieving a task by its ID.
        """
        task = self.manager.add_task("Test Task")
        
        retrieved_task = self.manager.get_task_by_id(task.id)
        self.assertIsNotNone(retrieved_task)
        self.assertEqual(retrieved_task.id, task.id)
        self.assertEqual(retrieved_task.title, task.title)
        
        # Test getting non-existent task
        nonexistent_task = self.manager.get_task_by_id(999)
        self.assertIsNone(nonexistent_task)
    
    def test_update_task(self):
        """
        Test updating a task's properties.
        """
        original_task = self.manager.add_task(
            title="Original Title",
            description="Original Description",
            priority="low",
            tags=["old", "tag"],
            due_date=datetime(2024, 1, 1),
            recurrence="none"
        )
        
        # Update the task
        updated_task = self.manager.update_task(
            task_id=original_task.id,
            title="Updated Title",
            description="Updated Description",
            priority="high",
            tags=["new", "tag"],
            due_date_str="2025-12-31 15:30",
            recurrence="weekly"
        )
        
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "Updated Title")
        self.assertEqual(updated_task.description, "Updated Description")
        self.assertEqual(updated_task.priority, "high")
        self.assertIn("new", updated_task.tags)
        self.assertIn("tag", updated_task.tags)
        self.assertNotIn("old", updated_task.tags)  # Old tag should be replaced
        self.assertEqual(updated_task.recurrence, "weekly")
    
    def test_delete_task(self):
        """
        Test deleting a task.
        """
        task = self.manager.add_task("Task to Delete")
        
        # Verify task exists
        self.assertIsNotNone(self.manager.get_task_by_id(task.id))
        
        # Delete the task
        result = self.manager.delete_task(task.id)
        self.assertTrue(result)
        
        # Verify task no longer exists
        self.assertIsNone(self.manager.get_task_by_id(task.id))
        
        # Try to delete non-existent task
        result2 = self.manager.delete_task(999)
        self.assertFalse(result2)
    
    def test_toggle_completion(self):
        """
        Test toggling a task's completion status.
        """
        task = self.manager.add_task("Toggle Task")
        self.assertFalse(task.completed)
        
        # Toggle completion
        toggled_task = self.manager.toggle_task_completion(task.id)
        self.assertTrue(toggled_task.completed)
        
        # Toggle again
        toggled_back_task = self.manager.toggle_task_completion(task.id)
        self.assertFalse(toggled_back_task.completed)
    
    def test_search_tasks(self):
        """
        Test searching for tasks by keyword.
        """
        # Add some tasks
        task1 = self.manager.add_task("Meeting with John", "Discuss project timeline")
        task2 = self.manager.add_task("Buy groceries", "Milk, bread, eggs")
        task3 = self.manager.add_task("Finish report", "Complete quarterly report for finance department")
        
        # Search for "john" (should match title case-insensitive)
        results_john = self.manager.search_tasks("john")
        self.assertEqual(len(results_john), 1)
        self.assertEqual(results_john[0].id, task1.id)
        
        # Search for "department" (should match description)
        results_dept = self.manager.search_tasks("department")
        self.assertEqual(len(results_dept), 1)
        self.assertEqual(results_dept[0].id, task3.id)
        
        # Search for "project" (should match description of task1)
        results_project = self.manager.search_tasks("project")
        self.assertEqual(len(results_project), 1)
        self.assertEqual(results_project[0].id, task1.id)
    
    def test_filter_tasks(self):
        """
        Test filtering tasks by various criteria.
        """
        # Add tasks with different properties
        task1 = self.manager.add_task("High Priority", priority="high", tags=["work", "urgent"])
        task2 = self.manager.add_task("Low Priority", priority="low", tags=["personal"])
        task3 = self.manager.add_task("Completed Task", priority="medium", tags=["work"])
        self.manager.toggle_task_completion(task3.id)  # Mark as completed
        
        # Filter by priority
        high_priority_tasks = self.manager.filter_tasks(priority="high")
        self.assertEqual(len(high_priority_tasks), 1)
        self.assertEqual(high_priority_tasks[0].id, task1.id)
        
        # Filter by status (pending)
        pending_tasks = self.manager.filter_tasks(status="pending")
        self.assertEqual(len(pending_tasks), 2)  # task1 and task2 are pending
        
        # Filter by status (completed)
        completed_tasks = self.manager.filter_tasks(status="completed")
        self.assertEqual(len(completed_tasks), 1)
        self.assertEqual(completed_tasks[0].id, task3.id)
        
        # Filter by tags (work - should return 2 tasks)
        work_tasks = self.manager.filter_tasks(tags=["work"])
        self.assertEqual(len(work_tasks), 2)  # task1 and task3 have "work" tag
        
        # Filter by multiple tags (AND logic - should return 0 tasks since no task has both work AND personal)
        multi_tag_tasks = self.manager.filter_tasks(tags=["work", "personal"])
        self.assertEqual(len(multi_tag_tasks), 0)
    
    def test_sort_tasks(self):
        """
        Test sorting tasks by different criteria.
        """
        # Add tasks with different properties
        task1 = self.manager.add_task("Alpha Task", priority="low")
        task2 = self.manager.add_task("Zulu Task", priority="high")
        task3 = self.manager.add_task("Bravo Task", priority="medium")
        
        all_tasks = self.manager.list_tasks()
        
        # Sort by ID (default)
        sorted_by_id = self.manager.sort_tasks(all_tasks, "id")
        self.assertEqual(sorted_by_id[0].id, 1)
        self.assertEqual(sorted_by_id[1].id, 2)
        self.assertEqual(sorted_by_id[2].id, 3)
        
        # Sort by priority (high first)
        sorted_by_priority = self.manager.sort_tasks(all_tasks, "priority")
        self.assertEqual(sorted_by_priority[0].priority, "high")  # task2
        self.assertEqual(sorted_by_priority[1].priority, "medium")  # task3
        self.assertEqual(sorted_by_priority[2].priority, "low")  # task1
        
        # Sort alphabetically
        sorted_alpha = self.manager.sort_tasks(all_tasks, "alpha")
        titles = [task.title for task in sorted_alpha]
        self.assertEqual(titles, ["Alpha Task", "Bravo Task", "Zulu Task"])
    
    def test_get_overdue_tasks(self):
        """
        Test getting overdue tasks.
        """
        # Add an overdue task
        past_due = datetime.now() - timedelta(days=1)
        overdue_task = self.manager.add_task(
            "Overdue Task", 
            "This task is overdue", 
            due_date=past_due
        )
        
        # Add a future task
        future_due = datetime.now() + timedelta(days=1)
        future_task = self.manager.add_task(
            "Future Task", 
            "This task is due in the future", 
            due_date=future_due
        )
        
        # Add a completed task with past due date (should not be considered overdue)
        completed_past_task = self.manager.add_task(
            "Completed Past Task", 
            "This task was due in the past but is completed", 
            due_date=past_due
        )
        self.manager.toggle_task_completion(completed_past_task.id)
        
        # Get overdue tasks
        overdue_tasks = self.manager.get_overdue_tasks()
        
        # Should only return the incomplete overdue task
        self.assertEqual(len(overdue_tasks), 1)
        self.assertEqual(overdue_tasks[0].id, overdue_task.id)
        self.assertFalse(overdue_tasks[0].completed)


if __name__ == '__main__':
    unittest.main()
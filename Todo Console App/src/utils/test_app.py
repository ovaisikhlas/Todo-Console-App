"""
Test module for the Todo application.
Contains tests for core functionality and edge cases.
"""
import unittest
from datetime import datetime, timedelta
from models import Task
from todo_manager import TodoManager


class TestTodoApp(unittest.TestCase):
    """
    Test suite for the Todo application core functionality.
    """
    
    def setUp(self):
        """
        Set up a fresh TodoManager instance for each test.
        """
        self.manager = TodoManager()
    
    def test_add_task_basic(self):
        """
        Test adding a basic task without priority or tags.
        """
        task = self.manager.add_task("Test task", "Test description")
        self.assertEqual(task.title, "Test task")
        self.assertEqual(task.description, "Test description")
        self.assertEqual(task.priority, "medium")
        self.assertEqual(task.tags, [])
        self.assertEqual(task.completed, False)
        self.assertIsNone(task.due_date)
        self.assertEqual(task.recurrence, "none")
    
    def test_add_task_with_priority_and_tags(self):
        """
        Test adding a task with priority and tags.
        """
        task = self.manager.add_task(
            "Test task", 
            "Test description", 
            "high", 
            ["work", "urgent"], 
            datetime(2025, 12, 31, 23, 59),
            "daily"
        )
        self.assertEqual(task.title, "Test task")
        self.assertEqual(task.priority, "high")
        self.assertIn("work", task.tags)
        self.assertIn("urgent", task.tags)
        self.assertIsNotNone(task.due_date)
        self.assertEqual(task.recurrence, "daily")
    
    def test_complete_task(self):
        """
        Test completing a task.
        """
        task = self.manager.add_task("Test task")
        self.assertFalse(task.completed)
        
        updated_task = self.manager.toggle_task_completion(task.id)
        self.assertTrue(updated_task.completed)
    
    def test_list_tasks(self):
        """
        Test listing all tasks.
        """
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 2)
    
    def test_update_task(self):
        """
        Test updating a task's properties.
        """
        task = self.manager.add_task("Original title", "Original description", "low", ["tag1"])
        self.manager.update_task(
            task.id, 
            title="Updated title",
            description="Updated description",
            priority="high",
            tags=["tag1", "tag2"]
        )
        
        updated_task = self.manager.get_task_by_id(task.id)
        self.assertEqual(updated_task.title, "Updated title")
        self.assertEqual(updated_task.description, "Updated description")
        self.assertEqual(updated_task.priority, "high")
        self.assertIn("tag1", updated_task.tags)
        self.assertIn("tag2", updated_task.tags)
        self.assertEqual(len(updated_task.tags), 2)
    
    def test_delete_task(self):
        """
        Test deleting a task.
        """
        task = self.manager.add_task("Test task")
        initial_count = len(self.manager.list_tasks())
        
        result = self.manager.delete_task(task.id)
        self.assertTrue(result)
        
        after_count = len(self.manager.list_tasks())
        self.assertEqual(after_count, initial_count - 1)
    
    def test_search_tasks(self):
        """
        Test searching for tasks by keyword.
        """
        self.manager.add_task("Meeting with team", "Discuss project")
        self.manager.add_task("Buy groceries", "Milk and bread")
        
        results = self.manager.search_tasks("team")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Meeting with team")
    
    def test_filter_tasks_by_status(self):
        """
        Test filtering tasks by status.
        """
        task1 = self.manager.add_task("Pending task")
        task2 = self.manager.add_task("Completed task")
        self.manager.toggle_task_completion(task2.id)  # Complete the second task
        
        pending_tasks = self.manager.filter_tasks(status="pending")
        self.assertEqual(len(pending_tasks), 1)
        self.assertEqual(pending_tasks[0].id, task1.id)
        
        completed_tasks = self.manager.filter_tasks(status="completed")
        self.assertEqual(len(completed_tasks), 1)
        self.assertEqual(completed_tasks[0].id, task2.id)
    
    def test_filter_tasks_by_priority(self):
        """
        Test filtering tasks by priority.
        """
        self.manager.add_task("Low priority task", priority="low")
        self.manager.add_task("High priority task", priority="high")
        
        high_priority_tasks = self.manager.filter_tasks(priority="high")
        self.assertEqual(len(high_priority_tasks), 1)
        self.assertEqual(high_priority_tasks[0].priority, "high")
    
    def test_sort_tasks_by_priority(self):
        """
        Test sorting tasks by priority.
        """
        low_task = self.manager.add_task("Low priority", priority="low")
        high_task = self.manager.add_task("High priority", priority="high")
        medium_task = self.manager.add_task("Medium priority", priority="medium")
        
        all_tasks = self.manager.list_tasks()
        sorted_tasks = self.manager.sort_tasks(all_tasks, "priority")
        
        # High priority should come first, then medium, then low
        self.assertEqual(sorted_tasks[0].id, high_task.id)
        self.assertEqual(sorted_tasks[1].id, medium_task.id)
        self.assertEqual(sorted_tasks[2].id, low_task.id)
    
    def test_recurring_task_completion_creates_new_instance(self):
        """
        Test that completing a recurring task creates a new instance.
        """
        initial_count = len(self.manager.list_tasks())
        
        # Add a recurring task
        recurring_task = self.manager.add_task(
            "Daily task", 
            "A task that repeats daily", 
            "medium", 
            ["daily"], 
            datetime(2024, 1, 1, 10, 0),  # Set a due date in the past
            "daily"
        )
        
        # Complete the recurring task
        self.manager.toggle_task_completion(recurring_task.id)
        
        # Check that a new instance was created
        final_count = len(self.manager.list_tasks())
        self.assertEqual(final_count, initial_count + 2)  # Original + new instance
        
        # Verify the original task is marked as completed
        original_task = self.manager.get_task_by_id(recurring_task.id)
        self.assertTrue(original_task.completed)
        
        # Find the new task (should have a different ID but same title)
        tasks = self.manager.list_tasks()
        new_task = None
        for task in tasks:
            if task.id != recurring_task.id and task.title == "Daily task" and not task.completed:
                new_task = task
                break
        
        self.assertIsNotNone(new_task)
        # The new task should have an updated due date (advanced by 1 day for daily pattern)
        expected_new_date = recurring_task.due_date + timedelta(days=1)
        self.assertEqual(new_task.due_date.date(), expected_new_date.date())


if __name__ == '__main__':
    unittest.main()
"""
Test module for advanced features of the Todo application.
Contains tests for due dates, recurrence, and other intelligent features.
"""
import unittest
from datetime import datetime, timedelta
from models import Task
from todo_manager import TodoManager


class TestAdvancedFeatures(unittest.TestCase):
    """
    Test suite for the advanced features of the Todo application.
    """
    
    def setUp(self):
        """
        Set up a fresh TodoManager instance for each test.
        """
        self.manager = TodoManager()
    
    def test_add_task_with_due_date(self):
        """
        Test adding a task with a due date.
        """
        due_date = datetime(2025, 12, 31, 23, 59)
        task = self.manager.add_task(
            "Test task with due date",
            "Test description",
            "medium",
            [],
            due_date,
            "none"
        )
        
        self.assertEqual(task.due_date, due_date)
        self.assertEqual(task.title, "Test task with due date")
    
    def test_is_overdue_functionality(self):
        """
        Test identifying overdue tasks.
        """
        # Add a task with a past due date
        past_due = datetime.now() - timedelta(days=1)
        overdue_task = self.manager.add_task(
            "Overdue task",
            "This task is overdue",
            "high",
            ["urgent"],
            past_due,
            "none"
        )
        
        # Add a task with a future due date
        future_due = datetime.now() + timedelta(days=1)
        future_task = self.manager.add_task(
            "Future task",
            "This task is due in the future",
            "low",
            [],
            future_due,
            "none"
        )
        
        # Get overdue tasks
        overdue_tasks = self.manager.get_overdue_tasks()
        
        # Only the first task should be overdue
        self.assertEqual(len(overdue_tasks), 1)
        self.assertEqual(overdue_tasks[0].id, overdue_task.id)
    
    def test_recurring_task_daily(self):
        """
        Test that completing a daily recurring task creates a new instance with due date advanced by 1 day.
        """
        initial_count = len(self.manager.list_tasks())
        
        # Add a daily recurring task
        due_date = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)
        recurring_task = self.manager.add_task(
            "Daily recurring task",
            "This task repeats daily",
            "medium",
            ["daily"],
            due_date,
            "daily"
        )
        
        # Complete the task
        completed_task = self.manager.toggle_task_completion(recurring_task.id)
        
        # Verify the original task is completed
        self.assertTrue(completed_task.completed)
        
        # Verify a new instance was created
        final_count = len(self.manager.list_tasks())
        self.assertEqual(final_count, initial_count + 1)  # Original + new instance
        
        # Find the new task (should have same title but different ID)
        all_tasks = self.manager.list_tasks()
        new_task = None
        for task in all_tasks:
            if task.id != recurring_task.id and task.title == "Daily recurring task" and not task.completed:
                new_task = task
                break
        
        self.assertIsNotNone(new_task)
        # The new task should have a due date 1 day after the original
        expected_new_date = due_date + timedelta(days=1)
        self.assertEqual(new_task.due_date.date(), expected_new_date.date())
    
    def test_recurring_task_weekly(self):
        """
        Test that completing a weekly recurring task creates a new instance with due date advanced by 7 days.
        """
        initial_count = len(self.manager.list_tasks())
        
        # Add a weekly recurring task
        due_date = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)
        recurring_task = self.manager.add_task(
            "Weekly recurring task",
            "This task repeats weekly",
            "high",
            ["weekly"],
            due_date,
            "weekly"
        )
        
        # Complete the task
        completed_task = self.manager.toggle_task_completion(recurring_task.id)
        
        # Verify the original task is completed
        self.assertTrue(completed_task.completed)
        
        # Verify a new instance was created
        final_count = len(self.manager.list_tasks())
        self.assertEqual(final_count, initial_count + 1)  # Original + new instance
        
        # Find the new task (should have same title but different ID)
        all_tasks = self.manager.list_tasks()
        new_task = None
        for task in all_tasks:
            if task.id != recurring_task.id and task.title == "Weekly recurring task" and not task.completed:
                new_task = task
                break
        
        self.assertIsNotNone(new_task)
        # The new task should have a due date 7 days after the original
        expected_new_date = due_date + timedelta(days=7)
        self.assertEqual(new_task.due_date.date(), expected_new_date.date())
    
    def test_recurring_task_monthly(self):
        """
        Test that completing a monthly recurring task creates a new instance with due date advanced by 1 month.
        """
        initial_count = len(self.manager.list_tasks())
        
        # Add a monthly recurring task
        due_date = datetime(2024, 1, 15, 10, 0)  # January 15th
        recurring_task = self.manager.add_task(
            "Monthly recurring task",
            "This task repeats monthly",
            "medium",
            ["monthly"],
            due_date,
            "monthly"
        )
        
        # Complete the task
        completed_task = self.manager.toggle_task_completion(recurring_task.id)
        
        # Verify the original task is completed
        self.assertTrue(completed_task.completed)
        
        # Verify a new instance was created
        final_count = len(self.manager.list_tasks())
        self.assertEqual(final_count, initial_count + 1)  # Original + new instance
        
        # Find the new task (should have same title but different ID)
        all_tasks = self.manager.list_tasks()
        new_task = None
        for task in all_tasks:
            if task.id != recurring_task.id and task.title == "Monthly recurring task" and not task.completed:
                new_task = task
                break
        
        self.assertIsNotNone(new_task)
        # The new task should have a due date 1 month after the original
        # (Note: This test assumes the advance_date_by_pattern function handles month boundaries correctly)
        self.assertEqual(new_task.due_date.month, 2)  # February
        self.assertEqual(new_task.due_date.day, 15)   # Same day of month
        self.assertEqual(new_task.due_date.year, 2024)
    
    def test_filter_tasks_by_overdue(self):
        """
        Test filtering tasks by overdue status.
        """
        # Add an overdue task
        past_due = datetime.now() - timedelta(days=1)
        overdue_task = self.manager.add_task(
            "Overdue task",
            "This task is overdue",
            "high",
            ["urgent"],
            past_due,
            "none"
        )
        
        # Add a future task
        future_due = datetime.now() + timedelta(days=1)
        future_task = self.manager.add_task(
            "Future task",
            "This task is due in the future",
            "low",
            [],
            future_due,
            "none"
        )
        
        # Add a completed task with past due date
        completed_past_task = self.manager.add_task(
            "Completed past task",
            "This task was due in the past but is completed",
            "medium",
            [],
            past_due,
            "none"
        )
        self.manager.toggle_task_completion(completed_past_task.id)
        
        # Filter for overdue tasks only
        overdue_filtered = self.manager.filter_tasks(overdue_only=True)
        
        # Should only return the incomplete overdue task
        self.assertEqual(len(overdue_filtered), 1)
        self.assertEqual(overdue_filtered[0].id, overdue_task.id)
        self.assertFalse(overdue_filtered[0].completed)
    
    def test_sort_tasks_by_due_date(self):
        """
        Test sorting tasks by due date with overdue tasks first.
        """
        # Add tasks with different due dates
        far_future = datetime.now() + timedelta(days=30)
        near_future = datetime.now() + timedelta(days=2)
        past_due = datetime.now() - timedelta(days=1)
        
        future_task = self.manager.add_task("Future task", "Due in 30 days", "medium", [], far_future, "none")
        near_task = self.manager.add_task("Near task", "Due in 2 days", "high", [], near_future, "none")
        overdue_task = self.manager.add_task("Overdue task", "Was due yesterday", "high", [], past_due, "none")
        
        all_tasks = self.manager.list_tasks()
        sorted_tasks = self.manager.sort_tasks(all_tasks, "due")
        
        # Overdue task should be first, then near future, then far future
        self.assertEqual(sorted_tasks[0].id, overdue_task.id)
        self.assertEqual(sorted_tasks[1].id, near_task.id)
        self.assertEqual(sorted_tasks[2].id, future_task.id)
    
    def test_parse_date_string(self):
        """
        Test parsing date strings in different formats.
        """
        from utils.main import parse_date_string
        
        # Test date only
        result1 = parse_date_string("2025-12-31")
        expected1 = datetime(2025, 12, 31, 23, 59)  # Should default to 23:59
        self.assertEqual(result1, expected1)
        
        # Test date with time
        result2 = parse_date_string("2025-12-31 14:30")
        expected2 = datetime(2025, 12, 31, 14, 30)
        self.assertEqual(result2, expected2)
        
        # Test empty string
        result3 = parse_date_string("")
        self.assertIsNone(result3)
        
        # Test invalid format
        with self.assertRaises(ValueError):
            parse_date_string("invalid-date-format")
    
    def test_format_date_for_display(self):
        """
        Test formatting dates for display.
        """
        from utils.main import format_date_for_display
        
        # Test with a datetime object
        dt = datetime(2025, 12, 31, 14, 30)
        result = format_date_for_display(dt)
        self.assertEqual(result, "2025-12-31 14:30")
        
        # Test with None
        result_none = format_date_for_display(None)
        self.assertEqual(result_none, "None")


if __name__ == '__main__':
    unittest.main()
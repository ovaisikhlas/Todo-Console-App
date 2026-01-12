"""
Test suite for the advanced features of the Todo application.
Tests the recurring tasks, due dates, and enhanced filtering/sorting functionality.
"""
import unittest
from datetime import datetime, timedelta
from src.models import Task
from src.todo_manager import TodoManager


class TestAdvancedFeatures(unittest.TestCase):
    """
    Test suite for advanced features: recurring tasks, due dates, and enhanced filtering/sorting.
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
        due_date = datetime(2025, 12, 31, 10, 30)
        task = self.manager.add_task(
            title="Test task with due date",
            description="Test description",
            priority="high",
            tags=["test", "important"],
            due_date=due_date,
            recurrence="none"
        )
        
        self.assertEqual(task.title, "Test task with due date")
        self.assertEqual(task.description, "Test description")
        self.assertEqual(task.priority, "high")
        self.assertIn("test", task.tags)
        self.assertIn("important", task.tags)
        self.assertEqual(task.due_date, due_date)
        self.assertEqual(task.recurrence, "none")
    
    def test_add_task_with_recurrence(self):
        """
        Test adding a task with recurrence pattern.
        """
        task = self.manager.add_task(
            title="Recurring task",
            description="A task that repeats",
            priority="medium",
            tags=["recurring"],
            due_date=datetime(2025, 1, 15, 9, 0),
            recurrence="daily"
        )
        
        self.assertEqual(task.title, "Recurring task")
        self.assertEqual(task.recurrence, "daily")
        self.assertIsNotNone(task.due_date)
    
    def test_complete_recurring_task_creates_new_instance(self):
        """
        Test that completing a recurring task creates a new instance with updated due date.
        """
        initial_count = len(self.manager.list_tasks())

        # Add a recurring task
        due_date = datetime(2024, 1, 15, 10, 0)
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

        # Verify the original task is marked as complete
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
        # The new task should have an updated due date (advanced by 1 day for daily pattern)
        expected_new_date = due_date + timedelta(days=1)
        self.assertEqual(new_task.due_date.date(), expected_new_date.date())
    
    def test_complete_weekly_recurring_task(self):
        """
        Test that completing a weekly recurring task creates a new instance with due date advanced by 7 days.
        """
        initial_count = len(self.manager.list_tasks())
        
        # Add a weekly recurring task
        due_date = datetime(2024, 1, 15, 10, 0)  # Monday
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

        # Verify the original task is marked as complete
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
    
    def test_complete_monthly_recurring_task(self):
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

        # Verify the original task is marked as complete
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
    
    def test_get_overdue_tasks(self):
        """
        Test getting overdue tasks (tasks with due date in the past that are not completed).
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
        
        # Get overdue tasks
        overdue_tasks = self.manager.get_overdue_tasks()
        
        # Should only return the incomplete overdue task
        self.assertEqual(len(overdue_tasks), 1)
        self.assertEqual(overdue_tasks[0].id, overdue_task.id)
        self.assertFalse(overdue_tasks[0].completed)
    
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
    
    def test_update_task_with_due_date_and_recurrence(self):
        """
        Test updating a task's due date and recurrence pattern.
        """
        # Add a task
        original_task = self.manager.add_task(
            "Original task",
            "Original description",
            "low",
            ["original"],
            datetime(2024, 1, 1),
            "none"
        )
        
        # Update the task with new due date and recurrence
        updated_task = self.manager.update_task(
            original_task.id,
            title="Updated task",
            description="Updated description",
            priority="high",
            tags=["updated", "important"],
            due_date_str="2025-12-31 15:30",
            recurrence="weekly"
        )

        self.assertEqual(updated_task.title, "Updated task")
        self.assertEqual(updated_task.description, "Updated description")
        self.assertEqual(updated_task.priority, "high")
        self.assertIn("updated", updated_task.tags)
        self.assertIn("important", updated_task.tags)
        self.assertEqual(len(updated_task.tags), 2)
        self.assertEqual(updated_task.due_date, datetime(2025, 12, 31, 15, 30))
        self.assertEqual(updated_task.recurrence, "weekly")
    
    def test_search_tasks_by_due_date_fields(self):
        """
        Test that search functionality works with tasks containing date-related information.
        """
        # Add tasks with date-related content in title or description
        task1 = self.manager.add_task(
            "Meeting on 2025-01-30",
            "Team sync on the last day of the month",
            "medium",
            ["meeting"],
            datetime(2025, 1, 30),
            "none"
        )
        
        task2 = self.manager.add_task(
            "Appointment",
            "Doctor visit on 2025-02-15 at 10:00 AM",
            "high",
            ["health"],
            datetime(2025, 2, 15, 10, 0),
            "none"
        )
        
        # Search for tasks containing "2025"
        results = self.manager.search_tasks("2025")
        self.assertEqual(len(results), 2)
        self.assertIn(task1.id, [t.id for t in results])
        self.assertIn(task2.id, [t.id for t in results])
        
        # Search for tasks containing "visit"
        results = self.manager.search_tasks("visit")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, task2.id)
    
    def test_filter_tasks_by_multiple_criteria(self):
        """
        Test filtering tasks by multiple criteria simultaneously.
        """
        # Add tasks with different attributes
        task1 = self.manager.add_task("Urgent work task", "Important work item", "high", ["work", "urgent"], datetime(2024, 1, 1), "none")
        task2 = self.manager.add_task("Personal chore", "Non-urgent personal item", "low", ["personal"], datetime(2025, 12, 31), "none")
        task3 = self.manager.add_task("Medium priority", "Regular task", "medium", ["work"], datetime(2024, 6, 15), "none")
        
        # Filter by priority high and tag work
        results = self.manager.filter_tasks(priority="high", tags=["work"])
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, task1.id)
        
        # Filter by status pending (all tasks should be pending)
        results = self.manager.filter_tasks(status="pending")
        self.assertEqual(len(results), 3)
        
        # Filter by status completed (should be empty)
        results = self.manager.filter_tasks(status="completed")
        self.assertEqual(len(results), 0)


if __name__ == '__main__':
    unittest.main()
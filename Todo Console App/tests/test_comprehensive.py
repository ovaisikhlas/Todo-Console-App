"""
Comprehensive test suite for the complete Todo application.
Tests all features from basic to advanced levels including edge cases and integration scenarios.
"""
import unittest
from datetime import datetime, timedelta
from src.models import Task
from src.todo_manager import TodoManager


class TestComprehensiveTodoApp(unittest.TestCase):
    """
    Comprehensive test suite covering all functionality of the Todo application
    from basic features through advanced features (recurring tasks, due dates, etc.).
    """
    
    def setUp(self):
        """
        Set up a fresh TodoManager instance for each test.
        """
        self.manager = TodoManager()
    
    def test_basic_task_operations(self):
        """
        Test basic task operations: add, list, update, delete, complete.
        """
        # Add a basic task
        task = self.manager.add_task("Basic task", "Description for basic task", "medium", ["basic"])
        
        self.assertEqual(task.title, "Basic task")
        self.assertEqual(task.description, "Description for basic task")
        self.assertEqual(task.priority, "medium")
        self.assertIn("basic", task.tags)
        self.assertFalse(task.completed)
        self.assertIsNone(task.due_date)
        self.assertEqual(task.recurrence, "none")
        
        # List tasks
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].id, task.id)
        
        # Update task
        updated_task = self.manager.update_task(
            task.id,
            title="Updated basic task",
            description="Updated description",
            priority="high"
        )
        
        self.assertEqual(updated_task.title, "Updated basic task")
        self.assertEqual(updated_task.description, "Updated description")
        self.assertEqual(updated_task.priority, "high")
        
        # Complete task
        completed_task = self.manager.toggle_task_completion(task.id)
        self.assertTrue(completed_task.completed)
        
        # Delete task
        result = self.manager.delete_task(task.id)
        self.assertTrue(result)
        
        tasks_after_delete = self.manager.list_tasks()
        self.assertEqual(len(tasks_after_delete), 0)
    
    def test_add_task_with_all_attributes(self):
        """
        Test adding a task with all possible attributes: title, description, priority, tags, due date, and recurrence.
        """
        due_date = datetime(2025, 12, 31, 15, 30)
        task = self.manager.add_task(
            title="Comprehensive task",
            description="Task with all attributes",
            priority="high",
            tags=["comprehensive", "all", "attributes"],
            due_date=due_date,
            recurrence="weekly"
        )
        
        self.assertEqual(task.title, "Comprehensive task")
        self.assertEqual(task.description, "Task with all attributes")
        self.assertEqual(task.priority, "high")
        self.assertIn("comprehensive", task.tags)
        self.assertIn("all", task.tags)
        self.assertIn("attributes", task.tags)
        self.assertEqual(len(task.tags), 3)
        self.assertEqual(task.due_date, due_date)
        self.assertEqual(task.recurrence, "weekly")
        self.assertFalse(task.completed)
    
    def test_task_priorities_functionality(self):
        """
        Test the priority functionality with all three levels: high, medium, low.
        """
        # Add tasks with different priorities
        high_task = self.manager.add_task("High priority task", priority="high")
        medium_task = self.manager.add_task("Medium priority task", priority="medium")
        low_task = self.manager.add_task("Low priority task", priority="low")
        
        # Verify priorities are set correctly
        self.assertEqual(high_task.priority, "high")
        self.assertEqual(medium_task.priority, "medium")
        self.assertEqual(low_task.priority, "low")
        
        # Test updating priority
        updated_task = self.manager.update_task(medium_task.id, priority="high")
        self.assertEqual(updated_task.priority, "high")
        
        # Test priority validation
        with self.assertRaises(ValueError):
            self.manager.add_task("Invalid priority task", priority="critical")
    
    def test_task_tags_functionality(self):
        """
        Test the tags functionality: adding, removing, preventing duplicates.
        """
        # Add task with tags
        task = self.manager.add_task("Task with tags", tags=["work", "urgent", "work"])  # Intentional duplicate
        
        # Verify duplicates were removed
        self.assertIn("work", task.tags)
        self.assertIn("urgent", task.tags)
        self.assertEqual(len(task.tags), 2)  # Only 2 unique tags
        
        # Update tags
        updated_task = self.manager.update_task(task.id, tags=["personal", "health", "work"])
        self.assertIn("personal", updated_task.tags)
        self.assertIn("health", updated_task.tags)
        self.assertIn("work", updated_task.tags)
        self.assertEqual(len(updated_task.tags), 3)
    
    def test_due_dates_functionality(self):
        """
        Test due date functionality: setting, updating, and clearing.
        """
        due_date = datetime(2025, 6, 15, 10, 0)
        
        # Add task with due date
        task = self.manager.add_task("Task with due date", due_date=due_date)
        self.assertEqual(task.due_date, due_date)
        
        # Update due date
        new_due_date = datetime(2025, 7, 20, 14, 30)
        updated_task = self.manager.update_task(task.id, due_date_str="2025-07-20 14:30")
        self.assertEqual(updated_task.due_date, new_due_date)
        
        # Clear due date
        cleared_task = self.manager.update_task(task.id, due_date_str="")
        self.assertIsNone(cleared_task.due_date)
    
    def test_recurring_tasks_daily(self):
        """
        Test daily recurring task functionality.
        """
        initial_count = len(self.manager.list_tasks())
        
        # Add a daily recurring task
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
    
    def test_recurring_tasks_weekly(self):
        """
        Test weekly recurring task functionality.
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
        # The new task should have an updated due date (advanced by 7 days for weekly pattern)
        expected_new_date = due_date + timedelta(days=7)
        self.assertEqual(new_task.due_date.date(), expected_new_date.date())
    
    def test_recurring_tasks_monthly(self):
        """
        Test monthly recurring task functionality.
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
        # The new task should have an updated due date (advanced by 1 month for monthly pattern)
        # (Note: This test assumes the advance_date_by_pattern function handles month boundaries correctly)
        self.assertEqual(new_task.due_date.month, 2)  # February
        self.assertEqual(new_task.due_date.day, 15)   # Same day of month
        self.assertEqual(new_task.due_date.year, 2024)
    
    def test_overdue_task_detection(self):
        """
        Test overdue task detection functionality.
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
        
        # Add a completed task with past due date (should not be considered overdue)
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
    
    def test_search_functionality(self):
        """
        Test search functionality for finding tasks by keyword.
        """
        # Add tasks with different content
        task1 = self.manager.add_task("Meeting with team", "Discuss project timeline", "high", ["work", "meeting"])
        task2 = self.manager.add_task("Buy groceries", "Milk, bread, eggs", "medium", ["personal", "errands"])
        task3 = self.manager.add_task("Complete project", "Finish the todo app project", "high", ["work", "project"])
        
        # Search by keyword in title
        results = self.manager.search_tasks("meeting")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, task1.id)
        
        # Search by keyword in description
        results = self.manager.search_tasks("project")
        self.assertEqual(len(results), 2)  # task1 and task3 contain "project"
        task_ids = [t.id for t in results]
        self.assertIn(task1.id, task_ids)
        self.assertIn(task3.id, task_ids)
        
        # Search by keyword in tags
        results = self.manager.search_tasks("work")
        self.assertEqual(len(results), 2)  # task1 and task3 have "work" in tags
        task_ids = [t.id for t in results]
        self.assertIn(task1.id, task_ids)
        self.assertIn(task3.id, task_ids)
    
    def test_filter_functionality(self):
        """
        Test filtering functionality by status, priority, and tags.
        """
        # Add tasks with different attributes
        task1 = self.manager.add_task("High priority task", "Important task", "high", ["work", "urgent"])
        task2 = self.manager.add_task("Low priority task", "Less important", "low", ["personal"])
        task3 = self.manager.add_task("Medium priority task", "Regular task", "medium", ["work"])
        
        # Filter by priority
        high_priority_tasks = self.manager.filter_tasks(priority="high")
        self.assertEqual(len(high_priority_tasks), 1)
        self.assertEqual(high_priority_tasks[0].id, task1.id)
        
        # Filter by status (all should be pending initially)
        pending_tasks = self.manager.filter_tasks(status="pending")
        self.assertEqual(len(pending_tasks), 3)
        
        # Complete a task and filter by status
        self.manager.toggle_task_completion(task2.id)
        completed_tasks = self.manager.filter_tasks(status="completed")
        self.assertEqual(len(completed_tasks), 1)
        self.assertEqual(completed_tasks[0].id, task2.id)
        
        # Filter by tags
        work_tasks = self.manager.filter_tasks(tags=["work"])
        self.assertEqual(len(work_tasks), 2)  # task1 and task3 have "work" tag
        task_ids = [t.id for t in work_tasks]
        self.assertIn(task1.id, task_ids)
        self.assertIn(task3.id, task_ids)
    
    def test_sort_functionality(self):
        """
        Test sorting functionality by different criteria.
        """
        # Add tasks with different attributes for sorting
        task1 = self.manager.add_task("Zebra task", "Last alphabetically", "low", [], datetime(2025, 12, 31))
        task2 = self.manager.add_task("Alpha task", "First alphabetically", "high", [], datetime(2024, 1, 1))
        task3 = self.manager.add_task("Middle task", "Middle alphabetically", "medium", [], datetime(2024, 6, 15))
        
        all_tasks = [task1, task2, task3]
        
        # Sort by ID (default order)
        sorted_by_id = self.manager.sort_tasks(all_tasks, "id")
        self.assertEqual(sorted_by_id[0].id, min(task1.id, task2.id, task3.id))
        self.assertEqual(sorted_by_id[-1].id, max(task1.id, task2.id, task3.id))
        
        # Sort by priority (high > medium > low)
        sorted_by_priority = self.manager.sort_tasks(all_tasks, "priority")
        self.assertEqual(sorted_by_priority[0].priority, "high")
        self.assertEqual(sorted_by_priority[-1].priority, "low")
        
        # Sort alphabetically by title
        sorted_alphabetically = self.manager.sort_tasks(all_tasks, "alpha")
        titles = [t.title for t in sorted_alphabetically]
        self.assertEqual(titles, sorted(titles))
        
        # Sort by due date
        sorted_by_due = self.manager.sort_tasks(all_tasks, "due")
        # The task with the earliest due date should be first
        self.assertEqual(sorted_by_due[0].due_date, task2.due_date)  # Earliest date
        self.assertEqual(sorted_by_due[-1].due_date, task1.due_date)  # Latest date
    
    def test_integration_scenario_full_workflow(self):
        """
        Test a full workflow integrating multiple features together.
        """
        # Add several tasks with different attributes
        task1 = self.manager.add_task(
            "Complete project proposal",
            "Finish the project proposal document for client review",
            "high",
            ["work", "urgent", "client"],
            datetime(2024, 2, 1, 10, 0),
            "none"
        )
        
        task2 = self.manager.add_task(
            "Buy groceries",
            "Milk, bread, eggs, fruits",
            "medium",
            ["personal", "errands"],
            datetime(2024, 1, 25, 18, 0),
            "weekly"
        )
        
        task3 = self.manager.add_task(
            "Schedule team meeting",
            "Coordinate with team members for project sync",
            "medium",
            ["work", "meeting"],
            datetime(2024, 1, 30, 14, 0),
            "none"
        )
        
        # Verify all tasks were added
        all_tasks = self.manager.list_tasks()
        self.assertEqual(len(all_tasks), 3)
        
        # Search for tasks containing "project"
        project_tasks = self.manager.search_tasks("project")
        self.assertEqual(len(project_tasks), 2)  # task1 and task3 contain "project"
        
        # Filter for high priority work tasks
        high_work_tasks = self.manager.filter_tasks(priority="high", tags=["work"])
        self.assertEqual(len(high_work_tasks), 1)
        self.assertEqual(high_work_tasks[0].id, task1.id)
        
        # Sort by due date
        sorted_tasks = self.manager.sort_tasks(all_tasks, "due")
        # task2 has the earliest due date
        self.assertEqual(sorted_tasks[0].id, task2.id)
        
        # Complete the recurring task (should create a new instance)
        initial_count = len(self.manager.list_tasks())
        completed_task = self.manager.toggle_task_completion(task2.id)
        self.assertTrue(completed_task.completed)
        
        # Verify a new instance was created
        final_count = len(self.manager.list_tasks())
        self.assertEqual(final_count, initial_count + 1)
        
        # Update the non-recurring task
        updated_task = self.manager.update_task(
            task1.id,
            title="Completed project proposal",
            priority="low",
            due_date_str="2024-02-15 17:00"
        )
        self.assertEqual(updated_task.title, "Completed project proposal")
        self.assertEqual(updated_task.priority, "low")
        self.assertEqual(updated_task.due_date, datetime(2024, 2, 15, 17, 0))
    
    def test_edge_cases_and_error_handling(self):
        """
        Test edge cases and error handling.
        """
        # Attempt to update non-existent task
        result = self.manager.update_task(999, title="Non-existent task")
        self.assertIsNone(result)
        
        # Attempt to delete non-existent task
        result = self.manager.delete_task(999)
        self.assertFalse(result)
        
        # Attempt to get non-existent task
        result = self.manager.get_task_by_id(999)
        self.assertIsNone(result)
        
        # Attempt to complete non-existent task
        result = self.manager.toggle_task_completion(999)
        self.assertIsNone(result)
        
        # Attempt to add task with empty title
        with self.assertRaises(ValueError):
            self.manager.add_task("", "Description for empty title task")
        
        # Attempt to add task with invalid priority
        with self.assertRaises(ValueError):
            self.manager.add_task("Invalid priority task", priority="superhigh")
        
        # Attempt to add task with invalid recurrence
        with self.assertRaises(ValueError):
            self.manager.add_task("Invalid recurrence task", recurrence="yearly")
        
        # Test with empty task list
        empty_tasks = self.manager.list_tasks()
        self.assertEqual(len(empty_tasks), 0)
        
        # Add a task and then delete it, then verify list is empty again
        task = self.manager.add_task("Temporary task")
        self.manager.delete_task(task.id)
        empty_tasks_after_delete = self.manager.list_tasks()
        self.assertEqual(len(empty_tasks_after_delete), 0)


if __name__ == '__main__':
    unittest.main()
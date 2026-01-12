from typing import List, Optional
from datetime import datetime, timedelta
import calendar
from models import Task


class TodoManager:
    """
    Core CRUD logic for managing tasks in memory with methods for add, update, delete, complete, and list operations.
    Enhanced with due date and recurrence functionality.
    """

    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, title: str, description: Optional[str] = None, priority: str = "medium", tags: Optional[list[str]] = None, due_date_str: Optional[str] = None, recurrence: str = "none") -> Task:
        """
        Add a new task with a unique sequential ID and additional attributes.

        Args:
            title: The task title (required)
            description: The task description (optional)
            priority: The task priority ("high", "medium", "low", default "medium")
            tags: List of tags for the task (default empty list)
            due_date_str: String representation of due date in format "YYYY-MM-DD [HH:MM]" (default None)
            recurrence: Recurrence pattern ("none", "daily", "weekly", "monthly", default "none")

        Returns:
            The newly created Task object
        """
        if tags is None:
            tags = []

        # Validate priority
        if priority not in ["high", "medium", "low"]:
            raise ValueError(f"Priority must be one of 'high', 'medium', 'low', got '{priority}'")

        # Validate recurrence
        if recurrence not in ["none", "daily", "weekly", "monthly"]:
            raise ValueError(f"Recurrence must be one of 'none', 'daily', 'weekly', 'monthly', got '{recurrence}'")

        # Handle due date - can be either a string or a datetime object
        due_date = None
        if due_date_str:
            if isinstance(due_date_str, datetime):
                # If it's already a datetime object, use it directly
                due_date = due_date_str
            elif isinstance(due_date_str, str):
                # If it's a string, parse it
                try:
                    # Try parsing with time first
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
                except ValueError:
                    try:
                        # Try parsing date only (default to 23:59)
                        date_part = datetime.strptime(due_date_str, "%Y-%m-%d")
                        due_date = date_part.replace(hour=23, minute=59)
                    except ValueError:
                        raise ValueError(f"Invalid date format: '{due_date_str}'. Expected format: YYYY-MM-DD [HH:MM]")
            else:
                raise ValueError(f"Due date must be a string or datetime object, got {type(due_date_str)}")

        # Remove duplicate tags while preserving order
        unique_tags = []
        for tag in tags:
            if tag not in unique_tags:
                unique_tags.append(tag)

        task = Task(
            id=self.next_id,
            title=title,
            description=description,
            completed=False,
            priority=priority,
            tags=unique_tags,
            due_date=due_date,
            recurrence=recurrence
        )
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self) -> List[Task]:
        """
        Return all tasks in the system.

        Returns:
            List of all Task objects
        """
        return self.tasks

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None, priority: Optional[str] = None, tags: Optional[list[str]] = None, due_date_str: Optional[str] = None, recurrence: Optional[str] = None) -> Optional[Task]:
        """
        Update an existing task's title, description, priority, tags, due date and/or recurrence.

        Args:
            task_id: The ID of the task to update
            title: New title (or None to keep current)
            description: New description (or None to keep current)
            priority: New priority (or None to keep current)
            tags: New tags list (or None to keep current)
            due_date_str: New due date string (or None to keep current)
            recurrence: New recurrence pattern (or None to keep current)

        Returns:
            The updated Task object, or None if task not found
        """
        for task in self.tasks:
            if task.id == task_id:
                if title is not None:
                    task.title = title
                if description is not None:
                    task.description = description
                if priority is not None:
                    if priority not in ["high", "medium", "low"]:
                        raise ValueError(f"Priority must be one of 'high', 'medium', 'low', got '{priority}'")
                    task.priority = priority
                if tags is not None:
                    # Remove duplicate tags while preserving order
                    unique_tags = []
                    for tag in tags:
                        if tag not in unique_tags:
                            unique_tags.append(tag)
                    task.tags = unique_tags
                if due_date_str is not None:
                    if due_date_str:  # If not empty string
                        if isinstance(due_date_str, datetime):
                            # If it's already a datetime object, use it directly
                            task.due_date = due_date_str
                        elif isinstance(due_date_str, str):
                            # If it's a string, parse it
                            try:
                                # Try parsing with time first
                                due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
                            except ValueError:
                                try:
                                    # Try parsing date only (default to 23:59)
                                    date_part = datetime.strptime(due_date_str, "%Y-%m-%d")
                                    due_date = date_part.replace(hour=23, minute=59)
                                except ValueError:
                                    raise ValueError(f"Invalid date format: '{due_date_str}'. Expected format: YYYY-MM-DD [HH:MM]")
                            task.due_date = due_date
                        else:
                            raise ValueError(f"Due date must be a string or datetime object, got {type(due_date_str)}")
                    else:  # Empty string means clear the due date
                        task.due_date = None
                if recurrence is not None:
                    if recurrence not in ["none", "daily", "weekly", "monthly"]:
                        raise ValueError(f"Recurrence must be one of 'none', 'daily', 'weekly', 'monthly', got '{recurrence}'")
                    task.recurrence = recurrence
                return task
        return None

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if task was deleted, False if not found
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False

    def toggle_task_completion(self, task_id: int) -> Optional[Task]:
        """
        Toggle the completion status of a task.
        If the task is recurring, create a new instance with updated due date based on recurrence pattern.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            The updated Task object, or None if task not found
        """
        for task in self.tasks:
            if task.id == task_id:
                # If the task is being marked as complete and it's recurring with a due date
                if not task.completed and task.recurrence != "none" and task.due_date:
                    task.completed = True  # Mark the current task as complete

                    # Create a new instance based on the recurrence pattern
                    new_task = self._create_recurring_instance(task)
                    self.tasks.append(new_task)

                    return task  # Return the original completed task
                else:
                    # For non-recurring tasks or when marking incomplete, just toggle
                    task.completed = not task.completed
                    return task
        return None

    def _create_recurring_instance(self, original_task: Task) -> Task:
        """
        Create a new task instance based on the recurrence pattern of the original task.

        Args:
            original_task: The original task that was completed

        Returns:
            A new Task object with updated due date based on recurrence pattern
        """
        # Calculate the new due date based on the recurrence pattern
        new_due_date = None
        if original_task.due_date:
            if original_task.recurrence == "daily":
                new_due_date = original_task.due_date + timedelta(days=1)
            elif original_task.recurrence == "weekly":
                new_due_date = original_task.due_date + timedelta(days=7)
            elif original_task.recurrence == "monthly":
                # Add one month to the due date
                year = original_task.due_date.year
                month = original_task.due_date.month
                day = original_task.due_date.day

                # Calculate next month
                if month == 12:
                    month = 1
                    year += 1
                else:
                    month += 1

                # Handle month-end edge cases (e.g., Jan 31 -> Feb 28/29)
                max_day = calendar.monthrange(year, month)[1]
                if day > max_day:
                    day = max_day

                new_due_date = original_task.due_date.replace(year=year, month=month, day=day)

        # Create a new task with the next available ID
        new_task = Task(
            id=self.next_id,
            title=original_task.title,
            description=original_task.description,
            completed=False,  # New task starts as incomplete
            priority=original_task.priority,
            tags=original_task.tags.copy(),
            due_date=new_due_date,
            recurrence=original_task.recurrence  # Preserve the recurrence pattern
        )

        # Increment the next ID
        self.next_id += 1

        return new_task

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object, or None if not found
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_overdue_tasks(self) -> List[Task]:
        """
        Get all tasks that are overdue (due date in the past and not completed).

        Returns:
            List of Task objects that have a due date in the past and are not completed
        """
        now = datetime.now()
        overdue_tasks = []
        for task in self.tasks:
            if task.due_date and task.due_date < now and not task.completed:
                overdue_tasks.append(task)
        return overdue_tasks

    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Find tasks containing the keyword in title or description (case-insensitive partial match).

        Args:
            keyword: The keyword to search for

        Returns:
            List of Task objects that contain the keyword in title or description
        """
        keyword_lower = keyword.lower()
        matching_tasks = []
        for task in self.tasks:
            # Check if keyword is in title or description (case-insensitive)
            if (task.title and keyword_lower in task.title.lower()) or \
               (task.description and keyword_lower in task.description.lower()):
                matching_tasks.append(task)
        return matching_tasks

    def filter_tasks(self, status: Optional[str] = None, priority: Optional[str] = None, tags: Optional[list[str]] = None, overdue_only: bool = False) -> List[Task]:
        """
        Filter tasks by status, priority, tags, and/or overdue status with AND logic for multiple tags.

        Args:
            status: Filter by status ("pending", "completed", "all", default None - no filter)
            priority: Filter by priority ("high", "medium", "low", "all", default None - no filter)
            tags: Filter by tags (tasks must have ALL specified tags, default None - no filter)
            overdue_only: Filter to show only overdue tasks (default False)

        Returns:
            List of Task objects that match all specified filter criteria
        """
        filtered_tasks = []
        for task in self.tasks:
            # Apply status filter
            if status and status != "all":
                if status == "pending" and task.completed:
                    continue
                elif status == "completed" and not task.completed:
                    continue

            # Apply priority filter
            if priority and priority != "all":
                if task.priority != priority:
                    continue

            # Apply tags filter (AND logic - task must have ALL specified tags)
            if tags:
                if not all(tag in task.tags for tag in tags):
                    continue

            # Apply overdue filter
            if overdue_only:
                now = datetime.now()
                if not (task.due_date and task.due_date < now and not task.completed):
                    continue

            filtered_tasks.append(task)

        return filtered_tasks

    def sort_tasks(self, tasks: List[Task], criterion: str) -> List[Task]:
        """
        Sort tasks by the specified criterion.

        Args:
            tasks: List of tasks to sort
            criterion: Sort criterion ("id", "priority", "alpha", "due")

        Returns:
            Sorted list of Task objects based on the specified criterion
        """
        if criterion == "id":
            # Sort by ID (default order)
            return sorted(tasks, key=lambda t: t.id)
        elif criterion == "priority":
            # Define priority order: high > medium > low
            priority_order = {"high": 0, "medium": 1, "low": 2}
            # Sort by priority first, then by ID for stability
            return sorted(tasks, key=lambda t: (priority_order[t.priority], t.id))
        elif criterion == "alpha":
            # Sort alphabetically by title (case-insensitive), then by ID for stability
            return sorted(tasks, key=lambda t: (t.title.lower(), t.id))
        elif criterion == "due":
            # Sort by due date: overdue tasks first, then by due date, then by ID
            now = datetime.now()
            def due_sort_key(task):
                # If no due date, put at the end
                if task.due_date is None:
                    return (2, 0, task.id)  # (group, timestamp, id) - group 2 for no due date

                # If overdue, group 0
                if task.due_date < now and not task.completed:
                    return (0, task.due_date.timestamp(), task.id)  # group 0 for overdue

                # If has due date but not overdue, group 1
                return (1, task.due_date.timestamp(), task.id)  # group 1 for not overdue

            return sorted(tasks, key=due_sort_key)
        else:
            # Default to ID sort if invalid criterion
            return sorted(tasks, key=lambda t: t.id)


class TaskFilter:
    """
    Represents filter criteria for status, priority, tags, and overdue status with methods to apply filters to task lists.
    """

    def __init__(self, status: Optional[str] = None, priority: Optional[str] = None, tags: Optional[list[str]] = None, overdue_only: bool = False):
        self.status = status
        self.priority = priority
        self.tags = tags
        self.overdue_only = overdue_only

    def apply(self, tasks: List[Task]) -> List[Task]:
        """
        Applies all active filters to the list of tasks.

        Args:
            tasks: List of Task objects to filter

        Returns:
            Filtered list of Task objects
        """
        filtered_tasks = []
        now = datetime.now()
        for task in tasks:
            # Apply status filter
            if self.status and self.status != "all":
                if self.status == "pending" and task.completed:
                    continue
                elif self.status == "completed" and not task.completed:
                    continue

            # Apply priority filter
            if self.priority and self.priority != "all":
                if task.priority != self.priority:
                    continue

            # Apply tags filter (AND logic - task must have ALL specified tags)
            if self.tags:
                if not all(tag in task.tags for tag in self.tags):
                    continue

            # Apply overdue filter
            if self.overdue_only:
                if not (task.due_date and task.due_date < now and not task.completed):
                    continue

            filtered_tasks.append(task)

        return filtered_tasks


class TaskSorter:
    """
    Represents sorting criteria and methods to sort task lists by different attributes.
    """

    def __init__(self, criterion: str = "id"):
        self.criterion = criterion  # "id", "priority", "alpha", or "due"

    def sort(self, tasks: List[Task]) -> List[Task]:
        """
        Sorts tasks by the specified criterion using stable sort to maintain consistent ordering.

        Args:
            tasks: List of Task objects to sort

        Returns:
            Sorted list of Task objects
        """
        if self.criterion == "id":
            # Sort by ID (default order)
            return sorted(tasks, key=lambda t: t.id)
        elif self.criterion == "priority":
            # Define priority order: high > medium > low
            priority_order = {"high": 0, "medium": 1, "low": 2}
            # Sort by priority first, then by ID for stability
            return sorted(tasks, key=lambda t: (priority_order[t.priority], t.id))
        elif self.criterion == "alpha":
            # Sort alphabetically by title (case-insensitive), then by ID for stability
            return sorted(tasks, key=lambda t: (t.title.lower(), t.id))
        elif self.criterion == "due":
            # Sort by due date: overdue tasks first, then by due date, then by ID
            now = datetime.now()
            def due_sort_key(task):
                # If no due date, put at the end
                if task.due_date is None:
                    return (2, 0, task.id)  # (group, timestamp, id) - group 2 for no due date

                # If overdue, group 0
                if task.due_date < now and not task.completed:
                    return (0, task.due_date.timestamp(), task.id)  # group 0 for overdue

                # If has due date but not overdue, group 1
                return (1, task.due_date.timestamp(), task.id)  # group 1 for not overdue

            return sorted(tasks, key=due_sort_key)
        else:
            # Default to ID sort if invalid criterion
            return sorted(tasks, key=lambda t: t.id)
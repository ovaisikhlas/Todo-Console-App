# Data Model: Todo App Advanced Level - Intelligent Features

## Entity: Task

### Fields
- **id** (int, required, auto-increment)
  - Unique sequential identifier for the task
  - Starts from 1 and increments for each new task
  - Allows gaps in sequence after deletions
  - Primary identifier for all CRUD operations

- **title** (str, required)
  - Task title with unlimited length
  - Required field for all tasks
  - Displayed in table view
  - Can be updated by user

- **description** (str, optional)
  - Optional task description
  - May be None if not provided
  - Truncated to 40 characters + "..." in table view
  - Can be updated by user

- **completed** (bool, default False)
  - Task completion status
  - False by default when task is created
  - Toggled between True/False via complete command
  - Displayed as [ ] or [x] in table view

- **priority** (str, default "medium")
  - Task priority level (high, medium, low)
  - "medium" by default when task is created
  - Can be updated by user
  - Displayed in table view

- **tags** (list[str], default empty list)
  - List of tags associated with the task
  - Empty list by default when task is created
  - Can be updated by user (add, remove, replace)
  - Duplicates automatically prevented
  - Displayed comma-separated in table view

- **due_date** (Optional[datetime.datetime], default None)
  - Optional due date/time for the task
  - None by default when task is created
  - Can be set/updated by user
  - Displayed in table view as "YYYY-MM-DD HH:MM" or "None"
  - Used for overdue detection and sorting

- **recurrence** (str, default "none")
  - Recurrence pattern for the task (none, daily, weekly, monthly)
  - "none" by default when task is created
  - Can be set/updated by user
  - Determines if a new task is created upon completion
  - Not displayed directly in table view but affects behavior

### Validation Rules
- Title must be provided (non-empty after stripping whitespace)
- ID must be unique within the system
- ID must be a positive integer
- Completed status must be boolean
- Priority must be one of "high", "medium", "low"
- Tags must be a list of strings
- Duplicate tags within the same task are prevented
- Due date must be a valid date if provided (not in the past relative to creation for some business rules, though this isn't enforced for flexibility)
- Recurrence must be one of "none", "daily", "weekly", "monthly"

### State Transitions
- **Creation**: id (auto-assigned), title (required), description (optional), completed (False), priority (default "medium"), tags (default []), due_date (default None), recurrence (default "none")
- **Completion Toggle**: completed (False → True or True → False)
- **Priority Update**: priority changed to one of "high", "medium", "low"
- **Tag Update**: tags list modified (additions, removals, or replacements)
- **Due Date Update**: due_date changed to new datetime or None
- **Recurrence Update**: recurrence changed to one of "none", "daily", "weekly", "monthly"
- **Recurring Completion**: When completed and recurrence != "none", a new task is created with updated due date based on pattern
- **Update**: title, description, priority, tags, due_date, and/or recurrence updated while preserving other fields
- **Deletion**: Task removed from storage (ID gap remains)

### Relationships
- No direct relationships with other entities
- Referenced by ID in all operations
- Stored in a list within TodoManager

## Entity: TodoManager

### Fields
- **_tasks** (List[Task], private)
  - Internal storage of all tasks
  - Maintains order of creation
  - Provides O(n) lookup by ID

- **_next_id** (int, private)
  - Tracks the next ID to assign
  - Incremented after each new task creation
  - Maintains sequential nature of IDs

### Operations
- **add_task(title: str, description: str = None, priority: str = "medium", tags: list[str] = None, due_date: datetime.datetime = None, recurrence: str = "none") -> Task**
  - Creates new task with next available ID and specified attributes
  - Returns the created task

- **list_tasks() -> List[Task]**
  - Returns all tasks in storage
  - Maintains creation order

- **get_task_by_id(task_id: int) -> Task | None**
  - Finds task by ID
  - Returns None if not found

- **update_task(task_id: int, title: str = None, description: str = None, priority: str = None, tags: list[str] = None, due_date: datetime.datetime = None, recurrence: str = None) -> Task | None**
  - Updates task fields if provided
  - Returns updated task or None if not found

- **delete_task(task_id: int) -> bool**
  - Removes task by ID
  - Returns True if successful, False if not found

- **toggle_task_completion(task_id: int) -> Task | None**
  - Toggles completed status of task
  - If task is recurring, creates a new instance with updated due date based on recurrence pattern
  - Returns updated task or None if not found

- **search_tasks(keyword: str) -> List[Task]**
  - Finds tasks containing the keyword in title or description
  - Returns list of matching tasks (case-insensitive partial match)

- **filter_tasks(status: str = None, priority: str = None, tags: list[str] = None, overdue_only: bool = False) -> List[Task]**
  - Filters tasks by status, priority, tags, and/or overdue status
  - Supports AND logic for multiple tags
  - Returns list of matching tasks

- **sort_tasks(tasks: List[Task], criterion: str) -> List[Task]**
  - Sorts tasks by specified criterion
  - Supports "id", "priority", "alpha", "due" (by due date)
  - Returns sorted list of tasks

- **get_overdue_tasks() -> List[Task]**
  - Returns tasks with due date in the past and not completed
  - Compares against current system time (datetime.now())

- **handle_recurrence(task_id: int) -> Task | None**
  - Creates a new task instance based on recurrence pattern of completed task
  - Advances due date according to pattern (daily: +1 day, weekly: +7 days, monthly: +1 month)
  - Returns the new task instance or None if not recurring

## Entity: TaskFilter

### Fields
- **status** (str, optional)
  - Filter by task status ("pending", "completed", "all")
  - Default is None (no filter)

- **priority** (str, optional)
  - Filter by task priority ("high", "medium", "low", "all")
  - Default is None (no filter)

- **tags** (list[str], optional)
  - Filter by task tags (tasks must have ALL specified tags)
  - Default is None (no filter)

- **overdue_only** (bool, default False)
  - Filter to show only overdue tasks
  - Default is False (no filter)

### Operations
- **apply(tasks: List[Task]) -> List[Task]**
  - Applies all active filters to the list of tasks
  - Returns filtered list of tasks

## Entity: TaskSorter

### Fields
- **criterion** (str)
  - Sorting criterion ("id", "priority", "alpha", "due")
  - Default is "id" (by creation order)

### Operations
- **sort(tasks: List[Task]) -> List[Task]**
  - Sorts tasks by the specified criterion
  - Returns sorted list of tasks
  - Uses stable sort to maintain consistent ordering
  - For "due" criterion: overdue tasks first, then by due date, then by ID
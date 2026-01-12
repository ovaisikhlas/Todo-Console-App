# Data Model: In-Memory Console Todo App

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

### Validation Rules
- Title must be provided (non-empty after stripping whitespace)
- ID must be unique within the system
- ID must be a positive integer
- Completed status must be boolean

### State Transitions
- **Creation**: id (auto-assigned), title (required), description (optional), completed (False)
- **Completion Toggle**: completed (False → True or True → False)
- **Update**: title and/or description updated while preserving other fields
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
- **add_task(title: str, description: str = None) -> Task**
  - Creates new task with next available ID
  - Returns the created task

- **list_tasks() -> List[Task]**
  - Returns all tasks in storage
  - Maintains creation order

- **get_task_by_id(task_id: int) -> Task | None**
  - Finds task by ID
  - Returns None if not found

- **update_task(task_id: int, title: str = None, description: str = None) -> Task | None**
  - Updates task fields if provided
  - Returns updated task or None if not found

- **delete_task(task_id: int) -> bool**
  - Removes task by ID
  - Returns True if successful, False if not found

- **toggle_task_completion(task_id: int) -> Task | None**
  - Toggles completed status of task
  - Returns updated task or None if not found
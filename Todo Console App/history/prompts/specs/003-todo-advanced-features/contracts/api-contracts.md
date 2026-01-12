# API Contracts: Todo App Advanced Level - Intelligent Features

## Overview
This document defines the contracts between the CLI layer and the TodoManager business logic layer for the Advanced Level features. These interfaces ensure proper separation of concerns and define the expected behavior of each component with the new intelligent features (recurring tasks and due dates).

## TodoManager Interface

### Task Creation (Enhanced)
```
add_task(title: str, description: str = None, priority: str = "medium", tags: list[str] = None, due_date_str: str = None, recurrence: str = "none") -> Task
```
- **Purpose**: Create a new task with a unique sequential ID and additional attributes including due date and recurrence pattern
- **Preconditions**: 
  - `title` must be a non-empty string after stripping whitespace
  - `priority` must be one of "high", "medium", "low"
  - `tags` must be a list of strings (duplicates will be removed)
  - `due_date_str` must be in format YYYY-MM-DD [HH:MM] or None
  - `recurrence` must be one of "none", "daily", "weekly", "monthly"
- **Postconditions**:
  - A new Task object is created with the next available ID
  - The task is added to the internal storage
  - The task's `completed` field is set to `False`
  - The task's `priority` field is set to the specified value (default "medium")
  - The task's `tags` field is set to the specified list (with duplicates removed)
  - The task's `due_date` field is set based on parsing `due_date_str` (default None)
  - The task's `recurrence` field is set to the specified value (default "none")
  - The `_next_id` is incremented
- **Returns**: The newly created Task object
- **Exceptions**: ValueError if title is empty after stripping, invalid priority, invalid recurrence pattern, or invalid date format

### Task Completion with Recurrence Handling
```
toggle_task_completion(task_id: int) -> Task | None
```
- **Purpose**: Toggle completion status of a task, with special handling for recurring tasks
- **Preconditions**: `task_id` must be a positive integer
- **Postconditions**:
  - If task exists and is not recurring: `completed` field toggled
  - If task exists and is recurring with due_date set: 
    - Original task marked as completed
    - New task instance created with updated due date based on recurrence pattern
    - New task gets next available ID
  - If task exists and is recurring without due_date: Just mark as completed (no new instance)
- **Returns**: The updated Task object if successful, None if task not found
- **Special behavior**: For recurring tasks, creates new instance with updated due date based on pattern (daily: +1 day, weekly: +7 days, monthly: +1 month preserving day)

### Task Filtering with Due Date Awareness
```
filter_tasks(status: str = None, priority: str = None, tags: list[str] = None, overdue_only: bool = False) -> List[Task]
```
- **Purpose**: Filter tasks by multiple criteria including overdue status
- **Preconditions**: 
  - `status` must be one of "pending", "completed", "all", or None
  - `priority` must be one of "high", "medium", "low", "all", or None
  - `tags` must be a list of strings (tasks must have ALL specified tags)
  - `overdue_only` is a boolean indicating whether to show only overdue tasks
- **Postconditions**: None
- **Returns**: A list of Task objects that match all specified filter criteria
- **Special handling**: When `overdue_only` is True, only tasks with due_date in the past and not completed are returned

### Task Sorting with Due Date Support
```
sort_tasks(tasks: List[Task], criterion: str) -> List[Task]
```
- **Purpose**: Sort tasks by the specified criterion, with special handling for due dates
- **Preconditions**: 
  - `tasks` is a list of Task objects
  - `criterion` is one of "id", "priority", "alpha", "due"
- **Postconditions**: None
- **Returns**: A sorted list of Task objects based on the specified criterion
- **Special handling**: 
  - For "due" criterion: overdue tasks first, then by due date (earliest first), then by ID
  - For other criteria: standard sorting behavior

### Overdue Task Detection
```
get_overdue_tasks() -> List[Task]
```
- **Purpose**: Get all tasks that are overdue (due date in the past and not completed)
- **Preconditions**: None
- **Postconditions**: None
- **Returns**: A list of Task objects that have a due date in the past and are not marked as completed

### Recurrence Handling
```
handle_recurrence(task_id: int) -> Task | None
```
- **Purpose**: Create a new task instance based on the recurrence pattern of a completed task
- **Preconditions**: 
  - `task_id` must be a positive integer
  - The task with this ID must exist and be recurring
  - The task must have a due date set
- **Postconditions**:
  - A new task instance is created with updated due date based on recurrence pattern
  - The new task gets the next available ID
  - The new task preserves title, description, priority, tags, and recurrence pattern
- **Returns**: The new Task object if successful, None if task not found or not recurring
- **Date advancement**:
  - Daily: current due date + 1 day
  - Weekly: current due date + 7 days
  - Monthly: current due date + 1 month (preserving day if possible)

## CLI Interface

### Enhanced Command Parsing
```
parse_command(user_input: str) -> tuple
```
- **Purpose**: Parse user input into command and arguments with support for flags and options
- **Preconditions**: `user_input` is a string from user input
- **Postconditions**: None
- **Returns**: A tuple containing (command: str, args: List[str], flags: dict) where command is lowercase and whitespace-trimmed, and flags contains parsed flag options like --status, --priority, --tag (repeatable), --sort, --overdue, --search

### Enhanced Display Functions
```
display_tasks(tasks: List[Task], show_overdue: bool = True) -> None
```
- **Purpose**: Display tasks in an enhanced formatted table with due date and overdue indicators
- **Preconditions**: `tasks` is a list of Task objects
- **Postconditions**: Tasks are displayed in a formatted table with ID, Status, Priority, Due Date, Title, Tags, and Description columns
- **Side Effects**: Output to console
- **Enhanced features**: 
  - Shows Due Date column with format "YYYY-MM-DD HH:MM" or "None"
  - Appends "(OVERDUE!)" to titles of overdue tasks
  - Shows recurrence indicators for recurring tasks

### Enhanced User Interaction
```
get_user_input_with_date(prompt: str) -> str | datetime.datetime | None
```
- **Purpose**: Get input from the user with a prompt, with special handling for date input
- **Preconditions**: `prompt` is a string to display to the user
- **Postconditions**: None
- **Returns**: The user's input as a string, a datetime object if valid date format provided, or None if empty input
- **Validation**: Parses date input in format YYYY-MM-DD [HH:MM] and validates it

## Error Handling Contracts

### Invalid Date Formats
- When an invalid date format is entered, the CLI displays an appropriate error message
- The application continues running and prompts for the next command
- Example: "Invalid date format. Please use YYYY-MM-DD [HH:MM] format."

### Invalid Recurrence Patterns
- When an invalid recurrence pattern is entered, an appropriate error message is displayed
- The application continues running and prompts for the next command
- Example: "Invalid recurrence pattern. Please use one of: none, daily, weekly, monthly."

### Recurrence Processing
- When a recurring task is completed, the system creates a new instance with updated due date
- The original task remains marked as completed
- The new task gets a new ID and the same recurrence pattern
- Example: "Task completed. Next occurrence scheduled for 2026-01-29 10:00 (ID: 5)."

### Overdue Task Highlighting
- When displaying tasks, overdue tasks are highlighted with "(OVERDUE!)" indicator
- The system compares each task's due date with the current system time (datetime.now())
- Example: "Submit report [ ] high 2026-01-25 17:00 (OVERDUE!) work, urgent"

### Month Boundary Handling
- When advancing a due date monthly and the target month doesn't have the same day, the system adjusts to the last day of the month
- Example: A task due on January 31st with monthly recurrence will reschedule to February 28th (or 29th in leap years)
# API Contracts: Todo App Intermediate Level - Organization & Usability

## Overview
This document defines the contracts between the CLI layer and the TodoManager business logic layer. These interfaces ensure proper separation of concerns and define the expected behavior of each component with the new Intermediate Level features.

## TodoManager Interface

### Task Creation (Enhanced)
```
add_task(title: str, description: str = None, priority: str = "medium", tags: list[str] = None) -> Task
```
- **Purpose**: Create a new task with a unique sequential ID and additional attributes
- **Preconditions**: 
  - `title` must be a non-empty string after stripping whitespace
  - `priority` must be one of "high", "medium", "low"
  - `tags` must be a list of strings (duplicates will be removed)
- **Postconditions**:
  - A new Task object is created with the next available ID
  - The task is added to the internal storage
  - The task's `completed` field is set to `False`
  - The task's `priority` field is set to the specified value (default "medium")
  - The task's `tags` field is set to the specified list (with duplicates removed)
  - The `_next_id` is incremented
- **Returns**: The newly created Task object
- **Exceptions**: ValueError if title is empty after stripping or priority is invalid

### Task Update (Enhanced)
```
update_task(task_id: int, title: str = None, description: str = None, priority: str = None, tags: list[str] = None) -> Task | None
```
- **Purpose**: Update an existing task's title, description, priority and/or tags
- **Preconditions**: 
  - `task_id` must be a positive integer
  - If `title` is provided, it must be a non-empty string after stripping
  - If `priority` is provided, it must be one of "high", "medium", "low"
  - If `tags` is provided, it must be a list of strings (duplicates will be removed)
- **Postconditions**:
  - If `title` is provided, the task's title is updated
  - If `description` is provided, the task's description is updated
  - If `priority` is provided, the task's priority is updated
  - If `tags` is provided, the task's tags are updated (duplicates removed)
  - Other fields remain unchanged
- **Returns**: The updated Task object if successful, None if task not found
- **Exceptions**: ValueError if title is provided but is empty after stripping or priority is invalid

### Task Search
```
search_tasks(keyword: str) -> List[Task]
```
- **Purpose**: Find tasks containing the keyword in title or description
- **Preconditions**: `keyword` is a string to search for
- **Postconditions**: None
- **Returns**: A list of Task objects that contain the keyword in title or description (case-insensitive partial match)

### Task Filter
```
filter_tasks(status: str = None, priority: str = None, tags: list[str] = None) -> List[Task]
```
- **Purpose**: Filter tasks by status, priority, and/or tags
- **Preconditions**: 
  - `status` must be one of "pending", "completed", "all", or None
  - `priority` must be one of "high", "medium", "low", "all", or None
  - `tags` must be a list of strings (tasks must have ALL specified tags)
- **Postconditions**: None
- **Returns**: A list of Task objects that match all specified filter criteria

### Task Sort
```
sort_tasks(tasks: List[Task], criterion: str) -> List[Task]
```
- **Purpose**: Sort tasks by the specified criterion
- **Preconditions**: 
  - `tasks` is a list of Task objects
  - `criterion` is one of "id", "priority", "alpha"
- **Postconditions**: None
- **Returns**: A sorted list of Task objects based on the specified criterion
  - "id": by creation order (default)
  - "priority": high > medium > low, then by ID
  - "alpha": by title case-insensitive, then by ID

## CLI Interface

### Enhanced Command Parsing
```
parse_command(user_input: str) -> tuple
```
- **Purpose**: Parse user input into command and arguments with support for flags
- **Preconditions**: `user_input` is a string from user input
- **Postconditions**: None
- **Returns**: A tuple containing (command: str, args: List[str], flags: dict) where command is lowercase and whitespace-trimmed, and flags contains parsed flag options

### Enhanced Display Functions
```
display_tasks(tasks: List[Task]) -> None
```
- **Purpose**: Display tasks in an enhanced formatted table with additional columns
- **Preconditions**: `tasks` is a list of Task objects
- **Postconditions**: Tasks are displayed in a formatted table with ID, Status, Priority, Title, Tags, and Description columns
- **Side Effects**: Output to console

### Enhanced User Interaction
```
get_user_input(prompt: str) -> str
```
- **Purpose**: Get input from the user with a prompt
- **Preconditions**: `prompt` is a string to display to the user
- **Postconditions**: None
- **Returns**: The user's input as a string (not trimmed)

## Error Handling Contracts

### Invalid Commands
- When an invalid command is entered, the CLI displays an appropriate error message
- The application continues running and prompts for the next command

### Invalid IDs
- When a non-existent task ID is provided, an appropriate error message is displayed
- The application continues running and prompts for the next command

### Invalid Priority
- When an invalid priority value is provided, an appropriate error message is displayed
- The application continues running and prompts for the next command

### Empty Input
- When required input is empty, an appropriate error message is displayed
- The application continues running and prompts for the next command

### Invalid Filters
- When invalid filter values are provided, an appropriate error message is displayed
- The application continues running and prompts for the next command
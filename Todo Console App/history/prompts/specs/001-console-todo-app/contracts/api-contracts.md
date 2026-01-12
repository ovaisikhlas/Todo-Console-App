# API Contracts: In-Memory Console Todo App

## Overview
This document defines the contracts between the CLI layer and the TodoManager business logic layer. These interfaces ensure proper separation of concerns and define the expected behavior of each component.

## TodoManager Interface

### Task Creation
```
add_task(title: str, description: str = None) -> Task
```
- **Purpose**: Create a new task with a unique sequential ID
- **Preconditions**: 
  - `title` must be a non-empty string after stripping whitespace
- **Postconditions**:
  - A new Task object is created with the next available ID
  - The task is added to the internal storage
  - The task's `completed` field is set to `False`
  - The `_next_id` is incremented
- **Returns**: The newly created Task object
- **Exceptions**: ValueError if title is empty after stripping

### Task Retrieval
```
list_tasks() -> List[Task]
```
- **Purpose**: Retrieve all tasks in the system
- **Preconditions**: None
- **Postconditions**: None
- **Returns**: A list of all Task objects in creation order

### Task Lookup
```
get_task_by_id(task_id: int) -> Task | None
```
- **Purpose**: Find a task by its ID
- **Preconditions**: `task_id` must be a positive integer
- **Postconditions**: None
- **Returns**: The Task object if found, None otherwise

### Task Update
```
update_task(task_id: int, title: str = None, description: str = None) -> Task | None
```
- **Purpose**: Update an existing task's title and/or description
- **Preconditions**: 
  - `task_id` must be a positive integer
  - If `title` is provided, it must be a non-empty string after stripping
- **Postconditions**:
  - If `title` is provided, the task's title is updated
  - If `description` is provided, the task's description is updated
  - Other fields remain unchanged
- **Returns**: The updated Task object if successful, None if task not found
- **Exceptions**: ValueError if title is provided but is empty after stripping

### Task Deletion
```
delete_task(task_id: int) -> bool
```
- **Purpose**: Remove a task by its ID
- **Preconditions**: `task_id` must be a positive integer
- **Postconditions**:
  - The task is removed from internal storage
  - The ID sequence will have a gap (no ID reassignment)
- **Returns**: True if task was found and deleted, False if not found

### Task Completion Toggle
```
toggle_task_completion(task_id: int) -> Task | None
```
- **Purpose**: Toggle the completion status of a task
- **Preconditions**: `task_id` must be a positive integer
- **Postconditions**:
  - The task's `completed` field is toggled (True becomes False, False becomes True)
- **Returns**: The updated Task object if successful, None if task not found

## CLI Interface

### Command Parsing
```
parse_command(user_input: str) -> tuple
```
- **Purpose**: Parse user input into command and arguments
- **Preconditions**: `user_input` is a string from user input
- **Postconditions**: None
- **Returns**: A tuple containing (command: str, args: List[str]) where command is lowercase and whitespace-trimmed

### Display Functions
```
display_tasks(tasks: List[Task]) -> None
```
- **Purpose**: Display tasks in a formatted table
- **Preconditions**: `tasks` is a list of Task objects
- **Postconditions**: Tasks are displayed in a formatted table with proper alignment and truncation
- **Side Effects**: Output to console

### User Interaction
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

### Empty Input
- When required input is empty, an appropriate error message is displayed
- The application continues running and prompts for the next command
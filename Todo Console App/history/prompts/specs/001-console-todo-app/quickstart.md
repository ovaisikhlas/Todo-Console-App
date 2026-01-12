# Quickstart Guide: In-Memory Console Todo App

## Prerequisites
- Python 3.13+
- UV package manager

## Setup
1. Clone or download the repository
2. Install dependencies using UV:
   ```bash
   uv sync
   ```
   Or if just running directly:
   ```bash
   uv run python -m src.main
   ```

## Running the Application
To start the todo application:
```bash
uv run python -m src.main
```

## Available Commands
Once the application is running, you can use the following commands:

### `add`
- **Purpose**: Add a new task
- **Usage**: Type `add` and follow the prompts
- **Example**:
  ```
  todo> add
  Enter task title (required): Buy groceries
  Enter task description (optional, press Enter to skip): Milk, bread, eggs
  ✓ Task added with ID 1: Buy groceries
  ```

### `list`
- **Purpose**: List all tasks in a formatted table
- **Usage**: Type `list`
- **Example**:
  ```
  todo> list
  ID   Status   Title                        Description
  --------------------------------------------------------------------------------
  1    [ ]      Buy groceries               Milk, bread, eggs
  2    [x]      Complete project            Final implementation
  ```

### `update <id>`
- **Purpose**: Update an existing task by ID
- **Usage**: `update <task_id>`
- **Example**:
  ```
  todo> update 1
  Enter new title (current: 'Buy groceries', press Enter to keep current): Buy weekly groceries
  Enter new description (current: 'Milk, bread, eggs', press Enter to keep current): 
  ✓ Task 1 updated successfully.
  ```

### `delete <id>`
- **Purpose**: Delete a task by ID
- **Usage**: `delete <task_id>`
- **Example**:
  ```
  todo> delete 1
  ✓ Task 1 deleted successfully.
  ```

### `complete <id>`
- **Purpose**: Toggle completion status of a task by ID
- **Usage**: `complete <task_id>`
- **Example**:
  ```
  todo> complete 1
  Task 1 marked as complete.
  ```

### `help`
- **Purpose**: Display help information
- **Usage**: Type `help`
- **Example**:
  ```
  todo> help
  
  Available commands:
    add              - Add a new task
    list             - List all tasks
    update <id>      - Update a task by ID
    delete <id>      - Delete a task by ID
    complete <id>    - Toggle completion status of a task by ID
    help             - Show this help message
    quit/exit        - Exit the application
  ```

### `quit` or `exit`
- **Purpose**: Exit the application
- **Usage**: Type `quit` or `exit`
- **Example**:
  ```
  todo> quit
  Goodbye!
  ```

## Example Session
Here's a complete example of using the application:

```
Welcome to the In-Memory Console Todo App!
Type 'help' for available commands or 'quit'/'exit' to exit.

todo> add
Enter task title (required): Complete project proposal
Enter task description (optional, press Enter to skip): Need to finish by Friday
✓ Task added with ID 1: Complete project proposal

todo> add
Enter task title (required): Buy groceries
Enter task description (optional, press Enter to skip): 
✓ Task added with ID 2: Buy groceries

todo> list
ID   Status   Title                        Description
--------------------------------------------------------------------------------
1    [ ]      Complete project proposal    Need to finish by Friday
2    [ ]      Buy groceries               

todo> complete 1
Task 1 marked as complete.

todo> list
ID   Status   Title                        Description
--------------------------------------------------------------------------------
1    [x]      Complete project proposal    Need to finish by Friday
2    [ ]      Buy groceries               

todo> update 2
Enter new title (current: 'Buy groceries', press Enter to keep current): Buy weekly groceries
Enter new description (current: '', press Enter to keep current): Milk, bread, eggs, fruits
✓ Task 2 updated successfully.

todo> list
ID   Status   Title                        Description
--------------------------------------------------------------------------------
1    [x]      Complete project proposal    Need to finish by Friday
2    [ ]      Buy weekly groceries         Milk, bread, eggs, fruits

todo> quit
Goodbye!
```

## Notes
- All commands are case-insensitive
- Extra whitespace is trimmed from commands
- Task IDs are sequential integers starting from 1
- IDs will have gaps after deletions
- Title and description lengths are unlimited
- Data is stored in memory only and will be lost when the application exits
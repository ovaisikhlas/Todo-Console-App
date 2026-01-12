# In-Memory Console Todo App

A simple, reliable command-line todo tool for quick task management. This application implements all 5 core features (Add Task, Delete Task, Update Task, View/List Tasks, Mark as Complete/Incomplete) with a polished CLI experience.

## Setup

1. Ensure you have Python 3.13+ installed
2. Install UV package manager if you don't have it already:
   ```bash
   pip install uv
   ```
3. Clone or download this repository

## How to Run

To run the application:

```bash
uv run python -m src.main
```

## Available Commands

- `add` - Add a new task
- `list` - List all tasks
- `update <id>` - Update a task by ID
- `delete <id>` - Delete a task by ID
- `complete <id>` - Toggle completion status of a task by ID
- `help` - Show available commands and usage
- `quit`/`exit` - Exit the application

## Complete Example Interactive Session

```
$ uv run python -m src.main
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

todo> delete 1
✓ Task 1 deleted successfully.

todo> list
ID   Status   Title                        Description
--------------------------------------------------------------------------------
2    [ ]      Buy weekly groceries         Milk, bread, eggs, fruits

todo> help

Available commands:
  add              - Add a new task
  list             - List all tasks
  update <id>      - Update a task by ID
  delete <id>      - Delete a task by ID
  complete <id>    - Toggle completion status of a task by ID
  help             - Show this help message
  quit/exit        - Exit the application

todo> quit
Goodbye!
```

## Features

- Add tasks with titles and optional descriptions
- List all tasks in a clean, formatted table
- Update existing tasks by ID
- Delete tasks by ID
- Mark tasks as complete/incomplete
- Help command for available options
- Case-insensitive commands with whitespace handling
- Unique sequential IDs that maintain gaps after deletion
- Truncated descriptions (40 characters) in table view
- In-memory storage (no persistence across sessions)
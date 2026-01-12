# Quickstart Guide: Todo App Intermediate Level - Organization & Usability

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
- **Purpose**: Add a new task with title, description, priority, and tags
- **Usage**: Type `add` and follow the prompts
- **Example**:
  ```
  todo> add
  Enter task title (required): Complete project proposal
  Enter task description (optional, press Enter to skip): Need to finish by Friday
  Enter priority (high/medium/low, default: medium): high
  Enter tags (comma-separated, e.g., work,urgent): work, urgent
  ✓ Task added with ID 1: Complete project proposal
  ```

### `list`
- **Purpose**: List all tasks in a formatted table with additional columns
- **Usage**: Type `list` or use enhanced options
- **Enhanced options**:
  - `list --status pending|completed|all` - Filter by status
  - `list --priority high|medium|low|all` - Filter by priority
  - `list --tag <tag>` - Filter by tag (can be used multiple times)
  - `list --sort id|priority|alpha` - Sort by criterion
  - `list --search <keyword>` - Search by keyword
- **Examples**:
  ```
  todo> list
  ID   Status   Priority   Title                        Tags           Description
  --------------------------------------------------------------------------------
  1    [ ]      high       Complete project proposal    work, urgent   Need to finish by Friday
  2    [x]      medium     Buy groceries               personal       Milk, bread, eggs

  todo> list --priority high --sort alpha
  ID   Status   Priority   Title                        Tags           Description
  --------------------------------------------------------------------------------
  1    [ ]      high       Complete project proposal    work, urgent   Need to finish by Friday

  todo> list --search project
  ID   Status   Priority   Title                        Tags           Description
  --------------------------------------------------------------------------------
  1    [ ]      high       Complete project proposal    work, urgent   Need to finish by Friday
  ```

### `update <id>`
- **Purpose**: Update an existing task by ID
- **Usage**: `update <task_id>` and follow prompts
- **Example**:
  ```
  todo> update 1
  What would you like to update? (title/description/priority/tags/all/skip): priority
  Enter new priority (high/medium/low): low
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
    add              - Add a new task with title, description, priority, and tags
    list             - List all tasks with optional filters and sorting
      --status [pending|completed|all]  Filter by status
      --priority [high|medium|low|all]  Filter by priority
      --tag <tag>                      Filter by tag (repeatable)
      --sort [id|priority|alpha]       Sort by criterion
      --search <keyword>               Search by keyword
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
Here's a complete example of using the application with Intermediate Level features:

```
$ uv run python -m src.main
Welcome to the In-Memory Console Todo App!
Type 'help' for available commands or 'quit'/'exit' to exit.

todo> add
Enter task title (required): Complete project proposal
Enter task description (optional, press Enter to skip): Need to finish by Friday
Enter priority (high/medium/low, default: medium): high
Enter tags (comma-separated, e.g., work,urgent): work, important
✓ Task added with ID 1: Complete project proposal

todo> add
Enter task title (required): Buy groceries
Enter task description (optional, press Enter to skip): 
Enter priority (high/medium/low, default: medium): medium
Enter tags (comma-separated, e.g., work,urgent): personal, errands
✓ Task added with ID 2: Buy groceries

todo> add
Enter task title (required): Schedule team meeting
Enter task description (optional, press Enter to skip): Weekly sync
Enter priority (high/medium/low, default: medium): high
Enter tags (comma-separated, e.g., work,urgent): work, meeting
✓ Task added with ID 3: Schedule team meeting

todo> list
ID   Status   Priority   Title                      Tags              Description
--------------------------------------------------------------------------------
1    [ ]      high       Complete project proposal  work, important   Need to finish by Friday
2    [ ]      medium     Buy groceries             personal, errands  
3    [ ]      high       Schedule team meeting      work, meeting      Weekly sync

todo> list --priority high
ID   Status   Priority   Title                     Tags           Description
--------------------------------------------------------------------------------
1    [ ]      high       Complete project proposal work, important Need to finish by Friday
3    [ ]      high       Schedule team meeting     work, meeting   Weekly sync

todo> list --tag work --sort priority
ID   Status   Priority   Title                     Tags           Description
--------------------------------------------------------------------------------
1    [ ]      high       Complete project proposal work, important Need to finish by Friday
3    [ ]      high       Schedule team meeting     work, meeting   Weekly sync
2    [ ]      medium     Buy groceries            personal, errands

todo> complete 1
Task 1 marked as complete.

todo> list --status completed
ID   Status   Priority   Title                     Tags           Description
--------------------------------------------------------------------------------
1    [x]      high       Complete project proposal work, important Need to finish by Friday

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
- Priority values are "high", "medium", or "low" with "medium" as default
- Tags are comma-separated and duplicates are automatically prevented
- The list command supports combining multiple filters and sorting options
# Quickstart Guide: Todo App Advanced Level - Intelligent Features

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
To start the advanced todo application:
```bash
uv run python -m src.main
```

## Enhanced Commands

### `add`
- **Purpose**: Add a new task with title, description, priority, tags, due date, and recurrence
- **Usage**: Type `add` and follow the prompts
- **Example**:
  ```
  todo> add
  Enter task title (required): Prepare quarterly report
  Enter task description (optional, press Enter to skip): Need to compile sales data and charts
  Enter priority (high/medium/low, default: medium): high
  Enter tags (comma-separated, e.g., work,urgent,client): work, quarterly, report
  Enter due date (YYYY-MM-DD [HH:MM], default none): 2026-01-15 10:00
  Enter recurrence pattern (none/daily/weekly/monthly, default: none): monthly
  ✓ Task added with ID 1: Prepare quarterly report
  ```

### `list`
- **Purpose**: List all tasks in a formatted table with additional columns
- **Usage**: Type `list` or use enhanced options
- **Enhanced options**:
  - `list --status pending|completed|all` - Filter by status
  - `list --priority high|medium|low|all` - Filter by priority
  - `list --tag <tag>` - Filter by tag (repeatable: --tag work --tag urgent)
  - `list --sort id|priority|alpha|due` - Sort by criterion (due includes overdue first)
  - `list --overdue` - Show only overdue tasks
  - `list --search <keyword>` - Find tasks by keyword
- **Examples**:
  ```
  todo> list
  ID   Status   Priority   Due Date           Title                        Tags                   Description
  ----------------------------------------------------------------------------------------------------------------
  1    [ ]      high       2026-01-15 10:00  Prepare quarterly report (OVERDUE!)  work, quarterly, report  Need to compile sales data...
  2    [x]      medium     None               Buy groceries                 personal, errands        Milk, bread, eggs

  todo> list --sort due
  ID   Status   Priority   Due Date           Title                        Tags                   Description
  ----------------------------------------------------------------------------------------------------------------
  1    [ ]      high       2026-01-15 10:00  Prepare quarterly report (OVERDUE!)  work, quarterly, report  Need to compile sales data...
  3    [ ]      low        2026-01-30 14:00  Schedule team meeting           work, meeting            Weekly sync
  2    [x]      medium     None               Buy groceries                 personal, errands        Milk, bread, eggs

  todo> list --overdue --priority high
  ID   Status   Priority   Due Date           Title                        Tags                   Description
  ----------------------------------------------------------------------------------------------------------------
  1    [ ]      high       2026-01-15 10:00  Prepare quarterly report (OVERDUE!)  work, quarterly, report  Need to compile sales data...
  ```

### `update <id>`
- **Purpose**: Update an existing task by ID, including due date and recurrence
- **Usage**: `update <task_id>` and follow prompts
- **Example**:
  ```
  todo> update 1
  Enter new title (current: 'Prepare quarterly report', press Enter to keep current): Prepare annual report
  Enter new description (current: 'Need to compile sales data...', press Enter to keep current): Need to compile full year sales data and charts
  Enter new priority (current: 'high', high/medium/low, press Enter to keep current): 
  Enter new tags (current: 'work, quarterly, report', comma-separated, press Enter to keep current): work, annual, report
  Enter new due date (current: '2026-01-15 10:00', YYYY-MM-DD [HH:MM], press Enter to keep current): 2026-02-15 10:00
  Enter new recurrence (current: 'monthly', none/daily/weekly/monthly, press Enter to keep current): 
  ✓ Task 1 updated successfully.
  ```

### `complete <id>`
- **Purpose**: Toggle completion status of a task by ID; if recurring, creates new instance
- **Usage**: `complete <task_id>`
- **Example**:
  ```
  todo> complete 1
  Task 1 marked as complete.
  Next occurrence scheduled for 2026-02-15 10:00 (ID: 4).
  ```

### `help`
- **Purpose**: Display help information with all new capabilities
- **Usage**: Type `help`
- **Example**:
  ```
  todo> help

  Available commands:
    add              - Add a new task with title, description, priority, tags, due date, and recurrence
    list             - List all tasks with optional filters and sorting
      --status [pending|completed|all]  Filter by status
      --priority [high|medium|low|all]  Filter by priority  
      --tag <tag>                      Filter by tag (repeatable: --tag work --tag urgent)
      --sort [id|priority|alpha|due]   Sort by criterion (due shows overdue first)
      --overdue                        Show only overdue tasks
      --search <keyword>               Search by keyword in title or description
    update <id>      - Update a task by ID (title, description, priority, tags, due date, recurrence)
    delete <id>      - Delete a task by ID
    complete <id>    - Toggle completion status; if recurring, schedule next occurrence
    help             - Show this help message
    quit / exit      - Exit the application
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
Here's a complete example of using the advanced application features:

```
$ uv run python -m src.main
Welcome to the In-Memory Console Todo App!
Type 'help' for available commands or 'quit'/'exit' to exit.

todo> add
Enter task title (required): Morning workout
Enter task description (optional, press Enter to skip): 30-minute exercise routine
Enter priority (high/medium/low, default: medium): medium
Enter tags (comma-separated, e.g., work,urgent,client): health, fitness
Enter due date (YYYY-MM-DD [HH:MM], default none): 2026-01-28 07:00
Enter recurrence pattern (none/daily/weekly/monthly, default: none): daily
✓ Task added with ID 1: Morning workout

todo> add
Enter task title (required): Team standup meeting
Enter task description (optional, press Enter to skip): Daily sync with team
Enter priority (high/medium/low, default: medium): high
Enter tags (comma-separated, e.g., work,urgent,client): work, meeting
Enter due date (YYYY-MM-DD [HH:MM], default none): 2026-01-28 10:00
Enter recurrence pattern (none/daily/weekly/monthly, default: none): daily
✓ Task added with ID 2: Team standup meeting

todo> add
Enter task title (required): Submit project proposal
Enter task description (optional, press Enter to skip): Final submission to client
Enter priority (high/medium/low, default: medium): high
Enter tags (comma-separated, e.g., work,urgent,client): work, urgent
Enter due date (YYYY-MM-DD [HH:MM], default none): 2026-01-30 17:00
Enter recurrence pattern (none/daily/weekly/monthly, default: none): none
✓ Task added with ID 3: Submit project proposal

todo> list
ID   Status   Priority   Due Date           Title                        Tags           Description
----------------------------------------------------------------------------------------------------------------
1    [ ]      medium     2026-01-28 07:00  Morning workout                health, fitness  30-minute exercise routine
2    [ ]      high       2026-01-28 10:00  Team standup meeting (OVERDUE!)  work, meeting    Daily sync with team
3    [ ]      high       2026-01-30 17:00  Submit project proposal        work, urgent     Final submission to client

todo> complete 2
Task 2 marked as complete.
Next occurrence scheduled for 2026-01-29 10:00 (ID: 4).

todo> list --overdue
ID   Status   Priority   Due Date           Title                        Tags           Description
----------------------------------------------------------------------------------------------------------------
2    [x]      high       2026-01-28 10:00  Team standup meeting (COMPLETED)  work, meeting    Daily sync with team

todo> list --sort due
ID   Status   Priority   Due Date           Title                        Tags           Description
----------------------------------------------------------------------------------------------------------------
1    [ ]      medium     2026-01-28 07:00  Morning workout                health, fitness  30-minute exercise routine
2    [x]      high       2026-01-28 10:00  Team standup meeting (COMPLETED)  work, meeting    Daily sync with team
4    [ ]      high       2026-01-29 10:00  Team standup meeting           work, meeting    Daily sync with team
3    [ ]      high       2026-01-30 17:00  Submit project proposal        work, urgent     Final submission to client

todo> quit
Goodbye!
```

## Notes
- All commands are case-insensitive
- Extra whitespace is trimmed from commands
- Task IDs are sequential integers starting from 1
- IDs will have gaps after deletions
- Title and description lengths are unlimited
- Due dates are checked against current system time for overdue status
- Recurring tasks create new instances with updated due dates when completed
- Data is stored in memory only and will be lost when the application exits
- The list command supports combining multiple filters and sorting options
- Overdue tasks are highlighted with "(OVERDUE!)" indicator
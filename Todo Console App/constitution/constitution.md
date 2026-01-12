# Todo App Multi-Level Constitution

## Core Principles

### I. Strict Spec-Driven Development
Every line of code must originate from approved specifications, plans, and tasks; No manual coding permitted; Strict adherence to Spec-Kit Plus workflow: constitution → specify → plan → tasks → implement → review; Every feature and change must originate from a documented specification; All development activities must be traceable to approved requirements.

### II. Code Quality Excellence
Code must be PEP8 compliant, fully type-annotated, modular, and readable; Follow Python best practices and idioms; Maintain consistent code style throughout the project; Use descriptive variable and function names that clearly express intent; Implement clean architecture principles with separation of concerns; Ensure professional-grade code quality in all implementations.

### III. Simplicity and Robustness
Focus on core functionality with excellent error handling and user feedback; Implement minimal viable product without unnecessary complexity; Ensure application is stable and handles edge cases gracefully; Prioritize reliability over feature richness; Provide comprehensive error handling for all user inputs and system operations.

### IV. Superior CLI Experience
Design intuitive commands with clear prompts and formatted output; Ensure consistent interaction patterns across all features; Make commands discoverable and self-explanatory; Provide helpful messages for all user interactions; Implement professional table output with alignment and truncation; Create an excellent user experience in the console environment.

### V. Zero External Dependencies
Use only Python standard library; No third-party packages whatsoever; Keep the application lightweight and portable; Ensure the application can run with minimal setup requirements; Maintain complete independence from external libraries or services.

### VI. Forward-Compatible Architecture
Design with future evolution in mind; Ensure new features can be added without breaking existing functionality; Structure code to allow seamless progression from Basic to Intermediate to Advanced levels; Maintain backward compatibility at all times; Design data models and interfaces to accommodate future enhancements without refactoring.

## Key Standards

- Python version: 3.13+ required for development
- Project management: UV exclusively
- Dependencies: Zero external libraries – standard library only
- Data model: Task as dataclass with id (int, auto-increment), title (str), description (str), completed (bool, default False), priority (str, default "medium"), tags (list[str], default empty list), due_date (Optional[datetime], default None), recurrence (str, default "none")
- Storage: In-memory list of Task objects (no persistence)
- Interface: Interactive REPL with extensible command system
- Required features (all must be implemented):
  - Basic Level: Add Task, View/List Tasks, Update Task, Delete Task, Mark Complete/Incomplete
  - Intermediate Level: Priorities (high/medium/low), Tags/Categories, Search, Filter (by status/priority/tags), Sort (by priority, alpha, ID)
  - Advanced Level: Due Dates & Time Reminders, Recurring Tasks (daily/weekly/monthly patterns)
- Command set (case-insensitive, trimmed whitespace):
  - Basic Commands:
    - add                → start add task flow
    - list               → show all tasks
    - update <id>        → update task by ID
    - delete <id>        → delete task by ID
    - complete <id>      → toggle completion
    - help               → display available commands and usage
    - quit / exit        → terminate application
  - Intermediate Commands:
    - add                → enhanced with priority and tags prompts
    - list               → enhanced with filtering and sorting options (e.g., --priority high, --sort priority)
    - update <id>        → enhanced with priority and tags modification
    - search <keyword>   → find tasks by keyword in title or description
  - Advanced Commands:
    - add                → further enhanced with due date and recurrence prompts
    - list               → enhanced with due date filtering (--overdue, --due-soon) and sorting (--sort due)
    - update <id>        → enhanced with due date and recurrence modification
    - complete <id>      → enhanced to handle recurring task rescheduling
- Display: Enhanced table with columns ID, Status ([x]/[ ]), Priority, Due Date, Title, Tags, Description (truncated)

## Project Structure

- constitution.md
- /specs_history/          # All .specify, .plan, .task files preserved
- /src/
  ├── __init__.py
  ├── main.py             # Entry point and REPL loop
  ├── models.py           # Task dataclass (enhanced with due_date and recurrence)
  ├── todo_manager.py     # Core CRUD and business logic (enhanced with overdue check, recurrence rescheduling)
  ├── cli.py              # Command parsing, display, and user interaction (enhanced with date/recurrence support)
  └── utils.py            # Formatting and utility functions (enhanced with date helpers)

## Constraints

- In-memory storage only (Phase I) – designed for future persistence
- No third-party packages whatsoever
- Console-only interface
- Development process: Strictly Spec-Kit Plus sequence (constitution → specify → plan → tasks → implement → review)
- No manual coding permitted - all code must be generated from approved specifications
- Progressive enhancement: Build on solid foundations, never compromise existing features
- All new features must preserve backward compatibility with existing functionality
- Date/time handling: Use only Python's datetime module for date operations
- Recurrence patterns: Implement daily (+1 day), weekly (+7 days), monthly (+1 month with day preservation)

## Success Criteria

- Basic and Intermediate Level features remain fully functional and polished
- Codebase is cleanly structured for potential future extensions
- Task model and manager layer support all Advanced Level features (due dates, recurrence)
- CLI command system handles all new functionality without breaking existing commands
- All specification evolution is documented in /specs_history/
- README.md reflects current state and clearly outlines planned progression
- Application remains runnable via `uv run python -m src.main`
- All features (Basic, Intermediate, Advanced) fully functional and integrated
- Due date validation handles invalid inputs gracefully with clear error messages
- Recurring tasks properly reschedule upon completion based on recurrence pattern
- Overdue tasks are highlighted in list views with "OVERDUE!" indicators
- Enhanced table display includes all columns with proper formatting and indicators
- Combined filters and sorts work correctly with all features (list --overdue --priority high --sort due)

## Feature Progression (Explicitly Defined Evolution Path)

### Basic Level (Foundation – Core MVP)
- Add Task: Create new task with title and description, assigning unique sequential ID
- View/List Tasks: Display formatted table with ID, status ([x]/[ ]), title, truncated description
- Update Task: Modify title and/or description by ID
- Delete Task: Remove task by ID with confirmation feedback
- Mark Complete/Incomplete: Toggle completion status by ID

### Intermediate Level (Organization & Usability Enhancement)
- Priorities: Assign high/medium/low to tasks with default "medium"
- Tags/Categories: Add multiple free-form labels (e.g., work, personal, errands, health)
- Search: Find tasks by keyword (case-insensitive partial match in title/description)
- Filter: Show tasks by status (pending/completed), priority (high/medium/low), and tags
- Sort: Order list by priority (high > medium > low), title (alphabetical), or ID (chronological)
- Enhanced Display: Additional columns for Priority and Tags in table format

### Advanced Level (Intelligent Automation)
- Due Dates: Add optional due date/time to tasks with text-based input (YYYY-MM-DD [HH:MM])
- Time Reminders: Simulated via highlighting overdue tasks in list views (e.g., "OVERDUE!" indicators)
- Recurring Tasks: Support daily, weekly, monthly patterns that auto-reschedule upon completion
- Smart Filtering: Enhanced filters (--overdue, --due-soon) and sorting (--sort due)
- Intelligent List View: Shows due dates, highlights overdue tasks, and sorts by due date

## Governance

This constitution serves as the foundational governing document for multi-level development; All development activities must comply with these principles; Amendments require documentation and approval; Code reviews must verify adherence to all principles; Version: 3.0.0 | Ratified: 2025-01-28 | Last Amended: 2025-01-28
# Feature Specification: In-Memory Console Todo App – Phase I Basic Level

**Feature Branch**: `001-console-todo-app`
**Created**: 2025-01-28
**Status**: Draft
**Input**: User description: "In-Memory Console Todo App – Phase I Basic Level Target audience: Developers learning spec-driven/agentic development; end-users seeking a simple, reliable command-line todo tool for quick task management. Focus: Build a complete, user-friendly, interactive command-line Todo application that fully implements the 5 core features (Add Task, Delete Task, Update Task, View/List Tasks, Mark as Complete/Incomplete) with polished CLI experience and strict adherence to clean code principles."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add New Tasks (Priority: P1)

As a user, I want to add new tasks to my todo list by entering a title (required, unlimited length) and description (optional), so that I can keep track of things I need to do. The system should assign a unique sequential ID to each task and provide confirmation of the addition.

**Why this priority**: This is the foundational functionality that enables all other operations. Without the ability to add tasks, the application has no purpose.

**Independent Test**: Can be fully tested by adding tasks with various titles and descriptions, verifying that each gets a unique sequential ID and confirmation message is displayed.

**Acceptance Scenarios**:

1. **Given** I am using the todo application, **When** I enter the "add" command, **Then** I am prompted to enter a task title and optional description
2. **Given** I have entered a task title, **When** I confirm the entry, **Then** the task is added with a unique sequential ID and confirmation message is displayed
3. **Given** I have entered a task title and description, **When** I confirm the entry, **Then** the task is added with both title and description, a unique sequential ID, and confirmation message

---

### User Story 2 - View/List All Tasks (Priority: P1)

As a user, I want to view all my tasks in a clean, aligned table format showing ID, Status, Title (truncated if needed), and Description (truncated to 40 characters with "..."), so that I can see everything I need to do at a glance.

**Why this priority**: This is a core functionality that allows users to see their tasks, which is essential for the application's primary purpose.

**Independent Test**: Can be fully tested by adding multiple tasks and then using the "list" command to verify they appear in the correct table format with proper alignment and truncation.

**Acceptance Scenarios**:

1. **Given** I have added one or more tasks, **When** I enter the "list" command, **Then** all tasks are displayed in a clean, aligned table format
2. **Given** I have tasks with long descriptions, **When** I enter the "list" command, **Then** descriptions are truncated to 40 characters with "..." appended
3. **Given** I have tasks with long titles, **When** I enter the "list" command, **Then** titles are truncated as needed to maintain table format
4. **Given** I have no tasks, **When** I enter the "list" command, **Then** the message "No tasks yet." is displayed

---

### User Story 3 - Update Existing Tasks (Priority: P2)

As a user, I want to update existing tasks by ID, modifying the title and/or description, with the option to keep current values by pressing Enter, so that I can correct mistakes or add more information to existing tasks.

**Why this priority**: This allows users to maintain and refine their task information, which is important for long-term usability.

**Independent Test**: Can be fully tested by adding a task, updating its title and description, and verifying the changes are reflected when listing tasks.

**Acceptance Scenarios**:

1. **Given** I have added a task, **When** I enter the "update <id>" command, **Then** I am prompted to enter new title and description values
2. **Given** I am updating a task, **When** I press Enter without typing for title or description, **Then** the current value for that field is preserved
3. **Given** I am updating a task with a non-existent ID, **When** I enter the "update <id>" command, **Then** an appropriate error message is displayed

---

### User Story 4 - Delete Tasks (Priority: P2)

As a user, I want to delete tasks by ID with immediate confirmation message, so that I can remove tasks that are no longer relevant. After deletion, the ID sequence will have gaps.

**Why this priority**: This allows users to manage their task list by removing completed or irrelevant items.

**Independent Test**: Can be fully tested by adding tasks, deleting one by ID, and verifying it no longer appears in the list.

**Acceptance Scenarios**:

1. **Given** I have added one or more tasks, **When** I enter the "delete <id>" command with a valid ID, **Then** the task is removed and a confirmation message is displayed
2. **Given** I attempt to delete a task with a non-existent ID, **When** I enter the "delete <id>" command, **Then** an appropriate error message is displayed

---

### User Story 5 - Mark Tasks as Complete/Incomplete (Priority: P2)

As a user, I want to toggle the completion status of tasks by ID with clear feedback ("marked as complete" or "marked as incomplete"), so that I can track my progress.

**Why this priority**: This is a core functionality that allows users to track task completion, which is essential for a todo application.

**Independent Test**: Can be fully tested by adding tasks, toggling their completion status, and verifying the status changes when listing tasks.

**Acceptance Scenarios**:

1. **Given** I have added a task, **When** I enter the "complete <id>" command, **Then** the task's completion status is toggled and appropriate feedback is provided
2. **Given** I attempt to toggle completion status of a non-existent task ID, **When** I enter the "complete <id>" command, **Then** an appropriate error message is displayed

---

### User Story 6 - Help and Exit Commands (Priority: P3)

As a user, I want to access help information and exit the application using dedicated commands, so that I can understand how to use the application and terminate it properly. The system should handle commands with preserved whitespace correctly.

**Why this priority**: These are important usability features that enhance the user experience.

**Independent Test**: Can be fully tested by entering the "help" command and verifying the list of commands is displayed, and by entering "quit" or "exit" to terminate the application.

**Acceptance Scenarios**:

1. **Given** I am using the application, **When** I enter the "help" command, **Then** a list of all available commands with brief usage instructions is displayed
2. **Given** I am using the application, **When** I enter "  help  " with extra whitespace, **Then** the command is processed correctly
3. **Given** I am using the application, **When** I enter the "quit" or "exit" command, **Then** the application terminates gracefully

### Edge Cases

- What happens when the user enters invalid commands or non-existent IDs?
- How does the system handle empty input when a value is required?
- How does the system handle very long titles and descriptions that need truncation?
- What happens when the user tries to update/delete/complete a task that doesn't exist?
- How does the system handle case-insensitive commands with extra whitespace?
- What happens to IDs after tasks are deleted (gaps in sequence)?
- How does the system handle commands with preserved whitespace?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Application MUST provide interactive REPL loop for command-based interface
- **FR-002**: Application MUST support add command to create new tasks with title (required) and description (optional), assigning unique sequential ID
- **FR-003**: Application MUST support list command to display all tasks in formatted table (ID | Status | Title | Description truncated to 40 chars)
- **FR-004**: Application MUST support update <id> command to modify existing task title/description with option to keep current values
- **FR-005**: Application MUST support delete <id> command to remove task by ID with confirmation feedback
- **FR-006**: Application MUST support complete <id> command to toggle completion status by ID with clear feedback
- **FR-007**: Application MUST support help command to display available commands and usage
- **FR-008**: Application MUST support quit/exit commands to terminate application
- **FR-009**: Application MUST assign unique sequential IDs to tasks automatically starting from 1, allowing gaps in sequence after deletions
- **FR-010**: Application MUST handle invalid commands, non-existent IDs, and empty input gracefully with clear error messages
- **FR-011**: Application MUST provide professional table output with proper alignment, truncating long titles and descriptions as needed
- **FR-012**: Application MUST implement case-insensitive command processing that preserves all whitespace but still processes commands correctly
- **FR-013**: Application MUST handle empty task list gracefully with "No tasks yet." message
- **FR-014**: Application MUST store all data in-memory only with no persistence across sessions
- **FR-015**: Application MUST follow the specified project structure with separate modules for models, business logic, and CLI
- **FR-016**: Application MUST use type hints only where necessary for clarity, adhering to PEP8 standards
- **FR-017**: Application MUST be runnable via `uv run python -m src.main`

### Key Entities *(include if feature involves data)*

- **Task**: Represents a todo item with id (int, auto-increment), title (str, required, unlimited length), description (str, optional), completed (bool, default False)
- **TodoManager**: Core CRUD logic for managing tasks in memory with methods for add, update, delete, complete, and list operations

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: User can add a task by entering title (required, unlimited length) and description (optional), receiving a unique sequential ID and confirmation
- **SC-002**: User can list all tasks in a clean, aligned table format showing: ID | Status ([x] for completed, [ ] for pending) | Title (truncated if needed) | Description (truncated to 40 characters with "...")
- **SC-003**: User can update any existing task's title and/or description by ID, with option to keep current values (by pressing Enter)
- **SC-004**: User can delete any task by ID with immediate confirmation message, IDs will have gaps after deletions
- **SC-005**: User can toggle completion status of any task by ID with clear feedback ("marked as complete" or "marked as incomplete")
- **SC-006**: Empty list handled gracefully with message "No tasks yet."
- **SC-007**: Invalid commands or non-existent IDs produce clear, helpful error messages without crashing
- **SC-008**: "help" command displays full list of commands with brief usage instructions
- **SC-009**: Application runs in continuous REPL loop until "quit" or "exit" is entered
- **SC-010**: Application successfully launches with `uv run python -m src.main`
- **SC-011**: Codebase is clean, modular, and uses type hints only where necessary for clarity, adhering to PEP8 standards
- **SC-012**: README.md includes UV setup instructions and complete example interactive session demonstrating all features

## Clarifications

### Session 2025-01-28

- Q: How should the system handle very long titles that exceed display limitations? → A: Allow unlimited title length without any limitations
- Q: How should the system handle commands with multiple consecutive spaces or special characters? → A: Preserve all whitespace but still process commands correctly
- Q: What should happen to IDs after tasks are deleted? → A: Allow gaps in ID sequence after deletions
- Q: How should the table handle tasks with very long titles that might exceed the column width? → A: Truncate titles in the display (similar to descriptions)
- Q: What level of strictness is expected for type annotations? → A: Use type hints only where necessary for clarity

# Implementation Tasks: In-Memory Console Todo App – Phase I Basic Level

**Feature**: In-Memory Console Todo App
**Branch**: 001-console-todo-app
**Generated**: 2025-01-28
**Based on**: spec.md, plan.md, data-model.md, contracts/api-contracts.md

## Implementation Strategy

Build the application incrementally, starting with the core data model and business logic, then adding CLI functionality. Each user story should be independently testable, with the first user story (adding tasks) forming the MVP.

## Dependencies

- User Story 1 (Add Tasks) must be completed before User Story 2 (List Tasks) can be fully tested
- User Story 2 (List Tasks) is required to verify other stories work correctly
- Foundational components (Task model, TodoManager) are prerequisites for all stories

## Parallel Execution Examples

- [P] Task model implementation can run in parallel with initial TodoManager skeleton
- [P] CLI command parsing can be developed in parallel with TodoManager operations
- [P] Individual user story implementations can be developed in parallel after foundational components exist

---

## Phase 1: Setup

### Goal
Initialize project structure and foundational components

- [X] T001 Create src directory structure if not already present
- [X] T002 Create src/__init__.py file
- [X] T003 Verify Python 3.13+ compatibility requirements

---

## Phase 2: Foundational Components

### Goal
Implement core data model and business logic layer that all user stories depend on

- [X] T004 [P] Create Task dataclass in src/models.py with id (int, auto-increment), title (str, required), description (str, optional), completed (bool, default False)
- [X] T005 [P] Create TodoManager class in src/todo_manager.py with _tasks (List[Task], private) and _next_id (int, private)
- [X] T006 [P] Implement add_task method in TodoManager: (title: str, description: str = None) -> Task with validation that title is non-empty after stripping
- [X] T007 [P] Implement list_tasks method in TodoManager: () -> List[Task]
- [X] T008 [P] Implement get_task_by_id method in TodoManager: (task_id: int) -> Task | None with validation that task_id is positive
- [X] T009 [P] Implement update_task method in TodoManager: (task_id: int, title: str = None, description: str = None) -> Task | None
- [X] T010 [P] Implement delete_task method in TodoManager: (task_id: int) -> bool
- [X] T011 [P] Implement toggle_task_completion method in TodoManager: (task_id: int) -> Task | None
- [X] T012 [P] Create CLI class in src/cli.py with TodoManager dependency

---

## Phase 3: [US1] Add New Tasks (Priority: P1)

### Goal
Enable users to add new tasks with title and optional description, receiving a unique sequential ID and confirmation

### Independent Test Criteria
Can be fully tested by adding tasks with various titles and descriptions, verifying that each gets a unique sequential ID and confirmation message is displayed.

- [X] T013 [US1] Implement get_user_input method in CLI: (prompt: str) -> str
- [X] T014 [US1] Implement add command handler in main.py that prompts for title and optional description
- [X] T015 [US1] Implement validation in CLI to ensure title is provided (non-empty after stripping)
- [X] T016 [US1] Connect add command to TodoManager.add_task method
- [X] T017 [US1] Display confirmation message with assigned ID after successful task creation
- [X] T018 [US1] Test adding tasks with various titles and descriptions to verify unique IDs and confirmation messages

---

## Phase 4: [US2] View/List All Tasks (Priority: P1)

### Goal
Display all tasks in a clean, aligned table format showing ID, Status, Title (truncated if needed), and Description (truncated to 40 characters with "...")

### Independent Test Criteria
Can be fully tested by adding multiple tasks and then using the "list" command to verify they appear in the correct table format with proper alignment and truncation.

- [X] T019 [US2] Implement display_tasks method in CLI: (tasks: List[Task]) -> None with formatted table output
- [X] T020 [US2] Implement proper alignment for ID, Status ([x]/[ ]), Title, and Description columns
- [X] T021 [US2] Implement truncation logic for long titles (truncated if needed)
- [X] T022 [US2] Implement truncation logic for descriptions (truncated to 40 chars + "...")
- [X] T023 [US2] Implement "No tasks yet." message when task list is empty
- [X] T024 [US2] Connect list command in main.py to TodoManager.list_tasks and CLI.display_tasks
- [X] T025 [US2] Test listing tasks with various lengths of titles and descriptions to verify proper formatting and truncation

---

## Phase 5: [US3] Update Existing Tasks (Priority: P2)

### Goal
Allow users to update existing tasks by ID, modifying the title and/or description, with the option to keep current values by pressing Enter

### Independent Test Criteria
Can be fully tested by adding a task, updating its title and description, and verifying the changes are reflected when listing tasks.

- [X] T026 [US3] Implement update command handler in main.py that parses task ID from arguments
- [X] T027 [US3] Implement interactive prompts in CLI for new title and description with option to keep current values by pressing Enter
- [X] T028 [US3] Connect update command to TodoManager.update_task method
- [X] T029 [US3] Display appropriate error message when updating non-existent task ID
- [X] T030 [US3] Display confirmation message after successful task update
- [X] T031 [US3] Test updating tasks to verify changes are reflected when listing tasks

---

## Phase 6: [US4] Delete Tasks (Priority: P2)

### Goal
Enable users to delete tasks by ID with immediate confirmation message, with gaps in ID sequence after deletions

### Independent Test Criteria
Can be fully tested by adding tasks, deleting one by ID, and verifying it no longer appears in the list.

- [X] T032 [US4] Implement delete command handler in main.py that parses task ID from arguments
- [X] T033 [US4] Connect delete command to TodoManager.delete_task method
- [X] T034 [US4] Display confirmation message after successful task deletion
- [X] T035 [US4] Display appropriate error message when deleting non-existent task ID
- [X] T036 [US4] Verify that ID sequence has gaps after deletion
- [X] T037 [US4] Test deleting tasks to verify they no longer appear in the list

---

## Phase 7: [US5] Mark Tasks as Complete/Incomplete (Priority: P2)

### Goal
Allow users to toggle completion status of tasks by ID with clear feedback ("marked as complete" or "marked as incomplete")

### Independent Test Criteria
Can be fully tested by adding tasks, toggling their completion status, and verifying the status changes when listing tasks.

- [X] T038 [US5] Implement complete command handler in main.py that parses task ID from arguments
- [X] T039 [US5] Connect complete command to TodoManager.toggle_task_completion method
- [X] T040 [US5] Display feedback message ("marked as complete" or "marked as incomplete") after toggling
- [X] T041 [US5] Display appropriate error message when toggling completion status of non-existent task ID
- [X] T042 [US5] Test toggling completion status to verify changes are reflected when listing tasks

---

## Phase 8: [US6] Help and Exit Commands (Priority: P3)

### Goal
Provide access to help information and exit functionality, with handling of commands with preserved whitespace

### Independent Test Criteria
Can be fully tested by entering the "help" command and verifying the list of commands is displayed, and by entering "quit" or "exit" to terminate the application.

- [X] T043 [US6] Implement parse_command method in CLI: (user_input: str) -> tuple that handles case-insensitivity and whitespace preservation
- [X] T044 [US6] Implement display_help method in CLI to show available commands and usage
- [X] T045 [US6] Implement help command handler in main.py
- [X] T046 [US6] Implement quit/exit command handlers in main.py
- [X] T047 [US6] Test help command to verify list of commands is displayed correctly
- [X] T048 [US6] Test quit/exit commands to verify application terminates gracefully
- [X] T049 [US6] Test command processing with extra whitespace to verify it's handled correctly

---

## Phase 9: Polish & Cross-Cutting Concerns

### Goal
Complete the application with error handling, type annotations, and final integration

- [X] T050 Implement error handling for invalid commands with appropriate error messages
- [X] T051 Implement error handling for non-existent IDs with appropriate error messages
- [X] T052 Implement error handling for empty input when required with appropriate error messages
- [X] T053 Add type hints to all functions and methods where necessary for clarity
- [X] T054 Implement main REPL loop in src/main.py with command dispatcher
- [X] T055 Ensure application runs continuously until quit/exit command is entered
- [X] T056 Test complete interactive session to verify all features work together
- [X] T057 Verify application can be run with `uv run python -m src.main`
- [X] T058 Create README.md with UV setup instructions and example interactive session
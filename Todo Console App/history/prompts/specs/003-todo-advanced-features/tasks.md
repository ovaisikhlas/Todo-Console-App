# Implementation Tasks: Todo App Advanced Level - Intelligent Features

**Feature**: Todo App Advanced Level - Intelligent Features
**Branch**: `003-todo-advanced-features`
**Generated**: 2025-01-28
**Based on**: spec.md, plan.md, data-model.md, contracts/api-contracts.md

## Implementation Strategy

Build the application incrementally, starting with the core data model and business logic extensions, then adding CLI functionality for the new features. Each user story should be independently testable, with the first user story (adding tasks with due dates and recurrence) forming the MVP.

## Dependencies

- User Story 1 (Add Tasks with Due Dates/Recurrence) must be completed before User Story 2 (List Tasks with Enhanced Display) can be fully tested
- User Story 2 (List Tasks) is required to verify other stories work correctly
- Foundational components (Task model extensions, TodoManager enhancements) are prerequisites for all stories

## Parallel Execution Examples

- [P] Task model extension can run in parallel with initial TodoManager skeleton
- [P] CLI command parsing can be developed in parallel with TodoManager operations
- [P] Individual user story implementations can be developed in parallel after foundational components exist

---

## Phase 1: Setup

### Goal
Initialize project structure and foundational components

- [ ] T001 Create src/utils.py file for date formatting and utility functions
- [ ] T002 Verify Python 3.13+ compatibility requirements

---

## Phase 2: Foundational Components

### Goal
Implement core data model and business logic layer extensions that all user stories depend on

- [ ] T003 [P] Extend Task dataclass in src/models.py with due_date (Optional[datetime.datetime], default None) and recurrence (str, default "none")
- [ ] T004 [P] Update TodoManager class in src/todo_manager.py with enhanced add_task method: (title: str, description: str = None, priority: str = "medium", tags: list[str] = None, due_date_str: str = None, recurrence: str = "none") -> Task
- [ ] T005 [P] Update TodoManager with enhanced update_task method: (task_id: int, title: str = None, description: str = None, priority: str = None, tags: list[str] = None, due_date_str: str = None, recurrence: str = None) -> Task | None
- [ ] T006 [P] Implement parse_date_string function in src/utils.py: (date_str: str) -> datetime.datetime | None with validation for YYYY-MM-DD [HH:MM] format
- [ ] T007 [P] Implement format_date_for_display function in src/utils.py: (dt: datetime.datetime | None) -> str with format "YYYY-MM-DD HH:MM" or "None"
- [ ] T008 [P] Implement is_overdue function in src/utils.py: (task: Task) -> bool comparing due date with current time
- [ ] T009 [P] Implement advance_date_by_pattern function in src/utils.py: (dt: datetime.datetime, pattern: str) -> datetime.datetime with daily (+1 day), weekly (+7 days), monthly (+1 month) logic
- [ ] T010 [P] Create CLI class in src/cli.py with TodoManager dependency and enhanced command parsing

---

## Phase 3: [US1] Add Tasks with Due Dates & Recurrence (Priority: P1)

### Goal
Enable users to add new tasks with due dates and recurrence patterns during creation

### Independent Test Criteria
Can be fully tested by adding tasks with various due dates and recurrence patterns, verifying that they are properly stored and displayed.

- [ ] T011 [US1] Implement add command handler in main.py that prompts for due date (with example format shown)
- [ ] T012 [US1] Implement add command handler in main.py that prompts for recurrence pattern (with default shown)
- [ ] T013 [US1] Implement validation in CLI to ensure due date format is valid (YYYY-MM-DD [HH:MM])
- [ ] T014 [US1] Implement validation in CLI to ensure recurrence pattern is one of "none", "daily", "weekly", "monthly"
- [ ] T015 [US1] Connect add command to TodoManager.add_task method with due_date and recurrence parameters
- [ ] T016 [US1] Test adding tasks with various due dates and recurrence patterns to verify correct assignment

---

## Phase 4: [US2] Enhanced Task Display with Due Dates (Priority: P1)

### Goal
Display tasks with additional information including due dates and overdue indicators

### Independent Test Criteria
Can be fully tested by adding tasks with various due dates (some in past, some in future), then listing them to verify that due dates are displayed correctly and overdue tasks are highlighted.

- [ ] T017 [US2] Implement enhanced display_tasks method in CLI: (tasks: List[Task]) -> None with new Due Date column
- [ ] T018 [US2] Implement proper alignment for ID, Status ([x]/[ ]), Priority, Due Date, Title, Tags, and Description columns
- [ ] T019 [US2] Implement overdue indicator display (e.g., append "(OVERDUE!)" to title for overdue tasks)
- [ ] T020 [US2] Implement due date formatting in display (YYYY-MM-DD HH:MM format)
- [ ] T021 [US2] Connect list command to enhanced display_tasks method
- [ ] T022 [US2] Test listing tasks with various due dates to verify proper formatting and overdue highlighting

---

## Phase 5: [US3] Recurring Task Automation (Priority: P2)

### Goal
Automatically create new task instances when recurring tasks are completed

### Independent Test Criteria
Can be fully tested by creating recurring tasks, completing them, and verifying that new instances are created with updated due dates based on the recurrence pattern.

- [ ] T023 [US3] Implement toggle_task_completion_with_recurrence method in TodoManager: (task_id: int) -> Task | None
- [ ] T024 [US3] Implement logic to clone task with updated due date based on recurrence pattern when completed
- [ ] T025 [US3] Implement proper ID assignment for new recurring task instances (next available ID)
- [ ] T026 [US3] Connect complete command to enhanced toggle method in main.py
- [ ] T027 [US3] Test completing recurring tasks to verify new instances are created with updated due dates
- [ ] T028 [US3] Test different recurrence patterns (daily, weekly, monthly) to verify correct date advancement

---

## Phase 6: [US4] Due Date Filtering & Sorting (Priority: P2)

### Goal
Allow users to filter and sort tasks by due date, including showing only overdue tasks

### Independent Test Criteria
Can be fully tested by creating tasks with various due dates, then applying different filter and sort combinations to verify correct results.

- [ ] T029 [US4] Extend command parser in CLI to support --overdue flag and --sort due option
- [ ] T030 [US4] Implement get_overdue_tasks method in TodoManager: () -> List[Task]
- [ ] T031 [US4] Implement sort_by_due_date method in TodoManager: (tasks: List[Task]) -> List[Task] with overdue first, then chronological
- [ ] T032 [US4] Connect list command orchestration in main.py to apply due date filters and sorting
- [ ] T033 [US4] Test filtering for overdue tasks to verify only overdue tasks are displayed
- [ ] T034 [US4] Test sorting by due date to verify correct chronological order with overdue tasks first

---

## Phase 7: [US5] Update Tasks with Due Dates & Recurrence (Priority: P3)

### Goal
Allow users to modify due dates and recurrence patterns of existing tasks

### Independent Test Criteria
Can be fully tested by adding tasks, updating their due dates and recurrence patterns, and verifying that changes are reflected when listing tasks.

- [ ] T035 [US5] Implement update command handler in main.py that allows due date modification
- [ ] T036 [US5] Implement update command handler in main.py that allows recurrence pattern modification
- [ ] T037 [US5] Connect update command to TodoManager.update_task method with due_date and recurrence parameters
- [ ] T038 [US5] Test updating tasks to change due dates and verify changes are reflected
- [ ] T039 [US5] Test updating tasks to change recurrence patterns and verify changes are reflected

---

## Phase 8: [US6] Enhanced Help & User Guidance (Priority: P3)

### Goal
Update help information to reflect all new capabilities with examples

### Independent Test Criteria
Can be fully tested by entering the "help" command and verifying that all new capabilities with due dates and recurrence are properly documented with examples.

- [ ] T040 [US6] Update help command display to include new options for due dates and recurrence
- [ ] T041 [US6] Add examples for new command options (list --overdue, list --sort due, etc.)
- [ ] T042 [US6] Test help command to verify all new capabilities are documented with examples

---

## Phase 9: Polish & Cross-Cutting Concerns

### Goal
Complete the application with error handling, type annotations, and final integration

- [ ] T043 Implement error handling for invalid date formats with appropriate error messages
- [ ] T044 Implement error handling for invalid recurrence patterns with appropriate error messages
- [ ] T045 Implement error handling for month boundary issues in recurrence (e.g., Jan 31 to Feb 28/29) with appropriate error messages
- [ ] T046 Add type hints to all new functions and methods where necessary for clarity
- [ ] T047 Update help command to reflect all new capabilities with examples
- [ ] T048 Ensure backward compatibility: all Basic/Intermediate Level commands continue to work unchanged when no new options are provided
- [ ] T049 Test complete interactive session to verify all features work together
- [ ] T050 Verify application can be run with `uv run python -m src.main`
- [ ] T051 Update README.md with Advanced Level section and example session showing new features
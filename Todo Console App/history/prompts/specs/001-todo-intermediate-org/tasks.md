# Implementation Tasks: Todo App Intermediate Level - Organization & Usability

**Feature**: Todo App Intermediate Level - Organization & Usability
**Branch**: 001-todo-intermediate-org
**Generated**: 2025-01-28
**Based on**: spec.md, plan.md, data-model.md, contracts/api-contracts.md

## Implementation Strategy

Build the application incrementally, starting with the core data model and business logic, then adding CLI functionality. Each user story should be independently testable, with the first user story (adding tasks with priority and tags) forming the MVP.

## Dependencies

- User Story 1 (Assign Task Priorities) must be completed before User Story 2 (Tag Tasks) can be fully tested
- User Story 3 (Search Tasks) and User Story 4 (Filter and Sort) depend on foundational components
- Foundational components (Task model, TodoManager) are prerequisites for all stories

## Parallel Execution Examples

- [P] Task model extension can run in parallel with initial TodoManager skeleton
- [P] CLI command parsing can be developed in parallel with TodoManager operations
- [P] Individual user story implementations can be developed in parallel after foundational components exist

---

## Phase 1: Setup

### Goal
Initialize project structure and foundational components

- [X] T001 Create src/utils.py file for formatting and utility functions
- [X] T002 Verify Python 3.13+ compatibility requirements

---

## Phase 2: Foundational Components

### Goal
Implement core data model and business logic layer that all user stories depend on

- [X] T003 [P] Extend Task dataclass in src/models.py with priority (str, default "medium") and tags (list[str], default empty list)
- [X] T004 [P] Update TodoManager class in src/todo_manager.py with enhanced add_task method: (title: str, description: str = None, priority: str = "medium", tags: list[str] = None) -> Task
- [X] T005 [P] Update TodoManager with enhanced update_task method: (task_id: int, title: str = None, description: str = None, priority: str = None, tags: list[str] = None) -> Task | None
- [X] T006 [P] Implement search_tasks method in TodoManager: (keyword: str) -> List[Task] with case-insensitive partial match
- [X] T007 [P] Implement filter_tasks method in TodoManager: (status: str = None, priority: str = None, tags: list[str] = None) -> List[Task] with AND logic for multiple tags
- [X] T008 [P] Implement sort_tasks method in TodoManager: (tasks: List[Task], criterion: str) -> List[Task] with support for "id", "priority", "alpha"
- [X] T009 [P] Create TaskFilter class in src/todo_manager.py with apply method
- [X] T010 [P] Create TaskSorter class in src/todo_manager.py with sort method
- [X] T011 [P] Create CLI class in src/cli.py with TodoManager dependency

---

## Phase 3: [US1] Assign Task Priorities (Priority: P1)

### Goal
Enable users to assign priority levels (high, medium, low) to tasks during creation and update

### Independent Test Criteria
Can be fully tested by adding tasks with different priority levels, updating existing tasks to change priorities, and verifying that priority information is preserved and displayed correctly.

- [X] T012 [US1] Implement add command handler in main.py that prompts for priority (with default shown)
- [X] T013 [US1] Implement validation in CLI to ensure priority is one of "high", "medium", "low"
- [X] T014 [US1] Connect add command to TodoManager.add_task method with priority parameter
- [X] T015 [US1] Implement update command handler in main.py that allows priority modification
- [X] T016 [US1] Connect update command to TodoManager.update_task method with priority parameter
- [ ] T017 [US1] Test adding tasks with various priority levels to verify correct assignment
- [ ] T018 [US1] Test updating tasks to change priorities and verify changes are reflected

---

## Phase 4: [US2] Tag Tasks with Categories (Priority: P1)

### Goal
Allow users to attach multiple free-form tags/categories to tasks during creation and update

### Independent Test Criteria
Can be fully tested by adding tasks with various tags, updating existing tasks to add/remove tags, and verifying that tags are preserved and displayed correctly.

- [X] T019 [US2] Implement add command handler in main.py that prompts for tags (comma-separated)
- [X] T020 [US2] Implement tag input parsing: split by comma, strip whitespace, prevent duplicates
- [X] T021 [US2] Connect add command to TodoManager.add_task method with tags parameter
- [X] T022 [US2] Implement update command handler in main.py that allows tag modification
- [X] T023 [US2] Connect update command to TodoManager.update_task method with tags parameter
- [X] T024 [US2] Implement duplicate tag prevention in TodoManager
- [ ] T025 [US2] Test adding tasks with various tags to verify correct assignment
- [ ] T026 [US2] Test updating tasks to add/remove tags and verify changes are reflected

---

## Phase 5: [US3] Search Tasks by Keyword (Priority: P2)

### Goal
Enable users to search tasks by keyword (case-insensitive match in title or description)

### Independent Test Criteria
Can be fully tested by creating tasks with various titles and descriptions, then searching for keywords that appear in them, verifying that matching tasks are returned.

- [X] T027 [US3] Implement search command handler in main.py that parses keyword from arguments
- [X] T028 [US3] Connect search command to TodoManager.search_tasks method
- [X] T029 [US3] Implement case-insensitive partial match in title and description
- [X] T030 [US3] Display search results using existing display_tasks method
- [ ] T031 [US3] Test searching for keywords in task titles to verify correct results
- [ ] T032 [US3] Test searching for keywords in task descriptions to verify correct results
- [ ] T033 [US3] Test searching for non-existent keywords to verify empty results

---

## Phase 6: [US4] Filter and Sort Task Lists (Priority: P2)

### Goal
Allow users to filter the list by status, priority, and tags, as well as sort by priority, alphabetically, or by ID

### Independent Test Criteria
Can be fully tested by creating tasks with various statuses, priorities, and tags, then applying different filter and sort combinations to verify correct results.

- [X] T034 [US4] Extend command parser in CLI to support flags: --status, --priority, --tag (repeatable), --sort
- [X] T035 [US4] Implement list command orchestration in main.py to apply filters and sorting
- [X] T036 [US4] Connect to TodoManager.filter_tasks method for filtering
- [X] T037 [US4] Connect to TodoManager.sort_tasks method for sorting
- [X] T038 [US4] Implement combined search, filter, and sort functionality
- [X] T039 [US4] Handle empty results gracefully with "No tasks match your criteria" message
- [ ] T040 [US4] Test filtering by status to verify correct results
- [ ] T041 [US4] Test filtering by priority to verify correct results
- [ ] T042 [US4] Test filtering by tags to verify correct results
- [ ] T043 [US4] Test sorting by priority to verify correct order
- [ ] T044 [US4] Test sorting alphabetically to verify correct order
- [ ] T045 [US4] Test combined filter and sort operations to verify correct results

---

## Phase 7: [US5] Enhanced Table Display (Priority: P3)

### Goal
Display additional information (priority and tags) in the task list display

### Independent Test Criteria
Can be fully tested by adding tasks with various priorities and tags, then listing them to verify that the enhanced table format displays all required information correctly.

- [X] T046 [US5] Implement enhanced display_tasks method in CLI: (tasks: List[Task]) -> None with new columns
- [X] T047 [US5] Implement proper alignment for ID, Status ([x]/[ ]), Priority, Title, Tags, and Description columns
- [X] T048 [US5] Implement intelligent truncation for tags (comma-separated, truncated if too long)
- [X] T049 [US5] Implement priority display with capitalized values
- [X] T050 [US5] Update table header to include new Priority and Tags columns
- [ ] T051 [US5] Test enhanced table display with tasks containing various priorities and tags
- [ ] T052 [US5] Test tag truncation with very long tag names to verify proper formatting

---

## Phase 8: Polish & Cross-Cutting Concerns

### Goal
Complete the application with error handling, type annotations, and final integration

- [X] T053 Implement error handling for invalid priority values with appropriate error messages
- [X] T054 Implement error handling for invalid filter values with appropriate error messages
- [X] T055 Implement error handling for invalid sort criteria with appropriate error messages
- [X] T056 Add type hints to all functions and methods where necessary for clarity
- [X] T057 Update help command to reflect all new capabilities with examples
- [X] T058 Ensure backward compatibility: all Basic Level commands continue to work unchanged when no new options are provided
- [X] T059 Test complete interactive session to verify all features work together
- [X] T060 Verify application can be run with `uv run python -m src.main`
- [X] T061 Update README.md with Intermediate Level section and example session
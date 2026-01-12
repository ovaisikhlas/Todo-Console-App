---

description: "Task list for implementing core Todo application requirements"
---

# Tasks: Core Todo Application Requirements

**Input**: Design documents from `/specs_history/todo-core-requirements/`
**Prerequisites**: todo-core-requirements.plan.md (required), todo-core-requirements.spec.md (required for user stories)

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are now specific to the Todo application
  implementation based on the feature specification.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan (src/, tests/)
- [ ] T002 Initialize Python 3.13+ project with UV dependency manager (no third-party libraries)
- [ ] T003 [P] Configure linting and formatting tools for Python (PEP8 compliance)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Create Task dataclass with id (int, auto-increment), title (str), description (str), completed (bool default False)
- [ ] T005 [P] Implement TodoManager with in-memory storage (list of Task objects)
- [ ] T006 [P] Setup CLI command parsing infrastructure
- [ ] T007 Create base models/entities that all stories depend on
- [ ] T008 Configure error handling and user feedback infrastructure
- [ ] T009 Setup application entry point with REPL loop

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks to their todo list

**Independent Test**: Can be fully tested by running the application, using the 'add' command, and verifying that a new task is created with a unique ID and appears in the task list.

### Implementation for User Story 1

- [ ] T010 [P] [US1] Create Task model in src/models.py with id (int, auto-increment), title (str), description (str), completed (bool default False)
- [ ] T011 [P] [US1] Create TodoManager class in src/todo_manager.py with in-memory storage and add_task method
- [ ] T012 [US1] Implement add command functionality in src/cli.py (depends on T010, T011)
- [ ] T013 [US1] Add validation and error handling for user inputs (empty title)
- [ ] T014 [US1] Add user feedback for successful operations and errors
- [ ] T015 [US1] Test the add functionality by running the application and adding tasks

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P1)

**Goal**: Display all tasks in a formatted list with ID, status, title, and description

**Independent Test**: Can be tested by adding tasks and then using the 'list' command to display them in a formatted table with ID, status, title, and description.

### Implementation for User Story 2

- [ ] T016 [P] [US2] Implement list_tasks method in TodoManager class in src/todo_manager.py
- [ ] T017 [US2] Implement list command functionality in src/cli.py
- [ ] T018 [US2] Format the task display as a table with columns ID, Status ([x]/[ ]), Title, Description (truncated)
- [ ] T019 [US2] Handle the case when no tasks exist
- [ ] T020 [US2] Test the list functionality by running the application and viewing tasks

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task (Priority: P2)

**Goal**: Allow users to update the title or description of an existing task

**Independent Test**: Can be tested by adding a task, using the 'update' command with a valid ID, and verifying that the task details are modified.

### Implementation for User Story 3

- [ ] T021 [P] [US3] Implement update_task method in TodoManager class in src/todo_manager.py
- [ ] T022 [US3] Implement update <id> command functionality in src/cli.py
- [ ] T023 [US3] Add validation and error handling for ID-based operations (invalid ID)
- [ ] T024 [US3] Add user feedback for successful updates and errors
- [ ] T025 [US3] Test the update functionality by running the application and updating tasks

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Task (Priority: P2)

**Goal**: Allow users to delete tasks from their list

**Independent Test**: Can be tested by adding tasks, using the 'delete' command with a valid ID, and verifying that the task is removed from the list.

### Implementation for User Story 4

- [ ] T026 [P] [US4] Implement delete_task method in TodoManager class in src/todo_manager.py
- [ ] T027 [US4] Implement delete <id> command functionality in src/cli.py
- [ ] T028 [US4] Add validation and error handling for ID-based operations (invalid ID)
- [ ] T029 [US4] Add user feedback for successful deletions and errors
- [ ] T030 [US4] Test the delete functionality by running the application and deleting tasks

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Mark as Complete (Priority: P2)

**Goal**: Allow users to mark tasks as complete/incomplete

**Independent Test**: Can be tested by adding tasks, using the 'complete' command with a valid ID, and verifying that the task's completion status is toggled.

### Implementation for User Story 5

- [ ] T031 [P] [US5] Implement toggle_complete method in TodoManager class in src/todo_manager.py
- [ ] T032 [US5] Implement complete <id> command functionality in src/cli.py
- [ ] T033 [US5] Add validation and error handling for ID-based operations (invalid ID)
- [ ] T034 [US5] Add user feedback for successful status changes and errors
- [ ] T035 [US5] Test the complete functionality by running the application and toggling task completion status

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Additional Commands & Polish

**Purpose**: Implement remaining required commands and finalize the application

- [ ] T036 [P] Implement help command functionality in src/cli.py
- [ ] T037 [P] Implement quit/exit command functionality in src/main.py
- [ ] T038 [P] Ensure all error handling provides clear user feedback
- [ ] T039 [P] Code cleanup and refactoring to ensure PEP8 compliance and type annotations
- [ ] T040 [P] Run application validation to ensure all commands work properly

---

## Phase 9: Documentation & Final Validation

**Purpose**: Create documentation and perform final validation

- [ ] T041 [P] Create README.md with UV setup instructions and example usage session
- [ ] T042 [P] Document all available commands and their usage
- [ ] T043 [P] Perform end-to-end testing of all features
- [ ] T044 [P] Verify application launches with `uv run python -m src.main`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Additional Commands (Phase 8)**: Depends on all desired user stories being complete
- **Documentation (Phase 9)**: Depends on all functionality being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Models before services
- Services before CLI commands
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Stories 1 & 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Task)
4. Complete Phase 4: User Story 2 (View Task List)
5. **STOP and VALIDATE**: Test Add and List functionality independently
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (Add functionality!)
3. Add User Story 2 → Test independently → Deploy/Demo (List functionality!)
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
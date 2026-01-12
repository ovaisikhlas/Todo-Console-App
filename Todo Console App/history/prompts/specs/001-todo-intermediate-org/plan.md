# Implementation Plan: Todo App Intermediate Level - Organization & Usability

**Branch**: `001-todo-intermediate-org` | **Date**: 2025-01-28 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-todo-intermediate-org/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Extend the completed Basic Level in-memory console Todo app with Intermediate Level features (Priorities, Tags/Categories, Search, Filter, Sort) while maintaining full backward compatibility, clean architecture, and excellent user experience. The implementation will enhance the existing Task model with priority and tags fields, implement search/filter/sort functionality in the TodoManager, extend the CLI to support new command options, and update the display formatting to show the additional information.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: UV only (no third-party libraries - standard library exclusively)
**Storage**: In-memory only (no file I/O or persistence mechanisms)
**Testing**: Manual interactive testing based on acceptance criteria (no automated tests required per specification)
**Target Platform**: Console/Command-line interface
**Project Type**: Single project CLI application
**Performance Goals**: Fast response times for CLI commands (sub-second execution)
**Constraints**: In-memory storage, no file I/O, console interaction only
**Scale/Scope**: Individual user task management (single-user, local application)
**Architecture**: Modular separation of concerns extending existing structure:
  - models.py: Extend Task dataclass with priority (str, default "medium") and tags (list[str], default empty list)
  - todo_manager.py: Add search_tasks(), filter_tasks(), sort_tasks() methods and enhance add_task(), update_task() to handle new fields
  - cli.py: Extend command parsing to support flags (--status, --priority, --tag, --sort, --search) and enhance display formatting
  - utils.py: Add formatting utilities for enhanced table display with new columns
**Data Flow**: CLI → TodoManager → Models → Storage (in-memory list)
**Command Processing**: Enhanced parsing to support flag-based options (e.g., list --sort priority --status pending)
**Priority Values**: "high", "medium", "low" with default "medium"
**Tags**: List of strings with automatic duplicate prevention
**Search**: Case-insensitive partial match in title and description
**Filter Logic**: Support AND logic for multiple tags
**Sort Options**: By ID (default), priority (high > medium > low), or alphabetically by title
**Display Format**: Enhanced table with new columns: ID | Status | Priority | Title | Tags | Description
**Backward Compatibility**: All Basic Level commands continue to work unchanged when no new options are provided

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Strict Spec-Driven Development**: Every line of code must originate from approved specifications, plans, and tasks - [PASS] - Following Spec-Kit Plus workflow: constitution → specify → plan → tasks → implement
- **Code Quality Excellence**: Code must be PEP8 compliant, fully type-annotated, modular, and readable - [PASS] - Implementation will follow PEP8 standards with type hints where necessary
- **Simplicity & Robustness**: Focus on core functionality with excellent error handling and user feedback - [PASS] - Implementation will focus on Intermediate Level features with comprehensive error handling
- **Superior CLI Experience**: Design intuitive commands with clear prompts and formatted output - [PASS] - Implementation will provide enhanced table output and intuitive command interface with flag-based options
- **Zero External Dependencies**: Use only Python standard library - no third-party packages whatsoever - [PASS] - Implementation will use only Python standard library
- **Forward-Compatible Architecture**: Design with future evolution in mind - [PASS] - Implementation will maintain backward compatibility while extending functionality for future Advanced Level features

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-intermediate-org/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── __init__.py
├── main.py           # entry point and REPL loop
├── models.py         # Task dataclass (extended with priority and tags)
├── todo_manager.py   # core CRUD logic (enhanced with search/filter/sort)
├── cli.py            # command parsing and UI helpers (enhanced with flag support)
└── utils.py          # formatting and utility functions (new for enhanced display)

tests/
└── unit/
```

**Structure Decision**: Single project CLI application extending the existing modular architecture with separation of concerns. The structure includes:
- models.py: Extended Task dataclass with priority and tags fields
- todo_manager.py: Enhanced with search, filter, and sort functionality
- cli.py: Enhanced command parsing and display formatting with flag support
- utils.py: New module for formatting utilities for enhanced table display
- main.py: Maintains existing REPL loop and command dispatcher

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No constitution check violations identified. All requirements can be implemented within the specified constraints.

## Phase Completion Status

### Phase 0: Outline & Research
- **Status**: Complete
- **Artifacts**: research.md
- **Summary**: Resolved all technical decisions including task model extension, search implementation, filter logic, sort implementation, CLI enhancement, and display format

### Phase 1: Design & Contracts
- **Status**: Complete
- **Artifacts**: data-model.md, quickstart.md, contracts/api-contracts.md
- **Summary**: Defined Task, TodoManager, TaskFilter, and TaskSorter entities with fields, validation rules, and operations; created API contracts; documented quickstart guide

### Phase 2: Task Generation
- **Status**: Pending
- **Next Step**: Run `/sp.tasks` to generate implementation tasks from this plan

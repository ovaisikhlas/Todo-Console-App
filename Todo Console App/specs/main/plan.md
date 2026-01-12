# Implementation Plan: [FEATURE]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

[Extract from feature spec: primary requirement + technical approach from research]

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python 3.13+
**Primary Dependencies**: UV only (no third-party libraries - standard library exclusively)
**Storage**: In-memory only (no file I/O or persistence mechanisms)
**Testing**: Unit tests using standard library (unittest or pytest if allowed by constitution)
**Target Platform**: Console/Command-line interface
**Project Type**: Single project CLI application
**Performance Goals**: Fast response times for CLI commands (sub-second execution)
**Constraints**: In-memory storage, no file I/O, console interaction only
**Scale/Scope**: Individual user task management (single-user, local application)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Strict Spec-Driven Development**: Every line of code must originate from approved specifications, plans, and tasks
- **Code Quality Excellence**: Code must be PEP8 compliant, fully type-annotated, modular, and readable
- **Simplicity & Robustness**: Focus on core functionality with excellent error handling and user feedback
- **Superior CLI Experience**: Design intuitive commands with clear prompts and formatted output
- **Zero External Dependencies**: Use only Python standard library - no third-party packages whatsoever
- **In-Memory Storage**: Store tasks in memory only - no files, JSON, or database persistence mechanisms

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
# [REMOVE IF UNUSED] Option 1: Single project (DEFAULT)
src/
├── __init__.py
├── main.py           # entry point and REPL loop
├── models.py         # Task dataclass
├── todo_manager.py   # core CRUD logic
└── cli.py            # command parsing and UI helpers

tests/
└── unit/

# [REMOVE IF UNUSED] Option 2: Web application (when "frontend" + "backend" detected)
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/

# [REMOVE IF UNUSED] Option 3: Mobile + API (when "iOS/Android" detected)
api/
└── [same as backend above]

ios/ or android/
└── [platform-specific structure: feature modules, UI flows, platform tests]
```

**Structure Decision**: [Document the selected structure and reference the real
directories captured above]

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |

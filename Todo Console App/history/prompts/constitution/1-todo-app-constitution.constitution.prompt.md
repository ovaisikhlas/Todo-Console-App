---
id: 1
title: Todo App Constitution
stage: constitution
date: 2025-12-28
surface: agent
model: Qwen
feature: todo-app
branch: main
user: ovais
command: /sp.constitution
labels: [constitution, todo, python]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
 - .specify/templates/spec-template.md
 - .specify/templates/tasks-template.md
tests:
 - null
---

## Prompt

```
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are updating the project constitution at `.specify/memory/constitution.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

Follow this execution flow:

1. Load the existing constitution template at `.specify/memory/constitution.md`.
   - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
   **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

2. Collect/derive values for placeholders:
   - If user input (conversation) supplies a value, use it.
   - Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
   - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
   - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
     - MAJOR: Backward incompatible governance/principle removals or redefinitions.
     - MINOR: New principle/section added or materially expanded guidance.
     - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
   - If version bump type ambiguous, propose reasoning before finalizing.

3. Draft the updated constitution content:
   - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
   - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
   - Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
   - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

4. Consistency propagation checklist (convert prior checklist into active validations):
   - Read `.specify/templates/plan-template.md` and ensure any "Constitution Check" or rules align with updated principles.
   - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
   - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
   - Read each command file in `.specify/templates/commands/*.md` (including this one) to verify no outdated references (agent-specific names like CLAUDE only) remain when generic guidance is required.
   - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

5. Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
   - Version change: old → new
   - List of modified principles (old title → new title if renamed)
   - Added sections
   - Removed sections
   - Templates requiring updates (✅ updated / ⚠ pending) with file paths
   - Follow-up TODOs if any placeholders intentionally deferred.

6. Validation before final output:
   - No remaining unexplained bracket tokens.
   - Version line matches report.
   - Dates ISO format YYYY-MM-DD.
   - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

7. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

8. Output a final summary to the user with:
   - New version and bump rationale.
   - Any files flagged for manual follow-up.
   - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

Formatting & Style Requirements:

- Use Markdown headings exactly as in the template (do not demote/promote levels).
- Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
- Keep a single blank line between sections.
- Avoid trailing whitespace.

If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.


/sp.constitution /sp.constitution In-Memory Console Todo App – Phase I (Basic Level)

Project: Build a fully functional command-line Todo application that stores tasks in memory, developed strictly through Spec-Kit Plus agentic workflow using Qwen.

Core principles:
- 100% spec-driven: No manual coding; all code generated from approved specs, plans, and tasks
- Clean, professional Python: PEP8 compliant, fully type-annotated, modular, readable
- Simplicity and reliability: Minimal viable product with robust error handling
- Excellent CLI user experience: Clear prompts, helpful feedback, intuitive commands

Key standards:
- Python 3.13+
- Dependency manager: UV only
- Zero external dependencies – standard library exclusively
- Task model: dataclass with fields -> id (int, auto-increment), title (str), description (str), completed (bool default False)
- Storage: Single in-memory list of Task objects
- CLI: Interactive REPL loop with command-based interface
- Required commands:
  - add          → interactively create new task
  - list         → display all tasks with formatted table
  - update <id>  → modify title/description of existing task
  - delete <id>  → remove task by ID
  - complete <id> → toggle completion status
  - help         → show available commands
  - quit/exit    → exit application
- Display: Table with columns ID, Status ([x]/[ ]), Title, Description (truncated)

Project structure:
- constitution.md
- /specs_history/ (all .specify, .plan, .task files preserved)
- /src/
  ├── __init__.py
  ├── main.py           # entry point and REPL loop
  ├── models.py         # Task dataclass
  ├── todo_manager.py   # core CRUD logic
  └── cli.py            # command parsing and UI helpers

Constraints:
- In-memory only – no persistence, no file I/O
- No third-party libraries
- Console interaction only
- Development process strictly follows Spec-Kit Plus flow: constitution → specify → plan → tasks → implement → review

Success criteria:
- Application launches with `uv run python -m src.main`
- All 5 core features (Add, Delete, Update, View/List, Mark Complete) work flawlessly
- Tasks assigned unique sequential IDs
- Invalid inputs (wrong ID, empty title, bad command) handled gracefully with clear messages
- Clean, modular, type-annotated codebase
- README.md includes UV setup instructions and example usage session
- All specification artifacts preserved in /specs_history/

This constitution governs the entire Phase I development./sp.constitution In-Memory Console Todo App – Phase I (Basic Level)

Project: Build a fully functional command-line Todo application that stores tasks in memory, developed strictly through Spec-Kit Plus agentic workflow using Qwen.

Core principles:
- 100% spec-driven: No manual coding; all code generated from approved specs, plans, and tasks
- Clean, professional Python: PEP8 compliant, fully type-annotated, modular, readable
- Simplicity and reliability: Minimal viable product with robust error handling
- Excellent CLI user experience: Clear prompts, helpful feedback, intuitive commands

Key standards:
- Python 3.13+
- Dependency manager: UV only
- Zero external dependencies – standard library exclusively
- Task model: dataclass with fields -> id (int, auto-increment), title (str), description (str), completed (bool default False)
- Storage: Single in-memory list of Task objects
- CLI: Interactive REPL loop with command-based interface
- Required commands:
  - add          → interactively create new task
  - list         → display all tasks with formatted table
  - update <id>  → modify title/description of existing task
  - delete <id>  → remove task by ID
  - complete <id> → toggle completion status
  - help         → show available commands
  - quit/exit    → exit application
- Display: Table with columns ID, Status ([x]/[ ]), Title, Description (truncated)

Project structure:
- constitution.md
- /specs_history/ (all .specify, .plan, .task files preserved)
- /src/
  ├── __init__.py
  ├── main.py           # entry point and REPL loop
  ├── models.py         # Task dataclass
  ├── todo_manager.py   # core CRUD logic
  └── cli.py            # command parsing and UI helpers

Constraints:
- In-memory only – no persistence, no file I/O
- No third-party libraries
- Console interaction only
- Development process strictly follows Spec-Kit Plus flow: constitution → specify → plan → tasks → implement → review

Success criteria:
- Application launches with `uv run python -m src.main`
- All 5 core features (Add, Delete, Update, View/List, Mark Complete) work flawlessly
- Tasks assigned unique sequential IDs
- Invalid inputs (wrong ID, empty title, bad command) handled gracefully with clear messages
- Clean, modular, type-annotated codebase
- README.md includes UV setup instructions and example usage session
- All specification artifacts preserved in /specs_history/

This constitution governs the entire Phase I development.

## Response snapshot

I've successfully updated the project constitution and aligned the dependent templates. Here's what was accomplished:

1. Created a new constitution file at `.specify/memory/constitution.md` with:
   - Version 1.0.0
   - Six core principles aligned with your requirements
   - Key standards, project structure, constraints, and success criteria
   - Governance section with amendment procedures

2. Updated the following templates to align with the new constitution:
   - `.specify/templates/plan-template.md`: Updated constitution check, technical context, and project structure
   - `.specify/templates/spec-template.md`: Updated functional requirements, key entities, and success criteria
   - `.specify/templates/tasks-template.md`: Updated implementation tasks to match the Todo app requirements

The constitution now properly reflects the In-Memory Console Todo App project with its specific requirements for spec-driven development, Python standards, simplicity, CLI UX, zero dependencies, and in-memory storage.

## Outcome

- ✅ Impact: Updated constitution and aligned templates to match Todo app requirements
- 🧪 Tests: No tests required for this configuration task
- 📁 Files: Updated .specify/memory/constitution.md, .specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md
- 🔁 Next prompts: Ready to proceed with feature specification using /sp.specify
- 🧠 Reflection: The constitution now properly governs the Todo app development with all required principles and constraints

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All updates completed successfully
- Prompt variant (if applicable): Standard constitution update
- Next experiment (smallest change to try): Begin feature specification with /sp.specify
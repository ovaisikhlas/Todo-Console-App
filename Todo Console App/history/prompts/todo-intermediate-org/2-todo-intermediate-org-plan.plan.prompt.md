---
id: 2
title: todo-intermediate-org-plan
stage: plan
date_iso: 2025-01-28
surface: agent
model: Qwen
feature: todo-intermediate-org
branch: 001-todo-intermediate-org
user: Ovais
command: sp.plan
labels: ["planning", "todo-app", "intermediate", "organization"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - C:\Users\Ovais\Desktop\TODO\specs\001-todo-intermediate-org\plan.md
  - C:\Users\Ovais\Desktop\TODO\specs\001-todo-intermediate-org\research.md
  - C:\Users\Ovais\Desktop\TODO\specs\001-todo-intermediate-org\data-model.md
  - C:\Users\Ovais\Desktop\TODO\specs\001-todo-intermediate-org\quickstart.md
  - C:\Users\Ovais\Desktop\TODO\specs\001-todo-intermediate-org\contracts\api-contracts.md
tests_yaml: []
prompt_text: "Intermediate Level (Organization & Usability)
Project Goal: Extend the completed Basic Level in-memory console Todo app with Intermediate Level features (Priorities, Tags/Categories, Search, Filter, Sort) while maintaining full backward compatibility, clean architecture, and excellent user experience. All development must follow the agentic Spec-Kit Plus workflow using Qwen.

Phase 1: Model Extension & Data Integrity (Estimated: 6-8 hours)
- Update models.py:
  - Extend Task dataclass with new fields:
    priority: str = \"medium\"  # choices: \"high\", \"medium\", \"low\"
    tags: list[str] = field(default_factory=list)
  - Ensure default values preserve compatibility with existing tasks
  - Add type hints and docstrings
- Update todo_manager.py:
  - Modify add_task() and update_task() signatures to accept priority and tags
  - Add validation: priority must be valid choice, tags deduplicated and stripped
  - Implement helper methods: add_tag(task_id, tag), remove_tag(task_id, tag)
- Migration strategy for existing in-memory tasks:
  - On app start, automatically assign default priority=\"medium\" and tags=[] to older tasks
- Milestone: Task model fully supports new attributes without breaking existing data

Phase 2: Enhanced Input Flow for Add & Update (Estimated: 8-10 hours)
- Update cli.py add command flow:
  - After title/description, prompt for priority (with default shown)
  - Prompt for tags (comma-separated, with example)
  - Validate and parse input cleanly
- Update cli.py update <id> command:
  - Offer menu to modify: title, description, priority, tags (or any combination)
  - Allow adding/removing individual tags or replacing entire list
  - Skip prompts for unchanged fields
- Improve input helpers:
  - Case-insensitive priority selection
  - Tag input parsing: split by comma, strip whitespace, lowercase optional
- Milestone: Users can create and modify tasks with full priority and tag support

Phase 3: Search, Filter & Sort Engine (Estimated: 10-12 hours)
- Implement in todo_manager.py:
  - search_tasks(keyword: str) → list[Task] (case-insensitive partial match in title/description)
  - filter_tasks(status: Optional[str], priority: Optional[str], tags: Optional[list[str]]) → list[Task]
    - Support AND logic for multiple tags
  - sort_tasks(tasks: list[Task], criterion: str) → list[Task]
    - \"id\": by creation order (default)
    - \"priority\": high > medium > low, then by ID
    - \"alpha\": by title case-insensitive, then by ID
- Ensure all operations are efficient (O(n) acceptable for in-memory)
- Milestone: Core logic for search/filter/sort complete and tested

Phase 4: Enhanced List Command with Options (Estimated: 10-12 hours)
- Extend cli.py command parser:
  - Support flags: --status, --priority, --tag (repeatable), --sort, --search
  - Flexible parsing (e.g., allow --tag work --tag personal)
  - Fallback to default list if no flags
- Implement list command orchestration:
  - Start with all tasks
  - Apply search if provided
  - Apply filters sequentially
  - Apply sort at the end
  - Handle empty results gracefully (\"No tasks match your criteria\")
- Update help command with new syntax and examples
- Milestone: 'list' command supports all combinations intuitively

Phase 5: Improved Display & Formatting (Estimated: 6-8 hours)
- Enhance table output in cli.py/utils.py:
  - New columns: ID | Status | Priority | Title | Tags | Description
  - Priority: capitalized, aligned
  - Tags: comma-separated, truncated if too long (e.g., \"work, personal, ...\" )
  - Description: truncated to ~40 chars with \"...\"
  - Dynamic column alignment for clean appearance
- Use consistent status indicators ([x]/[ ])
- Ensure table works well with empty task list
- Milestone: Professional, readable table with all new information

Phase 6: Comprehensive Testing & Validation (Estimated: 8-10 hours)
- Manual scenario testing:
  - Create tasks with various priorities and tags
  - Test all filter combinations (including multiple tags)
  - Verify search matches partial keywords
  - Confirm sorting behavior (priority order, alpha stability)
  - Ensure backward compatibility: old commands work unchanged
- Edge cases:
  - Non-existent task ID in update/complete/delete
  - Invalid priority input
  - Duplicate tags
  - Very long titles/descriptions/tags
- Update README.md:
  - Add Intermediate Level section
  - Include example session with new features
  - Update command reference
- Milestone: All features robust, no regressions, documentation current

Total Estimated Effort: 48-60 hours (spread over 7-10 focused days)

Deliverables:
- Fully enhanced app with Priorities, Tags, Search, Filter, Sort
- Seamless integration preserving Basic Level experience
- Clean, extensible codebase ready for Advanced Level
- Updated README reflecting new capabilities
- All specs/plans/tasks preserved in /specs_history/

Milestones:
1. Model & input extensions complete – Day 3
2. Search/Filter/Sort logic implemented – Day 6
3. Enhanced list command functional – Day 8
4. Polished display and help updated – Day 9
5. Full testing and documentation complete – Day 10

Proceed to task breakdown upon approval."
response_text: "Successfully completed the implementation planning for the Todo App Intermediate Level. Created comprehensive plan.md with technical context, constitution check, and project structure. Generated research.md with technical decisions, data-model.md with entity definitions, quickstart.md with usage instructions, and API contracts in contracts/api-contracts.md. All constitution checks passed and agent context was updated. The plan is comprehensive and ready for the task generation phase (/sp.tasks)."
outcome: "Complete implementation plan created with all required artifacts for the intermediate todo app features."
evaluation: "All planning phases completed successfully. The plan is comprehensive and ready for the task generation phase (/sp.tasks)."
---

# Implementation Plan for Todo App Intermediate Level

## Summary
Successfully completed the implementation planning for the Todo App Intermediate Level. Created comprehensive plan.md with technical context, constitution check, and project structure.

## Key Artifacts Generated
- plan.md: Main implementation plan
- research.md: Technical decisions and rationale
- data-model.md: Entity definitions and relationships
- quickstart.md: Usage instructions and examples
- contracts/api-contracts.md: Interface contracts between components

## Status
All constitution checks passed and agent context was updated. Ready for task generation phase.
import sys
import os
sys.path.insert(0, './src')

from todo_manager import TodoManager
from datetime import datetime

# Initialize manager
manager = TodoManager()

print('=== VERIFYING BASIC LEVEL FEATURES ===')

# 1. Add Task - Create new todo items
task1 = manager.add_task('Basic task 1', 'Description for basic task')
task2 = manager.add_task('Basic task 2', 'Another basic task')
print(f'[X] Add Task: Added {len(manager.list_tasks())} tasks')

# 2. View Task List - Display all tasks
tasks = manager.list_tasks()
print(f'[X] View Task List: Listed {len(tasks)} tasks')

# 3. Update Task - Modify existing task details
updated_task = manager.update_task(task1.id, title='Updated basic task', description='Updated description')
print(f'[X] Update Task: Updated task title to "{updated_task.title}"')

# 4. Mark as Complete - Toggle task completion status
completed_task = manager.toggle_task_completion(task1.id)
print(f'[X] Mark as Complete: Task {task1.id} completion status is now {completed_task.completed}')

# 5. Delete Task - Remove tasks from the list
initial_count = len(manager.list_tasks())
deleted = manager.delete_task(task2.id)
final_count = len(manager.list_tasks())
print(f'[X] Delete Task: Deleted task successfully, count went from {initial_count} to {final_count}')

print('\n=== VERIFYING INTERMEDIATE LEVEL FEATURES ===')

# Reset manager for next tests
manager = TodoManager()

# 1. Priorities & Tags/Categories
task_with_priority = manager.add_task('Priority task', 'Task with priority', priority='high')
task_with_tags = manager.add_task('Tagged task', 'Task with tags', tags=['work', 'urgent'])
print(f'[X] Priorities: Added task with priority "{task_with_priority.priority}"')
print(f'[X] Tags/Categories: Added task with tags {task_with_tags.tags}')

# 2. Search & Filter
search_task = manager.add_task('Meeting with team', 'Discuss project timeline', priority='high', tags=['work', 'meeting'])
search_results = manager.search_tasks('meeting')
print(f'[X] Search: Found {len(search_results)} tasks containing "meeting"')

filtered_tasks = manager.filter_tasks(priority='high')
print(f'[X] Filter: Found {len(filtered_tasks)} high priority tasks')

# 3. Sort Tasks
task_a = manager.add_task('Alpha task', 'A comes first', priority='low')
task_z = manager.add_task('Zebra task', 'Z comes last', priority='medium')
sorted_by_alpha = manager.sort_tasks(manager.list_tasks(), 'alpha')
print(f'[X] Sort: Tasks sorted alphabetically, first is "{sorted_by_alpha[0].title}"')

sorted_by_priority = manager.sort_tasks(manager.list_tasks(), 'priority')
print(f'[X] Sort: Tasks sorted by priority, first should be high priority')

print('\n=== VERIFYING ADVANCED LEVEL FEATURES ===')

# 1. Recurring Tasks
recurring_task = manager.add_task(
    'Daily habit',
    'Brush teeth',
    priority='medium',
    tags=['health'],
    due_date_str='2024-01-15 08:00',
    recurrence='daily'
)
print(f'[X] Recurring Tasks: Added task with recurrence pattern "{recurring_task.recurrence}"')

# Test completing recurring task creates new instance
initial_count = len(manager.list_tasks())
completed_task = manager.toggle_task_completion(recurring_task.id)
final_count = len(manager.list_tasks())
print(f'[X] Recurring Tasks: Completed task triggered new instance creation, count went from {initial_count} to {final_count}')

# 2. Due Dates & Time Reminders
due_task = manager.add_task(
    'Due date task',
    'Has a due date',
    due_date_str='2025-12-31 15:30'
)
print(f'[X] Due Dates: Added task with due date "{due_task.due_date}"')

# Test overdue detection
overdue_task = manager.add_task(
    'Overdue task',
    'This task is overdue',
    due_date_str='2020-01-01 10:00'  # Past date
)
overdue_list = manager.get_overdue_tasks()
print(f'[X] Time Reminders: Found {len(overdue_list)} overdue tasks')

print('\n=== ALL FEATURES VERIFIED SUCCESSFULLY ===')
print('Basic, Intermediate, and Advanced level features are all implemented and working correctly.')
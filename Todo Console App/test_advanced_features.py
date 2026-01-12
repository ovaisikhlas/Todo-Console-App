from src.todo_manager import TodoManager
from datetime import datetime, timedelta

# Test recurring task functionality
print("Testing recurring task functionality...")
manager = TodoManager()

# Add a recurring task
due_date = datetime(2024, 1, 15, 10, 0)
recurring_task = manager.add_task(
    title="Daily recurring task",
    description="This task repeats daily",
    priority="medium",
    tags=["daily"],
    due_date_str=due_date,
    recurrence="daily"
)

print(f"Created recurring task: ID={recurring_task.id}, Title={recurring_task.title}, Due date={recurring_task.due_date}, Recurrence={recurring_task.recurrence}")

# Complete the task to trigger recurrence
initial_count = len(manager.list_tasks())
print(f"Initial task count: {initial_count}")

completed_task = manager.toggle_task_completion(recurring_task.id)
print(f"Completed task: ID={completed_task.id}, Completed status: {completed_task.completed}")

# Check if a new instance was created
final_count = len(manager.list_tasks())
print(f"Final task count: {final_count}")

if final_count > initial_count:
    print("SUCCESS: New recurring instance was created")
    all_tasks = manager.list_tasks()
    for task in all_tasks:
        if task.id != recurring_task.id and task.title == "Daily recurring task":
            print(f"New instance: ID={task.id}, Due date={task.due_date}, Completed={task.completed}")
else:
    print("FAILURE: No new recurring instance was created")

# Test overdue functionality
print("\nTesting overdue functionality...")
past_due = datetime.now() - timedelta(days=1)
overdue_task = manager.add_task(
    title="Overdue task",
    description="This task is overdue",
    priority="high",
    tags=["urgent"],
    due_date_str=past_due,
    recurrence="none"
)

overdue_tasks = manager.get_overdue_tasks()
print(f"Overdue tasks count: {len(overdue_tasks)}")
for task in overdue_tasks:
    print(f"Overdue task: ID={task.id}, Title={task.title}, Due date={task.due_date}")

print("\nAll tests completed successfully!")
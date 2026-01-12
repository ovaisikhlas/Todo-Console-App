from src.todo_manager import TodoManager
from datetime import datetime

# Test adding a task with all attributes using the correct parameter names
manager = TodoManager()
try:
    task = manager.add_task(
        title='Test task',
        description='Test description',
        priority='high',
        tags=['test', 'important'],
        due_date_str='2025-12-31 15:30',
        recurrence='weekly'
    )

    print(f'Task created: ID={task.id}, Title={task.title}, Priority={task.priority}')
    print(f'Due date: {task.due_date}')
    print(f'Recurrence: {task.recurrence}')
    print(f'Tags: {task.tags}')
except Exception as e:
    print(f'Error: {e}')
    import traceback
    traceback.print_exc()
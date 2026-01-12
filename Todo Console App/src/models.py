from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class Task:
    """
    Represents a todo item with id, title, description, completion status, priority, tags, due date, and recurrence pattern.
    """
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    priority: str = "medium"  # Choices: "high", "medium", "low"
    tags: list[str] = field(default_factory=list)
    due_date: Optional[datetime] = None  # Optional due date/time for the task
    recurrence: str = "none"  # Recurrence pattern: "none", "daily", "weekly", "monthly"
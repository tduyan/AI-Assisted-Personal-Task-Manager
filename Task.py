import uuid
from datetime import datetime
from typing import Optional

class Task:
    def __init__(self, title: str, description: Optional[str] = None, due_date: Optional[str] = None,
                 reminder_at: Optional[str] = None, priority: Optional[str] = None, list_id: str = "default_list"):
        if not title.strip():
            raise ValueError("Task title cannot be empty or whitespace-only.")
        if len(title) > 200:
            raise ValueError("Task title cannot exceed 200 characters.")
        if description and len(description) > 1000:
            raise ValueError("Task description cannot exceed 1000 characters.")
        if priority and priority not in ["low", "medium", "high"]:
            raise ValueError("Priority must be 'low', 'medium', 'high', or None.")

        now = datetime.utcnow().isoformat() + "Z"
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description or ""
        self.status = "incomplete"
        self.created_at = now
        self.updated_at = now
        self.completed_at = None
        self.due_date = due_date
        self.reminder_at = reminder_at
        self.priority = priority
        self.list_id = list_id
        self.recurrence_rule = None
        self.parent_task_id = None
        self.sort_order = None
        self.deleted_at = None

    def mark_complete(self):
        """Mark the task as complete."""
        self.status = "complete" # Update the status to "complete"
        self.completed_at = datetime.utcnow().isoformat() + "Z" # Set the completed_at timestamp 
        self.updated_at = self.completed_at # Update the updated_at timestamp to the current time

    def mark_incomplete(self):
        """Mark the task as incomplete."""
        self.status = "incomplete"
        self.completed_at = None
        self.updated_at = datetime.utcnow().isoformat() + "Z"

    def to_dict(self):
        """Convert the task to a dictionary for JSON serialization."""
        return self.__dict__

    @staticmethod
    def from_dict(data: dict):
        """Create a Task object from a dictionary."""
        task = Task(
            title=data["title"],
            description=data.get("description"),
            due_date=data.get("due_date"),
            reminder_at=data.get("reminder_at"),
            priority=data.get("priority"),
            list_id=data.get("list_id", "default_list")
        )
        task.id = data["id"]
        task.status = data["status"]
        task.created_at = data["created_at"]
        task.updated_at = data["updated_at"]
        task.completed_at = data.get("completed_at")
        task.recurrence_rule = data.get("recurrence_rule")
        task.parent_task_id = data.get("parent_task_id")
        task.sort_order = data.get("sort_order")
        task.deleted_at = data.get("deleted_at")
        return task
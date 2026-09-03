import json
import uuid
from datetime import datetime
from typing import List, Dict, Optional

class TaskManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.tasks: List[Dict] = []

    def load_tasks(self) -> None:
        """Load tasks from the JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            print(f"No existing file found at {self.file_path}. Starting with an empty task list.")
            self.tasks = []
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with an empty task list.")
            self.tasks = []

    def save_tasks(self) -> None:
        """Save tasks to the JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file, indent=4, default=str)

    def create_task(self, title: str, description: Optional[str] = None, due_date: Optional[str] = None,
                    reminder_at: Optional[str] = None, priority: Optional[str] = None, list_id: str = "default_list") -> Dict:
        """Create a new task and return it."""
        if not title.strip():
            raise ValueError("Task title cannot be empty or whitespace-only.")
        if len(title) > 200:
            raise ValueError("Task title cannot exceed 200 characters.")
        if description and len(description) > 1000:
            raise ValueError("Task description cannot exceed 1000 characters.")
        if priority and priority not in ["low", "medium", "high"]:
            raise ValueError("Priority must be 'low', 'medium', 'high', or None.")

        now = datetime.utcnow().isoformat() + "Z"  # ISO 8601 format with UTC timezone
        task = {
            "id": str(uuid.uuid4()),  # Generate a unique UUID
            "title": title,
            "description": description or "",
            "status": "incomplete",
            "created_at": now,
            "updated_at": now,
            "completed_at": None,
            "due_date": due_date,
            "reminder_at": reminder_at,
            "priority": priority,
            "list_id": list_id,
            "recurrence_rule": None,
            "parent_task_id": None,
            "sort_order": None,
            "deleted_at": None
        }
        self.add_task(task)
        return task

    def add_task(self, task: Dict) -> None:
        """Add a new task to the list."""
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_id: str) -> bool:
        """Remove a task by its ID."""
        for i, task in enumerate(self.tasks):
            if task.get("id") == task_id:
                del self.tasks[i]
                self.save_tasks()
                return True
        return False

    def list_tasks(self) -> List[Dict]:
        """Return the list of tasks."""
        return self.tasks
    
if __name__ == "__main__":
    # Initialize TaskManager with the path to the tasks.json file
    manager = TaskManager("tasks.json")

    # Load existing tasks from the file
    manager.load_tasks()

    # Prompt the user to add a new task
    print("Welcome to Task Manager!")
    try:
        title = input("Enter task title: ").strip()
        description = input("Enter task description (optional): ").strip() or None
        due_date = input("Enter due date (optional, format: YYYY-MM-DDTHH:MM:SSZ): ").strip() or None
        reminder_at = input("Enter reminder date (optional, format: YYYY-MM-DDTHH:MM:SSZ): ").strip() or None
        priority = input("Enter priority (optional, choose from 'low', 'medium', 'high'): ").strip() or None
        list_id = input("Enter list ID (optional, default is 'default_list'): ").strip() or "default_list"

        # Create and save the new task
        new_task = manager.create_task(
            title=title,
            description=description,
            due_date=due_date,
            reminder_at=reminder_at,
            priority=priority,
            list_id=list_id
        )
        print("Task created successfully:", new_task)

    except ValueError as e:
        print("Error:", e)

    # Display all tasks
    print("\nAll tasks:")
    for task in manager.list_tasks():
        print(task)


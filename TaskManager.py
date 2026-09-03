import json
from typing import List
from Task import Task

class TaskManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.tasks: List[Task] = []

    def load_tasks(self):
        """Load tasks from the JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                task_data = json.load(file)
                self.tasks = [Task.from_dict(task) for task in task_data]
        except FileNotFoundError:
            print(f"No existing file found at {self.file_path}. Starting with an empty task list.")
            self.tasks = []
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with an empty task list.")
            self.tasks = []

    def save_tasks(self):
        """Save tasks to the JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, task: Task):
        """Add a new task to the list."""
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_id: str) -> bool:
        """Remove a task by its ID."""
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                self.save_tasks()
                return True
        return False

    def list_tasks(self) -> List[Task]:
        """Return the list of tasks."""
        return self.tasks
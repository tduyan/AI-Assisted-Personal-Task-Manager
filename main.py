import sys
from task_manager import TaskManager  # Assuming TaskManager is in task_manager.py

class TaskCLI:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def display_menu(self):
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

    def add_task(self):
        """Prompt the user to add a new task."""
        try:
            title = input("Enter task title: ").strip()
            description = input("Enter task description (optional): ").strip() or None
            due_date = input("Enter due date (optional, format: YYYY-MM-DDTHH:MM:SSZ): ").strip() or None
            reminder_at = input("Enter reminder date (optional, format: YYYY-MM-DDTHH:MM:SSZ): ").strip() or None
            priority = input("Enter priority (optional, choose from 'low', 'medium', 'high'): ").strip() or None
            list_id = input("Enter list ID (optional, default is 'default_list'): ").strip() or "default_list"

            # Create and save the new task
            new_task = self.task_manager.create_task(
                title=title,
                description=description,
                due_date=due_date,
                reminder_at=reminder_at,
                priority=priority,
                list_id=list_id
            )
            print("Task added successfully:", new_task)
        except ValueError as e:
            print("Error:", e)

    def view_tasks(self):
        """Display all tasks."""
        tasks = self.task_manager.list_tasks()
        if not tasks:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for task in tasks:
                status = task["status"]
                print(f"{task['id']}: {task['title']} - {status}")

    def complete_task(self):
        """Mark a task as completed."""
        try:
            task_id = input("Enter task ID to mark as completed: ").strip()
            for task in self.task_manager.tasks:
                if task["id"] == task_id:
                    task["status"] = "complete"
                    task["completed_at"] = self.task_manager._get_current_timestamp()
                    self.task_manager.save_tasks()
                    print("Task marked as completed.")
                    return
            print("Task not found.")
        except Exception as e:
            print("Error:", e)

    def delete_task(self):
        """Delete a task by its ID."""
        try:
            task_id = input("Enter task ID to delete: ").strip()
            if self.task_manager.remove_task(task_id):
                print("Task deleted successfully.")
            else:
                print("Task not found.")
        except Exception as e:
            print("Error:", e)

    def run(self):
        """Run the CLI menu loop."""
        while True:
            self.display_menu()
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.complete_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                print("Exiting Task Manager. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Initialize TaskManager with the path to the tasks.json file
    manager = TaskManager("tasks.json")

    # Load existing tasks from the file
    manager.load_tasks()

    # Start the CLI
    cli = TaskCLI(manager)
    cli.run()
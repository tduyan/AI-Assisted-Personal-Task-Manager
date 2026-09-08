# AI-Assisted Personal Task Manager

A command-line task management application built with Python. This tool allows users to add, view, complete, and delete tasks, with all data stored in a JSON file for persistence.

---

## Features
- Add tasks with optional details like description, due date, priority, and reminders.
- View all tasks with their current status.
- Mark tasks as complete.
- Delete tasks by their unique ID.
- Save and load tasks from a JSON file for persistence.

---

## Setup Instructions

### Prerequisites
- Python 3.7 or higher installed on your system.
- `pip` (Python package manager) installed.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AI-Assisted-Personal-Task-Manager.git
   cd AI-Assisted-Personal-Task-Manager
2. Create and activate a virtual environment (optional but recommended):
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows
3. Run the program:
    python main.py

---

## Supported Commands

**Main Menu**
1. Add Task: Add a new task with optional details like description, due date, priority, and reminders.
2. View Tasks: Display all tasks with their current status.
3. Complete Task: Mark a task as complete by entering its unique ID.
4. Delete Task: Delete a task by entering its unique ID.
5. Exit: Exit the program.

--- 

## Example Usage

**Adding a Task** 
Task Manager
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit
Enter your choice: 1
Enter task title: Write project documentation
Enter task description (optional): Complete the README and API docs for the project.
Enter due date (optional, format: YYYY-MM-DDTHH:MM:SSZ): 2023-10-15T12:00:00Z
Enter reminder date (optional, format: YYYY-MM-DDTHH:MM:SSZ): 2023-10-14T12:00:00Z
Enter priority (optional, choose from 'low', 'medium', 'high'): high
Enter list ID (optional, default is 'default_list'): work
Task added successfully.

**Viewing Tasks**
Task Manager
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit
Enter your choice: 2

Tasks:
123e4567-e89b-12d3-a456-426614174000: Write project documentation - incomplete

**Completing a Task**
Task Manager
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit
Enter your choice: 3
Enter task ID to mark as completed: 123e4567-e89b-12d3-a456-426614174000
Task 'Write project documentation' marked as completed.

**Deleting a Task**
Task Manager
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit
Enter your choice: 4
Enter task ID to delete: 123e4567-e89b-12d3-a456-426614174000
Task with ID '123e4567-e89b-12d3-a456-426614174000' has been deleted successfully.

---

## Future Improvements

1. Recurring Tasks:
- Add support for recurring tasks with customizable recurrence rules (e.g., daily, weekly, monthly).
2. Task Filtering and Sorting:
- Allow users to filter tasks by status, priority, or due date.
- Add sorting options for tasks (e.g., by due date, priority, or creation date).
3. Notifications:
- Implement reminders for tasks based on the reminder_at field.
4. Web Interface:
- Build a web-based interface for easier task management.
5. Sync Across Devices:
- Add support for syncing tasks across devices using a cloud-based backend.

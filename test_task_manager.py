import pytest
import os
import json
from TaskManager import TaskManager
from Task import Task

# Test file path for saving/loading tasks
TEST_FILE = "test_tasks.json"

@pytest.fixture
def task_manager():
    """Fixture to create a TaskManager instance with a test file."""
    manager = TaskManager(TEST_FILE)
    yield manager
    # Cleanup: Remove the test file after the test
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

# Verifies that a task can be added to the [TaskManager]
# Checks that the task's title matches the expected value
def test_add_task(task_manager):
    """Test adding a task."""
    task = Task(
        title="Test Task",
        description="This is a test task.",
        due_date="2023-10-15T12:00:00Z",
        reminder_at="2023-10-14T12:00:00Z",
        priority="high",
        list_id="test_list"
    )
    task_manager.add_task(task)
    assert len(task_manager.tasks) == 1
    assert task_manager.tasks[0].title == "Test Task"

# Adds multiple tasks and verifies that they are correctly listed by the [list_tasks] method
def test_view_tasks(task_manager):
    """Test viewing tasks."""
    task1 = Task(title="Task 1")
    task2 = Task(title="Task 2")
    task_manager.add_task(task1)
    task_manager.add_task(task2)
    tasks = task_manager.list_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"

# Adds a task, marks it as complete using the [mark_complete] method, 
# and verifies that the task's status is updated to "complete" and that the completion timestamp is set
def test_mark_complete(task_manager):
    """Test marking a task as complete."""
    task = Task(title="Incomplete Task")
    task_manager.add_task(task)
    task_id = task.id
    # Mark the task as complete
    for t in task_manager.tasks:
        if t.id == task_id:
            t.mark_complete()
    assert task_manager.tasks[0].status == "complete"
    assert task_manager.tasks[0].completed_at is not None

# Adds a task, deletes it using the [remove_task] method, 
# and verifies that the task is removed from the list of tasks  
def test_delete_task(task_manager):
    """Test deleting a task."""
    task = Task(title="Task to Delete")
    task_manager.add_task(task)
    task_id = task.id
    # Delete the task
    result = task_manager.remove_task(task_id)
    assert result is True
    assert len(task_manager.tasks) == 0

# Adds a task, saves the tasks to a file using the [save_tasks] method,
# and verifies that the file is created. 
# Then, it creates a new instance of [TaskManager], loads the tasks from the file using the [load_tasks] method, 
# and verifies that the loaded task matches the original task's title.
def test_save_and_load_tasks(task_manager):
    """Test saving and loading tasks."""
    task = Task(title="Task to Save")
    task_manager.add_task(task)
    # Save tasks to file
    task_manager.save_tasks()
    assert os.path.exists(TEST_FILE)

    # Create a new TaskManager instance and load tasks
    new_manager = TaskManager(TEST_FILE)
    new_manager.load_tasks()
    assert len(new_manager.tasks) == 1
    assert new_manager.tasks[0].title == "Task to Save"
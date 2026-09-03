# **Program Design Walk Through** 
Task Class:
Represents a single task.
Encapsulates task properties and methods for manipulating a task (e.g., mark as complete, update fields).

TaskManager Class:
Manages a collection of tasks.
Handles loading, saving, adding, deleting, and updating tasks.
Acts as the interface between the tasks and the storage (e.g., JSON file).

TaskCLI Class:
Provides a Command-Line Interface (CLI) for interacting with the TaskManager.
Handles user input and routes actions to the appropriate methods in TaskManager.

1. Encapsulation:
Task encapsulates all task-related data and methods.
TaskManager handles task storage and retrieval.
TaskCLI provides the user interface.

2. Separation of Concerns:
Each class has a single responsibility, making the code modular and easier to maintain.

3. Scalability:
You can extend the Task class with additional methods (e.g., archive).
The TaskManager can be extended to support advanced features like filtering or sorting tasks.
This OOP design ensures clean, maintainable, and scalable code.
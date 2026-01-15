from collections import defaultdict

class Task:
    def __init__(self, task_id, user_id, description, due_date, tags):
        self.task_id = task_id
        self.user_id = user_id
        self.description = description
        self.due_date = due_date
        self.tags = set(tags) # Set for O(1) tag lookups
        self.is_completed = False

class TodoList:
    def __init__(self):
        self.task_id_counter = 1
        # Maps taskId -> Task object for O(1) access
        self.tasks = {}
        # Maps userId -> list of Task objects for fast user retrieval
        self.user_tasks = defaultdict(list)

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: list[str]) -> int:
        task_id = self.task_id_counter
        new_task = Task(task_id, userId, taskDescription, dueDate, tags)
        
        # Store in both lookups
        self.tasks[task_id] = new_task
        self.user_tasks[userId].append(new_task)
        
        self.task_id_counter += 1
        return task_id

    def getAllTasks(self, userId: int) -> list[str]:
        # Filter for pending tasks and sort by dueDate
        pending = [t for t in self.user_tasks[userId] if not t.is_completed]
        # Sort by dueDate. Python's Timsort is stable and efficient.
        pending.sort(key=lambda x: x.due_date)
        return [t.description for t in pending]

    def getTasksForTag(self, userId: int, tag: str) -> list[str]:
        # Filter for pending tasks that contain the specific tag
        tagged_tasks = [
            t for t in self.user_tasks[userId] 
            if not t.is_completed and tag in t.tags
        ]
        tagged_tasks.sort(key=lambda x: x.due_date)
        return [t.description for t in tagged_tasks]

    def completeTask(self, userId: int, taskId: int) -> None:
        # O(1) lookup in the global task dictionary
        task = self.tasks.get(taskId)
        
        # Validation: exists, belongs to user, and is not already complete
        if task and task.user_id == userId and not task.is_completed:
            task.is_completed = True
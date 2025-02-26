from project.task import Task

class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        task = next((t for t in self.tasks if t.name == task_name), None)
        if task:
            task.completed = True
            return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        cleared_count = initial_count - len(self.tasks)
        return f"Cleared {cleared_count} tasks."

    def view_section(self):
        result = [f"Section {self.name}:"]
        for task in self.tasks:
            result.append(task.details())
        return '\n'.join(result)






